# Tight-binding simulation of stacking fault energies and atom relaxation for fcc Pd and Pt

## Problem background
Quantifying the generalized stacking fault (GSF) energy and the associated atomic-scale relaxation is crucial for understanding the mechanical properties of metals. The GSF energy curve characterizes the energetic cost of shearing one half of a crystal relative to the other, and the stacking fault energy (SFE) governs dislocation behavior. The effect of atom relaxation on the SFE and on the interlayer spacings near the fault plane is not fully understood; in particular, it is unclear whether relaxation significantly changes the SFE and whether its impact differs between metals. This task investigates these questions for the fcc metals Pd and Pt using a parameterized tight-binding total-energy method and simulated annealing relaxation.

## Approach
We implement a nonorthogonal two-center Slater-Koster tight-binding model to compute total energies. The parameters are taken from a public database. For each metal, we construct a 12-layer supercell containing a (11-1) slip plane. The stacking fault is introduced by a variable displacement q along the <11-2> direction, producing a series of geometries with q ranging from 0 (perfect fcc) to 1 (a full stacking fault, yielding a local hcp arrangement). The primitive vectors of the supercell are functions of the experimental lattice constant a0 and q, producing a periodic slab with one atom per (11-1) plane. We compute unrelaxed total energies using dense k-point sampling and Fermi smearing. Then, for each supercell, we relax the six layers nearest the boundary plane along the <11-1> direction using simulated annealing, yielding relaxed total energies and atomic positions. From these runs we extract (i) the GSF energy per unit area as a function of q, both unrelaxed and relaxed; (ii) the first, second, and third interlayer spacings near the boundary plane; and (iii) key quantities at q=1: the SFE, the unstable SFE (the maximum energy along the relaxed curve), and the c/a ratio of the local hcp-like environment.

## Reproduction target
Produce three CSV files under /app/outputs that report the computed results for both Pd and Pt: 
- gsf_energy.csv: the relaxed and unrelaxed GSF energy per unit area (mJ/m²) for each q (from 0 to 1 in steps of at most 0.1). 
- interlayer_spacings.csv: the first, second, and third interlayer spacings (Å) for each q, both relaxed and unrelaxed. 
- summary.csv: the SFE (energy at q=1), unstable SFE (maximum relaxed energy), and c/a ratio at q=1 for each metal. 
All values must be computed from scratch using the tight-binding total energy calculations; re-implement the tight-binding solver or use an open-source equivalent (the original Mehl TB code is proprietary).

## Assets

- Tight-binding parameters for Pd and Pt (NRL tight-binding database): http://cst-www.nrl.navy.mil/bind/
- Experimental lattice constants for fcc Pd and Pt

## Workflow steps

### Step 1: Generate supercell geometries
- Role: process
- Action: Construct 12-layer supercell models of the (11-1) slip plane for fcc Pd and Pt for stacking fault variable q from 0.0 to 1.0 in steps of at most 0.1. Use the experimental lattice constants and the primitive vectors defined as: a1 = (a0/2) y + (a0/2) z, a2 = (a0/2) x + (a0/2) z, a3 = (4 + q/6) a0 x + (4 + q/6) a0 y - (4 - q/3) a0 z. This produces a periodic slab with one atom per (11-1) plane and a boundary plane.
- Evidence: none

### Step 2: Compute unrelaxed total energies
- Role: process
- Action: Using an open-source implementation of nonorthogonal two-center Slater-Koster tight-binding, compute the total energy for each supercell geometry without atom relaxation. Use a dense Brillouin-zone integration and Fermi smearing (extrapolated to zero). Derive the unrelaxed generalized stacking fault energy per unit area for each q.
- Evidence: none

### Step 3: Relax atoms via simulated annealing
- Role: process
- Action: For each supercell, relax the positions of the six atomic layers nearest the boundary plane along the <11-1> direction using simulated annealing (exploring local minima in atom coordinates). Compute relaxed total energies and final atomic coordinates.
- Evidence: `/app/outputs/relaxation_energies.json`

### Step 4: Assemble GSF energies
- Role: scored (load-bearing)
- Action: For each metal and each q, report the relaxed and unrelaxed generalized stacking fault energy per unit area in mJ/m². Write gsf_energy.csv.
- Output file: `/app/outputs/gsf_energy.csv`
- Format: csv
- Contract: csv with columns: metal (string), q (float), relaxed_energy (float, mJ/m²), unrelaxed_energy (float, mJ/m²). One row per (metal, q) combination.
- Scoring: scored by hidden verifier

### Step 5: Compute interlayer spacings
- Role: scored
- Action: From the relaxed and unrelaxed atomic positions, extract the first, second, and third interlayer spacings for each q. Write interlayer_spacings.csv.
- Output file: `/app/outputs/interlayer_spacings.csv`
- Format: csv
- Contract: csv with columns: metal (string), q (float), layer_number (int, 1-3), relaxed_spacing (float, Å), unrelaxed_spacing (float, Å).
- Scoring: scored by hidden verifier

### Step 6: Summarize key quantities
- Role: scored
- Action: Report the stacking fault energy (SFE, energy at q=1), unstable SFE (maximum energy along the relaxed GSF curve), and the c/a ratio at the stacking fault (q=1) for each metal. Write summary.csv.
- Output file: `/app/outputs/summary.csv`
- Format: csv
- Contract: csv with columns: metal (string), SFE (float, mJ/m²), unstable_SFE (float, mJ/m²), c_over_a (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gsf_energy.csv`
- `/app/outputs/interlayer_spacings.csv`
- `/app/outputs/summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gsf_energy.csv
- path: `/app/outputs/gsf_energy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Generalized stacking fault energy curve (relaxed and unrelaxed) as a function of stacking fault variable q. The checker will recompute SFE (energy at q=1) and unstable SFE (maximum relaxed energy) from this file and compare to hidden paper-reported values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `q`, `relaxed_energy`, `unrelaxed_energy`
  - `units`:
    - `relaxed_energy`: mJ/m²
    - `unrelaxed_energy`: mJ/m²

### interlayer_spacings.csv
- path: `/app/outputs/interlayer_spacings.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Interlayer spacing changes vs q for the first, second, and third layers. The checker will audit qualitative trends (e.g., expansion/contraction patterns).
- schema:
  - `type`: table
  - `required_columns`: `metal`, `q`, `layer_number`, `relaxed_spacing`, `unrelaxed_spacing`
  - `units`:
    - `relaxed_spacing`: Å
    - `unrelaxed_spacing`: Å

### summary.csv
- path: `/app/outputs/summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Summary of SFE, unstable SFE, and c/a ratio at the stacking fault. Checker compares these values to hidden paper-reported references within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `SFE`, `unstable_SFE`, `c_over_a`
  - `units`:
    - `SFE`: mJ/m²
    - `unstable_SFE`: mJ/m²
    - `c_over_a`: dimensionless

Notes: The tight-binding solver must be implemented or adapted from an open-source code (e.g., pyscf, sisl, or a custom NRL-TB implementation). The original Mehl TB code is proprietary; the agent is expected to use an equivalent open-source engine. All results are computed from scratch; no pre-made intermediate files are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gsf_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "q",
          "relaxed_energy",
          "unrelaxed_energy"
        ],
        "units": {
          "relaxed_energy": "mJ/m²",
          "unrelaxed_energy": "mJ/m²"
        }
      },
      "description": "Generalized stacking fault energy curve (relaxed and unrelaxed) as a function of stacking fault variable q. The checker will recompute SFE (energy at q=1) and unstable SFE (maximum relaxed energy) from this file and compare to hidden paper-reported values within tolerances."
    },
    {
      "file": "interlayer_spacings.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "q",
          "layer_number",
          "relaxed_spacing",
          "unrelaxed_spacing"
        ],
        "units": {
          "relaxed_spacing": "Å",
          "unrelaxed_spacing": "Å"
        }
      },
      "description": "Interlayer spacing changes vs q for the first, second, and third layers. The checker will audit qualitative trends (e.g., expansion/contraction patterns)."
    },
    {
      "file": "summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "SFE",
          "unstable_SFE",
          "c_over_a"
        ],
        "units": {
          "SFE": "mJ/m²",
          "unstable_SFE": "mJ/m²",
          "c_over_a": "dimensionless"
        }
      },
      "description": "Summary of SFE, unstable SFE, and c/a ratio at the stacking fault. Checker compares these values to hidden paper-reported references within tolerances."
    }
  ],
  "notes": "The tight-binding solver must be implemented or adapted from an open-source code (e.g., pyscf, sisl, or a custom NRL-TB implementation). The original Mehl TB code is proprietary; the agent is expected to use an equivalent open-source engine. All results are computed from scratch; no pre-made intermediate files are provided."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three CSV artifacts. For gsf_energy.csv, the verifier will recompute the SFE and unstable SFE from your reported energy curve and check that these derived values are consistent with expected results. For interlayer_spacings.csv, the verifier will audit the qualitative trends of contraction/expansion across layers for each metal. For summary.csv, the verifier will compare your reported SFE, unstable SFE, and c/a ratio against reference values using appropriate tolerances. The final reward is a weighted combination of all checks, with the majority weight on the SFE and unstable SFE correctness. Reporting the paper's numbers without running the actual calculations is not sufficient; the verifier examines the raw data you submit.
