# RIMKEEP

RIMKEEP scores the keep-out around a crater rim. The rim is not a road.

**Owner:** Digital Currensy Inc.
**License:** Apache-2.0. Our code only. Cited maps stay with their authors.

## What it decides

On the rim, or off it. On the rim is not a route.

## The rule

The keep-out is the product. A point on the rim fails the walk. Slope, a missing sun angle, equal sites, an undeclared identity, or missing inputs fail closed. A synthetic case that sits off the rim can pass the keep-out and still is not a road.

## Worked cases

Surveyor crater, Faustini Rim A, and synthetic rims stored in this repository. Each one forces one gate: off-rim, sun angle, slope, thin data, on-rim first, a null sun angle, equal sites, an undeclared identity, or missing inputs. They are the desk’s cases, not a traverse plan.

## What it will not do

- Walk the rim because the picture looks flat.
- Fetch an elevation model in order to print the score.
- Call a keep-out a road.

## Run

```
PYTHONPATH=src python -m unittest tests.test_kernel
```

Notes under `docs/` are the build record. This page is the description.
