# Dynamical stability and phonon-driven transitions in doped La2CuO4

## Problem background
The cuprate La_{2-x}Sr_xCuO_4 exhibits structural phase transitions between high-temperature tetragonal (HTT), low-temperature orthorhombic (LTO), and low-temperature less-orthorhombic (LTLO) phases. At the doping level x≈1/8, the interplay of lattice instabilities and the underlying electronic structure is thought to drive these transitions, but the dynamical stability of the competing phases and the origin of the soft phonon modes remain open questions that first-principles calculations can address. This reproduction investigates the phonon stability and relative energetics of the HTT and LTLO phases of La_{1.875}Sr_{0.125}CuO_4 by computing their phonon dispersions, total energies, and the near-Fermi-level density of states splitting. The goal is to quantify which phase is the ground state and to confirm the presence/absence of phonon instabilities at the X point of the Brillouin zone.

## Approach
The investigation uses density-functional theory (DFT) within the generalized gradient approximation (GGA-PBE) as implemented in the OpenMX code, with norm-conserving pseudopotentials and optimized pseudo-atomic basis functions (La8.0-s3p3d3f2, Sr10.0-s3p2d2f2, Cu6.0-s2p2d2, O7.0-s2p2d1). Two crystal structures are built: HTT (I4/mmm, a=7.62 Å, c=13.22 Å) and LTLO (Pccn), both for a 56-atom unit cell of La_{1.875}Sr_{0.125}CuO_4 where one symmetrically equivalent La atom is replaced by Sr. All internal coordinates are relaxed until forces fall below 10⁻⁴ Ha/bohr using a 4×4×2 k-point mesh. Force constants are obtained via finite atomic displacements in (2×2×1) supercells (224 atoms). The dynamical matrix is constructed and diagonalized to yield phonon frequencies along high-symmetry paths, with special attention to the X point (0.5,0.5,0). Total energies are compared to determine the relative stability. Additionally, a non-self-consistent DFT calculation with a denser k-point mesh is performed for the LTLO structure to compute the Kohn-Sham eigenvalues, from which the density of states near the Fermi level is derived and the energy separation between the two closest peaks is measured.

## Reproduction target
Reproduce, using the OpenMX DFT code with the specified basis sets and pseudopotentials, the following four quantitative results for La_{1.875}Sr_{0.125}CuO_4: (1) the lowest phonon frequency and the full list of frequencies at the X point for the HTT phase; (2) the lowest phonon frequency and the full list of frequencies at the X point for the LTLO phase, verifying that no imaginary frequencies appear; (3) the total energy per formula unit for both HTT and LTLO and their difference; (4) the energy positions of the two peaks in the density of states of LTLO near the Fermi level and the energy splitting between them. All outputs must be written to the designated JSON files under /app/outputs exactly adhering to the declared schemas.

## Assets

- OpenMX DFT code: http://www.openmx-square.org/

## Workflow steps

### Step 1: Build initial HTT and LTLO structures
- Role: process
- Action: Construct initial atomic configurations for HTT (space group I4/mmm, a=7.62 Å, c=13.22 Å) and LTLO (Pccn) of La1.875Sr0.125CuO4 by replacing one symmetrically equivalent La atom with Sr per unit cell.
- Evidence: none

### Step 2: Relax HTT and LTLO structures via DFT-GGA
- Role: process
- Action: Perform DFT-GGA relaxation of both HTT and LTLO structures using OpenMX with GGA-PBE functional, norm-conserving pseudopotentials, and optimized basis sets. Relax until all forces < 10⁻⁴ Ha/bohr. Record total energies and relaxed coordinates.
- Evidence: none

### Step 3: Compute force constants
- Role: process
- Action: Construct (2×2×1) supercells from the relaxed HTT and LTLO structures and compute force constants via finite atomic displacements using OpenMX.
- Evidence: none

### Step 4: Calculate phonon dispersions
- Role: process
- Action: From the force constants, construct the dynamical matrix and solve for phonon frequencies and eigenvectors along high-symmetry paths. Record the complete list of frequencies at the X point (0.5,0.5,0) for both HTT and LTLO phases.
- Evidence: none

### Step 5: Output HTT phonon frequencies at X
- Role: scored (load-bearing)
- Action: Extract the lowest phonon frequency and the complete list of frequencies at the X point for the HTT phase. Write the results to HTT_phonon_X.json.
- Output file: `/app/outputs/HTT_phonon_X.json`
- Format: json
- Contract: {"type":"object","required":["lowest_frequency_cm-1","all_frequencies_X"],"properties":{"lowest_frequency_cm-1":{"type":"number"},"all_frequencies_X":{"type":"array","items":{"type":"number"}}}}
- Scoring: scored by hidden verifier

### Step 6: Output LTLO phonon frequencies at X
- Role: scored
- Action: Extract the lowest phonon frequency and the complete list of frequencies at the X point for the LTLO phase. Verify that no imaginary frequencies are present. Write to LTLO_phonon_X.json.
- Output file: `/app/outputs/LTLO_phonon_X.json`
- Format: json
- Contract: {"type":"object","required":["lowest_frequency_cm-1","all_frequencies_X"],"properties":{"lowest_frequency_cm-1":{"type":"number"},"all_frequencies_X":{"type":"array","items":{"type":"number"}}}}
- Scoring: scored by hidden verifier

### Step 7: Compare total energies of HTT and LTLO
- Role: scored
- Action: Read the total energies from the relaxation outputs, compute the energy per formula unit for each phase, and write the energies and their difference to total_energy_comparison.json.
- Output file: `/app/outputs/total_energy_comparison.json`
- Format: json
- Contract: {"type":"object","required":["E_HTT_eV_fu","E_LTLO_eV_fu","energy_difference_LTLO_HTT_eV_fu"],"properties":{"E_HTT_eV_fu":{"type":"number"},"E_LTLO_eV_fu":{"type":"number"},"energy_difference_LTLO_HTT_eV_fu":{"type":"number"}}}
- Scoring: scored by hidden verifier

### Step 8: Compute density of states for LTLO
- Role: process
- Action: Using the relaxed LTLO structure, run a non-self-consistent DFT calculation with a denser k-point mesh to obtain accurate Kohn-Sham eigenvalues for DOS calculation.
- Evidence: none

### Step 9: Output LTLO DOS splitting
- Role: scored
- Action: Compute the density of states from the eigenvalues, locate the two peaks near the Fermi level, and write their energies and the splitting in meV to LTLO_DOS_splitting.json.
- Output file: `/app/outputs/LTLO_DOS_splitting.json`
- Format: json
- Contract: {"type":"object","required":["peak1_energy_meV","peak2_energy_meV","splitting_meV"],"properties":{"peak1_energy_meV":{"type":"number"},"peak2_energy_meV":{"type":"number"},"splitting_meV":{"type":"number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/HTT_phonon_X.json`
- `/app/outputs/LTLO_phonon_X.json`
- `/app/outputs/total_energy_comparison.json`
- `/app/outputs/LTLO_DOS_splitting.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### HTT_phonon_X.json
- path: `/app/outputs/HTT_phonon_X.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: HTT phonon frequencies at the X point; scored against paper-reported unstable mode frequency.
- schema:
  - `type`: object
  - `required`: `lowest_frequency_cm-1`, `all_frequencies_X`
  - `properties`:
    - `lowest_frequency_cm-1`:
      - `type`: number
    - `all_frequencies_X`:
      - `type`: array
      - `items`:
        - `type`: number

### LTLO_phonon_X.json
- path: `/app/outputs/LTLO_phonon_X.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: LTLO phonon frequencies at the X point; structural check that no imaginary frequencies exist.
- schema:
  - `type`: object
  - `required`: `lowest_frequency_cm-1`, `all_frequencies_X`
  - `properties`:
    - `lowest_frequency_cm-1`:
      - `type`: number
    - `all_frequencies_X`:
      - `type`: array
      - `items`:
        - `type`: number

### total_energy_comparison.json
- path: `/app/outputs/total_energy_comparison.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energy per formula unit of HTT and LTLO, and their difference; compared to paper reference.
- schema:
  - `type`: object
  - `required`: `E_HTT_eV_fu`, `E_LTLO_eV_fu`, `energy_difference_LTLO_HTT_eV_fu`
  - `properties`:
    - `E_HTT_eV_fu`:
      - `type`: number
    - `E_LTLO_eV_fu`:
      - `type`: number
    - `energy_difference_LTLO_HTT_eV_fu`:
      - `type`: number

### LTLO_DOS_splitting.json
- path: `/app/outputs/LTLO_DOS_splitting.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Density of states peak splitting near Fermi level in LTLO; scored against paper value.
- schema:
  - `type`: object
  - `required`: `peak1_energy_meV`, `peak2_energy_meV`, `splitting_meV`
  - `properties`:
    - `peak1_energy_meV`:
      - `type`: number
    - `peak2_energy_meV`:
      - `type`: number
    - `splitting_meV`:
      - `type`: number

Notes: All scored artifacts require prior DFT heavy steps; no gold values or tolerances are given in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "HTT_phonon_X.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lowest_frequency_cm-1",
          "all_frequencies_X"
        ],
        "properties": {
          "lowest_frequency_cm-1": {
            "type": "number"
          },
          "all_frequencies_X": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "HTT phonon frequencies at the X point; scored against paper-reported unstable mode frequency."
    },
    {
      "file": "LTLO_phonon_X.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "lowest_frequency_cm-1",
          "all_frequencies_X"
        ],
        "properties": {
          "lowest_frequency_cm-1": {
            "type": "number"
          },
          "all_frequencies_X": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "LTLO phonon frequencies at the X point; structural check that no imaginary frequencies exist."
    },
    {
      "file": "total_energy_comparison.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "E_HTT_eV_fu",
          "E_LTLO_eV_fu",
          "energy_difference_LTLO_HTT_eV_fu"
        ],
        "properties": {
          "E_HTT_eV_fu": {
            "type": "number"
          },
          "E_LTLO_eV_fu": {
            "type": "number"
          },
          "energy_difference_LTLO_HTT_eV_fu": {
            "type": "number"
          }
        }
      },
      "description": "Total energy per formula unit of HTT and LTLO, and their difference; compared to paper reference."
    },
    {
      "file": "LTLO_DOS_splitting.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "peak1_energy_meV",
          "peak2_energy_meV",
          "splitting_meV"
        ],
        "properties": {
          "peak1_energy_meV": {
            "type": "number"
          },
          "peak2_energy_meV": {
            "type": "number"
          },
          "splitting_meV": {
            "type": "number"
          }
        }
      },
      "description": "Density of states peak splitting near Fermi level in LTLO; scored against paper value."
    }
  ],
  "notes": "All scored artifacts require prior DFT heavy steps; no gold values or tolerances are given in the public contract."
}
```

## How you are scored
A hidden verifier reads your four JSON artifacts and scores each independently against reference values and structural constraints derived from the original study. The verifier checks that the HTT and LTLO phonon frequencies are computed at the correct k-point and that the LTLO frequencies contain no negative values; it compares the extracted lowest frequency and total energy difference against hidden gold thresholds; and it validates the DOS peak splitting against a hidden tolerance. Each of the four outputs carries a weight that contributes to the final reward, with the load-bearing HTT phonon output receiving the highest weight. Passing the task requires producing numerically correct outputs that correspond to an honest execution of the entire DFT workflow; reporting the reference numbers without genuine computation will not satisfy the hidden checks.
