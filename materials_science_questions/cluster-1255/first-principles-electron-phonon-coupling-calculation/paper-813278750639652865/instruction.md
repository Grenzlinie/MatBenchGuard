# Self-consistent vertex correction calculation of Stoner factors for five-orbital Hubbard model

## Problem background
In iron-based superconductors, the origin of orbital fluctuations and their role in the structural transition and superconductivity is actively debated. Standard random-phase approximation (RPA) and fluctuation-exchange (FLEX) calculations, which neglect vertex corrections, fail to produce strong orbital fluctuations when realistic Coulomb parameters are used. This work introduces a self-consistent vertex correction (SC-VC) method that includes Maki-Thompson (MT) and Aslamazov-Larkin (AL) diagrams to account for mode-coupling effects beyond RPA. The present task implements this method for a specific five-orbital Hubbard model and computes the charge and spin Stoner factors, which measure the closeness to magnetic and orbital instabilities.

## Approach
The SC-VC method iteratively solves a Dyson-like equation for the charge and spin susceptibility matrices in the orbital basis. Starting from the noninteracting Green's function constructed from a five-orbital tight-binding model, the bare bubble susceptibility is computed. The irreducible susceptibility is formed by adding vertex corrections: the Maki-Thompson (MT) term and the Aslamazov-Larkin (AL) term, where the AL term involves products of two susceptibilities (two-orbiton and two-magnon processes). The self-consistent loop updates the charge and spin susceptibilities using the respective interaction vertices (which depend on intraorbital U, interorbital U', and Hund's J) until convergence. The Stoner factors are extracted as the largest eigenvalues of the product of the interaction vertex and the irreducible susceptibility at zero frequency: alpha_max_s for the spin channel at the wavevector where it is maximal (the nesting vector), alpha_0_c for the charge channel at q=0 (ferro-orbital), and alpha_Q_c for the charge channel at the antiferro-orbital wavevector.

## Reproduction target
Compute the three Stoner factors (alpha_max_s, alpha_0_c, alpha_Q_c) for a specific set of model parameters using the SC-VC method described above. The parameters are: filling n=6.1, temperature T=0.05 eV, intraorbital Coulomb interaction U=1.53 eV, Hund's coupling J such that J/U=0.088, and a 32×32 k-point mesh. Use the five-orbital tight-binding model from Kuroki et al. (PRL 2008). The calculation must include both MT and AL vertex corrections and assume no electron-phonon interaction (g=0). Write the three numbers to a JSON file.

## Assets

- Five-orbital tight-binding model for iron pnictides (Kuroki et al., PRL 2008): 10.1103/PhysRevLett.101.087004
- Python 3: https://www.python.org/
- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: SC-VC calculation and Stoner factors
- Role: scored (load-bearing)
- Action: Implement the self-consistent vertex correction (SC-VC) method for the five-orbital Hubbard model with filling n=6.1, temperature T=0.05 eV, intraorbital interaction U=1.53 eV, Hund’s coupling J such that J/U=0.088, and a 32x32 k-point mesh. Use the tight-binding parameters from the Kuroki et al. model (five-orbital model for iron pnictides). The calculation must include both Maki-Thompson (MT) and Aslamazov-Larkin (AL) vertex corrections for the charge and spin channels, with no electron-phonon interaction (g=0). Run the self-consistent loop until convergence of the charge and spin susceptibility matrices. Compute the three Stoner factors: alpha_max_s, alpha_0_c, alpha_Q_c. Write these three numbers to a JSON file.
- Output file: `/app/outputs/step_01_stoner_factors.json`
- Format: json
- Contract: {"alpha_max_s": float, "alpha_0_c": float, "alpha_Q_c": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stoner_factors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stoner_factors.json
- path: `/app/outputs/step_01_stoner_factors.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The three Stoner factors (spin, ferro‑orbital, and antiferro‑orbital) obtained from the converged SC‑VC calculation.
- schema:
  - `type`: object
  - `required`:
    - `alpha_max_s`: float (dimensionless)
    - `alpha_0_c`: float (dimensionless)
    - `alpha_Q_c`: float (dimensionless)

Notes: All values are dimensionless. The checker compares each submitted value to the paper‑reported reference with an absolute tolerance of 0.02.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stoner_factors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_max_s": "float (dimensionless)",
          "alpha_0_c": "float (dimensionless)",
          "alpha_Q_c": "float (dimensionless)"
        }
      },
      "description": "The three Stoner factors (spin, ferro‑orbital, and antiferro‑orbital) obtained from the converged SC‑VC calculation."
    }
  ],
  "notes": "All values are dimensionless. The checker compares each submitted value to the paper‑reported reference with an absolute tolerance of 0.02."
}
```

## How you are scored
A hidden verifier will read your submitted JSON artifact and compare each Stoner factor (alpha_max_s, alpha_0_c, alpha_Q_c) to a hidden reference value using an appropriate absolute tolerance. Full credit is awarded only if all three values lie within the tolerance. Reporting numbers that happen to match the reference is not sufficient; you must produce them by faithfully implementing the SC-VC method.
