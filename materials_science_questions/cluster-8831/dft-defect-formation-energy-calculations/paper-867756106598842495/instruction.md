# First-Principles Formation Energy and Electronic Structure of Oxygen-Vacancy-Ordered LaNiO3-x

## Problem background
Oxygen vacancies in rare-earth nickelates such as LaNiO₃₋ₓ can dramatically modify electronic and magnetic properties. As the vacancy content x increases, LaNiO₃₋ₓ undergoes a metal–insulator transition and the vacancy-ordered LaNiO₂.₅ phase is known to be insulating and antiferromagnetic at low temperatures. The microscopic origin of this insulating state and the thermodynamic stability of the vacancy-ordered structure are crucial for oxide electronics and correlated materials. In this task you will compute the formation energies of LaNiO₃, LaNiO₂.₅, and LaNiO₂ as a function of the oxygen chemical potential, and obtain the total density of states for LaNiO₂.₅ at around room temperature, to determine the stable oxygen-vacancy phases and the nature of the insulating gap.

## Approach
The approach uses first-principles electronic structure methods to treat the effect of oxygen vacancies on the electronic and thermodynamic properties of LaNiO₃₋ₓ. First, density functional theory with a Hubbard‑U correction (DFT+U) is used to relax the crystal structures of LaNiO₃, LaNiO₂.₅, and LaNiO₂ for different magnetic orderings and to obtain their ground‑state total energies. Maximally localized Wannier functions are then constructed for the Ni 3d and O 2p orbitals to form a realistic low‑energy Hamiltonian. These Wannier Hamiltonians serve as input for dynamical mean‑field theory (DFT+DMFT) calculations that treat the paramagnetic correlated electronic state at elevated temperature and at near room temperature. The computed total energies from both DFT+U and DFT+DMFT are combined with the energy of an oxygen molecule reservoir to compute the Gibbs formation energy of each vacancy-ordered structure as a function of the oxygen chemical potential. By evaluating the formation energies across a range of μ_O, the relative thermodynamic stability of the three phases is assessed. Finally, the total density of states of LaNiO₂.₅ is extracted from a DFT+DMFT calculation at T≈290 K to characterise the spectral gap.

## Reproduction target
Produce two scored artifacts. (1) A file `formation_energies.csv` containing the formation energies (in eV) of LaNiO₃, LaNiO₂.₅, and LaNiO₂ as a function of the oxygen chemical potential μ_O (in eV), computed with both DFT+U and DFT+DMFT. The data must cover a μ_O range that spans the oxygen‑rich to oxygen‑poor regimes, enabling a stability comparison. (2) A file `total_dos.csv` containing the total density of states (in states/eV) of LaNiO₂.₅ as a function of energy (in eV) referenced to the Fermi level, obtained from a DFT+DMFT calculation at T≈290 K. The data must allow the presence and width of an insulating gap to be determined.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: http://www.wannier.org/
- DMFTwDFT: https://github.com/HParkLAB/DMFTwDFT
- PBE-sol pseudopotentials (SSSP): https://www.materialscloud.org/discover/sssp/table/pbe

## Workflow steps

### Step 1: Structural relaxation and DFT+U total energies
- Role: process
- Action: Relax the crystal structures of LaNiO3, LaNiO2.5, LaNiO2 (and optionally intermediate vacancy levels) with DFT+U (Hubbard U=5 eV, Hund J=0.8 eV) for different magnetic orderings (NM, FM, G-AFM). Keep the lowest-energy magnetic configuration for each composition. Also compute the total energy of an isolated O2 molecule.
- Evidence: `/app/outputs/relaxation_summary.json`

### Step 2: Wannier function construction
- Role: process
- Action: From non-magnetic DFT calculations of LaNiO3, LaNiO2.5 and LaNiO2, build maximally localized Wannier functions for Ni 3d and O 2p orbitals using an energy window of -9 to +5 eV.
- Evidence: `/app/outputs/wannier_summary.txt`

### Step 3: DFT+DMFT total energy calculations at T=920 K
- Role: process
- Action: Perform DFT+DMFT self-consistent calculations for LaNiO3, LaNiO2.5, and LaNiO2 with paramagnetic ordering at T=920 K, using the Wannier Hamiltonians from Step 1 and the same interaction parameters (U=5 eV, J=0.8 eV). Obtain total energies.
- Evidence: `/app/outputs/dmft_total_energies.json`

### Step 4: Formation energy analysis
- Role: scored (load-bearing)
- Action: Compute the Gibbs formation energy E_form as a function of oxygen chemical potential μ_O (using the formation energy formula and the relation of μ_O to pressure) from the DFT+U total energies (Step 0) and the DFT+DMFT total energies (Step 2). Use T=920 K for DFT+DMFT and T=0 K for DFT+U. Output E_form curves for LaNiO3, LaNiO2.5, and LaNiO2.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: columns: structure (string), mu_O (float, in eV), E_form (float, in eV), method (string: 'DFT+U' or 'DFT+DMFT')
- Scoring: scored by hidden verifier

### Step 5: DFT+DMFT spectral calculation for LaNiO2.5 at T=290 K
- Role: scored (load-bearing)
- Action: Perform a DFT+DMFT self-consistent calculation for paramagnetic LaNiO2.5 at T≈290 K using the Wannier Hamiltonian from Step 1. Extract the total density of states (DOS) and output the total DOS as a function of energy.
- Output file: `/app/outputs/total_dos.csv`
- Format: csv
- Contract: columns: energy (float, relative to Fermi energy, in eV), total_dos (float, in states/eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/total_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Formation energies for LaNiO3, LaNiO2.5, LaNiO2 as a function of oxygen chemical potential from DFT+U and DFT+DMFT.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `mu_O`, `E_form`, `method`
  - `units`:
    - `mu_O`: eV
    - `E_form`: eV

### total_dos.csv
- path: `/app/outputs/total_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states for LaNiO2.5 computed via DFT+DMFT at T≈290 K.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`
  - `units`:
    - `energy`: eV
    - `total_dos`: states/eV

Notes: The checker verifies the formation energy ordering (LaNiO2.5 lowest at reduced μ_O) and the presence of an insulating gap in the total DOS.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "mu_O",
          "E_form",
          "method"
        ],
        "units": {
          "mu_O": "eV",
          "E_form": "eV"
        }
      },
      "description": "Formation energies for LaNiO3, LaNiO2.5, LaNiO2 as a function of oxygen chemical potential from DFT+U and DFT+DMFT."
    },
    {
      "file": "total_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos"
        ],
        "units": {
          "energy": "eV",
          "total_dos": "states/eV"
        }
      },
      "description": "Total density of states for LaNiO2.5 computed via DFT+DMFT at T≈290 K."
    }
  ],
  "notes": "The checker verifies the formation energy ordering (LaNiO2.5 lowest at reduced μ_O) and the presence of an insulating gap in the total DOS."
}
```

## How you are scored
A hidden verifier will independently score each output artifact. For the formation energies, it will check that the ordering of the phases as a function of μ_O is physically consistent with the oxygen chemical potential. For the total density of states, it will verify that the spectrum displays an insulating gap of physically reasonable width. Each stage carries a weight, and the verifier combines the per‑stage scores into a final reward between 0 and 1. Simply reporting numbers from the literature is not enough; you must run the computational workflow and produce the corresponding data files.
