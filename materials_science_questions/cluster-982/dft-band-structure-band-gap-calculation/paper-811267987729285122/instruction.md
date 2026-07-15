# First-Principles Study of Ti-Doped and Ti-VO-Co-Doped β-Ga₂O₃ Magnetic Properties

## Problem background
β-Ga₂O₃ is a wide-band-gap semiconductor with potential in spintronics when doped with nonmagnetic transition metals. First‑principles calculations can predict whether such doping induces a net magnetic moment and whether an intrinsic defect, such as an oxygen vacancy (V_O), alters the magnetic properties. This task investigates, using density functional theory, the magnetic moments and ferromagnetic coupling that arise when a Ti atom substitutes a Ga atom in the monoclinic β‑Ga₂O₃ crystal, and the effect of adjacent oxygen vacancies on those properties. The goal is to determine whether Ti doping alone produces a magnetic moment and, if it does, whether the presence of a nearby V_O increases the moment and strengthens the ferromagnetic interaction between two Ti dopants — both as open quantities to compute from first principles.

## Approach
The approach is a spin‑polarized density functional theory (DFT) study using the open‑source Quantum ESPRESSO code with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) and ultrasoft pseudopotentials. First, build a 40‑atom monoclinic β‑Ga₂O₃ supercell from the known crystal structure (Geller, 1960). Generate atomic models for the configurations of interest: a single Ti atom replacing the octahedral Ga(A) site; the same single‑Ti system with each of the three near‑neighbour oxygen vacancies O(1), O(2), O(3) removed; a two‑Ti configuration where Ti atoms occupy the A0 and A2 octahedral sites (distance ≈ 3.04 Å); and the same two‑Ti configuration with the adjacent VO(3) vacancy introduced. All structures are fully relaxed (cell parameters and atomic positions) without symmetry constraints. For each relaxed structure, run a self‑consistent field (SCF) calculation to extract the total magnetic moment of the supercell and, for the co‑doped cases, the magnetic moment projected onto the Ti atom. For the two‑Ti systems, compute total energies in both ferromagnetic (FM) and antiferromagnetic (AFM) spin arrangements; the ferromagnetic stabilization energy is defined as ΔE = E(AFM) – E(FM). The workflow aggregates the computed total moments, local Ti moments, and ΔE values into a single JSON file for verification.

## Reproduction target
Produce the following quantities for the key doping/co‑doping configurations derived from the same β‑Ga₂O₃ supercell and the same DFT method:

- Total magnetic moment of the system with one Ti at the octahedral Ga(A) site.
- Total magnetic moment of the single‑Ti system when each adjacent oxygen vacancy (VO(1), VO(2), VO(3)) is introduced.
- Local magnetic moment on the Ti atom in each of the three Ti+VO co‑doped systems.
- Ferromagnetic stabilization energy ΔE = E(AFM) – E(FM) for the A0‑A2 two‑Ti configuration without any oxygen vacancy, and for the same A0‑A2 configuration with a VO(3) oxygen vacancy.
- Total magnetic moment of the A0‑A2 two‑Ti system (FM state) both with and without the VO(3) vacancy.

Additionally, verify the qualitative trend that introducing an oxygen vacancy (any of VO(1), VO(2), VO(3)) increases the total magnetic moment compared with the vacancy‑free single‑Ti case, and that the ΔE for the A0‑A2+VO(3) system is larger than the ΔE for the A0‑A2 system without a vacancy (i.e., the oxygen vacancy strengthens the ferromagnetic coupling between the two Ti dopants).

## Assets

- β-Ga₂O₃ crystal structure (monoclinic): 10.1063/1.1729357
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials for Ga, O, Ti: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build supercell and doping configurations
- Role: process
- Action: Construct the 40‑atom monoclinic β‑Ga₂O₃ supercell using the known crystal structure and generate atomic models for all required doping/co‑doping configurations: intrinsic, single Ti at octahedral Ga(A) site, Ti with oxygen vacancies at O(1), O(2), O(3) adjacent to Ti, two Ti atoms at A0‑A2 sites, and A0‑A2 with VO(3).
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: For each configuration, perform spin‑polarized DFT geometry optimization using Quantum ESPRESSO with the GGA‑PBE functional and ultrasoft pseudopotentials. Relax atomic coordinates and cell parameters without symmetry constraints.
- Evidence: none

### Step 3: Single Ti electronic structure
- Role: process
- Action: Using the optimized single‑Ti Ga(A) structure, run a spin‑polarized self‑consistent field calculation to obtain the total energy and total magnetic moment.
- Evidence: none

### Step 4: Ti‑VO co‑doped electronic structure
- Role: process
- Action: For each Ti+VO configuration (VO(1), VO(2), VO(3) adjacent to Ti), run an SCF calculation to obtain total and local (projected on Ti) magnetic moments.
- Evidence: none

### Step 5: Two‑Ti FM/AFM energy calculations (no vacancy)
- Role: process
- Action: For the A0‑A2 two‑Ti configuration without a vacancy, compute total energies in both ferromagnetic and antiferromagnetic spin alignments. Calculate ΔE = E(AFM) – E(FM) and record the total magnetic moment in the FM state.
- Evidence: none

### Step 6: Two‑Ti + VO(3) FM/AFM calculation
- Role: process
- Action: Repeat the FM/AFM total‑energy calculation for the A0‑A2 configuration with the adjacent VO(3) oxygen vacancy, and calculate ΔE and total magnetic moment.
- Evidence: none

### Step 7: Collect and report results
- Role: scored (load-bearing)
- Action: Extract the required quantities from the DFT output files and write a single JSON file containing all computed magnetic moments and ferromagnetic stabilization energies for the key configurations.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: {
  "total_moment_Ti_Ga_A": "float (μB)",
  "total_moment_VO1_Ti": "float (μB)",
  "total_moment_VO2_Ti": "float (μB)",
  "total_moment_VO3_Ti": "float (μB)",
  "local_moment_Ti_VO1": "float (μB)",
  "local_moment_Ti_VO2": "float (μB)",
  "local_moment_Ti_VO3": "float (μB)",
  "Delta_E_A0_A2_no_vacancy": "float (meV)",
  "Delta_E_A0_A2_VO3": "float (meV)",
  "total_moment_A0_A2_no_vacancy": "float (μB)",
  "total_moment_A0_A2_VO3": "float (μB)"
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the computed total magnetic moments, local Ti moments, and FM stabilization energies for the Ti-doped and Ti‑VO co‑doped β‑Ga₂O₃ configurations. The hidden checker compares these values to the paper‑reported reference numbers with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `total_moment_Ti_Ga_A`: float
    - `total_moment_VO1_Ti`: float
    - `total_moment_VO2_Ti`: float
    - `total_moment_VO3_Ti`: float
    - `local_moment_Ti_VO1`: float
    - `local_moment_Ti_VO2`: float
    - `local_moment_Ti_VO3`: float
    - `Delta_E_A0_A2_no_vacancy`: float
    - `Delta_E_A0_A2_VO3`: float
    - `total_moment_A0_A2_no_vacancy`: float
    - `total_moment_A0_A2_VO3`: float
  - `units`:
    - `total_moment_Ti_Ga_A`: μB
    - `total_moment_VO1_Ti`: μB
    - `total_moment_VO2_Ti`: μB
    - `total_moment_VO3_Ti`: μB
    - `local_moment_Ti_VO1`: μB
    - `local_moment_Ti_VO2`: μB
    - `local_moment_Ti_VO3`: μB
    - `Delta_E_A0_A2_no_vacancy`: meV
    - `Delta_E_A0_A2_VO3`: meV
    - `total_moment_A0_A2_no_vacancy`: μB
    - `total_moment_A0_A2_VO3`: μB

Notes: Results are compared against the paper's values; no gold values are revealed here. The agent must perform all DFT stages to obtain these quantities.

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
          "total_moment_Ti_Ga_A": "float",
          "total_moment_VO1_Ti": "float",
          "total_moment_VO2_Ti": "float",
          "total_moment_VO3_Ti": "float",
          "local_moment_Ti_VO1": "float",
          "local_moment_Ti_VO2": "float",
          "local_moment_Ti_VO3": "float",
          "Delta_E_A0_A2_no_vacancy": "float",
          "Delta_E_A0_A2_VO3": "float",
          "total_moment_A0_A2_no_vacancy": "float",
          "total_moment_A0_A2_VO3": "float"
        },
        "units": {
          "total_moment_Ti_Ga_A": "μB",
          "total_moment_VO1_Ti": "μB",
          "total_moment_VO2_Ti": "μB",
          "total_moment_VO3_Ti": "μB",
          "local_moment_Ti_VO1": "μB",
          "local_moment_Ti_VO2": "μB",
          "local_moment_Ti_VO3": "μB",
          "Delta_E_A0_A2_no_vacancy": "meV",
          "Delta_E_A0_A2_VO3": "meV",
          "total_moment_A0_A2_no_vacancy": "μB",
          "total_moment_A0_A2_VO3": "μB"
        }
      },
      "description": "JSON file containing the computed total magnetic moments, local Ti moments, and FM stabilization energies for the Ti-doped and Ti‑VO co‑doped β‑Ga₂O₃ configurations. The hidden checker compares these values to the paper‑reported reference numbers with appropriate tolerances."
    }
  ],
  "notes": "Results are compared against the paper's values; no gold values are revealed here. The agent must perform all DFT stages to obtain these quantities."
}
```

## How you are scored
A hidden verifier independently scores the submission by examining the file `/app/outputs/computed_results.json`. Each reported quantity (total moments, local moments, ΔE values) is compared against hidden reference values using tolerances appropriate for the computational approach. The verifier also checks that the required trends hold (moments increase in the presence of a vacancy; ΔE for the two‑Ti+VO(3) system is greater than the two‑Ti system without a vacancy). The final reward is a weighted combination of the individual checks; reporting the paper’s numbers is not sufficient — the values must be the outcome of a properly executed first‑principles workflow. The hidden tolerances and weights are fixed in the checker and are not provided here.
