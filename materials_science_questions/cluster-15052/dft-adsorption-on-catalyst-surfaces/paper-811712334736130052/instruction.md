# DFT Cu Adsorption on Functionalized Carbon Nanotubes

## Problem background
Carbon nanotubes (CNTs) reinforced metal composites hold promise for lightweight structural applications, but weak interfacial bonding between CNTs and the metal matrix limits their performance. Oxygen-containing functional groups introduced during chemical treatment may alter Cu adhesion. This task addresses the question of how atomic oxygen (–O), hydroxyl (–OH), and carboxyl (–COOH) groups on pristine, Stone‑Wales defective, and monovacancy defective (6,6) CNTs affect the binding energy of a single Cu atom. The computed quantities — BSSE‑corrected binding energies and equilibrium Cu–O distances — are needed to assess which functionalization strategies strengthen the Cu–CNT interface.

## Approach
The method uses spin‑polarized density functional theory (DFT) with the PBE functional, DZP basis set, and periodic boundary conditions. For three CNT models (pristine, Stone‑Wales defect, monovacancy), geometry optimizations are performed both for the bare/functionalized tube alone and for the same tube with a Cu adatom placed near the oxygen site. Total energies from the optimizations are then used to compute the binding energy: Eb = E(CNT+Cu) – E(CNT) – E(Cu_atom), with counterpoise BSSE correction. The nearest Cu–O distance is extracted from the relaxed Cu‑adsorbed geometry. The workflow yields all twelve configurations (including the three bare CNT baselines) for which Eb and d_Cu‑O are reported, enabling comparison across defect types and functional groups.

## Reproduction target
Produce a CSV file `binding_energies.csv` containing BSSE‑corrected binding energies (Eb, in eV) and equilibrium Cu–O distances (d_Cu_O, in Å) for each of the twelve configurations: P‑CNT, SW‑CNT, MV‑CNT (bare baselines) and their nine oxygen‑functionalized variants (atomic O, OH, COOH). The file must have columns `system`, `Eb`, `d_Cu_O`; for bare CNTs without oxygen, d_Cu_O is not applicable; set it to `-1` or leave empty.

## Assets

- SIESTA DFT code: https://gitlab.com/siesta-project/siesta
- PBE pseudopotentials (Troullier‑Martins): https://departments.icmab.es/leem/siesta/Databases/Pseudopotentials/

## Workflow steps

### Step 1: Construct CNT and functionalized CNT models
- Role: process
- Action: Generate atomic coordinates for three (6,6) armchair CNT supercells (120 C atoms): pristine tube (P-CNT), a tube with a Stone‑Wales defect (SW-CNT), and a tube with a monovacancy (MV-CNT). For each CNT, create three functionalized variants by attaching atomic oxygen (ether‑like on P-CNT, bridge on SW-CNT, dangling‑C passivation on MV-CNT), a hydroxyl group (-OH), and a carboxyl group (-COOH) at the specified adsorption sites. Output twelve starting structures for subsequent DFT calculations.
- Evidence: `/app/outputs/cnT_structures.log`

### Step 2: DFT calculations and binding energy extraction
- Role: scored (load-bearing)
- Action: Using SIESTA with the PBE functional, DZP basis set, 150 Ry mesh cutoff, and 5 k‑points along the tube axis, perform spin‑polarized geometry optimizations for each of the 12 CNT models (without Cu) and for the corresponding 12 CNT+Cu complexes (single Cu placed near the oxygen/functional group), applying periodic boundary conditions with 6 Å lateral vacuum. From the optimized total energies, compute the BSSE‑corrected binding energy via Eb = E(CNT+Cu) − E(CNT) − E(Cu_atom). Extract the nearest Cu–O distance from each relaxed Cu‑adsorbed structure. Produce a CSV file binding_energies.csv with one row per configuration, containing the system identifier, calculated Eb (eV), and d_Cu‑O (Å). Include rows for the three bare CNT baselines; for these, set d_Cu_O to -1 or N/A.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with columns: system (str), Eb (float, eV), d_Cu_O (float, Å). Exactly 12 data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: BSSE‑corrected Cu binding energies for the nine functionalized CNT+Cu complexes and the three bare CNT baselines. Lower (more negative) binding energies indicate stronger binding.
- schema:
  - `type`: table
  - `required_columns`: `system`, `Eb`
  - `units`:
    - `Eb`: eV

Notes: Binding energies are reported with a minus sign for exothermic binding. The hidden checker compares each value to reference values; meeting or exceeding (more negative) the reference earns full credit, and score decays only for weaker binding (less negative).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "Eb"
        ],
        "units": {
          "Eb": "eV"
        }
      },
      "description": "BSSE‑corrected Cu binding energies for the nine functionalized CNT+Cu complexes and the three bare CNT baselines. Lower (more negative) binding energies indicate stronger binding."
    }
  ],
  "notes": "Binding energies are reported with a minus sign for exothermic binding. The hidden checker compares each value to reference values; meeting or exceeding (more negative) the reference earns full credit, and score decays only for weaker binding (less negative)."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/binding_energies.csv` and scores it against hidden quality criteria that combine numerical agreement (within tolerances appropriate for a re‑run of a DFT protocol) and consistency with expected physical trends (e.g., that functionalization strengthens binding, and that some functional groups provide larger enhancement than others). Each criterion contributes a weight to a final reward between 0 and 1. The verifier does not access the original paper; it judges only the content you place in `/app/outputs`.
