# BiFeO3 Low-Energy Phase Relative Energies via DFT

## Problem background
Multiferroic BiFeO3 is a perovskite oxide whose complex structural energy landscape is of great scientific interest. First‑principles density functional theory (DFT) calculations can explore competing low‑energy crystal phases and quantify their relative stabilities. This task focuses on computing the relative energies of several candidate crystal structures of BiFeO3 with respect to a common reference phase (the R3c‑G ground state). The result – a set of energy differences in meV per formula unit – probes whether a variety of distinct structural minima exist within a narrow energy window above the ground state.

## Approach
A plane‑wave DFT method based on the PBE+U exchange‑correlation functional is employed. A Hubbard U = 4 eV is applied to the Fe 3d electrons to improve the description of the correlated states. All calculations use an open‑source DFT code and standard projector‑augmented‑wave (PAW) pseudopotentials. For each of the six phases, an initial crystal structure (lattice vectors and fractional atomic coordinates) is provided in `initial_structures.json`. The approach consists of performing a full structural relaxation (variable‑cell relaxation) for each phase, allowing both atomic positions and cell parameters to adjust until the forces and stress converge. The converged total energy per formula unit (5 atoms) is extracted. The relative stability is then obtained as ΔE = E(phase) − E(R3c‑G), expressed in meV/f.u. The R3c‑G phase serves as the zero reference. Only the final ΔE values are required; the relaxation procedure itself must be carried out for each phase to produce a physically meaningful result.

## Reproduction target
Produce a single JSON file `relative_energies.json` saved under `/app/outputs`. This file must contain an object whose keys are exactly the following phase labels: `"R3c-G"`, `"Pnma-G"`, `"Pna2_1-G"`, `"Cc-C"`, `"Cm-C"`, and `"Pc-C"`. Each value must be a numeric scalar representing ΔE in meV per formula unit (the value for `"R3c-G"` must be exactly 0). The goal is to obtain these numbers by performing the full DFT relaxations described in the Approach. Report only the final, converged energy differences; no intermediate files are required.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP PAW pseudopotentials (PBE efficiency): https://www.materialscloud.org/discover/sssp/init
- Initial crystal structures of the six phases

## Workflow steps

### Step 1: PBE+U structural relaxations and energy differences
- Role: scored
- Action: For each BiFeO3 phase listed in initial_structures.json, create a Quantum ESPRESSO input file with the PBE+U functional (U=4 eV on Fe d states, plane-wave cutoff 500 eV, k-point grid scaled from a 2×2×2 mesh for the 40-atom cell to the primitive cell). Perform a full variable-cell relaxation (atomic positions and lattice parameters). After convergence, extract the total energy per formula unit (5 atoms) and compute ΔE = E(phase) − E(R3c‑G) in meV/f.u. Write a single JSON file relative_energies.json with keys exactly: R3c-G, Pnma-G, Pna2_1-G, Cc-C, Cm-C, Pc-C, and values as the numeric ΔE; ensure E(R3c‑G) is exactly 0.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: JSON object with keys 'R3c-G', 'Pnma-G', 'Pna2_1-G', 'Cc-C', 'Cm-C', 'Pc-C'; each value is a number (float) representing ΔE in meV/f.u. (the value for 'R3c-G' must be exactly 0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies (ΔE = E(phase) − E(R3c‑G)) for six BiFeO3 phases computed by PBE+U DFT relaxation. Each key contains a numeric value in meV/f.u.; R3c‑G must be exactly 0.
- schema:
  - `type`: object
  - `required`:
    - `R3c-G`: number
    - `Pnma-G`: number
    - `Pna2_1-G`: number
    - `Cc-C`: number
    - `Cm-C`: number
    - `Pc-C`: number
  - `units`: meV/f.u.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "R3c-G": "number",
          "Pnma-G": "number",
          "Pna2_1-G": "number",
          "Cc-C": "number",
          "Cm-C": "number",
          "Pc-C": "number"
        },
        "units": "meV/f.u."
      },
      "description": "Relative energies (ΔE = E(phase) − E(R3c‑G)) for six BiFeO3 phases computed by PBE+U DFT relaxation. Each key contains a numeric value in meV/f.u.; R3c‑G must be exactly 0."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `relative_energies.json` and compares the submitted ΔE values against a secret reference. Your score depends on two criteria: (i) the numerical agreement of each ΔE with the reference (within an undisclosed tolerance that accounts for legitimate numerical differences between DFT implementations), and (ii) the correct ordering of the ΔE values among the phases (i.e., which phases are more or less stable). The R3c‑G entry must be exactly 0. The verifier only checks your final output file; it does not inspect intermediate calculations. To succeed you must genuinely run the relaxations – a reasonable DFT calculation will reproduce the correct physical trends and magnitudes.
