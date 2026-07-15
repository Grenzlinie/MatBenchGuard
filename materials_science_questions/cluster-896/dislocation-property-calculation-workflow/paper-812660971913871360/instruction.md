# Critical Biaxial Elongations for Domain Wall Networks in Bilayer Graphene

## Problem background
Bilayer graphene consists of two atomically thin carbon layers. When one layer is biaxially stretched, the lattice mismatch breaks the commensurate AB/BA stacking and can give rise to domain wall networks that separate commensurate domains. Two distinct network morphologies have been observed: a regular triangular network and a striped pattern of parallel domain walls. An analytical two-chain Frenkel-Kontorova model describes these incommensurate phases and predicts that the system can undergo a sequence of phase transitions purely driven by the amount of biaxial strain. In this task we aim to compute the critical relative biaxial elongations at which these transitions are expected to occur, using the material parameters of graphene.

## Approach
The two-chain Frenkel-Kontorova model treats the interlayer interaction by approximating the potential energy surface with its leading Fourier harmonics. Domain walls correspond to stacking dislocations whose Burgers vectors equal the bond length and align along armchair directions. The energy per unit length of a single domain wall depends on the elastic constants, the interlayer sliding barrier, and the angle between the Burgers vector and the wall normal. For a regular triangular network, the total formation energy per unit area includes contributions from the domain walls, the dislocation nodes where walls cross, and a global elastic term due to the extra biaxial elongation needed to accommodate the network. Minimising this energy with respect to the network period yields a critical elongation below which the commensurate state is favoured. An analogous analysis for a striped network (free of nodes) gives a higher critical elongation. By comparing the optimal energies of the triangular and striped phases, one obtains the elongation at which the striped pattern becomes more stable. At very large strains the interlayer interaction becomes negligible, the system returns to a triangular-like incommensurate phase, and the reentrant critical elongation is derived from the elastic-energy balance in the fully incommensurate limit. The model uses the following material parameters: graphene bond length, elastic constant under uniaxial stress, Poisson ratio, and the maximum interlayer sliding barrier. The model prescribes the following exact analytical expressions. Let l be the graphene bond length, k the elastic constant under uniaxial stress, ν Poisson's ratio, and V_max the maximum interlayer sliding barrier. The domain-wall energy prefactor is

  W0 = sqrt( k l² V_max / (1 - ν²) * (3√3/π - 1) ).

For the regular triangular domain wall network, the formation energy per unit area takes the form ΔW = A l/L + B l²/L² with coefficients

  A = - (2√3 k ε)/(1 - ν) + (2√3 W0)/l,
  B = (3k (7 + 4ν)) / (4(1 - ν²)).

The commensurate phase is stable as long as A > 0; the critical elongation ε_c0 is therefore obtained from the condition A = 0:

  ε_c0 = (1 - ν) W0 / (k l).

For the optimal striped network (domain walls aligned along an armchair direction), the minimal critical elongation is

  ε_c0^s = ε_c0 * sqrt( (7 - ν) / 6 ).

Comparing the energies of the triangular and striped phases gives the elongation of the first-order transition:

  ε_c1 = ε_c0 * ( sqrt( ((7 + 4ν)(7 - ν)) / 6 ) - 2 ) / ( sqrt(7 + 4ν) - 2 ).

At very large strains, where the interlayer interaction becomes a small perturbation, the reentrant transition back to a triangular-like incommensurate phase occurs at

  ε_c2 = (3/2) * sqrt( (√3 (7 - ν) V_max) / (2π k) ).

Use these formulas to compute the four critical strains numerically.

## Reproduction target
Implement a computational script that computes the four dimensionless critical relative biaxial elongations: ε_c0 (commensurate-to-triangular transition), ε_c0^s (minimal critical elongation for the optimal striped network), ε_c1 (triangular-to-striped transition), and ε_c2 (reentrant transition back to the triangular phase). Use the material parameters given in the workflow step description. Save the results as a single JSON file `/app/outputs/critical_strains.json` containing the keys `epsilon_c0`, `epsilon_c0_s`, `epsilon_c1`, `epsilon_c2`.

## Assets

- Python scientific computing environment: numpy

## Workflow steps

### Step 1: Compute critical biaxial elongations
- Role: scored (load-bearing)
- Action: Implement the analytical two-chain Frenkel-Kontorova model for domain wall networks in bilayer graphene. Use the given material parameters (graphene bond length l=1.430 Å, elastic constant under uniaxial stress k=331 J/m², Poisson ratio ν=0.174, interlayer sliding barrier V_max=1.61 meV/atom). Compute the domain-wall energy prefactor W0 from the expression involving these parameters and the known dependence on the barrier and elastic constants. Then compute the four critical relative biaxial elongations: ε_c0 (commensurate–triangular transition, from the condition A=0 for the regular triangular network), ε_c0^s (optimal striped network minimal critical elongation using ε_c0 and Poisson's ratio), ε_c1 (triangular-to-striped transition from energy comparison), and ε_c2 (reentrant transition to triangular phase from the large-elongation limit). Output all four values as a JSON file with keys 'epsilon_c0', 'epsilon_c0_s', 'epsilon_c1', 'epsilon_c2'.
- Output file: `/app/outputs/critical_strains.json`
- Format: json
- Contract: {"epsilon_c0": <float>, "epsilon_c0_s": <float>, "epsilon_c1": <float>, "epsilon_c2": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_strains.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_strains.json
- path: `/app/outputs/critical_strains.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The four critical elongations computed from the analytical model.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_c0`: float
    - `epsilon_c0_s`: float
    - `epsilon_c1`: float
    - `epsilon_c2`: float
  - `description`: Critical relative biaxial elongations (dimensionless).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_strains.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_c0": "float",
          "epsilon_c0_s": "float",
          "epsilon_c1": "float",
          "epsilon_c2": "float"
        },
        "description": "Critical relative biaxial elongations (dimensionless)."
      },
      "description": "The four critical elongations computed from the analytical model."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted `critical_strains.json`. For each of the four strain values, the verifier compares your computed number to a hidden reference. The per-value score is highest when the difference is exactly zero and decreases as the absolute error grows; the final reward is a weighted combination of the four individual scores. Producing a value that matches the reference closely is therefore essential, but the reference values and the tolerance used are not disclosed in the instructions.
