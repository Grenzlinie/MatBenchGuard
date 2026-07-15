# MD Simulation of Self-Diffusion in Supercooled Iron using Pak-Doyama Potential

## Problem background
Supercooled liquid iron exhibits a glass transition when a percolation cluster of icosahedra forms, drastically altering atomic dynamics. Molecular dynamics simulation with the Pak-Doyama pair potential reveals that the mean‑square displacement (MSD) of atoms below the glass transition acquires a nonlinear, two‑component character: a logarithmic term from irreversible structural relaxation plus a linear Einstein diffusion term. The present task extracts the self‑diffusion activation parameters — activation energies and pre‑exponential factors — that characterize atomic transport in the supercooled melt and in the metallic glass states, as determined by this model.

## Approach
Build a molecular dynamics simulation of 100 000 iron atoms interacting via the Pak‑Doyama pair potential. Start from a random close‑packed configuration at 2300 K and equilibrate. Then instantaneously supercool the system to a series of target temperatures between 1240 K and 900 K and perform cyclic isothermal annealing. From the recorded trajectories, compute the mean‑square atomic displacement as a function of time after a fixed preannealing period. Fit each MSD curve with the two‑component model ⟨Δr²(t)⟩ = a k_B T ln(t/τ+1) + 6 D t to separate the structural relaxation contribution from the self‑diffusion coefficient D. Collect D(T) for all temperatures, split the data into the supercooled‑melt and metallic‑glass regimes, and perform an Arrhenius analysis (ln D vs. 1/T) to obtain the activation energy and pre‑exponential factor for each regime.

## Reproduction target
Perform the full MD workflow to compute the self‑diffusion coefficients D(T) for a set of supercooled iron temperatures and then derive the Arrhenius activation parameters separately for the supercooled melt (high‑temperature regime) and the metallic glass (low‑temperature regime). Output the activation energies (in eV) and the pre‑exponential factors (in m²/s) for both regimes as the file /app/outputs/diffusion_activation_parameters.json.

## Assets

- LAMMPS: https://lammps.sandia.gov/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate initial liquid iron configuration
- Role: process
- Action: Create a random close-packed configuration of 100000 iron atoms in a cubic box with periodic boundaries at density 7800 kg/m³. Assign Maxwell-distributed velocities at 2300 K.
- Evidence: none

### Step 2: Equilibrate the liquid at 2300 K
- Role: process
- Action: Run MD with the Pak-Doyama potential at fixed volume and T=2300 K: 3000 isothermal steps followed by 3000 adiabatic steps (Δ t = 1.523×10⁻¹⁵ s, Verlet integration).
- Evidence: none

### Step 3: Instantaneous quench and isothermal annealing
- Role: process
- Action: Instantaneously change temperature to each target (1240 K down to 900 K in 20 K steps). Run cyclic annealing (1000Δ t isothermal + 4000Δ t adiabatic per cycle) until rapid crystallization. Record atom trajectories and system energies.
- Evidence: `/app/outputs/trajectories.lammpstrj`

### Step 4: Compute mean-square displacement
- Role: process
- Action: After each annealing cycle, quench to 0 K to establish reference positions; compute mean-square atomic displacement ⟨Δ r²(t)⟩ as a function of time t from the start of the current cycle (preannealing time τ=0.7615×10⁻¹¹ s). Output MSD(t) curves for every temperature.
- Evidence: `/app/outputs/msd_data.csv`

### Step 5: Fit two-component model to MSD data
- Role: process
- Action: For each temperature, fit the equation ⟨Δ r²(t)⟩ = a k_B T ln(t/τ+1) + 6 D t to the MSD data using non-linear least squares, extracting the product a = δr² n₀ Ω and the self-diffusion coefficient D.
- Evidence: `/app/outputs/DT_values.csv`

### Step 6: Arrhenius analysis of self-diffusion
- Role: scored (load-bearing)
- Action: Separate the D(T) data into supercooled melt and metallic glass regimes; perform separate linear fits of ln D = ln D₀ − Eₐ/(k_B T) to obtain activation energies and pre-exponential factors. Write the results to /app/outputs/diffusion_activation_parameters.json.
- Output file: `/app/outputs/diffusion_activation_parameters.json`
- Format: json
- Contract: {"Ea_melt_eV": "number", "D0_melt_m2_per_s": "number", "Ea_glass_eV": "number", "D0_glass_m2_per_s": "number"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/diffusion_activation_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_activation_parameters.json
- path: `/app/outputs/diffusion_activation_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Self-diffusion activation energy and pre-exponential factor for the supercooled melt (above Tg) and metallic glass (below Tg) obtained from Arrhenius analysis of MD-derived self-diffusion coefficients.
- schema:
  - `type`: object
  - `required`:
    - `Ea_melt_eV`: number
    - `D0_melt_m2_per_s`: number
    - `Ea_glass_eV`: number
    - `D0_glass_m2_per_s`: number

Notes: The icosahedral percolation cluster analysis and nucleation timing are not reproduced; only the diffusion activation parameters are targeted. The workflow uses the Pak-Doyama pair potential and LAMMPS as the MD engine.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_activation_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Ea_melt_eV": "number",
          "D0_melt_m2_per_s": "number",
          "Ea_glass_eV": "number",
          "D0_glass_m2_per_s": "number"
        }
      },
      "description": "Self-diffusion activation energy and pre-exponential factor for the supercooled melt (above Tg) and metallic glass (below Tg) obtained from Arrhenius analysis of MD-derived self-diffusion coefficients."
    }
  ],
  "notes": "The icosahedral percolation cluster analysis and nucleation timing are not reproduced; only the diffusion activation parameters are targeted. The workflow uses the Pak-Doyama pair potential and LAMMPS as the MD engine."
}
```

## How you are scored
A hidden verifier will check the contents of diffusion_activation_parameters.json. It will compare the activation energies and pre‑exponential factors for the melt and the glass against independently determined reference values. It will also verify that the glass activation energy is greater than the melt activation energy, and that the glass pre‑exponential factor is greater than the melt pre‑exponential factor. Credit is awarded based on the agreement of each parameter with the reference and the correctness of the structural ordering.
