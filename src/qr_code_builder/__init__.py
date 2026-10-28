"""Build static QR codes.

A static QR code embeds the payload itself, so there is no redirect
service in the middle and nothing that can expire.
"""

import argparse
from pathlib import Path
from typing import Literal

import segno

ErrorLevel = Literal["L", "M", "Q", "H"]
ERROR_LEVELS: tuple[ErrorLevel, ...] = ("L", "M", "Q", "H")


def build(data: str, *, error: ErrorLevel = "M") -> segno.QRCode:
    """Encode `data` into a QR code. Raises ValueError if it does not fit."""
    if not data:
        raise ValueError("data must not be empty")
    return segno.make_qr(data, error=error)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("data", help="text or URL to encode")
    parser.add_argument("-o", "--output", type=Path, default=Path("qr.png"), help="output file (.png or .svg)")
    parser.add_argument("-e", "--error", choices=ERROR_LEVELS, default="M", help="error correction level")
    parser.add_argument("-s", "--scale", type=int, default=10, help="pixels per module")
    args = parser.parse_args(argv)

    try:
        build(args.data, error=args.error).save(args.output, scale=args.scale)
    except ValueError as exc:
        parser.exit(1, f"error: {exc}\n")
