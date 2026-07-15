# MD Simulation of Oxygen Diffusion in a Layered Tetrahedral Network

## Problem background
Melilite-type gallate ceramics are promising oxide ion conductors for applications such as solid oxide fuel cells. They feature a layered tetrahedral network that can accommodate excess interstitial oxygen atoms within pentagonal rings. The compound La2Ga3O7.5 represents the composition with the maximum possible interstitial oxygen content, and it crystallizes in a fully ordered orthorhombic superstructure. Despite having the highest interstitial concentration, its ionic conductivity is significantly lower than that of disordered melilites. Understanding the migration mechanism of the interstitial oxide ions in this ordered superstructure is key to explaining this unexpected behaviour and to designing better conductors. This task uses molecular dynamics simulations to determine the diffusion pathways, quantify the oxide ion mobility, and assess the dimensionality of ion transport in La2Ga3O7.5.

## Approach
The oxide ion dynamics are modelled by classical molecular dynamics (MD) with interatomic potentials of the Buckingham form supplemented by a shell model for oxygen polarizability. The following potential parameters are used:

| Interaction   | A (eV)   | ρ (Å) | C (eV·Å⁶) | Y (e)  | k (eV·Å⁻²) |
|---------------|----------|-------|-----------|--------|------------|
| La³⁺ – O²⁻    | 4317.17  | 0.2987| 0.0       | –      | –          |
| Ga³⁺ – O²⁻    | 2399.776 | 0.2742| 0.0       | –      | –          |
| O²⁻ – O²⁻     | 25.41    | 0.6937| 0.0       | –2.513 | 0          |

A 3×3×3 supercell (2700 atoms) is built from the experimental orthorhombic crystal structure. The cell is first relaxed to equilibrium via energy minimization. NVT MD simulations are then run at five temperatures (1473, 1673, 1873, 2073, and 2273 K) with a small time step of 0.05 fs, using a production period of 200 ps after equilibration. From the atomic trajectories, the mean square displacements (MSDs) of oxygen atoms are calculated. The total diffusion coefficient D at each temperature is obtained by linear regression of the long-time MSD. Fitting the diffusion coefficients to an Arrhenius law yields the activation energy for oxide ion migration. To probe the dimensionality of the diffusion, the components of the MSD along the three crystal axes are computed at 1473 K and converted to directional diffusion coefficients D_a, D_b, and D_c. The relative magnitudes of these components reveal whether the transport is isotropic, two-dimensional, or effectively one-dimensional.

## Reproduction target
Produce a JSON file containing the following quantities:
- The temperatures (K) at which the simulations were performed.
- The total oxygen diffusion coefficient D (in cm²/s) at each temperature.
- The activation energy Ea (in eV) obtained from an Arrhenius fit to the D(T) data.
- The directional diffusion coefficients D_a, D_b, D_c (in cm²/s) computed at 1473 K.
The goal is to obtain a physically meaningful set of diffusion coefficients that follow Arrhenius behaviour, and a pattern of directional components D_a, D_b, D_c at 1473 K that characterizes the dimensionality of the oxide ion migration in the ordered superstructure.

## Assets

- La2Ga3O7.5 crystal structure (CIF): 10.1021/acs.chemmater.0c02983
- Buckingham potential parameters (La-O, Ga-O, O-O) and shell model
- LAMMPS: https://lammps.sandia.gov
- Python scientific libraries: numpy, scipy

## Workflow steps

### Step 1: Build supercell and relax structure
- Role: process
- Action: Construct a 3×3×3 supercell of La2Ga3O7.5 from the provided CIF file using the Buckingham+shell model potentials, perform energy minimization to relax the structure, and output the relaxed supercell.
- Evidence: `/app/outputs/relaxed_supercell.lammps-data`

### Step 2: Run MD simulations at multiple temperatures
- Role: process
- Action: Using the relaxed supercell, run NVT molecular dynamics simulations at 1473, 1673, 1873, 2073, and 2273 K with a 0.05 fs timestep. Equilibrate and then run production for 200 ps to generate atomic trajectories.
- Evidence: `/app/outputs/md_simulation_log.txt`

### Step 3: Compute diffusion coefficients and activation energy
- Role: scored (load-bearing)
- Action: From the MD trajectories, compute mean square displacements (MSDs) of oxygen atoms. Extract total diffusion coefficients D by linear regression of MSD vs time. Fit an Arrhenius law to obtain activation energy. Also compute the directional components of D along the a, b, c axes at 1473 K. Write the results to msd_diffusion_coefficients.json.
- Output file: `/app/outputs/msd_diffusion_coefficients.json`
- Format: json
- Contract: {"temperatures": [1473, 1673, 1873, 2073, 2273], "D_total": [float, ...], "activation_energy": float, "D_a_1473K": float, "D_b_1473K": float, "D_c_1473K": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/msd_diffusion_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### msd_diffusion_coefficients.json
- path: `/app/outputs/msd_diffusion_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed oxygen diffusion coefficients, activation energy, and directional components confirming one-dimensional transport.
- schema:
  - `type`: object
  - `required`:
    - `temperatures`: array of numbers (K)
    - `D_total`: array of numbers (cm^2/s)
    - `activation_energy`: number (eV)
    - `D_a_1473K`: number (cm^2/s)
    - `D_b_1473K`: number (cm^2/s)
    - `D_c_1473K`: number (cm^2/s)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `temperatures`: K
    - `D_total`: cm^2/s
    - `activation_energy`: eV
    - `D_a_1473K`: cm^2/s
    - `D_b_1473K`: cm^2/s
    - `D_c_1473K`: cm^2/s

Notes: The activation energy and anisotropy condition are the main scored targets; activation energy is compared to a hidden reference within tolerance, and the directional components must show a ratio D_a/D_b > 10 and D_c negligible relative to D_b to confirm one-dimensional transport.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "msd_diffusion_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "temperatures": "array of numbers (K)",
          "D_total": "array of numbers (cm^2/s)",
          "activation_energy": "number (eV)",
          "D_a_1473K": "number (cm^2/s)",
          "D_b_1473K": "number (cm^2/s)",
          "D_c_1473K": "number (cm^2/s)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "temperatures": "K",
          "D_total": "cm^2/s",
          "activation_energy": "eV",
          "D_a_1473K": "cm^2/s",
          "D_b_1473K": "cm^2/s",
          "D_c_1473K": "cm^2/s"
        }
      },
      "description": "Computed oxygen diffusion coefficients, activation energy, and directional components confirming one-dimensional transport."
    }
  ],
  "notes": "The activation energy and anisotropy condition are the main scored targets; activation energy is compared to a hidden reference within tolerance, and the directional components must show a ratio D_a/D_b > 10 and D_c negligible relative to D_b to confirm one-dimensional transport."
}
```

## How you are scored
A hidden verifier reads the output file `msd_diffusion_coefficients.json` and checks the reported values. It evaluates two main aspects: (1) the activation energy and the set of total diffusion coefficients are compared to reference values derived from the literature (with tolerances that account for the differences in MD codes, random seeds, and implementation details); (2) the directional diffusion components at 1473 K are examined for a strong anisotropy pattern that indicates the dimensionality of the transport. The final reward is a weighted sum of these checks. Simply hard‑coding a known set of numbers without having actually performed the simulations is not sufficient to achieve a high score.
