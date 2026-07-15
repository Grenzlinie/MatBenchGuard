# Li-ion migration barrier in Na-doped LiFePO4 via DFT-NEB

## Problem background
Lithium iron phosphate (LiFePO4) is a promising solid-state electrolyte for lithium metal batteries, but its low ionic conductivity is a major limitation. Doping with sodium (Na) has been proposed to improve Li‑ion transport. Density functional theory (DFT) calculations combined with the nudged elastic band (NEB) method can quantify the effect of Na substitution on the Li‑ion migration energy barrier by comparing the barrier in pristine LiFePO4 with the barrier for a Li hop near a Na‑occupied site. This reproduction computes those barriers to assess whether Na doping enhances Li‑ion diffusion.

## Approach
Build two supercells: pristine LiFePO₄ containing 16 formula units (Li₁₆Fe₁₆P₁₆O₆₄) and Na‑doped LiFePO₄ (Li₁₅NaFe₁₆P₁₆O₆₄) where one Li at a 4a crystallographic site is replaced by Na. Perform DFT geometry optimizations on both supercells using the GGA‑PBE exchange‑correlation functional with a plane‑wave basis. After confirming that Na occupies the intended 4a site and that the three‑dimensional Li‑ion transport channels remain unblocked, use the NEB method to find the minimum‑energy path for a Li hop between two neighboring 4a sites. Run the NEB calculation for a hop in pristine LFP and for a hop adjacent to the Na impurity in the doped system. Extract the migration energy barriers (eV) from the energy profiles and report them as the primary result.

## Reproduction target
Compute the Li‑ion migration energy barrier (eV) for a hop between neighboring 4a sites in pristine LiFePO₄ (Li₁₆Fe₁₆P₁₆O₆₄) and for a hop adjacent to a Na‑occupied 4a site in Na‑doped LiFePO₄ (Li₁₅NaFe₁₆P₁₆O₆₄). Use an open‑source plane‑wave DFT code with the GGA‑PBE functional and the NEB method. Provide the two barriers in a JSON file named migration_barriers.json with keys LFP_pristine_barrier_eV and LNFP_doped_local_barrier_eV, each a floating‑point number in eV.

## Assets

- LiFePO4 olivine crystal structure: https://materialsproject.org/materials/mp-19017/
- Quantum ESPRESSO: https://www.quantum-espresso.org
- GGA-PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build pristine and Na-doped supercells
- Role: process
- Action: Construct a supercell for pristine LFP containing 16 formula units (Li16Fe16P16O64) and a Na-doped supercell (Li15NaFe16P16O64) by substituting one Li at a 4a site with Na. Generate atomic coordinates for both supercells.
- Evidence: `/app/outputs/supercell_structures.json`

### Step 2: DFT geometry optimization of pristine LFP
- Role: process
- Action: Run DFT geometry optimization on the pristine LFP supercell using Quantum ESPRESSO with GGA-PBE functional. Use a sufficiently high plane-wave cutoff and k-point mesh to converge forces and energy.
- Evidence: `/app/outputs/optimized_lfp_structure.json`

### Step 3: DFT geometry optimization of Na-doped LNFP
- Role: process
- Action: Run DFT geometry optimization on the Na-doped LNFP supercell using the same computational parameters as for the pristine LFP.
- Evidence: `/app/outputs/optimized_lnfp_structure.json`

### Step 4: Verify Na site occupancy
- Role: process
- Action: Analyze the relaxed LNFP structure to confirm that Na occupies the original Li 4a crystallographic site. Provide a short report documenting the site assignment.
- Evidence: `/app/outputs/na_occupancy_report.txt`

### Step 5: Assess Li-ion transport channels
- Role: process
- Action: Inspect the relaxed LFP and LNFP structures to verify that the three-dimensional Li-ion transport channels are not blocked by Na substitution. Provide a brief report.
- Evidence: `/app/outputs/channel_assessment.txt`

### Step 6: NEB calculations and barrier extraction
- Role: scored (load-bearing)
- Action: For the optimized pristine LFP supercell, select two neighboring 4a Li sites as initial and final states. Perform an NEB calculation to find the minimum-energy path and extract the migration energy barrier (eV). Repeat for the Na-doped LNFP supercell, selecting a Li hop adjacent to the Na site. Write the two barriers to the output file.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: JSON object with keys 'LFP_pristine_barrier_eV' and 'LNFP_doped_local_barrier_eV', each a float in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The Li-ion migration energy barriers computed from NEB for the pristine LFP system and for the Na-doped LNFP system near the Na-occupied site.
- schema:
  - `type`: object
  - `required`:
    - `LFP_pristine_barrier_eV`: float
    - `LNFP_doped_local_barrier_eV`: float
  - `items`: object
  - `units`:
    - `LFP_pristine_barrier_eV`: eV
    - `LNFP_doped_local_barrier_eV`: eV

Notes: The checker compares the two barrier values to the paper's reported values within a tolerance. No other files are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LFP_pristine_barrier_eV": "float",
          "LNFP_doped_local_barrier_eV": "float"
        },
        "items": {},
        "units": {
          "LFP_pristine_barrier_eV": "eV",
          "LNFP_doped_local_barrier_eV": "eV"
        }
      },
      "description": "The Li-ion migration energy barriers computed from NEB for the pristine LFP system and for the Na-doped LNFP system near the Na-occupied site."
    }
  ],
  "notes": "The checker compares the two barrier values to the paper's reported values within a tolerance. No other files are required."
}
```

## How you are scored
A hidden verifier reads the output artifacts and compares the reported migration barriers to a hidden reference. It also checks that all required intermediate evidence files (supercell structures, optimized geometries, site occupancy report, channel assessment) are present and properly formatted. The final reward is a weighted combination of these assessments, with the migration barrier values carrying the highest weight. Simply reporting pre‑known numbers is not sufficient; you must execute the workflow described in the steps and produce a genuine computational result.
