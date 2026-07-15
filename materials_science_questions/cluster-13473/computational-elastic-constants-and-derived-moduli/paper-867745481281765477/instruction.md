# Computational Elastic Constants and Derived Moduli

## Problem background
Neutron star crusts are solid Coulomb crystals of ions immersed in a degenerate electron gas. Torsional oscillations observed during magnetar giant flares depend sensitively on the crustal shear modulus, which is determined by the elastic constants of the crystalline lattice. Electron screening of the ion‑ion Coulomb interaction modifies the shear modulus relative to the unscreened case. This task requires computing the effective angle‑averaged shear modulus of a body‑centered‑cubic (bcc) Coulomb crystal, using molecular dynamics simulations with a screened potential.

## Approach
The ions interact via a screened Coulomb potential $v(r) = (Z^2 e^2/r) \exp(-r/\lambda_e)$, where $\lambda_e$ is the electron screening length. The system is characterized by the Coulomb parameter $\Gamma = Z^2 e^2/(a T)$, with $a$ the ion‑sphere radius. At zero temperature a perfect bcc lattice is used to compute the elastic constants $b_{11}$ and $c_{44}$ from the second derivatives of the total potential energy with respect to six volume‑conserving deformations. At finite temperatures molecular dynamics simulations are performed, and the same deformations are applied to thermally sampled configurations; the strain‑response expectation values are evaluated using the fluctuation formula to obtain $b_{11}$ and $c_{44}$. The effective angle‑averaged shear modulus is then $\mu_{\mathrm{eff}} = (2 b_{11} + 3 c_{44}) / 5$, expressed in units of $n Z^2 e^2 / a$.

## Reproduction target
Produce a CSV file (`mueff_table.csv`) containing the elastic constants and effective shear modulus for three thermodynamic states: (a) zero temperature ($\Gamma = \infty$), (b) $\Gamma = 834$, and (c) $\Gamma = 200$. Each row must report the Coulomb parameter Gamma, the elastic constants $b_{11}$ and $c_{44}$, the effective shear modulus $\mu_{\mathrm{eff}}$, and the statistical uncertainty of $\mu_{\mathrm{eff}}$. The zero‑temperature values are obtained from the perfect lattice; the finite‑temperature values are derived from the MD trajectories as described in the workflow steps.

## Assets

- Molecular dynamics simulator (e.g., LAMMPS)
- Python with NumPy: numpy

## Workflow steps

### Step 1: Zero-temperature elastic constants
- Role: process
- Action: For a perfect bcc lattice with the given screened Coulomb pair potential and density, apply six volume-conserving strains defined as follows (all off-diagonal components not listed are zero):
  D1: u_xx = ε + (3/4)ε², u_yy = −ε/2, u_zz = −ε/2
  D2: u_yy = ε + (3/4)ε², u_xx = −ε/2, u_zz = −ε/2
  D3: u_zz = ε + (3/4)ε², u_xx = −ε/2, u_yy = −ε/2
  D4: u_xy = u_yx = ε/2, u_zz = ε²/4
  D5: u_yz = u_zy = ε/2, u_xx = ε²/4
  D6: u_zx = u_xz = ε/2, u_yy = ε²/4
For each deformation m, compute the total potential energy V_tot by summing the screened Coulomb pair potential over all ion pairs within the 27 nearest periodic images. Use a five-point finite-difference formula to evaluate the second derivative d²V_tot/dε² at ε=0. At zero temperature the strain-response expectation value is f_m = (d²V_tot/dε²)/V, where V is the system volume. For a bcc lattice, f1 = f2 = f3 = 3b11 and f4 = f5 = f6 = c44; therefore b11 = (f1+f2+f3)/9 and c44 = (f4+f5+f6)/3. Determine b11 and c44 and save the values for later merging.
- Evidence: `/app/outputs/zero_T_elastic.json`

### Step 2: Finite-temperature MD simulations
- Role: process
- Action: Perform molecular dynamics simulations for N=3456 ions at the given density using the same screened potential. Start from a perfect bcc lattice, raise the temperature to 0.1 MeV (corresponding to Γ≈834) and later to the temperature that yields Γ=200. At each state point, equilibrate for 2.5×10^6 fm/c and then sample for 6.25×10^6 fm/c, storing ion configurations at regular intervals. Use velocity-Verlet integration with δt=25 fm/c and periodic boundary conditions; interactions during dynamics may use only the nearest periodic image, but the stored configurations will later be analysed with 27-image sums.
- Evidence: none

### Step 3: Compile effective shear modulus table
- Role: scored (load-bearing)
- Action: From the stored finite-temperature configurations and the zero-temperature result, apply the six volume-conserving deformations (D1–D6 as defined above: D1: u_xx = ε + 3/4 ε², u_yy = u_zz = −ε/2; D2: u_yy = ε + 3/4 ε², u_xx = u_zz = −ε/2; D3: u_zz = ε + 3/4 ε², u_xx = u_yy = −ε/2; D4: u_xy = u_yx = ε/2, u_zz = ε²/4; D5: u_yz = u_zy = ε/2, u_xx = ε²/4; D6: u_zx = u_xz = ε/2, u_yy = ε²/4) to each sampled configuration. Compute the total potential energy and its first and second numerical derivatives with respect to strain (five-point formula, summing over 27 periodic images). Evaluate the strain-response expectation values using the fluctuation formula f_m = (1/V){ ⟨d²V_tot/dε²⟩ − (1/T)[⟨(dV_tot/dε)²⟩ − ⟨dV_tot/dε⟩²] }. Because f1 = f2 = f3 = 3b11 and f4 = f5 = f6 = c44, average the six values to obtain b11 = (f1+f2+f3)/9 and c44 = (f4+f5+f6)/3. Calculate μ_eff = (2b11+3c44)/5 and its statistical uncertainty from the ensemble spread. Combine the results for Γ=∞ (zero-T), Γ=834, and Γ=200 into a single CSV file.
- Output file: `/app/outputs/mueff_table.csv`
- Format: csv
- Contract: Columns: Gamma (string: 'inf' or integer), b11 (float, units nZ²e²/a), c44 (float, units nZ²e²/a), mueff (float, units nZ²e²/a), uncertainty_mueff (float, units nZ²e²/a). One row per Gamma.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mueff_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mueff_table.csv
- path: `/app/outputs/mueff_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of effective shear modulus and its uncertainty for three Coulomb parameters: Γ=∞ (zero-T), Γ=834, and Γ=200.
- schema:
  - `type`: table
  - `required_columns`: `Gamma`, `b11`, `c44`, `mueff`, `uncertainty_mueff`
  - `units`:
    - `b11`: nZ^2e^2/a
    - `c44`: nZ^2e^2/a
    - `mueff`: nZ^2e^2/a
    - `uncertainty_mueff`: nZ^2e^2/a

Notes: The zero-temperature baseline and MD trajectory generation are required process steps. The scored output is the final CSV; its values are compared to hidden reference values within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mueff_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Gamma",
          "b11",
          "c44",
          "mueff",
          "uncertainty_mueff"
        ],
        "units": {
          "b11": "nZ^2e^2/a",
          "c44": "nZ^2e^2/a",
          "mueff": "nZ^2e^2/a",
          "uncertainty_mueff": "nZ^2e^2/a"
        }
      },
      "description": "Table of effective shear modulus and its uncertainty for three Coulomb parameters: Γ=∞ (zero-T), Γ=834, and Γ=200."
    }
  ],
  "notes": "The zero-temperature baseline and MD trajectory generation are required process steps. The scored output is the final CSV; its values are compared to hidden reference values within appropriate tolerances."
}
```

## How you are scored
A hidden verifier inspects the artifacts you produce. Each workflow step is scored independently, and the overall score is a weighted combination. The main scored artifact is the final CSV file; its effective shear modulus values and uncertainties are compared to reference results using tolerances that account for implementation spread. The process steps (zero‑temperature elastic constants and MD trajectory generation) are also checked for completeness but carry smaller weight. The verifier reports a single reward between 0 and 1.
