# DFT elastic constants and mechanical moduli of superconducting MAX phases Ti2InC and Ti2InN

## Problem background
Superconducting MAX phases Ti₂InC and Ti₂InN are nanolaminate ceramics that combine metallic conductivity with ceramic stiffness. Their mechanical behaviour—elastic stiffness, shear anisotropy, and the balance between brittleness and quasi-ductility—is critical for potential coating and structural applications. First-principles density functional theory (DFT) can compute the second-order elastic constants of these hexagonal crystals and derive polycrystalline mechanical moduli, allowing the brittle or ductile character to be assessed via the empirical G/B ratio criterion. This task requires computing those elastic constants and derived moduli for both compounds from first principles and determining whether each material is brittle or ductile according to the G/B criterion.

## Approach
The reproduction uses an open‑source plane‑wave pseudopotential DFT code (e.g., Quantum ESPRESSO) with the GGA‑PBE exchange‑correlation functional. Starting from the hexagonal crystal structures (space group P6₃/mmc, Wyckoff positions Ti at 4f, In at 2d, C/N at 2a), a full geometry optimization is performed to relax lattice parameters and atomic positions. Using the relaxed structures, small symmetry‑adapted strains are applied and the resulting stress tensors are computed to extract the five independent second‑order elastic stiffness constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄. From these constants, the polycrystalline mechanical moduli are derived using standard Voigt‑Reuss‑Hill averaging: bulk modulus B, shear modulus G, Young’s modulus Y, Poisson’s ratio ν, shear anisotropy A = 2·C₄₄/(C₁₁ − C₁₂), and the compressibility ratio kc/ka = (C₁₁ + C₁₂ − 2·C₁₃)/(C₃₃ − C₁₃). The G/B ratio is then used to classify each compound: G/B > 0.5 indicates brittle behaviour, while G/B < 0.5 indicates ductile behaviour. All computed quantities are written to structured CSV and text output files.

## Reproduction target
For both Ti₂InC and Ti₂InN, compute and output:
- The five independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ (in GPa) as a single-row CSV file per compound.
- The derived polycrystalline mechanical moduli B, G, Y, ν, A, kc/ka, and the G/B ratio (B, G, Y in GPa; others dimensionless) as a single-row CSV file per compound.
- A plain text file that states for each compound whether it is brittle or ductile according to the computed G/B ratio, including the numerical G/B value.
The goal is to reproduce the elastic and mechanical characterisation consistent with the published DFT study of these MAX phases, using only the publicly available crystal structures and open‑source DFT tools.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Ti, In, C, N: https://www.materialscloud.org/discover/sssp/table/efficiency
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Geometry optimization of Ti₂InC and Ti₂InN
- Role: process
- Action: Perform DFT geometry optimization of Ti₂InC and Ti₂InN starting from the hexagonal crystal structures (space group P6₃/mmc, Wyckoff positions: Ti at 4f, In at 2d, X at 2a). Relax lattice parameters and atomic positions using GGA-PBE. This provides the relaxed structures required for the elastic‑constants calculation.
- Evidence: `/app/outputs/geometry_optimization.out`

### Step 2: Elastic constants of Ti₂InC
- Role: scored (load-bearing)
- Action: Using the relaxed structure of Ti₂InC, apply small symmetry-adapted strains, compute the resulting stress tensor via DFT, and extract the second-order elastic stiffness constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ (in GPa). Write these five constants to a CSV file.
- Output file: `/app/outputs/step_01_elastic_constants_Ti2InC.csv`
- Format: csv
- Contract: Columns: C11, C12, C13, C33, C44. All values are floating-point numbers in units of GPa.
- Scoring: scored by hidden verifier

### Step 3: Elastic constants of Ti₂InN
- Role: scored (load-bearing)
- Action: Using the relaxed structure of Ti₂InN, apply small symmetry-adapted strains, compute the resulting stress tensor via DFT, and extract the second-order elastic stiffness constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ (in GPa). Write these five constants to a CSV file.
- Output file: `/app/outputs/step_01_elastic_constants_Ti2InN.csv`
- Format: csv
- Contract: Columns: C11, C12, C13, C33, C44. All values are floating-point numbers in units of GPa.
- Scoring: scored by hidden verifier

### Step 4: Derived mechanical moduli of Ti₂InC
- Role: scored
- Action: From the elastic constants of Ti₂InC, compute the polycrystalline mechanical moduli: bulk modulus B, shear modulus G, Young's modulus Y, Poisson's ratio ν, shear anisotropy A = 2·C₄₄/(C₁₁–C₁₂), compressibility ratio kc/ka = (C₁₁+C₁₂–2·C₁₃)/(C₃₃–C₁₃), and the G/B ratio. Output them to a CSV file.
- Output file: `/app/outputs/step_02_derived_moduli_Ti2InC.csv`
- Format: csv
- Contract: Columns: B, G, Y, nu, A, kc_ka, G_B. B, G, Y in GPa (float); nu, A, kc_ka, G_B are dimensionless floats.
- Scoring: scored by hidden verifier

### Step 5: Derived mechanical moduli of Ti₂InN
- Role: scored
- Action: From the elastic constants of Ti₂InN, compute the polycrystalline mechanical moduli: bulk modulus B, shear modulus G, Young's modulus Y, Poisson's ratio ν, shear anisotropy A = 2·C₄₄/(C₁₁–C₁₂), compressibility ratio kc/ka = (C₁₁+C₁₂–2·C₁₃)/(C₃₃–C₁₃), and the G/B ratio. Output them to a CSV file.
- Output file: `/app/outputs/step_02_derived_moduli_Ti2InN.csv`
- Format: csv
- Contract: Columns: B, G, Y, nu, A, kc_ka, G_B. B, G, Y in GPa (float); nu, A, kc_ka, G_B are dimensionless floats.
- Scoring: scored by hidden verifier

### Step 6: Brittle/ductile classification
- Role: scored (load-bearing)
- Action: Based on the G/B ratios from the derived moduli, classify each compound: if G/B > 0.5 the material is brittle; if G/B < 0.5 it is ductile. Summarize the classification for Ti₂InC and Ti₂InN in a plain text file, one line per compound in the format 'Ti2InX: <brittle|ductile> (G/B = <number>)' (e.g., 'Ti2InC: brittle (G/B = 0.XX)').
- Output file: `/app/outputs/step_03_classification.txt`
- Format: txt
- Contract: Two lines of free text each containing the compound name, the classification word ('brittle', 'ductile', or 'near borderline'), and the G/B value in parentheses.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_elastic_constants_Ti2InC.csv`
- `/app/outputs/step_01_elastic_constants_Ti2InN.csv`
- `/app/outputs/step_02_derived_moduli_Ti2InC.csv`
- `/app/outputs/step_02_derived_moduli_Ti2InN.csv`
- `/app/outputs/step_03_classification.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_elastic_constants_Ti2InC.csv
- path: `/app/outputs/step_01_elastic_constants_Ti2InC.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ for Ti₂InC.
- schema:
  - `type`: table
  - `required_columns`: `C11`, `C12`, `C13`, `C33`, `C44`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa

### step_01_elastic_constants_Ti2InN.csv
- path: `/app/outputs/step_01_elastic_constants_Ti2InN.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ for Ti₂InN.
- schema:
  - `type`: table
  - `required_columns`: `C11`, `C12`, `C13`, `C33`, `C44`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa

### step_02_derived_moduli_Ti2InC.csv
- path: `/app/outputs/step_02_derived_moduli_Ti2InC.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived polycrystalline mechanical moduli for Ti₂InC.
- schema:
  - `type`: table
  - `required_columns`: `B`, `G`, `Y`, `nu`, `A`, `kc_ka`, `G_B`
  - `units`:
    - `B`: GPa
    - `G`: GPa
    - `Y`: GPa
    - `nu`: dimensionless
    - `A`: dimensionless
    - `kc_ka`: dimensionless
    - `G_B`: dimensionless

### step_02_derived_moduli_Ti2InN.csv
- path: `/app/outputs/step_02_derived_moduli_Ti2InN.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived polycrystalline mechanical moduli for Ti₂InN.
- schema:
  - `type`: table
  - `required_columns`: `B`, `G`, `Y`, `nu`, `A`, `kc_ka`, `G_B`
  - `units`:
    - `B`: GPa
    - `G`: GPa
    - `Y`: GPa
    - `nu`: dimensionless
    - `A`: dimensionless
    - `kc_ka`: dimensionless
    - `G_B`: dimensionless

### step_03_classification.txt
- path: `/app/outputs/step_03_classification.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Brittle/ductile classification for Ti₂InC and Ti₂InN based on computed G/B ratios.
- schema:
  - `type`: text
  - `required`: object

Notes: The hidden check compares reported elastic constants and moduli to paper Table 2 with a relative tolerance; the classification text must be consistent with the G/B values computed from the submitted moduli.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_elastic_constants_Ti2InC.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "C11",
          "C12",
          "C13",
          "C33",
          "C44"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ for Ti₂InC."
    },
    {
      "file": "step_01_elastic_constants_Ti2InN.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "C11",
          "C12",
          "C13",
          "C33",
          "C44"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄ for Ti₂InN."
    },
    {
      "file": "step_02_derived_moduli_Ti2InC.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "B",
          "G",
          "Y",
          "nu",
          "A",
          "kc_ka",
          "G_B"
        ],
        "units": {
          "B": "GPa",
          "G": "GPa",
          "Y": "GPa",
          "nu": "dimensionless",
          "A": "dimensionless",
          "kc_ka": "dimensionless",
          "G_B": "dimensionless"
        }
      },
      "description": "Derived polycrystalline mechanical moduli for Ti₂InC."
    },
    {
      "file": "step_02_derived_moduli_Ti2InN.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "B",
          "G",
          "Y",
          "nu",
          "A",
          "kc_ka",
          "G_B"
        ],
        "units": {
          "B": "GPa",
          "G": "GPa",
          "Y": "GPa",
          "nu": "dimensionless",
          "A": "dimensionless",
          "kc_ka": "dimensionless",
          "G_B": "dimensionless"
        }
      },
      "description": "Derived polycrystalline mechanical moduli for Ti₂InN."
    },
    {
      "file": "step_03_classification.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {}
      },
      "description": "Brittle/ductile classification for Ti₂InC and Ti₂InN based on computed G/B ratios."
    }
  ],
  "notes": "The hidden check compares reported elastic constants and moduli to paper Table 2 with a relative tolerance; the classification text must be consistent with the G/B values computed from the submitted moduli."
}
```

## How you are scored
A hidden verifier will independently score each of the five output artifacts. The elastic constant CSVs and derived moduli CSVs are compared against reference values for the same quantities, and each holds a material share of the reward. The classification text file is checked for consistency with the computed G/B values. Reporting plausible numbers alone is not sufficient; the hidden check expects values that reflect a genuine DFT re‑run with the described protocol. The final reward (0–1) is the weighted sum of the scores from the individual artifacts.
