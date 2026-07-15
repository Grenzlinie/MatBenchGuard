# 2D Melting of Dipolar Particles: KTHNY Scenario, Specific Heat, and Defect Densities

## Problem background
Two-dimensional (2D) melting in systems of dipolar colloidal particles has been proposed to follow the Kosterlitz-Thouless-Halperin-Nelson-Young (KTHNY) scenario, featuring two continuous transitions and an intermediate hexatic phase. The specific heat of such a system is expected to reflect the unbinding of topological defects (dislocations and disclinations). The relationship between the specific heat peak, the transitions, and the defect densities remains an open subject, and Monte Carlo simulations offer a controlled way to investigate it.

## Approach
Run Monte Carlo NVT simulations of N=2500 point particles interacting via a dipolar pair potential βV(r) = Γ/r³, where Γ is the inverse temperature control parameter. The simulation box is rectangular with an aspect ratio 2:√3, an area fraction φ=0.07, and a potential cutoff at 9 times the mean interparticle distance a₀. Sweep Γ over a range that covers the solid, hexatic, and isotropic phases. For each Γ, record particle configurations and the total internal energy time series. Post-process by: (1) computing the sixfold bond-orientational order parameter ψ₆ and its spatial correlation function g₆(r) to determine the solid–hexatic (Γ_m) and hexatic–isotropic (Γ_i) transition points based on the decay behavior (constant, algebraic, or exponential); (2) calculating the specific heat per particle from energy fluctuations; (3) classifying particles by coordination to obtain the total defect fraction, the density of isolated dislocations (5‑7 pairs), and isolated disclinations (unpaired 5‑ or 7‑fold sites). The workflow is described in detail in the steps below.

## Reproduction target
Produce three output files from the simulation: transition_temperatures.json (containing the transition Γ values Γ_m and Γ_i), specific_heat.csv (a table of specific heat c_N versus Γ), and defect_density.csv (total, isolated dislocation, and isolated disclination fractions as functions of Γ). These results will be evaluated against hidden reference values and structural checks: the two-step melting scenario should be evident, the specific heat peak should be locatable, and the steepest increase in isolated dislocations should be associated with the specific heat maximum.

## Assets

- Python 3 with numpy and scipy: numpy, scipy

## Workflow steps

### Step 1: Monte Carlo simulation of 2D dipolar particles
- Role: process
- Action: Run Monte Carlo NVT simulations for N=2500 particles interacting via dipolar pair potential βV(r)=Γ/r³ in a rectangular box (aspect ratio 2:√3, area fraction φ=0.07, cutoff 9a₀) over a range of inverse temperatures Γ covering the solid to isotropic transition (e.g., 65–72). For each Γ, after equilibration, record particle configurations and total internal energy time series.
- Evidence: `/app/outputs/mc_simulation.log`

### Step 2: Determine solid–hexatic and hexatic–isotropic transition temperatures
- Role: scored
- Action: From the stored simulation configurations, compute the sixfold orientational order parameter ψ₆ and its spatial correlation function g₆(r). Classify the phase at each Γ by the decay of g₆(r) (constant→solid, algebraic→hexatic, exponential→isotropic). Determine the solid–hexatic transition Γ_m (highest Γ with solid behaviour) and the hexatic–isotropic transition Γ_i (lowest Γ with isotropic behaviour). Write the results to transition_temperatures.json.
- Output file: `/app/outputs/transition_temperatures.json`
- Format: json
- Contract: JSON object with keys: gamma_m (float, solid–hexatic transition), gamma_i (float, hexatic–isotropic transition).
- Scoring: scored by hidden verifier

### Step 3: Calculate specific heat and write c_N(Γ)
- Role: scored (load-bearing)
- Action: From the internal energy time series for each Γ, compute the specific heat per particle c_N via energy fluctuations: c_N = (⟨E²⟩−⟨E⟩²)/(N k_B T²). With the dimensionless control parameter Γ this becomes c_N/k_B = Γ²(⟨(βE)²⟩−⟨βE⟩²). Write a CSV file specific_heat.csv with columns Gamma and c_N.
- Output file: `/app/outputs/specific_heat.csv`
- Format: csv
- Contract: CSV with two columns: Gamma (float), c_N (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Calculate defect densities
- Role: scored
- Action: From the simulation configurations, identify particles that are not sixfold coordinated. Compute the total defect fraction, the fraction of isolated dislocations (neighbouring 5‑7 pairs), and the fraction of isolated disclinations (isolated 5‑ or 7‑fold sites not part of a dislocation). Use a suitable neighbour cutoff (e.g., 1.2 a₀) to define bound defects. Write a CSV file defect_density.csv with columns: Gamma, total_defect_frac, isolated_dislocation_frac, isolated_disclination_frac.
- Output file: `/app/outputs/defect_density.csv`
- Format: csv
- Contract: CSV with four columns: Gamma (float), total_defect_frac (float), isolated_dislocation_frac (float), isolated_disclination_frac (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_temperatures.json`
- `/app/outputs/specific_heat.csv`
- `/app/outputs/defect_density.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_temperatures.json
- path: `/app/outputs/transition_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Solid–hexatic and hexatic–isotropic inverse transition temperatures Γ_m and Γ_i determined from the decay of the orientational correlation function g₆(r).
- schema:
  - `type`: object
  - `required`:
    - `gamma_m`: number
    - `gamma_i`: number

### specific_heat.csv
- path: `/app/outputs/specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Specific heat per particle c_N as a function of inverse temperature Γ, computed from energy fluctuations in the MC simulations.
- schema:
  - `type`: table
  - `required_columns`: `Gamma`, `c_N`
  - `units`:
    - `Gamma`: dimensionless
    - `c_N`: dimensionless

### defect_density.csv
- path: `/app/outputs/defect_density.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Defect densities (total, isolated dislocations, isolated disclinations) as a function of Γ. The checker will verify that the steepest increase in isolated dislocations coincides with the specific heat peak.
- schema:
  - `type`: table
  - `required_columns`: `Gamma`, `total_defect_frac`, `isolated_dislocation_frac`, `isolated_disclination_frac`
  - `units`:
    - `Gamma`: dimensionless
    - `total_defect_frac`: fraction of particles
    - `isolated_dislocation_frac`: fraction of particles
    - `isolated_disclination_frac`: fraction of particles

Notes: The MC simulation must sweep a sufficient range of Γ (covering solid, hexatic, isotropic) to reliably determine the transition points and resolve the specific heat peak. The specific heat peak is expected to lie inside the hexatic phase (Γ_i < Γ_peak < Γ_m).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma_m": "number",
          "gamma_i": "number"
        }
      },
      "description": "Solid–hexatic and hexatic–isotropic inverse transition temperatures Γ_m and Γ_i determined from the decay of the orientational correlation function g₆(r)."
    },
    {
      "file": "specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Gamma",
          "c_N"
        ],
        "units": {
          "Gamma": "dimensionless",
          "c_N": "dimensionless"
        }
      },
      "description": "Specific heat per particle c_N as a function of inverse temperature Γ, computed from energy fluctuations in the MC simulations."
    },
    {
      "file": "defect_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Gamma",
          "total_defect_frac",
          "isolated_dislocation_frac",
          "isolated_disclination_frac"
        ],
        "units": {
          "Gamma": "dimensionless",
          "total_defect_frac": "fraction of particles",
          "isolated_dislocation_frac": "fraction of particles",
          "isolated_disclination_frac": "fraction of particles"
        }
      },
      "description": "Defect densities (total, isolated dislocations, isolated disclinations) as a function of Γ. The checker will verify that the steepest increase in isolated dislocations coincides with the specific heat peak."
    }
  ],
  "notes": "The MC simulation must sweep a sufficient range of Γ (covering solid, hexatic, isotropic) to reliably determine the transition points and resolve the specific heat peak. The specific heat peak is expected to lie inside the hexatic phase (Γ_i < Γ_peak < Γ_m)."
}
```

## How you are scored
A verification script will independently inspect each output file. It compares the reported transition temperatures and specific heat data to hidden reference values (derived from the paper’s own simulations) with appropriate tolerances. Structural checks will confirm that the specific heat exhibits a single peak within the hexatic regime, and that the defect density data aligns with the expected behavior (the greatest surge in isolated dislocations occurs near the specific heat maximum). The overall score is a weighted sum of these checks; higher-quality agreement yields a higher reward. Merely reporting the paper's numbers without running the simulation will not satisfy the verification because the artifacts must be self-consistent and obey the expected relationships.
