# Cesium Effect on Average Charge Density Oscillations at a LiF Grain Boundary

## Problem background
In lithium‑metal batteries, uncontrolled dendrite growth can lead to internal short circuits and safety hazards. One strategy to mitigate dendrite formation is the “self‑healing electrostatic shield” (SHES) mechanism, in which a small amount of cesium salt added to the electrolyte causes Cs⁺ ions to accumulate at dendrite tips and exposed anode surfaces, forming a positively charged layer that repels further Li deposition. The solid‑electrolyte interphase (SEI) that forms on the anode is a heterogeneous film containing inorganic grains (e.g., LiF). Grain boundaries within the SEI may provide preferential pathways for Li‑ion migration. It has been proposed that a Cs atom adsorbed at a Σ5 grain boundary of LiF can locally modify the average charge density (ACD) oscillations, potentially altering the energy landscape for Li transport. Understanding whether and how Cs changes the ACD near grain boundaries is therefore important for assessing the SHES effect in realistic SEI structures.

## Approach
We model a Σ5 grain boundary of LiF as a slab cleaved along the (310) plane with a lateral cell of approximately 28.6 × 10.2 Å and 6 Li layers. Two systems are studied: (1) a clean grain boundary slab, and (2) the same slab with a single Cs atom inserted at the most favorable grain‑boundary site (referred to as “site 1” in the literature). For each system, a first‑principles density‑functional theory (DFT) geometry relaxation is performed using an open‑source plane‑wave code (e.g., Quantum ESPRESSO) with projector‑augmented‑wave pseudopotentials from a public library, a plane‑wave cutoff of 400 eV, a 2×2×1 Monkhorst–Pack k‑point grid, and convergence thresholds of 10⁻⁴ eV on the total energy and 10⁻³ eV/Å on forces. From the relaxed self‑consistent charge densities we compute the average charge density along the direction perpendicular to the surface (z) by averaging the charge density over the x–y plane at each grid point, and along the direction parallel to the cleavage surface (x) by averaging over the y–z plane at each grid point. The final outputs are two CSV tables that contain the spatial coordinate and the ACD values for both the “no‑Cs” and “Cs” systems.

## Reproduction target
The target is to compute the average charge density profiles along the z‑direction (perpendicular to the surface) and the x‑direction (parallel to the surface) for the two defined systems. You must produce two CSV files under `/app/outputs`: `acd_z_profile.csv` with columns `z`, `ACD_no_Cs`, `ACD_Cs` and `acd_x_profile.csv` with columns `x`, `ACD_no_Cs`, `ACD_Cs`. The coordinates are in angstroms (Å) and the ACD values in e/Å³. The hidden verifier will then extract the oscillation amplitudes in the grain‑boundary region and evaluate whether the presence of Cs leads to a systematic change in those amplitudes.

## Assets

- LiF crystal structure (Fm-3m): https://www.crystallography.net/cod/9008690.html
- Li BCC crystal structure
- Cs BCC crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/
- SSSP pseudopotential library (or PseudoDojo): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate Σ5 grain boundary slab
- Role: process
- Action: Using the public LiF Fm-3m structure, build the Σ5 grain boundary model: cleave the (310) surface with a cell size of approximately 28.6 × 10.2 Å, containing 6 Li layers. Export the initial atomic coordinates.
- Evidence: `/app/outputs/gb_slab_init.xyz`

### Step 2: DFT relaxation of clean grain boundary slab
- Role: process
- Action: Perform DFT geometry relaxation of the clean grain boundary slab using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO). Employ pseudopotentials from a public library, a plane-wave cutoff of 400 eV, a 2×2×1 Monkhorst–Pack k-point grid, and convergence criteria of 10⁻⁴ eV for total energy and 10⁻³ eV/Å for forces. Save the relaxed structure and the self-consistent charge density.
- Evidence: `/app/outputs/clean_relaxed.log`

### Step 3: DFT relaxation of Cs-inserted grain boundary slab
- Role: process
- Action: Take the relaxed clean slab, insert one Cs atom at the grain boundary site designated as site 1 in the paper. Perform DFT relaxation using exactly the same computational settings as the clean relaxation. Save the relaxed structure and the self-consistent charge density.
- Evidence: `/app/outputs/cs_relaxed.log`

### Step 4: Compute average charge density profile along z
- Role: scored (load-bearing)
- Action: From the charge density outputs of the clean and Cs-inserted systems, compute the average charge density (ACD) along the z-direction (perpendicular to the surface). Average the charge density over the x–y plane at each z grid point. Output a CSV file with columns 'z', 'ACD_no_Cs', 'ACD_Cs'. Use units of Å for coordinates and e/Å³ for ACD.
- Output file: `/app/outputs/acd_z_profile.csv`
- Format: csv
- Contract: z (Angstrom, float), ACD_no_Cs (e/Ang^3, float), ACD_Cs (e/Ang^3, float)
- Scoring: scored by hidden verifier

### Step 5: Compute average charge density profile along x
- Role: scored
- Action: Compute ACD along the x-direction (parallel to the cleavage surface) by averaging over the y–z plane at each x grid point. Output a CSV file with columns 'x', 'ACD_no_Cs', 'ACD_Cs'. Use the same units as above.
- Output file: `/app/outputs/acd_x_profile.csv`
- Format: csv
- Contract: x (Angstrom, float), ACD_no_Cs (e/Ang^3, float), ACD_Cs (e/Ang^3, float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/acd_z_profile.csv`
- `/app/outputs/acd_x_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### acd_z_profile.csv
- path: `/app/outputs/acd_z_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average charge density along the z-direction (perpendicular to surface). Checker verifies that oscillation amplitude in the grain-boundary region is larger when Cs is present.
- schema:
  - `type`: table
  - `required_columns`: `z`, `ACD_no_Cs`, `ACD_Cs`
  - `units`:
    - `z`: Angstrom
    - `ACD_no_Cs`: e/Ang^3
    - `ACD_Cs`: e/Ang^3

### acd_x_profile.csv
- path: `/app/outputs/acd_x_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average charge density along the x-direction (parallel to cleavage). Same structural audit as the z profile.
- schema:
  - `type`: table
  - `required_columns`: `x`, `ACD_no_Cs`, `ACD_Cs`
  - `units`:
    - `x`: Angstrom
    - `ACD_no_Cs`: e/Ang^3
    - `ACD_Cs`: e/Ang^3

Notes: Both ACD profiles must be computed from the DFT charge densities of the relaxed clean and Cs-inserted slabs. The oscillation amplitudes are checked in a spatial window around the grain boundary (exact boundaries defined by the checker).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "acd_z_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "ACD_no_Cs",
          "ACD_Cs"
        ],
        "units": {
          "z": "Angstrom",
          "ACD_no_Cs": "e/Ang^3",
          "ACD_Cs": "e/Ang^3"
        }
      },
      "description": "Average charge density along the z-direction (perpendicular to surface). Checker verifies that oscillation amplitude in the grain-boundary region is larger when Cs is present."
    },
    {
      "file": "acd_x_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "ACD_no_Cs",
          "ACD_Cs"
        ],
        "units": {
          "x": "Angstrom",
          "ACD_no_Cs": "e/Ang^3",
          "ACD_Cs": "e/Ang^3"
        }
      },
      "description": "Average charge density along the x-direction (parallel to cleavage). Same structural audit as the z profile."
    }
  ],
  "notes": "Both ACD profiles must be computed from the DFT charge densities of the relaxed clean and Cs-inserted slabs. The oscillation amplitudes are checked in a spatial window around the grain boundary (exact boundaries defined by the checker)."
}
```

## How you are scored
A hidden verifier evaluates each of the two output files independently. For each direction, the verifier computes the peak‑to‑peak ACD oscillation amplitude within a spatial window around the grain boundary and compares the Cs and no‑Cs cases. Full credit is awarded if the amplitude with Cs is strictly larger than without Cs (a structural trend). The final reward is a weighted combination of the outcomes from the two profiles. The format, column headers, units, and file existence are also checked; an incorrectly formatted file may receive no credit for that direction.
