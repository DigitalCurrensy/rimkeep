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

"""On the rim is not a road.

Order: standing on the rim, then a negative slope, width, or setback,
then a shadow setback under 50 m, then an inner slope over 15 degrees,
then a width under 30 m.
Ok is not a road. A missing input is not ok.
A missing PSR setback is not a fail by itself.
"""

from __future__ import annotations

import math


def _bad(value: float | None) -> bool:
    return value is not None and not math.isfinite(value)


def keep(
    on_rim: bool | None,
    inner_slope_deg: float | None,
    psr_setback_m: float | None,
    width_m: float | None,
) -> str:
    if on_rim is None:
        return "missing"
    if _bad(inner_slope_deg) or _bad(psr_setback_m) or _bad(width_m):
        return "missing"
    if on_rim:
        return "on_rim"
    if inner_slope_deg is not None and inner_slope_deg < 0:
        return "missing"
    if width_m is not None and width_m < 0:
        return "missing"
    if psr_setback_m is not None and psr_setback_m < 0:
        return "missing"
    if psr_setback_m is not None and psr_setback_m < 50:
        return "psr"
    if inner_slope_deg is None or width_m is None:
        return "missing"
    if inner_slope_deg > 15:
        return "slope"
    if width_m < 30:
        return "thin"
    return "ok"
