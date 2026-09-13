# wiseshell.net

Lloc estàtic per wiseshell.net generat amb [Zola](https://www.getzola.org/).
Té un .github/workflows.yml que executa el build automàtic del site
cada vegada que es fa merge o push en la branca master.

## Requisits

- [Zola v0.23.5](https://github.com/getzola/zola/releases/tag/v0.23.5), o Docker

## Desenvolupament local

```bash
zola serve
```

Obre http://127.0.0.1:1111

```bash
zola build
```

Genera el lloc a `docs/`.

## Docker

```bash
docker compose up --build
```

Preview a http://localhost:1111

```bash
docker compose run --rm zola zola build
```

Per forçar arquitectura: `PLATFORM=linux/arm64 docker compose build`.

## Traduccions

Les traduccions es troben en format clau-valor dins i18n.

## GitHub Pages

wiseshell.net s'executa amb GitHub Pages dins `/docs`.

## Notes

* Imatges basades en https://retroarch.org
* Paleta de https://www.color-hex.com/color-palette/21486 i https://nhfournier.es
