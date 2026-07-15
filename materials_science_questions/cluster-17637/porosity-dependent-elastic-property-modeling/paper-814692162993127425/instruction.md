# Piezoelectric Property Modeling of a Layered Ceramic–Clay Composite

## Problem background
Piezoelectric composites based on ferroelectric ceramics and piezo-passive inclusions like clay exhibit electromechanical behavior that depends sensitively on microstructure. Porosity, inclusion shape, and layering can strongly influence the effective piezoelectric coefficients, dielectric permittivity, and voltage constants. This task targets a model of a novel ceramic–clay composite in which the restricted piezoelectric activity is attributed to a heterogeneous layered structure: thin, alternating regions of ferroelectric-ceramic/clay layers and porous clay layers are connected in series along the poling direction. Reconstructing the effective properties of such a composite from first-principles homogenisation is essential for understanding the interplay between constituent phases and microgeometry, and for guiding the design of piezo-active materials with tailored sensitivity and anisotropy.

## Approach
The composite is modeled as a 2–2 series-connected stack of two layer types, both described as 3–0 composites. In one layer, spheroidal clay inclusions are embedded in a continuous ferroelectric ceramic (FC) matrix; in the other, spheroidal air pores are embedded in a continuous clay matrix. Effective electromechanical tensors (stiffness, piezoelectric, dielectric) of each layer are obtained by finite-element homogenisation (or an equivalent micromechanical method) using the known material constants of the components. The overall effective properties of the multilayer are then computed via the matrix method for series-connected piezoelectric layers. Key parameters are the aspect ratios and volume fractions of the inclusions/pores, and the volume fraction of the FC/clay layers relative to the total thickness. The resulting longitudinal and transverse piezoelectric coefficients, dielectric permittivity, and voltage constant characterise the composite’s performance.

## Reproduction target
Compute the effective piezoelectric coefficients d33* (pC/N), d31* (pC/N), the dielectric permittivity ε33*σ/ε0, and the piezoelectric voltage constant g33* (mV·m/N) for the layered composite under the following fixed parameters: clay-inclusion aspect ratio ρ_i = 0.1, inclusion volume fraction m_i = 0.40, pore aspect ratio ρ_p = 100, pore volume fraction m_p = 0.40, and volume fraction of FC/clay layers m_1 = 0.93. In a second step, examine the trend of these same effective properties when m_1 is increased to 0.95 and 0.97 while all other parameters stay unchanged. Report the single‑point result in /app/outputs/step_03_computed_properties.json and the three‑point trend in /app/outputs/step_04_trend.csv.

## Assets

### Material constants of ZTS-19 FC and clay (from Table 1)

- ZTS-19 FC (poled, ∞mm symmetry):
  - Elastic moduli (10^10 Pa): c11E = 10.9, c12E = 6.1, c13E = 5.4, c33E = 9.3, c44E = 2.4
  - Piezoelectric coefficients (C/m²): e31 = -4.9, e33 = 14.9, e15 = 10.6
  - Dielectric permittivities (ε/ε0): ε11ξ/ε0 = 820, ε33ξ/ε0 = 840

- Clay (approximated as ∞mm, nearly isotropic):
  - Elastic moduli (10^10 Pa): c11E = 0.0445, c12E = 0.0173, c13E = 0.0173, c33E = 0.0445, c44E = 0.0136
  - Piezoelectric coefficients (C/m²): e31 = 0.0136, e33 = 0, e15 = 0
  - Dielectric permittivities: ε11ξ/ε0 = 8.0, ε33ξ/ε0 = 8.0

- Air (pore):
  - Elastic moduli: all zero
  - Piezoelectric coefficients: all zero
  - Dielectric permittivity: ε_air/ε0 = 1

- Python with numpy and scipy: numpy scipy
- Open-source finite element library: fenics or scikit-fem

## Workflow steps

### Step 1: Compute effective properties of FC/clay layer (3-0 structure)
- Role: process
- Action: Compute the effective electromechanical moduli (stiffness, piezoelectric, dielectric tensors) of a 3–0 composite consisting of spheroidal clay inclusions in a continuous ZTS-19 FC matrix. Use the material constants of FC and clay provided in the task, inclusion aspect ratio ρ_i = 0.1, and inclusion volume fraction m_i = 0.40. Write the resulting effective tensors as evidence.
- Evidence: `/app/outputs/fc_clay_layer_properties.json`

### Step 2: Compute effective properties of porous clay layer (3-0 structure)
- Role: process
- Action: Compute the effective elastic and dielectric tensors of a porous clay layer (clay matrix with spheroidal air pores) using the dilute approximation or an equivalent homogenisation method. Use clay constants, air dielectric constant ε_air/ε0 = 1, pore aspect ratio ρ_p = 100, and pore volume fraction m_p = 0.40. Write the resulting tensors as evidence.
- Evidence: `/app/outputs/porous_clay_layer_properties.json`

### Step 3: Compute effective properties of layered composite for target parameters
- Role: scored (load-bearing)
- Action: Combine the effective properties from the previous steps into a 2–2 series-connected layered composite (alternating FC/clay layers and porous clay layers along the poling axis) using the matrix method. Use the volume fraction of FC/clay layers m_1 = 0.93. Compute the effective piezoelectric coefficients d33* (pC/N), d31* (pC/N), dielectric permittivity ε33*σ/ε0, and piezoelectric voltage constant g33* (mV·m/N). Output these four values in a JSON file.
- Output file: `/app/outputs/step_03_computed_properties.json`
- Format: json
- Contract: JSON object with keys: d33 (float, pC/N), d31 (float, pC/N), epsilon33_over_eps0 (float), g33 (float, mV·m/N)
- Scoring: scored by hidden verifier

### Step 4: Compute trend of effective properties with varying m1
- Role: scored
- Action: Repeat the matrix method for three values of the volume fraction of FC/clay layers: m_1 = 0.93, 0.95, 0.97, keeping all other parameters unchanged (ρ_i = 0.1, m_i = 0.40, ρ_p = 100, m_p = 0.40). For each m_1, compute the same effective properties (d33*, d31*, ε33*σ/ε0, g33*). Write the results as a CSV file with columns: m1, d33, d31, epsilon33_over_eps0, g33. The CSV must include exactly three rows for the specified m_1 values.
- Output file: `/app/outputs/step_04_trend.csv`
- Format: csv
- Contract: CSV with columns: m1 (float), d33 (pC/N), d31 (pC/N), epsilon33_over_eps0 (float), g33 (mV·m/N). Contains three rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_computed_properties.json`
- `/app/outputs/step_04_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_computed_properties.json
- path: `/app/outputs/step_03_computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline effective properties of the layered composite for the parameter set m_1=0.93. Compared to the paper-reported reference with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `d33`: number (pC/N)
    - `d31`: number (pC/N)
    - `epsilon33_over_eps0`: number (dimensionless)
    - `g33`: number (mV·m/N)

### step_04_trend.csv
- path: `/app/outputs/step_04_trend.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Trend of effective properties for m1=0.93, 0.95, 0.97. Checked for monotonic trends: d33 must increase with m1, and the magnitude of d31 must also increase (d31 becomes more negative).
- schema:
  - `type`: table
  - `required_columns`: `m1`, `d33`, `d31`, `epsilon33_over_eps0`, `g33`
  - `columns`:
    - `m1`:
      - `type`: float
    - `d33`:
      - `type`: float
      - `unit`: pC/N
    - `d31`:
      - `type`: float
      - `unit`: pC/N
    - `epsilon33_over_eps0`:
      - `type`: float
      - `unit`: dimensionless
    - `g33`:
      - `type`: float
      - `unit`: mV·m/N

Notes: The material constants for FC and clay are provided inline in the instruction.md. The checker compares the agent's computed values to the paper-reported reference for step_03 and validates the structural trend (monotonicity) for step_04.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "d33": "number (pC/N)",
          "d31": "number (pC/N)",
          "epsilon33_over_eps0": "number (dimensionless)",
          "g33": "number (mV·m/N)"
        }
      },
      "description": "Headline effective properties of the layered composite for the parameter set m_1=0.93. Compared to the paper-reported reference with appropriate tolerances."
    },
    {
      "file": "step_04_trend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m1",
          "d33",
          "d31",
          "epsilon33_over_eps0",
          "g33"
        ],
        "columns": {
          "m1": {
            "type": "float"
          },
          "d33": {
            "type": "float",
            "unit": "pC/N"
          },
          "d31": {
            "type": "float",
            "unit": "pC/N"
          },
          "epsilon33_over_eps0": {
            "type": "float",
            "unit": "dimensionless"
          },
          "g33": {
            "type": "float",
            "unit": "mV·m/N"
          }
        }
      },
      "description": "Trend of effective properties for m1=0.93, 0.95, 0.97. Checked for monotonic trends: d33 must increase with m1, and the magnitude of d31 must also increase (d31 becomes more negative)."
    }
  ],
  "notes": "The material constants for FC and clay are provided inline in the instruction.md. The checker compares the agent's computed values to the paper-reported reference for step_03 and validates the structural trend (monotonicity) for step_04."
}
```

## How you are scored
A hidden verifier independently scores both output artifacts. The values in step_03_computed_properties.json are compared to a reference derived from the model under the specified parameters, with tolerances that account for legitimate implementation differences. The trend table step_04_trend.csv is audited for structural consistency: d33 should increase with increasing m_1, and the magnitude of d31 (its absolute value) should also grow (become more negative). The verifier also checks physical plausibility (e.g., positive dielectric permittivity, positive g33). Each stage carries a weight in the final reward. Running the prescribed computations is essential; simply reporting plausible numbers without executing the homogenisation and layering procedure will not earn full credit.
