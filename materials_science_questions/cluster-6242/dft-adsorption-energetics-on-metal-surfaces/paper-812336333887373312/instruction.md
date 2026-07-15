# First-principles statistical mechanics for steady-state CO oxidation on RuO2(110)

## Problem background
Heterogeneous catalysis operates under steady-state conditions where the continuous interplay of adsorption, desorption, diffusion, and surface reactions determines the overall turnover frequency (TOF). A first-principles description of the full steady state requires combining density-functional theory (DFT) energetics with transition-state theory (TST) and kinetic Monte Carlo (kMC) simulations to model the stochastic surface dynamics. This task reproduces the steady-state behavior of CO oxidation on a RuO2(110) model catalyst at a single representative condition. The goal is to compute the average site occupations of CO and O on bridge and cus sites and the resulting CO2 formation TOF, thereby validating the implementation of the kMC model and the derived rate constants.

## Approach
The simulation is built on a lattice of surface unit cells, each containing one bridge (br) and one coordinatively unsaturated (cus) site. All 26 elementary processes are considered: non-dissociative CO adsorption, dissociative O2 adsorption (requiring a vacant pair of adjacent sites), desorption via detailed balance, surface diffusion between br and cus sites, and the Langmuir-Hinshelwood reaction CO + O → CO2 on neighboring sites.

Rate constants are derived from the DFT-computed energetic parameters listed below, which are extracted from the published first-principles study:

| Species | Binding energy (eV) | Diffusion barrier to br (eV) | Diffusion barrier to cus (eV) | Reaction barrier with CO⁽ᵇʳ⁾ (eV) | Reaction barrier with CO⁽ᶜᵘˢ⁾ (eV) |
|---------|--------------------|------------------------------|-------------------------------|-------------------------------------|-------------------------------------|
| CO⁽ᵇʳ⁾ | -1.6 | 0.6 | 1.6 | – | – |
| CO⁽ᶜᵘˢ⁾ | -1.3 | 1.3 | 1.7 | – | – |
| O⁽ᵇʳ⁾ | -2.3 | 0.7 | 2.3 | 1.5 | 1.2 |
| O⁽ᶜᵘˢ⁾ | -1.0 | 1.0 | 1.6 | 0.8 | 0.9 |

Binding energies are referenced to gas-phase CO and ½ O₂. Adsorption rates per free site are computed from kinetic gas theory with a sticking coefficient of 1, while desorption rates are obtained from detailed balance using the binding energies. Diffusion and reaction rate constants are estimated via transition state theory with a prefactor of 10¹² Hz. The resulting microscopic rate constants for all 26 processes are collected in a JSON file.

Using these rate constants, a lattice kMC simulation is performed on a grid of at least 20×20 surface unit cells at T = 600 K, pCO = 20 atm, pO₂ = 1 atm. The simulation is run until the coverages and TOF stabilize, at which point the average site occupation numbers and the CO2 TOF (in cm⁻² s⁻¹) are recorded.

## Reproduction target
Produce the steady-state results for the single condition T = 600 K, pCO = 20 atm, pO₂ = 1 atm. Specifically, compute and save the following quantities:
- Average site occupation numbers: N_CO_br, N_CO_cus, N_O_br, N_O_cus (each a float between 0 and 1).
- CO2 turnover frequency TOF (float, cm⁻² s⁻¹).
The results must be written to `/app/outputs/steady_state_results.json` as a JSON object containing the fields T (float, K), pCO (float, atm), pO2 (float, atm), TOF, N_CO_br, N_CO_cus, N_O_br, N_O_cus. All fields are required.

## Assets
The only required asset is a Python 3 environment with standard numerical libraries (numpy, scipy) for implementing the kMC simulation and rate constant calculations. No external datasets, models, or pre-trained weights are needed; all energetic parameters are provided in the approach section above. Install any missing packages at runtime using the Tsinghua PyPI mirror.

## Workflow steps

### Step 1: Compute microscopic rate constants from DFT energetics
- Role: process
- Action: Using the DFT-computed binding energies, diffusion barriers, and reaction barriers provided in the instruction (extracted from Table I of the paper), compute adsorption rates (via kinetic impingement formula with sticking coefficient 1), desorption rates (via detailed balance using binding energies), and diffusion/reaction rate constants (via transition state theory with prefactor 10^12 Hz) for all 26 elementary processes on the RuO2(110) lattice with bridge and cus sites. Save the resulting rate constants to rate_constants.json.
- Evidence: `/app/outputs/rate_constants.json`

### Step 2: Run kMC simulation for optimum catalytic condition and report steady-state results
- Role: scored (load-bearing)
- Action: Implement a lattice kinetic Monte Carlo simulation for CO oxidation on RuO2(110) using the rate constants from step 1. Use a lattice of at least 20×20 surface unit cells (each with one br and one cus site). Set temperature T=600 K, pCO=20 atm, pO2=1 atm. Include all 26 elementary processes. Run the simulation until steady state is reached (coverages and TOF stabilize). Compute the average site occupation numbers for CO at bridge, CO at cus, O at bridge, O at cus, and the CO2 turnover frequency (TOF) in cm⁻² s⁻¹. Write the results to steady_state_results.json.
- Output file: `/app/outputs/steady_state_results.json`
- Format: json
- Contract: {"type":"object","required":{"T":"float","pCO":"float","pO2":"float","TOF":"float","N_CO_br":"float","N_CO_cus":"float","N_O_br":"float","N_O_cus":"float"},"units":{"T":"K","pCO":"atm","pO2":"atm","TOF":"cm^-2 s^-1"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/steady_state_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### steady_state_results.json
- path: `/app/outputs/steady_state_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Steady-state surface coverages and turnover frequency at T=600 K, pCO=20 atm, pO2=1 atm.
- schema:
  - `type`: object
  - `required`:
    - `T`: float
    - `pCO`: float
    - `pO2`: float
    - `TOF`: float
    - `N_CO_br`: float
    - `N_CO_cus`: float
    - `N_O_br`: float
    - `N_O_cus`: float
  - `units`:
    - `T`: K
    - `pCO`: atm
    - `pO2`: atm
    - `TOF`: cm^-2 s^-1

Notes: The scored artifact is compared against the paper's reported values for TOF and coverages with an allowed tolerance. The agent must implement the kMC algorithm; no pre-existing code is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "steady_state_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "T": "float",
          "pCO": "float",
          "pO2": "float",
          "TOF": "float",
          "N_CO_br": "float",
          "N_CO_cus": "float",
          "N_O_br": "float",
          "N_O_cus": "float"
        },
        "units": {
          "T": "K",
          "pCO": "atm",
          "pO2": "atm",
          "TOF": "cm^-2 s^-1"
        }
      },
      "description": "Steady-state surface coverages and turnover frequency at T=600 K, pCO=20 atm, pO2=1 atm."
    }
  ],
  "notes": "The scored artifact is compared against the paper's reported values for TOF and coverages with an allowed tolerance. The agent must implement the kMC algorithm; no pre-existing code is provided."
}
```

## How you are scored
A hidden verifier independently checks your `steady_state_results.json`. It validates that the JSON structure is correct, that all coverages lie between 0 and 1, and that the TOF is positive. The verifier then compares your computed TOF and coverage values against reference values with an allowed tolerance. The final reward is a weighted combination of these checks, with the TOF and coverages carrying the bulk of the credit. Reporting numbers that match the reference within tolerance is necessary but not sufficient; the checker also ensures the values are physically plausible. No single scalar metric value or tolerance is revealed here.
