# Ideal Mechanical Strength and Interface Cohesion of L1₂ Ir₃Nb and Ir₃Hf from First Principles

## Problem background
Ir-base superalloys with a fcc/L1₂ two-phase structure are candidates for ultra-high temperature applications. The ideal mechanical strength of defect-free L1₂ precipitates and the cohesion of coherent Ir/L1₂ interfaces critically influence alloy performance. This task computes the direction- and slip-system-resolved ideal tensile and shear strengths of L1₂ Ir₃Nb and Ir₃Hf, their elastic constants, and the work of separation and interface energies of Ir/Ir₃X (X=Nb, Hf) interfaces for (100) and (110) orientations.

## Approach
The reproduction uses ab initio density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) generalized-gradient approximation. All total-energy and force calculations are performed with an open-source plane-wave DFT code. The workflow builds the bulk L1₂ crystal structures, relaxes them, fits an equation of state to extract equilibrium lattice constants and elastic moduli, and then applies incremental tensile strains along ⟨100⟩, ⟨110⟩, ⟨111⟩ directions and shear strains along (001)[110], (110)[-110], (111)[-110], (111)[-211] slip systems, relaxing orthogonal cell vectors and atomic positions at each step, to obtain stress-strain curves and ideal strengths. For interface properties, slab supercells of the (100) and (110) interface orientations with two atomic configurations (interface layer with or without the Hf/Nb atom) are constructed, and total energies of the full interface, the separated Ir and Ir₃X surface slabs, and the bulk references are computed. From these, the work of separation and interface energy are derived. All derived quantities are aggregated into a single JSON file for verification.

## Reproduction target
Produce the file /app/outputs/results.json containing the following quantities for L1₂ Ir₃Nb and Ir₃Hf: equilibrium lattice constants, bulk modulus, shear modulus, G/B ratio, elastic constants C11, C12, C44; ideal tensile strengths in ⟨111⟩, ⟨100⟩, ⟨110⟩ directions; ideal shear strengths for slip systems (001)[110], (110)[-110], (111)[-110], (111)[-211]; work of separation and interface energy for (100)-I, (100)-II, (110)-I, (110)-II Ir/Ir₃X interfaces. The values must be computed by running the DFT workflow described in the steps; simply citing or fabricating the paper’s reported numbers is not sufficient.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PBE pseudopotentials for Ir, Nb, Hf: https://www.quantum-espresso.org/pseudopotentials
- Python scientific stack: numpy matplotlib ase

## Workflow steps

### Step 1: DFT optimization of pure reference elements
- Role: process
- Action: Perform full DFT relaxation (ion positions and cell parameters) of fcc Ir, bcc Nb, and hcp Hf to obtain equilibrium lattice constants and total energies.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 2: DFT optimization and elastic properties of L1₂ Ir₃Nb and Ir₃Hf
- Role: process
- Action: Optimize the L1₂ crystal structures of Ir₃Nb and Ir₃Hf. Perform a series of total-energy calculations at different volumes and fit an equation of state to obtain equilibrium lattice constants, bulk modulus, and elastic constants C₁₁, C₁₂, C₄₄. Compute the shear modulus G and the G/B ratio.
- Evidence: `/app/outputs/elastic_properties.json`

### Step 3: Heat of formation calculation
- Role: process
- Action: Calculate the heats of formation of L1₂ Ir₃Nb and Ir₃Hf using the total energies from step1 and step2.
- Evidence: `/app/outputs/heats_of_formation.txt`

### Step 4: Ideal tensile strength simulations
- Role: process
- Action: For both Ir₃Nb and Ir₃Hf, apply incremental tensile strain along the ⟨100⟩, ⟨110⟩, and ⟨111⟩ directions. At each strain step, relax the atomic positions and cell vectors orthogonal to the strain direction, and record the stress tensor. Identify the maximum tensile stress on each stress–strain curve as the ideal tensile strength.
- Evidence: `/app/outputs/tensile_stress_strain.csv`

### Step 5: Ideal shear strength simulations
- Role: process
- Action: For both compounds, apply incremental shear strain along the four slip systems: (001)[110], (110)[-110], (111)[-110], and (111)[-211]. At each strain step, relax the atomic positions and cell vectors orthogonal to the shear direction, and record the shear stress. Identify the maximum shear stress as the ideal shear strength for each slip system.
- Evidence: `/app/outputs/shear_stress_strain.csv`

### Step 6: Interface total energy calculations
- Role: process
- Action: Build supercell slab models for the (100) and (110) interface orientations with configurations I and II (interface layer with or without Hf/Nb atoms) for Ir/Ir₃Nb and Ir/Ir₃Hf. Compute total energies of the full interface slabs and of the separated Ir and Ir₃X surface slabs. Use these to calculate work of separation and interface energy via Eqs. (1) and (2) of the paper.
- Evidence: `/app/outputs/interface_energies_raw.json`

### Step 7: Compile final scored results
- Role: scored (load-bearing)
- Action: Aggregate all computed physical properties into a single JSON file. Include: equilibrium lattice constants, bulk modulus, shear modulus, G/B ratio, elastic constants C11, C12, C44 for both Ir₃Nb and Ir₃Hf; ideal tensile strengths for the three directions and ideal shear strengths for the four slip systems for both compounds; work of separation and interface energy for (100)-I, (100)-II, (110)-I, (110)-II interfaces of Ir/Ir₃Nb and Ir/Ir₃Hf.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with numeric keys: Ir3Nb_lattice_constant_A, Ir3Hf_lattice_constant_A, Ir3Nb_bulk_modulus_GPa, Ir3Hf_bulk_modulus_GPa, Ir3Nb_shear_modulus_GPa, Ir3Hf_shear_modulus_GPa, Ir3Nb_GB_ratio, Ir3Hf_GB_ratio, Ir3Nb_C11_GPa, Ir3Nb_C12_GPa, Ir3Nb_C44_GPa, Ir3Hf_C11_GPa, Ir3Hf_C12_GPa, Ir3Hf_C44_GPa, Ir3Nb_tensile_111_GPa, Ir3Nb_tensile_100_GPa, Ir3Nb_tensile_110_GPa, Ir3Hf_tensile_111_GPa, Ir3Hf_tensile_100_GPa, Ir3Hf_tensile_110_GPa, Ir3Nb_shear_001_110_GPa, Ir3Nb_shear_110_1-10_GPa, Ir3Nb_shear_111_1-10_GPa, Ir3Nb_shear_111_2-11_GPa, Ir3Hf_shear_001_110_GPa, Ir3Hf_shear_110_1-10_GPa, Ir3Hf_shear_111_1-10_GPa, Ir3Hf_shear_111_2-11_GPa, Ir3Nb_work_of_separation_100_I_Jm2, Ir3Nb_work_of_separation_100_II_Jm2, Ir3Nb_work_of_separation_110_I_Jm2, Ir3Nb_work_of_separation_110_II_Jm2, Ir3Hf_work_of_separation_100_I_Jm2, Ir3Hf_work_of_separation_100_II_Jm2, Ir3Hf_work_of_separation_110_I_Jm2, Ir3Hf_work_of_separation_110_II_Jm2, Ir3Nb_interface_energy_100_I_Jm2, Ir3Nb_interface_energy_100_II_Jm2, Ir3Nb_interface_energy_110_I_Jm2, Ir3Nb_interface_energy_110_II_Jm2, Ir3Hf_interface_energy_100_I_Jm2, Ir3Hf_interface_energy_100_II_Jm2, Ir3Hf_interface_energy_110_I_Jm2, Ir3Hf_interface_energy_110_II_Jm2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated physical property values for L1₂ Ir₃Nb and Ir₃Hf: lattice constants (Å), bulk modulus, shear modulus, elastic constants, tensile and shear strengths (GPa), works of separation and interface energies (J/m²). Values are compared to hidden reference using tolerances; structural trend checks verify the correct ordering of strengths and negativity of certain interface energies.
- schema:
  - `type`: object
  - `required`: `Ir3Nb_lattice_constant_A`, `Ir3Hf_lattice_constant_A`, `Ir3Nb_bulk_modulus_GPa`, `Ir3Hf_bulk_modulus_GPa`, `Ir3Nb_shear_modulus_GPa`, `Ir3Hf_shear_modulus_GPa`, `Ir3Nb_GB_ratio`, `Ir3Hf_GB_ratio`, `Ir3Nb_C11_GPa`, `Ir3Nb_C12_GPa`, `Ir3Nb_C44_GPa`, `Ir3Hf_C11_GPa`, `Ir3Hf_C12_GPa`, `Ir3Hf_C44_GPa`, `Ir3Nb_tensile_111_GPa`, `Ir3Nb_tensile_100_GPa`, `Ir3Nb_tensile_110_GPa`, `Ir3Hf_tensile_111_GPa`, `Ir3Hf_tensile_100_GPa`, `Ir3Hf_tensile_110_GPa`, `Ir3Nb_shear_001_110_GPa`, `Ir3Nb_shear_110_1-10_GPa`, `Ir3Nb_shear_111_1-10_GPa`, `Ir3Nb_shear_111_2-11_GPa`, `Ir3Hf_shear_001_110_GPa`, `Ir3Hf_shear_110_1-10_GPa`, `Ir3Hf_shear_111_1-10_GPa`, `Ir3Hf_shear_111_2-11_GPa`, `Ir3Nb_work_of_separation_100_I_Jm2`, `Ir3Nb_work_of_separation_100_II_Jm2`, `Ir3Nb_work_of_separation_110_I_Jm2`, `Ir3Nb_work_of_separation_110_II_Jm2`, `Ir3Hf_work_of_separation_100_I_Jm2`, `Ir3Hf_work_of_separation_100_II_Jm2`, `Ir3Hf_work_of_separation_110_I_Jm2`, `Ir3Hf_work_of_separation_110_II_Jm2`, `Ir3Nb_interface_energy_100_I_Jm2`, `Ir3Nb_interface_energy_100_II_Jm2`, `Ir3Nb_interface_energy_110_I_Jm2`, `Ir3Nb_interface_energy_110_II_Jm2`, `Ir3Hf_interface_energy_100_I_Jm2`, `Ir3Hf_interface_energy_100_II_Jm2`, `Ir3Hf_interface_energy_110_I_Jm2`, `Ir3Hf_interface_energy_110_II_Jm2`
  - `properties`:
    - `Ir3Nb_lattice_constant_A`:
      - `type`: number
      - `unit`: Å
    - `Ir3Hf_lattice_constant_A`:
      - `type`: number
      - `unit`: Å
    - `Ir3Nb_bulk_modulus_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_bulk_modulus_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_shear_modulus_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_shear_modulus_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_GB_ratio`:
      - `type`: number
    - `Ir3Hf_GB_ratio`:
      - `type`: number
    - `Ir3Nb_C11_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_C12_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_C44_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_C11_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_C12_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_C44_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_tensile_111_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_tensile_100_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_tensile_110_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_tensile_111_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_tensile_100_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_tensile_110_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_shear_001_110_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_shear_110_1-10_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_shear_111_1-10_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_shear_111_2-11_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_shear_001_110_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_shear_110_1-10_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_shear_111_1-10_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Hf_shear_111_2-11_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Ir3Nb_work_of_separation_100_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_work_of_separation_100_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_work_of_separation_110_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_work_of_separation_110_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_work_of_separation_100_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_work_of_separation_100_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_work_of_separation_110_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_work_of_separation_110_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_interface_energy_100_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_interface_energy_100_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_interface_energy_110_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Nb_interface_energy_110_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_interface_energy_100_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_interface_energy_100_II_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_interface_energy_110_I_Jm2`:
      - `type`: number
      - `unit`: J/m²
    - `Ir3Hf_interface_energy_110_II_Jm2`:
      - `type`: number
      - `unit`: J/m²

Notes: The verifier applies T0 exact_match with tolerances on each numeric value, plus T3 structural checks: Ir₃Nb strengths > Ir₃Hf strengths, (110) tensile weakest, (111)[-211] shear weakest, and (100)-I/(110)-I interface energies negative. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Ir3Nb_lattice_constant_A",
          "Ir3Hf_lattice_constant_A",
          "Ir3Nb_bulk_modulus_GPa",
          "Ir3Hf_bulk_modulus_GPa",
          "Ir3Nb_shear_modulus_GPa",
          "Ir3Hf_shear_modulus_GPa",
          "Ir3Nb_GB_ratio",
          "Ir3Hf_GB_ratio",
          "Ir3Nb_C11_GPa",
          "Ir3Nb_C12_GPa",
          "Ir3Nb_C44_GPa",
          "Ir3Hf_C11_GPa",
          "Ir3Hf_C12_GPa",
          "Ir3Hf_C44_GPa",
          "Ir3Nb_tensile_111_GPa",
          "Ir3Nb_tensile_100_GPa",
          "Ir3Nb_tensile_110_GPa",
          "Ir3Hf_tensile_111_GPa",
          "Ir3Hf_tensile_100_GPa",
          "Ir3Hf_tensile_110_GPa",
          "Ir3Nb_shear_001_110_GPa",
          "Ir3Nb_shear_110_1-10_GPa",
          "Ir3Nb_shear_111_1-10_GPa",
          "Ir3Nb_shear_111_2-11_GPa",
          "Ir3Hf_shear_001_110_GPa",
          "Ir3Hf_shear_110_1-10_GPa",
          "Ir3Hf_shear_111_1-10_GPa",
          "Ir3Hf_shear_111_2-11_GPa",
          "Ir3Nb_work_of_separation_100_I_Jm2",
          "Ir3Nb_work_of_separation_100_II_Jm2",
          "Ir3Nb_work_of_separation_110_I_Jm2",
          "Ir3Nb_work_of_separation_110_II_Jm2",
          "Ir3Hf_work_of_separation_100_I_Jm2",
          "Ir3Hf_work_of_separation_100_II_Jm2",
          "Ir3Hf_work_of_separation_110_I_Jm2",
          "Ir3Hf_work_of_separation_110_II_Jm2",
          "Ir3Nb_interface_energy_100_I_Jm2",
          "Ir3Nb_interface_energy_100_II_Jm2",
          "Ir3Nb_interface_energy_110_I_Jm2",
          "Ir3Nb_interface_energy_110_II_Jm2",
          "Ir3Hf_interface_energy_100_I_Jm2",
          "Ir3Hf_interface_energy_100_II_Jm2",
          "Ir3Hf_interface_energy_110_I_Jm2",
          "Ir3Hf_interface_energy_110_II_Jm2"
        ],
        "properties": {
          "Ir3Nb_lattice_constant_A": {
            "type": "number",
            "unit": "Å"
          },
          "Ir3Hf_lattice_constant_A": {
            "type": "number",
            "unit": "Å"
          },
          "Ir3Nb_bulk_modulus_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_bulk_modulus_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_shear_modulus_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_shear_modulus_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_GB_ratio": {
            "type": "number"
          },
          "Ir3Hf_GB_ratio": {
            "type": "number"
          },
          "Ir3Nb_C11_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_C12_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_C44_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_C11_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_C12_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_C44_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_tensile_111_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_tensile_100_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_tensile_110_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_tensile_111_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_tensile_100_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_tensile_110_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_shear_001_110_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_shear_110_1-10_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_shear_111_1-10_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_shear_111_2-11_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_shear_001_110_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_shear_110_1-10_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_shear_111_1-10_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Hf_shear_111_2-11_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Ir3Nb_work_of_separation_100_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_work_of_separation_100_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_work_of_separation_110_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_work_of_separation_110_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_work_of_separation_100_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_work_of_separation_100_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_work_of_separation_110_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_work_of_separation_110_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_interface_energy_100_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_interface_energy_100_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_interface_energy_110_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Nb_interface_energy_110_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_interface_energy_100_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_interface_energy_100_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_interface_energy_110_I_Jm2": {
            "type": "number",
            "unit": "J/m²"
          },
          "Ir3Hf_interface_energy_110_II_Jm2": {
            "type": "number",
            "unit": "J/m²"
          }
        }
      },
      "description": "Aggregated physical property values for L1₂ Ir₃Nb and Ir₃Hf: lattice constants (Å), bulk modulus, shear modulus, elastic constants, tensile and shear strengths (GPa), works of separation and interface energies (J/m²). Values are compared to hidden reference using tolerances; structural trend checks verify the correct ordering of strengths and negativity of certain interface energies."
    }
  ],
  "notes": "The verifier applies T0 exact_match with tolerances on each numeric value, plus T3 structural checks: Ir₃Nb strengths > Ir₃Hf strengths, (110) tensile weakest, (111)[-211] shear weakest, and (100)-I/(110)-I interface energies negative. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier inspects the evidence files produced by each workflow step and reads the final /app/outputs/results.json. For each numeric quantity, the verifier compares your computed value to a hidden reference value with an appropriate tolerance. In addition, the verifier checks structural consistency (e.g., relative ordering of strengths and interface energies) without revealing the expected relationships. The total reward is a weighted combination of correct absolute values and correct structural relationships. Running the full DFT pipeline to produce the required evidence is mandatory; merely reporting an expected number without producing the intermediate evidence will not pass.
