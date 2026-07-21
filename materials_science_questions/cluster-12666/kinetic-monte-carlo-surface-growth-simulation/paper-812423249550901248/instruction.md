# Kinetic Monte Carlo Simulation of A+B2 Reaction on a Roughened Supported Nanoparticle

## Problem background
Supported nanoparticles are central to heterogeneous catalysis, but traditional models treat the catalyst surface as a flat, homogeneous plane. Real nanoparticles have dynamic surface morphology that evolves due to thermal diffusion of metal atoms and interactions with adsorbed species. The interplay between particle shape, surface roughness, adsorbate diffusion (particularly spillover from particle to support), and reaction kinetics can lead to kinetic behaviors that differ substantially from the flat-surface idealization. This task implements a statistical lattice (solid-on-solid Kossel crystal) model of a single supported nanoparticle to quantify how the dynamic surface morphology and spillover of adsorbed A species alter the steady-state kinetics of the model Langmuir–Hinshelwood reaction 2A + B2 → 2AB. The goal is to compute the steady-state surface coverages and reaction rate as functions of the gas-phase molar ratio of A, and to document any adsorbate-induced shape change of the particle under reaction conditions.

## Approach
The particle is modeled as a finite Kossel crystal on an N×N square support with periodic boundary conditions. The initial particle is a 21×21×10 column block. Metal-surface atom diffusion is simulated via Metropolis Monte Carlo using pair interaction energies Jmm = -10 kJ/mol (metal-metal) and Jms = -2.5 kJ/mol (metal-support). After achieving a dynamic equilibrium shape at T=500 K, the reaction is overlaid on the particle using a kinetic Monte Carlo procedure. The reaction mechanism is the ZGB-type Langmuir–Hinshelwood mechanism: A adsorbs molecularly and can diffuse; B2 adsorbs dissociatively onto adjacent empty sites at the same height level, remains immobile, and reacts immediately when it has a neighboring A adsorbate also at the same level. The simulation is run for three distinct regimes to isolate key effects: (i) flat surface with no adsorbate or metal diffusion, serving as the ZGB baseline; (ii) roughened T=500 K surface with A adsorption and diffusion both on the metal particle and on the support (spillover) but no metal diffusion; (iii) roughened T=500 K surface with A adsorption and diffusion only on the metal particle (no support adsorption) and with concurrent metal atom diffusion. For each regime, the steady-state coverages θ_A, θ_B and the reaction rate (AB molecules per Monte Carlo step) are recorded at a range of A molar ratios YA = P_A/(P_A+P_{B2}) spanning from 0 to 1. The final particle morphology (height map) for the no-spillover case at YA=0.37 is also captured to examine adsorbate-induced reshaping.

## Algorithm specifications

All rules below are essential to reproduce the correct steady-state kinetics. Implement them exactly as described.

### 1. Lattice and height variables
- The system is a 200×200 square lattice of cells with periodic boundary conditions in both directions.
- Each cell `(x, y)` has an integer column height `h(x, y) ≥ 0`.  
  `h(x, y)` = number of metal atoms stacked in that column.
- Initial configuration (flat cube):  
  `h(x, y) = 10` for `0 ≤ x, y < 21`; `h(x, y) = 0` elsewhere.
- A **metal surface site** is any cell with `h(x, y) > 0` (the top atom of the column is exposed).  
  The number of such sites is denoted `N_metal`.
- A **support site** is any cell with `h(x, y) = 0`.
- Overhangs are forbidden: a column may never have a height greater than its neighbour + 1, and this SOS constraint is maintained at all times.

### 2. Metal diffusion (Metropolis Monte Carlo)

**Energy parameters:**
- `Jmm = -10 kJ/mol` – bond energy between two nearest-neighbour metal atoms.
- `Jms = -2.5 kJ/mol` – bond energy between a metal atom and the support immediately underneath it.
- Temperature `T = 500 K`.
- Gas constant `R = 8.314e-3 kJ/(mol·K)`.

**One metal diffusion MC step = N² = 40 000 transfer attempts.**

Each attempt:
1. Randomly select a surface metal atom: pick a cell `(x, y)` with `h(x,y) > 0`.
2. Randomly select a nearest-neighbour cell `(x', y')` from `{(x±1,y), (x,y±1)}` (respecting periodic boundaries).
3. **SOS condition check:** The move is only allowed if `h(x', y') ≤ h(x, y) - 1`.  
   If not, reject the attempt (no change) and proceed to the next attempt.
4. **Compute energy change ΔE.**  
   Let `h_old = h(x, y)` (height **before** moving the atom away) and `h_new = h(x', y') + 1` (height the atom would have after moving).
   - **Old position neighbour count `n_mm_old`:** number of nearest neighbours (among the four cells) whose height is `≥ h_old`.
   - **New position neighbour count `n_mm_new`:** number of nearest neighbours (among the four cells) whose height is `≥ h_new`.
   - **Support bond:**  
     `s_old = 1` if `h_old == 1` (atom directly on support before move), else `0`.  
     `s_new = 1` if `h_new == 1` (atom directly on support after move), else `0`.
   - `ΔE = Jmm * (n_mm_new - n_mm_old) + Jms * (s_new - s_old)`.
5. **Metropolis criterion:**  
   If `ΔE ≤ 0`, accept the move.  
   If `ΔE > 0`, accept with probability `exp(-ΔE / (R*T))`.
6. If accepted: `h(x, y) → h(x, y) - 1`, `h(x', y') → h(x', y') + 1`.

Run **50 000 – 70 000 such MC steps** to obtain the equilibrium particle shape. Store this height map; it will be used as the initial morphology for the roughened-surface reaction simulations (conditions `rough_T500_spillover` and `rough_T500_no_spillover`). The equilibrium height map is an internal intermediate and does not need to be written to `/app/outputs`.

### 3. Reaction model – common definitions

**Adsorption events – general rule:**  
Adsorption attempts are always made on empty (vacant) sites. An adsorbate (A or B) occupies the site and blocks it.

**Surface coverages** `θ_A` and `θ_B` are defined relative to the **metal surface sites only**:  
`θ_A = (number of A on metal surface) / N_metal`  
`θ_B = (number of B on metal surface) / N_metal`  
(A molecules residing on the support are **not** counted in `θ_A` or `θ_B`.)

**Reaction rate** `r` = number of AB molecules produced **per reaction MC step**.

**Reaction MC step definition:**  
One reaction MC step consists of **`N_metal` adsorption attempts**, where `N_metal` is the current number of metal surface sites.  
`N_metal` is fixed in `flat` and `rough_T500_spillover`, but varies in `rough_T500_no_spillover` because of simultaneous metal diffusion.

**Adsorption attempt details:**
- Draw a random number `u ∈ [0,1)`.
- **If `u < YA`** → attempt **A adsorption**:
  - Condition `flat` and `rough_T500_no_spillover`: randomly select a metal surface site (cell with `h>0`). If vacant, adsorb A there with probability 1.
  - Condition `rough_T500_spillover`: with probability 0.5 select a random metal surface site; with probability 0.5 select a random support site (cell with `h=0`). If the selected site is vacant, adsorb A there with probability 1.
- **If `u ≥ YA`** → attempt **B₂ dissociative adsorption**:
  - Randomly select a metal surface site `(i,j)`.  
  - Randomly select a neighbour `(i',j') ∈ {(i±1,j), (i,j±1)}`.  
  - **Height condition:** the attempt proceeds only if `h(i,j) == h(i',j')` (the two sites belong to the same terrace). Otherwise the attempt is rejected.
  - If both `(i,j)` and `(i',j')` are vacant:
      * Place one B atom on `(i,j)` and one on `(i',j')`.
      * **Immediate reaction check for each of the two B atoms:**
        - Inspect the four nearest neighbours at the **same height level**.
        - If at least one neighbour holds an A adsorbate, reaction occurs: that A atom and that B atom are removed (forming an AB molecule that desorbs instantly); increment the reaction counter by 1. The site pair becomes vacant again.
        - If no A neighbour is found, the B stays immobile on the site.
    - If the two sites are not both vacant, the attempt is rejected.

**A diffusion (performed once per reaction MC step):**
- After the `N_metal` adsorption attempts, all currently adsorbed A atoms undergo one diffusion attempt each (the order can be randomised or sequential).
- For an A atom at `(x,y)`:
   1. Randomly select a neighbour `(x',y')`.
   2. For conditions `flat` and `rough_T500_no_spillover`: the target must be a metal surface site (`h > 0`) and vacant. For `rough_T500_spillover`: the target can be either a metal surface site (`h > 0`) or a support site (`h = 0`), and must be vacant.
   3. If valid and vacant, move A there with probability 1 (diffusion is barrierless).

### 4. Simulation protocols for the three conditions

#### Condition `flat`
- Use the initial `21×21×10` block; **no metal diffusion**.
- Initial surface: all sites vacant.
- For each chosen `YA` value:
   1. Equilibrate for **5 000 reaction MC steps**.
   2. Measure averages over the subsequent **1 000 reaction MC steps**: `θ_A`, `θ_B`, and `r` (AB per step).
- Record one row in `kinetic_curves.csv` for this `YA`.

#### Condition `rough_T500_spillover`
- Use the equilibrium height map (from Section 2) as the fixed surface; **no metal diffusion during reaction**.
- Initial surface: all sites vacant.
- For each `YA`:
   1. Equilibrate for **5 000 reaction MC steps**.
   2. Measure over the next **1 000 reaction MC steps**.
- Record one row in `kinetic_curves.csv`.

#### Condition `rough_T500_no_spillover`
- Use the equilibrium height map (from Section 2) as the starting configuration; **metal diffusion and reaction run concurrently**.
- The two processes are **interleaved cycle by cycle**:  
  **One cycle = 1 metal diffusion MC step (40 000 transfer attempts, Section 2) + 1 reaction MC step (`N_metal` adsorption attempts, Section 3).**
- Initial surface: all sites vacant.
- For each `YA`:
   1. Equilibrate for **5 000 cycles**.
   2. Measure over the next **1 000 cycles**.
- Record one row in `kinetic_curves.csv`.
- **Additionally**, at `YA = 0.37`, after the measurement phase, extract the final height map `h(x,y)` for all `0 ≤ x,y < 200` and write it to `shape_T500_no_spillover.csv`.

## Reproduction target
Implement the above statistical-lattice Monte Carlo framework and produce the following scored outputs in `/app/outputs`:
1. **`kinetic_curves.csv`**: a CSV file with columns `condition` (string: `flat`, `rough_T500_spillover`, `rough_T500_no_spillover`), `YA` (float), `theta_A` (float), `theta_B` (float), `reaction_rate` (float). For each condition, provide steady-state values for at least 15 different YA points evenly covering the interval 0 to 1.
2. **`shape_T500_no_spillover.csv`**: a CSV file with columns `x` (int, 0..199), `y` (int, 0..199), `height` (int) giving the column heights of the entire 200×200 support lattice at steady state for the `rough_T500_no_spillover` condition at `YA=0.37`.

## Assets
No external datasets or pre-trained models are required. The simulation relies solely on the problem parameters given in the workflow steps and the algorithm specifications. You will need a Python environment with standard numerical libraries (`numpy`, `scipy` recommended). Optionally, `numba` can accelerate the Monte Carlo loops.

## Workflow steps

### Step 1: Equilibrate nanoparticle morphology at T=500 K
- Role: process
- Action: Using the Metropolis Monte Carlo surface-atom diffusion protocol described in Section 2 (initial 21×21×10 column block on a 200×200 support, Jmm = -10 kJ/mol, Jms = -2.5 kJ/mol, T=500 K), run for at least 50 000 MC steps (each step = N² transfer attempts) to reach a dynamic equilibrium shape. Store the resulting height map internally for use as the initial morphology in the roughened-surface reaction simulations (Step 2 and Step 3).

### Step 2: Reaction kinetics – coverage and rate curves
- Role: scored (load-bearing)
- Action: For the three simulation settings (`flat`, `rough_T500_spillover`, `rough_T500_no_spillover`) as defined in the algorithm specifications, run the kinetic Monte Carlo reaction for at least 15 values of YA spanning 0 to 1. After the specified equilibration and measurement phases, record steady-state `theta_A`, `theta_B` and `reaction_rate`. Aggregate all data into `kinetic_curves.csv`.
- Output file: `/app/outputs/kinetic_curves.csv`
- Format: csv
- Contract: CSV with columns: `condition` (string: `flat`, `rough_T500_spillover`, `rough_T500_no_spillover`), `YA` (float), `theta_A` (float), `theta_B` (float), `reaction_rate` (float). Each row is one YA point per condition.
- Scoring: scored by hidden verifier

### Step 3: Final particle shape for no-spillover case at YA=0.37
- Role: scored
- Action: From the `rough_T500_no_spillover` simulation at `YA=0.37`, extract the column heights `h(x,y)` of the entire 200×200 lattice after the system has reached a steady reaction state (end of the measurement phase). Write the height map to `shape_T500_no_spillover.csv`.
- Output file: `/app/outputs/shape_T500_no_spillover.csv`
- Format: csv
- Contract: CSV with columns: `x` (int, 0..199), `y` (int, 0..199), `height` (int). Each row gives the number of metal atoms in the column at that support cell.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kinetic_curves.csv`
- `/app/outputs/shape_T500_no_spillover.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kinetic_curves.csv
- path: `/app/outputs/kinetic_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of steady-state coverages and reaction rate as functions of YA for the three simulation conditions. Checker compares against hidden digitized reference curves with tolerances and rewards correct peak location and reaction window boundaries.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `YA`, `theta_A`, `theta_B`, `reaction_rate`

### shape_T500_no_spillover.csv
- path: `/app/outputs/shape_T500_no_spillover.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Final height map of the 200x200 support lattice for the no-spillover condition at YA=0.37. Checker audits structural properties (e.g., height variance, mean height deviation from initial block) to confirm an adsorbate-induced shape change, not exact heights.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `height`

Notes: All simulation parameters (N, Nin, hin, Jmm, Jms, T, reaction rules, MC step definitions) are explicitly given in the algorithm specifications and steps. The checker uses the paper's reported curves as reference for `kinetic_curves` and performs a structural audit for the shape output. No external datasets are required; the agent implements the Monte Carlo code from the described algorithm.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kinetic_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "YA",
          "theta_A",
          "theta_B",
          "reaction_rate"
        ]
      },
      "description": "Table of steady-state coverages and reaction rate as functions of YA for the three simulation conditions. Checker compares against hidden digitized reference curves with tolerances and rewards correct peak location and reaction window boundaries."
    },
    {
      "file": "shape_T500_no_spillover.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "height"
        ]
      },
      "description": "Final height map of the 200x200 support lattice for the no-spillover condition at YA=0.37. Checker audits structural properties (e.g., height variance, mean height deviation from initial block) to confirm an adsorbate-induced shape change, not exact heights."
    }
  ],
  "notes": "All simulation parameters (N, Nin, hin, Jmm, Jms, T) are explicitly given in the steps. The checker uses the paper's reported curves as reference for kinetic_curves and performs a structural audit for the shape output. No external datasets are required; the agent implements the Monte Carlo code from the described algorithm."
}
```

## How you are scored
Each output file is evaluated by a hidden verifier that assigns a weighted partial score, and the total score is their weighted sum. For `kinetic_curves.csv`, the verifier compares your θ_A, θ_B, and reaction rate curves to reference curves derived from the paper’s reported data, using tolerance-based scoring that rewards correct location of the reaction rate peak, the boundaries of the nonzero reaction window, and the overall shape of the coverage curves. For `shape_T500_no_spillover.csv`, the verifier audits structural properties of the height map (e.g., standard deviation of column heights, mean height relative to the initial block) to confirm a significant morphological change compared to the equilibrium shape. Reporting the paper’s numbers is not sufficient; your simulation must produce artifacts that the verifier can independently evaluate. Attempting to read or match the hidden reference is not possible, as the reference data are not accessible to you.