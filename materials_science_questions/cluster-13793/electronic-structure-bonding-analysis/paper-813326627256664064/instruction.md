# DFT geometry optimization and electronic structure analysis of LuB₂C

## Problem background
Rare-earth boride carbides REB₂C form layered structures where planar B/C nets determine electronic properties. For LuB₂C, the arrangement of boron and carbon atoms within the layers is not fully settled by X‑ray diffraction alone: two distinct colorings are possible, one with orthorhombic Pbam symmetry (B/C alternation), the other with tetragonal P4/mbm symmetry (boron rhombuses). Determining which coloring is the ground state and understanding its electronic structure requires first‑principles calculations. This task asks you to carry out such calculations and to compute the relative stability and band gaps of the two alternatives.

## Approach
The computational approach is density functional theory (DFT) with the PBE exchange‑correlation functional. You will use an open‑source plane‑wave DFT code and suitable pseudopotentials for Lu, B, and C. Two structural models must be built: (1) the orthorhombic Pbam model starting from the published experimental lattice parameters and atomic positions (a=6.7429 Å, b=6.7341 Å, c=3.5890 Å); (2) the tetragonal P4/mbm model (Coloring II) in which boron atoms form rhombuses. For each model, you will perform a full geometry optimization (relax all atomic positions and cell parameters) and then compute the electronic density of states (DOS) to extract the band gap and to judge whether the system is metallic or insulating. Finally, you will compare the total energies to obtain the relative stability ΔE = E(Pbam) – E(P4/mbm).

## Reproduction target
Using an open‑source plane‑wave DFT code and the PBE functional, compute the optimized lattice parameters, unit‑cell volume, total energy, and band gap for LuB₂C in the Pbam model and in the P4/mbm model. Then compute the relative energy ΔE = E(Pbam) – E(P4/mbm). The results must be written to the three JSON output files specified in the workflow steps.

## Assets

- Quantum ESPRESSO (or equivalent open-source plane-wave DFT code supporting PBE): https://www.quantum-espresso.org
- Pseudopotentials (e.g., SSSP PBEsol efficiency library or standard PBE pseudopotentials for Lu, B, C): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Construct initial DFT input geometries for LuB₂C in the orthorhombic Pbam structure (using the published experimental lattice parameters a=6.7429 Å, b=6.7341 Å, c=3.5890 Å and atomic coordinates) and the hypothetical tetragonal P4/mbm structure (Coloring II).
- Evidence: `/app/outputs/structural_inputs.generated`

### Step 2: Optimize LuB₂C in Pbam
- Role: scored (load-bearing)
- Action: Perform a DFT geometry optimization (relax atomic positions and cell) for LuB₂C in the Pbam structure using the PBE functional. Compute the electronic density of states (DOS) to determine the band gap. Report the final optimized lattice parameters, unit-cell volume, total energy, and band gap.
- Output file: `/app/outputs/step_01_lu_b2c_Pbam_opt.json`
- Format: json
- Contract: {"lattice_a_ang": 6.65, "lattice_b_ang": 6.77, "lattice_c_ang": 3.63, "volume_ang3": 163.5, "total_energy_ev": -1234.56, "band_gap_ev": 0.0}
- Scoring: scored by hidden verifier

### Step 3: Optimize LuB₂C in P4/mbm
- Role: scored (load-bearing)
- Action: Perform a DFT geometry optimization of the hypothetical P4/mbm structure (Coloring II) using the same functional and pseudopotentials as step 1. Compute the DOS and report the optimized lattice parameters, volume, total energy, and band gap.
- Output file: `/app/outputs/step_02_lu_b2c_P4mbm_opt.json`
- Format: json
- Contract: {"lattice_a_ang": 6.67, "lattice_b_ang": 6.67, "lattice_c_ang": 3.74, "volume_ang3": 166.0, "total_energy_ev": -1233.85, "band_gap_ev": 0.0}
- Scoring: scored by hidden verifier

### Step 4: Energy and electronic comparison
- Role: scored
- Action: Compute the relative total energy ΔE = E(Pbam) – E(P4/mbm) from steps 1 and 2. Summarize the optimized cell parameters, volumes, energy difference, and band gaps of both structures.
- Output file: `/app/outputs/step_03_results_summary.json`
- Format: json
- Contract: {"relative_energy_Pbam_minus_P4mbm_ev": 0.71, "band_gap_Pbam_ev": 0.0, "band_gap_P4mbm_ev": 0.0}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lu_b2c_Pbam_opt.json`
- `/app/outputs/step_02_lu_b2c_P4mbm_opt.json`
- `/app/outputs/step_03_results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lu_b2c_Pbam_opt.json
- path: `/app/outputs/step_01_lu_b2c_Pbam_opt.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters, volume, total energy, and band gap for the Pbam coloring.
- schema:
  - `type`: object
  - `required`:
    - `lattice_a_ang`: number (unit: angstrom)
    - `lattice_b_ang`: number (angstrom)
    - `lattice_c_ang`: number (angstrom)
    - `volume_ang3`: number (angstrom³)
    - `total_energy_ev`: number (eV)
    - `band_gap_ev`: number (eV)

### step_02_lu_b2c_P4mbm_opt.json
- path: `/app/outputs/step_02_lu_b2c_P4mbm_opt.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters, volume, total energy, and band gap for the P4/mbm coloring.
- schema:
  - `type`: object
  - `required`:
    - `lattice_a_ang`: number (angstrom)
    - `lattice_b_ang`: number (angstrom)
    - `lattice_c_ang`: number (angstrom)
    - `volume_ang3`: number (angstrom³)
    - `total_energy_ev`: number (eV)
    - `band_gap_ev`: number (eV)

### step_03_results_summary.json
- path: `/app/outputs/step_03_results_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative total energy and band gaps summary.
- schema:
  - `type`: object
  - `required`:
    - `relative_energy_Pbam_minus_P4mbm_ev`: number (eV)
    - `band_gap_Pbam_ev`: number (eV)
    - `band_gap_P4mbm_ev`: number (eV)

Notes: The checker compares the reported lattice parameters, volumes, energy difference, and band gaps to the paper's DFT-optimized values (hidden references) with tolerance appropriate for different DFT codes. Metallic behavior is confirmed by band gap ≤ 0.1 eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lu_b2c_Pbam_opt.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_a_ang": "number (unit: angstrom)",
          "lattice_b_ang": "number (angstrom)",
          "lattice_c_ang": "number (angstrom)",
          "volume_ang3": "number (angstrom³)",
          "total_energy_ev": "number (eV)",
          "band_gap_ev": "number (eV)"
        }
      },
      "description": "Optimized lattice parameters, volume, total energy, and band gap for the Pbam coloring."
    },
    {
      "file": "step_02_lu_b2c_P4mbm_opt.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_a_ang": "number (angstrom)",
          "lattice_b_ang": "number (angstrom)",
          "lattice_c_ang": "number (angstrom)",
          "volume_ang3": "number (angstrom³)",
          "total_energy_ev": "number (eV)",
          "band_gap_ev": "number (eV)"
        }
      },
      "description": "Optimized lattice parameters, volume, total energy, and band gap for the P4/mbm coloring."
    },
    {
      "file": "step_03_results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "relative_energy_Pbam_minus_P4mbm_ev": "number (eV)",
          "band_gap_Pbam_ev": "number (eV)",
          "band_gap_P4mbm_ev": "number (eV)"
        }
      },
      "description": "Relative total energy and band gaps summary."
    }
  ],
  "notes": "The checker compares the reported lattice parameters, volumes, energy difference, and band gaps to the paper's DFT-optimized values (hidden references) with tolerance appropriate for different DFT codes. Metallic behavior is confirmed by band gap ≤ 0.1 eV."
}
```

## How you are scored
The hidden verifier independently reads your three output files: step_01_lu_b2c_Pbam_opt.json, step_02_lu_b2c_P4mbm_opt.json, and step_03_results_summary.json. It compares your reported lattice parameters, volumes, total energies, energy difference, and band gaps against hidden reference targets with tolerances that account for differences between DFT codes and pseudopotentials. Each artifact is scored and the final reward is the weighted sum of per‑artifact scores. Simply writing plausible numbers will not suffice — the results must be genuine DFT‑computed quantities that are consistent with the specified functional and structures.
