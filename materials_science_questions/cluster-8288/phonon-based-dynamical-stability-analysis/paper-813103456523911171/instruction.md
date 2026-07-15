# Thickness-dependent formation energies of Te slabs and interlayer coupling

## Problem background
Ultrathin films of tellurium (Te) are promising candidates for extending the two-dimensional materials family to group-VI elements. When grown or truncated from the trigonal bulk Te structure (Te-I), Te films can display strongly thickness-dependent stability and may rearrange into layered motifs. Understanding how the formation energy of Te slabs depends on the number of atomic layers is essential for predicting which thicknesses are most stable. This task computes the formation energy per atom for Te slabs with N atomic layers (N = 1 to 20) and investigates the stability pattern, as well as the van der Waals coupling between neighbouring tellurene layers.

## Approach
The approach is a first-principles density functional theory (DFT) workflow using the Perdew–Burke–Ernzerhof (PBE) functional combined with the DFT-D2 van der Waals correction. First, the bulk trigonal Te (Te-I) unit cell is fully relaxed to obtain a reference energy per atom. Then slab models are built by truncating the relaxed bulk structure along the [001] direction with N atomic layers (N = 1 to 20). Each slab is padded with about 20 Å of vacuum and fully relaxed with the same DFT settings. The formation energy per atom for each thickness is computed as the difference between the slab total energy and the bulk reference, normalised by the number of atoms. Thicknesses that give local minima in the formation energy curve are identified as particularly stable. In addition, the interlayer coupling energy between two adjacent α-Te trilayers is calculated from the total energies of the relaxed 3‑layer and 6‑layer slabs, divided by the in‑plane unit‑cell area.

## Reproduction target
Produce two scored artifacts:
- formation_energies.csv: a table with columns N, E_slab_total (eV), E_bulk_per_atom (eV), and Ef (eV/atom) for every integer N from 1 to 20.
- interlayer_coupling_energy.txt: a single line containing the interlayer binding energy between two α-Te trilayers in meV/Å² (e.g. '26.0 meV/Å^2').
The derivation of these numbers must follow the workflow described in the steps section; the final files are the only submission required.

## Assets

- Bulk trigonal Te (Te-I) crystal structure: https://materialsproject.org/materials/mp-580/
- Te pseudopotential files: https://www.materialscloud.org/discover/sssp/table/efficiency
- Open-source DFT code supporting PBE and DFT-D2: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Relax bulk Te-I unit cell
- Role: process
- Action: Using DFT with PBE functional and DFT-D2 van der Waals correction, fully relax the bulk trigonal Te (Te-I) unit cell (space group P3121) to obtain the reference total energy per atom E_bulk_per_atom.
- Evidence: `/app/outputs/bulk_relaxation.log`

### Step 2: Construct and relax Te slabs for N = 1 to 20 layers
- Role: process
- Action: For each integer N from 1 to 20, construct a slab by truncating the relaxed bulk structure along [001] with N atomic layers, add ~20 Å vacuum, and fully relax atomic positions and cell degrees of freedom using the same DFT settings (PBE+DFT-D2). Record the total energy of each slab.
- Evidence: `/app/outputs/slab_energies.log`

### Step 3: Compute formation energies and write formation_energies.csv
- Role: scored
- Action: For each N, compute the formation energy per atom Ef(N) = [E_slab(N) − N · E_bulk_per_atom] / N and write a CSV file with columns N, E_slab_total (eV), E_bulk_per_atom (eV), and Ef (eV/atom).
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: N (int), E_slab_total (float, eV), E_bulk_per_atom (float, eV), Ef (float, eV/atom). One row per N.
- Scoring: scored by hidden verifier

### Step 4: Compute interlayer coupling energy between α-Te trilayers
- Role: scored (load-bearing)
- Action: From the relaxed structures of the 3‑layer slab (monolayer α‑Te) and the 6‑layer slab (two adjacent trilayers), compute the interlayer binding energy per unit area: (E_6layer − 2 × E_3layer) / (in‑plane area per unit cell). Output the result in meV/Å² to a text file.
- Output file: `/app/outputs/interlayer_coupling_energy.txt`
- Format: txt
- Contract: A single line containing a floating-point number followed by the unit ' meV/Å^2', e.g., '26.0 meV/Å^2'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/interlayer_coupling_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energy per atom for Te slabs of thickness N=1..20 layers, used to identify magic thicknesses via local minima in Ef.
- schema:
  - `type`: table
  - `required_columns`: `N`, `E_slab_total`, `E_bulk_per_atom`, `Ef`
  - `units`:
    - `E_slab_total`: eV
    - `E_bulk_per_atom`: eV
    - `Ef`: eV/atom

### interlayer_coupling_energy.txt
- path: `/app/outputs/interlayer_coupling_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Interlayer coupling energy between two adjacent α-Te trilayers, compared to the paper-reported value with symmetric tolerance.
- schema:
  - `type`: text
  - `required`: single line containing a number and unit 'meV/Å^2'
  - `units`: meV/Å^2

Notes: Magic thicknesses are derived from formation_energies.csv minima; absolute Ef values are not scored. Interlayer coupling energy is compared to the paper reference with a reference_match tolerance (full credit within ±40%, linear decay up to ±80%). Omitted headline quantities (with concrete reasons): (i) optical absorption spectra and carrier mobilities — require extensive additional DFT calculations (dielectric function, deformation potentials) that are not part of the core formation-energy/band-structure pipeline; (ii) β‑Te formation from [010]/[100] truncations — a separate thickness scan that would unnecessarily duplicate the slab‑relaxation pattern; (iii) stability under alternative vdW schemes — a sensitivity analysis beyond the single‑vdW scheme used in the main task; (iv) Se monolayer results — require a different element’s pseudopotential and crystal structure, constituting a separate study.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "E_slab_total",
          "E_bulk_per_atom",
          "Ef"
        ],
        "units": {
          "E_slab_total": "eV",
          "E_bulk_per_atom": "eV",
          "Ef": "eV/atom"
        }
      },
      "description": "Formation energy per atom for Te slabs of thickness N=1..20 layers, used to identify magic thicknesses via local minima in Ef."
    },
    {
      "file": "interlayer_coupling_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": "single line containing a number and unit 'meV/Å^2'",
        "units": "meV/Å^2"
      },
      "description": "Interlayer coupling energy between two adjacent α-Te trilayers, compared to the paper-reported value with symmetric tolerance."
    }
  ],
  "notes": "Magic thicknesses are derived from formation_energies.csv minima; absolute Ef values are not scored. Interlayer coupling energy is compared to the paper reference with a reference_match tolerance (full credit within ±40%, linear decay up to ±80%). Omitted headline quantities (with concrete reasons): (i) optical absorption spectra and carrier mobilities — require extensive additional DFT calculations (dielectric function, deformation potentials) that are not part of the core formation-energy/band-structure pipeline; (ii) β‑Te formation from [010]/[100] truncations — a separate thickness scan that would unnecessarily duplicate the slab‑relaxation pattern; (iii) stability under alternative vdW schemes — a sensitivity analysis beyond the single‑vdW scheme used in the main task; (iv) Se monolayer results — require a different element’s pseudopotential and crystal structure, constituting a separate study."
}
```

## How you are scored
A hidden verifier independently scores each of the two output artifacts:
- The formation_energies.csv is evaluated on the structural trend of Ef(N) — whether it exhibits well-defined local minima at stable thicknesses — not on the absolute energy values.
- The interlayer_coupling_energy.txt is compared to the paper-reported value (26 meV/Å²) with a reference_match policy: full credit within ±40%, linear decay up to ±80%.
The final reward is a weighted combination of these two checks. Simply reporting a number without executing the full simulation or replicating the procedure will not yield a passing score.
