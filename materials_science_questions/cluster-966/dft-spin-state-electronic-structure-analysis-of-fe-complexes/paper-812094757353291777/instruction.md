# DFT Spin-Density and TDDFT Analysis of Diethynylaryl-Bridged Fe Complexes

## Problem background
Bimetallic organometallic complexes with conjugated bridges are studied for their ability to transmit electronic information between metal centers, a property relevant to molecular wires and optoelectronic materials. This work investigates diethynylaryl-bridged iron complexes containing either CpFe(PH3)2 or CpFe(CO)2 terminal units, to understand how the ancillary ligands (donor vs. acceptor) and the aryl spacer (phenyl vs. phenoxy) influence the unpaired spin distribution and the presence of low-energy charge-transfer absorptions in the one-electron-oxidized radical cations.

## Approach
Density functional theory (DFT) at the B3LYP/LANL2DZ mixed basis level is used to optimize the geometries of the neutral complexes and their radical cations without symmetry constraints. Starting from the optimized cation geometries, Mulliken spin density populations on the iron atoms and the bridging ligand are computed, and time-dependent DFT (TDDFT) with an augmented basis on the light atoms (6-31+G*) is applied to obtain the lowest vertical excitation energies and oscillator strengths. The analysis compares three model radical cations: a PH3-substituted phenylene-bridged complex, a CO-substituted phenylene-bridged complex, and a CO-substituted dimethoxy-phenylene-bridged complex.

## Reproduction target
Construct, geometry-optimize, and compute properties for the three radical cations (PH3-7d+, 6d+, CH3O-6e+) as specified in the workflow steps. Write the computed Mulliken spin densities on the two iron atoms per cation, the lowest TDDFT vertical excitation energy and its oscillator strength into computed_results.json. Additionally, archive all optimized geometries (neutral and cation states) into optimized_geometries.tar.gz. The collected data should allow a comparison of the spin density distribution and the excitation energies between the PH3 and CO ancillary ligand sets. Determine the relative trend in spin density and excitation energy between the models.

## Assets

- ORCA quantum chemistry package (or equivalent open-source DFT code): https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Build model complex structures
- Role: process
- Action: Construct initial 3D coordinates for three neutral model complexes: PH3-7d (1,4-phenylene bridge, PH3 ligands), 6d (1,4-phenylene bridge, CO ligands), and CH3O-6e (2,5-dimethoxy-1,4-phenylene bridge, CO ligands), using the structural descriptions in the paper (CpFe(PH3)2 and CpFe(CO)2 units, bridging ligands C6H4, C6H2(OCH3)2).
- Evidence: none

### Step 2: Optimize geometry of neutral complexes
- Role: process
- Action: Perform DFT geometry optimization at the B3LYP/LANL2DZ,6-31G** level without symmetry constraints for each neutral model complex (PH3-7d, 6d, CH3O-6e). Save the optimized structures for later steps.
- Evidence: none

### Step 3: Optimize geometry of radical cation complexes
- Role: process
- Action: Starting from the optimized neutral geometries, perform DFT geometry optimization for the corresponding one-electron-oxidized radical cations (PH3-7d+, 6d+, CH3O-6e+) at the same level of theory.
- Evidence: none

### Step 4: Compute spin densities and TDDFT excitation energies
- Role: scored (load-bearing)
- Action: From the optimized cation structures, compute Mulliken spin density distributions and run TDDFT calculations (B3LYP/LANL2DZ,6-31+G*) to obtain the lowest vertical excitation energy (in cm⁻¹) and oscillator strength. Write the results to computed_results.json.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: {
  "PH3-7d+": {
    "spin_density_Fe1": float,
    "spin_density_Fe2": float,
    "excitation_energy_cm-1": float,
    "oscillator_strength": float
  },
  "6d+": {
    "spin_density_Fe1": float,
    "spin_density_Fe2": float,
    "excitation_energy_cm-1": float,
    "oscillator_strength": float
  },
  "CH3O-6e+": {
    "spin_density_Fe1": float,
    "spin_density_Fe2": float,
    "excitation_energy_cm-1": float,
    "oscillator_strength": float
  },
  "metadata": {
    "code": "string",
    "functional": "B3LYP",
    "basis_set": "LANL2DZ,6-31G** for geometry, 6-31+G* for TDDFT",
    "remarks": "Spin densities from Mulliken population analysis."
  }
}
- Scoring: scored by hidden verifier

### Step 5: Archive optimized geometries
- Role: scored
- Action: Package all optimized geometries (neutral and cation) of the three model complexes into a single tar.gz archive.
- Output file: `/app/outputs/optimized_geometries.tar.gz`
- Format: other
- Contract: tar.gz archive with subdirectories 'neutral' and 'cation', each containing files like PH3-7d_neutral.xyz, PH3-7d_cation.xyz, 6d_neutral.xyz, 6d_cation.xyz, CH3O-6e_neutral.xyz, CH3O-6e_cation.xyz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`
- `/app/outputs/optimized_geometries.tar.gz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed Mulliken spin densities on the two iron atoms and the lowest TDDFT vertical excitation energy (cm⁻¹) with oscillator strength for the three model radical cations PH3-7d+, 6d+, and CH3O-6e+.
- schema:
  - `type`: object
  - `required`:
    - `PH3-7d+`:
      - `spin_density_Fe1`: float
      - `spin_density_Fe2`: float
      - `excitation_energy_cm-1`: float
      - `oscillator_strength`: float
    - `6d+`:
      - `spin_density_Fe1`: float
      - `spin_density_Fe2`: float
      - `excitation_energy_cm-1`: float
      - `oscillator_strength`: float
    - `CH3O-6e+`:
      - `spin_density_Fe1`: float
      - `spin_density_Fe2`: float
      - `excitation_energy_cm-1`: float
      - `oscillator_strength`: float
    - `metadata`:
      - `code`: string
      - `functional`: string
      - `basis_set`: string
      - `remarks`: string

### optimized_geometries.tar.gz
- path: `/app/outputs/optimized_geometries.tar.gz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Archive of DFT-optimized geometries (XYZ format) for the neutral and radical cation states of PH3-7d, 6d, and CH3O-6e. The archive must contain the expected set of files with proper naming.
- schema:
  - `type`: other
  - `description`: tar.gz archive containing expected XYZ files for all neutral and cation complexes.

Notes: The main scored target is computed_results.json; the geometry archive provides supporting structural evidence. All calculations must use B3LYP functional with LANL2DZ effective core potential on Fe and 6-31G** (geometry) / 6-31+G* (TDDFT) basis sets for other atoms. Spin densities are obtained from Mulliken population analysis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "PH3-7d+": {
            "spin_density_Fe1": "float",
            "spin_density_Fe2": "float",
            "excitation_energy_cm-1": "float",
            "oscillator_strength": "float"
          },
          "6d+": {
            "spin_density_Fe1": "float",
            "spin_density_Fe2": "float",
            "excitation_energy_cm-1": "float",
            "oscillator_strength": "float"
          },
          "CH3O-6e+": {
            "spin_density_Fe1": "float",
            "spin_density_Fe2": "float",
            "excitation_energy_cm-1": "float",
            "oscillator_strength": "float"
          },
          "metadata": {
            "code": "string",
            "functional": "string",
            "basis_set": "string",
            "remarks": "string"
          }
        }
      },
      "description": "Computed Mulliken spin densities on the two iron atoms and the lowest TDDFT vertical excitation energy (cm⁻¹) with oscillator strength for the three model radical cations PH3-7d+, 6d+, and CH3O-6e+."
    },
    {
      "file": "optimized_geometries.tar.gz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "description": "tar.gz archive containing expected XYZ files for all neutral and cation complexes."
      },
      "description": "Archive of DFT-optimized geometries (XYZ format) for the neutral and radical cation states of PH3-7d, 6d, and CH3O-6e. The archive must contain the expected set of files with proper naming."
    }
  ],
  "notes": "The main scored target is computed_results.json; the geometry archive provides supporting structural evidence. All calculations must use B3LYP functional with LANL2DZ effective core potential on Fe and 6-31G** (geometry) / 6-31+G* (TDDFT) basis sets for other atoms. Spin densities are obtained from Mulliken population analysis."
}
```

## How you are scored
A hidden verifier evaluates each required output separately and combines the scores into a final reward. The verifier reads the contents of computed_results.json and checks the structure and presence of expected files in optimized_geometries.tar.gz. Numerical values are compared against reference criteria derived from the original study, including acceptable spreads and consistency between the complexes (the agent does not need to know the exact thresholds). Determine the relative trend in spin density and excitation energy between the models. The main scored artifact is the JSON file; the geometry archive contributes a smaller structural audit component. The verifier’s scoring function is monotonic in quality: better agreement and correct trends earn higher scores, and meeting or exceeding the reference standard yields full credit.
