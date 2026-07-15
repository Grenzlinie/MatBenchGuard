# Optimization of Solar Cell Efficiency via Coupled Optoelectronic Simulation

## Problem background
Thin-film photovoltaic solar cells can be made more efficient by incorporating a metallic back-reflector grating that is periodic along one lateral direction. The grating couples incident sunlight into guided-wave modes, increasing photon absorption in the semiconductor layers. The design problem involves multiple coupled variables — layer thicknesses, bandgap energies, and grating geometry — and the absorption enhancement interacts non-trivially with the charge-carrier transport that determines the electrical power output. This task reproduces the core computational evaluation that quantifies the solar-cell efficiency for one candidate optimal design, using a coupled optoelectronic simulation that models both the optical absorption and the electronic charge transport in a p-i-n semiconductor stack backed by a rectangular metallic grating.

## Approach
The workflow couples two physics models:

1. **Photonic step (RCWA):** The frequency-domain Maxwell equations are solved in two dimensions (x–z) using the rigorous coupled-wave approach (RCWA). The solar cell is illuminated by normally incident unpolarized light with the standard AM1.5G terrestrial solar spectrum. The optical calculation yields the electric field phasor throughout the cell, from which the position-dependent electron–hole-pair generation rate G(x,z) is obtained. The generation rate is then averaged over one grating period to produce a one-dimensional generation rate G(z) that varies only with depth.

2. **Electronic step (HDG):** The one-dimensional drift-diffusion equations (Poisson equation coupled with continuity equations for electrons and holes) are solved along the depth (z) direction using a hybridizable discontinuous Galerkin (HDG) method. The model includes Shockley-Read-Hall recombination. The solution produces the current density J as a function of the externally applied voltage Vext. By solving for a range of Vext, the full JV curve is obtained. The maximum power point on this curve determines the solar-cell efficiency.

## Reproduction target
Using the optimal design parameters listed below, run the coupled RCWA+HDG simulation to compute and report:

- The one-dimensional electron–hole-pair generation rate G(z) (averaged over the grating period) as a function of depth z.
- The current-density vs. voltage (JV) curve of the solar cell under AM1.5G illumination.
- The power-conversion efficiency η (%) defined as the ratio of the maximum electrical power density to the incident solar power density (1000 W m⁻²).

**Fixed optimal design parameters:**
- Grating period Lx = 632 nm
- Grating protrusion height Lg = 167 nm
- Protrusion fraction ζg = 0.3
- i-layer thickness Li = 596 nm
- p-layer bandgap Eg,p = 1.62 eV
- i-layer bandgap Eg,i = 1.467 eV
- n-layer bandgap Eg,n = 1.618 eV
- p-layer thickness Lp = 20 nm (doped with acceptor concentration 10¹⁷ cm⁻³)
- n-layer thickness Ln = 20 nm (doped with donor concentration 10¹⁷ cm⁻³)
- Total semiconductor thickness Lz = Lp + Li + Ln
- Grating metal: a representative metal with permittivity ε ≈ −22 + 0.4i at 680 nm (use realistic optical constants for a metal such as aluminum or silver).
- Groove dielectric: a realistic transparent dielectric (e.g. SiO₂, n≈1.5).
- CIGS electrical parameters: electron affinity χ = 4.5 eV, conduction/valence band densities of states Nc = 2.22×10¹⁸ cm⁻³, Nv = 1.78×10¹⁹ cm⁻³, DC relative permittivity εdc⁰ = 13.6, electron mobility μn = 100 cm² V⁻¹ s⁻¹, hole mobility μp = 25 cm² V⁻¹ s⁻¹, SRH lifetime parameters τn = τp = 1 ns.

The target is the efficiency obtained by an accurate implementation of the coupled optoelectronic model; no single “paper number” is provided as the goal — you must implement the methods faithfully and report the results your simulation produces.

## Assets

- AM1.5G solar spectrum (ASTM G173-03): https://www.nrel.gov/grid/solar-resource/spectra-am1.5.html
- CIGS optical constants
- Metal grating optical constants
- Dielectric material optical constants
- Python numerical libraries: numpy, scipy, matplotlib
- RCWA implementation

## Workflow steps

### Step 1: Compute 1D generation rate G(z)
- Role: scored
- Action: Using RCWA, simulate the electromagnetic field in the solar cell under AM1.5G illumination for the optimal design parameters (Lx=632 nm, Lg=167 nm, ζg=0.3, Li=596 nm, Eg,p=1.62 V, Eg,i=1.467 V, Eg,n=1.618 V). Calculate the electron-hole-pair generation rate G(x,z) and average over the x‑period to obtain G(z). Output the result as a CSV file.
- Output file: `/app/outputs/generation_rate.csv`
- Format: csv
- Contract: Two columns: 'z' (nm) and 'G' (cm⁻³ s⁻¹). z spans from 0 to Lz (approximately 636 nm for the optimal design). At least 100 equally spaced points.
- Scoring: scored by hidden verifier

### Step 2: Compute JV curve
- Role: scored
- Action: Solve the 1D drift-diffusion model with the HDG method using G(z) from step gen_rate. Apply a range of external voltages Vext from 0 V to slightly above the open-circuit voltage, in steps of ~0.01 V. For each Vext, compute the total current density J. Output the JV pairs.
- Output file: `/app/outputs/jv_curve.csv`
- Format: csv
- Contract: Two columns: 'Vext' (V) and 'J' (mA/cm²). At least 20 data points, Vext from 0 to approximately 0.8 V (or until current becomes negative).
- Scoring: scored by hidden verifier

### Step 3: Compute solar cell efficiency
- Role: scored (load-bearing)
- Action: From the JV curve, determine the maximum power density P_max = max(J * Vext) and compute the efficiency η = P_max / (1000 W m⁻²) expressed as a percentage. Output η.
- Output file: `/app/outputs/efficiency.txt`
- Format: txt
- Contract: Single floating-point number (e.g., 15.7).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/generation_rate.csv`
- `/app/outputs/jv_curve.csv`
- `/app/outputs/efficiency.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### generation_rate.csv
- path: `/app/outputs/generation_rate.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: 1D electron-hole-pair generation rate; audited for non‑negativity and monotonic decrease in z.
- schema:
  - `type`: table
  - `required_columns`: `z`, `G`
  - `units`:
    - `z`: nm
    - `G`: cm⁻³ s⁻¹

### jv_curve.csv
- path: `/app/outputs/jv_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: JV curve; audited for monotonic decrease of J with Vext and consistency with the maximum power point.
- schema:
  - `type`: table
  - `required_columns`: `Vext`, `J`
  - `units`:
    - `Vext`: V
    - `J`: mA/cm²

### efficiency.txt
- path: `/app/outputs/efficiency.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Solar cell efficiency; scored against a hidden gold value (≥ threshold earns full credit).
- schema:
  - `type`: text
  - `description`: Single floating-point number representing solar cell efficiency in percent.

Notes: All outputs are generated by a single evaluation of the optimal design under AM1.5G illumination. The hidden gold for efficiency is the paper-reported value; generation_rate.csv and jv_curve.csv are checked structurally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "generation_rate.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "G"
        ],
        "units": {
          "z": "nm",
          "G": "cm⁻³ s⁻¹"
        }
      },
      "description": "1D electron-hole-pair generation rate; audited for non‑negativity and monotonic decrease in z."
    },
    {
      "file": "jv_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vext",
          "J"
        ],
        "units": {
          "Vext": "V",
          "J": "mA/cm²"
        }
      },
      "description": "JV curve; audited for monotonic decrease of J with Vext and consistency with the maximum power point."
    },
    {
      "file": "efficiency.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing solar cell efficiency in percent."
      },
      "description": "Solar cell efficiency; scored against a hidden gold value (≥ threshold earns full credit)."
    }
  ],
  "notes": "All outputs are generated by a single evaluation of the optimal design under AM1.5G illumination. The hidden gold for efficiency is the paper-reported value; generation_rate.csv and jv_curve.csv are checked structurally."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently evaluates each workflow stage:

- `generation_rate.csv` is audited for structural consistency (non-negative values, physically plausible depth profile).
- `jv_curve.csv` is checked for monotonic decrease of current with voltage and internal consistency between the maximum power point and the extracted efficiency.
- `efficiency.txt` is compared to a hidden reference that captures the expected result of the coupled simulation. The efficiency is the primary (load-bearing) scored artifact.

The verifier does not expect a specific pre‑announced number; it compares your computed result to an independently obtained reference with appropriate tolerances that account for legitimate differences in implementation details (e.g. RCWA truncation order, HDG polynomial degree, quadrature rules, material dispersion interpolation). The total reward is a weighted combination of the scores from the three artifacts, with the efficiency carrying the largest weight. You must produce all three artifacts to receive a full score; reporting a plausible efficiency alone is insufficient.
