# Computational Characterization of MgX Clusters (O, S, Se, Te)

## Problem background
Magnesium-chalcogenide (MgX, with X = O, S, Se, Te) clusters are model systems for understanding Mg-based semiconductor nanocrystals. Their structural, vibrational, electronic, and optical properties depend strongly on the chalcogen atom and on the cluster conformation (hexagonal, tetrahedral, or octagonal rings). Characterizing these properties from first principles helps identify stable geometries, bonding trends, and optical behavior, which are essential for designing MgX materials for light-emitting and other optoelectronic applications.

## Approach
The calculations are performed using density functional theory (DFT) at the B3LYP level with the LANL2DZ effective-core-potential basis set. For each of the twelve clusters (Mg3X3 hexagon, Mg4X4-t tetrahedron, Mg4X4-o octagon; X = O, S, Se, Te), initial atomic coordinates are constructed from wurtzite and zinc blende crystal fragments. Each structure is then geometry-optimized and a harmonic vibrational frequency analysis is carried out. From these calculations, total energies, dipole moments, average Mg–X bond lengths, and HOMO–LUMO gaps are extracted. Natural Bond Orbital (NBO) analysis provides Wiberg bond indices (WBI) that quantify the bonding strength between Mg and X. Finally, time-dependent DFT (TDDFT) single-point calculations are performed at the same level of theory, using an implicit water solvent model (dielectric constant 78.39, nstates=10), to obtain the dominant optical absorption wavelength. The entire workflow is implemented with an open-source quantum chemistry package such as ORCA.

## Reproduction target
The goal is to reproduce the following computed properties for all twelve MgX clusters: lowest vibrational frequency (cm⁻¹), total energy (Hartree), dipole moment (Debye), average Mg–X bond length (Å), HOMO–LUMO gap (eV), dominant absorption wavelength in water (nm), and Wiberg bond index (dimensionless). All results must be collected into a single CSV file named `all_cluster_properties.csv` with one row per cluster and columns `cluster_name`, `freq_cm1`, `energy_au`, `dipole_moment_debye`, `bond_length_ang`, `homo_lumo_gap_eV`, `absorption_nm`, `wbi`. All numeric fields must be filled with values obtained from your own DFT calculations. The CSV will be compared against hidden reference values; correctness and systematic trends in your data determine success.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de
- LANL2DZ basis set: basis-set-exchange
- Water solvent implicit model parameter

## Workflow steps

### Step 1: Construct initial geometries
- Role: process
- Action: Construct the atomic coordinates for the twelve MgX clusters (Mg3X3 hexagon, Mg4X4-t tetrahedron, Mg4X4-o octagon; X=O, S, Se, Te) based on wurtzite and zinc blende crystal structure fragments as described in the method.
- Evidence: `/app/outputs/initial_geometries.txt`

### Step 2: DFT geometry optimization and frequency calculation
- Role: process
- Action: For each cluster, perform geometry optimization and harmonic vibrational frequency analysis at the DFT/B3LYP/LANL2DZ level using an open-source quantum chemistry package (e.g., ORCA). Extract total energies, lowest vibrational frequencies, dipole moments, average Mg-X bond lengths, and HOMO-LUMO gaps.
- Evidence: none

### Step 3: NBO analysis for Wiberg bond indices
- Role: process
- Action: Perform Natural Bond Orbital (NBO) population analysis on the optimized geometries to compute Wiberg bond indices (WBI) between Mg and the chalcogen atom.
- Evidence: none

### Step 4: TDDFT absorption calculation in water
- Role: process
- Action: For each optimized cluster, run a TDDFT single-point calculation with the same functional/basis set, using implicit water solvent (SCRF, dielectric=78.39, nstates=10). Extract the dominant absorption wavelength (nm) corresponding to the strongest low-energy transition.
- Evidence: none

### Step 5: Compile property table
- Role: scored (load-bearing)
- Action: Gather the computed quantities from the previous steps and produce a CSV file with one row per cluster (12 rows). Columns: cluster_name, freq_cm1, energy_au, dipole_moment_debye, bond_length_ang, homo_lumo_gap_eV, absorption_nm, wbi. All numeric fields must be filled.
- Output file: `/app/outputs/all_cluster_properties.csv`
- Format: csv
- Contract: 12 rows, columns: cluster_name (str, must be one of: Mg3O3, Mg3S3, Mg3Se3, Mg3Te3, Mg4O4_t, Mg4S4_t, Mg4Se4_t, Mg4Te4_t, Mg4O4_o, Mg4S4_o, Mg4Se4_o, Mg4Te4_o), freq_cm1 (float), energy_au (float), dipole_moment_debye (float), bond_length_ang (float), homo_lumo_gap_eV (float), absorption_nm (float), wbi (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/all_cluster_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### all_cluster_properties.csv
- path: `/app/outputs/all_cluster_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing computed properties for all 12 MgX clusters, one row per cluster. The cluster_name must match one of the allowed values exactly. The hidden checker will compare each numeric field to the paper's reference values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `cluster_name`, `freq_cm1`, `energy_au`, `dipole_moment_debye`, `bond_length_ang`, `homo_lumo_gap_eV`, `absorption_nm`, `wbi`
  - `units`:
    - `freq_cm1`: cm^{-1}
    - `energy_au`: Hartree (a.u.)
    - `dipole_moment_debye`: Debye
    - `bond_length_ang`: Angstrom
    - `homo_lumo_gap_eV`: eV
    - `absorption_nm`: nm
    - `wbi`: dimensionless
  - `cluster_name_allowed_values`: `Mg3O3`, `Mg3S3`, `Mg3Se3`, `Mg3Te3`, `Mg4O4_t`, `Mg4S4_t`, `Mg4Se4_t`, `Mg4Te4_t`, `Mg4O4_o`, `Mg4S4_o`, `Mg4Se4_o`, `Mg4Te4_o`

Notes: The checker also verifies the qualitative trend that absorption wavelengths increase in the order MgS < MgSe < MgTe for each conformer series.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "all_cluster_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_name",
          "freq_cm1",
          "energy_au",
          "dipole_moment_debye",
          "bond_length_ang",
          "homo_lumo_gap_eV",
          "absorption_nm",
          "wbi"
        ],
        "units": {
          "freq_cm1": "cm^{-1}",
          "energy_au": "Hartree (a.u.)",
          "dipole_moment_debye": "Debye",
          "bond_length_ang": "Angstrom",
          "homo_lumo_gap_eV": "eV",
          "absorption_nm": "nm",
          "wbi": "dimensionless"
        },
        "cluster_name_allowed_values": [
          "Mg3O3",
          "Mg3S3",
          "Mg3Se3",
          "Mg3Te3",
          "Mg4O4_t",
          "Mg4S4_t",
          "Mg4Se4_t",
          "Mg4Te4_t",
          "Mg4O4_o",
          "Mg4S4_o",
          "Mg4Se4_o",
          "Mg4Te4_o"
        ]
      },
      "description": "CSV containing computed properties for all 12 MgX clusters, one row per cluster. The cluster_name must match one of the allowed values exactly. The hidden checker will compare each numeric field to the paper's reference values with tolerances."
    }
  ],
  "notes": "The checker also verifies the qualitative trend that absorption wavelengths increase in the order MgS < MgSe < MgTe for each conformer series."
}
```

## How you are scored
A hidden verifier reads your CSV and compares each numeric column against reference values derived from the original study. It also checks that, within each conformer series (hexagon, tetrahedron, octagon), the absorption wavelengths follow a consistent monotonic trend across the chalcogen atoms. The final reward is a weighted combination of per-column numerical agreement and trend correctness. The reward is monotonic in quality: better agreement with the reference values and correct trends yield higher scores; there is no penalty for producing results that are more accurate than the reference. Legitimate differences due to the choice of quantum chemistry package are tolerated, so focus on correctly implementing the specified computational method rather than attempting to reproduce exact digits.
