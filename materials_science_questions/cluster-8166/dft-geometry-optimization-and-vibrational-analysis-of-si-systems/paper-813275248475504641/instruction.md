# DFT Optimization and Vibrational Analysis of Diruthenium Hydridosilicate Complexes

## Problem background
Transition-metal centers can stabilize highly reactive silicon species, including hydridosilicate anions, by forming σ-complexes. Diruthenium complexes featuring η³,η³-[H₄SiAr]⁻ and η⁴,η⁴-[SiH₆]²⁻ ligands have been synthesized and characterized experimentally. Density functional theory (DFT) calculations were used to optimize their geometries and predict vibrational frequencies, supporting the structural assignments and bonding analysis. This task reproduces the key computational results — the optimized bond lengths and IR-active Ru–H stretching frequencies — to verify the computational methodology and provide a benchmark for the reported structural data.

## Approach
The computational workflow is as follows: Starting geometries are obtained from publicly available X-ray crystal structures (CCDC accession codes). DFT geometry optimization is performed with the B3PW91 functional, the 6-31G(d,p) basis set for light atoms, and the LANL2DZ effective core potential and basis for ruthenium. After optimization, a harmonic vibrational frequency calculation is carried out on each complex to ensure that no significant imaginary frequencies remain and to obtain IR intensities. From the optimized structures, the average Si–H bond length (averaged over the coordinated Si–H bonds), the average Ru–H bond length (averaged over the Ru–H contacts), and the Ru–Si bond length (or the average of the two when two are present) are extracted. From the vibrational output, the two strongest IR-active Ru–H stretching modes are identified and listed in ascending wavenumber order. The results are then written to a JSON file as specified in the output contract.

## Reproduction target
Produce a JSON file at /app/outputs/dft_results.json containing, for each complex (3a, 3b, 4), the keys: `avg_Si_H_bond_length` (average Si–H bond length in Å), `avg_Ru_H_bond_length` (average Ru–H bond length in Å), `Ru_Si_bond_length` (Ru–Si bond length in Å, or the average of two when two are present), and `IR_frequencies_cm1` (an array of two floats, the two strongest IR-active Ru–H stretching frequencies in cm⁻¹, listed in increasing order). These values must be derived from the DFT-optimized geometry and harmonic frequency analysis at the specified level of theory. No additional outputs are required.

## Assets

- CCDC 900947 (3a crystal structure): https://www.ccdc.cam.ac.uk/structures/
- CCDC 900948 (3b crystal structure): https://www.ccdc.cam.ac.uk/structures/
- CCDC 900949 (4-tol crystal structure): https://www.ccdc.cam.ac.uk/structures/
- CCDC 900950 (4-ben crystal structure): https://www.ccdc.cam.ac.uk/structures/
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Fetch crystal structures
- Role: process
- Action: Download the crystal structure files (CIF format) for complexes 3a, 3b, and 4-tol from the Cambridge Structural Database using accession codes 900947, 900948, and 900949. Optionally also fetch 900950 (4-ben) for reference.
- Evidence: none

### Step 2: DFT geometry optimization and vibrational frequency calculation
- Role: process
- Action: For each complex (3a, 3b, 4), set up and run a DFT geometry optimization followed by a vibrational frequency calculation using the B3PW91 functional, the 6-31G(d,p) basis set for light atoms, and the LANL2DZ effective core potential and basis for Ru. Use an open-source quantum chemistry package (e.g., ORCA). Ensure convergence of the geometry and confirm that no significant imaginary frequencies remain.
- Evidence: none

### Step 3: Extract bond lengths and IR frequencies
- Role: scored (load-bearing)
- Action: From the optimized geometry of each complex, compute the average Si-H bond length (average over the coordinated Si-H bonds), the average Ru-H bond length (average over the corresponding Ru-H contacts), and the Ru-Si bond length (or average of the two when present). From the vibrational frequency output, identify the two strongest IR-active Ru-H stretching modes (in cm⁻¹) and list them in increasing wavenumber order. Write the results for 3a, 3b, and 4 to /app/outputs/dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: JSON object with keys '3a', '3b', '4'. Each key maps to an object containing: 'avg_Si_H_bond_length' (float, Å), 'avg_Ru_H_bond_length' (float, Å), 'Ru_Si_bond_length' (float, Å), 'IR_frequencies_cm1' (array of two floats).
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
- target_policy: reference_match
- description: Optimized geometries and vibrational frequencies for complexes 3a, 3b, and 4. The bond lengths are averages over the coordinated Si-H and Ru-H bonds. The IR frequencies are the two strongest Ru-H stretching modes in cm⁻¹, listed in increasing order.
- schema:
  - `type`: object
  - `required`: `3a`, `3b`, `4`
  - `properties`:
    - `3a`:
      - `type`: object
      - `required`: `avg_Si_H_bond_length`, `avg_Ru_H_bond_length`, `Ru_Si_bond_length`, `IR_frequencies_cm1`
      - `properties`:
        - `avg_Si_H_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `avg_Ru_H_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `Ru_Si_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `IR_frequencies_cm1`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
    - `3b`:
      - `type`: object
      - `required`: `avg_Si_H_bond_length`, `avg_Ru_H_bond_length`, `Ru_Si_bond_length`, `IR_frequencies_cm1`
      - `properties`:
        - `avg_Si_H_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `avg_Ru_H_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `Ru_Si_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `IR_frequencies_cm1`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
    - `4`:
      - `type`: object
      - `required`: `avg_Si_H_bond_length`, `avg_Ru_H_bond_length`, `Ru_Si_bond_length`, `IR_frequencies_cm1`
      - `properties`:
        - `avg_Si_H_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `avg_Ru_H_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `Ru_Si_bond_length`:
          - `type`: number
          - `units`: angstrom
        - `IR_frequencies_cm1`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2

Notes: The bond lengths are averaged over the four Si-H bonds and the six Ru-H contacts as appropriate for each complex. For complex 4, the Ru-Si bond length is the average of the two nearly equal distances. The IR frequencies correspond to the strongest IR-active Ru-H stretching modes predicted by DFT; the assignment follows the paper's convention.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "3a",
          "3b",
          "4"
        ],
        "properties": {
          "3a": {
            "type": "object",
            "required": [
              "avg_Si_H_bond_length",
              "avg_Ru_H_bond_length",
              "Ru_Si_bond_length",
              "IR_frequencies_cm1"
            ],
            "properties": {
              "avg_Si_H_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "avg_Ru_H_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "Ru_Si_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "IR_frequencies_cm1": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              }
            }
          },
          "3b": {
            "type": "object",
            "required": [
              "avg_Si_H_bond_length",
              "avg_Ru_H_bond_length",
              "Ru_Si_bond_length",
              "IR_frequencies_cm1"
            ],
            "properties": {
              "avg_Si_H_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "avg_Ru_H_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "Ru_Si_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "IR_frequencies_cm1": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              }
            }
          },
          "4": {
            "type": "object",
            "required": [
              "avg_Si_H_bond_length",
              "avg_Ru_H_bond_length",
              "Ru_Si_bond_length",
              "IR_frequencies_cm1"
            ],
            "properties": {
              "avg_Si_H_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "avg_Ru_H_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "Ru_Si_bond_length": {
                "type": "number",
                "units": "angstrom"
              },
              "IR_frequencies_cm1": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              }
            }
          }
        }
      },
      "description": "Optimized geometries and vibrational frequencies for complexes 3a, 3b, and 4. The bond lengths are averages over the coordinated Si-H and Ru-H bonds. The IR frequencies are the two strongest Ru-H stretching modes in cm⁻¹, listed in increasing order."
    }
  ],
  "notes": "The bond lengths are averaged over the four Si-H bonds and the six Ru-H contacts as appropriate for each complex. For complex 4, the Ru-Si bond length is the average of the two nearly equal distances. The IR frequencies correspond to the strongest IR-active Ru-H stretching modes predicted by DFT; the assignment follows the paper's convention."
}
```

## How you are scored
A hidden verifier reads your dft_results.json and compares each reported bond length and IR frequency to a set of reference values. For each of the 12 bond lengths and 6 frequencies across the three complexes, the verifier checks whether the deviation from the reference falls within a hidden tolerance that reflects the typical accuracy of the computational method and hardware variations. The reward is proportional to the fraction of quantities that pass this check; all 18 within tolerance earns the maximum reward. Your task is to correctly perform the DFT calculations and extract the quantities as described; simply guessing or fabricating results will generally produce values outside the tolerance and yield a low score.
