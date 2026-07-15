# Reproduce DFT-predicted properties of zinc-blende IrC

## Problem background
Transition metal carbides (TMCs) are widely sought as hard, wear-resistant materials. Many TMCs have been studied theoretically to guide synthesis, but several candidate structures remain unexplored. This work investigates the zinc-blende phase of iridium carbide (ZB‑IrC) using first-principles calculations. The goal is to determine whether ZB‑IrC is simultaneously stable (energy, mechanical, dynamical), hard, ductile, and metallic – a combination of properties that would make it an attractive conducting hard material for high-pressure synthesis.

## Approach
The approach is a first-principles DFT workflow using the Perdew–Burke–Ernzerhof (PBE) functional. You will perform the following: (i) optimize the geometry of ZB‑IrC to obtain the equilibrium lattice constant and total energy; (ii) compute the formation energy using elemental reference energies (fcc Ir metal and graphite); (iii) calculate the elastic stiffness constants (C11, C12, C44) via stress‑strain methods and derive the bulk and shear moduli as well as the Pugh ratio B/G; (iv) assess dynamical stability by computing phonon frequencies and verifying the absence of imaginary modes; (v) compute the electronic density of states to confirm metallic character (finite DOS at the Fermi level); (vi) perform Mulliken bond population analysis to extract the bond overlap population; and (vii) apply a semi‑empirical hardness model that incorporates d‑valence electrons to estimate the Vickers hardness from the bond parameters. All calculations should be carried out with the PBE functional and open‑source DFT software (Quantum ESPRESSO) using standard pseudopotentials.

## Reproduction target
Using DFT (PBE functional) and an open‑source plane‑wave code, compute and report the following properties of zinc‑blende IrC in the structured JSON files specified in the workflow steps:

- Equilibrium lattice constant (Å), total energy per formula unit (eV), and formation energy per atom (eV).
- Elastic constants C11, C12, C44 (GPa), bulk modulus B (GPa), shear modulus G (GPa), and the B/G ratio.
- Dynamical stability: absence of imaginary phonon frequencies (indicator and lowest frequency in cm⁻¹).
- Electronic metallicity: DOS at the Fermi level (states/eV/formula unit) and a boolean metallic flag.
- Vickers hardness Hv (GPa) together with the underlying bond parameters (bond length, electron density, overlap population, covalent population, ionicity factor, metallicity factor) as obtained from the semi‑empirical hardness model.

The task is to reproduce these quantities; do not simply report numbers – you must execute the entire computational pipeline to generate the results.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ir and C pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Construct ZB-IrC initial structure
- Role: process
- Action: Generate the initial zinc-blende IrC structure: Ir at (0,0,0), C at (0.25,0.25,0.25) in a cubic cell. Use a reasonable starting lattice constant (e.g., 4.6 Å).
- Evidence: `/app/outputs/initial_structure.json`

### Step 2: Calculate elemental reference energies
- Role: process
- Action: Perform DFT calculations for fcc Ir metal (4-atom cubic cell) and graphite (4-atom hexagonal cell) to obtain per-atom total energies (H_Ir and H_graphite) using the same functional and pseudopotentials as the main calculation.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Optimize ZB-IrC geometry and compute formation energy
- Role: scored
- Action: Using DFT (PBE functional), relax the atomic positions and cell parameters of ZB-IrC to obtain the equilibrium lattice constant and total energy. Compute the formation energy ΔE per atom from the optimized total energy and the elemental reference energies.
- Output file: `/app/outputs/geometry_optimization.json`
- Format: json
- Contract: {"lattice_constant_A": "float", "total_energy_eV_per_fu": "float", "formation_energy_eV_per_atom": "float"}
- Scoring: scored by hidden verifier

### Step 4: Calculate elastic constants and moduli
- Role: scored
- Action: Compute the elastic stiffness constants (C11, C12, C44) of ZB-IrC using the stress-strain method. Derive the bulk modulus B, shear modulus G using Voigt-Reuss-Hill averaging, and compute the Pugh ratio B/G.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"C11_GPa": "float", "C12_GPa": "float", "C44_GPa": "float", "bulk_modulus_B_GPa": "float", "shear_modulus_G_GPa": "float", "B_over_G": "float"}
- Scoring: scored by hidden verifier

### Step 5: Phonon dispersion and dynamical stability
- Role: scored
- Action: Calculate phonon frequencies for ZB-IrC along high-symmetry paths and at the Gamma point. Check for imaginary frequencies to confirm dynamical stability.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: {"has_imaginary_frequencies": "bool", "lowest_frequency_cm-1": "float", "note": "string"}
- Scoring: scored by hidden verifier

### Step 6: Electronic density of states
- Role: scored
- Action: Compute the total and projected density of states (DOS) for ZB-IrC. Determine if the DOS at the Fermi level is finite (indicating metallic character).
- Output file: `/app/outputs/dos_metallicity.json`
- Format: json
- Contract: {"DOS_at_Fermi_level_states_per_eV_per_fu": "float", "is_metallic": "bool"}
- Scoring: scored by hidden verifier

### Step 7: Mulliken bond population analysis
- Role: process
- Action: Perform Mulliken population analysis on the optimized ZB-IrC structure using a distance cutoff of 3 Å. Extract the bond overlap population P.
- Evidence: `/app/outputs/mulliken_population.json`

### Step 8: Estimate Vickers hardness
- Role: scored (load-bearing)
- Action: Apply the semi-empirical hardness model that considers d valence electrons to ZB-IrC. Use the bond length from the optimization step, the Mulliken overlap population from the population analysis, the valence electron number Z_Ir=4, and the model equations. Report all derived parameters and the Vickers hardness H_v.
- Output file: `/app/outputs/hardness.json`
- Format: json
- Contract: {"bond_length_d_A": "float", "electron_density_N_e": "float", "overlap_population_P": "float", "covalent_population_Pc": "float", "ionicity_factor_fi": "float", "metallicity_factor_fm": "float", "Vickers_hardness_Hv_GPa": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometry_optimization.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/phonon_stability.json`
- `/app/outputs/dos_metallicity.json`
- `/app/outputs/hardness.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometry_optimization.json
- path: `/app/outputs/geometry_optimization.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameter, total energy, and formation energy of ZB-IrC.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: float
    - `total_energy_eV_per_fu`: float
    - `formation_energy_eV_per_atom`: float

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic constants (C11, C12, C44), bulk and shear moduli, and B/G ratio of ZB-IrC.
- schema:
  - `type`: object
  - `required`:
    - `C11_GPa`: float
    - `C12_GPa`: float
    - `C44_GPa`: float
    - `bulk_modulus_B_GPa`: float
    - `shear_modulus_G_GPa`: float
    - `B_over_G`: float

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Dynamical stability verdict: absence of imaginary phonon modes (true = stable).
- schema:
  - `type`: object
  - `required`:
    - `has_imaginary_frequencies`: bool
    - `lowest_frequency_cm-1`: float
    - `note`: string

### dos_metallicity.json
- path: `/app/outputs/dos_metallicity.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: DOS at Fermi level and metallic character of ZB-IrC.
- schema:
  - `type`: object
  - `required`:
    - `DOS_at_Fermi_level_states_per_eV_per_fu`: float
    - `is_metallic`: bool

### hardness.json
- path: `/app/outputs/hardness.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Vickers hardness and bond parameters of ZB-IrC computed with the semi-empirical model.
- schema:
  - `type`: object
  - `required`:
    - `bond_length_d_A`: float
    - `electron_density_N_e`: float
    - `overlap_population_P`: float
    - `covalent_population_Pc`: float
    - `ionicity_factor_fi`: float
    - `metallicity_factor_fm`: float
    - `Vickers_hardness_Hv_GPa`: float

Notes: All outputs are scored against the paper-reported values with tolerances accounting for code differences (CASTEP vs Quantum ESPRESSO). The hardness step is load-bearing; it cannot be produced without the Mulliken population analysis (step_07).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometry_optimization.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "float",
          "total_energy_eV_per_fu": "float",
          "formation_energy_eV_per_atom": "float"
        }
      },
      "description": "Optimized lattice parameter, total energy, and formation energy of ZB-IrC."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11_GPa": "float",
          "C12_GPa": "float",
          "C44_GPa": "float",
          "bulk_modulus_B_GPa": "float",
          "shear_modulus_G_GPa": "float",
          "B_over_G": "float"
        }
      },
      "description": "Elastic constants (C11, C12, C44), bulk and shear moduli, and B/G ratio of ZB-IrC."
    },
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "has_imaginary_frequencies": "bool",
          "lowest_frequency_cm-1": "float",
          "note": "string"
        }
      },
      "description": "Dynamical stability verdict: absence of imaginary phonon modes (true = stable)."
    },
    {
      "file": "dos_metallicity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "DOS_at_Fermi_level_states_per_eV_per_fu": "float",
          "is_metallic": "bool"
        }
      },
      "description": "DOS at Fermi level and metallic character of ZB-IrC."
    },
    {
      "file": "hardness.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bond_length_d_A": "float",
          "electron_density_N_e": "float",
          "overlap_population_P": "float",
          "covalent_population_Pc": "float",
          "ionicity_factor_fi": "float",
          "metallicity_factor_fm": "float",
          "Vickers_hardness_Hv_GPa": "float"
        }
      },
      "description": "Vickers hardness and bond parameters of ZB-IrC computed with the semi-empirical model."
    }
  ],
  "notes": "All outputs are scored against the paper-reported values with tolerances accounting for code differences (CASTEP vs Quantum ESPRESSO). The hardness step is load-bearing; it cannot be produced without the Mulliken population analysis (step_07)."
}
```

## How you are scored
A hidden verifier independently scores each of the five scored output files (`geometry_optimization.json`, `elastic_constants.json`, `phonon_stability.json`, `dos_metallicity.json`, `hardness.json`). Each artifact is compared against reference values derived from the original DFT study, with tolerances that account for expected differences between DFT implementations (e.g., CASTEP vs. Quantum ESPRESSO). The per‑artifact scores are weighted and combined into a final reward between 0 and 1. Higher accuracy in the computed properties and correct structural verdicts (e.g., truly stable, truly metallic) yield a higher reward. Simply writing down the expected numbers is not sufficient; the verifier expects internally consistent artifacts that result from genuinely running the prescribed DFT workflow.
