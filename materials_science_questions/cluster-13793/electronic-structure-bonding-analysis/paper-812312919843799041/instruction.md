# Electronic Structure Bonding Analysis

## Problem background
Rare-earth metal carbide halides of the type Y₂X₂C₂ exhibit superconductivity. The origin is hypothesized to lie in the proximity of C₂-π* molecular states to the Fermi level, giving rise to a high density of states and strong electron–phonon coupling. Y₂Br₂C₂ is a prototypical system. Computing its electronic structure — the total density of states, the band dispersion with particular attention to a possible saddle point in the C₂-π* derived band, and the sensitivity of this band to frozen-phonon distortions — provides a test of the underlying bonding scenario.

## Approach
Self-consistent scalar-relativistic TB-LMTO-ASA calculations are carried out using the Questaal code. Starting from the experimental crystal structure (space group C2/m, lattice parameters and atomic positions given in the workflow steps), a reference equilibrium calculation provides the self-consistent potential and eigenvalues. From these, the total density of states and the band structure along a high-symmetry path are computed. The C₂-π* character is identified via orbital projections. Subsequently, two static (frozen-phonon) distortions are applied: (i) a stretching of the C–C bond to a target distance; (ii) a rigid rotation of the C₂ unit by a small angle. For each distorted geometry, the self-consistent band structure is recomputed and the energy shift of the C₂-π* band at the Gamma point relative to the equilibrium calculation is determined.

## Reproduction target
The task is to reproduce the electronic structure of Y₂Br₂C₂ as obtained from TB-LMTO-ASA. Specifically, compute and submit the total density of states (`dos.csv`), the band structure along the Γ–A–M–Z–Γ path (`band_structure.csv`), and the frozen-phonon energy shifts of the C₂-π* band at the Gamma point for the two specified distortions (`frozen_phonon_shifts.csv`). The computed DOS at the Fermi level and the band structure should reveal whether a flat C₂-π* band with a saddle point exists near E_F, and the frozen-phonon shifts should indicate the direction and strength of the electron–phonon coupling.

## Assets

- Questaal (TB-LMTO-ASA) package: https://www.questaal.org/

## Workflow steps

### Step 1: Equilibrium LMTO calculation
- Role: process
- Action: Set up and run a self-consistent TB-LMTO-ASA calculation for Y2Br2C2 using the equilibrium crystal structure (space group C2/m, a=6.953 Å, b=3.764 Å, c=9.938 Å, β=99.98°; atomic positions: Y (0.4040,0,0.1485), Br (0.7901,0,0.3333), C (0.0861,0,0.0361)). Store the self-consistent potential and eigenvalues for downstream use.
- Evidence: `/app/outputs/equilibrium_scf.log`

### Step 2: Total density of states (DOS)
- Role: scored
- Action: From the equilibrium calculation, compute the total density of states and save it as dos.csv with energy (eV) relative to Fermi level (EF=0).
- Output file: `/app/outputs/dos.csv`
- Format: csv
- Contract: columns: energy (eV), total_DOS (states/eV per formula unit)
- Scoring: scored by hidden verifier

### Step 3: Band structure and saddle point
- Role: scored (load-bearing)
- Action: Compute the band structure along the path Γ(0,0,0)–A(0,0,1/2)–M(0,1/2,1/2)–Z(0,1/2,0)–Γ using the equilibrium calculation. Save all bands within -3 to +3 eV of EF as band_structure.csv, with a consistent band index and k-point labels. Use a dense k-mesh to resolve the saddle point.
- Output file: `/app/outputs/band_structure.csv`
- Format: csv
- Contract: columns: kpoint_label (string, e.g., 'Gamma','A','M','Z'), band_index (int), energy (eV). Include all bands within -3 to +3 eV of EF. Use at least 50 k-point segments across the whole path.
- Scoring: scored by hidden verifier

### Step 4: Frozen-phonon band shifts
- Role: scored
- Action: Using the same LMTO setup, perform two distorted geometry calculations: (a) elongation: set C-C distance to 130.5 pm by displacing the C atoms along the bond; (b) rotation: rotate the C2 unit by 3° about the (010) axis into the ab-plane. For each distortion, recompute the self-consistent band structure and determine the energy of the band with predominant C2-π* character at the Gamma point. Also retrieve the equilibrium reference energy of the same band at Gamma from step1. Compute the energy shift (distorted minus equilibrium) for each case and save as frozen_phonon_shifts.csv.
- Output file: `/app/outputs/frozen_phonon_shifts.csv`
- Format: csv
- Contract: columns: distortion (string: 'elongation' or 'rotation'), band_name (string, e.g., 'pi*_band'), energy_shift (eV). Positive shift means the band moves upward.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos.csv`
- `/app/outputs/band_structure.csv`
- `/app/outputs/frozen_phonon_shifts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos.csv
- path: `/app/outputs/dos.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total density of states (DOS) for Y2Br2C2. Energy is relative to Fermi level (EF=0).
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_DOS`
  - `units`:
    - `energy`: eV
    - `total_DOS`: states/eV per formula unit

### band_structure.csv
- path: `/app/outputs/band_structure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band structure along Γ–A–M–Z–Γ path. Checks for existence of a saddle point near EF at Γ.
- schema:
  - `type`: table
  - `required_columns`: `kpoint_label`, `band_index`, `energy`
  - `units`:
    - `energy`: eV

### frozen_phonon_shifts.csv
- path: `/app/outputs/frozen_phonon_shifts.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy shift of the C2-π* band at Gamma for elongation and rotation distortions. Sign and magnitude are verified.
- schema:
  - `type`: table
  - `required_columns`: `distortion`, `band_name`, `energy_shift`
  - `units`:
    - `energy_shift`: eV

Notes: The agent must install and use the Questaal TB-LMTO-ASA package. The equilibrium LMTO serves as the process step; only the three derived data artifacts are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_DOS"
        ],
        "units": {
          "energy": "eV",
          "total_DOS": "states/eV per formula unit"
        }
      },
      "description": "Total density of states (DOS) for Y2Br2C2. Energy is relative to Fermi level (EF=0)."
    },
    {
      "file": "band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "kpoint_label",
          "band_index",
          "energy"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Band structure along Γ–A–M–Z–Γ path. Checks for existence of a saddle point near EF at Γ."
    },
    {
      "file": "frozen_phonon_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "distortion",
          "band_name",
          "energy_shift"
        ],
        "units": {
          "energy_shift": "eV"
        }
      },
      "description": "Energy shift of the C2-π* band at Gamma for elongation and rotation distortions. Sign and magnitude are verified."
    }
  ],
  "notes": "The agent must install and use the Questaal TB-LMTO-ASA package. The equilibrium LMTO serves as the process step; only the three derived data artifacts are scored."
}
```

## How you are scored
After you submit the three CSV files, a hidden verifier will independently score each artifact. For the DOS, it will compare the DOS value at the Fermi energy to a hidden reference. For the band structure, it will analyse the curvature near the Gamma point to verify the presence/absence of a saddle point with the correct characteristics. For the frozen-phonon shifts, it will check that the shifts meet a required sign and minimum magnitude. The stage scores are weighted and summed to produce a final reward between 0 and 1. Simply reporting the correct numbers is not sufficient; the submitted data must be derived from genuine LMTO calculations.
