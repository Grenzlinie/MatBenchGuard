# Li2MnSiO4 Defect Energetics and Li-ion Mobility via Classical Potential Simulations

## Problem background
Lithium-ion batteries are central to portable energy storage, and cathode materials largely determine their performance. The orthosilicate Li₂MnSiO₄ has attracted interest because, in principle, extraction of two lithium ions is possible, enabling higher capacity. The material exists in at least two polymorphs — monoclinic (space group P2₁/n) and orthorhombic (Pmn2₁) — and both show complex defect chemistry, Li‑ion mobility, and doping behaviour that are crucial to understanding its electrochemical properties. Atomistic simulations using classical interatomic potentials can provide quantitative predictions of defect formation energies, migration barriers, and dopant incorporation energetics, guiding materials design without requiring experimental synthesis.

## Approach
All calculations are performed with the GULP (General Utility Lattice Program) classical simulation code, using the interatomic potentials and shell model parameters supplied in this instruction. The simulation framework is built on the Born model: long‑range Coulombic interactions and short‑range Buckingham repulsion plus a three‑body O–Si–O angular term to maintain the tetrahedral SiO₄ units. Electronic polarisation is captured by a shell model for Mn²⁺ and O²⁻ ions. The two crystal structures are first optimised under constant pressure to obtain relaxed lattice parameters and atomic positions. Isolated point‑defect energies (vacancies and interstitials) are then computed within the Mott–Littleton approach and combined according to defect reaction equations to yield formation energies for Li, Mn, and O Frenkel pairs, full Schottky disorder, Li/Mn anti‑site disorder, and two off‑stoichiometry oxidation processes (lithium deficiency and oxygen excess). For Li‑ion migration, the energy profile along each candidate path is mapped by stepping the migrating ion along the path and relaxing the surrounding lattice, giving an activation barrier. Finally, trivalent dopant incorporation energies are evaluated by substituting Al³⁺ (and Ga³⁺) onto Li, Mn, and Si sites with the appropriate charge‑compensation mechanisms (Li interstitial for the Si site, Mn vacancies for the Li and Mn sites) and combining the calculated defect energies with the lattice energies of the binary oxides of the dopant. The required interatomic potentials for the dopant oxides are also supplied. Every required parameter and starting structure is given in the workflow steps; the agent must implement the energy‑calculation pipeline end‑to‑end.

## Reproduction target
Produce the following three numerical CSV artifacts by executing the ordered workflow steps described below:

1. Intrinsic defect formation energies for both monoclinic and orthorhombic Li₂MnSiO₄: compute the energy (eV) for each of the seven defect types — Li Frenkel, Mn Frenkel, O Frenkel, full Schottky, Li/Mn anti‑site, Li‑deficiency oxidation, and oxygen‑excess oxidation. Write results to intrinsic_defect_energies.csv.

2. Lithium‑ion migration activation energies: determine the minimum‑energy barrier (eV) for the low‑energy Li‑hopping paths A and B in monoclinic and path X in orthorhombic. Optionally include other paths (C, D, Y). Report the data in li_migration_energies.csv with columns for polymorph, path label, jump distance (Å, optional), and energy.

3. Trivalent dopant incorporation energies: calculate the incorporation energy (eV) for Al³⁺ substituting on the Si site (with Li interstitial compensation) in both polymorphs. Also compute energies for Al³⁺ on Mn and Li sites, and for Ga³⁺ on all three sites, as supporting data. Write all entries to dopant_incorporation_energies.csv with columns for polymorph, dopant, site, and energy.

The output files must be written to /app/outputs as specified in the workflow steps. The structural optimisation step is a prerequisite; its results are not directly scored, but the subsequent scored steps rely on it.

## Assets

- GULP (General Utility Lattice Program): http://gulp.curtin.edu.au/gulp/

## Workflow steps

### Step 1: Structural optimization of Li2MnSiO4 polymorphs
- Role: process
- Action: Using GULP and the provided interatomic potentials (Buckingham two-body, three-body O-Si-O, and shell model parameters), perform constant-pressure lattice optimization for the monoclinic (P2_1/n) and orthorhombic (Pmn2_1) phases of Li2MnSiO4 starting from the given initial lattice parameters and atomic positions. This is a prerequisite for all subsequent defect and migration calculations.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: Compute intrinsic defect formation energies
- Role: scored (load-bearing)
- Action: Calculate isolated point defect energies (vacancies, interstitials) in both optimized polymorphs and combine them according to the defect reaction equations for Li Frenkel, Mn Frenkel, O Frenkel, full Schottky, Li/Mn anti-site, Li-deficiency oxidation, and oxygen-excess oxidation. Write the resulting formation energies to intrinsic_defect_energies.csv.
- Output file: `/app/outputs/intrinsic_defect_energies.csv`
- Format: csv
- Contract: polymorph,defect_type,energy_eV
- Scoring: scored by hidden verifier

### Step 3: Compute lithium migration activation energies
- Role: scored
- Action: Determine the minimum energy paths for Li-ion hopping along migration pathways A and B in the monoclinic phase and pathway X in the orthorhombic phase. For each path, map the potential energy surface by moving the migrating Li-ion along the path and relaxing the surrounding lattice, then extract the activation barrier. Optionally compute additional paths (C, D for monoclinic; Y for orthorhombic). Write the migration energies and jump distances to li_migration_energies.csv.
- Output file: `/app/outputs/li_migration_energies.csv`
- Format: csv
- Contract: polymorph,path_label,jump_distance_A,energy_eV
- Scoring: scored by hidden verifier

### Step 4: Compute trivalent dopant incorporation energies
- Role: scored (load-bearing)
- Action: Calculate the incorporation energies for Al³⁺ (and optionally Ga³⁺) substituting on Si, Mn, and Li sites in both polymorphs, using the appropriate compensation mechanism (Li interstitial for Si site, Mn vacancy for Mn and Li sites as derived from charge neutrality). Combine calculated defect and lattice energies of binary oxides using the provided dopant-oxide potentials. Write the results to dopant_incorporation_energies.csv.
- Output file: `/app/outputs/dopant_incorporation_energies.csv`
- Format: csv
- Contract: polymorph,dopant,site,energy_eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intrinsic_defect_energies.csv`
- `/app/outputs/li_migration_energies.csv`
- `/app/outputs/dopant_incorporation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intrinsic_defect_energies.csv
- path: `/app/outputs/intrinsic_defect_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Intrinsic defect formation energies for both polymorphs. Lower (more negative) values indicate more favorable defects. The checker compares each reported energy to a hidden paper-derived threshold with tolerance; values at or below the threshold pass.
- schema:
  - `type`: table
  - `required_columns`: `polymorph`, `defect_type`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### li_migration_energies.csv
- path: `/app/outputs/li_migration_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Li-ion migration activation energies. Lower barriers indicate higher mobility. The checker scores paths A and B for monoclinic and path X for orthorhombic against hidden thresholds (with tolerance) in a threshold-or-better manner.
- schema:
  - `type`: table
  - `required_columns`: `polymorph`, `path_label`, `energy_eV`
  - `units`:
    - `energy_eV`: eV
    - `jump_distance_A`: Å

### dopant_incorporation_energies.csv
- path: `/app/outputs/dopant_incorporation_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Trivalent dopant incorporation energies. Lower energies indicate more favorable substitution. Only Al³⁺ on the Si site entries for both polymorphs are scored; the checker uses hidden thresholds with tolerance, accepting values at or below the threshold as correct.
- schema:
  - `type`: table
  - `required_columns`: `polymorph`, `dopant`, `site`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

Notes: The structural optimization (step_01) is a required process step but not directly scored. Only specific entries in each CSV are scored as described; the agent should still report all computed values for completeness. The hidden checker applies absolute tolerances when comparing to paper-reported energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intrinsic_defect_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymorph",
          "defect_type",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Intrinsic defect formation energies for both polymorphs. Lower (more negative) values indicate more favorable defects. The checker compares each reported energy to a hidden paper-derived threshold with tolerance; values at or below the threshold pass."
    },
    {
      "file": "li_migration_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymorph",
          "path_label",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV",
          "jump_distance_A": "Å"
        }
      },
      "description": "Li-ion migration activation energies. Lower barriers indicate higher mobility. The checker scores paths A and B for monoclinic and path X for orthorhombic against hidden thresholds (with tolerance) in a threshold-or-better manner."
    },
    {
      "file": "dopant_incorporation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymorph",
          "dopant",
          "site",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Trivalent dopant incorporation energies. Lower energies indicate more favorable substitution. Only Al³⁺ on the Si site entries for both polymorphs are scored; the checker uses hidden thresholds with tolerance, accepting values at or below the threshold as correct."
    }
  ],
  "notes": "The structural optimization (step_01) is a required process step but not directly scored. Only specific entries in each CSV are scored as described; the agent should still report all computed values for completeness. The hidden checker applies absolute tolerances when comparing to paper-reported energies."
}
```

## How you are scored
The repository includes a hidden verifier that inspects the CSV files you produce. Only specific entries are graded:

- intrinsic_defect_energies.csv: all defect types for both polymorphs.
- li_migration_energies.csv: paths A and B for monoclinic; path X for orthorhombic.
- dopant_incorporation_energies.csv: only the Al³⁺‑on‑Si entries for both polymorphs.

The verifier compares each of your computed energies to a set of hidden reference thresholds derived from the published scientific work. The comparison uses a threshold‑or‑better policy: if your energy is at or below the hidden threshold (i.e., more negative, indicating a more favourable defect, migration, or doping process), the entry passes. The hidden thresholds include a tolerance to absorb legitimate numerical differences that arise from running the calculations on different machines or with slightly different implementation choices.

The reward for the task is the weighted fraction of scored entries that pass. The exact thresholds and tolerances are not disclosed; you must faithfully implement the prescribed methodology and produce physically meaningful numbers — not attempt to guess the target values. Partial credit is awarded proportionally, and entries not listed as scored entries are ignored for grading.
