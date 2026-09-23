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

"""Local plane from an explicit lunar radius. Not a surveyed geodesic."""

import math

MOON_RADIUS_M = 1_737_400
meters_per_deg_lat = MOON_RADIUS_M * math.pi / 180


def disks_overlap(lat1, lon1, r1_m, lat2, lon2, r2_m) -> bool:
    """local plane, not a surveyed geodesic.

    Latitude scale is meters_per_deg_lat from a 1,737,400 m lunar radius.
    Longitude scale is that times cos(latitude).
    """
    meters_per_deg_lon = meters_per_deg_lat * math.cos(math.radians(lat1))
    dx = (lon1 - lon2) * meters_per_deg_lon
    dy = (lat1 - lat2) * meters_per_deg_lat
    return math.hypot(dx, dy) < (r1_m + r2_m)
