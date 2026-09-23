# RIMKEEP

For a traverse planner who wants to drive a crater rim.

**Owner:** Digital Currensy Inc.
**Copyright:** 2026 Digital Currensy Inc.
**License:** Apache-2.0. The file named LICENSE is the standard license and is not edited. The copyright notice is in NOTICE and at the top of each source file. Cited data and papers stay with their authors.
## What it decides

On the rim, or not. On the rim is not a road.

## The rule

Standing on the rim fails first. If the pin is off the rim, a sun-shadow setback under 50 m fails, then an inner slope over 15 degrees, then a width under 30 m. Anything else is ok, and ok is not a road. A missing rim is not ok.

## Worked cases

Surveyor crater and Faustini Rim A are named. The synthetic rims each force one gate. They are not a traverse plan, and this repository does not fetch an elevation model.

## What it will not do

- Walk the rim because the picture looks flat.
- Call a keep-out a road.
- Treat ok as a landing clearance.

## Run

```
git clone <this repo>
cd rimkeep
PYTHONPATH=src python -m unittest tests.test_kernel
```

Python 3.12. No third-party packages. The test is the demo.
