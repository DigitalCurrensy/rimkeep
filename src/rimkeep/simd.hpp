#pragma once
// Clenshaw Chebyshev of the first kind. c0 is NOT halved.
// P = τ b1 - b2 + c0. dP/dτ = b1 + τ d1 - d2. Velocity = (1/RADIUS) dP/dτ.
#include <cstddef>
namespace rimkeep { using f64 = double;
namespace simd {
inline f64 clenshaw(const f64* c, int deg, f64 tau) {
  if (deg < 0) return 0; if (deg == 0) return c[0];
  f64 b2 = 0, b1 = 0;
  for (int k = deg; k >= 1; --k) { const f64 b0 = 2.0 * tau * b1 - b2 + c[k]; b2 = b1; b1 = b0; }
  return tau * b1 - b2 + c[0];
}
inline void clenshaw_pd(const f64* c, int deg, f64 tau, f64* p, f64* dp) {
  if (deg <= 0) { *p = deg < 0 ? 0 : c[0]; *dp = 0; return; }
  f64 b2 = 0, b1 = 0, d2 = 0, d1 = 0;
  for (int k = deg; k >= 1; --k) {
    const f64 b0 = 2.0 * tau * b1 - b2 + c[k];
    const f64 d0 = 2.0 * b1 + 2.0 * tau * d1 - d2;
    b2 = b1; b1 = b0; d2 = d1; d1 = d0;
  }
  *p = tau * b1 - b2 + c[0]; *dp = b1 + tau * d1 - d2;
}
}}
