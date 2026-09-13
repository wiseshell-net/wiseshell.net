# wiseshell.net

Lloc estàtic per wiseshell.net generat amb [Zola](https://www.getzola.org/).
Després de cada merge a `master`, el workflow `.github/workflows/deploy.yml`
construeix el lloc i el desplega amb GitHub Pages (Actions).

## Requisits

- [Zola v0.23.5](https://github.com/getzola/zola/releases/tag/v0.23.5), o Docker

## Desenvolupament local

```bash
zola serve
```

Obre http://127.0.0.1:1111

```bash
make build
```

Genera el lloc a `public/` i hi copia el `CNAME` de l’arrel.

## Docker

```bash
docker compose up --build
```

Preview a http://localhost:1111

```bash
make docker-build-site
```

També genera `public/` amb el `CNAME` copiat.

Per forçar arquitectura: `PLATFORM=linux/arm64 docker compose build`.

## Traduccions

Les traduccions es troben en format clau-valor dins i18n.

## GitHub Pages

wiseshell.net es desplega amb GitHub Pages via **GitHub Actions** (artefacte de `public/`).
A Settings → Pages, la font ha de ser «GitHub Actions», no «Deploy from a branch».
El fitxer `CNAME` a l’arrel defineix el domini personalitzat.

## Notes

* Imatges basades en https://retroarch.org
* Paleta de https://www.color-hex.com/color-palette/21486 i https://nhfournier.es
