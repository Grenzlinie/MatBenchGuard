# Electronic Structure and Bader Charge Analysis of SrFeAsF and CaFeAsF

## Problem background
The discovery of iron-based superconductors has sparked intense research into layered pnictide materials. Among them, fluorine-containing four-component phases AFeAsF (A = Sr, Ca) have emerged as parent compounds for a new class of oxygen-free iron-based superconductors. These compounds crystallize in a tetragonal ZrCuSiAs-type structure (space group P4/nmm), consisting of alternating [AF] and [FeAs] layers along the c-axis, forming a quasi-two-dimensional network. A detailed understanding of their electronic band structure, density of electronic states, charge distribution, and the nature of interatomic bonding is essential to evaluate their potential for superconductivity and to guide future doping strategies. First-principles calculations can provide these properties, revealing the electronic structure that underlies the materials' behavior.

## Approach
We employ all-electron density functional theory (DFT) within the full-potential linearized augmented plane-wave (FP-LAPW) framework, using the open-source ELK code. The exchange-correlation energy is treated at the generalized gradient approximation (GGA) level with the Perdew-Burke-Ernzerhof (PBE) functional. For each compound, we first perform a full structural optimization (lattice parameters and internal atomic coordinates) in the nonmagnetic state. Using the optimized geometry, a self-consistent field (SCF) calculation with a dense k-point mesh provides converged charge density and Kohn-Sham eigenvalues. From the charge density, we perform a Bader charge analysis to obtain effective atomic charges and layer charges for the [AF] and [FeAs] slabs. We also compute the total and atom-projected (partial) density of states (DOS) on a fine k-mesh to extract the DOS at the Fermi level, including the Fe 3d and As contributions. Finally, we derive the electronic specific heat coefficient (Sommerfeld coefficient) and the Pauli paramagnetic susceptibility from the total DOS at the Fermi level using standard formulas. The workflow is carried out independently for SrFeAsF and CaFeAsF, and the results are assembled and compared.

## Reproduction target
Your goal is to produce a single JSON file, results.json, containing the following quantities computed from your DFT calculations for both SrFeAsF and CaFeAsF:
- optimized lattice parameters a and c (in Angstrom)
- optimized internal coordinates z_As and z_A (A = Sr or Ca)
- total DOS at the Fermi level (states/eV per formula unit)
- partial Fe 3d DOS at the Fermi level
- partial As DOS at the Fermi level
- Bader effective atomic charges (in electrons) for all atoms: A, Fe, As, F
- total charges (in electrons) of the [AF] and [FeAs] layers
- interlayer charge transfer ΔQ from [AF] to [FeAs] (electrons)
- Sommerfeld coefficient γ (mJ K⁻² mol⁻¹)
- Pauli paramagnetic susceptibility χ (10⁻⁴ emu/mol)
The JSON file must follow the schema described in the output contract exactly. The computed results reflect the electronic structure and bonding character of these compounds as obtained with the PBE-GGA functional.

## Assets

- ELK all-electron DFT code: https://elk.sourceforge.net/
- Bader charge analysis program: https://theory.cm.utexas.edu/henkelman/code/bader/
- Crystal structure parameters for SrFeAsF
- Crystal structure parameters for CaFeAsF

## Workflow steps

### Step 1: Prepare DFT input files
- Role: process
- Action: Generate ELK input files for SrFeAsF and CaFeAsF using the provided crystal structure parameters and the PBE-GGA exchange-correlation functional.
- Evidence: none

### Step 2: Geometry optimization
- Role: process
- Action: Run full structural relaxation (lattice parameters and atomic positions) for both SrFeAsF and CaFeAsF in the nonmagnetic state using DFT. Converge forces and stresses to tight tolerances.
- Evidence: `/app/outputs/step2_optimization.log`

### Step 3: Self-consistent field (SCF) calculation
- Role: process
- Action: Using the optimized structures, run a nonmagnetic SCF calculation with a dense k-mesh to obtain converged charge density and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/step3_scf.log`

### Step 4: Density of states (DOS) calculation
- Role: process
- Action: Compute the total and atom-projected (partial) DOS on a fine k-mesh. Extract the total DOS at the Fermi level, as well as the Fe 3d and As contributions.
- Evidence: `/app/outputs/step4_dos.dat`

### Step 5: Bader charge analysis
- Role: process
- Action: Apply Bader partitioning to the self-consistent charge density using a Bader analysis tool to obtain effective atomic charges for each atom. Compute total layer charges for the [AF] and [FeAs] layers by summing atomic charges.
- Evidence: `/app/outputs/step5_bader.out`

### Step 6: Assemble final results
- Role: scored (load-bearing)
- Action: Collect the optimized lattice constants, internal coordinates, DOS values at E_F, Bader atomic and layer charges, interlayer charge transfer ΔQ, Sommerfeld coefficient γ = (π²/3)k_B² N_tot(E_F), and Pauli susceptibility χ = μ_B² N_tot(E_F). Output a single JSON file containing all quantities for both SrFeAsF and CaFeAsF.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"SrFeAsF": {"lattice_a": float, "lattice_c": float, "z_As": float, "z_A": float, "Fe_d_DOS_EF": float, "As_DOS_EF": float, "total_DOS_EF": float, "atomic_charges": {"Sr": float, "Fe": float, "As": float, "F": float}, "layer_charges": {"AF": float, "FeAs": float}, "interlayer_charge_transfer": float, "gamma": float, "chi": float}, "CaFeAsF": {"lattice_a": float, "lattice_c": float, "z_As": float, "z_A": float, "Fe_d_DOS_EF": float, "As_DOS_EF": float, "total_DOS_EF": float, "atomic_charges": {"Ca": float, "Fe": float, "As": float, "F": float}, "layer_charges": {"AF": float, "FeAs": float}, "interlayer_charge_transfer": float, "gamma": float, "chi": float}}
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
- description: All computed electronic-structure and bonding quantities for SrFeAsF and CaFeAsF; includes lattice parameters, DOS at E_F, Bader charges, interlayer charge transfer, and derived γ and χ.
- schema:
  - `type`: object
  - `required`: `SrFeAsF`, `CaFeAsF`
  - `properties`:
    - `SrFeAsF`:
      - `type`: object
      - `required`: `lattice_a`, `lattice_c`, `z_As`, `z_A`, `Fe_d_DOS_EF`, `As_DOS_EF`, `total_DOS_EF`, `atomic_charges`, `layer_charges`, `interlayer_charge_transfer`, `gamma`, `chi`
      - `properties`:
        - `lattice_a`:
          - `type`: number
          - `unit`: Å
        - `lattice_c`:
          - `type`: number
          - `unit`: Å
        - `z_As`:
          - `type`: number
        - `z_A`:
          - `type`: number
        - `Fe_d_DOS_EF`:
          - `type`: number
          - `unit`: states/eV per formula unit
        - `As_DOS_EF`:
          - `type`: number
          - `unit`: states/eV per formula unit
        - `total_DOS_EF`:
          - `type`: number
          - `unit`: states/eV per formula unit
        - `atomic_charges`:
          - `type`: object
          - `required`: `Sr`, `Fe`, `As`, `F`
          - `properties`:
            - `Sr`:
              - `type`: number
              - `unit`: e
            - `Fe`:
              - `type`: number
              - `unit`: e
            - `As`:
              - `type`: number
              - `unit`: e
            - `F`:
              - `type`: number
              - `unit`: e
        - `layer_charges`:
          - `type`: object
          - `required`: `AF`, `FeAs`
          - `properties`:
            - `AF`:
              - `type`: number
              - `unit`: e
            - `FeAs`:
              - `type`: number
              - `unit`: e
        - `interlayer_charge_transfer`:
          - `type`: number
          - `unit`: e
        - `gamma`:
          - `type`: number
          - `unit`: mJ K^-2 mol^-1
        - `chi`:
          - `type`: number
          - `unit`: 10^-4 emu/mol
    - `CaFeAsF`:
      - `type`: object
      - `required`: `lattice_a`, `lattice_c`, `z_As`, `z_A`, `Fe_d_DOS_EF`, `As_DOS_EF`, `total_DOS_EF`, `atomic_charges`, `layer_charges`, `interlayer_charge_transfer`, `gamma`, `chi`
      - `properties`:
        - `lattice_a`:
          - `type`: number
          - `unit`: Å
        - `lattice_c`:
          - `type`: number
          - `unit`: Å
        - `z_As`:
          - `type`: number
        - `z_A`:
          - `type`: number
        - `Fe_d_DOS_EF`:
          - `type`: number
          - `unit`: states/eV per formula unit
        - `As_DOS_EF`:
          - `type`: number
          - `unit`: states/eV per formula unit
        - `total_DOS_EF`:
          - `type`: number
          - `unit`: states/eV per formula unit
        - `atomic_charges`:
          - `type`: object
          - `required`: `Ca`, `Fe`, `As`, `F`
          - `properties`:
            - `Ca`:
              - `type`: number
              - `unit`: e
            - `Fe`:
              - `type`: number
              - `unit`: e
            - `As`:
              - `type`: number
              - `unit`: e
            - `F`:
              - `type`: number
              - `unit`: e
        - `layer_charges`:
          - `type`: object
          - `required`: `AF`, `FeAs`
          - `properties`:
            - `AF`:
              - `type`: number
              - `unit`: e
            - `FeAs`:
              - `type`: number
              - `unit`: e
        - `interlayer_charge_transfer`:
          - `type`: number
          - `unit`: e
        - `gamma`:
          - `type`: number
          - `unit`: mJ K^-2 mol^-1
        - `chi`:
          - `type`: number
          - `unit`: 10^-4 emu/mol

Notes: The hidden checker compares each reported quantity to paper-reported values with tolerances appropriate for an independent DFT implementation. The scored quantities are those from Tables 1–3 of the paper.

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
        "required": [
          "SrFeAsF",
          "CaFeAsF"
        ],
        "properties": {
          "SrFeAsF": {
            "type": "object",
            "required": [
              "lattice_a",
              "lattice_c",
              "z_As",
              "z_A",
              "Fe_d_DOS_EF",
              "As_DOS_EF",
              "total_DOS_EF",
              "atomic_charges",
              "layer_charges",
              "interlayer_charge_transfer",
              "gamma",
              "chi"
            ],
            "properties": {
              "lattice_a": {
                "type": "number",
                "unit": "Å"
              },
              "lattice_c": {
                "type": "number",
                "unit": "Å"
              },
              "z_As": {
                "type": "number"
              },
              "z_A": {
                "type": "number"
              },
              "Fe_d_DOS_EF": {
                "type": "number",
                "unit": "states/eV per formula unit"
              },
              "As_DOS_EF": {
                "type": "number",
                "unit": "states/eV per formula unit"
              },
              "total_DOS_EF": {
                "type": "number",
                "unit": "states/eV per formula unit"
              },
              "atomic_charges": {
                "type": "object",
                "required": [
                  "Sr",
                  "Fe",
                  "As",
                  "F"
                ],
                "properties": {
                  "Sr": {
                    "type": "number",
                    "unit": "e"
                  },
                  "Fe": {
                    "type": "number",
                    "unit": "e"
                  },
                  "As": {
                    "type": "number",
                    "unit": "e"
                  },
                  "F": {
                    "type": "number",
                    "unit": "e"
                  }
                }
              },
              "layer_charges": {
                "type": "object",
                "required": [
                  "AF",
                  "FeAs"
                ],
                "properties": {
                  "AF": {
                    "type": "number",
                    "unit": "e"
                  },
                  "FeAs": {
                    "type": "number",
                    "unit": "e"
                  }
                }
              },
              "interlayer_charge_transfer": {
                "type": "number",
                "unit": "e"
              },
              "gamma": {
                "type": "number",
                "unit": "mJ K^-2 mol^-1"
              },
              "chi": {
                "type": "number",
                "unit": "10^-4 emu/mol"
              }
            }
          },
          "CaFeAsF": {
            "type": "object",
            "required": [
              "lattice_a",
              "lattice_c",
              "z_As",
              "z_A",
              "Fe_d_DOS_EF",
              "As_DOS_EF",
              "total_DOS_EF",
              "atomic_charges",
              "layer_charges",
              "interlayer_charge_transfer",
              "gamma",
              "chi"
            ],
            "properties": {
              "lattice_a": {
                "type": "number",
                "unit": "Å"
              },
              "lattice_c": {
                "type": "number",
                "unit": "Å"
              },
              "z_As": {
                "type": "number"
              },
              "z_A": {
                "type": "number"
              },
              "Fe_d_DOS_EF": {
                "type": "number",
                "unit": "states/eV per formula unit"
              },
              "As_DOS_EF": {
                "type": "number",
                "unit": "states/eV per formula unit"
              },
              "total_DOS_EF": {
                "type": "number",
                "unit": "states/eV per formula unit"
              },
              "atomic_charges": {
                "type": "object",
                "required": [
                  "Ca",
                  "Fe",
                  "As",
                  "F"
                ],
                "properties": {
                  "Ca": {
                    "type": "number",
                    "unit": "e"
                  },
                  "Fe": {
                    "type": "number",
                    "unit": "e"
                  },
                  "As": {
                    "type": "number",
                    "unit": "e"
                  },
                  "F": {
                    "type": "number",
                    "unit": "e"
                  }
                }
              },
              "layer_charges": {
                "type": "object",
                "required": [
                  "AF",
                  "FeAs"
                ],
                "properties": {
                  "AF": {
                    "type": "number",
                    "unit": "e"
                  },
                  "FeAs": {
                    "type": "number",
                    "unit": "e"
                  }
                }
              },
              "interlayer_charge_transfer": {
                "type": "number",
                "unit": "e"
              },
              "gamma": {
                "type": "number",
                "unit": "mJ K^-2 mol^-1"
              },
              "chi": {
                "type": "number",
                "unit": "10^-4 emu/mol"
              }
            }
          }
        }
      },
      "description": "All computed electronic-structure and bonding quantities for SrFeAsF and CaFeAsF; includes lattice parameters, DOS at E_F, Bader charges, interlayer charge transfer, and derived γ and χ."
    }
  ],
  "notes": "The hidden checker compares each reported quantity to paper-reported values with tolerances appropriate for an independent DFT implementation. The scored quantities are those from Tables 1–3 of the paper."
}
```

## How you are scored
A hidden verifier reads your results.json and extracts each target quantity. It compares your computed values to reference results obtained from independent first‑principles calculations of the same level of theory. The reward is the fraction of quantities that fall within acceptable agreement (within allowed tolerances) with the reference values; larger deviations lead to a lower reward. The verifier does not reveal its reference numbers or tolerances, so you must genuinely perform the full DFT workflow to produce accurate predictions. Simply copying numbers from a literature source or guessing will not yield a high score.
