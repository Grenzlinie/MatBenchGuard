# DFT and NEGF Study of Edge-Passivated Armchair Graphene Nanoribbons

## Problem background
Armchair graphene nanoribbons (AGNRs) are promising materials for nanoscale interconnects, but when passivated with hydrogen they exhibit a bandgap that makes them semiconducting rather than metallic. Finding an edge passivation that induces metallic behavior is critical. This study explores the use of osmium (Os) edge passivation: can replacing hydrogen with osmium turn AGNRs into metallic conductors? Using first-principles electronic structure and transport calculations, we investigate the bandgap and conduction properties of H-passivated and Os-passivated AGNRs of width N=7.

## Approach
We use density functional theory (DFT) with the generalized gradient approximation (GGA-PBE) and a double-zeta polarized basis set, as implemented in the open-source SIESTA code, along with its TranSIESTA/TBtrans modules for non-equilibrium Green's function (NEGF) transport. The workflow: (1) Build supercells for three edge configurations: hydrogen on both edges, osmium on one edge (hydrogen on the other), and osmium on both edges, with vacuum padding. (2) Relax atomic positions via DFT. (3) Compute electronic band structures and density of states to determine bandgaps and metallicity. (4) For the both-edge Os-passivated case, set up a two-probe transport model and compute the energy-resolved transmission spectrum at zero bias. (5) Extract key quantities: the bandgap of H-passivated AGNR, whether the Os-passivated configurations are metallic (gap < 0.1 eV), and the number of conduction channels at the Fermi level from the transmission spectrum.

## Reproduction target
Your task is to compute and report the following: (a) the bandgap in eV of the H-passivated AGNR, (b) whether the one-edge Os-passivated and both-edge Os-passivated AGNRs are metallic (bandgap < 0.1 eV), and (c) the number of conduction channels (transmission at energy = 0 eV) for the both-edge Os-passivated AGNR. Write the final aggregated results to `/app/outputs/results.json` with keys: `H_passivated_bandgap_eV` (float), `one_edge_Os_metallic` (boolean), `both_edge_Os_metallic` (boolean), `both_edge_Os_conduction_channels` (int). Additionally, save the raw transmission data for the both-edge Os-passivated case to `/app/outputs/transmission_both_edge_Os.csv` with columns `energy_eV` and `transmission`.

## Assets

- SIESTA (with TranSIESTA/TBtrans for transport): https://siesta-project.org/siesta/
- PBE pseudopotentials for C, H, Os: https://pseudo-dojo.org

## Workflow steps

### Step 1: Geometry optimization of GNR supercells
- Role: process
- Action: Build atomic structures for armchair GNR width N=7 with three edge passivation configurations: H on both edges, Os on one edge (H on the other), Os on both edges. Include 10 Å vacuum in X and Y. Perform DFT geometry relaxation using GGA-PBE, DZP basis, 150 Ry mesh cutoff, 1x1x100 k-points.
- Evidence: `/app/outputs/geom_optimization.log`

### Step 2: DFT electronic structure calculation
- Role: process
- Action: Using the optimized geometries, compute the electronic band structure and density of states (DOS) with the same DFT parameters. Identify the bandgap and metallic/semiconducting nature.
- Evidence: `/app/outputs/bands_dos.out`

### Step 3: NEGF transport calculation for both-edge Os-passivated AGNR
- Role: scored
- Action: Set up a two-probe transport model for the both-edge Os-passivated AGNR. Compute the energy-resolved transmission spectrum from -1 eV to +1 eV relative to Fermi level using NEGF (TranSIESTA/TBtrans) at zero bias. Save to transmission_both_edge_Os.csv.
- Output file: `/app/outputs/transmission_both_edge_Os.csv`
- Format: csv
- Contract: CSV with columns 'energy_eV' (float, energy relative to Fermi level) and 'transmission' (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Compile scored electronic and transport properties
- Role: scored (load-bearing)
- Action: From the DFT band structure, determine the bandgap of H-passivated AGNR (eV) and whether one-edge and both-edge Os-passivated configurations are metallic (bandgap < 0.1 eV). From the transmission CSV, extract the number of conduction channels as the transmission value at energy = 0 eV. Write these results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'H_passivated_bandgap_eV' (float), 'one_edge_Os_metallic' (boolean), 'both_edge_Os_metallic' (boolean), 'both_edge_Os_conduction_channels' (int).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transmission_both_edge_Os.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transmission_both_edge_Os.csv
- path: `/app/outputs/transmission_both_edge_Os.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Energy-resolved transmission for both-edge Os-passivated AGNR over [-1,1] eV. The checker recomputes the conduction channel count from the transmission at E=0 eV.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `transmission`
  - `units`:
    - `energy_eV`: eV
    - `transmission`: dimensionless

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bandgap and metallicity for H-passivated and Os-passivated AGNRs, and conduction channel count for both-edge Os-passivated AGNR. Compared to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `H_passivated_bandgap_eV`: float
    - `one_edge_Os_metallic`: boolean
    - `both_edge_Os_metallic`: boolean
    - `both_edge_Os_conduction_channels`: int
  - `units`:
    - `H_passivated_bandgap_eV`: eV

Notes: The transmission CSV and results.json must be produced in order. Bandgap and conduction channel values are verified against paper-reported results with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transmission_both_edge_Os.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "transmission"
        ],
        "units": {
          "energy_eV": "eV",
          "transmission": "dimensionless"
        }
      },
      "description": "Energy-resolved transmission for both-edge Os-passivated AGNR over [-1,1] eV. The checker recomputes the conduction channel count from the transmission at E=0 eV."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "H_passivated_bandgap_eV": "float",
          "one_edge_Os_metallic": "boolean",
          "both_edge_Os_metallic": "boolean",
          "both_edge_Os_conduction_channels": "int"
        },
        "units": {
          "H_passivated_bandgap_eV": "eV"
        }
      },
      "description": "Bandgap and metallicity for H-passivated and Os-passivated AGNRs, and conduction channel count for both-edge Os-passivated AGNR. Compared to hidden reference values."
    }
  ],
  "notes": "The transmission CSV and results.json must be produced in order. Bandgap and conduction channel values are verified against paper-reported results with appropriate tolerances."
}
```

## How you are scored
A hidden verifier will independently assess your output artifacts. For `results.json`, it checks the bandgap and metallicity labels against a hidden reference derived from the paper's reported values (with appropriate tolerances to account for differences in computational toolchains). For `transmission_both_edge_Os.csv`, the verifier reads the transmission value nearest to E=0 eV and compares the conduction channel count against an expected range. The overall reward is a weighted combination of these checks, with the bandgap and metallicity accuracy receiving higher weight. Merely reporting the paper's numbers without genuine computation will not pass the structural checks; the raw transmission data must be self-consistent.
