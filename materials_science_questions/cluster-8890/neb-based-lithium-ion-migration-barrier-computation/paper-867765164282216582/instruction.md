# Compute Lithium-ion Migration Activation Energies: Zero-temperature NEB vs Finite-temperature AIMD

## Problem background
Lithium superionic conductors are critical for solid-state batteries, but the effect of temperature on lithium-ion migration barriers is not fully understood. First-principles methods often estimate barriers at zero temperature using the nudged elastic band (NEB) method, potentially missing anharmonic lattice effects. Ab initio molecular dynamics (AIMD) can incorporate temperature, but whether it yields systematically different activation energies and how they correlate across materials remains an open quantitative question. This task investigates a set of chemically and structurally diverse lithium fast-ion conductors to compute and compare the activation energies for lithium vacancy migration obtained from zero-temperature NEB and from finite-temperature AIMD simulations.

## Approach
The central goal is to compute, for each candidate material, two key quantities: (1) the zero-temperature migration activation energy Ea0 using the nudged elastic band (NEB) method, and (2) the finite-temperature activation energy Ea and pre-exponential factor D0 via ab initio molecular dynamics (AIMD) combined with Arrhenius analysis. First, perform density functional theory (DFT) geometry optimizations on supercells of each material containing lithium vacancies. Then conduct NEB calculations to determine the minimum energy path and extract Ea0. Next, run canonical-ensemble AIMD simulations at several temperatures (e.g., 600–1000 K) for the non-stoichiometric supercells; from the ionic trajectories compute the mean square displacement of lithium, extract diffusion coefficients D(T), and fit the Arrhenius law D(T)=D0 exp(-Ea/kT) to obtain Ea and D0. Finally, compile the results and compare the zero-temperature and finite-temperature barriers across materials to assess whether temperature effects systematically increase the activation energy and alter the relative ordering among compounds.

## Reproduction target
Compute the zero-temperature NEB activation energy Ea0 and the finite-temperature AIMD activation energy Ea and pre-exponential factor D0 for lithium vacancy migration in at least three of the four superionic conductors Li3N, LiGaO2, LiIO3, Li3OCl. Write the results to activation_energies.json. The hidden verifier will evaluate the correctness of the activation energies based on expected physical trends and reference values.

## Assets

- Open-source DFT code (Quantum ESPRESSO 7.x or equivalent): https://www.quantum-espresso.org/
- Crystal structure data for Li3N (P63/mmc), LiGaO2 (Pna21), LiIO3 (P63), Li3OCl (P4/mmm): https://materialsproject.org/

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for each lithium fast-ion conductor (Li3N, LiGaO2, LiIO3, Li3OCl) using an open-source DFT code. Prepare supercells with lithium vacancies for the non-stoichiometric systems that will be used in subsequent NEB and AIMD calculations.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: Zero-temperature NEB calculations
- Role: process
- Action: For each material, set up initial and final configurations for lithium vacancy migration and compute the minimum energy path using the nudged elastic band method. Extract the zero-temperature migration activation energy Ea0.
- Evidence: `/app/outputs/neb_results.json`

### Step 3: AIMD simulations
- Role: process
- Action: Run ab initio molecular dynamics simulations in the canonical ensemble at several temperatures (e.g., 600–1000 K) for the non-stoichiometric supercells (containing ~2% lithium vacancies) of each material. Collect ionic trajectories over sufficient simulation time to converge diffusivities.
- Evidence: none

### Step 4: Diffusion analysis
- Role: process
- Action: From the AIMD trajectories, compute the mean square displacement of lithium ions, extract diffusion coefficients at each temperature, and fit the Arrhenius law to obtain finite-temperature activation energy Ea and pre-exponential factor D0.
- Evidence: `/app/outputs/diffusion_fit.log`

### Step 5: Compile activation energy results
- Role: scored (load-bearing)
- Action: Gather Ea0 from NEB, and Ea and D0 from the diffusion analysis for at least three of the four superionic conductors (Li3N, LiGaO2, LiIO3, Li3OCl). LiF is optional and not scored. Write a JSON file containing these values.
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: [{"material": "string", "Ea_0_NEB_eV": number, "Ea_AIMD_eV": number, "D0_cm2_per_s": number}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation energies and diffusion pre-exponential factors for lithium-ion migration in at least three superionic conductors (Li3N, LiGaO2, LiIO3, Li3OCl), comparing zero-temperature NEB barriers with finite-temperature AIMD results.
- schema:
  - `type`: array
  - `required`:
    - `material`: string
    - `Ea_0_NEB_eV`: number
    - `Ea_AIMD_eV`: number
    - `D0_cm2_per_s`: number
  - `items`:
    - `material`: string
    - `Ea_0_NEB_eV`: number
    - `Ea_AIMD_eV`: number
    - `D0_cm2_per_s`: number

Notes: The hidden checker verifies that for each material Ea_AIMD > Ea_0_NEB by at least 0.05 eV, that the Ea_AIMD ordering across materials is monotonic with respect to paper-reported values (Li3N < LiIO3 < Li3OCl < LiGaO2) allowing small inversions (<0.1 eV), and that absolute values are within 50% tolerance of the paper's reported values. LiF is optional and not scored. At least three materials must satisfy both inequality and ordering for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": {
          "material": "string",
          "Ea_0_NEB_eV": "number",
          "Ea_AIMD_eV": "number",
          "D0_cm2_per_s": "number"
        },
        "items": {
          "material": "string",
          "Ea_0_NEB_eV": "number",
          "Ea_AIMD_eV": "number",
          "D0_cm2_per_s": "number"
        }
      },
      "description": "Activation energies and diffusion pre-exponential factors for lithium-ion migration in at least three superionic conductors (Li3N, LiGaO2, LiIO3, Li3OCl), comparing zero-temperature NEB barriers with finite-temperature AIMD results."
    }
  ],
  "notes": "The hidden checker verifies that for each material Ea_AIMD > Ea_0_NEB by at least 0.05 eV, that the Ea_AIMD ordering across materials is monotonic with respect to paper-reported values (Li3N < LiIO3 < Li3OCl < LiGaO2) allowing small inversions (<0.1 eV), and that absolute values are within 50% tolerance of the paper's reported values. LiF is optional and not scored. At least three materials must satisfy both inequality and ordering for full credit."
}
```

## How you are scored
Each workflow step's output is evaluated independently by a hidden verifier. The most important artifact is activation_energies.json, which carries the majority of the score. The verifier checks that the JSON contains the required fields for at least three materials and that the reported activation energies are physically consistent and within expected ranges. Process steps (geometry optimization, NEB, AIMD, diffusion fitting) must produce expected evidence files (geom_opt.log, neb_results.json, diffusion_fit.log) which are audited for existence and basic sanity; these carry a small weight. The final reward is a weighted combination, scaled between 0 and 1, with a perfect score of 1.0 awarded for a submission that fully satisfies all requirements. Partial credit is given for partially correct results. To succeed, you must execute the entire pipeline; mere reporting of expected numbers is not sufficient.
