# First-principles vibrational spectra of CdSe/CdS core/shell nanoplatelets

## Problem background
Colloidal two-dimensional nanoplatelets of cadmium chalcogenides have attracted wide interest for their unique optical and electronic properties. Core/shell CdSe/CdS heterostructures promise enhanced quantum yield and stability, and their vibrational spectra (frequencies, symmetries, and localization of phonon modes) provide crucial insight into structural quality, strain, and surface effects. First-principles density functional calculations can predict the vibrational modes of such nanostructures, enabling detailed interpretation of experimental Raman and infrared spectra. This task asks the solver to compute from first principles the vibrational frequencies, mode symmetries, and the fraction of vibrational energy on terminating surface atoms for all optic-like modes in CdSe/CdS core/shell nanoplatelets with a fixed CdSe core (4 monolayers) and varying CdS shell thickness (1, 2, 3 monolayers). The results serve as a critical reference for analyzing experimentally observed vibrational bands and understanding how shell thickness modifies the phonon spectrum.

## Approach
The approach is based on scalar-relativistic density functional theory within the local density approximation (LDA), using plane-wave basis sets and norm-conserving pseudopotentials. The nanoplatelet geometry is modelled as a zinc-blende supercell with [001] orientation, terminated with Cd-rich surfaces compensated by fluorine atoms at virtual chalcogen sites, and a vacuum gap to isolate layers. For each shell thickness (1 ML, 2 ML, 3 ML of CdS), the calculation proceeds in three stages: (i) construct the supercell and prepare input files; (ii) relax the geometry until forces are below a tight threshold; (iii) compute the full dynamical matrix to obtain all normal-mode frequencies and eigenvectors. From the eigenvectors, one identifies the symmetry of each mode (A₁, B₂, or E) and the fraction WF of the total vibrational kinetic energy residing on the fluorine surface atoms (WF = Σ_F m_F u_F² / Σ_all m_i u_i²). Only modes with frequencies above 170 cm⁻¹ are retained as optic-like modes. This systematic protocol yields the complete vibrational fingerprint of the core/shell nanoplatelets for each shell thickness.

## Reproduction target
Produce a comma-separated value (CSV) file named frequencies_and_wf.csv containing the following columns: shell_ml (integer, 1, 2, or 3), mode_id (integer, distinguishing each mode within that shell thickness), symmetry (string, one of A1, B2, or E), frequency_cm1 (float, in cm⁻¹), and WF (float, dimensionless). The file must include all vibrational modes with frequency greater than 170 cm⁻¹ for each of the three shell thicknesses, based on first-principles calculations as described. The computed values constitute the primary quantitative output; their validation against independent expectations will be performed by the hidden verifier.

## Assets

- ABINIT (plane-wave DFT code): https://www.abinit.org/
- LDA Troullier-Martins norm-conserving pseudopotentials (Cd, Se, S, F): https://www.abinit.org/psp-tables
- Crystal structures of zinc-blende CdSe and CdS

## Workflow steps

### Step 1: Construct supercell models
- Role: process
- Action: Build ABINIT input files for three core/shell nanoplatelet geometries: CdSe core 4 ML, CdS shell thicknesses 1, 2, and 3 ML. Use zinc-blende [001] orientation, Cd-rich termination with F atoms at virtual chalcogen sites, and a 20 Å vacuum gap in the supercell. Package all input files.
- Evidence: `/app/outputs/input_files.tar.gz`

### Step 2: Relax nanoplatelet geometries
- Role: process
- Action: Run DFT geometry relaxation for each model using ABINIT with LDA, plane-wave cutoff 50 Ha, Monkhorst-Pack 8×8×2 k‑mesh, force convergence threshold 5·10⁻⁶ Ha/Bohr. Use norm-conserving pseudopotentials for Cd, Se, S, F.
- Evidence: `/app/outputs/relaxed_structures.tar.gz`

### Step 3: Phonon frequency and eigenvector calculation
- Role: process
- Action: Using the relaxed structures, perform phonon calculations (dynamical matrix) with the same DFT/LDA parameters to obtain normal‑mode frequencies and eigenvectors. Extract all vibrational modes up to the highest frequency.
- Evidence: `/app/outputs/phonon_outputs.tar.gz`

### Step 4: Extract optic-like mode frequencies and surface energy fraction
- Role: scored (load-bearing)
- Action: Process the phonon outputs to extract all modes with frequency >170 cm⁻¹. Determine mode symmetry (A₁, B₂, or E) from atomic displacement patterns. Compute WF = (Σ_F m_F u_F²) / (Σ_all m_i u_i²) for each mode. Write the results to frequencies_and_wf.csv.
- Output file: `/app/outputs/frequencies_and_wf.csv`
- Format: csv
- Contract: columns: shell_ml (int), mode_id (int), symmetry (str, one of A1, B2, E), frequency_cm1 (float, in cm⁻¹), WF (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies_and_wf.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies_and_wf.csv
- path: `/app/outputs/frequencies_and_wf.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of all optic-like vibrational modes above 170 cm⁻¹ for each shell thickness (1,2,3 ML) with their symmetry, frequency, and surface vibrational energy fraction.
- schema:
  - `type`: table
  - `required_columns`: `shell_ml`, `mode_id`, `symmetry`, `frequency_cm1`, `WF`
  - `units`:
    - `frequency_cm1`: cm⁻¹
    - `WF`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies_and_wf.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "shell_ml",
          "mode_id",
          "symmetry",
          "frequency_cm1",
          "WF"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹",
          "WF": "dimensionless"
        }
      },
      "description": "CSV table of all optic-like vibrational modes above 170 cm⁻¹ for each shell thickness (1,2,3 ML) with their symmetry, frequency, and surface vibrational energy fraction."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that runs after the workflow completes. The verifier inspects the frequencies_and_wf.csv file and compares the reported mode frequencies and surface energy fractions to hidden reference criteria. In particular, it assesses whether the low‑WF (interior‑like) mode frequencies agree with independently known reference values, whether a key characteristic mode exhibits the expected physical dependence on shell thickness, and whether high‑frequency modes with large surface character are present. The final reward is a combination of per‑thickness accuracy scores and a consistency/tendency bonus, normalized to a maximum of 1.0. Simply inserting arbitrary or guessed numbers will not satisfy the hidden checks; the results must originate from a correct DFT phonon calculation following the described protocol.
