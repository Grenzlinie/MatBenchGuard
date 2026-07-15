# DFT calculations of structural and elastic properties of boron-V compounds

## Problem background
Boron-V compounds (BN, BP, BAs, BSb, BBi) are semiconductors with high mechanical strength, short bond lengths, and wide or unusual band gaps, making them candidates for electronics, optoelectronics, and superhard coatings. A fundamental understanding of their structural stability and elastic response is essential for device and material design. First-principles density functional theory (DFT) can provide reliable predictions of crystal structure parameters and elastic moduli across the entire family, yielding a consistent dataset for comparison and application.

## Approach
We use DFT with the Perdew-Burke-Ernzerhof (PBE) generalized-gradient approximation and a plane-wave basis set (via an open-source DFT code) to perform two types of calculations for all five B-V compounds:

- **Total-energy vs volume scans:** For each compound in the zinc-blende (ZB), rock-salt (NaCl), and wurtzite (WZ) crystal structures, compute the total electronic energy at a series of unit-cell volumes around the equilibrium. These data allow the checker to determine the equilibrium lattice constant, bulk modulus, and pressure derivative by fitting an equation of state.
- **Elastic constants:** For the zinc-blende phase (the predicted ground state), compute the three independent elastic constants C₁₁, C₁₂, C₄₄ via the finite-strain method. From these, standard polycrystalline averaging formulas yield isotropic mechanical and thermal properties (shear modulus, Young's modulus, Poisson's ratio, anisotropy, wave velocities, Debye temperature, and melting point).

The solver is responsible for executing the converged DFT calculations and outputting the raw volume–energy pairs and elastic constants in the specified CSV files. The downstream derivation and comparison are performed by the hidden verifier.

## Reproduction target
Produce two correctly formatted CSV files under `/app/outputs`:

1. `energy_volume_data.csv` – raw total energy (eV) as a function of unit-cell volume (Å³ per formula unit) for every (compound, phase) combination, with at least 7 distinct volumes per combination.
2. `elastic_constants.csv` – the three independent elastic constants C₁₁, C₁₂, C₄₄ (GPa) for the zinc-blende phase of each compound.

The hidden verifier will process these files, fit the equation of state to extract structural parameters, and compute the complete set of derived elastic and thermal quantities. The reproduction is considered successful if the extracted parameters and derived properties are consistent with the published reference results within physically reasonable tolerances.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- numpy, scipy, pandas: numpy scipy pandas

## Workflow steps

### Step 1: DFT total-energy calculations for structural optimization
- Role: scored (load-bearing)
- Action: Perform DFT total-energy calculations for BN, BP, BAs, BSb, BBi in zinc-blende (ZB), rock-salt (NaCl), and wurtzite (WZ) crystal structures using the PBE exchange-correlation functional. For each compound and phase, compute total energies at a range of volumes (at least 7 distinct volumes around equilibrium) using a plane-wave basis set with sufficient convergence. Output the computed volume–energy pairs to energy_volume_data.csv.
- Output file: `/app/outputs/energy_volume_data.csv`
- Format: csv
- Contract: columns: compound (string, one of BN,BP,BAs,BSb,BBi), phase (string, one of ZB,NaCl,WZ), volume (float, Å³ per formula unit), total_energy (float, eV). At minimum, 7 distinct volume points per (compound, phase) must be present.
- Scoring: scored by hidden verifier

### Step 2: DFT elastic constants calculation for ZB phase
- Role: scored (load-bearing)
- Action: For the zinc-blende phase of BN, BP, BAs, BSb, BBi, compute the three independent elastic constants C11, C12, C44 (in GPa) using the finite-strain method within DFT at the equilibrium volume. Output the results to elastic_constants.csv.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: columns: compound (string), C11 (float, GPa), C12 (float, GPa), C44 (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_volume_data.csv`
- `/app/outputs/elastic_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_volume_data.csv
- path: `/app/outputs/energy_volume_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT total-energy vs volume data; checker fits Murnaghan EOS to extract equilibrium lattice constant, bulk modulus, and pressure derivative, then compares to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `phase`, `volume`, `total_energy`
  - `units`:
    - `volume`: Å³ per formula unit
    - `total_energy`: eV
  - `description`: Each row is one volume point. At least 7 distinct volume points per (compound, phase).

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Elastic constants for the zinc-blende phase; checker derives isotropic moduli, wave velocities, Debye temperature, and melting point, then compares to paper-reported values and checks mechanical stability.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `C11`, `C12`, `C44`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa

Notes: The agent must use the PBE functional and sufficient k-point sampling/convergence to obtain accurate results. All DFT inputs are publicly known; no pre-existing dataset is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_volume_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "phase",
          "volume",
          "total_energy"
        ],
        "units": {
          "volume": "Å³ per formula unit",
          "total_energy": "eV"
        },
        "description": "Each row is one volume point. At least 7 distinct volume points per (compound, phase)."
      },
      "description": "Raw DFT total-energy vs volume data; checker fits Murnaghan EOS to extract equilibrium lattice constant, bulk modulus, and pressure derivative, then compares to paper-reported values."
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "C11",
          "C12",
          "C44"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Elastic constants for the zinc-blende phase; checker derives isotropic moduli, wave velocities, Debye temperature, and melting point, then compares to paper-reported values and checks mechanical stability."
    }
  ],
  "notes": "The agent must use the PBE functional and sufficient k-point sampling/convergence to obtain accurate results. All DFT inputs are publicly known; no pre-existing dataset is required."
}
```

## How you are scored
A hidden scoring program reads your output files independently. It fits the energy–volume data to extract the equilibrium lattice constant, bulk modulus, and pressure derivative for each phase; it also computes isotropic mechanical moduli and thermal properties from the elastic constants using standard formulas. The program then compares these quantities to the paper‑reported values, checks mechanical stability conditions (e.g., elastic constants satisfy stability criteria), and verifies that the zinc‑blende phase is the ground state. Each scored artifact contributes a portion of the total reward, which is a single float between 0 and 1. Meeting or exceeding the reference accuracy yields full credit, while larger deviations reduce the score; the comparison uses tolerances appropriate for DFT‑based re‑implementation with a different plane‑wave code.
