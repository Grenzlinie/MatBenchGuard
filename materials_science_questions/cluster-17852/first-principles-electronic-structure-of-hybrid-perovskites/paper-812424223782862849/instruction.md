# DFT Bandgap Tuning of CsPbBrI₂ Perovskite under Uniaxial Strain

## Problem background
Metal halide perovskite quantum dots are promising for tunable optoelectronic applications because their bandgap and emission can be modified by external stimuli. In particular, mechanical deformation of the crystal lattice—strain engineering—can reversibly alter the electronic structure. This task investigates how uniaxial compressive strain along the crystallographic c‑axis of the mixed‑halide perovskite CsPbBrI₂ affects its electronic bandgap, the stress generated in the material, and the lengths of the Pb–halide bonds, as studied by first‑principles DFT calculations.

## Approach
You will use density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and appropriate pseudopotentials to model a periodic CsPbBrI₂ unit cell. First construct the unit cell from known perovskite lattice parameters. Then, for a series of c‑axis lattice constants representing uniaxial compressive strains (up to a few percent), determine the equilibrium in‑plane lattice constants by fitting the Murnaghan equation of state to total energy vs. volume data. With the relaxed lateral dimensions for each strain, perform static DFT calculations to obtain the total energy and the Kohn–Sham band gap. Derive the compressive stress from the energy‑volume relation. Finally, analyze the optimized structures to extract the average Pb–I and Pb–Br bond lengths at the unstrained condition and at a chosen compressive strain.

## Reproduction target
Compute and write two artifacts:

1. A CSV file `bandgap_stress_vs_strain.csv` reporting the Kohn–Sham band gap (in eV) and the compressive stress (in GPa) for a series of c‑axis compressive strains, including the unstrained case and a strain of −1.34%.
2. A JSON file `bond_lengths.json` containing the average Pb–I and Pb–Br bond lengths (in Å) for the equilibrium (0% strain) structure and for the structure under −1.34% compressive strain.

## Assets

- Quantum ESPRESSO: quantum-espresso
- PBE pseudopotentials (PAW/USPP): http://www.quantum-espresso.org/pseudopotentials
- Materials Project crystal structures: https://materialsproject.org/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Prepare CsPbBrI₂ crystal structure and DFT inputs
- Role: process
- Action: Construct the CsPbBrI₂ perovskite unit cell using standard perovskite lattice parameters (from public databases such as Materials Project) and prepare Quantum ESPRESSO input files for pw.x calculations with PBE pseudopotentials.
- Evidence: none

### Step 2: Murnaghan EOS fitting for equilibrium in-plane lattice constants
- Role: process
- Action: For a set of c-axis lattice constants covering a compressive strain range from 0% to about -2%, run DFT total energy calculations at several volumes, fit the Murnaghan equation of state to determine the equilibrium in-plane lattice constants a and b for each c, and derive the Poisson ratio.
- Evidence: none

### Step 3: Compute band gap and stress under uniaxial strain
- Role: scored (load-bearing)
- Action: Using the equilibrium in-plane lattice constants from step2 for each desired c-axis strain (including a compressive strain of -1.34% and the unstrained case), run static DFT calculations to obtain the total energy and the Kohn-Sham band gap. From the total energy vs. volume data, derive the compressive stress. Write the results into a CSV file with columns: strain, bandgap_ev, stress_gpa.
- Output file: `/app/outputs/bandgap_stress_vs_strain.csv`
- Format: csv
- Contract: CSV with columns: strain (float, dimensionless fraction), bandgap_ev (float, in eV), stress_gpa (float, in GPa; can be empty for strains where stress was not derived).
- Scoring: scored by hidden verifier

### Step 4: Extract bond lengths at equilibrium and under strain
- Role: scored
- Action: From the optimized DFT structures at equilibrium (0% strain) and at 1.34% compressive strain (obtained from the runs in step3), compute the average per-cell Pb–I and Pb–Br bond lengths. Output a JSON file with keys 'equilibrium' and 'strained_1.34', each containing 'pb_i_A' and 'pb_br_A'.
- Output file: `/app/outputs/bond_lengths.json`
- Format: json
- Contract: JSON object with keys 'equilibrium' and 'strained_1.34'. Each value is an object with keys 'pb_i_A' (float, average Pb–I bond length in Å) and 'pb_br_A' (float, average Pb–Br bond length in Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap_stress_vs_strain.csv`
- `/app/outputs/bond_lengths.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap_stress_vs_strain.csv
- path: `/app/outputs/bandgap_stress_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file reporting the Kohn-Sham band gap (eV) and compressive stress (GPa) for a series of c-axis compressive strain values.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `bandgap_ev`, `stress_gpa`
  - `units`:
    - `strain`: dimensionless (fraction)
    - `bandgap_ev`: eV
    - `stress_gpa`: GPa

### bond_lengths.json
- path: `/app/outputs/bond_lengths.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file reporting the average Pb-I and Pb-Br bond lengths at equilibrium and under 1.34% c-axis compressive strain.
- schema:
  - `type`: object
  - `required`:
    - `equilibrium`:
      - `type`: object
      - `fields`:
        - `pb_i_A`: float (average Pb-I bond length in Å)
        - `pb_br_A`: float (average Pb-Br bond length in Å)
    - `strained_1.34`:
      - `type`: object
      - `fields`:
        - `pb_i_A`: float (average Pb-I bond length in Å)
        - `pb_br_A`: float (average Pb-Br bond length in Å)

Notes: T0 result-level comparison: the hidden checker compares the agent's computed bandgap, stress, and bond-length values to the paper's reference values with tolerances, and verifies the monotonic bandgap-vs-strain trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap_stress_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "bandgap_ev",
          "stress_gpa"
        ],
        "units": {
          "strain": "dimensionless (fraction)",
          "bandgap_ev": "eV",
          "stress_gpa": "GPa"
        }
      },
      "description": "CSV file reporting the Kohn-Sham band gap (eV) and compressive stress (GPa) for a series of c-axis compressive strain values."
    },
    {
      "file": "bond_lengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "equilibrium": {
            "type": "object",
            "fields": {
              "pb_i_A": "float (average Pb-I bond length in Å)",
              "pb_br_A": "float (average Pb-Br bond length in Å)"
            }
          },
          "strained_1.34": {
            "type": "object",
            "fields": {
              "pb_i_A": "float (average Pb-I bond length in Å)",
              "pb_br_A": "float (average Pb-Br bond length in Å)"
            }
          }
        }
      },
      "description": "JSON file reporting the average Pb-I and Pb-Br bond lengths at equilibrium and under 1.34% c-axis compressive strain."
    }
  ],
  "notes": "T0 result-level comparison: the hidden checker compares the agent's computed bandgap, stress, and bond-length values to the paper's reference values with tolerances, and verifies the monotonic bandgap-vs-strain trend."
}
```

## How you are scored
A hidden verifier evaluates your two output files. It inspects the CSV for a monotonic trend of bandgap with strain, and compares the bandgap shift, stress, and bond‑length changes at the specific strains against reference values derived from the underlying study. The JSON file is checked for the correctness of the reported bond lengths. The verifier combines these assessments into a final reward score between 0 and 1. Simply writing expected numerical values is not sufficient; the verifier scores the actual computed quantities, and deviations beyond the allowed tolerances will reduce the reward.
