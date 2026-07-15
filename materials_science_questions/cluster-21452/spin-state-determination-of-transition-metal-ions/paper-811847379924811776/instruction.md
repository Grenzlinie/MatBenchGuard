# Crystal Field and Energy Level Calculation for Co2+ in MgF2 Using Exchange Charge Model

## Problem background
Transition metal ions doped into host crystals exhibit electronic structure strongly influenced by the surrounding ligands. When Co2+ substitutes for Mg2+ in the MgF2 crystal, the distorted octahedral environment splits the ion's 3d orbitals, giving rise to a characteristic crystal field. Accurate crystal field parameters are essential to predict the low-lying energy levels and to interpret optical spectra. This reproduction task computes the crystal field parameters for Co2+ in MgF2 using the exchange charge model, which accounts for both electrostatic and covalent contributions from the fluorine ligands.

## Approach
The exchange charge model (ECM) calculates crystal field parameters B_p^k by summing point-charge contributions (from the ligand charges) and exchange-charge contributions (reflecting metal-ligand covalency), derived from the crystal structure of MgF2. Using these parameters together with standard free-ion Racah parameters for Co2+ (electron correlation) and a spin-orbit coupling constant, the full crystal-field Hamiltonian is constructed in the basis of the 3d^7 configuration and diagonalized. The resulting eigenvalues are the energy levels of the impurity ion. The workflow is: (1) obtain the ligand coordinates around the Mg/Co site from the published MgF2 crystal structure, (2) compute the crystal field parameters via ECM, and (3) diagonalize the Hamiltonian including spin-orbit coupling to obtain the low-lying energy levels.

## Reproduction target
Compute the crystal field parameters B_p^k for p = 2, 4 and all allowed k values for Co2+ substituting Mg2+ in MgF2 using the exchange charge model, and compute the low-lying energy levels including spin-orbit coupling. Output the crystal field parameters as a JSON file (cfp.json) and the energy level table as a CSV file (energy_levels.csv). The results should be physically reasonable and obtained from the given structure and free-ion data; the final correctness will be evaluated against hidden reference data.

## Assets

- MgF2 crystal structure (Baur & Khan 1971): 10.1107/S0567740871006076
- Free-ion Racah parameters for Co2+

## Workflow steps

### Step 1: Prepare crystal structure
- Role: process
- Action: Obtain the MgF2 crystallographic data (lattice constants a=4.6213 Å, c=3.0159 Å, space group P42/mnm) and determine the six fluorine ligand positions around the substituted Mg/Co site at the distorted octahedron of D2h symmetry. Record the coordinates.
- Evidence: `/app/outputs/ligand_coordinates.json`

### Step 2: Compute crystal field parameters B_p^k using ECM
- Role: scored
- Action: Implement the Exchange Charge Model (ECM) to compute the crystal field parameters B_p^k for p=2,4 and all k (k=-p..p) for Co2+ in MgF2. Use the structural data from step 1 and the ECM formalism (point-charge and exchange-charge contributions). Output the parameters in cm⁻¹ as a JSON file.
- Output file: `/app/outputs/cfp.json`
- Format: json
- Contract: JSON object with string keys of the form 'B_p_k' (e.g. B_2_0, B_2_1, B_4_m4) and numeric values in cm⁻¹.
- Scoring: scored by hidden verifier

### Step 3: Calculate energy levels including spin-orbit coupling
- Role: scored (load-bearing)
- Action: Using the computed CFP, free-ion Racah parameters B and C for Co2+ (approximately B~1115 cm⁻¹, C~5120 cm⁻¹) and spin-orbit coupling constant ξ=520 cm⁻¹, diagonalize the full crystal-field Hamiltonian to obtain low-lying energy levels. Output a table with term labels and computed energies in cm⁻¹.
- Output file: `/app/outputs/energy_levels.csv`
- Format: csv
- Contract: CSV with columns: term_label (string), computed_energy_cm1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cfp.json`
- `/app/outputs/energy_levels.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cfp.json
- path: `/app/outputs/cfp.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Crystal field parameters for Co2+ in MgF2 computed with the Exchange Charge Model.
- schema:
  - `type`: object
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`: object
  - `description`: Keys: 'B_p_k' for p=2,4 and k=-p..p, e.g. 'B_2_0', 'B_4_m4'. Values: float (cm⁻¹). All independent parameters for D2h symmetry must be present.

### energy_levels.csv
- path: `/app/outputs/energy_levels.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed energy levels (in cm⁻¹) for the lowest terms of Co2+ in MgF2, including spin-orbit coupling.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `term_label`, `computed_energy_cm1`
  - `units`:
    - `computed_energy_cm1`: cm⁻¹

Notes: The checker compares cfp.json to the paper's reported CFP values with appropriate per-parameter tolerances. energy_levels.csv is scored by computing the RMS deviation from hidden experimental reference energies; full credit for RMS ≤500 cm⁻¹, degrading for larger deviations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cfp.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {},
        "description": "Keys: 'B_p_k' for p=2,4 and k=-p..p, e.g. 'B_2_0', 'B_4_m4'. Values: float (cm⁻¹). All independent parameters for D2h symmetry must be present."
      },
      "description": "Crystal field parameters for Co2+ in MgF2 computed with the Exchange Charge Model."
    },
    {
      "file": "energy_levels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "term_label",
          "computed_energy_cm1"
        ],
        "units": {
          "computed_energy_cm1": "cm⁻¹"
        }
      },
      "description": "Computed energy levels (in cm⁻¹) for the lowest terms of Co2+ in MgF2, including spin-orbit coupling."
    }
  ],
  "notes": "The checker compares cfp.json to the paper's reported CFP values with appropriate per-parameter tolerances. energy_levels.csv is scored by computing the RMS deviation from hidden experimental reference energies; full credit for RMS ≤500 cm⁻¹, degrading for larger deviations."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. The cfp.json crystal field parameters are compared against reference values with appropriate per-parameter tolerances. The energy_levels.csv table is compared against experimental energy levels to assess overall agreement (e.g., via an RMS deviation). The scores from these two artifacts are combined by weight to produce your final reward. You must compute the outputs from the crystal structure and the ECM theory; simply copying or guessing known numbers will not pass the verification checks.
