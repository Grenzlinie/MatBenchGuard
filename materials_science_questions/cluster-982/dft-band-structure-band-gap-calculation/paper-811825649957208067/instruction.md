# DFT Reproducibility of Electronic and Optical Properties of Chalcopyrite Semiconductors

## Problem background
Ternary chalcopyrite semiconductors of the form A^I B^III C_2^VI are widely studied for their applications in non-linear optics and as absorber materials in thin-film solar cells. First-principles electronic-structure calculations within density functional theory (DFT) provide insight into their band structures, densities of states, and optical dielectric response. Reproducing the key computed quantities — optimized lattice constants, raw (uncorrected) Kohn-Sham band gaps, and optical constants derived from the scissor-corrected dielectric function — tests the predictive power of open-source DFT methods for this class of materials.

## Approach
The work follows a three-stage DFT workflow implemented with Quantum ESPRESSO and the GGA-PBE exchange-correlation functional (ultrasoft pseudopotentials from the GBRV library).

1. **Geometry optimization**: Starting from experimental chalcopyrite crystal structures (space group I-42d), perform full variable-cell relaxation to obtain the equilibrium lattice constants *a* and *c* and unit-cell volume *V*.
2. **Band structure and raw band gap**: Using the optimized structures, run a non-self-consistent band-structure calculation to extract the valence-band maximum and conduction-band minimum and compute the uncorrected (Kohn-Sham) band gap.
3. **Optical properties**: Compute the frequency-dependent dielectric function ε(ω) = ε₁(ω) + i ε₂(ω) from the wavefunctions. Apply a rigid scissor shift to the conduction bands using the known experimental band gaps for each compound (supplied as an asset) to overcome the DFT band-gap underestimation. Obtain the refractive index at zero energy n₀ = √(ε₁(0)). Then compute the wavelength-dependent refractive index n(λ) and fit it to the Sellmeier equation with an infrared correction,

   n = A + B / (1 − (C/λ)²) − D λ² ,

   to extract the four parameters A, B, C (in nm) and D (in nm⁻²).

## Reproduction target
For each of the four compounds **CuAlS₂**, **CuGaS₂**, **CuInS₂**, and **AgGaS₂**, perform the described DFT workflow and produce the following results:

- Optimized lattice constants *a*, *c* (in Å) and unit-cell volume *V* (in Å³) — step 1.
- Uncorrected Kohn-Sham band gap (in eV) — step 2.
- Refractive index at infinite wavelength n₀ (dimensionless) and the four Sellmeier parameters A, B, C (nm), D (nm⁻²) obtained from the scissor-corrected dielectric function — step 3.

All results must be saved in the three JSON files with the exact structure described in the workflow steps and output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV ultrasoft pseudopotentials (PBE): https://www.physics.rutgers.edu/gbrv/
- Experimental chalcopyrite crystal structures: 10.1016/0038-1098(73)90708-4
- Experimental band gaps

## Workflow steps

### Step 1: Geometry optimization
- Role: scored
- Action: For each of the four compounds, build the initial chalcopyrite cell from experimental lattice constants and atomic positions. Perform a full variable-cell relaxation using DFT-GGA (PBE) with Quantum ESPRESSO and the chosen pseudopotentials, converging forces and stress. Save the final optimized lattice constants a, c and unit cell volume V.
- Output file: `/app/outputs/optimized_lattice_constants.json`
- Format: json
- Contract: Object with keys CuAlS2, CuGaS2, CuInS2, AgGaS2. Each value is {a: number (Å), c: number (Å), V: number (Å^3)}
- Scoring: scored by hidden verifier

### Step 2: Band structure and band gap
- Role: scored
- Action: Using the optimized structures, perform a non-self-consistent band structure calculation along the standard chalcopyrite high-symmetry k-path. Extract the Kohn-Sham eigenvalues to obtain the valence band maximum and conduction band minimum; compute the uncorrected band gap E_g = E_CBM - E_VBM. Save the uncorrected band gap values.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: Object with keys CuAlS2, CuGaS2, CuInS2, AgGaS2. Each value is {uncorrected_band_gap: number (eV)}
- Scoring: scored by hidden verifier

### Step 3: Optical properties with scissor correction
- Role: scored (load-bearing)
- Action: From the eigenvalues and wavefunctions of step2, compute the imaginary part epsilon2 of the dielectric function. Apply a rigid scissor shift equal to (E_exp - E_g_uncorrected) to the conduction bands, where E_exp are the provided experimental band gaps. Obtain the real part epsilon1 via Kramers-Kronig transform. Determine the refractive index n(0)=sqrt(epsilon1(0)). Compute the wavelength-dependent refractive index n(lambda) and fit to the Sellmeier equation with infrared correction n = A + B/(1-(C/lambda)^2) - D*lambda^2 to extract A, B, C, D. Save all optical results.
- Output file: `/app/outputs/optical_properties.json`
- Format: json
- Contract: Object with keys CuAlS2, CuGaS2, CuInS2, AgGaS2. Each value is {refractive_index_n0: number (dimensionless), sellmeier_params: {A: number, B: number, C: number (nm), D: number (nm^-2)}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lattice_constants.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/optical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lattice_constants.json
- path: `/app/outputs/optimized_lattice_constants.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Optimized lattice constants from DFT geometry optimization for all four compounds.
- schema:
  - `type`: object
  - `required`:
    - `CuAlS2`: object with a, c, V
    - `CuGaS2`: object with a, c, V
    - `CuInS2`: object with a, c, V
    - `AgGaS2`: object with a, c, V
  - `units`:
    - `a`: Å
    - `c`: Å
    - `V`: Å^3

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Uncorrected (raw GGA) band gaps for all four compounds.
- schema:
  - `type`: object
  - `required`:
    - `CuAlS2`: object with uncorrected_band_gap
    - `CuGaS2`: object with uncorrected_band_gap
    - `CuInS2`: object with uncorrected_band_gap
    - `AgGaS2`: object with uncorrected_band_gap
  - `units`:
    - `uncorrected_band_gap`: eV

### optical_properties.json
- path: `/app/outputs/optical_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Refractive index at zero energy and Sellmeier equation parameters from scissor-corrected dielectric function.
- schema:
  - `type`: object
  - `required`:
    - `CuAlS2`: object with refractive_index_n0 and sellmeier_params
    - `CuGaS2`: object with refractive_index_n0 and sellmeier_params
    - `CuInS2`: object with refractive_index_n0 and sellmeier_params
    - `AgGaS2`: object with refractive_index_n0 and sellmeier_params
  - `units`:
    - `refractive_index_n0`: dimensionless
    - `sellmeier_params.A`: dimensionless
    - `sellmeier_params.B`: dimensionless
    - `sellmeier_params.C`: nm
    - `sellmeier_params.D`: nm^-2

Notes: The scissor shift uses the provided experimental band gap values; the agent must compute it from the uncorrected gap of step2 and apply it to the dielectric function. All scored quantities are compared to the paper's own calculated values with per-quantity tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "CuAlS2": "object with a, c, V",
          "CuGaS2": "object with a, c, V",
          "CuInS2": "object with a, c, V",
          "AgGaS2": "object with a, c, V"
        },
        "units": {
          "a": "Å",
          "c": "Å",
          "V": "Å^3"
        }
      },
      "description": "Optimized lattice constants from DFT geometry optimization for all four compounds."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "CuAlS2": "object with uncorrected_band_gap",
          "CuGaS2": "object with uncorrected_band_gap",
          "CuInS2": "object with uncorrected_band_gap",
          "AgGaS2": "object with uncorrected_band_gap"
        },
        "units": {
          "uncorrected_band_gap": "eV"
        }
      },
      "description": "Uncorrected (raw GGA) band gaps for all four compounds."
    },
    {
      "file": "optical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "CuAlS2": "object with refractive_index_n0 and sellmeier_params",
          "CuGaS2": "object with refractive_index_n0 and sellmeier_params",
          "CuInS2": "object with refractive_index_n0 and sellmeier_params",
          "AgGaS2": "object with refractive_index_n0 and sellmeier_params"
        },
        "units": {
          "refractive_index_n0": "dimensionless",
          "sellmeier_params.A": "dimensionless",
          "sellmeier_params.B": "dimensionless",
          "sellmeier_params.C": "nm",
          "sellmeier_params.D": "nm^-2"
        }
      },
      "description": "Refractive index at zero energy and Sellmeier equation parameters from scissor-corrected dielectric function."
    }
  ],
  "notes": "The scissor shift uses the provided experimental band gap values; the agent must compute it from the uncorrected gap of step2 and apply it to the dielectric function. All scored quantities are compared to the paper's own calculated values with per-quantity tolerances."
}
```

## How you are scored
A hidden verifier reads the three JSON files from `/app/outputs`. It evaluates each artifact against a reference set for the four compounds, assigns partial scores, and combines them into a final reward (0 to 1). The weight distribution is:

- `optimized_lattice_constants.json`: 0.3
- `band_gaps.json`: 0.3
- `optical_properties.json` (refractive index n₀ and Sellmeier parameters): 0.4, split equally between n₀ (0.2) and the sellmeier_params (0.2).

The verifier’s comparison is designed to reward honest DFT reproduction; small numerical differences that arise from legitimate computational choices (e.g., pseudopotentials, convergence, implementation details) are expected and do not penalize a correct solve. You must execute the complete workflow — simply reporting the paper’s numbers is not sufficient and will not achieve a high score.
