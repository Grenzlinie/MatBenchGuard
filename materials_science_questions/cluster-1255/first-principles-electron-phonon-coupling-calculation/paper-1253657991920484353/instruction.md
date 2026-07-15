# DFT calculation of Fermi surface pocket energies in HCP cadmium

## Problem background
Electron hydrodynamic flow in cadmium has been attributed to momentum-conserving electron-electron collisions that occur at a rate set by small energy scales on the Fermi surface. First-principles electronic structure calculations identify several distinct pockets (lens, monster, cap, petty-1, petty-2, and a particularly tiny 'lilliputian' pocket) that create inter-valley bottlenecks. The Fermi energies of these pockets relative to the Fermi level are the key quantities that determine the phase space for momentum-conserving collisions. Reproducing these energy scales by an independent density-functional calculation provides a quantitative test of this picture.

## Approach
Use density functional theory (DFT) with the local density approximation (LDA) for exchange and correlation, including spin-orbit coupling, to compute the electronic structure of hexagonal close-packed (HCP) cadmium. Start from the experimental crystal structure (lattice parameters a=2.979 Å, c=5.618 Å). Perform a self-consistent field calculation to obtain the charge density, then compute the band structure on a dense k-point grid. From the resulting band structure, identify the Fermi energies (i.e., the difference between the Fermi level and the band extremum) of the six pockets defined by their location in the Brillouin zone: the electron-like lens at Γ, the hole-like monster and cap near H, the small petty-1 and petty-2 pockets near K, and the tiny lilliputian pocket along K-M.

## Reproduction target
Compute the Fermi energies (in eV relative to the Fermi level) for the six electronic pockets of HCP cadmium: lens, monster, cap, petty-1, petty-2, and lilliputian. Use density functional theory with the LDA functional and spin-orbit coupling as implemented in an open-source code (Quantum ESPRESSO). Report the results as a JSON file.

## Assets

- HCP cadmium crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials for Cd: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT calculation of HCP Cd Fermi energies
- Role: scored (load-bearing)
- Action: Set up and run a DFT calculation for hexagonal close-packed (HCP) cadmium using Quantum ESPRESSO with local density approximation (LDA) and spin-orbit coupling. Use the experimental lattice parameters a=2.979 Å, c=5.618 Å. Perform a self-consistent field (SCF) calculation to obtain the charge density, then carry out a non-self-consistent calculation on a dense k-point grid to compute the band structure. Identify the Fermi energies (in eV relative to the Fermi level) for the following six pockets: lens (electron pocket at Γ), monster (hole pocket at H), cap (hole pocket at H), petty-1 (near K), petty-2 (near K), and lilliputian (along K-M). Report these energies in a JSON file.
- Output file: `/app/outputs/fermi_energies.json`
- Format: json
- Contract: {"lens": float, "monster": float, "cap": float, "petty-1": float, "petty-2": float, "lilliputian": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fermi_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fermi_energies.json
- path: `/app/outputs/fermi_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Fermi energies (in eV) relative to the Fermi level for the six pockets defined in the paper's electronic structure analysis. The checker compares each value to the hidden paper-reported value with an appropriate tolerance.
- schema:
  - `type`: object
  - `required`: `lens`, `monster`, `cap`, `petty-1`, `petty-2`, `lilliputian`
  - `items`:
    - `lens`: float (eV)
    - `monster`: float (eV)
    - `cap`: float (eV)
    - `petty-1`: float (eV)
    - `petty-2`: float (eV)
    - `lilliputian`: float (eV)

Notes: The Fermi energies are method-dependent; tolerances are chosen to accommodate typical DFT code/pseudopotential differences while requiring a faithful calculation. The agent's installation of Quantum ESPRESSO and choice of pseudopotential are free but must support spin-orbit coupling.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fermi_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lens",
          "monster",
          "cap",
          "petty-1",
          "petty-2",
          "lilliputian"
        ],
        "items": {
          "lens": "float (eV)",
          "monster": "float (eV)",
          "cap": "float (eV)",
          "petty-1": "float (eV)",
          "petty-2": "float (eV)",
          "lilliputian": "float (eV)"
        }
      },
      "description": "Computed Fermi energies (in eV) relative to the Fermi level for the six pockets defined in the paper's electronic structure analysis. The checker compares each value to the hidden paper-reported value with an appropriate tolerance."
    }
  ],
  "notes": "The Fermi energies are method-dependent; tolerances are chosen to accommodate typical DFT code/pseudopotential differences while requiring a faithful calculation. The agent's installation of Quantum ESPRESSO and choice of pseudopotential are free but must support spin-orbit coupling."
}
```

## How you are scored
A hidden verifier reads your submitted `fermi_energies.json` and compares each pocket's Fermi energy to a hidden reference value. The comparison uses appropriate tolerances that account for legitimate differences between DFT codes and pseudopotentials. Each of the six pockets contributes equally to the final score. The verifier also validates that the JSON structure matches the contract. Simply reporting the paper's published numbers is not sufficient; the calculation must be performed as described.
