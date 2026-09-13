#!/usr/bin/make -f

ZOLA            ?= zola
ZOLA_VERSION    ?= 0.23.5
PORT            ?= 1111
INTERFACE       ?= 127.0.0.1
OUTPUT_DIR      ?= docs
PLATFORM        ?= linux/amd64
COMPOSE         ?= docker compose
DOCKER_IMAGE    ?= wiseshell-zola

.DEFAULT_GOAL := help

.PHONY: help \
	serve build check clean rebuild \
	docker-build docker-up docker-down docker-logs docker-shell \
	docker-serve docker-build-site docker-check docker-rebuild \
	version

##@ General

help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} \
		/^##@/ {printf "\n\033[1m%s\033[0m\n", substr($$0, 5)} \
		/^[a-zA-Z0-9_-]+:.*?##/ {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

version: ## Print Zola version (host)
	@$(ZOLA) --version

##@ Local (host Zola)

serve: ## Live preview (default http://127.0.0.1:1111)
	$(ZOLA) serve --interface $(INTERFACE) --port $(PORT)

build: ## Build static site into docs/
	$(ZOLA) build

check: ## Check site for errors / broken links
	$(ZOLA) check

clean: ## Remove build output (docs/)
	rm -rf $(OUTPUT_DIR)

rebuild: clean build ## Clean then build

##@ Docker

docker-build: ## Build the Debian 13 + Zola image
	PLATFORM=$(PLATFORM) $(COMPOSE) build

docker-up: ## Build (if needed) and start preview container
	PLATFORM=$(PLATFORM) $(COMPOSE) up --build

docker-down: ## Stop and remove containers
	$(COMPOSE) down

docker-logs: ## Follow container logs
	$(COMPOSE) logs -f zola

docker-shell: ## Open a shell in the Zola container
	PLATFORM=$(PLATFORM) $(COMPOSE) run --rm --entrypoint /bin/bash zola

docker-serve: ## Serve via Docker (foreground, port 1111)
	PLATFORM=$(PLATFORM) $(COMPOSE) run --rm --service-ports zola \
		zola serve --interface 0.0.0.0 --port $(PORT)

docker-build-site: ## Build site into docs/ via Docker
	PLATFORM=$(PLATFORM) $(COMPOSE) run --rm zola zola build

docker-check: ## Run zola check via Docker
	PLATFORM=$(PLATFORM) $(COMPOSE) run --rm zola zola check

docker-rebuild: ## Rebuild Docker image from scratch (no cache)
	PLATFORM=$(PLATFORM) $(COMPOSE) build --no-cache
