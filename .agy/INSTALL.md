# Installing grimoire-core for Antigravity CLI (agy)

## Recommended: grimoire CLI

```bash
curl -fsSL https://raw.githubusercontent.com/jeffreytse/grimoire/main/scripts/install.sh | bash
grimoire install --global --target antigravity
```

This links each skill into `~/.gemini/antigravity-cli/skills/<name>/`, the
one-level layout agy discovers.

## Why not `agy plugin install`?

grimoire-core keeps skills nested as
`skills/<domain>/<sub>/skills/<name>/SKILL.md`. `agy plugin install` only scans
`skills/*/` and ignores a manifest `skills` list, so it would register the 27
domain folders rather than the skills inside them. Use the grimoire CLI
until agy supports declared skill paths.

## Uninstall

```bash
grimoire uninstall --target antigravity
```
