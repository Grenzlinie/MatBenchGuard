# DFT adsorption energies of N and In adatoms on ZnO surfaces

## Problem background
The growth of high-quality InN thin films is sensitive to the substrate material and its surface termination (polarity). Unlike growth on GaN, where film quality strongly depends on whether the substrate is Ga-face or N-face, experiments on ZnO substrates suggest a weaker polarity dependence. Understanding the initial adsorption behavior of indium (In) and nitrogen (N) adatoms on ZnO surfaces can shed light on why the growth is less polarity-dependent. This task is to compute, using first-principles density functional theory (DFT), the relative stability of N and In adatoms on both Zn-face and O-face ZnO (0001) surfaces, providing insight into the early stages of InN growth.

## Approach
We will use plane-wave DFT with the open-source Quantum ESPRESSO package (pw.x). Construct stoichiometric, unreconstructed (1×1) surface supercells for both Zn-face and O-face ZnO using the known wurtzite lattice constants (a=3.25 Å, c=5.21 Å). Each supercell contains 8 double layers of ZnO plus a vacuum region. First, relax the atomic positions of the clean surfaces, keeping the bottom half of the slab fixed, to obtain reference structures. Then, for each of the four required combinations (N on Zn-face, N on O-face, In on Zn-face, In on O-face), place a single adatom at high-symmetry sites over the relaxed surface and perform energy calculations with adatom height relaxation. Identify the configuration giving the lowest total energy for each adatom/surface pair. The comparison of interest is the energy difference between N and In adatoms on the same surface polarity: ΔE = E(N) – E(In). Compute this separately for the Zn-face and for the O-face. Note: the original publication used VASP; here we replace it with Quantum ESPRESSO and appropriate pseudopotentials (e.g., from SSSP or PseudoDojo). Absolute total energies will differ, but the relative adsorption energetics are comparable and are the target.

## Reproduction target
Produce a single JSON file, `/app/outputs/adsorption_energies.json`, containing the minimum total energies (in eV) for each of the four adatom/surface configurations: N on Zn-face, N on O-face, In on Zn-face, In on O-face. These values should come from your DFT calculations after adatom relaxation, using the relaxed clean surface slabs constructed earlier. The JSON keys are: `N_Znface`, `N_Oface`, `In_Znface`, `In_Oface`. The objective is to compute these four energies accurately enough that the hidden verifier can derive the energy differences and assess the relative stability of N versus In adatoms on each surface polarity.

## Assets

- Wurtzite ZnO crystal structure
- Pseudopotentials for Zn, O, N, In: https://www.quantum-espresso.org/pseudopotentials
- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Relax clean ZnO surface slabs
- Role: process
- Action: Construct Zn-face and O-face ZnO (0001) surface supercell models using wurtzite lattice constants (a=3.25 Å, c=5.21 Å). Use a 1×1 in‑plane unit cell and 8 double layers of ZnO plus vacuum. Relax atomic positions using DFT (Quantum ESPRESSO) until forces converge, keeping the bottom half of the slab fixed. Separate relaxations for Zn-face and O-face terminations. This step provides the clean surface reference for adatom adsorption.
- Evidence: none

### Step 2: Compute minimum adsorption energies
- Role: scored (load-bearing)
- Action: For each combination (N on Zn‑face, N on O‑face, In on Zn‑face, In on O‑face), place the adatom at high‑symmetry sites over the relaxed surfaces from step01. Perform DFT total energy calculations with adatom height relaxation, locate the minimum total energy configuration, and record that minimum total energy in eV. Save all four minimum total energies to the output file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: object with keys 'N_Znface', 'N_Oface', 'In_Znface', 'In_Oface'; each value is a float (total energy in eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Minimum total energies in eV for N and In adatoms on Zn-face and O-face ZnO surfaces. The hidden checker recomputes the differences ΔE(Zn-face) = N_Znface – In_Znface and ΔE(O-face) = N_Oface – In_Oface, and compares them to hidden paper-derived reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `N_Znface`: float (eV)
    - `N_Oface`: float (eV)
    - `In_Znface`: float (eV)
    - `In_Oface`: float (eV)

Notes: Only the DFT calculation is reproduced; experimental MBE growth data are excluded. The original VASP code is replaced by Quantum ESPRESSO, so absolute total energies may differ, but relative adsorption energy differences are comparable within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "N_Znface": "float (eV)",
          "N_Oface": "float (eV)",
          "In_Znface": "float (eV)",
          "In_Oface": "float (eV)"
        }
      },
      "description": "Minimum total energies in eV for N and In adatoms on Zn-face and O-face ZnO surfaces. The hidden checker recomputes the differences ΔE(Zn-face) = N_Znface – In_Znface and ΔE(O-face) = N_Oface – In_Oface, and compares them to hidden paper-derived reference values with tolerance."
    }
  ],
  "notes": "Only the DFT calculation is reproduced; experimental MBE growth data are excluded. The original VASP code is replaced by Quantum ESPRESSO, so absolute total energies may differ, but relative adsorption energy differences are comparable within tolerance."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/adsorption_energies.json` and compute the energy differences ΔE(Zn-face) = N_Znface – In_Znface and ΔE(O-face) = N_Oface – In_Oface. It will compare each ΔE to a reference value derived from the original study, evaluating both the sign (which adatom species is more stable) and whether the magnitude lies within an allowed tolerance. The tolerance is chosen to absorb legitimate differences arising from the use of Quantum ESPRESSO and different pseudopotentials. Only the two computed differences matter; the absolute total energies are not scored directly. Your solution receives full credit if both differences satisfy the verifier's criteria (sign and tolerance). There is no need to match any published number exactly; the key is that the hidden comparison confirms the expected ordering and approximate magnitude.
