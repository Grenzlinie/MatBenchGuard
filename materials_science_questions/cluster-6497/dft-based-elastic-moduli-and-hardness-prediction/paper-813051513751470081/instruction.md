# First-principles elastic constants and derived mechanical properties of naphthalene

## Problem background
Predicting the elastic and acoustic properties of organic molecular crystals such as naphthalene and anthracene from first principles is important for understanding their mechanical behavior, which in turn relates to coal science and materials engineering. Density functional theory (DFT) calculations can provide elastic constants, but different exchange‑correlation functionals exhibit systematic biases: the local density approximation (LDA) tends to overestimate elastic moduli, while the generalized gradient approximation (PBE) underestimates them. This work investigates whether a simple empirical averaging protocol that combines the LDA and PBE results can give a more reliable description of the elastic, mechanical, and acoustic properties of the P2_1/a phase of naphthalene.

## Approach
The reproduction uses an open‑source DFT code to compute the elastic stiffness tensor of the naphthalene P2_1/a crystal from first principles. Two separate calculations are performed: one with the PBE functional and one with the LDA functional. The 13 independent elastic constants obtained are then arithmetically averaged to produce a (PBE+LDA)/2 set. For each of the three sets (LDA, PBE, PL/2), the Voigt‑Reuss‑Hill (VRH) averaging scheme is applied to estimate isotropic polycrystalline bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and Vickers hardness. Using these moduli and the crystal density derived from the optimized structure, longitudinal and transverse sound velocities, the average velocity, Debye temperature, and the acoustic Grüneisen parameter are computed. The input crystal structure is the experimental P2_1/a naphthalene structure from the Cambridge Structural Database (refcode NAPHTA01), corresponding to structure published in J. Phys. Chem. A 110, 11695 (2006).

## Reproduction target
For the naphthalene P2_1/a phase, compute the 13 independent elastic constants C11, C22, C33, C12, C13, C23, C44, C55, C66, C15, C25, C35, C46 (in GPa) using DFT with the LDA and PBE functionals, and produce the arithmetic mean (PBE+LDA)/2 for each constant. Using the Voigt‑Reuss‑Hill model, derive the polycrystalline bulk modulus (B), shear modulus (G), Young's modulus (E), Poisson's ratio (μ), and Vickers hardness (H) for LDA, PBE, and PL/2. From these, compute the longitudinal (v_p), transverse (v_s), and average (<v>) sound velocities, the Debye temperature (Θ_D), and the acoustic Grüneisen parameter (γ_a) for each functional. Report all values in the specified CSV files. The hidden verifier will assess the internal consistency of the VRH derivation and compare your computed results against experimental reference data.

## Assets

- Naphthalene P2_1/a crystal structure: 10.1021/jp0614370
- Open-source DFT code with LDA and PBE functionals: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: DFT geometry optimization and elastic constants – PBE
- Role: process
- Action: Perform full geometry optimization of naphthalene P2_1/a using the PBE functional, followed by calculation of the elastic stiffness tensor from energy‑strain expansions.
- Evidence: `/app/outputs/pbe_elastic_calc.log`

### Step 2: DFT geometry optimization and elastic constants – LDA
- Role: process
- Action: Perform the same calculations as step 1 but using the LDA functional.
- Evidence: `/app/outputs/lda_elastic_calc.log`

### Step 3: Assemble elastic constants table
- Role: scored (load-bearing)
- Action: Extract the 13 independent elastic constants (C11, C22, C33, C12, C13, C23, C44, C55, C66, C15, C25, C35, C46) for LDA and PBE from the DFT runs. Compute the arithmetic average (PBE+LDA)/2 for each constant. Collect the values into a single table.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: functional: str; C11,C22,C33,C12,C13,C23,C44,C55,C66,C15,C25,C35,C46: float
- Scoring: scored by hidden verifier

### Step 4: Compute polycrystalline mechanical properties
- Role: scored
- Action: From the elastic constants in step 3, apply the Voigt-Reuss-Hill averaging scheme to compute the isotropic polycrystalline bulk modulus (B), shear modulus (G), Young's modulus (E), Poisson's ratio (mu), and Vickers hardness (H) for each functional (LDA, PBE, PL/2). Use standard VRH formulas.
- Output file: `/app/outputs/mechanical_properties.csv`
- Format: csv
- Contract: functional: str; B,G,E,H (GPa): float; mu: float
- Scoring: scored by hidden verifier

### Step 5: Compute acoustic properties
- Role: scored
- Action: Using the bulk and shear moduli from step 4 and the crystal density (from the optimized PL/2 volume), compute longitudinal (v_p), transverse (v_s), and average sound velocities, the Debye temperature, and the acoustic Grüneisen parameter for each functional.
- Output file: `/app/outputs/acoustic_properties.csv`
- Format: csv
- Contract: functional: str; v_s,v_p,v_avg (m/s): float; Theta_D (K): float; gamma_a: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/mechanical_properties.csv`
- `/app/outputs/acoustic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constants for LDA, PBE, and PL/2 for naphthalene P2_1/a.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `C11`, `C22`, `C33`, `C12`, `C13`, `C23`, `C44`, `C55`, `C66`, `C15`, `C25`, `C35`, `C46`
  - `units`:
    - `C11`: GPa
    - `C22`: GPa
    - `C33`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C23`: GPa
    - `C44`: GPa
    - `C55`: GPa
    - `C66`: GPa
    - `C15`: GPa
    - `C25`: GPa
    - `C35`: GPa
    - `C46`: GPa

### mechanical_properties.csv
- path: `/app/outputs/mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline bulk, shear, Young's moduli, Poisson ratio, and Vickers hardness from VRH averaging.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `B`, `G`, `E`, `mu`, `H`
  - `units`:
    - `B`: GPa
    - `G`: GPa
    - `E`: GPa
    - `mu`: dimensionless
    - `H`: GPa

### acoustic_properties.csv
- path: `/app/outputs/acoustic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sound velocities, Debye temperature, and acoustic Grüneisen parameter.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `v_s`, `v_p`, `v_avg`, `Theta_D`, `gamma_a`
  - `units`:
    - `v_s`: m/s
    - `v_p`: m/s
    - `v_avg`: m/s
    - `Theta_D`: K
    - `gamma_a`: dimensionless

Notes: The PL/2 values are compared to the paper’s PL/2 results and to experimental references. The hidden checker verifies that the PL/2 elastic constants are within tolerance of the paper-reported values and that PL/2 absolute errors relative to experiment are lower than those for LDA and PBE.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "C11",
          "C22",
          "C33",
          "C12",
          "C13",
          "C23",
          "C44",
          "C55",
          "C66",
          "C15",
          "C25",
          "C35",
          "C46"
        ],
        "units": {
          "C11": "GPa",
          "C22": "GPa",
          "C33": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C23": "GPa",
          "C44": "GPa",
          "C55": "GPa",
          "C66": "GPa",
          "C15": "GPa",
          "C25": "GPa",
          "C35": "GPa",
          "C46": "GPa"
        }
      },
      "description": "Elastic constants for LDA, PBE, and PL/2 for naphthalene P2_1/a."
    },
    {
      "file": "mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "B",
          "G",
          "E",
          "mu",
          "H"
        ],
        "units": {
          "B": "GPa",
          "G": "GPa",
          "E": "GPa",
          "mu": "dimensionless",
          "H": "GPa"
        }
      },
      "description": "Polycrystalline bulk, shear, Young's moduli, Poisson ratio, and Vickers hardness from VRH averaging."
    },
    {
      "file": "acoustic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "v_s",
          "v_p",
          "v_avg",
          "Theta_D",
          "gamma_a"
        ],
        "units": {
          "v_s": "m/s",
          "v_p": "m/s",
          "v_avg": "m/s",
          "Theta_D": "K",
          "gamma_a": "dimensionless"
        }
      },
      "description": "Sound velocities, Debye temperature, and acoustic Grüneisen parameter."
    }
  ],
  "notes": "The PL/2 values are compared to the paper’s PL/2 results and to experimental references. The hidden checker verifies that the PL/2 elastic constants are within tolerance of the paper-reported values and that PL/2 absolute errors relative to experiment are lower than those for LDA and PBE."
}
```

## How you are scored
A hidden verifier reads your output CSV files and independently recomputes the Voigt‑Reuss‑Hill derived moduli and properties from the elastic constants you reported to check internal consistency and correct use of the VRH formulas. It then compares your computed PL/2 elastic constants and derived properties against experimental reference values, and further checks whether the absolute errors of the PL/2 results relative to those experimental references are consistently smaller than the errors for LDA and PBE. The reward is a weighted combination of these checks, with the primary weight on the correctness and consistency of the elastic constants and the derived mechanical properties. The acoustic properties also contribute. Reporting the paper's numbers without actually running the DFT and VRH computations will not pass the consistency checks.
