# Pseudosymmetry Twinning and Wall Tilt Angle in Ferroelastic Lead Phosphate

## Problem background
Lead phosphate (Pb₃(PO₄)₂) undergoes a ferroelastic phase transition from a high‑temperature trigonal prototype to a low‑temperature monoclinic phase. The room‑temperature domain pattern consists of three orientation states separated by two types of walls (W and W′). The W′ wall appears as a tilted stripe whose inclination relative to the (100) cleavage plane is found to be independent of temperature up to the transition, suggesting a direct link to the spontaneous strain. The underlying explanation is twinning by pseudosymmetry: a pseudotrigonal superlattice built from the monoclinic lattice parameters reveals approximate symmetry elements (pseudo‑binary axes and pseudo‑mirror planes) that dictate the domain configurations and wall orientations. From this construction, the W′ wall tilt angle θ and the angle 2ψ between the monoclinic twofold axes of neighboring domains can be computed purely from the lattice geometry, and a relation tanθ = –c/a (with a and c being components of the spontaneous strain tensor) is predicted.

## Approach
First, the monoclinic basis vectors (T₁, T₂, T₃) are used to build a pseudotrigonal superlattice with elementary translations V₁ = T₃+T₁, V₂ = T₁−T₂, V₃ = T₁+T₂. In this superlattice the directions [011] and [01\bar{1}] act as approximate twofold axes and the planes (11\bar{3}) and (1\bar{1}3) act as approximate mirror planes. The W′ wall is associated with twinning by the pseudo‑binary axis [011] (or equivalently [01\bar{1}]). Its orientation is determined by the rhombic‑section construction: (i) take the plane 𝒫 exactly normal to [011], (ii) intersect 𝒫 with the pseudomirror plane (11\bar{3}) to obtain a direction D, and (iii) the wall plane is spanned by [011] and D. The tilt angle θ is the angle between this wall plane and the normal to the monoclinic (100) plane. Separately, the spontaneous strain tensor components a = (ε₂₂−ε₁₁)/2 and c = ε₁₃ are computed by comparing the monoclinic lattice parameters with those of the trigonal prototypic phase, using standard relations. The quantity –c/a is then formed and compared to tanθ computed from the geometric construction. The whole procedure is carried out with room‑temperature lattice constants; because both a and c are expected to scale with the square of the order parameter, the predicted relation should hold at any temperature (a point that can be tested by repeating the calculation with elevated‑temperature lattice parameters if available).

## Reproduction target
Using the publicly available monoclinic lattice parameters of Pb₃(PO₄)₂ at room temperature (Brixner et al., 1973) and the trigonal lattice parameters of the high‑temperature prototypic phase (Keppler, 1970), perform the geometric and strain computations described above. Produce the intermediate pseudotrigonal lattice summary as `/app/outputs/pseudotrigonal_lattice.json` for documentation. Then generate the scored artifact `/app/outputs/computed_angles_and_relation.json` containing:
- the angle 2ψ between the monoclinic twofold axes of adjacent domains related by [011] (in degrees),
- the W′ wall tilt angle θ (in degrees),
- tanθ (dimensionless),
- –c/a (dimensionless),
- a boolean indicating whether tanθ equals –c/a within a small numerical tolerance. The artifact must follow the output contract described below.

## Assets

- Monoclinic lattice parameters of Pb₃(PO₄)₂ at room temperature (Brixner et al., 1973): 10.1016/0025-5408(73)90063-0
- Trigonal lattice parameters of high‑temperature phase (Keppler, 1970): 10.1524/zkri.1970.132.1-6.228
- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Construct pseudotrigonal superlattice
- Role: process
- Action: From the monoclinic lattice parameters (a, b, c, β), compute the pseudotrigonal basis vectors V₁ = T₃+T₁, V₂ = T₁−T₂, V₃ = T₁+T₂. Identify the pseudo‑binary axes [011] and [01\bar{1}] and the pseudo‑mirror planes (11\bar{3}) and (1\bar{1}3).
- Evidence: `/app/outputs/pseudotrigonal_lattice.json`

### Step 2: Compute W' wall angles and verify tanθ = –c/a
- Role: scored (load-bearing)
- Action: Using the pseudotrigonal lattice and the monoclinic metric, compute the angle ψ between [010] and [011], the angle 2ψ between twofold axes. Construct the rhombic section: determine the plane 𝒫 normal to [011], find its intersection direction D with (11\bar{3}), and compute the wall tilt angle θ from the normal to (100). Compute tanθ. Independently compute the spontaneous strain tensor components a = (ε₂₂−ε₁₁)/2 and c = ε₁₃ from the monoclinic vs. trigonal lattice parameters, obtain –c/a, and verify equality with tanθ within a small tolerance. Output the results as a JSON file.
- Output file: `/app/outputs/computed_angles_and_relation.json`
- Format: json
- Contract: {"type": "object", "required": ["two_psi_degrees", "theta_degrees", "tan_theta", "minus_c_over_a", "relation_verified"], "properties": {"two_psi_degrees": {"type": "number"}, "theta_degrees": {"type": "number"}, "tan_theta": {"type": "number"}, "minus_c_over_a": {"type": "number"}, "relation_verified": {"type": "boolean"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_angles_and_relation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_angles_and_relation.json
- path: `/app/outputs/computed_angles_and_relation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing computed W' and W wall angles and verification of tanθ = -c/a relation.
- schema:
  - `type`: object
  - `required`:
    - `two_psi_degrees`: number (degrees)
    - `theta_degrees`: number (degrees)
    - `tan_theta`: number (dimensionless)
    - `minus_c_over_a`: number (dimensionless)
    - `relation_verified`: boolean
    - `dihedral_angle_deg`: number (degrees)
    - `twofold_axes_angle_deg`: number (degrees)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `two_psi_degrees`: degrees
    - `theta_degrees`: degrees
    - `tan_theta`: dimensionless
    - `minus_c_over_a`: dimensionless
    - `dihedral_angle_deg`: degrees
    - `twofold_axes_angle_deg`: degrees

Notes: The checker recomputes 2ψ, θ, tanθ, –c/a, dihedral angle, and twofold axis angle from the same public lattice parameters and the formulas stated in the task. It compares the agent's reported values to the expected references using absolute tolerances (0.1° for angles, 0.001 for tanθ and –c/a). 'relation_verified' is scored by checking that the boolean matches the discrete equality of the two computed quantities. All comparisons use exact_match policy with tolerance, because the values are deterministic from the given inputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_angles_and_relation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "two_psi_degrees": "number (degrees)",
          "theta_degrees": "number (degrees)",
          "tan_theta": "number (dimensionless)",
          "minus_c_over_a": "number (dimensionless)",
          "relation_verified": "boolean",
          "dihedral_angle_deg": "number (degrees)",
          "twofold_axes_angle_deg": "number (degrees)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "two_psi_degrees": "degrees",
          "theta_degrees": "degrees",
          "tan_theta": "dimensionless",
          "minus_c_over_a": "dimensionless",
          "dihedral_angle_deg": "degrees",
          "twofold_axes_angle_deg": "degrees"
        }
      },
      "description": "Scored artifact containing computed W' and W wall angles and verification of tanθ = -c/a relation."
    }
  ],
  "notes": "The checker recomputes 2ψ, θ, tanθ, –c/a, dihedral angle, and twofold axis angle from the same public lattice parameters and the formulas stated in the task. It compares the agent's reported values to the expected references using absolute tolerances (0.1° for angles, 0.001 for tanθ and –c/a). 'relation_verified' is scored by checking that the boolean matches the discrete equality of the two computed quantities. All comparisons use exact_match policy with tolerance, because the values are deterministic from the given inputs."
}
```

## How you are scored
A hidden verifier independently recomputes 2ψ, θ, tanθ, and –c/a from the same public lattice parameters and the formulas described in the workflow. It compares the values you submit in `computed_angles_and_relation.json` to the expected references using absolute tolerances appropriate for the deterministic nature of the geometry. The `relation_verified` boolean is checked against the discrete near‑equality of the two computed quantities. The verifier combines the stage scores into an overall reward; reporting the expected numbers without performing the genuine computation will not pass these checks.
