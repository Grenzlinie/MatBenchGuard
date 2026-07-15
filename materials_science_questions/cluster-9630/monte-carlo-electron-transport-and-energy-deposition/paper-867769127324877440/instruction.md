# Monte Carlo simulation of electron energy deposition in GaN p-i-n betavoltaic layers

## Problem background
Gallium nitride (GaN) p‑i‑n junctions grown on silicon are candidates for betavoltaic energy harvesters powered by the radioisotope ⁶³Ni. The nuclear decay emits beta electrons, and the semiconductor junction converts the deposited energy into electrical power. For efficient device operation it is crucial to know how deeply the beta electrons penetrate and where they deposit their energy within the layered semiconductor stack. Monte Carlo electron‑transport simulations can model this process, providing depth‑resolved energy deposition profiles that guide the choice of layer thicknesses to maximise charge collection in the depletion region. This task asks you to compute such profiles for a specific GaN p‑i‑n stack under two different electron source conditions.

## Approach
Use a Monte Carlo electron‑transport code (such as CASINO or an equivalent open‑source platform) to simulate a vertical GaN stack consisting of p‑GaN (80 nm), i‑GaN (600 nm), and n‑GaN (80 nm) on a silicon substrate. Define the GaN material with standard physical properties (density ~6.15 g/cm³, atomic composition Ga and N).

Run two separate simulations:
1. An **isotropic source** emitting the full ⁶³Ni beta emission spectrum (energies from 0 keV up to 66.7 keV, with the known spectral shape).
2. A **monoenergetic 17.4 keV electron beam** normally incident on the top surface (p‑GaN).

For each simulation, track at least 50 000 primary electrons and record the depth‑resolved average energy deposited per incident primary electron (eV per electron). Output the results as CSV files with columns `depth_nm` (positive into the material) and `energy_deposition_eV_per_electron`. The two depth‑energy curves will capture how the different angular and energy distributions affect the energy deposition profile.

## Reproduction target
Produce two CSV files containing the depth‑dependent average energy deposition per incident primary electron for the specified GaN p‑i‑n stack under the two electron source conditions. The data must span 0–800 nm with at least 100 equally spaced depth points, and the simulation must use at least 50 000 primary electrons per source. The resulting depth‑energy curves allow a quantitative comparison of how the beam and the isotropic spectrum source differ in penetration and energy deposition. The curves must be physically plausible: the monoenergetic beam is expected to deposit energy closer to the surface than the isotropic spectrum source.

## Assets

- CASINO Monte Carlo simulation software: https://www.gel.usherbrooke.ca/casino/
- Ni-63 beta emission spectrum: https://www.nndc.bnl.gov/nudat2/
- Gallium nitride material properties

## Workflow steps

### Step 1: Simulate energy deposition for 63Ni beta spectrum
- Role: scored (load-bearing)
- Action: Set up and run a Monte Carlo electron transport simulation of a GaN stack consisting of p-GaN (80 nm), i-GaN (600 nm), and n-GaN (80 nm) on a silicon substrate. Use the full 63Ni beta emission spectrum as an isotropic electron source. Run at least 50,000 primary particles. Record the depth-resolved average energy deposited per incident primary electron.
- Output file: `/app/outputs/energy_deposition_Ni63_spectrum.csv`
- Format: csv
- Contract: Columns: depth_nm (float, nanometres from the surface into the material, positive), energy_deposition_eV_per_electron (float, eV deposited per incident primary electron). At least 100 equally spaced depth points covering 0–800 nm.
- Scoring: scored by hidden verifier

### Step 2: Simulate energy deposition for 17.4 keV electron beam
- Role: scored (load-bearing)
- Action: Set up a second Monte Carlo simulation for the same GaN stack, but this time with a monoenergetic 17.4 keV electron beam normally incident on the top surface (p-GaN). Run at least 50,000 primary electrons. Output the depth-resolved energy deposition as for the spectrum case.
- Output file: `/app/outputs/energy_deposition_17keV_beam.csv`
- Format: csv
- Contract: Same as step 1: depth_nm (float), energy_deposition_eV_per_electron (float), at least 100 equally spaced depth points spanning 0–800 nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_deposition_Ni63_spectrum.csv`
- `/app/outputs/energy_deposition_17keV_beam.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_deposition_Ni63_spectrum.csv
- path: `/app/outputs/energy_deposition_Ni63_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Energy deposition versus depth for isotropic 63Ni beta source. The checker will recompute a comparison metric (e.g., depth-dependent energy deposition or cumulative fraction) against a hidden digitized reference curve.
- schema:
  - `type`: table
  - `required_columns`: `depth_nm`, `energy_deposition_eV_per_electron`
  - `units`:
    - `depth_nm`: nm
    - `energy_deposition_eV_per_electron`: eV per electron

### energy_deposition_17keV_beam.csv
- path: `/app/outputs/energy_deposition_17keV_beam.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Energy deposition versus depth for 17.4 keV monoenergetic electron beam. The checker will recompute a comparison metric against a hidden digitized reference curve and verify that the beam curve peaks at a shallower depth than the spectrum curve.
- schema:
  - `type`: table
  - `required_columns`: `depth_nm`, `energy_deposition_eV_per_electron`
  - `units`:
    - `depth_nm`: nm
    - `energy_deposition_eV_per_electron`: eV per electron

Notes: The two CSV files provide the depth-resolved energy deposition profiles. The checker will independently recompute quantities such as cumulative energy fraction and compare depth profiles to digitized reference data from the source paper, using relative tolerances appropriate for Monte Carlo re-runs with different code implementations. No gold values or tolerances are revealed to the solving agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_deposition_Ni63_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "depth_nm",
          "energy_deposition_eV_per_electron"
        ],
        "units": {
          "depth_nm": "nm",
          "energy_deposition_eV_per_electron": "eV per electron"
        }
      },
      "description": "Energy deposition versus depth for isotropic 63Ni beta source. The checker will recompute a comparison metric (e.g., depth-dependent energy deposition or cumulative fraction) against a hidden digitized reference curve."
    },
    {
      "file": "energy_deposition_17keV_beam.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "depth_nm",
          "energy_deposition_eV_per_electron"
        ],
        "units": {
          "depth_nm": "nm",
          "energy_deposition_eV_per_electron": "eV per electron"
        }
      },
      "description": "Energy deposition versus depth for 17.4 keV monoenergetic electron beam. The checker will recompute a comparison metric against a hidden digitized reference curve and verify that the beam curve peaks at a shallower depth than the spectrum curve."
    }
  ],
  "notes": "The two CSV files provide the depth-resolved energy deposition profiles. The checker will independently recompute quantities such as cumulative energy fraction and compare depth profiles to digitized reference data from the source paper, using relative tolerances appropriate for Monte Carlo re-runs with different code implementations. No gold values or tolerances are revealed to the solving agent."
}
```

## How you are scored
A hidden verifier reads your two CSV files and independently recomputes depth‑dependent quantities (e.g., cumulative energy fraction). It compares your depth‑energy profiles against hidden reference data using relative tolerances that account for the expected run‑to‑run spread of Monte Carlo simulations. Additionally, the verifier checks a structural trend: the 17.4 keV beam profile should peak at a shallower depth than the spectrum source profile. Each scored artifact receives a weight, and your final reward is the weighted sum of the stage scores. Simply reporting a number from the literature is not sufficient; the verifier evaluates the actual computed energy deposition curves.
