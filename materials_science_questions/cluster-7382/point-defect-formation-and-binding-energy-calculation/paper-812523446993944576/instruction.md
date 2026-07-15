# CH3O Radical Binding Energies on Ice Clusters

## Problem background
The CH3O (methoxy) radical is a key intermediate in interstellar astrochemistry, formed on icy grain mantles and involved in the synthesis of complex organic molecules. Quantitative knowledge of its binding energy on water ice surfaces (both crystalline hexagonal ice Ih and amorphous solid water, ASW) is essential for astrochemical models that predict diffusion, reaction rates, and desorption. This computational study calculates the binding energies of the CH3O radical on model ice clusters for a set of 26 distinct binding sites, covering both Ih and ASW surfaces. The binding energies (with and without harmonic zero-point energy correction) are obtained using an ONIOM(QM:MM) scheme and span a range that captures the heterogeneity of realistic icy interstellar grain surfaces.

## Approach
The core approach is a two-layer ONIOM(QM:MM) method. The electronically important region (the top water layer and the adsorbed CH3O radical) is treated with the wB97X-D density functional and the def2-TZVP basis set. The rest of the ice cluster is described by the AMBER non-polarizable force field, using mechanical embedding where the QM–MM interactions are computed at the MM level. Ice structural models for Ih and ASW are taken from Andersson et al. (2006) and partitioned into a QM region of roughly 40–50 water molecules and a frozen MM region. For each of the 26 binding sites, geometry optimizations and harmonic vibrational frequency calculations are performed on the isolated CH3O radical, the bare ice cluster, and the CH3O-bound ice complex, always freezing the MM-region atoms. The binding energy for a site is the absolute difference between the total energy of the bound complex and the sum of the energies of the bare ice cluster and the isolated radical, computed both without zero-point energy and with it included. The procedure yields per-site binding energies that together characterize the distribution and average binding strength of CH3O on interstellar ice analogues.

## Reproduction target
Using the publicly available Andersson et al. (2006) ice cluster structures and an open-source QM/MM implementation (e.g., PySCF) that supports the ONIOM scheme with wB97X-D/def2-TZVP and the AMBER force field, compute the binding energies for all 26 binding sites: 16 on Ih (designated A1–A16) and 10 on ASW (B1–B10). The results must be written to binding_energies.csv with three columns: 'site' (site label), 'binding_energy_no_zpe' (in eV), and 'binding_energy_with_zpe' (in eV), one row per site. The target does not require reporting the aggregate average; the average will be derived from the per-site data by the verifier.

## Assets

- Andersson et al. (2006) ice cluster structures: doi:10.1063/1.2166380, supporting information
- PySCF QM/MM toolkit: https://pyscf.org
- AMBER force field parameters: Standard AMBER distribution (e.g., ff14SB, TIP3P parameters)

## Workflow steps

### Step 1: Build ice cluster models
- Role: process
- Action: Retrieve ice structural models from Andersson et al. (2006). Construct 26 ONIOM models (A1-A16 for Ih, B1-B10 for ASW) with QM region defined as the top water layer (40-50 H2O molecules) and MM region as the remaining frozen water molecules, according to the paper's partitioning.
- Evidence: `/app/outputs/ice_models_generated.txt`

### Step 2: Optimize isolated CH3O and bare ice clusters
- Role: process
- Action: Optimize the geometry of the isolated CH3O radical and each of the 26 bare ice cluster models using ONIOM(wB97X-D/def2-TZVP:AMBER) with mechanical embedding, freezing MM region atoms. Perform harmonic vibrational frequency calculations to obtain zero-point energies (ZPE) and confirm minima.
- Evidence: `/app/outputs/isolated_energies.log`

### Step 3: Optimize CH3O-bound ice complexes
- Role: process
- Action: For each of the 26 binding sites, place the CH3O radical on the ice surface, optimize the complex geometry and compute vibrational frequencies at the same ONIOM level, freezing MM atoms.
- Evidence: `/app/outputs/complex_energies.log`

### Step 4: Calculate binding energies and report
- Role: scored (load-bearing)
- Action: Compute the binding energy without ZPE as |E_complex - E_ice - E_radical|, and with ZPE as |(E_complex+ZPE_complex) - (E_ice+ZPE_ice) - (E_radical+ZPE_radical)| for each site. Write a CSV file 'binding_energies.csv' with columns site, binding_energy_no_zpe (eV), binding_energy_with_zpe (eV) for all 26 sites (A1-A16, B1-B10).
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with columns: site (string), binding_energy_no_zpe (float, eV), binding_energy_with_zpe (float, eV). 26 rows, one per binding site.
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
- target_policy: reference_match
- description: Binding energies (with and without zero-point energy) for each of the 26 binding sites. The checker will compare per-site energies to hidden gold values and recompute the average to verify the paper's reported average binding energy.
- schema:
  - `type`: table
  - `required_columns`: `site`, `binding_energy_no_zpe`, `binding_energy_with_zpe`
  - `units`:
    - `binding_energy_no_zpe`: eV
    - `binding_energy_with_zpe`: eV

Notes: The solver must use the ONIOM method with wB97X-D/def2-TZVP for the QM region and AMBER force field for the MM region, with mechanical embedding and frozen MM atoms. Only the 26 binding sites (A1-A16, B1-B10) are required; the energy decomposition analysis and AMOEBA comparisons are not part of this task.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "binding_energy_no_zpe",
          "binding_energy_with_zpe"
        ],
        "units": {
          "binding_energy_no_zpe": "eV",
          "binding_energy_with_zpe": "eV"
        }
      },
      "description": "Binding energies (with and without zero-point energy) for each of the 26 binding sites. The checker will compare per-site energies to hidden gold values and recompute the average to verify the paper's reported average binding energy."
    }
  ],
  "notes": "The solver must use the ONIOM method with wB97X-D/def2-TZVP for the QM region and AMBER force field for the MM region, with mechanical embedding and frozen MM atoms. Only the 26 binding sites (A1-A16, B1-B10) are required; the energy decomposition analysis and AMOEBA comparisons are not part of this task."
}
```

## How you are scored
A hidden verifier reads your binding_energies.csv. It extracts the binding energy with ZPE for each site and compares each value to independently determined reference energies. The verifier also computes the average of your reported 'binding_energy_with_zpe' values and checks that the binding energies fall within a physically plausible envelope. The final reward is a weighted combination of per-site accuracy and the accuracy of the implied average. Reporting the paper's published numbers is not sufficient; the verifier expects a result that could only come from executing the ONIOM calculations described in this task.
