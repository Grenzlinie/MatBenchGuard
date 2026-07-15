# DFT Energetics and Lattice Parameters of (CF)n and Graphane Monolayer Conformations

## Problem background
Carbon monofluoride (CF)n and graphane are two-dimensional polycyclic materials formed by fully covering a graphene sheet with fluorine or hydrogen adatoms. The atomic-scale structure can adopt several conformations that differ in how the adatoms alternate across the carbon layer. The chair and bed conformations have been studied previously, but a third arrangement—the washboard (gauche-chair) conformation, where adatoms form zigzag rows on each side—has received less attention. Its thermodynamic stability relative to the other conformations and its equilibrium in-plane lattice parameters in isolated monolayers are not fully established. Clarifying these properties is important for understanding experimental observations that indicate lattice constants smaller than those predicted by simple periodic models.

## Approach
Use density functional theory (DFT) with the PBE functional and a plane-wave basis. Construct atomic models for the chair, washboard, and bed monolayer conformations of both (CF)n and graphane by placing atoms in the appropriate alternation patterns. For each of the six structures, set up a periodic calculation that includes a vacuum layer to eliminate interlayer interactions, then perform a full variable-cell relaxation to simultaneously optimize atomic positions and the in-plane cell dimensions. Compute the total energy per formula unit. From the relaxed energies, derive the relative energy of each conformation with respect to the chair conformation, and extract the optimized in-plane lattice constants a and b. The workflow employs Quantum ESPRESSO (pw.x) and the publicly available PBE ultrasoft pseudopotentials for C, F, and H.

## Reproduction target
Produce a single JSON file, `/app/outputs/monolayer_results.json`, that contains the relative energies (E_rel, in eV per formula unit) and the in-plane lattice parameters a and b (in Å) for all six monolayer systems: CF-chair (CF_C), CF-washboard (CF_W), CF-bed (CF_B), CH-chair (CH_C), CH-washboard (CH_W), and CH-bed (CH_B). Each entry must be an object with the three fields `E_rel`, `a`, and `b`. The values must be obtained from the DFT variable-cell relaxations described above; reporting known literature numbers is insufficient.

## Assets

- Quantum-ESPRESSO: https://www.quantum-espresso.org/
- PBE ultrasoft pseudopotentials (C, F, H): https://pseudopotentials.quantum-espresso.org/legacy_tables/

## Workflow steps

### Step 1: DFT monolayer calculations
- Role: scored (load-bearing)
- Action: Construct atomic models for the chair, washboard, and bed monolayer conformations of (CF)n and graphane (six structures total). For each, set up a PWSCF calculation using the PBE functional with ultrasoft pseudopotentials, a plane-wave kinetic-energy cutoff and k-point grid dense enough to converge total energies, and a vacuum spacing to eliminate interlayer interaction. Perform a variable-cell relaxation to optimize atomic positions and in-plane lattice parameters. Compute the total energy per formula unit. Derive the relative energy (E − E_chair) for each conformation of each material. Extract the optimized in-plane lattice parameters a and b. Write all results to /app/outputs/monolayer_results.json.
- Output file: `/app/outputs/monolayer_results.json`
- Format: json
- Contract: {"CF_C": {"E_rel": "number (eV)", "a": "number (Å)", "b": "number (Å)"},"CF_W": {...},"CF_B": {...},"CH_C": {...},"CH_W": {...},"CH_B": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monolayer_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monolayer_results.json
- path: `/app/outputs/monolayer_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies (eV per formula unit) and in-plane lattice parameters (a and b in Å) for the chair, washboard, and bed conformations of both (CF)n and graphane monolayers, obtained from DFT variable-cell relaxations.
- schema:
  - `type`: object
  - `required`:
    - `CF_C`: object containing {E_rel: number (eV), a: number (Å), b: number (Å)}
    - `CF_W`: object containing {E_rel: number (eV), a: number (Å), b: number (Å)}
    - `CF_B`: object containing {E_rel: number (eV), a: number (Å), b: number (Å)}
    - `CH_C`: object containing {E_rel: number (eV), a: number (Å), b: number (Å)}
    - `CH_W`: object containing {E_rel: number (eV), a: number (Å), b: number (Å)}
    - `CH_B`: object containing {E_rel: number (eV), a: number (Å), b: number (Å)}
  - `units`:
    - `E_rel`: eV
    - `a`: Å
    - `b`: Å

Notes: The hidden checker compares each submitted E_rel and lattice constant to the paper-reported gold with tolerances (E_rel ±0.005 eV or 10% relative, a,b ±0.01 Å), weighting energies 0.6 and lattice parameters 0.4. Only this monolayer DFT stage is required; all other stages from the paper (force field fitting, vdW-DF 3D stacking, MD simulations, quasirandom model) are omitted per taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monolayer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CF_C": "object containing {E_rel: number (eV), a: number (Å), b: number (Å)}",
          "CF_W": "object containing {E_rel: number (eV), a: number (Å), b: number (Å)}",
          "CF_B": "object containing {E_rel: number (eV), a: number (Å), b: number (Å)}",
          "CH_C": "object containing {E_rel: number (eV), a: number (Å), b: number (Å)}",
          "CH_W": "object containing {E_rel: number (eV), a: number (Å), b: number (Å)}",
          "CH_B": "object containing {E_rel: number (eV), a: number (Å), b: number (Å)}"
        },
        "units": {
          "E_rel": "eV",
          "a": "Å",
          "b": "Å"
        }
      },
      "description": "Relative energies (eV per formula unit) and in-plane lattice parameters (a and b in Å) for the chair, washboard, and bed conformations of both (CF)n and graphane monolayers, obtained from DFT variable-cell relaxations."
    }
  ],
  "notes": "The hidden checker compares each submitted E_rel and lattice constant to the paper-reported gold with tolerances (E_rel ±0.005 eV or 10% relative, a,b ±0.01 Å), weighting energies 0.6 and lattice parameters 0.4. Only this monolayer DFT stage is required; all other stages from the paper (force field fitting, vdW-DF 3D stacking, MD simulations, quasirandom model) are omitted per taskability scope."
}
```

## How you are scored
A hidden verifier reads your JSON file and compares each submitted value against a reference set derived from published DFT results. The check evaluates both absolute accuracy of the energies and lattice constants, and the correct ordering of the three conformations for each material (chair, washboard, bed). The accuracy of the relative energies contributes more to your final score than the accuracy of the lattice parameters. The verifier produces a single numeric reward between 0 and 1; reporting a number does not automatically earn credit—the values themselves are verified.
