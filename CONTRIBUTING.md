# Contributing to grimoire-core

grimoire-core is the official, curated skills package for [grimoire](https://github.com/jeffreytse/grimoire). Every skill must meet the [Skill Standard](./STANDARD.md). The bar: would this skill make an AI agent perform like a domain expert? If not, it's not ready.

Writing skills for your own package instead? Those have no such requirement — see [docs/user-package.md](./docs/user-package.md).

By participating you agree to follow the [Code of Conduct](./CODE_OF_CONDUCT.md).

---

## Adding a Skill

The fastest path is to let the meta skills guide you. In an agent with grimoire installed, run `grimoire:write-best-practice-skill` (or `/write-best-practice-skill` in skills mode). It walks through every step below.

### 1. Check it qualifies and isn't a duplicate

- **Majority adoption** by top-tier companies or credentialed professionals — not one team's approach.
- **Measurable impact** — a number or a named study, not "helps" or "improves".
- **No genuine controversy** — if experts are split roughly 50/50, there is no best practice.
- **No duplicate** — search first (`grimoire:suggest-best-practice <topic>`, or `grep -ri "<topic>" skills/`). If an existing skill covers it, extend that skill instead.

### 2. Create the file

Skills live at `skills/<domain>/<subdomain>/skills/<skill-name>/SKILL.md` (`meta` is flat: `skills/meta/skills/<skill-name>/SKILL.md`). Start from [SKILL_TEMPLATE.md](./SKILL_TEMPLATE.md):

```
skills/engineering/development/skills/review-pull-request/SKILL.md
skills/health/fitness/skills/design-training-program/SKILL.md
skills/finance/investing/skills/calculate-dcf/SKILL.md
skills/law/contracts/skills/review-saas-contract/SKILL.md
```

The folder name must equal the frontmatter `name`.

### 3. Write it to the standard

- **Name:** `<verb>-<subject>[-<qualifier>]`, kebab-case, ≤50 characters, using an approved verb from [STANDARD.md](./STANDARD.md). Rejected verbs: `do-`, `handle-`, `manage-`, `improve-`, `get-`, `use-`, `help-`.
- **Frontmatter:** `name`, `description` (starts with "Use when" and describes *when* to use the skill, not what it does), `source`, `tags` (3–8).
- **`## Why This Is Best Practice`:** **Adopted by** (named companies or institutions), **Impact** (a number or named study), **Why best** (names an alternative and why this wins), and a **Sources** line.
- **Verify sources:** if you aren't sure a source is current or says what you claim, check it online. Don't rely on memory for numbers, dates, or adoption claims.
- **Steps:** concrete actions the reader can take right now, including what to do when something fails.
- **Size:** 50–300 lines. Under 50 is too shallow; over 300, split it.
- **Skills that load other skills** (meta workflows and routers) must work in both skills mode and MCP mode: include the [Skill Access](./STANDARD.md#skill-access-conditional) section, give install hints for every route, and keep practice pins in `grimoire.toml`.

### 4. Add the required safety footer

| Domain | Footer |
|--------|--------|
| Health / medicine | `> For personal health decisions, consult a qualified healthcare provider.` |
| Law | `> This is educational content, not legal advice. Consult qualified legal counsel for your situation.` |
| Finance / investing | `> This is educational content, not financial advice. Consult a licensed financial advisor for personal decisions.` |
| Psychology / mental health | `> For mental health concerns, consult a qualified mental health professional.` |

### 5. Review it

Run `grimoire:review-best-practice-skill` on your file and fix every REJECT and NEEDS-REVISION finding (`grimoire:revise-best-practice-skill` helps). Test the skill with at least one AI agent on a real task.

### 6. Register it

1. Add a line to [SKILLS.md](./SKILLS.md) under the right domain and subdomain, in alphabetical order:
   ```markdown
   - [`skill-name`](./skills/<domain>/<subdomain>/skills/<skill-name>/) — <description, verbatim>
   ```
2. Increase the domain count in both the table of contents and the section header, and the total on line 3.
3. Regenerate the agent manifests:
   ```bash
   make update-plugin-manifest   # python3 scripts/gen-manifests.py
   make check-manifest           # must print "in sync"
   ```

### 7. Validate

```bash
go install github.com/jeffreytse/grimoire@latest
make validate                   # grimoire validate skills/ — the same check CI runs
```

---

## Adding a Sub-domain

Run `grimoire:design-best-practice-domain` for guidance on scope and boundaries. Then:

1. Create `skills/<domain>/<subdomain>/skills/` and add its first skill.
2. Add `"./<subdomain>/skills"` to the `skills` array in `skills/<domain>/.claude-plugin/plugin.json`.
3. Add the sub-domain to the domain's row in the domains tables of `README.md`, `CLAUDE.md`, and `AGENTS.md`, and add a `### <subdomain>` section to `SKILLS.md`.
4. Run `make update-plugin-manifest`.

## Adding a Domain

1. Create `skills/<domain>/.claude-plugin/plugin.json`, modelled on an existing domain's, listing its sub-domains' `skills` folders.
2. Add a `grimoire-<domain>` entry to `.claude-plugin/marketplace.json` (`git-subdir` source, path `skills/<domain>`).
3. Add a row to the domains tables in `README.md`, `CLAUDE.md`, and `AGENTS.md`, and a `## <Domain> (N)` section plus table-of-contents link to `SKILLS.md`.
4. If the domain needs a safety footer, add it to the table above and to `STANDARD.md`.
5. Run `make update-plugin-manifest`.

---

## Pull Requests

- One skill per PR when possible — easier to review.
- Fill in the [PR template](./.github/PULL_REQUEST_TEMPLATE.md), including the checklist below.
- Use [Conventional Commits](https://www.conventionalcommits.org/), scoped by domain: `feat(design): add design-button-hierarchy`, `fix(psychology): add required disclaimer`, `docs(skills): index 3 new skills`.
- No vendor lock-in unless the skill is explicitly about that tool.
- Revising or retiring a skill: use the [skill revision](./.github/ISSUE_TEMPLATE/skill-revision.md) issue template, or `grimoire:deprecate-best-practice-skill`.

## Self-Check Before Submitting

### Qualifies
- [ ] Majority top-tier adoption, measurable impact, no ~50/50 expert split
- [ ] Searched for duplicates; extended an existing skill if one covers this

### Frontmatter
- [ ] `name` equals the folder name, starts with an approved verb, specific subject, ≤50 characters
- [ ] `description` starts with "Use when" and describes triggering conditions only
- [ ] `source` names specific institutions, standards bodies, studies, or companies — not "industry standard"
- [ ] `tags`: 3–8, covering problem, method, role/context, and outcome — not domain names

### Content
- [ ] `## Why This Is Best Practice` with Adopted by, Impact, Why best, and Sources
- [ ] Sources and numbers verified, not quoted from memory
- [ ] Steps are concrete and immediately executable, including failure cases
- [ ] One concept only
- [ ] 50–300 lines
- [ ] Required safety footer for health, law, finance, or psychology
- [ ] Skill Access section, if the skill loads other skills

### Registered
- [ ] Entry and counts updated in `SKILLS.md`
- [ ] `make check-manifest` and `make validate` pass

---

## Governance

How skills are reviewed and how disputes are settled: [GOVERNANCE.md](./GOVERNANCE.md).

## License

By contributing, you agree your contributions are licensed under [MIT](./LICENSE).
