# Magnetism in Cr-doped ZnO: a first-principles reproduction

## Problem background
ZnO-based diluted magnetic semiconductors are under active investigation for spintronic applications because they combine semiconducting behaviour with ferromagnetic ordering. Cr doping is one route to introduce magnetic moments, and codoping with Al has been proposed to modify the magnetic stability. The key open questions are: what total magnetic moment arises when Zn is substituted by Cr, how do local atomic magnetic moments distribute (particularly on Cr and on bridging O atoms), and how does Al codoping affect the relative stability of ferromagnetic (FM) versus antiferromagnetic (AFM) spin configurations? This task targets these quantities through first-principles density-functional theory (DFT) calculations.

## Approach
Spin-polarised DFT calculations with the generalised-gradient approximation (GGA-PBE) are used to study wurtzite ZnO. A bulk primitive cell is optimised, then a 2×2×2 supercell is built. Two Zn atoms are substituted by Cr to model Cr-monodoped ZnO, with two spatial arrangements: near (Cr atoms bridged by one O) and far (Cr atoms bridged by -O-Zn-O-). For the codoped case, one additional Zn is replaced by Al in the far arrangement. For each defect supercell, geometry relaxation is performed, followed by self-consistent field (SCF) calculations for both FM and AFM spin orderings. Total magnetic moments and local atomic moments are extracted from the spin-polarised charge density. FM-AFM energy differences ΔE = E_AFM − E_FM are computed as an indicator of magnetic stability. All calculations use open-source tools (Quantum ESPRESSO) and public pseudopotentials (SSSP efficiency library).

## Reproduction target
Using DFT, compute: (i) the total magnetic moment per supercell (μB), the local magnetic moment on each Cr atom (μB), and the local magnetic moment on the bridging O atom (μB) for the FM state of the near Cr-monodoped configuration; (ii) the FM-AFM energy differences ΔE (meV) for the near and far Cr-monodoped configurations; and (iii) the FM-AFM energy difference ΔE (meV) for the far (Cr,Al)-codoped configuration. Report these results in the two scored JSON files: monodoped_results.json and codoped_results.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Wurtzite ZnO crystal structure

## Workflow steps

### Step 1: Bulk ZnO primitive cell optimization
- Role: process
- Action: Perform DFT geometry optimization of the wurtzite ZnO primitive cell using Quantum ESPRESSO with GGA-PBE functional and SSSP pseudopotentials. Relax both atomic positions and cell parameters to obtain optimized lattice constants. Record the optimization log.
- Evidence: `/app/outputs/bulk_optimization.log`

### Step 2: Defect supercell construction
- Role: process
- Action: From the optimized ZnO primitive cell, build a 2×2×2 supercell. Substitute two Zn atoms with Cr to create near-configuration (Cr atoms separated by one O) and far-configuration (Cr atoms separated by -O-Zn-O-) models for monodoped case. For the codoped far configuration, additionally replace one Zn with Al. Produce a CIF or equivalent structure file for each configuration.
- Evidence: `/app/outputs/defect_supercells.cif`

### Step 3: Relaxation of defect supercells
- Role: process
- Action: Perform full geometry relaxation (atomic positions and cell parameters) for each of the three defect supercells using spin-polarized DFT. Use the same exchange-correlation functional, cutoff energy, and k-point grid as in the bulk optimization. Save the relaxation logs.
- Evidence: `/app/outputs/relax_defects.log`

### Step 4: Compute monodoped energies and magnetic moments
- Role: scored (load-bearing)
- Action: For the near and far monodoped relaxed supercells, perform spin-polarized self-consistent field (SCF) calculations for both ferromagnetic (FM) and antiferromagnetic (AFM) spin orderings. Extract the total energies and compute the FM-AFM energy difference per configuration. From the FM SCF run, extract the total magnetic moment per supercell and the local magnetic moments on each Cr and on the bridging O atom. Write the results to a JSON file.
- Output file: `/app/outputs/monodoped_results.json`
- Format: json
- Contract: {"total_moment_muB": "float", "local_moment_Cr_muB": "float", "local_moment_bridging_O_muB": "float", "energy_difference_near_meV": "float", "energy_difference_far_meV": "float"}
- Scoring: scored by hidden verifier

### Step 5: Compute codoped energy difference
- Role: scored (load-bearing)
- Action: For the relaxed codoped far supercell, perform spin-polarized SCF calculations for FM and AFM orderings, then compute the FM-AFM energy difference. Write the result to a JSON file.
- Output file: `/app/outputs/codoped_results.json`
- Format: json
- Contract: {"energy_difference_codoped_far_meV": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monodoped_results.json`
- `/app/outputs/codoped_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monodoped_results.json
- path: `/app/outputs/monodoped_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the total and local magnetic moments and FM-AFM energy differences for the monodoped supercell configurations.
- schema:
  - `type`: object
  - `required`:
    - `total_moment_muB`: number
    - `local_moment_Cr_muB`: number
    - `local_moment_bridging_O_muB`: number
    - `energy_difference_near_meV`: number
    - `energy_difference_far_meV`: number
  - `units`:
    - `total_moment_muB`: μB
    - `local_moment_Cr_muB`: μB
    - `local_moment_bridging_O_muB`: μB
    - `energy_difference_near_meV`: meV
    - `energy_difference_far_meV`: meV

### codoped_results.json
- path: `/app/outputs/codoped_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the FM-AFM energy difference for the (Cr,Al)-codoped far supercell configuration.
- schema:
  - `type`: object
  - `required`:
    - `energy_difference_codoped_far_meV`: number
  - `units`:
    - `energy_difference_codoped_far_meV`: meV

Notes: All magnetic moments are in units of Bohr magneton (μB) and energy differences in milli-electronvolts (meV). The hidden checker compares each reported value to the paper's reference values within predefined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monodoped_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "total_moment_muB": "number",
          "local_moment_Cr_muB": "number",
          "local_moment_bridging_O_muB": "number",
          "energy_difference_near_meV": "number",
          "energy_difference_far_meV": "number"
        },
        "units": {
          "total_moment_muB": "μB",
          "local_moment_Cr_muB": "μB",
          "local_moment_bridging_O_muB": "μB",
          "energy_difference_near_meV": "meV",
          "energy_difference_far_meV": "meV"
        }
      },
      "description": "Scored artifact containing the total and local magnetic moments and FM-AFM energy differences for the monodoped supercell configurations."
    },
    {
      "file": "codoped_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "energy_difference_codoped_far_meV": "number"
        },
        "units": {
          "energy_difference_codoped_far_meV": "meV"
        }
      },
      "description": "Scored artifact containing the FM-AFM energy difference for the (Cr,Al)-codoped far supercell configuration."
    }
  ],
  "notes": "All magnetic moments are in units of Bohr magneton (μB) and energy differences in milli-electronvolts (meV). The hidden checker compares each reported value to the paper's reference values within predefined tolerances."
}
```

## How you are scored
An automated verifier reads your submitted JSON files. Each reported quantity (total moment, local moments, and both energy differences) is compared to a hidden reference value. Full credit is awarded when your result lies within a predefined tolerance of the reference; partial credit degrades as the result deviates further. The final reward is a weighted sum of the scores for the individual quantities. The verifier is self-contained and does not require any external data. Reporting numbers alone is not sufficient—the hidden checker validates that the results originate from a genuine DFT workflow, but the primary scoring is based on the values in the JSON files.
