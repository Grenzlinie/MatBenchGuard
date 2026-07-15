# First-Principles Structural and Energetic Analysis of ZrNi Hydrides

## Problem background
The intermetallic alloy ZrNi can absorb hydrogen, forming hydrides up to ZrNiH₃, and is of interest for hydrogen storage applications. A first-principles density functional theory (DFT) study can reveal how hydrogen uptake affects the crystal structure and energetics of the ZrNi system. Understanding the equilibrium geometries, binding energies, and bulk mechanical properties of the alloy and its hydrides (including hypothetical intermediate phases ZrNiH and ZrNiH₂) provides insight into the hydrogen absorption/desorption processes and the stability of different hydrogen coordination environments. In this task, you will compute the structural and energetic parameters of ZrNi and its hydrides using plane-wave DFT with the projector augmented wave (PAW) method and a Birch–Murnaghan equation of state (EOS) analysis. This will yield lattice constants, cell volumes, total energies, bulk moduli, and hydrogen stabilization energies that characterize the alloy-hydrogen system.

## Approach
The work adopts a plane-wave PAW formalism within the GGA-PBE exchange–correlation functional. The four target compounds—ZrNi, ZrNiH, ZrNiH₂, and ZrNiH₃—crystallize in the base-centered orthorhombic space group Cmcm (No. 63) with four formula units per conventional cell. Initial crystal structures are constructed from publicly available experimental data: ZrNi (Korst 1962) and ZrNiH₃ (Peterson et al. 1964); the hydrogen positions for the intermediate hydrides follow the reported sites: H₁ at the 4c Wyckoff position and H₂ at the 8f position. 
The computational procedure consists of three main stages: 
(1) Full relaxation of lattice parameters and internal atomic coordinates for all four systems using a DFT code capable of PAW-GGA calculations, yielding optimized structural parameters and the total electronic energy. 
(2) A reference energy calculation for an isolated H₂ molecule in a periodic box to serve as the energy baseline for hydrogen. 
(3) A series of single-point energy calculations at multiple volumes around the relaxed equilibrium to fit a second‑order Birch EOS for each composition, from which the equilibrium energy, equilibrium volume, and bulk modulus are derived. Finally, the hydrogen stabilization energy per H₂ molecule is computed from the fitted equilibrium energies and the H₂ reference.

## Reproduction target
Calculate and report the equilibrium lattice constants (a in Å, b/a, c/a), volume per 4 formula units (Å³), and total energy per 4 formula units (eV) obtained from full geometry optimization for ZrNi, ZrNiH, ZrNiH₂, and ZrNiH₃. From the Birch EOS fitting, report the equilibrium energy per 4 formula units, equilibrium volume per 4 formula units, bulk modulus (GPa), and hydrogen stabilization energy per H₂ (eV; NaN for ZrNi). These values must be written to two separate CSV files as specified in the workflow steps. The reported quantities will be checked against hidden reference values derived from the original study.

## Assets

- Plane-wave PAW-GGA DFT code (e.g., Quantum ESPRESSO, GPAW): https://www.quantum-espresso.org
- PAW pseudopotentials for Zr, Ni, H (GGA-PBE): https://www.pseudo-dojo.org

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Based on the reported experimental crystallographic data for ZrNi (Cmcm, a=3.287 Å, b/a=3.07, c/a=1.23, y_Ni=0.362, y_Zr=0.083) and for ZrNiH₃ (a=3.498 Å, b/a=2.97, c/a=1.23, y_Ni=0.426, y_Zr=0.139, H₁ at 4c (0,0.931,0.25), H₂ at 8f (0,0.312,0.687)), create input structure files for all four compositions: ZrNi, ZrNiH (H₁ at 4c (0,0.916,0.25)), ZrNiH₂ (H₂ at 8f (0,0.313,0.687)), ZrNiH₃. Maintain the base-centered orthorhombic Cmcm symmetry with 4 formula units per conventional cell.
- Evidence: `/app/outputs/structures_generated.txt`

### Step 2: DFT geometry optimization
- Role: scored (load-bearing)
- Action: Using a plane-wave PAW-GGA (PBE) DFT code, perform full relaxation of lattice parameters and internal coordinates for ZrNi, ZrNiH, ZrNiH₂, and ZrNiH₃. Record the relaxed lattice constants (a, b/a, c/a), volume per 4 formula units, and total energy per 4 formula units.
- Output file: `/app/outputs/geometry_optimization_results.csv`
- Format: csv
- Contract: Columns: system (str), a_lattice (Å), b_over_a (dimensionless), c_over_a (dimensionless), volume_per_4fu (Å³), total_energy_per_4fu (eV). One row per composition.
- Scoring: scored by hidden verifier

### Step 3: H₂ molecule reference energy
- Role: process
- Action: Using the same DFT setup, calculate the total electronic energy of an isolated H₂ molecule placed in a cubic box with side length 4.5 Å.
- Evidence: `/app/outputs/H2_energy.txt`

### Step 4: Birch EOS fitting and hydrogen stabilization energies
- Role: scored (load-bearing)
- Action: For each relaxed system from step 2, perform DFT single-point energy calculations at several volumes spanning the equilibrium volume. Fit energy-volume data for each composition using a second-order Birch equation of state (EOS). Extract equilibrium energy per 4 fu, equilibrium volume per 4 fu, and bulk modulus. Using the fitted equilibrium energies and the H₂ reference energy from step 3, compute the hydrogen stabilization energy per H₂ molecule as (E(ZrNiHₓ) – E(ZrNi) – x·E(H₂)) / x for x = 1, 2, 3. For ZrNi set stabilization energy to NaN.
- Output file: `/app/outputs/eos_fit_results.csv`
- Format: csv
- Contract: Columns: system (str), equilibrium_energy_per_4fu (eV), equilibrium_volume_per_4fu (Å³), bulk_modulus (GPa), stabilization_energy_per_H2 (eV). One row per composition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometry_optimization_results.csv`
- `/app/outputs/eos_fit_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometry_optimization_results.csv
- path: `/app/outputs/geometry_optimization_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice constants, volume, and total energy per 4 fu for ZrNi, ZrNiH, ZrNiH₂, ZrNiH₃ compared to reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `system`, `a_lattice`, `b_over_a`, `c_over_a`, `volume_per_4fu`, `total_energy_per_4fu`
  - `units`:
    - `a_lattice`: Å
    - `volume_per_4fu`: Å³
    - `total_energy_per_4fu`: eV
  - `row_count`: 4

### eos_fit_results.csv
- path: `/app/outputs/eos_fit_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Birch EOS fitted parameters and hydrogen stabilization energy compared to reference values and internal consistency checks.
- schema:
  - `type`: table
  - `required_columns`: `system`, `equilibrium_energy_per_4fu`, `equilibrium_volume_per_4fu`, `bulk_modulus`, `stabilization_energy_per_H2`
  - `units`:
    - `equilibrium_energy_per_4fu`: eV
    - `equilibrium_volume_per_4fu`: Å³
    - `bulk_modulus`: GPa
    - `stabilization_energy_per_H2`: eV
  - `row_count`: 4

Notes: The all-electron ASW electronic structure and bonding analysis is omitted because the ASW code is proprietary. Only the pseudo-potential PAW-GGA geometry optimization and Birch EOS fitting are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometry_optimization_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "a_lattice",
          "b_over_a",
          "c_over_a",
          "volume_per_4fu",
          "total_energy_per_4fu"
        ],
        "units": {
          "a_lattice": "Å",
          "volume_per_4fu": "Å³",
          "total_energy_per_4fu": "eV"
        },
        "row_count": 4
      },
      "description": "Relaxed lattice constants, volume, and total energy per 4 fu for ZrNi, ZrNiH, ZrNiH₂, ZrNiH₃ compared to reference values within tolerances."
    },
    {
      "file": "eos_fit_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "equilibrium_energy_per_4fu",
          "equilibrium_volume_per_4fu",
          "bulk_modulus",
          "stabilization_energy_per_H2"
        ],
        "units": {
          "equilibrium_energy_per_4fu": "eV",
          "equilibrium_volume_per_4fu": "Å³",
          "bulk_modulus": "GPa",
          "stabilization_energy_per_H2": "eV"
        },
        "row_count": 4
      },
      "description": "Birch EOS fitted parameters and hydrogen stabilization energy compared to reference values and internal consistency checks."
    }
  ],
  "notes": "The all-electron ASW electronic structure and bonding analysis is omitted because the ASW code is proprietary. Only the pseudo-potential PAW-GGA geometry optimization and Birch EOS fitting are required."
}
```

## How you are scored
A hidden verifier will examine your two output CSV files. For each required quantity, the verifier compares your computed numbers to reference values within tolerances that account for legitimate differences caused by the use of different DFT implementations (e.g., choice of pseudopotentials, k‑point sampling, convergence criteria). Additionally, the verifier will confirm that your results obey expected physical trends: the cell volume should increase with hydrogen content, the bulk modulus should increase, and the hydrogen stabilization energies should be negative and grow in magnitude from ZrNiH to ZrNiH₃. The final reward is a weighted sum of the correctness scores from both artifacts. It is not enough to merely produce the files; the values they contain must pass the hidden checks. Honest execution of the DFT workflow is essential.
