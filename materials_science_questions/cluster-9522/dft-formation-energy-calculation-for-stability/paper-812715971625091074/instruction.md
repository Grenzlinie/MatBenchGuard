# DFT Formation Energy and ORR Overpotential Computation for FeNx Active Sites

## Problem background
Fe–N–C catalysts with atomically dispersed FeN_x active sites are promising non‑precious metal catalysts for the oxygen reduction reaction (ORR). The coordination number x of the nitrogen atoms around the iron centre can strongly influence the stability of the active site and its catalytic activity. While FeN_4 sites are commonly studied, a systematic computational investigation of the formation energies and ORR overpotentials for the full series FeN_x (x = 1–5) is essential to understand the structure–function relationship. This task requires you to compute, from first‑principles density functional theory (DFT), the formation energies of FeN_x models embedded in a graphene support and the ORR overpotentials on these sites, following the computational protocol established in the field.

## Approach
Using spin‑polarised DFT with a plane‑wave pseudopotential code (e.g., Quantum ESPRESSO), construct atomic models of FeN_x (x = 1,…,5) active sites by substituting carbon atoms with nitrogen atoms around an iron centre in a graphene supercell. Compute the ground‑state total energies of each FeN_x model, as well as reference total energies for pristine graphene, an isolated N₂ molecule, and bulk bcc Fe. From these, calculate the formation energy of each FeN_x site as the energy difference between the FeN_x system and the reference phases, adjusted for the number of atoms of each species. For ORR activity, determine the adsorption free energies of the reaction intermediates O*, OH*, and OOH* on each relaxed FeN_x site, applying the computational hydrogen electrode (CHE) model with standard free‑energy corrections. Build the four‑electron ORR free‑energy diagram and extract the overpotential for each coordination number. Write the final formation energies and overpotentials to CSV files as specified in the workflow steps.

## Reproduction target
Produce two CSV files under `/app/outputs`: `step_01_formation_energies.csv` and `step_02_orr_overpotentials.csv`. `step_01_formation_energies.csv` must contain, for each coordination number from 1 to 5, the computed formation energy in eV (columns: `coordination_number` (int) and `formation_energy_eV` (float)). `step_02_orr_overpotentials.csv` must contain, for each coordination number from 1 to 5, the computed ORR overpotential in V (columns: `coordination_number` (int) and `overpotential_V` (float)).

## Assets

- Quantum ESPRESSO (DFT package): https://www.quantum-espresso.org/download
- SSSP pseudopotentials (efficiency library): https://www.quantum-espresso.org/pseudopotentials/sssp
- Python 3 with numpy, scipy, pandas: python3 -m pip install numpy scipy pandas

## Workflow steps

### Step 1: FeNx structural model construction
- Role: process
- Action: Start from a graphene supercell, create carbon vacancies and substitute nitrogen atoms around an Fe centre to form FeN_x configurations (x=1..5); relax the initial geometries. Output relaxed geometry files for subsequent DFT steps.
- Evidence: `/app/outputs/fe_nx_models.xyz`

### Step 2: DFT reference calculations
- Role: process
- Action: Perform spin-polarized DFT total energy calculations for reference phases: pristine graphene, N2 molecule, and bulk Fe (bcc) using the same computational setup as for FeN_x models.
- Evidence: none

### Step 3: DFT total energies of FeNx
- Role: process
- Action: For each FeN_x model (x=1..5), perform spin-polarized DFT geometry optimization and compute the ground-state total energy.
- Evidence: none

### Step 4: Formation energy calculation
- Role: scored (load-bearing)
- Action: Calculate formation energies for each FeN_x (x=1..5) using the total energies from previous steps and reference chemical potentials derived from the reference calculations. Write the results to /app/outputs/step_01_formation_energies.csv.
- Output file: `/app/outputs/step_01_formation_energies.csv`
- Format: csv
- Contract: coordination_number (int), formation_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 5: ORR intermediate adsorption energies
- Role: process
- Action: Compute total energies of ORR intermediates (O*, OH*, OOH*) adsorbed on each relaxed FeN_x model (x=1..5). Derive adsorption free energies including zero-point energy and entropy corrections using the computational hydrogen electrode (CHE) approach with standard references (H2, H2O).
- Evidence: none

### Step 6: ORR overpotential evaluation
- Role: scored
- Action: Construct ORR free energy diagrams for the 4-electron pathway on each FeN_x (x=1..5) using the adsorption free energies from the previous step. Determine the overpotential for each coordination number and write the values to /app/outputs/step_02_orr_overpotentials.csv.
- Output file: `/app/outputs/step_02_orr_overpotentials.csv`
- Format: csv
- Contract: coordination_number (int), overpotential_V (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.csv`
- `/app/outputs/step_02_orr_overpotentials.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.csv
- path: `/app/outputs/step_01_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies of FeN_x (x=1..5) computed from DFT total energies. The hidden checker compares each value to paper-reported reference values and verifies that FeN4 is the minimum (inverted volcano).
- schema:
  - `type`: table
  - `required_columns`: `coordination_number`, `formation_energy_eV`
  - `units`:
    - `coordination_number`: dimensionless integer
    - `formation_energy_eV`: eV

### step_02_orr_overpotentials.csv
- path: `/app/outputs/step_02_orr_overpotentials.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: ORR overpotentials of FeN_x (x=1..5) computed from free energy diagrams. The hidden checker compares each value to paper-reported reference values and verifies that FeN4 has the lowest overpotential (volcano trend).
- schema:
  - `type`: table
  - `required_columns`: `coordination_number`, `overpotential_V`
  - `units`:
    - `coordination_number`: dimensionless integer
    - `overpotential_V`: V

Notes: The contract requires exactly one row per coordination number x=1..5 in each file. The checker will also verify the inverted volcano trend in formation energies and the volcano trend in overpotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coordination_number",
          "formation_energy_eV"
        ],
        "units": {
          "coordination_number": "dimensionless integer",
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energies of FeN_x (x=1..5) computed from DFT total energies. The hidden checker compares each value to paper-reported reference values and verifies that FeN4 is the minimum (inverted volcano)."
    },
    {
      "file": "step_02_orr_overpotentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coordination_number",
          "overpotential_V"
        ],
        "units": {
          "coordination_number": "dimensionless integer",
          "overpotential_V": "V"
        }
      },
      "description": "ORR overpotentials of FeN_x (x=1..5) computed from free energy diagrams. The hidden checker compares each value to paper-reported reference values and verifies that FeN4 has the lowest overpotential (volcano trend)."
    }
  ],
  "notes": "The contract requires exactly one row per coordination number x=1..5 in each file. The checker will also verify the inverted volcano trend in formation energies and the volcano trend in overpotentials."
}
```

## How you are scored
A hidden verifier will read your two CSV files and compare the values you report to reference DFT values computed with a consistent protocol (the reference values are not disclosed). For each coordination number, the verifier checks that your formation energy and overpotential lie within a tolerance of the reference. In addition, the verifier checks that the set of values across the five coordination numbers satisfies the expected structural trends (e.g., a specific coordination number should give the minimum formation energy and the minimum overpotential). Your final reward is the weighted sum of scores from the two artifacts; reporting the paper’s numbers without performing the required DFT calculations will not produce the correct trends and will be penalised.
