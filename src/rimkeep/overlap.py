import math


def disks_overlap(lat1, lon1, r1_m, lat2, lon2, r2_m, meters_per_deg=30300.0) -> bool:
    # crude lunar local plane; replace with proper geodesic later
    dx = (lon1 - lon2) * meters_per_deg * math.cos(math.radians(lat1))
    dy = (lat1 - lat2) * meters_per_deg
    return math.hypot(dx, dy) < (r1_m + r2_m)
