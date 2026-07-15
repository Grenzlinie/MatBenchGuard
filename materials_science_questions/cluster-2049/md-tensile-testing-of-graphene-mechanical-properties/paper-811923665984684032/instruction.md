# Vibrational Behavior of Single-Layered Graphene Sheets as Strain Sensors

## Problem background
Single-layered graphene sheets (SLGSs) are atomically thin two-dimensional membranes whose mechanical vibrations are highly sensitive to applied deformation, making them candidates for nanoscale strain sensors. Understanding how the fundamental vibrational frequency depends on sheet geometry, chirality, and uniaxial tensile strain is crucial for sensor design. Molecular structural mechanics (MSM) offers an atomistic modelling pathway: covalent bonds are replaced by equivalent elastic beams and carbon atoms by lumped masses, enabling efficient eigenfrequency analysis of nanometer-thick plates.

## Approach
The core modelling approach treats an SLGS as a space-frame structure. Carbon‑carbon covalent bonds are represented by elastic beams whose cross-sectional diameter, Young's modulus, and shear modulus are derived from three interatomic force constants (bond stretching, angle bending, torsional stiffness) and the equilibrium C–C bond length. Carbon nuclei are modelled as concentrated masses at the beam joints. For each geometry (side length, width, chirality: zigzag or armchair) and each uniaxial tensile strain, the honeycomb lattice is built with clamped-clamped edges. Global mass and stiffness matrices are assembled, static condensation is applied, and the fundamental frequency is obtained by solving the eigenvalue problem. Strain is applied by elongating the side along which the tension acts while keeping the perpendicular width constant. This simulation is repeated over a matrix of side lengths, aspect ratios, chiralities, and strain levels to map the frequency response.

## Reproduction target
Compute the fundamental vibrational frequency (in GHz) for every combination of:
- Side lengths a = 5.9070, 8.5260, 14.4972 nm, each in zigzag (a/b = 0.8660) and armchair (a/b = 1.1547) chiralities;
- For the zigzag sheet with a = 8.5260 nm and the armchair sheet with a = 7.8760 nm, additionally vary the aspect ratio a/b over a representative set covering 0.2165 to 3.8490;
- For all geometries, apply uniaxial tensile strains ε = 0, 0.01, 0.03, 0.05, 0.07 (stretch side a by ε, keep b fixed).
Write the results to `frequencies.csv` with columns `side_length_nm`, `width_nm`, `aspect_ratio`, `chirality`, `strain_fraction`, `frequency_ghz`. The verification will compare your computed frequencies to hidden reference values and evaluate consistency with physical expectations (details not disclosed).

## Assets

- SciPy (sparse linear algebra and eigensolvers): pip install scipy

## Workflow steps

### Step 1: Compute Equivalent Beam Properties
- Role: process
- Action: Calculate the equivalent structural beam cross-sectional diameter (d), Young's modulus (E), and shear modulus (G) from the interatomic force constants (k_r = 6.52e-7 N/nm, k_theta = 8.76e-10 N nm/rad^2, k_phi = 2.78e-10 N nm/rad^2) and the carbon–carbon bond length (L = 0.142 nm) using the molecular structural mechanics equivalence relations for a circular cross-section (without writing the closed-form expressions).
- Evidence: none

### Step 2: Compute SLGS Fundamental Frequencies
- Role: scored (load-bearing)
- Action: For the following geometries and conditions: base side lengths a = 5.9070, 8.5260, 14.4972 nm, each modelled for both zigzag and armchair chiralities; for zigzag use aspect ratio a/b = 0.8660, for armchair use a/b = 1.1547. Additionally, for the zigzag sheet with a = 8.5260 nm and the armchair sheet with a = 7.8760 nm, vary the aspect ratio over the range [0.2165, 3.8490] (choose at least a representative set). For every geometry, apply uniaxial tensile strains of 0, 0.01, 0.03, 0.05, 0.07 (increase side a by strain fraction, keep b fixed). For each case: construct the honeycomb lattice with clamped-clamped edges, assign beam elements with the beam properties from step_01 and lumped carbon atom masses (m_c = 1.9943e-23 g), assemble global mass and stiffness matrices, perform static condensation, solve the eigenvalue problem to obtain the fundamental frequency, and write the result to `frequencies.csv`.
- Output file: `/app/outputs/frequencies.csv`
- Format: csv
- Contract: side_length_nm (float, nm), width_nm (float, nm), aspect_ratio (float, dimensionless), chirality (string, 'zigzag' or 'armchair'), strain_fraction (float, fraction), frequency_ghz (float, GHz)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies.csv
- path: `/app/outputs/frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed fundamental frequencies of single-layered graphene sheets for all geometry, chirality, aspect ratio, and strain levels specified in the workflow.
- schema:
  - `type`: table
  - `required_columns`: `side_length_nm`, `width_nm`, `aspect_ratio`, `chirality`, `strain_fraction`, `frequency_ghz`
  - `units`:
    - `side_length_nm`: nm
    - `width_nm`: nm
    - `aspect_ratio`: dimensionless
    - `strain_fraction`: fraction
    - `frequency_ghz`: GHz

Notes: The checker will compare each reported frequency against hidden gold values within a tolerance and verify hidden consistency criteria (details not disclosed).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "side_length_nm",
          "width_nm",
          "aspect_ratio",
          "chirality",
          "strain_fraction",
          "frequency_ghz"
        ],
        "units": {
          "side_length_nm": "nm",
          "width_nm": "nm",
          "aspect_ratio": "dimensionless",
          "strain_fraction": "fraction",
          "frequency_ghz": "GHz"
        }
      },
      "description": "Computed fundamental frequencies of single-layered graphene sheets for all geometry, chirality, aspect ratio, and strain levels specified in the workflow."
    }
  ],
  "notes": "The checker will compare each reported frequency against hidden gold values within a tolerance and verify hidden consistency criteria (details not disclosed)."
}
```

## How you are scored
Your output will be evaluated by an automated hidden verifier. It parses `frequencies.csv` and compares your computed fundamental frequencies to expected target values within appropriate tolerances. It also verifies that your frequencies conform to hidden consistency criteria that any correct physical model would satisfy. The score (0 to 1) is computed from these checks. Simply reporting a number without having actually built and solved the molecular structural mechanics model will not satisfy these checks.
