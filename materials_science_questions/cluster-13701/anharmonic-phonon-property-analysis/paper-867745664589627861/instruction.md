# Steepest descent velocity decay exponent in 2D harmonic spheres

## Problem background
Glass-forming liquids exhibit complex relaxation dynamics when quenched to low energy states. The steepest descent (overdamped) dynamics from equilibrium configurations probes the geometry of the potential energy landscape. A central observable is the root-mean-squared velocity, which often follows a power-law decay with an exponent β that can depend on initial temperature and spatial dimension. Understanding this exponent in finite-dimensional systems is important for characterizing the nature of energy landscapes and the role of localized defects in structural glasses. This task requires computing the steepest descent velocity decay exponent β for a two-dimensional polydisperse harmonic sphere model at two contrasting initial conditions.

## Physical model
The system is a two‑dimensional polydisperse collection of N = 64000 soft harmonic spheres. The pairwise interaction potential is

\[
U(r_{ij}) =
\begin{cases}
\displaystyle \frac{\varepsilon}{2}\left(1 - \frac{r_{ij}}{\sigma_{ij}}\right)^2, & r_{ij} < \sigma_{ij} \\[6pt]
0, & r_{ij} \ge \sigma_{ij}
\end{cases}
\]

with additive contact distance \(\sigma_{ij} = \frac{d_i + d_j}{2}\), where \(d_i\) is the diameter of particle \(i\).

- Energy scale: \(\varepsilon = 1.0\).
- Length scale: mean particle diameter \(\langle d \rangle = 1.0\).
- Particle diameters are drawn from the continuous size distribution \(f(d) \propto d^{-3}\) with \(d \in [0.8, 1.2]\), giving a polydispersity \(\delta \approx 0.23\) (standard deviation/mean).
- Volume fraction: \(\phi = 1.2\) (particles may overlap because the potential is soft).
- Number of particles: \(N = 64000\).
- The simulation box is square with periodic boundary conditions in both directions. The side length \(L\) is determined from \(\phi = \frac{\pi}{4 L^2} \sum_i d_i^2\).

Equations of motion (steepest‑descent, overdamped dynamics):

\[
\zeta \frac{\mathrm d \mathbf r_i}{\mathrm d t} = -\frac{\partial E}{\partial \mathbf r_i},
\]

with damping coefficient \(\zeta = 1.0\).  The time unit is \(\tau_0 = \zeta \ell^2 / \varepsilon = 1.0\) because the unit length \(\ell = 1\) and unit energy \(\varepsilon = 1.0\).

The instantaneous root‑mean‑squared velocity is

\[
\langle |\mathbf v(t)| \rangle = \sqrt{\frac{1}{N} \sum_i \left| \frac{\mathrm d \mathbf r_i}{\mathrm d t} \right|^2 }.
\]

## Approach
For the high‑temperature limit (\(T \to \infty\)) a fully random configuration (uniform positions in the box) is generated.  For the low‑temperature regime an equilibrium configuration is prepared by swap Monte Carlo at \(T = 0.035\).  From each configuration the overdamped equations of motion are integrated numerically.  The root‑mean‑squared velocity is recorded at logarithmically spaced time points.  A power‑law model \(\langle |\mathbf v(t)| \rangle \sim t^{-\beta}\) is fitted to the long‑time tail of the decay to extract the exponent \(\beta\) for both initial conditions.

## Reproduction target

- Generate a random (uniform) initial configuration for the high‑temperature limit and an equilibrium configuration at \(T = 0.035\) using swap Monte Carlo.
- Simulate steepest‑descent dynamics from each configuration.  Record \(\langle |\mathbf v(t)| \rangle\) as a function of time in two CSV files (`velocity_highT.csv`, `velocity_lowT.csv`).
- Fit a power‑law decay to the appropriate long‑time window for each velocity series and extract the exponents \(\beta_{\mathrm{highT}}\) and \(\beta_{\mathrm{lowT}}\).
- Write the fitted exponents to `beta_results.json`.

## Assets

- LAMMPS: https://www.lammps.org/
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Prepare initial configurations
- **Role:** process
- **Action:**  
  - **High‑T configuration:** Create a box of side length \(L\) (computed from \(\phi = 1.2\) and the randomly drawn diameters) and place the \(N\) particles uniformly at random inside the box.  No exclusion constraint is enforced (overlaps are allowed).  
  - **Low‑T configuration:** Equilibrate the same system at \(T = 0.035\) using swap Monte Carlo.  Use a swap attempt probability of \(0.2\) and restrict swaps to particle pairs with \(|d_i - d_j| < 0.2\).  Use at least \(10^6\) Monte Carlo sweeps to ensure equilibrium.  
  Save the resulting configurations as intermediate files (e.g., `init_highT.data` and `init_lowT.data`; these are **not** required by the verifier).
- **Evidence:** `init_highT.data`, `init_lowT.data` (intermediate, not scored)

### Step 2: Run steepest‑descent dynamics (high temperature)
- **Role:** scored (load‑bearing)
- **Action:** Starting from the high‑temperature configuration, integrate the overdamped equations of motion \(\zeta \dot{\mathbf r}_i = -\nabla_i E\) with \(\zeta = 1.0\) and a time step \(\Delta t = 0.005\).  Run the simulation for at least \(t_{\max} = 10^4\) time units.  Record the root‑mean‑squared velocity \(\langle |\mathbf v(t)| \rangle\) at 200 logarithmically spaced time points from \(t_0 = 0.1\) to \(t_{\max}\).  Save the time series as a CSV file with columns `time` and `velocity`.
- **Output file:** `/app/outputs/velocity_highT.csv`
- **Format:** csv
- **Contract:** Columns: `time` (float, simulation time units), `velocity` (float, RMS velocity).
- **Scoring:** scored by hidden verifier

### Step 3: Run steepest‑descent dynamics (low temperature)
- **Role:** scored (load‑bearing)
- **Action:** Repeat the steepest‑descent integration starting from the low‑temperature configuration.  Use the same integration parameters, duration, and recording scheme as in Step 2.
- **Output file:** `/app/outputs/velocity_lowT.csv`
- **Format:** csv
- **Contract:** Columns: `time` (float), `velocity` (float).
- **Scoring:** scored by hidden verifier

### Step 4: Fit velocity decay exponents
- **Role:** scored
- **Action:** Read `velocity_highT.csv` and `velocity_lowT.csv`.  For each file, select the long‑time window where the decay follows a power law (after initial transients, before finite‑size cutoff).  Fit a model \(\langle |\mathbf v(t)| \rangle = A \cdot t^{-\beta}\) (e.g., log–log linear regression).  Extract the exponents \(\beta_{\mathrm{highT}}\) and \(\beta_{\mathrm{lowT}}\).  Write the results as a JSON file.
- **Output file:** `/app/outputs/beta_results.json`
- **Format:** json
- **Contract:** `{"beta_highT": float, "beta_lowT": float}`
- **Scoring:** scored by hidden verifier

## Output files
Write all scored artifacts under `/app/outputs`:
- `/app/outputs/velocity_highT.csv`
- `/app/outputs/velocity_lowT.csv`
- `/app/outputs/beta_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### velocity_highT.csv
- path: `/app/outputs/velocity_highT.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: High‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data.
- schema:
  - `type`: table
  - `required_columns`: `time`, `velocity`
  - `units`:
    - `time`: simulation time units
    - `velocity`: RMS velocity (same units as dr_i/dt)

### velocity_lowT.csv
- path: `/app/outputs/velocity_lowT.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Low‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data.
- schema:
  - `type`: table
  - `required_columns`: `time`, `velocity`
  - `units`:
    - `time`: simulation time units
    - `velocity`: RMS velocity

### beta_results.json
- path: `/app/outputs/beta_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Self‑reported fitted exponents β for the two temperatures. The checker will recompute β from the raw velocity files, compare to hidden paper‑reported values, and cross‑verify the self‑reported numbers.
- schema:
  - `type`: object
  - `required`:
    - `beta_highT`: float (unitless)
    - `beta_lowT`: float (unitless)

Notes: The primary scoring is based on recomputing β from velocity_highT.csv and velocity_lowT.csv using a power‑law fit in the appropriate long‑time window. The beta_results.json file provides self‑consistency cross‑check but does not carry strong scoring weight.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "velocity_highT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "velocity"
        ],
        "units": {
          "time": "simulation time units",
          "velocity": "RMS velocity (same units as dr_i/dt)"
        }
      },
      "description": "High‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data."
    },
    {
      "file": "velocity_lowT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "velocity"
        ],
        "units": {
          "time": "simulation time units",
          "velocity": "RMS velocity"
        }
      },
      "description": "Low‑temperature steepest descent velocity time series. The checker will refit the decay exponent β from these data."
    },
    {
      "file": "beta_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "beta_highT": "float (unitless)",
          "beta_lowT": "float (unitless)"
        }
      },
      "description": "Self‑reported fitted exponents β for the two temperatures. The checker will recompute β from the raw velocity files, compare to hidden paper‑reported values, and cross‑verify the self‑reported numbers."
    }
  ],
  "notes": "The primary scoring is based on recomputing β from velocity_highT.csv and velocity_lowT.csv using a power‑law fit in the appropriate long‑time window. The beta_results.json file provides self‑consistency cross‑check but does not carry strong scoring weight."
}
```

## How you are scored
A hidden verifier independently reads your `velocity_highT.csv` and `velocity_lowT.csv`. It performs its own power-law fit on the long-time domain and obtains recomputed β values. It then compares these recomputed exponents to reference values (not revealed to you) and cross‑checks the self‑reported β in `beta_results.json` for consistency. Each scored stage (the two velocity CSVs and the final beta_results.json) contributes to a weighted score. The overall reward reflects how accurately your computed exponents agree with the reference, measured with a permissive tolerance that absorbs legitimate implementation variability. Simply reporting a number is not sufficient; the raw velocity data must support a comparable fit.