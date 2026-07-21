# Kinetic Monte Carlo Simulation of Step Wandering and Characteristic Wavelength Scaling

## Problem background
During deposition of Ga on a Si(111) vicinal face, a structural transition occurs preferentially from the lower side of steps, releasing extra adatoms that cause the steps to advance. Under these conditions, a straight step becomes unstable and spontaneously develops a finger-like wandering pattern. This task reproduces a Kinetic Monte Carlo simulation of a single step with an adatom source immediately in front of it to investigate how the characteristic wavelength of the pattern emerges and how it depends on the step stiffness and step velocity. The goal is to implement the simulation and measure the wavelength to test the predicted scaling behavior.

## Approach
The approach is based on a lattice model for a single step on a square grid with periodic boundary conditions in the step-parallel direction. A thin buffer layer with a fixed adatom density is placed a constant distance ahead of the step, mimicking the phase boundary that supplies atoms. The kinetic Monte Carlo algorithm tracks adatom diffusion and solidification/melting events at the step edge using Metropolis-type transition probabilities. The distance between the average step height and the buffer layer is kept constant by periodically shifting the buffer position.

The simulation is run under multiple parameter sets that vary the bond energy, buffer density, and buffer distance to systematically change the step stiffness and the steady-state step velocity. For each set, the early-stage characteristic wavelength is measured by counting the number of step branches crossing a horizontal line near the step origin, and the late-stage wavelength is measured further ahead. Both values are compared to the theoretical most unstable wavelength obtained from a linear stability analysis of the step evolution equation. The final artifact is a CSV table that collects these measured and computed quantities for all parameter sets.

### Lattice model, parameters and governing equations

**Units and fixed constants**  
The simulation uses a square lattice of spacing \(a = 1\).  Temperature is fixed so that \(k_{\mathrm{B}} T = 1\), the diffusion coefficient is \(D_{\mathrm{s}} = 1\), and the atomic area is \(\Omega = a^{2} = 1\).  The chemical potential gain by solidification is set to \(\phi = 3.0\) (in units of \(k_{\mathrm{B}} T\)).

**Step stiffness**  
For a step oriented along the [01] direction the step stiffness is given by

\[
\tilde{\beta}_{[01]} = \frac{2 k_{\mathrm{B}} T}{a} \sinh^{2}\!\left(\frac{\varepsilon}{2 k_{\mathrm{B}} T}\right)
\;=\; 2 \sinh^{2}\!\left(\frac{\varepsilon}{2}\right) \qquad (\text{with } a=1,\; k_{\mathrm{B}} T=1).
\]

\(\varepsilon\) is the bond energy per in‑plane neighbor.

**Equilibrium adatom density**  
The equilibrium adatom density at the step edge is

\[
c_{\mathrm{eq}}^{0} = \exp\!\left(-\frac{\phi}{k_{\mathrm{B}} T}\right)
= \exp(-3) \;\approx\; 0.0498.
\]

**Solidification and melting probabilities**  
When a solidification trial (placing an adatom adjacent to a step atom) or a melting trial (removing a step atom) is performed, the Metropolis‑type acceptance probabilities are

\[
p_{\pm} = \left[1 + \exp\!\left(\frac{\Delta E \mp \phi}{k_{\mathrm{B}} T}\right)\right]^{-1},
\]

where \(p_{+}\) applies to solidification and \(p_{-}\) to melting.  
The energy change \(\Delta E\) is the increase in step energy due to the change in the number of in‑plane (nearest‑neighbour) bonds:

\[
\Delta E = \varepsilon \times (\text{change in the number of occupied nearest‑neighbour sites of the step atom}).
\]

Concretely, on the square lattice each site has four nearest neighbours.
- For a **solidification** trial: let \(N_{\mathrm{before}}\) be the number of solid neighbours of the target empty site before the trial, and \(N_{\mathrm{after}}\) the number after inserting the new solid atom (the new atom itself does not count, but it may form bonds with already occupied neighbours). Then \(\Delta E = \varepsilon\,(N_{\mathrm{after}} - N_{\mathrm{before}})\).
- For a **melting** trial: the step atom to be removed currently has \(N_{\mathrm{before}}\) solid neighbours. After removal it will have none, so \(\Delta E = -\varepsilon\, N_{\mathrm{before}}\).

**Diffusion dynamics**  
Active atoms are adatoms (mobile) and step atoms (which can melt). In each KMC trial one active atom is chosen and:
- If it is an adatom, a diffusion attempt is made: a neighbouring site is chosen randomly with equal probability among the four directions; if the site is empty the adatom moves there.  After a diffusion move, if the adatom becomes adjacent to a step atom, a solidification trial is immediately performed on that adatom.
- If it is a step atom, a melting trial is performed.

The time increment for a diffusion trial is \(\Delta t = 1/(4 N_{\mathrm{g}})\), where \(N_{\mathrm{g}}\) is the number of adatoms in the system. This ensures a diffusion coefficient of unity.

**Adatom source (buffer layer)**  
A thin buffer layer of constant adatom density \(c_{0}\) is placed at a distance \(l\) in front of the **average** height of the step. The source is assumed to act only below the buffer line (the line itself is the buffer). To mimic the experimental situation, the buffer layer is shifted periodically so that the distance between the averaged step height and the buffer line remains constant at \(l\). The range \(0 < c_{0} < 1\) and \(l > 0\) are simulation parameters varied across runs.

**Steady step velocity**  
Under steady supply from the buffer, the straight step moves at velocity \(V_{0}\) given by

\[
V_{0} = -\frac{D_{\mathrm{s}}}{l}
        \ln\!\left(\frac{1 - \Omega c_{0}}{1 - \Omega c_{\mathrm{eq}}^{0}}\right)
     = -\frac{1}{l}
        \ln\!\left(\frac{1 - c_{0}}{1 - c_{\mathrm{eq}}^{0}}\right)
\qquad (\Omega = D_{\mathrm{s}} = 1).
\]

**Theoretical most unstable wavelength**  
Linear stability analysis of the step motion yields the wavelength of the fastest growing Fourier mode, \(\lambda_{\max}\). In our reduced units it simplifies to

\[
\lambda_{\max}
= 2\pi \sqrt{
    \frac{3\,\Omega^{2}\,\tilde{\beta}_{[01]}\,c_{\mathrm{eq}}^{0}\,
          (D_{\mathrm{s}} / V_{0})}
         {k_{\mathrm{B}} T \,(1 - \Omega c_{\mathrm{eq}}^{0})}
  }
= 2\pi \sqrt{
    \frac{3\,\tilde{\beta}_{[01]}\,c_{\mathrm{eq}}^{0}}
         {V_{0}\,(1 - c_{\mathrm{eq}}^{0})}
  }.
\]

This expression must be evaluated for each parameter set and compared with the simulated characteristic wavelengths.

**Simulation domain and initial condition**  
- System size in the step‑parallel direction: \(L_{x} = 1024\).  Periodic boundary conditions are applied in this direction.
- The step is initially straight (a horizontal line of solid atoms at some low height, e.g. \(y = 10\)).  Adatoms are initially placed according to the steady‑state density profile or simply filled around the buffer; the early transient is not critical because measurements are taken after some growth.
- The buffer layer is positioned at \(y = \text{avg\_step\_height} + l\) and is moved as the step advances to maintain this separation.

**Measurement of characteristic wavelength**  
- **Early stage**: When the **average** step height reaches a prescribed low value (e.g. \(y \approx 30\)), count the number \(N\) of distinct branches (step protrusions) that cross the horizontal line at that height. The characteristic wavelength is \(\lambda^{*}_{\mathrm{early}} = L_{x} / N\).  Average this quantity over **50 independent simulation runs** (each with a different random seed).
- **Late stage**: In a later phase, once the step has grown substantially further, choose a convenient horizontal line at a greater height and count the branches crossing it.  The late‑stage wavelength is \(\lambda^{*}_{\mathrm{late}} = L_{x} / N\) averaged over **10 independent runs**.

Each run uses the same parameter set \((ε/k_{\mathrm{B}}T,\; c_{0},\; l)\); the step stiffness \(\tilde{\beta}_{[01]}/k_{\mathrm{B}}T\) and steady velocity \(V_{0}\) can be computed from the formulas above.

---

## Reproduction target
Produce the file `/app/outputs/wavelength_results.csv` containing, for at least three distinct simulation parameter sets, the early-stage characteristic wavelength, the late-stage characteristic wavelength, and the theoretical most unstable wavelength λmax. The hidden verifier will check that the early wavelength is close to λmax (within a specified ratio), that the late wavelength is larger, and that the wavelength scales with the step stiffness and velocity as a power law. The precise target ranges and tolerances are part of the hidden scoring specification.

## Assets
This task requires only standard scientific Python libraries and no external datasets, models, or tools. The agent is expected to use NumPy and SciPy for numerical computation and data output; Matplotlib may be used for optional visualisation but is not required. All required resources can be installed from PyPI:

- `numpy`: numerical arrays and random number generation
- `scipy`: curve fitting / linear regression
- `matplotlib` (optional): plotting

## Workflow steps

### Step 1: KMC simulation and wavelength extraction
- Role: scored (load-bearing)
- Action: Implement a Kinetic Monte Carlo simulation of a single [01] step on a square lattice (periodic x-boundary, system width \(L_x = 1024\)).  Follow the model described in **Lattice model, parameters and governing equations** above: use \(k_B T = 1\), \(D_s = 1\), \(\Omega = 1\), \(\phi = 3.0\), the stiffness formula \(\tilde{\beta} = 2\sinh^2(\varepsilon/2)\), the probability formulas for solidification/melting, and the buffer layer maintained at constant distance \(l\) from the average step height.  Run simulations for at least three distinct parameter sets (vary \(\varepsilon/k_B T\), \(c_0\), \(l\)) to cover different step stiffnesses and velocities.  For each set, measure the early‑stage characteristic wavelength \(\lambda^*_{\mathrm{early}}\) (at a low average height, averaged over 50 independent runs) and the late‑stage wavelength \(\lambda^*_{\mathrm{late}}\) (at a substantially greater height, averaged over 10 runs).  For each parameter set compute the theoretical most‑unstable wavelength \(\lambda_{\max}\) using the formula given above.  Save all results in a CSV file.
- Output file: `/app/outputs/wavelength_results.csv`
- Format: csv
- Contract: parameter_set: string identifier; epsilon_kBT: float; c0: float; l: float; beta_tilde_kBT: float; V0: float; lambda_early: float; lambda_late: float; lambda_max: float. At least three rows (three distinct parameter sets).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/wavelength_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### wavelength_results.csv
- path: `/app/outputs/wavelength_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Artifact verifying that the simulated characteristic wavelengths satisfy the scaling relation λ* ∝ (β̃/V0)^{1/2} and that the early/late-stage ratios to λmax fall within the ranges reported in the paper.
- schema:
  - `type`: table
  - `required_columns`: `parameter_set`, `epsilon_kBT`, `c0`, `l`, `beta_tilde_kBT`, `V0`, `lambda_early`, `lambda_late`, `lambda_max`
  - `description`: Each row corresponds to one parameter set. Columns contain simulation conditions, the observed characteristic wavelengths (early and late stages), and the theoretical most unstable wavelength λmax.

Notes: The checker will verify internal consistency (λearly < λlate, recomputed λmax from the parameters), check ratio ranges, and perform a log-log regression to confirm the 1/2-power scaling.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "wavelength_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter_set",
          "epsilon_kBT",
          "c0",
          "l",
          "beta_tilde_kBT",
          "V0",
          "lambda_early",
          "lambda_late",
          "lambda_max"
        ],
        "description": "Each row corresponds to one parameter set. Columns contain simulation conditions, the observed characteristic wavelengths (early and late stages), and the theoretical most unstable wavelength λmax."
      },
      "description": "Artifact verifying that the simulated characteristic wavelengths satisfy the scaling relation λ* ∝ (β̃/V0)^{1/2} and that the early/late-stage ratios to λmax fall within the ranges reported in the paper."
    }
  ],
  "notes": "The checker will verify internal consistency (λearly < λlate, recomputed λmax from the parameters), check ratio ranges, and perform a log-log regression to confirm the 1/2-power scaling."
}
```

## How you are scored
A hidden verifier reads your submitted `wavelength_results.csv` and performs several checks to compute a reward between 0 and 1. The verifier first recomputes λmax from each row's reported step stiffness and velocity to confirm internal consistency. It then verifies that the early and late wavelengths satisfy certain expected inequalities and that the ratio λearly/λmax and λlate/λmax fall within acceptable ranges (as determined by the paper's stability analysis). If three or more distinct parameter sets are provided, the verifier performs a log-log linear regression between the early wavelength and the quantity (β̃/V0) and checks that the fitted slope lies in a predetermined interval. The largest portion of the reward is tied to the ratio checks and the scaling exponent; structural checks such as column presence carry only minimal weight.