# Optimization of Plasmonic Hybrid Laser via Eigenmode Simulations

## Problem background
Hybrid III-V/silicon evanescent lasers are a promising platform for silicon photonics, but when the silicon waveguide is scaled to sub-micron dimensions the optical mode loses confinement and the device can no longer lase. To overcome this, a buried periodic metal grating is introduced between the III‑V gain region and the silicon waveguide. The grating supports plasmonic effects that can reshape the optical field distribution, potentially enabling a nanoscale hybrid laser. The central challenge is to find a combination of structural parameters — ridge height, grating depth, grating width, and grating period — that yields single‑mode operation and a low lasing threshold gain.

## Approach
We model the hybrid structure using a three‑dimensional eigenmode electromagnetic simulation at a wavelength of 1.55 μm. The simulation cell includes the full layer stack with the embedded silicon ridge waveguide, the Al grating, and the III‑V quantum‑well gain region. Periodic boundary conditions are applied along the grating direction, while scattering boundary conditions are used in the transverse directions. The effective index (real and imaginary parts) is obtained from the eigenmode calculation, and the electric field distribution is used to compute the power confinement factors in the silicon waveguide and in the quantum wells by volume integration of |E|². The threshold gain is then calculated from the standard formula that combines the mirror loss (due to dielectric‑air Fresnel reflections from a 30 μm‑long cavity) with the imaginary part of the effective index and the quantum‑well confinement factor.

The optimization proceeds in three stages. First, the ridge height and grating depth are swept to identify a height that supports a single transverse mode while balancing the optical energy between the waveguide and the quantum wells. Next, the grating depth and width are varied at that fixed ridge height to find the cross‑sectional dimensions that minimize threshold gain and avoid the metallic short‑circuit regime where the grating touches the bottom metal layer. Finally, the grating period is swept, and the period that offers the best compromise between low threshold gain and fabrication tolerance is selected. The final set of optimized parameters, together with the corresponding threshold gain and quantum‑well confinement factor, constitute the main result of the workflow.

## Reproduction target
Implement the eigenmode simulation of the described plasmonic hybrid laser structure at λ = 1.55 μm using an open‑source electromagnetic solver capable of handling complex permittivities (e.g., MEEP or a custom FEM implementation). Use the material refractive indices given in the workflow. Execute the multi‑stage parameter sweeps exactly as described: (i) sweep ridge height H and grating depth h with w = 0.1 μm, p = 0.3 μm; select an optimal H that supports a single guided mode; (ii) sweep h and width w at the chosen H; select optimal h and w based on low threshold gain and balanced energy distribution; (iii) sweep period p over 0.1–3 μm at those fixed H, h, w; select a final period that balances threshold gain and tolerance. For every parameter combination, compute and record the complex effective index and the electric field distribution. Use these to obtain the power confinement factors Γ_WG and Γ_QW and the threshold gain g_th, employing the standard threshold gain formula with cavity length ℓ = 30 μm and mirror reflectivity R = ((n_eff(r)–1)/(n_eff(r)+1))². The scored deliverable is a JSON file containing the final optimized structural parameters (ridge height, grating depth, grating width, grating period, all in μm), the threshold gain per μm, and the quantum‑well power confinement factor (as a percentage).

## Assets

- Electromagnetic eigenmode solver: meep

## Workflow steps

### Step 1: Simulation model setup
- Role: process
- Action: Define the 3D unit-cell geometry (Fig. 3 of the paper) with the given layer stack (InP substrate, SCH, QW, contact layer, Si ridge waveguide, SiO₂ cladding, buried Al bottom layer, and Al grating). Use the material refractive indices (real part for all materials except Al, which has a complex index) from the known table. Set up periodic boundary conditions along the grating direction and scattering boundary conditions in the transverse directions. The operating wavelength is 1.55 μm, and the device cavity length is ℓ=30 μm with mirror loss from dielectric‑air Fresnel reflection.
- Evidence: `/app/outputs/simulation_setup_report.txt`

### Step 2: Eigenmode sweep for ridge height H and grating depth h
- Role: process
- Action: With grating width w=0.1 μm and period p=0.3 μm fixed, perform eigenmode simulations over ridge height H (range 0.05–1.2 μm) and grating depth h (values 50 nm, 100 nm, 200 nm). For each combination compute the complex effective index n_eff (real and imaginary parts) and save the full electric field distribution (required for confinement factor integration).
- Evidence: `/app/outputs/sweep_H_h_raw.csv`

### Step 3: Select optimal ridge height H
- Role: process
- Action: From the H‑h sweep results, compute the power confinement factors Γ_WG (silicon waveguide) and Γ_QW (quantum wells) by volume integration of |E|² over the respective regions. Compute the threshold gain g_th using the given formula with the real and imaginary parts of n_eff, cavity length ℓ=30 μm, and mirror reflectivity R = ((n_eff(r)-1)/(n_eff(r)+1))². Inspect the energy‑density cross‑sections and the number of transverse modes. Select the ridge height H that supports a single guided mode while providing a balanced energy distribution between waveguide and quantum‑well regions; avoid heights that allow multiple transverse hybrid SPP modes.
- Evidence: `/app/outputs/H_optimization_report.txt`

### Step 4: Eigenmode sweep for grating depth h and width w
- Role: process
- Action: Fix the ridge height to the optimal H determined in the previous step and the period p=0.3 μm. Sweep grating depth h (range 0–0.55 μm) and width w (values 0.1, 0.2, 0.3 μm). For each (h,w) compute the complex effective index and save the electric field distribution.
- Evidence: `/app/outputs/sweep_h_w_raw.csv`

### Step 5: Select optimal grating depth h and width w
- Role: process
- Action: From the h‑w sweep, compute the confinement factors Γ_WG, Γ_QW and threshold gain g_th for each configuration. Examine energy‑density maps for different grating depths. Select the grating depth h and width w that yield low threshold gain and an equally distributed energy between the QW and waveguide regions, while avoiding the metallic short‑circuit regime where the grating touches the bottom Al layer.
- Evidence: `/app/outputs/hw_optimization_report.txt`

### Step 6: Eigenmode sweep for grating period p
- Role: process
- Action: With the previously determined optimal H, h, and w, sweep the grating period p over the range 0.1 μm to 3 μm. For each period compute the effective indices, field distributions, confinement factors, and threshold gain.
- Evidence: `/app/outputs/sweep_p_raw.csv`

### Step 7: Select optimal period and report final design
- Role: scored (load-bearing)
- Action: From the period sweep, select the optimal period p that gives a favorable trade‑off between low threshold gain and fabrication tolerance (the sub‑micron regime is acceptable as one possible optimum). For the complete optimized design (H, h, w, p) compute the final threshold gain g_th and the quantum‑well power confinement factor Γ_QW. Write the optimized structural parameters (ridge height, grating depth, grating width, period) and the two metrics (threshold gain, QW confinement factor) to optimal_parameters.json.
- Output file: `/app/outputs/optimal_parameters.json`
- Format: json
- Contract: {"ridge_height_um": float in micrometers, "grating_depth_um": float in micrometers, "grating_width_um": float in micrometers, "period_um": float in micrometers, "threshold_gain_per_um": float (per μm), "Qw_confinement_factor": float (percentage, e.g., 16.3 for 16.3%)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimal_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_parameters.json
- path: `/app/outputs/optimal_parameters.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The fully optimized design parameters and the corresponding threshold gain and QW confinement factor, obtained after running the complete eigenmode sweep pipeline and selecting the best configuration based on physical considerations.
- schema:
  - `type`: object
  - `required`: `ridge_height_um`, `grating_depth_um`, `grating_width_um`, `period_um`, `threshold_gain_per_um`, `Qw_confinement_factor`
  - `properties`:
    - `ridge_height_um`:
      - `description`: Optimized ridge height in micrometers.
    - `grating_depth_um`:
      - `description`: Optimized grating depth in micrometers.
    - `grating_width_um`:
      - `description`: Optimized grating width in micrometers.
    - `period_um`:
      - `description`: Optimized grating period in micrometers.
    - `threshold_gain_per_um`:
      - `description`: Final threshold gain in per micrometer (lower is better).
    - `Qw_confinement_factor`:
      - `description`: Quantum‑well power confinement factor expressed as a percentage (e.g., 16.3 means 16.3%).

Notes: The checker will verify each structural parameter against the paper’s hidden gold with an absolute tolerance, and evaluate threshold gain with a threshold‑or‑better policy (lower gain is better; meeting or beating the reference earns full credit). The confinement factor is compared with an absolute tolerance. The agent must have genuinely performed the sweeps; the final result cannot be guessed without running the simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "ridge_height_um",
          "grating_depth_um",
          "grating_width_um",
          "period_um",
          "threshold_gain_per_um",
          "Qw_confinement_factor"
        ],
        "properties": {
          "ridge_height_um": {
            "description": "Optimized ridge height in micrometers."
          },
          "grating_depth_um": {
            "description": "Optimized grating depth in micrometers."
          },
          "grating_width_um": {
            "description": "Optimized grating width in micrometers."
          },
          "period_um": {
            "description": "Optimized grating period in micrometers."
          },
          "threshold_gain_per_um": {
            "description": "Final threshold gain in per micrometer (lower is better)."
          },
          "Qw_confinement_factor": {
            "description": "Quantum‑well power confinement factor expressed as a percentage (e.g., 16.3 means 16.3%)."
          }
        }
      },
      "description": "The fully optimized design parameters and the corresponding threshold gain and QW confinement factor, obtained after running the complete eigenmode sweep pipeline and selecting the best configuration based on physical considerations."
    }
  ],
  "notes": "The checker will verify each structural parameter against the paper’s hidden gold with an absolute tolerance, and evaluate threshold gain with a threshold‑or‑better policy (lower gain is better; meeting or beating the reference earns full credit). The confinement factor is compared with an absolute tolerance. The agent must have genuinely performed the sweeps; the final result cannot be guessed without running the simulations."
}
```

## How you are scored
Your work is evaluated by a hidden verifier that compares the numerical values in `optimal_parameters.json` to a set of hidden reference results. The verifier checks each structural parameter (ridge height, grating depth, grating width, grating period) against the reference using appropriate tolerances that account for numerical differences between solvers. The threshold gain is assessed with a threshold‑or‑better policy: gains lower than or equal to the reference earn full credit, while higher gains receive partial or no credit. The quantum‑well confinement factor is compared to the reference value with an allowed deviation. The verifier combines these checks into an overall reward score between 0 and 1. Submitting evidence of intermediate steps (the raw sweep data, optimization reports) is required as part of the pipeline, but the reward is determined solely from the correctness of the final optimized parameters and metrics. Reporting the paper’s numbers without actually running the simulation pipeline will not produce a faithful reproduction and will likely fail the tolerance checks.
