# Optimization of Diffractive Grating Performance via RCWA Simulations

## Problem background
Dichromatic white light-emitting diodes (white LEDs) combine a blue LED with a yellow phosphor to produce white light. Their efficiency is limited by light extraction losses at the encapsulation/air interface: the refractive-index mismatch between the PDMS encapsulation layer (n ≈ 1.45) and air (n = 1.0) causes Fresnel reflection and total internal reflection, trapping a fraction of the generated light. Introducing periodic textured structures on the encapsulation surface can reduce these losses and improve the overall light output. This task simulates the light extraction behaviour of four families of periodic textures on PDMS using the rigorous coupled-wave analysis (RCWA) method, with the goal of identifying the texture geometry that yields the highest light extraction efficiency enhancement for yellow light (550 nm) and evaluating the resulting enhancement at blue (455 nm) and across the visible spectrum.

## Approach
RCWA is used to compute the angular transmittance of a textured PDMS slab illuminated from the inside by randomly polarized light. The slab is modelled as infinite in thickness (no back‑side reflection) with a periodic surface texture facing air. For each texture and wavelength, the simulation yields transmittance versus incidence angle for s‑ and p‑polarized light; the transmittance for randomly polarized light is obtained by averaging the two polarizations. Light extraction efficiency (η) is defined as the square of the average transmittance over incidence angles 0–89°:

  η = [ (1/90) Σ_{θ=0°}^{89°} T(θ) ]²

where T(θ) is the transmittance at incident angle θ. The enhancement of a textured structure relative to a flat PDMS reference is

  Enhancement (%) = [ (η_textured – η_flat) / η_flat ] × 100 .

The four texture families tested are: nanorods (duty 0.5), inverted rods (duty 0.5), hexagonally close-packed pyramids, and hexagonally close-packed inverted pyramids. For each family, period P ranges from 200 nm to 900 nm and depth D from 200 nm to 1500 nm. The workflow first computes the flat PDMS baseline efficiency at 455 nm and 550 nm. Then it performs a parameter sweep at 550 nm to find the texture and (P,D) that maximize the yellow‑light enhancement. After identifying the optimal configuration, it calculates the enhancement at 455 nm and 550 nm for that structure and produces a wavelength‑dependent enhancement spectrum from 400 nm to 700 nm.

## Reproduction target
1. Perform RCWA simulations for the four texture families at 550 nm over the specified period and depth ranges, compute the light extraction efficiency enhancement relative to a flat PDMS reference, and identify the texture type and geometric parameters (period, depth) that give the largest enhancement. Write the result to step_01_best_params.json.
2. For the optimal structure from (1), compute the RCWA enhancement at 455 nm and 550 nm relative to the flat PDMS baseline. Write the two values as a CSV with columns wavelength_nm and enhancement_percent to step_02_enhancement_values.csv.
3. For the same optimal structure, compute the enhancement spectrum over 400–700 nm (step no coarser than 10 nm) and write the result to step_03_enhancement_spectrum.csv.

## Assets

- RCWA solver (e.g., S4, Python RCWA package): https://github.com/facebookincubator/s4 (or pip install rcwa)

## Workflow steps

### Step 1: Compute flat PDMS reference light extraction efficiency
- Role: process
- Action: Use RCWA to calculate angular transmittance for a flat PDMS slab (refractive index ≈1.45) at wavelengths 455 nm and 550 nm, and compute the reference light extraction efficiency η_ref using the scalar metric defined as the square of the average transmittance over incidence angles 0–89° for randomly polarized light (averaging s- and p-polarized outputs).
- Evidence: `/app/outputs/flat_baseline.json`

### Step 2: Parameter sweep for yellow light extraction at 550 nm
- Role: process
- Action: For four closely-packed periodic texture families (nanorods duty 0.5, inverted rods duty 0.5, hexagonally-close-packed pyramids, hexagonally-close-packed inverted pyramids), perform RCWA simulations at λ=550 nm over period P from 200 to 900 nm and depth D from 200 to 1500 nm. For each (P,D) and texture, compute extraction efficiency η and the enhancement relative to the flat PDMS baseline. Record the enhancement values in a structured dataset to be used for identifying the optimal structure in the next step.
- Evidence: `/app/outputs/sweep_results.json`

### Step 3: Report optimal texture and parameters for yellow light
- Role: scored (load-bearing)
- Action: From the sweep data produced in step 02, identify the texture family and the period/depth that give the maximum enhancement at 550 nm. Write the texture name, period (nm), and depth (nm) to the output file.
- Output file: `/app/outputs/step_01_best_params.json`
- Format: json
- Contract: {"texture": "<texture_name>", "period_nm": <integer>, "depth_nm": <integer>}
- Scoring: scored by hidden verifier

### Step 4: Report enhancement values at key wavelengths for optimal structure
- Role: scored
- Action: For the optimal texture and parameters identified in step 03, compute the RCWA light extraction enhancement at wavelengths 455 nm and 550 nm relative to the flat PDMS baseline obtained in step 01. Write a CSV with columns 'wavelength_nm' and 'enhancement_percent'.
- Output file: `/app/outputs/step_02_enhancement_values.csv`
- Format: csv
- Contract: A CSV with columns `wavelength_nm,enhancement_percent`. Must contain exactly two rows: one for 455 nm and one for 550 nm, with values computed by RCWA.
- Scoring: scored by hidden verifier

### Step 5: Simulate wavelength‑dependent enhancement spectrum for optimal inverted pyramid
- Role: process
- Action: Using RCWA, compute the light extraction efficiency of the optimal inverted pyramid (period 500 nm, depth 900 nm) at wavelengths from 400 nm to 700 nm (step no coarser than 10 nm). For each wavelength, compute the enhancement relative to the flat PDMS baseline calculated at that wavelength (extend the baseline calculation from step 01). Store the raw transmittances or enhancement per wavelength for use in the next step.
- Evidence: `/app/outputs/spectrum_raw.json`

### Step 6: Report enhancement spectrum
- Role: scored (load-bearing)
- Action: From the wavelength‑dependent enhancement data produced in step 05, write a CSV file containing the enhancement in percent versus wavelength. Cover the range 400–700 nm with a step no coarser than 10 nm.
- Output file: `/app/outputs/step_03_enhancement_spectrum.csv`
- Format: csv
- Contract: wavelength_nm,enhancement_percent
400,<value>
410,<value>
...
700,<value>
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_best_params.json`
- `/app/outputs/step_02_enhancement_values.csv`
- `/app/outputs/step_03_enhancement_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_best_params.json
- path: `/app/outputs/step_01_best_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimal texture type and geometric parameters that maximize yellow‑light extraction at 550 nm, as determined from the RCWA parameter sweep.
- schema:
  - `type`: object
  - `required`:
    - `texture`: string (one of: nanorod, inverted_rod, pyramid, inverted_pyramid)
    - `period_nm`: integer (nm)
    - `depth_nm`: integer (nm)

### step_02_enhancement_values.csv
- path: `/app/outputs/step_02_enhancement_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Light extraction efficiency enhancements at 455 nm and 550 nm for the optimal inverted pyramid, compared against hidden reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `enhancement_percent`
  - `units`:
    - `wavelength_nm`: nm
    - `enhancement_percent`: %

### step_03_enhancement_spectrum.csv
- path: `/app/outputs/step_03_enhancement_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Enhancement spectrum from 400 to 700 nm for the optimal inverted pyramid; audited for shape (peak near 550 nm, monotonic fall-off) and a hidden value around 490 nm.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `enhancement_percent`
  - `units`:
    - `wavelength_nm`: nm
    - `enhancement_percent`: %

Notes: All gold values are taken from the paper's Table 1 and Fig. 6b. The exact optimal parameters (texture, period, depth) are checked. Enhancement values at 455/550 nm are compared with tolerance. The spectrum is checked for structural consistency and a sample value at 490 nm.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_best_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "texture": "string (one of: nanorod, inverted_rod, pyramid, inverted_pyramid)",
          "period_nm": "integer (nm)",
          "depth_nm": "integer (nm)"
        }
      },
      "description": "Optimal texture type and geometric parameters that maximize yellow‑light extraction at 550 nm, as determined from the RCWA parameter sweep."
    },
    {
      "file": "step_02_enhancement_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "enhancement_percent"
        ],
        "units": {
          "wavelength_nm": "nm",
          "enhancement_percent": "%"
        }
      },
      "description": "Light extraction efficiency enhancements at 455 nm and 550 nm for the optimal inverted pyramid, compared against hidden reference values from the paper."
    },
    {
      "file": "step_03_enhancement_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "enhancement_percent"
        ],
        "units": {
          "wavelength_nm": "nm",
          "enhancement_percent": "%"
        }
      },
      "description": "Enhancement spectrum from 400 to 700 nm for the optimal inverted pyramid; audited for shape (peak near 550 nm, monotonic fall-off) and a hidden value around 490 nm."
    }
  ],
  "notes": "All gold values are taken from the paper's Table 1 and Fig. 6b. The exact optimal parameters (texture, period, depth) are checked. Enhancement values at 455/550 nm are compared with tolerance. The spectrum is checked for structural consistency and a sample value at 490 nm."
}
```

## How you are scored
A hidden verifier independently checks each of the three scored artifacts. For step_01_best_params.json, it compares the reported texture, period, and depth against a hidden reference derived from the source paper. For step_02_enhancement_values.csv, it compares the enhancement values at 455 nm and 550 nm to hidden reference values, allowing a tolerance that accounts for differences in RCWA implementation. For step_03_enhancement_spectrum.csv, it performs a structural audit: it checks that the enhancement spectrum peaks near 550 nm, falls off monotonically away from the peak, and compares a specific wavelength’s enhancement (not disclosed) to a hidden sample value. The verification does NOT require an exact match to the paper’s numbers; instead it checks that your independently computed results are consistent with the expected physical outcome and within reasonable bounds. The final reward is a weighted combination of the scores for the three outputs.
