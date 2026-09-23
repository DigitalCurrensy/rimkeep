from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rimkeep.keep import keep  # noqa: E402


class KeepTests(unittest.TestCase):
    def test_on_rim_wins_even_when_the_other_gates_also_trip(self) -> None:
        self.assertEqual(keep(True, 20, 20, 10), "on_rim")

    def test_shadow_before_slope(self) -> None:
        self.assertEqual(keep(False, 20, 20, 40), "psr")

    def test_slope_then_thin_then_ok(self) -> None:
        self.assertEqual(keep(False, 16, 80, 40), "slope")
        self.assertEqual(keep(False, 10, 80, 20), "thin")
        self.assertEqual(keep(False, 10, 80, 40), "ok")

    def test_missing_is_not_ok(self) -> None:
        self.assertEqual(keep(None, 10, 80, 40), "missing")
        self.assertEqual(keep(False, None, None, 40), "missing")


if __name__ == "__main__":
    unittest.main()
