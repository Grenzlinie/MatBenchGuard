# First-Principles Calculation of Nontrivial Band Gaps in Os-Alloyed 2D TMD Monolayers

## Problem background
Two-dimensional transition-metal dichalcogenide (TMD) monolayers such as MX₂ (M=Mo,W; X=S,Se,Te) are semiconductors with sizable electronic band gaps. Introducing exotic elements through alloying can drastically alter their electronic properties. In particular, alloying with 5d transition metals that carry strong spin-orbit coupling has been proposed as a route to induce a topological insulator (TI) state, characterized by a nontrivial band gap and the quantum spin Hall effect. The central physical question is whether replacing 25 % of the metal atoms with osmium (Os) opens a SOC-induced band gap with inverted band character, and how large that gap is for the six alloy compositions M0.75Os0.25X2. Determining these gaps from first principles, as well as their response to external biaxial strain, provides essential guidance for experimental realization of 2D topological insulators.

## Approach
The reproduction uses density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and fully self-consistent spin-orbit coupling (SOC). The calculations are performed with an open-source plane-wave code (Quantum ESPRESSO) and norm-conserving or PAW pseudopotentials from the SSSP library. For each of the six alloy systems, a 2×2 supercell of the pristine MX₂ monolayer is constructed, one M atom is replaced by Os, and the atomic positions are relaxed under SOC until forces converge. From the relaxed structure, a high-resolution band structure is computed. The nontrivial character of the gap is diagnosed by identifying the band inversion between the 5d orbitals of Os that opens a direct SOC gap along the Γ–K path. Both the indirect (global) band gap and the smallest direct gap at the inversion point are extracted for each system. For Mo0.75Os0.25Te2, the same band-structure calculation is repeated under a series of in-plane biaxial strains (from compressive to tensile) to map the strain dependence of the direct gap. The entire workflow is self-contained: the required crystal structures are fully specified by the lattice types and lattice constants published for the pristine MX₂ monolayers; no external experimental data are needed.

## Reproduction target
Produce two comma-separated value (CSV) files under `/app/outputs`. The first, `band_gaps.csv`, must contain one row for each of the six Os-alloyed systems: Mo0.75Os0.25S2, Mo0.75Os0.25Se2, Mo0.75Os0.25Te2, W0.75Os0.25S2, W0.75Os0.25Se2, W0.75Os0.25Te2. For each system, report the global (indirect) band gap and the direct band gap at the band-inversion point, both in units of meV. If a system is metallic (no gap), enter the string `metallic` for both gap values. The second file, `strain_gaps.csv`, must contain seven rows, one for each biaxial strain percentage (−2, −1, 0, 1, 2, 3, 4) applied to Mo0.75Os0.25Te2, and the corresponding direct nontrivial band gap in meV.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE PAW): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct and relax Os-alloy supercells
- Role: process
- Action: Build 2×2 supercells of pristine MX₂ monolayers (M=Mo,W; X=S,Se,Te) and replace one M atom with Os to form M0.75Os0.25X2. Relax atomic positions using DFT (PBE, spin-orbit coupling) until forces converge.
- Evidence: none

### Step 2: Compute band gaps for all alloys
- Role: scored (load-bearing)
- Action: For each relaxed alloy, compute the band structure with DFT (PBE, SOC) and extract the global (indirect) band gap and the direct band gap at the band-inversion point. Write the results to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: system (string), global_gap_meV (float or 'metallic'), direct_gap_meV (float or 'metallic')
- Scoring: scored by hidden verifier

### Step 3: Compute strain-dependent gaps for Mo0.75Os0.25Te2
- Role: scored (load-bearing)
- Action: For the relaxed Mo0.75Os0.25Te2 structure, apply biaxial strain from -2% to +4% in 1% steps. For each strain, compute the band structure with DFT (PBE, SOC) and extract the direct nontrivial band gap. Write the results to strain_gaps.csv.
- Output file: `/app/outputs/strain_gaps.csv`
- Format: csv
- Contract: CSV with columns: strain_percent (float), direct_gap_meV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/strain_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed global and direct nontrivial band gaps for all six Os-alloyed TMD monolayers.
- schema:
  - `required_columns`: `system`, `global_gap_meV`, `direct_gap_meV`
  - `description`: Six rows, one per system: Mo₀.₇₅Os₀.₂₅S₂, Mo₀.₇₅Os₀.₂₅Se₂, Mo₀.₇₅Os₀.₂₅Te₂, W₀.₇₅Os₀.₂₅S₂, W₀.₇₅Os₀.₂₅Se₂, W₀.₇₅Os₀.₂₅Te₂. Values in meV. 'metallic' for systems without a gap.

### strain_gaps.csv
- path: `/app/outputs/strain_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct band gap of Mo₀.₇₅Os₀.₂₅Te₂ as a function of biaxial strain.
- schema:
  - `required_columns`: `strain_percent`, `direct_gap_meV`
  - `description`: Seven rows for strains -2,-1,0,1,2,3,4. Direct gap in meV.

Notes: The checker compares the submitted gap values to hidden paper-reported reference values with appropriate tolerances. Systems flagged 'metallic' in band_gaps.csv are checked for exact match of the string 'metallic'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "system",
          "global_gap_meV",
          "direct_gap_meV"
        ],
        "description": "Six rows, one per system: Mo₀.₇₅Os₀.₂₅S₂, Mo₀.₇₅Os₀.₂₅Se₂, Mo₀.₇₅Os₀.₂₅Te₂, W₀.₇₅Os₀.₂₅S₂, W₀.₇₅Os₀.₂₅Se₂, W₀.₇₅Os₀.₂₅Te₂. Values in meV. 'metallic' for systems without a gap."
      },
      "description": "Computed global and direct nontrivial band gaps for all six Os-alloyed TMD monolayers."
    },
    {
      "file": "strain_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "strain_percent",
          "direct_gap_meV"
        ],
        "description": "Seven rows for strains -2,-1,0,1,2,3,4. Direct gap in meV."
      },
      "description": "Direct band gap of Mo₀.₇₅Os₀.₂₅Te₂ as a function of biaxial strain."
    }
  ],
  "notes": "The checker compares the submitted gap values to hidden paper-reported reference values with appropriate tolerances. Systems flagged 'metallic' in band_gaps.csv are checked for exact match of the string 'metallic'."
}
```

## How you are scored
A hidden automated verifier will independently inspect your two submitted CSV files. It checks structural correctness (correct number of rows/columns, expected system names, valid numeric or 'metallic' entries) and then compares your computed gap values to a set of reference values. The comparison accounts for the expected numerical spread arising from different DFT implementations and convergence choices. The two files contribute separate weighted components to a final reward between 0 and 1. The verifier does not merely look for exact numbers; it evaluates whether your gaps follow the physically expected trends and fall within acceptable ranges. For the strain data, it additionally verifies the qualitative dependence of the gap on strain. Your job is to perform the DFT calculations honestly and report the results; there is no reward for simply reproducing numbers from the literature.
