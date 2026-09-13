# syntax=docker/dockerfile:1

FROM debian:trixie-slim

ARG ZOLA_VERSION=0.23.5
ARG TARGETARCH

RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates curl tar \
  && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
  case "${TARGETARCH}" in \
    amd64) ZOLA_ARCH="x86_64-unknown-linux-gnu" ;; \
    arm64) ZOLA_ARCH="aarch64-unknown-linux-gnu" ;; \
    *) echo "Unsupported architecture: ${TARGETARCH}" >&2; exit 1 ;; \
  esac; \
  curl -fsSL \
    "https://github.com/getzola/zola/releases/download/v${ZOLA_VERSION}/zola-v${ZOLA_VERSION}-${ZOLA_ARCH}.tar.gz" \
    | tar -xz -C /usr/local/bin zola; \
  zola --version

WORKDIR /site
EXPOSE 1111

CMD ["zola", "serve", "--interface", "0.0.0.0", "--port", "1111"]
