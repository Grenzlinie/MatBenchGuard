# Adhesion Energy of Substituted Benzenes on Carbon Nanopores from First Principles

## Problem background
Benzene and its substituted analogs are classified as hazardous air pollutants due to their high risk to public health and the environment. Porous carbon materials, such as graphitic slits and carbon nanotubes, are promising candidates for filtering these pollutants. The effectiveness of such filters depends on the adhesion energy between the pollutant molecules and the carbon nanopore. First-principles density functional theory (DFT) calculations provide a quantitative way to determine these adhesion energies and to assess how different chemical substituents (e.g., chloro, nitro, isopropyl) on the benzene ring influence adsorption selectivity.

## Approach
Use an open-source plane-wave DFT code supporting the GGA-PW91 exchange-correlation functional and ultrasoft pseudopotentials. Model two carbon nanopore systems: a graphitic slit formed by a single graphite sheet with periodic boundary conditions, and a (9,9) carbon nanotube. For each of four molecules — benzene, chlorobenzene, nitrobenzene, and isopropylbenzene — and for each substrate, perform geometry optimization (relaxing only the molecule while keeping the substrate fixed) followed by high-precision single-point energy calculations along the surface normal to locate the potential energy minimum. Extract the total energies of the combined molecule–substrate system, the isolated substrate, and the isolated molecule (in the same unit cell) to compute the adhesion energy as E_adhesion = E_combined − E_system − E_molecule.

## Reproduction target
Compute, using the above DFT protocol, the adhesion energy (in eV per molecule) for each of the four molecules in both the graphitic slit and the (9,9) carbon nanotube. Write the results, together with the constituent total energies (E_combined, E_system, E_molecule), to a CSV file named `adhesion_energies.csv` with the columns: `system`, `molecule`, `E_combined`, `E_system`, `E_molecule`, `E_adhesion`. The CSV must contain exactly eight rows, one per condition.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare atomic structures of substrates and molecules
- Role: process
- Action: Construct the unit cell of a graphitic slit (48 carbon atoms, cell dimensions 12.77 Å × 9.88 Å × 14.00 Å), the unit cell of a (9,9) carbon nanotube (144 carbon atoms, tube length 9.98 Å), and the initial geometries of benzene, chlorobenzene, nitrobenzene, and isopropylbenzene.
- Evidence: none

### Step 2: DFT geometry optimization of molecule–surface systems
- Role: process
- Action: For each molecule (benzene, chlorobenzene, nitrobenzene, isopropylbenzene) on each surface (graphitic slit and (9,9) CNT), perform a DFT geometry optimization using the GGA-PW91 exchange-correlation functional, ultrasoft pseudopotentials, and a single k-point. Keep the substrate atoms fixed and relax only the molecule positions.
- Evidence: none

### Step 3: High-precision single-point energy calculation with potential-surface verification
- Role: process
- Action: For each optimized molecule–substrate system, perform a series of single-point DFT energy calculations by stepping the molecule along the surface normal direction. Use a consistent, high plane-wave kinetic energy cutoff for all systems to obtain the total energies of the combined system (E_combined), the empty substrate (E_system), and the isolated molecule in the same unit cell (E_molecule).
- Evidence: none

### Step 4: Calculate and report adhesion energies
- Role: scored (load-bearing)
- Action: For each of the eight conditions (4 molecules × 2 substrates), compute the adhesion energy as E_adhesion = E_combined - E_system - E_molecule. Write all energies to a CSV file named 'adhesion_energies.csv' with columns: system, molecule, E_combined, E_system, E_molecule, E_adhesion.
- Output file: `/app/outputs/adhesion_energies.csv`
- Format: csv
- Contract: Columns: system (string: 'graphitic_slit' or 'cnt_9_9'), molecule (string: benzene, chlorobenzene, nitrobenzene, isopropylbenzene), E_combined (float, eV), E_system (float, eV), E_molecule (float, eV), E_adhesion (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adhesion_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adhesion_energies.csv
- path: `/app/outputs/adhesion_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Eight rows, one per condition. Columns: system (string: 'graphitic_slit' or 'cnt_9_9'), molecule (string: benzene, chlorobenzene, nitrobenzene, isopropylbenzene), E_combined (float, eV), E_system (float, eV), E_molecule (float, eV), E_adhesion (float, eV).
- schema:
  - `type`: table
  - `required_columns`: `system`, `molecule`, `E_combined`, `E_system`, `E_molecule`, `E_adhesion`
  - `units`:
    - `E_combined`: eV
    - `E_system`: eV
    - `E_molecule`: eV
    - `E_adhesion`: eV

Notes: The task requires plane-wave DFT calculations which are computationally intensive. The solving agent is expected to install an open-source DFT code (e.g., Quantum ESPRESSO) and retrieve appropriate pseudopotentials at runtime. Only the final scored CSV artifact is required to be placed under /app/outputs; intermediate DFT output files are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adhesion_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "molecule",
          "E_combined",
          "E_system",
          "E_molecule",
          "E_adhesion"
        ],
        "units": {
          "E_combined": "eV",
          "E_system": "eV",
          "E_molecule": "eV",
          "E_adhesion": "eV"
        }
      },
      "description": "Eight rows, one per condition. Columns: system (string: 'graphitic_slit' or 'cnt_9_9'), molecule (string: benzene, chlorobenzene, nitrobenzene, isopropylbenzene), E_combined (float, eV), E_system (float, eV), E_molecule (float, eV), E_adhesion (float, eV)."
    }
  ],
  "notes": "The task requires plane-wave DFT calculations which are computationally intensive. The solving agent is expected to install an open-source DFT code (e.g., Quantum ESPRESSO) and retrieve appropriate pseudopotentials at runtime. Only the final scored CSV artifact is required to be placed under /app/outputs; intermediate DFT output files are not required."
}
```

## How you are scored
A hidden verifier will read your `adhesion_energies.csv`. First, it will recompute `E_adhesion` from the provided `E_combined`, `E_system`, and `E_molecule` to confirm internal consistency. Then it will compare each of the eight adhesion energy values to a hidden set of reference values (derived from the original experimental study) using a pre-defined tolerance. Full credit is awarded if all eight values fall within the tolerance; partial credit may be given for partially correct sets. The verifier only checks the final output file; intermediate DFT outputs are not scored.
