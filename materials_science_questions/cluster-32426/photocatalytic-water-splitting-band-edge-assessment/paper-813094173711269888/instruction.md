# Photocatalytic Water Splitting Band Edge Assessment of Doped ZnS

## Problem background
Zinc sulfide (ZnS) is a semiconductor photocatalyst capable of splitting water into hydrogen and oxygen under UV light. However, its wide band gap (~3.7 eV) prevents it from using visible light, which constitutes the largest fraction of the solar spectrum. Doping ZnS with carbon‑group elements (C, Si, Ge, Sn, Pb) is a proposed strategy to reduce the band gap and shift optical absorption into the visible range. For practical solar‑driven water splitting, the doped materials must simultaneously satisfy two thermodynamic requirements: the conduction band minimum (CBM) must lie above the H⁺/H₂ reduction potential, and the valence band maximum (VBM) must lie below the O₂/H₂O oxidation potential, while the band gap must remain >1.23 eV. This task assesses whether these doped ZnS systems meet those criteria and whether their visible‑light absorption is enhanced relative to pristine ZnS.

## Approach
The assessment is performed with first‑principles density functional theory (DFT) calculations using an open‑source DFT package (Quantum ESPRESSO). Supercells of zinc‑blende ZnS (2×2×2, 64 atoms) are constructed; for each dopant X ∈ {C, Si, Ge, Sn, Pb}, one Zn atom is substituted by X. The workflow proceeds in stages:

- **Geometry optimization**: all supercells (pristine plus five doped) are relaxed using the GGA‑PBE exchange‑correlation functional.
- **Formation energy**: total energies of the optimized supercells and of elemental reference phases in their standard states are computed with PBE; the formation energy of each doped structure is calculated as E_form = E(doped) − E(pristine) − μ_X + μ_Zn, where μ_X and μ_Zn are the chemical potentials of the dopant and Zn in their reference phases.
- **Electronic structure**: a static calculation with the meta‑GGA+MBJ potential is performed for each optimized structure to obtain accurate Kohn‑Sham eigenvalues and wavefunctions.
- **Band gaps**: the energy difference between the VBM and CBM is extracted from the MBJ eigenvalues.
- **Optical absorption**: from the MBJ wavefunctions the imaginary part of the dielectric function is computed via momentum matrix elements, the real part is obtained by Kramers‑Kronig transformation, and the absorption coefficient α(ω) is derived.
- **Band edge positions**: the Mulliken electronegativity χ of each compound is taken as the geometric mean of the atomic Mulliken electronegativities of its constituents. Absolute VBM and CBM energies are then estimated as E_VBM = χ − E_g/2, E_CBM = χ + E_g/2 (vacuum scale). These are converted to the normal hydrogen electrode (NHE) scale by subtracting 4.44 eV.

The computed band edges are compared to the water‑splitting redox potentials (H⁺/H₂ at −4.44 eV vs. vacuum, O₂/H₂O at −5.67 eV).

## Reproduction target
For each of the six systems (pristine ZnS, C@Zn, Si@Zn, Ge@Zn, Sn@Zn, Pb@Zn), compute and write the following outputs:

- `/app/outputs/band_gaps.csv`: system name and band gap in eV.
- `/app/outputs/band_edges.csv`: system name, VBM and CBM energies in both vacuum and NHE scales (eV).
- `/app/outputs/formation_energies.csv`: system name and formation energy in eV (omit pristine, whose formation energy is zero by definition).
- `/app/outputs/absorption_coefficient.csv`: for each system, the absorption coefficient (cm⁻¹) at photon energies 2.0, 2.5, and 3.0 eV.

In addition, verify (as part of your analysis) that every doped system satisfies the thermodynamic water‑splitting requirements: CBM (vacuum) < −4.44 eV and VBM (vacuum) > −5.67 eV, and that the absorption coefficient of each doped system is greater than that of pristine ZnS at each of the three energies. These inequalities constitute the final goal of the reproduction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotential Library: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Optimize atomic positions and lattice parameters of pristine ZnS and five doped supercells (C@Zn, Si@Zn, Ge@Zn, Sn@Zn, Pb@Zn) using the GGA-PBE functional on a 2×2×2 supercell of zinc-blende ZnS (64 atoms) with one Zn substituted by the respective dopant.
- Evidence: `/app/outputs/geo_opt.log`

### Step 2: Formation energy calculation
- Role: scored
- Action: Compute total energies of the optimized pristine and doped supercells and of elemental reference phases in their standard states using the same PBE functional. Calculate formation energies using E_form = E(doped) - E(pristine) - μ_X + μ_Zn.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: system (string), formation_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 3: Meta-GGA+MBJ electronic structure calculation
- Role: process
- Action: Perform static electronic structure calculations on all optimized structures using the meta-GGA+MBJ potential to obtain Kohn-Sham eigenvalues and wavefunctions.
- Evidence: `/app/outputs/mbj_calc.log`

### Step 4: Band gap extraction
- Role: scored
- Action: From the MBJ eigenvalues, extract the energy band gap (eV) for each structure as the difference between the valence band maximum and conduction band minimum.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: system (string), band_gap_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Optical absorption coefficient
- Role: scored (load-bearing)
- Action: Compute the complex dielectric function from the MBJ wavefunctions via momentum matrix elements and Kramers-Kronig transformation, then calculate the absorption coefficient α(ω). Report α for each system at photon energies 2.0, 2.5, and 3.0 eV.
- Output file: `/app/outputs/absorption_coefficient.csv`
- Format: csv
- Contract: system (string), energy_eV (float), absorption_cm1 (float)
- Scoring: scored by hidden verifier

### Step 6: Band edge positions
- Role: scored
- Action: Calculate the Mulliken electronegativity χ of each compound as the geometric mean of atomic Mulliken electronegativities of its constituent elements. Compute absolute VBM and CBM energies (eV, vacuum scale) as E_VBM = χ - E_g/2, E_CBM = χ + E_g/2, where E_g is the band gap from the previous step. Convert to NHE scale by subtracting 4.44 eV (H⁺/H₂ reference).
- Output file: `/app/outputs/band_edges.csv`
- Format: csv
- Contract: system (string), VBM_vacuum (float), CBM_vacuum (float), VBM_NHE (float), CBM_NHE (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/band_gaps.csv`
- `/app/outputs/absorption_coefficient.csv`
- `/app/outputs/band_edges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies for each doped structure.
- schema:
  - `type`: table
  - `required_columns`: `system`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap values for pristine and doped ZnS.
- schema:
  - `type`: table
  - `required_columns`: `system`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

### absorption_coefficient.csv
- path: `/app/outputs/absorption_coefficient.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Absorption coefficient at selected photon energies. For each doped system, at each energy, absorption must exceed that of pristine ZnS.
- schema:
  - `type`: table
  - `required_columns`: `system`, `energy_eV`, `absorption_cm1`
  - `units`:
    - `energy_eV`: eV
    - `absorption_cm1`: cm^-1

### band_edges.csv
- path: `/app/outputs/band_edges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Absolute band edge positions for all structures, in vacuum and NHE scales.
- schema:
  - `type`: table
  - `required_columns`: `system`, `VBM_vacuum`, `CBM_vacuum`, `VBM_NHE`, `CBM_NHE`
  - `units`:
    - `VBM_vacuum`: eV
    - `CBM_vacuum`: eV
    - `VBM_NHE`: eV
    - `CBM_NHE`: eV

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
          "system",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energies for each doped structure."
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Band gap values for pristine and doped ZnS."
    },
    {
      "file": "absorption_coefficient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "energy_eV",
          "absorption_cm1"
        ],
        "units": {
          "energy_eV": "eV",
          "absorption_cm1": "cm^-1"
        }
      },
      "description": "Absorption coefficient at selected photon energies. For each doped system, at each energy, absorption must exceed that of pristine ZnS."
    },
    {
      "file": "band_edges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "VBM_vacuum",
          "CBM_vacuum",
          "VBM_NHE",
          "CBM_NHE"
        ],
        "units": {
          "VBM_vacuum": "eV",
          "CBM_vacuum": "eV",
          "VBM_NHE": "eV",
          "CBM_NHE": "eV"
        }
      },
      "description": "Absolute band edge positions for all structures, in vacuum and NHE scales."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier scores each scored artifact independently and then combines the scores (weighted) into a final reward between 0 and 1.

- **band_gaps.csv**: the verifier compares your band gap values to independently established reference values within a tolerance that accounts for differences in DFT implementations and pseudopotentials.
- **band_edges.csv**: similarly, your VBM and CBM values (both scales) are compared to reference values.
- **formation_energies.csv**: your formation energies are compared to reference values.
- **absorption_coefficient.csv**: the verifier checks that, for each doped system and each of the three energies, the absorption coefficient you report is strictly greater than the pristine ZnS value at that same energy (within a small epsilon). This structural check does not rely on absolute reference values.

Each artifact must follow the format and schema given in the Workflow steps. Producing the correct trends and values (within tolerance) for all artifacts yields a high reward; missing or severely deviating results reduce the score accordingly.
