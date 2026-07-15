# DFT Reproduction of Co₂Se₃ Monolayer Electronic, Magnetic, and Mechanical Properties

## Problem background
Two-dimensional (2D) materials that combine intrinsic ferromagnetism with high Curie temperature and mechanical flexibility are attractive for next-generation flexible spintronic devices. Density functional theory (DFT) predictions indicate that a monolayer of Co₂Se₃, featuring a buckling hinge-like structure, could serve as such a material. The theoretical work suggests that Co₂Se₃ may exhibit half-metallic behaviour, a large magnetic moment, a Curie temperature well above room temperature, and extraordinary mechanical properties—including an unusually high critical strain and a giant out-of-plane negative Poisson’s ratio. This task aims to recompute these key electronic, magnetic, and mechanical properties to assess their reproducibility with open-source tools.

## Approach
The reproduction employs first-principles calculations based on plane-wave DFT. The structure of the Co₂Se₃ monolayer (hinge-like five-layer atomic configuration) is built from the reported orthorhombic lattice. Spin-polarised geometry relaxation is performed using the PBE functional to obtain the ferromagnetic ground state, and total energies for non-magnetic and several antiferromagnetic configurations are computed to confirm magnetic ordering. Electronic structure (band structure and density of states) is then calculated to check for half-metallicity and to extract the spin-up band gap. The Curie temperature is estimated via mean-field theory from the energy difference between the ferromagnetic and the lowest antiferromagnetic state. A series of static DFT relaxations under uniaxial tensile strain along the two in‑plane directions is then performed to obtain stress‑strain curves, bond‑length and bond‑angle evolutions, and buckling‑height changes. From these, critical strains, ideal strengths, the out‑of‑plane Poisson’s ratio, and the two‑stage unfolding mechanism (bond‑angle vs. bond‑length changes) are derived. All calculations are implemented with an open‑source DFT code and standard PBE pseudopotentials.

## Reproduction target
Produce a single JSON file, `/app/outputs/reproduced_properties.json`, that contains the following computed properties of the Co₂Se₃ monolayer, each with the exact key and unit indicated:

- `lattice_constant_a_angstrom`, `lattice_constant_b_angstrom` (Å)
- `cohesive_energy_eV_per_atom` (eV/atom)
- `bond_length_d1_angstrom`, `bond_length_d2_angstrom`, `bond_length_d3_angstrom` (Å)
- `buckling_height_angstrom` (Å)
- `spin_up_band_gap_eV` (eV)
- `magnetic_moment_per_Co_muB` (µB per Co atom)
- `curie_temperature_K` (K)
- `critical_strain_x`, `critical_strain_y` (dimensionless fraction)
- `ideal_strength_x_GPa`, `ideal_strength_y_GPa` (GPa)
- `negative_poisson_ratio_yz` (dimensionless)
- `bond_angle_alpha_change_stage1_percent`, `bond_length_d3_change_stage1_percent`, `bond_angle_alpha_change_stage2_percent`, `bond_length_d3_change_stage2_percent` (percentage changes for the two deformation stages under y‑strain)
- `stress_jump_strain_x` (dimensionless fraction)
- `new_dimer_bond_length_d4_angstrom` (Å)

All values must be numerical. The two‑stage unfolding is defined by the tensile loading along the y direction: stage 1 is strain < 20%, and stage 2 is from 20% up to the critical strain. The out‑of‑plane Poisson’s ratio is extracted from the buckling height change under y‑direction strain.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotentials (efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python with numpy, scipy, matplotlib: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Build initial Co2Se3 monolayer structure
- Role: process
- Action: Construct the Co2Se3 monolayer with the hinge-like five-layer geometry (two Co and three Se per formula unit) using lattice parameters a=5.415 Å and b=5.782 Å as an initial guess, and create a DFT input file (e.g., CIF or Quantum ESPRESSO input).
- Evidence: `/app/outputs/co2se3_initial.cif`

### Step 2: DFT geometry relaxation and magnetic ground state
- Role: process
- Action: Perform spin-polarized DFT relaxation for Co2Se3 using the PBE functional, obtaining the FM relaxed structure, total energies for FM, NM, and three AFM configurations to determine the magnetic ground state, and extracting relaxed lattice constants, bond lengths, buckling height, and magnetic moment. Save the optimized structure and energy summary.
- Evidence: `/app/outputs/relaxed_fm.log`

### Step 3: Electronic structure calculation
- Role: process
- Action: Using the relaxed FM Co2Se3 structure, perform a non-self-consistent band structure calculation along high-symmetry paths and compute the density of states to confirm half-metallic character and extract the spin-up band gap.
- Evidence: `/app/outputs/bands.dat`

### Step 4: Curie temperature estimation
- Role: process
- Action: Using the total energy difference between the FM state and the lowest AFM state (AFM3) from step_02, compute the Curie temperature via the mean-field formula (3k_B T_C = 2ΔE) and save the value.
- Evidence: `/app/outputs/curie_temperature.txt`

### Step 5: Uniaxial tensile tests and deformation analysis
- Role: process
- Action: For the Co2Se3 monolayer, perform a series of static DFT relaxations under uniaxial tensile strain along the x and y directions (small strain increments up to failure). At each strain, relax atomic positions (fixing the strained cell dimensions) and compute the engineering stress tensor. Record the evolution of bond lengths (d1, d3, d4) and bond angle (alpha) from the relaxed structures, as well as the buckling height change to extract the out-of-plane Poisson's ratio. Identify the critical strain (peak stress) and the sudden stress jump associated with Se-dimer breaking along x.
- Evidence: `/app/outputs/stress_strain.csv`

### Step 6: Assemble reproduced properties JSON
- Role: scored (load-bearing)
- Action: Collect all computed quantities from previous steps and write a single JSON file, /app/outputs/reproduced_properties.json, containing the exact numeric keys and units specified in the output contract.
- Output file: `/app/outputs/reproduced_properties.json`
- Format: json
- Contract: JSON object with keys: lattice_constant_a_angstrom, lattice_constant_b_angstrom, cohesive_energy_eV_per_atom, bond_length_d1_angstrom, bond_length_d2_angstrom, bond_length_d3_angstrom, buckling_height_angstrom, spin_up_band_gap_eV, magnetic_moment_per_Co_muB, curie_temperature_K, critical_strain_x, critical_strain_y, ideal_strength_x_GPa, ideal_strength_y_GPa, negative_poisson_ratio_yz, bond_angle_alpha_change_stage1_percent, bond_length_d3_change_stage1_percent, bond_angle_alpha_change_stage2_percent, bond_length_d3_change_stage2_percent, stress_jump_strain_x, new_dimer_bond_length_d4_angstrom. All values numeric; units as indicated in key names.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_properties.json
- path: `/app/outputs/reproduced_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All principal reproduced properties of the Co2Se3 monolayer, scored by comparing each field to hidden reference values from the published work. Reward is proportional to the number of fields within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_a_angstrom`: number
    - `lattice_constant_b_angstrom`: number
    - `cohesive_energy_eV_per_atom`: number
    - `bond_length_d1_angstrom`: number
    - `bond_length_d2_angstrom`: number
    - `bond_length_d3_angstrom`: number
    - `buckling_height_angstrom`: number
    - `spin_up_band_gap_eV`: number
    - `magnetic_moment_per_Co_muB`: number
    - `curie_temperature_K`: number
    - `critical_strain_x`: number
    - `critical_strain_y`: number
    - `ideal_strength_x_GPa`: number
    - `ideal_strength_y_GPa`: number
    - `negative_poisson_ratio_yz`: number
    - `bond_angle_alpha_change_stage1_percent`: number
    - `bond_length_d3_change_stage1_percent`: number
    - `bond_angle_alpha_change_stage2_percent`: number
    - `bond_length_d3_change_stage2_percent`: number
    - `stress_jump_strain_x`: number
    - `new_dimer_bond_length_d4_angstrom`: number
  - `items`: object
  - `units`:
    - `lattice_constant_a_angstrom`: angstrom
    - `lattice_constant_b_angstrom`: angstrom
    - `cohesive_energy_eV_per_atom`: eV/atom
    - `bond_length_d1_angstrom`: angstrom
    - `bond_length_d2_angstrom`: angstrom
    - `bond_length_d3_angstrom`: angstrom
    - `buckling_height_angstrom`: angstrom
    - `spin_up_band_gap_eV`: eV
    - `magnetic_moment_per_Co_muB`: μB per Co
    - `curie_temperature_K`: K
    - `critical_strain_x`: dimensionless (fraction)
    - `critical_strain_y`: dimensionless (fraction)
    - `ideal_strength_x_GPa`: GPa
    - `ideal_strength_y_GPa`: GPa
    - `negative_poisson_ratio_yz`: dimensionless
    - `bond_angle_alpha_change_stage1_percent`: percentage change
    - `bond_length_d3_change_stage1_percent`: percentage change
    - `bond_angle_alpha_change_stage2_percent`: percentage change
    - `bond_length_d3_change_stage2_percent`: percentage change
    - `stress_jump_strain_x`: dimensionless (fraction)
    - `new_dimer_bond_length_d4_angstrom`: angstrom

Notes: The file must be valid JSON. All numeric fields are required; missing or malformed fields are scored as zero for that property. The two-stage unfolding percentages must satisfy the qualitative trend (angle change > length change in stage 1 and < in stage 2) as an additional consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_a_angstrom": "number",
          "lattice_constant_b_angstrom": "number",
          "cohesive_energy_eV_per_atom": "number",
          "bond_length_d1_angstrom": "number",
          "bond_length_d2_angstrom": "number",
          "bond_length_d3_angstrom": "number",
          "buckling_height_angstrom": "number",
          "spin_up_band_gap_eV": "number",
          "magnetic_moment_per_Co_muB": "number",
          "curie_temperature_K": "number",
          "critical_strain_x": "number",
          "critical_strain_y": "number",
          "ideal_strength_x_GPa": "number",
          "ideal_strength_y_GPa": "number",
          "negative_poisson_ratio_yz": "number",
          "bond_angle_alpha_change_stage1_percent": "number",
          "bond_length_d3_change_stage1_percent": "number",
          "bond_angle_alpha_change_stage2_percent": "number",
          "bond_length_d3_change_stage2_percent": "number",
          "stress_jump_strain_x": "number",
          "new_dimer_bond_length_d4_angstrom": "number"
        },
        "items": {},
        "units": {
          "lattice_constant_a_angstrom": "angstrom",
          "lattice_constant_b_angstrom": "angstrom",
          "cohesive_energy_eV_per_atom": "eV/atom",
          "bond_length_d1_angstrom": "angstrom",
          "bond_length_d2_angstrom": "angstrom",
          "bond_length_d3_angstrom": "angstrom",
          "buckling_height_angstrom": "angstrom",
          "spin_up_band_gap_eV": "eV",
          "magnetic_moment_per_Co_muB": "μB per Co",
          "curie_temperature_K": "K",
          "critical_strain_x": "dimensionless (fraction)",
          "critical_strain_y": "dimensionless (fraction)",
          "ideal_strength_x_GPa": "GPa",
          "ideal_strength_y_GPa": "GPa",
          "negative_poisson_ratio_yz": "dimensionless",
          "bond_angle_alpha_change_stage1_percent": "percentage change",
          "bond_length_d3_change_stage1_percent": "percentage change",
          "bond_angle_alpha_change_stage2_percent": "percentage change",
          "bond_length_d3_change_stage2_percent": "percentage change",
          "stress_jump_strain_x": "dimensionless (fraction)",
          "new_dimer_bond_length_d4_angstrom": "angstrom"
        }
      },
      "description": "All principal reproduced properties of the Co2Se3 monolayer, scored by comparing each field to hidden reference values from the published work. Reward is proportional to the number of fields within tolerance."
    }
  ],
  "notes": "The file must be valid JSON. All numeric fields are required; missing or malformed fields are scored as zero for that property. The two-stage unfolding percentages must satisfy the qualitative trend (angle change > length change in stage 1 and < in stage 2) as an additional consistency check."
}
```

## How you are scored
A hidden verifier reads the `/app/outputs/reproduced_properties.json` you produce and compares each numeric field against reference values obtained from the original published work. Each field’s match is evaluated with a field‑specific tolerance that accounts for legitimate differences arising from the use of different DFT software, pseudopotentials, and numerical settings. Fields that fall within the tolerance and satisfy qualitative requirements (e.g., negative sign for the Poisson’s ratio, larger bond‑angle change than bond‑length change in stage 1 and the reverse in stage 2) contribute positively to your reward. Missing, non‑numeric, or out‑of‑tolerance fields contribute zero for that property. The final reward is proportional to the number of correctly reproduced fields, weighted so that the mechanical and magnetic properties together carry the majority of the score. Simply reporting the paper’s numbers without executing the workflow will produce large discrepancies because the tolerances are tight enough to require a genuine DFT run. You must follow the workflow steps and produce all intermediates; the verifier only inspects the final JSON file.
