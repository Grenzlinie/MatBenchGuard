# Symmetry breaking and dynamical stability of scandium trihydride hcp phases

## Problem background
Scandium trihydride (ScH3) in its hcp phase can adopt different arrangements of hydrogen atoms around the metal plane. These arrangements break the high symmetry of the P6_3/mmc structure, leading to fundamental changes in electronic structure and potentially opening a band gap. The present task investigates four candidate phases: P6_3/mmc, P-3c1, P6_3cm, and P6_3. Your goal is to determine how the band gap evolves across these structures and which phase is dynamically stable by carrying out first-principles calculations and phonon analysis.

## Approach
The approach is to construct each phase from its published space group and fractional coordinates, relax the geometries with density functional theory using the GGA-PBE functional, compute the electronic band structure along a standard high-symmetry k-path, and extract the minimum indirect band gap. For the lowest-energy phase, you will also obtain a corrected band gap using a hybrid functional (e.g., HSE06) as a proxy for screened-exchange. Then you will perform finite-displacement phonon calculations for all four phases using supercells containing at least 192 atoms and analyze the phonon dispersions for imaginary modes to assess dynamical stability. The key comparisons are the trend in the GGA band gap across the four phases and the gap enhancement from GGA to hybrid level for the most stable phase.

## Reproduction target
Produce, from first-principles using Quantum ESPRESSO (or an equivalent open-source plane-wave DFT code) with the PBE functional, the following: (i) the minimum indirect GGA band gap (eV) for each of the four phases; (ii) the hybrid functional band gap (eV) for the P6_3 phase; (iii) raw GGA band structure eigenvalues for P6_3 that allow independent recomputation of its gap; (iv) raw phonon dispersion frequencies for P6_3; and (v) a stability flag (dynamically stable or not) for each phase based on the presence of imaginary phonon modes. Report all results in the specified JSON output files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotential Library: https://www.materialscloud.org/discover/sssp
- Phonopy: https://phonopy.github.io/phonopy/
- Python packages (numpy, scipy, pymatgen, ase): https://pypi.org/

## Workflow steps

### Step 1: Construct initial structures
- Role: process
- Action: Construct the four ScH3 hcp phases (P6_3/mmc, P-3c1, P6_3cm, P6_3) using the space group and fractional atomic coordinates from the paper's Table 1. Create input files for a plane-wave DFT code.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Geometry relaxation
- Role: process
- Action: Perform full geometry optimization (lattice parameters and atomic positions) for each structure using DFT with the PBE functional and appropriate pseudopotentials. Converge forces and stresses to standard thresholds.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: GGA band structure calculation
- Role: process
- Action: Run self-consistent DFT and non-self-consistent band-structure calculations along a standard high-symmetry k-path for all four phases. Retain the Kohn-Sham eigenvalues and k-point weights.
- Evidence: `/app/outputs/gga_bands.log`

### Step 4: Extract P6_3 GGA band structure
- Role: scored (load-bearing)
- Action: From the GGA calculation output, extract the eigenvalues and k-point coordinates for the P6_3 phase and save as JSON. Also compute the minimum indirect band gap for each phase (retain internally for later step).
- Output file: `/app/outputs/p6_3_band_structure.json`
- Format: json
- Contract: {"kpoints": [[float,float,float], ...], "eigenvalues": [[float, ...], ...]}
- Scoring: scored by hidden verifier

### Step 5: Hybrid functional calculation for P6_3
- Role: process
- Action: Perform a DFT calculation for the optimized P6_3 structure using a hybrid functional (e.g., HSE06) or a screened-exchange LDA (sX-LDA) to obtain the corrected band gap.
- Evidence: `/app/outputs/hybrid_calc.log`

### Step 6: Compile band gaps
- Role: scored
- Action: Collect the minimum indirect band gaps from the GGA runs for all four phases and the hybrid gap for P6_3. Write these values in a JSON file. Set the 'dynamically_stable' field to null initially.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"phases": [{"name": "string", "band_gap_GGA": float, "dynamically_stable": bool}], "p6_3_hybrid_gap": float}
- Scoring: scored by hidden verifier

### Step 7: Phonon calculations
- Role: process
- Action: Build supercells of at least 192 atoms for each phase. Compute force constants via finite-displacement DFT, then use Phonopy to obtain phonon dispersions for all phases.
- Evidence: `/app/outputs/phonon.log`

### Step 8: Phonon dispersion extraction and stability verdict
- Role: scored (load-bearing)
- Action: Extract phonon frequencies along the high-symmetry q-path for P6_3 and save as JSON. For each phase, check for imaginary modes and update the 'dynamically_stable' field in band_gaps.json (true if no imaginary modes, false otherwise).
- Output file: `/app/outputs/p6_3_phonon_dispersion.json`
- Format: json
- Contract: {"qpoints": [[float,float,float], ...], "frequencies": [[float, ...], ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/p6_3_band_structure.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/p6_3_phonon_dispersion.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### p6_3_band_structure.json
- path: `/app/outputs/p6_3_band_structure.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw GGA-PBE band structure of the P6_3 phase along the standard high-symmetry path. The checker recomputes the minimum indirect band gap from these eigenvalues.
- schema:
  - `type`: object
  - `required`:
    - `kpoints`: list of lists of 3 floats (k-path coordinates)
    - `eigenvalues`: list of lists of floats; eigenvalues[i] are the band energies (in eV) for kpoints[i]

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reported GGA band gaps for all four phases, hybrid gap for P6_3, and static stability flags (filled after phonon step). The checker compares the GGA gaps and the hybrid gap to hidden reference values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `phases`: array of objects, each with name (string), band_gap_GGA (float, eV), dynamically_stable (bool)
    - `p6_3_hybrid_gap`: float (eV)

### p6_3_phonon_dispersion.json
- path: `/app/outputs/p6_3_phonon_dispersion.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion of the P6_3 phase. The checker inspects this file for the absence of negative (imaginary) frequencies to confirm dynamical stability.
- schema:
  - `type`: object
  - `required`:
    - `qpoints`: list of [float,float,float] (q-path coordinates)
    - `frequencies`: list of lists of floats; frequencies[i] are the phonon mode frequencies (in meV or cm-1) for qpoints[i]

Notes: The agent must run all the DFT+phonon workflow and produce the three scored artifacts. The checker will recompute the band gap from the raw band structure, compare reported gaps to paper reference values, and audit phonon frequencies for imaginary modes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "p6_3_band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "kpoints": "list of lists of 3 floats (k-path coordinates)",
          "eigenvalues": "list of lists of floats; eigenvalues[i] are the band energies (in eV) for kpoints[i]"
        }
      },
      "description": "Raw GGA-PBE band structure of the P6_3 phase along the standard high-symmetry path. The checker recomputes the minimum indirect band gap from these eigenvalues."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phases": "array of objects, each with name (string), band_gap_GGA (float, eV), dynamically_stable (bool)",
          "p6_3_hybrid_gap": "float (eV)"
        }
      },
      "description": "Reported GGA band gaps for all four phases, hybrid gap for P6_3, and static stability flags (filled after phonon step). The checker compares the GGA gaps and the hybrid gap to hidden reference values within tolerances."
    },
    {
      "file": "p6_3_phonon_dispersion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "qpoints": "list of [float,float,float] (q-path coordinates)",
          "frequencies": "list of lists of floats; frequencies[i] are the phonon mode frequencies (in meV or cm-1) for qpoints[i]"
        }
      },
      "description": "Phonon dispersion of the P6_3 phase. The checker inspects this file for the absence of negative (imaginary) frequencies to confirm dynamical stability."
    }
  ],
  "notes": "The agent must run all the DFT+phonon workflow and produce the three scored artifacts. The checker will recompute the band gap from the raw band structure, compare reported gaps to paper reference values, and audit phonon frequencies for imaginary modes."
}
```

## How you are scored
Each scored artifact (p6_3_band_structure.json, band_gaps.json, p6_3_phonon_dispersion.json) is inspected by a hidden verifier. The verifier recomputes the P6_3 GGA gap from the raw band structure to cross-check consistency, compares your reported band gaps to hidden reference thresholds (including the correct ordering across phases), and audits the phonon dispersion for the absence of negative frequencies. The final reward is a weighted sum over these checks, with the main numerical gaps and the stability verdict carrying the largest weight. A solution that merely copies the paper's reported numbers without performing the real calculations will receive a low or zero reward.
