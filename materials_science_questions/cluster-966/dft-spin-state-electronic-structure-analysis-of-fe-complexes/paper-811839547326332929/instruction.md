# DFT ground-state spin and symmetry of FeCn charged clusters

## Problem background
Iron-doped carbon clusters are of interest in astrochemistry, catalysis, and nanomaterials, yet systematic knowledge of the electronic structure of charged iron-carbon chains (FeC_n^+ and FeC_n^-) across a range of cluster sizes remains incomplete. This task targets the computational mapping of the potential energy surfaces of linear, fan, and cyclic isomers of FeC_n^+ and FeC_n^- (n = 1–8) to identify the most stable electronic states. Understanding ground-state spin multiplicities, symmetries, and the energetic ordering of low-lying states for these systems establishes baseline patterns that inform the growth mechanisms and stability of larger iron-doped carbon species.

## Approach
The method uses density functional theory (DFT) at the B3LYP/6-311+G(d) level, a hybrid functional with a triple-zeta basis set including diffuse and polarization functions. The core idea is to treat each cluster as a molecular system and systematically explore the following degrees of freedom: cluster size (n = 1 to 8), net charge (+ or -), three structural conformations (linear, fan, cyclic), and four spin multiplicities (doublet, quartet, sextet, octet). For every combination, a geometry optimization followed by a harmonic vibrational frequency calculation is performed to obtain a stationary point and the corresponding zero-point vibrational energy (ZPVE) correction. From the resulting total energies, the ground-state spin (the multiplicity of the lowest-energy isomer) and the relative energies of all visited spin states (referenced to the ground state) are determined. Any open-source DFT package that supports the B3LYP functional and the 6-311+G(d) basis set can be used.

## Reproduction target
For every combination of cluster size n (1–8), charge (+ or -), and conformation (linear, fan, cyclic), compute the ground-state spin multiplicity (2S+1) and its symmetry label. Additionally, compute the ZPVE-corrected relative energies (in kcal/mol) of all successfully located spin states; the ground state is set to 0.0. The results must be written to `/app/outputs/system_summary.json` as an array of objects, each containing the fields `n`, `charge`, `conformation`, `ground_state_spin`, `ground_state_symmetry`, and `relative_energies` (a map from spin multiplicity as a string, e.g. "2", "4", "6", "8", to the relative energy in kcal/mol).

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- PySCF quantum chemistry framework: https://github.com/pyscf/pyscf
- NWChem computational chemistry software: https://github.com/nwchemgit/nwchem

## Workflow steps

### Step 1: DFT geometry optimization and frequency analysis
- Role: process
- Action: For every combination of cluster size n=1..8, charge (+/'−'), conformation (linear, fan, cyclic), and spin multiplicity (doublet, quartet, sextet, octet) that is chemically plausible, perform geometry optimization and harmonic vibrational frequency calculation at the B3LYP/6-311+G(d) level using an open-source DFT package. Save the total electronic energy with zero-point vibrational energy (ZPVE) correction for each located stationary point.
- Evidence: none

### Step 2: Compile electronic state summary
- Role: scored (load-bearing)
- Action: From the DFT calculation outputs, for each (n, charge, conformation) identify the lowest-energy spin state and compute ZPVE-corrected relative energies (kcal/mol) for all successfully located spin states. Write the result to system_summary.json.
- Output file: `/app/outputs/system_summary.json`
- Format: json
- Contract: Array of objects, each with: n (integer 1-8), charge (string '+' or '-'), conformation (string 'linear'/'fan'/'cyclic'), ground_state_spin (integer, 2S+1), ground_state_symmetry (string, e.g. '^6Σ'), relative_energies (object mapping spin multiplicity (as integer string) to ZPVE-corrected relative energy in kcal/mol, with ground state set to 0.0). Include all spin states successfully located.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/system_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### system_summary.json
- path: `/app/outputs/system_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Complete set of ground-state spin, symmetry, and relative energies for all FeC_n+/FeC_n- systems considered. The checker compares ground-state spin and symmetry to paper gold, verifies that energy ordering is consistent with tolerances, and confirms octet states are not competitive.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `n`:
        - `type`: integer
        - `minimum`: 1
        - `maximum`: 8
      - `charge`:
        - `type`: string
        - `enum`: `+`, `-`
      - `conformation`:
        - `type`: string
        - `enum`: `linear`, `fan`, `cyclic`
      - `ground_state_spin`:
        - `type`: integer
        - `minimum`: 2
        - `maximum`: 8
      - `ground_state_symmetry`:
        - `type`: string
      - `relative_energies`:
        - `type`: object
        - `additionalProperties`:
          - `type`: number
        - `description`: Keys are spin multiplicities as integer strings (e.g. '2','4','6','8'), values are ZPVE-corrected relative energies in kcal/mol; the ground state is set to 0.0.
    - `required`: `n`, `charge`, `conformation`, `ground_state_spin`, `ground_state_symmetry`, `relative_energies`

Notes: The verifier uses reference match against hidden paper gold for ground-state multiplicities and symmetries, and checks relative energy trends (e.g., quartet/sextet ordering, octet non-competitiveness) within tolerance. Tolerance values are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "system_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "n": {
              "type": "integer",
              "minimum": 1,
              "maximum": 8
            },
            "charge": {
              "type": "string",
              "enum": [
                "+",
                "-"
              ]
            },
            "conformation": {
              "type": "string",
              "enum": [
                "linear",
                "fan",
                "cyclic"
              ]
            },
            "ground_state_spin": {
              "type": "integer",
              "minimum": 2,
              "maximum": 8
            },
            "ground_state_symmetry": {
              "type": "string"
            },
            "relative_energies": {
              "type": "object",
              "additionalProperties": {
                "type": "number"
              },
              "description": "Keys are spin multiplicities as integer strings (e.g. '2','4','6','8'), values are ZPVE-corrected relative energies in kcal/mol; the ground state is set to 0.0."
            }
          },
          "required": [
            "n",
            "charge",
            "conformation",
            "ground_state_spin",
            "ground_state_symmetry",
            "relative_energies"
          ]
        }
      },
      "description": "Complete set of ground-state spin, symmetry, and relative energies for all FeC_n+/FeC_n- systems considered. The checker compares ground-state spin and symmetry to paper gold, verifies that energy ordering is consistent with tolerances, and confirms octet states are not competitive."
    }
  ],
  "notes": "The verifier uses reference match against hidden paper gold for ground-state multiplicities and symmetries, and checks relative energy trends (e.g., quartet/sextet ordering, octet non-competitiveness) within tolerance. Tolerance values are hidden."
}
```

## How you are scored
A hidden verifier scores your work by comparing the content of `/app/outputs/system_summary.json` against paper-derived reference values. The verifier checks, for each system, whether the reported ground-state spin multiplicity and symmetry match the reference, whether the relative energy ordering of spin states is consistent with expectations (within a tolerance), and whether octet states are reported at sufficiently high relative energies. Each system's ground-state identification contributes to the final reward. Merely reporting correct-looking numbers is not enough—the verifier expects that all computed systems follow physically consistent trends. No paper titles, DOIs, or result values are provided; you must execute the complete DFT workflow yourself to produce the required summary.
