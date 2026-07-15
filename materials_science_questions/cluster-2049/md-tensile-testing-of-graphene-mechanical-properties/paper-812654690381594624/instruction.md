# Compute bacterial cell wall plane-strain modulus from graphene wrinkle wavelengths

## Problem background
When a graphene sheet covers a bacterial cell and the cell undergoes vacuum‑induced shrinkage, confined wrinkles form on the graphene surface. The wrinkle wavelength is determined by the stiffness of the underlying substrate — the bacterial cell wall — through the Föppl–von Kármán buckling model for a thin film on a compliant substrate. The plane‑strain modulus of the cell wall can therefore be extracted from the measured wrinkle wavelengths, the geometry of the bacterial deformation, and the known properties of graphene.

## Approach
The computation proceeds in three stages. First, average wrinkle wavelengths are obtained from raw peak count data. For the AFM measurement, the number of wrinkle peaks counted in sequential 200‑nm segments along eight height‑scan lines on a single bacterium yields the average AFM wavelength. For the FESEM measurement, the number of peaks per transverse line and the wrinkle‑region diameter for eight individual bacteria are used to compute the average FESEM wavelength. Second, the Föppl–von Kármán buckling model for a thin elastic film on a compliant substrate is applied. Given the heights of the bacterium before and after vacuum and the widths of the wrinkled region, the arc lengths of the graphene profile are determined, from which the compressive strain in the graphene is computed. The substrate strain and a pre‑stretch factor S are then derived. Third, the wavelength–modulus relation from the buckling model is inverted to obtain the plane‑strain modulus of the bacterial cell wall. This yields two independent estimates — one from the AFM wavelength and one from the FESEM wavelength — that are reported in a JSON file.

## Reproduction target
From the raw AFM and FESEM peak count data and geometric parameters provided in the instructions, compute the average wrinkle wavelengths for both imaging modalities. Then, using the Föppl–von Kármán buckling model, compute the bacterial cell wall plane‑strain moduli corresponding to each wavelength. Produce the two moduli, expressed in MPa, and write them to a JSON file as described in the output contract.

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Compute average AFM wrinkle wavelength
- Role: process
- Action: From the raw AFM peak count data (provided in the instructions as Table S1: number of peaks per 200-nm segment for 8 lines), compute the average wrinkle wavelength λ_AFM. For each line, sum peaks over the 800 nm length, then average across lines. Report the result in nanometers to one decimal place. Write the value to afm_wavelength.json.
- Evidence: `/app/outputs/afm_wavelength.json`

### Step 2: Compute average FESEM wrinkle wavelength
- Role: process
- Action: From the raw FESEM peak count data (Table S2: number of peaks per line for 8 bacteria, Table S3: wrinkle region diameters Dw), compute the wrinkle wavelength for each bacterium as Dw / (average number of peaks per line), then average over all 8 bacteria. Report the result in nanometers to one decimal place. Write the value to fesem_wavelength.json.
- Evidence: `/app/outputs/fesem_wavelength.json`

### Step 3: Compute bacterial cell wall plane-strain moduli
- Role: scored (load-bearing)
- Action: Using the computed AFM wavelength (from step_compute_afm_wavelength) and FESEM wavelength (from step_compute_fesem_wavelength), together with the provided geometric parameters (H = 0.279 μm, h = 0.186 μm, Dc = 1.1 μm, Dw = 0.628 μm) and graphene material properties (Eg = 1 TPa, νg = 0.165, t = 0.355 nm), apply the Föppl–von Kármán buckling model: (1) compute arc lengths and compressive strain, (2) compute substrate strain and pre-stretch factor S, (3) invert the buckling wavelength–modulus relation to obtain the plane-strain modulus of the bacterial cell wall for each wavelength. Write the two moduli (in MPa) to plane_strain_moduli.json with keys "EB_AFM_MPa" and "EB_FESEM_MPa".
- Output file: `/app/outputs/plane_strain_moduli.json`
- Format: json
- Contract: {"EB_AFM_MPa": "number", "EB_FESEM_MPa": "number"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/plane_strain_moduli.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### plane_strain_moduli.json
- path: `/app/outputs/plane_strain_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Plane-strain modulus of bacterial cell wall computed from the AFM and FESEM wrinkle wavelengths via the Föppl–von Kármán buckling model. Checker compares against hidden reference values derived from the same raw data.
- schema:
  - `type`: object
  - `required`:
    - `EB_AFM_MPa`: float
    - `EB_FESEM_MPa`: float
  - `units`:
    - `EB_AFM_MPa`: MPa
    - `EB_FESEM_MPa`: MPa

Notes: The two moduli correspond to the two independent wrinkle wavelength measurements (AFM and FESEM). Both must be within a relative tolerance of the hidden reference values to earn full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "plane_strain_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "EB_AFM_MPa": "float",
          "EB_FESEM_MPa": "float"
        },
        "units": {
          "EB_AFM_MPa": "MPa",
          "EB_FESEM_MPa": "MPa"
        }
      },
      "description": "Plane-strain modulus of bacterial cell wall computed from the AFM and FESEM wrinkle wavelengths via the Föppl–von Kármán buckling model. Checker compares against hidden reference values derived from the same raw data."
    }
  ],
  "notes": "The two moduli correspond to the two independent wrinkle wavelength measurements (AFM and FESEM). Both must be within a relative tolerance of the hidden reference values to earn full credit."
}
```

## How you are scored
Your submission will be scored by a hidden verifier. The verifier independently recomputes the bacterial cell wall plane‑strain moduli from the same raw data tables using the same analytical model, and compares your reported values to its references. The reward is a weighted sum across all scored artifacts, with the two moduli carrying the majority weight; full credit is earned when both of your computed moduli agree closely with the verifier’s recomputed values.
