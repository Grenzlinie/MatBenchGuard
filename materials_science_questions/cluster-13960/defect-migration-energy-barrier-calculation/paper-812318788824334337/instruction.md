# Oxygen vacancy formation energy under electric fields in a cuprate slab

## Problem background
Ionic-liquid gating can create extremely large electric fields at the surface of oxides, driving the superconductor-to-insulator transition in thin films of YBa2Cu3O7. The microscopic origin of this transition is thought to involve the formation and migration of oxygen vacancies from the CuO chain-terminated surface. This task investigates how external electric fields affect the oxygen vacancy formation energy and surface structure in such a slab, providing insight into the doping mechanism behind the resistivity change.

## Approach
We employ density-functional theory (DFT) with the PBE functional and Rappe-Rabe-Kaxiras-Joannopoulos ultrasoft pseudopotentials, as implemented in Quantum ESPRESSO. A CuO chain-terminated YBa2Cu3O7 slab with two unit cells along the z direction and a 2×2 in-plane supercell is constructed, using a fixed in-plane lattice constant. External electric fields are applied via a self-consistent sawtooth potential with a dipole correction. The formation energy of a single oxygen vacancy at the surface CuO chain (configuration (a)) is computed for a range of field strengths using the formula ΔE_vac = (E_vac − E_stoi + μ_O), where μ_O is obtained from the total energy of an isolated O2 molecule. Additionally, characteristic bond lengths are extracted from the relaxed geometry at the strongest field to quantify structural changes.

## Reproduction target
Compute the oxygen vacancy formation energy per vacancy for a single surface CuO chain vacancy in a two-unit-cell-thick YBa2Cu3O7 slab at external electric fields of 0, 4, 6, 10, and 30 V/nm. Use the formula ΔE_vac = (E_vac − E_stoi + μ_O) with μ_O = E(O2)/2. Output the formation energies in formation_energies.csv. From the optimized defective slab at 30 V/nm, extract the Cu–O_surface and O_plane–O_surface bond lengths and write them to bond_lengths.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- pslibrary ultrasoft pseudopotentials (RRKJ): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build slab models
- Role: process
- Action: Construct the CuO chain-terminated YBa2Cu3O7 slab with two unit cells along z and a 2x2 supercell in-plane (lattice constant a=3.9419 Å), including a vacuum region. Also build the defective slab with a single oxygen vacancy at the surface CuO chain (configuration (a)).
- Evidence: `/app/outputs/slab_models.pdb`

### Step 2: O2 molecule reference calculation
- Role: process
- Action: Compute the total energy of an isolated O2 molecule using DFT with the same settings (PBE, ultrasoft pseudopotentials, wavefunction/charge density cutoffs 50/450 Ry) to derive the oxygen chemical potential mu_O = E(O2)/2.
- Evidence: `/app/outputs/o2_energy.txt`

### Step 3: Calculate oxygen vacancy formation energy
- Role: scored (load-bearing)
- Action: For each external electric field (0, 4, 6, 10, 30 V/nm), apply a sawtooth potential with dipole correction, relax the stoichiometric slab and the defective slab (configuration (a)), then compute the vacancy formation energy per vacancy using ΔE_vac = (E_vac - E_stoi + mu_O). Output formation_energies.csv with columns field_V_per_nm and delta_E_vac_eV.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: field_V_per_nm: float, delta_E_vac_eV: float
- Scoring: scored by hidden verifier

### Step 4: Extract bond lengths at 30 V/nm
- Role: scored (load-bearing)
- Action: From the optimized defective slab at 30 V/nm, measure the Cu-O_surface bond length and the O_plane-O_surface distance. Write bond_lengths.json with keys Cu_O_surface_A and O_plane_O_surface_A, both in Angstrom.
- Output file: `/app/outputs/bond_lengths.json`
- Format: json
- Contract: {"Cu_O_surface_A": float, "O_plane_O_surface_A": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/bond_lengths.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vacancy formation energies per vacancy for configuration (a) at five electric field strengths.
- schema:
  - `type`: table
  - `required_columns`: `field_V_per_nm`, `delta_E_vac_eV`
  - `units`:
    - `field_V_per_nm`: V/nm
    - `delta_E_vac_eV`: eV

### bond_lengths.json
- path: `/app/outputs/bond_lengths.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Cu-O_surface and O_plane-O_surface distances from the relaxed defective slab at 30 V/nm, showing bond lengthening.
- schema:
  - `type`: object
  - `required`:
    - `Cu_O_surface_A`: float
    - `O_plane_O_surface_A`: float
  - `units`:
    - `Cu_O_surface_A`: Å
    - `O_plane_O_surface_A`: Å

Notes: The task reproduces the surface vacancy configuration (a) and the structural change at maximum field. Other defect configurations, band structure, CI-NEB, and field penetration analysis are omitted.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_V_per_nm",
          "delta_E_vac_eV"
        ],
        "units": {
          "field_V_per_nm": "V/nm",
          "delta_E_vac_eV": "eV"
        }
      },
      "description": "Vacancy formation energies per vacancy for configuration (a) at five electric field strengths."
    },
    {
      "file": "bond_lengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Cu_O_surface_A": "float",
          "O_plane_O_surface_A": "float"
        },
        "units": {
          "Cu_O_surface_A": "Å",
          "O_plane_O_surface_A": "Å"
        }
      },
      "description": "Cu-O_surface and O_plane-O_surface distances from the relaxed defective slab at 30 V/nm, showing bond lengthening."
    }
  ],
  "notes": "The task reproduces the surface vacancy configuration (a) and the structural change at maximum field. Other defect configurations, band structure, CI-NEB, and field penetration analysis are omitted."
}
```

## How you are scored
An automated hidden verifier inspects your two scored output files. For formation_energies.csv it verifies that the reported delta_E_vac_eV values strictly decrease with increasing field, and it compares each value to reference numbers within a tolerance. For bond_lengths.json it compares the two distances to reference values within predefined tolerances. The final reward is a weighted combination of the scores from these checks; simply reporting numbers without performing the required DFT calculations will not satisfy the verifier.
