# Pseudo Alloy Atom Model for Cs-K Alloys: Binding Energies and Elastic Properties

## Problem background
The Cs-K alloy system forms continuous solid solutions over the full composition range and is a prototypical binary alkali-metal system. Understanding the energetics of disordered alloys and predicting their total binding energies, bulk moduli, and heats of solution is a fundamental challenge in materials science. The Pseudo Alloy Atom (PAA) model replaces the disordered binary alloy by a hypothetical perfect monatomic crystal of pseudo atoms characterized by a mean valency and a single adjustable empty‑core radius. Within second‑order perturbation theory and the Ashcroft empty‑core pseudopotential, the model offers a computationally tractable route to compute alloy properties directly from lattice parameters. This task reproduces the PAA prediction of the alloying energetics for Cs–K across the entire composition range.

## Approach
Implement the Ashcroft empty‑core pseudopotential for a body‑centred cubic (BCC) lattice. The total energy per atom is expressed as a sum of the Madelung energy, uniform electron gas energy (kinetic, exchange, correlation), first‑order perturbation energy, and band‑structure energy, which involves a summation over nonzero reciprocal lattice vectors using the Ashcroft form factor and the static Lindhard dielectric function. The mean valency Z_av = 1 (both Cs and K are monovalent) and the lattice parameter varies with composition (Vegard's law). The empty‑core radius r_c^PAA is determined for each composition by solving the zero‑pressure condition dE/dr_s = 0 at the electron‑sphere radius r_s obtained from the experimental lattice constant extrapolated to 0 K. With r_c^PAA fixed, compute the total binding energy E (Rydberg), the bulk modulus B from the energy‑volume relation (using the compressibility ratio), and the heat of solution ΔH as the deviation of the alloy energy from the linear interpolation of the pure‑metal energies. The workflow proceeds composition by composition for eleven equispaced concentrations x = 0.0, 0.1, …, 1.0.

## Reproduction target
For each of the 11 Cs–K alloy compositions (x = 0.0, 0.1, …, 1.0), produce a CSV file (`results.csv`) with the following quantities computed by your code: composition_x, electron‑sphere radius r_s (bohr), empty‑core radius r_c^PAA (bohr), total binding energy E (Rydberg), bulk modulus B (erg/cm²), and heat of solution ΔH (mRyd). All values must be the result of your own implementation of the PAA model; simply reporting numbers found elsewhere is not sufficient. The CSV will be validated for format and schema, and then scored by a hidden checker that compares your computed E, B, and ΔH to independent reference data and verifies internal consistency of the energy with the reported r_s and r_c.

## Assets

- Cs-K lattice parameters from Pearson 1958
- Python scientific stack: numpy, scipy

## Workflow steps

### Step 1: Prepare lattice parameters and compute electron gas properties
- Role: process
- Action: From the provided experimental lattice constants (Pearson 1958) for Cs-K alloys at 11 compositions (x=0.0,0.1,...,1.0), extrapolate to 0 K using linear thermal expansion coefficients of pure Cs and K. Compute the electron‑sphere radius r_s (bohr), atomic volume Ω0, Madelung energy E_M, uniform electron gas energy E0, and free‑electron compressibility K0 for each composition.
- Evidence: `/app/outputs/step01_intermediates.csv`

### Step 2: Determine empty‑core radius r_c^PAA via zero‑pressure condition
- Role: process
- Action: Using the Ashcroft empty‑core energy expression for a BCC lattice with Z_av=1, numerically solve dE/dr_s=0 at the observed r_s for each composition to obtain the composition‑dependent empty‑core radius r_c^PAA (bohr). The sum over reciprocal lattice vectors must be performed. The obtained r_c^PAA values are required for final property calculations.
- Evidence: `/app/outputs/step02_rc_paa.csv`

### Step 3: Compute total binding energy, bulk modulus, and heat of solution
- Role: scored (load-bearing)
- Action: For each composition, using the determined r_c^PAA, compute: (a) first‑order perturbation energy E1 and band‑structure energy E_bs via summation over BCC reciprocal lattice vectors with the Ashcroft form factor and the static Lindhard dielectric function; (b) total binding energy per atom E (Ryd) from the full expression; (c) bulk modulus B (erg/cm^2) from the energy‑volume derivative and compressibility ratio; (d) heat of solution ΔH (mRyd) as E(x) – [(1–x)E(pure Cs) + x E(pure K)]. Write a CSV file results.csv with columns: composition_x, rs_bohr, rc_bohr, E_Ryd, B_erg_per_cm2, Delta_H_mRyd. All values must be the agent's own computed results.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: composition_x (float), rs_bohr (float), rc_bohr (float), E_Ryd (float), B_erg_per_cm2 (float), Delta_H_mRyd (float). 11 rows for fractional concentrations x = 0.0, 0.1, …, 1.0. Units: r_s and r_c in bohr; E in Rydberg; B in erg/cm^2; ΔH in mRyd.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed properties for 11 alloy compositions. The checker verifies that the reported E_Ryd is consistent with the given rs_bohr and rc_bohr via the Ashcroft empty‑core energy expression, and compares E_Ryd, B_erg_per_cm2, and Delta_H_mRyd against paper‑reported reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `composition_x`, `rs_bohr`, `rc_bohr`, `E_Ryd`, `B_erg_per_cm2`, `Delta_H_mRyd`
  - `units`:
    - `composition_x`: fraction
    - `rs_bohr`: bohr
    - `rc_bohr`: bohr
    - `E_Ryd`: Rydberg
    - `B_erg_per_cm2`: erg/cm^2
    - `Delta_H_mRyd`: mRyd

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_x",
          "rs_bohr",
          "rc_bohr",
          "E_Ryd",
          "B_erg_per_cm2",
          "Delta_H_mRyd"
        ],
        "units": {
          "composition_x": "fraction",
          "rs_bohr": "bohr",
          "rc_bohr": "bohr",
          "E_Ryd": "Rydberg",
          "B_erg_per_cm2": "erg/cm^2",
          "Delta_H_mRyd": "mRyd"
        }
      },
      "description": "Computed properties for 11 alloy compositions. The checker verifies that the reported E_Ryd is consistent with the given rs_bohr and rc_bohr via the Ashcroft empty‑core energy expression, and compares E_Ryd, B_erg_per_cm2, and Delta_H_mRyd against paper‑reported reference values within tolerances."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by an automated hidden verifier. The verifier first checks that all required columns and rows are present and correctly formatted. It then evaluates each of the three physical quantities:

- Total binding energy E (50% of overall reward): the verifier recomputes the expected energy from your reported r_s and r_c using the Ashcroft empty‑core expression and penalises inconsistencies; it also compares your E values against reference data within hidden tolerances.
- Bulk modulus B (25% of overall reward): compared against reference data.
- Heat of solution ΔH (25% of overall reward): compared against reference data.

For each quantity, meeting or exceeding the reference accuracy (i.e. being at least as close as the published values derived from independent measurements) earns full credit; credit decreases smoothly as the deviation grows beyond the allowed hidden threshold. The final reward is the weighted average of these sub‑scores. The verifier does not have access to your code; it only reads the final CSV and any evidence files you output.
