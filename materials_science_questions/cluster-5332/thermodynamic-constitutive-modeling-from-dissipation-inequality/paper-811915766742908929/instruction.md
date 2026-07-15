# Instantaneous Storage Fraction in Shocked Metal from Thermodynamic Theory

## Problem background
Metals subjected to extreme loading rates (strain rates >10³ /s) exhibit nonequilibrium phenomena such as abrupt dynamic strengthening and the formation of organized defect structures (slip bands, dislocation cells). A thermodynamic theory describes energy redistribution through mobile dislocations, characterized by an instantaneous storage fraction k_s that quantifies the portion of plastic dissipation stored in the defect structure. The theory predicts that k_s can be substantial at high dislocation velocities. This task requires computing the critical dislocation velocity and the storage fraction for a copperlike metal under uniaxial strain shock loading.

## Approach
The workflow implements the thermodynamic constitutive model for a copperlike material under uniaxial strain. First, compute the critical dislocation velocity v_cr from the material's shear modulus, density, and Poisson ratio using the formula derived from the theory. Then, for a range of normalized dislocation velocities v_d/v_cr (0.0 to 0.9), evaluate the instantaneous storage fraction k_s at three time instances (5, 10, 20 ns). The computation involves evaluating the plastic dissipation terms U_ζ^f and U_0^f, which depend on the incompatibility field, dynamic hardening, and characteristic scale parameters. The required formulas are provided in the workflow steps. Outputs: a text file with v_cr and a CSV with k_s values.

## Reproduction target
Using the provided material constants (shear modulus G, Poisson ratio ν, mass density ρ, yield stress σ0, mobile dislocation density ρ_d^m, characteristic length l_c, time increment Δt_c, and incompatibility parameters ψ_inc^s, ψ1, ψ2), compute the critical dislocation velocity v_cr (in m/s) and compute the instantaneous storage fraction k_s for normalized dislocation velocities v_d/v_cr = 0.0, 0.1, ..., 0.9 at time instances t = 5×10⁻⁹ s, 1×10⁻⁸ s, 2×10⁻⁸ s. The target is to produce a single v_cr value and a CSV with columns: vd_over_vcr, t_ns (time in nanoseconds: 5, 10, or 20), and k_s (dimensionless). The computed values should be physically reasonable; the hidden verifier will assess correctness against reference results.

## Constants

The copperlike material constants are:

| G | ν | ρ | σ₀ | ρ_d^m |
|---|---|---|---|---|
| 51 GPa | 0.3 | 9830 kg/m³ | 200 MPa | 10¹⁵ /m² |

| N | l_c | Δt_c | ψ_inc^s | ψ₁=ψ₂ |
|---|---|---|---|---|
| 4 | 10⁻⁶ m | 2×10⁻¹⁰ s | 10⁻³ | 0.033 ψ_inc^s |

## Dependencies

- Python 3 with numpy: numpy

## Workflow steps

### Step 1: Compute critical dislocation velocity
- Role: scored
- Action: Using the material constants for a copperlike metal, compute the critical dislocation velocity v_cr from the formula v_cr = (sqrt(2) * c_s / N) * sqrt((1-ν)/(1-2ν)), where c_s = sqrt(G/ρ). Use the shear modulus G, Poisson ratio ν, mass density ρ, and N=4 from the constants. Write the result as a single float in m/s to the output file.
- Output file: `/app/outputs/critical_velocity.txt`
- Format: txt
- Contract: A plain text file containing a single float value representing the critical dislocation velocity in m/s.
- Scoring: scored by hidden verifier

### Step 2: Compute instantaneous storage fraction vs normalized velocity
- Role: scored
- Action: For each normalized dislocation velocity ratio r = v_d/v_cr in {0.0, 0.1, …, 0.9} and each time t ∈ {5×10⁻⁹ s, 10⁻⁸ s, 2×10⁻⁸ s}:
  1. Compute the characteristic scale ζ_c = l_c − N v_d Δt_c, where v_d = r · v_cr, N=4, l_c=10⁻⁶ m, Δt_c=2×10⁻¹⁰ s.
  2. Evaluate the path variable s = √24 · (−N v_d t) / ζ_c.
  3. Compute the incompatibility field at the material point: ψ_inc = ψ_inc^s + ψ₁ sin(s) + ψ₂ cos(s), with ψ_inc^s = 10⁻³, ψ₁ = ψ₂ = 0.033 ψ_inc^s.
  4. Compute the dynamic hardening:
     θ_ψ = (G ρ_d^m ζ_c²) / (3 N²) · (c_s/v_cr)² · r² / (1 − r²),
     where c_s = √(G/ρ), G=51 GPa, ρ=9830 kg/m³, ρ_d^m=10¹⁵ m⁻².
  5. Compute the far-field plastic dissipation (constant):
     U_0^f = (l_c² ρ_d^m σ₀ ψ_inc^s) / 12,
     with σ₀ = 200 MPa.
  6. Compute the plastic dissipation at the path position:
     U_ζ^f = U_0^f − (ζ_c² ρ_d^m / 12) · (σ₀ ψ_inc + ½ θ_ψ ψ_inc²).
  7. Calculate the instantaneous storage fraction: k_s = U_ζ^f / U_0^f.
  Write one CSV row with columns vd_over_vcr (= r), t_ns (5, 10, or 20), and k_s. For r=0, set θ_ψ=0 and handle division (r²=0 gives denominator 1). Ensure all quantities are in SI units (Pa, m, s, etc.).
- Output file: `/app/outputs/k_s_vs_velocity.csv`
- Format: csv
- Contract: CSV with columns: vd_over_vcr (float, dimensionless), t_ns (float, time in nanoseconds, one of 5, 10, 20), k_s (float, dimensionless). One row per (vd_over_vcr, t) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_velocity.txt`
- `/app/outputs/k_s_vs_velocity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_velocity.txt
- path: `/app/outputs/critical_velocity.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical dislocation velocity v_cr computed from material constants.
- schema:
  - `type`: text
  - `format`: single_float
  - `description`: A single float value representing the critical dislocation velocity in m/s.

### k_s_vs_velocity.csv
- path: `/app/outputs/k_s_vs_velocity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Instantaneous storage fraction k_s vs normalized dislocation velocity for three time instances.
- schema:
  - `type`: table
  - `required_columns`: `vd_over_vcr`, `t_ns`, `k_s`
  - `units`:
    - `vd_over_vcr`: dimensionless
    - `t_ns`: ns
    - `k_s`: dimensionless
  - `description`: vd_over_vcr: normalized dislocation velocity ratio (v_d / v_cr); t_ns: time in nanoseconds (5, 10, or 20); k_s: instantaneous storage fraction.

Notes: The CSV should contain exactly 30 rows (10 velocity ratios x 3 times). The checker will compare k_s values at checkpoints (vd_over_vcr = 0.1, 0.3, 0.5, 0.7, 0.9) for each time instance against paper-derived reference values using a mean absolute error tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_velocity.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single_float",
        "description": "A single float value representing the critical dislocation velocity in m/s."
      },
      "description": "Critical dislocation velocity v_cr computed from material constants."
    },
    {
      "file": "k_s_vs_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "vd_over_vcr",
          "t_ns",
          "k_s"
        ],
        "units": {
          "vd_over_vcr": "dimensionless",
          "t_ns": "ns",
          "k_s": "dimensionless"
        },
        "description": "vd_over_vcr: normalized dislocation velocity ratio (v_d / v_cr); t_ns: time in nanoseconds (5, 10, or 20); k_s: instantaneous storage fraction."
      },
      "description": "Instantaneous storage fraction k_s vs normalized dislocation velocity for three time instances."
    }
  ],
  "notes": "The CSV should contain exactly 30 rows (10 velocity ratios x 3 times). The checker will compare k_s values at checkpoints (vd_over_vcr = 0.1, 0.3, 0.5, 0.7, 0.9) for each time instance against paper-derived reference values using a mean absolute error tolerance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each output artifact. The critical velocity is compared against a hidden reference value using a tolerance-based check; full credit if within the tolerance, zero otherwise. For the storage fraction CSV, the verifier extracts k_s at a set of checkpoints (specific vd_over_vcr values) for each time instance and computes the mean absolute error (MAE) against hidden gold values. A MAE below a threshold earns full credit, with the score decreasing linearly as the MAE grows beyond that threshold. The final reward is a weighted combination of the scores from both stages, with the k_s stage carrying the larger weight. You must produce plausible computed numbers; simply reporting known target values will not guarantee credit, as tolerances and checkpoint sampling are not disclosed.
