# qr-code-builder

[![CI](https://github.com/laisbsc/qr-code-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/laisbsc/qr-code-builder/actions/workflows/ci.yml)

Static QR codes that never expire. The payload is encoded directly into the
image; there is no redirect service, no tracking, no account, nothing to lapse.

```sh
uv run qr-code-builder "https://example.com" -o site.png
uv run qr-code-builder "WIFI:S:home;T:WPA;P:secret;;" -o wifi.svg -e H
```

Options: `-o/--output` (.png or .svg), `-e/--error` (L, M, Q, H), `-s/--scale`.

Keep the content static: encode the final URL, not a link shortener.

```sh
uv run pytest
uv run ruff check . && uv run ruff format --check .
```
