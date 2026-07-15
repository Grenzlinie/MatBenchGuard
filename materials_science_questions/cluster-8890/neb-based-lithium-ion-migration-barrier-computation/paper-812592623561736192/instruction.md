# Lithium Ion Diffusion and Capacity in 2D Phosphorus Carbide Monolayers

## Problem background
Two-dimensional materials such as phosphorus carbide (PC_x) monolayers are being explored as high-capacity anode materials for lithium-ion batteries due to their potential to combine low Li diffusion barriers with large theoretical specific capacities. In this task you will reproduce the key density functional theory (DFT) predictions for monolayers PC2, PC5, and PC6: their Li adsorption characteristics, the minimum energy barriers for Li diffusion, and the maximum stable Li loading from which the theoretical specific capacity is derived. Successful reproduction yields a quantitative evaluation of these candidates.

## Approach
The workflow uses plane-wave DFT with the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional and the DFT-D2 van der Waals correction. First, the pristine monolayer structures are fully relaxed. Then high-symmetry Li adsorption sites are explored on a 2×2 supercell and the most stable site is identified via adsorption energy. The climbing-image nudged elastic band (CI-NEB) method is employed to locate the minimum-energy path for a single Li atom between nearest-neighbor stable sites, yielding the diffusion barrier. Finally, Li atoms are added incrementally to both sides of the monolayer, with full structural relaxation after each addition, to determine the maximum Li content before structural collapse or loss of binding; this maximum adatom concentration is converted to specific capacity using Faraday's law. All calculations use open-source tools (Quantum ESPRESSO or equivalent DFT code, with the Atomic Simulation Environment (ASE) for workflow management) and standard pseudopotentials (e.g., SSSP library).

## Reproduction target
Compute and report: (1) optimized atomic structures of PC2, PC5, and PC6 monolayers as a ZIP archive containing PC2.cif, PC5.cif, PC6.cif; (2) the most stable Li adsorption site and its adsorption energy (eV) for each monolayer, as a CSV; (3) the lowest Li diffusion energy barrier (eV) between nearest-neighbor adsorption sites for each monolayer, with a brief path description, as a CSV; (4) the maximum Li atoms per formula unit and the corresponding theoretical specific capacity (mAh g⁻¹) for each monolayer, as a CSV. The hidden verifier will compare your computed values to reference results from the literature within predetermined tolerances.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table
- Initial PC2, PC5, PC6 crystal structures: 10.1021/jacs.8b11397

## Workflow steps

### Step 1: Geometry optimization of PCx monolayers
- Role: scored
- Action: Perform DFT geometry optimization for PC2, PC5, and PC6 monolayers using PBE functional with van der Waals correction (DFT-D2). Output the relaxed structures in CIF or POSCAR format, bundled into a ZIP archive.
- Output file: `/app/outputs/step_01_structures.zip`
- Format: other
- Contract: A ZIP archive containing three files: PC2.cif, PC5.cif, PC6.cif. Each file must include lattice constants and atomic coordinates (structure existence check, low weight).
- Scoring: scored by hidden verifier

### Step 2: Li adsorption site search and adsorption energy
- Role: scored
- Action: For each monolayer (PC2, PC5, PC6), identify high-symmetry Li adsorption sites using a 2x2 supercell. Compute the adsorption energy for a single Li atom at the most stable site using E_ad = (E_{PC_xLi} - E_{PC_x} - mu_Li), where mu_Li is the energy per atom in bcc Li. Report the most favourable site per material.
- Output file: `/app/outputs/step_02_adsorption_energies.csv`
- Format: csv
- Contract: CSV with columns: material (string), site_label (string), E_ad_eV (float). One row per material, reporting the most favourable site.
- Scoring: scored by hidden verifier

### Step 3: Li diffusion barrier via CI-NEB
- Role: scored (load-bearing)
- Action: Using the climbing-image nudged elastic band (CI-NEB) method, compute the minimum energy path and diffusion barrier for a single Li atom between nearest-neighbor stable adsorption sites on PC2, PC5, and PC6 monolayers (2x2 supercell). Report the lowest barrier height for each material.
- Output file: `/app/outputs/step_03_diffusion_barriers.csv`
- Format: csv
- Contract: CSV with columns: material (string), barrier_eV (float), path_description (string). One row per material (PC2, PC5, PC6).
- Scoring: scored by hidden verifier

### Step 4: Maximum Li capacity and theoretical specific capacity
- Role: scored (load-bearing)
- Action: Determine the maximum stable Li loading for PC2, PC5, and PC6 by incrementally intercalating Li atoms on both sides of the monolayer in a 2x2 supercell. After each addition, fully relax atomic positions and lattice constants. The maximum loading is the highest number before structural collapse or large Li-substrate distance. Convert the maximum adatom content y_max to theoretical specific capacity using C_M = z * y_max * F / M_{PCx} (z=1, F=26.8 Ah mol^-1, M_{PCx} the molar mass of the monolayer formula unit). Report y_max and capacity for each material.
- Output file: `/app/outputs/step_04_capacity.csv`
- Format: csv
- Contract: CSV with columns: material (string), max_Li_per_fu (float), specific_capacity_mAh_g (float). One row per material (PC2, PC5, PC6).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structures.zip`
- `/app/outputs/step_02_adsorption_energies.csv`
- `/app/outputs/step_03_diffusion_barriers.csv`
- `/app/outputs/step_04_capacity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structures.zip
- path: `/app/outputs/step_01_structures.zip`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Geometry-optimized structures of PC2, PC5, and PC6 monolayers.
- schema:
  - `type`: other
  - `required_files`: `PC2.cif`, `PC5.cif`, `PC6.cif`
  - `description`: ZIP archive containing three CIF/POSCAR files. Checker verifies existence of required files and basic structure (low weight).

### step_02_adsorption_energies.csv
- path: `/app/outputs/step_02_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Li adsorption energy at the most stable site for each monolayer.
- schema:
  - `type`: table
  - `required_columns`: `material`, `site_label`, `E_ad_eV`
  - `units`:
    - `E_ad_eV`: eV

### step_03_diffusion_barriers.csv
- path: `/app/outputs/step_03_diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Li diffusion energy barrier (minimum energy path) for each monolayer.
- schema:
  - `type`: table
  - `required_columns`: `material`, `barrier_eV`, `path_description`
  - `units`:
    - `barrier_eV`: eV

### step_04_capacity.csv
- path: `/app/outputs/step_04_capacity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum Li atom content per formula unit and corresponding theoretical specific capacity.
- schema:
  - `type`: table
  - `required_columns`: `material`, `max_Li_per_fu`, `specific_capacity_mAh_g`
  - `units`:
    - `max_Li_per_fu`: Li per formula unit
    - `specific_capacity_mAh_g`: mAh/g

Notes: The checker compares diffusion barriers and specific capacities to hidden paper reference values using tolerance of ±0.05 eV and 5% relative, respectively; meeting or exceeding (lower barrier, higher capacity) earns full credit. Adsorption energies are checked for consistency with hidden paper values. Structure files are audited for existence and minimal content.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structures.zip",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "required_files": [
          "PC2.cif",
          "PC5.cif",
          "PC6.cif"
        ],
        "description": "ZIP archive containing three CIF/POSCAR files. Checker verifies existence of required files and basic structure (low weight)."
      },
      "description": "Geometry-optimized structures of PC2, PC5, and PC6 monolayers."
    },
    {
      "file": "step_02_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "site_label",
          "E_ad_eV"
        ],
        "units": {
          "E_ad_eV": "eV"
        }
      },
      "description": "Li adsorption energy at the most stable site for each monolayer."
    },
    {
      "file": "step_03_diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "barrier_eV",
          "path_description"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Li diffusion energy barrier (minimum energy path) for each monolayer."
    },
    {
      "file": "step_04_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "max_Li_per_fu",
          "specific_capacity_mAh_g"
        ],
        "units": {
          "max_Li_per_fu": "Li per formula unit",
          "specific_capacity_mAh_g": "mAh/g"
        }
      },
      "description": "Maximum Li atom content per formula unit and corresponding theoretical specific capacity."
    }
  ],
  "notes": "The checker compares diffusion barriers and specific capacities to hidden paper reference values using tolerance of ±0.05 eV and 5% relative, respectively; meeting or exceeding (lower barrier, higher capacity) earns full credit. Adsorption energies are checked for consistency with hidden paper values. Structure files are audited for existence and minimal content."
}
```

## How you are scored
Your submission will be evaluated by a hidden checker that independently assesses each scored artifact. For adsorption energies, diffusion barriers, and specific capacities, the checker compares your reported value to a hidden reference value using a directional policy: a lower diffusion barrier or higher capacity than the reference earns full credit, while a worse value earns proportionally less. The checker also verifies that the relative ordering of the diffusion barriers across the three monolayers matches the expected physical trend. The structure archive is audited for the presence of the required files and minimal structural information, carrying a small weight. The final reward is a weighted sum of the step-level scores, scaled to a 0–1 range. You do not need to match exact numbers; the tolerances account for variation due to different DFT implementations and computational settings.
