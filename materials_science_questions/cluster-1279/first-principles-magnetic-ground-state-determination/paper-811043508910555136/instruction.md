# First-principles magnetic ground state of Y2Fe3Mn Laves phase

## Problem background
The pseudobinary intermetallics Y(Fe₁₋ₓMnₓ)₂ with the cubic Laves‑phase (C15) structure exhibit complex magnetic behaviour: one of the central questions is the spin state of Mn atoms and their magnetic alignment relative to Fe. The ordered compound Y₂Fe₃Mn serves as a model system to disentangle these effects. Using first‑principles electronic structure calculations, the magnetic ground state and local moments can be studied as a function of the lattice parameter, exploring nonmagnetic, ferromagnetic (Mn moment parallel to Fe), and ferrimagnetic (Mn moment antiparallel) spin configurations. The key hypothesis to be tested is whether Mn can adopt high‑ or low‑spin states depending on lattice parameter and relative spin orientation, and how the energies of parallel and antiparallel configurations compare.

## Approach
The approach is a series of self‑consistent density‑functional theory (DFT) total‑energy calculations. Starting from the experimentally known cubic C15 crystal structure, an ordered arrangement of Y, Fe, and Mn atoms is constructed (space group Fd‑3m, with Y on 8a sites and Fe/Mn on 16d sites). For a range of lattice parameters (e.g., 6.8 – 7.6 Å), DFT input files are generated for three magnetic configurations: nonmagnetic (NM), ferromagnetic with Mn spins parallel to Fe (FM), and ferrimagnetic with Mn spins antiparallel to Fe (FIM). Self‑consistent total‑energy calculations are performed using an open‑source DFT code (e.g., Quantum ESPRESSO) with standard pseudopotentials. From each converged calculation, the total energy and site‑projected magnetic moments of Fe and Mn are extracted. The raw results are collected into a single CSV table, which then allows systematic analysis of spin‑state transitions and energy differences between the magnetic configurations.

## Reproduction target
Perform self‑consistent DFT total‑energy calculations for the ordered Y₂Fe₃Mn compound in the cubic C15 Laves phase over a set of lattice parameters spanning roughly 6.8 – 7.6 Å. For each lattice parameter, compute the nonmagnetic, ferromagnetic (Mn parallel to Fe), and ferrimagnetic (Mn antiparallel) spin configurations. Extract the total energy and site‑projected magnetic moments of Fe and Mn for each case and write the combined dataset to `/app/outputs/magnetic_data.csv` following the specified schema. The CSV is the sole scored artifact; the verifier will check that the computed trends comply with the expected magnetic behaviour.

## Assets

- Open-source DFT code: https://www.quantum-espresso.org/
- Pseudopotential library: https://www.materialscloud.org/discover/sssp/
- Cubic Laves-phase crystal structure details

## Crystal structure specification

To guarantee a unique and reproducible initial structure for the ordered Y₂Fe₃Mn compound, build the conventional cubic cell as follows:

- Space group: Fd‑3m (No. 227), origin choice 1 (point group ‑3m; the 8a and 16d Wyckoff positions are conventionally given with the origin at the centre, -3m).
- Lattice parameter: a (variable, in Angstrom). The three lattice vectors are a*(0,1/2,1/2), a*(1/2,0,1/2), a*(1/2,1/2,0).
- Yttrium (Y) occupies the 8a sites: fractional coordinates (1/8,1/8,1/8), (1/8,5/8,5/8), (5/8,1/8,5/8), (5/8,5/8,1/8), and the four positions obtained by adding (0,1/2,1/2), (1/2,0,1/2), (1/2,1/2,0) to the first four (i.e. the remaining four equivalent positions). All 8 sites are completely filled by Y.
- Iron (Fe) and Manganese (Mn) share the 16d sites. The total number of 16d sites is 16, which must accommodate 12 Fe atoms and 4 Mn atoms (to preserve the Y₂Fe₃Mn stoichiometry with 8 Y in the cell).
- Ordered arrangement of Fe/Mn: place the four Mn atoms at the following 16d fractional coordinates:
  - (1/2, 1/2, 1/2)
  - (1/2, 3/4, 3/4)
  - (3/4, 1/2, 3/4)
  - (3/4, 3/4, 1/2)
  The remaining twelve 16d sites are occupied by Fe atoms. (This ordered arrangement is one valid hypothesis that reproduces the 1:3 Mn:Fe ratio on the 16d sublattice and lowers the symmetry appropriately; other physically equivalent orderings are acceptable as long as the 16d occupancy is exactly 4 Mn and 12 Fe.)
- Magnetic initialisation: for ferromagnetic (FM) and ferrimagnetic (FIM) calculations, set initial magnetic moments on Fe and Mn atoms according to the desired alignment (parallel for FM, antiparallel for FIM). For nonmagnetic (NM) calculations, do not impose any spin polarization.

You may use any standard crystallographic tool (e.g., ASE, pymatgen, Quantum ESPRESSO’s `ibrav` settings) to generate the full list of atomic positions and the corresponding DFT input files.

## Workflow steps

### Step 1: Structure setup
- Role: process
- Action: Construct the ordered crystal structure of Y2Fe3Mn in the cubic C15 Laves phase for a range of lattice parameters (e.g., 6.8–7.6 Å) using the specification above. Generate input files for nonmagnetic (NM), ferromagnetic (FM, Mn moment parallel to Fe), and ferrimagnetic (FIM, Mn moment antiparallel to Fe) spin configurations.

### Step 2: DFT total-energy and moment calculations
- Role: scored (load-bearing)
- Action: Run self-consistent DFT total-energy calculations for each magnetic configuration and lattice parameter. Extract the total energy and site-projected magnetic moments of Fe and Mn, and write the results to magnetic_data.csv.
- Output file: `/app/outputs/magnetic_data.csv`
- Format: csv
- Contract: Columns: a (float, Angstrom), configuration (string: NM, FM, FIM), total_energy (float, eV), Fe_moment (float, mu_B), Mn_moment (float, mu_B). One row per lattice parameter per configuration.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_data.csv
- path: `/app/outputs/magnetic_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Raw DFT total energies and site-projected magnetic moments for all spin configurations as a function of lattice parameter, used to verify the paper's reported spin-state transitions, energetic proximity, and stabilization trends.
- schema:
  - `type`: table
  - `required_columns`: `a`, `configuration`, `total_energy`, `Fe_moment`, `Mn_moment`
  - `units`:
    - `a`: Angstrom
    - `total_energy`: eV
    - `Fe_moment`: mu_B
    - `Mn_moment`: mu_B

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a",
          "configuration",
          "total_energy",
          "Fe_moment",
          "Mn_moment"
        ],
        "units": {
          "a": "Angstrom",
          "total_energy": "eV",
          "Fe_moment": "mu_B",
          "Mn_moment": "mu_B"
        }
      },
      "description": "Raw DFT total energies and site-projected magnetic moments for all spin configurations as a function of lattice parameter, used to verify the paper's reported spin-state transitions, energetic proximity, and stabilization trends."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier loads your `magnetic_data.csv` and independently evaluates the results against reference data (the paper‑reported trends and values). Each workflow stage’s artifact carries a weight, and the verifier combines the per‑artifact scores into a final reward between 0 and 1. The scoring primarily assesses whether the data reproduce the correct qualitative trends (e.g., spin‑state transitions, energy ordering between configurations) and satisfy magnitude‑based checks within physically motivated tolerances. The exact tolerances and reference values are not disclosed. To earn full credit, your calculations must faithfully implement the specified workflow and yield physically reasonable results; simply guessing or transcribing numbers from the paper is not sufficient.