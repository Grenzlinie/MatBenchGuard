# Strain-dependent electronic and dielectric properties of monolayer black phosphorus from first-principles

## Problem background
Monolayer black phosphorus (phosphorene) is a two-dimensional semiconductor with a direct band gap and strong in-plane optical anisotropy, making it a candidate for optoelectronic applications such as photodetectors and solar cells. The electronic and dielectric response of phosphorene can be tuned by applying mechanical strain, but the quantitative effect of biaxial strain on the band gap and static dielectric constants must be determined from first-principles calculations. This task reproduces density functional theory (DFT) computations of these properties across a range of strains, providing key insight into the strain-dependent behavior.

## Approach
The core approach is plane-wave density functional theory (DFT) using the screened hybrid functional HSE06 to obtain accurate band structures and dielectric functions. The monolayer black phosphorus structure is first relaxed with a van-der-Waals-corrected exchange-correlation functional (e.g., PBE-D3) to obtain the equilibrium geometry. The dielectric function is computed via momentum matrix elements, from which the static dielectric constant ε₁(0) and the imaginary part ε₂(ω) are extracted separately for the in-plane armchair (x) and zigzag (y) directions. By applying equal biaxial scaling of the in-plane lattice constants, strain-dependent band gaps and dielectric constants are mapped out. The computed data enable an analysis of optical anisotropy and the tunability of the dielectric response.

## Reproduction target
The task requires you to compute and report the following for monolayer black phosphorus:

- The HSE06 direct band gap at Γ and the static dielectric constants ε₁ₓ(0) (armchair) and ε₁ᵧ(0) (zigzag) at five equi-biaxial in-plane strains: −7%, −3%, 0%, 3%, and 7%. Store these results in a JSON file (`static_properties.json`) as an array of objects, each with fields: strain (string), Eg_HSE06 (eV), epsilon1x0, epsilon1y0.
- The imaginary part of the dielectric function ε₂(ω) for the unstrained (0% strain) case, covering photon energies from 0 to 12 eV with at least 100 points, for both polarizations. Output this as a CSV (`epsilon2_0pct.csv`) with columns: energy_eV (monotonic increasing), epsilon2_x, epsilon2_y.

All results must be produced by running DFT calculations as described in the workflow; do not fabricate numbers.

## Assets

- Monolayer black phosphorus crystal structure
- Plane-wave DFT code with HSE06 support: https://www.quantum-espresso.org/
- Norm-conserving pseudopotential for phosphorus: http://pseudodojo.org/
- Van der Waals dispersion correction (Grimme D3)

## Workflow steps

### Step 1: Geometry optimization of monolayer black phosphorus
- Role: process
- Action: Perform geometry optimization of monolayer BP using DFT with a dispersion-corrected functional (e.g., PBE-Grimme D3) to obtain the relaxed equilibrium lattice constants and atomic positions for the unstrained structure. This structure is required for all subsequent strain-series calculations.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Strain-dependent band gaps and static dielectric constants
- Role: scored (load-bearing)
- Action: For biaxial in-plane strains of -7%, -3%, 0%, 3%, and 7% (applied as equal scaling of the in-plane lattice constants of the relaxed structure), compute the electronic structure using the HSE06 hybrid functional. Extract the direct band gap at Γ. Then compute the complex dielectric function via momentum matrix elements for x (armchair) and y (zigzag) polarizations; read the zero-frequency limit ε₁(0) to obtain the static dielectric constants. Write the results to static_properties.json.
- Output file: `/app/outputs/static_properties.json`
- Format: json
- Contract: Array of objects: { strain: string (e.g., '-7%'), Eg_HSE06: float (eV), epsilon1x0: float, epsilon1y0: float }
- Scoring: scored by hidden verifier

### Step 3: Epsilon2 spectrum for unstrained monolayer
- Role: scored
- Action: From the unstrained (0% strain) dielectric function calculation, extract the imaginary part ε₂(ω) for photon energies covering 0 to 12 eV, separately for x and y polarizations. Sample densely (≥100 points). Write the spectrum to epsilon2_0pct.csv.
- Output file: `/app/outputs/epsilon2_0pct.csv`
- Format: csv
- Contract: Columns: energy_eV (float, monotonic increasing), epsilon2_x (float), epsilon2_y (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_properties.json`
- `/app/outputs/epsilon2_0pct.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_properties.json
- path: `/app/outputs/static_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Strain-dependent HSE06 band gaps and static dielectric constants (ε₁ₓ(0) and ε₁ᵧ(0)) for monolayer BP at -7%, -3%, 0%, 3%, and 7% biaxial strain.
- schema:
  - `type`: array
  - `items`:
    - `strain`: string
    - `Eg_HSE06`: float (eV)
    - `epsilon1x0`: float
    - `epsilon1y0`: float
  - `required`: `strain`, `Eg_HSE06`, `epsilon1x0`, `epsilon1y0`

### epsilon2_0pct.csv
- path: `/app/outputs/epsilon2_0pct.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Imaginary part of the dielectric function ε₂(ω) for x and y polarizations at 0% strain, covering 0–12 eV with dense sampling.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `epsilon2_x`, `epsilon2_y`
  - `units`:
    - `energy_eV`: eV
    - `epsilon2_x`: dimensionless
    - `epsilon2_y`: dimensionless

Notes: The static dielectric constants and band gaps are scored by comparison with hidden reference values (paper Table 2 and Table 3) within tolerances. The epsilon2 spectrum is audited for structural validity (non-negative values, energy range, monotonic energy grid).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "strain": "string",
          "Eg_HSE06": "float (eV)",
          "epsilon1x0": "float",
          "epsilon1y0": "float"
        },
        "required": [
          "strain",
          "Eg_HSE06",
          "epsilon1x0",
          "epsilon1y0"
        ]
      },
      "description": "Strain-dependent HSE06 band gaps and static dielectric constants (ε₁ₓ(0) and ε₁ᵧ(0)) for monolayer BP at -7%, -3%, 0%, 3%, and 7% biaxial strain."
    },
    {
      "file": "epsilon2_0pct.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "epsilon2_x",
          "epsilon2_y"
        ],
        "units": {
          "energy_eV": "eV",
          "epsilon2_x": "dimensionless",
          "epsilon2_y": "dimensionless"
        }
      },
      "description": "Imaginary part of the dielectric function ε₂(ω) for x and y polarizations at 0% strain, covering 0–12 eV with dense sampling."
    }
  ],
  "notes": "The static dielectric constants and band gaps are scored by comparison with hidden reference values (paper Table 2 and Table 3) within tolerances. The epsilon2 spectrum is audited for structural validity (non-negative values, energy range, monotonic energy grid)."
}
```

## How you are scored
Your outputs will be evaluated by an automated verifier that has access to hidden reference values and structural rules.

- For `static_properties.json`, the verifier compares your reported Eg_HSE06, ε₁ₓ(0), and ε₁ᵧ(0) to reference values within pre-defined tolerances. It also checks whether the strain-dependent trend (e.g., the evolution of the dielectric constant) is physically consistent.
- For `epsilon2_0pct.csv`, the verifier audits structural properties: non-negative values, energy range covering 0–12 eV, monotonic energy grid, and plausibility of the curve shape. Additional consistency checks against the static dielectric constant may be performed.

Each output file contributes a weighted fraction to the total score. Submitting results that match the reference values without genuinely computing them from a DFT workflow will not pass all checks, because the verifier can cross‑validate between artifacts and may penalise fabrication. The final reward is a single number between 0 and 1.
