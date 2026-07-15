# Mg²⁺ hexahydrate second-shell cluster: S6 and PRC conformer energy and binding enthalpy benchmarking

## Problem background
Understanding the arrangement of water molecules around divalent magnesium ions is fundamental to ion solvation. When six water molecules fill the first hydration shell to form an octahedral Mg[H₂O]₆²⁺ cluster, additional waters occupy a second shell, and the way these outer waters hydrogen‑bond to the inner core and to each other determines the cluster's stability. A previously reported structure (the PRC conformer) arranges the 12 second‑shell waters as four non‑interacting trimers. Computational evidence suggests that a different arrangement, in which the 12 waters form an integrated network involving pentameric motifs, might be more stable. Reproducing the energy gap between these two conformers and the net binding enthalpy of the second shell for the integrated‑network model is the focus of this task.

## Approach
The proposed method uses density functional theory (DFT) at the B3LYP/6‑31+G** level to optimize the geometries of the Mg[H₂O]₆²⁺·[H₂O]₁₂ clusters. Two starting geometries are constructed: the PRC conformer (four noninteracting hydrogen‑bonded trimers of second‑shell waters attached to alternate faces of the inner octahedron) and the S₆ conformer (octahedral inner shell encased in a dodecahedral hydrogen‑bond network where water pentamers join four second‑shell waters to one first‑shell water). Both structures are optimized without symmetry constraints and verified as local minima by vibrational frequency analysis. Reference energies are computed for the isolated water monomer and the bare Mg[H₂O]₆²⁺ core. From these, the electronic energy difference between the two conformers is calculated, and the net binding enthalpy for adding 12 water molecules to the hexahydrate core to form the S₆ cluster is obtained at 298 K.

## Reproduction target
Run the full workflow and produce the two scored output files: `energy_ordering.json` containing the total electronic energies of the S₆ and PRC conformers and their difference ΔE = E(PRC) – E(S₆) in kcal·mol⁻¹, and `binding_enthalpy.json` containing the net binding enthalpy at 298 K for the reaction Mg[H₂O]₆²⁺ + 12 H₂O → Mg[H₂O]₆²⁺·[H₂O]₁₂ (S₆) at the B3LYP/6‑31+G** level. The supporting optimized geometries (`S6_optimized.xyz`, `PRC_optimized.xyz`) must also be saved, but only the two JSON files are scored.

## Assets

- ORCA, NWChem, or PySCF quantum chemistry package: https://orcaforum.kofo.mpg.de (ORCA) or https://nwchemgit.github.io (NWChem) or https://pyscf.org (PySCF)
- 6-31+G** basis set: Included in the chosen QM package or from Basis Set Exchange (https://www.basissetexchange.org)

## Provided initial geometries
The following initial Cartesian coordinates (XYZ format) are provided as public starting points for the DFT optimisations. Write each block to a file with the indicated name before beginning the DFT steps.

### PRC_initial.xyz
```
55
PRC initial guess
Mg      0.000000    0.000000    0.000000
O       2.100000    0.000000    0.000000
H       2.600000    0.800000    0.000000
H       2.600000   -0.800000    0.000000
O      -2.100000    0.000000    0.000000
H      -2.600000    0.800000    0.000000
H      -2.600000   -0.800000    0.000000
O       0.000000    2.100000    0.000000
H       0.800000    2.600000    0.000000
H      -0.800000    2.600000    0.000000
O       0.000000   -2.100000    0.000000
H       0.800000   -2.600000    0.000000
H      -0.800000   -2.600000    0.000000
O       0.000000    0.000000    2.100000
H       0.800000    0.000000    2.600000
H      -0.800000    0.000000    2.600000
O       0.000000    0.000000   -2.100000
H       0.800000    0.000000   -2.600000
H      -0.800000    0.000000   -2.600000
O       4.000000    0.000000    0.000000
H       4.500000    0.700000    0.000000
H       4.500000   -0.700000    0.000000
O      -4.000000    0.000000    0.000000
H      -4.500000    0.700000    0.000000
H      -4.500000   -0.700000    0.000000
O       0.000000    4.000000    0.000000
H       0.700000    4.500000    0.000000
H      -0.700000    4.500000    0.000000
O       0.000000   -4.000000    0.000000
H       0.700000   -4.500000    0.000000
H      -0.700000   -4.500000    0.000000
O       0.000000    0.000000    4.000000
H       0.700000    0.000000    4.500000
H      -0.700000    0.000000    4.500000
O       0.000000    0.000000   -4.000000
H       0.700000    0.000000   -4.500000
H      -0.700000    0.000000   -4.500000
O       4.500000    2.500000    0.000000
H       5.000000    2.900000    0.000000
H       4.000000    2.900000    0.000000
O      -4.500000   -2.500000    0.000000
H      -5.000000   -2.900000    0.000000
H      -4.000000   -2.900000    0.000000
O       0.000000    4.500000    2.500000
H       0.400000    5.000000    2.900000
H      -0.400000    4.000000    2.900000
O       0.000000   -4.500000   -2.500000
H       0.400000   -5.000000   -2.900000
H      -0.400000   -4.000000   -2.900000
O       2.500000    0.000000    4.500000
H       2.900000    0.400000    5.000000
H       2.900000   -0.400000    4.000000
O      -2.500000    0.000000   -4.500000
H      -2.900000    0.400000   -5.000000
H      -2.900000   -0.400000   -4.000000
```

### S6_initial.xyz
```
55
S6 initial guess
Mg      0.000000    0.000000    0.000000
O       2.100000    0.000000    0.000000
H       2.600000    0.800000    0.000000
H       2.600000   -0.800000    0.000000
O      -2.100000    0.000000    0.000000
H      -2.600000    0.800000    0.000000
H      -2.600000   -0.800000    0.000000
O       0.000000    2.100000    0.000000
H       0.800000    2.600000    0.000000
H      -0.800000    2.600000    0.000000
O       0.000000   -2.100000    0.000000
H       0.800000   -2.600000    0.000000
H      -0.800000   -2.600000    0.000000
O       0.000000    0.000000    2.100000
H       0.800000    0.000000    2.600000
H      -0.800000    0.000000    2.600000
O       0.000000    0.000000   -2.100000
H       0.800000    0.000000   -2.600000
H      -0.800000    0.000000   -2.600000
O       3.500000    1.500000    0.000000
H       4.000000    2.000000    0.500000
H       3.000000    1.000000   -0.500000
O      -3.500000   -1.500000    0.000000
H      -4.000000   -2.000000    0.500000
H      -3.000000   -1.000000   -0.500000
O       0.000000    3.500000    1.500000
H       0.500000    4.000000    2.000000
H      -0.500000    3.000000    1.000000
O       0.000000   -3.500000   -1.500000
H       0.500000   -4.000000   -2.000000
H      -0.500000   -3.000000   -1.000000
O       1.500000    0.000000    3.500000
H       2.000000    0.500000    4.000000
H       1.000000   -0.500000    3.000000
O      -1.500000    0.000000   -3.500000
H      -2.000000    0.500000   -4.000000
H      -1.000000   -0.500000   -3.000000
O       4.000000    3.000000    1.500000
H       4.500000    3.500000    2.000000
H       3.500000    2.500000    1.000000
O      -4.000000   -3.000000   -1.500000
H      -4.500000   -3.500000   -2.000000
H      -3.500000   -2.500000   -1.000000
O       1.500000    4.000000    3.000000
H       2.000000    4.500000    3.500000
H       1.000000    3.500000    2.500000
O      -1.500000   -4.000000   -3.000000
H      -2.000000   -4.500000   -3.500000
H      -1.000000   -3.500000   -2.500000
O       3.000000    1.500000    4.000000
H       3.500000    2.000000    4.500000
H       2.500000    1.000000    3.500000
O      -3.000000   -1.500000   -4.000000
H      -3.500000   -2.000000   -4.500000
H      -2.500000   -1.000000   -3.500000
```

## Workflow steps

### Step 1: Compute water monomer reference
- Role: process
- Action: Optimize a single H₂O molecule at the B3LYP/6-31+G** level and perform a vibrational frequency calculation to obtain its total electronic energy and thermal correction (enthalpy) at 298 K. Write the total energy and enthalpy to a JSON file.
- Evidence: `/app/outputs/water_energy.json`

### Step 2: Optimize Mg[H₂O]₆²⁺ core cluster
- Role: process
- Action: Build the Mg[H₂O]₆²⁺ octahedral complex (Tₕ symmetry), optimize at B3LYP/6-31+G**, and perform a frequency calculation to confirm it is a minimum and to obtain its thermal correction. Write the total energy and enthalpy at 298 K to a JSON file.
- Evidence: `/app/outputs/mg_hexahydrate_energy.json`

### Step 3: Optimize PRC conformer
- Role: process
- Action: Read the initial geometry from the provided PRC_initial.xyz file (see "Provided initial geometries" section below). Optimize at B3LYP/6-31+G** without symmetry constraints and verify (via frequency analysis) that it is a local minimum. Save the optimized Cartesian coordinates as PRC_optimized.xyz and write the total electronic energy to `/app/outputs/PRC_energy.json`.
- Evidence: `/app/outputs/PRC_energy.json`

### Step 4: Optimize new S₆ conformer
- Role: process
- Action: Read the initial geometry from the provided S6_initial.xyz file (see "Provided initial geometries" section below). Optimize at B3LYP/6-31+G** without symmetry constraints and verify that it is a local minimum. Save the optimized coordinates as S6_optimized.xyz and write the total electronic energy to `/app/outputs/S6_energy.json`.
- Evidence: `/app/outputs/S6_energy.json`

### Step 5: Compute energy ordering
- Role: scored (load-bearing)
- Action: Read the total electronic energies from the previous steps. Compute the energy difference ΔE = E(PRC) – E(S₆) in kcal·mol⁻¹ (positive when S₆ is lower) and write the two total energies and the difference to energy_ordering.json.
- Output file: `/app/outputs/energy_ordering.json`
- Format: json
- Contract: {"S6_total_energy_hartree": number, "PRC_total_energy_hartree": number, "delta_E_kcal_per_mol": number}
- Scoring: scored by hidden verifier

### Step 6: Compute net binding enthalpy
- Role: scored (load-bearing)
- Action: Using the total energies and thermal corrections (enthalpies) obtained for water monomer (step 1), Mg[H₂O]₆²⁺ (step 2), and the S₆ cluster (step 4), compute the net binding enthalpy ΔH298 for the reaction Mg[H₂O]₆²⁺ + 12 H₂O → Mg[H₂O]₆²⁺·[H₂O]₁₂ (S₆) at the B3LYP/6-31+G** level. Report the result in kcal·mol⁻¹ together with the computational level in binding_enthalpy.json.
- Output file: `/app/outputs/binding_enthalpy.json`
- Format: json
- Contract: {"net_binding_enthalpy_kcal_per_mol": number, "level": "B3LYP/6-31+G**"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_ordering.json`
- `/app/outputs/binding_enthalpy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_ordering.json
- path: `/app/outputs/energy_ordering.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reports the total electronic energies of the S6 and PRC conformers and the energy difference (E(PRC)−E(S6)) in kcal·mol⁻¹, which should be positive when S6 is lower.
- schema:
  - `type`: object
  - `required`:
    - `S6_total_energy_hartree`: number
    - `PRC_total_energy_hartree`: number
    - `delta_E_kcal_per_mol`: number
  - `units`:
    - `S6_total_energy_hartree`: hartree
    - `PRC_total_energy_hartree`: hartree
    - `delta_E_kcal_per_mol`: kcal/mol

### binding_enthalpy.json
- path: `/app/outputs/binding_enthalpy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Net binding enthalpy for Mg[H₂O]₆²⁺ + 12 H₂O → Mg[H₂O]₆²⁺·[H₂O]₁₂ (S6) at the B3LYP/6-31+G** level.
- schema:
  - `type`: object
  - `required`:
    - `net_binding_enthalpy_kcal_per_mol`: number
    - `level`: string
  - `units`:
    - `net_binding_enthalpy_kcal_per_mol`: kcal/mol

Notes: The checker compares the reported values to the paper's published results with appropriate tolerances. The supporting optimized geometries (XYZ files) produced during the process steps are not part of the scored output contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_ordering.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "S6_total_energy_hartree": "number",
          "PRC_total_energy_hartree": "number",
          "delta_E_kcal_per_mol": "number"
        },
        "units": {
          "S6_total_energy_hartree": "hartree",
          "PRC_total_energy_hartree": "hartree",
          "delta_E_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Reports the total electronic energies of the S6 and PRC conformers and the energy difference (E(PRC)−E(S6)) in kcal·mol⁻¹, which should be positive when S6 is lower."
    },
    {
      "file": "binding_enthalpy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "net_binding_enthalpy_kcal_per_mol": "number",
          "level": "string"
        },
        "units": {
          "net_binding_enthalpy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Net binding enthalpy for Mg[H₂O]₆²⁺ + 12 H₂O → Mg[H₂O]₆²⁺·[H₂O]₁₂ (S6) at the B3LYP/6-31+G** level."
    }
  ],
  "notes": "The checker compares the reported values to the paper's published results with appropriate tolerances. The supporting optimized geometries (XYZ files) produced during the process steps are not part of the scored output contract."
}
```

## How you are scored
A hidden verifier independently inspects each scored output file. It compares your reported difference ΔE and net binding enthalpy against the expected values obtained from the original investigation, using tolerances that allow for the variation among different quantum‑chemistry program implementations. Each scored artifact carries a weight, and the final reward is the weighted sum of the per‑artifact scores. You must produce valid JSON files with the exact schema described; reporting a number that matches the paper’s value without actually performing the computation will not suffice because the verifier enforces the workflow evidence and checks internal consistency where possible. No further detail on the hidden tolerances or weights is provided.
