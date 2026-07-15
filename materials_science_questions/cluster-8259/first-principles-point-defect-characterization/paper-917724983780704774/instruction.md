# DFT characterization of a substitutional point defect in monolayer WS2

## Problem background
Point defects in two-dimensional (2D) transition metal dichalcogenides (TMDs) are promising candidates for quantum information science (QIS) applications, such as single-photon emitters and spin qubits. An ideal quantum defect should exhibit localized in-gap electronic states that enable bright optical transitions, preferably in the telecom or visible spectral range. However, identifying such defects is challenging due to the vast compositional and configurational space. This task focuses on computationally characterizing one candidate defect — the neutral cobalt substitution on a sulfur site (Co_S^0) in monolayer WS₂ — using first-principles calculations. The goal is to compute key electronic and optical properties that determine whether this defect could serve as a useful quantum defect, including its thermodynamic charge transition levels, single-particle excitation energies, transition dipole moments, and zero-phonon line.

## Approach
The characterization follows a hybrid density functional theory (DFT) protocol based on the PBE0 functional, which mixes a fraction of exact (Fock) exchange into the semilocal PBE functional. Because a single fraction of exact exchange cannot simultaneously describe the host band edges and the localized defect states accurately, two different mixing parameters are employed: α = 0.22 for the pristine WS₂ host to obtain reliable band-edge positions, and α = 0.07 for the defect supercells to satisfy the generalized Koopmans' condition for localized defect levels. The methodology involves: (1) constructing a supercell of monolayer WS₂ and creating the Co_S defect; (2) computing the valence band maximum (VBM) and conduction band minimum (CBM) of the pristine host aligned to the vacuum level; (3) relaxing the geometry of the neutral Co_S defect and identifying its Kohn-Sham defect states; (4) calculating formation energies for the +1, 0, and -1 charge states and extracting thermodynamic charge transition levels (+1/0) and (0/−1) relative to the band edges; (5) evaluating the lowest intra-defect single-particle excitation (from d_z² to d_x²−y²) and its transition dipole moment; and (6) using constrained DFT to relax the structure with the excited-state occupation imposed and determine the zero-phonon line (ZPL) of that transition. The results are collected into a single output file.

## Reproduction target
Compute the following five quantities for the Co_S^0 defect in monolayer WS₂ using fully self-consistent PBE0 calculations as described in the workflow steps, and write them to the file `computed_properties.json` in `/app/outputs`:
- CTL_p1_0: the thermodynamic (+1/0) charge transition level, in eV above the valence band maximum (VBM).
- CTL_0_m1: the thermodynamic (0/−1) charge transition level, in eV below the conduction band minimum (CBM).
- KS_energy_difference: the single-particle Kohn-Sham energy difference between the occupied d_z² and unoccupied d_x²−y² defect states, in eV.
- TDM: the transition dipole moment of that same transition, in Debye.
- ZPL: the zero-phonon line of that transition obtained via constrained DFT, in eV.

The output JSON file must contain exactly these five keys with numeric values in the specified units. The file will be compared against hidden reference values derived from the literature; the reproduction is considered successful if each value falls within an acceptable tolerance.

## Assets

- Monolayer WS2 crystal structure: https://materialsproject.org/materials/mp-224/
- Open-source DFT code: https://www.cp2k.org/
- Pseudopotentials or PAW datasets: https://materialscloud.org/sssp
- pymatgen: pymatgen

## Workflow steps

### Step 1: Build supercells and create defect
- Role: process
- Action: Construct a 144-atom orthorhombic supercell of monolayer WS2 with ~14 Å vacuum using the public crystal structure. Create the Co_S defect by substituting one sulfur atom with cobalt.
- Evidence: `/app/outputs/supercell_coords.txt`

### Step 2: Compute pristine WS2 band edges (PBE0, α=0.22)
- Role: process
- Action: Perform a DFT calculation on the pristine WS2 supercell using the PBE0 hybrid functional with 22% Fock exchange. Optionally include spin-orbit coupling. Determine the valence band maximum (VBM) and conduction band minimum (CBM) energies aligned to the vacuum level.
- Evidence: `/app/outputs/pristine_bandedge.json`

### Step 3: Relax Co_S^0 defect structure (PBE0, α=0.07)
- Role: process
- Action: Perform a fully self-consistent PBE0 calculation (7% Fock exchange) with structural relaxation of the neutral Co_S defect. Obtain the relaxed atomic positions and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/relaxed_structure.json`

### Step 4: Compute formation energies and charge transition levels
- Role: process
- Action: For the Co_S defect in charge states +1, 0, -1, compute total energies using PBE0 (α=0.07) with finite-size corrections. Align defect levels to the pristine band edges via the vacuum level and determine the thermodynamic charge transition levels (+1/0) and (0/−1) relative to VBM and CBM.
- Evidence: `/app/outputs/ctl_data.json`

### Step 5: Compute KS energy difference and transition dipole moment
- Role: process
- Action: Using the relaxed Co_S^0 structure, identify the Kohn-Sham states corresponding to the occupied d_z^2 and unoccupied d_x^2−y^2 defect levels. Compute the single-particle energy difference and the transition dipole moment (TDM) between these states.
- Evidence: `/app/outputs/ks_tdm.json`

### Step 6: Compute zero-phonon line via constrained DFT
- Role: process
- Action: Perform a constrained DFT calculation by imposing occupation of the unoccupied d_x^2−y^2 state and relaxing the structure. Compute the zero-phonon line (ZPL) as the energy difference between the ground-state relaxed geometry and the excited-state relaxed geometry in the same charge state.
- Evidence: `/app/outputs/zpl.json`

### Step 7: Write computed properties
- Role: scored (load-bearing)
- Action: Collect the computed charge transition levels, KS energy difference, transition dipole moment, and ZPL into a single JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: Object with keys: CTL_p1_0 (number, eV above VBM), CTL_0_m1 (number, eV below CBM), KS_energy_difference (number, eV), TDM (number, Debye), ZPL (number, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final computed properties for the Co_S^0 defect: thermodynamic charge transition levels, single-particle excitation energy, transition dipole moment, and zero-phonon line.
- schema:
  - `type`: object
  - `required`:
    - `CTL_p1_0`: number
    - `CTL_0_m1`: number
    - `KS_energy_difference`: number
    - `TDM`: number
    - `ZPL`: number
  - `units`:
    - `CTL_p1_0`: eV
    - `CTL_0_m1`: eV
    - `KS_energy_difference`: eV
    - `TDM`: Debye
    - `ZPL`: eV

Notes: All quantities are compared to hidden reference values from the paper with appropriate tolerances. The solver must produce this file after completing all preceding process steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CTL_p1_0": "number",
          "CTL_0_m1": "number",
          "KS_energy_difference": "number",
          "TDM": "number",
          "ZPL": "number"
        },
        "units": {
          "CTL_p1_0": "eV",
          "CTL_0_m1": "eV",
          "KS_energy_difference": "eV",
          "TDM": "Debye",
          "ZPL": "eV"
        }
      },
      "description": "Final computed properties for the Co_S^0 defect: thermodynamic charge transition levels, single-particle excitation energy, transition dipole moment, and zero-phonon line."
    }
  ],
  "notes": "All quantities are compared to hidden reference values from the paper with appropriate tolerances. The solver must produce this file after completing all preceding process steps."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that runs independently after your task finishes. The verifier reads the file `/app/outputs/computed_properties.json` and compares each of the five reported numeric values (CTL_p1_0, CTL_0_m1, KS_energy_difference, TDM, ZPL) against hidden reference numbers. For each quantity, a tolerance is defined that accounts for legitimate differences due to the choice of DFT code, pseudopotentials, and numerical settings. A reported value that falls within the tolerance of its reference earns full credit for that quantity; credit decreases for larger deviations. The final reward is a weighted combination of the per-quantity scores, with all five quantities receiving equal weight. Note that simply reporting a number is not sufficient; the verifier expects that you have actually executed the computational workflow described in the steps to produce these results. The hidden reference values and exact tolerances are not disclosed, but they are set to be reachable by a careful implementation of the protocol described in this instruction.
