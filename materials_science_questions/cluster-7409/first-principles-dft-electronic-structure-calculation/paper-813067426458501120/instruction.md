# DFT electronic structure of WO3 surfaces: glucose binding and PDOS enhancement

## Problem background
Tungsten oxide (WO3) is a promising material for non-enzymatic electrochemical glucose sensors. Doping with silver (Ag) has been found to significantly improve the sensitivity compared to pure WO3, but the underlying electronic-structure mechanism is not fully understood. Density functional theory (DFT) simulations can probe how glucose interacts with bare and Ag-doped WO3 surfaces, revealing differences in binding strength and changes in the electronic density of states that may explain the enhanced sensing performance.

## Approach
Use periodic density functional theory (DFT) with the PW91 generalized gradient approximation (GGA) and plane-wave basis sets, employing pseudopotentials to describe core electrons. The workflow begins with bulk monoclinic WO3: optimize its unit cell, compute lattice parameters and the GGA band gap. From the relaxed bulk, cleave and construct an O-terminated (100) surface slab with sufficient vacuum, then relax the slab. Next, place a single Ag atom on the relaxed surface and relax the combined system to obtain the Ag-adsorbed surface. Independently, optimize an isolated alpha-D-glucose molecule in a large box. Then, adsorb the glucose molecule onto both the bare WO3 (100) surface and the Ag-adsorbed WO3 (100) surface, relaxing each adsorbate–surface system. From the total energies of the separate components and the combined systems, compute binding energies for Ag on WO3, glucose on bare WO3, and glucose on Ag-WO3. Additionally, extract the projected density of states (PDOS) of the W d orbital for the bare and Ag-doped surface systems, aligning the energy so that the Fermi level is at 0 eV. All DFT calculations can be performed with the open-source Quantum ESPRESSO package using appropriate pseudopotentials (e.g., from the SSSP efficiency library).

## Reproduction target
The goal is to compute the following quantities and write them to the specified output files:
1. `bulk_properties.json`: optimized lattice parameters a, b, c (Å), GGA band gap (eV), and total DOS at the Fermi level (states/eV/unit cell) for monoclinic WO3.
2. `surface_results.json`: binding energies (eV) for Ag on WO3, glucose on bare WO3, and glucose on Ag-WO3, together with the glucose O–W bond length on the bare surface and the glucose O–Ag bond length on the Ag-doped surface.
3. `pdos_comparison.csv`: a table with columns `energy_eV` (energy relative to Fermi level), `pdos_W_d_bare`, and `pdos_W_d_Ag_doped`, covering at least the energy range from –2 to +2 eV around the Fermi level.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Monoclinic WO3 bulk structure: https://materialsproject.org/materials/mp-19030
- Alpha-D-glucose molecular structure: https://pubchem.ncbi.nlm.nih.gov/compound/5793

## Workflow steps

### Step 1: Bulk WO3 DFT optimization and electronic structure
- Role: scored
- Action: Relax the bulk monoclinic WO3 unit cell using DFT, compute the optimized lattice parameters a, b, c, the band gap (GGA), and the total density of states at the Fermi level. Write the results to bulk_properties.json.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: JSON object with keys 'a', 'b', 'c' (lattice parameters in Angstrom, floats), 'band_gap' (eV, float), 'total_dos_at_fermi' (states/eV/unit cell, float).
- Scoring: scored by hidden verifier

### Step 2: WO3 (100) surface generation and relaxation
- Role: process
- Action: From the optimized bulk WO3, cleave and construct the O-terminated (100) surface slab with appropriate vacuum. Relax the slab geometry with DFT, saving the final structure to surface_slab.poscar.
- Evidence: `/app/outputs/surface_slab.poscar`

### Step 3: Ag adsorption on WO3 (100) surface
- Role: process
- Action: Place one Ag atom above the relaxed WO3 (100) surface, perform DFT relaxation, and save the optimized geometry to ag_surface.poscar. Record the final Ag-O bond length (to be used later).
- Evidence: `/app/outputs/ag_surface.poscar`

### Step 4: Glucose molecule optimization
- Role: process
- Action: Optimize the geometry of an isolated alpha-D-glucose molecule in a large cubic box, writing the optimized coordinates to glucose_opt.xyz.
- Evidence: `/app/outputs/glucose_opt.xyz`

### Step 5: Glucose adsorption on bare and Ag-doped WO3 surfaces
- Role: process
- Action: Perform DFT relaxations of glucose on the bare WO3 (100) surface and on the Ag-doped WO3 (100) surface. From each relaxed system, extract: the final total energy of the system, the W-O(glucose) bond length (bare) or Ag-O(glucose) bond length (Ag-doped), and the projected density of states (PDOS) of the W d orbital aligned so that the Fermi level is at 0 eV. Save all energies, bond lengths, and PDOS data into adsorption_data.json.
- Evidence: `/app/outputs/adsorption_data.json`

### Step 6: Surface binding energies
- Role: scored (load-bearing)
- Action: Using the energies from adsorption_data.json and the separate isolated component energies (isolated Ag atom, isolated glucose, bare slab, Ag-doped slab), compute the binding energies: Ag on WO3 (E_b_Ag = E(WO3+Ag) - E(WO3_slab) - E(Ag_isolated)), glucose on bare WO3 (E_b_glc_bare = E(WO3+glc) - E(WO3_slab) - E(glc_isolated)), glucose on Ag-WO3 (E_b_glc_Ag = E(Ag-WO3+glc) - E(Ag-WO3_slab) - E(glc_isolated)). Also extract the bond lengths O-W (bare) and O-Ag (Ag-doped). Write the results to surface_results.json.
- Output file: `/app/outputs/surface_results.json`
- Format: json
- Contract: JSON object with keys: 'binding_energy_Ag_on_WO3' (eV, float), 'binding_energy_glucose_on_WO3' (eV, float), 'binding_energy_glucose_on_Ag_WO3' (eV, float), 'bond_length_glucose_O_W' (Angstrom, float), 'bond_length_glucose_O_Ag' (Angstrom, float).
- Scoring: scored by hidden verifier

### Step 7: PDOS comparison
- Role: scored
- Action: From the PDOS data in adsorption_data.json, extract the W d-orbital PDOS for the bare and Ag-doped surface systems. Align the energy axis so that the Fermi level is at 0 eV and create a CSV file with columns: 'energy_eV' (energy relative to Fermi level in eV), 'pdos_W_d_bare' (PDOS of W d orbital on bare WO3 surface), 'pdos_W_d_Ag_doped' (PDOS of W d orbital on Ag-doped WO3 surface). Cover the energy range at least from -2 to +2 eV. Save to pdos_comparison.csv.
- Output file: `/app/outputs/pdos_comparison.csv`
- Format: csv
- Contract: CSV file with three columns: 'energy_eV' (float, energy in eV relative to Fermi level), 'pdos_W_d_bare' (float, PDOS of W d orbital on bare WO3 surface), 'pdos_W_d_Ag_doped' (float, PDOS of W d orbital on Ag-doped WO3 surface).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/surface_results.json`
- `/app/outputs/pdos_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized bulk monoclinic WO3 lattice parameters, GGA band gap, and total DOS at the Fermi level; validates the DFT setup.
- schema:
  - `type`: object
  - `required`: `a`, `b`, `c`, `band_gap`, `total_dos_at_fermi`
  - `units`:
    - `a`: Angstrom
    - `b`: Angstrom
    - `c`: Angstrom
    - `band_gap`: eV
    - `total_dos_at_fermi`: states/eV/unit cell

### surface_results.json
- path: `/app/outputs/surface_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT-computed binding energies of Ag on WO3, glucose on WO3, and glucose on Ag-WO3, together with the relevant surface bond lengths.
- schema:
  - `type`: object
  - `required`: `binding_energy_Ag_on_WO3`, `binding_energy_glucose_on_WO3`, `binding_energy_glucose_on_Ag_WO3`, `bond_length_glucose_O_W`, `bond_length_glucose_O_Ag`
  - `units`:
    - `binding_energy_Ag_on_WO3`: eV
    - `binding_energy_glucose_on_WO3`: eV
    - `binding_energy_glucose_on_Ag_WO3`: eV
    - `bond_length_glucose_O_W`: Angstrom
    - `bond_length_glucose_O_Ag`: Angstrom

### pdos_comparison.csv
- path: `/app/outputs/pdos_comparison.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Projected density of states for the W d orbital on bare and Ag-doped WO3(100) surfaces, aligned with the Fermi level at 0 eV. Used to recompute the integrated density of states near the Fermi level and verify enhancement upon Ag doping.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `pdos_W_d_bare`, `pdos_W_d_Ag_doped`
  - `units`:
    - `energy_eV`: eV
    - `pdos_W_d_bare`: states/eV
    - `pdos_W_d_Ag_doped`: states/eV

Notes: The original paper used VASP; the reproduction package uses open-source Quantum ESPRESSO with PW91 GGA pseudopotentials. The experimental synthesis, characterization, and electrochemical sensing parts are excluded because they are wet-lab procedures that cannot be reproduced by code. This plan covers only the DFT electronic structure simulations that provide theoretical insight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "b",
          "c",
          "band_gap",
          "total_dos_at_fermi"
        ],
        "units": {
          "a": "Angstrom",
          "b": "Angstrom",
          "c": "Angstrom",
          "band_gap": "eV",
          "total_dos_at_fermi": "states/eV/unit cell"
        }
      },
      "description": "Optimized bulk monoclinic WO3 lattice parameters, GGA band gap, and total DOS at the Fermi level; validates the DFT setup."
    },
    {
      "file": "surface_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "binding_energy_Ag_on_WO3",
          "binding_energy_glucose_on_WO3",
          "binding_energy_glucose_on_Ag_WO3",
          "bond_length_glucose_O_W",
          "bond_length_glucose_O_Ag"
        ],
        "units": {
          "binding_energy_Ag_on_WO3": "eV",
          "binding_energy_glucose_on_WO3": "eV",
          "binding_energy_glucose_on_Ag_WO3": "eV",
          "bond_length_glucose_O_W": "Angstrom",
          "bond_length_glucose_O_Ag": "Angstrom"
        }
      },
      "description": "DFT-computed binding energies of Ag on WO3, glucose on WO3, and glucose on Ag-WO3, together with the relevant surface bond lengths."
    },
    {
      "file": "pdos_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "pdos_W_d_bare",
          "pdos_W_d_Ag_doped"
        ],
        "units": {
          "energy_eV": "eV",
          "pdos_W_d_bare": "states/eV",
          "pdos_W_d_Ag_doped": "states/eV"
        }
      },
      "description": "Projected density of states for the W d orbital on bare and Ag-doped WO3(100) surfaces, aligned with the Fermi level at 0 eV. Used to recompute the integrated density of states near the Fermi level and verify enhancement upon Ag doping."
    }
  ],
  "notes": "The original paper used VASP; the reproduction package uses open-source Quantum ESPRESSO with PW91 GGA pseudopotentials. The experimental synthesis, characterization, and electrochemical sensing parts are excluded because they are wet-lab procedures that cannot be reproduced by code. This plan covers only the DFT electronic structure simulations that provide theoretical insight."
}
```

## How you are scored
Each of the three scored artifacts (`bulk_properties.json`, `surface_results.json`, `pdos_comparison.csv`) will be evaluated independently by a hidden verifier. The verifier checks structural validity (schemas, units, columns) and compares your reported numbers against physical expectations derived from the DFT methodology. The final reward (a number between 0 and 1) is the weighted sum of the per-artifact scores, with the binding energy file carrying the largest weight. Simply reporting numbers that happen to match a target without following the required workflow will not yield a high reward; your entire DFT execution must be consistent and the results must be physically plausible.
