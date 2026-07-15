# Calculate carbon adatom lifetime and migration distance on a charged single-walled carbon nanotube

## Problem background
Carbon adatom surface diffusion on single‑walled carbon nanotubes (SWCNTs) is an important process for nanotube growth in plasma environments, where the tubes can become negatively charged. The effect of such charging on adatom migration—adsorption stability, hopping barriers, and ultimately adatom lifetime and migration distance—is not well established. This task investigates how varying the negative charge on a finite‑length armchair (5,5) SWCNT influences the surface diffusion and desorption of a carbon adatom at high temperature.

## Approach
The approach combines first‑principles electronic structure calculations with kinetic Monte Carlo (KMC) simulation. First, an atomic model of a hydrogen‑terminated (5,5) SWCNT (180 C atoms + 10 H atoms, ≈1.98 nm long) is built, and a single carbon adatom is placed at the three bridge adsorption sites (labelled 1, 2, 3). All‑electron density functional theory (DFT) with the PBE0 hybrid functional and the 6‑31G* basis set is used to optimise geometries and compute energies for the pristine tube and for the tube with the adatom at each site, at total charges q = 0, ‑2e, ‑4e, …, ‑12e. The adsorption energy at each site is obtained as E_a = E(CNT+C) − E(CNT) − E(C). Nudged elastic band (NEB) calculations yield the minimum‑energy paths and barriers for adatom hopping between adjacent sites. Normal‑mode vibrational frequencies of the adatom at each site are computed via a numerical Hessian. These adsorption energies, barriers, and frequencies are then used in Arrhenius‑type formulas (k = ν exp(−ΔE/k_B T)) to derive temperature‑dependent transition rates for hopping and desorption at T = 1700 K. Finally, a KMC simulation is performed on an infinite (5,5) tube using these rates: starting from site 2, 400,000 independent trajectories are run (up to 10^10 steps each) for every charge state, recording the time until desorption and the net migration distance along the tube axis. The averaged lifetime and migration distance are the quantities to be reported.

## Reproduction target
Compute the average adatom lifetime (in seconds) and average migration distance along the tube axis (in metres) for an armchair (5,5) SWCNT carrying negative charges q = 0, ‑2e, ‑4e, ‑6e, ‑8e, ‑10e, ‑12e at T = 1700 K, starting the adatom from site 2. The results must be derived from the DFT‑based adsorption energies, migration barriers, vibrational frequencies, and the subsequent KMC simulation described above. Output these seven charge‑condition averages as a JSON file `/app/outputs/results.json` containing an array of objects, each with the keys `charge_e` (integer), `lifetime_s` (float, seconds), and `migration_distance_m` (float, metres).

## Assets

- NWChem: https://nwchemgit.github.io/
- Python3: python3

## Workflow steps

### Step 1: Construct atomic models
- Role: process
- Action: Build the atomic model of a finite, hydrogen-terminated (5,5) SWCNT (180 C atoms + 10 H atoms, length ~1.98 nm). Place a single carbon adatom at the three bridge adsorption sites (site 1, 2, 3) as described in the paper. Generate initial Cartesian coordinates for all subsequent DFT calculations.
- Evidence: `/app/outputs/model_coordinates.log`

### Step 2: DFT adsorption energy calculations
- Role: process
- Action: Using NWChem with PBE0/6-31G* basis set, perform geometry optimizations for: (i) pristine (5,5) SWCNT at charges q = 0, -2e, -4e, -6e, -8e, -10e, -12e; (ii) SWCNT + adatom at each of the three sites for each charge state. Compute the total energy of a spin-polarized isolated carbon atom (triplet). For each site and charge, calculate the adsorption energy via E_a^q = E(CNT+C)^q - E(CNT)^q - E(C). Output a table of adsorption energies.
- Evidence: `/app/outputs/adsorption_energies.csv`

### Step 3: NEB migration barrier calculations
- Role: process
- Action: For each charge state, perform nudged elastic band (NEB) calculations between pairs of adjacent adsorption sites to determine the minimum energy path and energy barriers. Use NWChem with PBE0/6-31G*. Extract the energy barrier heights (difference between transition state and equilibrium energy). Output a table of barriers.
- Evidence: `/app/outputs/migration_barriers.csv`

### Step 4: Vibrational frequency calculations
- Role: process
- Action: For each charge and adsorption site, compute normal-mode vibrational frequencies of the adatom via numerical Hessian in NWChem. Identify the three vibrational modes (radial, axial, circumferential). Output the frequencies.
- Evidence: `/app/outputs/vibrational_frequencies.csv`

### Step 5: Transition rate calculation
- Role: process
- Action: Using the computed adsorption energies, migration barriers, and vibrational frequencies, calculate the hopping rates (k_{s->f}) and desorption rates (k_d^s) at T=1700 K via Arrhenius-type formulas: k_{s->f} = ν_s exp(-E_{s->f}/k_B T), k_d^s = ν_s exp(-E_a^s/k_B T). Project the normal-mode frequencies onto the reaction coordinate to obtain the prefactor ν_s. Output a table of all transition rates.
- Evidence: `/app/outputs/transition_rates.csv`

### Step 6: KMC simulation and lifetime/migration distance calculation
- Role: scored (load-bearing)
- Action: Implement a kinetic Monte Carlo simulation of adatom diffusion and desorption on an infinite (5,5) SWCNT using the transition rates from step_05. The adatom is initially adsorbed at site 2. Run 400,000 independent trajectories (each up to 1e10 steps) for each charge state (0, -2e, -4e, -6e, -8e, -10e, -12e), tracking the adatom’s axial position. Compute the average lifetime before desorption (in seconds) and the average migration distance along the tube axis (in meters). Output these values for all charges in a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of objects, each with keys: 'charge_e' (integer, negative multiples of 2 from 0 to -12), 'lifetime_s' (float, seconds), 'migration_distance_m' (float, meters). Must cover all charges 0, -2, -4, -6, -8, -10, -12.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported adatom lifetime and migration distance for each charge state. Checker will compare to hidden reference values for selected charges and verify monotonic increase.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `charge_e`, `lifetime_s`, `migration_distance_m`
    - `properties`:
      - `charge_e`:
        - `type`: integer
      - `lifetime_s`:
        - `type`: number
      - `migration_distance_m`:
        - `type`: number

Notes: The DFT and NEB steps are computationally intensive and expected to run on external/HPC resources. The KMC simulation must cover all seven charge states with 400k trajectories each. The checker applies tolerance-based comparison to paper-reported values (factor 2) and checks monotonic trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "charge_e",
            "lifetime_s",
            "migration_distance_m"
          ],
          "properties": {
            "charge_e": {
              "type": "integer"
            },
            "lifetime_s": {
              "type": "number"
            },
            "migration_distance_m": {
              "type": "number"
            }
          }
        }
      },
      "description": "Agent-reported adatom lifetime and migration distance for each charge state. Checker will compare to hidden reference values for selected charges and verify monotonic increase."
    }
  ],
  "notes": "The DFT and NEB steps are computationally intensive and expected to run on external/HPC resources. The KMC simulation must cover all seven charge states with 400k trajectories each. The checker applies tolerance-based comparison to paper-reported values (factor 2) and checks monotonic trend."
}
```

## How you are scored
A hidden verifier will inspect your submitted artifacts—primarily the final `/app/outputs/results.json`. It will compare your reported adatom lifetime and migration distance at each charge to hidden reference values obtained from the underlying physical model, and will check that the numbers exhibit the qualitative behaviour that must follow from the computed energetics. To succeed, you must genuinely execute the DFT and KMC pipeline; simply guessing or hardcoding values will not match the hidden criteria. The verifier computes a composite reward that reflects the accuracy of your results across the different charge states.
