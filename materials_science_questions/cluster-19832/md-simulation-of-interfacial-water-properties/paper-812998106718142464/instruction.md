# Compute PVDF–Water Interaction Energy per Area for Crystal and Amorphous Surfaces

## Problem background
Poly(vinylidene fluoride) (PVDF) is a semi‑crystalline polymer widely used in separation membranes and other applications.  The wettability of PVDF surfaces, often characterized by water contact angle, depends on the microscopic surface structure—specifically, whether the surface is crystalline or amorphous.  Understanding this structure–wettability relationship at the molecular level can guide membrane design.  This task investigates the energetic basis of the wettability difference by computing the interaction energy between water and PVDF for both crystalline and amorphous surfaces using planar slab molecular dynamics simulations.

## Approach
This reproduction uses all‑atom molecular dynamics (MD) simulations with the GROMACS engine, the Lachet et al. OPLS‑type force field for PVDF, and the TIP4P/2005 water model.  The workflow starts from scratch: build an α‑phase crystalline PVDF (020) surface using optimized lattice constants and an amorphous PVDF surface via a melt‑quench protocol.  For each surface, a simulation box is constructed containing a PVDF film, an approximately 7 nm thick water layer, and a vacuum region to create a planar PVDF–water interface.  NVT MD simulations at 298.15 K relax the interfaces and allow the system to reach a stable state.  From the final part of the trajectories, the non‑bonded interaction energies (Lennard‑Jones and Coulombic components) are computed between the PVDF and water molecules using a cutoff scheme, normalized by the interfacial area, and compared.  The key comparison is the total (LJ + Coulomb) interaction energy per area between the two surface types.

## Reproduction target
Compute the PVDF–water interaction energy per interfacial area—separated into Lennard‑Jones, Coulombic, and total contributions—for both the α‑phase crystalline PVDF (020) surface and an amorphous PVDF surface from planar slab MD simulations.  Report the results as a CSV file with columns for surface type, interaction type, value (in kJ mol⁻¹ nm⁻²), and uncertainty.  Verify which of the two surfaces exhibits a more negative total (LJ + Coulomb) interaction energy, indicating more favorable PVDF–water interactions.

## Assets

- GROMACS: https://manual.gromacs.org/current/
- Packmol: https://github.com/m3g/packmol
- Lachet et al. PVDF force field: 10.1021/jp507807b
- TIP4P/2005 water model: gromacs

## Workflow steps

### Step 1: Prepare initial configuration of PVDF/water/vacuum slab systems
- Role: process
- Action: Construct the α‑crystal PVDF (020) surface and the amorphous PVDF surface using the Lachet et al. force field, the specified unit cell parameters (a=0.4985 nm, b=0.964 nm, c=0.482 nm), and the melt‑quench protocol described in the paper. For each surface, create a rectangular simulation box containing a PVDF film and an ~7 nm thick water layer, terminated by a vacuum region, as described in the methodology. Generate GROMACS topology and coordinate files for both systems.
- Evidence: `/app/outputs/initial_slab_systems.md`

### Step 2: Run NVT MD simulation of slab interfaces
- Role: process
- Action: Using GROMACS, perform NVT simulations for both the crystal and amorphous slab systems at T=298.15 K. Use leap‑frog integrator with dt=2 fs, Nosé‑Hoover thermostat (τ_T=1 ps), LJ switch from 1.0 to 1.2 nm cutoff, PME electrostatics (real‑space cutoff 1.2 nm, 6th‑order B‑spline, grid spacing ≤0.12 nm), and bond constraints (SETTLE for water, LINCS for PVDF). Run each system for at least 20 ns of production, with the final 15 ns used for analysis. Ensure temperature and total energy are stable.
- Evidence: `/app/outputs/md_slab_runs.log`

### Step 3: Compute PVDF–water interaction energy per area
- Role: scored
- Action: From the final 5 ns of each slab trajectory, calculate the non‑bonded interaction energy between PVDF and water molecules using a 2.0 nm cutoff (LJ and Coulombic contributions computed directly with the cutoff scheme). Normalize by the interfacial area (the X‑Y cross‑sectional area of the simulation box). Report the LJ, Coulombic, and total (LJ+Coulomb) energies per area for both the crystal and amorphous surfaces, including the uncertainty estimated over the analysis segment. Save the results in a CSV file.
- Output file: `/app/outputs/step_01_pvdf_water_interaction_energies.csv`
- Format: csv
- Contract: surface (string: crystal or amorphous), interaction_type (LJ, Coulomb, total), value (kJ mol−1 nm−2), uncertainty (kJ mol−1 nm−2)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_pvdf_water_interaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_pvdf_water_interaction_energies.csv
- path: `/app/outputs/step_01_pvdf_water_interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Per‑area PVDF–water interaction energies (Lennard‑Jones, Coulomb, and total) for the crystalline and amorphous PVDF surfaces. The checker verifies that the amorphous total energy is more negative (more favourable) than the crystal total, and that the individual components are within a tolerance of the hidden reference values from the paper’s Table 3.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `interaction_type`, `value`, `uncertainty`
  - `columns`:
    - `surface`:
      - `type`: string
      - `values`: `crystal`, `amorphous`
    - `interaction_type`:
      - `type`: string
      - `values`: `LJ`, `Coulomb`, `total`
    - `value`:
      - `type`: number
      - `unit`: kJ mol^{-1} nm^{-2}
    - `uncertainty`:
      - `type`: number
      - `unit`: kJ mol^{-1} nm^{-2}

Notes: Only the slab interaction energy is reproduced. Droplet contact angle simulations and detailed structural/electrostatic analyses are excluded due to computational cost for a minimal reproduction task. The target trend (amorphous more negative) is scored via threshold_or_better; absolute values are compared to reference with a tolerance window.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_pvdf_water_interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "interaction_type",
          "value",
          "uncertainty"
        ],
        "columns": {
          "surface": {
            "type": "string",
            "values": [
              "crystal",
              "amorphous"
            ]
          },
          "interaction_type": {
            "type": "string",
            "values": [
              "LJ",
              "Coulomb",
              "total"
            ]
          },
          "value": {
            "type": "number",
            "unit": "kJ mol^{-1} nm^{-2}"
          },
          "uncertainty": {
            "type": "number",
            "unit": "kJ mol^{-1} nm^{-2}"
          }
        }
      },
      "description": "Per‑area PVDF–water interaction energies (Lennard‑Jones, Coulomb, and total) for the crystalline and amorphous PVDF surfaces. The checker verifies that the amorphous total energy is more negative (more favourable) than the crystal total, and that the individual components are within a tolerance of the hidden reference values from the paper’s Table 3."
    }
  ],
  "notes": "Only the slab interaction energy is reproduced. Droplet contact angle simulations and detailed structural/electrostatic analyses are excluded due to computational cost for a minimal reproduction task. The target trend (amorphous more negative) is scored via threshold_or_better; absolute values are compared to reference with a tolerance window."
}
```

## How you are scored
A hidden verifier reads the CSV you produce and compares the reported interaction energies per area (LJ, Coulomb, and total) for both surfaces to hidden reference values and an undisclosed physical trend.  The exact scoring criteria and weights are hidden; producing a valid CSV following the output contract and executing all workflow steps is required to obtain a non-zero reward.  The verifier only inspects the final CSV but the intermediate evidence documents your process.
