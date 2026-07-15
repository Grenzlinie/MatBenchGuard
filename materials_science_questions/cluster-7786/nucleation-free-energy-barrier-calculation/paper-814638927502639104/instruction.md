# Effect of compositional fluctuations on nucleation kinetics

## Problem background
In multicomponent alloys, precipitate nucleation from a supersaturated solid solution can be strongly affected by spatial fluctuations in composition. This work studies a model Fe–Cr–C (A–B–C) system in which (A,B)₃C carbides form by combining substitutional A and B atoms with interstitial carbon. Classical nucleation theory is applied locally at each bcc lattice site, making the nucleation barrier depend on the local B content. The question is how different spatial arrangements of A and B atoms—random, regular, or homogeneous—alter the nucleation kinetics, especially at high interface energies. Reproducing the evolution of the precipitate number density for the three arrangements under specified conditions will quantify the role of compositional fluctuations.

## Approach
A simulation box of a large bcc lattice (300×300×300 unit cells) with periodic boundary conditions is populated with A and B atoms in three ways: (1) random – each site independently assigned A or B with probability equal to the average B fraction; (2) regular – a periodic placement that gives the same average B content; (3) homogeneous – every site has the same effective composition, not discrete atoms.
For each site, a local critical nucleus is considered. The chemical driving force ΔF is determined from a provided lookup table as a function of the local B fraction inside a sphere of arbitrary radius; then the nucleation barrier G* and critical radius ρ* are computed from CNT: G* = 16πγ³/(3ΔF²), ρ* = 2γ/ΔF, with γ = 0.20 J/m².
Using material parameters (C diffusivity, lattice spacing, atomic volume, equilibrium C site fractions, temperature = 773 K), the steady‑state nucleation rate J^SS and attachment rate β* are evaluated. A random number s ∈ [0,1] is drawn for every site, and the equation η(t) = 1 − exp(−J^SS t / N₀) is solved to obtain a nucleation time t_p^{nuc} for that site.
All sites are sorted by their nucleation times. Beginning with the earliest time, each site is checked: if it lies within the carbon‑depleted zone (radius Z_p = α ρ_p) of a previously nucleated and growing precipitate, it is skipped; otherwise a precipitate nucleates at that site with initial radius ρ*, and its depleted zone grows according to a diffusion‑controlled growth law. The growth uses the average ΔF and the given diffusion parameters. The procedure continues until all sites are processed or the box is filled.
The recorded nucleated precipitates and their nucleation times yield the cumulative number density (precipitates per m³) as a function of time for each atomic arrangement. The final artifact is a time series comparing random, regular, and homogeneous cases.

## Reproduction target
Carry out the full pipeline described in the Approach section and produce the file `nucleation_kinetics.csv` with the following columns:
- `time` (seconds, float)
- `arrangement` (string: one of `random`, `regular`, `homogeneous`)
- `number_density` (precipitates per cubic meter, float)
The time series must span from early times (≈ 10² s) to at least 10⁸ s, with enough points to resolve the evolution of the number density for all three arrangements.
The simulation must be run for the parameter set: temperature 773 K, average B site fraction 0.0185, specific interface energy γ = 0.20 J/m², and the carbon‑related constants provided in the workflow steps. The output will be evaluated by comparing the nucleation kinetics among the three atomic arrangements; the exact number of precipitates is not prescribed, but the relative behavior must be consistent with the effect of compositional fluctuations.

## Assets

- Thermodynamic driving force ΔF(Y_B) table

## Workflow steps

### Step 1: Generate simulation box
- Role: process
- Action: Generate a bcc lattice of 300³ unit cells (~54 million sites) with periodic boundary conditions. Populate the lattice with A and B atoms according to random, regular, and homogeneous distributions for B site fraction 0.0185. Store the simulation box for all three arrangements.
- Evidence: none

### Step 2: Compute local nucleation barriers
- Role: process
- Action: For each lattice site, determine the local B fraction within a spherical cluster of varying radius (number of C atoms), compute the local chemical driving force ΔF using the provided lookup table, and calculate the nucleation barrier G* and critical radius ρ* using classical nucleation theory (G* = 16πγ³/(3ΔF²), ρ* = 2γ/ΔF) with γ = 0.20 J/m². Record barriers and critical radii for all sites.
- Evidence: none

### Step 3: Assign nucleation times
- Role: process
- Action: For each potential nucleation site, compute the steady-state nucleation rate J^SS from the CNT rate expression and attachment rate β* using material parameters (D_C^M = 1.6×10⁻¹² m²/s, a = 0.248 nm, Ω = 1.18×10⁻²⁹ m³, Y_C^Meq = 4.63×10⁻⁴, Y_C^P = 1/3, etc.). Draw a random number s from [0,1] for each site and solve η(t_p^{nuc}) = s using η(t)=1−exp(−J^SS t) to obtain the nucleation time t_p^{nuc}. Assign each site a nucleation time.
- Evidence: none

### Step 4: Simulate nucleation kinetics with growth and exclusion
- Role: process
- Action: Sort sites by increasing nucleation time. Process sites in order: for each site, check whether it lies inside the C-depleted zone (radius Z_p = α ρ_p) of any already nucleated precipitate at the current time. If not, nucleate a precipitate at this site with initial radius ρ*, and let it grow according to the diffusion-controlled growth law (analytical solution) using the average ΔF and prescribed parameters. Update the depleted zone radii. Continue until all sites are processed or the box is filled. Record the set of nucleated precipitates and their nucleation times.
- Evidence: none

### Step 5: Compute number density evolution
- Role: scored (load-bearing)
- Action: From the recorded precipitates, compute the cumulative number density (precipitates per m³) as a function of time for each of the three atomic arrangements. Write the time series to the file nucleation_kinetics.csv with columns: time (s), arrangement, number_density.
- Output file: `/app/outputs/nucleation_kinetics.csv`
- Format: csv
- Contract: time (s): float, arrangement: string (one of 'random','regular','homogeneous'), number_density (m^-3): float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_kinetics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_kinetics.csv
- path: `/app/outputs/nucleation_kinetics.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time series of precipitate number density for random, regular, and homogeneous atomic arrangements. The checker verifies structural trends consistent with the paper's claims: the random arrangement yields a significantly earlier onset and higher number density than regular and homogeneous, with at least an order-of-magnitude enhancement at early times and a large speed‑up in time to reach a reference density.
- schema:
  - `type`: table
  - `required_columns`: `time`, `arrangement`, `number_density`
  - `units`:
    - `time`: s
    - `number_density`: m^-3

Notes: The ΔF(Y_B) lookup table is provided in the task instruction. The stochastic nature of nucleation may cause run‑to‑run scatter; scoring is based on relative structural trends rather than exact numeric values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_kinetics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "arrangement",
          "number_density"
        ],
        "units": {
          "time": "s",
          "number_density": "m^-3"
        }
      },
      "description": "Time series of precipitate number density for random, regular, and homogeneous atomic arrangements. The checker verifies structural trends consistent with the paper's claims: the random arrangement yields a significantly earlier onset and higher number density than regular and homogeneous, with at least an order-of-magnitude enhancement at early times and a large speed‑up in time to reach a reference density."
    }
  ],
  "notes": "The ΔF(Y_B) lookup table is provided in the task instruction. The stochastic nature of nucleation may cause run‑to‑run scatter; scoring is based on relative structural trends rather than exact numeric values."
}
```

## How you are scored
A hidden verifier reads your `nucleation_kinetics.csv` and computes several structural properties for each arrangement — for example, the number density at a given time, and the time needed to reach a reference density. It checks that the random arrangement exhibits faster nucleation kinetics (earlier onset, higher number density) compared to the regular and homogeneous arrangements, and that the magnitude of the speed‑up is in agreement with known predictions. The verifier uses thresholds that account for the stochastic nature of the nucleation‑time assignment; exact numerical match with any published curve is not required.
Each scored stage of the workflow contributes a portion of the total reward, and the final score is a weighted sum. Simply reporting a value from the literature without executing the simulation will not satisfy the checks.
