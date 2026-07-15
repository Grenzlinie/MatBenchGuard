# DFT nonlocal density functional: ground-state and band-gap predictions for semiconductors

## Problem background
Density functional theory (DFT) within the local density approximation (LDA) is widely used for electronic structure calculations, but LDA often overestimates binding energies and underestimates band gaps in semiconductors. A nonlocal density functional (NLDA) that incorporates the exchange-correlation kernel of the homogeneous electron gas has been proposed as a correction for weakly inhomogeneous systems. This task computes ground-state and electronic properties of several semiconductors using both LDA and NLDA to benchmark the functional's performance.

## Approach
The task implements the NLDA exchange-correlation functional together with the CPOD parametrization of the homogeneous electron gas kernel in a plane-wave DFT code. For each semiconductor (Si, diamond, SiC, GaAs) the solver generates norm-conserving pseudopotentials with both LDA and NLDA, performs pseudoatom total-energy calculations, and then carries out bulk total-energy scans over a range of lattice constants to extract equilibrium lattice constants, bulk moduli, and cohesive energies. In addition, direct band gaps at high-symmetry points (Γ, X, L) are obtained from band structure calculations at the theoretical lattice constant. The results are compared between LDA and NLDA to assess the differences introduced by the nonlocal correction.

## Reproduction target
Compute the equilibrium lattice constant a0 (a.u.), bulk modulus B0 (Mbar), and cohesive energy Eb (eV) for Si, diamond, SiC, and GaAs using both LDA and the NLDA functional, and write the results to `/app/outputs/bulk_properties.json`. For Si, diamond, and GaAs, compute the direct band gaps (eV) at the Γ, X, and L high-symmetry points for both functionals and write them to `/app/outputs/band_gaps.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Atomic code for pseudopotential generation (ld1.x or fhi98pp): Quantum ESPRESSO (ld1.x) or ABINIT (fhi98pp)
- CPOD parametrization of the homogeneous electron gas XC kernel: 10.1103/PhysRevB.57.14569
- Crystal structures: Si (diamond), C (diamond), SiC (zincblende), GaAs (zincblende)

## Workflow steps

### Step 1: Generate NLDA and LDA pseudopotentials
- Role: process
- Action: Generate norm-conserving pseudopotentials for Si, C, Ga, As using the Troullier-Martins or Hamann method, within both LDA and the NLDA functional that employs the CPOD exchange-correlation kernel. Ensure suitable cutoff radii for transferability in bulk and pseudoatom calculations. The pseudopotentials must be in a plane-wave code format (e.g., Quantum ESPRESSO UPF).
- Evidence: `/app/outputs/pp_generation.log`

### Step 2: Pseudoatom DFT total energies
- Role: process
- Action: For each element (Si, C, Ga, As), perform spin-unpolarized pseudoatom DFT calculations using the generated pseudopotentials and both the NLDA and LDA functionals. Use a large cubic cell to avoid interactions. Record the self-consistent total energy for each pseudoatom; these will be used to compute cohesive energies.
- Evidence: `/app/outputs/pseudoatom_energies.txt`

### Step 3: Bulk DFT and ground-state properties
- Role: scored (load-bearing)
- Action: For Si, diamond, SiC, and GaAs, perform plane-wave DFT total-energy calculations over a range of lattice constants using both LDA and NLDA, with appropriate k-point sampling and energy cutoffs. Fit the total energy versus volume to an equation of state to extract the equilibrium lattice constant a0 and bulk modulus B0, and obtain the total energy per atom at equilibrium. Compute the cohesive energy as the difference between the solid's total energy per atom and the pseudoatom energy from step s1. Output the results in /app/outputs/bulk_properties.json.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: A JSON object with top-level keys "Si", "C", "SiC", "GaAs". Each key maps to an object with numeric fields: a0_LDA, a0_NLDA, B0_LDA, B0_NLDA, Eb_LDA, Eb_NLDA.
- Scoring: scored by hidden verifier

### Step 4: Direct band gaps at Γ, X, L
- Role: scored
- Action: For Si, diamond, and GaAs, using the equilibrium lattice constant from step s2, perform a non-self-consistent band structure calculation and extract direct band gaps (eV) at the Γ, X, and L high-symmetry points for both LDA and NLDA. Output the results in /app/outputs/band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: A JSON object with top-level keys "Si", "C", "GaAs". Each key maps to an object with numeric fields: Gamma_LDA, Gamma_NLDA, X_LDA, X_NLDA, L_LDA, L_NLDA (all in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium lattice constants, bulk moduli, and cohesive energies for four semiconductors using LDA and NLDA exchange-correlation functionals.
- schema:
  - `type`: object
  - `required`: `Si`, `C`, `SiC`, `GaAs`
  - `properties`:
    - `Si`:
      - `type`: object
      - `required`: `a0_LDA`, `a0_NLDA`, `B0_LDA`, `B0_NLDA`, `Eb_LDA`, `Eb_NLDA`
      - `properties`:
        - `a0_LDA`:
          - `type`: number
          - `units`: a.u.
        - `a0_NLDA`:
          - `type`: number
          - `units`: a.u.
        - `B0_LDA`:
          - `type`: number
          - `units`: Mbar
        - `B0_NLDA`:
          - `type`: number
          - `units`: Mbar
        - `Eb_LDA`:
          - `type`: number
          - `units`: eV
        - `Eb_NLDA`:
          - `type`: number
          - `units`: eV
    - `C`:
      - `type`: object
      - `required`: `a0_LDA`, `a0_NLDA`, `B0_LDA`, `B0_NLDA`, `Eb_LDA`, `Eb_NLDA`
      - `properties`:
        - `a0_LDA`:
          - `type`: number
          - `units`: a.u.
        - `a0_NLDA`:
          - `type`: number
          - `units`: a.u.
        - `B0_LDA`:
          - `type`: number
          - `units`: Mbar
        - `B0_NLDA`:
          - `type`: number
          - `units`: Mbar
        - `Eb_LDA`:
          - `type`: number
          - `units`: eV
        - `Eb_NLDA`:
          - `type`: number
          - `units`: eV
    - `SiC`:
      - `type`: object
      - `required`: `a0_LDA`, `a0_NLDA`, `B0_LDA`, `B0_NLDA`, `Eb_LDA`, `Eb_NLDA`
      - `properties`:
        - `a0_LDA`:
          - `type`: number
          - `units`: a.u.
        - `a0_NLDA`:
          - `type`: number
          - `units`: a.u.
        - `B0_LDA`:
          - `type`: number
          - `units`: Mbar
        - `B0_NLDA`:
          - `type`: number
          - `units`: Mbar
        - `Eb_LDA`:
          - `type`: number
          - `units`: eV
        - `Eb_NLDA`:
          - `type`: number
          - `units`: eV
    - `GaAs`:
      - `type`: object
      - `required`: `a0_LDA`, `a0_NLDA`, `B0_LDA`, `B0_NLDA`, `Eb_LDA`, `Eb_NLDA`
      - `properties`:
        - `a0_LDA`:
          - `type`: number
          - `units`: a.u.
        - `a0_NLDA`:
          - `type`: number
          - `units`: a.u.
        - `B0_LDA`:
          - `type`: number
          - `units`: Mbar
        - `B0_NLDA`:
          - `type`: number
          - `units`: Mbar
        - `Eb_LDA`:
          - `type`: number
          - `units`: eV
        - `Eb_NLDA`:
          - `type`: number
          - `units`: eV

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gaps at high-symmetry points for Si, diamond, and GaAs computed with LDA and NLDA exchange-correlation functionals.
- schema:
  - `type`: object
  - `required`: `Si`, `C`, `GaAs`
  - `properties`:
    - `Si`:
      - `type`: object
      - `required`: `Gamma_LDA`, `Gamma_NLDA`, `X_LDA`, `X_NLDA`, `L_LDA`, `L_NLDA`
      - `properties`:
        - `Gamma_LDA`:
          - `type`: number
          - `units`: eV
        - `Gamma_NLDA`:
          - `type`: number
          - `units`: eV
        - `X_LDA`:
          - `type`: number
          - `units`: eV
        - `X_NLDA`:
          - `type`: number
          - `units`: eV
        - `L_LDA`:
          - `type`: number
          - `units`: eV
        - `L_NLDA`:
          - `type`: number
          - `units`: eV
    - `C`:
      - `type`: object
      - `required`: `Gamma_LDA`, `Gamma_NLDA`, `X_LDA`, `X_NLDA`, `L_LDA`, `L_NLDA`
      - `properties`:
        - `Gamma_LDA`:
          - `type`: number
          - `units`: eV
        - `Gamma_NLDA`:
          - `type`: number
          - `units`: eV
        - `X_LDA`:
          - `type`: number
          - `units`: eV
        - `X_NLDA`:
          - `type`: number
          - `units`: eV
        - `L_LDA`:
          - `type`: number
          - `units`: eV
        - `L_NLDA`:
          - `type`: number
          - `units`: eV
    - `GaAs`:
      - `type`: object
      - `required`: `Gamma_LDA`, `Gamma_NLDA`, `X_LDA`, `X_NLDA`, `L_LDA`, `L_NLDA`
      - `properties`:
        - `Gamma_LDA`:
          - `type`: number
          - `units`: eV
        - `Gamma_NLDA`:
          - `type`: number
          - `units`: eV
        - `X_LDA`:
          - `type`: number
          - `units`: eV
        - `X_NLDA`:
          - `type`: number
          - `units`: eV
        - `L_LDA`:
          - `type`: number
          - `units`: eV
        - `L_NLDA`:
          - `type`: number
          - `units`: eV

Notes: The checker compares the submitted values to hidden reference values derived from the original paper's reported results, within appropriate tolerances. The process steps (pseudopotential generation and pseudoatom energies) are required to be executed but their direct outputs are not scored; only the final ground-state properties and band gaps are evaluated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Si",
          "C",
          "SiC",
          "GaAs"
        ],
        "properties": {
          "Si": {
            "type": "object",
            "required": [
              "a0_LDA",
              "a0_NLDA",
              "B0_LDA",
              "B0_NLDA",
              "Eb_LDA",
              "Eb_NLDA"
            ],
            "properties": {
              "a0_LDA": {
                "type": "number",
                "units": "a.u."
              },
              "a0_NLDA": {
                "type": "number",
                "units": "a.u."
              },
              "B0_LDA": {
                "type": "number",
                "units": "Mbar"
              },
              "B0_NLDA": {
                "type": "number",
                "units": "Mbar"
              },
              "Eb_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Eb_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "C": {
            "type": "object",
            "required": [
              "a0_LDA",
              "a0_NLDA",
              "B0_LDA",
              "B0_NLDA",
              "Eb_LDA",
              "Eb_NLDA"
            ],
            "properties": {
              "a0_LDA": {
                "type": "number",
                "units": "a.u."
              },
              "a0_NLDA": {
                "type": "number",
                "units": "a.u."
              },
              "B0_LDA": {
                "type": "number",
                "units": "Mbar"
              },
              "B0_NLDA": {
                "type": "number",
                "units": "Mbar"
              },
              "Eb_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Eb_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "SiC": {
            "type": "object",
            "required": [
              "a0_LDA",
              "a0_NLDA",
              "B0_LDA",
              "B0_NLDA",
              "Eb_LDA",
              "Eb_NLDA"
            ],
            "properties": {
              "a0_LDA": {
                "type": "number",
                "units": "a.u."
              },
              "a0_NLDA": {
                "type": "number",
                "units": "a.u."
              },
              "B0_LDA": {
                "type": "number",
                "units": "Mbar"
              },
              "B0_NLDA": {
                "type": "number",
                "units": "Mbar"
              },
              "Eb_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Eb_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "GaAs": {
            "type": "object",
            "required": [
              "a0_LDA",
              "a0_NLDA",
              "B0_LDA",
              "B0_NLDA",
              "Eb_LDA",
              "Eb_NLDA"
            ],
            "properties": {
              "a0_LDA": {
                "type": "number",
                "units": "a.u."
              },
              "a0_NLDA": {
                "type": "number",
                "units": "a.u."
              },
              "B0_LDA": {
                "type": "number",
                "units": "Mbar"
              },
              "B0_NLDA": {
                "type": "number",
                "units": "Mbar"
              },
              "Eb_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Eb_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          }
        }
      },
      "description": "Computed equilibrium lattice constants, bulk moduli, and cohesive energies for four semiconductors using LDA and NLDA exchange-correlation functionals."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Si",
          "C",
          "GaAs"
        ],
        "properties": {
          "Si": {
            "type": "object",
            "required": [
              "Gamma_LDA",
              "Gamma_NLDA",
              "X_LDA",
              "X_NLDA",
              "L_LDA",
              "L_NLDA"
            ],
            "properties": {
              "Gamma_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Gamma_NLDA": {
                "type": "number",
                "units": "eV"
              },
              "X_LDA": {
                "type": "number",
                "units": "eV"
              },
              "X_NLDA": {
                "type": "number",
                "units": "eV"
              },
              "L_LDA": {
                "type": "number",
                "units": "eV"
              },
              "L_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "C": {
            "type": "object",
            "required": [
              "Gamma_LDA",
              "Gamma_NLDA",
              "X_LDA",
              "X_NLDA",
              "L_LDA",
              "L_NLDA"
            ],
            "properties": {
              "Gamma_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Gamma_NLDA": {
                "type": "number",
                "units": "eV"
              },
              "X_LDA": {
                "type": "number",
                "units": "eV"
              },
              "X_NLDA": {
                "type": "number",
                "units": "eV"
              },
              "L_LDA": {
                "type": "number",
                "units": "eV"
              },
              "L_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          },
          "GaAs": {
            "type": "object",
            "required": [
              "Gamma_LDA",
              "Gamma_NLDA",
              "X_LDA",
              "X_NLDA",
              "L_LDA",
              "L_NLDA"
            ],
            "properties": {
              "Gamma_LDA": {
                "type": "number",
                "units": "eV"
              },
              "Gamma_NLDA": {
                "type": "number",
                "units": "eV"
              },
              "X_LDA": {
                "type": "number",
                "units": "eV"
              },
              "X_NLDA": {
                "type": "number",
                "units": "eV"
              },
              "L_LDA": {
                "type": "number",
                "units": "eV"
              },
              "L_NLDA": {
                "type": "number",
                "units": "eV"
              }
            }
          }
        }
      },
      "description": "Direct band gaps at high-symmetry points for Si, diamond, and GaAs computed with LDA and NLDA exchange-correlation functionals."
    }
  ],
  "notes": "The checker compares the submitted values to hidden reference values derived from the original paper's reported results, within appropriate tolerances. The process steps (pseudopotential generation and pseudoatom energies) are required to be executed but their direct outputs are not scored; only the final ground-state properties and band gaps are evaluated."
}
```

## How you are scored
A hidden verifier reads your submitted artifact files and compares each reported quantity to a hidden reference value that corresponds to the main result of the original study, allowing appropriate tolerances for methodological spread. The verifier independently scores each of the two artifacts, combines them with pre-defined weights (with the ground-state properties receiving the larger share), and writes a final reward between 0 and 1. Submitting correct values from a faithful reproduction yields the highest reward, but merely reporting the paper's numbers without executing the required calculations will not suffice because the verifier checks for consistency of trends and magnitudes across the full workflow.
