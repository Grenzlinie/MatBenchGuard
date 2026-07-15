# DFT Geometry and Adsorption of Doped Zeolites

## Problem background
Zeolites are nanoporous crystalline silicates with wide application in catalysis, adsorption, and ion exchange. Substituting bridging oxygen atoms with methylene (CH₂) or amine (NH) groups can alter the structural and chemical properties of these frameworks. Density functional theory (DFT) can be used to probe whether such doped zeolites are mechanically stable, to quantify the residual strain introduced by the substitution, and to assess whether the amine impurity enhances the Lewis base strength of the material. The target of this task is to compute the polymer reference angles, the relaxed geometries of pristine and singly doped sodalites, the defect strain energies, and the BF₃ adsorption energies that together characterise the stability and basicity of the doped frameworks.

## Approach
The reproduction employs plane-wave pseudopotential DFT calculations within the local density approximation (LDA). All structures—pristine and doped zeolites, reference chain polymers, and BF₃ adsorption complexes—are fully geometry-optimised using an open-source DFT code. Strain energies are evaluated using a polymer-reference method: the total substitution energy per defect (doped zeolite minus pristine zeolite) is corrected by subtracting the chemical substitution energy obtained from analogous chain polymers, which isolates the lattice strain. Lewis basicity is assessed by computing the adsorption energy of BF₃ at a Si–O–Si site in pristine sodalite and at a Si–NH–Si site in NH-doped sodalite, defined as the energy of the complex minus the sum of the bare zeolite and isolated BF₃ energies. The workflow progresses from building initial atomic coordinates, through DFT geometry optimisations, to extraction of target structural parameters and energies.

## Reproduction target
Using DFT-LDA plane-wave pseudopotential calculations, produce the following quantities and write them to CSV files:

1. **Polymer reference angles and repeat lengths** (step_01_polymer_angles.csv): the relaxed Si–O–Si angles for the (SiO)₂(OH)₄ polymer, the Si–N–Si angle for (SiNH)(SiO)(OH)₄, the Si–C–Si angle for (SiCH₂)(SiO)(OH)₄, and the corresponding Si–O–Si angles of the doped polymers, along with the repeat length of each chain.

2. **Geometry of pristine and doped sodalites** (step_02_doped_geometries.csv): for pristine OXY-SOD (full relaxation), and for 1CH₂-SOD and 1NH-SOD under both internal‑only and full lattice+internal relaxation, report the lattice parameter a (Å), the Si–X–Si (X = O, C, N) angle, and the Si–C or Si–N bond length (where applicable).

3. **Strain energy per defect** (step_03_strain_energy.csv): for 1CH₂-SOD (full relaxation) and 1NH-SOD (full relaxation), compute the strain energy per impurity using the polymer-reference method.

4. **BF₃ adsorption energies** (step_04_adsorption_energy.csv): compute the adsorption energy for BF₃ at a Si–O–Si site in OXY-SOD and at a Si–NH–Si site in 1NH-SOD, defined as ΔE = E(complex) − E(zeolite) − E(isolated BF₃).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency LDA pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- All-silica sodalite crystallographic data (space group I-43m, a=8.83 Å)

## Workflow steps

### Step 1: Structure generation for all model systems
- Role: process
- Action: Build initial atomic coordinates and supercells for pristine sodalite (OXY-SOD), singly doped sodalites (1CH2-SOD, 1NH-SOD), and the three reference chain polymers ((SiO)₂(OH)₄, (SiNH)(SiO)(OH)₄, (SiCH₂)(SiO)(OH)₄) using crystallographic data and standard bond lengths.
- Evidence: `/app/outputs/structure_log.txt`

### Step 2: Polymer reference optimization and angle extraction
- Role: scored
- Action: Perform DFT geometry optimizations on the three polymer reference systems using Quantum ESPRESSO with LDA and the specified pseudopotentials. From the relaxed structures, extract the Si-O-Si (two values), Si-N-Si, and Si-C-Si three-body angles and the polymer repeat lengths. Write these values to step_01_polymer_angles.csv.
- Output file: `/app/outputs/step_01_polymer_angles.csv`
- Format: csv
- Contract: Columns: polymer_name, angle_type, angle_value_deg, repeat_length_A. Rows correspond to (SiO)₂(OH)₄ Si-O-Si angles (two), (SiNH)(SiO)(OH)₄ Si-N-Si, (SiCH₂)(SiO)(OH)₄ Si-C-Si, and the Si-O-Si angles of the doped polymers.
- Scoring: scored by hidden verifier

### Step 3: Geometry optimization of pristine and doped sodalites
- Role: scored
- Action: Using the same DFT protocol, run full geometry optimizations for pristine OXY-SOD (full relaxation), 1CH2-SOD (internal‑only and full relaxation), and 1NH-SOD (internal‑only and full relaxation). For each system and relaxation type, extract the lattice parameter a (in Å), the Si-X-Si angle, and the Si-C or Si-N bond lengths. Write the results to step_02_doped_geometries.csv.
- Output file: `/app/outputs/step_02_doped_geometries.csv`
- Format: csv
- Contract: Columns: system, relaxation_type (i or f), lattice_parameter_a_A, SiXSi_angle_deg, SiC_bond_length_A, SiN_bond_length_A. Rows: OXY-SOD f, 1CH2-SOD i, 1CH2-SOD f, 1NH-SOD i, 1NH-SOD f. Missing bond lengths are left empty.
- Scoring: scored by hidden verifier

### Step 4: Strain energy per defect
- Role: scored (load-bearing)
- Action: Using the total energies from the polymer and sodalite optimizations, compute the defect strain energy per impurity for 1CH2-SOD (f) and 1NH-SOD (f) according to the polymer-reference method: E^s = n⁻¹ [E(nX-SOD) − E(OXY-SOD)] − [E(X-POLY) − E(OXY-POLY)]. Write the results to step_03_strain_energy.csv.
- Output file: `/app/outputs/step_03_strain_energy.csv`
- Format: csv
- Contract: Columns: system, strain_energy_per_defect_eV. Rows: 1CH2-SOD (f), 1NH-SOD (f).
- Scoring: scored by hidden verifier

### Step 5: DFT calculations for BF3 adsorption complexes
- Role: process
- Action: Perform DFT geometry optimizations for the isolated BF3 molecule, the BF3@Si-O-Si complex in OXY-SOD, and the BF3@Si-NH-Si complex in NH-SOD. Record the total energies of each system.
- Evidence: `/app/outputs/bf3_calc_log.txt`

### Step 6: BF3 adsorption energies
- Role: scored (load-bearing)
- Action: Compute the adsorption energy for each system as ΔE = E_complex − (E_zeolite + E_isolated_BF3) using the energies from step_5 and the appropriate bare zeolite energies. Write the results to step_04_adsorption_energy.csv.
- Output file: `/app/outputs/step_04_adsorption_energy.csv`
- Format: csv
- Contract: Columns: reaction, adsorption_energy_eV. Rows: BF3 + Si-O-Si (OXY-SOD), BF3 + Si-NH-Si (1NH-SOD).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_polymer_angles.csv`
- `/app/outputs/step_02_doped_geometries.csv`
- `/app/outputs/step_03_strain_energy.csv`
- `/app/outputs/step_04_adsorption_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_polymer_angles.csv
- path: `/app/outputs/step_01_polymer_angles.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized polymer reference angles and repeat lengths.
- schema:
  - `type`: table
  - `required_columns`: `polymer_name`, `angle_type`, `angle_value_deg`, `repeat_length_A`
  - `units`:
    - `angle_value_deg`: degrees
    - `repeat_length_A`: Angstrom

### step_02_doped_geometries.csv
- path: `/app/outputs/step_02_doped_geometries.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Geometry parameters for pristine and singly doped sodalites.
- schema:
  - `type`: table
  - `required_columns`: `system`, `relaxation_type`, `lattice_parameter_a_A`, `SiXSi_angle_deg`, `SiC_bond_length_A`, `SiN_bond_length_A`
  - `units`:
    - `lattice_parameter_a_A`: Angstrom
    - `SiXSi_angle_deg`: degrees
    - `SiC_bond_length_A`: Angstrom
    - `SiN_bond_length_A`: Angstrom

### step_03_strain_energy.csv
- path: `/app/outputs/step_03_strain_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Defect strain energies per impurity.
- schema:
  - `type`: table
  - `required_columns`: `system`, `strain_energy_per_defect_eV`
  - `units`:
    - `strain_energy_per_defect_eV`: eV

### step_04_adsorption_energy.csv
- path: `/app/outputs/step_04_adsorption_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: BF3 adsorption energies at Si-O-Si and Si-NH-Si sites.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `adsorption_energy_eV`
  - `units`:
    - `adsorption_energy_eV`: eV

Notes: Values are compared to the paper's DFT-LDA results with tolerances that account for code-to-code differences (Quantum ESPRESSO vs VASP). The verifier reads the CSV files and checks each numeric value within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_polymer_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymer_name",
          "angle_type",
          "angle_value_deg",
          "repeat_length_A"
        ],
        "units": {
          "angle_value_deg": "degrees",
          "repeat_length_A": "Angstrom"
        }
      },
      "description": "Optimized polymer reference angles and repeat lengths."
    },
    {
      "file": "step_02_doped_geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "relaxation_type",
          "lattice_parameter_a_A",
          "SiXSi_angle_deg",
          "SiC_bond_length_A",
          "SiN_bond_length_A"
        ],
        "units": {
          "lattice_parameter_a_A": "Angstrom",
          "SiXSi_angle_deg": "degrees",
          "SiC_bond_length_A": "Angstrom",
          "SiN_bond_length_A": "Angstrom"
        }
      },
      "description": "Geometry parameters for pristine and singly doped sodalites."
    },
    {
      "file": "step_03_strain_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "strain_energy_per_defect_eV"
        ],
        "units": {
          "strain_energy_per_defect_eV": "eV"
        }
      },
      "description": "Defect strain energies per impurity."
    },
    {
      "file": "step_04_adsorption_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "adsorption_energy_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "BF3 adsorption energies at Si-O-Si and Si-NH-Si sites."
    }
  ],
  "notes": "Values are compared to the paper's DFT-LDA results with tolerances that account for code-to-code differences (Quantum ESPRESSO vs VASP). The verifier reads the CSV files and checks each numeric value within a tolerance."
}
```

## How you are scored
Each scored workflow stage produces a CSV file with a prescribed schema. A hidden verifier independently reads each file, extracts the reported numeric values, and compares them to reference gold values (unseen by the agent) using tolerances appropriate for each quantity. The verifier also checks required qualitative ordering relations among certain quantities. The final reward is a weighted sum of the per‑stage scores, with higher weight given to the strain energy and adsorption energy stages. Providing numbers that match the reference without genuinely executing the DFT workflow will not pass, because the verifier evaluates the actual computed outputs from the submitted artifacts.
