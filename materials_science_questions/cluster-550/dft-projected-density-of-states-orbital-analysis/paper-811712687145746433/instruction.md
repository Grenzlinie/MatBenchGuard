# First-principles study of layered nitride: electronic structure and phonons

## Problem background
Layered transition-metal nitrides have attracted interest as potential superconductors when electron-doped. The ternary nitride BaHfN₂ shares structural and chemical similarities with known superconducting nitrides such as the MNCl (M=Ti,Zr,Hf) family, suggesting it may also exhibit superconductivity upon doping. Understanding its underlying electronic structure, the character of its conduction band, and its vibrational properties (phonons, dielectric response, Born effective charges) is essential to assess its potential and to compare with related compounds. This task investigates these properties using first-principles density-functional theory.

## Approach
We employ density-functional theory (DFT) within the local-density approximation (LDA) using the ABINIT code and Hartwigsen-Goedecker-Hutter (HGH) norm-conserving pseudopotentials. The pseudopotentials include semicore 5s and 5p states for Ba and Hf (and La in the doped case) to capture significant hybridization effects. The workflow begins with structural relaxation of the tetragonal BaHfN₂ crystal (space group P4/nmm). Using the relaxed geometry, we compute the electronic band structure, the indirect band gap, and the orbital-projected density of states to identify the dominant character at the conduction band minimum. Vibrational properties are then obtained via density-functional perturbation theory (DFPT): Born effective charge tensors, the high-frequency and static dielectric constants, and zone-center phonon frequencies with their LO-TO splittings for the insulating undoped system. To model electron doping, one Ba atom is replaced by La, the doped cell is relaxed, and zone-center phonon frequencies are recomputed for the now metallic Ba₀.₅La₀.₅HfN₂.

## Reproduction target
The goal is to compute the following quantities from first principles:
- Indirect band gap (eV) of undoped BaHfN₂.
- Dominant orbital character at the conduction band minimum of undoped BaHfN₂ (e.g., 'Hf 5d_xy').
- Born effective charge tensors (in-plane and out-of-plane components) for Ba, Hf, N1, and N2 in undoped BaHfN₂.
- High-frequency (ε∞) and static (ε₀) dielectric constants for undoped BaHfN₂ (xx and zz components).
- Zone-center phonon frequencies (TO and LO where applicable) along with mode symmetries for undoped BaHfN₂.
- Zone-center phonon frequencies for the La-doped metallic system Ba₀.₅La₀.₅HfN₂ (no LO-TO splitting).

## Assets

- ABINIT DFT code: https://www.abinit.org/
- HGH pseudopotential for Ba (5s,5p,6s): https://www.abinit.org/psp-tables/hgh
- HGH pseudopotential for Hf (5s,5p,5d,6s): https://www.abinit.org/psp-tables/hgh
- HGH pseudopotential for N (2s,2p): https://www.abinit.org/psp-tables/hgh
- HGH pseudopotential for La (5s,5p,5d,6s): https://www.abinit.org/psp-tables/hgh
- Crystal structure data for BaHfN2: 10.1016/S0022-4596(98)90007-5

## Workflow steps

### Step 1: DFT structural relaxation of undoped BaHfN2
- Role: process
- Action: Perform structural relaxation of BaHfN2 using ABINIT with LDA HGH pseudopotentials (Ba, Hf, N) including semicore states. Start from the experimental geometry (tetragonal P4/nmm, a=4.128 Å, c=8.382 Å, internal coordinates from literature).
- Evidence: `/app/outputs/relax_log.txt`

### Step 2: Compute indirect band gap of undoped BaHfN2
- Role: scored
- Action: Using the relaxed undoped structure, perform a SCF calculation and band structure calculation to determine the indirect band gap (in eV). Write the gap value to band_gap.txt.
- Output file: `/app/outputs/band_gap.txt`
- Format: txt
- Contract: Single float on the first line, representing the gap in eV.
- Scoring: scored by hidden verifier

### Step 3: Determine conduction band minimum orbital character
- Role: scored
- Action: Compute the projected density of states or fatbands to identify the dominant orbital character at the conduction band minimum. Write the result (e.g., 'Hf 5d_xy') to cbm_character.txt.
- Output file: `/app/outputs/cbm_character.txt`
- Format: txt
- Contract: Single string on the first line.
- Scoring: scored by hidden verifier

### Step 4: Compute Born effective charges
- Role: scored
- Action: Use ABINIT DFPT to compute the Born effective charge tensors for all atoms in undoped BaHfN2. Write the results to bec.txt in tabular format.
- Output file: `/app/outputs/bec.txt`
- Format: csv
- Contract: Table with columns: atom (string), Zxx (float), Zyy (float, equal to Zxx), Zzz (float). One row per distinct atom.
- Scoring: scored by hidden verifier

### Step 5: Compute dielectric constants
- Role: scored
- Action: Using ABINIT DFPT, compute the high-frequency (ε∞) and static (ε0) dielectric tensors for undoped BaHfN2. Write the xx and zz components to dielectric.txt.
- Output file: `/app/outputs/dielectric.txt`
- Format: txt
- Contract: Four floats on separate lines: epsilon_inf_xx, epsilon_inf_zz, epsilon_0_xx, epsilon_0_zz.
- Scoring: scored by hidden verifier

### Step 6: Compute zone-center phonon frequencies (undoped)
- Role: scored (load-bearing)
- Action: Use ABINIT DFPT to calculate zone-center phonon frequencies for undoped BaHfN2, including LO-TO splitting for IR active modes. Write the mode labels, symmetries, and TO/LO frequencies to phonon_undoped.txt.
- Output file: `/app/outputs/phonon_undoped.txt`
- Format: csv
- Contract: Table with columns: mode_label (string), symmetry (string), frequency_TO (float, cm⁻¹), frequency_LO (float, cm⁻¹; empty for Raman modes). One mode per row.
- Scoring: scored by hidden verifier

### Step 7: Create and relax Ba0.5La0.5HfN2 structure
- Role: process
- Action: Replace one Ba atom in the BaHfN2 unit cell with La, then relax the lattice constants and internal coordinates using ABINIT with LDA HGH pseudopotentials (Ba, Hf, La, N) including semicore states. Start from the experimental undoped geometry.
- Evidence: `/app/outputs/doped_relax_log.txt`

### Step 8: Compute doped phonon frequencies
- Role: scored (load-bearing)
- Action: Using the relaxed Ba0.5La0.5HfN2 structure, compute zone-center phonon frequencies with ABINIT DFPT. The system is metallic; no LO-TO splitting is reported. Write the mode labels and frequencies to phonon_doped.txt.
- Output file: `/app/outputs/phonon_doped.txt`
- Format: csv
- Contract: Table with columns: mode_label (string), frequency (float, cm⁻¹). One mode per row. Degenerate modes are listed per pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.txt`
- `/app/outputs/cbm_character.txt`
- `/app/outputs/bec.txt`
- `/app/outputs/dielectric.txt`
- `/app/outputs/phonon_undoped.txt`
- `/app/outputs/phonon_doped.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.txt
- path: `/app/outputs/band_gap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Indirect band gap of undoped BaHfN2.
- schema:
  - `type`: text
  - `description`: A single float on the first line representing the indirect band gap in eV.

### cbm_character.txt
- path: `/app/outputs/cbm_character.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Orbital character of the conduction band minimum.
- schema:
  - `type`: text
  - `description`: A single string on the first line representing the dominant orbital character at the conduction band minimum (e.g., 'Hf 5d_xy').

### bec.txt
- path: `/app/outputs/bec.txt`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Born effective charge tensors for Ba, Hf, N1, N2.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `Zxx`, `Zyy`, `Zzz`
  - `description`: Atom symbol (string), Zxx (float), Zyy (float), Zzz (float). In tetragonal symmetry Zxx equals Zyy.
  - `units`:
    - `Zxx`: e
    - `Zyy`: e
    - `Zzz`: e

### dielectric.txt
- path: `/app/outputs/dielectric.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: High-frequency and static dielectric tensor components.
- schema:
  - `type`: text
  - `description`: Four floats on separate lines in order: epsilon_inf_xx, epsilon_inf_zz, epsilon_0_xx, epsilon_0_zz. Each is dimensionless.

### phonon_undoped.txt
- path: `/app/outputs/phonon_undoped.txt`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zone-center optical phonon frequencies and LO-TO splittings for undoped BaHfN2.
- schema:
  - `type`: table
  - `required_columns`: `mode_label`, `symmetry`, `frequency_TO`, `frequency_LO`
  - `description`: Zone-center phonon frequencies for undoped BaHfN2. Columns: mode_label (string, e.g., '1-2'), symmetry (string), frequency_TO (float, cm⁻¹), frequency_LO (float, cm⁻¹; empty for Raman modes).
  - `units`:
    - `frequency_TO`: cm⁻¹
    - `frequency_LO`: cm⁻¹

### phonon_doped.txt
- path: `/app/outputs/phonon_doped.txt`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zone-center phonon frequencies for the metallic La-doped system.
- schema:
  - `type`: table
  - `required_columns`: `mode_label`, `frequency`
  - `description`: Zone-center phonon frequencies for doped Ba0.5La0.5HfN2. Columns: mode_label (string), frequency (float, cm⁻¹).
  - `units`:
    - `frequency`: cm⁻¹

Notes: All scored artifacts are recomputed quantities from DFT/DFPT. The checker will compare them against paper-reported reference values with appropriate tolerances (not provided here). The structural relaxation steps are required prerequisites but are not directly scored; their execution is enforced by the load-bearing phonon steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single float on the first line representing the indirect band gap in eV."
      },
      "description": "Indirect band gap of undoped BaHfN2."
    },
    {
      "file": "cbm_character.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single string on the first line representing the dominant orbital character at the conduction band minimum (e.g., 'Hf 5d_xy')."
      },
      "description": "Orbital character of the conduction band minimum."
    },
    {
      "file": "bec.txt",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "Zxx",
          "Zyy",
          "Zzz"
        ],
        "description": "Atom symbol (string), Zxx (float), Zyy (float), Zzz (float). In tetragonal symmetry Zxx equals Zyy.",
        "units": {
          "Zxx": "e",
          "Zyy": "e",
          "Zzz": "e"
        }
      },
      "description": "Born effective charge tensors for Ba, Hf, N1, N2."
    },
    {
      "file": "dielectric.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Four floats on separate lines in order: epsilon_inf_xx, epsilon_inf_zz, epsilon_0_xx, epsilon_0_zz. Each is dimensionless."
      },
      "description": "High-frequency and static dielectric tensor components."
    },
    {
      "file": "phonon_undoped.txt",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_label",
          "symmetry",
          "frequency_TO",
          "frequency_LO"
        ],
        "description": "Zone-center phonon frequencies for undoped BaHfN2. Columns: mode_label (string, e.g., '1-2'), symmetry (string), frequency_TO (float, cm⁻¹), frequency_LO (float, cm⁻¹; empty for Raman modes).",
        "units": {
          "frequency_TO": "cm⁻¹",
          "frequency_LO": "cm⁻¹"
        }
      },
      "description": "Zone-center optical phonon frequencies and LO-TO splittings for undoped BaHfN2."
    },
    {
      "file": "phonon_doped.txt",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_label",
          "frequency"
        ],
        "description": "Zone-center phonon frequencies for doped Ba0.5La0.5HfN2. Columns: mode_label (string), frequency (float, cm⁻¹).",
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "Zone-center phonon frequencies for the metallic La-doped system."
    }
  ],
  "notes": "All scored artifacts are recomputed quantities from DFT/DFPT. The checker will compare them against paper-reported reference values with appropriate tolerances (not provided here). The structural relaxation steps are required prerequisites but are not directly scored; their execution is enforced by the load-bearing phonon steps."
}
```

## How you are scored
Each output file you produce (band_gap.txt, cbm_character.txt, bec.txt, dielectric.txt, phonon_undoped.txt, phonon_doped.txt) will be independently evaluated by a hidden verifier against reference values derived from the scientific literature. The verifier compares your computed numbers to the expected results, applying appropriate tolerances to account for legitimate differences in DFT implementations (pseudopotentials, k-point sampling, convergence criteria). Each scored artifact contributes a specific weight toward the final score (ranging from 0.0 to 1.0). The task is not a single number match; you must faithfully execute the entire workflow, and the final reward reflects the aggregate agreement across all required quantities. Reporting numbers without performing the underlying calculations will not succeed.
