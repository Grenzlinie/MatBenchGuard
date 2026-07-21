# Growth Rate and Critical Supersaturation of Elongated Nanostructures via Kinetic Monte Carlo

## Problem background
Elongated nanostructures, such as quantum wires or interconnecting lines, are grown from the gas phase onto a masked substrate where material can only deposit on the exposed stripe. The finite width of the stripe creates size-dependent behavior: the growth rate and thermal stability are expected to vary with the stripe width. This modeling task addresses the central question of how the width of an elongated nanostructure influences its growth rate and the critical vapor pressure required for growth versus etching. Using kinetic Monte Carlo simulations, you will compute the time-average growth rate as a function of stripe width at a fixed supersaturation, and determine the critical supersaturation (equilibrium vapor pressure relative to an infinite surface) as a function of width.

## Approach
The growth is modeled with a continuous-time kinetic Monte Carlo method under the solid-on-solid approximation on a simple cubic lattice. The simulation cell is 80 lattice sites long in the stripe direction (periodic boundary condition) and w sites wide (free boundaries). At each surface site, adsorption and desorption events compete. The essential kinetic model is defined by the following equations, which must be implemented exactly.

### Time unit and equilibrium reference
The natural time scale is set by the adsorption rate of a gas in equilibrium with the solid. Denote by p_{a,e} the equilibrium adsorption probability per site per unit time. Equilibrium requires that the adsorption rate equals the desorption rate at kink sites (sites with exactly 3 first‑nearest neighbours). This gives the condition:

p_d(3) = p_{a,e}.

All rates will be expressed in units of 1/τ_a where τ_a = 1/p_{a,e} is the characteristic adsorption time. The dimensionless time t' = t/τ_a is used throughout the simulation.

### Adsorption probability
At a relative supersaturation σ∞ = P/P_c^∞ - 1 (with respect to an infinite surface) the adsorption probability per site, in units of 1/τ_a, is:

p_a = 1 + σ∞.

For the main growth-rate task you fix σ∞ = 0.6.

### Desorption probability
The desorption probability of an atom depends on its number n of first‑nearest neighbours. With interaction energy ε = 0.23 eV, temperature T = 1000 K, and Boltzmann constant k, the dimensionless parameter is ε/kT = 2.669.

In units of 1/τ_a the desorption probability for an atom with n neighbours is:

p_d(n) = exp( (3 − n) ε / kT )   =   exp( (3 − n) × 2.669 ).

### Solid‑on‑solid representation and neighbour counting
The surface is described by an integer height array h(i,j), i = 0,…,79 (long direction), j = 0,…,w−1 (width direction). Periodic boundary conditions apply in the i‑direction; free boundaries apply in the j‑direction (sites outside [0,w−1] do not exist and cannot provide neighbours).

An atom is a “surface atom” if it sits at the top of a column, i.e. its height is the current maximum height at that (i,j). Only surface atoms can desorb; adsorption occurs on top of an existing column, increasing its height by 1.

The number of first‑nearest neighbours n for a surface atom at (i,j) with height h is computed as follows:
- **Below:** If h > 0 there is always 1 neighbour immediately below (the atom of the same column at height h−1).
- **Horizontal (four possible):** For each of the four neighbours (i±1, j) and (i, j±1) that exist within the lattice (respecting the free boundaries in j), check whether the neighbour column height is at least h. If so, count 1 neighbour; otherwise 0.

Thus n ranges from 1 (only the below neighbour, for an isolated adatom) up to 5 (below + four horizontal neighbours, for an atom embedded in a complete layer). The condition p_d(3) = p_{a,e} corresponds to a kink atom with 3 neighbours (typically 1 below + 2 horizontal).

### Total event probability
Let the set of all surface sites be S. For each surface site with a local neighbour count n_i its desorption probability is p_d(n_i). Every surface site also has an adsorption probability p_a (for the column to grow one more atom). The total dimensionless event rate is:

p^tot = Σ_{i∈S} [ p_a + p_d(n_i) ]   =   Σ_{i∈S} [ (1 + σ∞) + exp( (3−n_i) ε / kT) ].

### Time advancement
After each event, the dimensionless time is incremented by:

Δt' = − ln(ξ) / p^tot,

where ξ is a random number uniformly distributed in (0, 1).

### Event selection (continuous‑time algorithm)
1. Compute the partial rates of each event class: the total adsorption rate is N_surface × p_a; the desorption rate for each class of atoms with n neighbours is N_d(n) × p_d(n), where N_d(n) is the number of surface atoms with exactly n neighbours.
2. Choose an event class with probability proportional to its rate. Within a class, pick a site uniformly at random.
3. Execute the event: for adsorption, h(i,j) → h(i,j) + 1; for desorption, h(i,j) → h(i,j) − 1 (must have h > 0).
4. Update p^tot and the time.

### Growth rate measurement
The instantaneous film height is the average of h(i,j) over all stripe columns. The growth rate is the slope of the height‑versus‑time curve in the (long‑time) linear regime, expressed in dimensionless units (layers per dimensionless time). Because nucleation barriers cause oscillatory behaviour for narrow stripes, you must average over at least 10 independent realisations (different random number seeds) per stripe width.

### Critical supersaturation
The critical supersaturation σ_c for a given width is the value of σ∞ at which the net growth rate becomes zero. Perform simulations for a few values of σ∞ around the expected zero‑growth point, measure the time‑averaged growth or etching rate, and interpolate to find σ_c.

## Reproduction target
Produce two scored comma-separated values (CSV) files under `/app/outputs`. First, `growth_rates.csv` must contain the time-average growth rate (dimensionless) for each specified stripe width w/a0 at a fixed relative supersaturation σ∞ = 0.6. The list of widths is: 6, 8, 10, 15, 20, 40, 160. Second, `critical_supersaturation.csv` must report the critical supersaturation σ_c (dimensionless) at which the net growth rate becomes zero for at least the widths w/a0 = 8 and 15. The growth rates are derived from averaging over at least 10 independent KMC simulations per width; the critical supersaturations are obtained by interpolating growth/etch rates from simulations spanning a range of σ∞. Both CSV files have columns: width (in units of a0) and either growth_rate or critical_supersaturation.

## Assets

- Python 3 with numpy/scipy: numpy scipy

## Workflow steps

### Step 1: Run KMC growth simulations at fixed supersaturation
- Role: process
- Action: Implement the continuous-time Monte Carlo model as detailed in the Approach section: solid-on-solid approximation, periodic boundary along the long direction, free boundaries at edges. For stripe widths w/a0 = 6, 8, 10, 15, 20, 40, 160 at relative supersaturation σ∞=0.6, run at least 10 independent simulations per width and record the number of deposited layers vs. dimensionless time.

### Step 2: Compute growth rates vs. width
- Role: scored
- Action: From the height-time trajectories obtained in Step 1, compute the time-average growth rate as the slope of height vs. time (in the linear regime) for each stripe width. Write the results to growth_rates.csv.
- Output file: `/app/outputs/growth_rates.csv`
- Format: csv
- Contract: CSV with two columns: width (float, in units of a0) and growth_rate (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 3: Run KMC simulations for varying supersaturations
- Role: process
- Action: For selected stripe widths (at least w/a0 = 8 and 15), perform KMC simulations over a range of relative supersaturations σ∞ near the expected zero-growth point. For each condition, record the net growth or etching rate.

### Step 4: Determine critical supersaturations
- Role: scored (load-bearing)
- Action: For each width, interpolate the growth/etch rates as a function of supersaturation to find the critical supersaturation σ_c at which the net growth rate is zero. Write the results to critical_supersaturation.csv.
- Output file: `/app/outputs/critical_supersaturation.csv`
- Format: csv
- Contract: CSV with two columns: width (float, in units of a0) and critical_supersaturation (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/growth_rates.csv`
- `/app/outputs/critical_supersaturation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### growth_rates.csv
- path: `/app/outputs/growth_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time-average growth rate of the elongated nanostructure as a function of stripe width at a fixed relative supersaturation of 0.6. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the growth rate increases with width.
- schema:
  - `type`: table
  - `required_columns`: `width`, `growth_rate`
  - `units`:
    - `width`: a0
    - `growth_rate`: dimensionless

### critical_supersaturation.csv
- path: `/app/outputs/critical_supersaturation.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical relative supersaturation as a function of stripe width. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the critical supersaturation decreases with increasing width.
- schema:
  - `type`: table
  - `required_columns`: `width`, `critical_supersaturation`
  - `units`:
    - `width`: a0
    - `critical_supersaturation`: dimensionless

Notes: No hidden gold or tolerances revealed; all scoring is based on comparison to paper-reported values via hidden tests.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "growth_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "width",
          "growth_rate"
        ],
        "units": {
          "width": "a0",
          "growth_rate": "dimensionless"
        }
      },
      "description": "Time-average growth rate of the elongated nanostructure as a function of stripe width at a fixed relative supersaturation of 0.6. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the growth rate increases with width."
    },
    {
      "file": "critical_supersaturation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "width",
          "critical_supersaturation"
        ],
        "units": {
          "width": "a0",
          "critical_supersaturation": "dimensionless"
        }
      },
      "description": "Critical relative supersaturation as a function of stripe width. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the critical supersaturation decreases with increasing width."
    }
  ],
  "notes": "No hidden gold or tolerances revealed; all scoring is based on comparison to paper-reported values via hidden tests."
}
```

## How you are scored
Your submission is scored by an automated hidden verifier. It reads the submitted growth_rates.csv and critical_supersaturation.csv and compares each entry against expected reference values, with tolerances that accommodate legitimate simulation-to-simulation variability. The verifier also checks that the reported growth rates increase with stripe width and that the critical supersaturations decrease with width. The final reward is a weighted combination of these checks; the exact reference values, tolerances, and weights are hidden. The task is not satisfied by simply reporting the paper's numbers — you must execute the Monte Carlo pipeline described in the workflow steps and compute the quantities from your own simulation runs.