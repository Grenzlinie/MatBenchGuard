# Crystal Stability Comparison via Energy and Elastic Analysis

## Problem background
Copper (Cu) crystallizes in a face-centered cubic (FCC) structure under ambient conditions. Under high pressure the FCC lattice can distort toward a body-centered tetragonal (BCT) arrangement, raising questions about the relative stability of the two phases. This work investigates whether a BCT phase of Cu can exist as a metastable or even stable state when both high pressure and high temperature are applied, and what structural, elastic, and thermodynamic signatures characterize such a phase. The central unresolved question is: at a pressure near 80 GPa, does a BCT variant appear as a local minimum in the energy landscape, and does it become thermodynamically favoured over FCC as temperature increases?

## Approach
Density functional theory (DFT) calculations with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional are used to compute total energies. First, the total energy per atom of Cu is mapped as a function of the tetragonal ratio c/a while the atomic volume is held fixed at 8.99 Å³/atom (corresponding to approximately 80 GPa pressure). This energy curve reveals any local minima and allows extraction of the equilibrium lattice parameters of the BCT phase. Second, the elastic stiffness constants of both the FCC ground state and the high-pressure BCT structure are computed via the stress-strain method to assess mechanical stability criteria. Third, phonon calculations within the harmonic approximation provide the vibrational density of states and the Helmholtz free energy F(V,T) for a series of volumes around equilibrium. Finally, the quasi-harmonic approximation is applied: the Birch-Murnaghan equation of state is fitted to F(V,T) at each temperature, and minimization of F(V,T)+PV at constant pressure P=80 GPa yields the temperature-dependent Gibbs free energies of the FCC and BCT phases. The comparison of these Gibbs energies reveals which phase is favoured as temperature rises.

## Reproduction target
The objective is to produce the following artifacts from first-principles calculations:

1. A table of DFT total energies per atom as a function of c/a ratio at fixed volume 8.99 Å³/atom covering the range 0.8 to 1.6 (at least 20 points). From this curve, identify the global minimum (FCC) and any local minimum (BCT) and report the structural parameters (a and c) derived from the local minimum's c/a and the fixed atomic volume.

2. A JSON object containing the elastic stiffness constants C11, C12, C44 (and C13, C33, C66 for the tetragonal case) and the shear modulus c' = (C11-C12)/2 for both the FCC phase at its equilibrium volume and the BCT phase at V=8.99 Å³/atom and c/a=0.966. Use these to verify whether each phase satisfies the Born stability criteria for its crystal system.

3. A CSV file giving the Gibbs free energy difference ΔG = G_BCT − G_FCC as a function of temperature from 0 K to 1500 K (steps ≤ 100 K) at a constant pressure of 80 GPa, computed within the quasi-harmonic approximation. Determine the temperature (if any) at which ΔG changes sign, indicating that BCT becomes the more stable phase.

## Assets

- Quantum ESPRESSO (or any open-source DFT code with PBE functional and stress capabilities): https://www.quantum-espresso.org/
- phonopy: https://phonopy.github.io/phonopy/
- Cu PBE pseudopotential: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT total energy vs c/a at 80 GPa
- Role: scored
- Action: Compute total energy per atom from DFT for Cu at a fixed atomic volume of 8.99 Å³/atom as a function of the tetragonal ratio c/a, covering the range from 0.8 to 1.6 with sufficient sampling around minima (at least 20 points). Write the data to energy_vs_ca.csv.
- Output file: `/app/outputs/energy_vs_ca.csv`
- Format: csv
- Contract: columns: c/a_ratio (float, dimensionless), total_energy_per_atom_eV (float, eV/atom)
- Scoring: scored by hidden verifier

### Step 2: DFT elastic constants of FCC and BCT
- Role: scored
- Action: Compute the elastic stiffness constants for FCC Cu (at equilibrium) and for the high-pressure BCT phase (at V=8.99 Å³/atom, c/a=0.966) using the stress-strain method. Output the results as elastic_constants.json including elastic constants in GPa and the derived shear modulus c' = (c11-c12)/2 for both phases.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: object with keys 'fcc' and 'bct'. fcc contains c11, c12, c44, c_prime. bct contains c11, c12, c13, c33, c44, c66, c_prime.
- Scoring: scored by hidden verifier

### Step 3: Phonon DOS and Helmholtz free energy for FCC and BCT
- Role: process
- Action: Generate supercells for FCC and BCT phases; compute interatomic force constants using finite-displacement DFT calculations. Use phonon codes (e.g., phonopy) to obtain phonon density of states at multiple volumes (at least 10 volumes spanning ±5% around equilibrium). Compute temperature-dependent Helmholtz free energy F(V,T) for each volume and phase within the harmonic approximation.
- Evidence: none

### Step 4: Equation-of-state fit and Gibbs free energy construction
- Role: process
- Action: Fit the Birch-Murnaghan equation of state to the Helmholtz free energy data F(V,T) at each temperature for both FCC and BCT. Then minimize F(V,T)+P V with respect to volume at constant pressure P = 80 GPa to obtain temperature-dependent Gibbs free energies G(T) for each phase.
- Evidence: none

### Step 5: Gibbs free energy difference BCT vs FCC at 80 GPa
- Role: scored (load-bearing)
- Action: Compute the Gibbs free energy difference deltaG = G_BCT(T) - G_FCC(T) at pressure 80 GPa as a function of temperature. Write a CSV file gibbs_free_energy_difference.csv with columns temperature_K and delta_G_eV_per_atom covering 0 K to 1500 K in temperature steps no larger than 100 K.
- Output file: `/app/outputs/gibbs_free_energy_difference.csv`
- Format: csv
- Contract: columns: temperature_K (float, K), delta_G_eV_per_atom (float, eV/atom)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_vs_ca.csv`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/gibbs_free_energy_difference.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_vs_ca.csv
- path: `/app/outputs/energy_vs_ca.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DFT total energy per atom as a function of tetragonal ratio c/a at fixed volume 8.99 Å³/atom. Reveals the global FCC minimum and a local BCT minimum.
- schema:
  - `type`: table
  - `required_columns`: `c/a_ratio`, `total_energy_per_atom_eV`
  - `units`:
    - `c/a_ratio`: dimensionless
    - `total_energy_per_atom_eV`: eV/atom

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Elastic stiffness constants and shear modulus c' for FCC and BCT phases. Enables verification of mechanical stability criteria.
- schema:
  - `type`: object
  - `required`: `fcc`, `bct`
  - `properties`:
    - `fcc`:
      - `type`: object
      - `required`: `c11`, `c12`, `c44`, `c_prime`
      - `units`: GPa
    - `bct`:
      - `type`: object
      - `required`: `c11`, `c12`, `c13`, `c33`, `c44`, `c66`, `c_prime`
      - `units`: GPa

### gibbs_free_energy_difference.csv
- path: `/app/outputs/gibbs_free_energy_difference.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Gibbs free energy difference between BCT and FCC as a function of temperature at 80 GPa. Shows the sign change near ~600 K where BCT becomes stable.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `delta_G_eV_per_atom`
  - `units`:
    - `temperature_K`: K
    - `delta_G_eV_per_atom`: eV/atom

Notes: Process steps 3 and 4 are essential to compute the phonon and quasi-harmonic free energies; the Gibbs free energy step is load-bearing to ensure they are executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_vs_ca.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "c/a_ratio",
          "total_energy_per_atom_eV"
        ],
        "units": {
          "c/a_ratio": "dimensionless",
          "total_energy_per_atom_eV": "eV/atom"
        }
      },
      "description": "DFT total energy per atom as a function of tetragonal ratio c/a at fixed volume 8.99 Å³/atom. Reveals the global FCC minimum and a local BCT minimum."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "fcc",
          "bct"
        ],
        "properties": {
          "fcc": {
            "type": "object",
            "required": [
              "c11",
              "c12",
              "c44",
              "c_prime"
            ],
            "units": "GPa"
          },
          "bct": {
            "type": "object",
            "required": [
              "c11",
              "c12",
              "c13",
              "c33",
              "c44",
              "c66",
              "c_prime"
            ],
            "units": "GPa"
          }
        }
      },
      "description": "Elastic stiffness constants and shear modulus c' for FCC and BCT phases. Enables verification of mechanical stability criteria."
    },
    {
      "file": "gibbs_free_energy_difference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "delta_G_eV_per_atom"
        ],
        "units": {
          "temperature_K": "K",
          "delta_G_eV_per_atom": "eV/atom"
        }
      },
      "description": "Gibbs free energy difference between BCT and FCC as a function of temperature at 80 GPa. Shows the sign change near ~600 K where BCT becomes stable."
    }
  ],
  "notes": "Process steps 3 and 4 are essential to compute the phonon and quasi-harmonic free energies; the Gibbs free energy step is load-bearing to ensure they are executed."
}
```

## How you are scored
A hidden verifier examines each of the three scored output files independently. It recomputes key quantities from the submitted data (e.g., energy differences, derived structural parameters, compliance with stability criteria, sign and zero-crossing of the free energy difference) and compares them against expected reference values and trends. The three stages are weighted: the Gibbs free energy difference carries the largest weight because it depends on the correct execution of the phonon and quasi-harmonic processing steps; the energy vs c/a curve and elastic constants also receive meaningful weight. The final reward is a combination of the per-stage scores. Fabricating numbers that merely match typical literature values is insufficient; the verifier checks internal consistency across the artifacts and evaluates whether the submitted data reflect a genuine computational workflow.
