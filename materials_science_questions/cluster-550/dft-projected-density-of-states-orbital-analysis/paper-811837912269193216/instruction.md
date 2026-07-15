# First-principles calculation of elastic constants and electronic DOS for a B2 intermetallic compound

## Problem background
The intermetallic YCu alloy in the B2 (CsCl) phase exhibits an interesting combination of mechanical and electronic properties. First-principles calculations can predict its equilibrium lattice constant, bulk modulus, elastic constants, and the electronic density of states at the Fermi level. In this task, you will compute these quantities from first principles using density functional theory, following a well-established computational protocol.

## Approach
You will perform plane-wave pseudopotential DFT calculations with the generalized gradient approximation (GGA) in the Perdew-Wang flavor (PW91). Three computational stages are required: (1) total-energy calculations as a function of lattice constant, fitting to the Murnaghan equation of state to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative; (2) application of three homogeneous strain patterns (hydrostatic, tri-axial shear, volume-conserving orthorhombic) to the equilibrium cell, computing energy changes for a range of strain amplitudes and fitting quadratic energy-strain relations to obtain the three independent elastic constants C11, C12, C44; (3) a self-consistent electronic structure calculation at the equilibrium geometry followed by band-structure and density-of-states computations along the high-symmetry path Γ-X-M-R-Γ-M, extracting the total DOS at the Fermi level. All calculations use the open-source Quantum ESPRESSO suite and publicly available pseudopotentials.

## Reproduction target
Your goal is to produce, in /app/outputs/outputs.json, a JSON object with the following seven numeric fields representing the physical quantities obtained from the DFT workflow:

- lattice_constant_a_nm (equilibrium lattice constant in nm)
- bulk_modulus_B_GPa (bulk modulus in GPa)
- B_prime (first pressure derivative of the bulk modulus, dimensionless)
- C11_GPa (elastic constant C11 in GPa)
- C12_GPa (elastic constant C12 in GPa)
- C44_GPa (elastic constant C44 in GPa)
- total_DOS_at_Fermi_level_N_EF_states_per_eV (total density of states at the Fermi level in states/eV)

These values must be obtained by re-running the full DFT protocol; no pre-existing data or hard-coded numbers should be used.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential for Yttrium (Y) – GGA-PW91: https://www.quantum-espresso.org/pseudopotentials
- Pseudopotential for Copper (Cu) – GGA-PW91: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT structural optimization and equation-of-state fitting
- Role: process
- Action: Run DFT total-energy calculations for the B2 compound at multiple lattice constants around the equilibrium. Fit the energy-volume data to the Murnaghan equation of state to obtain the equilibrium lattice constant a, bulk modulus B, and its pressure derivative B'.
- Evidence: none

### Step 2: Elastic constants from strain-energy method
- Role: process
- Action: Apply three homogeneous strain patterns (hydrostatic, tri-axial shear, volume-conserving orthorhombic) to the equilibrium lattice. For each pattern compute DFT total energies at multiple strain amplitudes and fit the quadratic ΔE/V versus δ² relations to extract C11, C12, C44.
- Evidence: none

### Step 3: Electronic structure calculations
- Role: process
- Action: Using the equilibrium geometry from step_01, perform a self-consistent DFT calculation, then compute the electronic band structure along the high-symmetry path Γ-X-M-R-Γ-M and the total density of states. Extract the total DOS at the Fermi energy, N(E_F).
- Evidence: none

### Step 4: Compile final results
- Role: scored (load-bearing)
- Action: Collect the seven key values from the previous steps and write them as a JSON file with fields: lattice_constant_a_nm, bulk_modulus_B_GPa, B_prime, C11_GPa, C12_GPa, C44_GPa, total_DOS_at_Fermi_level_N_EF_states_per_eV.
- Output file: `/app/outputs/outputs.json`
- Format: json
- Contract: {"lattice_constant_a_nm": "float", "bulk_modulus_B_GPa": "float", "B_prime": "float", "C11_GPa": "float", "C12_GPa": "float", "C44_GPa": "float", "total_DOS_at_Fermi_level_N_EF_states_per_eV": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/outputs.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### outputs.json
- path: `/app/outputs/outputs.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Seven key physical quantities reproduced from the DFT calculations: lattice constant a, bulk modulus B, its pressure derivative B', elastic constants C11, C12, C44, and total DOS at the Fermi level N(E_F).
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_a_nm`: float
    - `bulk_modulus_B_GPa`: float
    - `B_prime`: float
    - `C11_GPa`: float
    - `C12_GPa`: float
    - `C44_GPa`: float
    - `total_DOS_at_Fermi_level_N_EF_states_per_eV`: float
  - `units`:
    - `lattice_constant_a_nm`: nm
    - `bulk_modulus_B_GPa`: GPa
    - `B_prime`: dimensionless
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa
    - `total_DOS_at_Fermi_level_N_EF_states_per_eV`: states/eV

Notes: All values must be computed from the DFT workflow; no external lookup. The hidden checker compares each field to the paper-reported values within absolute tolerances typical for pseudopotential/implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "outputs.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_a_nm": "float",
          "bulk_modulus_B_GPa": "float",
          "B_prime": "float",
          "C11_GPa": "float",
          "C12_GPa": "float",
          "C44_GPa": "float",
          "total_DOS_at_Fermi_level_N_EF_states_per_eV": "float"
        },
        "units": {
          "lattice_constant_a_nm": "nm",
          "bulk_modulus_B_GPa": "GPa",
          "B_prime": "dimensionless",
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa",
          "total_DOS_at_Fermi_level_N_EF_states_per_eV": "states/eV"
        }
      },
      "description": "Seven key physical quantities reproduced from the DFT calculations: lattice constant a, bulk modulus B, its pressure derivative B', elastic constants C11, C12, C44, and total DOS at the Fermi level N(E_F)."
    }
  ],
  "notes": "All values must be computed from the DFT workflow; no external lookup. The hidden checker compares each field to the paper-reported values within absolute tolerances typical for pseudopotential/implementation spread."
}
```

## How you are scored
A hidden verifier will read your outputs.json and compare each of the seven numerical fields against reference values that represent the expected outcome of such a calculation. Tolerances are set to account for the normal spread caused by different choices of pseudopotentials, k-point meshes, and numerical settings. Your reward is the fraction of fields that fall within the allowed tolerances. Simply reporting numbers without executing the computational workflow will not produce values that match the reference; the tolerances are designed to require a genuine re-run of the protocol. The verifier works independently and awards partial credit if only some values are within tolerance.
