# Reproduce superconducting Tc of hexagonal PtH via Quantum ESPRESSO

## Problem background
Superconductivity was reported in compressed silane, but the measured X-ray diffraction pattern did not match any known silane phase. The observation of platinum in the sample led to the hypothesis that a platinum hydride formed from the electrodes could be responsible. First-principles calculations were used to investigate whether a platinum hydride phase at high pressure could explain the anomalous superconductivity. The study predicted a candidate crystal structure, computed its lattice constants, and estimated the superconducting critical temperature from electron-phonon coupling, aiming to reproduce the experimental anomalies.

## Approach
Using density functional theory (DFT), the equilibrium geometry of a hexagonal PtH crystal is obtained at a target pressure of 113 GPa. Dynamical stability is verified through phonon dispersion calculations. Electron-phonon coupling is then evaluated within the framework of density-functional perturbation theory to extract the coupling strength λ and the logarithmic average phonon frequency ω_log. The superconducting transition temperature Tc is estimated from these quantities via the Allen–Dynes modified McMillan equation, assuming a typical Coulomb pseudopotential μ* = 0.1.

## Reproduction target
Build the P6_3/mmc PtH crystal structure (Pt at Wyckoff 2c (1/3,2/3,1/4), H at 2a (0,0,0)) and perform a variable-cell DFT relaxation at 113 GPa using Quantum ESPRESSO and appropriate pseudopotentials. Following relaxation, compute the phonon dispersion and electron-phonon coupling to obtain λ and ω_log. Finally, calculate Tc using the Allen–Dynes formula with μ* = 0.1. The results—lattice constants a and c, λ, ω_log, and Tc—must be written to a JSON file as specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (ultrasoft, GGA-PBE/PW91) for Pt and H: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT relaxation of PtH at 113 GPa
- Role: process
- Action: Build the P6_3/mmc PtH crystal structure (Pt at Wyckoff 2c (1/3,2/3,1/4); H at 2a (0,0,0)) with initial lattice parameters a ≈ 2.671 Å, c ≈ 4.491 Å (experimental lattice constants for PtH at 113 GPa). Run a variable-cell relaxation in Quantum ESPRESSO (pw.x) at a target pressure of 113 GPa using the chosen pseudopotentials, until forces are below a typical threshold (e.g., 10^-2 eV/Å). Save the relaxed structure for the next stages.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Phonon and electron-phonon coupling calculation
- Role: process
- Action: Using the relaxed PtH structure from step_01_relax, compute dynamical matrices on a q-point grid via DFPT (ph.x). Then compute electron-phonon coupling matrix elements, Eliashberg spectral function, lambda, and omega_log using the QE stack.
- Evidence: `/app/outputs/epc_output.log`

### Step 3: Extract results and compute Tc
- Role: scored (load-bearing)
- Action: From step_01_relax, extract the final lattice constants a and c (in Å). From step_02_epc, extract the EPC strength lambda and the logarithmic average phonon frequency omega_log (in K). Compute Tc using the Allen-Dynes modified McMillan formula with μ*=0.1. Write these five values to pth_results.json.
- Output file: `/app/outputs/pth_results.json`
- Format: json
- Contract: JSON object with keys: a (float, Å), c (float, Å), lambda (float), omega_log (float, K), Tc (float, K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pth_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pth_results.json
- path: `/app/outputs/pth_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the reproduced lattice constants a, c and superconducting transition temperature Tc, along with intermediate quantities lambda and omega_log for traceability. Checker compares a, c, and Tc against hidden gold values from the paper within tolerance windows.
- schema:
  - `type`: object
  - `required`: `a`, `c`, `lambda`, `omega_log`, `Tc`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `lambda`: dimensionless
    - `omega_log`: K
    - `Tc`: K

Notes: lambda and omega_log are included but not directly scored; they provide traceability for the Tc calculation. Tolerance windows for a, c, and Tc are set in hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pth_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "c",
          "lambda",
          "omega_log",
          "Tc"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "lambda": "dimensionless",
          "omega_log": "K",
          "Tc": "K"
        }
      },
      "description": "Scored artifact containing the reproduced lattice constants a, c and superconducting transition temperature Tc, along with intermediate quantities lambda and omega_log for traceability. Checker compares a, c, and Tc against hidden gold values from the paper within tolerance windows."
    }
  ],
  "notes": "lambda and omega_log are included but not directly scored; they provide traceability for the Tc calculation. Tolerance windows for a, c, and Tc are set in hidden grading specification."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier. The verifier reads your pth_results.json and compares the lattice constants a and c and the superconducting Tc against reference values. The intermediate quantities λ and ω_log are included for traceability and are checked, but carry lower weight. The final score is a weighted combination of these comparisons; simply reporting numbers from the literature without executing the required calculations will yield a low score.
