# Ion pair S_N2 reaction barrier trends via quantum chemistry

## Problem background
Gas-phase identity ion-pair $\mathrm{S_N2}$ reactions at nitrogen,
$\mathrm{LiX} + \mathrm{NH_2X} \rightarrow \mathrm{NH_2X} + \mathrm{LiX}$
($\mathrm{X} = \mathrm{F, Cl, Br, I}$), were investigated computationally to
understand the potential energy surface, structural preferences, and the
influence of the lithium cation and halogen identity on the reaction
mechanisms. Two possible pathways—inversion and retention—were proposed.
This task aims to reproduce the key structural parameters, vibrational
frequencies, and energetic quantities (complexation energies, central
barriers, overall barriers, and looseness parameters) for both pathways,
and to determine how the reaction energetics vary across the halogen
series.

## Approach
Use a quantum chemical workflow approximating the G2M(+) methodology.
All molecular geometries (reactants, pre-reaction complexes, and transition
states for both inversion and retention pathways) are optimized at the
B3LYP/6-311+G(d,p) level. Harmonic vibrational frequencies are computed on
each optimized structure to characterize stationary points and to obtain
zero-point energy corrections. For bromine and iodine, Hay–Wadt effective
core potentials (LANL2DZ) are employed together with the valence basis;
all lighter atoms use the all-electron 6-311+G(d,p) basis. On each
optimized geometry, a single-point energy is evaluated at the
CCSD(T)/6-311+G(3df,2p) level with the same basis/ECP conventions.
From the resulting geometries, frequencies, and energies, derive the
following quantities for every halogen: bond lengths, vibrational
frequencies, dipole moments; Li–X and N–X bond dissociation energies;
inversion and retention complexation energies, central barriers, and
overall barriers; and looseness parameters %Li–X$^\neq$ and %N–X$^\neq$.

## Reproduction target
Compute the structural and energetic quantities listed in the workflow
steps for all four halogens and both reaction pathways. The final output
is a single JSON file (`computed_results.json`) that must contain:
- per-halogen blocks (F, Cl, Br, I) with sub-objects for each species
  (LiX, NH$_2$X, inversion complex, retention complex, inversion TS,
  retention TS), each holding bond lengths, frequencies, and dipole
  moments, plus dissociation energies for LiX and NH$_2$X;
- an `energetics` block with, per halogen, the complexation energies,
  central barriers, and overall barriers for both inversion and retention;
- a `looseness_parameters` block with the %N–X$^\neq$ and %Li–X$^\neq$
  values per halogen and pathway.
## Assets

- Psi4 quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: Build initial molecular structures
- Role: process
- Action: Construct initial guess geometries for all molecular species: isolated LiX, NH2X, inversion and retention pre-reaction complexes, and transition states for X=F, Cl, Br, I. Use standard chemical knowledge and known symmetry constraints.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: B3LYP geometry optimization and frequency calculation
- Role: process
- Action: Perform B3LYP/6-311+G(d,p) geometry optimization and harmonic vibrational frequency calculations on all species. Use 6-311+G(d,p) basis for light atoms and LANL2DZ effective core potentials for Br and I.
- Evidence: `/app/outputs/b3lyp_optimization.log`

### Step 3: CCSD(T) single-point energy calculations
- Role: process
- Action: Perform single-point energy calculations at CCSD(T)/6-311+G(3df,2p) level using the same basis/ECP conventions on each optimized geometry.
- Evidence: `/app/outputs/ccsd_t_energies.log`

### Step 4: Compute and report energetics and structural parameters
- Role: scored (load-bearing)
- Action: From the geometries, frequencies, and energies of previous steps, calculate: bond lengths, vibrational frequencies, dipole moments; Li-X and N-X bond dissociation energies; inversion and retention complexation energies, central barriers, overall barriers; looseness parameters %Li-X^≠ and %N-X^≠. Output all results in a single JSON file.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: JSON object with top-level keys for each halogen (F,Cl,Br,I) containing nested species objects, plus top-level keys 'energetics' and 'looseness_parameters' with arrays/objects of values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The aggregated computational results file, containing all structural parameters, energetics, and looseness parameters for all four halogens and both reaction pathways.
- schema:
  - `type`: object
  - `required`: `F`, `Cl`, `Br`, `I`, `energetics`, `looseness_parameters`
  - `properties`:
    - `F`:
      - `type`: object
      - `description`: Per-halogen species data
      - `properties`:
        - `LiX`:
          - `type`: object
          - `properties`:
            - `bond_lengths`:
              - `type`: object
              - `description`: atom pair -> Å
            - `frequencies`:
              - `type`: array
              - `items`:
                - `type`: number
              - `description`: cm⁻¹
            - `dipole_moment`:
              - `type`: number
              - `description`: Debye
            - `dissociation_energy`:
              - `type`: number
              - `description`: kJ/mol
        - `NH2X`:
          - `type`: object
          - `properties`:
            - `bond_lengths`:
              - `type`: object
            - `frequencies`:
              - `type`: array
              - `items`:
                - `type`: number
            - `dipole_moment`:
              - `type`: number
            - `dissociation_energy`:
              - `type`: number
        - `complex_inv`:
          - `type`: object
          - `properties`:
            - `bond_lengths`:
              - `type`: object
            - `frequencies`:
              - `type`: array
              - `items`:
                - `type`: number
            - `dipole_moment`:
              - `type`: number
        - `complex_ret`:
          - `type`: object
          - `properties`:
            - `bond_lengths`:
              - `type`: object
            - `frequencies`:
              - `type`: array
              - `items`:
                - `type`: number
            - `dipole_moment`:
              - `type`: number
        - `ts_inv`:
          - `type`: object
          - `properties`:
            - `bond_lengths`:
              - `type`: object
            - `frequencies`:
              - `type`: array
              - `items`:
                - `type`: number
            - `dipole_moment`:
              - `type`: number
        - `ts_ret`:
          - `type`: object
          - `properties`:
            - `bond_lengths`:
              - `type`: object
            - `frequencies`:
              - `type`: array
              - `items`:
                - `type`: number
            - `dipole_moment`:
              - `type`: number
    - `Cl`:
      - `type`: object
      - `description`: Same structure as F but for chlorine
      - `properties`: object
    - `Br`:
      - `type`: object
      - `description`: Same structure as F but for bromine
      - `properties`: object
    - `I`:
      - `type`: object
      - `description`: Same structure as F but for iodine
      - `properties`: object
    - `energetics`:
      - `type`: object
      - `properties`:
        - `F`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `complexation_energy_inv`:
                - `type`: number
                - `unit`: kJ/mol
              - `complexation_energy_ret`:
                - `type`: number
                - `unit`: kJ/mol
              - `central_barrier_inv`:
                - `type`: number
                - `unit`: kJ/mol
              - `central_barrier_ret`:
                - `type`: number
                - `unit`: kJ/mol
              - `overall_barrier_inv`:
                - `type`: number
                - `unit`: kJ/mol
              - `overall_barrier_ret`:
                - `type`: number
                - `unit`: kJ/mol
        - `Cl`:
          - `type`: array
          - `items`:
            - `type`: object
        - `Br`:
          - `type`: array
          - `items`:
            - `type`: object
        - `I`:
          - `type`: array
          - `items`:
            - `type`: object
    - `looseness_parameters`:
      - `type`: object
      - `properties`:
        - `F`:
          - `type`: object
          - `properties`:
            - `%N-X^neq_inv`:
              - `type`: number
            - `%Li-X^neq_inv`:
              - `type`: number
            - `%N-X^neq_ret`:
              - `type`: number
            - `%Li-X^neq_ret`:
              - `type`: number
        - `Cl`:
          - `type`: object
          - `properties`: object
        - `Br`:
          - `type`: object
          - `properties`: object
        - `I`:
          - `type`: object
          - `properties`: object

Notes: The computed_results.json must contain all required fields; the checker will parse it to verify numeric tolerances and trend ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "F",
          "Cl",
          "Br",
          "I",
          "energetics",
          "looseness_parameters"
        ],
        "properties": {
          "F": {
            "type": "object",
            "description": "Per-halogen species data",
            "properties": {
              "LiX": {
                "type": "object",
                "properties": {
                  "bond_lengths": {
                    "type": "object",
                    "description": "atom pair -> Å"
                  },
                  "frequencies": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "description": "cm⁻¹"
                  },
                  "dipole_moment": {
                    "type": "number",
                    "description": "Debye"
                  },
                  "dissociation_energy": {
                    "type": "number",
                    "description": "kJ/mol"
                  }
                }
              },
              "NH2X": {
                "type": "object",
                "properties": {
                  "bond_lengths": {
                    "type": "object"
                  },
                  "frequencies": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "dipole_moment": {
                    "type": "number"
                  },
                  "dissociation_energy": {
                    "type": "number"
                  }
                }
              },
              "complex_inv": {
                "type": "object",
                "properties": {
                  "bond_lengths": {
                    "type": "object"
                  },
                  "frequencies": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "dipole_moment": {
                    "type": "number"
                  }
                }
              },
              "complex_ret": {
                "type": "object",
                "properties": {
                  "bond_lengths": {
                    "type": "object"
                  },
                  "frequencies": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "dipole_moment": {
                    "type": "number"
                  }
                }
              },
              "ts_inv": {
                "type": "object",
                "properties": {
                  "bond_lengths": {
                    "type": "object"
                  },
                  "frequencies": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "dipole_moment": {
                    "type": "number"
                  }
                }
              },
              "ts_ret": {
                "type": "object",
                "properties": {
                  "bond_lengths": {
                    "type": "object"
                  },
                  "frequencies": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "dipole_moment": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "Cl": {
            "type": "object",
            "description": "Same structure as F but for chlorine",
            "properties": {}
          },
          "Br": {
            "type": "object",
            "description": "Same structure as F but for bromine",
            "properties": {}
          },
          "I": {
            "type": "object",
            "description": "Same structure as F but for iodine",
            "properties": {}
          },
          "energetics": {
            "type": "object",
            "properties": {
              "F": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "complexation_energy_inv": {
                      "type": "number",
                      "unit": "kJ/mol"
                    },
                    "complexation_energy_ret": {
                      "type": "number",
                      "unit": "kJ/mol"
                    },
                    "central_barrier_inv": {
                      "type": "number",
                      "unit": "kJ/mol"
                    },
                    "central_barrier_ret": {
                      "type": "number",
                      "unit": "kJ/mol"
                    },
                    "overall_barrier_inv": {
                      "type": "number",
                      "unit": "kJ/mol"
                    },
                    "overall_barrier_ret": {
                      "type": "number",
                      "unit": "kJ/mol"
                    }
                  }
                }
              },
              "Cl": {
                "type": "array",
                "items": {
                  "type": "object"
                }
              },
              "Br": {
                "type": "array",
                "items": {
                  "type": "object"
                }
              },
              "I": {
                "type": "array",
                "items": {
                  "type": "object"
                }
              }
            }
          },
          "looseness_parameters": {
            "type": "object",
            "properties": {
              "F": {
                "type": "object",
                "properties": {
                  "%N-X^neq_inv": {
                    "type": "number"
                  },
                  "%Li-X^neq_inv": {
                    "type": "number"
                  },
                  "%N-X^neq_ret": {
                    "type": "number"
                  },
                  "%Li-X^neq_ret": {
                    "type": "number"
                  }
                }
              },
              "Cl": {
                "type": "object",
                "properties": {}
              },
              "Br": {
                "type": "object",
                "properties": {}
              },
              "I": {
                "type": "object",
                "properties": {}
              }
            }
          }
        }
      },
      "description": "The aggregated computational results file, containing all structural parameters, energetics, and looseness parameters for all four halogens and both reaction pathways."
    }
  ],
  "notes": "The computed_results.json must contain all required fields; the checker will parse it to verify numeric tolerances and trend ordering."
}
```

## How you are scored
A hidden verifier inspects the artifacts you write under `/app/outputs`.
The scored artifact is `computed_results.json`; the other workflow steps
provide process evidence but are not directly scored.
The verifier compares your computed structural parameters (bond lengths,
frequencies) and energetic quantities (dissociation energies, complexation
energies, barriers, looseness parameters) against expected reference
values, and evaluates whether the results are physically consistent across
the halogen series and reaction pathways. Each component
carries a weight: quantitative agreement carries the largest share, and
trend correctness also contributes. The combined score is reported as a
single number between 0 and 1. Simply reporting numbers from the
literature without running the quantum chemical calculations will not
earn full credit; the verifier expects results that reflect genuine
computations.
