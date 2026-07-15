# DFT optical properties calculation for alkaline-earth metal nitrides

## Problem background
Alkaline-earth metal nitrides (Be3N2, Mg3N2, Ca3N2) are wide-band-gap semiconductors with potential applications in optoelectronics and UV devices. First-principles density functional theory calculations can predict their electronic structure and optical properties, but prior to the work that motivates this task, no systematic theoretical investigation of their full optical spectra had been reported. This task focuses on reproducing the critical computed quantities—fundamental band gap, static dielectric constant, and electron energy loss (EELS) features—for the three compounds in their cubic bcc phase (space group Ia-3) using an all-electron FP-LAPW approach.

## Approach
The reproduction uses a full-potential linearized augmented plane wave (FP-LAPW) code with the generalized gradient approximation (GGA) in the Perdew-Burke-Ernzerhof (PBE) functional. For each compound, self-consistent electronic structure calculations are performed to obtain converged charge densities, eigenvalues, wavefunctions, band structures, and densities of states. From these, the imaginary part of the complex dielectric function is computed within the random phase approximation (RPA) using momentum matrix elements, and the real part is obtained via Kramers-Kronig transformation. The electron energy loss function (EELS) is then derived. The target quantities are extracted from these results: the fundamental band gap and its direct/indirect character from the band structure, the static dielectric constant ε(0) (real part at zero frequency) without any scissor operator shift and without spin-orbit coupling, and for Be3N2 and Mg3N2 the shoulder and main maximum peak positions in the EELS. Spin-orbit coupling and scissor correction are intentionally excluded from the scored target because their effects are negligible for the requested quantities.

## Reproduction target
Perform all-electron density functional theory calculations using an open-source FP-LAPW code (e.g., Elk) with the GGA-PBE functional for the cubic bcc phases (space group Ia-3) of Be3N2, Mg3N2, and Ca3N2. Compute and write to a JSON file the fundamental band gap (eV) and whether it is direct or indirect for each compound, the static dielectric constant ε(0) (without scissor shift and without spin-orbit coupling), and for Be3N2 and Mg3N2 only, the shoulder and main maximum positions (eV) of the electron energy loss function. The output must follow the schema specified in the output contract. No scissor correction or spin-orbit coupling is applied.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.net/
- Crystal structures of Be3N2, Mg3N2, Ca3N2

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Obtain the cubic bcc crystal structures (space group Ia-3) of Be3N2, Mg3N2, and Ca3N2 from published crystallographic data and prepare input files for the FP-LAPW code.
- Evidence: `/app/outputs/structure_info.txt`

### Step 2: Run DFT electronic structure calculations
- Role: process
- Action: Perform self-consistent all-electron FP-LAPW calculations with the GGA-PBE functional (no spin-orbit coupling) for each compound to obtain converged charge densities, eigenvalues, wavefunctions, band structures, and densities of states.
- Evidence: `/app/outputs/dft_convergence.log`

### Step 3: Compute optical properties and extract scored quantities
- Role: scored (load-bearing)
- Action: From the electronic structure, compute the imaginary part of the dielectric function via momentum matrix elements (RPA) and the real part via Kramers-Kronig transformation. Compute the electron energy loss function (EELS). Extract the fundamental band gap (eV) and its direct/indirect character from the band structure. Extract the static dielectric constant ε(0) as the real part at zero frequency. Identify the shoulder and main maximum positions (eV) in the EELS for Be3N2 and Mg3N2. Write all results to step_01_results.json.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: Object with keys 'Be3N2', 'Mg3N2', 'Ca3N2'. Each is an object with keys: band_gap_eV (float), gap_direct (boolean), epsilon0 (float). For Be3N2 and Mg3N2 also include eels_shoulder_eV (float) and eels_max_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed optical properties and band gaps for the three nitrides; values are compared against the paper's reference data with tolerances.
- schema:
  - `type`: object
  - `required`: `Be3N2`, `Mg3N2`, `Ca3N2`
  - `properties`:
    - `Be3N2`:
      - `type`: object
      - `required`: `band_gap_eV`, `gap_direct`, `epsilon0`, `eels_shoulder_eV`, `eels_max_eV`
    - `Mg3N2`:
      - `type`: object
      - `required`: `band_gap_eV`, `gap_direct`, `epsilon0`, `eels_shoulder_eV`, `eels_max_eV`
    - `Ca3N2`:
      - `type`: object
      - `required`: `band_gap_eV`, `gap_direct`, `epsilon0`

Notes: The checker compares the reported values with noise-tolerant reference values derived from published data. No gold values or tolerances are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Be3N2",
          "Mg3N2",
          "Ca3N2"
        ],
        "properties": {
          "Be3N2": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "gap_direct",
              "epsilon0",
              "eels_shoulder_eV",
              "eels_max_eV"
            ]
          },
          "Mg3N2": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "gap_direct",
              "epsilon0",
              "eels_shoulder_eV",
              "eels_max_eV"
            ]
          },
          "Ca3N2": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "gap_direct",
              "epsilon0"
            ]
          }
        }
      },
      "description": "Computed optical properties and band gaps for the three nitrides; values are compared against the paper's reference data with tolerances."
    }
  ],
  "notes": "The checker compares the reported values with noise-tolerant reference values derived from published data. No gold values or tolerances are exposed."
}
```

## How you are scored
A hidden verifier reads your `step_01_results.json` and compares each reported value to a reference derived from the motivating study. The verifier applies pre‑set tolerances appropriate for independent reproductions with a different code implementation. Each successfully reproduced quantity contributes to the total reward, and the final score is a weighted combination of the per‑stage results. Reporting the numbers from the original publication without genuine computation is not sufficient; the verifier expects values produced by your own DFT workflow within the specified tolerance windows.
