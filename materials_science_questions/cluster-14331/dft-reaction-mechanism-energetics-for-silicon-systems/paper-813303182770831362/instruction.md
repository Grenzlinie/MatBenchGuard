# CCSD(T)//MP2/6-31G** Energetics of Dominant Cycloaddition Channels for a Silicon System

## Problem background
The cycloaddition reaction between singlet silylene silylene (H2Si=Si:) and acetaldehyde can proceed via multiple possible pathways, and the distribution of products depends sensitively on the relative energies of intermediates and transition states. Understanding the detailed energetics of this reaction and identifying the kinetically most favorable reaction channels is essential for predicting the outcome of silicon-based cycloadditions and for guiding experimental synthesis.

## Approach
The potential energy surface (PES) is explored using ab initio quantum chemistry methods at the CCSD(T)//MP2/6-31G** level. The workflow consists of two computational stages: first, geometry optimizations and harmonic vibrational frequency calculations at the MP2/6-31G** level are performed for all relevant stationary points (reactants, intermediates, transition states, products) to characterize minima and transition states and to obtain zero-point vibrational corrections. Second, single-point energy calculations at the coupled-cluster CCSD(T) level with the same 6-31G** basis set are carried out on the MP2-optimized geometries, and the total energy for each species is obtained by adding the zero-point correction. The resulting total energies are then used to construct a relative energy profile, from which the energy barriers and exothermicities of the possible reaction channels are derived. By comparing the relative energetics, the dominant, competitive reaction pathways can be identified.

## Reproduction target
Reproduce the CCSD(T)//MP2/6-31G** total energies (with zero-point correction) for the set of stationary points involved in the three dominant reaction channels for the cycloaddition between H2Si=Si: and acetaldehyde, as listed in the workflow steps. From these energies, compute relative energies (in kJ/mol) with the reference states specified, and determine the energy barriers and exothermicities (first step) for each of the three channels. The target is to obtain energies consistent with the computational methodology; the resulting relative barriers and exothermicities should reflect the correct ordering and magnitudes expected from this level of theory.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/app.php/portal

## Workflow steps

### Step 1: MP2/6-31G** Geometry Optimization and Vibrational Analysis
- Role: process
- Action: For each of the following stationary points: H2Si=Si: (R1), acetaldehyde (R2), INT2, TS2, P2, INT3, TS3, P3, INT4, TS4, P4, INT5, TS5, P5, perform full geometry optimization and harmonic vibrational frequency calculation at the MP2/6-31G** level. Characterize each stationary point as a minimum (all real frequencies) or a transition state (exactly one imaginary frequency) and retain the zero-point vibrational energy correction.
- Evidence: `/app/outputs/orca_opt_freq.log`

### Step 2: CCSD(T)//MP2/6-31G** Single-Point Energy and Zero-Point Correction
- Role: process
- Action: Using the MP2/6-31G** optimized geometries from step_01, perform a CCSD(T) single-point energy calculation with the 6-31G** basis set for each species. Add the zero-point energy correction obtained in step_01 to obtain the total energy E_T (in Hartree) for each species.
- Evidence: `/app/outputs/ccsdt_sp.log`

### Step 3: Compile Total and Relative Energies
- Role: scored (load-bearing)
- Action: Combine the CCSD(T)//MP2/6-31G** total energies (E_T) from step_02 into a single table. For each species compute its relative energy E_R (kJ/mol) with respect to the appropriate reference: R1+R2 for all species except those involved in the later stages of Reaction(3) (where the reference is P2+R2) and Reaction(5) (where the reference is INT4+R2). Output a CSV file `step_01_total_energies.csv`.
- Output file: `/app/outputs/step_01_total_energies.csv`
- Format: csv
- Contract: columns: species (string), total_energy_hartree (float), relative_energy_kJmol (float), reference (string)
- Scoring: scored by hidden verifier

### Step 4: Extract Dominant Channel Barriers and Exothermicities
- Role: scored
- Action: From the relative energies in step_01_total_energies.csv, identify the three competitive dominant reaction channels. For each channel, compute the key energy barrier (kJ/mol) and the exothermicity of the initial formation step (kJ/mol). Output a JSON file `step_02_dominant_barriers.json`.
- Output file: `/app/outputs/step_02_dominant_barriers.json`
- Format: json
- Contract: array of objects with keys: channel (string), barrier_kJmol (float), exothermicity_kJmol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_total_energies.csv`
- `/app/outputs/step_02_dominant_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_total_energies.csv
- path: `/app/outputs/step_01_total_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total CCSD(T)//MP2/6-31G** energies with zero-point correction, relative energies, and reference state for all relevant species.
- schema:
  - `type`: table
  - `required_columns`: `species`, `total_energy_hartree`, `relative_energy_kJmol`, `reference`
  - `units`:
    - `total_energy_hartree`: Hartree
    - `relative_energy_kJmol`: kJ/mol

### step_02_dominant_barriers.json
- path: `/app/outputs/step_02_dominant_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Barriers and exothermicities for the three dominant reaction channels derived from the relative energies.
- schema:
  - `type`: array
  - `items`:
    - `channel`: string
    - `barrier_kJmol`: float
    - `exothermicity_kJmol`: float
  - `units`:
    - `barrier_kJmol`: kJ/mol
    - `exothermicity_kJmol`: kJ/mol

Notes: The checker recomputes relative energies and derived barriers/exothermicities from the total energies CSV, then compares the barrier/exothermicity values in the JSON to paper-reported hidden values within a tolerance. The CSV structure is audited for completeness and plausible units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "total_energy_hartree",
          "relative_energy_kJmol",
          "reference"
        ],
        "units": {
          "total_energy_hartree": "Hartree",
          "relative_energy_kJmol": "kJ/mol"
        }
      },
      "description": "Total CCSD(T)//MP2/6-31G** energies with zero-point correction, relative energies, and reference state for all relevant species."
    },
    {
      "file": "step_02_dominant_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "channel": "string",
          "barrier_kJmol": "float",
          "exothermicity_kJmol": "float"
        },
        "units": {
          "barrier_kJmol": "kJ/mol",
          "exothermicity_kJmol": "kJ/mol"
        }
      },
      "description": "Barriers and exothermicities for the three dominant reaction channels derived from the relative energies."
    }
  ],
  "notes": "The checker recomputes relative energies and derived barriers/exothermicities from the total energies CSV, then compares the barrier/exothermicity values in the JSON to paper-reported hidden values within a tolerance. The CSV structure is audited for completeness and plausible units."
}
```

## How you are scored
A hidden verifier evaluates your submitted artifacts. For `step_01_total_energies.csv`, the verifier checks the file format, column structure, and units, then recomputes relative energies from the reported total energies and verifies consistency. For `step_02_dominant_barriers.json`, the verifier extracts the reported barriers and exothermicities and compares them to a set of reference values obtained from the same computational protocol, within appropriate tolerances. The verifier also checks that the channel identifiers match the expected three dominant channels. Each artifact receives a weighted score, and the final reward is the combined score. To maximise your score, you must execute the full computational pipeline and produce each output artifact as specified; simply guessing the final values is unlikely to yield correct results because the verifier checks for numerical consistency with the intermediate total energies.
