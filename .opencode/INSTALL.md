# Installing grimoire for OpenCode

## Installation

```bash
opencode plugin 'github:jeffreytse/grimoire-core#main' -g   # -g: global config; omit for project
```

Or add it to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["github:jeffreytse/grimoire-core#main"]
}
```

Restart OpenCode. The plugin registers every nested `skills/` folder of grimoire-core and injects the `AGENTS.md` bootstrap context.

## Usage

Use OpenCode's native `skill` tool:

```
use skill tool to list skills
use skill tool to load propose-conventional-commit
```

## Updating

To pin a specific version:

```json
{
  "plugin": ["github:jeffreytse/grimoire-core#v1.0.0"]
}
```

## Alternative: grimoire CLI

```bash
grimoire install --target opencode --global   # links skills into ~/.config/opencode/skills
```

## Troubleshooting

### Skills not found

Check that the plugin is loading:
```bash
opencode run --print-logs "hello" 2>&1 | grep -i grimoire
```

### Tool mapping

When skills reference Claude Code tools:
- `Skill` tool → OpenCode's native `skill` tool
- `Read`, `Write`, `Edit`, `Bash` → your native tools
- `TodoWrite` → `todowrite`
