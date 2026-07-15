# Electron-Phonon Superconducting Tc Estimation of GeH3 at High Pressure

## Problem background
Group-14 trihydrides at high pressure are predicted to exhibit metallic behavior and high-temperature superconductivity. This task investigates GeH3, a stoichiometry that becomes energetically competitive near 180 GPa, where three crystal structures (A15, P4_2/mmc, Cccm) are close in enthalpy. First-principles electron-phonon coupling calculations are used to estimate their superconducting transition temperatures Tc. The goal is to compute the microscopic electron-phonon parameters (coupling constant λ and logarithmic average phonon frequency ω_log) and the resulting Tc for each candidate structure, starting from the published structural data.

## Approach
Density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and plane-wave pseudopotentials is used to relax the three candidate GeH3 structures. The optimized geometries are then employed in density functional perturbation theory (DFPT) calculations on a uniform q-point grid to obtain phonon frequencies and eigenvectors. The electron-phonon coupling matrix elements are computed to yield the Eliashberg spectral function α²F(ω). Integrating this function gives the electron-phonon coupling constant λ and the logarithmic average phonon frequency ω_log. Lastly, the McMillan-Allen-Dynes formula with a Coulomb pseudopotential μ* = 0.13 is applied to estimate the superconducting critical temperature Tc for each structure.

## Reproduction target
Compute and report the electron-phonon coupling constant λ, the logarithmic average phonon frequency ω_log (in K), and the superconducting critical temperature Tc at μ* = 0.13 for the A15, P4_2/mmc, and Cccm structures of GeH3 at ~180 GPa. Use the structural parameters provided in Step 1 of the workflow, perform the full DFT relaxation and DFPT pipeline, and compile the results into the JSON file specified in the output contract. The target is to produce accurate values via an honest re-run of the computational procedure, not to match a particular reference by guesswork.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for Ge and H: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: DFT geometry optimization of the three GeH3 structures
- Role: process
- Action: For each candidate structure (A15, P4_2/mmc, Cccm) using the lattice constants and atomic positions given in the paper (A15: Pm-3n primitive cell; P4_2/mmc: a=b=3.033 Å, c=3.318 Å, Ge at 2c (0,0.5,0), H at 2e (0,0,0.25) and 4k (0.2244,0.5,0.5); Cccm: a=4.718, b=4.292, c=3.014 Å, Ge at 4e (0.25,0.25,0), H at 4b (0,0.5,0.25) and 8l (0.1043,0.8726,0)), perform a full variable-cell relaxation (atomic positions and cell parameters) using DFT with the PBE functional and the chosen pseudopotentials. Use an open-source plane-wave code (e.g. Quantum ESPRESSO). Record the final optimized structures for downstream phonon calculations.
- Evidence: `/app/outputs/relax_logs`

### Step 2: DFPT phonon and electron-phonon coupling calculations
- Role: process
- Action: For each optimized structure, compute the dynamical matrix on a uniform q-point grid using density functional perturbation theory (DFPT) to obtain phonon frequencies and eigenvectors. Then compute the electron-phonon coupling matrix elements to obtain the Eliashberg spectral function α²F(ω). Integrate to obtain the electron-phonon coupling constant λ and the logarithmic average phonon frequency ω_log using the standard definitions. Use the same pseudopotentials and DFT functional as in the relaxation step. Save the extracted λ and ω_log for each structure for the next step; raw DFPT outputs may be kept as evidence.
- Evidence: `/app/outputs/dfpt_outputs`

### Step 3: Tc estimation and result compilation
- Role: scored (load-bearing)
- Action: Using the λ and ω_log obtained from step 2 for each structure (A15, P4_2/mmc, Cccm), calculate the superconducting critical temperature Tc via the McMillan-Allen-Dynes formula with Coulomb pseudopotential μ* = 0.13. Assemble the results into a single JSON file containing, for each structure, the coupling constant λ, logarithmic average phonon frequency ω_log (in K), and the resulting Tc at μ* = 0.13 (in K).
- Output file: `/app/outputs/tc_results.json`
- Format: json
- Contract: json array of objects, each with keys: structure (string), lambda (float), omega_log (float, K), Tc_at_mu_0.13 (float, K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_results.json
- path: `/app/outputs/tc_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Superconducting critical temperature Tc (McMillan-Allen-Dynes) and electron-phonon coupling parameters λ and ω_log for the three GeH3 structures. The verifier compares against reference values with relative tolerances and checks the ordering of Tc (A15 > Cccm > P4_2/mmc).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `structure`, `lambda`, `omega_log`, `Tc_at_mu_0.13`
    - `properties`:
      - `structure`:
        - `type`: string
        - `enum`: `A15`, `P4_2/mmc`, `Cccm`
      - `lambda`:
        - `type`: number
      - `omega_log`:
        - `type`: number
        - `unit`: K
      - `Tc_at_mu_0.13`:
        - `type`: number
        - `unit`: K

Notes: The scored artifact is the compiled Tc results. All DFT and DFPT calculations are intermediate process steps; their outputs are not scored but must be executed to obtain λ and ω_log. The verifier reads the reported values; no raw recomputation from DFPT outputs is performed at scoring time.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "structure",
            "lambda",
            "omega_log",
            "Tc_at_mu_0.13"
          ],
          "properties": {
            "structure": {
              "type": "string",
              "enum": [
                "A15",
                "P4_2/mmc",
                "Cccm"
              ]
            },
            "lambda": {
              "type": "number"
            },
            "omega_log": {
              "type": "number",
              "unit": "K"
            },
            "Tc_at_mu_0.13": {
              "type": "number",
              "unit": "K"
            }
          }
        }
      },
      "description": "Superconducting critical temperature Tc (McMillan-Allen-Dynes) and electron-phonon coupling parameters λ and ω_log for the three GeH3 structures. The verifier compares against reference values with relative tolerances and checks the ordering of Tc (A15 > Cccm > P4_2/mmc)."
    }
  ],
  "notes": "The scored artifact is the compiled Tc results. All DFT and DFPT calculations are intermediate process steps; their outputs are not scored but must be executed to obtain λ and ω_log. The verifier reads the reported values; no raw recomputation from DFPT outputs is performed at scoring time."
}
```

## How you are scored
A hidden verifier reads your output file `tc_results.json`. It extracts the reported λ, ω_log, and Tc (μ*=0.13) for each of the three structures and compares them against reference values using relative tolerances that account for differences due to computational choices (codes, pseudopotentials, convergence settings). The verifier also inspects the relative Tc ordering among the structures. The final reward is a weighted combination of these per-structure comparisons and the ordering check. Better agreement with the expected results increases the reward; you do not need to know the reference values, only to execute the computational pipeline faithfully.
