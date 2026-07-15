# Mesoscale Elastic Stiffness Tensor from Gay-Berne Simulations of Clay Nanoplatelets

## Problem background
Clay minerals form aggregates whose mechanical properties control the behaviour of soils, shales, and industrial suspensions. Understanding how nanoscale platelet interactions translate into mesoscale stiffness requires bridging length scales. This work uses an upscaling strategy: atomistic potential-of-mean-force calculations are distilled into Gay-Berne (GB) potential parameters for oblate ellipsoidal particles, and mesoscale molecular dynamics simulations of 1000 platelets are performed to generate jammed configurations. From these, a quasi-static stress-strain protocol extracts the full 6×6 elastic stiffness tensor (Voigt notation). The aim of the reproduction is to obtain the mean stiffness tensor for three representative simulation cases and evaluate how well it approximates cubic symmetry, as well as whether the stiffness components increase with confining pressure — all of which characterise the mechanical response of clay platelet assemblies.

## Approach
The core concept is to treat each clay platelet as an oblate ellipsoid interacting via a Gay-Berne potential that has been calibrated against atomistic free-energy profiles. The GB parameters (shape radii, interaction radius σ, and energy well depths εₐ, ε_b, ε_c) for different platelet diameters are provided in the assets below.

Simulations are run in LAMMPS using the GB pair style. First, NPT simulations at T=300 K compress an initial random simple-cubic lattice of 1000 particles until the system reaches a jammed state (no further energy evolution). At least 10 independent samples per case are needed. Second, for each jammed configuration, a quasi-static stress-strain protocol is applied: six independent small homogeneous strain modes are imposed, and the system is relaxed under NVT (T≈0.01 K) to extract the linear-elastic response. The internal stress tensor is computed from particle velocities and forces, and a linear fit over the initial strain region yields the 6×6 stiffness matrix in Voigt notation. The mean matrix over the 10 samples per case is the final output. The checker will then compute cubic-averaged elastic constants and a normalised Euclidean distance metric from the submitted mean tensors, comparing them to hidden reference values and verifying a pressure trend.

## Reproduction target
Produce the mean full 6×6 elastic stiffness tensor (Voigt notation, in GPa) for three simulation cases:
- D=500 Å platelets at confining pressure P=1 atm
- D=1000 Å platelets at confining pressure P=1 atm
- D=1000 Å platelets at confining pressure P=10 atm

The hidden verifier will independently compute from the submitted tensors:
- cubic-averaged elastic constants C̄₁₁ = (C₁₁+C₂₂+C₃₃)/3, C̄₁₂ = (C₁₂+C₁₃+C₂₃)/3, C̄₄₄ = (C₄₄+C₅₅+C₆₆)/3;
- the Euclidean distance between the full tensor and its cubic approximation divided by the norm of the cubic approximation.
These derived quantities will be compared to hidden reference values. Additionally, the verifier will check that for D=1000 Å, each of C̄₁₁, C̄₁₂, C̄₄₄ is larger at P=10 atm than at P=1 atm. Submit the three mean matrices as a single JSON file /app/outputs/elastic_tensors.json with the format described under the output contract.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/

### Gay‑Berne potential parameters (first face‑to‑face minimum, Table II)

For D=500 Å:
- Diameter (2a, 2b): 504.12 Å
- Thickness (2c): 9.62 Å
- Interaction radius σ: 11.00 Å
- Energy parameters ε_a, ε_b: 12.88
- Energy parameter ε_c: 551.81

For D=1000 Å:
- Diameter (2a, 2b): 1004.12 Å
- Thickness (2c): 9.62 Å
- Interaction radius σ: 11.00 Å
- Energy parameters ε_a, ε_b: 12.94
- Energy parameter ε_c: 1108.46

## Workflow steps

### Step 1: Generate jammed configurations via NPT simulations
- Role: process
- Action: For each of the three required simulation cases (D=500 Å, P=1 atm; D=1000 Å, P=1 atm; D=1000 Å, P=10 atm), use LAMMPS with the provided Gay-Berne parameters (Table II, first face-to-face minimum) to simulate 1000 oblate ellipsoidal particles. Initial configurations: simple cubic lattice with random orientations. Run NPT at T=300 K until the system reaches a jammed state (potential/kinetic energy stabilize). At least 10 independent samples (different random seeds) per case.
- Evidence: `/app/outputs/jammed_configs.log`

### Step 2: Compute elastic stiffness tensor
- Role: scored (load-bearing)
- Action: For each jammed configuration sample, apply a quasi-static stress-strain protocol: impose small homogeneous strains (six independent modes) and relax under NVT at T=0.01 K. Compute the internal stress tensor using the standard atomic-level stress formula (mass, velocity, force, and distance terms). Fit the initial linear region of each stress-strain curve to obtain the 6×6 elastic stiffness matrix in Voigt notation (indices: 11→1, 22→2, 33→3, 23→4, 13→5, 12→6). Average the matrix over the 10 samples for each case to obtain the mean tensor. Output the three mean matrices.
- Output file: `/app/outputs/elastic_tensors.json`
- Format: json
- Contract: A JSON object with keys "D500_P1", "D1000_P1", "D1000_P10". Each key maps to an object containing "mean": a list of 6 lists (each of length 6) of floats representing the matrix Cij in Voigt order (C11, C22, C33, C23, C13, C12 for upper triangle). Optional field "std" (same shape) may be included.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_tensors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_tensors.json
- path: `/app/outputs/elastic_tensors.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Mean full 6×6 elastic stiffness tensor (Voigt notation) in GPa for each of the three simulation conditions. The checker recomputes cubic-averaged constants and Euclidean distance from the submitted raw matrices and compares them against the paper's reference values.
- schema:
  - `type`: object
  - `required`:
    - `D500_P1`: object
    - `D1000_P1`: object
    - `D1000_P10`: object
  - `properties`:
    - `D500_P1`:
      - `type`: object
      - `required`: `mean`
      - `properties`:
        - `mean`:
          - `type`: array
          - `items`:
            - `type`: array
            - `minItems`: 6
            - `maxItems`: 6
            - `items`:
              - `type`: number
              - `unit`: GPa
          - `minItems`: 6
          - `maxItems`: 6

Notes: The elastic tensors are the core scored artifact. The checker does not rely on any other agent-written file. All derived quantities (C11_avg, C12_avg, C44_avg, Euclidean distance) are recomputed deterministically from the submitted tensors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_tensors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "D500_P1": "object",
          "D1000_P1": "object",
          "D1000_P10": "object"
        },
        "properties": {
          "D500_P1": {
            "type": "object",
            "required": [
              "mean"
            ],
            "properties": {
              "mean": {
                "type": "array",
                "items": {
                  "type": "array",
                  "minItems": 6,
                  "maxItems": 6,
                  "items": {
                    "type": "number",
                    "unit": "GPa"
                  }
                },
                "minItems": 6,
                "maxItems": 6
              }
            }
          }
        }
      },
      "description": "Mean full 6×6 elastic stiffness tensor (Voigt notation) in GPa for each of the three simulation conditions. The checker recomputes cubic-averaged constants and Euclidean distance from the submitted raw matrices and compares them against the paper's reference values."
    }
  ],
  "notes": "The elastic tensors are the core scored artifact. The checker does not rely on any other agent-written file. All derived quantities (C11_avg, C12_avg, C44_avg, Euclidean distance) are recomputed deterministically from the submitted tensors."
}
```

## How you are scored
Your reward is determined by a hidden verifier that reads /app/outputs/elastic_tensors.json. For each of the three simulation cases, it extracts the 6×6 mean stiffness matrix, recomputes the cubic-averaged elastic constants (C̄₁₁, C̄₁₂, C̄₄₄) and the normalised Euclidean distance metric, and compares them against hidden reference values using predetermined tolerances. The verifier also checks the monotonic pressure trend for D=1000 Å (all three constants must increase with pressure). The total reward, a float between 0.0 and 1.0, is proportional to the fraction of cases and checks that pass all requirements. Simply reporting the paper's numbers is not sufficient; the verifier recomputes the quantities from your submitted tensor to ensure genuine reproduction. No other artifacts are scored.
