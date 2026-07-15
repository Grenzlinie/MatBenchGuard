# Monte Carlo Simulation of Electron Transport and Breakdown Field in Dielectrics

## Problem background
Irradiation of dielectrics creates an internal electric field that pulls electrons toward the surface. At high field strengths, electron multiplication via impact ionization and cascading can cause electrical breakdown. This task implements a refined Monte Carlo model for electron transport in crystalline SiO2 that includes phonon scattering, impact ionization, and cascading, and uses it to compute the breakdown electric field range.

## Approach
The method consists of two conceptual stages. First, compute the energy-dependent scattering rates (and corresponding mean free paths) for the relevant physical processes: longitudinal optical phonons (Frohlich theory), acoustic phonons (low- and high-energy regimes), and impact ionization. Use the provided material parameters for crystalline SiO2. Second, run a Monte Carlo simulation of electron trajectories starting from a given electron localization depth (e.g., 100 nm). For each electric field strength in a range spanning 1–15 MV/cm, simulate many independent electron histories. Each history includes propagation, energy updates due to field acceleration and phonon interactions, impact ionization events, a cascading probability factor, and surface emission when the electron’s energy exceeds the electron affinity. Record all emitted electrons. From the simulation logs, construct a curve of emitted electron count as a function of field strength. Finally, analyze this curve to identify the field range where an avalanche-like sharp increase in emitted electrons occurs, which indicates dielectric breakdown.

## Reproduction target
Your goal is to produce two scored artifacts stored in /app/outputs:
1. `emitted_electrons_vs_field.csv`: a CSV with two columns—`electric_field_strength` (MV/cm, float) and `emitted_electron_count` (unitless float)—for field strengths from 1 to 15 MV/cm.
2. `breakdown_range.json`: a JSON file containing the breakdown field range as a list of two floats: `{"breakdown_range_MV_per_cm": [lower_bound, upper_bound]}`. The breakdown range is defined as the electric field interval where the emitted electron count exhibits a sharp, sustained rise (avalanche), not a gradual increase.
You must implement the full Monte Carlo simulation that generates these artifacts; simply guessing or fabricating the numbers will not survive the scoring checks.

## Assets
The simulation requires the following publicly reported material constants for crystalline SiO2 (no external dataset download is needed):
- Longitudinal optical phonon energy: ħω_LO = 0.063 eV
- Static permittivity: ε = 3.84
- High-frequency permittivity: ε_∞ = 2.25
- Deformation potential constant: C1 = 3.5 eV
- Cross section for acoustic phonon scattering at high energies: σ = 3.5e-15 cm²
- Mass density: ρ = 2.65 g/cm³
- Speed of sound: Cs = 4030 m/s
- Impact ionization coefficient: Cii = 1.26e15 1/s
- Impact screening parameter: Dii = 0.01
- Exponent constant: α = 0.45
- Mass of heaviest atom in unit cell: M = 46.6e-27 kg
- Temperature: T = 300 K
- Electron affinity: χ = 0.3 eV
- Effective masses and other microscopic parameters as appropriate from standard literature.

## Workflow steps

### Step 1: Compute electron scattering rates and mean free paths
- Role: process
- Action: Using the material parameters for crystalline SiO2 (ħω_LO, ε, ε_∞, C1, σ, ρ, Cs, M, T, Cii, Dii, α, m*, etc.), compute the energy-dependent scattering rates for longitudinal optical phonons (Fröhlich theory), acoustic phonons (low-energy and high-energy regimes), and impact ionization, as well as the mean free path as a function of energy. Tabulate these for use in the Monte Carlo simulation.
- Evidence: `/app/outputs/rates_and_mfp.csv`

### Step 2: Run Monte Carlo simulation of electron transport
- Role: process
- Action: For electric field strengths from 1 to 15 MV/cm (with sufficient resolution to capture the breakdown onset), simulate 10,000 electron trajectories starting from a localization depth of 100 nm. Use the previously computed scattering rates, the energy update rule, the cascading probability factor, and the surface emission condition. Record all emission events (electron count, energies, angles).
- Evidence: `/app/outputs/simulation_event_log.txt`

### Step 3: Produce emitted electron count vs. field strength curve
- Role: scored
- Action: From the recorded emission events, compute the number (or fraction) of emitted electrons for each field strength and save as a CSV.
- Output file: `/app/outputs/emitted_electrons_vs_field.csv`
- Format: csv
- Contract: Two columns: electric_field_strength (MV/cm, float), emitted_electron_count (float, unitless)
- Scoring: scored by hidden verifier

### Step 4: Determine breakdown electric field range
- Role: scored (load-bearing)
- Action: Analyze the emission vs field curve to identify the electric field range where an avalanche increase (breakdown) occurs. The range should correspond to a sharp, sustained rise in emitted electron count, not just a gradual increase. Report the lower and upper bounds in a JSON file.
- Output file: `/app/outputs/breakdown_range.json`
- Format: json
- Contract: {"breakdown_range_MV_per_cm": [lower_bound, upper_bound]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/emitted_electrons_vs_field.csv`
- `/app/outputs/breakdown_range.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### emitted_electrons_vs_field.csv
- path: `/app/outputs/emitted_electrons_vs_field.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The emission curve data, verified for structural features (plateau region below 10 MV/cm and a sharp increase around 11-13 MV/cm).
- schema:
  - `type`: table
  - `required_columns`: `electric_field_strength`, `emitted_electron_count`
  - `units`:
    - `electric_field_strength`: MV/cm
    - `emitted_electron_count`: unitless

### breakdown_range.json
- path: `/app/outputs/breakdown_range.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The extracted breakdown electric field range in MV/cm. Checked against the paper's reported range with a tolerance on each bound.
- schema:
  - `type`: object
  - `required`:
    - `breakdown_range_MV_per_cm`: list of two floats

Notes: The emission curve provides a structural audit; the breakdown range is the primary headline result and is load-bearing.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "emitted_electrons_vs_field.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_strength",
          "emitted_electron_count"
        ],
        "units": {
          "electric_field_strength": "MV/cm",
          "emitted_electron_count": "unitless"
        }
      },
      "description": "The emission curve data, verified for structural features (plateau region below 10 MV/cm and a sharp increase around 11-13 MV/cm)."
    },
    {
      "file": "breakdown_range.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "breakdown_range_MV_per_cm": "list of two floats"
        }
      },
      "description": "The extracted breakdown electric field range in MV/cm. Checked against the paper's reported range with a tolerance on each bound."
    }
  ],
  "notes": "The emission curve provides a structural audit; the breakdown range is the primary headline result and is load-bearing."
}
```

## How you are scored
A hidden verifier independently scores each output file and combines them by weight into a final reward in [0,1]. The file `emitted_electrons_vs_field.csv` is audited for structural features: a plateau at low fields (below ~10 MV/cm) and a sharp rise at higher fields, consistent with an avalanche. The `breakdown_range.json` is compared against a hidden reference range with appropriate tolerances. The final score reflects whether your artifacts are physically plausible and match the expected breakdown behavior; reporting numbers without running the simulation will not pass these checks. You do not need to know the reference values: simply implement the described model faithfully, and the verifier will determine the score.
