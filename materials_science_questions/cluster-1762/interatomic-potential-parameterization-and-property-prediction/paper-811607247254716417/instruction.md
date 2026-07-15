# EPM Band Structure and Optical Properties of MgZnS Alloys

## Problem background
Mg_x Zn_{1-x} S zinc-blende ternary alloys are candidate materials for blue and ultraviolet optoelectronic devices. The electronic band gap (direct versus indirect) and optical constants such as refractive index and reflectivity as a function of composition x are essential for device design. This task applies the empirical pseudopotential method (EPM) coupled with the virtual crystal approximation (VCA) to compute these properties across the full composition range.

## Approach
The empirical pseudopotential method represents the electron-ion interaction in a zinc-blende crystal using a small set of local pseudopotential form factors – symmetric and antisymmetric – obtained by fitting to experimental reflection data. The form factors and lattice constants for the endpoint compounds MgS and ZnS are provided as fixed input parameters. The band structure is computed by solving the secular equation at the high-symmetry points Γ, X, and L in the Brillouin zone, from which the relevant band-gap energies are extracted. For ternary Mg_x Zn_{1-x} S alloys, the virtual crystal approximation linearly interpolates the symmetric and antisymmetric form factors and the lattice constant between the endpoint values. After obtaining the direct band gap from the EPM calculation, the refractive index is estimated using the Moss model and the Ghosh model, and the normal-incidence reflection coefficient is derived from the refractive index.

## Reproduction target
Compute the band-gap energies E_g^Γ, E_g^X, and E_g^L of zinc-blende MgS and ZnS using the EPM with the given symmetric and antisymmetric form factors and lattice constants. Then, for Mg_x Zn_{1-x} S at compositions x = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, compute the alloy form factors via VCA, perform EPM band structure calculations, and extract the direct and indirect band gaps as well as the antisymmetric gap. Finally, compute the refractive index from the direct band gap using the Moss and Ghosh formulas, and calculate the corresponding reflection coefficients.

## Assets

- numpy: numpy
- scipy: scipy
- Pseudopotential form factors for MgS and ZnS

## Workflow steps

### Step 1: Compute binary band gaps for MgS and ZnS
- Role: scored
- Action: Implement the empirical pseudopotential method (EPM) for a zinc-blende crystal using the given symmetric and antisymmetric form factors and lattice constants for MgS and ZnS. Set up the Hamiltonian in reciprocal space, solve the secular equation at high-symmetry points Γ, X, L, and extract the band-gap energies: E_g^Γ (Γ→Γ), E_g^X (Γ→X), and E_g^L (Γ→L). Write the results.
- Output file: `/app/outputs/binary_band_gaps.json`
- Format: json
- Contract: {"MgS": {"Eg_Gamma": float, "Eg_X": float, "Eg_L": float}, "ZnS": {"Eg_Gamma": float, "Eg_X": float, "Eg_L": float}}
- Scoring: scored by hidden verifier

### Step 2: Compute ternary alloy form factors via VCA
- Role: process
- Action: For each composition x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], compute symmetric and antisymmetric form factors for Mg_xZn_{1-x}S using the virtual crystal approximation: V(x) = x * V(MgS) + (1-x) * V(ZnS). Also compute the lattice constant using linear interpolation (Vegard's law).
- Evidence: `/app/outputs/vca_interpolation.log`

### Step 3: Compute ternary alloy band gaps
- Role: scored (load-bearing)
- Action: Using the interpolated form factors and lattice constant for each x from the previous step, perform EPM band structure calculations for the ternary alloys. Extract the direct band gap E_g^Γ, indirect gaps E_g^X and E_g^L, and the antisymmetric gap (energy difference between the first and second valence bands at the X point). Write the results.
- Output file: `/app/outputs/ternary_band_gaps.csv`
- Format: csv
- Contract: columns: x (float), Eg_Gamma (float eV), Eg_X (float eV), Eg_L (float eV), antisymmetric_gap (float eV)
- Scoring: scored by hidden verifier

### Step 4: Compute refractive index and reflection coefficient
- Role: scored
- Action: For each composition x, compute the refractive index n using the Moss model (n^4 = 1 + A/(E_g + B)^2 with A = 25*E_g + 212, B = 0.21*E_g + 4.25) and the Ghosh model (n^4 = 1 + (25*E_g + 212)/(E_g + 4.25)^2). Then compute the normal-incidence reflection coefficient R = ((n-1)^2)/((n+1)^2) for each model. Use the direct band gap E_g^Γ from the ternary band gaps file.
- Output file: `/app/outputs/optical_properties.csv`
- Format: csv
- Contract: columns: x (float), n_Moss (float), n_Ghosh (float), R_Moss (float), R_Ghosh (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binary_band_gaps.json`
- `/app/outputs/ternary_band_gaps.csv`
- `/app/outputs/optical_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binary_band_gaps.json
- path: `/app/outputs/binary_band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed band-gap energies of MgS and ZnS at Γ, X, L high-symmetry points, to be compared with hidden gold values (paper Table 2) within tolerance.
- schema:
  - `type`: object
  - `required`: `MgS`, `ZnS`
  - `properties`:
    - `MgS`:
      - `type`: object
      - `required`: `Eg_Gamma`, `Eg_X`, `Eg_L`
      - `units`:
        - `Eg_Gamma`: eV
        - `Eg_X`: eV
        - `Eg_L`: eV
    - `ZnS`:
      - `type`: object
      - `required`: `Eg_Gamma`, `Eg_X`, `Eg_L`
      - `units`:
        - `Eg_Gamma`: eV
        - `Eg_X`: eV
        - `Eg_L`: eV

### ternary_band_gaps.csv
- path: `/app/outputs/ternary_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Band gaps of Mg_xZn_{1-x}S alloys. The checker will recompute for each x the expected gap as x*Eg(MgS) + (1-x)*Eg(ZnS) using the agent's own binary gaps and compare to the reported values.
- schema:
  - `type`: table
  - `required_columns`: `x`, `Eg_Gamma`, `Eg_X`, `Eg_L`, `antisymmetric_gap`
  - `units`:
    - `Eg_Gamma`: eV
    - `Eg_X`: eV
    - `Eg_L`: eV
    - `antisymmetric_gap`: eV

### optical_properties.csv
- path: `/app/outputs/optical_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Refractive indices and reflection coefficients computed from the agent's ternary direct band gap via Moss and Ghosh models. The checker will recompute n and R from the agent's reported Eg_Gamma and compare.
- schema:
  - `type`: table
  - `required_columns`: `x`, `n_Moss`, `n_Ghosh`, `R_Moss`, `R_Ghosh`
  - `units`:
    - `n_Moss`: dimensionless
    - `n_Ghosh`: dimensionless
    - `R_Moss`: dimensionless
    - `R_Ghosh`: dimensionless

Notes: Binary band gaps are scored by exact match with hidden reference values (within tolerance). Ternary band gaps are scored by linear consistency check using the agent's own binary gaps; this forces the VCA process step. Optical properties are scored by recomputation from the agent's ternary direct band gap.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binary_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "MgS",
          "ZnS"
        ],
        "properties": {
          "MgS": {
            "type": "object",
            "required": [
              "Eg_Gamma",
              "Eg_X",
              "Eg_L"
            ],
            "units": {
              "Eg_Gamma": "eV",
              "Eg_X": "eV",
              "Eg_L": "eV"
            }
          },
          "ZnS": {
            "type": "object",
            "required": [
              "Eg_Gamma",
              "Eg_X",
              "Eg_L"
            ],
            "units": {
              "Eg_Gamma": "eV",
              "Eg_X": "eV",
              "Eg_L": "eV"
            }
          }
        }
      },
      "description": "Computed band-gap energies of MgS and ZnS at Γ, X, L high-symmetry points, to be compared with hidden gold values (paper Table 2) within tolerance."
    },
    {
      "file": "ternary_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "Eg_Gamma",
          "Eg_X",
          "Eg_L",
          "antisymmetric_gap"
        ],
        "units": {
          "Eg_Gamma": "eV",
          "Eg_X": "eV",
          "Eg_L": "eV",
          "antisymmetric_gap": "eV"
        }
      },
      "description": "Band gaps of Mg_xZn_{1-x}S alloys. The checker will recompute for each x the expected gap as x*Eg(MgS) + (1-x)*Eg(ZnS) using the agent's own binary gaps and compare to the reported values."
    },
    {
      "file": "optical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "n_Moss",
          "n_Ghosh",
          "R_Moss",
          "R_Ghosh"
        ],
        "units": {
          "n_Moss": "dimensionless",
          "n_Ghosh": "dimensionless",
          "R_Moss": "dimensionless",
          "R_Ghosh": "dimensionless"
        }
      },
      "description": "Refractive indices and reflection coefficients computed from the agent's ternary direct band gap via Moss and Ghosh models. The checker will recompute n and R from the agent's reported Eg_Gamma and compare."
    }
  ],
  "notes": "Binary band gaps are scored by exact match with hidden reference values (within tolerance). Ternary band gaps are scored by linear consistency check using the agent's own binary gaps; this forces the VCA process step. Optical properties are scored by recomputation from the agent's ternary direct band gap."
}
```

## How you are scored
A hidden verifier scores each of the three scored output files independently. For the binary band gaps, your computed values are compared against a hidden reference. For the ternary band gaps, the verifier checks that the gaps obey the linear VCA relation using your own binary gap values, and examines the antisymmetric gap for expected trends. For the optical properties, the verifier recomputes the refractive index and reflection coefficient from your reported direct band gap and compares them with your submitted numbers. The final reward is a weighted combination of these stage scores. Reporting a number without performing the underlying computation will not earn full credit.
