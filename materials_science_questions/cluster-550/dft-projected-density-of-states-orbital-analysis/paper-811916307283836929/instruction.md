# DFT Study of Structural Stability and Electronic Structures of TaN

## Problem background
Transition metal nitrides such as TaN are important in hard coatings, diffusion barriers, and gate electrodes. The properties of TaN depend on its crystal structure, and several competing phases have been proposed. This task reproduces a first-principles study that compares the energetic and electronic properties of five TaN structural models: CoSn (P6̅2m), WC (P6̅m2), NaCl (Fm3̅m), ZnS-B3 (F4̅3m), and CsCl (Pm3̅m). The target is to determine the relative stability ordering of these phases, their equilibrium lattice parameters and bulk moduli, and key electronic descriptors such as the density of states at the Fermi level.

## Approach
Use density functional theory (DFT) with the plane-wave pseudopotential method, employing the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation and ultrasoft pseudopotentials. For each of the five structures, compute the total energy over a range of unit-cell volumes. Fit the resulting energy–volume data to the third-order Birch–Murnaghan equation of state to extract equilibrium properties: cohesive energy, equilibrium volume, lattice constants, bulk modulus, and its pressure derivative. For the CoSn structure also determine the optimized Wyckoff position of the nitrogen atom. Then, at the equilibrium volume, perform a self-consistent field calculation using the tetrahedron method and obtain the total density of states at the Fermi level and atomic partial charges via Löwdin population analysis. The whole workflow is carried out with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and standard Python scientific libraries for fitting.

## Reproduction target
Produce and save the following results for the five TaN phases (CoSn, WC, NaCl, ZnS-B3, CsCl):
- Raw total energy versus volume data points.
- Derived equilibrium properties: cohesive energy (eV per formula unit), lattice constants a and c (Å), bulk modulus K0 (GPa), first pressure derivative K0′, and for CoSn the N Wyckoff x-coordinate.
- Electronic properties: total density of states at the Fermi level (states/eV per formula unit) and Löwdin atomic charges (e) for each inequivalent Ta site and for N.
From the cohesive energies, deduce the energetic stability ordering of the five structures.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ta ultrasoft pseudopotential (PBE): https://www.quantum-espresso.org/pseudopotentials/
- N ultrasoft pseudopotential (PBE): https://www.quantum-espresso.org/pseudopotentials/
- Python scientific libraries: numpy, scipy, ase, pymatgen

## Workflow steps

### Step 1: Total energy vs volume calculations
- Role: scored
- Action: Using Quantum ESPRESSO (or equivalent DFT code) with PBE-GGA and ultrasoft pseudopotentials, perform total energy calculations for each of the five TaN structures (CoSn, WC, NaCl, ZnS-B3, CsCl) at a series of unit cell volumes (at least 7 volumes per structure spanning equilibrium). Save the collected raw energy-volume data.
- Output file: `/app/outputs/energy_volume_data.csv`
- Format: csv
- Contract: CSV with columns: structure (string), volume (float, Å³/f.u.), total_energy (float, eV/f.u.). One header row, then rows for each volume.
- Scoring: scored by hidden verifier

### Step 2: Equation of state fitting and derived properties
- Role: scored (load-bearing)
- Action: Fit the energy-volume data from Step 1 to the third-order Birch-Murnaghan equation of state. Extract equilibrium properties: cohesive energy E0, equilibrium volume V0, lattice constants a and c, bulk modulus K0, and pressure derivative K0_prime. For CoSn also include the optimized N Wyckoff x-coordinate. Save results.
- Output file: `/app/outputs/derived_properties.csv`
- Format: csv
- Contract: CSV with columns: structure (str), a (float, Å), c (float, Å, NA for cubic), E0 (float, eV/f.u.), V0 (float, Å³/f.u.), K0 (float, GPa), K0_prime (float), N_x (float, NA for non-CoSn). One header row, one row per structure.
- Scoring: scored by hidden verifier

### Step 3: Electronic structure properties at equilibrium
- Role: scored
- Action: At the equilibrium geometries determined from Step 2, run DFT scf calculations with tetrahedron method and Löwdin population analysis. Compute total DOS at the Fermi level (N_tot(E_F)) and atomic partial charges. Save the electronic properties.
- Output file: `/app/outputs/electronic_properties.csv`
- Format: csv
- Contract: CSV with columns: structure (str), N_tot_EF (float, states/eV per f.u.), q_Ta_1 (float, electrons), q_Ta_2 (float, electrons or NA), q_N (float, electrons). One header row, one row per structure.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_volume_data.csv`
- `/app/outputs/derived_properties.csv`
- `/app/outputs/electronic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_volume_data.csv
- path: `/app/outputs/energy_volume_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw energy–volume data points for five TaN phases. The checker will fit the Birch–Murnaghan EOS to these points and recompute derived properties.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `volume`, `total_energy`
  - `units`:
    - `volume`: Å³/f.u.
    - `total_energy`: eV/f.u.

### derived_properties.csv
- path: `/app/outputs/derived_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Derived equilibrium structural properties for each phase. The checker will cross-check these against its own EOS fitting from the energy–volume data and compare them to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `a`, `c`, `E0`, `V0`, `K0`, `K0_prime`, `N_x`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `E0`: eV/f.u.
    - `V0`: Å³/f.u.
    - `K0`: GPa

### electronic_properties.csv
- path: `/app/outputs/electronic_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic properties: total DOS at the Fermi level and Löwdin atomic charges. The checker will compare these values to paper-reported results within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `N_tot_EF`, `q_Ta_1`, `q_Ta_2`, `q_N`
  - `units`:
    - `N_tot_EF`: states/eV per f.u.
    - `q_Ta_1`: electrons
    - `q_Ta_2`: electrons
    - `q_N`: electrons

Notes: All files must be valid CSVs with the specified columns. The agent may choose any suitable DFT implementation and pseudopotentials as long as the protocol (PBE-GGA, ultrasoft, plane-wave) is followed.

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
          "structure",
          "volume",
          "total_energy"
        ],
        "units": {
          "volume": "Å³/f.u.",
          "total_energy": "eV/f.u."
        }
      },
      "description": "Raw energy–volume data points for five TaN phases. The checker will fit the Birch–Murnaghan EOS to these points and recompute derived properties."
    },
    {
      "file": "derived_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "a",
          "c",
          "E0",
          "V0",
          "K0",
          "K0_prime",
          "N_x"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "E0": "eV/f.u.",
          "V0": "Å³/f.u.",
          "K0": "GPa"
        }
      },
      "description": "Derived equilibrium structural properties for each phase. The checker will cross-check these against its own EOS fitting from the energy–volume data and compare them to paper-reported values."
    },
    {
      "file": "electronic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "N_tot_EF",
          "q_Ta_1",
          "q_Ta_2",
          "q_N"
        ],
        "units": {
          "N_tot_EF": "states/eV per f.u.",
          "q_Ta_1": "electrons",
          "q_Ta_2": "electrons",
          "q_N": "electrons"
        }
      },
      "description": "Electronic properties: total DOS at the Fermi level and Löwdin atomic charges. The checker will compare these values to paper-reported results within tolerances."
    }
  ],
  "notes": "All files must be valid CSVs with the specified columns. The agent may choose any suitable DFT implementation and pseudopotentials as long as the protocol (PBE-GGA, ultrasoft, plane-wave) is followed."
}
```

## How you are scored
A hidden verifier will evaluate the three output files independently. It will refit the Birch–Murnaghan equation of state from your raw energy–volume data, cross‑check your derived properties for consistency, and compare your electronic properties against the expected physical range. The final reward is a weighted combination of scores from each stage: the derived properties of the CoSn phase carry the largest weight, followed by the derived properties of the other structures, then the electronic properties, and finally the stability ordering. Reporting numbers alone is not enough; the verifier checks internal consistency and physical plausibility.
