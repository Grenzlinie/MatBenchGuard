# Dielectric Screening and Graphene Transport Properties via Quantum Transport Simulations

## Problem background
Monolayer graphene's electronic transport properties are strongly influenced by the dielectric environment. Electrostatic potential fluctuations, known as electron-hole puddles, arise from charged impurities in the substrate and are screened by the surrounding media. The amplitude of these puddles depends on the average dielectric constant of the materials above and below the graphene. Understanding how different dielectric environments alter charge mobility and the Seebeck coefficient is crucial for optimizing graphene-based electronic and thermoelectric devices. This task requires a computational investigation of graphene's conductivity in the presence of a disorder potential that models electron-hole puddles, with the puddle height linked to the dielectric constant of the top medium.

## Approach
The approach is a numerical quantum transport simulation using a real-space linear-scaling method. Graphene is described by a nearest-neighbor tight-binding Hamiltonian, and the electron-hole puddle disorder is modeled as a set of randomly located Gaussian potential wells with a fixed spatial width and a height distribution that is set by the puddle strength. The energy-dependent conductivity σ(E) is obtained via the kernel polynomial method (KPM) with a Chebyshev expansion and Jackson kernel, averaging over multiple disorder realizations. Three puddle heights are considered: W = 50, 25, and 10 meV, corresponding to top dielectric constants ε_top = 1, 5.9, and 20.6 (with a bottom dielectric of ε_bot = 3.9). From σ(E), the carrier density n(E) is computed by integrating the density of states, and the mobility μ = (1/e) dσ/dn is derived. The Seebeck coefficient S(E) is calculated using the standard linear-response expression involving integrals of σ(E) weighted by the derivative of the Fermi-Dirac distribution at T = 300 K. Finally, the scaling of mobility with puddle height at a fixed carrier density is extracted to quantify the dependence μ ∝ 1/W^γ.

## Reproduction target
The objective is to produce three output files:
- mobility_vs_density.csv: Mobility (cm²/Vs) as a function of carrier density (cm⁻²) for each of the three top dielectric constants ε_top.
- seebeck_vs_EF.csv: Seebeck coefficient (μV/K) as a function of Fermi energy (eV) for each ε_top.
- scaling_summary.json: A JSON object containing the puddle heights W (meV), the mobility at a carrier density of n = 10¹² cm⁻² for each W, the maximum Seebeck coefficient for each ε_top, and the fitted scaling exponent γ from the relation μ ∝ 1/W^γ.

## Assets

- Graphene tight-binding parameters
- Kernel polynomial method implementation: kwant
- Python and scientific libraries: numpy, scipy

## Workflow steps

### Step 1: KPM simulation of conductivity
- Role: process
- Action: Implement the real-space quantum transport simulation for graphene with electron-hole puddles. For each puddle height W = 50, 25, 10 meV (corresponding to epsilon_top = 1, 5.9, 20.6), run the kernel polynomial method (KPM) with Chebyshev expansion on a system of ~8 million atoms, averaging over 10 random puddle configurations and random-phase initial states. Compute the energy-dependent conductivity sigma(E).
- Evidence: `/app/outputs/conductivity_raw.npz`

### Step 2: Derive mobility vs density
- Role: scored (load-bearing)
- Action: From the energy-dependent conductivity sigma(E), compute the carrier density n(E) by integrating the density of states. Then compute the mobility as mu = (1/e) d sigma / d n for a range of carrier densities n in [10^11, 10^13] cm^-2 for each epsilon_top. Save the results to mobility_vs_density.csv.
- Output file: `/app/outputs/mobility_vs_density.csv`
- Format: csv
- Contract: columns: density (float, cm^-2), epsilon_top (float, dimensionless), mobility (float, cm^2/Vs).
- Scoring: scored by hidden verifier

### Step 3: Derive Seebeck coefficient vs Fermi energy
- Role: scored (load-bearing)
- Action: From sigma(E), compute the Seebeck coefficient S(E) = -(1/(e T)) K1(E)/K0(E) at T=300 K, where K_j are integrals over energy using the derivative of the Fermi-Dirac distribution. Compute S for Fermi energies in the range [-0.3, 0.3] eV for each epsilon_top. Save to seebeck_vs_EF.csv.
- Output file: `/app/outputs/seebeck_vs_EF.csv`
- Format: csv
- Contract: columns: Fermi_energy (float, eV), epsilon_top (float), Seebeck (float, muV/K).
- Scoring: scored by hidden verifier

### Step 4: Compile scaling summary
- Role: scored (load-bearing)
- Action: Extract the mobility at n=10^12 cm^-2 for each W, and the maximum Seebeck value for each epsilon_top. Fit the mobility data to mu proportional to 1/W^gamma and record the exponent gamma. Write these values to scaling_summary.json.
- Output file: `/app/outputs/scaling_summary.json`
- Format: json
- Contract: object with keys: W_values [float], mobility_at_1e12 [float], max_Seebeck [float], scaling_exponent (float, nullable).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mobility_vs_density.csv`
- `/app/outputs/seebeck_vs_EF.csv`
- `/app/outputs/scaling_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mobility_vs_density.csv
- path: `/app/outputs/mobility_vs_density.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mobility as a function of carrier density for each dielectric environment.
- schema:
  - `type`: table
  - `required_columns`: `density`, `epsilon_top`, `mobility`
  - `units`:
    - `density`: cm^-2
    - `mobility`: cm^2/Vs

### seebeck_vs_EF.csv
- path: `/app/outputs/seebeck_vs_EF.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Seebeck coefficient as a function of Fermi energy for each dielectric environment.
- schema:
  - `type`: table
  - `required_columns`: `Fermi_energy`, `epsilon_top`, `Seebeck`
  - `units`:
    - `Fermi_energy`: eV
    - `Seebeck`: muV/K

### scaling_summary.json
- path: `/app/outputs/scaling_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Key mobility and Seebeck scaling results extracted from the simulation.
- schema:
  - `type`: object
  - `required`:
    - `W_values`: array of floats (meV)
    - `mobility_at_1e12`: array of floats (cm^2/Vs)
    - `max_Seebeck`: array of floats (muV/K)
    - `scaling_exponent`: float (nullable, for mu ~ 1/W^gamma)

Notes: All outputs are derived from the KPM conductivity data; the checker compares the reported mobility and Seebeck values to paper's hidden reference values with tolerances, and verifies the scaling exponent trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mobility_vs_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "density",
          "epsilon_top",
          "mobility"
        ],
        "units": {
          "density": "cm^-2",
          "mobility": "cm^2/Vs"
        }
      },
      "description": "Mobility as a function of carrier density for each dielectric environment."
    },
    {
      "file": "seebeck_vs_EF.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Fermi_energy",
          "epsilon_top",
          "Seebeck"
        ],
        "units": {
          "Fermi_energy": "eV",
          "Seebeck": "muV/K"
        }
      },
      "description": "Seebeck coefficient as a function of Fermi energy for each dielectric environment."
    },
    {
      "file": "scaling_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "W_values": "array of floats (meV)",
          "mobility_at_1e12": "array of floats (cm^2/Vs)",
          "max_Seebeck": "array of floats (muV/K)",
          "scaling_exponent": "float (nullable, for mu ~ 1/W^gamma)"
        }
      },
      "description": "Key mobility and Seebeck scaling results extracted from the simulation."
    }
  ],
  "notes": "All outputs are derived from the KPM conductivity data; the checker compares the reported mobility and Seebeck values to paper's hidden reference values with tolerances, and verifies the scaling exponent trend."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier. Each required output file (mobility_vs_density.csv, seebeck_vs_EF.csv, scaling_summary.json) is inspected and scored independently. The verifier compares the reported mobility, Seebeck, and scaling exponent against reference values using appropriate tolerances. The scores from the three artifacts are weighted and combined into a single final reward between 0 and 1. Simply writing approximate numbers is not sufficient; the verifier expects internally consistent results derived from the KPM simulation. The exact tolerances and reference values are not disclosed, but they are chosen to accept legitimate computational variations. Your task is to faithfully execute the simulation and post-processing pipeline, not to guess the reference numbers.
