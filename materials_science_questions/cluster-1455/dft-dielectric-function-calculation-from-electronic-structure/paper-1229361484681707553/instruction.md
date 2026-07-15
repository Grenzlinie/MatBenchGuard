# Reproduction of electronic band gaps using SE-RSH functional

## Problem background
Accurate prediction of electronic band gaps for heterogeneous materials remains a significant challenge for density functional theory (DFT) because standard semi-local and hybrid functionals often fail to capture the varying dielectric screening in systems with interfaces, surfaces, or low-dimensional structures. Recently, a non-empirical Screened-Exchange Range-Separated Hybrid (SE-RSH) functional was proposed that uses spatially dependent mixing fractions derived from a local dielectric function and a local screening function. The functional is designed to be applicable to 2D and 3D materials without any empirical fitting parameters. In this task, you will reproduce the SE-RSH functional and apply it to compute the fundamental band gaps of a set of representative materials to validate its predictive power.

## Approach
The core idea of the SE-RSH functional is to define a mixing fraction α(r,r′) that varies in space according to a local dielectric function ε(r) and a local screening function µ(r), inspired by the static COHSEX approximation. In the long‑range part, α approaches a dielectric‑dependent value (1/√(ε(r)ε(r′))), while in the short range the exact exchange fraction is set to 1, ensuring accurate description of both localized and delocalized states. The semilocal exchange is treated at the PBE level, with a long‑range part scaled by the PBE exchange hole. The local dielectric function ε(r) is obtained from DFT calculations in a finite electric field via Wannier‑function‑based polarization, while µ(r) is derived from the Thomas–Fermi screening length using the valence electron density. For computational efficiency, µ(r) is coarse‑grained using an adaptive binning scheme. In your reproduction, you will perform these steps using an open‑source DFT code (Qbox) and optimized norm‑conserving Vanderbilt pseudopotentials. You will first compute ε(r) and µ(r) for each target system using the PBE functional and a finite external electric field. Then you will implement the SE-RSH functional (or verify its already existing implementation) and run self‑consistent generalized Kohn–Sham calculations. Finally, you will extract the fundamental band gaps from the converged eigenvalues. The target systems are: Si (diamond), SiO₂ (α‑quartz), cubic BN (zincblende) and monolayer h‑BN (with a vacuum spacing of at least 15 Å). Standard lattice parameters from public crystallographic databases should be used.

## Reproduction target
Your goal is to compute the fundamental band gap (in eV) for each of the four materials (Si, SiO₂, BN, h‑BN) using the SE‑RSH functional as described above, and to write the results into the file `/app/outputs/se_rsh_band_gaps.json`. The file must be a JSON object with keys 'Si', 'SiO2', 'BN', 'h‑BN', each mapped to a floating-point number representing the band gap. The computed gaps will be compared to reference values to assess the accuracy of your reproduction.

## Assets

- Qbox code: https://qboxcode.org/
- Optimized norm-conserving Vanderbilt pseudopotentials: http://www.pseudo-dojo.org/
- Crystal structures for Si, SiO2, BN, h-BN

## Workflow steps

### Step 1: Compute local dielectric and screening functions
- Role: process
- Action: For each of the four systems (Si, SiO2, BN, h-BN), compute the local dielectric function ε(𝐫) and local screening function μ(𝐫) using the PBE functional and a finite external electric field. Use the method described in the paper (finite-field approach, Wannier-function-based polarization). Save the resulting fields for subsequent steps.
- Evidence: `/app/outputs/local_fields_output.log`

### Step 2: Implement SE-RSH functional
- Role: process
- Action: Implement the SE-RSH exchange-correlation functional in a DFT code (e.g., Qbox): define the mixing fraction α^{SE-RSH}(𝐫,𝐫′), the long-range semilocal exchange v_x^{lr} via scaled PBE exchange hole, and the expression for the xc potential. Incorporate coarse-grained approximation of μ(𝐫) and handle exchange divergence. Validate the implementation on a simple system.
- Evidence: `/app/outputs/implementation_check.txt`

### Step 3: Run SE-RSH self-consistent calculations
- Role: process
- Action: For each system, perform a self-consistent generalized Kohn–Sham calculation using the SE-RSH functional, the local ε(𝐫) and binned μ(𝐫) from step1, ONCV pseudopotentials, and an appropriate plane-wave cutoff. Use standard lattice parameters for the four systems. Monitor convergence.
- Evidence: `/app/outputs/scf_output.log`

### Step 4: Extract band gaps and write results
- Role: scored (load-bearing)
- Action: From the converged Kohn–Sham eigenvalues of step3, determine the fundamental band gap (energy difference between the valence band maximum and conduction band minimum) for each system. Write the result as a JSON file with keys 'Si', 'SiO2', 'BN', 'h-BN' and the computed gaps in eV as values.
- Output file: `/app/outputs/se_rsh_band_gaps.json`
- Format: json
- Contract: JSON object with keys: Si, SiO2, BN, h-BN, each a float (band gap in eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/se_rsh_band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### se_rsh_band_gaps.json
- path: `/app/outputs/se_rsh_band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fundamental band gaps in eV for Si (diamond), SiO2 (α-quartz), c-BN (zincblende), and monolayer h-BN, computed with the SE-RSH functional.
- schema:
  - `type`: object
  - `required`:
    - `Si`: float
    - `SiO2`: float
    - `BN`: float
    - `h-BN`: float

Notes: Tolerance and trend checks are defined in the hidden grading specification. The agent should use the described functional and public structures without empirical fitting.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "se_rsh_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Si": "float",
          "SiO2": "float",
          "BN": "float",
          "h-BN": "float"
        }
      },
      "description": "Fundamental band gaps in eV for Si (diamond), SiO2 (α-quartz), c-BN (zincblende), and monolayer h-BN, computed with the SE-RSH functional."
    }
  ],
  "notes": "Tolerance and trend checks are defined in the hidden grading specification. The agent should use the described functional and public structures without empirical fitting."
}
```

## How you are scored
The verifier will read your `se_rsh_band_gaps.json` file and compare each computed band gap to a hidden reference value (the value reported in the original study). It will also verify that the relative ordering of the gaps across the four materials follows a physically sensible trend (e.g., insulating materials have larger gaps than semiconductors, and monolayers have larger gaps than their bulk counterparts). Full credit corresponds to an accurate reproduction of the reference values and a correct trend. The verifier will also check that all required output files exist and are correctly formatted. The final reward is a weighted sum of these checks.
