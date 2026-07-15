# Monte Carlo Electron Transport and Energy Deposition Simulation

## Problem background
High-energy electron beams (10–50 keV) are widely used in manufacturing for surface hardening, cutting, and welding. When a beam impinges on a solid target, electrons undergo elastic scattering with atomic nuclei and inelastic energy loss due to interactions with orbital electrons, depositing energy as heat in the subsurface region. Accurate knowledge of the spatial profile of deposited heat and the fraction of beam power reflected from the surface is critical for controlling the treatment depth and efficiency. This analysis focuses on the difference between the electron density distribution and the volumetric heat-generation density, and aims to quantify the associated penetration depths and reflection ratios for a realistic beam and material system.

## Approach
A Monte Carlo simulation tracks individual electrons through a solid using a kinetic model. Elastic scattering is modeled with a Rutherford-type differential cross-section; an angular cutoff excludes very small-angle deflections. Inelastic energy loss follows the relativistic Bethe stopping-power formula, which gives the continuous energy-loss rate as a function of the instantaneous electron energy. The electron trajectory is discretized into path segments; at each step the scattering angle is sampled from the differential cross-section, the energy is decremented according to the stopping power, and the deposited energy is accumulated on a computational mesh. The simulation runs until the fraction of moving electrons falls below a predefined threshold. From the accumulated spatial distributions, the depth profiles of electron density and heat generation are obtained. The derived output quantities are: power reflection ratio (reflected beam power over incident power), beam reflection ratio (number of reflected electrons over total incident electrons), electron penetration depth (depth at which the depth-averaged electron density decays to 1/e of its maximum), heat penetration depth (depth at which the depth-averaged heat-generation density decays to 1/e of its maximum), and the ratio of the two penetration depths. The simulation is performed for a silver target under a monoenergetic 30 keV electron beam at normal incidence.

## Reproduction target
Implement the Monte Carlo electron transport and energy-deposition simulation for a silver target (atomic number Z=47, density ρ_m=10 490 kg/m³, excitation potential J=422 eV) irradiated by a monoenergetic 30 keV electron beam with a rectangular cross-section (width 6 mm, length 50 mm) at normal incidence (α=0°). Use the Rutherford-type elastic scattering cross-section (cutoff angle 5°), the relativistic Bethe stopping power with its correction function, and terminate the ensemble when the fraction of moving electrons drops below 1e-4. From the accumulated volumetric heat-generation and electron-number densities, compute and report: (1) power reflection ratio, (2) beam reflection ratio, (3) electron penetration depth (µm), (4) heat penetration depth (µm), and (5) the ratio of heat to electron penetration depths. Store the derived quantities in /app/outputs/results.json following the output contract.

## Assets

- Standard scientific Python packages (numpy, scipy, etc.)

## Workflow steps

### Step 1: Run Monte Carlo electron transport and energy deposition simulation
- Role: process
- Action: Implement and run the Monte Carlo electron transport and energy deposition simulation for a silver target (atomic number Z=47, density ρ_m=10490 kg/m³, excitation potential J=422 eV). Use a monoenergetic 30 keV electron beam with a rectangular cross-section (width 6 mm, length 50 mm) at normal incidence (α=0°). Model elastic scattering with the Rutherford-type differential cross section (cutoff angle χ_m=5°), inelastic energy loss with the relativistic Bethe stopping power including the correction function f, path segmentation for inelastic loss integration, and ensemble termination when the fraction of moving electrons falls below ε=1e-4. Accumulate volumetric heat-generation density and electron density on a computational mesh. Save the spatial distributions to /app/outputs/simulation_data.npz.
- Evidence: `/app/outputs/simulation_data.npz`

### Step 2: Compute derived quantities from simulation
- Role: scored
- Action: From the simulation outputs (simulation_data.npz), compute the following quantities for the silver target case: (1) power reflection ratio η0 (reflected beam power divided by incident beam power); (2) beam reflection ratio ηb (number of reflected electrons divided by total incident electrons); (3) electron penetration depth h_e (depth where depth-averaged electron density falls to 1/e of its maximum); (4) heat penetration depth h_0 (depth where depth-averaged heat-generation density falls to 1/e of its maximum); (5) ratio h_0 / h_e. Report depths in µm. Write the results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": ["power_reflection", "beam_reflection", "electron_penetration_depth_um", "heat_penetration_depth_um", "ratio_heat_to_electron"], "properties": {"power_reflection": {"type": "number"}, "beam_reflection": {"type": "number"}, "electron_penetration_depth_um": {"type": "number", "unit": "µm"}, "heat_penetration_depth_um": {"type": "number", "unit": "µm"}, "ratio_heat_to_electron": {"type": "number"}}}
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
- target_policy: reference_match
- description: Derived quantities from the Monte Carlo simulation of electron transport and energy deposition in silver for a 30 keV beam at normal incidence.
- schema:
  - `type`: object
  - `required`: `power_reflection`, `beam_reflection`, `electron_penetration_depth_um`, `heat_penetration_depth_um`, `ratio_heat_to_electron`
  - `properties`:
    - `power_reflection`:
      - `type`: number
    - `beam_reflection`:
      - `type`: number
    - `electron_penetration_depth_um`:
      - `type`: number
      - `unit`: µm
    - `heat_penetration_depth_um`:
      - `type`: number
      - `unit`: µm
    - `ratio_heat_to_electron`:
      - `type`: number

Notes: The checker compares the agent's reported values to hidden reference values for the same material and beam conditions, applying appropriate tolerances for statistical reproducibility.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "power_reflection",
          "beam_reflection",
          "electron_penetration_depth_um",
          "heat_penetration_depth_um",
          "ratio_heat_to_electron"
        ],
        "properties": {
          "power_reflection": {
            "type": "number"
          },
          "beam_reflection": {
            "type": "number"
          },
          "electron_penetration_depth_um": {
            "type": "number",
            "unit": "µm"
          },
          "heat_penetration_depth_um": {
            "type": "number",
            "unit": "µm"
          },
          "ratio_heat_to_electron": {
            "type": "number"
          }
        }
      },
      "description": "Derived quantities from the Monte Carlo simulation of electron transport and energy deposition in silver for a 30 keV beam at normal incidence."
    }
  ],
  "notes": "The checker compares the agent's reported values to hidden reference values for the same material and beam conditions, applying appropriate tolerances for statistical reproducibility."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json and compares each required field to a hidden reference for the same material and beam conditions. The comparison uses appropriate tolerances that account for stochastic variation in Monte Carlo simulations. Each field's agreement with the reference contributes to a weighted score, and the final reward is a number between 0 and 1. The verifier does not disclose the reference values or the tolerances. You must produce a valid JSON file conforming to the output contract; reporting the paper's numbers without running the simulation is insufficient to earn the reward.
