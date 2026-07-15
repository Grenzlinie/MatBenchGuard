# DFT-Based O2 Activation and CO Oxidation on CuTCNQ Surface

## Problem background
Low-temperature oxidation of carbon monoxide (CO) is important for air pollution control. The paper reports that CuTCNQ nanowire arrays (a metal–organic charge-transfer complex) exhibit catalytic CO oxidation activity at low temperatures. To understand the origin of this activity, density functional theory (DFT) calculations were performed to investigate the mechanism of O2 activation and subsequent CO oxidation on the CuTCNQ surface. Your task is to reproduce the computed energetic profile and key structural changes that underpin the proposed catalytic cycle.

## Approach
The computational approach uses first-principles DFT with a periodic slab model. Starting from the crystallographic structure of CuTCNQ, a (2×2×1) supercell is constructed and a vacuum layer is added to represent the surface. The energies of the clean slab, isolated gas-phase O2 and CO, and all reaction intermediates along an Eley–Rideal mechanism are calculated. Adsorption energies are obtained as the energy difference relative to the bare slab plus the isolated gas-phase molecules. Two alternative pathways after CO addition to the activated O2 are considered, denoted the 'red' and 'blue' pathways. The C≡N bond length is tracked as a structural marker of O2 activation. This set of calculations yields the energy profile and structural parameters that characterize the reaction.

## Reproduction target
Your goal is to compute and report the following quantities from DFT: (1) the optimized lattice parameters a, b, c of the CuTCNQ unit cell; (2) the C≡N bond length in the bare optimized CuTCNQ surface; (3) the adsorption energies (in eV) for O2 approaching the surface (state i), O2 activated at the C≡N bond (state ii), and CO adsorbed on the activated O2 (state iii); (4) the adsorption energies for the red pathway intermediates (states iv, v, FS) and the blue pathway intermediates (states vi, vii, FS); and (5) the C≡N bond length in the O2-activated state ii. All energies are referenced to the clean slab and gas-phase molecules. The results are collected in the scored output file dft_results.json as detailed in the Workflow steps below.

## Assets

- CuTCNQ crystal structure (primitive cell): https://www.ccdc.cam.ac.uk/structures/
- Open-source DFT code that supports PBE plane-wave calculations (e.g., Quantum ESPRESSO, ABINIT, GPAW). You may use any such code; the original paper used VASP, but VASP is commercial and not required. For instance, Quantum ESPRESSO can be installed from https://www.quantum-espresso.org/.
- PBE pseudopotentials appropriate for the chosen code (e.g., SSSP efficiency/precision library for Quantum ESPRESSO, available at https://www.materialscloud.org/discover/sssp/). Any standard PBE pseudopotential set (SSSP, PseudoDojo, GBRV) is acceptable.

## Workflow steps

### Step 1: DFT optimization of CuTCNQ unit cell and supercell
- Role: process
- Action: Perform DFT geometry optimization of the CuTCNQ unit cell using PBE functional, plane-wave cutoff, and k-point sampling to obtain optimized lattice parameters a, b, c. Then build a (2×2×1) supercell and add approximately 15 Å vacuum to create a slab model for subsequent surface reaction calculations.
- Evidence: `/app/outputs/cu_tcnq_optimized.cif`

### Step 2: O2 activation and CO oxidation reaction pathway on CuTCNQ
- Role: scored (load-bearing)
- Action: Using the optimized CuTCNQ supercell from step 01, compute the adsorption energies and structural changes for the O2 activation and CO oxidation pathway via the Eley-Rideal mechanism. Calculate: (1) bare surface energy and gas-phase reference energies for O2 and CO; (2) O2 adsorption near the surface (state i); (3) activated O2 at the C≡N bond (state ii) energy and the elongated C≡N bond length; (4) CO adsorption on activated O2 (state iii) energy; (5) red pathway: energies of state iv, state v, and final state (FS); (6) blue pathway: energies of state vi, state vii, and FS. All adsorption energies are relative to the bare slab plus isolated gas-phase molecules. Also report the optimized cell parameters and the C≡N bond length in the bare CuTCNQ surface.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: A JSON object with exactly the following keys: cell_params (object with a,b,c in Å), bare_C_N_bond_length (float, Å), state_i_energy (float, eV), state_ii_energy (float, eV), state_ii_C_N_bond_length (float, Å), state_iii_energy (float, eV), red_path_iv_energy (float, eV), red_path_v_energy (float, eV), red_path_FS_energy (float, eV), blue_path_vi_energy (float, eV), blue_path_vii_energy (float, eV), blue_path_FS_energy (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scoring compares each energy and bond length against paper-reported reference values using predefined tolerances, and checks that the red pathway is energetically preferred over the blue pathway (structural ordering).
- schema:
  - `type`: object
  - `required`:
    - `cell_params`: object (with keys a, b, c in Angstrom)
    - `bare_C_N_bond_length`: float (Angstrom)
    - `state_i_energy`: float (eV)
    - `state_ii_energy`: float (eV)
    - `state_ii_C_N_bond_length`: float (Angstrom)
    - `state_iii_energy`: float (eV)
    - `red_path_iv_energy`: float (eV)
    - `red_path_v_energy`: float (eV)
    - `red_path_FS_energy`: float (eV)
    - `blue_path_vi_energy`: float (eV)
    - `blue_path_vii_energy`: float (eV)
    - `blue_path_FS_energy`: float (eV)

Notes: All energies are in eV and bond lengths in Angstrom. The checker will apply tolerances appropriate for DFT re-computation and verify relative ordering to determine the minimum energy pathway.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "cell_params": "object (with keys a, b, c in Angstrom)",
          "bare_C_N_bond_length": "float (Angstrom)",
          "state_i_energy": "float (eV)",
          "state_ii_energy": "float (eV)",
          "state_ii_C_N_bond_length": "float (Angstrom)",
          "state_iii_energy": "float (eV)",
          "red_path_iv_energy": "float (eV)",
          "red_path_v_energy": "float (eV)",
          "red_path_FS_energy": "float (eV)",
          "blue_path_vi_energy": "float (eV)",
          "blue_path_vii_energy": "float (eV)",
          "blue_path_FS_energy": "float (eV)"
        }
      },
      "description": "Scoring compares each energy and bond length against paper-reported reference values using predefined tolerances, and checks that the red pathway is energetically preferred over the blue pathway (structural ordering)."
    }
  ],
  "notes": "All energies are in eV and bond lengths in Angstrom. The checker will apply tolerances appropriate for DFT re-computation and verify relative ordering to determine the minimum energy pathway."
}
```

## How you are scored
A hidden checker will read your dft_results.json and compare each reported quantity against reference values using pre-defined tolerances that absorb the spread typical of independent DFT re-implementations. The checker will also verify the correct relative ordering between the red and blue pathways. Each check contributes to the final score; full credit requires physically correct results, not merely reporting the paper's numbers. No credit is given for formats or shapes alone; the computed values must be numerically plausible.
