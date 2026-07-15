# DFT Magnetic Moments for Defects in 6H-SiC

## Problem background
This task investigates the origin of defect-induced ferromagnetism (d0-magnetism) in carbon-based materials. The specific system is 6H-SiC crystal, where various defects (vacancies and Zn impurities) can introduce magnetic moments. Understanding which defects produce localized moments and whether they can couple ferromagnetically is crucial for spintronic applications. The target is to compute the total magnetic moment and atomic contributions for a set of defect configurations using density functional theory, providing quantitative evidence about the role of carbon 2p electrons.

## Approach
The approach uses spin-polarized density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation. A 3×2×2 supercell of 6H-SiC (96 atoms) is constructed from the known crystal structure. Seven configurations are studied: perfect crystal, single Si vacancy (V_Si), single C vacancy (V_C), substitutional Zn at a Si site (Zn_subs), interstitial Zn at the octahedral site (Zn_inter), nearest-neighbor V_Si–V_Si pair, and nearest-neighbor V_Si–V_C pair. For each configuration, the atomic positions are relaxed until forces fall below a chosen threshold, and a static self-consistent calculation yields the spin density, from which total and atomic magnetic moments are extracted. The calculations use open-source DFT software (e.g., Quantum ESPRESSO) with standard PBE pseudopotentials.

## Reproduction target
Produce a JSON file containing the total magnetic moment per supercell for each of the seven defect configurations. For V_Si and Zn_subs, also report the atomic magnetic moment on the defect site and the average atomic moment on the nearest-neighbor carbon atoms. For vacancy-pair configurations (V_Si_V_Si and V_Si_V_C), indicate whether the coupling is ferromagnetic. The output must follow the schema defined in the output contract.

## Assets

- 6H-SiC crystal structure
- Open-source DFT code (Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/precise

## Workflow steps

### Step 1: Build defect supercells and prepare DFT inputs
- Role: process
- Action: Construct a 3x2x2 supercell of 6H-SiC (48 Si + 48 C atoms) from the public crystal structure. Generate the seven configurations: perfect, single Si vacancy (V_Si), single C vacancy (V_C), substitutional Zn at a Si site (Zn_subs), interstitial Zn at the octahedral site (Zn_inter), nearest-neighbor V_Si–V_Si pair, and nearest-neighbor V_Si–V_C pair. Prepare spin-polarized DFT input files (e.g., pw.x input scripts) using GGA-PBE and the required pseudopotentials.
- Evidence: `/app/outputs/defect_inputs.zip`

### Step 2: Run spin-polarized DFT relaxation and static calculations
- Role: process
- Action: For each of the seven supercell configurations, perform spin-polarized DFT structural relaxation (forces < 0.01 eV/Å) followed by a self-consistent field calculation to obtain total energies, charge/spin densities, and magnetic moments. Use an open-source DFT code (e.g., Quantum ESPRESSO) with the PBE exchange-correlation functional and a plane-wave basis set.
- Evidence: `/app/outputs/dft_output_logs.zip`

### Step 3: Extract magnetic moments and compile results
- Role: scored (load-bearing)
- Action: Parse the DFT output files to extract the total magnetic moment of each supercell, the atomic magnetic moment on the defect site (for single-defect and pair configurations), the average atomic moment on nearest-neighbor C atoms (for V_Si and Zn_subs), and the ferromagnetic coupling status for vacancy pairs (true if the total moment indicates parallel alignment). Write the results to a structured JSON file.
- Output file: `/app/outputs/defect_magnetic_moments.json`
- Format: json
- Contract: Array of objects. Each object: { 'defect_type': string (one of the seven identifiers), 'total_moment_muB': float, 'atomic_moment_defect_site_muB': float|None, 'atomic_moment_nearest_C_muB': float|None, 'ferromagnetic_coupling': bool|None }.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_magnetic_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_magnetic_moments.json
- path: `/app/outputs/defect_magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed total and atomic magnetic moments for seven defect configurations in 6H-SiC, used to verify the DFT sub-result supporting the paper's conclusion about C2p-driven magnetism.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `defect_type`, `total_moment_muB`
    - `properties`:
      - `defect_type`:
        - `type`: string
      - `total_moment_muB`:
        - `type`: number
        - `unit`: μB
      - `atomic_moment_defect_site_muB`:
        - `type`: `number`, `null`
        - `unit`: μB
      - `atomic_moment_nearest_C_muB`:
        - `type`: `number`, `null`
        - `unit`: μB
      - `ferromagnetic_coupling`:
        - `type`: `boolean`, `null`

Notes: Only the DFT sub-result is scored; experimental work is excluded. The agent must run DFT with an open-source code; the hidden gold tolerances account for expected method-dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "defect_type",
            "total_moment_muB"
          ],
          "properties": {
            "defect_type": {
              "type": "string"
            },
            "total_moment_muB": {
              "type": "number",
              "unit": "μB"
            },
            "atomic_moment_defect_site_muB": {
              "type": [
                "number",
                "null"
              ],
              "unit": "μB"
            },
            "atomic_moment_nearest_C_muB": {
              "type": [
                "number",
                "null"
              ],
              "unit": "μB"
            },
            "ferromagnetic_coupling": {
              "type": [
                "boolean",
                "null"
              ]
            }
          }
        }
      },
      "description": "Computed total and atomic magnetic moments for seven defect configurations in 6H-SiC, used to verify the DFT sub-result supporting the paper's conclusion about C2p-driven magnetism."
    }
  ],
  "notes": "Only the DFT sub-result is scored; experimental work is excluded. The agent must run DFT with an open-source code; the hidden gold tolerances account for expected method-dependent spread."
}
```

## How you are scored
A hidden verifier reads your `defect_magnetic_moments.json` and independently scores each reported quantity against a reference (which accounts for method-dependent spread). Your reward is a weighted combination of checks for correct total moments, atomic moments, and coupling indicators. Reporting the paper's published values without running the DFT workflow will not succeed, because the verifier's tolerances are set to discriminate between a genuine calculation and a blind guess. The exact scoring thresholds are hidden; you must execute the full computational pipeline to achieve a high score.
