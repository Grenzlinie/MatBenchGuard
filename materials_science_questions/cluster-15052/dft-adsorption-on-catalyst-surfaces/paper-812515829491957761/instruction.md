# H2S Stability Ranking of Metal-Organic Frameworks via DFT

## Problem background
Metal–organic frameworks (MOFs) are promising for gas separation and capture, but their practical use depends on stability under harsh conditions, particularly exposure to hydrogen sulfide (H₂S) present in natural gas and flue gas. Experimental stability testing of MOFs with H₂S is challenging due to the gas's high toxicity and corrosiveness. This computational study tackles the problem by using periodic density functional theory (DFT) to systematically evaluate the first-step degradation mechanism of MOFs upon H₂S adsorption and to derive a rate constant that characterizes their stability. The goal is to compute and compare the relative stability ordering of several MIL-53(Al) variants using this approach, thereby demonstrating how computational modelling can guide the design of robust MOFs.

## Approach
The approach employs periodic DFT calculations to simulate the reaction between an H₂S molecule and the MOF framework. For each MOF, the empty framework and the H₂S-adsorbed initial state are geometry optimized. The first-step degradation pathway investigated is Mechanism 1: cleavage of one Al–O bond, proton transfer from H₂S to a μ-O site, and formation of an Al–S bond. The climbing-image nudged elastic band (CI-NEB) method is used to locate the transition state (TS) and final state (FS) along this reaction coordinate. Harmonic vibrational frequencies are computed to confirm that the initial and final states are minima and the TS is a first-order saddle point. From the DFT energies and vibrational frequencies, the reaction energy and energy barrier are determined, and free energy barriers at 298 K are computed. The rate constant k is then calculated from the free energy barriers using an Eyring-type expression (accounting for forward and reverse barriers). The resulting k for each MOF serves as a descriptor of its stability: a more negative k indicates a higher kinetic barrier to degradation and thus a more stable framework. This protocol is applied to the isoreticular series MIL-53(Al)-BDC, MIL-53(Al)-FA, and MIL-53(Al)-TDC to establish their stability ranking.

## Reproduction target
Using the computational workflow described above, compute the rate constant k at 298 K for the first-step H₂S degradation reaction (Mechanism 1) for MIL-53(Al)-BDC, MIL-53(Al)-FA, and MIL-53(Al)-TDC. Report the quantities in the file step_05_rate_constants.json. The primary objective is to verify that the three MOFs follow a specific relative ordering of stabilities: one of the three is significantly more stable (much more negative k) than the other two, while the other two have comparable rate constants. The check will be based on the qualitative trend among the computed k values.

## Assets

- Periodic DFT software with CI-NEB (e.g., Quantum ESPRESSO, CP2K, or VASP): https://www.quantum-espresso.org
- PBE pseudopotentials (PAW or USPP): https://www.materialscloud.org/discover/sssp/table/efficiency
- Grimme's DFT-D3 dispersion correction: https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3
- Crystal structures of MIL-53(Al)-BDC, MIL-53(Al)-FA, MIL-53(Al)-TDC

## Workflow steps

### Step 1: Prepare initial structures
- Role: process
- Action: Obtain crystal structures of MIL-53(Al)-BDC, MIL-53(Al)-FA, and MIL-53(Al)-TDC from public databases and set up unit cells for DFT input (including supercell construction if needed).
- Evidence: none

### Step 2: Optimize empty MOF geometries
- Role: process
- Action: Perform periodic DFT geometry optimizations for the empty MOFs using PBE functional, DFT-D3 dispersion correction, and an appropriate plane-wave cutoff. Obtain optimized structures and total energies.
- Evidence: none

### Step 3: Optimize H₂S adsorption state (IS)
- Role: process
- Action: Introduce one H₂S molecule per unit cell into each optimized empty MOF, then perform DFT geometry optimization to locate the most stable initial adsorption configuration (IS).
- Evidence: none

### Step 4: CI-NEB and frequency calculations for Mechanism 1
- Role: process
- Action: For each MOF, set up the reaction coordinate for Mechanism 1 (cleavage of one Al–O bond, proton transfer to μ-O, Al–S bond formation), run climbing-image NEB to locate the transition state (TS) and final state (FS), then perform harmonic frequency calculations to confirm stationary points.
- Evidence: none

### Step 5: Compute rate constants
- Role: scored (load-bearing)
- Action: From the DFT energies and vibrational frequencies of IS, TS, and FS, compute the reaction energy ΔE, barrier ΔE‡, and free energy corrections at 298 K. Calculate the rate constant k using the Eyring-type formula and write the results to step_05_rate_constants.json.
- Output file: `/app/outputs/step_05_rate_constants.json`
- Format: json
- Contract: Array of objects, each with keys: MOF (string, one of 'MIL-53(Al)-BDC', 'MIL-53(Al)-FA', 'MIL-53(Al)-TDC'), barrier_kJ_per_mol (float, ΔE‡), reaction_energy_kJ_per_mol (float, ΔE), rate_constant (float, k at 298 K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_05_rate_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_05_rate_constants.json
- path: `/app/outputs/step_05_rate_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Rate constants k (at 298 K), energy barriers ΔE‡, and reaction energies ΔE for the first-step H₂S degradation mechanism for MIL-53(Al)-BDC, -FA, and -TDC. The checker verifies the relative ordering of k and barrier values against expected physical trends.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `MOF`, `barrier_kJ_per_mol`, `reaction_energy_kJ_per_mol`, `rate_constant`
    - `properties`:
      - `MOF`:
        - `type`: string
      - `barrier_kJ_per_mol`:
        - `type`: float
        - `unit`: kJ mol⁻¹
      - `reaction_energy_kJ_per_mol`:
        - `type`: float
        - `unit`: kJ mol⁻¹
      - `rate_constant`:
        - `type`: float

Notes: The rate constant is computed from free energy barriers at 298 K using an Eyring-type expression (eq 3 in the method). The reported barrier and reaction energy are 0 K values from DFT total energies. The agent must ensure vibrational calculations confirm stationary points (no imaginary frequencies for IS/FS, one imaginary frequency for TS).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_05_rate_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "MOF",
            "barrier_kJ_per_mol",
            "reaction_energy_kJ_per_mol",
            "rate_constant"
          ],
          "properties": {
            "MOF": {
              "type": "string"
            },
            "barrier_kJ_per_mol": {
              "type": "float",
              "unit": "kJ mol⁻¹"
            },
            "reaction_energy_kJ_per_mol": {
              "type": "float",
              "unit": "kJ mol⁻¹"
            },
            "rate_constant": {
              "type": "float"
            }
          }
        }
      },
      "description": "Rate constants k (at 298 K), energy barriers ΔE‡, and reaction energies ΔE for the first-step H₂S degradation mechanism for MIL-53(Al)-BDC, -FA, and -TDC. The checker verifies the relative ordering of k and barrier values against expected physical trends."
    }
  ],
  "notes": "The rate constant is computed from free energy barriers at 298 K using an Eyring-type expression (eq 3 in the method). The reported barrier and reaction energy are 0 K values from DFT total energies. The agent must ensure vibrational calculations confirm stationary points (no imaginary frequencies for IS/FS, one imaginary frequency for TS)."
}
```

## How you are scored
A hidden verifier reads your step_05_rate_constants.json and checks whether the reported barrier, reaction energy, and rate constant values are internally consistent and physically plausible. The main scoring criterion is that the relative ordering of the rate constants k across the three MOFs matches the expected stability trend: one MOF must be clearly more stable (k more negative by at least an order of magnitude compared to the others) and the other two must have k values within an order of magnitude of each other. Additionally, the energy barrier for that more stable MOF should be noticeably lower than for the others. Tolerances allow for differences between DFT implementations, so your values do not need to match a fixed reference number; rather, the qualitative trend and reasonable magnitudes are key. The verifier combines these checks into a final reward. Note that simply quoting a known value without running the workflow will not produce a consistent set of energies and barriers that satisfy the physical trend simultaneously, so the reliable path to a good score is to execute the full protocol.
