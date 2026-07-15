# Luminescence Enhancement and Optical Losses in Quantum-Well Structures with Metallic Gratings via FED

## Problem background
Spontaneous light emission from InGaN quantum wells (QWs) placed close to a metallic layer can be strongly enhanced through coupling to surface plasmons. However, the metal also introduces optical absorption losses that can counteract the benefit. This work quantifies the luminescence enhancement and the associated absorption losses in a GaN-based QW structure that incorporates a silver grating, comparing three configurations: a flat semiconductor reference (no metal), a planar metal layer, and a periodically grated metal layer.

## Approach
Use the fluctuational electrodynamics (FED) framework, which treats spontaneous emission as stochastic current sources inside the QW. The total electric field in a grated multilayer is expressed through a recursive Green's function series that accounts for scattering by the grating periodicity. Implement the recursive method to order n=3 for transverse-magnetic (TM) polarization, averaging equally over x- and z-oriented dipole sources in the QW plane. For each structure, compute the angle-resolved luminescence intensity, integrate the power over the light cone (|K| < k0) at a single target wavelength, and extract energy fluxes in the GaN barrier above the QW and in the air region. From these, derive the two main quantities: (1) the luminescence enhancement factor, the ratio of the total emitted power from the grated metallic structure to that from the flat semiconductor reference, and (2) the absorption loss fraction, (P_GaN − P_air)/P_GaN, for both the ungrated and grated metallic structures. The required multilayer geometry consists of GaN(10 nm)/In0.12Ga0.88N(2 nm QW)/GaN(3 μm)/sapphire, with the QW positioned 1 nm below the GaN/silver interface. The metal layer is silver (thickness 17 nm) and the grating is a one-dimensional square-wave with period 200 nm and 50% duty cycle. Dielectric functions for GaN, InGaN, and Ag are taken from published literature as listed in the Assets section.

## Reproduction target
Compute and submit two JSON artifacts: (i) the luminescence enhancement factor (ratio defined above) at λ ≈ 540 nm for the grated metallic structure relative to the flat semiconductor reference, and (ii) the absorption loss percentages for both the ungrated (planar) and grated silver structures at the same wavelength. The enhancement factor is evaluated by integrating the total emitted power over the light cone; the absorption loss uses the net power flux in the GaN barrier and in air. All computations use TM polarization and equal x- and z-dipole averaging.

## Assets

- Optical constants of GaN and InGaN (Leung et al. 1998): 10.1063/1.368831
- Optical constants of Ag (Lynch & Hunter 1985)
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Reference flat semiconductor simulation
- Role: process
- Action: Implement the fluctuational electrodynamics (FED) recursive Green's function method with recursion order n=3 for the flat semiconductor structure (no metal layer): GaN(10 nm) / InGaN(2 nm QW) / GaN(3 μm) / sapphire. Use TM-polarized point current sources with both x- and z-dipole orientations in the QW plane (equally weighted). Compute the angle-resolved luminescence and integrate the power over the light cone (|K| < k0) at wavelength 540 nm to obtain the total emitted power P_ref_total.
- Evidence: `/app/outputs/ref_total_power.json`

### Step 2: Ungrated metallic structure simulation
- Role: process
- Action: Implement the FED recursive Green's function method (order n=3) for the ungrated metallic structure: Ag(17 nm planar) / GaN(10 nm) / InGaN(2 nm QW) / GaN(3 μm) / sapphire. Use the same TM-polarized sources. Compute the net energy fluxes P_GaN (in GaN barrier above QW) and P_air (into air) at wavelength 540 nm.
- Evidence: `/app/outputs/ungrated_metal_powers.json`

### Step 3: Grated metallic structure simulation
- Role: process
- Action: Implement the FED recursive Green's function method (order n=3) for the grated metallic structure: a one-dimensional square-wave silver grating (period 200 nm, 50% duty cycle, thickness 17 nm) on the same underlying layers. Use TM-polarized sources. Compute at 540 nm: (a) total emitted power integrated over the light cone, P_total_gr, and (b) net fluxes P_GaN_gr, P_air_gr.
- Evidence: `/app/outputs/grated_metal_powers.json`

### Step 4: Compute luminescence enhancement factor
- Role: scored (load-bearing)
- Action: Using the total emitted powers from steps 1 and 3, compute the enhancement factor as enhancement_factor = P_total_gr / P_ref_total at wavelength 540 nm. Write a JSON object to /app/outputs/enhancement_factor.json with keys "wavelength_nm" (number) and "enhancement_factor" (number).
- Output file: `/app/outputs/enhancement_factor.json`
- Format: json
- Contract: {"type": "object", "required": {"wavelength_nm": "number", "enhancement_factor": "number"}}
- Scoring: scored by hidden verifier

### Step 5: Compute absorption losses
- Role: scored (load-bearing)
- Action: Using P_GaN_ungr, P_air_ungr from step 2 and P_GaN_gr, P_air_gr from step 3, compute ungrated_loss = (P_GaN_ungr − P_air_ungr) / P_GaN_ungr and grated_loss = (P_GaN_gr − P_air_gr) / P_GaN_gr, expressed as percentages. Write a JSON object to /app/outputs/absorption_loss.json with keys "wavelength_nm" (number), "ungrated_loss" (number), "grated_loss" (number).
- Output file: `/app/outputs/absorption_loss.json`
- Format: json
- Contract: {"type": "object", "required": {"wavelength_nm": "number", "ungrated_loss": "number", "grated_loss": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enhancement_factor.json`
- `/app/outputs/absorption_loss.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enhancement_factor.json
- path: `/app/outputs/enhancement_factor.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Luminescence enhancement factor at λ=540 nm; higher is better, meeting or exceeding the paper's result earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `wavelength_nm`: number
    - `enhancement_factor`: number

### absorption_loss.json
- path: `/app/outputs/absorption_loss.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Absorption loss percentages at λ=540 nm; lower is better, meeting or undershooting the paper's losses earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `wavelength_nm`: number
    - `ungrated_loss`: number
    - `grated_loss`: number

Notes: All quantities are for TM polarization and averaged over x- and z-oriented dipole sources in the quantum well. The grating period is 200 nm with a 50% duty cycle. The silver and GaN/InGaN permittivities are taken from the public references listed in resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enhancement_factor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "wavelength_nm": "number",
          "enhancement_factor": "number"
        }
      },
      "description": "Luminescence enhancement factor at λ=540 nm; higher is better, meeting or exceeding the paper's result earns full credit."
    },
    {
      "file": "absorption_loss.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "wavelength_nm": "number",
          "ungrated_loss": "number",
          "grated_loss": "number"
        }
      },
      "description": "Absorption loss percentages at λ=540 nm; lower is better, meeting or undershooting the paper's losses earns full credit."
    }
  ],
  "notes": "All quantities are for TM polarization and averaged over x- and z-oriented dipole sources in the quantum well. The grating period is 200 nm with a 50% duty cycle. The silver and GaN/InGaN permittivities are taken from the public references listed in resources."
}
```

## How you are scored
A hidden verifier will independently compare your submitted enhancement factor and absorption loss values against reference gold values derived from the original study. The comparison uses tolerances and directional policies: meeting or exceeding the reference performance (higher enhancement factor, lower loss) earns full credit; deviation degrades credit monotonically. Both metrics contribute to a single combined reward score. Simply reporting the gold numbers without executing the simulation pipeline will not score well against the hidden checks.
