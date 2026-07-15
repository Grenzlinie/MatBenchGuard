# Calculate Ground- and Excited-State Dipole Moments of DMPI via Solvatochromic Analysis and TDDFT

## Problem background
The green fluorescent protein (GFP) luminophore is responsible for the strong fluorescence of GFP. An analog of this luminophore, molecule DMPI, shows solvent-dependent fluorescence properties that could shed light on the excited-state relaxation mechanism. The key question is whether DMPI undergoes twisted intramolecular charge transfer (TICT) via single-bond rotation or a hula‑twist mechanism. By analyzing the shift of absorption and emission spectra in different solvents (solvatochromism) and performing quantum chemical calculations, one can extract ground‑ and excited‑state dipole moments that help characterize the nature of the excited state. Your goal is to compute these dipole moments from the provided experimental data and from first-principles calculations.

## Approach
The work uses two complementary methods to determine dipole moments. The first method is a solvatochromic analysis based on the Onsager cavity model. Given the absorption and emission wavenumbers of DMPI in a series of solvents, along with solvent polarity functions f(ε,n) and f(ε,n)+2g(n), you perform linear regression of the Stokes shift vs. f(ε,n) and of the sum of absorption and emission wavenumbers vs. f(ε,n)+2g(n). The slopes obtained, together with an Onsager cavity radius (half the distance between the dimethylamine nitrogen and carbonyl oxygen atoms), give the ground-state dipole (μg), excited-state dipole (μe), and their difference (Δμ) via the Onsager equations. The second method is a direct quantum‑mechanical computation: optimize the geometry of DMPI at the B3LYP/6-31G(d) level and run a time‑dependent DFT (TDDFT) calculation to obtain the excited‑state dipole moment in vacuum. Both results are then combined into a single output.

## Reproduction target
Compute and report the following four quantities as a JSON object:
- μg: ground-state dipole moment (Debye) from solvatochromic analysis
- μe: excited-state dipole moment (Debye) from solvatochromic analysis
- Δμ: = μe − μg (Debye)
- μe_tddft: excited-state dipole moment (Debye) from the TDDFT calculation in vacuum.
You must use the provided solvatochromic data file and the initial molecular structure, perform the regression and the TDDFT calculation, and write the result to `/app/outputs/dipole_moments.json`.

## Assets

- solvatochromic_data.csv
- dmpi.xyz
- PySCF: https://github.com/pyscf/pyscf

## Workflow steps

### Step 1: Solvatochromic dipole analysis
- Role: process
- Action: Load the solvatochromic data from solvatochromic_data.csv. Perform linear regression of Stokes shift (ν_a - ν_f) vs. solvent polarity function f(ε,n) to obtain slope m1, and of (ν_a + ν_f) vs. f(ε,n)+2g(n) to obtain slope m2. Compute the Onsager cavity radius a (half the distance between the dimethylamine nitrogen and carbonyl oxygen atoms of DMPI). Apply the Onsager cavity method to calculate the ground-state dipole moment μ_g, excited-state dipole moment μ_e, and the change Δμ = μ_e - μ_g. Save these three values in an intermediate JSON file.
- Evidence: `/app/outputs/solvatochromic_dipoles.json`

### Step 2: TDDFT excited-state dipole calculation
- Role: process
- Action: Optimize the geometry of DMPI from dmpi.xyz at the B3LYP/6-31G(d) level using PySCF (or equivalent open-source package). Perform a TDDFT calculation to obtain the excited-state dipole moment in vacuum. Save the result in an intermediate JSON file.
- Evidence: `/app/outputs/tddft_dipole.json`

### Step 3: Compile final dipole moments
- Role: scored
- Action: Read the intermediate results from solvatochromic_dipoles.json and tddft_dipole.json. Write a single JSON file containing the four quantities: mu_g, mu_e, delta_mu, and mu_e_tddft.
- Output file: `/app/outputs/dipole_moments.json`
- Format: json
- Contract: {"mu_g": <float>, "mu_e": <float>, "delta_mu": <float>, "mu_e_tddft": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_moments.json
- path: `/app/outputs/dipole_moments.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Combined dipole moments: mu_g (ground-state), mu_e (excited-state from solvatochromism), delta_mu (change), mu_e_tddft (TDDFT excited-state).
- schema:
  - `type`: object
  - `required`:
    - `mu_g`: float
    - `mu_e`: float
    - `delta_mu`: float
    - `mu_e_tddft`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `mu_g`: Debye
    - `mu_e`: Debye
    - `delta_mu`: Debye
    - `mu_e_tddft`: Debye

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "mu_g": "float",
          "mu_e": "float",
          "delta_mu": "float",
          "mu_e_tddft": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "mu_g": "Debye",
          "mu_e": "Debye",
          "delta_mu": "Debye",
          "mu_e_tddft": "Debye"
        }
      },
      "description": "Combined dipole moments: mu_g (ground-state), mu_e (excited-state from solvatochromism), delta_mu (change), mu_e_tddft (TDDFT excited-state)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted `dipole_moments.json` is evaluated by a hidden verifier. The verifier compares each of the four dipole values to a hidden reference (the paper-reported results) with predetermined tolerances. You earn partial credit for each value that falls within its tolerance; full credit requires all four to be within tolerance. Only the numeric values in the JSON are scored; intermediate files are not directly rewarded but are required for the workflow. The final reward is a float between 0 and 1, computed as the average of the individual per-value scores.
