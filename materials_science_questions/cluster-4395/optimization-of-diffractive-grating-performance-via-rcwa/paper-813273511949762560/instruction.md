# Subwavelength Grating Plasmonic Sensitivity via FDTD

## Problem background
Surface plasmon resonance (SPR) sensing is a leading technology for label-free biosensing. One promising direction is to use a lamellar grating of highly doped semiconductors as the active region, operating in the mid-infrared. The period is chosen to be sub-wavelength relative to the plasma wavelength, which excites localized surface plasmon (LSP) modes propagating vertically into the slits. The task is to evaluate the sensitivity of such a grating by computing the shift of the LSP resonance when the refractive index of the dielectric filling the slits changes.

## Approach
Use a finite-difference time-domain (FDTD) simulation to model the optical response of the lamellar grating under TM polarization at normal incidence. The structure consists of alternating strips of a Drude-model semiconductor (plasma wavelength near 6 µm) and slits filled with a dielectric. Geometry: period = 520 nm, slit and ribbon widths both 260 nm, thickness = 1 µm. Run two simulations with slit refractive indices of 1.5 and 1.51. From the transmittance spectrum, identify the wavelength of the transmission dip that corresponds to the LSP resonance. Compute the shift in resonance wavelength and the corresponding sensitivity Δλ/Δn.

## Reproduction target
Compute the LSP resonance wavelengths (in nm) for slit dielectric indices of 1.5 and 1.51, under TM polarization at normal incidence. From these, compute the resonance shift (difference, in nm) and the sensitivity (shift divided by the index change of 0.01, in nm/RIU). All values must be extracted from the FDTD-computed transmittance dip and written to the required output file.

## Assets

- MEEP FDTD solver: https://github.com/NanoComp/meep

## Workflow steps

### Step 1: FDTD simulation and sensitivity analysis
- Role: scored
- Action: Run FDTD simulation of the lamellar grating at normal incidence under TM polarization. Set geometry: period d=520 nm, slit and ribbon widths a=b=260 nm, thickness h=1 μm. Model the doped semiconductor with a Drude dielectric function: ε(ω)=1−ωp²/(ω²+iγω) with plasma wavelength λp=6 μm. Use two values for the refractive index of the slit dielectric: n=1.5 and n=1.51. From the computed transmittance spectra, identify the wavelength of the transmission dip that corresponds to the localized surface plasmon (LSP) resonance. Record the resonance wavelengths for each index. Calculate the resonance red shift Δλ and the sensitivity S=Δλ/Δn (with Δn=0.01). Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: resonance_n1.5 (float, in nm), resonance_n1.51 (float, in nm), shift_nm (float, in nm), sensitivity_nm_per_RIU (float, in nm/RIU).
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
- target_policy: exact_match
- description: FDTD-computed LSP resonance red shift and sensitivity for the bare lamellar grating. The checker compares shift_nm and sensitivity_nm_per_RIU to reference values within hidden tolerances, and reserves the right to audit resonance wavelengths for plausibility.
- schema:
  - `type`: object
  - `required`:
    - `resonance_n1.5`: float, unit nm
    - `resonance_n1.51`: float, unit nm
    - `shift_nm`: float, unit nm
    - `sensitivity_nm_per_RIU`: float, unit nm/RIU

Notes: Only TM polarization at normal incidence is required. Drude damping γ may be assumed small (e.g., 0.01ωp); the agent should choose an FDTD resolution sufficient to resolve the 6 μm resonance.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "resonance_n1.5": "float, unit nm",
          "resonance_n1.51": "float, unit nm",
          "shift_nm": "float, unit nm",
          "sensitivity_nm_per_RIU": "float, unit nm/RIU"
        }
      },
      "description": "FDTD-computed LSP resonance red shift and sensitivity for the bare lamellar grating. The checker compares shift_nm and sensitivity_nm_per_RIU to reference values within hidden tolerances, and reserves the right to audit resonance wavelengths for plausibility."
    }
  ],
  "notes": "Only TM polarization at normal incidence is required. Drude damping γ may be assumed small (e.g., 0.01ωp); the agent should choose an FDTD resolution sufficient to resolve the 6 μm resonance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the output artifact /app/outputs/results.json. The verifier checks the reported numerical quantities against reference criteria (e.g., tolerance intervals) defined in a hidden grading specification. It computes a score for each scored artifact according to the rubric, then combines them into a final reward. The checks compare your computed shift and sensitivity against expected plasmonic behavior; they reward genuine FDTD simulation results. The grading weights and exact tolerance values are not disclosed.
