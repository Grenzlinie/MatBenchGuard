# Superconducting Tc from First-Principles Electron-Phonon Coupling

## Problem background
Intermetallic compounds formed under high pressure can exhibit interesting physical properties, including conventional superconductivity driven by electron-phonon coupling. The Cu–Bi system, although immiscible at ambient conditions, has yielded several superconducting phases at high pressure. Among them, cubic Cu₂Bi (C15 Laves phase) is predicted to be dynamically stable when recovered to ambient pressure. Characterizing its electron-phonon coupling and superconducting critical temperature is the focus of this task.

## Approach
First-principles density functional perturbation theory (DFPT) will be used as implemented in Quantum Espresso with norm-conserving pseudopotentials. The workflow begins with a self-consistent field calculation for the cubic Cu₂Bi structure at 0 GPa. Phonon dispersion and electron-phonon coupling are then computed on a q‑point grid and a dense k‑point mesh, respectively, yielding the Eliashberg spectral function α²F(ω) and the integrated coupling strength λ. The logarithmic average phonon frequency ω_log is extracted from the phonon density of states and α²F(ω). Finally, the superconducting transition temperature Tc is estimated via the Allen‑Dynes modified McMillan formula with a Coulomb pseudopotential of μ* = 0.13.

## Reproduction target
Produce the three key superconducting parameters for cubic Cu₂Bi: the electron‑phonon coupling constant λ (dimensionless), the logarithmic average phonon frequency ω_log (in K), and the critical temperature Tc (in K). These numbers must be computed from the DFPT workflow described above and written to `/app/outputs/sc_results.json` as a JSON object with keys `lambda`, `w_log`, `tc`. The verifier will check the values against an independent hidden reference to assess correctness.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBEsol): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of cubic Cu₂Bi

## Workflow steps

### Step 1: DFT phonon and electron-phonon coupling calculation
- Role: process
- Action: Using Quantum Espresso with norm-conserving pseudopotentials, perform a self-consistent field calculation, followed by phonon dispersion calculation on a q-grid and electron-phonon coupling calculation on a dense k-mesh for the provided cubic Cu₂Bi structure at 0 GPa. Obtain the Eliashberg spectral function α²F(ω), the electron-phonon coupling constant λ, and the logarithmic average phonon frequency ω_log.
- Evidence: `/app/outputs/phonon_dos_alpha2F.dat`

### Step 2: Compute Tc and output results
- Role: scored (load-bearing)
- Action: From the electron-phonon coupling results, apply the Allen-Dynes modified McMillan formula with Coulomb pseudopotential μ*=0.13 to compute the superconducting critical temperature Tc. Output λ, ω_log (converted to K), and Tc in a JSON file.
- Output file: `/app/outputs/sc_results.json`
- Format: json
- Contract: { "lambda": "float (dimensionless)", "w_log": "float (K)", "tc": "float (K)" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sc_results.json
- path: `/app/outputs/sc_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed electron-phonon coupling constant λ, logarithmic average phonon frequency ω_log, and superconducting critical temperature Tc for cubic Cu₂Bi at 0 GPa.
- schema:
  - `type`: object
  - `required`:
    - `lambda`: float
    - `w_log`: float
    - `tc`: float
  - `additionalProperties`: False
  - `units`:
    - `lambda`: dimensionless
    - `w_log`: K
    - `tc`: K

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lambda": "float",
          "w_log": "float",
          "tc": "float"
        },
        "additionalProperties": false,
        "units": {
          "lambda": "dimensionless",
          "w_log": "K",
          "tc": "K"
        }
      },
      "description": "The computed electron-phonon coupling constant λ, logarithmic average phonon frequency ω_log, and superconducting critical temperature Tc for cubic Cu₂Bi at 0 GPa."
    }
  ],
  "notes": ""
}
```

## How you are scored
An automated hidden verifier reads your `sc_results.json` and compares the three reported values to a hidden gold standard derived from the same procedure. The verifier awards a score between 0 and 1 based on how close your computed values are to the reference. Better agreement yields a higher score; larger deviations reduce the score. There is no requirement to match an exact published number, but your methodology should reliably reproduce the correct physical quantities. The final reward is the weighted combination of the scores for each parameter.
