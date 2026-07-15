# Surface relaxation calculations of cubic BaZrO3 and BaTiO3 (001) surfaces

## Problem background
The (001) surfaces of cubic perovskite oxides BaZrO3 (BZO) and BaTiO3 (BTO) exhibit distinct patterns of atomic relaxation and surface rumpling. A proposed explanation is that the larger bulk cell volume of BaZrO3 provides more free space for surface atoms, enabling greater displacements. This task investigates that hypothesis by computing the relaxed surface structures and the energetic response of surface atoms to displacements, allowing a quantitative assessment of the cell-volume effect.

## Approach
First-principles density functional theory (DFT) calculations will be used to construct (001) slab models of cubic BaZrO3 and BaTiO3 with two different terminations: BaO and MO2 (M = Zr or Ti). The bulk equilibrium lattice constants are first determined using both LDA and GGA exchange-correlation functionals. Symmetric slabs are built from the optimized bulk lattices, and all atomic positions are relaxed until forces and energies converge. From the relaxed structures, atomic displacements δz (relative to ideal bulk positions) and geometric relaxation parameters (rumpling s, interlayer spacing changes Δd12, Δd23) are extracted. To probe the energetic driving forces for relaxation, total energies are computed as a function of controlled rigid displacements of selected surface atoms (Ba in the BaO termination, O in the MO2 termination). Additionally, the indirect band gap of the ZrO2-terminated BaZrO3 surface is calculated.

## Reproduction target
Produce four structured CSV files containing:
- Atomic displacements δz for the first three atomic layers, expressed as a percentage of the theoretical lattice constant a0, for each combination of material (BZO/BTO), termination (BaO/MO2), and functional (LDA/GGA).
- Surface relaxation parameters: rumpling s and interlayer spacing changes Δd12 and Δd23, all in percent of a0, for the same combinations.
- Total energy versus displacement fraction (in fractions of a0) for Ba atoms (BaO termination) and O atoms (MO2 termination) over a range of displacements, separately for BZO and BTO.
- Indirect band gap (in eV) of the relaxed ZrO2-terminated BaZrO3 surface for both LDA and GGA.
The goal is to obtain results that allow a consistent comparison of the surface relaxation behavior and energy trends between the two materials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (PseudoDojo / SSSP): https://www.materialscloud.org/discover/sssp/
- Crystal structures for cubic BaZrO3 and BaTiO3

## Workflow steps

### Step 1: Bulk structure optimization
- Role: process
- Action: Perform DFT bulk structure optimization for cubic BaZrO3 and BaTiO3 using both LDA and GGA functionals to obtain equilibrium lattice constants a0.
- Evidence: `/app/outputs/bulk_opt.log`

### Step 2: Surface slab relaxation for all terminations and functionals
- Role: process
- Action: Construct (001) slab models for both BaO- and MO2-terminated surfaces of BaZrO3 and BaTiO3 using the computed bulk lattice constants. Relax all atomic positions with LDA and GGA until forces are below threshold and energies converged.
- Evidence: `/app/outputs/slab_relax.log`

### Step 3: Atomic displacements
- Role: scored
- Action: From the relaxed slab structures, compute the atomic displacements δz (in % of a0) for layers 1-3 for all material/termination/functional combinations. Write to step_01_displacements.csv.
- Output file: `/app/outputs/step_01_displacements.csv`
- Format: csv
- Contract: Columns: material (BZO/BTO), termination (BaO/MO2), functional (LDA/GGA), layer (1/2/3), atom (Ba/Zr/Ti/O), displacement_percent (float, % of a0).
- Scoring: scored by hidden verifier

### Step 4: Surface relaxation parameters
- Role: scored
- Action: From the relaxed slab structures, compute the rumpling parameter s and interlayer spacing changes Δd12 and Δd23 (all in % of a0) for each material/termination/functional combination. Write to step_02_surface_params.csv.
- Output file: `/app/outputs/step_02_surface_params.csv`
- Format: csv
- Contract: Columns: material, termination, functional, s (float, % a0), d12 (float, % a0), d23 (float, % a0).
- Scoring: scored by hidden verifier

### Step 5: Total energy vs displacement scans
- Role: scored (load-bearing)
- Action: Using the relaxed slab structures, perform static total-energy calculations while rigidly displacing the Ba atom (BaO-termination) or the O atom (MO2-termination) along [001] in small steps. Record total energy as a function of displacement fraction for BZO and BTO. Write to step_03_energy_scans.csv.
- Output file: `/app/outputs/step_03_energy_scans.csv`
- Format: csv
- Contract: Columns: material, termination, atom (Ba or O), displacement_fraction (float, fraction of a0), total_energy_Ry (float).
- Scoring: scored by hidden verifier

### Step 6: Band gap for ZrO2-terminated surface
- Role: scored (load-bearing)
- Action: Perform a band-gap calculation on the relaxed ZrO2-terminated BaZrO3 surface slab for both LDA and GGA. Report the indirect band gap in eV. Write to step_04_band_gap.csv.
- Output file: `/app/outputs/step_04_band_gap.csv`
- Format: csv
- Contract: Columns: functional (LDA/GGA), band_gap_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_displacements.csv`
- `/app/outputs/step_02_surface_params.csv`
- `/app/outputs/step_03_energy_scans.csv`
- `/app/outputs/step_04_band_gap.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_displacements.csv
- path: `/app/outputs/step_01_displacements.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Atomic displacements δz for layers 1-3, comparable to paper Table I.
- schema:
  - `type`: table
  - `required_columns`: `material`, `termination`, `functional`, `layer`, `atom`, `displacement_percent`
  - `units`:
    - `displacement_percent`: % of a0

### step_02_surface_params.csv
- path: `/app/outputs/step_02_surface_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface relaxation parameters s, Δd12, Δd23, comparable to paper Table II.
- schema:
  - `type`: table
  - `required_columns`: `material`, `termination`, `functional`, `s`, `d12`, `d23`
  - `units`:
    - `s`: % a0
    - `d12`: % a0
    - `d23`: % a0

### step_03_energy_scans.csv
- path: `/app/outputs/step_03_energy_scans.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total energy vs. displacement curves; must show energy decreases for BZO and not for BTO.
- schema:
  - `type`: table
  - `required_columns`: `material`, `termination`, `atom`, `displacement_fraction`, `total_energy_Ry`
  - `units`:
    - `displacement_fraction`: fraction of a0
    - `total_energy_Ry`: Rydberg

### step_04_band_gap.csv
- path: `/app/outputs/step_04_band_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Indirect band gap of the ZrO2-terminated BZO surface.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: The additional BTO-with-enlarged-lattice test (~12% Ba displacement) is omitted as it is a supportive control, not a headline result. Full band-structure plots and projected density-of-states are not included.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_displacements.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "termination",
          "functional",
          "layer",
          "atom",
          "displacement_percent"
        ],
        "units": {
          "displacement_percent": "% of a0"
        }
      },
      "description": "Atomic displacements δz for layers 1-3, comparable to paper Table I."
    },
    {
      "file": "step_02_surface_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "termination",
          "functional",
          "s",
          "d12",
          "d23"
        ],
        "units": {
          "s": "% a0",
          "d12": "% a0",
          "d23": "% a0"
        }
      },
      "description": "Surface relaxation parameters s, Δd12, Δd23, comparable to paper Table II."
    },
    {
      "file": "step_03_energy_scans.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "termination",
          "atom",
          "displacement_fraction",
          "total_energy_Ry"
        ],
        "units": {
          "displacement_fraction": "fraction of a0",
          "total_energy_Ry": "Rydberg"
        }
      },
      "description": "Total energy vs. displacement curves; must show energy decreases for BZO and not for BTO."
    },
    {
      "file": "step_04_band_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Indirect band gap of the ZrO2-terminated BZO surface."
    }
  ],
  "notes": "The additional BTO-with-enlarged-lattice test (~12% Ba displacement) is omitted as it is a supportive control, not a headline result. Full band-structure plots and projected density-of-states are not included."
}
```

## How you are scored
Each of the four output files is evaluated independently by a hidden verifier. The verifier compares the reported atomic displacements and surface relaxation parameters against reference values (with allowances for differences arising from the choice of DFT code and pseudopotentials). For the energy-vs-displacement curves, the verifier performs a structural check: it confirms that the energy curves for the different materials and terminations exhibit the expected qualitative behavior (e.g., monotonicity). For the band gap, the verifier compares the computed value to a reference. The final reward is a weighted sum of the scores from these four components.
