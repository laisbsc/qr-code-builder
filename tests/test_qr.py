from pathlib import Path

import pytest
import segno

from qr_code_builder import build, main


def test_build_honours_error_level() -> None:
    assert build("https://example.com", error="H").error == "H"


def test_build_rejects_empty() -> None:
    with pytest.raises(ValueError, match="empty"):
        build("")


def test_build_rejects_oversized() -> None:
    with pytest.raises(segno.DataOverflowError):
        build("x" * 10_000)


@pytest.mark.parametrize("suffix", [".png", ".svg"])
def test_main_writes_file(tmp_path: Path, suffix: str) -> None:
    out = tmp_path / f"qr{suffix}"
    main(["hello", "-o", str(out), "-e", "H", "-s", "4"])
    assert out.stat().st_size > 0


def test_main_exits_on_empty(tmp_path: Path) -> None:
    with pytest.raises(SystemExit, match="1"):
        main(["", "-o", str(tmp_path / "x.png")])
