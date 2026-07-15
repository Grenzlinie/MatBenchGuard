# First-Principles DFT of Superconducting Be2B and its Ternary Phases

## Problem background
The discovery of superconductivity in MgB₂ has driven interest in other light-element borides that may exhibit similar properties. Beryllium semiboride Be₂B crystallizes in the cubic antifluorite structure (CaF₂-type) and shares important electronic features with MgB₂, including hole states at Γ and a notable density of states (DOS) near the Fermi energy. Partial substitution of Be by Na, Mg, or Al modifies the lattice constant and the electronic structure, particularly the distribution of B 2p states at the Fermi level. Understanding how these substitutions alter the structural and electronic characteristics is key to assessing the potential superconductivity of these compounds. In this task you will compute the fundamental structural and electronic properties of Be₂B and its ternary phases using first-principles density functional theory.

## Approach
The reproduction uses first-principles DFT within the generalized gradient approximation (PBE-GGA) implemented in an open-source code such as Quantum ESPRESSO. For each of the four compounds—Be₂B, AlBeB, MgBeB, NaBeB—you will set up the cubic antifluorite unit cell (Be atoms at the 8c Wyckoff position, B at 4a, with Na/Mg/Al substituting one Be for the ternary phases). The workflow proceeds as follows:

1. **Structural relaxation**: Compute the total energy at several lattice constants around the expected equilibrium, then fit the energy–volume data to the Murnaghan equation of state to extract the equilibrium lattice constant a, bulk modulus B, and its pressure derivative B′.
2. **Electronic structure**: At the equilibrium volume, perform a self-consistent field calculation to obtain the converged charge density. Then compute the band structure along high-symmetry directions (including Γ and X) and the total and partial density of states (DOS).
3. **Parameter extraction**: From the band structure and DOS, extract the valence bandwidth VB, the band gap between Γ and X (Eg(Γ‑X)), the number of valence electrons per formula unit Nv, the total DOS at the Fermi level N(EF), and the partial B p contribution to N(EF). For AlBeB the B p contribution is not applicable and must be recorded as '-'.

All results are collected into a single tab-separated file.

## Reproduction target
Using a first-principles DFT code with the PBE-GGA functional, compute the following quantities for Be₂B, AlBeB, MgBeB, and NaBeB:
- equilibrium lattice constant a (Å)
- bulk modulus B (GPa) and its pressure derivative B′
- valence bandwidth VB (eV)
- Γ‑X band gap Eg (eV)
- number of valence electrons per formula unit Nv
- total Fermi-level DOS N(EF) (states/eV/cell)
- partial B p contribution to N(EF) (states/eV/cell), or '-' for AlBeB.

Write the results to a TSV file `computed_properties.tsv` with exactly the columns: compound, a_Ang, B_GPa, Bprime, VB_eV, Eg_Gamma_X_eV, Nv, N_EF_total_states_per_eV, B_p_contribution_states_per_eV. The lattice constants must satisfy the relative ordering NaBeB > MgBeB > AlBeB > Be₂B.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- PBE pseudopotential library: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Volume relaxation and equation-of-state fitting
- Role: process
- Action: For each compound Be2B, AlBeB, MgBeB, NaBeB, set up the cubic antifluorite unit cell, perform DFT total energy calculations with PBE-GGA at several volumes, and fit the energy-volume data to the Murnaghan equation of state to extract equilibrium lattice constant a, bulk modulus B, and pressure derivative B'.
- Evidence: none

### Step 2: SCF and electronic structure calculation
- Role: process
- Action: For each compound, using its equilibrium lattice constant, perform a self-consistent field (SCF) calculation to obtain converged charge density. Then compute the electronic band structure along high-symmetry lines (including Γ and X) and the total and partial density of states (DOS).
- Evidence: none

### Step 3: Extract and compile electronic parameters
- Role: scored (load-bearing)
- Action: From the band structure and DOS data, extract for each compound: valence bandwidth VB, band gap between Γ and X (Eg(Γ-X)), number of valence electrons per formula unit Nv, total DOS at Fermi level N(EF), and the B p partial contribution to N(EF). For AlBeB, the B p contribution is not applicable, use '-'. Compile all values along with the structural parameters (a, B, B') into a TSV file 'computed_properties.tsv' with columns: compound, a_Ang, B_GPa, Bprime, VB_eV, Eg_Gamma_X_eV, Nv, N_EF_total_states_per_eV, B_p_contribution_states_per_eV.
- Output file: `/app/outputs/computed_properties.tsv`
- Format: tsv
- Contract: compound (string), a_Ang (float), B_GPa (float), Bprime (float), VB_eV (float), Eg_Gamma_X_eV (float), Nv (int), N_EF_total_states_per_eV (float), B_p_contribution_states_per_eV (float or '-' for AlBeB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.tsv
- path: `/app/outputs/computed_properties.tsv`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Compiled structural and electronic properties for Be2B, AlBeB, MgBeB, NaBeB.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a_Ang`, `B_GPa`, `Bprime`, `VB_eV`, `Eg_Gamma_X_eV`, `Nv`, `N_EF_total_states_per_eV`, `B_p_contribution_states_per_eV`
  - `units`:
    - `a_Ang`: Angstrom
    - `B_GPa`: GPa
    - `Bprime`: dimensionless
    - `VB_eV`: eV
    - `Eg_Gamma_X_eV`: eV
    - `Nv`: integer
    - `N_EF_total_states_per_eV`: states/eV/cell
    - `B_p_contribution_states_per_eV`: states/eV/cell

Notes: The agent must compute these properties using first-principles DFT. No gold values or tolerances are given here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a_Ang",
          "B_GPa",
          "Bprime",
          "VB_eV",
          "Eg_Gamma_X_eV",
          "Nv",
          "N_EF_total_states_per_eV",
          "B_p_contribution_states_per_eV"
        ],
        "units": {
          "a_Ang": "Angstrom",
          "B_GPa": "GPa",
          "Bprime": "dimensionless",
          "VB_eV": "eV",
          "Eg_Gamma_X_eV": "eV",
          "Nv": "integer",
          "N_EF_total_states_per_eV": "states/eV/cell",
          "B_p_contribution_states_per_eV": "states/eV/cell"
        }
      },
      "description": "Compiled structural and electronic properties for Be2B, AlBeB, MgBeB, NaBeB."
    }
  ],
  "notes": "The agent must compute these properties using first-principles DFT. No gold values or tolerances are given here."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks the computed properties. The verifier compares your reported values against a set of hidden reference values using tolerances that account for systematic differences between DFT codes and approximations. The verifier also checks that the lattice constant ordering NaBeB > MgBeB > AlBeB > Be₂B holds. Each property and each compound contribute to a weighted score, and the final reward is the combined score across all items. Simply reporting numbers without performing the DFT workflow will result in a low or zero score.
