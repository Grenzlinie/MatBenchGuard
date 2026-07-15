# Recomputing Spin-Orbit Coupling Constants for a Cobalt Complex Spin-Crossover

## Problem background
Molecular-level memory devices that exploit spin-crossover phenomena can be read without UV-vis degradation if they couple proton and electron motion. This work experimentally and computationally examines photo-induced spin-crossover in the complex monomer [Co(Hbim)(C6H4O2)(NH3)2], a key building block for a hydrogen-bonded dimer that serves as a candidate molecular memory. The spin-crossover process involves transitions between low-spin (singlet) and high-spin (quintet) states via intermediate triplet states, and the efficiency of these spin-forbidden transitions is governed by spin-orbit coupling (SOC). Understanding the magnitudes of SOC matrix elements between specific low-lying electronic states is essential to determine whether efficient forward (low-spin → high-spin) and backward (high-spin → low-spin) spin-crossover pathways exist. This task requires recomputing these SOC constants to assess the feasibility of the proposed memory writing and erasing mechanisms.

## Approach
The reproduction adopts a multi-stage quantum chemical workflow. First, geometry optimizations of the monomer in the singlet, triplet, and quintet spin states are performed using density functional theory (B3LYP) with a mixed basis set (SBKJC effective core potential for Co, 6-31G(d,p) for light atoms). Next, time-dependent DFT (TD-B3LYP) calculations at each optimized geometry yield vertical excitation energies and assignments for the low-lying electronic states, confirming the qualitative energy ordering required for spin-crossover. Subsequently, a complete active space self-consistent field (CASSCF) calculation with an active space of 12 electrons in 9 orbitals (the five Co d orbitals plus the π/π* orbitals of the Hbim and bq ligands) provides a multiconfigurational reference wave function. Finally, a spin-orbit complete active space configuration interaction (SO-CASCI) calculation using the full Breit-Pauli Hamiltonian is performed on the CASSCF wave functions to diagonalize the spin-orbit CI matrix and extract the SOC matrix elements. The monomer model is sufficient because the spin-state conversions of the dimer correspond to combinations of monomer conversions. The calculations are carried out at the appropriate geometries: singlet-optimized geometry for the singlet and triplet states, and quintet-optimized geometry for the quintet states. The derived SOC values consist of six key constants: three associated with the forward pathway and three with the backward pathway, along with the derived conclusion of whether each pathway is preferred.

## Reproduction target
Compute the six spin-orbit coupling matrix elements (in cm⁻¹) for the state pairs that govern the forward and backward spin-crossover pathways of the monomer, and determine from those values whether the forward and backward crossover directions are preferred. Specifically, produce the following key SOC constants:
- SOC between the first excited singlet (1A'') and the lowest triplet (1³A'')
- SOC between the lowest triplet (1³A'') and the lowest quintet (5A')
- SOC between the lowest triplet (1³A'') and the ground singlet (1A')
- SOC between the first excited quintet (5A'') and the second triplet (2³A'')
- SOC between the first excited quintet (5A'') and the lowest triplet (1³A'')
- SOC between the second triplet (2³A'') and the ground singlet (1A')
Additionally, record boolean conclusions: whether the forward crossover from low-spin to high-spin is kinetically preferred, and whether the backward crossover from high-spin to low-spin is preferred, based solely on the magnitudes of the computed SOC values. The results must be saved to /app/outputs/soc_results.json in the exact JSON schema specified in the workflow steps.

## Assets

- GAMESS (or equivalent quantum chemistry software): https://www.msg.chem.iastate.edu/gamess/
- SBKJC VDZ ECP for Co and 6-31G(d,p) for H, C, N, O: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Geometry optimization of monomer in multiple spin states
- Role: process
- Action: Optimize the molecular geometry of [Co(Hbim)(C6H4O2)(NH3)2] in the singlet (1A'), triplet (13A''), and quintet (5A') spin states using B3LYP with SBKJC VDZ ECP for Co and 6-31G(d,p) for H, C, N, O. Keep the optimized coordinates for later steps.
- Evidence: `/app/outputs/optimized_coords.log`

### Step 2: TD-B3LYP calculation of low-lying excited states
- Role: process
- Action: Perform TD-B3LYP calculations at the optimized geometries of each spin state to obtain vertical excitation energies and assignments for the states 1A', 1A'', 13A'', 23A'', 5A', and 5A''. Verify that the qualitative energy ordering matches the scheme required for the spin-crossover mechanism.
- Evidence: `/app/outputs/td_b3lyp_output.log`

### Step 3: CASSCF(12,9) calculation of multiconfigurational reference wave functions
- Role: process
- Action: Run CASSCF(12,9) on the monomer using the active space comprising five Co d orbitals and the π/π* orbitals of Hbim and bq ligands. Extract the natural orbitals and the multiconfigurational reference wave function required for the spin-orbit CI step.
- Evidence: `/app/outputs/casscf_output.log`

### Step 4: SO-CASCI calculation of spin-orbit coupling constants
- Role: scored (load-bearing)
- Action: Using the CASSCF wave functions and the appropriately optimized geometries (1A' geometry for singlet and triplet states, 5A' geometry for quintet states), perform spin-orbit complete active space configuration interaction (SO-CASCI) with the full Breit-Pauli Hamiltonian. Diagonalize the spin-orbit CI matrix to obtain the SOC matrix elements. Extract the six key SOC values (cm⁻¹) for the forward (low-spin → high-spin) and backward (high-spin → low-spin) pathways and determine the preferred crossover directions. Write the results to soc_results.json.
- Output file: `/app/outputs/soc_results.json`
- Format: json
- Contract: JSON object with keys: forward_1A''_to_13A''_SOC_cm-1 (number), forward_13A''_to_5A'_SOC_cm-1 (number), forward_13A''_to_1A'_SOC_cm-1 (number), backward_5A''_to_23A''_SOC_cm-1 (number), backward_5A''_to_13A''_SOC_cm-1 (number), backward_23A''_to_1A'_SOC_cm-1 (number), forward_crossover_preferred (boolean), backward_crossover_preferred (boolean). All SOC values in cm⁻¹ as positive floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/soc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### soc_results.json
- path: `/app/outputs/soc_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin-orbit coupling constants for the six key state pairs governing forward and backward spin-crossover, plus boolean conclusions on pathway preference.
- schema:
  - `type`: object
  - `required`: `forward_1A''_to_13A''_SOC_cm-1`, `forward_13A''_to_5A'_SOC_cm-1`, `forward_13A''_to_1A'_SOC_cm-1`, `backward_5A''_to_23A''_SOC_cm-1`, `backward_5A''_to_13A''_SOC_cm-1`, `backward_23A''_to_1A'_SOC_cm-1`, `forward_crossover_preferred`, `backward_crossover_preferred`
  - `properties`:
    - `forward_1A''_to_13A''_SOC_cm-1`:
      - `type`: number
      - `unit`: cm^-1
    - `forward_13A''_to_5A'_SOC_cm-1`:
      - `type`: number
      - `unit`: cm^-1
    - `forward_13A''_to_1A'_SOC_cm-1`:
      - `type`: number
      - `unit`: cm^-1
    - `backward_5A''_to_23A''_SOC_cm-1`:
      - `type`: number
      - `unit`: cm^-1
    - `backward_5A''_to_13A''_SOC_cm-1`:
      - `type`: number
      - `unit`: cm^-1
    - `backward_23A''_to_1A'_SOC_cm-1`:
      - `type`: number
      - `unit`: cm^-1
    - `forward_crossover_preferred`:
      - `type`: boolean
    - `backward_crossover_preferred`:
      - `type`: boolean

Notes: The agent must recompute SOC values via SO-CASCI. The hidden checker compares each reported SOC value to the paper's gold within a tolerance and checks that both boolean conclusions are true.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "soc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "forward_1A''_to_13A''_SOC_cm-1",
          "forward_13A''_to_5A'_SOC_cm-1",
          "forward_13A''_to_1A'_SOC_cm-1",
          "backward_5A''_to_23A''_SOC_cm-1",
          "backward_5A''_to_13A''_SOC_cm-1",
          "backward_23A''_to_1A'_SOC_cm-1",
          "forward_crossover_preferred",
          "backward_crossover_preferred"
        ],
        "properties": {
          "forward_1A''_to_13A''_SOC_cm-1": {
            "type": "number",
            "unit": "cm^-1"
          },
          "forward_13A''_to_5A'_SOC_cm-1": {
            "type": "number",
            "unit": "cm^-1"
          },
          "forward_13A''_to_1A'_SOC_cm-1": {
            "type": "number",
            "unit": "cm^-1"
          },
          "backward_5A''_to_23A''_SOC_cm-1": {
            "type": "number",
            "unit": "cm^-1"
          },
          "backward_5A''_to_13A''_SOC_cm-1": {
            "type": "number",
            "unit": "cm^-1"
          },
          "backward_23A''_to_1A'_SOC_cm-1": {
            "type": "number",
            "unit": "cm^-1"
          },
          "forward_crossover_preferred": {
            "type": "boolean"
          },
          "backward_crossover_preferred": {
            "type": "boolean"
          }
        }
      },
      "description": "Spin-orbit coupling constants for the six key state pairs governing forward and backward spin-crossover, plus boolean conclusions on pathway preference."
    }
  ],
  "notes": "The agent must recompute SOC values via SO-CASCI. The hidden checker compares each reported SOC value to the paper's gold within a tolerance and checks that both boolean conclusions are true."
}
```

## How you are scored
A hidden verifier will evaluate your submitted soc_results.json. It will independently extract the six SOC values and the two boolean conclusions you computed. The SOC values are compared against an external reference using an appropriate tolerance; the closer your values are to the expected range, the higher the score. The boolean conclusions are checked for correctness based on the expected preference direction. Each component contributes a weighted share to the overall score, with the SOC values carrying the majority of the weight. To achieve a high score, you must faithfully execute the complete computational pipeline as described in the workflow steps; simply reporting numbers from the literature without performing the calculations will not earn credit. No additional data or internal thresholds are provided—your computed results are the sole basis for scoring.
