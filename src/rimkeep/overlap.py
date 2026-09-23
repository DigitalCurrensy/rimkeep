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

"""Haversine on a sphere of radius 1,737,400 m. Not a surveyed control network."""

import math

MOON_RADIUS_M = 1_737_400
meters_per_deg_lat = MOON_RADIUS_M * math.pi / 180


def disks_overlap(lat1, lon1, r1_m, lat2, lon2, r2_m) -> bool:
    """True when haversine distance is less than the sum of the radii.

    A negative radius does not overlap.
    """
    if r1_m < 0 or r2_m < 0:
        return False
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lam = math.radians(lon2 - lon1)
    a = math.sin(d_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lam / 2.0) ** 2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(max(0.0, 1.0 - a)))
    return (MOON_RADIUS_M * c) < (r1_m + r2_m)
