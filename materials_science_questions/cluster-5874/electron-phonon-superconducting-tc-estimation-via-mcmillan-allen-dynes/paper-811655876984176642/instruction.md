# Superconducting critical temperature prediction of hexagonal platinum hydride from first principles

## Problem background
Platinum hydride (PtH) is a compound formed under high pressure that adopts a hexagonal close-packed (hcp) structure (PtH-II). First-principles calculations have explored the possibility that PtH-II becomes superconducting at pressures near 90 GPa. Predicting the superconducting critical temperature from first principles requires modeling the electronic structure, lattice dynamics, and electron-phonon coupling of this material.

## Approach
The prediction is carried out using density functional theory (DFT) and density functional perturbation theory (DFPT). First, the crystal structure of hcp PtH-II is relaxed under a target pressure of 90 GPa via a variable-cell DFT relaxation. Then, using the relaxed structure, a DFPT phonon calculation is performed to obtain the phonon frequencies and eigenvectors. From these, the electron-phonon coupling constant λ and the logarithmic average phonon frequency ω_log are computed. Finally, the superconducting critical temperature Tc is estimated from λ and ω_log using the Allen-Dynes modified McMillan equation, adopting a Coulomb pseudopotential μ* = 0.13.

## Reproduction target
Compute and report the superconducting critical temperature Tc of hcp PtH-II at a pressure of 90 GPa, together with the electron-phonon coupling constant λ and the logarithmic average phonon frequency ω_log, following the first-principles procedure outlined above. Save these values to the file output_tc.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Library (pseudopotentials for Pt and H): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT variable-cell relaxation of hcp PtH-II at 90 GPa
- Role: process
- Action: Set up a DFT calculation for the hcp PtH-II crystal (space group P6_3/mmc, Pt at 2c, H at 2a) and perform a variable-cell relaxation to optimize lattice parameters at a target external pressure of 90 GPa.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: DFPT phonon and electron-phonon coupling calculation
- Role: process
- Action: Using the relaxed structure from step_01, run a DFPT phonon calculation on a q-point mesh to obtain dynamical matrices and phonon frequencies. Then perform an electron-phonon coupling calculation to compute the Eliashberg function, the electron-phonon coupling constant λ, and the logarithmic average frequency ω_log.
- Evidence: `/app/outputs/epc_output.log`

### Step 3: Compute superconducting Tc and report results
- Role: scored (load-bearing)
- Action: Compute the superconducting critical temperature Tc using the Allen-Dynes modified McMillan formula: k_B T_c = (ℏ ω_log / 1.20) exp[ -1.04 (1+λ) / (λ - μ* (1+0.62λ) ) ], with μ* = 0.13. Save Tc (in K), λ (dimensionless), and ω_log (in K) to the JSON file.
- Output file: `/app/outputs/output_tc.json`
- Format: json
- Contract: JSON object with keys: Tc (float, in K), lambda (float), omega_log (float, in K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/output_tc.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### output_tc.json
- path: `/app/outputs/output_tc.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Superconducting critical temperature Tc (K), electron-phonon coupling constant λ (dimensionless), logarithmic average phonon frequency ω_log (K) computed for hcp PtH-II at 90 GPa using the Allen-Dynes modified McMillan equation with μ*=0.13.
- schema:
  - `type`: object
  - `required`:
    - `Tc`: number
    - `lambda`: number
    - `omega_log`: number
  - `units`:
    - `Tc`: K
    - `omega_log`: K

Notes: Tc is the primary scored quantity; λ and ω_log serve as consistency checks. The hidden checker compares these values to paper-reported references with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "output_tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc": "number",
          "lambda": "number",
          "omega_log": "number"
        },
        "units": {
          "Tc": "K",
          "omega_log": "K"
        }
      },
      "description": "Superconducting critical temperature Tc (K), electron-phonon coupling constant λ (dimensionless), logarithmic average phonon frequency ω_log (K) computed for hcp PtH-II at 90 GPa using the Allen-Dynes modified McMillan equation with μ*=0.13."
    }
  ],
  "notes": "Tc is the primary scored quantity; λ and ω_log serve as consistency checks. The hidden checker compares these values to paper-reported references with appropriate tolerances."
}
```

## How you are scored
A hidden verifier inspects your output_tc.json file. It checks that the file is valid JSON with the expected keys (Tc, lambda, omega_log) and that each value is a number with appropriate units. The verifier then compares your reported Tc, λ, and ω_log against reference values derived from the original study, using tolerances that account for legitimate differences in computational implementation. Your final reward reflects how well your computed quantities agree with the references; close agreement yields the highest score, while larger deviations reduce the reward.
