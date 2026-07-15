# DFT-based Elastic Moduli and Hardness Prediction of Zinc-Blende BP

## Problem background
Boron phosphide (BP) is a wide-band-gap semiconductor that crystallises in the zinc-blende structure. Because of its strong covalent bonding and structural analogy to cubic boron nitride, BP is a candidate for superhard applications. Predicting its intrinsic mechanical properties—elastic moduli, empirical hardness, and ideal tensile and shear strengths—from first-principles theory is essential for evaluating its performance limits. Density functional theory (DFT) provides a well-established route to compute these quantities from the crystal structure alone, without requiring experimental input. This task implements a complete DFT workflow to obtain the key mechanical descriptors of zinc-blende BP.

## Approach
The workflow is a series of plane-wave DFT calculations using the generalised-gradient approximation (GGA-PBE) and projector-augmented wave (PAW) pseudopotentials. Zinc-blende BP (space group F-43m, initial lattice parameter approximately 4.540 Å) is first relaxed to find its equilibrium lattice constant. From the optimised structure, single-crystal elastic constants C11, C12, C44 are obtained by applying small deformations and extracting the stress–strain relation. The polycrystalline bulk and shear moduli are then derived via Voigt–Reuss–Hill averaging, giving the Pugh ratio k = G_V / B_V. The Chen empirical Vickers hardness follows as H_V = 2 (k^2 G_V)^0.585 − 3. Finally, ideal strengths are studied by imposing incremental uniaxial tensile strains along [100], [110], [111] and pure shear strains on the (110)[001], (100)[010], (111)[11-2] slip systems; stress is recorded at each step, generating stress–strain curves that capture strain stiffening up to fracture. The entire procedure is carried out with open-source DFT tools and publicly available pseudopotentials.

## Reproduction target
Predict the following mechanical properties for zinc-blende BP from first-principles DFT calculations:

1. Compute the equilibrium lattice constant, single-crystal elastic constants C11, C12, C44, Voigt–Reuss–Hill bulk modulus B_V, shear modulus G_V, the ratio k = G_V/B_V, and the Chen Vickers hardness H_V. Save these results in a JSON file `results.json`.

2. Simulate stress–strain curves for uniaxial tension along the [100], [110], [111] directions and for pure shear along the shear systems (110)[001], (100)[010], (111)[11-2]. Write the strain–stress data to a CSV file `stress_strain_curves.csv`.

The output files must strictly follow the schemas defined in the output contract below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSlibrary PAW pseudopotentials for B and P: https://dalcorso.github.io/pslibrary/

## Workflow steps

### Step 1: Geometry optimization of zinc-blende BP
- Role: process
- Action: Perform DFT geometry optimization for zinc-blende BP (cubic, space group F-43m, initial lattice parameter ≈4.540 Å) using GGA-PBE and PAW pseudopotentials. Relax atomic positions and cell dimensions to obtain equilibrium lattice constant and internal coordinates.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Elastic constants calculation
- Role: process
- Action: Using the optimized structure, compute single-crystal elastic constants C11, C12, C44 via the strain-energy method. Apply small deformations, relax internal atomic positions, and extract the stress–strain relationship.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 3: VRH averaging and Chen hardness prediction
- Role: scored
- Action: From the elastic constants, compute Voigt–Reuss–Hill polycrystalline bulk modulus B_V, shear modulus G_V, ratio k = G_V/B_V, and predicted Vickers hardness H_V = 2(k^2 G_V)^0.585 − 3. Write all derived quantities along with the computed elastic constants and lattice constant to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: lattice_constant_A (float, Å), C11, C12, C44, B_V, G_V, k, H_V (all float, GPa).
- Scoring: scored by hidden verifier

### Step 4: Ideal tensile and shear strength simulations
- Role: scored (load-bearing)
- Action: Using the optimized structure, perform DFT calculations to generate stress–strain curves for uniaxial tensile deformations along [100], [110], [111] and pure shear deformations on (110)[001], (100)[010], (111)[11-2] systems. Increase strain in small steps until fracture, recording stress at each strain. Write all data to stress_strain_curves.csv.
- Output file: `/app/outputs/stress_strain_curves.csv`
- Format: csv
- Contract: CSV with columns: deformation_mode (string), strain (float, dimensionless), stress (float, GPa). Modes include: tensile_100, tensile_110, tensile_111, shear_110_001, shear_100_010, shear_111_11-2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/stress_strain_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic constants (C11,C12,C44), Voigt-Reuss-Hill bulk and shear moduli (B_V,G_V), Pugh ratio k, and Chen-predicted Vickers hardness H_V for zinc-blende BP.
- schema:
  - `type`: object
  - `properties`:
    - `lattice_constant_A`:
      - `type`: number
      - `unit`: Å
    - `C11`:
      - `type`: number
      - `unit`: GPa
    - `C12`:
      - `type`: number
      - `unit`: GPa
    - `C44`:
      - `type`: number
      - `unit`: GPa
    - `B_V`:
      - `type`: number
      - `unit`: GPa
    - `G_V`:
      - `type`: number
      - `unit`: GPa
    - `k`:
      - `type`: number
      - `unit`: dimensionless
    - `H_V`:
      - `type`: number
      - `unit`: GPa
  - `required`: `lattice_constant_A`, `C11`, `C12`, `C44`, `B_V`, `G_V`, `k`, `H_V`

### stress_strain_curves.csv
- path: `/app/outputs/stress_strain_curves.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Stress-strain curves for uniaxial tensile and pure shear deformations. The deformation_mode column identifies the loading direction (tensile_100, tensile_110, tensile_111, shear_110_001, shear_100_010, shear_111_11-2).
- schema:
  - `type`: table
  - `columns`: `deformation_mode`, `strain`, `stress`
  - `column_types`:
    - `deformation_mode`: string
    - `strain`: number (dimensionless)
    - `stress`: number (GPa)
  - `required_columns`: `deformation_mode`, `strain`, `stress`

Notes: Hidden checker recomputes derived quantities from elastic_constants.json (evidence from step_02) to verify results.json. It also extracts maximum stress per deformation mode from stress_strain_curves.csv and compares minimum strengths to paper gold with tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "lattice_constant_A": {
            "type": "number",
            "unit": "Å"
          },
          "C11": {
            "type": "number",
            "unit": "GPa"
          },
          "C12": {
            "type": "number",
            "unit": "GPa"
          },
          "C44": {
            "type": "number",
            "unit": "GPa"
          },
          "B_V": {
            "type": "number",
            "unit": "GPa"
          },
          "G_V": {
            "type": "number",
            "unit": "GPa"
          },
          "k": {
            "type": "number",
            "unit": "dimensionless"
          },
          "H_V": {
            "type": "number",
            "unit": "GPa"
          }
        },
        "required": [
          "lattice_constant_A",
          "C11",
          "C12",
          "C44",
          "B_V",
          "G_V",
          "k",
          "H_V"
        ]
      },
      "description": "Elastic constants (C11,C12,C44), Voigt-Reuss-Hill bulk and shear moduli (B_V,G_V), Pugh ratio k, and Chen-predicted Vickers hardness H_V for zinc-blende BP."
    },
    {
      "file": "stress_strain_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "columns": [
          "deformation_mode",
          "strain",
          "stress"
        ],
        "column_types": {
          "deformation_mode": "string",
          "strain": "number (dimensionless)",
          "stress": "number (GPa)"
        },
        "required_columns": [
          "deformation_mode",
          "strain",
          "stress"
        ]
      },
      "description": "Stress-strain curves for uniaxial tensile and pure shear deformations. The deformation_mode column identifies the loading direction (tensile_100, tensile_110, tensile_111, shear_110_001, shear_100_010, shear_111_11-2)."
    }
  ],
  "notes": "Hidden checker recomputes derived quantities from elastic_constants.json (evidence from step_02) to verify results.json. It also extracts maximum stress per deformation mode from stress_strain_curves.csv and compares minimum strengths to paper gold with tolerance."
}
```

## How you are scored
A hidden verifier examines the submitted artefacts. For `results.json`, the verifier recomputes the derived moduli (B_V, G_V, k, H_V) from the elastic constants and compares them to reference values with appropriate tolerances; it also checks that the lattice constant and elastic constants are physically reasonable and internally consistent with the evidence file `elastic_constants.json`. For `stress_strain_curves.csv`, the verifier extracts the maximum stress for each deformation mode and verifies that each stress–strain curve shows monotonic increase to a peak (strain stiffening) before failure. The final score is a weighted combination of the partial scores from both artefacts. Reporting numbers without executing the DFT workflow will not pass, because the verifier validates internal consistency and curve shapes that cannot be guessed from prior knowledge alone.
