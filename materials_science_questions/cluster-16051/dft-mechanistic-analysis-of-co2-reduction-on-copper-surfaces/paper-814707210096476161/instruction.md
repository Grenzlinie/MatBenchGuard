# Activation barriers of CO insertion on CuY zeolite catalysts with different local cation environments

## Problem background
The CuY zeolite is a promising chloride-free catalyst for dimethyl carbonate (DMC) synthesis via oxidative carbonylation of methanol. The catalytic cycle runs on Cu⁺ cations that occupy exchange sites within the zeolite framework. In the working catalyst, Cu⁺ and other co-cations populate nearby framework sites, creating different local electrostatic and steric environments around the active Cu⁺ centre. The rate-limiting step of the catalytic cycle is the insertion of co‑adsorbed CO into a surface methoxide (CH₃O) to form an adsorbed CH₃OCO intermediate. The activation barrier for this CO-insertion step is taken as the measure of catalytic activity. Understanding how the identity and location of neighbouring cations affect this barrier is essential for rational catalyst design. This task investigates four CuY zeolite models with different local cation environments around the active Cu⁺ site in the supercage.

## Approach
The calculation uses density functional theory (DFT) at the GGA-PBE level with an open‑source DFT code (e.g., Quantum ESPRESSO, CP2K, ORCA) that replaces the proprietary DMol³. A 31‑tetrahedral‑atom (31T) cluster is cut from the FAU framework; it contains a sodalite cage and a hexagonal prism. Five silicon atoms are substituted by aluminium according to a published Al distribution, giving a Si/Al ratio of 5.3. Charge‑compensating protons are placed at O1 and O3 framework oxygen sites. The active Cu⁺ is placed at site II (inside the supercage, near a six‑membered ring). Four catalyst models are built by populating neighbouring cation sites differently:

- **CuIIY**: the active Cu⁺ at site II only.
- **CuIICuIIaY**: a second Cu⁺ placed at an adjacent supercage site IIa.
- **CuIICuI′aY**: a second Cu⁺ placed in a nearby sodalite‑cage site I′a.
- **CuIICsIIa*Y**: a Cs⁺ cation placed at an adjacent supercage site IIa*.

For each model the bare cluster geometry is first optimised. Then CO (carbon‑bound) and CH₃O (oxygen‑bound) are co‑adsorbed on the active Cu⁺, and the co‑adsorbed state is optimised. Finally the transition state (TS) for CO insertion (CH₃O + CO → CH₃OCO) is located using a combined LST/QST method or an equivalent transition‑state search. The activation barrier is computed as the total‑energy difference between the TS and the co‑adsorbed initial state. The four barriers are collected into a single CSV file, and the computed barriers and their relative ordering across the four conditions constitute the main result.

## Reproduction target
Produce the activation barriers (in kJ/mol) for the CO‑insertion step on the four CuY zeolite models listed above. Write the results to `/app/outputs/activation_barriers.csv`, a comma‑separated file with two columns: `catalyst` (one of CuIIY, CuIICuIIaY, CuIICuI′aY, CuIICsIIa*Y) and `barrier_kJ_mol` (the computed barrier as a floating‑point number). The four barriers must be obtained from a consistent DFT protocol at the GGA‑PBE level on the prescribed cluster models; the barriers and their relative ordering across the four conditions will be evaluated.

## Assets

- FAU zeolite framework structure: http://www.iza-structure.org/databases/
- Al distribution in CuY zeolite cluster (Ref. [16]): 10.1039/c3ra41475f
- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, ORCA): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Construct and optimize catalyst cluster models
- Role: process
- Action: Build the 31T FAU cluster containing a sodalite cage and a hexagonal prism. Replace five Si by Al according to the Al distribution in Ref. [16] (DOI:10.1039/c3ra41475f), achieving Si/Al=5.3. Add charge-compensating protons at O1 and O3 sites. Place Cu⁺ at site II near Al2 as the active center. Construct the four models: CuIIY, CuIICuIIaY, CuIICuI′aY, CuIICsIIa*Y by placing additional Cu⁺ or Cs⁺ at sites IIa, I′a, IIa*. Optimize the geometry of each bare cluster using DFT at the GGA-PBE level.
- Evidence: none

### Step 2: Optimize co-adsorbed CO/CH₃O initial states
- Role: process
- Action: For each optimized catalyst model, co-adsorb CO (C‑bound) and CH₃O (O‑bound) on the active Cu⁺ cation. Optimize the geometry to obtain the initial co‑adsorbed state (CO+CH₃O/CuY) for the CO insertion reaction.
- Evidence: none

### Step 3: Transition state search and activation barrier calculation
- Role: scored (load-bearing)
- Action: For each catalyst, locate the transition state (TS) for CO insertion (CH₃O + CO → CH₃OCO) using LST/QST or an equivalent method. Compute the activation barrier as Eᵃ = E_TS − E_coads (total energies of the transition state and co‑adsorbed initial state). Write the four barriers to activation_barriers.csv.
- Output file: `/app/outputs/activation_barriers.csv`
- Format: csv
- Contract: catalyst (string, one of CuIIY, CuIICuIIaY, CuIICuI′aY, CuIICsIIa*Y), barrier_kJ_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_barriers.csv
- path: `/app/outputs/activation_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation barriers for CO insertion into methoxide on the four CuY zeolite catalyst models. The hidden checker compares each barrier and the overall ordering to the paper-reported reference values.
- schema:
  - `type`: table
  - `required_columns`: `catalyst`, `barrier_kJ_mol`
  - `column_types`:
    - `catalyst`: string
    - `barrier_kJ_mol`: float
  - `units`:
    - `barrier_kJ_mol`: kJ/mol

Notes: The four catalyst identifiers must be exactly CuIIY, CuIICuIIaY, CuIICuI'aY, CuIICsIIa*Y. The barrier should be in kJ/mol.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "catalyst",
          "barrier_kJ_mol"
        ],
        "column_types": {
          "catalyst": "string",
          "barrier_kJ_mol": "float"
        },
        "units": {
          "barrier_kJ_mol": "kJ/mol"
        }
      },
      "description": "Activation barriers for CO insertion into methoxide on the four CuY zeolite catalyst models. The hidden checker compares each barrier and the overall ordering to the paper-reported reference values."
    }
  ],
  "notes": "The four catalyst identifiers must be exactly CuIIY, CuIICuIIaY, CuIICuI'aY, CuIICsIIa*Y. The barrier should be in kJ/mol."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/activation_barriers.csv` and compares the four reported barriers against reference values derived from the same protocol. Scoring rewards two properties: (1) the absolute value of each barrier relative to the reference (within an appropriate tolerance that accounts for legitimate toolchain spread between DFT implementations), and (2) the overall ordering of the four barriers across the catalyst models. A correct ordering carries the larger share of the weight; numerical closeness to the reference carries the remaining share. Reporting plausible numbers without genuine computation will score poorly because the tolerance window and the required ordering both come from the protocol — the verifier does not reward matching a published table without running the workflow. Only the correct CSV file at the correct path is scored.
