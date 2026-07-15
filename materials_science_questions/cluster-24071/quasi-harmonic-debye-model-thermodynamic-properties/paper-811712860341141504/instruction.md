# Quasi-harmonic Debye model thermodynamic properties

## Problem background
Rare-earth monopnictides such as holmium arsenide (HoAs) and holmium phosphide (HoP) crystallize in the rocksalt (B1) structure and exhibit strongly correlated f-electron behavior. Understanding their structural, elastic, and thermodynamic properties is important for potential industrial applications, but experimental data are scarce and systematic first-principles predictions have not been reported for these compounds. This task aims to compute the equilibrium structural parameters (lattice constant, bulk modulus, its pressure derivative, cohesive energy), second-order elastic constants, derived polycrystalline elastic moduli (Zener anisotropy factor, Poisson’s ratio, Young’s modulus, isotropic shear modulus), and key thermodynamic quantities (heat capacity at constant volume at 300 K, Debye temperature at 0 K, Grüneisen parameter at 0 K, all at zero pressure) for both HoAs and HoP using density functional theory (DFT) and a quasi-harmonic Debye model.

## Approach
Density functional theory (DFT) calculations are performed with an open-source plane-wave code (e.g., Quantum ESPRESSO) using publicly available pseudopotentials. Total energies are computed for the B1 structure of HoAs and HoP over a range of volumes; atomic reference energies are obtained for isolated Ho, As, and P atoms using the same pseudopotential set. The Murnaghan equation of state is fitted to the energy–volume data to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative, and the cohesive energy per atom is derived from the bulk and atomic energies. Second-order elastic constants C₁₁, C₁₂, C₄₄ are obtained from stress–strain relations under volume-conserving distortions. From these, the Voigt–Reuss–Hill isotropic shear modulus, Zener anisotropy factor, Poisson’s ratio, and Young’s modulus are calculated. Finally, the quasi-harmonic Debye model (using e.g. the GIBBS program or an equivalent Python implementation) is applied to the energy–volume data and Poisson’s ratio to compute the heat capacity at constant volume at 300 K, the Debye temperature at 0 K, and the Grüneisen parameter at 0 K, all at ambient pressure. The workflow proceeds in four stages, each producing a scored CSV file.

## Reproduction target
Using an open-source DFT code (e.g., Quantum ESPRESSO) with publicly available pseudopotentials, compute total energies for HoAs and HoP in the rocksalt B1 structure over a series of volumes and for the isolated atoms Ho, As, P. Fit the Murnaghan equation of state to obtain the equilibrium lattice constant (Å), bulk modulus (GPa), pressure derivative of bulk modulus, and cohesive energy (eV/atom) for both compounds. Perform volume-conserving strain calculations to extract the elastic constants C₁₁, C₁₂, C₄₄ (GPa). Derive the Zener anisotropy factor, Poisson’s ratio (ν), Young’s modulus (GPa), and isotropic shear modulus (GPa) from the elastic constants and bulk modulus. Using the quasi-harmonic Debye model, compute the heat capacity at constant volume C_V (J mol⁻¹ K⁻¹) at 300 K, the Debye temperature (K) at 0 K, and the Grüneisen parameter at 0 K, all at zero pressure. Write the results for each stage into the specified CSV files: step_01_structural.csv, step_02_elastic.csv, step_03_derived_elastic.csv, and step_04_thermodynamic.csv.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Ho, As, P: https://www.materialscloud.org/discover/sssp/table
- GIBBS program or Debye model implementation: https://github.com/pmla/gibbs
- Python scientific libraries: numpy scipy ase pymatgen

## Workflow steps

### Step 1: Structural parameters and cohesive energy
- Role: scored (load-bearing)
- Action: Perform DFT total-energy calculations for HoAs and HoP in the rocksalt (B1) structure at a series of volumes. Compute the total energies of isolated Ho, As, and P atoms using the same pseudopotentials. Fit the energy-volume data for each compound to the Murnaghan equation of state; extract equilibrium lattice constant, bulk modulus, and its pressure derivative. Compute cohesive energy per atom from atomic and bulk energies. Save results to step_01_structural.csv and retain the raw E(V) data for later steps.
- Output file: `/app/outputs/step_01_structural.csv`
- Format: csv
- Contract: material (string), a_A (float), B_GPa (float), B_prime (float), E_coh_eV_per_atom (float); one row per compound.
- Scoring: scored by hidden verifier

### Step 2: Second-order elastic constants
- Role: scored
- Action: Starting from the relaxed B1 structures, apply volume-conserving strain patterns and compute the stress tensor from DFT for each distorted configuration. Fit the stress-strain relations to extract the cubic elastic constants C11, C12, C44 for HoAs and HoP. Write results to step_02_elastic.csv.
- Output file: `/app/outputs/step_02_elastic.csv`
- Format: csv
- Contract: material (string), C11_GPa (float), C12_GPa (float), C44_GPa (float); one row per compound.
- Scoring: scored by hidden verifier

### Step 3: Derived elastic moduli
- Role: scored
- Action: From the elastic constants and bulk modulus, compute the Voigt and Reuss shear moduli and the Hill average (isotropic shear modulus G). Then calculate the Zener anisotropy factor (A = 2*C44/(C11-C12)), Poisson's ratio (ν), and Young's modulus (E = 9BG/(3B+G)). Write results to step_03_derived_elastic.csv.
- Output file: `/app/outputs/step_03_derived_elastic.csv`
- Format: csv
- Contract: material (string), A (float), nu (float), E_GPa (float), G_GPa (float); one row per compound.
- Scoring: scored by hidden verifier

### Step 4: Thermodynamic properties from quasi-harmonic Debye model
- Role: scored (load-bearing)
- Action: Using the energy-volume data obtained in step 1 and Poisson's ratio from step 3, run the quasi-harmonic Debye model (e.g., with the GIBBS program or an equivalent Python implementation) to compute the heat capacity at constant volume Cv at 300 K, the Debye temperature at 0 K, and the Grüneisen parameter at 0 K, all at zero pressure, for both compounds. Write results to step_04_thermodynamic.csv.
- Output file: `/app/outputs/step_04_thermodynamic.csv`
- Format: csv
- Contract: material (string), Cv_300K_J_per_mol_K (float), Debye_T_0K_K (float), gamma_0K (float); one row per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural.csv`
- `/app/outputs/step_02_elastic.csv`
- `/app/outputs/step_03_derived_elastic.csv`
- `/app/outputs/step_04_thermodynamic.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural.csv
- path: `/app/outputs/step_01_structural.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant, bulk modulus, pressure derivative of bulk modulus, and cohesive energy for HoAs and HoP.
- schema:
  - `type`: table
  - `required_columns`: `material`, `a_A`, `B_GPa`, `B_prime`, `E_coh_eV_per_atom`
  - `units`:
    - `a_A`: Angstrom
    - `B_GPa`: GPa
    - `B_prime`: dimensionless
    - `E_coh_eV_per_atom`: eV/atom

### step_02_elastic.csv
- path: `/app/outputs/step_02_elastic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Second-order elastic constants C11, C12, C44 for HoAs and HoP.
- schema:
  - `type`: table
  - `required_columns`: `material`, `C11_GPa`, `C12_GPa`, `C44_GPa`
  - `units`:
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa

### step_03_derived_elastic.csv
- path: `/app/outputs/step_03_derived_elastic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zener anisotropy factor, Poisson's ratio, Young's modulus, and isotropic shear modulus for HoAs and HoP.
- schema:
  - `type`: table
  - `required_columns`: `material`, `A`, `nu`, `E_GPa`, `G_GPa`
  - `units`:
    - `A`: dimensionless
    - `nu`: dimensionless
    - `E_GPa`: GPa
    - `G_GPa`: GPa

### step_04_thermodynamic.csv
- path: `/app/outputs/step_04_thermodynamic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Heat capacity at 300 K, Debye temperature at 0 K, and Grüneisen parameter at 0 K at zero pressure for HoAs and HoP.
- schema:
  - `type`: table
  - `required_columns`: `material`, `Cv_300K_J_per_mol_K`, `Debye_T_0K_K`, `gamma_0K`
  - `units`:
    - `Cv_300K_J_per_mol_K`: J/(mol*K)
    - `Debye_T_0K_K`: K
    - `gamma_0K`: dimensionless

Notes: All outputs are scored by comparison with hidden reference values using appropriate tolerances. The checker also validates basic structural requirements (e.g., HoP has larger bulk modulus and Young's modulus than HoAs, Zener anisotropy < 1).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "a_A",
          "B_GPa",
          "B_prime",
          "E_coh_eV_per_atom"
        ],
        "units": {
          "a_A": "Angstrom",
          "B_GPa": "GPa",
          "B_prime": "dimensionless",
          "E_coh_eV_per_atom": "eV/atom"
        }
      },
      "description": "Equilibrium lattice constant, bulk modulus, pressure derivative of bulk modulus, and cohesive energy for HoAs and HoP."
    },
    {
      "file": "step_02_elastic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "C11_GPa",
          "C12_GPa",
          "C44_GPa"
        ],
        "units": {
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa"
        }
      },
      "description": "Second-order elastic constants C11, C12, C44 for HoAs and HoP."
    },
    {
      "file": "step_03_derived_elastic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "A",
          "nu",
          "E_GPa",
          "G_GPa"
        ],
        "units": {
          "A": "dimensionless",
          "nu": "dimensionless",
          "E_GPa": "GPa",
          "G_GPa": "GPa"
        }
      },
      "description": "Zener anisotropy factor, Poisson's ratio, Young's modulus, and isotropic shear modulus for HoAs and HoP."
    },
    {
      "file": "step_04_thermodynamic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "Cv_300K_J_per_mol_K",
          "Debye_T_0K_K",
          "gamma_0K"
        ],
        "units": {
          "Cv_300K_J_per_mol_K": "J/(mol*K)",
          "Debye_T_0K_K": "K",
          "gamma_0K": "dimensionless"
        }
      },
      "description": "Heat capacity at 300 K, Debye temperature at 0 K, and Grüneisen parameter at 0 K at zero pressure for HoAs and HoP."
    }
  ],
  "notes": "All outputs are scored by comparison with hidden reference values using appropriate tolerances. The checker also validates basic structural requirements (e.g., HoP has larger bulk modulus and Young's modulus than HoAs, Zener anisotropy < 1)."
}
```

## How you are scored
A hidden verifier reads the four CSV files you produce and compares each numerical value to independently known reference results using appropriate tolerances. The comparison accounts for legitimate differences arising from the choice of DFT code, pseudopotentials, and computational parameters, so reproducible values within a reasonable margin receive full credit; better-than-reference values are not penalized. In addition, the verifier checks several well-established physical trends (e.g., HoP should have larger bulk modulus, Young’s modulus, and shear modulus than HoAs; the Zener anisotropy factor should be less than 1 for both compounds; Poisson’s ratio should be near 0.4; the B/G ratio should exceed 1.75). Each property contributes equally to a composite score, and the final reward is a number between 0 and 1 that reflects how many of the required quantities fall within the expected tolerance or satisfy the trend conditions. Simply reporting numbers that match published values is not sufficient; you must genuinely execute the computational workflow to produce correct and self-consistent outputs.
