# DFT dielectric and optical properties of chalcopyrite semiconductors

## Problem background
Ternary chalcopyrite semiconductors with formula AI BIII S2 (where B = Al, Ga, In and A = Cu, Ag) are widely studied for nonlinear optics, solar cells, and optoelectronic devices because of their direct band gaps and large optical nonlinearities. Reliable predictions of their lattice structure, electronic band gaps, and optical dispersion are essential for device design, yet experimental data often show scatter and first‑principles calculations using standard density‑functional approximations systematically underestimate band gaps. Reproducing a self‑consistent set of optimized structural parameters, corrected band gaps, static refractive indices, and dispersion coefficients for four prototype compounds—CuAlS2, CuGaS2, CuInS2, and AgGaS2—provides a stringent test of the computational protocol and delivers practical optical constants for these materials.

## Approach
The workflow uses plane‑wave pseudopotential density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation, which is an open‑source equivalent of the original CASTEP calculations. For each compound, the crystal structure is first fully relaxed until forces and stress are below tight convergence thresholds, starting from the known experimental chalcopyrite lattice parameters (space group I‾42d). From the optimized geometry, a self‑consistent electronic structure calculation yields Kohn‑Sham eigenvalues and wavefunctions. The optical dielectric function is obtained by computing the imaginary part ε₂(ω) from dipole matrix elements and then obtaining the real part ε₁(ω) by Kramers‑Kronig transformation. The systematic DFT band‑gap underestimation is corrected with a rigid conduction‑band shift (scissor operator). After the shift, the static refractive index n₀ is extracted as √(ε₁(ω=0)), and the wavelength‑dependent refractive index n(λ) in the visible–near‑IR range is fitted to the Sellmeier equation with infrared correction, n = A + B/(1 − (C/λ)²) − D λ². The procedure is repeated for all four compounds, and all headline quantities are collected into a single JSON file for verification.

## Reproduction target
For each of the four compounds (CuAlS2, CuGaS2, CuInS2, AgGaS2), perform the full DFT protocol using an open‑source plane‑wave code with GGA‑PBE pseudopotentials. From the calculations, obtain:

- Optimized lattice constants a, c and the unit‑cell volume.
- The direct DFT band gap (valence‑band maximum to conduction‑band minimum) and the corrected band gap after applying the specified scissor shift.
- The static refractive index n₀, defined as the square root of the real part of the dielectric function at zero frequency.
- The four parameters (A, B, C, D) of the Sellmeier fit to the computed n(λ) curve.

The results must be written to `/app/outputs/results.json` following the schema declared in the output contract. The initial experimental lattice parameters and the scissor shifts are given in the workflow steps; the computational parameters (k‑point mesh, energy cutoffs) should be chosen to be consistent with those described there.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials (PSLibrary): https://www.quantum-espresso.org/pseudopotentials/pslibrary

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: For each of the four compounds (CuAlS2, CuGaS2, CuInS2, AgGaS2), perform DFT geometry optimization starting from the experimental lattice constants (provided in the task). Use GGA-PBE pseudopotentials, a 5×5×2 k-point grid, and appropriate energy cutoffs. Converge forces and stress to tight thresholds.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Electronic structure calculation
- Role: process
- Action: For each optimized structure, run a self-consistent DFT calculation to obtain Kohn-Sham eigenvalues and wavefunctions on a suitable grid. This step produces the electronic ground state required for optical property calculations.
- Evidence: `/app/outputs/electronic_structure.log`

### Step 3: Optical dielectric function calculation
- Role: process
- Action: Using the wavefunctions and eigenvalues, compute the imaginary part ε₂(ω) via dipole matrix elements. Obtain the real part ε₁(ω) by Kramers-Kronig transformation. Apply 0.25 eV Gaussian smearing. Produce raw ω, ε₁, ε₂ data for each compound.
- Evidence: `/app/outputs/dielectric_raw.csv`

### Step 4: Post-processing and fitting
- Role: scored (load-bearing)
- Action: From the DFT results: extract the calculated band gap, apply scissor operator shifts (1.55 eV for CuAlS2, 1.5 eV for others) to obtain corrected gaps, compute the static refractive index n₀ = sqrt(ε₁(ω=0)), generate the n(λ) curve and fit the Sellmeier equation n = A + B/(1 - (C/λ)²) - Dλ². Collect the optimized lattice constants a, c, and volume. Write all quantities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"compounds": [{"compound_name": "string", "optimized_a": "float (Å)", "optimized_c": "float (Å)", "optimized_volume": "float (Å³)", "band_gap_calculated": "float (eV)", "scissor_shift": "float (eV)", "band_gap_corrected": "float (eV)", "refractive_index_n0": "float", "sellmeyer_A": "float", "sellmeyer_B": "float", "sellmeyer_C_nm": "float (nm)", "sellmeyer_D": "float (nm⁻²)"}]}
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
- description: Headline DFT results for all four compounds: optimized lattice constants, scissor-corrected band gaps, static refractive index, and Sellmeier dispersion parameters.
- schema:
  - `type`: object
  - `required`: `compounds`
  - `compounds`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `compound_name`, `optimized_a`, `optimized_c`, `optimized_volume`, `band_gap_calculated`, `scissor_shift`, `band_gap_corrected`, `refractive_index_n0`, `sellmeyer_A`, `sellmeyer_B`, `sellmeyer_C_nm`, `sellmeyer_D`
      - `properties`:
        - `compound_name`: string
        - `optimized_a`:
          - `type`: number
          - `unit`: Å
        - `optimized_c`:
          - `type`: number
          - `unit`: Å
        - `optimized_volume`:
          - `type`: number
          - `unit`: Å³
        - `band_gap_calculated`:
          - `type`: number
          - `unit`: eV
        - `scissor_shift`:
          - `type`: number
          - `unit`: eV
        - `band_gap_corrected`:
          - `type`: number
          - `unit`: eV
        - `refractive_index_n0`:
          - `type`: number
          - `unit`: dimensionless
        - `sellmeyer_A`:
          - `type`: number
        - `sellmeyer_B`:
          - `type`: number
        - `sellmeyer_C_nm`:
          - `type`: number
          - `unit`: nm
        - `sellmeyer_D`:
          - `type`: number
          - `unit`: nm⁻²

Notes: The hidden gold values are the paper-reported numbers with tolerances (±2% for lattice constants, ±0.1 eV for band gaps, ±0.05 for refractive index, ±10% for Sellmeier parameters). This is a result-level comparison; the checker reads results.json and compares each numeric field to the gold values.

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
          "compounds"
        ],
        "compounds": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "compound_name",
              "optimized_a",
              "optimized_c",
              "optimized_volume",
              "band_gap_calculated",
              "scissor_shift",
              "band_gap_corrected",
              "refractive_index_n0",
              "sellmeyer_A",
              "sellmeyer_B",
              "sellmeyer_C_nm",
              "sellmeyer_D"
            ],
            "properties": {
              "compound_name": "string",
              "optimized_a": {
                "type": "number",
                "unit": "Å"
              },
              "optimized_c": {
                "type": "number",
                "unit": "Å"
              },
              "optimized_volume": {
                "type": "number",
                "unit": "Å³"
              },
              "band_gap_calculated": {
                "type": "number",
                "unit": "eV"
              },
              "scissor_shift": {
                "type": "number",
                "unit": "eV"
              },
              "band_gap_corrected": {
                "type": "number",
                "unit": "eV"
              },
              "refractive_index_n0": {
                "type": "number",
                "unit": "dimensionless"
              },
              "sellmeyer_A": {
                "type": "number"
              },
              "sellmeyer_B": {
                "type": "number"
              },
              "sellmeyer_C_nm": {
                "type": "number",
                "unit": "nm"
              },
              "sellmeyer_D": {
                "type": "number",
                "unit": "nm⁻²"
              }
            }
          }
        }
      },
      "description": "Headline DFT results for all four compounds: optimized lattice constants, scissor-corrected band gaps, static refractive index, and Sellmeier dispersion parameters."
    }
  ],
  "notes": "The hidden gold values are the paper-reported numbers with tolerances (±2% for lattice constants, ±0.1 eV for band gaps, ±0.05 for refractive index, ±10% for Sellmeier parameters). This is a result-level comparison; the checker reads results.json and compares each numeric field to the gold values."
}
```

## How you are scored
A hidden verifier reads the scored output file `/app/outputs/results.json` and compares each numerical field to reference values with tolerances appropriate for a re‑implementation with a different code and pseudopotentials. The final reward is computed from the agreement across all quantities (lattice constants, corrected band gaps, refractive index, Sellmeier parameters) for all four compounds. The intermediate process steps (geometry optimization, electronic structure, dielectric function) are not directly scored but are required because the final scored step is load‑bearing: it can only produce correct results if those steps have genuinely been executed. Reporting a number without executing the workflow will not yield the correct values and will be detected by the verifier.
