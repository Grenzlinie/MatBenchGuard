# Prediction of Magnetic Superexchange Constants in Lithium Silver Fluorides

## Problem background
Lithium–silver(II)–fluoride systems are an unexplored family of ternary fluorides. This work used evolutionary structure search and density functional theory (DFT) to predict the crystal structures of five low‑energy Li–Ag–F phases (LiAgF₃‑1, LiAgF₃‑2, Li₂AgF₄‑1, Li₂AgF₄‑2, Li₂AgF₄‑3) and to evaluate their thermodynamic stability and magnetic properties. All predicted structures were found to prefer antiferromagnetic (AFM) ground states. The primary magnetic quantities of interest are the magnetic superexchange constants J (in meV) that quantify the strength of the antiferromagnetic interactions, and the energy above the convex hull ΔE (in kJ/mol) that indicates metastability relative to decomposition into the binary fluorides LiF and AgF₂. This task asks you to reproduce these quantities from DFT+U calculations.

## Approach
Perform spin‑polarized DFT+U calculations within the PBEsol exchange‑correlation functional, applying a Hubbard U = 5.0 eV and J = 1.0 eV to the Ag 4d orbitals. For each ternary structure and for the binary references LiF (rocksalt) and AgF₂ (monoclinic), compute total energies in ferromagnetic (FM) and antiferromagnetic (AFM) spin configurations; for LiAgF₃‑2 an additional antiferromagnetic configuration (AFM2) is required.

The magnetic superexchange constants J are extracted from the total energies using the Heisenberg model H = −½ Σ Jᵢⱼ Sᵢ·Sⱼ. For each compound the mapping between total energies and J is given by the linear expressions written below. The equations follow the spin patterns of the magnetic unit cells and define the J values in meV.

- LiAgF₃‑1:  E_FM = E₀ − J ,  E_AFM = E₀ + J  →  J = (E_AFM − E_FM) / 2
- LiAgF₃‑2:  E_FM = E₀ − J₁ − J₂ ,  E_AFM = E₀ + J₁ + J₂ ,  E_AFM2 = E₀ + J₁ − J₂  →  J₁ = (E_AFM2 − E_FM) / 2 ,  J₂ = (E_AFM − E_AFM2) / 2
- Li₂AgF₄‑1:  E_FM = E₀ − 2 J ,  E_AFM = E₀ + 2 J  →  J = (E_AFM − E_FM) / 4
- Li₂AgF₄‑2:  E_FM = E₀ − 0.5 J ,  E_AFM = E₀ + 0.5 J  →  J = E_AFM − E_FM
- Li₂AgF₄‑3:  E_FM = E₀ − 0.5 J ,  E_AFM = E₀ + 0.5 J  →  J = E_AFM − E_FM

For the convex hull analysis, the energy above the hull ΔE is defined as the total energy of the ternary compound minus the sum of the total energies of the equivalent amounts of LiF and AgF₂, converted to kJ · mol⁻¹. Use the most stable (lowest) total energy for each ternary structure (E_AFM) and the FM total energy for the binary references. For LiAgF₃ the decomposition is LiF + AgF₂; for Li₂AgF₄ it is 2 LiF + AgF₂.

## Reproduction target
1. Write the converged total energies (in eV) to `total_energies.json` for all seven structures in the magnetic configurations specified.
2. From those energies, compute the magnetic superexchange constants J (in meV) using the Heisenberg model expressions listed above and write them to `j_values.json`.
3. Compute the energy above the convex hull ΔE (in kJ · mol⁻¹) for each ternary structure and write the results to `convex_hull.json`.
4. Verify that in `total_energies.json` every ternary structure has E_AFM < E_FM, confirming the antiferromagnetic ground state.

## Assets

- CIF files for LiAgF3-1, LiAgF3-2, Li2AgF4-1, Li2AgF4-2, Li2AgF4-3
- Quantum ESPRESSO (or any open-source DFT code): https://www.quantum-espresso.org/
- PBEsol pseudopotentials (e.g., SSSP library): https://www.materialscloud.org/discover/sssp/table/pbesol
- LiF crystal structure (rocksalt): https://materialsproject.org/materials/mp-1138
- AgF2 crystal structure (monoclinic): https://materialsproject.org/materials/mp-558848

## Workflow steps

### Step 1: DFT+U Spin-Polarized Total-Energy Calculations
- Role: process
- Action: Perform spin-polarized DFT+U (PBEsol functional, Hubbard U=5.0 eV, J=1.0 eV on Ag 4d) total-energy calculations for the five Li–Ag–F ternary structures and the binary references LiF and AgF2, using the specified magnetic configurations (FM, AFM, and for LiAgF3-2 also AFM2). Use the provided CIFs for the ternary compounds and obtain the binary structures from public databases. Write a log file as evidence.
- Evidence: `/app/outputs/dft_calc.log`

### Step 2: Collect Total Energies
- Role: scored
- Action: Extract converged total energies (in eV) from the DFT output files and write them to total_energies.json. The JSON must contain keys for all structures and their magnetic configurations.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: JSON object with keys: 'LiAgF3-1', 'LiAgF3-2', 'Li2AgF4-1', 'Li2AgF4-2', 'Li2AgF4-3', 'LiF', 'AgF2'. Each value is an object with keys 'E_FM' and 'E_AFM' (float, eV); 'LiAgF3-2' additionally has 'E_AFM2'.
- Scoring: scored by hidden verifier

### Step 3: Compute Magnetic Superexchange Constants J
- Role: scored (load-bearing)
- Action: Using the total energies from step_02_total_energies and the Heisenberg model energy expressions (provided in the instructions), compute magnetic superexchange constants J (in meV) for each structure: LiAgF3-1 (single J), LiAgF3-2 (J1 and J2), Li2AgF4-1 (single J), Li2AgF4-2 (single J), Li2AgF4-3 (single J). Output to j_values.json.
- Output file: `/app/outputs/j_values.json`
- Format: json
- Contract: JSON object with keys: 'LiAgF3-1', 'LiAgF3-2_J1', 'LiAgF3-2_J2', 'Li2AgF4-1', 'Li2AgF4-2', 'Li2AgF4-3'. Each value is a float (meV).
- Scoring: scored by hidden verifier

### Step 4: Compute Convex Hull Energies
- Role: scored (load-bearing)
- Action: From the total energies of ternary compounds and binary references (LiF, AgF2) in total_energies.json, calculate the energy above the convex hull (ΔE) for each ternary structure, defined as the total energy of the compound minus the sum of energies of the equivalent proportion of LiF and AgF2. Convert to kJ/mol (per formula unit). Write to convex_hull.json.
- Output file: `/app/outputs/convex_hull.json`
- Format: json
- Contract: JSON object with keys: 'LiAgF3-1', 'LiAgF3-2', 'Li2AgF4-1', 'Li2AgF4-2', 'Li2AgF4-3'. Each value is a float (kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/j_values.json`
- `/app/outputs/convex_hull.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw total energies from DFT+U calculations for all structures and spin configurations. The checker recomputes J and hull energies from this file.
- schema:
  - `type`: object
  - `required_keys`: `LiAgF3-1`, `LiAgF3-2`, `Li2AgF4-1`, `Li2AgF4-2`, `Li2AgF4-3`, `LiF`, `AgF2`
  - `properties`:
    - `LiAgF3-1`:
      - `type`: object
      - `required`: `E_FM`, `E_AFM`
      - `E_FM`: float, eV
      - `E_AFM`: float, eV
    - `LiAgF3-2`:
      - `type`: object
      - `required`: `E_FM`, `E_AFM`, `E_AFM2`
      - `E_FM`: float, eV
      - `E_AFM`: float, eV
      - `E_AFM2`: float, eV
    - `Li2AgF4-1`:
      - `type`: object
      - `required`: `E_FM`, `E_AFM`
      - `E_FM`: float, eV
      - `E_AFM`: float, eV
    - `Li2AgF4-2`:
      - `type`: object
      - `required`: `E_FM`, `E_AFM`
      - `E_FM`: float, eV
      - `E_AFM`: float, eV
    - `Li2AgF4-3`:
      - `type`: object
      - `required`: `E_FM`, `E_AFM`
      - `E_FM`: float, eV
      - `E_AFM`: float, eV
    - `LiF`:
      - `type`: object
      - `required`: `E_FM`
      - `E_FM`: float, eV
    - `AgF2`:
      - `type`: object
      - `required`: `E_FM`
      - `E_FM`: float, eV

### j_values.json
- path: `/app/outputs/j_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic superexchange constants J. The checker compares these values (and their ordering) to hidden paper-reported references.
- schema:
  - `type`: object
  - `required_keys`: `LiAgF3-1`, `LiAgF3-2_J1`, `LiAgF3-2_J2`, `Li2AgF4-1`, `Li2AgF4-2`, `Li2AgF4-3`
  - `LiAgF3-1`: float, meV
  - `LiAgF3-2_J1`: float, meV
  - `LiAgF3-2_J2`: float, meV
  - `Li2AgF4-1`: float, meV
  - `Li2AgF4-2`: float, meV
  - `Li2AgF4-3`: float, meV

### convex_hull.json
- path: `/app/outputs/convex_hull.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy above convex hull (ΔE). The checker compares these values to hidden paper-reported convex hull positions.
- schema:
  - `type`: object
  - `required_keys`: `LiAgF3-1`, `LiAgF3-2`, `Li2AgF4-1`, `Li2AgF4-2`, `Li2AgF4-3`
  - `LiAgF3-1`: float, kJ/mol
  - `LiAgF3-2`: float, kJ/mol
  - `Li2AgF4-1`: float, kJ/mol
  - `Li2AgF4-2`: float, kJ/mol
  - `Li2AgF4-3`: float, kJ/mol

Notes: All energies are per formula unit. The checker will verify that all ternary structures have E_AFM < E_FM in total_energies.json, confirming the antiferromagnetic ground state.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required_keys": [
          "LiAgF3-1",
          "LiAgF3-2",
          "Li2AgF4-1",
          "Li2AgF4-2",
          "Li2AgF4-3",
          "LiF",
          "AgF2"
        ],
        "properties": {
          "LiAgF3-1": {
            "type": "object",
            "required": [
              "E_FM",
              "E_AFM"
            ],
            "E_FM": "float, eV",
            "E_AFM": "float, eV"
          },
          "LiAgF3-2": {
            "type": "object",
            "required": [
              "E_FM",
              "E_AFM",
              "E_AFM2"
            ],
            "E_FM": "float, eV",
            "E_AFM": "float, eV",
            "E_AFM2": "float, eV"
          },
          "Li2AgF4-1": {
            "type": "object",
            "required": [
              "E_FM",
              "E_AFM"
            ],
            "E_FM": "float, eV",
            "E_AFM": "float, eV"
          },
          "Li2AgF4-2": {
            "type": "object",
            "required": [
              "E_FM",
              "E_AFM"
            ],
            "E_FM": "float, eV",
            "E_AFM": "float, eV"
          },
          "Li2AgF4-3": {
            "type": "object",
            "required": [
              "E_FM",
              "E_AFM"
            ],
            "E_FM": "float, eV",
            "E_AFM": "float, eV"
          },
          "LiF": {
            "type": "object",
            "required": [
              "E_FM"
            ],
            "E_FM": "float, eV"
          },
          "AgF2": {
            "type": "object",
            "required": [
              "E_FM"
            ],
            "E_FM": "float, eV"
          }
        }
      },
      "description": "Raw total energies from DFT+U calculations for all structures and spin configurations. The checker recomputes J and hull energies from this file."
    },
    {
      "file": "j_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "LiAgF3-1",
          "LiAgF3-2_J1",
          "LiAgF3-2_J2",
          "Li2AgF4-1",
          "Li2AgF4-2",
          "Li2AgF4-3"
        ],
        "LiAgF3-1": "float, meV",
        "LiAgF3-2_J1": "float, meV",
        "LiAgF3-2_J2": "float, meV",
        "Li2AgF4-1": "float, meV",
        "Li2AgF4-2": "float, meV",
        "Li2AgF4-3": "float, meV"
      },
      "description": "Magnetic superexchange constants J. The checker compares these values (and their ordering) to hidden paper-reported references."
    },
    {
      "file": "convex_hull.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "LiAgF3-1",
          "LiAgF3-2",
          "Li2AgF4-1",
          "Li2AgF4-2",
          "Li2AgF4-3"
        ],
        "LiAgF3-1": "float, kJ/mol",
        "LiAgF3-2": "float, kJ/mol",
        "Li2AgF4-1": "float, kJ/mol",
        "Li2AgF4-2": "float, kJ/mol",
        "Li2AgF4-3": "float, kJ/mol"
      },
      "description": "Energy above convex hull (ΔE). The checker compares these values to hidden paper-reported convex hull positions."
    }
  ],
  "notes": "All energies are per formula unit. The checker will verify that all ternary structures have E_AFM < E_FM in total_energies.json, confirming the antiferromagnetic ground state."
}
```

## How you are scored
A hidden verifier inspects your three output files. It reads `total_energies.json` and recomputes the magnetic superexchange constants J and the convex‑hull energies ΔE from the raw total energies using the same Heisenberg model expressions and decomposition formulas. The recomputed J values are checked against the values in your `j_values.json`, and the recomputed ΔE values are checked against your `convex_hull.json`; the expected numbers are derived from the paper’s results and hidden tolerances. The verifier also verifies that each ternary structure exhibits an antiferromagnetic ground state (E_AFM < E_FM) and that the ordering and magnitude requirements for LiAgF₃‑2 are satisfied. Each file contributes to a composite reward between 0 and 1; larger weights are attached to the J values and the convex‑hull energies.
