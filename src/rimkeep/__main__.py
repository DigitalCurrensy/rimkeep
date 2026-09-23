# Copyright 2026 Digital Currensy Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Score each row of a rim CSV. Empty fields are missing."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from .keep import keep

HEADER = ("on_rim", "slope_deg", "psr_m", "width_m")


def _blank(value: str | None) -> str:
    if value is None:
        return ""
    return value.strip()


def _parse_on_rim(value: str | None) -> bool | None:
    text = _blank(value).lower()
    if text == "":
        return None
    if text in {"true", "yes", "1"}:
        return True
    if text in {"false", "no", "0"}:
        return False
    raise ValueError(f"bad on_rim value: {value}")


def _parse_float(value: str | None) -> float | None:
    text = _blank(value)
    if text == "":
        return None
    return float(text)


def score_csv(path: Path) -> list[str]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        names = tuple((reader.fieldnames or ()))
        if names != HEADER:
            raise ValueError("header must be on_rim,slope_deg,psr_m,width_m")
        verdicts: list[str] = []
        for row in reader:
            verdicts.append(
                keep(
                    _parse_on_rim(row["on_rim"]),
                    _parse_float(row["slope_deg"]),
                    _parse_float(row["psr_m"]),
                    _parse_float(row["width_m"]),
                )
            )
    return verdicts


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("usage: python -m rimkeep examples/rim.csv", file=sys.stderr)
        return 2
    try:
        for verdict in score_csv(Path(args[0])):
            print(verdict)
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
