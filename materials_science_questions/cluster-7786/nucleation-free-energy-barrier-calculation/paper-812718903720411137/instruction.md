# Melting temperature calculation of Cu using modified void method

## Problem background
Melting temperature is a fundamental materials property, but many molecular dynamics (MD) methods for estimating it suffer from superheating or lack a clear thermodynamic criterion. The modified void method is a heterogeneous-nucleation approach that introduces a cubic void into a solid supercell and evolves the system in the constant-pressure constant-enthalpy (NPH) ensemble. Under appropriate conditions, this procedure can yield a stable solid-liquid coexistence phase. The melting temperature can then be extracted from the plateau region of the equilibrium temperature versus enthalpy curve, providing a thermodynamically grounded estimate.

## Approach
A face-centered cubic (FCC) copper supercell is constructed with a central cubic void to act as a nucleation site. Using the Mishin embedded-atom method (EAM) potential, a series of NPH MD simulations is performed at different initial per‑atom enthalpies that span the solid, coexistence, and liquid regimes. For each simulation, the equilibrium temperature (TE) is recorded once the system stabilizes, yielding a TE vs. per‑atom enthalpy (Hp) curve. The flat plateau region of this curve is taken to correspond to solid-liquid coexistence. The melting temperature is estimated as the average TE over that plateau. As a structural confirmation, the per‑atom bond-orientational order parameter Q6 is computed for one coexistence point and profiled along the long axis of the supercell; distinct Q6 values indicate solid-like and liquid-like regions, verifying the coexistence claim.

## Reproduction target
Reproduce the modified void method for monoatomic Cu at ambient pressure. Construct a 5×5×40 FCC supercell (lattice constant 3.615 Å) with a 2×2×2 a0³ cubic void at the center, using the Mishin EAM potential. Run NPH MD simulations at multiple initial per‑atom enthalpies (at least 20 points) covering solid, coexistence, and liquid regimes. Produce a TE vs. Hp curve (te_hp_curve.csv) that shows the three regimes. Identify the coexistence plateau and compute the melting temperature as the average TE over that plateau; write it to melting_temperature.txt. Additionally, for one point on the coexistence plateau, compute the Q6 order parameter profile along the z‑axis and output it as q6_profile.csv. All results must be placed under /app/outputs.

## Assets

- Mishin Cu EAM potential file: https://www.ctcms.nist.gov/potentials/Cu.html (file Cu1.eam.alloy)
- LAMMPS molecular dynamics software: lammps

## Workflow steps

### Step 1: Prepare initial Cu supercell and void configuration
- Role: process
- Action: Construct a 5x5x40 FCC Cu supercell (lattice constant 3.615 Å) using the Mishin EAM potential. Create a 2x2x2 a0^3 cubic void at the center by deleting 63 atoms. Set up LAMMPS NPH ensemble input scripts for scanning per‑atom enthalpy.
- Evidence: none

### Step 2: Generate TE-Hp curve via NPH simulations
- Role: scored (load-bearing)
- Action: Perform NPH ensemble simulations at multiple initial per‑atom enthalpies (at least 20 points) spanning solid, coexistence, and liquid regimes. For each simulation, record the equilibrium temperature TE (after system stabilizes) and the per‑atom enthalpy Hp. Classify each state as solid, coexistence, or liquid based on the observed T-H trend. Output as te_hp_curve.csv.
- Output file: `/app/outputs/te_hp_curve.csv`
- Format: csv
- Contract: CSV with columns: initial_enthalpy_per_atom (float, eV), equilibrium_temperature (float, K), structure_label (string, one of solid/coexistence/liquid). At least 20 rows.
- Scoring: scored by hidden verifier

### Step 3: Derive melting temperature from coexistence plateau
- Role: scored (load-bearing)
- Action: Analyze te_hp_curve.csv. Locate the flat plateau region (coexistence) and identify at least 5 consecutive points with nearly constant TE. Compute the melting temperature as the arithmetic mean of TE over that plateau. Write the average value (in Kelvin) to melting_temperature.txt. Optionally include a note on the plateau boundaries.
- Output file: `/app/outputs/melting_temperature.txt`
- Format: txt
- Contract: A single line with the average melting temperature in Kelvin (e.g. '1327 K'). A second line may contain a brief note about the plateau range.
- Scoring: scored by hidden verifier

### Step 4: Compute Q6 order parameter profile for a plateau point
- Role: scored
- Action: Select one simulation point on the coexistence plateau (e.g., Hp around -3.11 eV/atom). For that configuration, compute the per‑atom bond‑orientational order parameter Q6 (l=6) using spherical harmonics and 12 nearest neighbors. Bin atoms into slices along the z‑axis and compute the average Q6 per slice. Output a CSV with slice midpoint and average Q6.
- Output file: `/app/outputs/q6_profile.csv`
- Format: csv
- Contract: CSV with columns: z_slice_midpoint (float, Å), avg_Q6 (float). Profile should exhibit solid-like (Q6 ~0.48) and liquid-like (Q6 ~0.37) regions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/te_hp_curve.csv`
- `/app/outputs/melting_temperature.txt`
- `/app/outputs/q6_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### te_hp_curve.csv
- path: `/app/outputs/te_hp_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV output of the TE-Hp scan for Cu from NPH simulations; checker verifies three-regime shape.
- schema:
  - `type`: table
  - `required_columns`: `initial_enthalpy_per_atom`, `equilibrium_temperature`, `structure_label`
  - `units`:
    - `initial_enthalpy_per_atom`: eV
    - `equilibrium_temperature`: K

### melting_temperature.txt
- path: `/app/outputs/melting_temperature.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Melting temperature (in Kelvin) for Cu averaged over the coexistence plateau; compared to paper-reported gold with tolerance.
- schema:
  - `type`: text
  - `required`:
    - `value`: float_with_unit_K

### q6_profile.csv
- path: `/app/outputs/q6_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Q6 order parameter profile along Z for Cu; checker confirms coexistence through distinct solid/liquid Q6 values.
- schema:
  - `type`: table
  - `required_columns`: `z_slice_midpoint`, `avg_Q6`
  - `units`:
    - `z_slice_midpoint`: Å
    - `avg_Q6`: dimensionless

Notes: All outputs must be placed under /app/outputs. The melting temperature is the headline result; the TE-Hp curve and Q6 profile provide supporting structural evidence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "te_hp_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "initial_enthalpy_per_atom",
          "equilibrium_temperature",
          "structure_label"
        ],
        "units": {
          "initial_enthalpy_per_atom": "eV",
          "equilibrium_temperature": "K"
        }
      },
      "description": "CSV output of the TE-Hp scan for Cu from NPH simulations; checker verifies three-regime shape."
    },
    {
      "file": "melting_temperature.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "value": "float_with_unit_K"
        }
      },
      "description": "Melting temperature (in Kelvin) for Cu averaged over the coexistence plateau; compared to paper-reported gold with tolerance."
    },
    {
      "file": "q6_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_slice_midpoint",
          "avg_Q6"
        ],
        "units": {
          "z_slice_midpoint": "Å",
          "avg_Q6": "dimensionless"
        }
      },
      "description": "Q6 order parameter profile along Z for Cu; checker confirms coexistence through distinct solid/liquid Q6 values."
    }
  ],
  "notes": "All outputs must be placed under /app/outputs. The melting temperature is the headline result; the TE-Hp curve and Q6 profile provide supporting structural evidence."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects each scored artifact independently and combines them into a weighted reward.

- The te_hp_curve.csv is checked for the expected three-regime shape: a monotonically increasing solid region, a flat coexistence plateau (at least five consecutive points with small TE variation), and a final liquid region. The plateau identification must be consistent with the melting temperature you report.
- The melting_temperature.txt is compared against a hidden reference value derived from the paper's reported result, within a tolerance that accounts for statistical and implementation differences. The verifier recomputes the plateau average from your curve data and ensures your reported value matches that average.
- The q6_profile.csv is audited for structural evidence of coexistence: it must show intervals where the average Q6 is clearly solid-like (high) and others where it is clearly liquid-like (lower), confirming that both phases coexist along the simulation box.

The reward weights are: melting temperature 60%, TE‑Hp curve shape and consistency 20%, Q6 profile structural evidence 20%. Simply reporting a number, even if correct, is insufficient; the supporting artifacts must be internally consistent and structurally valid.
