# Electronic Structure and Bonding Analysis of CuTe2 and Cu7Te4

## Problem background
Copper tellurides CuTe2 and Cu7Te4 are of interest for understanding the electronic structure and the nature of chemical bonding in transition-metal chalcogenides. This task will determine whether they are metallic or insulating by computing the band gap and Fermi-level density of states, and will quantify the bonding interactions (Cu–Te, Cu–Cu, Te–Te) using crystal orbital Hamilton population (COHP) analysis.

## Approach
Use density functional theory (DFT) in the local density approximation (LDA) to compute the electronic structure. Start from experimentally determined crystal structures (CuTe2 and Cu7Te4) obtained from public databases. Perform spin-unpolarized self-consistent field calculations to obtain the ground-state charge density and wavefunction. From the converged solution, compute the electronic band structure along high-symmetry paths and the total density of states. In addition, carry out a chemical bonding analysis using the crystal orbital Hamilton population (COHP) method to quantify pair interactions (Cu–Te, Cu–Cu, Te–Te) and integrate the COHP up to the Fermi energy. The workflow yields the band gap, the Fermi-level density of states, and integrated COHP values that characterise the bonding network.

## Reproduction target
For both CuTe2 and Cu7Te4, compute and report:
- the band gap (eV) and the density of states at the Fermi level (states/eV per unit cell), to be written to `/app/outputs/electronic_structure_results.json`.
- the integrated COHP (ICOHP) values (eV per bond) for Cu–Te, Cu–Cu, and Te–Te pair interactions, to be written to `/app/outputs/bonding_analysis.json`.
The results must show whether each compound is metallic or insulating and whether the Cu–Te interactions are net bonding below the Fermi level, according to the expected physical signatures of the COHP method.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LOBSTER: https://www.cohp.de/
- LDA pseudopotentials (Cu, Te): https://www.materialscloud.org/discover/sssp/
- Crystal structures of CuTe2 and Cu7Te4: https://materialsproject.org/

## Workflow steps

### Step 1: Fetch crystal structures
- Role: process
- Action: Download crystal structures (unit cell parameters, atomic positions) for CuTe2 and Cu7Te4 from a public database (e.g., Materials Project) and prepare input files for DFT calculations. Use the LDA exchange-correlation functional.
- Evidence: `/app/outputs/structures_used.json`

### Step 2: DFT self-consistent field calculation
- Role: process
- Action: Perform a spin-unpolarized DFT self-consistent field calculation using the LDA exchange-correlation functional (e.g., with Quantum ESPRESSO) for each compound. Use a converged k-point grid and plane-wave cutoff to obtain self-consistent charge density and wavefunction.
- Evidence: `/app/outputs/dft_scf.log`

### Step 3: Compute band structure and density of states
- Role: scored (load-bearing)
- Action: Using the converged wavefunction from the SCF calculation, compute the electronic band structure along standard high-symmetry paths and the total (and optionally projected) density of states. Determine the band gap and the density of states at the Fermi level. Write results as electronic_structure_results.json.
- Output file: `/app/outputs/electronic_structure_results.json`
- Format: json
- Contract: {"CuTe2": {"band_gap_eV": "float", "dos_at_fermi_states_eV_cell": "float"}, "Cu7Te4": {"band_gap_eV": "float", "dos_at_fermi_states_eV_cell": "float"}}
- Scoring: scored by hidden verifier

### Step 4: Chemical bonding analysis (COHP)
- Role: scored
- Action: Using the DFT wavefunction and the LOBSTER code, compute crystal orbital Hamilton populations for Cu-Te, Cu-Cu, and Te-Te pair interactions. Integrate the COHP up to the Fermi energy to obtain integrated COHP (ICOHP) values. Write results as bonding_analysis.json.
- Output file: `/app/outputs/bonding_analysis.json`
- Format: json
- Contract: {"CuTe2": {"Cu_Te_ICOHP_eV_bond": "float", "Cu_Cu_ICOHP_eV_bond": "float", "Te_Te_ICOHP_eV_bond": "float"}, "Cu7Te4": {"Cu_Te_ICOHP_eV_bond": "float", "Cu_Cu_ICOHP_eV_bond": "float", "Te_Te_ICOHP_eV_bond": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_structure_results.json`
- `/app/outputs/bonding_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_structure_results.json
- path: `/app/outputs/electronic_structure_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Band gap and Fermi-level DOS for both compounds; the checker verifies physical plausibility.
- schema:
  - `type`: object
  - `required`:
    - `CuTe2`:
      - `type`: object
      - `required`: `band_gap_eV`, `dos_at_fermi_states_eV_cell`
      - `units`:
        - `band_gap_eV`: eV
        - `dos_at_fermi_states_eV_cell`: states/eV/cell
    - `Cu7Te4`:
      - `type`: object
      - `required`: `band_gap_eV`, `dos_at_fermi_states_eV_cell`
      - `units`:
        - `band_gap_eV`: eV
        - `dos_at_fermi_states_eV_cell`: states/eV/cell

### bonding_analysis.json
- path: `/app/outputs/bonding_analysis.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: ICOHP values for pair interactions; the checker verifies bonding character consistency.
- schema:
  - `type`: object
  - `required`:
    - `CuTe2`:
      - `type`: object
      - `required`: `Cu_Te_ICOHP_eV_bond`, `Cu_Cu_ICOHP_eV_bond`, `Te_Te_ICOHP_eV_bond`
      - `units`:
        - `Cu_Te_ICOHP_eV_bond`: eV/bond
        - `Cu_Cu_ICOHP_eV_bond`: eV/bond
        - `Te_Te_ICOHP_eV_bond`: eV/bond
    - `Cu7Te4`:
      - `type`: object
      - `required`: `Cu_Te_ICOHP_eV_bond`, `Cu_Cu_ICOHP_eV_bond`, `Te_Te_ICOHP_eV_bond`
      - `units`:
        - `Cu_Te_ICOHP_eV_bond`: eV/bond
        - `Cu_Cu_ICOHP_eV_bond`: eV/bond
        - `Te_Te_ICOHP_eV_bond`: eV/bond

Notes: The agent must run the full DFT workflow: structural retrieval, SCF, band/DOS calculation, and COHP analysis. Only the final JSON artifacts are submitted for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "CuTe2": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "dos_at_fermi_states_eV_cell"
            ],
            "units": {
              "band_gap_eV": "eV",
              "dos_at_fermi_states_eV_cell": "states/eV/cell"
            }
          },
          "Cu7Te4": {
            "type": "object",
            "required": [
              "band_gap_eV",
              "dos_at_fermi_states_eV_cell"
            ],
            "units": {
              "band_gap_eV": "eV",
              "dos_at_fermi_states_eV_cell": "states/eV/cell"
            }
          }
        }
      },
      "description": "Band gap and Fermi-level DOS for both compounds; the checker verifies physical plausibility."
    },
    {
      "file": "bonding_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "CuTe2": {
            "type": "object",
            "required": [
              "Cu_Te_ICOHP_eV_bond",
              "Cu_Cu_ICOHP_eV_bond",
              "Te_Te_ICOHP_eV_bond"
            ],
            "units": {
              "Cu_Te_ICOHP_eV_bond": "eV/bond",
              "Cu_Cu_ICOHP_eV_bond": "eV/bond",
              "Te_Te_ICOHP_eV_bond": "eV/bond"
            }
          },
          "Cu7Te4": {
            "type": "object",
            "required": [
              "Cu_Te_ICOHP_eV_bond",
              "Cu_Cu_ICOHP_eV_bond",
              "Te_Te_ICOHP_eV_bond"
            ],
            "units": {
              "Cu_Te_ICOHP_eV_bond": "eV/bond",
              "Cu_Cu_ICOHP_eV_bond": "eV/bond",
              "Te_Te_ICOHP_eV_bond": "eV/bond"
            }
          }
        }
      },
      "description": "ICOHP values for pair interactions; the checker verifies bonding character consistency."
    }
  ],
  "notes": "The agent must run the full DFT workflow: structural retrieval, SCF, band/DOS calculation, and COHP analysis. Only the final JSON artifacts are submitted for scoring."
}
```

## How you are scored
A hidden verifier will inspect your submitted `electronic_structure_results.json` and `bonding_analysis.json`. It evaluates whether your computed band gap and density of states fall within physically plausible ranges for the studied materials, and whether the bonding analysis is consistent with chemical bonding expectations. Both output files contribute to the final reward score. You are not required to match a specific published number; the verifier assesses whether your computed quantities are compatible with the physical claims the experiment is designed to test.
