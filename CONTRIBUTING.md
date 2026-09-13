# Contribució

Aquest lloc és estàtic (Zola). No hi ha admin ni base de dades.

## Contingut

- Pàgines: `content/` (ca), `content/es/`, `content/en/`
- Cadenes d’interfície: `i18n/*.toml`
- Estils: `static/css/campaign.css`
- Plantilles: `templates/`

## Flux

1. Edita Markdown / TOML / CSS
2. `zola serve` o `docker compose up --build`
3. `make build` per generar `public/` localment; el merge a `master` desplega via Actions

## Wiki

Per documentar un joc, afegeix una pàgina Markdown sota `content/wiki/` (i les traduccions a `es/` / `en/`) i enllaça-la des de `wiki.md`.
