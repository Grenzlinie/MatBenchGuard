# Benchmarking HF and B3LYP methods for geometry and vibrational frequencies of β-2APDP

## Problem background
Computational quantum chemistry methods are widely used to predict molecular geometries and vibrational spectra, but their accuracy depends on the choice of theoretical model and basis set. This task investigates how well two common electronic structure methods — Hartree-Fock (HF) and the hybrid density functional B3LYP — reproduce the experimentally observed structure and infrared spectrum of a molecular crystal of β-2-aminopyridinium dihydrogenphosphate (β-2APDP). The central question is: which method yields better agreement with experimental X-ray crystal structures and FT‑IR vibrational data? The benchmark focuses on the optimized bond lengths, bond angles, and harmonic vibrational frequencies, which together provide a quantitative test of the two methods.

## Approach
The molecular geometry of β-2APDP is fully optimized and harmonic vibrational frequencies are computed using both HF and B3LYP with the 6-311++G(d,p) basis set. The initial structure is built from the chemical formula (C5H7N2)(H2PO4) and reasonable bond connectivity. After optimization, a predefined set of 16 bond lengths and 16 bond angles is extracted. The raw harmonic frequencies are then scaled using scaling factors derived specifically for this molecule: for HF, frequencies above 2000 cm⁻¹ are multiplied by 0.8381 and those ≤2000 cm⁻¹ by 0.8892; for B3LYP, frequencies above 2000 cm⁻¹ are multiplied by 0.9596 and those ≤2000 cm⁻¹ by 0.9665. The scaled frequencies are sorted in ascending order (modes 1–57). To evaluate the performance, the geometric parameters and scaled frequencies from each method are compared against experimental X-ray and FT‑IR reference data. The vibrational assessment uses the root-mean-square deviation (RMSD) and the Pearson correlation coefficient (R²) between the computed scaled frequencies and the experimental values.

## Reproduction target
Produce two scored artifacts:

1. **Geometric parameters** — the optimized bond lengths (Å) and bond angles (°) for both HF and B3LYP, covering the 16 bonds and 16 angles listed in the output schema. These should be extracted from fully optimized geometries obtained with the specified methods and basis set.

2. **Scaled vibrational frequencies** — a sorted list of 57 scaled harmonic frequencies (cm⁻¹) for each method, computed by applying the provided scaling factors and ordering the modes in ascending order.

The evaluation target is to compute, from these scaled frequencies, the RMS deviation and Pearson R² between the computed frequencies and the hidden experimental IR frequencies, and to quantitatively compare the two methods. The comparison provides a benchmark of method accuracy for this system.

## Assets

- Psi4: psi4

## Workflow steps

### Step 1: Geometry optimization and harmonic frequency analysis
- Role: process
- Action: Perform geometry optimization and harmonic vibrational frequency calculations for β-2‑aminopyridinium dihydrogenphosphate (β-2APDP) using both HF/6‑311++G(d,p) and B3LYP/6‑311++G(d,p) methods. Construct the initial molecular geometry from the chemical formula (C5H7N2)(H2PO4) and reasonable bond connectivity. Use an open‑source quantum chemistry package (e.g., Psi4).
- Evidence: `/app/outputs/optimization.log`

### Step 2: Extract optimized geometric parameters
- Role: scored (load-bearing)
- Action: From the optimized geometries at both levels, extract the 16 bond lengths and 16 bond angles listed in the output schema and write them to geometric_parameters.json.
- Output file: `/app/outputs/geometric_parameters.json`
- Format: json
- Contract: A JSON object with keys 'hf' and 'b3lyp'. Each contains a 'bond_lengths' object (key: bond name, value in Å) and a 'bond_angles' object (key: angle name, value in degrees). Required bond lengths: P1-O1, P1-O2, P1-O3, P1-O4, N1-C5, N1-C1, N2-C5, C1-C2, C2-C3, C3-C4, C4-C5, O3-N1, O4-N2, N1-H7, N2-H8, N2-H9. Required angles: O3-P1-O4, O3-P1-O1, O4-P1-O1, O3-P1-O2, O4-P1-O2, O1-P1-O2, C2-C1-N1, C1-C2-C3, C4-C3-C2, C3-C4-C5, C5-N1-C1, N2-C5-N1, N2-C5-C4, N1-C5-C4, N1-H7-O3, N1-H8-O4.
- Scoring: scored by hidden verifier

### Step 3: Scale and output vibrational frequencies
- Role: scored (load-bearing)
- Action: Take the raw harmonic frequencies from the B3LYP and HF calculations. Apply the predetermined scaling factors: for HF, frequencies >2000 cm⁻¹ multiplied by 0.8381, ≤2000 cm⁻¹ by 0.8892; for B3LYP, >2000 cm⁻¹ multiplied by 0.9596, ≤2000 cm⁻¹ by 0.9665. Sort the scaled frequencies in ascending order (mode 1 to 57) and output scaled_frequencies.json.
- Output file: `/app/outputs/scaled_frequencies.json`
- Format: json
- Contract: A JSON object with keys 'hf' and 'b3lyp'. Each is an array of 57 floats (units cm⁻¹), sorted in ascending order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometric_parameters.json`
- `/app/outputs/scaled_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometric_parameters.json
- path: `/app/outputs/geometric_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized bond lengths (Å) and bond angles (°) from HF/6‑311++G(d,p) and B3LYP/6‑311++G(d,p) calculations. Every value is compared to the paper‑reported optimized parameters with an absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `hf`:
      - `bond_lengths`:
        - `unit`: Å
      - `bond_angles`:
        - `unit`: degrees
    - `b3lyp`:
      - `bond_lengths`:
        - `unit`: Å
      - `bond_angles`:
        - `unit`: degrees
  - `properties`:
    - `hf`:
      - `bond_lengths`:
        - `P1-O1`: float
        - `P1-O2`: float
        - `P1-O3`: float
        - `P1-O4`: float
        - `N1-C5`: float
        - `N1-C1`: float
        - `N2-C5`: float
        - `C1-C2`: float
        - `C2-C3`: float
        - `C3-C4`: float
        - `C4-C5`: float
        - `O3-N1`: float
        - `O4-N2`: float
        - `N1-H7`: float
        - `N2-H8`: float
        - `N2-H9`: float
      - `bond_angles`:
        - `O3-P1-O4`: float
        - `O3-P1-O1`: float
        - `O4-P1-O1`: float
        - `O3-P1-O2`: float
        - `O4-P1-O2`: float
        - `O1-P1-O2`: float
        - `C2-C1-N1`: float
        - `C1-C2-C3`: float
        - `C4-C3-C2`: float
        - `C3-C4-C5`: float
        - `C5-N1-C1`: float
        - `N2-C5-N1`: float
        - `N2-C5-C4`: float
        - `N1-C5-C4`: float
        - `N1-H7-O3`: float
        - `N1-H8-O4`: float
    - `b3lyp`:
      - `bond_lengths`:
        - `P1-O1`: float
        - `P1-O2`: float
        - `P1-O3`: float
        - `P1-O4`: float
        - `N1-C5`: float
        - `N1-C1`: float
        - `N2-C5`: float
        - `C1-C2`: float
        - `C2-C3`: float
        - `C3-C4`: float
        - `C4-C5`: float
        - `O3-N1`: float
        - `O4-N2`: float
        - `N1-H7`: float
        - `N2-H8`: float
        - `N2-H9`: float
      - `bond_angles`:
        - `O3-P1-O4`: float
        - `O3-P1-O1`: float
        - `O4-P1-O1`: float
        - `O3-P1-O2`: float
        - `O4-P1-O2`: float
        - `O1-P1-O2`: float
        - `C2-C1-N1`: float
        - `C1-C2-C3`: float
        - `C4-C3-C2`: float
        - `C3-C4-C5`: float
        - `C5-N1-C1`: float
        - `N2-C5-N1`: float
        - `N2-C5-C4`: float
        - `N1-C5-C4`: float
        - `N1-H7-O3`: float
        - `N1-H8-O4`: float

### scaled_frequencies.json
- path: `/app/outputs/scaled_frequencies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scaled harmonic vibrational frequencies (cm⁻¹) for 57 normal modes, sorted in ascending order. The checker recomputes RMSE and Pearson R² against hidden experimental frequencies and verifies that the relative performance of the two methods matches the expected ranking.
- schema:
  - `type`: object
  - `required`:
    - `hf`: array of 57 floats
    - `b3lyp`: array of 57 floats
  - `items`:
    - `unit`: cm⁻¹

Notes: Scaling factors are provided in the public step description and must be applied. The initial molecular geometry is not provided; the agent builds connectivity from the formula (C5H7N2)(H2PO4). The score for geometric parameters uses an absolute tolerance; the frequency score uses recomputed RMSE/R² with trend requirements.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometric_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hf": {
            "bond_lengths": {
              "unit": "Å"
            },
            "bond_angles": {
              "unit": "degrees"
            }
          },
          "b3lyp": {
            "bond_lengths": {
              "unit": "Å"
            },
            "bond_angles": {
              "unit": "degrees"
            }
          }
        },
        "properties": {
          "hf": {
            "bond_lengths": {
              "P1-O1": "float",
              "P1-O2": "float",
              "P1-O3": "float",
              "P1-O4": "float",
              "N1-C5": "float",
              "N1-C1": "float",
              "N2-C5": "float",
              "C1-C2": "float",
              "C2-C3": "float",
              "C3-C4": "float",
              "C4-C5": "float",
              "O3-N1": "float",
              "O4-N2": "float",
              "N1-H7": "float",
              "N2-H8": "float",
              "N2-H9": "float"
            },
            "bond_angles": {
              "O3-P1-O4": "float",
              "O3-P1-O1": "float",
              "O4-P1-O1": "float",
              "O3-P1-O2": "float",
              "O4-P1-O2": "float",
              "O1-P1-O2": "float",
              "C2-C1-N1": "float",
              "C1-C2-C3": "float",
              "C4-C3-C2": "float",
              "C3-C4-C5": "float",
              "C5-N1-C1": "float",
              "N2-C5-N1": "float",
              "N2-C5-C4": "float",
              "N1-C5-C4": "float",
              "N1-H7-O3": "float",
              "N1-H8-O4": "float"
            }
          },
          "b3lyp": {
            "bond_lengths": {
              "P1-O1": "float",
              "P1-O2": "float",
              "P1-O3": "float",
              "P1-O4": "float",
              "N1-C5": "float",
              "N1-C1": "float",
              "N2-C5": "float",
              "C1-C2": "float",
              "C2-C3": "float",
              "C3-C4": "float",
              "C4-C5": "float",
              "O3-N1": "float",
              "O4-N2": "float",
              "N1-H7": "float",
              "N2-H8": "float",
              "N2-H9": "float"
            },
            "bond_angles": {
              "O3-P1-O4": "float",
              "O3-P1-O1": "float",
              "O4-P1-O1": "float",
              "O3-P1-O2": "float",
              "O4-P1-O2": "float",
              "O1-P1-O2": "float",
              "C2-C1-N1": "float",
              "C1-C2-C3": "float",
              "C4-C3-C2": "float",
              "C3-C4-C5": "float",
              "C5-N1-C1": "float",
              "N2-C5-N1": "float",
              "N2-C5-C4": "float",
              "N1-C5-C4": "float",
              "N1-H7-O3": "float",
              "N1-H8-O4": "float"
            }
          }
        }
      },
      "description": "Optimized bond lengths (Å) and bond angles (°) from HF/6‑311++G(d,p) and B3LYP/6‑311++G(d,p) calculations. Every value is compared to the paper‑reported optimized parameters with an absolute tolerance."
    },
    {
      "file": "scaled_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "hf": "array of 57 floats",
          "b3lyp": "array of 57 floats"
        },
        "items": {
          "unit": "cm⁻¹"
        }
      },
      "description": "Scaled harmonic vibrational frequencies (cm⁻¹) for 57 normal modes, sorted in ascending order. The checker recomputes RMSE and Pearson R² against hidden experimental frequencies and verifies that the relative performance of the two methods matches the expected ranking."
    }
  ],
  "notes": "Scaling factors are provided in the public step description and must be applied. The initial molecular geometry is not provided; the agent builds connectivity from the formula (C5H7N2)(H2PO4). The score for geometric parameters uses an absolute tolerance; the frequency score uses recomputed RMSE/R² with trend requirements."
}
```

## How you are scored
A hidden verifier automatically scores each artifact you produce and combines the results into a single reward.

- **geometric_parameters.json**: Every bond length and bond angle is compared against reference values with absolute tolerances. Full credit is earned when all reported geometric parameters lie within the tolerance window.
- **scaled_frequencies.json**: The verifier recomputes the root-mean-square deviation (RMSD) and Pearson correlation coefficient (R²) between your submitted scaled frequencies and a hidden set of experimental IR frequencies. It then compares the two methods using these metrics. Credit is assigned based on whether your frequencies reproduce the correct relative performance (one method yielding lower RMSD and higher R²) and whether the magnitudes are in the expected range.

No credit is given for simply reporting paper numbers; the verifier independently recomputes comparisons from your raw output files. Reproducing the correct trends and achieving accurate geometric parameters are equally important for earning the full reward.
