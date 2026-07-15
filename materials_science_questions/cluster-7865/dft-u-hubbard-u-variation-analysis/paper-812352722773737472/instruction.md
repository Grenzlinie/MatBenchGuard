# DFT study of Hf2Co: relaxed structure, partial charges, and electric field gradients

## Problem background
Hf2Co is an intermetallic compound crystallizing in the Ti2Ni-type structure (space group Fd-3m). Its electronic structure and bonding—a mixture of metallic, covalent, and ionic contributions—are of interest for potential hydrogen-storage applications. First‑principles electronic‑structure calculations can provide key physical quantities: the relaxed internal atomic coordinates, the distribution of valence charge among the atomic species, and the electric field gradient (EFG) tensor at the two inequivalent hafnium sites. The goal of this task is to compute these quantities using an all‑electron density‑functional‑theory (DFT) code and to output them in structured form for verification.

## Approach
The computations are performed with the Elk full‑potential linearized augmented plane‑wave (FP‑LAPW) code, employing the Perdew–Burke–Ernzerhof generalized gradient approximation. The primitive unit cell of Hf2Co (24 atoms, experimental lattice constant a = 12.066 Å, initial internal parameters u = 0.2142, v = 0.816) is used. Muffin‑tin radii are approximately 1.333 Å for Hf and 1.317 Å for Co. Structural relaxation is carried out by moving the Co and Hf2 atoms along their symmetry‑allowed directions until the Hellmann–Feynman forces are small. With the relaxed structure, a self‑consistent electronic‑structure calculation yields the total and site‑projected density of states, from which the l‑decomposed (s, p, d, f) partial charges inside the muffin‑tin spheres are extracted for the Hf1 (16c), Hf2 (48f) and Co sites. Finally, the EFG tensor at the two Hf positions is computed and its largest principal component V_ZZ (in 10^17 V cm⁻²) and asymmetry parameter η are reported.

## Reproduction target
Reproduce the DFT‑predicted relaxed internal parameters u and v for the Hf2Co primitive cell; the site‑projected s, p, d, f charges inside the muffin‑tin spheres for the Hf atoms at the 16c and 48f Wyckoff positions and for Co; and the electric field gradient principal component V_ZZ (in 10^17 V cm⁻²) and asymmetry parameter η for both Hf sites. The results must be saved as three separate JSON files following the exact schemas given in the workflow steps.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Structural relaxation of Hf2Co
- Role: scored
- Action: Perform full structural relaxation of the primitive cell of Hf2Co (space group Fd-3m, 24 atoms) using FP-LAPW with PBE exchange-correlation functional, starting from the experimental lattice constant and initial atomic positions. Use the conventional muffin-tin radii. Relax until Hellmann-Feynman forces are small. Extract the relaxed internal parameters u and v.
- Output file: `/app/outputs/relaxed_params.json`
- Format: json
- Contract: {"type": "object", "required": ["u", "v", "units"], "properties": {"u": {"type": "number"}, "v": {"type": "number"}, "units": {"type": "string", "const": "dimensionless"}}}
- Scoring: scored by hidden verifier

### Step 2: Site-projected partial charges
- Role: scored
- Action: Using the relaxed structure, compute the electronic structure (total and site-projected density of states) and extract the l-decomposed site-projected partial charges inside the muffin-tin spheres for Hf1 (16c), Hf2 (48f), and Co. Use the same DFT settings (PBE, FP-LAPW).
- Output file: `/app/outputs/partial_charges.json`
- Format: json
- Contract: {"type": "object", "required": ["Hf1", "Hf2", "Co", "units"], "properties": {"Hf1": {"type": "object", "required": ["s","p","d","f"], "properties": {"s": {"type": "number"}, "p": {"type": "number"}, "d": {"type": "number"}, "f": {"type": "number"}}}, "Hf2": {"type": "object", "required": ["s","p","d","f"]}, "Co": {"type": "object", "required": ["s","p","d","f"]}, "units": {"type": "string", "const": "electrons"}}}
- Scoring: scored by hidden verifier

### Step 3: Electric field gradient calculation
- Role: scored (load-bearing)
- Action: Calculate the electric field gradient tensor at the Hf1 (16c) and Hf2 (48f) lattice sites in the relaxed Hf2Co structure using the same DFT method. Extract the largest principal component V_ZZ (in 10^17 V/cm^2) and the asymmetry parameter eta. Report values for both sites.
- Output file: `/app/outputs/efg_params.json`
- Format: json
- Contract: {"type": "object", "required": ["16c", "48f", "units"], "properties": {"16c": {"type": "object", "required": ["V_ZZ","eta","site"], "properties": {"V_ZZ": {"type": "number"}, "eta": {"type": "number"}, "site": {"type": "string", "const": "Hf1"}}}, "48f": {"type": "object", "required": ["V_ZZ","eta","site"], "properties": {"V_ZZ": {"type": "number"}, "eta": {"type": "number"}, "site": {"type": "string", "const": "Hf2"}}}, "units": {"type": "string", "const": "V_ZZ in 10^17 V/cm^2"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_params.json`
- `/app/outputs/partial_charges.json`
- `/app/outputs/efg_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_params.json
- path: `/app/outputs/relaxed_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed internal parameters u and v after DFT structural relaxation, compared against paper-reported values with absolute tolerance.
- schema:
  - `type`: object
  - `required`: `u`, `v`, `units`
  - `properties`:
    - `u`:
      - `type`: number
    - `v`:
      - `type`: number
    - `units`:
      - `type`: string
      - `const`: dimensionless

### partial_charges.json
- path: `/app/outputs/partial_charges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: l-decomposed site-projected charges inside muffin-tin spheres for Hf1, Hf2, and Co, compared against paper Table 3 with relative tolerance.
- schema:
  - `type`: object
  - `required`: `Hf1`, `Hf2`, `Co`, `units`
  - `properties`:
    - `Hf1`:
      - `type`: object
      - `required`: `s`, `p`, `d`, `f`
      - `properties`:
        - `s`:
          - `type`: number
        - `p`:
          - `type`: number
        - `d`:
          - `type`: number
        - `f`:
          - `type`: number
    - `Hf2`:
      - `type`: object
      - `required`: `s`, `p`, `d`, `f`
    - `Co`:
      - `type`: object
      - `required`: `s`, `p`, `d`, `f`
    - `units`:
      - `type`: string
      - `const`: electrons

### efg_params.json
- path: `/app/outputs/efg_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: EFG principal component V_ZZ and asymmetry parameter eta at the two Hf sites, compared against paper Table 5 values with relative/absolute tolerances and sign match.
- schema:
  - `type`: object
  - `required`: `16c`, `48f`, `units`
  - `properties`:
    - `16c`:
      - `type`: object
      - `required`: `V_ZZ`, `eta`, `site`
      - `properties`:
        - `V_ZZ`:
          - `type`: number
        - `eta`:
          - `type`: number
        - `site`:
          - `type`: string
          - `const`: Hf1
    - `48f`:
      - `type`: object
      - `required`: `V_ZZ`, `eta`, `site`
      - `properties`:
        - `V_ZZ`:
          - `type`: number
        - `eta`:
          - `type`: number
        - `site`:
          - `type`: string
          - `const`: Hf2
    - `units`:
      - `type`: string
      - `const`: V_ZZ in 10^17 V/cm^2

Notes: The task reproduces the FP-LAPW electronic-structure calculations of pure Hf2Co. Tantalum-impurity supercell calculations and TDPAC experimental data are excluded. The agent must install and run the open-source Elk code. The hidden checker compares the submitted values to paper-reported gold values with predefined tolerances (absolute 0.005 for u,v; relative 20% for partial charges; relative 50% for V_ZZ with sign match; absolute 0.15 for eta).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "u",
          "v",
          "units"
        ],
        "properties": {
          "u": {
            "type": "number"
          },
          "v": {
            "type": "number"
          },
          "units": {
            "type": "string",
            "const": "dimensionless"
          }
        }
      },
      "description": "Relaxed internal parameters u and v after DFT structural relaxation, compared against paper-reported values with absolute tolerance."
    },
    {
      "file": "partial_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Hf1",
          "Hf2",
          "Co",
          "units"
        ],
        "properties": {
          "Hf1": {
            "type": "object",
            "required": [
              "s",
              "p",
              "d",
              "f"
            ],
            "properties": {
              "s": {
                "type": "number"
              },
              "p": {
                "type": "number"
              },
              "d": {
                "type": "number"
              },
              "f": {
                "type": "number"
              }
            }
          },
          "Hf2": {
            "type": "object",
            "required": [
              "s",
              "p",
              "d",
              "f"
            ]
          },
          "Co": {
            "type": "object",
            "required": [
              "s",
              "p",
              "d",
              "f"
            ]
          },
          "units": {
            "type": "string",
            "const": "electrons"
          }
        }
      },
      "description": "l-decomposed site-projected charges inside muffin-tin spheres for Hf1, Hf2, and Co, compared against paper Table 3 with relative tolerance."
    },
    {
      "file": "efg_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "16c",
          "48f",
          "units"
        ],
        "properties": {
          "16c": {
            "type": "object",
            "required": [
              "V_ZZ",
              "eta",
              "site"
            ],
            "properties": {
              "V_ZZ": {
                "type": "number"
              },
              "eta": {
                "type": "number"
              },
              "site": {
                "type": "string",
                "const": "Hf1"
              }
            }
          },
          "48f": {
            "type": "object",
            "required": [
              "V_ZZ",
              "eta",
              "site"
            ],
            "properties": {
              "V_ZZ": {
                "type": "number"
              },
              "eta": {
                "type": "number"
              },
              "site": {
                "type": "string",
                "const": "Hf2"
              }
            }
          },
          "units": {
            "type": "string",
            "const": "V_ZZ in 10^17 V/cm^2"
          }
        }
      },
      "description": "EFG principal component V_ZZ and asymmetry parameter eta at the two Hf sites, compared against paper Table 5 values with relative/absolute tolerances and sign match."
    }
  ],
  "notes": "The task reproduces the FP-LAPW electronic-structure calculations of pure Hf2Co. Tantalum-impurity supercell calculations and TDPAC experimental data are excluded. The agent must install and run the open-source Elk code. The hidden checker compares the submitted values to paper-reported gold values with predefined tolerances (absolute 0.005 for u,v; relative 20% for partial charges; relative 50% for V_ZZ with sign match; absolute 0.15 for eta)."
}
```

## How you are scored
A hidden verifier reads each of your three output JSON files and compares the numerical entries to reference values (not disclosed to you). Each artifact is scored individually, with tolerances appropriate for the re‑computation of DFT results from a different code generation. The three scores are combined with a weighted average; the EFG step carries the most weight, the relaxed‑parameters step the least. Additionally, the verifier checks that the relative magnitudes and structural trends among the EFG parameters are physically consistent. Your total reward is a float between 0 and 1; reporting numerically plausible values that pass all checks yields a non‑zero score, and close agreement with the reference gives the highest reward.
