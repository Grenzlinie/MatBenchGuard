# GPR-Accelerated Dimer Saddle Point Search for Solid-State Diffusion

## Problem background
Accurate prediction of diffusion coefficients in solid materials requires knowledge of the energy barrier and the transition state for atomic jumps. Saddle point search methods, such as the dimer algorithm, are powerful but computationally demanding when combined with density functional theory (DFT). This work develops a method to accelerate the dimer saddle point search by employing a Gaussian process regression (GPR) surrogate model to predict forces and energies, thereby reducing the number of expensive DFT evaluations. The method is demonstrated on two solid‑state diffusion problems: vacancy‑mediated self‑diffusion in body‑centred cubic (bcc) molybdenum and sulfur diffusion in hexagonal molybdenum disulfide (MoS2).

## Approach
The core idea is an iterative feedback loop between a standard dimer algorithm and a GPR surrogate. Starting from an interpolated guess for the saddle point, a small number of DFT calculations are performed to train a multi‑task Gaussian process that simultaneously predicts the potential energy and all atomic force components. The GPR uses an inverse‑distance covariance function that only considers atom pairs involving the diffusing atom within a specified active radius, thereby reducing the dimensionality of the high‑dimensional atomic configuration space. Once trained, the GPR replaces DFT during the rotation and translation steps of the dimer. To prevent overfitting to the dimer path, a translation‑hop sampling strategy is employed: after a fixed number of translation steps, the GPR is retrained using all DFT data accumulated up to that point. The cycle repeats until the GPR‑predicted maximum force falls below a convergence threshold. The method is applied to vacancy‑mediated self‑diffusion in a 3×3×3 bcc Mo supercell and to sulfur vacancy diffusion in a 2×2×2 hexagonal MoS2 supercell. All DFT calculations use the PBE functional via an open‑source DFT code (GPAW). The GPR is implemented with GPyTorch using multi‑task learning with a rank‑1 task similarity matrix.

## Reproduction target
Implement the GPR‑accelerated dimer method and apply it to two systems: (1) a monovacancy hop in bcc Mo (3×3×3 supercell, 54 atoms) and (2) a sulfur vacancy hop in hexagonal MoS2 (2×2×2 supercell, 48 atoms). Use GPAW with the PBE functional for all DFT calculations. Build the initial and final vacancy configurations, relax them, prepare an interpolated guess, collect initial training data from a short DFT‑dimer run, train the multi‑task GPR surrogate, run the GPR‑dimer with translation‑hop sampling until convergence (maximum GPR‑predicted force below 0.01 eV/Å), and finally compute the migration barrier as the DFT energy difference between the final saddle point configuration and the initial relaxed minimum. Record the total number of DFT evaluations performed during the entire workflow. Report the results in /app/outputs/results.json with the keys `mo_barrier` (eV), `mos2_barrier` (eV), `mo_dft_calls` (integer), `mos2_dft_calls` (integer).

## Assets

- Atomic Simulation Environment (ASE): ase
- GPAW (open‑source DFT with PBE functional): https://gitlab.com/gpaw/gpaw
- GPyTorch (Gaussian process library): gpytorch
- NumPy: numpy
- Crystallographic data for bcc Mo and hexagonal MoS2

## Workflow steps

### Step 1: Prepare initial and final reference states
- Role: process
- Action: Build 3×3×3 bcc Mo and 2×2×2 hexagonal MoS2 supercells using standard lattice constants, introduce single vacancies, and relax the structures with GPAW (PBE) to obtain local minimum configurations and energies. Also create the final state (hopped vacancy) for each system.
- Evidence: `/app/outputs/relaxed_structures.xyz`

### Step 2: Generate initial saddle point guess
- Role: process
- Action: For each system, perform linear interpolation (3/4 initial and 1/4 final) between the relaxed initial and final configurations to produce the initial dimer input configuration.
- Evidence: `/app/outputs/guess_configurations.xyz`

### Step 3: Initial DFT-dimer training data collection
- Role: process
- Action: Run a standard DFT‑dimer with GPAW from the interpolated configuration for 3 translation steps, saving the atomic configurations, DFT energies, and force components as training data.
- Evidence: `/app/outputs/training_data.npz`

### Step 4: Train multi-task GPR surrogate model
- Role: process
- Action: Implement the inverse‑distance covariance function with active regions (active radius 3 Å for Mo, 5 Å for MoS2) and train a multi‑task Gaussian process (using GPyTorch) to predict energy and forces simultaneously. Use the data from step_03 and optimize hyperparameters via marginal likelihood maximization.
- Evidence: `/app/outputs/gpr_model.pt`

### Step 5: GPR-accelerated dimer saddle point search
- Role: process
- Action: Run the GPR‑guided dimer algorithm for both systems. Use translation‑hop sampling (nh=10 translation steps between DFT re‑evaluations). During rotation and translation, use GPR‑predicted forces/energies. Retrain the GPR after each new DFT evaluation using all preceding DFT‑sampled configurations. Terminate when maximum GPR‑predicted force falls below 0.01 eV/Å. Record the total number of DFT evaluations performed.
- Evidence: `/app/outputs/dimer_trajectory.txt`

### Step 6: Compute migration barriers and DFT cost
- Role: scored (load-bearing)
- Action: Perform DFT single‑point calculations (GPAW) on the final saddle point configurations from step_05 and on the initial local minimum configurations from step_01 for both systems. Compute the energy difference as the migration barrier. Report the barriers (eV) and the total number of DFT evaluations used throughout the pipeline.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"mo_barrier": float, "mos2_barrier": float, "mo_dft_calls": int, "mos2_dft_calls": int}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the migration barriers and DFT call counts for both systems.
- schema:
  - `type`: object
  - `required`: `mo_barrier`, `mos2_barrier`, `mo_dft_calls`, `mos2_dft_calls`
  - `properties`:
    - `mo_barrier`:
      - `type`: number
      - `description`: Migration energy barrier for bcc Mo in eV
    - `mos2_barrier`:
      - `type`: number
      - `description`: Migration energy barrier for MoS2 in eV
    - `mo_dft_calls`:
      - `type`: integer
      - `description`: Total number of DFT calculations for Mo
    - `mos2_dft_calls`:
      - `type`: integer
      - `description`: Total number of DFT calculations for MoS2

Notes: The hidden checker compares the reported barriers to the paper-reported values within ±0.15 eV tolerance and compares DFT call counts within ±10% relative difference. The exact tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "mo_barrier",
          "mos2_barrier",
          "mo_dft_calls",
          "mos2_dft_calls"
        ],
        "properties": {
          "mo_barrier": {
            "type": "number",
            "description": "Migration energy barrier for bcc Mo in eV"
          },
          "mos2_barrier": {
            "type": "number",
            "description": "Migration energy barrier for MoS2 in eV"
          },
          "mo_dft_calls": {
            "type": "integer",
            "description": "Total number of DFT calculations for Mo"
          },
          "mos2_dft_calls": {
            "type": "integer",
            "description": "Total number of DFT calculations for MoS2"
          }
        }
      },
      "description": "Scored artifact containing the migration barriers and DFT call counts for both systems."
    }
  ],
  "notes": "The hidden checker compares the reported barriers to the paper-reported values within ±0.15 eV tolerance and compares DFT call counts within ±10% relative difference. The exact tolerances are hidden."
}
```

## How you are scored
Your results.json is evaluated by a hidden verifier. The verifier compares the reported migration barriers (`mo_barrier`, `mos2_barrier`) to hidden reference values within an acceptable tolerance range, and similarly compares the reported DFT call counts (`mo_dft_calls`, `mos2_dft_calls`) to hidden reference values within a tolerance. The overall score is a weighted combination of barrier accuracy and DFT‑call accuracy, with larger weight on the barriers. Simply reporting numbers does not guarantee a high score; only results that fall within the expected ranges will earn credit. The verifier does not disclose the tolerances or the reference values.
