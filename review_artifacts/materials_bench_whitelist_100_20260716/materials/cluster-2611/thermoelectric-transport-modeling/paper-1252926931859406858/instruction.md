# Thermoelectric transport coefficients for flat-band chains using non-interacting NEGF

## Problem background
Thermoelectric materials convert a temperature difference into electricity. A long-standing design principle, established by Mahan and Sofo, suggests that a perfectly narrow transport window—ideally a delta-function in the energy-dependent transmission—would maximize the thermoelectric figure of merit zT. Flat electronic bands, which concentrate the density of states into a tiny energy range, appear to offer a natural route to such sharp transport resonances and hence to exceptional thermoelectric performance. However, a flat band also implies zero group velocity, which may suppress charge transport entirely. This project investigates the thermoelectric response of two one-dimensional model systems with flat bands: the sawtooth chain, where the flat band is separated from the dispersive band by a gap, and the diamond chain, where the flat band touches the dispersive band. By computing the full set of linear-response transport coefficients as a function of gate voltage, we examine whether and under what conditions a flat band can actually enhance thermoelectric performance, and how the proximity of the flat band to dispersive states matters.

## Approach
Transport is treated within the Landauer–Büttiker / non-equilibrium Green function framework for non-interacting electrons. Two tight-binding Hamiltonians are constructed: the sawtooth lattice (with parameters satisfying the flat-band condition, homogeneous onsite energies and hopping ratio t_ab = √2 t_aa) and the diamond lattice (equal onsite energies, with hopping t' = t, giving a gapless flat band touching a dispersive band). Each chain of N=24 unit cells is coupled to two semi-infinite metallic leads in the wide-band limit, characterized by a constant lead coupling strength Γ. The energy-dependent transmission function T(ω) is computed using the Landauer formula (e.g., via the Kwant package). The transport integrals ℐ_n = (1/(2πħ)) ∫ dω (−∂f/∂ω) T(ω) (ω−μ)^n are evaluated numerically. From these, the electrical conductivity σ, Seebeck coefficient S, electronic thermal conductivity κ_e, Lorenz ratio L/L₀, and thermoelectric figure of merit zT are obtained using the standard linear-response expressions, with a fixed phonon thermal conductivity κ_ph = 10⁻³ g₀ T (g₀ is the quantum of thermal conductance). The gate voltage V_g (which shifts the chemical potential μ = −e V_g) is swept across the flat-band region at temperature T = 80 K, and the whole procedure is repeated for two lead broadening values Γ = 5 meV and Γ = 50 meV. This setup allows a direct comparison of transport in an isolated-flat-band system (sawtooth) and a gapless-flat-band system (diamond).

## Reproduction target
Produce two CSV files containing the computed thermoelectric coefficients as functions of the gate voltage V_g for both models at T = 80 K, each for the two lead coupling strengths Γ = 5 meV and Γ = 50 meV:

1. `/app/outputs/sawtooth_transport.csv` — data for the sawtooth chain.
2. `/app/outputs/diamond_transport.csv` — data for the diamond chain.

Each file must have columns: Vg (eV), Gamma (meV), sigma (dimensionless, units G₀/Γ), S (mV/K), L_over_L0 (dimensionless), zT (dimensionless). The file should contain two contiguous blocks: first all rows for Γ=5 meV (in increasing Vg), then all rows for Γ=50 meV (in increasing Vg).

The resulting curves will be evaluated by a hidden verifier that checks whether the transport coefficients satisfy the physical expectations for flat-band systems: (i) in the sawtooth model the electrical conductivity should be strongly suppressed when the chemical potential lies within the flat band, while the Seebeck coefficient becomes large; (ii) in the diamond model the conductivity should remain finite in the flat-band region; (iii) the peak of zT should occur near the edge of the flat band, not deep inside it. No exact numeric match to any published figure is required; only these structural trends are scored.

## Assets

- Kwant: https://kwant-project.org/
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute transport coefficients for the sawtooth chain
- Role: scored (load-bearing)
- Action: Build the sawtooth-chain tight-binding Hamiltonian with parameters satisfying the flat-band condition (homogeneous onsite energies, hopping t_ab = sqrt(2)*t_aa). Couple the chain to two semi-infinite leads in the wide-band limit with coupling strengths Gamma = 5 meV and 50 meV. Compute the energy-dependent transmission function T(ω) using the Landauer-Büttiker formula (via Kwant). Numerically evaluate the transport integrals I_n to obtain electrical conductivity σ, Seebeck coefficient S, Lorenz ratio L/L0, and thermoelectric figure of merit zT using a fixed phonon thermal conductivity κ_ph = 10⁻³ g₀ T (where g₀ is the quantum of thermal conductance). Scan the gate voltage Vg over a range that includes the flat-band region at temperature T = 80 K. Output all results as a CSV file.
- Output file: `/app/outputs/sawtooth_transport.csv`
- Format: csv
- Contract: CSV with columns: Vg (float, eV), Gamma (float, meV), sigma (float, units of G0/Gamma), S (float, mV/K), L_over_L0 (float, dimensionless), zT (float, dimensionless). One row per Vg value. The file contains two blocks: first all rows for Gamma=5 meV, then all rows for Gamma=50 meV.
- Scoring: scored by hidden verifier

### Step 2: Compute transport coefficients for the diamond chain
- Role: scored (load-bearing)
- Action: Build the diamond-chain tight-binding Hamiltonian with parameters giving a gapless flat band touching a dispersive band (equal onsite energies, t'=t). Couple to leads with Γ = 5 meV and 50 meV. Compute T(ω), integrals, and derive σ, S, κ_e, L/L0, and zT exactly as in step 01. Scan Vg at T = 80 K and produce the CSV.
- Output file: `/app/outputs/diamond_transport.csv`
- Format: csv
- Contract: CSV with columns: Vg (float, eV), Gamma (float, meV), sigma (float, units of G0/Gamma), S (float, mV/K), L_over_L0 (float, dimensionless), zT (float, dimensionless). One row per Vg value. The file contains two blocks: first all rows for Gamma=5 meV, then all rows for Gamma=50 meV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sawtooth_transport.csv`
- `/app/outputs/diamond_transport.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sawtooth_transport.csv
- path: `/app/outputs/sawtooth_transport.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Transport properties (σ, S, L/L0, zT) as a function of gate voltage for the sawtooth chain at Γ=5 and 50 meV.
- schema:
  - `type`: table
  - `required_columns`: `Vg`, `Gamma`, `sigma`, `S`, `L_over_L0`, `zT`
  - `units`:
    - `Vg`: eV
    - `Gamma`: meV
    - `sigma`: G0/Gamma (dimensionless)
    - `S`: mV/K
    - `L_over_L0`: dimensionless
    - `zT`: dimensionless

### diamond_transport.csv
- path: `/app/outputs/diamond_transport.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Transport properties (σ, S, L/L0, zT) as a function of gate voltage for the diamond chain at Γ=5 and 50 meV.
- schema:
  - `type`: table
  - `required_columns`: `Vg`, `Gamma`, `sigma`, `S`, `L_over_L0`, `zT`
  - `units`:
    - `Vg`: eV
    - `Gamma`: meV
    - `sigma`: G0/Gamma (dimensionless)
    - `S`: mV/K
    - `L_over_L0`: dimensionless
    - `zT`: dimensionless

Notes: The output files contain the computed transport coefficients under non-interacting NEGF. The units and column ordering must match the schema. The checker will verify structural trends (e.g., σ → 0 for sawtooth flat-band, S above threshold, peak zT below flat-band edge) against hidden criteria; no exact match to published figures is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sawtooth_transport.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vg",
          "Gamma",
          "sigma",
          "S",
          "L_over_L0",
          "zT"
        ],
        "units": {
          "Vg": "eV",
          "Gamma": "meV",
          "sigma": "G0/Gamma (dimensionless)",
          "S": "mV/K",
          "L_over_L0": "dimensionless",
          "zT": "dimensionless"
        }
      },
      "description": "Transport properties (σ, S, L/L0, zT) as a function of gate voltage for the sawtooth chain at Γ=5 and 50 meV."
    },
    {
      "file": "diamond_transport.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vg",
          "Gamma",
          "sigma",
          "S",
          "L_over_L0",
          "zT"
        ],
        "units": {
          "Vg": "eV",
          "Gamma": "meV",
          "sigma": "G0/Gamma (dimensionless)",
          "S": "mV/K",
          "L_over_L0": "dimensionless",
          "zT": "dimensionless"
        }
      },
      "description": "Transport properties (σ, S, L/L0, zT) as a function of gate voltage for the diamond chain at Γ=5 and 50 meV."
    }
  ],
  "notes": "The output files contain the computed transport coefficients under non-interacting NEGF. The units and column ordering must match the schema. The checker will verify structural trends (e.g., σ → 0 for sawtooth flat-band, S above threshold, peak zT below flat-band edge) against hidden criteria; no exact match to published figures is required."
}
```

## How you are scored
A hidden verifier parses your two CSV output files. It performs a structural audit that tests:

- Whether the electrical conductivity σ for the sawtooth chain falls below a (hidden) low threshold when the gate voltage is tuned to the flat-band energy, while the Seebeck coefficient S simultaneously exceeds a hidden large threshold, for both Γ values.
- Whether, for the diamond chain, σ remains above a (hidden) minimum threshold in the same flat-band gate-voltage region.
- Whether the gate voltage at which the zT maximum occurs is located below the flat-band edge (within a hidden voltage window) for both models, i.e., the peak thermoelectric performance does not lie inside the flat band.

The verifier does not require exact numerical agreement with any published data; it checks only that the computed trends respect these physical constraints. The two scored steps carry approximately equal weight in the final reward. Accurately implementing the non-interacting NEGF transport calculation to obtain the correct physical trends is essential for a passing score.
