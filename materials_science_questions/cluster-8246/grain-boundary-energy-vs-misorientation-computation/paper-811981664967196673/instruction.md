# Compute Grain Boundary Energy per Unit Area for Tilt Boundaries

## Problem background
Low‑angle tilt grain boundaries in aluminium consist of arrays of edge and 60° dislocations. The stability of different grain boundary planes (GBP) depends on their elastic energy per unit area, which can be calculated using isotropic elasticity theory. For a rotation around the [011] axis, three GBP orientations are possible: the (011) plane composed of pure edge dislocations (A‑type), the (100) plane composed of alternating 60° dislocations (B′‑type), and the (211) plane composed of another arrangement of 60° dislocations (B‑type). The question is which of these boundaries has the lowest energy, and whether the energy ratio between the B′‑type and A‑type walls can be predicted from material constants alone.

## Approach
We use isotropic linear elasticity to compute the energy per unit area of each grain‑boundary wall as a function of the tilt angle θ. The energy expressions are as follows (with shear modulus μ, Burgers vector magnitude b, Poisson ratio ν, core cut‑off radius r₀, and the mathematical constant e):

For the A‑type wall (edge dislocations on (011) plane):
W<sub>A</sub> = (μ b θ / (4π(1‑ν))) * log(e b / (2π r₀ θ))

For the B′‑type wall (60° dislocations on (100) plane):
W<sub>B′</sub> = (μ b √2 (4‑ν) θ / (16π(1‑ν))) * log(u b / (√2 π r₀ θ))
where u = exp(3/(4‑ν) ‑ ν log 2/(4‑ν))

For the B‑type wall (60° dislocations on (211) plane):
W<sub>B</sub> = (μ b (4‑ν) θ / (8π √3 (1‑ν))) * log(v b √3 / (2π r₀ θ))
where v = exp(3/(4‑ν) ‑ (2+ν) log 2/(4‑ν))

Because only relative energies are needed, we set μ = 1. The parameters are: b = 2.86 Å, ν = 0.33, r₀ = b/4. The calculation is carried out for tilt angles of 1°, 2°, 3°, 4°, 5° for all three boundary types. The implementation requires simple numerical evaluation of these formulas using logarithms, exponentials, and trigonometric functions to convert angles to radians. The computed energies are then used to compare the relative stability of the three GBPs and to obtain the ratio W<sub>B′</sub>/W<sub>A</sub>, which can be contrasted with the analytical prediction √2(4‑ν)/4 ≈ 1.2975.

## Reproduction target
Implement the three grain‑boundary energy formulas (for the A‑type, B‑type and B′‑type walls) using the parameters Burgers vector magnitude b = 2.86 Å, Poisson ratio ν = 0.33, core cut‑off radius r₀ = b/4, and shear modulus μ = 1. Compute the energy per unit area for tilt angles θ = 1°, 2°, 3°, 4° and 5° for each boundary type. Write the results to a JSON file containing the list of tilt angles, the three energy arrays, and the computed ratio W<sub>B′</sub>/W<sub>A</sub>.

## Assets

- Python 3 with numpy: python3, numpy

## Workflow steps

### Step 1: Compute grain boundary energies
- Role: scored
- Action: Implement the isotropic elasticity formulas for grain boundary energy per unit area for the (011) edge-dislocation wall (A-type), (100) 60°-dislocation wall (B'-type), and (211) 60°-dislocation wall (B-type) using the parameters Burgers vector magnitude b=2.86 Å, Poisson ratio ν=0.33, core cut-off radius r0=b/4, and shear modulus μ set to 1 (only relative energies matter). Compute the energies for tilt angles θ = 1°, 2°, 3°, 4°, 5° for each type. Output a JSON file containing the tilt angles, the energies, and the computed ratio W_B' / W_A.
- Output file: `/app/outputs/grain_boundary_energies.json`
- Format: json
- Contract: {
  "tilt_angles_deg": [1.0, 2.0, 3.0, 4.0, 5.0],
  "energies": {
    "A_type": [number, ...],
    "B_type": [number, ...],
    "B_prime_type": [number, ...]
  },
  "ratio_WBprime_WA": number
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/grain_boundary_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### grain_boundary_energies.json
- path: `/app/outputs/grain_boundary_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The computed grain boundary energies (in units where μ=1) and the ratio W_B' / W_A. The checker will recompute the ratio from the A_type and B_prime_type energies, verify it matches the theoretical prediction sqrt(2)*(4-ν)/4, and confirm the ordering A_type < B_type < B_prime_type for all tilt angles.
- schema:
  - `type`: object
  - `required`:
    - `tilt_angles_deg`: array of floats
    - `energies`: object with keys A_type, B_type, B_prime_type, each array of floats
    - `ratio_WBprime_WA`: float

Notes: Only the analytical grain boundary energy calculation (Stage 1) is required. The numerical dislocation rotation analysis (Table 2) is excluded because the interaction energy functions are not fully specified in the paper. Shear modulus µ is set to 1 because only relative energies matter.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "grain_boundary_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "tilt_angles_deg": "array of floats",
          "energies": "object with keys A_type, B_type, B_prime_type, each array of floats",
          "ratio_WBprime_WA": "float"
        }
      },
      "description": "The computed grain boundary energies (in units where μ=1) and the ratio W_B' / W_A. The checker will recompute the ratio from the A_type and B_prime_type energies, verify it matches the theoretical prediction sqrt(2)*(4-ν)/4, and confirm the ordering A_type < B_type < B_prime_type for all tilt angles."
    }
  ],
  "notes": "Only the analytical grain boundary energy calculation (Stage 1) is required. The numerical dislocation rotation analysis (Table 2) is excluded because the interaction energy functions are not fully specified in the paper. Shear modulus µ is set to 1 because only relative energies matter."
}
```

## How you are scored
A hidden verifier reads your submitted JSON artifact. It recomputes the ratio W<sub>B′</sub>/W<sub>A</sub> directly from the A‑type and B′‑type energy arrays you provide, and checks that the ratio is consistent with the theoretical expectation for the given material constants. It also examines the energy ordering across the three types for every tilt angle to verify that the computational output exhibits the physically expected relative trends. The final reward is a weighted combination of these checks; reporting a number without having actually performed the computation will not satisfy the verifier.
