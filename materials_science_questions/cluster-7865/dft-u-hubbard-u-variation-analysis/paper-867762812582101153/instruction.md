# Americium 5f Electron Localization in Bulk vs (111) Films via DFT

## Problem background
Americium occupies a pivotal position in the actinide series, where 5f electrons undergo a transition from localized to itinerant behavior. Understanding how the reduced atomic coordination at a surface influences this localization is important for predicting chemical bonding and surface reactivity of actinide materials. This task investigates the 5f electron behavior in bulk fcc americium versus (111) ultra-thin films.

## Approach
We use density functional theory (DFT) with the full-potential linearized augmented-plane-wave (FP-LAPW) method, as implemented in the open-source Elk code. Calculations are performed at the antiferromagnetic ground state with spin-orbit coupling and the GGA-PBE exchange-correlation functional. Three systems are compared: bulk fcc Am, a 1-layer (111) slab, and a 5-layer (111) slab, all at the experimental lattice constant of 9.26 a.u. From the self-consistent field calculations, the partial 5f density of states is extracted, and the energy of the first prominent peak below the Fermi level is identified for each system. This peak position serves as a probe of 5f localization.

## Reproduction target
Run the described DFT calculations and report the binding energies of the first prominent 5f DOS peak below the Fermi level for bulk fcc Am, the 1-layer (111) slab, and the 5-layer (111) slab. Write the three values (negative numbers in eV) to `/app/outputs/dos_peak_positions.json`. A hidden verifier will then assess the scientific quality of your results, checking for physically consistent trends and plausible energy ranges.

## Assets

- Elk FP-LAPW code: https://sourceforge.net/projects/elk/

## Workflow steps

### Step 1: Prepare crystal structures for bulk and (111) slabs
- Role: process
- Action: Generate input files (crystal structure, k-point meshes, plane-wave cutoff, etc.) for bulk fcc Am and (111) slabs with 1 and 5 layers, using the experimental lattice constant of 9.26 a.u. Use the antiferromagnetic (AFM) configuration and the GGA-PBE exchange-correlation functional with spin-orbit coupling (SO).
- Evidence: none

### Step 2: Run self-consistent field DFT calculations
- Role: process
- Action: Perform self-consistent field (SCF) calculations for the bulk, 1-layer, and 5-layer systems using the FP-LAPW method at the GGA-AFM-SO level. Converge the charge density to high precision (e.g., 0.01 mRy/atom).
- Evidence: none

### Step 3: Compute and report 5f DOS peak positions
- Role: scored (load-bearing)
- Action: Use the SCF results to calculate the partial density of states for Am 5f electrons. Identify the energy of the first prominent peak below the Fermi level (EF set to zero) for each system. Write the three binding energies (negative eV) to the output JSON file.
- Output file: `/app/outputs/dos_peak_positions.json`
- Format: json
- Contract: {"type": "object", "properties": {"bulk": {"type": "number", "description": "Energy (eV) of first 5f peak below EF for bulk fcc Am"}, "film_1layer": {"type": "number", "description": "Energy (eV) of first 5f peak below EF for 1-layer (111) slab"}, "film_5layer": {"type": "number", "description": "Energy (eV) of first 5f peak below EF for 5-layer (111) slab"}}, "required": ["bulk", "film_1layer", "film_5layer"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_peak_positions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_peak_positions.json
- path: `/app/outputs/dos_peak_positions.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Binding energies (negative eV) of the first 5f DOS peak below Fermi level for bulk fcc Am, 1-layer (111) slab, and 5-layer (111) slab computed at GGA-AFM-SO level. The checker will verify that bulk < film_5layer < film_1layer (more negative = more localized) and that film_5layer lies between -2.0 and -1.0 eV.
- schema:
  - `type`: object
  - `properties`:
    - `bulk`:
      - `type`: number
      - `description`: Energy (eV) of first 5f peak below EF for bulk fcc Am
    - `film_1layer`:
      - `type`: number
      - `description`: Energy (eV) of first 5f peak below EF for 1-layer (111) slab
    - `film_5layer`:
      - `type`: number
      - `description`: Energy (eV) of first 5f peak below EF for 5-layer (111) slab
  - `required`: `bulk`, `film_1layer`, `film_5layer`

Notes: The relative trend and range check serve as structural scoring (T3). Exact peak energies depend on the specific DFT implementation (Elk vs. WIEN2k) and computational settings, so a tolerance-based match to the paper's numbers is not required. The scored ordering is robust against code/functional variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_peak_positions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "bulk": {
            "type": "number",
            "description": "Energy (eV) of first 5f peak below EF for bulk fcc Am"
          },
          "film_1layer": {
            "type": "number",
            "description": "Energy (eV) of first 5f peak below EF for 1-layer (111) slab"
          },
          "film_5layer": {
            "type": "number",
            "description": "Energy (eV) of first 5f peak below EF for 5-layer (111) slab"
          }
        },
        "required": [
          "bulk",
          "film_1layer",
          "film_5layer"
        ]
      },
      "description": "Binding energies (negative eV) of the first 5f DOS peak below Fermi level for bulk fcc Am, 1-layer (111) slab, and 5-layer (111) slab computed at GGA-AFM-SO level. The checker will verify that bulk < film_5layer < film_1layer (more negative = more localized) and that film_5layer lies between -2.0 and -1.0 eV."
    }
  ],
  "notes": "The relative trend and range check serve as structural scoring (T3). Exact peak energies depend on the specific DFT implementation (Elk vs. WIEN2k) and computational settings, so a tolerance-based match to the paper's numbers is not required. The scored ordering is robust against code/functional variations."
}
```

## How you are scored
Your submission will be automatically evaluated by a hidden verifier. The verifier reads your `dos_peak_positions.json` and checks structural properties of the computed peak energies—in particular, relative ordering among the three systems and whether the values lie within physically reasonable bounds. The verifier combines these checks into a reward between 0.0 and 1.0. Reporting numbers alone without executing the full computational workflow will not suffice; the verifier's checks are designed to validate genuine reproduction of the DFT calculations.
