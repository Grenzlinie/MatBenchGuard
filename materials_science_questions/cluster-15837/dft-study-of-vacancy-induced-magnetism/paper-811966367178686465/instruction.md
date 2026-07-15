# Prediction of Magnetism in Carbon-Doped ZnO from Density Functional Theory

## Problem background
Dilute magnetic semiconductors (DMS) are sought for spintronic devices that exploit both charge and spin. ZnO has been a candidate host, but doping with transition metals often yields inconsistent magnetism due to clustering. Exploring non‑transition‑metal dopants such as carbon could circumvent these issues. This task investigates whether carbon doping in wurtzite ZnO can induce magnetism and, if so, what the electronic origin and magnetic coupling are. Using density functional theory, you will compute the magnetic moment, orbital contributions, formation energy, local density of states, and inter‑defect coupling for carbon introduced at various sites in ZnO, providing a quantitative picture of magnetism in this system.

## Approach
The investigation is carried out with first‑principles spin‑polarized density functional theory (DFT) within the local spin density approximation (LSDA) and the projector‑augmented wave (PAW) method. You will construct periodic ZnO supercells and introduce carbon at three sites: substitutional on an oxygen site (C_O), substitutional on a zinc site (C_Zn), and interstitial (C_I). After relaxing each structure, you will perform self‑consistent field calculations to obtain total energies, spin densities, and wavefunctions. From these you extract the integrated magnetic moment for C_Zn and C_I, the local density of states projected onto carbon and neighboring zinc atoms for C_O, and the total magnetization per carbon together with orbital‑resolved contributions and the formation energy of the C_O defect. Finally, you will build a supercell with two well‑separated C_O defects, calculate total energies for ferromagnetic and antiferromagnetic spin alignments, and determine the energy difference that characterises the magnetic coupling. All calculations will be performed with an open‑source DFT code such as Quantum ESPRESSO.

## Reproduction target
Produce the key electronic and magnetic properties of carbon‑doped wurtzite ZnO from first‑principles DFT. Specifically:
- Determine whether C_Zn and C_I defects carry a magnetic moment (expected to be near zero if non‑magnetic).
- For the C_O defect, compute the total magnetic moment per carbon atom, the moment decomposed into contributions from carbon 2p orbitals, nearest‑neighbour Zn atoms, and second‑nearest‑neighbour O atoms, and the formation energy relative to pristine ZnO and an isolated carbon atom.
- Obtain the local density of states projected onto carbon and identify the energy positions of the C 2s and C 2p peaks relative to the Fermi level.
- For two C_O defects at a separation of about 7.76 Å, compute the total energy of the ferromagnetic (FM) and antiferromagnetic (AFM) spin arrangements and report the energy difference ΔE = E(AFM) – E(FM), where a positive value indicates a FM ground state.

## Assets

- Wurtzite ZnO crystal structure and lattice parameters
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PAW pseudopotentials for Zn, O, C (e.g., Pslibrary): https://github.com/dalcorso/pslibrary
- Structure generation tools (ASE, pymatgen): ase

## Workflow steps

### Step 1: Build and relax defect supercells
- Role: process
- Action: Construct a wurtzite ZnO supercell (18 formula units, with the paper-reported lattice constants a=3.184 Å, c=5.111 Å). Create initial configurations for carbon substitution at the oxygen site (C_O), carbon substitution at the zinc site (C_Zn), and interstitial carbon (C_I). Relax atomic positions of each defect structure using spin-polarized DFT (LSDA, plane-wave cutoff appropriate for the chosen pseudopotentials, and a Monkhorst-Pack k-point grid sufficient for the supercell) until Hellman-Feynman forces are converged.
- Evidence: `/app/outputs/relaxed_coordinates.json`

### Step 2: DFT total energy and charge density calculations
- Role: process
- Action: For the relaxed C_O, C_Zn, C_I supercells, as well as a pristine ZnO 18-f.u. supercell and an isolated carbon atom in a large simulation cell, perform spin-polarized self-consistent field (SCF) calculations using the same DFT settings. Save total energies, spin densities, and wavefunctions for subsequent analysis.
- Evidence: `/app/outputs/scf_outputs.zip`

### Step 3: Magnetic moments for C_Zn and C_I defects
- Role: scored
- Action: From the SCF outputs for the C_Zn and C_I supercells, extract the integrated absolute magnetic moment per supercell. Write the results to other_defects_magnetism.json.
- Output file: `/app/outputs/other_defects_magnetism.json`
- Format: json
- Contract: {"C_Zn_moment": float (μ_B), "C_I_moment": float (μ_B)}
- Scoring: scored by hidden verifier

### Step 4: Local density of states peak positions for C_O
- Role: scored
- Action: Using the wavefunction/charge density from step02 for the C_O defect, compute the projected local density of states (LDOS) on carbon and neighboring Zn atoms. Identify the energy positions (in eV, relative to the Fermi level) of the carbon 2s and carbon 2p peaks. Write to ldos_peaks.json.
- Output file: `/app/outputs/ldos_peaks.json`
- Format: json
- Contract: {"C_2s_peak": float (eV), "C_2p_peak": float (eV)}
- Scoring: scored by hidden verifier

### Step 5: Magnetic moments, orbital contributions, and formation energy for C_O
- Role: scored (load-bearing)
- Action: From the step02 data for C_O, pristine ZnO, and isolated carbon: (1) compute the total magnetic moment per substituted carbon for the C_O defect; (2) decompose the moment into contributions from the carbon 2p orbitals, each nearest-neighbor Zn atom, and each second-nearest-neighbor O atom; (3) compute the formation energy of C_O as E(C_O) – E(pristine) – E(isolated C). Write all results to properties_c_o.json.
- Output file: `/app/outputs/properties_c_o.json`
- Format: json
- Contract: {"total_moment_per_C": float (μ_B), "C_2p_contribution": float (μ_B), "Zn_contribution": float (μ_B), "O_contribution": float (μ_B), "formation_energy": float (eV)}
- Scoring: scored by hidden verifier

### Step 6: Two-C defect supercell and ferromagnetic/antiferromagnetic total energies
- Role: process
- Action: Build a supercell with two oxygen atoms substituted by carbon atoms at the largest possible separation (~7.76 Å). Relax atomic positions and perform spin-polarized DFT calculations for both ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments. Save the total energy of each configuration to two_C_energies.json.
- Evidence: `/app/outputs/two_C_energies.json`

### Step 7: Ferromagnetic coupling energy
- Role: scored (load-bearing)
- Action: Compute the energy difference ΔE = E(AFM) – E(FM) using the two-C total energies from step06. Write the result (a positive difference means the FM state is lower in energy) to coupling_energy.json.
- Output file: `/app/outputs/coupling_energy.json`
- Format: json
- Contract: {"fm_afm_energy_difference": float (eV), positive means FM lower}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/other_defects_magnetism.json`
- `/app/outputs/ldos_peaks.json`
- `/app/outputs/properties_c_o.json`
- `/app/outputs/coupling_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### other_defects_magnetism.json
- path: `/app/outputs/other_defects_magnetism.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Magnetic moment per supercell for C_Zn and C_I defects. The paper reports these configurations as non-magnetic. The checker verifies that each moment is ≤ 0.01 μ_B.
- schema:
  - `type`: object
  - `required`:
    - `C_Zn_moment`: float (μ_B)
    - `C_I_moment`: float (μ_B)

### ldos_peaks.json
- path: `/app/outputs/ldos_peaks.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy positions of the carbon 2s and 2p peaks in the local density of states of the C_O defect, relative to the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `C_2s_peak`: float (eV)
    - `C_2p_peak`: float (eV)

### properties_c_o.json
- path: `/app/outputs/properties_c_o.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moment per carbon, orbital-resolved contributions, and formation energy of the substitutional C_O defect.
- schema:
  - `type`: object
  - `required`:
    - `total_moment_per_C`: float (μ_B)
    - `C_2p_contribution`: float (μ_B)
    - `Zn_contribution`: float (μ_B)
    - `O_contribution`: float (μ_B)
    - `formation_energy`: float (eV)

### coupling_energy.json
- path: `/app/outputs/coupling_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy difference between the antiferromagnetic and ferromagnetic spin alignments of two C_O defects. A positive value indicates a ferromagnetic ground state.
- schema:
  - `type`: object
  - `required`:
    - `fm_afm_energy_difference`: float (eV)

Notes: All numeric quantities are compared against the paper-reported values with tolerances appropriate for a DFT reimplementation using an open-source code and a different pseudopotential set. The load-bearing steps 05 and 07 ensure that the intermediate DFT pipeline must be executed to produce the target properties.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "other_defects_magnetism.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "C_Zn_moment": "float (μ_B)",
          "C_I_moment": "float (μ_B)"
        }
      },
      "description": "Magnetic moment per supercell for C_Zn and C_I defects. The paper reports these configurations as non-magnetic. The checker verifies that each moment is ≤ 0.01 μ_B."
    },
    {
      "file": "ldos_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C_2s_peak": "float (eV)",
          "C_2p_peak": "float (eV)"
        }
      },
      "description": "Energy positions of the carbon 2s and 2p peaks in the local density of states of the C_O defect, relative to the Fermi level."
    },
    {
      "file": "properties_c_o.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "total_moment_per_C": "float (μ_B)",
          "C_2p_contribution": "float (μ_B)",
          "Zn_contribution": "float (μ_B)",
          "O_contribution": "float (μ_B)",
          "formation_energy": "float (eV)"
        }
      },
      "description": "Total magnetic moment per carbon, orbital-resolved contributions, and formation energy of the substitutional C_O defect."
    },
    {
      "file": "coupling_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "fm_afm_energy_difference": "float (eV)"
        }
      },
      "description": "Energy difference between the antiferromagnetic and ferromagnetic spin alignments of two C_O defects. A positive value indicates a ferromagnetic ground state."
    }
  ],
  "notes": "All numeric quantities are compared against the paper-reported values with tolerances appropriate for a DFT reimplementation using an open-source code and a different pseudopotential set. The load-bearing steps 05 and 07 ensure that the intermediate DFT pipeline must be executed to produce the target properties."
}
```

## How you are scored
A hidden verifier evaluates your results after you finish. It reads the scored JSON artifacts (`other_defects_magnetism.json`, `ldos_peaks.json`, `properties_c_o.json`, `coupling_energy.json`) and compares each numeric entry against independently determined reference values derived from the original study. Tolerances account for differences between DFT implementations, pseudopotentials, and numerical settings. Reporting the paper's numbers without performing the calculations will not yield passing scores, because several outputs depend on the intermediate DFT pipeline and the verifier checks that the pipeline was genuinely executed. Each scored artifact carries a weight; the verifier combines them into a final reward between 0 and 1.
