# Terahertz Waveguide Eigenmode Analysis and Loss Calculation

## Problem background
Silicon-based terahertz quantum cascade lasers require efficient waveguides that tightly confine the optical mode within a thin active region while minimizing propagation losses. This work explores a surface-mode waveguide consisting of a periodic silver-coated grating on top of a Si–SiGe multilayer heterostructure. The waveguide is characterized by two parameters: the equivalent propagation loss, which reflects how strongly the mode decays along the guide, and the modal overlap with the active region, which indicates what fraction of the field energy lies in the gain medium. Your task is to compute these two numbers for a specified grating geometry and layer stack.

## Approach
The method uses rigorous coupled-wave analysis (RCWA) in the form of a plane-wave expansion eigenmode solver to find the surface Bloch mode at the band edge (wavevector k_x = π/Λ, where Λ is the grating period). The structure is assumed translation-invariant along the out-of-plane direction, so a two-dimensional analysis suffices. The permittivity of silver is modeled with a Drude formula using room-temperature parameters (resistivity and scattering time), while the doped SiGe layers use parameters from the literature. After solving for the complex eigenfrequency and the field profiles, the equivalent propagation loss is obtained from the imaginary part of the frequency via α = 4π n_eff / (Λ Im(f_n)), and the modal overlap is computed as the ratio of the squared |E_y| field integrated over the active region to the total integrated field energy. Only one grating depth (the “shallow” condition) is required; you do not need to sweep multiple depths.

## Reproduction target
Run the RCWA simulation for the structure described below and compute the key figures:
- Grating period Λ = 14 μm, filling factor 50%, etched depth d = 0.56 μm.
- Active region thickness h_AR = 8 μm (the exact layer stack is specified in the problem background).
- Material permittivities as described in the approach.
Your output must be a single JSON file containing the equivalent propagation loss α (in cm⁻¹) and the modal overlap Γ (dimensionless). Report these as the fields "alpha_cm1" and "gamma". The hidden verifier will compare your numbers to the reference values known to the verifier.

## Assets

- Open‑source RCWA eigenmode solver (e.g., S4, pyS4, or equivalent): https://github.com/nicolaef/pyS4

## Workflow steps

### Step 1: Run RCWA eigenmode simulation
- Role: process
- Action: Using the described multilayer Si‑SiGe heterostructure geometry and the material permittivities (silver from the Drude model with τ=40 fs, ρ=1.51 Ω·cm; doped SiGe from literature parameters with τ≈38 fs, m*=0.37m₀), run an RCWA eigenmode solver to compute the surface Bloch mode at the band edge (k_x = π/Λ). Record the complex eigenfrequency (real and imaginary parts), the effective index n_eff, and the electric field components E_y and E_x on the spatial grid.
- Evidence: `/app/outputs/eigenmode_data.h5`

### Step 2: Compute propagation loss and modal overlap
- Role: scored (load-bearing)
- Action: From the eigenmode data (complex eigenfrequency, effective index, and field profiles) compute the equivalent propagation loss α (cm⁻¹) via α = 4π n_eff / (Λ Im(f_n)) and the modal overlap Γ = ∬_AR |E_y|² dx dy / ∬ (|E_y|²+|E_x|²) dx dy, where Λ = 14 μm and AR denotes the active region (8 μm thick). Report both values in a single JSON file.
- Output file: `/app/outputs/step_01_shallow_grating_results.json`
- Format: json
- Contract: {"alpha_cm1": float, "gamma": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_shallow_grating_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_shallow_grating_results.json
- path: `/app/outputs/step_01_shallow_grating_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed equivalent propagation loss and modal overlap for the specified shallow‑grating structure (h_AR = 8 μm, d = 0.56 μm, Λ = 14 μm, filling factor 50%).
- schema:
  - `type`: object
  - `required`:
    - `alpha_cm1`: number
    - `gamma`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_shallow_grating_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "alpha_cm1": "number",
          "gamma": "number"
        }
      },
      "description": "Computed equivalent propagation loss and modal overlap for the specified shallow‑grating structure (h_AR = 8 μm, d = 0.56 μm, Λ = 14 μm, filling factor 50%)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier that reads the output file step_01_shallow_grating_results.json. It extracts the two numeric fields, compares them to reference thresholds derived from the original study, and awards a score. The score is monotonic in the quality of your result: for the propagation loss, meeting or beating a pass threshold earns full credit; for the modal overlap, results within an acceptable window earn credit. Additional minor weight may be given for the presence and correct format of intermediate evidence files. The exact thresholds are not provided to you; you must produce physically correct results by faithfully executing the simulation and post-processing steps described in the workflow.
