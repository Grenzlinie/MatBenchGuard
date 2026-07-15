# Coherent Phase Diagrams for Binary Nanoparticles: Effect of Particle Size and Surface Stress

## Problem background
The thermodynamic phase stability of isolated binary alloy nanoparticles is influenced by surface stress and particle size. For radially symmetric particles in which two coherent phases form a concentric core‑shell structure with a sharp interface, the equilibrium free energy can be expressed solely in terms of temperature, composition, and an effective pressure (related to the trace of the stress tensor). The task is to compute coherent phase diagrams for such nanoparticles under a regular‑solution free energy model that includes compositional strain (a quadratic dependence of the lattice parameter on composition) and coherency constraints.

## Approach
Implement the coherent two‑phase equilibrium model for core‑shell nanoparticles. The free energy density consists of a regular solution (chemical) part and an elastic strain energy that depends quadratically on composition through two parameters: ηc (linear coefficient) and ηcc (second‑order coefficient). Because of coherency, each phase is homogeneous in composition and effective pressure at equilibrium, and the equilibrium conditions are the common‑tangent construction in (composition, effective pressure) space: equality of diffusion potential and effective strain, together with conservation of composition and effective pressure.

For the four prescribed dimensionless parameter sets (varying Λ, ηc, and ηcc), numerically solve these equilibrium equations over ranges of scaled temperature t, overall composition co, and external effective pressure Πo. From the solutions, trace the phase boundaries (coexistence curves) at a fixed external pressure Πo = 0.1, compute the coherent spinodal, determine the consolute critical point, obtain tie‑lines at t = 0.8 and Πo = 0.1, and compute the miscibility gap width as a function of Π at a fixed temperature. All implementation is done in Python with numpy and scipy; the output is a structured JSON file.

## Reproduction target
Compute the coherent phase diagram data for the following four dimensionless parameter sets:

- Λ = 100, ηc = −0.05, ηcc = 0.04
- Λ = 100, ηc = −0.03, ηcc = 0
- Λ = 100, ηc = −0.01, ηcc = −0.04
- Λ = 350, ηc = −0.05, ηcc = 0.05

For each set, produce:
- Coordinates of the consolute critical point (t_c, c_c) at the external pressure Πo = 0.1.
- Phase boundary arrays (temperature t and the two equilibrium compositions c_alpha, c_beta) along the miscibility gap at Πo = 0.1.
- The coherent spinodal curve (t, c) at Πo = 0.1.
- A set of tie‑lines at scaled temperature t = 0.8 and Πo = 0.1, each represented by (c_alpha, Π_alpha, c_beta, Π_beta).
- A dataset showing how the miscibility gap width (difference between the two equilibrium compositions) varies with effective external pressure Π at a fixed temperature (e.g., t = 0.8).

Write all results to `/app/outputs/phase_diagram_data.json` in the structure described in the output contract. All numbers are dimensionless according to the scaling defined in the model.

## Assets

- Python 3 with numpy, scipy: python3, numpy, scipy

## Workflow steps

### Step 1: Compute coherent phase diagram data
- Role: scored (load-bearing)
- Action: Implement the coherent phase equilibrium model for core-shell nanoparticles using the free energy density (regular solution plus elastic strain energy with compositional eigenstrain) and coherency constraints. For the four specified dimensionless parameter sets: (Λ=100, ηc=-0.05, ηcc=0.04), (Λ=100, ηc=-0.03, ηcc=0), (Λ=100, ηc=-0.01, ηcc=-0.04), (Λ=350, ηc=-0.05, ηcc=0.05), solve the common-tangent equilibrium equations to determine phase boundaries at Π=0.1, the coherent spinodal, the consolute critical point, tie-lines at t=0.8 and Π=0.1, and the miscibility gap width as a function of effective pressure at a fixed temperature. Output all results in a structured JSON file named phase_diagram_data.json.
- Output file: `/app/outputs/phase_diagram_data.json`
- Format: json
- Contract: A JSON object with top-level keys per parameter set (e.g. 'L100_eta_c_-0.05_eta_cc_0.04'). Each value is an object with keys: 'critical_point' (object with float fields 't_c' and 'c_c'), 'phase_boundary_at_Pi_0_1' (object with array fields 't', 'c_alpha', 'c_beta' of floats), 'spinodal_at_Pi_0_1' (object with array fields 't', 'c' of floats), 'tie_lines_at_t_0_8' (array of objects each with float fields 'c_alpha', 'Pi_alpha', 'c_beta', 'Pi_beta'), 'effect_of_Pi' (object with float 't', array 'Pi', and array 'gap_width' of floats showing miscibility gap width vs effective pressure). All numeric values are dimensionless as defined in the paper.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_data.json
- path: `/app/outputs/phase_diagram_data.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Coherent phase diagram data for four parameter sets covering miscibility gap, spinodal, critical point, tie-lines, and effective pressure effect.
- schema:
  - `type`: object
  - `required`:
    - `L100_eta_c_-0.05_eta_cc_0.04`: object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi
    - `L100_eta_c_-0.03_eta_cc_0`: object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi
    - `L100_eta_c_-0.01_eta_cc_-0.04`: object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi
    - `L350_eta_c_-0.05_eta_cc_0.05`: object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi
  - `items`:
    - `critical_point`:
      - `type`: object
      - `required`:
        - `t_c`: float
        - `c_c`: float
    - `phase_boundary_at_Pi_0_1`:
      - `type`: object
      - `required`:
        - `t`: array of floats
        - `c_alpha`: array of floats
        - `c_beta`: array of floats
    - `spinodal_at_Pi_0_1`:
      - `type`: object
      - `required`:
        - `t`: array of floats
        - `c`: array of floats
    - `tie_lines_at_t_0_8`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `c_alpha`: float
          - `Pi_alpha`: float
          - `c_beta`: float
          - `Pi_beta`: float
    - `effect_of_Pi`:
      - `type`: object
      - `required`:
        - `t`: float
        - `Pi`: array of floats
        - `gap_width`: array of floats
  - `required_columns`:
  - `units`:
    - `t_c`: dimensionless temperature
    - `c_c`: dimensionless composition
    - `t`: dimensionless temperature
    - `c_alpha`: dimensionless composition
    - `c_beta`: dimensionless composition
    - `c`: dimensionless composition
    - `Pi_alpha`: dimensionless effective pressure
    - `Pi_beta`: dimensionless effective pressure
    - `Pi`: dimensionless effective pressure
    - `gap_width`: dimensionless composition difference

Notes: All values are dimensionless using the scaling defined in the paper. The agent must compute the phase boundaries by solving the common-tangent conditions, not by digitising published figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "L100_eta_c_-0.05_eta_cc_0.04": "object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi",
          "L100_eta_c_-0.03_eta_cc_0": "object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi",
          "L100_eta_c_-0.01_eta_cc_-0.04": "object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi",
          "L350_eta_c_-0.05_eta_cc_0.05": "object with critical_point, phase_boundary_at_Pi_0_1, spinodal_at_Pi_0_1, tie_lines_at_t_0_8, effect_of_Pi"
        },
        "items": {
          "critical_point": {
            "type": "object",
            "required": {
              "t_c": "float",
              "c_c": "float"
            }
          },
          "phase_boundary_at_Pi_0_1": {
            "type": "object",
            "required": {
              "t": "array of floats",
              "c_alpha": "array of floats",
              "c_beta": "array of floats"
            }
          },
          "spinodal_at_Pi_0_1": {
            "type": "object",
            "required": {
              "t": "array of floats",
              "c": "array of floats"
            }
          },
          "tie_lines_at_t_0_8": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "c_alpha": "float",
                "Pi_alpha": "float",
                "c_beta": "float",
                "Pi_beta": "float"
              }
            }
          },
          "effect_of_Pi": {
            "type": "object",
            "required": {
              "t": "float",
              "Pi": "array of floats",
              "gap_width": "array of floats"
            }
          }
        },
        "required_columns": [],
        "units": {
          "t_c": "dimensionless temperature",
          "c_c": "dimensionless composition",
          "t": "dimensionless temperature",
          "c_alpha": "dimensionless composition",
          "c_beta": "dimensionless composition",
          "c": "dimensionless composition",
          "Pi_alpha": "dimensionless effective pressure",
          "Pi_beta": "dimensionless effective pressure",
          "Pi": "dimensionless effective pressure",
          "gap_width": "dimensionless composition difference"
        }
      },
      "description": "Coherent phase diagram data for four parameter sets covering miscibility gap, spinodal, critical point, tie-lines, and effective pressure effect."
    }
  ],
  "notes": "All values are dimensionless using the scaling defined in the paper. The agent must compute the phase boundaries by solving the common-tangent conditions, not by digitising published figures."
}
```

## How you are scored
After you submit, a hidden verifier will independently solve the same equilibrium equations (or use a trusted reference solution) for each parameter set. It will compare your submitted values against this gold solution using a set of checks:

- Critical point coordinates: tolerance on t_c and c_c.
- Phase boundary compositions at given t and Πo = 0.1: tolerance on c_alpha and c_beta.
- Tie‑line endpoints: correct ordering of compositions and pressures, and the sign of the pressure difference between phases.
- Miscibility gap width vs. Π: the direction of change (monotonicity and sign) must be consistent with the model, particularly with the sign of ηcc.
- Structural consistency: the spinodal must lie inside the phase boundary, and tie‑lines must lie in the c‑Π plane with no variation in t.

Each check carries a weight, and your final reward (a number between 0 and 1) is the weighted combination of the passed checks. There is no need to match any published figure exactly; the verifier scores the correctness of your computed quantities against the model.
