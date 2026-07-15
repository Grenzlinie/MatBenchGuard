# Equilibrium fluid distribution in porous media via interfacial energy minimization

## Problem background
In multiphase porous media, the equilibrium distribution of fluid phases (e.g., liquid water and water vapor) is governed by the minimization of total interfacial free energy. Accurately predicting this distribution is important for modeling rock physics properties because the microscopic arrangement of fluids strongly influences transport and geophysical measurements. The challenge is to compute an energy-minimizing configuration of liquid and vapor in a discretized pore space, given known interfacial energy parameters.

## Approach
The model represents a 2D pore space as a grid of solid and pore elements. Three numerical methods are used to search for the configuration that minimizes the total interfacial free energy G^s_t = Σ A_i γ_i, considering nearest and next-nearest neighbors. Method 1 starts with all pore elements as vapor and sequentially converts the element whose change yields the largest energy drop to liquid until the target water saturation S_w is reached. Method 2 starts with all liquid and converts to vapor similarly. Method 3 is a simulated annealing procedure that randomly exchanges liquid and vapor elements, accepting or rejecting exchanges based on a Metropolis criterion with a cooling schedule, to find a low-energy configuration for a fixed S_w. For each method, the total interfacial free energy is computed at saturations from 0.0 to 1.0. The output is normalized such that G^s_t at S_w=0.0 equals 1.000 and at S_w=1.0 equals 0.000.

## Reproduction target
For the synthetic 2D pore space model (a 20×12 binary grid provided below, with solid=1, pore=0) and the given interfacial energies (γ_SV=422 mJ/m², γ_SL=350 mJ/m², γ_LV=72 mJ/m²), compute the normalized total interfacial free energy as a function of water saturation S_w for each of the three methods. Produce a CSV file with columns: S_w, method_1_normalized, method_2_normalized, method_3_normalized, for S_w ranging from 0.0 to 1.0 in increments no larger than 0.1 (recommended 0.05). The normalized energies must satisfy the endpoint condition exactly: G^s_t(S_w=0.0)=1.000, G^s_t(S_w=1.0)=0.000. The resulting CSV is the primary scored artifact.

## Assets

- 2D synthetic pore space model (Figure 6)
- Interfacial free energy values

## Workflow steps

### Step 1: Run three fluid distribution methods and output normalized energy table
- Role: scored (load-bearing)
- Action: Implement Methods 1, 2, and 3 (simulated annealing) as described in the paper's approach. Use the provided 2D pore model and surface energy values. For each water saturation S_w from 0.0 to 1.0 in steps no larger than 0.1 (recommended 0.05), compute the total interfacial free energy G^s_t for each method. Normalize the energies so that G^s_t(S_w=0.0)=1.000 and G^s_t(S_w=1.0)=0.000. Write a CSV file with columns: S_w, method_1_normalized, method_2_normalized, method_3_normalized, including at least the rows from 0.0 to 1.0.
- Output file: `/app/outputs/energy_table.csv`
- Format: csv
- Contract: Columns: S_w (float, 0.0 to 1.0), method_1_normalized (float), method_2_normalized (float), method_3_normalized (float). Normalization: G^s_t at S_w=0 equals exactly 1.000, at S_w=1 equals exactly 0.000.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_table.csv
- path: `/app/outputs/energy_table.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized total interfacial free energy G^s_t versus water saturation for the three numerical methods. The hidden checker verifies structural properties: exact endpoints (0.0=1.000, 1.0=0.000), that method_3_normalized is the lowest at every intermediate saturation, and that method_1_normalized shows a metastable peak at intermediate saturations.
- schema:
  - `type`: table
  - `required_columns`: `S_w`, `method_1_normalized`, `method_2_normalized`, `method_3_normalized`
  - `units`:
    - `S_w`: dimensionless (fraction)
    - `method_1_normalized`: dimensionless
    - `method_2_normalized`: dimensionless
    - `method_3_normalized`: dimensionless

Notes: The hidden checker assesses ordering, peak presence, and normalization endpoints. No comparison to gold reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "S_w",
          "method_1_normalized",
          "method_2_normalized",
          "method_3_normalized"
        ],
        "units": {
          "S_w": "dimensionless (fraction)",
          "method_1_normalized": "dimensionless",
          "method_2_normalized": "dimensionless",
          "method_3_normalized": "dimensionless"
        }
      },
      "description": "Normalized total interfacial free energy G^s_t versus water saturation for the three numerical methods. The hidden checker verifies structural properties: exact endpoints (0.0=1.000, 1.0=0.000), that method_3_normalized is the lowest at every intermediate saturation, and that method_1_normalized shows a metastable peak at intermediate saturations."
    }
  ],
  "notes": "The hidden checker assesses ordering, peak presence, and normalization endpoints. No comparison to gold reference values."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored workflow stage and combine them by weight into a final reward. For the energy table, the verifier checks that the file is correctly formatted, that the endpoint values are exactly 1.000 and 0.000, that method_3_normalized is the lowest at every intermediate saturation, and that method_1_normalized shows a metastable peak at intermediate saturations. The verifier may also verify structural consistency, such as the relative ordering of the three methods across the saturation range. Reproducing these structural properties is required to obtain full credit; merely reporting arbitrary numbers will not pass.
