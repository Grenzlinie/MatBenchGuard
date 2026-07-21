# Surface Enhancement Crossover in Ferromagnetic Thin Films

## Problem background
Ferromagnetic thin films can exhibit a surface enhancement crossover. Because the surface breaks translational symmetry, the exchange interaction at the surface, Js, may differ from the bulk exchange Jb. The ratio R = Js / Jb governs whether the magnetic order is dominated by the bulk (ordinary transition) or the surface (extraordinary transition). At a special value R_c, the dynamic critical temperature Tc is expected to become independent of the film thickness L, marking a crossover between these two regimes. The application of an external oscillating magnetic field may shift this crossover. Using Monte Carlo simulations, we can map out Tc as a function of R, L, and the reduced field amplitude H0 to locate the crossover point and examine its response to the oscillating field.

## Approach
We simulate the spin-1/2 Ising model on a simple cubic lattice of size 70×70×L with periodic boundary conditions in the film plane and free boundaries perpendicular to the film. The Hamiltonian includes nearest‑neighbor exchange interactions Jb = 1 in the bulk and Js = R·Jb on the two surface layers. An oscillating magnetic field h(t) = h0 sin(ωt) is applied, with period P = 100 Monte Carlo steps per spin (MCS). The reduced field amplitude is H0 = h0 / Jb. For each combination of film thickness L ∈ {3, 4, 5}, reduced surface exchange R from 1.0 to 2.0 in steps of 0.1, and H0 ∈ {0.0, 0.5}, we perform 50 independent Metropolis Monte Carlo runs, each with 25 000 MCS equilibration and 50 000 MCS production. From the time series of the total energy, we compute the time‑averaged energy per spin over one field period and then the specific heat C(T) = ∂⟨E⟩/∂T via finite differences on a fine temperature grid. The dynamic critical temperature Tc for each (L, H0, R) is taken as the temperature of the maximum of C(T).

## Reproduction target
Produce a CSV file `critical_temperatures.csv` with columns L (integer), H0 (float), R (float), Tc (float), where Tc is the reduced temperature (in units of kB T / Jb) at which the specific heat reaches its maximum. The file must contain one row for each simulated (L, H0, R) combination. The correctness of the Tc values will be inferred from the structural properties of the resulting Tc‑vs‑R curves, not from matching a single published number.

## Assets

- Python 3
- numpy: https://pypi.tuna.tsinghua.edu.cn/simple

## Workflow steps

### Step 1: Monte Carlo simulation and specific heat computation
- Role: process
- Action: Implement Metropolis Monte Carlo simulation of the spin-1/2 Ising model on a 70x70xL simple cubic lattice with periodic in-plane and free perpendicular boundary conditions. Use Jb=1, Js=R*Jb with R from 1.0 to 2.0 step 0.1, oscillating field h(t)=h0 sin(ωt) period P=100 MCS, reduced amplitude H0 ∈ {0.0, 0.5}. For each (L, H0, R) with L=3,4,5, perform 50 independent runs, 25000 MCS equilibration, 50000 MCS production. Record instantaneous total energy per spin, compute time-averaged energy over one period, and compute specific heat C(T) = dE_tot/dT via finite differences over a temperature grid. Store intermediate energy data (optional).
- Evidence: `/app/outputs/simulation_energies.csv`

### Step 2: Extract dynamic critical temperatures
- Role: scored (load-bearing)
- Action: For each combination (L, H0, R), locate the temperature T_c where C(T) reaches its maximum. Compile all results into a CSV file.
- Output file: `/app/outputs/critical_temperatures.csv`
- Format: csv
- Contract: L:int, H0:float, R:float, Tc:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_temperatures.csv
- path: `/app/outputs/critical_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dynamic critical temperatures extracted from specific heat maxima for each parameter set.
- schema:
  - `type`: table
  - `required_columns`: `L`, `H0`, `R`, `Tc`
  - `units`:
    - `L`: number of layers (integer)
    - `H0`: dimensionless
    - `R`: dimensionless
    - `Tc`: reduced temperature (k_B T_c / J_b)

Notes: The hidden checker will perform structural analysis on this CSV to identify the intersection point R_c and verify crossover behavior and slow variation with H0; no numeric gold values are required from the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "H0",
          "R",
          "Tc"
        ],
        "units": {
          "L": "number of layers (integer)",
          "H0": "dimensionless",
          "R": "dimensionless",
          "Tc": "reduced temperature (k_B T_c / J_b)"
        }
      },
      "description": "Dynamic critical temperatures extracted from specific heat maxima for each parameter set."
    }
  ],
  "notes": "The hidden checker will perform structural analysis on this CSV to identify the intersection point R_c and verify crossover behavior and slow variation with H0; no numeric gold values are required from the agent."
}
```

## How you are scored
A hidden verifier will read your `critical_temperatures.csv`. For each value of H0, it will interpolate Tc as a function of R separately for each film thickness L. It will then locate the reduced exchange R at which the Tc curves for different L intersect, i.e., the point where Tc becomes independent of L. The verifier checks that for R below this intersection, Tc increases with L, while above it, Tc decreases with L, corresponding to the ordinary‑to‑extraordinary crossover. It also verifies that the intersection point obtained from the H0 = 0.5 data is consistent with the zero‑field intersection point (within a tolerance). Your score reflects how well the computed Tc values reproduce this crossover structure, not exact agreement with a tabulated reference. The verifier uses tolerance bands that account for statistical noise; a careful implementation of the protocol is expected to pass.
