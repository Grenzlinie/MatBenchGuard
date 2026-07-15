# Ring‑Approximation Free Energies and Phase Boundaries for a Cubic Ferroelectric

## Problem background
In a cubic ferroelectric, the coupling of critical fluctuations of the order parameter can turn a continuous phase transition into a first‑order one. The ring‑diagram approximation sums an infinite series of one‑loop diagrams to obtain the free energy of the low‑temperature phases (tetragonal and rhombohedral). This reveals fluctuation‑driven first‑order character and yields closed‑form expressions for the free energy, the binodal and spinodal curves, and the corresponding jumps in the polarization order parameter. Reproducing the numerical evaluation of these expressions confirms the analytic structure.

## Approach
The method uses the asymptotic (large‑polarization) form of the free energy obtained from the ring approximation. For each phase the free energy $F$ is expressed as a polynomial in the dimensionless polarization $p$ with coefficients that depend on the coupling constants ($g_2$ for the tetragonal phase, $g_1$ for the rhombohedral phase) and on the anisotropy $f$. The cubic and quartic terms drive the first‑order transition.

**Tetragonal phase** (polarization along the cube side, $z=\gamma_1/\gamma_2$ set to zero):
- Asymptotic free energy (with overall prefactor $\varkappa^3/(12\pi)$ set to 1 for simplicity):
  $$F^{(1)} = \frac{1}{g_2}\Bigg\{[1+g_2\big(2-\tfrac{179}{280}f\big)]p^2 - g_2\big(\tfrac{6}{5}-\tfrac{4}{35}f\big)|p|^3 + g_2\big(\tfrac{9}{20}+\tfrac{13}{140}f\big)p^4\Bigg\}$$
- Binodal polarization jump:
  $$p_b = \frac{2}{\frac{6}{5}-\frac{4}{35}f}\left[\frac{1}{g_2}+\big(2-\tfrac{179}{280}f\big)\right]$$
- Spinodal polarization jump:
  $$p_s = \frac{4}{3}\frac{1}{\frac{6}{5}-\frac{4}{35}f}\left[\frac{1}{g_2}+\big(2-\tfrac{179}{280}f\big)\right]$$
- Binodal condition (an expression for $g_1$ in terms of $g_2$ and $f$):
  $$g_1 \approx -g_2^2\Big(\tfrac{9}{10}+\tfrac{13}{70}f\Big)\left[1-\frac{4g_2\big(\tfrac{9}{5}-\tfrac{2}{7}f\big)}{9+\tfrac{13}{7}f}\right]$$
- Spinodal condition:
  $$g_1 \approx -g_2^2\Big(\tfrac{9}{10}+\tfrac{13}{70}f\Big)\left[1-\frac{\tfrac{9}{2}g_2\big(\tfrac{9}{5}-\tfrac{2}{7}f\big)}{9+\tfrac{13}{7}f}\right]$$

**Rhombohedral phase** (polarization along the cube diagonal, with $z=-2$):
- Asymptotic free energy (same prefactor convention):
  $$F^{(2)} = \frac{1}{g_1}\Bigg\{[1+g_1\big(2+\tfrac{2}{5}f\big)]p^2 - g_1\big(\tfrac{6}{5}+\tfrac{229}{630}f\big)|p|^3 + g_1\big(\tfrac{9}{20}+\tfrac{8}{63}f\big)p^4\Bigg\}$$
- Binodal polarization jump:
  $$p_b = \frac{2}{\frac{6}{5}+\frac{229}{630}f}\left[\frac{1}{g_1}+\big(2+\tfrac{2}{5}f\big)\right]$$
- Spinodal polarization jump:
  $$p_s = \frac{4}{3}\frac{1}{\frac{6}{5}+\frac{229}{630}f}\left[\frac{1}{g_1}+\big(2+\tfrac{2}{5}f\big)\right]$$
- Binodal condition (an expression for $g_2$ in terms of $g_1$ and $f$):
  $$g_2 \approx -\frac{g_1}{2} - g_1^2\Big(\tfrac{27}{20}+\tfrac{8}{21}f\Big)\left[1-\frac{g_1\big(\tfrac{36}{25}+\tfrac{229}{315}f\big)}{\tfrac{9}{5}+\tfrac{32}{63}f}\right]$$
- Spinodal condition:
  $$g_2 \approx -\frac{g_1}{2} - g_1^2\Big(\tfrac{27}{20}+\tfrac{8}{21}f\Big)\left[1-\frac{\tfrac{9}{32}g_1\big(\tfrac{36}{25}+\tfrac{229}{315}f\big)}{\tfrac{9}{20}+\tfrac{8}{63}f}\right]$$

For the consistency checks, evaluate the right‑hand side of each binodal/spinodal equation; a valid, finite, negative value confirms that the corresponding equation is satisfied for the given parameters, so set the corresponding boolean to `true`. You will implement these formulas in a Python script.

## Reproduction target
Implement the above formulas numerically. Compute the following quantities for the tetragonal phase using $g_2=0.3,\; f=0.05,\; p=2.0$ and for the rhombohedral phase using $g_1=0.2,\; f=0.05,\; z=-2,\; p=2.0$:
- Free energy $F$ from the respective asymptotic expression.
- Binodal polarization jump $p_b$.
- Spinodal polarization jump $p_s$.
- Boolean flags `binodal_check` and `spinodal_check` indicating whether the corresponding binodal/spinodal condition evaluates to a consistent value (i.e., yields a valid numerical result).
Write all results into `/app/outputs/results.json` following the schema given in the output contract.
You may use only Python 3 and its standard `math` module; no external libraries are required.

## Assets

- Python 3: python

## Workflow steps

### Step 1: Compute ring‑approximation quantities for both phases
- Role: scored (load-bearing)
- Action: Implement the free‑energy formulas for the tetragonal and rhombohedral phases in the ring approximation. For the tetragonal phase, using the large‑polarization asymptotic expression, compute the free energy F, the binodal polarization jump p_b, the spinodal polarization jump p_s, and verify the binodal and spinodal equations. For the rhombohedral phase, similarly compute the free energy F, the jumps p_b and p_s, and verify the binodal and spinodal equations. Use the provided parameters: for tetragonal, g2=0.3, f=0.05, p=2.0; for rhombohedral, g1=0.2, f=0.05, z=-2, p=2.0. Write all results to results.json in the specified schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys 'tetragonal' and 'rhombohedral'. Each value is an object containing numeric fields: g2, f, p, F_asymptotic, p_b, p_s (for tetragonal; g1 instead of g2 for rhombohedral) and boolean fields binodal_check, spinodal_check.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed ring‑approximation quantities for the tetragonal and rhombohedral phases of a cubic ferroelectric, including free energies, polarization jumps, and binodal/spinodal equation verification.
- schema:
  - `type`: object
  - `required`: `tetragonal`, `rhombohedral`
  - `items`:
    - `tetragonal`: object with numeric g2, f, p, F_asymptotic, p_b, p_s and boolean binodal_check, spinodal_check
    - `rhombohedral`: object with numeric g1, f, p, F_asymptotic, p_b, p_s and boolean binodal_check, spinodal_check

Notes: All quantities are computed from the analytical formulas derived in the paper. No external dataset is required; the given parameter values serve as inputs. The hidden checker compares the numerical values against pre‑computed references within tight tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "tetragonal",
          "rhombohedral"
        ],
        "items": {
          "tetragonal": "object with numeric g2, f, p, F_asymptotic, p_b, p_s and boolean binodal_check, spinodal_check",
          "rhombohedral": "object with numeric g1, f, p, F_asymptotic, p_b, p_s and boolean binodal_check, spinodal_check"
        }
      },
      "description": "Computed ring‑approximation quantities for the tetragonal and rhombohedral phases of a cubic ferroelectric, including free energies, polarization jumps, and binodal/spinodal equation verification."
    }
  ],
  "notes": "All quantities are computed from the analytical formulas derived in the paper. No external dataset is required; the given parameter values serve as inputs. The hidden checker compares the numerical values against pre‑computed references within tight tolerances."
}
```

## How you are scored
A hidden verifier will recompute all expected quantities using the same formulas and parameter values. Your submitted numeric fields will be compared against the reference values within a strict relative/absolute tolerance. The boolean consistency flags will also be checked against the expected values. The final reward is a weighted combination of these per‑field comparisons. You must derive every output from the formulas described above; simply outputting a fixed number will not pass inspection.
