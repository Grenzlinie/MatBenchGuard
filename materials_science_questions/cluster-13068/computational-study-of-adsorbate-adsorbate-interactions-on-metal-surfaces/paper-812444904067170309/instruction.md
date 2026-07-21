# Computational model of indirect adatom interactions via quasi-1D surface states

## Problem background
When a hydrogen adatom is adsorbed on a metal surface, the substrate electrons screen the impurity charge, leading to an indirect interaction between two adatoms. On certain fcc (110) surfaces, quasi-one-dimensional (Q-1D) electronic states can form in the troughs, channelling electron propagation along the rows. This task investigates the screening of a hydrogen impurity by such Q-1D states using a nonorthogonal Anderson model. The goal is to compute the self-energy of the localized adatom level, the resulting phase shift, and the indirect interaction energy between two hydrogen adatoms mediated by these Q-1D electrons, for a given set of model parameters derived for the H/Ni(110) system.

## Approach
The model uses the nonorthogonal Anderson Hamiltonian for a hydrogen adatom in a quasi-1D electron gas confined to a tube of length L and radius l. The hopping matrix elements are evaluated in the overlap approximation, where the matrix element between the adatom 1s orbital |a⟩ and a tube state |k⟩ is V_{ak} ≈ V_{aa} ⟨a|k⟩. The key analytical expressions are:

Define dimensionless energy Ω = ω / Ry, and let V_a = V_{aa} / Ry.

**Single-impurity self-energy (Λ, Δ):**
- Real part (level shift):
Λ(Ω) = (β l / a₀)²  (V_a − Ω)² / (1 + Ω)²  [ (3 + Ω) − (2 / √|Ω|) θ(−Ω) ]  Ry   (Eq. 33)
- Imaginary part (level halfwidth):
Δ(Ω) = (β l / a₀)²  (V_a − Ω)²  2 / [ √Ω (1 + Ω)² ]  θ(Ω)  Ry   (Eq. 34)
where θ is the Heaviside step function.

**Phase shift for a single adatom:**
η_a(ω) = arctan( Δ(ω) / ( ω − ε_a − Λ(ω) ) )   (Eq. 25)

**Two-impurity self-energy (distance d):**
Σ_{ab}(d, ω) = (β l / a₀)² [ ( 2 + (1 + |d/a₀|)(1 + Ω) ) / (1 + Ω)² · e^{−|d/a₀|} − i · (2 e^{i|d/a₀| √Ω}) / ( √Ω (1 + Ω)² ) ]  Ry   (Eq. 43)

**Indirect interaction energy W_ab(d):**
W_{ab}(d) = −(2/π) ∫_{−∞}^{ε_F} dω  Im[ ln( 1 − ( Σ_{ab}(d,ω) )² / ( ω − ε_a − Λ(ω) + i Δ(ω) )² ) ]   (Eq. 42)
The integration is performed numerically, with the lower limit effectively replaced by a large negative value (or a cutoff) because the integrand vanishes for ω ≪ 0.

The implementation should provide callable functions for Λ(Ω), Δ(Ω), η(ω), and Σ_{ab}(d,ω) using the above expressions, and compute W_{ab}(d) by numerical integration of Eq. (42). Use the parameters given in the Reproduction target.

## Reproduction target
Implement the nonlinear Anderson model for a hydrogen adatom in a Q-1D electron gas using the given parameters (β=0.8, l=0.244 a0, Vaa=-0.019 Ry, εa=0.102 Ry, kF=0.55 a0⁻¹, εF=0.3 Ry). Then:
- Evaluate the self-energy components Λ(Ω) and Δ(Ω) at the dimensionless energies Ω = 0.05, 0.1, 0.2, 0.3, 0.5, 1.0 and write them to step_01_sigma.csv.
- Compute the phase shift η at the Fermi energy (Ω = 0.3) and write it as a single float (radians) to step_02_phase_shift.txt.
- Compute the indirect interaction energy W_ab(d) for inter-adatom distances d = 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20 a0 by numerical integration of the two-impurity expression, and write the results to step_03_interaction_energy.csv.
All output files must be placed in /app/outputs and match the declared schemas exactly.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement nonlinear Anderson model for H in Q-1D electron gas
- Role: process
- Action: Implement the closed-form expressions for the self-energy components Λ(Ω) and Δ(Ω), the phase shift η(ω), and the two-impurity self-energy Σ_ab(d,ω) for a hydrogen adatom in a quasi-1D electron gas using the nonorthogonal Anderson model with the overlap approximation, as described in the method approach. Use the parameters: β=0.8, l=0.244 a0, Vaa=-0.019 Ry, εa=0.102 Ry, kF=0.55 a0^-1, εF=0.3 Ry. The implementation must provide callable functions that can be evaluated at arbitrary points and used for integration.
- Evidence: none

### Step 2: Compute self-energy components at specified energies
- Role: scored
- Action: Evaluate the real part Λ(Ω) and imaginary part Δ(Ω) at the dimensionless energies Ω = [0.05, 0.1, 0.2, 0.3, 0.5, 1.0] using the implemented functions. Write the results to step_01_sigma.csv with columns Omega, Lambda, Delta.
- Output file: `/app/outputs/step_01_sigma.csv`
- Format: csv
- Contract: CSV with columns: Omega (dimensionless), Lambda (Ry), Delta (Ry). No header. One row per Omega value.
- Scoring: scored by hidden verifier

### Step 3: Compute phase shift at Fermi energy
- Role: scored
- Action: Calculate the phase shift η(εF) using the phase-shift formula with the self-energy functions evaluated at Ω = εF/Ry = 0.3. Write the result as a single float to step_02_phase_shift.txt.
- Output file: `/app/outputs/step_02_phase_shift.txt`
- Format: txt
- Contract: Single line containing a floating-point number (phase shift in radians).
- Scoring: scored by hidden verifier

### Step 4: Compute indirect interaction energy W_ab(d)
- Role: scored (load-bearing)
- Action: Numerically compute the indirect interaction energy W_ab(d) from the two-impurity interaction integral using Σ_ab(d,ω) for distances d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20] a0. Perform the integration over ω from -∞ to εF with appropriate numerical methods. Write the results to step_03_interaction_energy.csv with columns d, W_ab.
- Output file: `/app/outputs/step_03_interaction_energy.csv`
- Format: csv
- Contract: CSV with columns: d (a0), W_ab (Ry). No header. One row per distance.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_sigma.csv`
- `/app/outputs/step_02_phase_shift.txt`
- `/app/outputs/step_03_interaction_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_sigma.csv
- path: `/app/outputs/step_01_sigma.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Self-energy components at Omega values [0.05, 0.1, 0.2, 0.3, 0.5, 1.0]. The checker recomputes the reference values from the analytical formulas.
- schema:
  - `type`: table
  - `required_columns`: `Omega`, `Lambda`, `Delta`
  - `units`:
    - `Omega`: dimensionless
    - `Lambda`: Ry
    - `Delta`: Ry

### step_02_phase_shift.txt
- path: `/app/outputs/step_02_phase_shift.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Phase shift η(εF) in radians. The checker recomputes the reference value from the analytical formulas.
- schema:
  - `type`: text
  - `required`: `value`
  - `units`:
    - `value`: radians

### step_03_interaction_energy.csv
- path: `/app/outputs/step_03_interaction_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Indirect interaction energy for inter-adatom distances d = 2,3,4,5,6,7,8,9,10,12,15,20 a0. The checker recomputes the reference values via numerical integration of the analytical expressions.
- schema:
  - `type`: table
  - `required_columns`: `d`, `W_ab`
  - `units`:
    - `d`: a0
    - `W_ab`: Ry

Notes: All outputs are compared to reference values recomputed by the checker using the same analytical formulas and parameters (β=0.8, l=0.244 a0, Vaa=-0.019 Ry, εa=0.102 Ry, kF=0.55 a0^-1, εF=0.3 Ry). Tolerances accommodate minor numerical integration differences but require correct implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_sigma.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Omega",
          "Lambda",
          "Delta"
        ],
        "units": {
          "Omega": "dimensionless",
          "Lambda": "Ry",
          "Delta": "Ry"
        }
      },
      "description": "Self-energy components at Omega values [0.05, 0.1, 0.2, 0.3, 0.5, 1.0]. The checker recomputes the reference values from the analytical formulas."
    },
    {
      "file": "step_02_phase_shift.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": [
          "value"
        ],
        "units": {
          "value": "radians"
        }
      },
      "description": "Phase shift η(εF) in radians. The checker recomputes the reference value from the analytical formulas."
    },
    {
      "file": "step_03_interaction_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "d",
          "W_ab"
        ],
        "units": {
          "d": "a0",
          "W_ab": "Ry"
        }
      },
      "description": "Indirect interaction energy for inter-adatom distances d = 2,3,4,5,6,7,8,9,10,12,15,20 a0. The checker recomputes the reference values via numerical integration of the analytical expressions."
    }
  ],
  "notes": "All outputs are compared to reference values recomputed by the checker using the same analytical formulas and parameters (β=0.8, l=0.244 a0, Vaa=-0.019 Ry, εa=0.102 Ry, kF=0.55 a0^-1, εF=0.3 Ry). Tolerances accommodate minor numerical integration differences but require correct implementation."
}
```

## How you are scored
Each scored step is evaluated independently by a hidden verifier that implements the same theoretical model with the same parameters. It recomputes the expected values from the analytical formulas and numerical integration, then compares your submitted values at each required point. The reward for a step is the fraction of points that match the reference within a tolerance that accounts for minor numerical differences introduced by integration and implementation choices. Reporting the literature values without correctly implementing the model will not satisfy the verifier. The final score is a weighted combination of the per‑step rewards.
