# First-Principles Evaluation of Ternary Cu-Sn-S Photovoltaic Absorbers

## Problem background
Next-generation thin-film solar cells require earth-abundant absorber materials. This study evaluates ternary Cu-Sn-S compounds using first-principles calculations to assess their potential as photovoltaic absorbers. The materials under investigation are Cu4SnS4, Cu2SnS3, and Cu4Sn7S16, all with Cu in a +1 oxidation state. Their suitability depends on several interconnected properties: thermodynamic stability relative to competing phases, the nature and energy of the band gaps, optical absorption strength, and the behavior of native point defects — particularly Cu vacancies, which can control p-type conductivity or pin the Fermi level. A comprehensive computational evaluation of these properties will identify which compound has the most favourable profile for a solar absorber.

## Approach
The evaluation is carried out through a sequence of first-principles calculations applied to the three ternary compounds as well as reference elemental and binary phases. The workflow combines several established methods:

- **DFT+U relaxations**: Geometry optimizations and total energies are obtained using the PBE functional with an on-site Coulomb correction (U=5 eV) on Cu d states.
- **Thermodynamic stability**: FERE elemental reference energies are applied to the DFT+U total energies to compute accurate formation enthalpies (eV/atom). From these, the relative stability windows and competition with secondary phases are determined.
- **GW band structure**: Quasiparticle band energies and the dielectric function are calculated in the GW approximation, starting from the DFT+U wavefunctions. An on-site potential shift is applied to Cu d states to correct for overestimated d-orbital energies in GW.
- **Optical absorption**: Absorption coefficients are derived from the GW dielectric function within the independent-particle approximation.
- **Defect supercell calculations**: Supercells containing ~100 atoms are constructed for each ternary compound, Cu vacancies are introduced in different charge states, and DFT+U total energies are computed. GW-corrected band-edge positions and finite-size corrections (electrostatic image charge and band filling) are applied to obtain accurate defect formation energies. These are then used to determine Fermi-level pinning energy ranges.

The procedure must be repeated for Cu4SnS4, Cu2SnS3, and Cu4Sn7S16. The comparison across these three materials — covering stability, electronic structure, optical response, and defect physics — reveals which candidate is the most robust and thus the most promising for photovoltaic applications.

## Reproduction target
Reproduce the key computational results that underpin the material evaluation: (1) relative thermodynamic stability via formation enthalpies, (2) GW quasiparticle band gaps (direct and indirect), (3) optical absorption spectra, and (4) Cu-vacancy defect formation energies and the resulting Fermi-level pinning energy ranges for Cu4SnS4, Cu2SnS3, and Cu4Sn7S16.

You must execute the workflow described in the steps below, using any DFT code that supports PBE+U and any compatible GW implementation. Assemble the crystal structures from public databases (ICSD, Materials Project, COD, etc.) and apply the required FERE corrections. Write the final results to the following CSV files:

- `step_01_stability.csv` — formation enthalpies per atom.
- `step_02_defect_formation.csv` — Cu-vacancy formation energies and pinning energy ranges.
- `step_03_band_gaps.csv` — quasiparticle band gaps.
- `step_04_absorption_spectra.csv` — optical absorption coefficients vs photon energy.

Do not try to match exact numbers from the literature; run the calculations faithfully with your chosen codes and report the computed quantities.

## Assets

- DFT code (Quantum ESPRESSO or VASP): https://www.quantum-espresso.org/
- GW calculation code (BerkeleyGW, YAMBO, etc.): https://berkeleygw.org/
- PBE pseudopotentials / PAW datasets
- FERE reference energetics: 10.1103/PhysRevB.85.115104
- Crystal structures for Cu-Sn-S compounds and reference phases

## Workflow steps

### Step 1: DFT+U bulk relaxations and total energies
- Role: process
- Action: Perform DFT+U (PBE+U, U=5 eV on Cu d) geometry relaxations and total energy calculations for all starting crystal structures: Cu4SnS4, Cu2SnS3, Cu4Sn7S16, and necessary reference phases (elements and binaries).
- Evidence: `/app/outputs/dft_relaxation.log`

### Step 2: Thermodynamic stability analysis
- Role: scored
- Action: Using DFT+U total energies and FERE reference corrections, compute formation enthalpies (eV/atom) for the ternary compounds and relevant reference phases. Output the formation enthalpies.
- Output file: `/app/outputs/step_01_stability.csv`
- Format: csv
- Contract: CSV with columns: compound (string), formation_enthalpy_eV_per_atom (float).
- Scoring: scored by hidden verifier

### Step 3: GW quasiparticle band structure
- Role: process
- Action: Starting from DFT+U wavefunctions, perform GW calculations (with on-site potential V_d = -2.8 eV on Cu d states) to obtain quasiparticle band energies and the dielectric function.
- Evidence: `/app/outputs/gw_calculation.log`

### Step 4: Band gaps
- Role: scored (load-bearing)
- Action: Extract quasiparticle band gaps from GW calculations. For each compound, report the fundamental (indirect if applicable) and direct gap values.
- Output file: `/app/outputs/step_03_band_gaps.csv`
- Format: csv
- Contract: CSV with columns: compound (string), gap_type (string, 'direct' or 'indirect'), quasiparticle_gap_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Optical absorption spectra
- Role: scored
- Action: Compute optical absorption coefficients from the GW dielectric function (independent-particle approximation) for each compound over the photon energy range 0–3 eV.
- Output file: `/app/outputs/step_04_absorption_spectra.csv`
- Format: csv
- Contract: CSV with columns: compound (string), energy_eV (float), absorption_coefficient_cm-1 (float).
- Scoring: scored by hidden verifier

### Step 6: Defect supercell calculations
- Role: process
- Action: Construct supercells (~100 atoms) for each compound, introduce Cu vacancies, and perform DFT+U calculations for relevant charge states, applying GW-corrected band-edge positions and finite-size corrections (electrostatic image charge, band filling).
- Evidence: `/app/outputs/defect_calculations.log`

### Step 7: Defect formation energies and pinning levels
- Role: scored
- Action: From the defect supercell calculations, determine Cu-vacancy formation energies for each charge state and compute Fermi-level pinning energy ranges. Output the formation energies and the pinning energy ranges.
- Output file: `/app/outputs/step_02_defect_formation.csv`
- Format: csv
- Contract: CSV with columns: compound (string), charge_state (integer), formation_energy_eV (float). Additionally includes rows with compound='E_F_pin_range' and formation_energy_eV representing the pinning energy range.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stability.csv`
- `/app/outputs/step_02_defect_formation.csv`
- `/app/outputs/step_03_band_gaps.csv`
- `/app/outputs/step_04_absorption_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stability.csv
- path: `/app/outputs/step_01_stability.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Formation enthalpies per atom for Cu4SnS4, Cu2SnS3, Cu4Sn7S16, and necessary reference phases.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `formation_enthalpy_eV_per_atom`

### step_02_defect_formation.csv
- path: `/app/outputs/step_02_defect_formation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Cu vacancy formation energies for each charge state, plus Fermi-level pinning energy range rows (compound='E_F_pin_range').
- schema:
  - `type`: table
  - `required_columns`: `compound`, `charge_state`, `formation_energy_eV`

### step_03_band_gaps.csv
- path: `/app/outputs/step_03_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: GW quasiparticle band gaps (direct and indirect) for Cu4SnS4, Cu2SnS3, Cu4Sn7S16.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `gap_type`, `quasiparticle_gap_eV`

### step_04_absorption_spectra.csv
- path: `/app/outputs/step_04_absorption_spectra.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Optical absorption coefficients vs photon energy (0–3 eV) for the three Cu-Sn-S compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `energy_eV`, `absorption_coefficient_cm-1`

Notes: Scoring of stability and defect energies will recompute derived quantities (stability windows, pinning levels) and compare to paper trends. Band gaps are compared to paper-reported values with allowed tolerance. Absorption spectra are scored via structural/trend checks (onset, ordering).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "formation_enthalpy_eV_per_atom"
        ]
      },
      "description": "Formation enthalpies per atom for Cu4SnS4, Cu2SnS3, Cu4Sn7S16, and necessary reference phases."
    },
    {
      "file": "step_02_defect_formation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "charge_state",
          "formation_energy_eV"
        ]
      },
      "description": "Cu vacancy formation energies for each charge state, plus Fermi-level pinning energy range rows (compound='E_F_pin_range')."
    },
    {
      "file": "step_03_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "gap_type",
          "quasiparticle_gap_eV"
        ]
      },
      "description": "GW quasiparticle band gaps (direct and indirect) for Cu4SnS4, Cu2SnS3, Cu4Sn7S16."
    },
    {
      "file": "step_04_absorption_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "energy_eV",
          "absorption_coefficient_cm-1"
        ]
      },
      "description": "Optical absorption coefficients vs photon energy (0–3 eV) for the three Cu-Sn-S compounds."
    }
  ],
  "notes": "Scoring of stability and defect energies will recompute derived quantities (stability windows, pinning levels) and compare to paper trends. Band gaps are compared to paper-reported values with allowed tolerance. Absorption spectra are scored via structural/trend checks (onset, ordering)."
}
```

## How you are scored
A hidden verifier will independently inspect each scored output file and compute a reward from 0 to 1 that reflects the overall quality of the reproduction. The four scored stages carry different weights, with the band gaps and stability carrying the most weight.

The verifier may recompute derived quantities (such as stability windows from formation enthalpies, or pinning levels from defect formation energies) and compare your results to reference trends and values. Comparisons account for the fact that different codes and pseudopotentials can shift absolute numbers, so scoring places emphasis on consistent relative trends (e.g., which compound has the widest stability window, whether a band gap is direct or indirect, the ordering of pinning energies) as well as on the magnitudes within realistic tolerances.

Simply reporting paper numbers without genuine computation will not be rewarded; the verifier is designed to verify that the workflow was actually executed. The burden is on you to produce a complete, self-consistent set of results from your chosen implementation.
