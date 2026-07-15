# Crystal Stability Comparison via Energy/Elastic Analysis

## Problem background
Transition metal stacking-fault energies are a key signature of structural stability but cannot be adequately described by conventional second-order pseudopotential theory because of the large scattering strength of d electrons. Extending the theory to third order incorporates three-ion interactions, which may dominate and explain observed trends across transition-metal series. This task asks you to implement a resonant-scattering multi-ion interaction model and compute the intrinsic stacking-fault energy γ for fcc crystals as a function of total valence Z. The result will reveal whether the three-ion terms dominate and whether the computed energy follows the expected structural trends.

## Approach
The total stacking-fault energy γ is modelled as the sum of a pairwise (second-order) contribution γ₂ and a three-ion (third-order) contribution γ₃. γ₂ is obtained from an asymptotic approximation based on Blandin et al.’s interplanar potential formalism; γ₃ is evaluated by summing the energies of all distinct three-ion diagrams that meet a truncation criterion. The electron-ion scattering is described by a simple resonant model: the d-electron resonance is parameterised by a fixed resonance energy and width; non-resonant scattering is treated with an empty-core pseudopotential having a known core radius. The Fermi energy for each valence Z is read from published tabulated data. To bracket the uncertainty in the non-resonant channel, the calculation is performed for two choices of effective nonresonant valence, Z_s = 1 and Z_s = 2. The nearest-neighbor distance, crystal structure, and truncation parameters are held constant across all valences, making the model a minimal parameterisation that isolates the effect of resonant scattering.

## Reproduction target
Your job is to implement this workflow and produce one CSV file, /app/outputs/stacking_fault_energies.csv, containing for each integer valence Z from 4 to 11 and for Z_s = 1 and Z_s = 2 the columns: Z, Z_s, gamma_total (Ry), gamma_2 (Ry), gamma_3 (Ry), where gamma_total = γ₂ + γ₃. The intermediate results (scattering data, γ₂, γ₃) should be written as evidence as specified in the steps. The checker will evaluate the CSV against a set of hidden structural scoring rules that capture the physically expected behaviour of the model—such as the sign of γ at key valence values, the monotonic trend across the series, and the relative dominance of the three-ion term. Exact numerical agreement with any particular implementation is not required; the task rewards a solution whose computed γ exhibits the correct structural physics.

## Assets

- NumPy: numpy
- SciPy: scipy
- Pettifor E_F - E_r values: 10.1088/0022-3719/3/2/014
- Ashcroft-Langreth empty-core radius for Cu

## Workflow steps

### Step 1: Compute scattering phase shifts and amplitude
- Role: process
- Action: For each total valence Z (4..11) and each nonresonant valence Z_s (1,2), compute resonant (l=2) and non-resonant scattering phase shifts using the Pettifor resonance model (E_r=0.33 Ry, Δ=0.014 Ry) and an empty-core pseudopotential with Ashcroft-Langreth radius for copper (r_c ≈ 1.01 a.u.). Derive the scattering amplitude f(E,π) as a function of electron energy up to the Fermi energy E_F (determined from Pettifor’s tabulated E_F-E_r).
- Evidence: `/app/outputs/scattering_data.json`

### Step 2: Compute pairwise stacking fault energy γ₂
- Role: process
- Action: Using the scattering amplitudes, compute the pairwise (second-order) contribution γ₂ to the intrinsic stacking fault energy via the asymptotic approximation formula combined with Blandin et al. interplanar potential formalism. Evaluate for the fcc crystal with nearest-neighbor distance 5.0 a.u. Obtain γ₂ as a function of Z for both Z_s values.
- Evidence: `/app/outputs/gamma2.json`

### Step 3: Compute three-ion stacking fault energy γ₃
- Role: process
- Action: Construct all distinct three-ion diagrams that satisfy the truncation criteria (at least two ions are nearest neighbors, third ion in adjacent or next-nearest plane, α ≤ 30° or R ≤ 20 a.u.). For each diagram geometry evaluate the three-ion energy v₃ (from the multi-ion formulation) for faulted and perfect fcc configurations and multiply by diagram weights N_i^F, N_i^P. Sum over all geometries to obtain γ₃ for each Z and Z_s.
- Evidence: `/app/outputs/gamma3.json`

### Step 4: Assemble and output total stacking fault energy
- Role: scored (load-bearing)
- Action: For each Z (4..11) and Z_s (1,2), compute gamma_total = γ₂ + γ₃. Write one row per (Z, Z_s) with columns Z, Z_s, gamma_total (Ry), gamma_2 (Ry), gamma_3 (Ry) to /app/outputs/stacking_fault_energies.csv.
- Output file: `/app/outputs/stacking_fault_energies.csv`
- Format: csv
- Contract: Columns: Z (int), Z_s (int), gamma_total (float, Ry), gamma_2 (float, Ry), gamma_3 (float, Ry)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stacking_fault_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stacking_fault_energies.csv
- path: `/app/outputs/stacking_fault_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing computed intrinsic stacking fault energies for fcc crystals over Z=4..11 for Z_s=1 and Z_s=2.
- schema:
  - `type`: table
  - `required_columns`: `Z`, `Z_s`, `gamma_total`, `gamma_2`, `gamma_3`
  - `units`:
    - `gamma_total`: Ry
    - `gamma_2`: Ry
    - `gamma_3`: Ry

Notes: The hidden checker will read this file and verify (i) sign pattern at key Z values (positive for Z>9, negative for 6<Z<9, negative near Z=4 for Z_s=1 and positive near Z=4 for Z_s=2), (ii) overall monotonic increase of gamma_total with Z, and (iii) dominance of three-ion term |gamma_3| >> |gamma_2| for most Z, as described in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stacking_fault_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Z",
          "Z_s",
          "gamma_total",
          "gamma_2",
          "gamma_3"
        ],
        "units": {
          "gamma_total": "Ry",
          "gamma_2": "Ry",
          "gamma_3": "Ry"
        }
      },
      "description": "CSV file containing computed intrinsic stacking fault energies for fcc crystals over Z=4..11 for Z_s=1 and Z_s=2."
    }
  ],
  "notes": "The hidden checker will read this file and verify (i) sign pattern at key Z values (positive for Z>9, negative for 6<Z<9, negative near Z=4 for Z_s=1 and positive near Z=4 for Z_s=2), (ii) overall monotonic increase of gamma_total with Z, and (iii) dominance of three-ion term |gamma_3| >> |gamma_2| for most Z, as described in the paper."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/stacking_fault_energies.csv and apply several independent structural checks derived from the underlying physics. Each check contributes a weight to a total reward between 0 and 1. The verifier does NOT require bitwise reproduction of a reference table; instead it assesses whether your computed γ satisfies the directional trends, sign patterns, and component-size relationships that a correct implementation of the model must produce. No intermediate checks (scattering data, γ₂, γ₃) are directly scored, but their presence as specified evidence is expected. The final reward combines the scores of all structural checks; a solution that shows the correct physical trends will earn full credit.
