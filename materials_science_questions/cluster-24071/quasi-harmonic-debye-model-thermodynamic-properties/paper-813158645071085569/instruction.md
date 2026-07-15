# First-principles thermodynamic and elastic properties of zirconium hydrides

## Problem background
Zirconium-based alloys are used for fuel cladding in nuclear power reactors. During service, hydrogen can enter the cladding and form zirconium hydrides once the solid solubility limit is exceeded. These hydrides can embrittle the material and compromise cladding integrity. Accurate mechanical and thermodynamic properties of the hydride phases are essential input for multiscale modelling of cladding performance, yet experimental data are limited and prior computational studies have produced inconsistent results. This task addresses that gap by computing the elastic and thermodynamic properties of the key zirconium hydride phases from first principles.

## Approach
Density functional theory (DFT) calculations are performed with the plane-wave code Quantum ESPRESSO, using the PW91 GGA exchange-correlation functional and projector augmented wave (PAW) pseudopotentials for Zr and H. The crystal structures of α-Zr, γ-ZrH, δ-ZrH₁.₅ (modeled as an ordered hydrogen divacancy phase), and ε-ZrH₂ are fully relaxed to obtain zero-temperature, stress-free lattice parameters. Single-crystal elastic constants are extracted by applying symmetry-adapted strain states, fitting the energy-volume relation, and solving for the independent Cij. Polycrystalline Voigt–Reuss–Hill (VRH) averages of Young’s, bulk, and shear moduli are then derived. To cover a wide temperature range, the quasi-harmonic approximation (QHA) is employed. The vibrational free energy is obtained from the phonon density of states computed via density functional perturbation theory; the electronic contribution comes from the electronic density of states computed with a tetrahedron-based method. The H₂ molecule ground-state energy and harmonic vibrational frequency are calculated as a reference for the enthalpy of formation. From these inputs, temperature-dependent entropy, heat capacity, enthalpy, and the enthalpy of formation, Debye temperature, and electronic heat capacity constant are derived.

## Reproduction target
Produce two scored JSON output files from the complete DFT + QHA workflow:

1. `step_02_elastic_properties.json`: for each of the four phases (α-Zr, γ-ZrH, δ-ZrH₁.₅, ε-ZrH₂), report the equilibrium lattice parameters a and c (in Å), the independent elastic constants C11, C12, C13, C33, C44, and (for tetragonal phases) C66 (in GPa), and the VRH polycrystalline moduli E, B, G (in GPa).

2. `step_03_thermodynamic_data.json`: for each of the same four phases, report the entropy (J/(mol·K)), heat capacity (J/(mol·K)), and enthalpy (kJ/mol) at 11 temperatures from 0 K to 1000 K in steps of 100 K; the enthalpy of formation at 298 K (kJ/mol); the Debye temperature (K); and the electronic heat capacity constant (mJ/(mol·K²)).

These quantities are computed from the DFT ground-state energies, phonon and electronic densities of states, and the H₂ reference; they must follow the QHA framework described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Zr PAW pseudopotential (PW91): https://www.quantum-espresso.org/pseudopotentials
- H PAW pseudopotential (PW91): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for α-Zr, γ-ZrH, δ-ZrH1.5, and ε-ZrH2 using Quantum ESPRESSO with PW91 GGA PAW pseudopotentials. Relax cell parameters and atomic positions until convergence.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Elastic constants and polycrystalline moduli
- Role: scored
- Action: For each optimized phase, apply the strain combinations appropriate for its crystal symmetry and fit the energy-volume relations to extract independent elastic constants. Compute isotropic polycrystalline moduli (Young's modulus E, bulk modulus B, shear modulus G) via Voigt–Reuss–Hill averaging. Output the lattice parameters, elastic constants, and VRH moduli.
- Output file: `/app/outputs/step_02_elastic_properties.json`
- Format: json
- Contract: JSON object with key 'phases': array of objects, each with keys: name (string), a (float, Å), c (float, Å), C11..C66 (float, GPa; C66 for tetragonal phases, omit for α-Zr), E (float, GPa), B (float, GPa), G (float, GPa).
- Scoring: scored by hidden verifier

### Step 3: H₂ molecule reference
- Role: process
- Action: Compute the ground-state energy, equilibrium bond length, and harmonic vibrational frequency of the H₂ molecule using the same DFT settings (isolated molecule in a large cell).
- Evidence: `/app/outputs/h2_reference.log`

### Step 4: Phonon dispersion and PHDOS
- Role: process
- Action: For each relaxed phase, compute phonon dispersion and phonon density of states using density functional perturbation theory.
- Evidence: `/app/outputs/phonon_calculations.log`

### Step 5: Electronic DOS
- Role: process
- Action: For each relaxed phase, compute the electronic density of states using a tetrahedron-based method with a dense k‑point grid.
- Evidence: `/app/outputs/electronic_dos.log`

### Step 6: Quasi-harmonic thermodynamic properties
- Role: scored (load-bearing)
- Action: Using the ground-state energies, phonon DOS, electronic DOS, and H₂ reference, compute the vibrational and electronic contributions to the Helmholtz free energy via the quasi-harmonic approximation. Derive entropy, heat capacity, and enthalpy as functions of temperature (0–1000 K). Compute enthalpy of formation, Debye temperature, and electronic heat capacity constant. Output the temperature-dependent quantities and derived constants.
- Output file: `/app/outputs/step_03_thermodynamic_data.json`
- Format: json
- Contract: JSON object with key 'phases': array of objects, each with keys: name (string), entropy (array of 11 floats at T=0,100,…,1000 K, J/(mol·K)), heat_capacity (array of 11 floats, J/(mol·K)), enthalpy (array of 11 floats, kJ/mol), enthalpy_of_formation (float, kJ/mol), Debye_temperature (float, K), electronic_heat_constant (float, mJ/(mol·K²)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_elastic_properties.json`
- `/app/outputs/step_03_thermodynamic_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_elastic_properties.json
- path: `/app/outputs/step_02_elastic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single-crystal elastic constants and VRH polycrystalline moduli.
- schema:
  - `type`: object
  - `required`:
    - `phases`: array
  - `items`:
    - `name`: string
    - `a`: float (Å)
    - `c`: float (Å)
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C13`: float (GPa)
    - `C33`: float (GPa)
    - `C44`: float (GPa)
    - `C66`: float (GPa, present only for tetragonal phases)
    - `E`: float (GPa)
    - `B`: float (GPa)
    - `G`: float (GPa)

### step_03_thermodynamic_data.json
- path: `/app/outputs/step_03_thermodynamic_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Temperature-dependent thermodynamic properties and derived constants.
- schema:
  - `type`: object
  - `required`:
    - `phases`: array
  - `items`:
    - `name`: string
    - `entropy`: array of 11 floats (J/(mol·K))
    - `heat_capacity`: array of 11 floats (J/(mol·K))
    - `enthalpy`: array of 11 floats (kJ/mol)
    - `enthalpy_of_formation`: float (kJ/mol)
    - `Debye_temperature`: float (K)
    - `electronic_heat_constant`: float (mJ/(mol·K²))

Notes: All quantities are compared against the paper's reported values with a hidden tolerance. The Debye temperature should be computed from the low-temperature Cv fit (Eq. 10 of the paper).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "phases": "array"
        },
        "items": {
          "name": "string",
          "a": "float (Å)",
          "c": "float (Å)",
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C13": "float (GPa)",
          "C33": "float (GPa)",
          "C44": "float (GPa)",
          "C66": "float (GPa, present only for tetragonal phases)",
          "E": "float (GPa)",
          "B": "float (GPa)",
          "G": "float (GPa)"
        }
      },
      "description": "Single-crystal elastic constants and VRH polycrystalline moduli."
    },
    {
      "file": "step_03_thermodynamic_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "phases": "array"
        },
        "items": {
          "name": "string",
          "entropy": "array of 11 floats (J/(mol·K))",
          "heat_capacity": "array of 11 floats (J/(mol·K))",
          "enthalpy": "array of 11 floats (kJ/mol)",
          "enthalpy_of_formation": "float (kJ/mol)",
          "Debye_temperature": "float (K)",
          "electronic_heat_constant": "float (mJ/(mol·K²))"
        }
      },
      "description": "Temperature-dependent thermodynamic properties and derived constants."
    }
  ],
  "notes": "All quantities are compared against the paper's reported values with a hidden tolerance. The Debye temperature should be computed from the low-temperature Cv fit (Eq. 10 of the paper)."
}
```

## How you are scored
A hidden verifier independently inspects your two scored output files. It compares your reported lattice parameters, elastic constants, VRH moduli, and each thermodynamic quantity to hidden reference values with appropriate tolerances. Each scored stage is assigned a weight, and the final reward (0–1) is the weighted sum of those stage-level scores. The last step (quasi-harmonic thermodynamic properties) is load‑bearing; its reward depends on whether the required upstream process steps (geometry optimization, H₂ reference, phonon and electronic DOS calculations) were genuinely executed. Reporting a number that happens to match the reference without correct underlying calculations will be penalized. You do not need to know the reference numbers; execute the full protocol faithfully and the tolerances will accommodate legitimate implementation differences.
