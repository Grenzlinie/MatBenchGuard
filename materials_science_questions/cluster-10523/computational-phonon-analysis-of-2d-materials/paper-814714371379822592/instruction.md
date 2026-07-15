# First-Principles Dielectric and Phonon Properties of Ordered Ba(B′₁/₃B″₂/₃)O₃ Compounds

## Problem background
Microwave dielectric resonators and filters are key components in modern communication systems. The 1:2 ordered complex perovskites Ba(B′₁/₃B″₂/₃)O₃ (B′ = Mg²⁺, Zn²⁺; B″ = Ta⁵⁺, Nb⁵⁺) exhibit an excellent combination of moderate dielectric constant, high quality factor, and near-zero temperature coefficient of resonant frequency, making them indispensable for wireless communication. However, the detailed microscopic mechanisms that determine their intrinsic dielectric properties—specifically the role of B-site cation substitutions on the lattice dynamics and dielectric response—remain insufficiently understood. First-principles density functional perturbation theory (DFPT) can provide quantitative insights by computing zone-center optical phonon frequencies, mode effective charges, and the decomposition of the dielectric tensor into atomic contributions. This task investigates the intrinsic dielectric response and polar phonon properties of three representative compounds: Ba(Mg₁/₃Ta₂/₃)O₃ (BMT), Ba(Mg₁/₃Nb₂/₃)O₃ (BMN), and Ba(Zn₁/₃Nb₂/₃)O₃ (BZN). The goal is to compute these quantities and thereby uncover how replacing Ta with Nb and Mg with Zn affects the vibrational and dielectric behavior.

## Approach
The calculations are performed within density functional theory (DFT) using the generalized gradient approximation (PBE) and the projector-augmented wave (PAW) method. Starting from the experimental crystal structures (space group P-3m1, 15 atoms per primitive cell), the atomic positions are relaxed at fixed lattice parameters until the residual forces are small. For each compound, a subsequent DFPT calculation at the Γ point yields the zone-center dynamical matrix, Born effective charge tensors, and the electronic and lattice contributions to the dielectric tensor. From these outputs we extract: (i) the electronic and lattice dielectric tensors and the average static dielectric constant, (ii) the frequencies of all Γ-point optical phonon modes (IR-active E_u and A_2u, Raman-active A_1g and E_g), (iii) the mode effective charges Z*_{λ,α} for the dominant IR-active modes and their decomposition into contributions from individual ions, and (iv) the per-atom contributions to the lattice dielectric tensor (ε_i,αβ) for each unique atomic site. The analysis thus provides a complete picture of the intrinsic dielectric response. The workflow is implemented with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials, ensuring full reproducibility without proprietary software.

## Reproduction target
For the three compounds BMT, BMN, and BZN, compute and report in a single structured JSON file (step_04_computed_properties.json) the following quantities:

1. **Dielectric constants** – the electronic dielectric tensor components (ε∞,₁₁, ε∞,₃₃), the lattice dielectric tensor components (ε_ph,₁₁, ε_ph,₃₃), the total dielectric tensor components (ε₁₁, ε₃₃), and the average static dielectric constant ε̅ = (2ε₁₁ + ε₃₃)/3.

2. **Phonon frequencies** – the frequencies (cm⁻¹) of all zone-center optical modes sorted by symmetry: IR-active E_u (doubly degenerate) and A₂_u (singlet), and Raman-active A₁_g and E_g modes.

3. **Mode effective charges** – for the dominant IR modes (E_u(6), E_u(7), E_u(8), A₂_u(4), A₂_u(5), A₂_u(6)), report the total mode effective charge Z*_{λ,α} and its decomposition into contributions from individual ions, i.e., the atomic mode effective charges Z*^k_{λ,α} for Ba1, Ba2, B′, B″, O1, and O2.

4. **Per-atom dielectric contributions** – the contribution of each atomic sublattice (Ba1, Ba2, B′, B″, O1, O2) to the lattice dielectric tensor elements ε_i,₁₁ and ε_i,₃₃. The sum of these per-atom contributions should approximately equal the total lattice dielectric components.

The output file must conform to the schema described in the Output contract section.

## Assets

- Crystal structures of 1:2 ordered Ba perovskites from Lufaso 2004: 10.1021/cm049721w
- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP PBE PAW pseudopotentials: https://www.materialscloud.org/discover/sssp/table/pbe

## Workflow steps

### Step 1: DFT geometry optimization of the primitive cells
- Role: process
- Action: For each compound (BMT, BMN, BZN), build the initial crystal structure using the experimental lattice parameters and Wyckoff positions from Lufaso 2004 (space group P-3m1, 15 atoms per cell). Perform a fixed-cell relaxation of internal coordinates with Quantum ESPRESSO pw.x using PBE PAW pseudopotentials. Converge forces to a tight threshold.
- Evidence: `/app/outputs/relax.out`

### Step 2: DFPT phonon and dielectric tensor calculations
- Role: process
- Action: For each relaxed structure, run a Gamma-point DFPT calculation with Quantum ESPRESSO ph.x to compute zone-center dynamical matrices, phonon frequencies, Born effective charges, and dielectric tensors (electronic and lattice). Use the same pseudopotentials.
- Evidence: `/app/outputs/ph.out`

### Step 3: Compile intrinsic dielectric properties and phonon frequencies
- Role: scored (load-bearing)
- Action: Parse the DFT/DFPT outputs and compile a JSON file containing: (1) electronic and lattice dielectric tensor components and average static dielectric constants for each compound; (2) zone-center optical phonon frequencies for all IR-active (E_u, A_2u) and Raman-active (A_1g, E_g) modes; (3) mode effective charges Z*_λ,α for dominant IR modes and contributions from each ion; (4) per-atom contributions to the lattice dielectric tensor.
- Output file: `/app/outputs/step_04_computed_properties.json`
- Format: json
- Contract: object with keys: 'dielectric_constants' (object per compound with 'average', 'epsilon_11', 'epsilon_33'), 'phonon_frequencies' (object per compound with 'IR_active' (object with lists 'E_u', 'A_2u') and 'Raman_active' list), 'mode_effective_charges' (object per compound, each with mode keys mapping to lists of numbers), 'per_atom_dielectric_contributions' (object per compound with atom-type keys 'Ba1','Ba2','B_prime','B_doubleprime','O1','O2', each with 'epsilon_i_11','epsilon_i_33').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_computed_properties.json
- path: `/app/outputs/step_04_computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled DFT+DFPT results: dielectric constants, phonon frequencies, mode effective charges, and per-atom lattice dielectric contributions.
- schema:
  - `type`: object
  - `required`: `dielectric_constants`, `phonon_frequencies`, `mode_effective_charges`, `per_atom_dielectric_contributions`
  - `dielectric_constants`:
    - `type`: object
    - `keys`: `BMT`, `BMN`, `BZN`
    - `values`:
      - `type`: object
      - `required`: `average`, `epsilon_11`, `epsilon_33`
      - `average`: float
      - `epsilon_11`: float
      - `epsilon_33`: float
  - `phonon_frequencies`:
    - `type`: object
    - `keys`: `BMT`, `BMN`, `BZN`
    - `values`:
      - `type`: object
      - `required`: `IR_active`, `Raman_active`
      - `IR_active`:
        - `type`: object
        - `required`: `E_u`, `A_2u`
        - `E_u`: list[float]
        - `A_2u`: list[float]
      - `Raman_active`: list[float]
  - `mode_effective_charges`:
    - `type`: object
    - `keys`: `BMT`, `BMN`, `BZN`
    - `values`:
      - `type`: object
      - `mode_keys`: `E_u_6`, `E_u_7`, `E_u_8`, `A_2u_4`, `A_2u_5`, `A_2u_6`
      - `mode_value`: list[float] (total mode charge or list of atomic contributions)
  - `per_atom_dielectric_contributions`:
    - `type`: object
    - `keys`: `BMT`, `BMN`, `BZN`
    - `values`:
      - `type`: object
      - `atom_keys`: `Ba1`, `Ba2`, `B_prime`, `B_doubleprime`, `O1`, `O2`
      - `each`:
        - `type`: object
        - `required`: `epsilon_i_11`, `epsilon_i_33`
        - `epsilon_i_11`: float
        - `epsilon_i_33`: float

Notes: All values are computed from first-principles; the checker compares the submitted quantities against paper-reported reference values with moderate tolerances. Units: dielectric constants dimensionless, phonon frequencies cm⁻¹, mode effective charges in |e|.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "dielectric_constants",
          "phonon_frequencies",
          "mode_effective_charges",
          "per_atom_dielectric_contributions"
        ],
        "dielectric_constants": {
          "type": "object",
          "keys": [
            "BMT",
            "BMN",
            "BZN"
          ],
          "values": {
            "type": "object",
            "required": [
              "average",
              "epsilon_11",
              "epsilon_33"
            ],
            "average": "float",
            "epsilon_11": "float",
            "epsilon_33": "float"
          }
        },
        "phonon_frequencies": {
          "type": "object",
          "keys": [
            "BMT",
            "BMN",
            "BZN"
          ],
          "values": {
            "type": "object",
            "required": [
              "IR_active",
              "Raman_active"
            ],
            "IR_active": {
              "type": "object",
              "required": [
                "E_u",
                "A_2u"
              ],
              "E_u": "list[float]",
              "A_2u": "list[float]"
            },
            "Raman_active": "list[float]"
          }
        },
        "mode_effective_charges": {
          "type": "object",
          "keys": [
            "BMT",
            "BMN",
            "BZN"
          ],
          "values": {
            "type": "object",
            "mode_keys": [
              "E_u_6",
              "E_u_7",
              "E_u_8",
              "A_2u_4",
              "A_2u_5",
              "A_2u_6"
            ],
            "mode_value": "list[float] (total mode charge or list of atomic contributions)"
          }
        },
        "per_atom_dielectric_contributions": {
          "type": "object",
          "keys": [
            "BMT",
            "BMN",
            "BZN"
          ],
          "values": {
            "type": "object",
            "atom_keys": [
              "Ba1",
              "Ba2",
              "B_prime",
              "B_doubleprime",
              "O1",
              "O2"
            ],
            "each": {
              "type": "object",
              "required": [
                "epsilon_i_11",
                "epsilon_i_33"
              ],
              "epsilon_i_11": "float",
              "epsilon_i_33": "float"
            }
          }
        }
      },
      "description": "Compiled DFT+DFPT results: dielectric constants, phonon frequencies, mode effective charges, and per-atom lattice dielectric contributions."
    }
  ],
  "notes": "All values are computed from first-principles; the checker compares the submitted quantities against paper-reported reference values with moderate tolerances. Units: dielectric constants dimensionless, phonon frequencies cm⁻¹, mode effective charges in |e|."
}
```

## How you are scored
A hidden verifier will automatically evaluate your submitted `step_04_computed_properties.json`. The verifier compares the reported dielectric constants and selected dominant phonon frequencies to reference values (derived from the original study) with prescribed tolerances that account for expected implementation-related differences (choice of code, pseudopotentials, convergence settings). It also verifies that the mode effective charges and per-atom contributions are present and internally consistent (for example, that the per-atom contributions sum approximately to the total lattice dielectric component). The overall reward is a weighted average: approximately 40% for the average static dielectric constants, 40% for the critical phonon frequencies, and 20% for the completeness and self-consistency of the mode effective charges and per-atom contributions. The exact tolerances and weighting factors are not disclosed. Reporting values that are plausible but not obtained from a genuine DFPT workflow will not yield a high score; you must execute the full computational pipeline.
