# DFT dielectric function of biaxially strained GeS monolayer

## Problem background
Single‑layer GeS is a two‑dimensional semiconductor with a finite indirect band gap, making it a candidate for optoelectronic devices. Mechanical strain is an effective way to tune the electronic and optical behaviour of such 2D materials. Understanding how biaxial deformation influences the band gap and dielectric response of a GeS monolayer is therefore important for designing strain‑engineered applications. This work employs first‑principles density functional theory (DFT) to compute the electronic band structure and the frequency‑dependent dielectric function of single‑layer GeS under biaxial compression and tension.

## Approach
All calculations are carried out with the open‑source Quantum ESPRESSO package using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation and projector augmented‑wave (PAW) pseudopotentials. The workflow consists of three stages:

1. **Geometry relaxation** – the in‑plane lattice parameters and atomic positions of the GeS monolayer are relaxed for the equilibrium state and for biaxial strains of −8 % and +8 % until forces are converged.
2. **Electronic band gap** – from the relaxed structures, the band structure is computed and the indirect band gap is extracted for each strain.
3. **Dielectric function** – the imaginary part of the dielectric function is evaluated from the momentum matrix elements, and the real part is obtained via the Kramers–Kronig transformation. The in‑plane average (trace/2 of the diagonal components) is reported for photon energies in the range 0–8 eV.

The goal is to obtain the strain‑dependent band gap and the real and imaginary parts of the dielectric function as a function of photon energy.

## Reproduction target
Produce two CSV files inside `/app/outputs`:

- **band_gap_vs_strain.csv** – columns `strain_percent` (int) and `band_gap_eV` (float). One row for each of the strains −8, 0, and +8 %.
- **dielectric_function.csv** – columns `strain_percent` (int), `energy_eV` (float), `epsilon1` (float), and `epsilon2` (float). For each strain (−8, 0, +8 %) provide the in‑plane averaged real and imaginary parts of the dielectric function over the photon energy range 0 to 8 eV with an energy step of at most 0.1 eV.

The dielectric function must be the average of the in‑plane diagonal components, `(ε_xx + ε_yy)/2` (or equivalently the trace divided by 2). The output must strictly follow the column ordering and naming given above; no extra rows or columns are allowed.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- PBE PAW pseudopotentials for Ge and S: https://www.materialscloud.org/discover/sssp/
- GeS monolayer crystal structure

## Workflow steps

### Step 1: DFT geometry relaxation
- Role: process
- Action: Perform DFT geometry relaxation of single-layer GeS at equilibrium and under biaxial strains -8%, 0%, and +8% using Quantum ESPRESSO with PBE PAW pseudopotentials, until forces are below 0.001 eV/Angstrom.
- Evidence: none

### Step 2: Electronic band gap calculation
- Role: scored
- Action: Using the relaxed structures, compute the electronic band structure with an appropriate k-mesh and extract the indirect band gap (in eV) for each strain value.
- Output file: `/app/outputs/band_gap_vs_strain.csv`
- Format: csv
- Contract: Columns: strain_percent (int), band_gap_eV (float). Rows: -8, 0, 8.
- Scoring: scored by hidden verifier

### Step 3: Dielectric function computation
- Role: scored (load-bearing)
- Action: From the electronic structure output, compute the imaginary part of the dielectric function via momentum matrix elements and the real part via Kramers-Kronig transformation. Report the in-plane average (trace/2 of diagonal components) for photon energies 0-8 eV at each strain.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: Columns: strain_percent (int), energy_eV (float), epsilon1 (float), epsilon2 (float). Energy step <= 0.1 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_vs_strain.csv`
- `/app/outputs/dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_vs_strain.csv
- path: `/app/outputs/band_gap_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: DFT-PBE band gap of single-layer GeS at biaxial strains -8%, 0%, +8%.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `band_gap_eV`
  - `columns`:
    - `strain_percent`: int, biaxial strain in percent
    - `band_gap_eV`: float, DFT-PBE indirect band gap in eV
  - `units`:
    - `band_gap_eV`: eV

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: In-plane averaged real and imaginary parts of the dielectric function for strains -8%, 0%, +8% over 0-8 eV.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `energy_eV`, `epsilon1`, `epsilon2`
  - `columns`:
    - `strain_percent`: int, biaxial strain in percent
    - `energy_eV`: float, photon energy in eV
    - `epsilon1`: float, real part of dielectric function (dimensionless)
    - `epsilon2`: float, imaginary part of dielectric function (dimensionless)
  - `units`:
    - `energy_eV`: eV

Notes: The checker will recompute the peak ratio of epsilon2 near 4.5 eV for strain -8% relative to 0% and verify the strain-induced band gap trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "band_gap_eV"
        ],
        "columns": {
          "strain_percent": "int, biaxial strain in percent",
          "band_gap_eV": "float, DFT-PBE indirect band gap in eV"
        },
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "DFT-PBE band gap of single-layer GeS at biaxial strains -8%, 0%, +8%."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "energy_eV",
          "epsilon1",
          "epsilon2"
        ],
        "columns": {
          "strain_percent": "int, biaxial strain in percent",
          "energy_eV": "float, photon energy in eV",
          "epsilon1": "float, real part of dielectric function (dimensionless)",
          "epsilon2": "float, imaginary part of dielectric function (dimensionless)"
        },
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "In-plane averaged real and imaginary parts of the dielectric function for strains -8%, 0%, +8% over 0-8 eV."
    }
  ],
  "notes": "The checker will recompute the peak ratio of epsilon2 near 4.5 eV for strain -8% relative to 0% and verify the strain-induced band gap trend."
}
```

## How you are scored
A hidden verifier reads the two CSV files you write to `/app/outputs` and scores them independently. The verifier checks the band gap data for physically reasonable strain‑dependent trends and inspects the dielectric function for the presence of expected spectral features. It does not require you to match a particular numeric value from the literature; rather, it evaluates whether the computed results are self‑consistent and exhibit the correct qualitative behaviour. Simply reporting a stored number without performing the DFT workflow will not suffice because the verifier examines structural relationships across the full dataset. The two scored steps (band gap calculation and dielectric function computation) are combined with weights that reflect their importance, yielding a final reward between 0 and 1.
