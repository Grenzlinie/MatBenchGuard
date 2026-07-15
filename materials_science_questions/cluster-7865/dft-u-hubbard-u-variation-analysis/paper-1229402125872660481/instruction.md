# Self-consistent Hubbard U Parameter Determination and Band Gap Prediction for UO2

## Problem background
Uranium dioxide (UO2) is a strongly correlated Mott insulator where standard density-functional theory (DFT) fails due to self-interaction errors. The Hubbard U correction is essential to restore the insulating nature, and the magnetic ground state—whether ferromagnetic (FM) or antiferromagnetic (AFM)—is a key experimental fact. This task applies density-functional perturbation theory (DFPT) to compute Hubbard parameters from first principles without empirical fitting, and aims to determine the energetically stable magnetic configuration of UO2.

## Approach
The reproduction uses the DFT+U method with the PBE-sol exchange-correlation functional. Hubbard U parameters are obtained self-consistently via the DFPT-based HP code of Quantum-ESPRESSO. The procedure alternates self-consistent field calculations, linear-response DFPT calculations to extract updated U values, and full geometry optimizations until the Hubbard U parameter converges. Calculations are performed for both FM and AFM spin arrangements of U atoms in a simple tetragonal unit cell, employing two variants of the Hubbard orbital projection: ortho-atomic and atomic. After convergence, the electronic band gap is computed from a final DFT+U calculation. All relevant quantities—converged U, relative total energies, magnetizations, lattice constants, and band gaps—are collected for the four configuration/projection combinations.

## Reproduction target
For each of the four cases (ortho-atomic AFM, ortho-atomic FM, atomic AFM, atomic FM), carry out the self-consistent Hubbard U procedure described in Step 1. Then, as detailed in Step 2, compute the following: the converged Hubbard U parameter (U_sc), the total energy difference relative to the lowest-energy configuration (delta_E), total and absolute magnetizations per formula unit, equilibrium lattice constants a and c, and the electronic band gap (E_g). Write these results into `/app/outputs/results_table.json` according to the specified JSON schema.

## Assets

- Quantum-ESPRESSO with HP code (pw.x, hp.x): https://github.com/QEF/q-e
- pslibrary ultrasoft pseudopotentials for U and O: https://github.com/dalcorso/pslibrary

## Workflow steps

### Step 1: Self-consistent Hubbard U parameter determination and geometry optimization
- Role: process
- Action: For each of the four magnetic state/projection combinations (ortho-atomic AFM, ortho-atomic FM, atomic AFM, atomic FM), perform the self-consistent Hubbard U parameter loop using Quantum-ESPRESSO (pw.x and hp.x) with PBE-sol functional and ultrasoft pseudopotentials for U and O, starting from a simple tetragonal unit cell. The loop alternates SCF calculations, DFPT linear-response calculations to obtain U_out, and full geometry optimizations until the Hubbard U parameter converges. Record the final converged U_sc, total energy, optimized lattice constants a and c, and magnetization values (M_tot, M_abs) for later use.
- Evidence: `/app/outputs/hubbard_convergence.log`

### Step 2: Compute electronic band gaps and collect final results
- Role: scored (load-bearing)
- Action: Using the converged U_sc and optimized geometries from the self-consistent loops, perform a final DFT+U SCF calculation for each of the four cases. Compute the electronic band gap (energy difference between valence-band maximum and conduction-band minimum) from the resulting electronic structure. Collect all final quantities: U_sc (eV), total energy difference delta_E (eV) relative to the ortho-atomic AFM configuration, total magnetization M_tot (μ_B per formula unit), absolute magnetization M_abs (μ_B), lattice constants a (Å) and c (Å), and band gap E_g (eV). Write an array of four objects, one per configuration, to results_table.json.
- Output file: `/app/outputs/results_table.json`
- Format: json
- Contract: Array of 4 objects. Each object has keys: 'projection' (string, one of 'ortho-atomic' or 'atomic'), 'magnetic' (string, one of 'AFM' or 'FM'), 'U_sc' (float, eV), 'delta_E' (float, eV), 'M_tot' (float, μ_B), 'M_abs' (float, μ_B), 'a' (float, Å), 'c' (float, Å), 'E_g' (float, eV). Values must be the self-consistent final results.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_table.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_table.json
- path: `/app/outputs/results_table.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final converged results for the four UO2 configurations. The values are compared against hidden reference values with appropriate tolerances and trend checks.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `projection`, `magnetic`, `U_sc`, `delta_E`, `M_tot`, `M_abs`, `a`, `c`, `E_g`
    - `properties`:
      - `projection`:
        - `type`: string
        - `enum`: `ortho-atomic`, `atomic`
      - `magnetic`:
        - `type`: string
        - `enum`: `AFM`, `FM`
      - `U_sc`:
        - `type`: number
        - `unit`: eV
      - `delta_E`:
        - `type`: number
        - `unit`: eV
      - `M_tot`:
        - `type`: number
        - `unit`: μ_B per formula unit
      - `M_abs`:
        - `type`: number
        - `unit`: μ_B per formula unit
      - `a`:
        - `type`: number
        - `unit`: Å
      - `c`:
        - `type`: number
        - `unit`: Å
      - `E_g`:
        - `type`: number
        - `unit`: eV
  - `minItems`: 4
  - `maxItems`: 4

Notes: Only the quantitative results in results_table.json are scored. The density-of-states plot and qualitative analysis are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_table.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "projection",
            "magnetic",
            "U_sc",
            "delta_E",
            "M_tot",
            "M_abs",
            "a",
            "c",
            "E_g"
          ],
          "properties": {
            "projection": {
              "type": "string",
              "enum": [
                "ortho-atomic",
                "atomic"
              ]
            },
            "magnetic": {
              "type": "string",
              "enum": [
                "AFM",
                "FM"
              ]
            },
            "U_sc": {
              "type": "number",
              "unit": "eV"
            },
            "delta_E": {
              "type": "number",
              "unit": "eV"
            },
            "M_tot": {
              "type": "number",
              "unit": "μ_B per formula unit"
            },
            "M_abs": {
              "type": "number",
              "unit": "μ_B per formula unit"
            },
            "a": {
              "type": "number",
              "unit": "Å"
            },
            "c": {
              "type": "number",
              "unit": "Å"
            },
            "E_g": {
              "type": "number",
              "unit": "eV"
            }
          }
        },
        "minItems": 4,
        "maxItems": 4
      },
      "description": "Final converged results for the four UO2 configurations. The values are compared against hidden reference values with appropriate tolerances and trend checks."
    }
  ],
  "notes": "Only the quantitative results in results_table.json are scored. The density-of-states plot and qualitative analysis are not required."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results_table.json` and compares each reported value against reference results (derived from published data) using appropriate tolerances. It also checks that the results satisfy structural relationships: for each projection scheme, the relative energies and band gaps must follow a consistent physical ordering between FM and AFM states, and the lattice constants across the four configurations should be nearly identical (within a small variation). The final reward is a weighted combination of these checks; a result with all values within tolerance and all trend checks satisfied earns full credit, otherwise partial credit is awarded in proportion to the number of passing checks.
