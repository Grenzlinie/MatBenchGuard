# Stability Boundaries and Phase Transition Temperature in a Uniaxial S=1 Spin Model with Biquadratic Exchange

## Problem background
We study the ferromagnetic phase of a uniaxial magnet with site spin S=1, easy-plane single-ion anisotropy D>0, and anisotropic biquadratic exchange interaction (BQEI) characterized by parameters ξ, η, ζ. In the mean-field approximation the order parameters are the thermal averages ⟨S^Z⟩ and ⟨O₂⁰⟩. They obey the coupled self-consistency equations

⟨S^Z⟩ = \frac{2\operatorname{sh}\frac{h_Z+2J_0⟨S^Z⟩}{\theta} \exp\frac{6K_0⟨O₂⁰⟩-D}{\theta}}{1+2\operatorname{ch}\frac{h_Z+2J_0⟨S^Z⟩}{\theta} \exp\frac{6K_0⟨O₂⁰⟩-D}{\theta}},

⟨O₂⁰⟩ = \frac13 - \frac{1}{1+2\operatorname{ch}\frac{h_Z+2J_0⟨S^Z⟩}{\theta} \exp\frac{6K_0⟨O₂⁰⟩-D}{\theta}},

where θ = kT is the temperature in energy units, h_Z is the external field along the z-axis, and J₀, K₀ are the Fourier transforms of the exchange and BQEI constants at k=0. The ferromagnetic phase corresponds to the solution that tends to ⟨S^Z⟩→1, ⟨O₂⁰⟩→⅓ as θ→0.

Spin excitations are obtained via a Hubbard-operator dynamic matrix. In the k→0 limit the excitation spectrum consists of two branches with gaps

ω₁(0) = 2h_Z + 4⟨S^Z⟩(J₀ − ζ K₀),

ω₂(0) = h_Z + ⟨S^Z⟩(2J₀ − ξ J₀ − η K₀) −
\Bigl[⟨S^Z⟩^2(ξ J₀ − η K₀)^2 +
\bigl(D − 6⟨O₂⁰⟩(K₀ − ξ J₀)\bigr)\,\bigl(D − 6⟨O₂⁰⟩(K₀ − η K₀)\bigr)\Bigr]^{1/2}.

A stable mode requires ω₁,₂(0)>0. The boundary ω₁(0)=0 coincides with the second-order phase transition line between the ferromagnetic phase and an asymmetric phase. The boundary ω₂(0)=0 marks the stability limit of the second excitation mode. The goal is to determine these boundaries in the reduced temperature–field plane and to find how the phase transition temperature depends on the BQEI anisotropy constant ζ.

## Approach
We treat the problem computationally. First, for the given set of dimensionless Hamiltonian parameters we solve the two coupled mean-field self-consistency equations on a dense grid of reduced temperature θ = kT/K₀ and reduced field h = h_Z/K₀. Starting from the low-temperature ferromagnetic limits, a numerical root-finding or fixed-point iteration yields ⟨S^Z⟩ and ⟨O₂⁰⟩ at each (θ,h) point.

Using those order parameters we then evaluate the two spin-excitation gap expressions ω₁(0) and ω₂(0) at every grid point. The loci where each gap crosses zero are traced to produce two curves in the θ–h plane: one for ω₁(0)=0 (the second-order phase transition boundary) and one for ω₂(0)=0 (the second-mode stability limit). The curves are resolved finely enough to capture any reentrant features.

In a separate computation, we fix the field at three values h=0.6, 0.8, 1.0 and solve the condition ω₁(0)=0 for the critical temperature θ_c while varying the anisotropy constant ζ. This yields the function θ_c(ζ) at each field, showing how the transition temperature evolves with the biquadratic exchange anisotropy.

## Reproduction target
1. **Stability boundaries (θ–h plane).** For the fixed Hamiltonian parameters J₀=0.8, D=0.4, K₀=1, ζ=1.2, η=0.8, ξ=1.25, compute the curves in the reduced temperature–reduced field plane where the two spin-excitation gaps vanish: ω₁(0)=0 and ω₂(0)=0. Output the result as a CSV file `stability_boundaries.csv` with columns `reduced_temperature`, `reduced_field`, `boundary_type` (1 for ω₁(0)=0, 2 for ω₂(0)=0). Provide sufficiently many points to define both branches accurately.

2. **Critical temperature vs. ζ.** Using the same Hamiltonian (J₀=0.8, D=0.4, K₀=1, η=0.8, ξ=1.25), fix the reduced field at three values: h = 0.6, 0.8, 1.0. For each field, vary the BQEI anisotropy constant ζ over a range that covers the interesting dependence (e.g., from 0.5 to 2.0) and solve ω₁(0)=0 to obtain the critical temperature θ_c. Write the results to `pt_temperature_vs_zeta.csv` with columns `zeta`, `reduced_temperature`, `reduced_field`. Produce at least 50 points per field.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute self-consistent order parameters over a grid
- Role: process
- Action: Solve the coupled mean-field self-consistency equations for the ferromagnetic phase (⟨S^Z⟩ → 1, ⟨O₂⁰⟩ → 1/3 as T→0) on a fine grid of reduced temperature θ = kT/K₀ and reduced external field h = h_Z/K₀ for the parameter set J₀=0.8, D=0.4, K₀=1, ζ=1.2, η=0.8, ξ=1.25. Use any reliable numerical method (e.g., fixed-point iteration, fsolve).
- Evidence: `/app/outputs/order_parameters_grid.csv`

### Step 2: Trace spectral mode stability boundaries
- Role: scored (load-bearing)
- Action: For the same Hamiltonian parameters, compute the two spin-excitation gap expressions at k=0 using the self-consistent order parameters. Determine the curves in the θ–h plane where each gap equals zero: the first boundary corresponds to the second-order phase transition condition (ω₁(0)=0), the second to the spectral stability limit of the second mode (ω₂(0)=0). Trace both branches densely to resolve any reentrant features. Assign boundary_type = 1 for the ω₁(0)=0 curve and 2 for ω₂(0)=0.
- Output file: `/app/outputs/stability_boundaries.csv`
- Format: csv
- Contract: Columns: reduced_temperature (float, θ = kT/K₀), reduced_field (float, h = h_Z/K₀), boundary_type (int, 1 for ω₁(0)=0 curve, 2 for ω₂(0)=0 curve).
- Scoring: scored by hidden verifier

### Step 3: Compute critical temperature vs. BQEI anisotropy ζ
- Role: scored
- Action: For the same Hamiltonian (J₀=0.8, D=0.4, K₀=1, η=0.8, ξ=1.25) and three fixed reduced fields h = 0.6, 0.8, 1.0, solve the second-order phase transition condition (the first gap, ω₁(0)=0) while varying the biquadratic exchange anisotropy constant ζ. For each ζ, find the temperature θ_c that satisfies the condition. Output results for a dense range of ζ (e.g., 0.5 to 2.0) at each field.
- Output file: `/app/outputs/pt_temperature_vs_zeta.csv`
- Format: csv
- Contract: Columns: zeta (float, dimensionless anisotropy constant ζ), reduced_temperature (float, θ_c), reduced_field (float, one of 0.6, 0.8, 1.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stability_boundaries.csv`
- `/app/outputs/pt_temperature_vs_zeta.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stability_boundaries.csv
- path: `/app/outputs/stability_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Curves where spin excitation gaps ω₁(0) and ω₂(0) vanish in the reduced temperature–field plane. The checker recomputes gaps at the submitted points, constructs reference boundaries, and scores by maximum deviation from the reference within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `reduced_temperature`, `reduced_field`, `boundary_type`

### pt_temperature_vs_zeta.csv
- path: `/app/outputs/pt_temperature_vs_zeta.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Second-order phase transition temperature θ_c as a function of BQEI anisotropy constant ζ at three fixed fields. The checker recomputes θ_c from the self-consistency equations and transition condition, and scores deviation within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `zeta`, `reduced_temperature`, `reduced_field`

Notes: All parameters are dimensionless ratios. The agent may choose any numerical method (fixed-point iteration, root-finding), but must respect the ferromagnetic ground-state limits (⟨S^Z⟩→1, ⟨O₂⁰⟩→1/3 as T→0). The checker independently recomputes gap zeros and compares boundaries/curves, so the agent's method can differ from the checker's reference implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stability_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_temperature",
          "reduced_field",
          "boundary_type"
        ]
      },
      "description": "Curves where spin excitation gaps ω₁(0) and ω₂(0) vanish in the reduced temperature–field plane. The checker recomputes gaps at the submitted points, constructs reference boundaries, and scores by maximum deviation from the reference within a tolerance."
    },
    {
      "file": "pt_temperature_vs_zeta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "zeta",
          "reduced_temperature",
          "reduced_field"
        ]
      },
      "description": "Second-order phase transition temperature θ_c as a function of BQEI anisotropy constant ζ at three fixed fields. The checker recomputes θ_c from the self-consistency equations and transition condition, and scores deviation within a tolerance."
    }
  ],
  "notes": "All parameters are dimensionless ratios. The agent may choose any numerical method (fixed-point iteration, root-finding), but must respect the ferromagnetic ground-state limits (⟨S^Z⟩→1, ⟨O₂⁰⟩→1/3 as T→0). The checker independently recomputes gap zeros and compares boundaries/curves, so the agent's method can differ from the checker's reference implementation."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently recomputes the physics from the same equations. For `stability_boundaries.csv` the verifier solves the mean-field equations at the submitted (θ,h) points, evaluates the corresponding gap (ω₁ or ω₂ according to boundary_type), and checks that the absolute gap is close to zero (within a numerical tolerance). It also compares your traced boundary curves against reference boundaries generated from the same model and computes the maximum deviation; a smaller deviation yields a higher score, with full credit when the deviation is below a pre-set tolerance. For `pt_temperature_vs_zeta.csv` the verifier recomputes θ_c at each (ζ,h) point using the same self-consistency condition and compares the values; again, the score is highest when differences are small and decreases as the discrepancies grow.

Each of the two scored artifacts carries a weight, and the final reward is the weighted sum of their scores. Reporting plausible numbers is not enough—your computed artifacts must pass these recomputed checks.
