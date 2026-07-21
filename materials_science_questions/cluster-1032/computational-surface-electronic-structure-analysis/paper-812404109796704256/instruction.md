# Positronium formation sensitivity to surface barrier shape

## Problem background
The surface electronic barrier potential is crucial for understanding surface states but is difficult to measure experimentally. Positronium (Ps) formation at surfaces is proposed as a highly surface-sensitive spectroscopy. The formation probability depends on the overlap of incident positron and surface electron wavefunctions, which are modified by the shape of the surface barrier potentials. This task reproduces a theoretical study that models smooth barriers for electrons and positrons and calculates the Ps formation matrix element to investigate the sensitivity of the formation probability to the barrier shape.

## Surface barrier models (atomic units: ℏ = m_e = e = 1, energies in hartree, lengths in bohr)

### Electronic surface barrier V_e(z)
The electronic barrier is given by the Jones–Jennings–Jepsen formula (Eq. 3 of the paper):

$$
V_e(z) = 
\begin{cases}
-\dfrac{1}{4(z-z_0)} \Bigl(1 - e^{\lambda\,(z-z_0)}\Bigr), & z < z_0, \\[8pt]
\dfrac{-U_0}{A\,e^{-\beta\,(z-z_0)} + 1}, & z > z_0.
\end{cases}
$$

**Parameter values (fixed except λ):**
- \(z_0 = 0.0\) bohr (image plane position)
- \(U_0 = 0.5\) hartree (potential depth inside the metal)
- \(A = 1.0\)
- \(\beta = 1.0\) bohr⁻¹
- \(\lambda\) is the inverse decay length; the shape parameter is \(\lambda^{-1}\), which varies in the study.

### Positronic surface barrier V_p(z)
The positronic barrier uses the empirical form of Jennings (Eq. 4 of the paper):

$$
V_p(z) = 
\begin{cases}
-\dfrac{1}{4(z-z_0)\bigl[1 - e^{\lambda\,(z-z_0)}\bigr]} + \dfrac{e^{\gamma z}}{z}, & z < z_c, \\[8pt]
U_+, & z > z_c.
\end{cases}
$$

**Parameter values (fixed except λ):**
- \(z_0 = 0.0\) bohr (same image plane)
- \(z_c = 2.0\) bohr (sharp cut‑off position, outside the surface)
- \(U_+ = 0.0\) hartree (inner potential for positrons, set to zero as in the paper)
- \(\gamma = 1.0\) bohr⁻¹
- The same \(\lambda^{-1}\) parameter governs the shape.

---

## Single‑particle wavefunctions

The one‑dimensional Schrödinger equation (atomic units) for a particle of energy \(E\) in the potential \(V(z)\) is

$$
-\frac12 \frac{d^2\psi}{dz^2} + V(z)\,\psi(z) = E\,\psi(z).
$$

### Electron wavefunction (bound state)
Electron energy: \(E_e = -0.375\) hartree.

Because the electron is in a bound state, the wavefunction must decay to zero for \(z \to \infty\). The asymptotic potential is the image tail \(-1/(4z)\), and the exact solution of the Schrödinger equation in this tail is the Whittaker function \(W_{k,\frac12}(z)\) with

$$
k = \frac{1}{2\sqrt{2|E_e|}}.
$$

For \(E_e = -0.375\) hartree, \(\kappa_e = \sqrt{2|E_e|} = \sqrt{0.75} \approx 0.8660\), and \(k \approx 0.5774\).

The Whittaker function has the following series representation (Eq. 6 of the paper, truncated at \(n=8\) as stated):

$$
\begin{aligned}
W_{k,\frac12}(z) &= e^{-z/2} z^{k} \Bigg[ 1 + \sum_{n=1}^{\infty} \frac{ \bigl(\tfrac14 - (k-\tfrac12)^2\bigr) \cdots \bigl(\tfrac14 - (k-n+\tfrac12)^2\bigr) }{n! \, z^{n}} \Bigg].
\end{aligned}
$$

Numerical procedure:
- Choose a sufficiently large right‑hand boundary \(z_{\max}\) where the potential is well described by the image tail (e.g. \(z_{\max} = 20\) bohr).
- Evaluate \(\psi_e(z_{\max}) = W_{k,\frac12}(z_{\max})\) and \(\psi_e'(z_{\max})\) using the series (truncated after \(n=8\) terms) and differentiate analytically.
- Use these values as initial conditions for an inward Runge–Kutta integration of the Schrödinger equation toward the surface (\(z\) decreasing from \(z_{\max}\) to a point deep inside the metal, e.g. \(z_{\min} = -10\) bohr).
- Normalise the wavefunction so that the maximum amplitude is of order unity (only relative shapes matter).

### Positron wavefunction (scattering state)
Positron kinetic energy: \(E_p = 1.5\) hartree.

For the scattering state we adopt a plane‑wave incident condition from the vacuum side. Far outside the surface (\(z \to \infty\)) the potential vanishes and the solution is a superposition of incoming and reflected waves:

$$
\psi_p(z) \;\sim\; e^{-i k_p z} + R\,e^{i k_p z}, \qquad k_p = \sqrt{2E_p} = \sqrt{3} \approx 1.732 \; \text{bohr}^{-1}.
$$

Numerical procedure:
- At a large distance \(z_{\max}\) (e.g. \(20\) bohr) set \(\psi_p(z_{\max}) = 1\) and \(\psi_p'(z_{\max}) = -i k_p\) (pure incoming wave, setting any unknown reflection coefficient to zero — the reflection will develop naturally as the integration proceeds).
- Integrate the Schrödinger equation inward using Runge–Kutta down to \(z_{\min}\).
- (Optional) After integration one may re‑normalise the wavefunction; the relative amplitude does not affect the final trend verification.

For both particles use a standard 4th‑order Runge–Kutta method with step size \(\Delta z \approx 0.01\) bohr.

---

## Ps formation matrix element

The dimensionless matrix element for Ps formation (without reciprocal‑lattice sums, after integrating out parallel coordinates) can be written in a simplified one‑dimensional form based on Eqs. (8)–(9) of the paper:

$$
M = \int_{-L}^{z_{\max}} dz_- \, \psi_e(z_-) \, I(z_-),
$$

where

$$
I(z_-) = \int_{-L}^{z_-} dz_+ \, \psi_p(z_+) \, e^{-\alpha\,(z_- - z_+)},
$$

with the kernel decay constant \(\alpha = 1.0\) bohr⁻¹. The integration domain covers the region where the wavefunctions are non‑negligible; choose \(L = 10\) bohr (i.e. integrate from \(-10\) to \(z_{\max} \approx 20\) bohr). The electron wavefunction vanishes deep inside the metal, and the positron wavefunction is oscillatory in the outer region.

The squared magnitude \(|M|^2\) is the score quantity reported as `intensity`.

---

## Reproduction target

Compute \(|M|^2\) for the inverse decay length \(\lambda^{-1}\) taking values:

\[
\lambda^{-1} \in \{1.0,\; 1.2,\; 1.4,\; 1.6,\; 1.8,\; 2.0,\; 2.2,\; 2.4,\; 2.5\}.
\]

For each \(\lambda^{-1}\) compute the intensity under three cases:

| Case       | Electronic \(\lambda^{-1}\) | Positronic \(\lambda^{-1}\) |
|------------|-----------------------------|-----------------------------|
| `electron` | varies                      | fixed at \(1.5\)            |
| `positron` | fixed at \(1.5\)            | varies                      |
| `both`     | varies                      | varies (same value as electronic) |

Use the fixed electron energy \(E_e = -0.375\) hartree and the fixed incident positron kinetic energy \(E_p = 1.5\) hartree for all calculations.

**Required trend:** The variation in \(|M|^2\) (as measured by the range, i.e. max‑min across the \(\lambda^{-1}\) values) must satisfy:

- The range for the `electron` case is larger than the range for the `positron` case.
- The range for the `both` case is larger than the range for the `electron` case.

This reflects the physical result that Ps formation is more sensitive to the electronic surface barrier shape than to the positronic one, and that varying both barriers simultaneously amplifies the effect.

---

## Output file

Write the results to `/app/outputs/ps_formation_intensity.csv`.

### File format
- **Path:** `/app/outputs/ps_formation_intensity.csv`
- **Format:** CSV
- **Header:** `lambda_inv,case,intensity`
- **Columns:**
  - `lambda_inv` — numeric, the value of \(\lambda^{-1}\) (1.0, 1.2, …, 2.5)
  - `case` — string, one of `electron`, `positron`, `both`
  - `intensity` — numeric, the computed \(|M|^2\) (positive, dimensionless)

Each \(\lambda^{-1}\) generates three rows, one per case.

### Output contract (machine‑readable)

```json
{
  "outputs": [
    {
      "file": "ps_formation_intensity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda_inv",
          "case",
          "intensity"
        ],
        "columns": {
          "lambda_inv": {
            "type": "number",
            "description": "Inverse decay length parameter λ⁻¹"
          },
          "case": {
            "type": "string",
            "enum": [
              "electron",
              "positron",
              "both"
            ]
          },
          "intensity": {
            "type": "number",
            "description": "Square magnitude of Ps formation matrix element, dimensionless"
          }
        }
      },
      "description": "The CSV file contains the computed |M|² for each λ⁻¹ value and variation case. The file is audited structurally: the verifier checks that all intensities are physically plausible (positive and within a generous bound) and that the data are internally consistent across the three variation cases."
    }
  ],
  "notes": "The target policy is structural audit; no exact numeric tolerance is applied. The checker will verify the relative ordering of intensity changes across the three cases."
}
```

---

## How you are scored

Your submission is scored by a hidden verifier that reads the output CSV file. The verifier performs the following **structural** checks:

1. All `intensity` values are **positive** and do not exceed a generous upper bound (0.5).
2. The computed **range** of intensity (max − min over the nine \(\lambda^{-1}\) values) satisfies:
   - \(R_{\text{electron}} > R_{\text{positron}}\)
   - \(R_{\text{both}} > R_{\text{electron}}\)

If all checks pass you receive full credit. No exact numerical tolerance is applied; the scoring relies on the relative trends.

---

## Assets available
- NumPy (numpy)
- SciPy (scipy) — provides ODE solvers (`scipy.integrate.solve_ivp`) and special functions, including `scipy.special.whittaker_w` if you prefer to use the built‑in Whittaker W function.

---

## Self‑check before finishing (optional, not scored)

A small script that checks file existence and column names is given below. It does **not** verify scientific correctness.

```python
import csv, os, json

spec = json.load(open("/tests/grading_spec.json"))
contract = spec["output_contract"]["outputs"][0]
path = os.path.join("/app/outputs", os.path.basename(contract["file"]))
if not os.path.isfile(path):
    raise SystemExit("Missing output file")
with open(path, newline="") as f:
    cols = set(next(csv.reader(f)))
required = [c["name"] if isinstance(c, dict) else c for c in contract["schema"]["required_columns"]]
missing = [c for c in required if c not in cols]
if missing:
    raise SystemExit(f"Missing columns: {missing}")
print("Shape OK")
```