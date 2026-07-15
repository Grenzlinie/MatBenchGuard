# Extended Embedded-Atom Method (XEAM) Reproduction for Platinum

## Problem background
Platinum nanoparticles play a central role in catalysis, and understanding their behaviour requires accurate interatomic potentials that are transferable from bulk crystals to low-coordination environments such as surfaces and atomic clusters. The conventional embedded-atom method (EAM) is widely used for metals, but potentials fitted solely to bulk properties often perform poorly in non‑bulk settings. This task focuses on an extension of EAM—the extended embedded-atom method (XEAM)—that introduces an asymmetry‑sensitive correction to the embedding energy in order to better capture the energetics of under‑coordinated structures while preserving bulk properties. The agent will implement two candidate potentials, the original Cai–Ye EAM (CY‑EAM) and the corresponding CY‑XEAM2 potential, and compute a set of bulk, cluster, and surface properties for platinum to examine how the XEAM correction affects the predicted physical quantities.

## Approach
The XEAM scheme extends a standard EAM by defining an effective embedding energy that depends on a local asymmetry density, which measures the deviation from perfect symmetry around an atom. A multiplicative prefactor scales the embedding function; it equals 1 for fully symmetric bulk environments and deviates from 1 for configurations with broken symmetry, thereby adjusting the potential in clusters, surfaces, and other non‑bulk settings without changing the bulk limit.

The task proceeds by implementing two potentials for platinum:
- The baseline CY‑EAM (Cai–Ye EAM) with its published functional forms and parameters.
- The extended CY‑XEAM2 potential, obtained by adding the asymmetry correction to the same base EAM using three additional parameters (α, ε, k).

Both potentials must correctly compute total energies, forces, embedding energies, electron densities, pair potentials, and, for XEAM, the asymmetry density and effective embedding function. Once implemented, the following physical properties are evaluated for each potential:
(1) Bulk fcc platinum properties: equilibrium lattice constant, cohesive energy, unrelaxed vacancy formation energy, and elastic constants C11, C12, C44.
(2) Small cluster properties: relaxed binding energy per atom and average bond length for the dimer, trimer, and tetrahedron.
(3) Surface properties: clean (111) and (100) surface energies and the adatom diffusion barrier on the Pt(111) surface (computed from the energies at the fcc and saddle adsorption sites).

The results for the two potentials are reported side‑by‑side so that the automated verifier can later compare them against reference data and evaluate any required trends.

## Reproduction target
Implement the CY‑EAM and CY‑XEAM2 potentials for platinum using the provided functional forms and parameter sets. With the implemented potentials, compute the following quantities and report them in the three JSON files specified in the workflow steps:

- bulk_properties.json: for each potential, the equilibrium fcc lattice constant (Å), cohesive energy (eV/atom), unrelaxed vacancy formation energy (eV), and the three fcc elastic constants C11, C12, C44 (GPa).
- cluster_properties.json: for each potential, the relaxed binding energy per atom (eV/atom) and average bond length (Å) of the Pt dimer, trimer, and tetrahedron.
- surface_properties.json: for each potential, the (111) and (100) surface energies (eV/Å²) and the diffusion barrier of a single Pt adatom on the Pt(111) surface (eV).

All results must be obtained from the two potentials as implemented. The objective is to produce the numerical values that will be scrutinised by the hidden verifier.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- CY‑EAM functional form and parameters
- CY‑XEAM2 parameters

## Workflow steps

### Step 1: Implement CY‑EAM and CY‑XEAM2 potentials
- Role: process
- Action: Write code to implement the Cai‑Ye EAM (CY‑EAM) and the CY‑XEAM2 extended EAM potentials for platinum. The total energy, electron density, embedding function, pair potential, and the XEAM asymmetric density correction must be correctly computed. Verify correctness by checking energy and forces on a simple test configuration (e.g., a platinum dimer at the bulk nearest-neighbour distance).
- Evidence: none

### Step 2: Compute bulk properties
- Role: scored
- Action: Using the implemented potentials, compute for both CY‑EAM and CY‑XEAM2: (i) equilibrium fcc lattice constant and cohesive energy by relaxing the primitive cell; (ii) unrelaxed vacancy formation energy from a supercell with one atom removed; (iii) elastic constants C11, C12, C44. Report all values in a JSON file.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: Object with keys "CY‑EAM" and "CY‑XEAM2". Each value is an object with keys: "lattice_constant_A" (float, Å), "cohesive_energy_eV" (float, eV/atom), "vacancy_formation_energy_eV" (float, eV), "C11_GPa" (float), "C12_GPa" (float), "C44_GPa" (float).
- Scoring: scored by hidden verifier

### Step 3: Compute cluster properties
- Role: scored (load-bearing)
- Action: Relax the geometries of a platinum dimer, trimer, and tetrahedron using both potentials. For each cluster, extract the binding energy per atom and the average bond length. Report the results for both potentials in a JSON file.
- Output file: `/app/outputs/cluster_properties.json`
- Format: json
- Contract: Object with keys "CY‑EAM" and "CY‑XEAM2". Each value is an object with keys "dimer", "trimer", "tetrahedron". Each cluster object has keys: "bond_length_A" (float, Å) and "binding_energy_eV_per_atom" (float, eV/atom).
- Scoring: scored by hidden verifier

### Step 4: Compute surface properties
- Role: scored
- Action: For both potentials, calculate the clean (111) and (100) surface energies using slab models. Compute the diffusion barrier of a single platinum adatom on the Pt(111) surface by evaluating the total energy at the fcc and saddle adsorption sites. Report the results in a JSON file.
- Output file: `/app/outputs/surface_properties.json`
- Format: json
- Contract: Object with keys "CY‑EAM" and "CY‑XEAM2". Each value is an object with keys: "surface_energy_111_eV_per_A2" (float, eV/Å²), "surface_energy_100_eV_per_A2" (float, eV/Å²), "adatom_diffusion_barrier_eV" (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/cluster_properties.json`
- `/app/outputs/surface_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk fcc platinum properties for both CY‑EAM and CY‑XEAM2 potentials: lattice constant, cohesive energy, vacancy formation energy, and elastic constants C11, C12, C44.
- schema:
  - `type`: object
  - `required`: `CY-EAM`, `CY-XEAM2`
  - `items`:
    - `CY-EAM`:
      - `type`: object
      - `required`: `lattice_constant_A`, `cohesive_energy_eV`, `vacancy_formation_energy_eV`, `C11_GPa`, `C12_GPa`, `C44_GPa`
      - `units`:
        - `lattice_constant_A`: Angstrom
        - `cohesive_energy_eV`: eV/atom
        - `vacancy_formation_energy_eV`: eV
        - `C11_GPa`: GPa
        - `C12_GPa`: GPa
        - `C44_GPa`: GPa
    - `CY-XEAM2`:
      - `type`: object
      - `required`: `lattice_constant_A`, `cohesive_energy_eV`, `vacancy_formation_energy_eV`, `C11_GPa`, `C12_GPa`, `C44_GPa`
      - `units`:
        - `lattice_constant_A`: Angstrom
        - `cohesive_energy_eV`: eV/atom
        - `vacancy_formation_energy_eV`: eV
        - `C11_GPa`: GPa
        - `C12_GPa`: GPa
        - `C44_GPa`: GPa

### cluster_properties.json
- path: `/app/outputs/cluster_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed binding energies per atom and average bond lengths for Pt dimer, trimer, and tetrahedron, computed with CY‑EAM and CY‑XEAM2. Load‑bearing step that forces the potential implementation to be correct.
- schema:
  - `type`: object
  - `required`: `CY-EAM`, `CY-XEAM2`
  - `items`:
    - `CY-EAM`:
      - `type`: object
      - `required`: `dimer`, `trimer`, `tetrahedron`
      - `items`:
        - `dimer`:
          - `type`: object
          - `required`: `bond_length_A`, `binding_energy_eV_per_atom`
          - `units`:
            - `bond_length_A`: Angstrom
            - `binding_energy_eV_per_atom`: eV/atom
        - `trimer`:
          - `type`: object
          - `required`: `bond_length_A`, `binding_energy_eV_per_atom`
          - `units`:
            - `bond_length_A`: Angstrom
            - `binding_energy_eV_per_atom`: eV/atom
        - `tetrahedron`:
          - `type`: object
          - `required`: `bond_length_A`, `binding_energy_eV_per_atom`
          - `units`:
            - `bond_length_A`: Angstrom
            - `binding_energy_eV_per_atom`: eV/atom
    - `CY-XEAM2`:
      - `type`: object
      - `required`: `dimer`, `trimer`, `tetrahedron`
      - `items`:
        - `dimer`:
          - `type`: object
          - `required`: `bond_length_A`, `binding_energy_eV_per_atom`
          - `units`:
            - `bond_length_A`: Angstrom
            - `binding_energy_eV_per_atom`: eV/atom
        - `trimer`:
          - `type`: object
          - `required`: `bond_length_A`, `binding_energy_eV_per_atom`
          - `units`:
            - `bond_length_A`: Angstrom
            - `binding_energy_eV_per_atom`: eV/atom
        - `tetrahedron`:
          - `type`: object
          - `required`: `bond_length_A`, `binding_energy_eV_per_atom`
          - `units`:
            - `bond_length_A`: Angstrom
            - `binding_energy_eV_per_atom`: eV/atom

### surface_properties.json
- path: `/app/outputs/surface_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Surface energies of Pt(111) and Pt(100) and the adatom diffusion barrier on Pt(111) for both potentials.
- schema:
  - `type`: object
  - `required`: `CY-EAM`, `CY-XEAM2`
  - `items`:
    - `CY-EAM`:
      - `type`: object
      - `required`: `surface_energy_111_eV_per_A2`, `surface_energy_100_eV_per_A2`, `adatom_diffusion_barrier_eV`
      - `units`:
        - `surface_energy_111_eV_per_A2`: eV/Å²
        - `surface_energy_100_eV_per_A2`: eV/Å²
        - `adatom_diffusion_barrier_eV`: eV
    - `CY-XEAM2`:
      - `type`: object
      - `required`: `surface_energy_111_eV_per_A2`, `surface_energy_100_eV_per_A2`, `adatom_diffusion_barrier_eV`
      - `units`:
        - `surface_energy_111_eV_per_A2`: eV/Å²
        - `surface_energy_100_eV_per_A2`: eV/Å²
        - `adatom_diffusion_barrier_eV`: eV

Notes: The hidden checker compares each reported value to the paper's gold values within tolerances, and for the cluster and surface properties additionally verifies that the XEAM values are closer to the DFT/experimental reference than the corresponding EAM values, confirming the improvement that the paper claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CY-EAM",
          "CY-XEAM2"
        ],
        "items": {
          "CY-EAM": {
            "type": "object",
            "required": [
              "lattice_constant_A",
              "cohesive_energy_eV",
              "vacancy_formation_energy_eV",
              "C11_GPa",
              "C12_GPa",
              "C44_GPa"
            ],
            "units": {
              "lattice_constant_A": "Angstrom",
              "cohesive_energy_eV": "eV/atom",
              "vacancy_formation_energy_eV": "eV",
              "C11_GPa": "GPa",
              "C12_GPa": "GPa",
              "C44_GPa": "GPa"
            }
          },
          "CY-XEAM2": {
            "type": "object",
            "required": [
              "lattice_constant_A",
              "cohesive_energy_eV",
              "vacancy_formation_energy_eV",
              "C11_GPa",
              "C12_GPa",
              "C44_GPa"
            ],
            "units": {
              "lattice_constant_A": "Angstrom",
              "cohesive_energy_eV": "eV/atom",
              "vacancy_formation_energy_eV": "eV",
              "C11_GPa": "GPa",
              "C12_GPa": "GPa",
              "C44_GPa": "GPa"
            }
          }
        }
      },
      "description": "Bulk fcc platinum properties for both CY‑EAM and CY‑XEAM2 potentials: lattice constant, cohesive energy, vacancy formation energy, and elastic constants C11, C12, C44."
    },
    {
      "file": "cluster_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CY-EAM",
          "CY-XEAM2"
        ],
        "items": {
          "CY-EAM": {
            "type": "object",
            "required": [
              "dimer",
              "trimer",
              "tetrahedron"
            ],
            "items": {
              "dimer": {
                "type": "object",
                "required": [
                  "bond_length_A",
                  "binding_energy_eV_per_atom"
                ],
                "units": {
                  "bond_length_A": "Angstrom",
                  "binding_energy_eV_per_atom": "eV/atom"
                }
              },
              "trimer": {
                "type": "object",
                "required": [
                  "bond_length_A",
                  "binding_energy_eV_per_atom"
                ],
                "units": {
                  "bond_length_A": "Angstrom",
                  "binding_energy_eV_per_atom": "eV/atom"
                }
              },
              "tetrahedron": {
                "type": "object",
                "required": [
                  "bond_length_A",
                  "binding_energy_eV_per_atom"
                ],
                "units": {
                  "bond_length_A": "Angstrom",
                  "binding_energy_eV_per_atom": "eV/atom"
                }
              }
            }
          },
          "CY-XEAM2": {
            "type": "object",
            "required": [
              "dimer",
              "trimer",
              "tetrahedron"
            ],
            "items": {
              "dimer": {
                "type": "object",
                "required": [
                  "bond_length_A",
                  "binding_energy_eV_per_atom"
                ],
                "units": {
                  "bond_length_A": "Angstrom",
                  "binding_energy_eV_per_atom": "eV/atom"
                }
              },
              "trimer": {
                "type": "object",
                "required": [
                  "bond_length_A",
                  "binding_energy_eV_per_atom"
                ],
                "units": {
                  "bond_length_A": "Angstrom",
                  "binding_energy_eV_per_atom": "eV/atom"
                }
              },
              "tetrahedron": {
                "type": "object",
                "required": [
                  "bond_length_A",
                  "binding_energy_eV_per_atom"
                ],
                "units": {
                  "bond_length_A": "Angstrom",
                  "binding_energy_eV_per_atom": "eV/atom"
                }
              }
            }
          }
        }
      },
      "description": "Relaxed binding energies per atom and average bond lengths for Pt dimer, trimer, and tetrahedron, computed with CY‑EAM and CY‑XEAM2. Load‑bearing step that forces the potential implementation to be correct."
    },
    {
      "file": "surface_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CY-EAM",
          "CY-XEAM2"
        ],
        "items": {
          "CY-EAM": {
            "type": "object",
            "required": [
              "surface_energy_111_eV_per_A2",
              "surface_energy_100_eV_per_A2",
              "adatom_diffusion_barrier_eV"
            ],
            "units": {
              "surface_energy_111_eV_per_A2": "eV/Å²",
              "surface_energy_100_eV_per_A2": "eV/Å²",
              "adatom_diffusion_barrier_eV": "eV"
            }
          },
          "CY-XEAM2": {
            "type": "object",
            "required": [
              "surface_energy_111_eV_per_A2",
              "surface_energy_100_eV_per_A2",
              "adatom_diffusion_barrier_eV"
            ],
            "units": {
              "surface_energy_111_eV_per_A2": "eV/Å²",
              "surface_energy_100_eV_per_A2": "eV/Å²",
              "adatom_diffusion_barrier_eV": "eV"
            }
          }
        }
      },
      "description": "Surface energies of Pt(111) and Pt(100) and the adatom diffusion barrier on Pt(111) for both potentials."
    }
  ],
  "notes": "The hidden checker compares each reported value to the paper's gold values within tolerances, and for the cluster and surface properties additionally verifies that the XEAM values are closer to the DFT/experimental reference than the corresponding EAM values, confirming the improvement that the paper claims."
}
```

## How you are scored
A hidden, deterministic verifier will inspect the three output files (bulk_properties.json, cluster_properties.json, surface_properties.json) and compare each reported numerical value to independently determined reference targets. The verifier may also evaluate structural trends among the reported numbers. Each workflow stage contributes a weight to the overall reward, and the verifier combines the stage scores into a single final reward. Simply guessing or copying a set of numbers is not sufficient; your implementation must correctly compute the physical properties from the specified potentials, using appropriate atomistic simulation techniques and the functional forms and parameters provided in this instruction.
