# Mott transition and Kondo screening phase diagram from DMFT and Gutzwiller approximation

## Problem background
The nature of the Mott transition in f-electron materials is a central question in correlated electron physics. In these systems, a narrow correlated f-band is hybridized with a broad conduction band. The interplay between local-moment formation and Kondo screening gives rise to a complex phase diagram. We consider a periodic Anderson model supplemented with direct f-f hopping, which interpolates between a Hubbard model for the f-electrons and the conventional periodic Anderson model. The key open question is whether a finite hybridization between the f-band and the conduction band suppresses the Mott metal-insulator transition, and how the transition evolves at finite temperature.

## Approach
We study this model using dynamical mean-field theory (DMFT) and the Gutzwiller approximation. At zero temperature, the quasiparticle weight Z(U,V) is computed from the Gutzwiller approximation, which describes the correlated ground state through a variational estimate of the double-occupancy probability. At finite temperature, DMFT maps the lattice model onto an effective single-impurity Anderson model that is solved self-consistently using iterated perturbation theory (IPT) as the impurity solver. The model is studied in the paramagnetic sector with particle-hole symmetry and semicircular densities of states (bandwidth ratio α = 0.1). The coexistence region between screened (itinerant) and unscreened (local-moment) solutions is mapped, and the critical end point temperatures where the first-order transition terminates are determined for different hybridization strengths.

## Reproduction target
1. For hybridization values V/D_f = 0.0, 0.1, 0.2, 0.3, compute the quasiparticle weight Z as a function of the interaction U (ranging from 0 to at least 5) using the Gutzwiller approximation. Save the results in quasiparticle_weight.csv. The verifier will check that Z is monotonically non-increasing with U for each V, and that for V=0 it vanishes near the Mott transition while for V>0 it remains finite.

2. For V/D_f = 0.1, 0.2, 0.3, perform DMFT+IPT simulations by scanning U and temperature T to map the coexistence region between screened and unscreened phases. Determine the upper and lower critical end point temperatures and save them in critical_temperatures.csv. The verifier will compare your reported critical temperatures to hidden reference data.

## Assets

- Python scientific computing environment: python3, numpy, scipy, matplotlib

## Workflow steps

### Step 1: Gutzwiller approximation for quasiparticle weight
- Role: scored
- Action: Implement the Gutzwiller approximation for the model Hamiltonian (particle-hole symmetric periodic Anderson model with f-f hopping, semicircular densities of states, α=0.1). For hybridisation V/D_f = 0.0, 0.1, 0.2, 0.3, compute the quasiparticle weight Z(U) over U from 0 to at least 5 in steps ≤0.5. Save the results.
- Output file: `/app/outputs/quasiparticle_weight.csv`
- Format: csv
- Contract: Columns: V (float, in units of D_f), U (float, in units of D_f), Z (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 2: DMFT+IPT finite-temperature phase diagram
- Role: scored (load-bearing)
- Action: Implement DMFT self-consistency for the model using iterated perturbation theory (IPT) impurity solver in the paramagnetic sector. For V/D_f = 0.1, 0.2, 0.3, scan U and temperature T to find coexisting screened and unscreened solutions. Determine the boundaries of the coexistence region and the upper and lower critical end points where the first-order transition terminates. Save the critical temperatures.
- Output file: `/app/outputs/critical_temperatures.csv`
- Format: csv
- Contract: Columns: V (float), upper_Tc (float, units of D_f), lower_Tc (float, units of D_f).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quasiparticle_weight.csv`
- `/app/outputs/critical_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quasiparticle_weight.csv
- path: `/app/outputs/quasiparticle_weight.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Quasiparticle weight computed via Gutzwiller approximation. Verifies that for V>0, Z remains finite (structural check).
- schema:
  - `type`: table
  - `required_columns`: `V`, `U`, `Z`
  - `units`:
    - `V`: D_f
    - `U`: D_f
    - `Z`: dimensionless

### critical_temperatures.csv
- path: `/app/outputs/critical_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Upper and lower critical end point temperatures from DMFT+IPT phase diagram, compared to hidden gold values from the paper's reference data.
- schema:
  - `type`: table
  - `required_columns`: `V`, `upper_Tc`, `lower_Tc`
  - `units`:
    - `V`: D_f
    - `upper_Tc`: D_f
    - `lower_Tc`: D_f

Notes: The hidden gold for critical temperatures is extracted from the paper's Fig. 3(c) with appropriate tolerance. The quasiparticle weight artifact is checked for structural properties: Z > 1e-3 for all V>0 and U≤5, Z decreasing with U, and for V=0 Z approaches zero near U≈2.8 D_f.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quasiparticle_weight.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "V",
          "U",
          "Z"
        ],
        "units": {
          "V": "D_f",
          "U": "D_f",
          "Z": "dimensionless"
        }
      },
      "description": "Quasiparticle weight computed via Gutzwiller approximation. Verifies that for V>0, Z remains finite (structural check)."
    },
    {
      "file": "critical_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V",
          "upper_Tc",
          "lower_Tc"
        ],
        "units": {
          "V": "D_f",
          "upper_Tc": "D_f",
          "lower_Tc": "D_f"
        }
      },
      "description": "Upper and lower critical end point temperatures from DMFT+IPT phase diagram, compared to hidden gold values from the paper's reference data."
    }
  ],
  "notes": "The hidden gold for critical temperatures is extracted from the paper's Fig. 3(c) with appropriate tolerance. The quasiparticle weight artifact is checked for structural properties: Z > 1e-3 for all V>0 and U≤5, Z decreasing with U, and for V=0 Z approaches zero near U≈2.8 D_f."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that inspects each output file. For quasiparticle_weight.csv, the verifier checks structural properties: monotonicity of Z with respect to U and whether Z remains finite or vanishes appropriately. For critical_temperatures.csv, the verifier compares your reported upper_Tc and lower_Tc against hidden reference values within an appropriate tolerance. The final reward is a weighted sum of the scores from both stages.
