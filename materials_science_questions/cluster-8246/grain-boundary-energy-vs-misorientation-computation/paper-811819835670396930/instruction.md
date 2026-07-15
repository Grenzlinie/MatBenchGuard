# 2D Monte Carlo Potts Simulation of Texture Evolution in Cu Thin Films

## Problem background
Grain growth in thin Cu films during annealing leads to a preferred crystallographic texture — the distribution of crystallographic orientations of individual grains relative to the film normal. The evolution is governed by a competition among surface/interface energy, biaxial strain energy, and grain boundary energy. Additionally, annealing twin boundaries with lower energy can form and influence the texture by favoring twin-related orientations. This task studies the texture evolution predicted by a 2D Monte Carlo Potts model that incorporates all these energetic contributions. The goal is to simulate the model for three film thicknesses and compute, at the end of the simulation, the fractions of grains oriented with {111}, {001}, {511}, and {101} planes parallel to the film surface.

## Approach
The approach uses a 2D Monte Carlo Potts model on a triangular lattice with periodic boundary conditions. The Hamiltonian contains four terms: (i) surface energy from a broken‑bond model dependent on the crystallographic plane normal, parameterised by the (100) surface energy at a reference temperature and its temperature derivative; (ii) interface energy taken equal to the surface energy; (iii) biaxial strain energy proportional to film thickness, the square of the thermal mismatch strain (from deposition to annealing temperature), and the biaxial modulus of the grain (computed from the elastic constants and their temperature derivatives); (iv) grain‑boundary energy separated into large‑angle (LAGB), incoherent twin (ICTB), and coherent twin (CTB) contributions, each with an energy at a reference temperature and a temperature derivative. Reorientation attempts follow a standard Metropolis probability. The simulation is run for three film thicknesses (100 nm, 500 nm, 800 nm) at a fixed annealing temperature until the texture fractions stabilise. The orientation of every lattice site is recorded at regular Monte Carlo steps and at the final step, and then classified into one of the four texture components based on a misorientation tolerance relative to the ideal orientations.

## Reproduction target
Implement the 2D Monte Carlo Potts simulation model described in the approach above and run it for film thicknesses of 100 nm, 500 nm, and 800 nm at the annealing temperature of 300 °C. From the final orientation state of each simulation, classify every lattice site into the texture components {111}, {001}, {511}, and {101} and compute the volume fraction of each component. Provide a time‑resolved record of these fractions in `texture_fractions.csv` (one row per snapshot per thickness) and a final summary in `final_texture_summary.json` with the fractions for each thickness.

## Assets

- Python scientific computing stack (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Implement the Monte Carlo Potts simulation model
- Role: process
- Action: Implement a 2D Monte Carlo Potts simulation on a triangular lattice (6 nearest-neighbours) with periodic boundary conditions. The system has Q=3722 distinct crystallographic orientations (Bunge Euler angles). The total Hamiltonian includes surface energy (broken-bond model with γ0(100)=2.610 J/m² at 200°C and dγ/dT=-5.0e-4 J/(m²°C)), interface energy (equal to surface), biaxial strain energy (γ_strain = h e² ∫ M_hkl dA_hkl, with thermal mismatch strain e ≈ Δα·ΔT, Δα = 14e-6 /K, ΔT = 275°C from deposition 25°C to anneal 300°C, and biaxial modulus M_hkl computed from elastic constants C11=170.2 GPa, C12=123.2 GPa, C44=75.4 GPa at 25°C with temperature derivatives dC11/dT=-0.0353 GPa/°C, dC12/dT=-0.0153 GPa/°C, dC44/dT=-0.0277 GPa/°C), and grain-boundary energy separated into large-angle (LAGB), incoherent twin (ICTB), and coherent twin (CTB) contributions (γ_LAGB=0.625 J/m² at 925°C, γ_ICTB=0.498 J/m² at 950°C, γ_CTB=0.024 J/m² at 800°C with temperature derivatives dγ_LAGB/dT=-1.0e-4, dγ_ICTB/dT=-1.0e-4, dγ_CTB/dT=-2.0e-5 J/(m²°C)). The reorientation probability is p=1 for ΔE≤0 and p=exp(-ΔE/(k_B T)) for ΔE>0, where T=300°C annealing temperature and k_B is Boltzmann constant. The n-fold algorithm may optionally be used to accelerate late-stage growth, but a standard Metropolis loop is acceptable. No external data—embed all constants directly.
- Evidence: none

### Step 2: Run grain growth simulations for three film thicknesses
- Role: process
- Action: Using the implemented model, simulate grain growth for film thicknesses h = 100 nm, 500 nm, and 800 nm at 300°C. Use a lattice size of at least 200×200 sites and periodic boundary conditions. Run the simulation until the major texture components stabilise (typically thousands of Monte Carlo steps, MCS). For each thickness, record the orientation (Bunge Euler angles) of every lattice site at regular MCS intervals (e.g., every 500 or 1000 MCS) and at the final MCS. Save the full time series of orientation maps for later analysis.
- Evidence: `/app/outputs/simulation_state.pkl`

### Step 3: Extract time-series texture component fractions
- Role: scored
- Action: For each recorded MCS snapshot and for each thickness, classify every lattice site into one of the texture components {111}, {001}, {511}, {101} by comparing its Bunge Euler angle orientation to the ideal orientation of each component (use a misorientation tolerance, e.g., 15°). Compute the volume fraction of each component at that MCS. Write the time-series data to texture_fractions.csv with columns: thickness_nm (int), MCS (int), fraction_111 (float), fraction_001 (float), fraction_511 (float), fraction_101 (float). Include rows for every recorded snapshot, including the final MCS.
- Output file: `/app/outputs/texture_fractions.csv`
- Format: csv
- Contract: CSV with columns: thickness_nm (int), MCS (int), fraction_111 (float), fraction_001 (float), fraction_511 (float), fraction_101 (float). One row per snapshot per thickness.
- Scoring: scored by hidden verifier

### Step 4: Extract final texture summary
- Role: scored
- Action: From the final MCS orientation data for each film thickness (100 nm, 500 nm, 800 nm), compute the final fractions of the {111}, {001}, {511}, and {101} texture components (using the same misorientation classification as in step 03). Write these final fractions to final_texture_summary.json as a JSON object with top-level keys "100nm", "500nm", "800nm". Each key maps to an object containing the keys "fraction_111", "fraction_001", "fraction_511", and "fraction_101" with their numeric final values.
- Output file: `/app/outputs/final_texture_summary.json`
- Format: json
- Contract: JSON object with keys '100nm', '500nm', '800nm'. Each value is an object with keys 'fraction_111', 'fraction_001', 'fraction_511', 'fraction_101' (numeric fractions).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/texture_fractions.csv`
- `/app/outputs/final_texture_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### texture_fractions.csv
- path: `/app/outputs/texture_fractions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Time series of texture component fractions for each film thickness and Monte Carlo step.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `MCS`, `fraction_111`, `fraction_001`, `fraction_511`, `fraction_101`
  - `units`:
    - `thickness_nm`: nm
    - `MCS`: Monte Carlo steps
    - `fraction_111`: fraction
    - `fraction_001`: fraction
    - `fraction_511`: fraction
    - `fraction_101`: fraction

### final_texture_summary.json
- path: `/app/outputs/final_texture_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Final texture component fractions for the 100 nm, 500 nm, and 800 nm films.
- schema:
  - `type`: object
  - `required`:
    - `100nm`: object
    - `500nm`: object
    - `800nm`: object
  - `items`:
    - `fraction_111`: float
    - `fraction_001`: float
    - `fraction_511`: float
    - `fraction_101`: float

Notes: The checker reads both artifacts and applies threshold checks on the final fractions (e.g., {111} dominance in 100 nm films, {001} dominance in 800 nm films, appearance of {511} twin component in 500 nm films). The CSV is used to verify simulation length (MCS > 1000) and fractions-sum sanity. All scoring uses tolerance margins appropriate for stochastic simulation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "texture_fractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "MCS",
          "fraction_111",
          "fraction_001",
          "fraction_511",
          "fraction_101"
        ],
        "units": {
          "thickness_nm": "nm",
          "MCS": "Monte Carlo steps",
          "fraction_111": "fraction",
          "fraction_001": "fraction",
          "fraction_511": "fraction",
          "fraction_101": "fraction"
        }
      },
      "description": "Time series of texture component fractions for each film thickness and Monte Carlo step."
    },
    {
      "file": "final_texture_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "100nm": "object",
          "500nm": "object",
          "800nm": "object"
        },
        "items": {
          "fraction_111": "float",
          "fraction_001": "float",
          "fraction_511": "float",
          "fraction_101": "float"
        }
      },
      "description": "Final texture component fractions for the 100 nm, 500 nm, and 800 nm films."
    }
  ],
  "notes": "The checker reads both artifacts and applies threshold checks on the final fractions (e.g., {111} dominance in 100 nm films, {001} dominance in 800 nm films, appearance of {511} twin component in 500 nm films). The CSV is used to verify simulation length (MCS > 1000) and fractions-sum sanity. All scoring uses tolerance margins appropriate for stochastic simulation spread."
}
```

## How you are scored
A hidden verifier reads your `final_texture_summary.json` and `texture_fractions.csv`. It first checks that the simulation ran for a non‑trivial number of Monte Carlo steps and that the reported fractions sum approximately to 1. It then compares the final texture fractions for each film thickness against the expected qualitative pattern: which orientation dominates for the thinnest film, which orientation dominates for the thickest film, and whether a twin‑related component appears at intermediate thickness. Because the simulation is stochastic, the verifier uses generous tolerances. Your overall reward is proportional to how many of these trend conditions are satisfied; simply reporting the paper's numbers is not enough — the verifier expects results genuinely derived from the simulation you ran.
