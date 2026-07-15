# DFT Study of Nb Substitution in K-OMS-2 and Its Effect on CO Adsorption

## Problem background
Catalytic oxidation of carbon monoxide (CO) is critical for environmental remediation and clean energy applications. Manganese oxide octahedral molecular sieves (K‑OMS‑2) are promising catalysts, and doping with high‑valent metal cations such as niobium can enhance their activity. However, the atomic‑scale mechanism by which Nb substitution improves CO oxidation is not obvious from experiments alone. Density functional theory (DFT) calculations were performed to investigate the thermodynamic feasibility of Nb incorporation into the K‑OMS‑2 framework and to quantify how the dopant alters the electronic structure and CO adsorption properties of the material.

## Approach
The computational approach uses cluster models built from the crystallographic coordinates of K‑OMS‑2. Two distinct Mn sites (denoted Mn(1) and Mn(2)) are considered for Nb substitution. For each undoped and Nb‑doped model, geometry optimization is performed with DFT using the PW91 exchange‑correlation functional and a double‑numeric polarized (DNP) quality basis set. Substitution energies are obtained from total energy differences of the optimized structures and free atoms. Condensed Fukui functions for nucleophilic attack (f⁻) are computed within the Hirshfeld population analysis to identify the most electrophilic centers. Finally, CO is adsorbed on each metal site (Mn(1), Mn(2), Nb(1), Nb(2)) and additional geometry optimizations yield CO adsorption energies and M–CO bond lengths. The entire workflow is executed for undoped K‑OMS‑2 and two Nb‑doped variants (Nb replacing Mn(1) and Nb replacing Mn(2)).

## Reproduction target
Produce a single JSON file, `/app/outputs/dft_results.json`, that contains all DFT‑derived numerical quantities. Specifically:

- **Substitution energies** for replacing Mn by Nb at the Mn(1) and Mn(2) sites.
- **Condensed Fukui functions f⁻** for nucleophilic attack on K, Mn(1), Mn(2), and Nb in undoped K‑OMS‑2, Nb(1)‑K‑OMS‑2, and Nb(2)‑K‑OMS‑2.
- **CO adsorption energies and M–CO bond lengths** for CO adsorbed on the Mn(1), Mn(2), Nb(1), and Nb(2) sites.

The file must follow the exact JSON schema described in the output contract, with all numeric fields filled using consistent units (kJ mol⁻¹ for energies, Å for bond lengths).

## Assets

- K-OMS-2 crystal structure (Calvert et al. 2008): 10.1021/cm801825g
- DFT code with PW91 functional and DNP basis: quantum-espresso
- PW91 exchange-correlation functional
- Double-numeric polarized (DNP) basis set

## Workflow steps

### Step 1: Build cluster models
- Role: process
- Action: Construct cluster models of undoped K-OMS-2 and Nb-substituted structures (Nb replacing Mn at the two distinct sites) using crystallographic coordinates from the public dataset.
- Evidence: none

### Step 2: Geometry optimization
- Role: process
- Action: Perform geometry optimization of all models (undoped K-OMS-2, Nb(1)-K-OMS-2, Nb(2)-K-OMS-2) using DFT with PW91 functional and a DNP-quality basis. Relax atomic positions until forces converge.
- Evidence: `/app/outputs/geom_opt.log`

### Step 3: Compute substitution energies, Fukui functions, and CO adsorption
- Role: scored (load-bearing)
- Action: Using the optimized geometries: (1) compute total energies and derive substitution energies ΔE = E(Nb-K-OMS-2) + E(Mn) – E(K-OMS-2) – E(Nb) for Nb at Mn(1) and Mn(2); (2) calculate condensed Fukui functions f⁻ for nucleophilic attack on K, Mn(1), Mn(2), and Nb via Hirshfeld population analysis for all models; (3) adsorb CO on each Mn and Nb site, perform additional geometry optimizations, and extract CO adsorption energies and M–CO bond lengths. Output all results in a single JSON file.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: object with keys substitution_energies, fukui_functions, co_adsorption; each an array of objects with required numeric fields as defined in output contract.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: This JSON file collects all DFT-computed numerical results needed to verify the paper's claim that Nb substitution is exothermic and creates strong CO adsorption sites.
- schema:
  - `type`: object
  - `required`: `substitution_energies`, `fukui_functions`, `co_adsorption`
  - `substitution_energies`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `site`, `energy_kJ_mol`
      - `properties`:
        - `site`:
          - `type`: string
          - `enum`: `Mn(1)`, `Mn(2)`
        - `energy_kJ_mol`:
          - `type`: number
  - `fukui_functions`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `material`, `atom`, `f_minus`
      - `properties`:
        - `material`:
          - `type`: string
          - `enum`: `K-OMS-2`, `Nb(1)-K-OMS-2`, `Nb(2)-K-OMS-2`
        - `atom`:
          - `type`: string
          - `enum`: `K`, `Mn(1)`, `Mn(2)`, `Nb`
        - `f_minus`:
          - `type`: number
  - `co_adsorption`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `site`, `bond_length_angstrom`, `adsorption_energy_kJ_mol`
      - `properties`:
        - `site`:
          - `type`: string
          - `enum`: `Mn(1)`, `Mn(2)`, `Nb(1)`, `Nb(2)`
        - `bond_length_angstrom`:
          - `type`: number
        - `adsorption_energy_kJ_mol`:
          - `type`: number

Notes: Scoring uses threshold-or-better for energies (more negative is better) and reference-match with tolerances for Fukui values and bond lengths. Additionally, monotonic trends (e.g., f⁻(Nb) > f⁻(Mn) in Nb(2)-K-OMS-2, CO adsorption energies more negative on Nb than on Mn) must be satisfied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "substitution_energies",
          "fukui_functions",
          "co_adsorption"
        ],
        "substitution_energies": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "site",
              "energy_kJ_mol"
            ],
            "properties": {
              "site": {
                "type": "string",
                "enum": [
                  "Mn(1)",
                  "Mn(2)"
                ]
              },
              "energy_kJ_mol": {
                "type": "number"
              }
            }
          }
        },
        "fukui_functions": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "material",
              "atom",
              "f_minus"
            ],
            "properties": {
              "material": {
                "type": "string",
                "enum": [
                  "K-OMS-2",
                  "Nb(1)-K-OMS-2",
                  "Nb(2)-K-OMS-2"
                ]
              },
              "atom": {
                "type": "string",
                "enum": [
                  "K",
                  "Mn(1)",
                  "Mn(2)",
                  "Nb"
                ]
              },
              "f_minus": {
                "type": "number"
              }
            }
          }
        },
        "co_adsorption": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "site",
              "bond_length_angstrom",
              "adsorption_energy_kJ_mol"
            ],
            "properties": {
              "site": {
                "type": "string",
                "enum": [
                  "Mn(1)",
                  "Mn(2)",
                  "Nb(1)",
                  "Nb(2)"
                ]
              },
              "bond_length_angstrom": {
                "type": "number"
              },
              "adsorption_energy_kJ_mol": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "This JSON file collects all DFT-computed numerical results needed to verify the paper's claim that Nb substitution is exothermic and creates strong CO adsorption sites."
    }
  ],
  "notes": "Scoring uses threshold-or-better for energies (more negative is better) and reference-match with tolerances for Fukui values and bond lengths. Additionally, monotonic trends (e.g., f⁻(Nb) > f⁻(Mn) in Nb(2)-K-OMS-2, CO adsorption energies more negative on Nb than on Mn) must be satisfied."
}
```

## How you are scored
A hidden verifier inspects the contents of `/app/outputs/dft_results.json`. For each reported quantity (substitution energies, Fukui functions, CO adsorption energies, bond lengths) the verifier compares your computed value against reference data using appropriate tolerances. It also enforces qualitative physical trends—for instance, certain Fukui function values should be ordered in a physically meaningful way, and CO adsorption energies on different sites should follow a plausible trend. The final reward is a weighted combination of these per‑item and trend checks. Simply copying numbers from the literature is not sufficient; the verifier expects values derived from the workflow described in the steps above.
