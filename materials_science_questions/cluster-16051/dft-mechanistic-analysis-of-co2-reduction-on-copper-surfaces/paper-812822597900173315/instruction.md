# DFT Analysis of CO Adsorption Site Change on Cu-Ru Alloy Surfaces

## Problem background
Ru is the best monometallic catalyst for carbon monoxide (CO) oxidation but is expensive and scarce. Alloying Ru with inexpensive Cu to form solid-solution Cu-Ru nanoparticles can reduce cost and improve CO oxidation activity. The computational component of this study investigates how Cu substitution alters CO adsorption on Ru surface atoms by computing the preferred adsorption site and the C-O stretching vibrational frequency for a series of Cu-Ru alloy surfaces. These quantities are thought to be correlated with catalytic performance, making their reliable determination essential for understanding the alloying effect.

## Approach
Construct slab models of the fcc (111) surface for CuₓRu₁₋ₓ alloys with compositions x = 0 (pure Ru), 0.2, 0.5, 0.7, and 1.0 (pure Cu). Use lattice constants obtained by linear interpolation between fcc-Ru and fcc-Cu (Vegard's law). For each slab, place a CO molecule near Ru surface atoms at plausible adsorption geometries (hollow, top, bridge). Perform periodic DFT geometry optimization using the GGA-PBE functional with spin polarization and an appropriate dispersion correction, then identify the lowest-energy adsorption configuration. Compute the harmonic C-O stretching vibrational frequency on that optimized geometry. Finally, record the adsorption site of CO on Ru atoms (hollow or top) and the corresponding frequency for every composition.

## Reproduction target
Produce the file `/app/outputs/co_frequencies.csv` containing, for each alloy composition labeled 'Ru', 'Cu0.2Ru0.8', 'Cu0.5Ru0.5', 'Cu0.7Ru0.3', and 'Cu', the CO adsorption site on Ru atoms (either 'hollow' or 'top') and the harmonic C-O stretching vibrational frequency in units of cm⁻¹.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build fcc (111) slab models
- Role: process
- Action: Generate atomic slab models of fcc (111) surfaces for Ru, Cu, and CuxRu1-x alloys with x=0.2, 0.5, 0.7. Use lattice constants from Vegard's law (linear interpolation between fcc-Ru 3.805 Å and fcc-Cu 3.615 Å). Create slabs with at least four layers, a ~15 Å vacuum region, and fix the bottom two layers. Prepare DFT input files for subsequent geometry optimization.
- Evidence: `/app/outputs/slab_structures.zip`

### Step 2: DFT geometry optimization for CO adsorption
- Role: process
- Action: For each slab composition, place a CO molecule at plausible adsorption sites (hollow, top, bridge) near surface Ru atoms. Run DFT geometry optimization using GGA-PBE with spin polarization and an appropriate dispersion correction (e.g., DFT-D3). Identify the most stable adsorption geometry (lowest total energy) for each composition.
- Evidence: `/app/outputs/optimized_geometries.zip`

### Step 3: CO vibrational frequencies and site determination
- Role: scored (load-bearing)
- Action: For each composition, using the most stable optimized geometry, compute the harmonic C-O stretching frequency. Determine the adsorption site of CO on Ru atoms (hollow or top) from the final geometry. Write a comma-separated file with columns composition, adsorption_site, frequency_cm1. Compositions should be labeled as 'Ru', 'Cu0.2Ru0.8', 'Cu0.5Ru0.5', 'Cu0.7Ru0.3', 'Cu'.
- Output file: `/app/outputs/co_frequencies.csv`
- Format: csv
- Contract: CSV with columns: composition (string), adsorption_site (string, either 'hollow' or 'top'), frequency_cm1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/co_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### co_frequencies.csv
- path: `/app/outputs/co_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The table contains the predicted CO adsorption site on Ru atoms (hollow or top) and the harmonic C-O stretching frequency for each alloy composition. The checker will verify the structural trend: for pure Ru the site is hollow, for all Cu-substituted compositions the site is top, and the frequency increases monotonically with Cu content.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `adsorption_site`, `frequency_cm1`
  - `items`: object
  - `units`:
    - `frequency_cm1`: cm^{-1}

Notes: No absolute tolerance is applied to frequencies; scoring relies on the site assignment and the monotonic trend (blueshift) matching the paper's claim. The process steps produce intermediate evidence (slab_structures.zip, optimized_geometries.zip) that is not scored but is required for a correct final artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "co_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "adsorption_site",
          "frequency_cm1"
        ],
        "items": {},
        "units": {
          "frequency_cm1": "cm^{-1}"
        }
      },
      "description": "The table contains the predicted CO adsorption site on Ru atoms (hollow or top) and the harmonic C-O stretching frequency for each alloy composition. The checker will verify the structural trend: for pure Ru the site is hollow, for all Cu-substituted compositions the site is top, and the frequency increases monotonically with Cu content."
    }
  ],
  "notes": "No absolute tolerance is applied to frequencies; scoring relies on the site assignment and the monotonic trend (blueshift) matching the paper's claim. The process steps produce intermediate evidence (slab_structures.zip, optimized_geometries.zip) that is not scored but is required for a correct final artifact."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. The verifier reads the artifacts you place in `/app/outputs` and computes a weighted score from 0 to 1. For the main scored artifact `co_frequencies.csv`, the verifier checks that the file structure matches the contract and then performs a structural audit: it verifies that the site assignments and the frequency values across compositions follow the physically expected behavior induced by Cu substitution. Absolute numerical agreement with published values is not required; the scoring rewards the correct physical trend. The intermediate process evidence (slab and geometry archives) is checked for presence and basic validity but contributes less weight.
