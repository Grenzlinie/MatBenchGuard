# DFT structural stability and elastic moduli of TaN

## Problem background
Transition metal nitrides, such as TaN, are widely studied for applications as hard coatings and diffusion barriers. TaN exhibits several crystallographic polymorphs, and predicting their relative stability and associated properties is essential for understanding and controlling the material's behaviour. The aim is to determine the ground-state structure and compute the equilibrium structural, elastic, and electronic properties from first principles.

## Approach
The stability and properties are investigated using density functional theory (DFT) with the generalized gradient approximation (GGA-PBE). Electron-ion interactions are described by ultrasoft pseudopotentials, and total energies are calculated for five candidate crystal structures: CoSn, WC, NaCl, ZnS-B3, and CsCl. For each structure, the total energy is computed at a series of unit cell volumes around the expected equilibrium. The sum of isolated neutral atom energies is taken as the reference to define the cohesive energy, which is fitted to the third-order Birch-Murnaghan equation of state. The fit yields equilibrium lattice constants, cohesive energy, bulk modulus, and its pressure derivative. Subsequently, the density of states (DOS) at the Fermi level is computed for each structure at its equilibrium volume.

## Reproduction target
You must produce two JSON artifacts:
- fitted_properties.json: contains, for each TaN phase (CoSn, WC, CsCl, ZnS_B3, NaCl), the equilibrium lattice constants a and c (where applicable), the cohesive energy E0, equilibrium volume V0, bulk modulus K0, and pressure derivative K0_prime.
- dos_at_fermi.json: contains the total density of states at the Fermi energy, N_tot(E_F), in states/eV per TaN formula unit for each phase.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ta pseudopotential (GGA-PBE): https://pseudopotentials.quantum-espresso.org/upf_files/Ta.pbe-spn-rrkjus_psl.1.0.0.UPF
- N pseudopotential (GGA-PBE): https://pseudopotentials.quantum-espresso.org/upf_files/N.pbe-n-rrkjus_psl.1.0.0.UPF

## Workflow steps

### Step 1: Reference atom energy calculation
- Role: process
- Action: Calculate total energies of isolated neutral Ta and N atoms using the same DFT setup (GGA-PBE, ultrasoft Vanderbilt pseudopotentials, 40 Ry kinetic energy cutoff) as the bulk calculations, e.g. in large supercells with appropriate k-point sampling. Obtain E_Ta and E_N.
- Evidence: `/app/outputs/atomic_energies.log`

### Step 2: DFT total energy vs. volume for TaN phases
- Role: process
- Action: For each of the five TaN structures (CoSn, WC, NaCl, ZnS-B3, CsCl), perform self-consistent total-energy calculations at a series of volumes (at least 7 volumes per phase) around equilibrium. Use the specified crystal structures with appropriate k-point meshes and 40 Ry cutoff. Convert total energies to per TaN formula unit.
- Evidence: `/app/outputs/ev_data.csv`

### Step 3: Birch-Murnaghan EOS fitting
- Role: scored (load-bearing)
- Action: Subtract the sum of isolated atom energies from the total energies to obtain cohesive energies. Fit the cohesive energy vs. volume data for each structure to the third-order Birch-Murnaghan equation of state. Extract equilibrium lattice constants (a and c if applicable), cohesive energy E0, equilibrium volume V0, bulk modulus K0, and pressure derivative K0'. Write the extracted properties as JSON.
- Output file: `/app/outputs/fitted_properties.json`
- Format: json
- Contract: {"CoSn": {"a": number, "c": number, "E0": number, "V0": number, "K0": number, "K0_prime": number}, "WC": {"a": number, "c": number, "E0": number, "V0": number, "K0": number, "K0_prime": number}, ...}
- Scoring: scored by hidden verifier

### Step 4: DOS at Fermi level
- Role: scored
- Action: Using the equilibrium lattice constants from the EOS fit, perform a self-consistent DFT calculation followed by a non-self-consistent calculation on a denser k-point mesh to obtain the total density of states. Extract the total DOS at the Fermi level, N_tot(E_F), in states/eV per TaN formula unit for each structure. Write the values as JSON.
- Output file: `/app/outputs/dos_at_fermi.json`
- Format: json
- Contract: {"CoSn": number, "WC": number, "CsCl": number, "ZnS_B3": number, "NaCl": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_properties.json`
- `/app/outputs/dos_at_fermi.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_properties.json
- path: `/app/outputs/fitted_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium properties from Birch-Murnaghan fit for the five TaN phases.
- schema:
  - `type`: object
  - `required`: `CoSn`, `WC`, `CsCl`, `ZnS_B3`, `NaCl`
  - `items`:
    - `a`: number (Å)
    - `c`: number or null (Å)
    - `E0`: number (eV per TaN f.u.)
    - `V0`: number (Å³ per TaN f.u.)
    - `K0`: number (GPa)
    - `K0_prime`: number (dimensionless)

### dos_at_fermi.json
- path: `/app/outputs/dos_at_fermi.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total density of states at the Fermi level for each TaN phase.
- schema:
  - `type`: object
  - `required`: `CoSn`, `WC`, `CsCl`, `ZnS_B3`, `NaCl`
  - `items`:
    - `CoSn`: number (states/eV per f.u.)
    - `WC`: number (states/eV per f.u.)
    - `CsCl`: number (states/eV per f.u.)
    - `ZnS_B3`: number (states/eV per f.u.)
    - `NaCl`: number (states/eV per f.u.)

Notes: The checker compares the agent's submitted fitted_properties.json and dos_at_fermi.json against hidden reference values derived from the paper's reported data, using appropriate tolerances for DFT reproducibility.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CoSn",
          "WC",
          "CsCl",
          "ZnS_B3",
          "NaCl"
        ],
        "items": {
          "a": "number (Å)",
          "c": "number or null (Å)",
          "E0": "number (eV per TaN f.u.)",
          "V0": "number (Å³ per TaN f.u.)",
          "K0": "number (GPa)",
          "K0_prime": "number (dimensionless)"
        }
      },
      "description": "Equilibrium properties from Birch-Murnaghan fit for the five TaN phases."
    },
    {
      "file": "dos_at_fermi.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CoSn",
          "WC",
          "CsCl",
          "ZnS_B3",
          "NaCl"
        ],
        "items": {
          "CoSn": "number (states/eV per f.u.)",
          "WC": "number (states/eV per f.u.)",
          "CsCl": "number (states/eV per f.u.)",
          "ZnS_B3": "number (states/eV per f.u.)",
          "NaCl": "number (states/eV per f.u.)"
        }
      },
      "description": "Total density of states at the Fermi level for each TaN phase."
    }
  ],
  "notes": "The checker compares the agent's submitted fitted_properties.json and dos_at_fermi.json against hidden reference values derived from the paper's reported data, using appropriate tolerances for DFT reproducibility."
}
```

## How you are scored
A hidden verifier will read your submitted fitted_properties.json and dos_at_fermi.json and compare every numerical value against independently stored reference values. The comparison uses appropriate tolerances to absorb legitimate differences between DFT implementations (e.g., pseudopotential details, small k-point sampling variations). Each matching field contributes a fraction of the total reward; the final score is the sum of per-field credits. There is no need to match any particular reference exactly; instead, the verifier checks whether your computed values fall within an expected range. The overall score ranges from 0 to 1, with a higher score indicating better agreement with the reference.
