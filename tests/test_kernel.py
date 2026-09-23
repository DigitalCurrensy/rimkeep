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

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from rimkeep.keep import keep  # noqa: E402
from rimkeep.overlap import MOON_RADIUS_M, disks_overlap, meters_per_deg_lat  # noqa: E402


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

    def test_negative_slope_width_or_setback_is_missing(self) -> None:
        self.assertEqual(keep(False, -1, 80, 40), "missing")
        self.assertEqual(keep(False, 10, 80, -1), "missing")
        self.assertEqual(keep(False, 10, -1, 40), "missing")


class OverlapTests(unittest.TestCase):
    def test_a_point_overlaps_itself_when_radii_are_positive(self) -> None:
        self.assertTrue(disks_overlap(0.0, 0.0, 1.0, 0.0, 0.0, 1.0))
        self.assertTrue(disks_overlap(-12.5, 40.25, 0.5, -12.5, 40.25, 25.0))

    def test_one_degree_of_latitude_does_not_overlap_at_100_m(self) -> None:
        self.assertFalse(disks_overlap(0.0, 0.0, 100.0, 1.0, 0.0, 100.0))
        self.assertFalse(disks_overlap(20.0, 10.0, 100.0, 21.0, 10.0, 100.0))

    def test_points_a_few_meters_apart_overlap_when_radii_cover_the_gap(self) -> None:
        self.assertEqual(MOON_RADIUS_M, 1_737_400)
        self.assertEqual(meters_per_deg_lat, MOON_RADIUS_M * math.pi / 180.0)
        four_m_deg = 4.0 / meters_per_deg_lat
        self.assertTrue(disks_overlap(0.0, 10.0, 3.0, four_m_deg, 10.0, 3.0))
        lat = 60.0
        dlon = 4.0 / (meters_per_deg_lat * math.cos(math.radians(lat)))
        self.assertTrue(disks_overlap(lat, 0.0, 3.0, lat, dlon, 3.0))

    def test_negative_radius_does_not_overlap(self) -> None:
        self.assertFalse(disks_overlap(0.0, 0.0, -1.0, 0.0, 0.0, 1.0))
        self.assertFalse(disks_overlap(0.0, 0.0, 1.0, 0.0, 0.0, -5.0))



class FiniteRimTests(unittest.TestCase):
    def test_non_finite_is_missing(self) -> None:
        self.assertEqual(keep(False, float("nan"), 100.0, 40.0), "missing")


    def test_non_finite_overlap_is_not_separate(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            disks_overlap(float("nan"), 0.0, 1.0, 0.0, 0.0, 1.0)
        self.assertEqual(str(ctx.exception), "bad number")


if __name__ == "__main__":
    unittest.main()
