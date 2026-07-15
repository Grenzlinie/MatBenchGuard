# DFT Formation Energy, Lattice Constants, and Elastic Properties of Doped AuSn4 Intermetallics

## Problem background
AuSn4-based intermetallic compounds form in microelectronic solder joints during the reflow process, especially when Ni/Au or ENEPIG surface finishes are used. Ni and Pd atoms can diffuse into the AuSn4 lattice and substitute for Au, potentially altering the mechanical, thermodynamic, and electronic properties of the compound. This task investigates how Ni and Pd substitution affects the structural stability, elastic moduli, Poisson's ratio, hardness, Debye temperature, and minimum thermal conductivity of orthorhombic AuSn4 (PdSn4-type, space group Aba2), using first-principles density functional theory (DFT). The goal is to compute these quantities for six specific compositions: AuSn4, Au0.75Ni0.25Sn4, Au0.5Ni0.5Sn4, Au0.75Pd0.25Sn4, Au0.5Pd0.5Sn4, and Au0.5Pd0.25Ni0.25Sn4, and thereby provide mechanistic insight into the embrittlement observed in such solder joints.

## Approach
The reproduction uses open‑source DFT code Quantum ESPRESSO with the Perdew–Burke–Ernzerhof (PBE) generalized‑gradient approximation and PAW pseudopotentials. The workflow consists of two main stages:
1. **Structure stability analysis** – Build candidate structures for all doped compositions by substituting Au atoms at the four nonequivalent crystallographic sites. Compute per‑atom total energies of the pure phases (fcc‑Au, fcc‑Ni, fcc‑Pd, β‑Sn) as references. Perform full variable‑cell geometry optimisation on every candidate to obtain equilibrium total energies and lattice constants. From these, compute the compositionally averaged formation energy ΔH per atom; for each doped composition select the most stable (lowest ΔH) substitution site.
2. **Elastic and thermodynamic characterisation** – For the six most stable structures, apply small strains to the equilibrium cell and extract the nine independent single‑crystal elastic stiffness constants Cij from the resulting energy–strain curves. Using the Voigt–Reuss–Hill averaging scheme, derive the polycrystalline bulk and shear moduli, Young's modulus, Poisson's ratio, and hardness. Finally, from the density and elastic wave velocities compute the Debye temperature θD and the minimum thermal conductivity κmin according to the standard Cahill–Pohl model.

## Reproduction target
Compute and report the following quantities for the six compositions: AuSn4, Au0.75Ni0.25Sn4, Au0.5Ni0.5Sn4, Au0.75Pd0.25Sn4, Au0.5Pd0.5Sn4, and Au0.5Pd0.25Ni0.25Sn4.
- Formation energy ΔH (kJ per mol of atoms), relaxed lattice constants a, b, c (Å), and cell volume (Å³).
- Nine independent elastic stiffness constants C11, C22, C33, C44, C55, C66, C12, C13, C23 (GPa).
- Polycrystalline elastic moduli: bulk modulus K, shear modulus G, Young's modulus E, Poisson's ratio ν, and hardness H (GPa).
- Debye temperature θD (K) and minimum thermal conductivity κmin (W·m⁻¹·K⁻¹).
The results must be written to the two JSON files described in Steps 4 and 6.

## Assets

- Quantum ESPRESSO (QE): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials for Au, Ni, Pd, Sn: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate candidate structures
- Role: process
- Action: Build initial crystal structures for AuSn4 and all doped compositions (Au_{1-x}Ni_xSn4, Au_{1-x}Pd_xSn4, and Au_{0.5}Pd_{0.25}Ni_{0.25}Sn4, with x=0.25, 0.5) by substituting Au atoms at the four crystallographic sites in the orthorhombic PdSn4-type prototype (space group Aba2, 4 Au and 16 Sn per conventional cell). Use the experimental lattice constants of AuSn4 as initial guess. Generate all distinct substitution configurations required to identify the most stable occupation for each composition.
- Evidence: none

### Step 2: Elemental reference total energies
- Role: process
- Action: Compute the per-atom total energies of the elemental reference phases: Au (fcc), Ni (fcc), Pd (fcc), and Sn (beta-Sn) using DFT with the PBE functional and a plane-wave pseudopotential approach. Perform these calculations with Quantum ESPRESSO and record the resulting energies for use in the formation energy formula.
- Evidence: `/app/outputs/elemental_energies.log`

### Step 3: DFT geometry optimizations
- Role: process
- Action: For every candidate structure from step01, run full DFT geometry optimization (relax cell shape and atomic positions) using Quantum ESPRESSO. Keep the same exchange-correlation functional and convergence criteria as in step02. Obtain the equilibrium total energies and relaxed lattice parameters (a, b, c) for all candidates.
- Evidence: `/app/outputs/optimization_logs`

### Step 4: Formation energies and stable structures
- Role: scored (load-bearing)
- Action: Using the total energies from step03 and the elemental reference energies from step02, compute the compositionally averaged formation energy ΔH per atom for each candidate structure via the formation energy formula. For each doped composition select the substitution site that yields the lowest (most negative) ΔH. Write a JSON file containing, for the six most stable compositions (AuSn4, Au0.75Ni0.25Sn4, Au0.5Ni0.5Sn4, Au0.75Pd0.25Sn4, Au0.5Pd0.5Sn4, Au0.5Pd0.25Ni0.25Sn4), the total energy per formula unit, relaxed lattice constants (a, b, c), cell volume, the computed ΔH, and the elemental reference energies that were used.
- Output file: `/app/outputs/formation_energies_and_lattice.json`
- Format: json
- Contract: {"compounds": [{"name": "string", "total_energy_per_fu": number, "total_energy_fu_units": "eV", "a": number, "b": number, "c": number, "volume": number, "delta_H_kJ_per_mol_atoms": number}], "elemental_references": {"Au_fcc": number, "Ni_fcc": number, "Pd_fcc": number, "Sn_beta": number}}
- Scoring: scored by hidden verifier

### Step 5: DFT elastic constant calculations
- Role: process
- Action: For each of the six stable structures determined in step04, perform DFT stress-strain calculations with Quantum ESPRESSO: apply a series of small strains to the equilibrium lattice, fit the resulting total energy changes, and extract the nine independent single-crystal elastic stiffness constants C11, C22, C33, C44, C55, C66, C12, C13, and C23 (in GPa).
- Evidence: `/app/outputs/elastic_logs`

### Step 6: Elastic and thermodynamic properties
- Role: scored
- Action: From the elastic constants obtained in step05, compute the polycrystalline elastic moduli (bulk modulus K, shear modulus G, Young's modulus E, Poisson's ratio ν) using the Voigt–Reuss–Hill averaging scheme. Derive hardness H from E and ν. Calculate the density ρ, the transverse and longitudinal elastic wave velocities, the average sound velocity, the Debye temperature θ_D, and the minimum thermal conductivity k_min. Write the complete set of elastic stiffnesses, polycrystalline moduli, Debye temperature, and k_min to a JSON file for the six stable compositions.
- Output file: `/app/outputs/elastic_and_thermodynamic.json`
- Format: json
- Contract: {"compounds": [{"name": "string", "C11": number, "C22": number, "C33": number, "C44": number, "C55": number, "C66": number, "C12": number, "C13": number, "C23": number, "Bulk_modulus_VRH": number, "Shear_modulus_VRH": number, "Young_modulus": number, "Poisson_ratio": number, "Hardness": number, "Debye_temperature": number, "kmin": number}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies_and_lattice.json`
- `/app/outputs/elastic_and_thermodynamic.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies_and_lattice.json
- path: `/app/outputs/formation_energies_and_lattice.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Formation energies computed from total energies and elemental references; lattice constants and cell volume compared to hidden reference. Checker recomputes ΔH with tolerance.
- schema:
  - `type`: object
  - `properties`:
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `total_energy_per_fu`, `total_energy_fu_units`, `a`, `b`, `c`, `volume`, `delta_H_kJ_per_mol_atoms`
        - `properties`:
          - `name`:
            - `type`: string
          - `total_energy_per_fu`:
            - `type`: number
            - `units`: eV
          - `total_energy_fu_units`:
            - `type`: string
            - `enum`: `eV`
          - `a`:
            - `type`: number
            - `units`: Angstrom
          - `b`:
            - `type`: number
            - `units`: Angstrom
          - `c`:
            - `type`: number
            - `units`: Angstrom
          - `volume`:
            - `type`: number
            - `units`: Ang^3
          - `delta_H_kJ_per_mol_atoms`:
            - `type`: number
            - `units`: kJ/mol atoms
    - `elemental_references`:
      - `type`: object
      - `required`: `Au_fcc`, `Ni_fcc`, `Pd_fcc`, `Sn_beta`
      - `properties`:
        - `Au_fcc`:
          - `type`: number
        - `Ni_fcc`:
          - `type`: number
        - `Pd_fcc`:
          - `type`: number
        - `Sn_beta`:
          - `type`: number

### elastic_and_thermodynamic.json
- path: `/app/outputs/elastic_and_thermodynamic.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness constants, polycrystalline moduli, Debye temperature, and minimum thermal conductivity. Values are compared to hidden gold with tolerance; relative trends between compositions are also checked.
- schema:
  - `type`: object
  - `properties`:
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `C11`, `C22`, `C33`, `C44`, `C55`, `C66`, `C12`, `C13`, `C23`, `Bulk_modulus_VRH`, `Shear_modulus_VRH`, `Young_modulus`, `Poisson_ratio`, `Hardness`, `Debye_temperature`, `kmin`
        - `properties`:
          - `name`:
            - `type`: string
          - `C11`:
            - `type`: number
            - `units`: GPa
          - `C22`:
            - `type`: number
            - `units`: GPa
          - `C33`:
            - `type`: number
            - `units`: GPa
          - `C44`:
            - `type`: number
            - `units`: GPa
          - `C55`:
            - `type`: number
            - `units`: GPa
          - `C66`:
            - `type`: number
            - `units`: GPa
          - `C12`:
            - `type`: number
            - `units`: GPa
          - `C13`:
            - `type`: number
            - `units`: GPa
          - `C23`:
            - `type`: number
            - `units`: GPa
          - `Bulk_modulus_VRH`:
            - `type`: number
            - `units`: GPa
          - `Shear_modulus_VRH`:
            - `type`: number
            - `units`: GPa
          - `Young_modulus`:
            - `type`: number
            - `units`: GPa
          - `Poisson_ratio`:
            - `type`: number
          - `Hardness`:
            - `type`: number
            - `units`: GPa
          - `Debye_temperature`:
            - `type`: number
            - `units`: K
          - `kmin`:
            - `type`: number
            - `units`: W/(m·K)

Notes: The checker recomputes the formation energies from the raw total energies and references provided by the agent (T1). For elastic and thermodynamic properties, a result-level comparison (T0) is used because full recomputation would require re-running DFT elastic constant calculations in the verifier sandbox, which is not feasible. Relative ordering checks (e.g., formation energy becoming more negative with doping, Poisson's ratio decreasing with Ni doping) are part of the scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies_and_lattice.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "total_energy_per_fu",
                "total_energy_fu_units",
                "a",
                "b",
                "c",
                "volume",
                "delta_H_kJ_per_mol_atoms"
              ],
              "properties": {
                "name": {
                  "type": "string"
                },
                "total_energy_per_fu": {
                  "type": "number",
                  "units": "eV"
                },
                "total_energy_fu_units": {
                  "type": "string",
                  "enum": [
                    "eV"
                  ]
                },
                "a": {
                  "type": "number",
                  "units": "Angstrom"
                },
                "b": {
                  "type": "number",
                  "units": "Angstrom"
                },
                "c": {
                  "type": "number",
                  "units": "Angstrom"
                },
                "volume": {
                  "type": "number",
                  "units": "Ang^3"
                },
                "delta_H_kJ_per_mol_atoms": {
                  "type": "number",
                  "units": "kJ/mol atoms"
                }
              }
            }
          },
          "elemental_references": {
            "type": "object",
            "required": [
              "Au_fcc",
              "Ni_fcc",
              "Pd_fcc",
              "Sn_beta"
            ],
            "properties": {
              "Au_fcc": {
                "type": "number"
              },
              "Ni_fcc": {
                "type": "number"
              },
              "Pd_fcc": {
                "type": "number"
              },
              "Sn_beta": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Formation energies computed from total energies and elemental references; lattice constants and cell volume compared to hidden reference. Checker recomputes ΔH with tolerance."
    },
    {
      "file": "elastic_and_thermodynamic.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "C11",
                "C22",
                "C33",
                "C44",
                "C55",
                "C66",
                "C12",
                "C13",
                "C23",
                "Bulk_modulus_VRH",
                "Shear_modulus_VRH",
                "Young_modulus",
                "Poisson_ratio",
                "Hardness",
                "Debye_temperature",
                "kmin"
              ],
              "properties": {
                "name": {
                  "type": "string"
                },
                "C11": {
                  "type": "number",
                  "units": "GPa"
                },
                "C22": {
                  "type": "number",
                  "units": "GPa"
                },
                "C33": {
                  "type": "number",
                  "units": "GPa"
                },
                "C44": {
                  "type": "number",
                  "units": "GPa"
                },
                "C55": {
                  "type": "number",
                  "units": "GPa"
                },
                "C66": {
                  "type": "number",
                  "units": "GPa"
                },
                "C12": {
                  "type": "number",
                  "units": "GPa"
                },
                "C13": {
                  "type": "number",
                  "units": "GPa"
                },
                "C23": {
                  "type": "number",
                  "units": "GPa"
                },
                "Bulk_modulus_VRH": {
                  "type": "number",
                  "units": "GPa"
                },
                "Shear_modulus_VRH": {
                  "type": "number",
                  "units": "GPa"
                },
                "Young_modulus": {
                  "type": "number",
                  "units": "GPa"
                },
                "Poisson_ratio": {
                  "type": "number"
                },
                "Hardness": {
                  "type": "number",
                  "units": "GPa"
                },
                "Debye_temperature": {
                  "type": "number",
                  "units": "K"
                },
                "kmin": {
                  "type": "number",
                  "units": "W/(m·K)"
                }
              }
            }
          }
        }
      },
      "description": "Elastic stiffness constants, polycrystalline moduli, Debye temperature, and minimum thermal conductivity. Values are compared to hidden gold with tolerance; relative trends between compositions are also checked."
    }
  ],
  "notes": "The checker recomputes the formation energies from the raw total energies and references provided by the agent (T1). For elastic and thermodynamic properties, a result-level comparison (T0) is used because full recomputation would require re-running DFT elastic constant calculations in the verifier sandbox, which is not feasible. Relative ordering checks (e.g., formation energy becoming more negative with doping, Poisson's ratio decreasing with Ni doping) are part of the scoring."
}
```

## How you are scored
A hidden verifier script independently scores your two JSON output files against concealed reference values. For `formation_energies_and_lattice.json`, the verifier recomputes ΔH from the raw total energies and elemental references you provide and compares the recomputed values to the hidden gold; lattice constants and volume are compared directly. For `elastic_and_thermodynamic.json`, each reported elastic modulus, Debye temperature, and κmin is compared to the hidden reference with tolerances that account for the use of a different DFT code. In addition, the verifier checks that the computed values exhibit internally consistent trends (e.g., monotonic changes in formation energy and elastic properties with doping fraction). All checks are combined into a single weighted reward. Supplying the paper’s published numbers without actually running the DFT calculations will not yield a high score.
