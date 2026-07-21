# Piezoelectric Field and Pressure Coefficients of Light Emission in III-Nitride Heterostructures

## Problem background
Wurtzite III‑nitride heterostructures (such as InGaN/GaN and GaN/AlGaN) possess large spontaneous and piezoelectric polarizations that create strong built‑in electric fields along the c‑axis. These fields induce the quantum‑confined Stark effect (QCSE), bending the band edges and reducing the optical transition energy. Under hydrostatic pressure, the strain and the electric fields change, causing a pressure-dependent shift of the emission energy. The pressure coefficient dE_E/dP of the fundamental optical transition is known to depend sensitively on the quantum‑well thickness and composition. In contrast, cubic III‑nitride structures grown along [001] have no spontaneous or piezoelectric polarization and therefore no internal electric fields, so their pressure response is expected to be different.

This task investigates these effects computationally by modeling the strain, polarization, electric fields, and electronic states under hydrostatic pressure for three quantum‑well systems: wurtzite GaN/AlGaN, wurtzite InGaN/GaN, and cubic InGaN/GaN. The goal is to compute the pressure coefficient dE_E/dP as a function of well width and the built‑in electric field at selected pressures.

## Approach
The model combines anisotropic linear elasticity with the k·p method. First, the strain tensor components in every layer are calculated for pressures from 0 to 10 GPa, assuming pseudomorphic growth and that the in-plane strain is set by a thick substrate (sapphire for wurtzite, SiC for cubic). For the wurtzite structures, the resulting strain is used with strain‑dependent piezoelectric constants and the spontaneous polarization to compute the total macroscopic polarization and the electrostatic built‑in electric field in the quantum wells and barriers. For the cubic structures the internal electric field is zero by symmetry.

Next, the one‑dimensional effective‑mass Schrödinger equation is solved for electrons and heavy holes in the quantum well, including the effect of the internal electric field (if present) and the strain‑induced shifts of the band edges. The fundamental optical transition energy is obtained at each pressure. A linear fit of this energy versus pressure yields dE_E/dP for each well width. The procedure is repeated for all three material systems and for the required well‑width ranges.

## Reproduction target
Implement a computational workflow that computes and writes the following results to the indicated JSON files under `/app/outputs`:

1. **`step_01_gaaln_results.json`** – For wurtzite GaN/Al₀.₁₇Ga₀.₈₃N multiple quantum wells with well widths of 6, 10, 16, 24, and 32 monolayers: the pressure coefficient dE_E/dP (meV/GPa), the well thickness in nm, and the built‑in electric field in the 8 nm (32 ML) well at 0 GPa and 10 GPa (MV/cm).
2. **`step_02_ingan_wurtzite_results.json`** – For wurtzite In₀.₂Ga₀.₈N/GaN quantum wells with well widths of 1, 2, 2.5, 3.5, 4, and 5 nm: the pressure coefficient dE_E/dP (meV/GPa).
3. **`step_03_ingan_cubic_results.json`** – For cubic In₀.₁Ga₀.₉N/GaN quantum wells with well widths of 0.6, 1, 2, 3, 4, and 5 nm: the pressure coefficient dE_E/dP (meV/GPa).

Each output file must follow the exact schema described in the steps below.

## Assets

- numpy: numpy
- scipy: scipy
- Elastic constants of wurtzite III-N (Wright, JAP 1997): 10.1063/1.364390
- Strain-dependent piezoelectric constants (Shimada et al., JJAP 1998): 10.1143/JJAP.37.L1421
- Spontaneous polarization values (Bernardini & Fiorentini, PRB 2001): 10.1103/PhysRevB.64.085207
- III-N band parameters (Vurgaftman et al., JAP 2001): 10.1063/1.1368672
- Elastic constants of sapphire (Al2O3)
- Elastic constants of cubic SiC

## Workflow steps

### Step 1: Compute strain under hydrostatic pressure
- Role: process
- Action: Using anisotropic linear elasticity, calculate the strain tensor components in each layer of the wurtzite (on sapphire) and cubic (on SiC) heterostructures for pressures 0–10 GPa, assuming pseudomorphic growth and in-plane strain set by the substrate. For wurtzite GaN/AlGaN, include well widths from 6 to 32 monolayers; for wurtzite InGaN/GaN, include well widths 1–5 nm; for cubic InGaN/GaN, include well widths 0.6–5 nm.
- Evidence: `/app/outputs/strain_output.json`

### Step 2: Calculate piezoelectric polarization and internal electric fields (wurtzite only)
- Role: process
- Action: For the wurtzite GaN/AlGaN and InGaN/GaN structures, use the strain tensors from step_strain together with strain‑dependent piezoelectric constants (Shimada 1998) and spontaneous polarizations (Bernardini 2001) to compute the total polarization and the built‑in electric field in the quantum well and barriers. Compute for each well width and each pressure.
- Evidence: `/app/outputs/field_profile.json`

### Step 3: GaN/AlGaN pressure coefficients and fields
- Role: scored (load-bearing)
- Action: Solve the one‑dimensional effective‑mass Schrödinger equation for electrons and heavy holes in each GaN quantum well of the wurtzite GaN/AlGaN MQW structure at pressures 0–10 GPa, using the electric field profile from step_polarization_field. Perform a linear fit of the fundamental transition energy vs pressure to extract dE_E/dP for each well width (6–32 ML). Record also the electric field in the 8 nm well at 0 and 10 GPa.
- Output file: `/app/outputs/step_01_gaaln_results.json`
- Format: json
- Contract: List of objects: each object has keys well_width_ML (int), thickness_nm (float), dE_dP_meV_per_GPa (float), field_0_GPa_MV_per_cm (float), field_10_GPa_MV_per_cm (float).
- Scoring: scored by hidden verifier

### Step 4: Wurtzite InGaN/GaN pressure coefficients
- Role: scored
- Action: Using the field profile from step_polarization_field for the wurtzite In0.2Ga0.8N/GaN QWs, solve the effective‑mass equations and obtain dE_E/dP (meV/GPa) for each well width (1–5 nm) by linear fitting of transition energy vs pressure.
- Output file: `/app/outputs/step_02_ingan_wurtzite_results.json`
- Format: json
- Contract: List of objects: each object has keys well_width_nm (float), dE_dP_meV_per_GPa (float).
- Scoring: scored by hidden verifier

### Step 5: Cubic InGaN/GaN pressure coefficients
- Role: scored
- Action: For the cubic In0.1Ga0.9N/GaN QWs (zero internal electric field), solve the effective‑mass equations using the strain state from step_strain to adjust the band gap via hydrostatic deformation potentials. Compute dE_E/dP for each well width (0.6–5 nm) by linear fitting.
- Output file: `/app/outputs/step_03_ingan_cubic_results.json`
- Format: json
- Contract: List of objects: each object has keys well_width_nm (float), dE_dP_meV_per_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_gaaln_results.json`
- `/app/outputs/step_02_ingan_wurtzite_results.json`
- `/app/outputs/step_03_ingan_cubic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_gaaln_results.json
- path: `/app/outputs/step_01_gaaln_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pressure coefficients dE_E/dP and built-in electric fields for GaN/Al0.17Ga0.83N quantum wells of thicknesses 6–32 monolayers; field values only required for the 8 nm well (others may be null).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `well_width_ML`, `thickness_nm`, `dE_dP_meV_per_GPa`, `field_0_GPa_MV_per_cm`, `field_10_GPa_MV_per_cm`

### step_02_ingan_wurtzite_results.json
- path: `/app/outputs/step_02_ingan_wurtzite_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pressure coefficients dE_E/dP for wurtzite In0.2Ga0.8N/GaN quantum wells with well widths 1–5 nm.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `well_width_nm`, `dE_dP_meV_per_GPa`

### step_03_ingan_cubic_results.json
- path: `/app/outputs/step_03_ingan_cubic_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pressure coefficients dE_E/dP for cubic In0.1Ga0.9N/GaN quantum wells with well widths 0.6–5 nm.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `well_width_nm`, `dE_dP_meV_per_GPa`

Notes: Reproduces the computational model for strain-induced piezoelectric polarization and resulting pressure coefficients of optical transition energies in wurtzite InGaN/GaN, GaN/AlGaN, and cubic InGaN/GaN quantum wells.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_gaaln_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "well_width_ML",
            "thickness_nm",
            "dE_dP_meV_per_GPa",
            "field_0_GPa_MV_per_cm",
            "field_10_GPa_MV_per_cm"
          ]
        }
      },
      "description": "Pressure coefficients dE_E/dP and built-in electric fields for GaN/Al0.17Ga0.83N quantum wells of thicknesses 6–32 monolayers; field values only required for the 8 nm well (others may be null)."
    },
    {
      "file": "step_02_ingan_wurtzite_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "well_width_nm",
            "dE_dP_meV_per_GPa"
          ]
        }
      },
      "description": "Pressure coefficients dE_E/dP for wurtzite In0.2Ga0.8N/GaN quantum wells with well widths 1–5 nm."
    },
    {
      "file": "step_03_ingan_cubic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "well_width_nm",
            "dE_dP_meV_per_GPa"
          ]
        }
      },
      "description": "Pressure coefficients dE_E/dP for cubic In0.1Ga0.9N/GaN quantum wells with well widths 0.6–5 nm."
    }
  ],
  "notes": "Reproduces the computational model for strain-induced piezoelectric polarization and resulting pressure coefficients of optical transition energies in wurtzite InGaN/GaN, GaN/AlGaN, and cubic InGaN/GaN quantum wells."
}
```

## How you are scored
A hidden verifier checks each required output file independently and assigns a score per artifact. It compares your reported pressure coefficients and electric fields to reference values (derived from the published model results) using appropriate tolerances that allow for numerical differences between implementations. The verifier also checks for the expected qualitative trends (e.g., the thickness dependence of dE_E/dP). The final reward is a weighted combination of the per‑artifact scores; all artifacts must be present and correctly formatted. Bypassing the physics‑based workflow (e.g., by copying numbers without performing the strain, polarization, and Schrödinger‑equation calculations) will not produce valid results and will earn zero credit.
