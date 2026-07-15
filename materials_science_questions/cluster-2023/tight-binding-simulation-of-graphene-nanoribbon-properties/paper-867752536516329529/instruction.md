# Bent MoS2 Nanoribbon Electronic and Optical Properties Simulation

## Problem background
Armchair MoS2 nanoribbons are one-dimensional semiconductors whose electronic structure can be tuned by mechanical bending. Mechanical deformation introduces complex strain patterns that alter band gaps and exciton formation, making bent nanoribbons promising for flexible optoelectronic devices. The key open questions are how edge and non-edge band gaps evolve with bending curvature, which critical curvatures separate distinct electronic regimes, and how these changes affect exciton binding energies and singlet-triplet splittings.

## Approach
The problem is studied by a multi-level computational workflow. First, first-principles density-functional theory (DFT) with the PBE functional is used to relax hydrogen-passivated armchair MoS2 nanoribbon structures at different widths and bending radii, and to compute their band structures. From the Γ‑point band energies, edge band gaps (EG), non-edge band gaps (NEG), and edge-band splittings (ΔEC and ΔEV) are extracted. The gap‑versus‑curvature curves reveal critical curvatures that define different bending regimes. Second, for selected curvatures, many‑body perturbation theory (G₀W₀ and the Bethe‑Salpeter equation) is employed to compute quasiparticle gaps, lowest singlet and triplet exciton energies, exciton binding energies, and singlet‑triplet splittings. The results are collected into tabular output files.

## Reproduction target
Produce the following scored artifacts:

1. A CSV file (`band_gap_curvature.csv`) containing the edge band gap (EG) and non-edge band gap (NEG) as a function of bending curvature (in Å⁻¹) for the A13MoS₂ nanoribbon, covering the set of curvatures that includes the flat case and radii down to 6 Å.  
2. A text file (`identification_of_critical_curvatures.txt`) giving the three critical bending curvatures κ₀, κc₁, κc₂ (in Å⁻¹) derived from the EG and NEG curves.  
3. A CSV file (`edge_gap_width_flat.csv`) with the edge gap EG and the edge-band splits ΔEC and ΔEV (in eV) for flat armchair MoS₂ nanoribbons of widths n = 9 through 24.  
4. A CSV file (`excitontable.csv`) with the quasiparticle gap Eg, lowest singlet exciton energy EA, binding energy Eb, triplet exciton energy Eₐᵗᵣᶦᵖˡᵉᵗ, and singlet‑triplet splitting ΔS‑T (all in eV) for the A13MoS₂ nanoribbon at four selected bending radii: flat (R = ∞), 13 Å, 9 Å, and 6 Å.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BerkeleyGW: https://berkeleygw.org/
- PBE/SCAN pseudopotentials for Mo and S: https://www.quantum-espresso.org/pseudopotentials/
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/

## Workflow steps

### Step 1: Generate and relax bent A13MoS2 structures
- Role: process
- Action: Build hydrogen‑passivated armchair MoS2 nanoribbon geometries with 13 MoS2 units in the unit cell (A13MoS2) at a series of bending radii R = ∞, 50, 25, 20, 16, 13, 10, 9, 8, 7, 6 Å (or equivalent curvatures). Relax each structure with DFT‑PBE, fixing the x‑y coordinates of the outermost Mo atoms on each edge while allowing all other atoms to relax until forces are below the paper’s convergence threshold.
- Evidence: none

### Step 2: Compute DFT band structures for bent A13MoS2 and extract EG and NEG
- Role: process
- Action: Perform DFT‑PBE band structure calculations for each relaxed A13MoS2 structure. At the Γ point, extract the edge band gap EG = E(C1) − E(V1) and the non‑edge gap NEG = E(C3) − E(V3) (using V1 instead of V3 when the edge valence bands merge into the continuum).
- Evidence: none

### Step 3: Output curvature vs gap data
- Role: scored
- Action: Collect the extracted EG and NEG for every computed curvature into a CSV file.
- Output file: `/app/outputs/band_gap_curvature.csv`
- Format: csv
- Contract: curvature (float), EG (float), NEG (float)
- Scoring: scored by hidden verifier

### Step 4: Identify critical curvatures
- Role: scored
- Action: From the EG and NEG vs curvature curves, determine the three critical bending curvatures: κ0 (point where EG begins to decrease), κc1 (maximum of NEG), and κc2 (point where the edge valence bands merge into the continuum). Write them to a plain text file.
- Output file: `/app/outputs/identification_of_critical_curvatures.txt`
- Format: txt
- Contract: Three lines, each with a text label and a floating‑point value.
- Scoring: scored by hidden verifier

### Step 5: Compute DFT band structures for flat nanoribbons n=9‑24
- Role: process
- Action: Build hydrogen‑passivated flat armchair MoS2 nanoribbons for each integer n from 9 to 24. Relax each structure with DFT‑PBE with the same edge‑fixing protocol. Compute band energies at the Γ point and extract the edge gap EG, upper edge split ΔEC = E(C2)−E(C1), and lower edge split ΔEV = E(V1)−E(V2).
- Evidence: none

### Step 6: Output width‑dependent edge gap and splits
- Role: scored
- Action: Collect the extracted EG, ΔEC, ΔEV for n=9‑24 into a CSV file.
- Output file: `/app/outputs/edge_gap_width_flat.csv`
- Format: csv
- Contract: n (int), EG (float), delta_EC (float), delta_EV (float)
- Scoring: scored by hidden verifier

### Step 7: Perform GW and BSE calculations for selected bending radii
- Role: process
- Action: Using Quantum ESPRESSO wavefunctions as input, run G₀W₀ quasiparticle and G₀W₀+BSE optical absorption calculations for A13MoS2 at bending radii R = ∞, 13, 9, 6 Å. Extract the quasiparticle gap Eg, the energies of the lowest‑energy singlet and triplet excitons (EA and EAtriplet), and compute the exciton binding energy Eb = Eg − EA and the singlet‑triplet splitting ΔS‑T = EA − EAtriplet.
- Evidence: none

### Step 8: Output exciton properties table
- Role: scored (load-bearing)
- Action: Write the extracted exciton properties to a CSV file.
- Output file: `/app/outputs/excitontable.csv`
- Format: csv
- Contract: radius (string), Eg (float), EA (float), Eb (float), EAtriplet (float), DeltaST (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_curvature.csv`
- `/app/outputs/identification_of_critical_curvatures.txt`
- `/app/outputs/edge_gap_width_flat.csv`
- `/app/outputs/excitontable.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_curvature.csv
- path: `/app/outputs/band_gap_curvature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Edge band gap (EG) and non‑edge band gap (NEG) as a function of bending curvature for A13MoS2. Rows must cover the full set of curvatures from flat to high bending.
- schema:
  - `type`: table
  - `required_columns`: `curvature`, `EG`, `NEG`
  - `units`:
    - `curvature`: 1/Å
    - `EG`: eV
    - `NEG`: eV

### identification_of_critical_curvatures.txt
- path: `/app/outputs/identification_of_critical_curvatures.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: The three critical bending curvatures κ0, κc1, κc2 derived from the EG/NEG curves.
- schema:
  - `type`: text
  - `description`: Three lines, each containing a label (e.g., kappa0:, kappac1:, kappac2:) followed by a floating‑point value in 1/Å.

### edge_gap_width_flat.csv
- path: `/app/outputs/edge_gap_width_flat.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Edge gap and non‑degenerate edge‑band splits for flat armchair MoS2 nanoribbons as a function of ribbon width n (n = 9…24).
- schema:
  - `type`: table
  - `required_columns`: `n`, `EG`, `delta_EC`, `delta_EV`
  - `units`:
    - `n`: dimensionless
    - `EG`: eV
    - `delta_EC`: eV
    - `delta_EV`: eV

### excitontable.csv
- path: `/app/outputs/excitontable.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Quasiparticle and exciton properties for A13MoS2 at four bending radii (R = ∞, 13, 9, 6 Å) as defined in the paper’s Table 1.
- schema:
  - `type`: table
  - `required_columns`: `radius`, `Eg`, `EA`, `Eb`, `EAtriplet`, `DeltaST`
  - `units`:
    - `radius`: Å (or inf)
    - `Eg`: eV
    - `EA`: eV
    - `Eb`: eV
    - `EAtriplet`: eV
    - `DeltaST`: eV

Notes: All files are plain text (CSV or TXT). Numeric values should be reported with sufficient precision for comparison. No gold values or tolerances are given here; they are part of the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_curvature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "curvature",
          "EG",
          "NEG"
        ],
        "units": {
          "curvature": "1/Å",
          "EG": "eV",
          "NEG": "eV"
        }
      },
      "description": "Edge band gap (EG) and non‑edge band gap (NEG) as a function of bending curvature for A13MoS2. Rows must cover the full set of curvatures from flat to high bending."
    },
    {
      "file": "identification_of_critical_curvatures.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Three lines, each containing a label (e.g., kappa0:, kappac1:, kappac2:) followed by a floating‑point value in 1/Å."
      },
      "description": "The three critical bending curvatures κ0, κc1, κc2 derived from the EG/NEG curves."
    },
    {
      "file": "edge_gap_width_flat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "EG",
          "delta_EC",
          "delta_EV"
        ],
        "units": {
          "n": "dimensionless",
          "EG": "eV",
          "delta_EC": "eV",
          "delta_EV": "eV"
        }
      },
      "description": "Edge gap and non‑degenerate edge‑band splits for flat armchair MoS2 nanoribbons as a function of ribbon width n (n = 9…24)."
    },
    {
      "file": "excitontable.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius",
          "Eg",
          "EA",
          "Eb",
          "EAtriplet",
          "DeltaST"
        ],
        "units": {
          "radius": "Å (or inf)",
          "Eg": "eV",
          "EA": "eV",
          "Eb": "eV",
          "EAtriplet": "eV",
          "DeltaST": "eV"
        }
      },
      "description": "Quasiparticle and exciton properties for A13MoS2 at four bending radii (R = ∞, 13, 9, 6 Å) as defined in the paper’s Table 1."
    }
  ],
  "notes": "All files are plain text (CSV or TXT). Numeric values should be reported with sufficient precision for comparison. No gold values or tolerances are given here; they are part of the hidden grading specification."
}
```

## How you are scored
A hidden verifier independently reads each of your output files and compares the reported quantities to reference values. The comparison checks numerical agreement within reasonable tolerances and verifies that qualitative trends (such as the non‑monotonic evolution of gaps with curvature or the period‑3 oscillation of edge‑band splittings with width) are correctly reproduced. Each artifact contributes a weighted portion to the final aggregate score between 0 and 1. Providing a correct artifact is not enough if the verifier detects inconsistencies between different outputs, such as critical curvatures that do not match the curvature‑gap curves.
