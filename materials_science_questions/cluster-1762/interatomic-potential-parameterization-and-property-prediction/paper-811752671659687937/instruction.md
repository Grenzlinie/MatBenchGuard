# Argon Ion Sputtering Yield of GaN Surfaces from Molecular Dynamics Simulations

## Problem background
Gallium nitride (GaN) is a key material for short-wavelength optoelectronic devices, but its chemical inertness means that dry etching using chlorine-based plasmas is essential for device fabrication. Molecular dynamics (MD) simulations can reveal the atomic-scale sputtering mechanisms when Ar ions impact a GaN surface, both with and without an adsorbed chlorine layer. The main quantity of interest is the sputtering yield – the average number of surface atoms ejected per incident ion – as a function of the ion energy and surface chemistry. This task asks you to compute these yields for Ga and N atoms on both clean and Cl-adsorbed wurtzite GaN(0001) surfaces.

## Approach
The system is modelled with a classical two-body interatomic potential that includes Coulomb interactions, Gilbert-type short-range repulsion, Morse-type covalent terms, and van der Waals forces. The potential parameters for the atomic species Ga, N, Ar, Cl, and Na are predetermined. You will construct a rectangular simulation cell of wurtzite GaN with the known lattice constants, then create a second cell that adds a half-monolayer of Cl atoms on the (0001) surface together with compensating Na atoms on the bottom. After equilibrating both cells at 300 K, you will perform independent Ar impact simulations at normal incidence, with incident energies of 100, 150, and 250 eV. For each surface condition and energy, you will average over 30 impacts with random lateral positions. An atom is considered sputtered when it travels farther than 6.1 nm above the surface. Finally, you will tabulate the average number of sputtered Ga and N atoms per impact, separately for the two surface chemistries.

## Reproduction target
Produce a CSV file, `sputtering_yields.csv`, with columns: `surface` (string, either `clean` or `Cl`), `energy_eV` (integer 100, 150, or 250), `species` (string `Ga` or `N`), `yield` (floating-point number, the average sputtered atoms per impact), and `num_impacts` (integer, the number of impacts used for averaging, should be 30). Each row gives the average yield for one species at one energy on one surface condition, averaged over 30 statistically independent Ar impacts.

## Assets

- LAMMPS: https://www.lammps.org

## Potential parameters

The two-body potential is defined in equation (1) with the following parameters. The Coulomb term uses effective charges $Z_i$ and Ewald summation. The Gilbert repulsion uses $f_0 = 41.86$ kJ/(nm·mol), repulsion radii $a$, and softness parameters $b$. The van der Waals term uses coefficients $c$. Covalent terms use $D_1$, $\beta_1$, $D_2$, $\beta_2$ only for the N–Ga pair. Other atom pairs use $D_1 = D_2 = 0$.

### Atomic parameters

| Species | $Z$ (e) | $a$ (nm) | $b$ (nm) | $c$ (kJ$^{1/2}$·nm$^3$/mol$^{1/2}$) |
|----------|---------|----------|----------|--------------------------------------|
| N        | -1.150  | 0.1970   | 0.0123   | 0.0364                               |
| Ga       | +1.150  | 0.0834   | 0.00911  | 0.0                                  |
| Ar       | 0       | 0.1878   | 0.0117   | 0.0788                               |
| Cl       | -0.480  | 0.2061   | 0.0190   | 0.0573                               |
| Na       | +0.480  | 0.1493   | 0.0120   | 0.0184                               |

### Pair-specific covalent parameters (only N–Ga)

| Pair  | $D_1$ (kJ/mol) | $\beta_1$ (nm$^{-1}$) | $D_2$ (kJ/mol) | $\beta_2$ (nm$^{-1}$) |
|-------|---------------|----------------------|---------------|----------------------|
| N–Ga  | -5250.5       | 20.0                 | 6581.7        | 40.0                 |

## Workflow steps

### Step 1: Build MD simulation cells
- Role: process
- Action: Construct wurtzite GaN rectangular cells for clean and Cl-adsorbed (0001) surfaces using lattice constants a=0.320031 nm, b=0.320031 nm, c=0.51574 nm, internal parameter u=0.369894, with dimensions 10a × 6b′ × 8c (b′ = √3 a). For the Cl-adsorbed cell, add 60 Cl atoms on the (0001) surface and 60 Na atoms on the bottom surface.
- Evidence: `/app/outputs/cell_setup.txt`

### Step 2: Equilibrate the system
- Role: process
- Action: For each cell, perform NVE MD relaxation using the two-body potential (Coulomb, Gilbert repulsion, Morse-type covalent, van der Waals) with the parameters given in the Potential parameters section above and Ewald summation. Thermostat the bottom one-pair Ga-N layer and Na atoms at 300 K. Run relaxation without Cl/Na then with Cl/Na.
- Evidence: `/app/outputs/equilibration_done.log`

### Step 3: Run Ar ion impact simulations
- Role: process
- Action: For each surface type (clean, Cl-adsorbed) and each incident energy (100, 150, 250 eV), conduct 30 independent Ar impacts at normal incidence with random lateral positions. Simulate each impact for at least 7 ps with a time step of 0.7–1.0 fs. Record atomic escape beyond 6.1 nm above the surface.
- Evidence: `/app/outputs/impact_trajectories.tar.gz`

### Step 4: Compute sputtering yields
- Role: scored (load-bearing)
- Action: From the impact simulation data, count the number of sputtered Ga and N atoms per impact, average over the 30 impacts for each condition, and write a CSV file.
- Output file: `/app/outputs/sputtering_yields.csv`
- Format: csv
- Contract: CSV with columns: surface (string, 'clean' or 'Cl'), energy_eV (int, one of 100,150,250), species (string, 'Ga' or 'N'), yield (float, average sputtered atoms per impact), num_impacts (int, should be 30)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sputtering_yields.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sputtering_yields.csv
- path: `/app/outputs/sputtering_yields.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sputtering yields for Ga and N on clean and Cl-adsorbed wurtzite GaN(0001) surfaces for Ar ion impacts at 100, 150, and 250 eV. The checker compares yields to the paper-reported values with appropriate tolerances and verifies the trend that Ga yield is negligible on clean surfaces and significant and energy-dependent on Cl-adsorbed surfaces.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `energy_eV`, `species`, `yield`, `num_impacts`
  - `units`:
    - `yield`: atoms/impact
    - `num_impacts`: integer count

Notes: The checker uses hidden reference values extracted from Fig. 4 of the paper and performs structural trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sputtering_yields.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "energy_eV",
          "species",
          "yield",
          "num_impacts"
        ],
        "units": {
          "yield": "atoms/impact",
          "num_impacts": "integer count"
        }
      },
      "description": "Sputtering yields for Ga and N on clean and Cl-adsorbed wurtzite GaN(0001) surfaces for Ar ion impacts at 100, 150, and 250 eV. The checker compares yields to the paper-reported values with appropriate tolerances and verifies the trend that Ga yield is negligible on clean surfaces and significant and energy-dependent on Cl-adsorbed surfaces."
    }
  ],
  "notes": "The checker uses hidden reference values extracted from Fig. 4 of the paper and performs structural trend checks."
}
```

## How you are scored
Your submitted sputtering yields will be evaluated by a hidden verifier against reference values and structural trends. The verifier checks whether the Ga yield on the clean surface is negligible (essentially zero) and whether the yields on the Cl-adsorbed surface are positive and increase with impact energy. Meeting or exceeding these expected trends earns full credit; the verification tolerances are chosen to absorb the natural spread of independent MD implementations. Simply reporting a plausible number without running the simulation protocol is not sufficient – the verifier may also inspect the intermediate process evidence (cell construction log, equilibration confirmation, impact trajectories) that documents the required workflow.
