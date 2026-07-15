# DFT Formation Energy Calculation for Stability

## Problem background
Automotive three-way catalysts (TWC) simultaneously convert harmful emissions CO, hydrocarbons, and NOₓ. Rhodium (Rh) is a key component for NOₓ reduction, but it is scarce and expensive. Binary PdRu solid-solution alloy nanoparticles exhibit promising NOₓ reduction activity, potentially replacing Rh. However, at the high temperatures encountered in TWC operation, the metastable PdRu solid solution segregates into Pd-rich and Ru-rich phases, causing a severe loss of catalytic activity. Recent concepts from high-entropy alloys suggest that adding a third element can increase configurational entropy and thereby stabilize the solid-solution phase against segregation. The central question is whether a ternary PdRuM (M = a third metal) nanoparticle can achieve sufficient entropic stabilization to maintain the homogeneous solid-solution structure at TWC-relevant temperatures, and which elements M are effective.

## Approach
To investigate this, we perform first-principles density functional theory (DFT) calculations on model nanoparticle systems. We build 201-atom truncated octahedral face-centered cubic (fcc) nanoparticles for binary PdRu and ternary PdRuM compositions with several third elements M (Ir, Pt, Rh, Ag, Au). For each composition, multiple random solid-solution configurations and a phase-segregated structure are generated. Total energies are computed using DFT with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and projector augmented wave (PAW) pseudopotentials. Excess energies at 0 K are derived relative to monometallic reference nanoparticles. The configurational entropy is estimated via the Bragg–Williams approximation (ideal mixing). Using the calculated excess energies and configurational entropy, the Gibbs free energy difference between the solid-solution and segregated states is evaluated as a function of temperature. The temperature at which the solid-solution phase becomes thermodynamically more stable than the segregated one is defined as the critical temperature T_c. By comparing T_c for different third elements and compositions, we assess the entropic stabilization effect.

## Reproduction target
Compute and report the following quantities for PdRuM nanoparticles (M = Ir, Pt, Rh, Ag, Au) and for binary PdRu: (i) Configurational entropy per atom for compositions PdₓRuₓM₁₋₂ₓ with x = 0.33, 0.40, 0.45, 0.50, assuming ideal mixing in a 201-atom nanoparticle. (ii) Excess energy per atom for solid-solution and phase-segregated models at 0 K for each composition, averaged over multiple random solid-solution configurations and the segregated model. (iii) Critical temperature T_c where the Gibbs free energy of the solid-solution model equals that of the segregated model, at the equiatomic composition (Pd:Ru:M = 1:1:1) for each ternary and for the binary. The results must be written to the designated JSON output files. The objective is to determine the relative stabilization of the solid-solution phase as a function of the third element, revealing which M can effectively lower T_c.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO) supporting PBE and PAW: https://www.quantum-espresso.org
- PBE PAW pseudopotentials for Pd, Ru, Ir, Pt, Rh, Ag, Au: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate nanoparticle atomic models
- Role: process
- Action: Build 201-atom truncated octahedral fcc nanoparticle models for all required compositions: monometallic references (Pd₂₀₁, Ru₂₀₁, M₂₀₁ for M=Ir, Pt, Rh, Ag, Au), binary PdRu at multiple ratios, and ternary PdₓRuₓM₁₋₂ₓ for each M with x=0.33, 0.40, 0.45, 0.50. For each composition create at least 16 solid-solution configurations with random atomic occupations and low pairwise short-range order, plus one phase-segregated model.
- Evidence: `/app/outputs/np_models_summary.json`

### Step 2: Run DFT energy calculations
- Role: process
- Action: For every generated NP model and monometallic reference, run a DFT single-point energy calculation using PBE, PAW pseudopotentials, plane-wave cutoff 400 eV, Γ‑point k‑sampling, SCF convergence 1e‑5 eV. Extract the total energy of each cell.
- Evidence: `/app/outputs/dft_total_energies.json`

### Step 3: Compute configurational entropy
- Role: scored
- Action: Using the Bragg–Williams formula, calculate configurational entropy per atom for compositions PdₓRuₓM₁₋₂ₓ with x = 0.50, 0.45, 0.40, 0.33, with total atoms N=201.
- Output file: `/app/outputs/configurational_entropy.json`
- Format: json
- Contract: array of {x: float, entropy_per_atom_eV: float}
- Scoring: scored by hidden verifier

### Step 4: Calculate excess energies
- Role: scored (load-bearing)
- Action: From DFT total energies, compute excess energy per atom for each composition as average over solid-solution configurations and segregated model, using monometallic references. Report for solid-solution and segregated states.
- Output file: `/app/outputs/excess_energies.json`
- Format: json
- Contract: object with system keys, each an object with 'solid_solution' and 'segregated' arrays of floats
- Scoring: scored by hidden verifier

### Step 5: Determine critical temperatures
- Role: scored
- Action: From excess energies and configurational entropy, compute Gibbs free energy difference; find temperature Tc where solid-solution becomes favoured over segregated for binary PdRu and each ternary PdRuM (M=Ir, Pt, Rh, Ag, Au) at equiatomic composition (Pd:Ru:M=1:1:1).
- Output file: `/app/outputs/critical_temperatures.json`
- Format: json
- Contract: object with system name keys and numeric Tc values
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/configurational_entropy.json`
- `/app/outputs/excess_energies.json`
- `/app/outputs/critical_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### configurational_entropy.json
- path: `/app/outputs/configurational_entropy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Configurational entropy per atom values for compositions x=0.50,0.45,0.40,0.33.
- schema:
  - `type`: array
  - `items`:
    - `x`: float
    - `entropy_per_atom_eV`: float

### excess_energies.json
- path: `/app/outputs/excess_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Excess energy values (eV/atom) for solid-solution and segregated models per composition. The checker verifies that at 0 K solid_solution > segregated for every system.
- schema:
  - `type`: object
  - `required`:
  - `additionalProperties`:
    - `type`: object
    - `required`: `solid_solution`, `segregated`
    - `properties`:
      - `solid_solution`:
        - `type`: array
        - `items`:
          - `type`: number
      - `segregated`:
        - `type`: array
        - `items`:
          - `type`: number

### critical_temperatures.json
- path: `/app/outputs/critical_temperatures.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Critical temperatures Tc (K) at which solid-solution Gibbs free energy equals that of segregated model for equiatomic (1:1:1) compositions.
- schema:
  - `type`: object
  - `required`: `PdRu`, `PdRuIr`, `PdRuPt`, `PdRuRh`, `PdRuAg`, `PdRuAu`
  - `additionalProperties`: False
  - `properties`:
    - `PdRu`:
      - `type`: number
    - `PdRuIr`:
      - `type`: number
    - `PdRuPt`:
      - `type`: number
    - `PdRuRh`:
      - `type`: number
    - `PdRuAg`:
      - `type`: number
    - `PdRuAu`:
      - `type`: number

Notes: All intermediate outputs must be derived from DFT calculations on 201-atom NP models. The checker uses hidden gold values for configurational entropy and recomputes Tc from the agent's excess energies and entropy, comparing to reference values. Structural check on excess energies ensures solid_solution > segregated at 0 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "configurational_entropy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "x": "float",
          "entropy_per_atom_eV": "float"
        }
      },
      "description": "Configurational entropy per atom values for compositions x=0.50,0.45,0.40,0.33."
    },
    {
      "file": "excess_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [],
        "additionalProperties": {
          "type": "object",
          "required": [
            "solid_solution",
            "segregated"
          ],
          "properties": {
            "solid_solution": {
              "type": "array",
              "items": {
                "type": "number"
              }
            },
            "segregated": {
              "type": "array",
              "items": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Excess energy values (eV/atom) for solid-solution and segregated models per composition. The checker verifies that at 0 K solid_solution > segregated for every system."
    },
    {
      "file": "critical_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "PdRu",
          "PdRuIr",
          "PdRuPt",
          "PdRuRh",
          "PdRuAg",
          "PdRuAu"
        ],
        "additionalProperties": false,
        "properties": {
          "PdRu": {
            "type": "number"
          },
          "PdRuIr": {
            "type": "number"
          },
          "PdRuPt": {
            "type": "number"
          },
          "PdRuRh": {
            "type": "number"
          },
          "PdRuAg": {
            "type": "number"
          },
          "PdRuAu": {
            "type": "number"
          }
        }
      },
      "description": "Critical temperatures Tc (K) at which solid-solution Gibbs free energy equals that of segregated model for equiatomic (1:1:1) compositions."
    }
  ],
  "notes": "All intermediate outputs must be derived from DFT calculations on 201-atom NP models. The checker uses hidden gold values for configurational entropy and recomputes Tc from the agent's excess energies and entropy, comparing to reference values. Structural check on excess energies ensures solid_solution > segregated at 0 K."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently assesses each of the three required output files. For `configurational_entropy.json`, the verifier checks that the computed entropy values are physically correct for the given compositions. For `excess_energies.json`, the verifier validates that the reported excess energies satisfy the expected ordering at 0 K (solid-solution excess energies must be higher than those of the segregated model for each system) and that the numerical values are physically reasonable given the DFT protocol. For `critical_temperatures.json`, the verifier recomputes T_c from your submitted excess energies and configurational entropy, then compares the recomputed T_c against a hidden reference. The final reward is a weighted combination of the scores from the three artifacts, with the critical temperatures carrying highest weight and configurational entropy the lowest. A high reward requires that all three artifacts are consistent and, for T_c, that the recomputed values agree with the hidden criteria. Note: simply reporting expected numbers without correctly deriving them from the DFT workflow will not pass the verification checks.
