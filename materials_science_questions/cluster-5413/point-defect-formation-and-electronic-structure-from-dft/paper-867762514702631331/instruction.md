# Point defect formation energies and gap states of monolayer WSe₂ from DFT

## Problem background
Monolayer WSe₂ is a wide-bandgap 2D semiconductor. Point defects—especially vacancies and antisites—are common and can introduce electronic states in the band gap, strongly affecting device properties. Understanding the formation energies of intrinsic defects and whether they create gap states is critical for controlling doping, transport, and optical emission. This task aims to compute the formation energies of the most likely intrinsic point defects in monolayer WSe₂ (isolated and on a graphite substrate) using first-principles density functional theory, and to determine if a Se vacancy can be electronically passivated by substituting an oxygen atom.

## Approach
Use plane-wave density functional theory at the PBE-D2 level as implemented in Quantum ESPRESSO, with PAW pseudopotentials. Construct supercells of monolayer WSe₂ (isolated and supported on graphite) and create models for four intrinsic point defects: Se vacancy (Seᵥₐc), W vacancy (Wᵥₐc), Se antisite (Se<sub>W</sub>, where a Se atom replaces a W), and a Se divacancy (2Seᵥₐc). For each defect, relax the atomic positions and obtain the total energy. Compute chemical potentials for W and Se from reference phases (bcc W, Se₆ molecular crystal, bulk WSe₂) and evaluate formation energies under both W-rich and Se-rich limits using the standard defect formation energy expression. Separately, for the isolated monolayer, investigate the electronic density of states (DOS) of the pristine cell, the Se vacancy, and the same vacancy where the missing Se is replaced by an O atom (O<sub>Se</sub>), to determine if gap states appear. The workflow yields two quantitative results: (1) a table of defect formation energies for all four defects under the four substrate/condition combinations, and (2) a gap‑state presence table for the three systems.

## Reproduction target
Produce two CSV files under /app/outputs: formation_energies.csv and gap_state_passivation.csv. formation_energies.csv must contain, for each of the four defects (Seᵥₐc, Wᵥₐc, Se<sub>W</sub>, 2Seᵥₐc), the formation energy in eV under both W‑rich and Se‑rich chemical potentials for the isolated monolayer and for the monolayer supported on graphite (16 rows total). gap_state_passivation.csv must report, for the isolated monolayer, whether the pristine system, the Se vacancy, and the oxygen‑passivated Se vacancy (Seᵥₐc+O) possess electronic states inside the pristine band gap (3 rows, boolean). The reproduction is considered successful if the computed formation energies agree with a hidden reference within expected computational accuracy and if the defect with the lowest formation energy in each substrate/condition combination is correctly identified, and if the gap‑state passivation check returns the expected boolean values.

## Assets

- Quantum ESPRESSO (DFT package): https://www.quantum-espresso.org
- PAW pseudopotentials for W, Se, C, O, H: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Reference‑phase total energies
- Role: process
- Action: Perform DFT relaxations of bcc W, the Se₆ molecular crystal, and bulk WSe₂ (primitive cell) to obtain the total energy per atom or per formula unit.
- Evidence: `/app/outputs/reference_energies.json`

### Step 2: Relax pristine WSe₂ monolayer and WSe₂/graphite supercells
- Role: process
- Action: Build a 5×5 supercell of monolayer WSe₂ with >20 Å vacuum (isolated) and a 3×3 WSe₂ on 4×4 graphite supercell (3 graphite layers, 13 Å vacuum, <1% tensile strain on WSe₂) using relaxed lattice constants. Relax atomic positions and record total energies of the pristine cells.
- Evidence: `/app/outputs/pristine_energies.json`

### Step 3: Relax intrinsic defect supercells
- Role: process
- Action: Using the relaxed pristine supercells, create supercells containing a single intrinsic defect (Seᵥₐc, Wᵥₐc, Sew, 2Seᵥₐc) in both isolated monolayer and supported WSe₂/graphite. Relax each defect geometry and record its total energy.
- Evidence: `/app/outputs/defect_energies.json`

### Step 4: Relax Seᵥₐc passivated by O atom
- Role: process
- Action: Create a supercell of isolated monolayer WSe₂ with a Se vacancy and substitute an O atom at that site (OSe). Relax the geometry and record its total energy.
- Evidence: `/app/outputs/opassivation_energy.json`

### Step 5: Compute formation energies of intrinsic defects
- Role: scored (load-bearing)
- Action: Using total energies from reference phases, pristine and defect supercells, calculate the chemical potentials μW and μSe for both W‑rich (μSe = μSe_min) and Se‑rich (μSe = μSe_max) limits. Compute the formation energy for each defect under each condition and substrate. Write the per‑row results to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: defect (str), condition (str: 'W-rich' or 'Se-rich'), substrate (str: 'isolated' or 'supported'), formation_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Compute density of states (DOS) for pristine, Seᵥₐc, and OSe
- Role: process
- Action: For the isolated monolayer, perform non‑self‑consistent PBE‑D2 calculations with dense k‑mesh to obtain the density of states for (i) pristine supercell, (ii) Seᵥₐc defect supercell, (iii) OSe supercell. Align the energy scales using a common core‑level reference (e.g., deepest W 1s core level far from the defect).
- Evidence: `/app/outputs/dos_data.json`

### Step 7: Identify presence of gap states
- Role: scored (load-bearing)
- Action: From the computed DOS, determine the energy range of the pristine band gap. For each system (pristine, Seᵥₐc, OSe), check whether any electronic states appear inside that gap. Write the result to gap_state_passivation.csv.
- Output file: `/app/outputs/gap_state_passivation.csv`
- Format: csv
- Contract: system (str: 'pristine', 'Sevac', 'Sevac+O'), has_gap_states (bool: True if defect states within pristine band gap)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/gap_state_passivation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation energies of Seᵥₐc, Wᵥₐc, Sew, 2Seᵥₐc for isolated and supported monolayer WSe₂ under W‑rich and Se‑rich chemical potentials. The checker compares each reported formation energy to hidden paper‑reported values within an absolute tolerance and verifies that Seᵥₐc has the lowest formation energy among the four defects for each substrate/condition combination.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `condition`, `substrate`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

### gap_state_passivation.csv
- path: `/app/outputs/gap_state_passivation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Gap‑state presence for pristine (false), Seᵥₐc (true), and oxygen‑passivated Seᵥₐc (false) in isolated monolayer WSe₂. The checker verifies these exact boolean expectations.
- schema:
  - `type`: table
  - `required_columns`: `system`, `has_gap_states`

Notes: The task covers the main intrinsic defect formation energies and the passivation of gap states by oxygen. Ionization energies, STM simulation, extrinsic defects beyond O passivation, and functional benchmarks are omitted per taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "condition",
          "substrate",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Formation energies of Seᵥₐc, Wᵥₐc, Sew, 2Seᵥₐc for isolated and supported monolayer WSe₂ under W‑rich and Se‑rich chemical potentials. The checker compares each reported formation energy to hidden paper‑reported values within an absolute tolerance and verifies that Seᵥₐc has the lowest formation energy among the four defects for each substrate/condition combination."
    },
    {
      "file": "gap_state_passivation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "has_gap_states"
        ]
      },
      "description": "Gap‑state presence for pristine (false), Seᵥₐc (true), and oxygen‑passivated Seᵥₐc (false) in isolated monolayer WSe₂. The checker verifies these exact boolean expectations."
    }
  ],
  "notes": "The task covers the main intrinsic defect formation energies and the passivation of gap states by oxygen. Ionization energies, STM simulation, extrinsic defects beyond O passivation, and functional benchmarks are omitted per taskability scope."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads your two CSV files. For formation_energies.csv, the verifier compares each formation energy to a hidden reference value using an appropriate tolerance and confirms that the Se vacancy (Seᵥₐc) has the lowest formation energy among the four defects for each of the four substrate–condition combinations. For gap_state_passivation.csv, the verifier checks that the three boolean entries match hidden expected values. The total score is a weighted combination where formation_energies.csv carries the majority of the weight. Simply printing the paper's numbers is not sufficient—you must genuinely execute the full DFT workflow and derive your results from your own calculations.
