.PHONY: validate test-schema \
        update-plugin-manifest check-manifest bump-version help

validate: ## Validate all SKILL.md files (quality + duplicates)
	grimoire validate skills/

test-schema: ## Run conformance test suite against schema/tests fixtures
	grimoire validate --test-schema schema/tests

fix-frontmatter: ## Fix validation errors via AI (deterministic pre-fix + AI fallback)
	grimoire validate skills/ --fix

update-plugin-manifest: ## Regenerate every agent manifest (skill folders, version) from skills/
	python3 scripts/gen-manifests.py

check-manifest: ## Verify agent manifests match skills/ and VERSION
	python3 scripts/gen-manifests.py --check

bump-version: ## Bump skills library version — usage: make bump-version V=1.2.3
	@test -n "$(V)" || (echo "Usage: make bump-version V=x.y.z"; exit 1)
	bash scripts/bump-version.sh $(V)

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
