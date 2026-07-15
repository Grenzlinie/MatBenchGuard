# Magnetic Properties of V-Doped ZnO Nanotubes via DFT

## Problem background
ZnO nanotubes are promising host structures for dilute magnetic semiconductors, where substituting a small fraction of Zn ions with transition-metal impurities can induce spontaneous magnetization. This task focuses on the effect of vanadium (V) doping on the electronic and magnetic properties of a single-walled ZnO nanotube. First-principles density functional theory (DFT) is used to predict the magnetic moment on the dopant atom, the total magnetization of the system, and the spin-resolved electronic band structure, which may reveal half-metallic behavior. Understanding these properties is relevant for developing transparent ferromagnets and magneto‑optical devices.

## Approach
The workflow constructs a (9,0) zigzag single-walled ZnO nanotube from the wurtzite crystal structure using lattice parameters a=0.3253 nm, c=0.521 nm. One Zn atom in the 72‑atom unit cell is replaced by a V atom. Spin-polarised DFT calculations are performed within the generalized gradient approximation using the Perdew-Wang 1991 (PW91) exchange-correlation functional. Geometry relaxation is carried out to obtain the equilibrium atomic positions, after which the magnetic moment on the V atom and total cell magnetization are extracted. A subsequent static calculation yields the spin-resolved electronic band structure and density of states (DOS). From these, the minority-spin band gap is measured and the majority-spin channel is examined for metallicity. The open-source Quantum ESPRESSO code (pw.x) with publicly available ultrasoft pseudopotentials serves as the implementation, making the entire workflow reproducible without proprietary software. A pristine (undoped) ZnO nanotube band structure is not required for scoring, but can be computed as a consistency check.

## Reproduction target
Using the V‑doped (9,0) ZnO nanotube described above, compute the following quantities after full structural relaxation and static electronic structure calculation:
1. The magnetic moment on the V atom (in μB) and the total magnetization of the supercell.
2. The band gap for the minority-spin channel (in eV) and a true/false indication of whether the majority-spin channel is metallic (no gap at the Fermi level).
Write the magnetic moment results to `/app/outputs/magnetic_moment.json` and the band-gap/metal results to `/app/outputs/band_gap.json`, following the exact schemas specified in the output contract. The relax geometry (`relaxed_structure.cif`) and band structure / DOS files (`band_structure.dat`, `dos.dat`) must also be produced as supporting evidence.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotentials (GGA-PW91) for Zn, O, V: https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase

## Workflow steps

### Step 1: Generate ZnO (9,0) nanotube structure
- Role: process
- Action: Build a wurtzite ZnO supercell with lattice parameters a=0.3253 nm, c=0.521 nm; construct a (9,0) zigzag single-walled ZnO nanotube with diameter 0.958 nm and 72 atoms per unit cell, adding 1.2 nm vacuum spacing. Save the structure as initial_nanotube.cif.
- Evidence: `/app/outputs/initial_nanotube.cif`

### Step 2: Substitute Zn with V
- Role: process
- Action: In the generated ZnO nanotube, replace one Zn atom with a V atom to create the initial V-doped nanotube; save as initial_V_doped_nanotube.cif.
- Evidence: `/app/outputs/initial_V_doped_nanotube.cif`

### Step 3: DFT geometry relaxation of V-doped nanotube
- Role: process
- Action: Perform spin-polarized DFT structural relaxation of the V-doped nanotube using GGA-PW91 exchange-correlation, saving the relaxed geometry as relaxed_structure.cif and retaining the full calculation output.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 4: Extract magnetic moment
- Role: scored (load-bearing)
- Action: From the DFT relaxation output, extract the magnetic moment on the V atom (in μB) and the total magnetization of the cell. Write a JSON file with these values.
- Output file: `/app/outputs/magnetic_moment.json`
- Format: json
- Contract: {"V_magnetic_moment_mu_B": <float>, "total_magnetization_mu_B": <float>}
- Scoring: scored by hidden verifier

### Step 5: DFT electronic structure calculation
- Role: process
- Action: Using the relaxed V-doped nanotube structure, run a spin-polarized DFT static calculation to obtain the spin-resolved band structure and total/partial density of states. Save band_structure.dat and dos.dat.
- Evidence: `/app/outputs/band_structure.dat`

### Step 6: Extract band gap and half-metallic character
- Role: scored
- Action: From the band structure and/or density of states, determine the band gap for the minority spin channel (in eV) and verify that the majority spin has no gap at the Fermi level (metallic). Write the results to band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"minority_spin_gap_eV": <float>, "majority_spin_metallic": <bool>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moment.json`
- `/app/outputs/band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moment.json
- path: `/app/outputs/magnetic_moment.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetic moment of the V atom and total magnetization of the doped nanotube after DFT relaxation.
- schema:
  - `type`: object
  - `required`: `V_magnetic_moment_mu_B`, `total_magnetization_mu_B`
  - `properties`:
    - `V_magnetic_moment_mu_B`:
      - `type`: number
      - `unit`: μB
    - `total_magnetization_mu_B`:
      - `type`: number
      - `unit`: μB

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gap of the minority spin channel and confirmation that the majority spin channel is metallic (half-metallic character).
- schema:
  - `type`: object
  - `required`: `minority_spin_gap_eV`, `majority_spin_metallic`
  - `properties`:
    - `minority_spin_gap_eV`:
      - `type`: number
      - `unit`: eV
    - `majority_spin_metallic`:
      - `type`: boolean

Notes: The hidden checker compares the reported magnetic moment and band gap to the paper-reported values within hidden tolerances; the majority_spin_metallic boolean must be true.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moment.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "V_magnetic_moment_mu_B",
          "total_magnetization_mu_B"
        ],
        "properties": {
          "V_magnetic_moment_mu_B": {
            "type": "number",
            "unit": "μB"
          },
          "total_magnetization_mu_B": {
            "type": "number",
            "unit": "μB"
          }
        }
      },
      "description": "Magnetic moment of the V atom and total magnetization of the doped nanotube after DFT relaxation."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "minority_spin_gap_eV",
          "majority_spin_metallic"
        ],
        "properties": {
          "minority_spin_gap_eV": {
            "type": "number",
            "unit": "eV"
          },
          "majority_spin_metallic": {
            "type": "boolean"
          }
        }
      },
      "description": "Band gap of the minority spin channel and confirmation that the majority spin channel is metallic (half-metallic character)."
    }
  ],
  "notes": "The hidden checker compares the reported magnetic moment and band gap to the paper-reported values within hidden tolerances; the majority_spin_metallic boolean must be true."
}
```

## How you are scored
Each scored JSON artifact is independently checked by a hidden verifier. The verifier reads your reported magnetic moment, total magnetization, minority-spin band gap, and majority-spin metallic flag and compares them to hidden reference values derived from the original study. Numeric tolerances appropriate for DFT re-runs with different implementations are applied. The verifier does not inspect your calculation logs; it only evaluates the contents of the output files listed in the output contract. Your final score is a weighted sum of the scores from the individual artifacts, with the magnetic moment and band-gap results carrying the largest weight. Producing the required intermediate structure files (CIF and data files) is mandatory and their absence may be penalised, but the primary reward comes from the JSON values.
