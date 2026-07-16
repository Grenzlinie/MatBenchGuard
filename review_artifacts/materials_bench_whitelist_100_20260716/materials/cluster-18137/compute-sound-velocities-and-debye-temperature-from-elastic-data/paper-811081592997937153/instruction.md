# Compute Polycrystalline Moduli, Sound Velocities, and Debye Temperature from Elastic Constants

## Problem background
The B2 CuZr intermetallic compound is of interest for its mechanical and thermal properties. Density functional theory calculations can predict single‑crystal elastic constants, from which polycrystalline mechanical moduli, sound velocities, and the Debye temperature are derived using standard relations. This task reproduces that derivation: given the single‑crystal elastic constants and lattice parameter of B2 CuZr, compute the Hill shear modulus, Young's modulus, Poisson's ratio, the Pugh ratio, the sound velocities, and the Debye temperature.

## Approach
The Hill shear modulus G_H is obtained by Voigt–Reuss–Hill averaging for cubic crystals, combining the Voigt and Reuss bounds. From G_H and the bulk modulus B, Young's modulus E and Poisson's ratio σ are computed using isotropic elasticity relations. The Pugh ratio B/G_H quantifies ductility. Sound velocities—longitudinal v_l, transverse v_t, and average v_avg—are calculated from the elastic constants and the mass density using the relations from the original study. Finally, the Debye temperature θ_D is obtained from the average sound velocity, the atomic volume, and fundamental constants. The required mass density is first computed from the lattice constant and the atomic masses via Avogadro's number.

## Reproduction target
Compute the polycrystalline mechanical moduli G_H (GPa), E (GPa), σ (dimensionless), and B/G_H (dimensionless); the sound velocities v_l, v_t, and v_avg (m/s); and the Debye temperature θ_D (K) for B2 CuZr. Use the fixed single‑crystal elastic constants C11 = 141 GPa, C12 = 108 GPa, C44 = 43 GPa, the bulk modulus B = 119 GPa, and the mass density derived from the lattice constant a0 = 3.268 Å (atomic masses: Cu 63.546 u, Zr 91.224 u; 2 atoms per formula unit). Report all results in the required JSON output file. No external comparison is required; correctness is evaluated by the hidden verifier.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute mass density
- Role: process
- Action: From the given B2 CuZr lattice constant a0 = 3.268 Å, with atomic masses Cu 63.546 u, Zr 91.224 u and 2 atoms per formula unit (one Cu, one Zr), compute the mass density in kg/m^3 using the unit cell volume and Avogadro's number. Write the numeric value to density.txt.
- Evidence: `/app/outputs/density.txt`

### Step 2: Compute mechanical and thermal properties
- Role: scored (load-bearing)
- Action: Using the single-crystal elastic constants C11=141 GPa, C12=108 GPa, C44=43 GPa, the bulk modulus B=119 GPa, and the mass density from the previous step, compute the Hill shear modulus G_H via Voigt–Reuss–Hill averaging for cubic crystals, Young's modulus E, Poisson's ratio sigma, Pugh ratio B/G_H, longitudinal sound velocity v_l, transverse sound velocity v_t, average sound velocity v_avg, and Debye temperature theta_D. Report all results in mechanical_thermal_properties.json.
- Output file: `/app/outputs/mechanical_thermal_properties.json`
- Format: json
- Contract: { "G_H": float (GPa), "E": float (GPa), "sigma": float (dimensionless), "B_over_G_H": float (dimensionless), "v_l": float (m/s), "v_t": float (m/s), "v_avg": float (m/s), "theta_D": float (K) }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_thermal_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_thermal_properties.json
- path: `/app/outputs/mechanical_thermal_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline mechanical moduli and thermal properties computed from single-crystal elastic constants and density for B2 CuZr.
- schema:
  - `type`: object
  - `required`: `G_H`, `E`, `sigma`, `B_over_G_H`, `v_l`, `v_t`, `v_avg`, `theta_D`
  - `properties`:
    - `G_H`:
      - `type`: number
      - `units`: GPa
    - `E`:
      - `type`: number
      - `units`: GPa
    - `sigma`:
      - `type`: number
      - `units`: dimensionless
    - `B_over_G_H`:
      - `type`: number
      - `units`: dimensionless
    - `v_l`:
      - `type`: number
      - `units`: m/s
    - `v_t`:
      - `type`: number
      - `units`: m/s
    - `v_avg`:
      - `type`: number
      - `units`: m/s
    - `theta_D`:
      - `type`: number
      - `units`: K

Notes: Values are compared to the paper-reported references with appropriate tolerances. No gold values or tolerance limits are disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_thermal_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "G_H",
          "E",
          "sigma",
          "B_over_G_H",
          "v_l",
          "v_t",
          "v_avg",
          "theta_D"
        ],
        "properties": {
          "G_H": {
            "type": "number",
            "units": "GPa"
          },
          "E": {
            "type": "number",
            "units": "GPa"
          },
          "sigma": {
            "type": "number",
            "units": "dimensionless"
          },
          "B_over_G_H": {
            "type": "number",
            "units": "dimensionless"
          },
          "v_l": {
            "type": "number",
            "units": "m/s"
          },
          "v_t": {
            "type": "number",
            "units": "m/s"
          },
          "v_avg": {
            "type": "number",
            "units": "m/s"
          },
          "theta_D": {
            "type": "number",
            "units": "K"
          }
        }
      },
      "description": "Polycrystalline mechanical moduli and thermal properties computed from single-crystal elastic constants and density for B2 CuZr."
    }
  ],
  "notes": "Values are compared to the paper-reported references with appropriate tolerances. No gold values or tolerance limits are disclosed to the agent."
}
```

## How you are scored
A hidden verifier independently recomputes each required quantity from the same inputs and formulas and compares your computed values to a hidden reference. The verifier assigns a score to each quantity based on its deviation from the reference, with appropriate tolerances. The final reward is a weighted combination of the per‑quantity scores, giving a graded measure of accuracy rather than a binary pass/fail. You only need to write the output artifact; the verifier handles the comparison.
