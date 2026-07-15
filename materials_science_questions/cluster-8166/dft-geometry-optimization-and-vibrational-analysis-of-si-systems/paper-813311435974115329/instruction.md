# Electronic Structure Analysis of Si(111)-7×7 Adatoms via DFT

## Problem background
The Si(111)-7×7 reconstructed surface is metallic despite bulk Si being a semiconductor. The surface adopts the dimer-adatom stacking-fault (DAS) structure, containing four inequivalent types of adatoms that give rise to distinct dangling-bond states. Scanning tunneling microscopy (STM) experiments observe that the apparent brightness of these adatoms depends on the doping type of the Si sample: the order of prominence changes between p-type, intrinsic, and n-type samples. This task reproduces the first-principles explanation: density functional theory (DFT) calculations of the projected density of states (PDOS) of the four adatom types, integrated over energy windows that emulate different doping conditions, reveal how the electronic structure dictates the doping-dependent STM contrast.

## Approach
The approach employs DFT with the Perdew-Burke-Ernzerhof generalized gradient approximation (PBE-GGA) functional and projector-augmented-wave (PAW) pseudopotentials. A six-layer Si(111) slab with a 7×7 supercell is constructed using the known DAS atomic coordinates, with the bottom surface passivated by hydrogen and the bottom two Si bilayers frozen in bulk-like positions. After geometry relaxation, a non-self-consistent density-of-states calculation is performed to obtain the PDOS projected onto the four inequivalent adatom types: corner-fault (CoF), centre-fault (CeF), corner-unfault (CoU), and centre-unfault (CeU). The PDOS curves are then numerically integrated over three energy windows relative to the Fermi level that correspond to p-type doping ([-0.6, -0.1] eV), intrinsic doping ([-0.5, 0.0] eV), and n-type doping ([-0.4, 0.1] eV). The integrated PDOS values for each adatom and window are used to infer the adatom brightness ordering, which can be compared with experimental STM observations.

## Reproduction target
The reproduction target is to compute the PDOS of the four inequivalent adatom types on Si(111)-7×7 via DFT, integrate the PDOS over the specified doping energy windows, and determine the ordering of the integrated values for p-type, intrinsic, and n-type conditions. The raw PDOS data and the integrated values must be written to the required output files. The verifier will check that the ordering of the integrated PDOS correctly reflects the experimentally observed doping-dependent adatom contrast reversal.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO or GPAW): https://www.quantum-espresso.org/ or https://wiki.fysik.dtu.dk/gpaw/
- PBE-GGA PAW pseudopotentials for Si and H: Standard SSSP library for Quantum ESPRESSO or GPAW setups
- si111_7x7_coords.xyz

## Workflow steps

### Step 1: Build Si(111)-7×7 DAS slab model
- Role: process
- Action: Construct a 6-layer Si(111) slab with a 7×7 supercell according to the dimer-adatom-stacking-fault (DAS) model using the provided si111_7x7_coords.xyz coordinates. The slab contains adatoms, rest atoms, dimers, corner holes, and bottom hydrogen passivation. The bottom two silicon bilayers are frozen in bulk-like positions.
- Evidence: `/app/outputs/slab_structure.log`

### Step 2: Geometry optimization of the slab
- Role: process
- Action: Perform a DFT geometry relaxation using the PBE-GGA functional with the slab model. Relax all atoms except the bottom two bilayers (and attached H atoms) until forces are below a tight threshold. Output the relaxed atomic positions.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 3: Calculate projected density of states (PDOS)
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, perform a non-self-consistent DOS calculation with a dense k-point mesh. Extract the PDOS projected onto the four inequivalent adatom types: corner-fault (CoF), centre-fault (CeF), corner-unfault (CoU), and centre-unfault (CeU). For each energy bin relative to the Fermi level (E_F=0), output the PDOS values.
- Output file: `/app/outputs/raw_pdos.csv`
- Format: csv
- Contract: Energy_eV (float), PDOS_CoF (float), PDOS_CeF (float), PDOS_CoU (float), PDOS_CeU (float)
- Scoring: scored by hidden verifier

### Step 4: Integrate PDOS over doping windows
- Role: scored
- Action: From the raw PDOS data, numerically integrate the PDOS over the following energy windows: p-type [-0.6, -0.1] eV; intrinsic [-0.5, 0.0] eV; n-type [-0.4, 0.1] eV. Report the integrated values for each adatom type.
- Output file: `/app/outputs/integrated_pdos.csv`
- Format: csv
- Contract: adatom (string: CoF, CeF, CoU, CeU), window (string: p-type, intrinsic, n-type), integrated_pdos (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raw_pdos.csv`
- `/app/outputs/integrated_pdos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raw_pdos.csv
- path: `/app/outputs/raw_pdos.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw projected density of states for the four inequivalent adatoms on Si(111)-7×7. The checker integrates these curves over specified doping windows and checks the ordering of the integrated values.
- schema:
  - `type`: table
  - `required_columns`: `Energy_eV`, `PDOS_CoF`, `PDOS_CeF`, `PDOS_CoU`, `PDOS_CeU`
  - `units`:
    - `Energy_eV`: eV
    - `PDOS_CoF`: arbitrary
    - `PDOS_CeF`: arbitrary
    - `PDOS_CoU`: arbitrary
    - `PDOS_CeU`: arbitrary

### integrated_pdos.csv
- path: `/app/outputs/integrated_pdos.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-reported integrated PDOS for each adatom type and doping window. The checker cross-checks these against the values recomputed from raw_pdos.csv.
- schema:
  - `type`: table
  - `required_columns`: `adatom`, `window`, `integrated_pdos`
  - `units`:
    - `integrated_pdos`: arbitrary

Notes: The primary scoring is based on the correct ordering of integrated PDOS values recomputed from raw_pdos.csv for the three doping windows. The agent-reported integrated_pdos.csv serves as a consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raw_pdos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Energy_eV",
          "PDOS_CoF",
          "PDOS_CeF",
          "PDOS_CoU",
          "PDOS_CeU"
        ],
        "units": {
          "Energy_eV": "eV",
          "PDOS_CoF": "arbitrary",
          "PDOS_CeF": "arbitrary",
          "PDOS_CoU": "arbitrary",
          "PDOS_CeU": "arbitrary"
        }
      },
      "description": "Raw projected density of states for the four inequivalent adatoms on Si(111)-7×7. The checker integrates these curves over specified doping windows and checks the ordering of the integrated values."
    },
    {
      "file": "integrated_pdos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "adatom",
          "window",
          "integrated_pdos"
        ],
        "units": {
          "integrated_pdos": "arbitrary"
        }
      },
      "description": "Agent-reported integrated PDOS for each adatom type and doping window. The checker cross-checks these against the values recomputed from raw_pdos.csv."
    }
  ],
  "notes": "The primary scoring is based on the correct ordering of integrated PDOS values recomputed from raw_pdos.csv for the three doping windows. The agent-reported integrated_pdos.csv serves as a consistency check."
}
```

## How you are scored
A hidden verifier independently assesses your outputs. For the raw PDOS data, the verifier recomputes the integrated PDOS for each adatom and doping window and then checks the ordering among the adatoms. The primary score is derived from the correctness of these orderings. Additionally, the verifier compares your self-reported integrated_pdos.csv with the values recomputed from raw_pdos.csv to ensure consistency. The final reward is a weighted combination of these checks. Simply reporting numbers that happen to satisfy the ordering without correctly performing the DFT workflow will not pass verification.
