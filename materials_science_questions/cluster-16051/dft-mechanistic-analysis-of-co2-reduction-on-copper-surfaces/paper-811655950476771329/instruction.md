# DFT Activation Barriers for Key Elementary Steps in CO2 Hydrogenation on Cu(111)

## Problem background
Methanol synthesis from CO₂ hydrogenation on Cu-based catalysts is an important industrial and environmental process, but the reaction mechanism remains debated. The commonly assumed formate route faces kinetic obstacles, while a hydrocarboxyl route, potentially assisted by trace amounts of water, has been proposed as an alternative. Distinguishing these pathways requires accurate activation barriers for the key elementary steps that differentiate the two mechanisms. This task focuses on computing the energy barriers for three such steps on the Cu(111) surface using periodic density functional theory.

## Approach
We use periodic plane-wave density functional theory with the PW91 exchange-correlation functional to model a Cu(111) slab (three atomic layers, (2×3) surface unit cell, 12 Å vacuum). The computational workflow builds the slab model, optimizes the co-adsorbed initial states for three reactions, locates the transition states via a saddle-point search (dimer method or climbing-image nudged elastic band), and computes zero-point-energy-corrected forward activation barriers from vibrational frequency analysis. The three reactions are: (1) CO₂(g) + H → mono-HCOO (Eley-Rideal path to formate), (2) physisorbed CO₂ + H → trans-COOH (Langmuir-Hinshelwood path to hydrocarboxyl), and (3) CO₂ + H₂O + H → trans-COOH (water-assisted hydrogen transfer to hydrocarboxyl). The computed barriers are compared to each other to infer which route is kinetically preferred.

## Reproduction target
Compute and report the zero-point-energy-corrected forward activation barriers (E_a^ZPEC) for the three elementary steps specified in the workflow. The barriers must be obtained from a consistent DFT protocol using the PW91 functional, the Cu(111) slab model described in Step 1, and must include ZPE corrections derived from vibrational frequencies of the initial and transition states. The results should be written to key_barriers.json in electron‑volts (eV).

## Assets

- Quantum ESPRESSO (open-source DFT code, version >=6.8): https://www.quantum-espresso.org/
- SSSP efficiency PAW pseudopotentials (version 1.3): https://www.materialscloud.org/discover/sssp/table/efficiency
- Bulk Cu fcc crystal structure

## Workflow steps

### Step 1: Build and converge Cu(111) slab model
- Role: process
- Action: Construct a Cu(111) slab model: 3 atomic layers, (2×3) surface unit cell, 12 Å vacuum gap, bottom two layers fixed at bulk positions. Use the PW91 exchange-correlation functional and PAW pseudopotentials. Perform convergence tests to ensure relative energies are converged to within 0.05 eV.
- Evidence: `/app/outputs/slab.log`

### Step 2: Optimize initial reactant configurations
- Role: process
- Action: For each of the three target reactions, build and optimize the co-adsorbed initial state on the Cu(111) slab: (a) gas‑phase CO2 approaching a surface H (ER path for mono-HCOO); (b) physisorbed CO2 co‑adsorbed with an atomic H (LH path for trans-COOH); (c) CO2, H, and H2O co‑adsorbed (water‑assisted trans-COOH). Relax all free atoms until forces are <0.02 eV/Å. Keep only the lowest‑energy configuration for each system.
- Evidence: `/app/outputs/initial_geometries.json`

### Step 3: Saddle-point search, ZPE correction, and output activation barriers
- Role: scored (load-bearing)
- Action: For each of the three reactions, locate the transition state using a saddle-point search method (the dimer method or climbing‑image NEB). Confirm the TS by a vibrational frequency analysis showing exactly one imaginary frequency. Perform a vibrational frequency calculation for the initial state to obtain zero‑point energies. Compute the ZPE‑corrected forward activation barrier E_a^ZPEC = (E_TS + ZPE_TS) - (E_IS + ZPE_IS). Write the three barriers (in eV) to /app/outputs/key_barriers.json with keys: CO2_to_trans_COOH_LH, CO2_to_mono_HCOO, CO2_plus_H2O_to_trans_COOH.
- Output file: `/app/outputs/key_barriers.json`
- Format: json
- Contract: {"CO2_to_trans_COOH_LH": "number (eV)", "CO2_to_mono_HCOO": "number (eV)", "CO2_plus_H2O_to_trans_COOH": "number (eV)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/key_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### key_barriers.json
- path: `/app/outputs/key_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: ZPE-corrected activation barriers for three elementary steps that distinguish the formate and hydrocarboxyl mechanisms.
- schema:
  - `type`: object
  - `required`:
    - `CO2_to_trans_COOH_LH`: number (eV)
    - `CO2_to_mono_HCOO`: number (eV)
    - `CO2_plus_H2O_to_trans_COOH`: number (eV)

Notes: The three barriers are compared to paper-reported values within a 0.1 eV tolerance. The full 46-step network is not required; only these three barriers are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "key_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CO2_to_trans_COOH_LH": "number (eV)",
          "CO2_to_mono_HCOO": "number (eV)",
          "CO2_plus_H2O_to_trans_COOH": "number (eV)"
        }
      },
      "description": "ZPE-corrected activation barriers for three elementary steps that distinguish the formate and hydrocarboxyl mechanisms."
    }
  ],
  "notes": "The three barriers are compared to paper-reported values within a 0.1 eV tolerance. The full 46-step network is not required; only these three barriers are scored."
}
```

## How you are scored
A hidden verifier independently evaluates the artifacts you produce in each workflow stage. The primary reward comes from the key_barriers.json file; the verifier compares each reported activation barrier against a predetermined reference value. Additional process evidence contributes minor weight, ensuring the full pipeline was executed. The total reward is capped at 1.0. Simply writing paper‑reported numbers is not sufficient — the verifier checks that your barriers are physically reasonable and follow from the required computational procedure.
