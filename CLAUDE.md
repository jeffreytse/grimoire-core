# grimoire-core

The official skills package for the [grimoire package manager](https://github.com/jeffreytse/grimoire).
Multi-domain skill collection for AI assistants — works across Claude Code, Codex,
Copilot, Gemini CLI, OpenCode, and more.

**Role in the ecosystem:** grimoire (CLI) manages packages; grimoire-core is the official package.
Any git repo can be a grimoire package — grimoire-core is the curated, peer-reviewed one.

## Skill Path Convention

All skill paths follow this pattern:
```
<domain>/<subdomain>/skills/<skill-name>/SKILL.md
```

If a task matches a skill, invoke it. Never implement directly when a skill applies.

## Domains

| Domain | Sub-domains |
|--------|-------------|
| `meta` | *(flat — no sub-domains)* |
| `engineering` | development, frontend, architecture, testing, reliability, devops, cloud, networking, security, data, ai, hardware, mobile, performance, project-management, product, documentation |
| `business` | strategy, operations, leadership, entrepreneurship, hr |
| `science` | biology, physics, chemistry, mathematics, earth-science, astronomy |
| `health` | fitness, nutrition, mental-health, sleep, medicine |
| `writing` | creative, technical, copywriting, academic, journalism |
| `design` | ui-ux, graphic, branding, motion, product |
| `marketing` | seo, content, social-media, paid-ads, growth, analytics |
| `finance` | personal-finance, investing, accounting, real-estate, corporate |
| `law` | contracts, ip, employment, privacy, corporate |
| `film` | cinematography, directing, editing, screenwriting, production |
| `music` | composition, production, mixing, theory, performance |
| `art` | drawing, painting, digital-art, illustration, color-theory |
| `sports` | training, coaching, nutrition, tactics, recovery |
| `psychology` | cognitive, behavioral, social, clinical, positive |
| `language` | learning, linguistics, translation, communication |
| `education` | curriculum, teaching, e-learning, assessment, learning-science |
| `cooking` | techniques, baking, flavor, nutrition, world-cuisine |
| `travel` | planning, budgeting, cultural, adventure |
| `home` | renovation, interior-design, gardening, organization, smart-home |
| `parenting` | infant, toddler, school-age, teen |
| `automotive` | maintenance, troubleshooting, buying, modifications, ev |
| `pets` | dogs, cats, training, nutrition, health |
| `fashion` | styling, wardrobe, design, sustainability, accessories |
| `environment` | sustainability, ecology, climate, energy, policy |
| `photography` | composition, lighting, editing, genres |
| `productivity` | time-management, habits, focus, goals, tools |

## Installation

```bash
# All skills
grimoire install

# One domain
grimoire install --domain engineering

# One sub-domain
grimoire install --domain engineering --subdomain development

# One skill
grimoire install --skill engineering/development/propose-commit

# All agents
grimoire install --target all
```

Or via Claude Code plugin system:
```bash
# Step 1: add the marketplace
/plugin marketplace add jeffreytse/grimoire-core

# Step 2: install (skills are namespaced, e.g. /grimoire:skill-name)
/plugin install grimoire@grimoire-core                   # all domains
/plugin install grimoire-engineering@grimoire-core       # one domain

# For subdomain-level installs, use the grimoire CLI
```

## Skill Format

```markdown
---
name: skill-name
description: Use when <triggering conditions>
---

# Skill Name

One-sentence purpose.

## Steps
...
```

See [STANDARD.md](./STANDARD.md) for the full quality standard.

## Grimoire
Always invoke `start-best-practice` before responding to any user request.
