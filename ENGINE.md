# Engine bind

Product code is clean-room C++20. No CSPICE.

- DAF Type-2 reader + Clenshaw (c0 not halved) + dP/dτ
- Geometric chain 301→3→0 / 399→3→0 / 10→0
- PA 3-1-3 inverse R3(-φ)R1(-θ)R3(-W), PA→ME 67.8526/78.6944/0.2785"
- Light-time + solar aberration
- LOLA cylindrical + polar stereographic (file-backed seek)

Large rasters / DE441 exceed this sandbox write cap (~600 MB). URLs in project `ASSET_BIND.json`.
Earthdata/Space-Track/Copernicus keys are not required for this gate.
CUDA kernels exist; this host has no nvcc — CPU twin in `src/cpu/slope_field.cpp`.

Do not merge until the operator reviews. Draft PR only.
