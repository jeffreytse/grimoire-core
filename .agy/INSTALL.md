# Installing grimoire-core for Antigravity CLI (agy)

## One-command install (recommended)

```bash
agy plugin install https://github.com/jeffreytse/grimoire-core
```

Stages under `~/.gemini/config/plugins/grimoire-core/`.

## Local install

```bash
git clone https://github.com/jeffreytse/grimoire-core
agy plugin install ./grimoire-core
```

Or install via the bundled `.agy/` entry point:

```bash
agy plugin install ./grimoire-core/.agy
```

## Pin a release

```bash
git clone --branch v0.1.0 --depth 1 https://github.com/jeffreytse/grimoire-core
agy plugin install ./grimoire-core
```

## Uninstall

```bash
agy plugin uninstall grimoire-core
```

## Alternative: grimoire CLI

The [grimoire CLI](https://github.com/jeffreytse/grimoire) manages skills across all agents:

```bash
grimoire install --target antigravity
```
