# Equilibrium Shape and Surface Diffusion of SiC Nanoparticles from MD

## Problem background
Ceramic nanocrystals such as silicon carbide (SiC) exhibit properties that depend sensitively on their shape. The equilibrium shape of a nanocrystal is determined by the minimization of surface free energy, which produces facets — flat crystal planes. However, the kinetic pathways and atomic-level mechanisms by which a nanoparticle transforms from an arbitrary initial shape to its final faceted equilibrium shape are largely unknown. Directly observing and quantifying this transformation is challenging, as faceting can involve rare events and long timescales. In this work, molecular dynamics simulations are used to model the shape evolution of an 8 nm spherical SiC nanoparticle at high temperature, providing atomic-scale insight into how facets form and what surface diffusion processes drive them.

## Approach
The production workflow comprises three stages: (1) build the initial system — an 8 nm diameter spherical SiC nanoparticle carved from a 3C-SiC lattice; (2) run an NVT molecular dynamics simulation in vacuum at 2200 K for 1 microsecond using the Vashishta interatomic potential; (3) analyse the resulting trajectory. The analysis is split into two scored deliverables: (a) from the final 100 ns of the trajectory, identify the (110) and (111) facets, compute the average distances from the particle centre to each set of facet planes, and deduce the surface energy ratio E_110/E_111 via the Wulff construction; (b) from the first 100 ps, isolate atoms in the top three surface layers and compute their mean-squared displacement to extract the surface diffusion coefficients of Si and C atoms.

## Reproduction target
Produce the following two scored artifacts for the spherical SiC nanoparticle (8 nm diameter, T=2200 K, 1 µs simulation): (i) equilibrium_shape.json containing the mean distances from the particle centre to the (110) and (111) planes and the derived surface energy ratio; (ii) diffusion_coefficients.json containing the surface diffusion coefficients of Si and C atoms during the early faceting stage (0–100 ps), together with the temperature and time range used. The output contract defines the exact JSON schemas.

## Assets

- LAMMPS: https://www.lammps.org/
- Vashishta SiC potential parameters: 10.1063/1.2746028

## Workflow steps

### Step 1: Generate initial spherical SiC nanoparticle
- Role: process
- Action: Create an 8 nm diameter spherical SiC nanoparticle from bulk 3C-SiC (lattice constant 4.358 Å). Delete atoms outside the sphere and restore stoichiometry by adding atoms. Output a LAMMPS data file.
- Evidence: `/app/outputs/init_nanoparticle.data`

### Step 2: Run MD simulation at 2200 K
- Role: process
- Action: Run an NVT MD simulation of the spherical nanoparticle at 2200 K using the Vashishta potential, 2 fs timestep, and Nosé-Hoover thermostat with a damping time of 1 ps. Simulate for at least 1 microsecond, storing atomic trajectories.
- Evidence: `/app/outputs/sphere_trajectory.nc`

### Step 3: Compute equilibrium shape distances and surface energy ratio
- Role: scored (load-bearing)
- Action: From the final 100 ns of the trajectory, identify (110) and (111) facets, compute the average distance from the nanoparticle center to each facet plane, and calculate the ratio E_{110}/E_{111} = d_{110}/d_{111}.
- Output file: `/app/outputs/equilibrium_shape.json`
- Format: json
- Contract: {"d_110": float, "d_111": float, "ratio_E110_E111": float}
- Scoring: scored by hidden verifier

### Step 4: Compute surface diffusion coefficients
- Role: scored (load-bearing)
- Action: From the first 100 ps of the trajectory, select atoms in the top three surface layers. Compute the mean squared displacement of Si and C atoms over this interval and fit to obtain diffusion coefficients D_Si and D_C in cm2/s.
- Output file: `/app/outputs/diffusion_coefficients.json`
- Format: json
- Contract: {"D_Si": float, "D_C": float, "temperature": 2200.0, "timestep_range": "0-100 ps"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_shape.json`
- `/app/outputs/diffusion_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_shape.json
- path: `/app/outputs/equilibrium_shape.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium shape distances of the faceted nanoparticle (mean distance from center to (110) and (111) planes) and the derived surface energy ratio.
- schema:
  - `type`: object
  - `required`:
    - `d_110`: float (nm)
    - `d_111`: float (nm)
    - `ratio_E110_E111`: float (unitless)

### diffusion_coefficients.json
- path: `/app/outputs/diffusion_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Surface diffusion coefficients of Si and C atoms in the top three surface layers during early facet formation (0-100 ps).
- schema:
  - `type`: object
  - `required`:
    - `D_Si`: float (cm2/s)
    - `D_C`: float (cm2/s)
    - `temperature`: float (K)
    - `timestep_range`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_shape.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "d_110": "float (nm)",
          "d_111": "float (nm)",
          "ratio_E110_E111": "float (unitless)"
        }
      },
      "description": "Equilibrium shape distances of the faceted nanoparticle (mean distance from center to (110) and (111) planes) and the derived surface energy ratio."
    },
    {
      "file": "diffusion_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "D_Si": "float (cm2/s)",
          "D_C": "float (cm2/s)",
          "temperature": "float (K)",
          "timestep_range": "string"
        }
      },
      "description": "Surface diffusion coefficients of Si and C atoms in the top three surface layers during early facet formation (0-100 ps)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your equilibrium_shape.json and diffusion_coefficients.json, compares the reported values for d_110, d_111, ratio_E110_E111, D_Si and D_C against independently obtained reference values, and assigns a per-artifact score. The final reward is a weighted sum of these scores. The schemas must be followed; artifacts with missing fields or wrong types will be penalised. No other outputs are scored.
