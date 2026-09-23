# RIMKEEP

For a traverse planner who wants to drive a crater rim.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited.

## What it decides

A crater-rim keep-out from on-rim, shadow setback, slope, and width. Ok is not a road.

## The rule

`keep` returns the first gate that trips, in this order:

1. `on_rim` is missing → `missing`
2. `on_rim` is true → `on_rim`
3. PSR setback is not missing and is under 50 m → `psr`
4. slope or width is missing → `missing`
5. slope is over 15 degrees → `slope`
6. width is under 30 m → `thin`
7. otherwise → `ok`

Ok is not a road. A missing `on_rim`, slope, or width is not ok. A missing PSR setback does not fail by itself.

## Overlap

The overlap helper is a local plane using a 1,737,400 m lunar radius and is not a geodesic. Latitude meters per degree are that radius times π/180. Longitude scale is that times cos(latitude).

## Worked rows

`examples/rim.csv` uses the header `on_rim,slope_deg,psr_m,width_m`. It includes one on-rim row and one ok row. Empty fields mean missing. Worked rows are not a traverse plan and no elevation model is fetched.

## Run

```
git clone <this repo>
cd rimkeep
PYTHONPATH=src python -m unittest tests.test_kernel
PYTHONPATH=src python -m rimkeep examples/rim.csv
```

Python 3.11 or newer. No third-party packages.

Copyright 2026 Digital Currensy Inc. Apache-2.0.
