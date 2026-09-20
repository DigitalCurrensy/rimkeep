# RIMKEEP

Lunar traffic law. Two plans cannot sit on the same ground. Heritage is a keep-out, not a storybook.

Live C++20 engine (this repo was docs-only; engine sources land on `engine/wave-polar`):

```
g++ -std=c++20 -O3 -fno-exceptions -fno-rtti -I src src/*.cpp -o rimkeep-eval
./rimkeep-eval --probe --iso 2026-09-20T12:00:00
./rimkeep-eval --site reiner-gamma --vehicle nova-c --iso 2026-09-07T00:00:00
```

Kernels and LOLA rasters are **not** in git. Bind `/workspace/shared_space_assets` (project hub).

Sanity lock 2026-09-20T12:00Z: subsolar 0.74S 70.64E, sub-Earth 4.73N 1.30W, range 403011.6 km.
Reiner Gamma + Nova-C 2026-09-07: sun el 24.35, composite 85.7, pass.
Polar sites use LDEM 40 m (80–90S) and 20 m (87.5–90S). Gate lifts off `not_enough` at ≤60 m.
