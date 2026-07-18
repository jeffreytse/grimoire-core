.PHONY: validate test-schema \
        update-plugin-manifest check-manifest bump-version help

validate: ## Validate all SKILL.md files (quality + duplicates)
	grimoire validate skills/

test-schema: ## Run conformance test suite against schema/tests fixtures
	grimoire validate --test-schema schema/tests

fix-frontmatter: ## Fix validation errors via AI (deterministic pre-fix + AI fallback)
	grimoire validate skills/ --fix

update-plugin-manifest: ## Auto-generate skills list in .claude-plugin/plugin.json
	python3 scripts/update-plugin-manifest.py

check-manifest: ## Verify plugin.json skill list matches actual dirs
	@actual=$$(find skills -mindepth 1 -type d -name "skills" -not -empty | wc -l | tr -d ' '); \
	listed=$$(python3 -c "import json; d=json.load(open('.claude-plugin/plugin.json')); print(len(d['skills']))"); \
	echo "Actual skill dirs: $$actual"; \
	echo "Listed in manifest: $$listed"; \
	if [ "$$actual" != "$$listed" ]; then \
		echo "MISMATCH — run: make update-plugin-manifest"; exit 1; \
	else \
		echo "OK"; \
	fi

bump-version: ## Bump skills library version — usage: make bump-version V=1.2.3
	@test -n "$(V)" || (echo "Usage: make bump-version V=x.y.z"; exit 1)
	bash scripts/bump-version.sh $(V)

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
