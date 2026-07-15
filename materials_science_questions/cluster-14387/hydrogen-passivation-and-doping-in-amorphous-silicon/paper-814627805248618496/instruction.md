# Phosphorus defect states in silicon nanocrystal/SiO2 systems

## Problem background
Silicon nanocrystals (SiNCs) embedded in SiO₂ are promising building blocks for nanoelectronics, but the role of phosphorus (P) as a dopant is not well understood. In bulk silicon, P acts as a shallow donor, providing free electrons. In SiNC/SiO₂ systems, however, P incorporation has been linked to both increased conductivity and photoluminescence quenching, and it is unclear whether P actually ionizes and donates electrons into the nanocrystals or instead creates deep defect states that alter transport and recombination. Resolving this question is essential for designing doped SiNC-based devices.

## Approach
This task uses hybrid density functional theory (DFT) calculations to determine the electronic structure of P in different environments relevant to the SiNC/SiO₂ system. Four atomic approximants are constructed: (1) a SiO₂ reference with a central Si replaced by P (SiO₂:P), (2) a fully OH‑terminated Si nanocrystal of ~1.5 nm size serving as the intrinsic reference (OH‑SiNC), (3) the same nanocrystal with a central Si atom replaced by P (substitutional P), and (4) the nanocrystal with P placed on a central interstitial site. All-electron B3LYP/6-31G(d) calculations are performed on each structure to obtain the HOMO and LUMO energies. From these energies, three key sets of quantities are derived: the effect of P in SiO₂ on electron and hole transport barriers relative to the intrinsic nanocrystal, the ionization properties of substitutional P inside the nanocrystal, and the positions of gap states and recombination energy introduced by interstitial P.

## Reproduction target
The objective is to compute the three following results from the DFT calculations:
1. For P in SiO₂: the reduction in electron and hole transport barriers, expressed as percentages, using the known Si/SiO₂ conduction-band and valence-band offsets (3.2 eV and 4.5 eV).
2. For substitutional P inside the SiNC: the donor ionization energy and its ionization probability at 300 K.
3. For interstitial P inside the SiNC: the energies of the two gap states (occupied and unoccupied) relative to the SiNC band edges, and the optical recombination transition energy between them.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- alpha-quartz crystal structure
- ideal silicon nanocrystal geometry
- Si/SiO2 band offsets

## Workflow steps

### Step 1: Build atomic approximants
- Role: process
- Action: Construct the atomic structures for four systems: SiO2:P (central Si replaced by P in alpha-quartz, OH-terminated), OH-SiNC (fully OH-terminated ~15 Å Si nanocrystal), OH-SiNC-P[Si] (substitutional P in SiNC), and OH-SiNC-P[is] (interstitial P in SiNC). Use ASE or similar tools to build models based on published structural data.
- Evidence: none

### Step 2: Hybrid DFT geometry optimization and energy calculation
- Role: process
- Action: Perform geometry optimization followed by single-point energy calculation for each approximant using B3LYP/6-31G(d) in ORCA. Extract HOMO and LUMO energies for each system. Save optimized geometries and orbital energies to an intermediate file.
- Evidence: `/app/outputs/dft_energies.json`

### Step 3: SiO2:P barrier reductions
- Role: scored (load-bearing)
- Action: From the HOMO/LUMO energies of SiO2:P and OH-SiNC, compute the α-HOMO offset (SiO2:P α-HOMO minus OH-SiNC HOMO) and β-LUMO offset (SiO2:P β-LUMO minus OH-SiNC LUMO). Using the known Si/SiO2 band offsets (conduction-band offset 3.2 eV, valence-band offset 4.5 eV), compute the effective electron transport barrier reduction and hole transport barrier reduction percentages.
- Output file: `/app/outputs/sio2_p_energies.json`
- Format: json
- Contract: {"sio2_p_homo_ev": "number (eV)", "oh_sinc_homo_ev": "number (eV)", "alpha_homo_offset_ev": "number (eV)", "sio2_p_lumo_ev": "number (eV)", "oh_sinc_lumo_ev": "number (eV)", "beta_lumo_offset_ev": "number (eV)", "electron_barrier_reduction_pct": "number (%)", "hole_barrier_reduction_pct": "number (%)"}
- Scoring: scored by hidden verifier

### Step 4: Substitutional P donor ionization
- Role: scored
- Action: For the OH-SiNC-P[Si] system, extract the HOMO energy. Compute the donor ionization energy as OH-SiNC LUMO minus OH-SiNC-P[Si] HOMO. Compute the ionization probability at 300 K using exp(-E_ion/kT).
- Output file: `/app/outputs/sinc_p_substitutional_energies.json`
- Format: json
- Contract: {"oh_sinc_lumo_ev": "number (eV)", "substitutional_homo_relative_to_lumo_ev": "number (eV)", "ionization_energy_ev": "number (eV)", "ionization_probability_300K": "number"}
- Scoring: scored by hidden verifier

### Step 5: Interstitial P gap states
- Role: scored
- Action: For the OH-SiNC-P[is] system, identify the two gap states: the occupied HOMO and unoccupied LUMO. Compute the HOMO offset relative to OH-SiNC HOMO, LUMO offset relative to OH-SiNC LUMO, and the optical recombination transition energy as (LUMO − HOMO).
- Output file: `/app/outputs/sinc_p_interstitial_energies.json`
- Format: json
- Contract: {"oh_sinc_homo_ev": "number (eV)", "oh_sinc_lumo_ev": "number (eV)", "interstitial_homo_ev": "number (eV)", "interstitial_homo_relative_to_sinc_homo_ev": "number (eV)", "interstitial_lumo_ev": "number (eV)", "interstitial_lumo_relative_to_sinc_lumo_ev": "number (eV)", "optical_transition_energy_ev": "number (eV)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sio2_p_energies.json`
- `/app/outputs/sinc_p_substitutional_energies.json`
- `/app/outputs/sinc_p_interstitial_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sio2_p_energies.json
- path: `/app/outputs/sio2_p_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the computed HOMO/LUMO energies for SiO2:P and OH-SiNC, the derived offsets, and the resulting electron and hole transport barrier reduction percentages. The offsets and reduction percentages are the scored quantities; the raw energies provide context.
- schema:
  - `type`: object
  - `required`: `sio2_p_homo_ev`, `oh_sinc_homo_ev`, `alpha_homo_offset_ev`, `sio2_p_lumo_ev`, `oh_sinc_lumo_ev`, `beta_lumo_offset_ev`, `electron_barrier_reduction_pct`, `hole_barrier_reduction_pct`
  - `items`:
    - `sio2_p_homo_ev`: number (eV)
    - `oh_sinc_homo_ev`: number (eV)
    - `alpha_homo_offset_ev`: number (eV)
    - `sio2_p_lumo_ev`: number (eV)
    - `oh_sinc_lumo_ev`: number (eV)
    - `beta_lumo_offset_ev`: number (eV)
    - `electron_barrier_reduction_pct`: number (%)
    - `hole_barrier_reduction_pct`: number (%)

### sinc_p_substitutional_energies.json
- path: `/app/outputs/sinc_p_substitutional_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the OH-SiNC LUMO energy, the substitutional P HOMO relative to that LUMO, the resulting ionization energy, and ionization probability at 300 K. The ionization energy and probability are scored.
- schema:
  - `type`: object
  - `required`: `oh_sinc_lumo_ev`, `substitutional_homo_relative_to_lumo_ev`, `ionization_energy_ev`, `ionization_probability_300K`
  - `items`:
    - `oh_sinc_lumo_ev`: number (eV)
    - `substitutional_homo_relative_to_lumo_ev`: number (eV)
    - `ionization_energy_ev`: number (eV)
    - `ionization_probability_300K`: number

### sinc_p_interstitial_energies.json
- path: `/app/outputs/sinc_p_interstitial_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the reference OH-SiNC band edge energies, the two gap state energies for interstitial P, their offsets from the SiNC edges, and the optical recombination transition energy. The offsets and transition energy are scored.
- schema:
  - `type`: object
  - `required`: `oh_sinc_homo_ev`, `oh_sinc_lumo_ev`, `interstitial_homo_ev`, `interstitial_homo_relative_to_sinc_homo_ev`, `interstitial_lumo_ev`, `interstitial_lumo_relative_to_sinc_lumo_ev`, `optical_transition_energy_ev`
  - `items`:
    - `oh_sinc_homo_ev`: number (eV)
    - `oh_sinc_lumo_ev`: number (eV)
    - `interstitial_homo_ev`: number (eV)
    - `interstitial_homo_relative_to_sinc_homo_ev`: number (eV)
    - `interstitial_lumo_ev`: number (eV)
    - `interstitial_lumo_relative_to_sinc_lumo_ev`: number (eV)
    - `optical_transition_energy_ev`: number (eV)

Notes: The scored quantities are the offsets and derived properties; the raw reference energies (OH-SiNC HOMO/LUMO) must be computed correctly from the DFT step to serve as the baseline for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sio2_p_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "sio2_p_homo_ev",
          "oh_sinc_homo_ev",
          "alpha_homo_offset_ev",
          "sio2_p_lumo_ev",
          "oh_sinc_lumo_ev",
          "beta_lumo_offset_ev",
          "electron_barrier_reduction_pct",
          "hole_barrier_reduction_pct"
        ],
        "items": {
          "sio2_p_homo_ev": "number (eV)",
          "oh_sinc_homo_ev": "number (eV)",
          "alpha_homo_offset_ev": "number (eV)",
          "sio2_p_lumo_ev": "number (eV)",
          "oh_sinc_lumo_ev": "number (eV)",
          "beta_lumo_offset_ev": "number (eV)",
          "electron_barrier_reduction_pct": "number (%)",
          "hole_barrier_reduction_pct": "number (%)"
        }
      },
      "description": "Contains the computed HOMO/LUMO energies for SiO2:P and OH-SiNC, the derived offsets, and the resulting electron and hole transport barrier reduction percentages. The offsets and reduction percentages are the scored quantities; the raw energies provide context."
    },
    {
      "file": "sinc_p_substitutional_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "oh_sinc_lumo_ev",
          "substitutional_homo_relative_to_lumo_ev",
          "ionization_energy_ev",
          "ionization_probability_300K"
        ],
        "items": {
          "oh_sinc_lumo_ev": "number (eV)",
          "substitutional_homo_relative_to_lumo_ev": "number (eV)",
          "ionization_energy_ev": "number (eV)",
          "ionization_probability_300K": "number"
        }
      },
      "description": "Contains the OH-SiNC LUMO energy, the substitutional P HOMO relative to that LUMO, the resulting ionization energy, and ionization probability at 300 K. The ionization energy and probability are scored."
    },
    {
      "file": "sinc_p_interstitial_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "oh_sinc_homo_ev",
          "oh_sinc_lumo_ev",
          "interstitial_homo_ev",
          "interstitial_homo_relative_to_sinc_homo_ev",
          "interstitial_lumo_ev",
          "interstitial_lumo_relative_to_sinc_lumo_ev",
          "optical_transition_energy_ev"
        ],
        "items": {
          "oh_sinc_homo_ev": "number (eV)",
          "oh_sinc_lumo_ev": "number (eV)",
          "interstitial_homo_ev": "number (eV)",
          "interstitial_homo_relative_to_sinc_homo_ev": "number (eV)",
          "interstitial_lumo_ev": "number (eV)",
          "interstitial_lumo_relative_to_sinc_lumo_ev": "number (eV)",
          "optical_transition_energy_ev": "number (eV)"
        }
      },
      "description": "Contains the reference OH-SiNC band edge energies, the two gap state energies for interstitial P, their offsets from the SiNC edges, and the optical recombination transition energy. The offsets and transition energy are scored."
    }
  ],
  "notes": "The scored quantities are the offsets and derived properties; the raw reference energies (OH-SiNC HOMO/LUMO) must be computed correctly from the DFT step to serve as the baseline for scoring."
}
```

## How you are scored
A hidden verifier independently scores each of the three scored workflow stages. For every stage, the verifier reads the JSON artifact you produce under /app/outputs and compares the numeric values you report to reference values (derived from the original study) using appropriate tolerances. The three stages are weighted and combined into a single reward between 0 and 1. Submitting the paper's numbers without executing the full workflow will not yield a passing score, because the verification checks both the reported quantities and the consistency of the underlying calculations.
