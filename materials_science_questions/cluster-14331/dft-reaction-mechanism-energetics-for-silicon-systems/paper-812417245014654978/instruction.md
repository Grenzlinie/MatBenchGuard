# ICN Adsorption and Decomposition on Si(100) Model Clusters

## Problem background
ICN adsorption on Si(100)-(2×1) surfaces is relevant for understanding the surface reactivity of cyanogen halides in semiconductor processing. The adsorption and decomposition pathways determine how the molecule interacts with the silicon dangling bonds, whether the CN triple bond remains intact, and how the resulting fragments are bound to the surface. This task computationally maps the potential energy surface (PES) of ICN on a model silicon cluster, identifying the relative stabilities of molecularly adsorbed and dissociated structures, the transition states connecting them, and the energy barrier for isomerization between the SiNC and SiCN configurations.

## Approach
Density functional theory (DFT) at the B3LYP/LanL2DZ+6-31G* level is used with the open-source ORCA package. The Si(100)-(2×1) surface is represented by a Si9H12 single-dimer cluster. Geometries of the key adsorption structures are fully optimised: end-on ICN1, side-on ICN2, dissociated SiNC and SiCN, and the INC-derived structures INC1 (with a collinear bond-angle constraint) and INC2. For each minimum, a frequency calculation confirms the absence of imaginary modes. Transition states (TS1–TS5) linking the minima are located using ORCA's transition-state search methods, and each is verified to have exactly one imaginary frequency. An additional transition-state search between ICN2 and INC2 is attempted. The total energy of gas-phase ICN is also computed at the same level. All stationary-point energies are referenced to the sum of the isolated Si9H12 cluster and gas-phase ICN to obtain relative energies in kJ/mol. The isomerization barrier between SiNC and SiCN is taken as the energy difference between TS4 and SiNC. The stability of the INC1 structure is assessed by re-optimising without the angle constraint; if the resulting IN bond length exceeds 3.0 Å or the structure dissociates, INC1 is considered unstable. The outcome of the TS search between ICN2 and INC2 is recorded as a Boolean.

## Reproduction target
Compute the relative energies (in kJ/mol) of the stationary points ICN1, ICN2, SiNC, SiCN, TS1, TS2, TS3, TS4, and TS5 with respect to the separated Si9H12 cluster and gas-phase ICN. From these values, calculate the isomerization barrier as E(TS4) − E(SiNC). Determine whether the INC1 structure, when optimised without the bond-angle constraint, retains an IN bond length below 3.0 Å (INC1_stable = true) or not (false). Determine whether a transition state between ICN2 and INC2 (TS6) could be located (TS6_found = true) or not (false). Output all results in /app/outputs/energies.json.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- LanL2DZ basis set and ECP for iodine: ORCA
- 6-31G* basis set for Si, C, N, H: ORCA
- Si9H12 single-dimer cluster geometry

## Workflow steps

### Step 1: Geometry optimization of adsorption minima
- Role: process
- Action: Using ORCA at B3LYP/LanL2DZ+6-31G* level, fully optimise the geometries of ICN1, ICN2, SiNC, SiCN, INC1 (constrained) and INC2 on the Si9H12 single-dimer cluster. Perform frequency calculations to confirm local minima (no imaginary frequencies).
- Evidence: `/app/outputs/minima_optimization.log`

### Step 2: Transition state search
- Role: process
- Action: Optimise transition states TS1–TS5 connecting the relevant minima using ORCA's TS search methods. Perform frequency calculations to confirm one imaginary frequency each. Attempt a transition state search between ICN2 and INC2; record if no stationary point is found.
- Evidence: `/app/outputs/ts_search.log`

### Step 3: Compute relative energies and qualitative analysis
- Role: scored (load-bearing)
- Action: Extract total energies from all stationary-point calculations and from a separate gas-phase ICN optimisation at the same level. Compute relative energies (kJ/mol) of ICN1, ICN2, SiNC, SiCN, TS1–TS5 with respect to separated Si9H12 cluster + gas-phase ICN. Calculate the isomerization barrier as E(TS4) - E(SiNC). Determine INC1 stability: if the optimised structure without angle constraint has an IN bond length > 3.0 Å or dissociates, set INC1_stable=false; otherwise true. Set TS6_found=false if no TS was located between ICN2 and INC2. Write all values to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: {"ICN1": number, "ICN2": number, "SiNC": number, "SiCN": number, "TS1": number, "TS2": number, "TS3": number, "TS4": number, "TS5": number, "isomerization_barrier": number, "INC1_stable": boolean, "TS6_found": boolean}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed relative energies (kJ/mol) of all stationary points on the single-dimer PES and the isomerisation barrier, together with the stability flag for INC1 and whether a transition state between ICN2 and INC2 was found.
- schema:
  - `type`: object
  - `required`: `ICN1`, `ICN2`, `SiNC`, `SiCN`, `TS1`, `TS2`, `TS3`, `TS4`, `TS5`, `isomerization_barrier`, `INC1_stable`, `TS6_found`
  - `properties`:
    - `ICN1`:
      - `type`: number
      - `unit`: kJ/mol
    - `ICN2`:
      - `type`: number
      - `unit`: kJ/mol
    - `SiNC`:
      - `type`: number
      - `unit`: kJ/mol
    - `SiCN`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS1`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS2`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS3`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS4`:
      - `type`: number
      - `unit`: kJ/mol
    - `TS5`:
      - `type`: number
      - `unit`: kJ/mol
    - `isomerization_barrier`:
      - `type`: number
      - `unit`: kJ/mol
    - `INC1_stable`:
      - `type`: boolean
    - `TS6_found`:
      - `type`: boolean

Notes: All energies are relative to separated Si9H12 cluster + gas-phase ICN. The agent must construct the cluster geometry, run the DFT calculations, and extract the energies. Tolerances for scoring are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "ICN1",
          "ICN2",
          "SiNC",
          "SiCN",
          "TS1",
          "TS2",
          "TS3",
          "TS4",
          "TS5",
          "isomerization_barrier",
          "INC1_stable",
          "TS6_found"
        ],
        "properties": {
          "ICN1": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "ICN2": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "SiNC": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "SiCN": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS1": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS2": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS3": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS4": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "TS5": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "isomerization_barrier": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "INC1_stable": {
            "type": "boolean"
          },
          "TS6_found": {
            "type": "boolean"
          }
        }
      },
      "description": "Computed relative energies (kJ/mol) of all stationary points on the single-dimer PES and the isomerisation barrier, together with the stability flag for INC1 and whether a transition state between ICN2 and INC2 was found."
    }
  ],
  "notes": "All energies are relative to separated Si9H12 cluster + gas-phase ICN. The agent must construct the cluster geometry, run the DFT calculations, and extract the energies. Tolerances for scoring are hidden."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted energies.json. It compares each reported numeric energy against a hidden reference value derived from the paper's original calculations at the same level of theory, allowing for a small tolerance that accounts for differences between ORCA and the original quantum chemistry code. The isomerization barrier is recomputed from your TS4 and SiNC values and compared to the expected barrier. The Boolean flags (INC1_stable and TS6_found) are checked against the qualitative findings. Your final score is the weighted sum of correctly matched entries, where numeric and Boolean items each contribute a defined share. Reporting numbers that match the paper without actually running the required DFT calculations is unlikely to succeed, because the tolerance is tight enough to exclude generic guesses but wide enough to allow a correct re-run with ORCA. No further manual review is performed.
