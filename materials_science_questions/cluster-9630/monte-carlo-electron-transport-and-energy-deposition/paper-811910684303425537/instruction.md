# Monte Carlo simulation of secondary electron generation and transport in diamond

## Problem background
A novel photoinjector design based on a diamond amplifier aims to generate high-brightness electron beams by converting a small primary electron population into a much larger secondary electron cascade. Understanding the dynamics of secondary electron generation and transport inside diamond is critical for optimizing this device. The present task implements a detailed Monte Carlo model of electron scattering in diamond to simulate the cascade and predict the number of secondary electrons as a function of time and primary energy.

## Approach
The simulation uses a Monte Carlo algorithm extended with the null collision method. Free electrons travel between scattering events with energy-dependent mean free times derived from total elastic and inelastic cross sections (Ziaja et al., 2005). Two elastic scattering models are employed: isotropic scattering and the Conwell-Weisskopf anisotropic approach. Inelastic scattering is handled through the Ashley approximation, which uses the energy-loss function (ELF) of diamond (Ziaja et al., 2001). At each inelastic event, the energy loss ω and momentum transfer q are sampled from the doubly differential cross section via von Neumann rejection. Electron-hole pair creation is modeled considering the diamond band structure at T = 0 K, and holes also generate secondaries. Two limiting cases are considered: one forbidding energy transfer to the lattice for energy losses below the band gap, and one allowing such loss. For each condition, a single primary electron is injected and its trajectory tracked until 2000 fs.

## Reproduction target
Implement the Monte Carlo simulation as described. Simulate a single primary electron at four initial kinetic energies above the conduction band minimum: E' = 250, 500, 750, 1000 eV. For each energy, run two limiting cases (with and without lattice energy loss for ω < Eg). For each of the eight conditions, launch 200 independent trajectories, each starting with one primary electron and evolving for 2000 fs. Record the number of secondary electrons present at 10 fs intervals. From the raw trajectory data, compute the ensemble-averaged time evolution (mean number of secondaries vs. time) and the maximum of this average for each condition. Output these aggregated results in simulation_results.json.

## Assets

- Ziaja et al. (2005) J. Appl. Phys. 97, 064905 - elastic and inelastic total cross sections: 10.1063/1.1857051
- Ziaja et al. (2001) Phys. Rev. B 64, 214104 - energy-loss function (ELF) for diamond: 10.1103/PhysRevB.64.214104

## Workflow steps

### Step 1: Extract cross sections and compute mean free times
- Role: process
- Action: Obtain the total elastic and inelastic scattering cross sections from Ziaja et al. (2005) and the energy-loss function (ELF) for diamond from Ziaja et al. (2001). Implement routines to compute the energy-dependent elastic mean free time τ_el(E) and inelastic mean free time τ_in(E) from these cross sections.
- Evidence: `/app/outputs/cross_sections_mfp.json`

### Step 2: Run Monte Carlo simulations for all conditions
- Role: process
- Action: Implement the Monte Carlo algorithm with null collision method, elastic scattering (isotropic and Conwell-Weisskopf), inelastic scattering (Ashley approximation using the ELF, von Neumann rejection), and electron-hole pair creation (diamond band structure, T=0 K). For each primary electron kinetic energy E′ = 250, 500, 750, 1000 eV above Ec, and for two limiting cases (with and without lattice energy loss for ω < Eg), run 200 trajectories each. Start each trajectory with a single primary electron and evolve until 2000 fs. Record the number of secondary electrons at intervals of 10 fs. Write all raw trajectory data to raw_traces.csv.
- Evidence: `/app/outputs/raw_traces.csv`

### Step 3: Aggregate time evolution and maximum secondary counts
- Role: scored (load-bearing)
- Action: From raw_traces.csv, compute the average number of secondary electrons at each recorded time step for each condition. Determine the maximum of the average time series for each condition. Write the results to simulation_results.json.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: {"time_evolution": [{"energy_eV": float, "limiting_case": string, "time_fs": float, "mean_num_secondaries": float} ...], "max_secondaries": [{"energy_eV": float, "limiting_case": string, "max_num": float} ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the time evolution of the average number of secondary electrons and the maximum average number for each primary energy and limiting case, derived from the Monte Carlo simulation.
- schema:
  - `type`: object
  - `required`:
    - `time_evolution`: array of objects with fields: energy_eV (float), limiting_case (string), time_fs (float), mean_num_secondaries (float)
    - `max_secondaries`: array of objects with fields: energy_eV (float), limiting_case (string), max_num (float)
  - `items`:
    - `time_evolution_entry`:
      - `energy_eV`: float
      - `limiting_case`: string
      - `time_fs`: float
      - `mean_num_secondaries`: float
    - `max_secondaries_entry`:
      - `energy_eV`: float
      - `limiting_case`: string
      - `max_num`: float

Notes: The time_evolution array should have entries for every recorded time step (0 to 2000 fs in 10 fs increments) for all 8 conditions. max_secondaries should have one entry per condition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "time_evolution": "array of objects with fields: energy_eV (float), limiting_case (string), time_fs (float), mean_num_secondaries (float)",
          "max_secondaries": "array of objects with fields: energy_eV (float), limiting_case (string), max_num (float)"
        },
        "items": {
          "time_evolution_entry": {
            "energy_eV": "float",
            "limiting_case": "string",
            "time_fs": "float",
            "mean_num_secondaries": "float"
          },
          "max_secondaries_entry": {
            "energy_eV": "float",
            "limiting_case": "string",
            "max_num": "float"
          }
        }
      },
      "description": "Contains the time evolution of the average number of secondary electrons and the maximum average number for each primary energy and limiting case, derived from the Monte Carlo simulation."
    }
  ],
  "notes": "The time_evolution array should have entries for every recorded time step (0 to 2000 fs in 10 fs increments) for all 8 conditions. max_secondaries should have one entry per condition."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads simulation_results.json. The verifier checks the mean number of secondary electrons at selected time snapshots and the maximum average count for each condition against reference values derived from the original study. It also verifies structural relationships: the maximum average number should increase with primary energy, and for each energy the count in the 'no loss to lattice' case should be at least as high as the 'with loss' case. Scoring is monotonic: meeting or exceeding the expected threshold earns full credit; results that fall short receive proportionally lower scores. No single hardcoded number is required — only faithful re‑implementation of the physical model is expected.
