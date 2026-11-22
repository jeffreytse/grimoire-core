#!/usr/bin/env python3
"""Generate every agent's plugin manifest from the skills tree.

Skills live in one place only: skills/<domain>/<sub>/skills/<name>/SKILL.md.
Agents that scan a single skills/ level cannot find them on their own, so each
manifest lists the nested skills/ folders explicitly. This script regenerates
those lists (and the version from VERSION) so they never drift from the tree.

Also enforces the Agent Skills naming rule (Pi, Codex, Gemini, Kimi): a
skill's frontmatter name equals its folder name, is lowercase-hyphen, and is
at most 64 characters; and names are unique across the whole tree.

Usage:
  python3 scripts/gen-manifests.py          # write manifests
  python3 scripts/gen-manifests.py --check  # exit 1 if any manifest is stale
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skills"
NAME = "grimoire"
KEYWORDS = ["best-practices", "skills", "grimoire", "engineering", "medicine",
            "law", "finance", "claude-code", "codex", "copilot", "gemini-cli"]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter_name(skill_md):
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            return line[5:].strip().strip("\"'")
    return None


def find_skills():
    """Return {name: skill_dir} for every skills/**/skills/<name>/SKILL.md."""
    found = {}
    dupes = {}
    for skill_md in sorted(SRC.rglob("SKILL.md")):
        skill_dir = skill_md.parent
        if skill_dir.parent.name != "skills":
            continue  # not a skill dir (e.g. a fixture or nested doc)
        name = skill_dir.name
        if name in found:
            dupes.setdefault(name, [found[name]]).append(skill_dir)
            continue
        found[name] = skill_dir
    bad = []
    for name, d in sorted(found.items()):
        fm = frontmatter_name(d / "SKILL.md")
        if fm != name or not NAME_RE.match(name) or len(name) > 64:
            bad.append(f"  {d.relative_to(ROOT)}: frontmatter name={fm!r}")
    if bad:
        print("error: skill name must equal folder name, lowercase-hyphen, "
              "<= 64 chars:", file=sys.stderr)
        print("\n".join(bad), file=sys.stderr)
        sys.exit(1)
    if dupes:
        print("error: duplicate skill names:", file=sys.stderr)
        for name, dirs in sorted(dupes.items()):
            for d in dirs:
                print(f"  {name}: {d.relative_to(ROOT)}", file=sys.stderr)
        sys.exit(1)
    return found


def skill_dirs(skills):
    """Sorted ./-relative paths of every skills/ folder that holds a skill."""
    return sorted({"./" + d.parent.relative_to(ROOT).as_posix()
                   for d in skills.values()})


def manifests(skills):
    """Return {relative_path: json_data} for every generated manifest."""
    claude_path = ROOT / ".claude-plugin" / "plugin.json"
    meta = json.loads(claude_path.read_text())
    version = (ROOT / "VERSION").read_text().strip()
    dirs = skill_dirs(skills)
    desc = meta["description"]
    author = meta["author"]["name"]
    repo = meta["repository"]
    homepage = meta.get("homepage", repo)
    lic = meta.get("license", "MIT")

    pkg = json.loads((ROOT / "package.json").read_text())
    pkg["version"] = version
    pkg.setdefault("pi", {})["skills"] = dirs

    return {
        # Claude Code, Copilot, Codex, OMP, MiniMax (Claude reader).
        ".claude-plugin/plugin.json": {**meta, "version": version, "skills": dirs},
        ".codex-plugin/plugin.json": {
            "name": NAME,
            "version": version,
            "description": desc,
            "author": {"name": author},
            "homepage": homepage,
            "repository": repo,
            "license": lic,
            "keywords": KEYWORDS,
            "skills": dirs,
            "interface": {
                "displayName": "grimoire",
                "shortDescription": "Cited professional best practices for every field",
                "developerName": author,
                "category": "Productivity",
                "capabilities": ["Read"],
                "websiteURL": homepage,
            },
        },
        ".grok-plugin/plugin.json": {
            "name": NAME,
            "version": version,
            "description": desc,
            "skills": dirs,
        },
        # Muse requires every skill listed individually.
        ".muse-plugin/plugin.json": {
            "schemaVersion": 1,
            "name": NAME,
            "displayName": "grimoire",
            "version": version,
            "description": desc,
            "compat": {"source": "native", "manifestDir": ".muse-plugin"},
            "capabilities": {
                "skills": [
                    {"id": n,
                     "path": (d / "SKILL.md").relative_to(ROOT).as_posix(),
                     "enabledDefault": True}
                    for n, d in sorted(skills.items())
                ]
            },
        },
        "kimi.plugin.json": {
            "name": NAME,
            "version": version,
            "description": desc,
            "homepage": homepage,
            "license": lic,
            "skills": dirs,
        },
        # Pi package (pi.skills) and OpenCode entry point.
        "package.json": pkg,
    }


def dump(data):
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true",
                        help="verify manifests are up to date; do not write")
    args = parser.parse_args()

    skills = find_skills()
    wanted = {ROOT / p: dump(d) for p, d in manifests(skills).items()}

    if args.check:
        stale = [p for p, text in wanted.items()
                 if not p.exists() or p.read_text() != text]
        if stale:
            for p in stale:
                print(f"STALE — {p.relative_to(ROOT)}")
            print("run: make update-plugin-manifest")
            sys.exit(1)
        print(f"OK — {len(skills)} skills in {len(skill_dirs(skills))} folders, "
              f"{len(wanted)} manifests in sync")
        return

    for path, text in wanted.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    print(f"Wrote {len(wanted)} manifests: {len(skills)} skills in "
          f"{len(skill_dirs(skills))} folders")


if __name__ == "__main__":
    main()
