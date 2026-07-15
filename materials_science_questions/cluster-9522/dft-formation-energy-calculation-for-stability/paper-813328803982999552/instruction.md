# DFT Formation Energy and Electronic Structure of Carbides in Steels

## Problem background
Niobium microalloyed steels derive their strength and toughness in part from carbide precipitates that form during processing. Understanding which carbide phases are thermodynamically stable and how strongly they bind is essential for predicting the behavior of the steel. First-principles calculations based on density functional theory (DFT) can quantify the intrinsic energetic properties of candidate carbides — binding energy (cohesive energy), formation energy, and electronic density of states at the Fermi level — providing physical insight into their relative stability and forming ability. This task focuses on four carbide types commonly considered in niobium-bearing steels: Fe₃C, Fe₂C, Fe₅C₂, and NbC. You will construct crystal structure models for each carbide, perform DFT geometry optimization and total energy calculations, compute reference energies for isolated atoms and bulk elemental solids, and derive the binding energy per atom, formation energy per atom, and the number of bonding electrons at the Fermi level, N(E_F).

## Approach
The approach follows a standard computational materials science protocol. For each of the four carbides (Fe₃C, Fe₂C, Fe₅C₂, NbC), you will:

- Build an initial crystal structure from known lattice parameters and space groups.
- Perform a DFT geometry optimization to obtain the relaxed structure and its total energy, using the GGA-PBE exchange-correlation functional and ultrasoft pseudopotentials.
- Separately compute the energies of isolated Fe, C, and Nb atoms (free-atom references) and the per-atom energies of the elemental solids (bcc-Fe, a reference solid form of carbon such as diamond or graphite, and bcc-Nb) as solid-state references, employing the same DFT settings.
- Derive the binding energy per atom from the carbide total energy and the free-atom references, and the formation energy per atom from the carbide total energy and the solid-state references.
- Compute the total electronic density of states (DOS) from the optimized structure and extract the density of states at the Fermi level, N(E_F), measured in electrons per eV per atom.

The entire workflow is executable with the open-source Quantum ESPRESSO package and standard pseudopotential libraries. No pre-trained models or external datasets are needed; all required inputs follow from public crystallographic data and the DFT method itself.

## Reproduction target
Your task is to compute, via DFT, the binding energy per atom (eV/atom), formation energy per atom (eV/atom), and the number of bonding electrons at the Fermi level N(E_F) (electrons/eV) for the four carbide phases: Fe₃C, Fe₂C, Fe₅C₂, and NbC. The computed values should reflect the physics of these compounds as determined by the first-principles protocol described above. The objective is to reproduce the energetic and electronic-structure results that are characteristic of these carbide systems.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build crystal structures
- Role: process
- Action: Construct crystal structure models for Fe3C (orthorhombic, Pnma), Fe2C (orthorhombic, Pnnm), Fe5C2 (monoclinic, C2/c), and NbC (cubic, Fm-3m) using publicly known lattice parameters and atomic positions. Save the models as a compressed archive.
- Evidence: `/app/outputs/step_01_structures.zip`

### Step 2: DFT geometry optimization and total energy calculation
- Role: process
- Action: For each carbide, perform geometry optimization and total energy calculation using an open-source DFT code (e.g., Quantum ESPRESSO) with GGA-PBE functional, ultrasoft pseudopotentials, appropriate plane-wave cutoff and k-point sampling. Record the optimized total energy per unit cell, optimized lattice constant a0, and unit cell volume V0.
- Evidence: `/app/outputs/step_02_total_energies.csv`

### Step 3: Free-atom reference energy calculation
- Role: process
- Action: Calculate the energies of isolated free atoms of Fe, C, and Nb using the same pseudopotentials and calculation settings (spin-polarized treatment for Fe, large vacuum cell).
- Evidence: `/app/outputs/step_03_free_atom_energies.csv`

### Step 4: Solid reference energy calculation
- Role: process
- Action: Determine the average atomic energies of the elemental solids: bcc-Fe, the reference crystalline form of carbon (e.g., diamond), and bcc-Nb. Perform DFT calculations on the primitive cells using the same functional, pseudopotential, cutoff, and k-point mesh. Report the per-atom energies.
- Evidence: `/app/outputs/step_04_solid_energies.csv`

### Step 5: Compute binding energies
- Role: scored
- Action: For each carbide, compute the binding energy per atom (cohesive energy) using the formula E_coh = (E_tot - sum of free-atom energies of constituent atoms) / (total number of atoms). Write the results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: columns: carbide (string), binding_energy_eV_per_atom (float)
- Scoring: scored by hidden verifier

### Step 6: Compute formation energies
- Role: scored
- Action: For each carbide, compute the formation energy per atom using the formula E_form = (E_tot - sum of solid reference energies of constituent atoms) / (total number of atoms). Write the results to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: columns: carbide (string), formation_energy_eV_per_atom (float)
- Scoring: scored by hidden verifier

### Step 7: Calculate density of states and N(E_F)
- Role: scored
- Action: Using the optimized structures, perform a non-self-consistent field calculation with a dense k-point mesh to compute the total density of states for each carbide. Extract the number of bonding electrons at the Fermi level per atom, N(E_F), in units of electrons/eV. Write the results to dos_n_ef.csv.
- Output file: `/app/outputs/dos_n_ef.csv`
- Format: csv
- Contract: columns: carbide (string), N_EF_electrons_per_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/formation_energies.csv`
- `/app/outputs/dos_n_ef.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Binding energy per atom for each carbide. The checker compares each value to the paper-reported gold within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `carbide`, `binding_energy_eV_per_atom`
  - `units`:
    - `binding_energy_eV_per_atom`: eV/atom

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation energy per atom for each carbide. The checker compares each value to the paper-reported gold within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `carbide`, `formation_energy_eV_per_atom`
  - `units`:
    - `formation_energy_eV_per_atom`: eV/atom

### dos_n_ef.csv
- path: `/app/outputs/dos_n_ef.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: N(E_F) per atom for each carbide. The checker compares each value to the paper-reported gold within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `carbide`, `N_EF_electrons_per_eV`
  - `units`:
    - `N_EF_electrons_per_eV`: electrons/eV

Notes: All three scored outputs are CSV files with identical row structure; each row corresponds to one carbide (Fe3C, Fe2C, Fe5C2, NbC). The checker also verifies ordering: NbC must have the most negative formation energy, and Fe2C must have a positive formation energy. Process-step evidence files are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "carbide",
          "binding_energy_eV_per_atom"
        ],
        "units": {
          "binding_energy_eV_per_atom": "eV/atom"
        }
      },
      "description": "Binding energy per atom for each carbide. The checker compares each value to the paper-reported gold within a hidden tolerance."
    },
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "carbide",
          "formation_energy_eV_per_atom"
        ],
        "units": {
          "formation_energy_eV_per_atom": "eV/atom"
        }
      },
      "description": "Formation energy per atom for each carbide. The checker compares each value to the paper-reported gold within a hidden tolerance."
    },
    {
      "file": "dos_n_ef.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "carbide",
          "N_EF_electrons_per_eV"
        ],
        "units": {
          "N_EF_electrons_per_eV": "electrons/eV"
        }
      },
      "description": "N(E_F) per atom for each carbide. The checker compares each value to the paper-reported gold within a hidden tolerance."
    }
  ],
  "notes": "All three scored outputs are CSV files with identical row structure; each row corresponds to one carbide (Fe3C, Fe2C, Fe5C2, NbC). The checker also verifies ordering: NbC must have the most negative formation energy, and Fe2C must have a positive formation energy. Process-step evidence files are not scored."
}
```

## How you are scored
After you submit your output artifacts, a hidden verifier will independently evaluate your work. For each of the three scored CSV files (`binding_energies.csv`, `formation_energies.csv`, `dos_n_ef.csv`), the verifier compares the carbide-specific values you report against hidden reference values that are derived from the original computational study. The comparison uses tolerances that account for legitimate numerical differences arising from the use of a different DFT code, pseudopotential versions, and convergence settings. Additionally, the verifier checks that required ordering relationships among the four carbides (for example, which carbide must have the most negative formation energy and which must have a positive formation energy) are satisfied according to the expected physical pattern. The three artifact scores are combined with predefined weights to yield a final reward between 0 and 1. Simply reporting the published numbers without executing the workflow will not guarantee a high score, because the verifier may also perform cross-consistency checks among your submitted artifacts.
