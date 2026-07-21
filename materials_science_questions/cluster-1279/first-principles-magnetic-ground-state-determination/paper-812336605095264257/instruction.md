# First-principles magnetic ground state of face-centered tetragonal Fe

## Problem background
Iron films grown on Rh(001) experience a large lattice mismatch, which induces a face-centered tetragonal (fct) structure. The magnetic properties of these films depend on the lattice constant and are central to understanding the observed magnetic dead layers. This task determines the magnetic ground state by computing total energies for non‑magnetic (NM), antiferromagnetic (AF), and ferromagnetic (FM) orderings of fct Fe at the in‑plane lattice constant of Rh(001) (a = b = 3.84 Å).

## Approach
Use an all‑electron density functional theory (DFT) code (e.g., Elk, FLEUR, or WIEN2k) to perform spin‑polarized total‑energy calculations. A four‑atom fct unit cell is used with fixed in‑plane lattice constants a = b = 3.84 Å. For each of the three magnetic configurations — NM, AF, and FM — optimize the out‑of‑plane lattice constant c (or the c/a ratio) to locate the total‑energy minimum. Compare the optimized total energies per atom to identify the most stable magnetic phase and quantify the energy differences among the phases.

### Magnetic-phase definitions
The four‑atom fct unit cell contains atoms at the base‑centered‑tetragonal positions: (0,0,0), (0.5,0.5,0), (0,0.5,0.5), (0.5,0,0.5) in fractional coordinates. The magnetic configurations are:
- **Nonmagnetic (NM):** Spin‑unpolarized calculation; no spin‑orbit coupling.
- **Ferromagnetic (FM):** All four atoms carry parallel magnetic moments.
- **Antiferromagnetic (AF):** The two atoms in the first basal layer (z = 0) have opposite spin to the two atoms in the second basal layer (z = 0.5c). For example, set (0,0,0) and (0.5,0.5,0) spin‑up, (0,0.5,0.5) and (0.5,0,0.5) spin‑down, so the net magnetic moment of the cell is zero.

### Exchange‑correlation functional
Use the generalized gradient approximation (GGA) for exchange‑correlation, as adopted in the paper (e.g., PBE or PW91). Other functionals (e.g., LDA) are not acceptable; the check tolerances assume GGA results.

## Reproduction target
Run the DFT calculations for the three magnetic phases of fct Fe as described. From the converged results, extract the equilibrium total energy per atom (in mRy) for each phase. Set the FM energy as the zero reference and compute the energy differences `AF_minus_FM_mRy` and `NM_minus_FM_mRy` in mRy/atom. Determine which phase is the ground state and write everything to the output file `results.json` as specified in the workflow steps.

**Expected physical ordering:** According to the paper, the AF total energy is lower than the NM total energy; therefore `AF_minus_FM_mRy` should be smaller than `NM_minus_FM_mRy`. The hidden verifier checks that both differences are positive (indicating FM is the ground state) **and** that `AF_minus_FM_mRy < NM_minus_FM_mRy`. Make sure your calculations reproduce this ordering.

## Assets

- All-electron FP-LAPW DFT code (Elk / FLEUR / WIEN2k): https://elk.sourceforge.io/ (Elk), https://www.flapw.de/ (FLEUR), https://www.wien2k.at/ (WIEN2k)

## Workflow steps

### Step 1: Run DFT total energy calculations for fct Fe NM, AF, FM phases
- Role: process
- Action: Use an all-electron DFT code (e.g., Elk, FLEUR, WIEN2k) to perform spin‑polarized total‑energy calculations for face‑centered tetragonal (fct) Fe with in‑plane lattice constants a = b = 3.84 Å. Use GGA for exchange‑correlation. For each of the three magnetic configurations — nonmagnetic (NM, spin‑unpolarized), antiferromagnetic (AF, alternating layer spins as defined above), and ferromagnetic (FM, all spins parallel) — optimize the out‑of‑plane lattice constant c (or scan c/a ratio) to find the total‑energy minimum. Use a sufficiently dense k‑point mesh and tight convergence criteria.
- Evidence: DFT calculation logs are generated during the run; only the final `results.json` is required for scoring.

### Step 2: Extract and report total energy differences
- Role: scored (load-bearing)
- Action: From the DFT output, extract the total energy per atom (in mRy) for the equilibrium geometry of each magnetic phase. Set the FM energy as the reference (0.000 mRy/atom) and compute the energy differences `AF_minus_FM_mRy` and `NM_minus_FM_mRy`. Write a JSON file with the per‑phase energies and the differences.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: `FM` (object with `energy_per_atom_mRy` (float)), `AF` (object with `energy_per_atom_mRy` (float)), `NM` (object with `energy_per_atom_mRy` (float)), and `energy_differences` (object with `AF_minus_FM_mRy` (float) and `NM_minus_FM_mRy` (float)). All values in mRy/atom.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energies per atom for NM, AF, and FM phases of fct Fe at a=b=3.84 Å after c optimization, and the energy differences relative to the FM ground state.
- schema:
  - `type`: object
  - `required`:
    - `FM`: object containing 'energy_per_atom_mRy' (float)
    - `AF`: object containing 'energy_per_atom_mRy' (float)
    - `NM`: object containing 'energy_per_atom_mRy' (float)
    - `energy_differences`: object containing 'AF_minus_FM_mRy' (float) and 'NM_minus_FM_mRy' (float)
  - `items`: object
  - `units`:
    - `FM.energy_per_atom_mRy`: mRy/atom
    - `AF.energy_per_atom_mRy`: mRy/atom
    - `NM.energy_per_atom_mRy`: mRy/atom
    - `energy_differences.AF_minus_FM_mRy`: mRy/atom
    - `energy_differences.NM_minus_FM_mRy`: mRy/atom

Notes: The scored output reports relative energies consistent with the paper's Table 1. The checker will verify that FM is the lowest energy (both AF and NM differences are positive) and that `AF_minus_FM_mRy` is less than `NM_minus_FM_mRy`, then compare the reported differences to hidden reference values within a tolerance that accounts for DFT implementation variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "FM": "object containing 'energy_per_atom_mRy' (float)",
          "AF": "object containing 'energy_per_atom_mRy' (float)",
          "NM": "object containing 'energy_per_atom_mRy' (float)",
          "energy_differences": "object containing 'AF_minus_FM_mRy' (float) and 'NM_minus_FM_mRy' (float)"
        },
        "items": {},
        "units": {
          "FM.energy_per_atom_mRy": "mRy/atom",
          "AF.energy_per_atom_mRy": "mRy/atom",
          "NM.energy_per_atom_mRy": "mRy/atom",
          "energy_differences.AF_minus_FM_mRy": "mRy/atom",
          "energy_differences.NM_minus_FM_mRy": "mRy/atom"
        }
      },
      "description": "Total energies per atom for NM, AF, and FM phases of fct Fe at a=b=3.84 Å after c optimization, and the energy differences relative to the FM ground state."
    }
  ],
  "notes": "The scored output reports relative energies consistent with the paper's Table 1. The checker will verify that FM is the lowest energy and compare the reported differences to hidden reference values within a tolerance that accounts for DFT implementation variations."
}
```

## How you are scored
A hidden verifier reads your `results.json`. It checks that FM is the ground state (both AF and NM energy differences are positive and AF < NM) and compares your reported energy differences against a hidden reference. The final reward is a weighted combination of these checks, producing a score between 0 and 1. Only an honest execution of the DFT workflow — not guessing or fabricating numbers — can yield results that pass the verifier.