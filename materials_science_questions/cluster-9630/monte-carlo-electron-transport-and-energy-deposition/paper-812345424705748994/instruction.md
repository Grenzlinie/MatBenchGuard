# Monte Carlo secondary emission model for insulating spherical grains

## Problem background
Secondary electron emission from insulating dust grains plays a critical role in the charging of dust in space and laboratory plasmas. Unlike large planar metal surfaces, small, highly curved insulating grains can charge to non-negligible potentials under electron bombardment, and their secondary emission behaviour deviates from classical universal curves. The work addresses this problem by developing a Monte Carlo model of primary electron transport inside a spherical grain. The model computes the true secondary emission yield, the fraction of reflected primaries, and the net charge accumulated on the grain, which is then converted into an electrostatic surface potential. Comparing the model with experimental measurements for micron‑sized spheres allows understanding the mechanisms that determine the grain potential as a function of primary electron energy and grain size.

## Approach
The model follows the physical assumptions of Sternglass: a primary electron penetrates the grain and loses a fixed energy ΔE at each inelastic collision, exciting one secondary electron. The distance between collisions is taken as λ = λ₀ · (E/ΔE), where E is the current primary energy and λ₀ the elementary mean‑free path. After each collision the primary direction is randomly scattered, with a cosine‑weighted probability distribution. The probability that an excited secondary electron reaches the surface from depth x is P(x) = A exp(−α x), where α is the absorption constant and A is normalized such that the total escape probability at a planar surface is 1/2. For each (grain material, grain diameter, primary beam energy) condition, a large number of primary electrons are launched from the surface, and their trajectories are followed until leaving the grain or exhausting their energy. The simulation accumulates the sum of individual secondary escape probabilities S, the total number of primaries launched Nprim, and the number of primaries that backscatter out of the grain Pesc. From these, the secondary electron yield is δ = S/Nprim and the primary reflection coefficient is η = Pesc/Nprim. The net charge on the grain is Q_net = e·Nprim·(1 − η − δ), where e is the elementary charge. The grain capacitance is modelled as that of an isolated sphere C = 4πε₀ r, with r the grain radius, giving a raw potential φ_r = Q_net / C. Following the convention used in the literature, negative potentials are set to zero.

## Reproduction target
Implement the Monte Carlo simulation described above and compute the secondary electron yield and grain surface potential for three grain sizes: melamine formaldehyde resin spheres of diameter 2.35 μm and 9.78 μm, and a SiO₂ sphere of diameter 1.2 μm. For each size, run the simulation at four primary beam energies: 1 keV, 2 keV, 5 keV, and 10 keV, using the material parameters given in the workflow steps. Output the yield in a CSV file `secondary_yield.csv` and the potential (with negative potentials zeroed) in `grain_potential.csv`. The files must contain one row per (material, diameter, beam energy) combination, with the exact column schema described in the output contract. No other quantities need to be reported.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Monte Carlo simulation of primary electron transport
- Role: process
- Action: Implement and run a Monte Carlo simulation of primary electron trajectories inside a spherical grain for each specified grain diameter (2.35 μm and 9.78 μm for melamine formaldehyde; 1.2 μm for SiO2) and primary beam energy (1, 2, 5, 10 keV). Use the given material parameters: for MF resin ΔE=37 eV, λ0=0.21 nm, α=0.03, T_SE=3 eV; for SiO2 ΔE=34 eV, λ0=0.12 nm, α=0.016, T_SE=2.2 eV. Follow the model assumptions: fixed energy loss ΔE per collision, path length λ = λ0·(E/ΔE), cosine-weighted scattering, exponential secondary escape probability P(x)=A·exp(-αx) with A normalized to 1/2 at a planar surface. For each condition, launch N_prim = 1e5 primary electrons from the grain surface and simulate until exit or energy exhaustion. Accumulate total sum of escape probabilities S, the number of launched primaries N_prim, and the number of escaping primaries P_esc. Store results as a JSON list of per-condition dictionaries with keys: grain_material (str), grain_diameter_um (float), beam_energy_eV (float), N_prim (int), S (float), P_esc (int). Write the JSON to `simulation_events.json`.
- Evidence: `/app/outputs/simulation_events.json`

### Step 2: Compute secondary electron yield
- Role: scored
- Action: From the simulation_events.json tally data, for each condition compute the secondary electron yield δ = S / N_prim. Write the results to a CSV file `secondary_yield.csv` with one row per condition and columns: grain_material, grain_diameter_um, beam_energy_eV, secondary_yield.
- Output file: `/app/outputs/secondary_yield.csv`
- Format: csv
- Contract: Columns: grain_material (string), grain_diameter_um (float), beam_energy_eV (float), secondary_yield (float).
- Scoring: scored by hidden verifier

### Step 3: Compute grain surface potential
- Role: scored
- Action: From the simulation_events.json and the secondary yield, for each condition compute the net charge Q_net = e * N_prim * (1 - η - δ) where η = P_esc / N_prim, e = 1.602e-19 C. Compute grain capacitance C = 4πε0 r with ε0 = 8.854e-12 F/m and grain radius r = (grain_diameter_um/2)*1e-6 m. Compute raw potential φ_r = Q_net / C. Set φ = max(0, φ_r) following the paper's convention. Write the results to `grain_potential.csv` with columns: grain_material, grain_diameter_um, beam_energy_eV, potential_V.
- Output file: `/app/outputs/grain_potential.csv`
- Format: csv
- Contract: Columns: grain_material (string), grain_diameter_um (float), beam_energy_eV (float), potential_V (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/secondary_yield.csv`
- `/app/outputs/grain_potential.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### secondary_yield.csv
- path: `/app/outputs/secondary_yield.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Secondary electron emission yield for each grain material, diameter, and primary beam energy.
- schema:
  - `type`: table
  - `required_columns`: `grain_material`, `grain_diameter_um`, `beam_energy_eV`, `secondary_yield`
  - `units`:
    - `grain_diameter_um`: micrometers
    - `beam_energy_eV`: electronvolts
    - `secondary_yield`: dimensionless

### grain_potential.csv
- path: `/app/outputs/grain_potential.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electrostatic surface potential of the grain for each material, diameter, and primary beam energy, following the paper's convention of setting negative potentials to zero.
- schema:
  - `type`: table
  - `required_columns`: `grain_material`, `grain_diameter_um`, `beam_energy_eV`, `potential_V`
  - `units`:
    - `grain_diameter_um`: micrometers
    - `beam_energy_eV`: electronvolts
    - `potential_V`: volts

Notes: The checker compares the agent's computed values to hidden gold values extracted from the paper's model outputs at the specified (grain size, beam energy) conditions, with tolerances that account for Monte Carlo noise. The simulation must be run with the given parameters and N_prim = 1e5; no parameter fitting is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "secondary_yield.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "grain_material",
          "grain_diameter_um",
          "beam_energy_eV",
          "secondary_yield"
        ],
        "units": {
          "grain_diameter_um": "micrometers",
          "beam_energy_eV": "electronvolts",
          "secondary_yield": "dimensionless"
        }
      },
      "description": "Secondary electron emission yield for each grain material, diameter, and primary beam energy."
    },
    {
      "file": "grain_potential.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "grain_material",
          "grain_diameter_um",
          "beam_energy_eV",
          "potential_V"
        ],
        "units": {
          "grain_diameter_um": "micrometers",
          "beam_energy_eV": "electronvolts",
          "potential_V": "volts"
        }
      },
      "description": "Electrostatic surface potential of the grain for each material, diameter, and primary beam energy, following the paper's convention of setting negative potentials to zero."
    }
  ],
  "notes": "The checker compares the agent's computed values to hidden gold values extracted from the paper's model outputs at the specified (grain size, beam energy) conditions, with tolerances that account for Monte Carlo noise. The simulation must be run with the given parameters and N_prim = 1e5; no parameter fitting is required."
}
```

## How you are scored
After you submit your output files, a hidden verifier will read the `secondary_yield.csv` and `grain_potential.csv` files. For each of the 12 (material × diameter × beam energy) conditions, the verifier compares your computed yield and potential to hidden reference values that correspond to the model’s expected behaviour under the given parameters. The final score is based on the fraction of conditions where both yield and potential are within an acceptable agreement with the references. The evaluation is designed to be robust to the intrinsic Monte Carlo noise and small implementation differences, rewarding solutions that faithfully execute the simulation. Simply copying numbers from an external source will not match the hidden references; only a correct implementation of the model will achieve a high score.
