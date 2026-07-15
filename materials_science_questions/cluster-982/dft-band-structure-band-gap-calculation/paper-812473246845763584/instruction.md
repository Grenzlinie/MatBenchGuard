# DFT Calculation of Band Gap and Stability for a 2D Carbon Nitride Material

## Problem background
Two-dimensional (2D) carbon nitride materials offer opportunities for nanoelectronics and optoelectronics. This work examines a pentagon-based graphyne derivative, ID-GY, formed by linking imidazole molecules with acetylenic groups. The material is proposed to have a direct band gap, dynamic stability, anisotropic mechanical properties, and strong near-infrared refraction. To evaluate these properties, this task asks you to compute, from first‑principles, the electronic band gap, the in‑plane elastic constants, the derived Young's modulus along the diagonal direction, and the phonon stability of the ID‑GY sheet.

## Approach
The computational protocol uses density functional theory (DFT). First, you will construct the ID‑GY crystal structure (tetragonal P4/mbm space group, lattice parameters a = b ≈ 12.14 Å, 40 atoms per unit cell) and perform a geometry optimization with the PBE exchange‑correlation functional. On the relaxed structure you will then: (1) compute the direct band gap with the hybrid HSE06 functional; (2) extract the in‑plane elastic stiffness constants C11, C12, C66 through finite‑strain energy‑strain analysis; (3) calculate the phonon dispersion via density functional perturbation theory (DFPT) with the Phonopy code and record the minimum phonon frequency; (4) derive the Young's modulus along the diagonal direction (θ = 45°) from the elastic constants using the anisotropic elasticity relation for a 2D sheet. All steps are executed with open‑source tools and public pseudopotentials, making the pipeline fully reproducible.

## Reproduction target
Your task is to produce the following quantities for the ID‑GY monolayer: the direct band gap (in eV) at the HSE06 level of theory; the independent in‑plane elastic constants C11, C12, and C66 (in N/m); the Young's modulus along the diagonal direction (in N/m) computed from those constants; and the minimum phonon frequency across the entire Brillouin zone (in THz). The phonon minimum is used to check dynamic stability: a non‑negative value (no imaginary frequencies) confirms that the structure is dynamically stable. All results must be written to the specified output files under /app/outputs as described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP precision pseudopotential library: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Geometry optimization of ID-GY
- Role: process
- Action: Construct the ID-GY crystal structure as described (tetragonal P4/mbm, a=b=12.14 Å, 40 atoms per unit cell) and perform DFT geometry optimization with the PBE functional to obtain the relaxed lattice parameters and atomic positions.
- Evidence: none

### Step 2: Compute HSE06 direct band gap
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, perform a hybrid-functional (HSE06) electronic band structure calculation. Identify the valence band maximum (VBM) and conduction band minimum (CBM) at the same k-point; compute the direct band gap and write the value in eV.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: A single floating-point number representing the band gap in eV.
- Scoring: scored by hidden verifier

### Step 3: Compute phonon minimum frequency
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, build a supercell and compute the phonon dispersion across the first Brillouin zone via density functional perturbation theory (DFPT) with Phonopy. Determine the minimum phonon frequency (in THz). If all modes are real (≥ 0), output the lowest positive frequency; if any imaginary mode exists, output a negative value.
- Output file: `/app/outputs/phonon_min_frequency.txt`
- Format: txt
- Contract: A single floating-point number representing the minimum phonon frequency in THz. A non‑negative value indicates dynamical stability; a negative value indicates the presence of imaginary frequencies.
- Scoring: scored by hidden verifier

### Step 4: Compute elastic constants
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, apply finite strains and perform energy‑strain analysis to extract the independent in‑plane elastic stiffness components C11, C22 (=C11), C12, and C66 for the 2D sheet. Write the values (in N/m) as a JSON object.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: A JSON object with keys C11, C12, C66, each mapping to a floating‑point number in units of N/m.
- Scoring: scored by hidden verifier

### Step 5: Compute diagonal Young's modulus
- Role: scored
- Action: From the elastic constants obtained in the previous step, compute the Young's modulus along the diagonal direction (θ = 45°) using the analytical expression for anisotropic 2D materials. Write the result in N/m.
- Output file: `/app/outputs/young_modulus_diagonal.txt`
- Format: txt
- Contract: A single floating-point number representing Young's modulus in N/m.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/young_modulus_diagonal.txt`
- `/app/outputs/phonon_min_frequency.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Direct band gap of ID-GY computed at the HSE06 level. The checker compares this value to the paper‑reported band gap with a tolerance that accounts for code/functional differences.
- schema:
  - `type`: text
  - `units`: eV
  - `description`: A single floating-point number representing the direct band gap at HSE06 level.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Independent in-plane elastic stiffness constants of ID-GY. Each constant is compared to the paper's reported value with a tolerance.
- schema:
  - `type`: object
  - `required`: `C11`, `C12`, `C66`
  - `properties`:
    - `C11`:
      - `type`: number
      - `units`: N/m
    - `C12`:
      - `type`: number
      - `units`: N/m
    - `C66`:
      - `type`: number
      - `units`: N/m

### young_modulus_diagonal.txt
- path: `/app/outputs/young_modulus_diagonal.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Young's modulus along the diagonal direction derived from the elastic constants. The checker compares this value to the paper-derived reference with a tolerance.
- schema:
  - `type`: text
  - `units`: N/m
  - `description`: A single floating-point number representing the Young's modulus along the diagonal direction.

### phonon_min_frequency.txt
- path: `/app/outputs/phonon_min_frequency.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Minimum phonon frequency. The checker verifies that the value is non-negative (threshold = 0), confirming the absence of imaginary modes and thus dynamical stability. A value >= 0 earns full reward; a negative value indicates imaginary modes and a reduced score.
- schema:
  - `type`: text
  - `units`: THz
  - `description`: A single floating-point number representing the minimum phonon frequency across the Brillouin zone.

Notes: All outputs are scored. The checker compares band gap, elastic constants, and Young's modulus to the paper's reported values with tolerances set to absorb typical toolchain differences when using Quantum ESPRESSO and PBE pseudopotentials. The phonon minimum is checked for non-negativity to verify the dynamic stability claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "eV",
        "description": "A single floating-point number representing the direct band gap at HSE06 level."
      },
      "description": "Direct band gap of ID-GY computed at the HSE06 level. The checker compares this value to the paper‑reported band gap with a tolerance that accounts for code/functional differences."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "C11",
          "C12",
          "C66"
        ],
        "properties": {
          "C11": {
            "type": "number",
            "units": "N/m"
          },
          "C12": {
            "type": "number",
            "units": "N/m"
          },
          "C66": {
            "type": "number",
            "units": "N/m"
          }
        }
      },
      "description": "Independent in-plane elastic stiffness constants of ID-GY. Each constant is compared to the paper's reported value with a tolerance."
    },
    {
      "file": "young_modulus_diagonal.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "N/m",
        "description": "A single floating-point number representing the Young's modulus along the diagonal direction."
      },
      "description": "Young's modulus along the diagonal direction derived from the elastic constants. The checker compares this value to the paper-derived reference with a tolerance."
    },
    {
      "file": "phonon_min_frequency.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": "THz",
        "description": "A single floating-point number representing the minimum phonon frequency across the Brillouin zone."
      },
      "description": "Minimum phonon frequency. The checker verifies that the value is non-negative (threshold = 0), confirming the absence of imaginary modes and thus dynamical stability. A value >= 0 earns full reward; a negative value indicates imaginary modes and a reduced score."
    }
  ],
  "notes": "All outputs are scored. The checker compares band gap, elastic constants, and Young's modulus to the paper's reported values with tolerances set to absorb typical toolchain differences when using Quantum ESPRESSO and PBE pseudopotentials. The phonon minimum is checked for non-negativity to verify the dynamic stability claim."
}
```

## How you are scored
A hidden verifier independently examines each output file. For the band gap, elastic constants, and Young's modulus, the verifier compares your computed values against reference values that originate from the original DFT study, using tolerances that account for expected differences between quantum‑chemical codes, functionals, and pseudopotentials. For the phonon minimum frequency, the verifier applies a threshold check: it verifies that the value is non‑negative (≥ 0), which confirms the absence of imaginary modes and indicates dynamical stability. The final reward is a weighted combination of the scores from each artifact. Reporting numbers without performing the required computations will not yield a passing score.
