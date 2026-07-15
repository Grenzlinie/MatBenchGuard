# Hydrogen interstitial formation energies in Ti3SiC2

## Problem background
Ti3SiC2 is a MAX-phase ceramic that combines metallic and ceramic properties, making it a candidate for high-temperature structural applications. In service environments, exposure to hydrogen may cause embrittlement—a well-known degradation mechanism in metals where dissolved hydrogen reduces cohesive strength. It is unclear whether Ti3SiC2, with its mixed covalent-ionic-metallic bonding, resists such degradation. This investigation uses density functional theory (DFT) to compute the formation energies of hydrogen interstitials in Ti3SiC2 and the associated lattice volume changes, providing insight into site preference and the influence of hydrogen on bonding.

## Approach
First-principles DFT calculations are performed within the generalized gradient approximation (GGA-PBE) using plane-wave basis sets and norm-conserving pseudopotentials. A perfect Ti3SiC2 supercell is fully relaxed to its equilibrium geometry, and the total energy of an isolated hydrogen atom is computed in a large periodic box with spin polarization. Three interstitial sites with large free volumes are examined: I-Ti (tetrahedral, surrounded by three Ti(1) and one Ti(2) atoms), I-SiTi (hexahedral, surrounded by three Si and two Ti(2) atoms), and I-SiC (tetrahedral, surrounded by three Si and one C atom). For each site, a single H atom is placed near the site centre in the relaxed perfect supercell, and the atomic positions and cell parameters are fully relaxed. The formation energy is obtained as E_H^f = E(Ti3SiC2 + H) - E(Ti3SiC2) - E(H), and the relative volume change as ΔV = (V_doped - V_perfect)/V_perfect × 100%. The key question is which interstitial sites are energetically preferred and how the volume change correlates with formation energy.

## Reproduction target
Using an open-source DFT code (e.g., Quantum ESPRESSO) and suitable norm-conserving pseudopotentials, compute:
- The total energy of the perfect Ti3SiC2 supercell.
- The total energy of an isolated H atom.
- For each of the three interstitial sites (I-Ti, I-SiTi, I-SiC): the formation energy E_H^f (eV) and the relative volume change ΔV (%).
The primary objective is to determine the energetic ordering of the three sites (which sites are most/least stable) and the ordering of the volume changes.

## Assets

- Ti3SiC2 crystal structure: https://next-gen.materialsproject.org/materials/mp-925
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/download
- Norm-conserving pseudopotentials (PseudoDojo or SG15): http://www.pseudo-dojo.org

## Workflow steps

### Step 1: Crystal structure preparation
- Role: process
- Action: Retrieve the Ti3SiC2 crystal structure from a public source (e.g., Materials Project mp-925) and build the 2×1×1 supercell with the correct Wyckoff positions. Prepare input files for the subsequent DFT relaxation.
- Evidence: none

### Step 2: Relax perfect Ti3SiC2 supercell
- Role: scored
- Action: Perform DFT geometry optimization (full relaxation of atomic positions and lattice parameters) on the perfect 2×1×1 Ti3SiC2 supercell using GGA-PBE, norm-conserving pseudopotentials, a suitable plane-wave cutoff, and a Monkhorst–Pack k-point grid appropriate for the supercell size. Extract the final total energy in eV and write it to a single-line text file.
- Output file: `/app/outputs/perfect_cell_energy.txt`
- Format: txt
- Contract: A single line containing a floating-point number representing the total energy in eV.
- Scoring: scored by hidden verifier

### Step 3: Isolated hydrogen atom energy
- Role: scored
- Action: Compute the total energy of an isolated hydrogen atom using the same pseudopotential and plane-wave cutoff (large periodic box, spin-polarized). Write the energy in eV to a single-line text file.
- Output file: `/app/outputs/isolated_H_energy.txt`
- Format: txt
- Contract: A single line containing a floating-point number in eV.
- Scoring: scored by hidden verifier

### Step 4: Hydrogen interstitial relaxation and formation energies
- Role: scored (load-bearing)
- Action: For each of the three interstitial sites: (a) I-Ti: tetrahedral site surrounded by three Ti(1) and one Ti(2) atoms; (b) I-SiTi: hexahedral site surrounded by three Si and two Ti(2) atoms; (c) I-SiC: tetrahedral site surrounded by three Si and one C atom, place a single H atom at the approximate centre of the site in the relaxed perfect supercell. Perform full relaxation (atomic positions and cell parameters) with the same DFT settings. Extract the total energy and relaxed supercell volume. Compute the formation energy E_H^f = E(doped) – E(perfect) – E(H) using the previously obtained total energies, and the relative volume change ΔV = (V_doped – V_perfect)/V_perfect × 100%. Write a CSV with columns site, E_H_f (eV), delta_V (%).
- Output file: `/app/outputs/interstitial_results.csv`
- Format: csv
- Contract: CSV with header: site,E_H_f,delta_V. Three data rows (I-Ti, I-SiTi, I-SiC) with numeric formation energy in eV and volume change in percent.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/perfect_cell_energy.txt`
- `/app/outputs/isolated_H_energy.txt`
- `/app/outputs/interstitial_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### perfect_cell_energy.txt
- path: `/app/outputs/perfect_cell_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Total energy of the relaxed perfect Ti3SiC2 supercell, used as a reference for formation energies and checked against a hidden reference value.
- schema:
  - `type`: text
  - `description`: A single line containing the total energy in eV as a floating-point number.

### isolated_H_energy.txt
- path: `/app/outputs/isolated_H_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Total energy of an isolated hydrogen atom, used as a reference for formation energies and checked against a hidden reference value.
- schema:
  - `type`: text
  - `description`: A single line containing the total energy in eV as a floating-point number.

### interstitial_results.csv
- path: `/app/outputs/interstitial_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies and relaxed volume changes for the three interstitial sites. The checker evaluates the relative ordering of formation energies (I-SiC ≈ I-SiTi < I-Ti) and volume changes (I-SiC < I-SiTi < I-Ti).
- schema:
  - `type`: table
  - `required_columns`: `site`, `E_H_f`, `delta_V`
  - `units`:
    - `E_H_f`: eV
    - `delta_V`: %

Notes: The primary verification is structural: the correct energetic ordering of the three sites. Additional reference checks compare absolute total energies (perfect_cell_energy.txt, isolated_H_energy.txt) against hidden paper-derived values with generous tolerance to account for code/pseudopotential differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "perfect_cell_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the total energy in eV as a floating-point number."
      },
      "description": "Total energy of the relaxed perfect Ti3SiC2 supercell, used as a reference for formation energies and checked against a hidden reference value."
    },
    {
      "file": "isolated_H_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the total energy in eV as a floating-point number."
      },
      "description": "Total energy of an isolated hydrogen atom, used as a reference for formation energies and checked against a hidden reference value."
    },
    {
      "file": "interstitial_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "E_H_f",
          "delta_V"
        ],
        "units": {
          "E_H_f": "eV",
          "delta_V": "%"
        }
      },
      "description": "Formation energies and relaxed volume changes for the three interstitial sites. The checker evaluates the relative ordering of formation energies (I-SiC ≈ I-SiTi < I-Ti) and volume changes (I-SiC < I-SiTi < I-Ti)."
    }
  ],
  "notes": "The primary verification is structural: the correct energetic ordering of the three sites. Additional reference checks compare absolute total energies (perfect_cell_energy.txt, isolated_H_energy.txt) against hidden paper-derived values with generous tolerance to account for code/pseudopotential differences."
}
```

## How you are scored
A hidden verifier evaluates each output file independently. The total energies in `perfect_cell_energy.txt` and `isolated_H_energy.txt` are checked against hidden reference values with generous tolerances that account for differences between DFT codes and pseudopotential choices. The main scored file is `interstitial_results.csv`, where the verifier compares the relative ordering of the formation energies (which site is most stable, intermediate, least stable) and the relative ordering of the volume changes against the ordering determined by the paper's own DFT calculations. Correct ordering yields full credit; partial credit is awarded when the trend is correct even if the absolute numbers deviate. Reporting numbers without performing the required DFT relaxations is unlikely to match the expected structural signatures and will score very low. The reward is monotonic: better agreement with the reference ordering (within tolerances) always yields a higher score.
