"""On the rim is not a road.

Order: standing on the rim, then a shadow setback under 50 m,
then an inner slope over 15 degrees, then a width under 30 m.
Ok is not a road. A missing input is not ok.
"""

from __future__ import annotations


def keep(
    on_rim: bool | None,
    inner_slope_deg: float | None,
    psr_setback_m: float | None,
    width_m: float | None,
) -> str:
    if on_rim is None:
        return "missing"
    if on_rim:
        return "on_rim"
    if psr_setback_m is not None and psr_setback_m < 50:
        return "psr"
    if inner_slope_deg is None or width_m is None:
        return "missing"
    if inner_slope_deg > 15:
        return "slope"
    if width_m < 30:
        return "thin"
    return "ok"
