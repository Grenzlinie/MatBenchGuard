# KMC Simulation of Polymer Surface Transport with In-Plane Diffusion

## Problem background
Polymer dynamics at solid/liquid interfaces involve intermittent motion combining desorption-mediated long “flights” and periods of apparent immobility. Previous studies suggested that these apparently immobile periods might actually be slow in-plane (2D) diffusion. To test this hypothesis, single-molecule tracking experiments compared polymer surface transport on chemically homogeneous surfaces against nanopatterned surfaces where polymers are confined within isolated domains, thereby suppressing any continuous in-plane diffusion. The step-size distributions (probability of displacement in a fixed time interval) on homogeneous surfaces showed an additional diffusive mode that was absent on the patterned surfaces, consistent with a slow 2D diffusion process. A kinetic Monte Carlo continuous-time-random-walk model that incorporates both desorption-mediated flights and Gaussian in-plane diffusion was proposed to reproduce the observations on both surface types. The central computational question is: what value of the in-plane diffusion coefficient D₂D best accounts for the experimentally measured step-size distributions across these two contrasting surface chemistries? The answer requires running a stochastic simulation of the surface transport process and calibrating D₂D against the provided experimental data.

## Approach
The approach is to implement a 2D lattice kinetic Monte Carlo (KMC) continuous-time random walk (CTRW) simulation that faithfully captures the essential physics of polymer surface transport. The simulation environment consists of a square lattice of size 100 × 100 μm² with site size 0.01 × 0.01 μm². Two surface configurations are used: (1) a homogeneous polystyrene (PS) surface where every site is designated as PS, and (2) a PS-hexagonal surface where non-overlapping circular PS domains are randomly placed to achieve a total PS coverage of 32 %, with the remainder designated as PMMA (polymethyl methacrylate). The CTRW model alternates waiting times and desorption-mediated flights. Waiting times are drawn from a power-law distribution ψ(τ) ~ τ⁻ᵝ (with exponent values specific to each surface). Flight lengths are drawn from a power-law distribution f(r) ~ r⁻β (with a universal exponent) and are realized as on-lattice random walks of an appropriate number of steps; any flight that terminates on a non-PS site is rejected and a new flight is sampled until the landing site is PS. During each waiting period, a fraction of the time steps are immobile while the remainder undergo Gaussian in-plane diffusion characterized by a displacement variance that depends on the diffusion coefficient D₂D and the waiting-time duration. The simulation is run for a range of candidate D₂D values on both surface types, accumulating sufficient statistics to construct step-size histograms G(Δx, Δt = 0.1 s). The simulated histograms are compared to provided experimental calibration data (digitized step-size distributions for the two surfaces) using a sum-of-squared-differences error metric, and the D₂D value that minimizes the total error is selected as the best-fit coefficient. The final outputs are the simulated histograms for the optimal D₂D and the best-fit D₂D value itself.

## Reproduction target
The objective is to produce three artifacts by running the KMC CTRW simulation and comparing against the provided experimental step-size distributions: (1) the step-size histogram for the homogeneous PS surface (step_size_homogeneous_ps.csv), containing columns displacement_nm and probability; (2) the step-size histogram for the PS-hexagonal surface (step_size_ps_hexagonal.csv), also with displacement_nm and probability; and (3) the selected in-plane diffusion coefficient D₂D (best_fit_d2d.txt) in units of μm²/s. The histograms must be generated from the agent’s own stochastic simulations; the calibration data are for guiding the selection of D₂D only and must not be copied as the final outputs. The final histograms should be normalized so that the probabilities sum to 1. The binning scheme, simulation time-step, and number of Monte Carlo steps are at the agent’s discretion, provided the resulting distributions resolve the displacement range relevant to the experimental observations (up to several hundred nanometres).

## Assets

- Experimental step-size distributions for dextran on homogeneous PS and PS-hexagonal surfaces (digitized from paper Figure 3)

## Workflow steps

### Step 1: Construct 2D lattice representation of surfaces
- Role: process
- Action: Create a 100×100 μm² square lattice with 0.01×0.01 μm² sites. For the homogeneous PS surface, label every site as PS (type 1). For the PS-hexagonal surface, randomly place non-overlapping circular PS domains to achieve a surface fraction of 32%, labeling PS sites as 1 and PMMA sites as 0. Save the lattice arrays as NumPy arrays for later use.
- Evidence: `/app/outputs/lattice_homogeneous.npy, lattice_ps_hex.npy (optional)`

### Step 2: Run KMC simulations for candidate D2D values
- Role: process
- Action: Implement the full CTRW Kinetic Monte Carlo algorithm on the built lattices. Use waiting-time exponents α=1.20 (homogeneous PS) and α=1.18 (PS-hexagonal), flight-length exponent β=1.30, and 40% immobile waiting periods with 60% undergoing Gaussian in-plane diffusion. For D2D values from 0.15 to 0.25 μm²/s (step 0.01), run simulations on both surfaces to accumulate enough statistics for accurate step-size histograms. Store the candidate histograms for each D2D and surface.
- Evidence: `/app/outputs/ directory with CSV files (e.g., step_size_homogeneous_d2d_0.20.csv)`

### Step 3: Select best D2D value
- Role: scored
- Action: For each candidate D2D, compute the sum of squared differences between the simulated step-size histograms (for both surfaces) and the provided experimental step-size distributions. Select the D2D value that minimizes the total error and write it to best_fit_d2d.txt.
- Output file: `/app/outputs/best_fit_d2d.txt`
- Format: txt
- Contract: Single floating-point number.
- Scoring: scored by hidden verifier

### Step 4: Write step-size histogram for homogeneous PS
- Role: scored (load-bearing)
- Action: Write the step-size histogram (displacement bins and probability) for the best D2D on the homogeneous PS surface to step_size_homogeneous_ps.csv. Bins should correspond to the typical displacement range and normalized so that probabilities sum to 1.
- Output file: `/app/outputs/step_size_homogeneous_ps.csv`
- Format: csv
- Contract: Columns: displacement_nm (float, center of displacement bin), probability (float, normalized frequency).
- Scoring: scored by hidden verifier

### Step 5: Write step-size histogram for PS-hexagonal
- Role: scored (load-bearing)
- Action: Write the step-size histogram (displacement bins and probability) for the best D2D on the PS-hexagonal surface to step_size_ps_hexagonal.csv.
- Output file: `/app/outputs/step_size_ps_hexagonal.csv`
- Format: csv
- Contract: Columns: displacement_nm (float), probability (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/best_fit_d2d.txt`
- `/app/outputs/step_size_homogeneous_ps.csv`
- `/app/outputs/step_size_ps_hexagonal.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### best_fit_d2d.txt
- path: `/app/outputs/best_fit_d2d.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimal in-plane diffusion coefficient selected by the agent.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing D2D in μm²/s.

### step_size_homogeneous_ps.csv
- path: `/app/outputs/step_size_homogeneous_ps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated step-size histogram for the homogeneous PS surface, used to verify the model's reproduction of the experimental in-plane diffusion mode.
- schema:
  - `type`: table
  - `required_columns`: `displacement_nm`, `probability`
  - `units`:
    - `displacement_nm`: nm
    - `probability`: dimensionless

### step_size_ps_hexagonal.csv
- path: `/app/outputs/step_size_ps_hexagonal.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated step-size histogram for the PS-hexagonal surface, used to verify the model's reproduction of the flight-dominated transport without in-plane diffusion.
- schema:
  - `type`: table
  - `required_columns`: `displacement_nm`, `probability`
  - `units`:
    - `displacement_nm`: nm
    - `probability`: dimensionless

Notes: The experimental step-size distributions are provided for calibration only; the graded histograms must be generated by the agent's own KMC simulation. The hidden gold references are digitized from the paper's Figure 3 simulation curves for the same conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "best_fit_d2d.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing D2D in μm²/s."
      },
      "description": "Optimal in-plane diffusion coefficient selected by the agent."
    },
    {
      "file": "step_size_homogeneous_ps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement_nm",
          "probability"
        ],
        "units": {
          "displacement_nm": "nm",
          "probability": "dimensionless"
        }
      },
      "description": "Simulated step-size histogram for the homogeneous PS surface, used to verify the model's reproduction of the experimental in-plane diffusion mode."
    },
    {
      "file": "step_size_ps_hexagonal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement_nm",
          "probability"
        ],
        "units": {
          "displacement_nm": "nm",
          "probability": "dimensionless"
        }
      },
      "description": "Simulated step-size histogram for the PS-hexagonal surface, used to verify the model's reproduction of the flight-dominated transport without in-plane diffusion."
    }
  ],
  "notes": "The experimental step-size distributions are provided for calibration only; the graded histograms must be generated by the agent's own KMC simulation. The hidden gold references are digitized from the paper's Figure 3 simulation curves for the same conditions."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that independently compares them against reference data. The verifier checks the reported D₂D value against a gold standard within a tolerance that accounts for implementation-dependent variation. The step-size histograms are compared bin-by-bin to reference distributions using a relative error metric; the closer your simulated histogram is to the expected distribution, the higher the score. The overall reward is a weighted sum of the scores for the three outputs, with the histograms carrying the largest weight because they are load-bearing evidence that the KMC simulation was correctly executed. Importantly, simply writing down a number without actually performing the simulations will not pass, because the verifier examines the full histogram shapes and the internal consistency between the simulated histograms and the D₂D value. The exact reference values, tolerances, and weights are not disclosed to prevent cheating.
