# DFT study of Zn-doped SnO2 magnetism

## Problem background
Diluted magnetic semiconductors (DMS) hold promise for spintronic devices that utilize both charge and spin. Recent attention has turned to wide-bandgap oxides doped with nonmagnetic elements to avoid the magnetic secondary phases often encountered with transition metal dopants. Tin dioxide (SnO₂) in its rutile phase, when doped with zinc (Zn), has been reported to exhibit ferromagnetism, making it a candidate for room-temperature DMS. The microscopic origin of this magnetism and the role of native point defects, particularly oxygen vacancies (V_O) and tin vacancies (V_Sn), remain open questions. Reproducing the magnetic coupling strengths and the influence of vacancies is essential to assess the viability of Zn-doped SnO₂ for spintronic applications. The target of this task is to quantify the ferromagnetic stability for various Zn pair arrangements and the effect of native vacancies on the magnetic coupling.

## Approach
The investigation uses density functional theory (DFT) within the local density approximation (LDA) to perform spin-polarized total energy calculations. A 2×2×4 rutile SnO₂ supercell (32 Sn, 64 O atoms) is constructed using the experimental lattice constants a=4.680 Å and c=3.154 Å with Sn at (0,0,0) and O at (0.307,0.307,0). Two Sn atoms are substituted by Zn atoms at six different relative positions, labeled (0,1) through (0,6), to study the dependence of magnetic coupling on Zn–Zn distance and location. For each configuration, the energies of the ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments are computed after full geometry relaxation. The FM ground state is identified as the configuration with the lowest FM total energy, and its total magnetic moment is extracted. To assess the impact of native defects, one oxygen vacancy (V_O) and one tin vacancy (V_Sn) are introduced separately into the ground-state supercell, and FM and AFM energies are again computed. The calculations require an open-source DFT code (Quantum ESPRESSO) and standard LDA pseudopotentials for Sn, O, and Zn, which are publicly available. The comparative analysis focuses on the energy difference ΔE = E_FM − E_AFM for each configuration and the change in ΔE upon vacancy introduction.

## Reproduction target
Produce a single JSON file (`reproduction_results.json`) containing the results of all DFT calculations. The file must include: for each of the six Zn-doped configurations (0,1) to (0,6) in the 2×2×4 supercell, the identifier (e.g., `2x2x4_(0,1)`), the FM–AFM energy difference in meV, and the total magnetic moment of the supercell in μB; the identifier of the configuration that is the FM ground state (lowest FM total energy); and the FM–AFM energy differences for the ground state when one oxygen vacancy or one tin vacancy is present. The results should reflect full geometry optimizations carried out with an LDA functional and should be self-consistent. The purpose is to establish which spin arrangement is more stable and to quantify how native vacancies alter the magnetic coupling.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/download
- SSSP efficiency pseudopotentials (LDA) for Sn, O, Zn: https://www.materialscloud.org/discover/sssp/table/efficiency
- Rutile SnO2 crystal structure parameters

## Workflow steps

### Step 1: Run DFT calculations for Zn-doped configurations
- Role: process
- Action: Construct a 2×2×4 rutile SnO2 supercell (a=4.680 Å, c=3.154 Å, Sn at (0,0,0), O at (0.307,0.307,0)). For each of the six Zn pair configurations (0,1) through (0,6) where two Sn atoms are replaced by Zn, perform spin-polarized DFT calculations using an LDA functional. For each configuration, run fully relaxed geometry optimization and self-consistent field calculation for both ferromagnetic (initial total magnetic moment ~2 μB) and antiferromagnetic (initial total moment 0 μB) spin alignments. Save the optimized structures and total energies.
- Evidence: none

### Step 2: Run DFT calculations for vacancy cases
- Role: process
- Action: Identify the FM ground-state configuration (the configuration with the lowest FM total energy from step 1). Using its fully relaxed FM supercell, create two defective cells: one with one oxygen vacancy (V_O) and one with one tin vacancy (V_Sn), both located near the Zn atoms. For each defect cell, perform spin-polarized DFT geometry relaxation and self-consistent field calculation with FM and AFM spin alignments, and obtain total energies.
- Evidence: none

### Step 3: Compile results into scored artifact
- Role: scored (load-bearing)
- Action: Extract total energies and total magnetic moments from the output files of steps 1 and 2. Compute ΔE = E_FM − E_AFM (in meV) for each Zn configuration and for the two vacancy cases. Identify the ground-state configuration (lowest FM total energy). Compile all results into reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: A JSON object with keys: 'configurations' (array of objects, each with 'id' (string), 'delta_E_meV' (number), 'total_moment_muB' (number)), 'ground_state' (string, the id of the configuration with lowest FM total energy), 'vacancy_effects' (object with 'V_O_delta_E_meV' (number) and 'V_Sn_delta_E_meV' (number)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the computed FM-AFM energy differences, total magnetic moments, ground-state identification, and vacancy effects. The hidden checker compares reported values to paper references (±50 meV tolerance for ΔE, ±0.2 μB for moments), verifies all ΔE values are negative, checks that the ground-state id matches (0,3) and that V_Sn ΔE is more negative than the ground-state ΔE while V_O ΔE is less negative.
- schema:
  - `type`: object
  - `required`: `configurations`, `ground_state`, `vacancy_effects`
  - `properties`:
    - `configurations`:
      - `type`: array
      - `description`: List of results for each Zn configuration
      - `items`:
        - `type`: object
        - `required`: `id`, `delta_E_meV`, `total_moment_muB`
        - `properties`:
          - `id`:
            - `type`: string
            - `description`: Configuration identifier, e.g. 2x2x4_(0,3)
          - `delta_E_meV`:
            - `type`: number
            - `description`: FM-AFM energy difference in meV
          - `total_moment_muB`:
            - `type`: number
            - `description`: Total magnetic moment of the supercell in μB
    - `ground_state`:
      - `type`: string
      - `description`: The id of the configuration with the lowest FM total energy
    - `vacancy_effects`:
      - `type`: object
      - `required`: `V_O_delta_E_meV`, `V_Sn_delta_E_meV`
      - `properties`:
        - `V_O_delta_E_meV`:
          - `type`: number
          - `description`: FM-AFM energy difference with one oxygen vacancy, in meV
        - `V_Sn_delta_E_meV`:
          - `type`: number
          - `description`: FM-AFM energy difference with one tin vacancy, in meV

Notes: The checker will also verify structural properties (all ΔE negative, correct ground state ID, expected vacancy effect ordering). The numeric comparisons use tolerances that account for typical DFT code/functional variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "configurations",
          "ground_state",
          "vacancy_effects"
        ],
        "properties": {
          "configurations": {
            "type": "array",
            "description": "List of results for each Zn configuration",
            "items": {
              "type": "object",
              "required": [
                "id",
                "delta_E_meV",
                "total_moment_muB"
              ],
              "properties": {
                "id": {
                  "type": "string",
                  "description": "Configuration identifier, e.g. 2x2x4_(0,3)"
                },
                "delta_E_meV": {
                  "type": "number",
                  "description": "FM-AFM energy difference in meV"
                },
                "total_moment_muB": {
                  "type": "number",
                  "description": "Total magnetic moment of the supercell in μB"
                }
              }
            }
          },
          "ground_state": {
            "type": "string",
            "description": "The id of the configuration with the lowest FM total energy"
          },
          "vacancy_effects": {
            "type": "object",
            "required": [
              "V_O_delta_E_meV",
              "V_Sn_delta_E_meV"
            ],
            "properties": {
              "V_O_delta_E_meV": {
                "type": "number",
                "description": "FM-AFM energy difference with one oxygen vacancy, in meV"
              },
              "V_Sn_delta_E_meV": {
                "type": "number",
                "description": "FM-AFM energy difference with one tin vacancy, in meV"
              }
            }
          }
        }
      },
      "description": "Scored artifact containing the computed FM-AFM energy differences, total magnetic moments, ground-state identification, and vacancy effects. The hidden checker compares reported values to paper references (±50 meV tolerance for ΔE, ±0.2 μB for moments), verifies all ΔE values are negative, checks that the ground-state id matches (0,3) and that V_Sn ΔE is more negative than the ground-state ΔE while V_O ΔE is less negative."
    }
  ],
  "notes": "The checker will also verify structural properties (all ΔE negative, correct ground state ID, expected vacancy effect ordering). The numeric comparisons use tolerances that account for typical DFT code/functional variations."
}
```

## How you are scored
A hidden verifier will read `reproduction_results.json` and independently evaluate multiple aspects of the submitted results. The verifier checks that all reported ΔE values are negative (FM stability), that the identifier of the FM ground state matches the expected configuration, that the total magnetic moment of the ground state falls within acceptable variation, and that the vacancy results show a trend consistent with the physical effect (V_Sn enhancing FM coupling and V_O weakening it). Each check is weighted, and the verifier combines them into a single reward score between 0 and 1. It is not sufficient to simply report the expected numerical values; the submitted results must be a faithful outcome of the described DFT workflow. No tolerances or reference values are disclosed to the agent.
