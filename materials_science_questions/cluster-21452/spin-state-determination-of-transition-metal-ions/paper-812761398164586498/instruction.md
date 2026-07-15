# DFT Spin-State Energetics and Exchange Coupling of Binuclear Cobalt Di-o-Quinone Complexes

## Problem background
Designing transition metal complexes with multiple accessible spin states that respond to different external stimuli (thermal, light) is important for molecular switches, sensors, and spintronics. This task investigates binuclear cobalt di-o-quinone complexes with polycyclic acene linkers using quantum chemical calculations to predict whether they can combine thermally switchable spin-state changes at the metal centers with photoinitiated singlet–triplet transitions of the linker. The key open questions are: what is the energetic ordering of the possible electromers (metal-centered spin-state combinations), and what are the magnetic exchange interactions between the paramagnetic centers? Answering these questions determines whether the complexes can function as dual-stimuli molecular switches.

## Approach
The computational approach is density functional theory (DFT) with the UTPSSh (or TPSS0) functional and the 6-311++G(d,p) basis set. For each molecular complex defined in the workflow, build the geometry, perform an unrestricted geometry optimization, and check wavefunction stability. Then compute total energies and <S²> expectation values. To extract exchange coupling constants J (cm⁻¹), use the broken‑symmetry (BS) DFT formalism with the generalized spin‑projection (GSP) method; set up high‑spin and the relevant broken‑symmetry determinants for the paramagnetic electromers. All calculations will be re‑implemented with the open‑source quantum chemistry package ORCA (≥5.0.3). The complexes to study are binuclear systems I (with acene linker lengths n=0 and n=2), II (n=1), and the model mononuclear compounds III (n=2) and IV (n=1), which help characterise the magnetic behavior of the linker.

## Reproduction target
Produce two scored artifacts:

1. **Relative electromer energies** (`relative_energies.json`): For all specified electromers of complexes I (n=0,2), II (n=1), III (n=2), and IV (n=1), report the total energy E_au, relative energy ΔE (kcal/mol) with respect to the ground‑state electromer of each complex, total spin S, and <S²> expectation value.

2. **Exchange coupling constants** (`exchange_parameters.json`): For the relevant paramagnetic electromers of complex I (n=0) and model complexes III (n=2) and IV (n=1), report the exchange coupling constants J (cm⁻¹) between the paramagnetic centers labelled 1=Co, 2=SQ (semiquinone), 3=second SQ or linker carbon, 4=second Co or linker carbon.

The energetic ordering of electromers must be internally consistent, and the computed J values should reflect the expected ferromagnetic/antiferromagnetic character of the various Co–SQ, SQ–SQ, and Co–linker interactions.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- 6-311++G(d,p) basis set: https://www.basissetexchange.org/

## Workflow steps

### Step 1: DFT geometry optimization and energy evaluation for all electromers
- Role: process
- Action: Build the molecular structures of complexes I (n=0,2), II (n=1), III (n=2), IV (n=1) as defined in the paper. For every electromer (LS-LS, LS-HS, HS-HS, catecholate for I(n=0); LS-LS, LS-HS, HS-HS for I(n=2) and II(n=1); LS and HS for III and IV), perform full unrestrained geometry optimization using the UTPSSh (or TPSS0) functional and the 6-311++G(d,p) basis set. Check wavefunction stability. Extract total energies E_tot (Hartree) and <S²> expectation values.
- Evidence: `/app/outputs/step01_geom_opt.log`

### Step 2: Broken-symmetry DFT and exchange coupling calculation
- Role: process
- Action: Using the optimized geometries from step01, set up broken-symmetry (BS) DFT calculations for the paramagnetic electromers: complex I (n=0) LS-LS, LS-HS, HS-HS; complex III (n=2) LS and HS; complex IV (n=1) LS and HS. For each, compute the energies of the high-spin state and all relevant broken-symmetry determinants needed to extract the exchange constants J_ij using the generalized spin-projection (GSP) method.
- Evidence: `/app/outputs/step02_j_calc.log`

### Step 3: Compile relative electromer energies
- Role: scored (load-bearing)
- Action: Collect the total energies from step01 for every electromer and compute relative energies (ΔE in kcal/mol) with respect to the ground-state electromer of each complex. Write the results to /app/outputs/relative_energies.json.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: Array of objects: {complex: string, electromer: string, S: number, E_au: number, dE_kcal: number, S2: number}. Example: [{complex: 'I_n0', electromer: 'LS_LS', S: 2, E_au: -6377.080699, dE_kcal: 0.0, S2: 6.031}, ...]
- Scoring: scored by hidden verifier

### Step 4: Compile exchange coupling constants
- Role: scored (load-bearing)
- Action: Collect the exchange coupling constants J (cm⁻¹) computed in step02 for the relevant electromers. Write the results to /app/outputs/exchange_parameters.json.
- Output file: `/app/outputs/exchange_parameters.json`
- Format: json
- Contract: Object with electromer keys; each value is an object with keys J12, J13, J14, J23, J24, J34 (some may be absent). Values in cm⁻¹. Example: {'I_n0_LS_LS': {J12: 535, J13: 1, J14: 9, J23: -17, J24: 1, J34: 535}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.json`
- `/app/outputs/exchange_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: A list of all computed electromers (complexes I(n=0,2), II(n=1), III(n=2), IV(n=1)) with total energies, relative energies, spin states, and S² expectations. The checker compares the agent's computed relative energies to the paper-reported reference values with an appropriate tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `complex`, `electromer`, `S`, `E_au`, `dE_kcal`, `S2`
    - `properties`:
      - `complex`:
        - `type`: string
      - `electromer`:
        - `type`: string
      - `S`:
        - `type`: number
      - `E_au`:
        - `type`: number
      - `dE_kcal`:
        - `type`: number
      - `S2`:
        - `type`: number

### exchange_parameters.json
- path: `/app/outputs/exchange_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Object mapping electromer keys (e.g., 'I_n0_LS_LS') to an object of J parameters (J12, J13, J14, J23, J24, J34). Values in cm⁻¹. The checker compares the agent's computed J parameters to the paper-reported reference values with an appropriate tolerance.
- schema:
  - `type`: object
  - `additionalProperties`:
    - `type`: object
    - `additionalProperties`:
      - `type`: number

Notes: The agent must re-implement the DFT calculations using an open-source tool (ORCA) and the same functional/basis set. All molecular geometries are constructed from the paper's description; no pre-built coordinates are provided. The hidden gold consists of the paper's reported relative energies and J parameters from Tables 1,2,4. Scoring tolerances account for implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "complex",
            "electromer",
            "S",
            "E_au",
            "dE_kcal",
            "S2"
          ],
          "properties": {
            "complex": {
              "type": "string"
            },
            "electromer": {
              "type": "string"
            },
            "S": {
              "type": "number"
            },
            "E_au": {
              "type": "number"
            },
            "dE_kcal": {
              "type": "number"
            },
            "S2": {
              "type": "number"
            }
          }
        }
      },
      "description": "A list of all computed electromers (complexes I(n=0,2), II(n=1), III(n=2), IV(n=1)) with total energies, relative energies, spin states, and S² expectations. The checker compares the agent's computed relative energies to the paper-reported reference values with an appropriate tolerance."
    },
    {
      "file": "exchange_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "additionalProperties": {
            "type": "number"
          }
        }
      },
      "description": "Object mapping electromer keys (e.g., 'I_n0_LS_LS') to an object of J parameters (J12, J13, J14, J23, J24, J34). Values in cm⁻¹. The checker compares the agent's computed J parameters to the paper-reported reference values with an appropriate tolerance."
    }
  ],
  "notes": "The agent must re-implement the DFT calculations using an open-source tool (ORCA) and the same functional/basis set. All molecular geometries are constructed from the paper's description; no pre-built coordinates are provided. The hidden gold consists of the paper's reported relative energies and J parameters from Tables 1,2,4. Scoring tolerances account for implementation spread."
}
```

## How you are scored
A hidden verifier independently scores each required output file. It compares your reported relative energies and exchange coupling constants to reference values derived from the original study. Tolerances are chosen to accommodate legitimate implementation differences (e.g., different DFT code, subtle convergence choices) while still requiring a genuine re‑computation of the quantum chemistry. The final reward is a weighted combination of the checks on `relative_energies.json` and `exchange_parameters.json`, with the relative energies contributing the larger share. Additional trend checks verify that the electromer energy ordering and the sign/magnitude pattern of key exchange couplings are physically reasonable. Note that simply reporting numbers without actually running the DFT workflow will not satisfy the verifier; you must produce the outputs through your own calculations.
