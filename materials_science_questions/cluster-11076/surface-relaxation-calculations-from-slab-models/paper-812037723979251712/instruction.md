# Half-metallicity and magnetism of zinc blende CrP(001) surface from first principles

## Problem background
Half-metallic ferromagnets are attractive for spintronic devices because they exhibit 100% spin polarization. Zinc-blende CrP is predicted to be half-metallic in the bulk. The surface magnetism of CrP(001) is crucial for device applications but may differ from the bulk. This task investigates the electronic and magnetic properties of the CrP(001) surface for Cr- and P-terminated configurations, examining whether half-metallicity is retained and how magnetic moments change at the surface layers compared to the bulk-like center.

## Approach
The surface is studied using first-principles spin-polarized density functional theory (DFT) with the all-electron full-potential linearized augmented plane wave (FLAPW) method and the generalized gradient approximation (GGA-PBE) exchange-correlation functional. Slab models are constructed for Cr-terminated (9 layers) and P-terminated (11 layers with extra P) surfaces of zinc-blende CrP(001) at two lattice constants: 5.48 Å (equilibrium zb-CrP) and 5.89 Å (lattice constant of InP). The topmost Cr layer is relaxed (relaxation is expected negligible). Self-consistent field calculations yield spin-polarized atom-projected density of states (DOS) for surface and bulk-like center atoms, as well as magnetic moments per atom.

## Reproduction target
Produce the spin-polarized DOS of the surface Cr atom for Cr-terminated surfaces and the surface P atom for P-terminated surfaces at both lattice constants, covering the energy range -2.0 to +4.0 eV relative to the Fermi level. Compile a table of magnetic moments (in µB) for all atoms, classified by termination, lattice constant, atom type (Cr/P), and layer (surface S, sub-surface S-1, bulk-like center C). From the DOS, determine the minority-spin band gap width, verify whether surface states exist within the gap, and compute the Cr exchange splitting as the energy separation between the majority spin d-band peak below the Fermi level and the minority spin d-band peak above the gap.

## Assets

- Elk all-electron FLAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Build slab models
- Role: process
- Action: Construct a 9-layer Cr-terminated slab and an 11-layer P-terminated slab (with additional P layers) of zinc-blende CrP(001) for lattice constants 5.48 Å and 5.89 Å. Set up Elk input files with standard computational parameters.
- Evidence: `/app/outputs/slab_input_files`

### Step 2: Surface geometry relaxation
- Role: process
- Action: Perform spin-polarized FLAPW relaxation for each slab by minimizing total energy with respect to the topmost Cr layer positions. Relaxation is expected to be negligible; save relaxed geometries.
- Evidence: `/app/outputs/relaxation_output`

### Step 3: Static SCF and DOS calculation
- Role: process
- Action: Run spin-polarized self-consistent field calculations for each relaxed slab to obtain converged charge density, atom-projected spin-polarized local density of states (DOS) for surface and bulk-like center atoms, and magnetic moments.
- Evidence: `/app/outputs/scf_dos_raw`

### Step 4: Magnetic moments table
- Role: scored
- Action: Extract magnetic moments (in μB) of all atoms for each termination and lattice constant from the DFT output and write magnetic_moments.csv according to the output contract.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: Columns: termination (Cr or P), lattice_constant_A (5.48 or 5.89), atom (Cr or P), layer (S, S-1, C), magnetic_moment_muB (float). All four termination/lattice combinations must be present.
- Scoring: scored by hidden verifier

### Step 5: DOS Cr-terminated at a_ZB
- Role: scored (load-bearing)
- Action: Extract spin-polarized DOS for the surface Cr atom of the Cr-terminated slab at lattice constant 5.48 Å and write dos_cr_term_aZB.csv.
- Output file: `/app/outputs/dos_cr_term_aZB.csv`
- Format: csv
- Contract: Columns: energy_eV (float, Fermi level at 0.0), dos_up (float, states/eV/atom), dos_down (float). Energy range -2.0 to +4.0 eV.
- Scoring: scored by hidden verifier

### Step 6: DOS Cr-terminated at a_InP
- Role: scored
- Action: Extract spin-polarized DOS for the surface Cr atom of the Cr-terminated slab at lattice constant 5.89 Å and write dos_cr_term_aInP.csv.
- Output file: `/app/outputs/dos_cr_term_aInP.csv`
- Format: csv
- Contract: Columns: energy_eV, dos_up, dos_down. Energy range -2.0 to +4.0 eV.
- Scoring: scored by hidden verifier

### Step 7: DOS P-terminated at a_ZB
- Role: scored
- Action: Extract spin-polarized DOS for the surface P atom of the P-terminated slab at lattice constant 5.48 Å and write dos_p_term_aZB.csv.
- Output file: `/app/outputs/dos_p_term_aZB.csv`
- Format: csv
- Contract: Columns: energy_eV, dos_up, dos_down. Energy range -2.0 to +4.0 eV.
- Scoring: scored by hidden verifier

### Step 8: DOS P-terminated at a_InP
- Role: scored
- Action: Extract spin-polarized DOS for the surface P atom of the P-terminated slab at lattice constant 5.89 Å and write dos_p_term_aInP.csv.
- Output file: `/app/outputs/dos_p_term_aInP.csv`
- Format: csv
- Contract: Columns: energy_eV, dos_up, dos_down. Energy range -2.0 to +4.0 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`
- `/app/outputs/dos_cr_term_aZB.csv`
- `/app/outputs/dos_cr_term_aInP.csv`
- `/app/outputs/dos_p_term_aZB.csv`
- `/app/outputs/dos_p_term_aInP.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetic moments of surface, sub-surface, and bulk-like atoms for both terminations and lattice constants.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `lattice_constant_A`, `atom`, `layer`, `magnetic_moment_muB`
  - `units`:
    - `magnetic_moment_muB`: µB

### dos_cr_term_aZB.csv
- path: `/app/outputs/dos_cr_term_aZB.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DOS of the surface Cr atom at a_ZB; used to recompute minority-spin gap, exchange splitting, and check for surface states.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos_up`, `dos_down`
  - `units`:
    - `energy_eV`: eV (Fermi level at 0.0)
    - `dos_up`: states/eV/atom
    - `dos_down`: states/eV/atom

### dos_cr_term_aInP.csv
- path: `/app/outputs/dos_cr_term_aInP.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DOS of the surface Cr atom at a_InP.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos_up`, `dos_down`
  - `units`:
    - `energy_eV`: eV
    - `dos_up`: states/eV/atom
    - `dos_down`: states/eV/atom

### dos_p_term_aZB.csv
- path: `/app/outputs/dos_p_term_aZB.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DOS of the surface P atom at a_ZB; used to verify metallic character (absence of half-metallicity).
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos_up`, `dos_down`
  - `units`:
    - `energy_eV`: eV
    - `dos_up`: states/eV/atom
    - `dos_down`: states/eV/atom

### dos_p_term_aInP.csv
- path: `/app/outputs/dos_p_term_aInP.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DOS of the surface P atom at a_InP.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos_up`, `dos_down`
  - `units`:
    - `energy_eV`: eV
    - `dos_up`: states/eV/atom
    - `dos_down`: states/eV/atom

Notes: Checker will recompute minority-spin band gap, exchange splitting, and verify presence/absence of surface states from the DOS CSVs. Magnetic moments are compared to hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "lattice_constant_A",
          "atom",
          "layer",
          "magnetic_moment_muB"
        ],
        "units": {
          "magnetic_moment_muB": "µB"
        }
      },
      "description": "Magnetic moments of surface, sub-surface, and bulk-like atoms for both terminations and lattice constants."
    },
    {
      "file": "dos_cr_term_aZB.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos_up",
          "dos_down"
        ],
        "units": {
          "energy_eV": "eV (Fermi level at 0.0)",
          "dos_up": "states/eV/atom",
          "dos_down": "states/eV/atom"
        }
      },
      "description": "DOS of the surface Cr atom at a_ZB; used to recompute minority-spin gap, exchange splitting, and check for surface states."
    },
    {
      "file": "dos_cr_term_aInP.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos_up",
          "dos_down"
        ],
        "units": {
          "energy_eV": "eV",
          "dos_up": "states/eV/atom",
          "dos_down": "states/eV/atom"
        }
      },
      "description": "DOS of the surface Cr atom at a_InP."
    },
    {
      "file": "dos_p_term_aZB.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos_up",
          "dos_down"
        ],
        "units": {
          "energy_eV": "eV",
          "dos_up": "states/eV/atom",
          "dos_down": "states/eV/atom"
        }
      },
      "description": "DOS of the surface P atom at a_ZB; used to verify metallic character (absence of half-metallicity)."
    },
    {
      "file": "dos_p_term_aInP.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos_up",
          "dos_down"
        ],
        "units": {
          "energy_eV": "eV",
          "dos_up": "states/eV/atom",
          "dos_down": "states/eV/atom"
        }
      },
      "description": "DOS of the surface P atom at a_InP."
    }
  ],
  "notes": "Checker will recompute minority-spin band gap, exchange splitting, and verify presence/absence of surface states from the DOS CSVs. Magnetic moments are compared to hidden reference values with appropriate tolerances."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier with hidden reference data. Each of the five scored output files is checked independently. The magnetic moments table is compared to reference values within an appropriate tolerance. Each DOS CSV is post-processed: the minority-spin gap is extracted, surface state presence/absence is assessed, and exchange splitting is computed. The correctness of these derived quantities and of the magnetic moments contributes equally to the final reward. The overall score is the average of the scores across the five artifacts.
