# Spin Model Phase Diagram Construction

## Problem background
The [N(CH3)4]2CuCl4 crystal exhibits a sequence of structural phase transitions driven by an incommensurate modulation. A phenomenological Landau-type theory describes the system in terms of order-parameter amplitudes and phases, leading to thermodynamic potentials for the incommensurate phase and several commensurate lock-in phases. The goal of this work is to construct the theoretical phase diagram in the space of two dimensionless coefficients, D0 and A, which arise from the expansion of the soft-mode dispersion. The diagram is used to investigate the possible stabilization of a commensurate phase with wavenumber q = 2/5, alongside other known commensurate phases.

## Approach
The phase diagram is built by implementing the phenomenological potentials for the incommensurate (IC) phase and for commensurate phases C_{0/1}, C_{1/3}, C_{2/5}, and C_{3/8}. The potentials include a sextic term to remain valid away from the transition point. The soft-branch dispersion maps a microscopic variable B^2 to the dimensionless parameters D0 and Dl that enter the potentials. For each phase pair, the phase boundary is obtained by equating the minimized potentials and solving for A as a function of D0. Both the full minimized expressions and the weak-anisotropy or small-A approximations are used, covering the whole diagram. A fixed set of material parameters (Aγ = A3 = 0.6, A8 = 1.5, A5 = 0.8, Q_L² = 0.2, Q = 0.5) is adopted from the original work. The boundaries are traced with sufficient point density to resolve the topology of the diagram, including the region where a C_{2/5} phase would appear.

## Reproduction target
Produce the phase boundary coordinates in the D0–A plane for all relevant phase pairs: IC–C0/1, IC–C1/3, IC–C2/5, IC–C3/8, C1/3–C0/1, C2/5–C1/3, and any additional curves that bound the C_{2/5} region. The output must be a CSV file with columns phase_pair (string), D0 (float), A (float). Each row is a point on a boundary curve; the curves must be sampled densely enough to faithfully represent their shape. The diagram should allow one to identify the relative location and extent of the predicted phases.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Implement thermodynamic potentials and solve for phase boundaries
- Role: process
- Action: Implement the dimensionless thermodynamic potentials φ_IC, φ_m/l (for l=0/1, 1/3, 2/5, 3/8) from the paper's expressions, including the sextic term with A_γ, and the mapping from microscopic parameter B^2 to D0 and Dl via D0=2B^4(B^2−Q_L^2) and Dl=(B^2−Q_L^2)[Q_1^2+2(B^2−Q_L^2)]. Using the fixed parameter set (A_γ=A_3=0.6, A_8=1.5, A_5=0.8, Q_L^2=0.2, Q=0.5), numerically solve for the phase boundaries on the D0–A plane by equating the relevant potentials for each phase pair (IC–C0/1, IC–C1/3, IC–C2/5, IC–C3/8, C1/3–C0/1, C2/5–C1/3, and any additional boundaries that define the C_{2/5} region). Use both the full minimized expressions and the small-A approximations where applicable. Trace each boundary curve with enough point density to resolve the diagram.
- Evidence: none

### Step 2: Export phase boundary coordinates to CSV
- Role: scored (load-bearing)
- Action: Write the computed phase boundary points to 'phase_boundaries_d0_a.csv'. The file must contain columns: phase_pair (string identifier, e.g., 'IC-C0/1', 'IC-C1/3', 'IC-C2/5', 'C1/3-C0/1', 'C2/5-C1/3', 'C2/5-IC', etc.), D0 (float, dimensionless), A (float, dimensionless). Each row is one point on a boundary curve. Ensure the C_{2/5} phase region is bounded by its surrounding curves.
- Output file: `/app/outputs/phase_boundaries_d0_a.csv`
- Format: csv
- Contract: table with columns: phase_pair (string, e.g., 'IC-C0/1', 'IC-C1/3', ...), D0 (float), A (float). Header: phase_pair,D0,A
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundaries_d0_a.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundaries_d0_a.csv
- path: `/app/outputs/phase_boundaries_d0_a.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase boundary points on the D0–A plane for the specified parameter set. The checker will recompute the boundaries using the same public equations and compare the agent's points to verify accuracy and the presence of a stable C_{2/5} region.
- schema:
  - `type`: table
  - `required_columns`: `phase_pair`, `D0`, `A`

Notes: The mapping to the P–T phase diagram is omitted because the paper does not specify the linear mapping coefficients between (A, D0) and (P, T). Only the quantitative D0–A diagram is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundaries_d0_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase_pair",
          "D0",
          "A"
        ]
      },
      "description": "Phase boundary points on the D0–A plane for the specified parameter set. The checker will recompute the boundaries using the same public equations and compare the agent's points to verify accuracy and the presence of a stable C_{2/5} region."
    }
  ],
  "notes": "The mapping to the P–T phase diagram is omitted because the paper does not specify the linear mapping coefficients between (A, D0) and (P, T). Only the quantitative D0–A diagram is scored."
}
```

## How you are scored
A hidden verifier independently recomputes the phase boundaries using the same potentials and parameter set. It compares your submitted points to the recomputed curves using a tolerance in the dimensionless parameter A. The score is the fraction of boundary curves that match the expected curves, plus an additional reward for correctly demonstrating the presence of a stable C_{2/5} region. Each workflow stage's artifact is evaluated separately and the scores are combined by weight. Simply reporting numbers from the literature is insufficient; the verifier expects the artifacts produced by your own computation.
