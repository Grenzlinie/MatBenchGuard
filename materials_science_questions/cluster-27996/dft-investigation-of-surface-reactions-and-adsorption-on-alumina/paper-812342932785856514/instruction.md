# Constrained proton potential energy scan and adsorption properties on chabazite O3 acid site

## Problem background
Zeolites are among the most important industrial solid-acid catalysts. Their Brønsted acidity arises from bridging hydroxyl groups (Si–OH–Al) located at framework oxygen sites, but quantifying the acid strength of these sites remains a challenge. It is debated whether the acid sites within a single zeolite are homogeneous or show significant variations in strength, and which computational or experimental proxies best capture acidity. Understanding the proton potential energy surface at a specific acid site, and computing quantities such as deprotonation energy, O–H vibrational frequency, and adsorption energies of probe bases, can shed light on these questions. Chabazite (SSZ-13) is a small-unit-cell zeolite that can be modeled with periodic density functional theory, making it a practical system for first-principles investigations. This task focuses on the O3 acid site in chabazite and requires mapping the proton potential energy surface and determining key energetic and vibrational properties.

## Approach
The study is carried out using periodic density functional theory (DFT) with the PW91 generalized gradient approximation (GGA) for exchange and correlation. A plane-wave basis set and norm-conserving pseudopotentials represent the electrons and atomic cores, respectively. Starting from published neutron diffraction coordinates of chabazite, a single silicon atom is substituted by aluminum (Si/Al = 11) and a proton is placed on the O3 oxygen. After a full geometry optimization of the protonated framework (with fixed lattice vectors), the proton out-of-plane angle relative to the Al–O–Si plane is constrained to a series of fixed values, and a geometry optimization is performed at each constraint. This series of constrained relaxations yields the potential energy of the proton as a function of angular displacement. The same optimized protonated structure is used to compute three additional properties: (i) the deprotonation energy, obtained by removing the proton, re-optimizing the anionic framework, and taking the energy difference; (ii) the harmonic O–H stretch frequency, evaluated via finite-difference derivatives of the forces; and (iii) the ammonia adsorption energy, computed as the energy difference between the optimized zeolite–NH₃ complex and the sum of the isolated zeolite and isolated ammonia energies.

## Reproduction target
Produce a CSV file (constrained_scan.csv) containing the out-of-plane angle (degrees), total electronic energy (Hartree), and relative energy (kJ/mol, referenced to the unconstrained optimized minimum) for at least 20 distinct angles spanning approximately −60° to +60°. Additionally, produce a JSON file (step_02_properties.json) reporting the deprotonation energy (kJ/mol), the O–H harmonic stretching frequency (cm⁻¹), and the ammonia adsorption energy (kJ/mol) for the O3 acid site. The hidden verifier will analyze the angle–energy curve to locate local minima and their separation, and compare the three scalar properties to reference values.

## Assets

- Plane-wave DFT code with PW91 functional and norm-conserving pseudopotentials (CPMD or equivalent such as Quantum ESPRESSO, ABINIT): https://www.cpmd.org/ (CPMD) or https://www.quantum-espresso.org/ (QE)
- Troullier–Martins norm-conserving pseudopotentials for Si, Al, O, H
- Crystallographic coordinates of chabazite (SSZ-13) from neutron diffraction by Smith et al. (1997): 10.1007/BF00784754

## Workflow steps

### Step 1: Setup and geometry optimization of periodic chabazite (1 Al/unit cell, proton on O3)
- Role: process
- Action: Construct a periodic chabazite unit cell using the crystallographic coordinates from Smith et al. (1997) with one Al replacing Si (Si/Al = 11) and a proton placed on the O3 oxygen. Perform a full DFT geometry optimization using the PW91 GGA functional, a plane-wave basis, Γ-point sampling, and Troullier–Martins norm-conserving pseudopotentials. All atoms are free to move while lattice vectors are fixed. The resulting relaxed structure is used in subsequent steps.
- Evidence: `/app/outputs/optimized_structure.xyz`

### Step 2: Constrained geometry scan – O3 proton out-of-plane angle
- Role: scored (load-bearing)
- Action: Starting from the optimized O3-protonated chabazite structure, perform a series of geometry optimizations in which the proton out‑of‑plane angle (relative to the Al–O–Si plane) is constrained to fixed values. Scan angles from approximately −60° to +60° in steps fine enough to resolve two local minima (at least 20 distinct angles). Record the DFT total energy at each constrained angle, and report the energies relative to the unconstrained optimized minimum (angle = 0).
- Output file: `/app/outputs/constrained_scan.csv`
- Format: csv
- Contract: Columns: out_of_plane_angle (float, degrees), total_energy_Ha (float, Hartree), relative_energy_kJmol (float, kJ/mol). Each row corresponds to one constrained optimization.
- Scoring: scored by hidden verifier

### Step 3: Deprotonation energy, O–H vibrational frequency, and ammonia adsorption energy for all four acid sites (O1–O4)
- Role: scored
- Action: For each of the four acid sites (O1, O2, O3, O4) in chabazite (1 Al/unit cell), compute the three properties listed below. 1) Deprotonation energy: for each site, calculate the total energy of the deprotonated (anionic) framework with the proton removed from that specific oxygen, allowing full framework relaxation, and obtain ΔE = E(deprotonated) − E(protonated). 2) O–H vibrational frequency: compute the harmonic stretch frequency of the bridging O–H group at each site using finite differences of forces or an equivalent vibrational analysis on the optimized protonated structure. 3) Ammonia adsorption energy: for each site, optimize an ammonia molecule adsorbed on the acid site and compute Eads = E(zeolite+NH3) − [E(zeolite) + E(NH3)], where the isolated NH3 molecule is relaxed in the same cell. Report all values in a single JSON file.
- Output file: `/app/outputs/step_02_properties.json`
- Format: json
- Contract: {"acid_sites": [{"site": "O1" | "O2" | "O3" | "O4", "deprotonation_energy_kJmol": <float> (kJ/mol), "oh_stretch_frequency_cm1": <float> (cm⁻¹), "ammonia_adsorption_energy_kJmol": <float> (kJ/mol)}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/constrained_scan.csv`
- `/app/outputs/step_02_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### constrained_scan.csv
- path: `/app/outputs/constrained_scan.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Potential energy scan of the proton out-of-plane angle on the O3 oxygen. The checker will fit a cubic spline to the energy curve, locate the two local minima, and compare their angles and the energy difference to the paper-reported values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `out_of_plane_angle`, `total_energy_Ha`, `relative_energy_kJmol`
  - `units`:
    - `out_of_plane_angle`: degrees
    - `total_energy_Ha`: Hartree
    - `relative_energy_kJmol`: kJ/mol

### step_02_properties.json
- path: `/app/outputs/step_02_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed deprotonation energy, O–H vibrational stretch frequency, and ammonia adsorption energy for each of the four acid sites O1–O4. The checker compares each site's values to the paper-reported values within tolerances, testing the homogeneity conclusion.
- schema:
  - `type`: object
  - `required`: `acid_sites`
  - `properties`:
    - `acid_sites`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `site`, `deprotonation_energy_kJmol`, `oh_stretch_frequency_cm1`, `ammonia_adsorption_energy_kJmol`
        - `properties`:
          - `site`:
            - `type`: string
            - `enum`: `O1`, `O2`, `O3`, `O4`
          - `deprotonation_energy_kJmol`:
            - `type`: number
            - `units`: kJ/mol
          - `oh_stretch_frequency_cm1`:
            - `type`: number
            - `units`: cm⁻¹
          - `ammonia_adsorption_energy_kJmol`:
            - `type`: number
            - `units`: kJ/mol

Notes: The scan artifact remains focused on O3 to identify proton minima. The properties artifact now contains all four acid sites, allowing the verifier to check cross-site comparisons required by the paper's central claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "constrained_scan.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "out_of_plane_angle",
          "total_energy_Ha",
          "relative_energy_kJmol"
        ],
        "units": {
          "out_of_plane_angle": "degrees",
          "total_energy_Ha": "Hartree",
          "relative_energy_kJmol": "kJ/mol"
        }
      },
      "description": "Potential energy scan of the proton out-of-plane angle on the O3 oxygen. The checker will fit a cubic spline to the energy curve, locate the two local minima, and compare their angles and the energy difference to the paper-reported values with appropriate tolerances."
    },
    {
      "file": "step_02_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "acid_sites"
        ],
        "properties": {
          "acid_sites": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "site",
                "deprotonation_energy_kJmol",
                "oh_stretch_frequency_cm1",
                "ammonia_adsorption_energy_kJmol"
              ],
              "properties": {
                "site": {
                  "type": "string",
                  "enum": [
                    "O1",
                    "O2",
                    "O3",
                    "O4"
                  ]
                },
                "deprotonation_energy_kJmol": {
                  "type": "number",
                  "units": "kJ/mol"
                },
                "oh_stretch_frequency_cm1": {
                  "type": "number",
                  "units": "cm⁻¹"
                },
                "ammonia_adsorption_energy_kJmol": {
                  "type": "number",
                  "units": "kJ/mol"
                }
              }
            }
          }
        }
      },
      "description": "Computed deprotonation energy, O–H vibrational stretch frequency, and ammonia adsorption energy for each of the four acid sites O1–O4. The checker compares each site's values to the paper-reported values within tolerances, testing the homogeneity conclusion."
    }
  ],
  "notes": "The scan artifact remains focused on O3 to identify proton minima. The properties artifact now contains all four acid sites, allowing the verifier to check cross-site comparisons required by the paper's central claims."
}
```

## How you are scored
A hidden verifier reads your constrained_scan.csv and fits a smooth spline to the angle–energy table. From the fitted curve it identifies any local minima, extracts their angular positions, and computes the energy difference between the two lowest-energy minima. These extracted quantities are compared to expected values within prescribed tolerances. The verifier also reads your step_02_properties.json and compares each reported number (deprotonation energy, frequency, adsorption energy) to reference values, again within tolerances. The final reward is a weighted sum: the scan analysis (correct identification of the minima and their energy difference) carries the majority of the weight, while each of the three scalar properties carries a smaller equal weight. Missing or malformed output fields receive zero credit for that component.
