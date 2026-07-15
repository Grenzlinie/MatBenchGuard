# DFT-PBE0 Relative Stability of Candidate Silicon Allotropes from a Layered Polyanionic Network

## Problem background
The Zintl phase Li₃NaSi₆ contains polyanionic silicon layers with a characteristic topology of four-, three-, and two-bonded Si atoms. Chemical extraction of the alkali metals could, in principle, lead to a new silicon allotrope formed by topotactic combination of these layers. To assess the energetic plausibility of such allotropes, quantum‑chemical calculations can evaluate the relative stability of candidate framework structures derived from the Si substructure. One set of model structures (designated SA, SB, SC, SD) was proposed in the public literature by mapping the layer connectivity onto three‑dimensional networks. The task is to compute the relative energies of these candidate allotropes with respect to the ground‑state diamond‑cubic α‑Si phase.

## Approach
The computational approach uses hybrid density functional theory (DFT) with the PBE0 functional and a split‑valence plus polarisation (SVP) basis set for silicon. First, the diamond‑cubic α‑Si reference structure is fully geometry‑optimised (lattice parameters and atomic positions) and its total energy per Si atom recorded. Then each of the four S‑type candidate structures (SA, SB, SC, SD) is geometry‑optimised under its space‑group constraints at the same level of theory, and its energy per Si atom is obtained. Finally, the relative energy of each candidate is computed as ΔE = (E_allotrope − E_α‑Si) and converted to kJ mol⁻¹ per Si atom. All structures are publicly known: the coordinates of the S‑type allotropes are available from the literature (Conesa 2002), and α‑Si is a standard crystallographic structure.

## Reproduction target
Produce a CSV file `relative_energies.csv` containing the computed relative total energies per Si atom (kJ mol⁻¹) for the four S‑type allotropes (SA, SB, SC, SD) with respect to diamond‑cubic α‑Si, obtained from geometry optimisations at the PBE0/SVP level. The file must have columns: `structure` (one of SA, SB, SC, SD) and `energy_rel_alpha_Si` (a floating‑point number).

## Assets

- S-type Si allotrope coordinates (Conesa 2002): 10.1021/jp013380m
- Diamond-cubic α-Si crystal structure: ICSD 51688
- SVP basis set for Si: https://www.basissetexchange.org/
- Open-source DFT code with PBE0 support: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare Si allotrope structures
- Role: process
- Action: Obtain the atomic coordinates of the four S-type Si allotropes (SA, SB, SC, SD) from the public literature and the diamond-cubic α-Si reference structure. Generate geometry input files suitable for a chosen DFT code, specifying the PBE0 hybrid functional and the SVP basis set for Si.
- Evidence: none

### Step 2: Optimize α-Si reference
- Role: process
- Action: Perform a full geometry optimization (lattice parameters and atomic positions) of diamond-cubic α-Si using the PBE0 hybrid functional and the SVP basis set. Record the final total energy per Si atom.
- Evidence: `/app/outputs/alpha_si_energy.json`

### Step 3: Optimize S-type Si allotropes
- Role: process
- Action: For each of the four S-type structures (SA, SB, SC, SD), perform a geometry optimization under space-group constraints using the same DFT method (PBE0/SVP). Record the final total energy per Si atom for each optimized structure.
- Evidence: `/app/outputs/allotrope_energies.json`

### Step 4: Compute relative energies
- Role: scored (load-bearing)
- Action: Calculate the relative energy per Si atom (ΔE = E_allotrope − E_α-Si) for each S-type structure and convert to kJ mol⁻¹ per Si. Output the results in a CSV file.
- Output file: `/app/outputs/relative_energies.csv`
- Format: csv
- Contract: CSV file with header: structure,energy_rel_alpha_Si. structure is one of SA,SB,SC,SD; energy_rel_alpha_Si is a float (kJ mol⁻¹ per Si).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.csv
- path: `/app/outputs/relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relative total energies of the four S-type Si allotropes (SA, SB, SC, SD) with respect to diamond-cubic α-Si, computed at PBE0/SVP level. The checker compares each energy to a hidden gold value and verifies that SD is the most stable.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `energy_rel_alpha_Si`
  - `units`:
    - `energy_rel_alpha_Si`: kJ mol⁻¹ per Si atom

Notes: The hidden checker performs an exact-match comparison against the published values with a tolerance that absorbs toolchain spread. It also checks the relative ordering to ensure SD has the lowest energy. The agent must therefore produce physically reasonable energies from the DFT workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "energy_rel_alpha_Si"
        ],
        "units": {
          "energy_rel_alpha_Si": "kJ mol⁻¹ per Si atom"
        }
      },
      "description": "Relative total energies of the four S-type Si allotropes (SA, SB, SC, SD) with respect to diamond-cubic α-Si, computed at PBE0/SVP level. The checker compares each energy to a hidden gold value and verifies that SD is the most stable."
    }
  ],
  "notes": "The hidden checker performs an exact-match comparison against the published values with a tolerance that absorbs toolchain spread. It also checks the relative ordering to ensure SD has the lowest energy. The agent must therefore produce physically reasonable energies from the DFT workflow."
}
```

## How you are scored
A hidden verifier will read your `relative_energies.csv` and evaluate the reported energies. It compares each computed `energy_rel_alpha_Si` to a set of reference values obtained from consistent DFT computations and checks whether the allotrope with the lowest energy is correctly identified. Your reward is computed from the agreement between your values and the reference, and degrades as deviations increase or the ordering is incorrect. The precise comparison tolerances and reference values are not disclosed; producing energies from a correct DFT workflow that faithfully follows the prescribed protocol will yield a high score. The file must strictly conform to the output contract; formatting errors also reduce the score.
