# Stability and optical properties of (CN)Si split-interstitial in Si via DFT

## Problem background
Point defects in silicon are promising for quantum information science, but the widely studied T center, (CCH)Si, suffers from sensitivity to hydrogen. This work investigates a carbon‑nitrogen (CN) complex as a hydrogen‑free alternative. The CN complex is isoelectronic to the T center, offering similar electronic structure and potential for single‑photon emission. The goal of this task is to computationally assess the thermodynamic stability, electronic structure, and optical properties of the (CN)Si split‑interstitial configuration using first‑principles density functional theory (DFT). Specifically, the following key quantities must be determined: the defect’s stability against decomposition, the migration barrier of its most mobile constituent, the Debye‑Waller factor, the zero‑phonon line energy in the dilute limit, and the associated radiative lifetime.

## Approach
The core methodology is hybrid DFT with projector‑augmented wave pseudopotentials, using an open‑source plane‑wave code (e.g., Quantum ESPRESSO). First, the equilibrium lattice constant and band gap of bulk Si are obtained with the HSE functional. Next, defect geometries are relaxed in a 512‑atom supercell (4×4×4 conventional cubic cells) with Γ‑point sampling for the neutral charge states of (CN)Si, C_Si, and (NSi)Si. Formation energies are computed from the total energies using chemical potentials derived from bulk Si, diamond, and an N2 molecule, and a finite‑size correction for charged defects. The charge transition level between (CN)Si^0 and (CN)Si^-1 is extracted from the formation energy versus Fermi level curves.

The decomposition stability is evaluated by comparing formation energies for the lowest‑energy product channel, (CN)Si^0 → C_Si^0 + (NSi)Si^0. The migration barrier of (NSi)Si^0 is obtained via the climbing‑image nudged elastic band method.

Excited‑state properties are modelled with the ΔSCF constrained‑occupation approach, creating a localized‑electron exciton. A one‑dimensional configuration‑coordinate curve in the ground state around the excited‑state equilibrium yields the relaxation energy and effective phonon frequency, from which the Huang‑Rhys factor and Debye‑Waller factor are derived.

The zero‑phonon line (ZPL) energy is the total‑energy difference between the excited and ground states. Due to the extended nature of the hydrogenic hole, ZPL values are computed for three supercell sizes (216, 512, and 1000 atoms) using single‑shot PBE0 on HSE‑relaxed geometries. A linear extrapolation of the ZPL against inverse supercell volume provides the dilute‑limit value.

For the radiative lifetime, the ground‑state transition dipole moment is computed for the three supercells, then scaled to the dilute limit using a hydrogenic‑envelope factor derived from the Si heavy‑hole effective mass and dielectric constant. The lifetime is obtained from the Weisskopf‑Wigner formula using the extrapolated ZPL and the scaled transition dipole moment.

## Reproduction target
Reproduce the following computationally determined properties of the (CN)Si defect in silicon, and write them into the two JSON output files specified in the Workflow steps:

- **Step 1** (`step_01_bulk_and_defect_formation.json`): the HSE bulk lattice constant and band gap of Si; the formation energies of (CN)Si^0, C_Si^0, and (NSi)Si^0 in a 512‑atom supercell; and the 0/‑1 charge transition level for (CN)Si.

- **Step 2** (`step_02_main_results.json`): the decomposition energy for the lowest‑energy channel ((CN)Si^0 → C_Si^0 + (NSi)Si^0); the migration barrier of (NSi)Si^0; the Debye‑Waller factor (in percent); ZPL energies for supercells of 216, 512, and 1000 atoms computed with single‑shot PBE0, and the dilute‑limit extrapolated ZPL; and the radiative lifetime of the ZPL transition.

All values must be computed from first principles using an open‑source DFT code with standard PAW pseudopotentials and hybrid functionals (HSE and PBE0). The target is a full computational reproduction of the pipeline, not a match to any externally supplied reference numbers.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PAW pseudopotentials (efficiency) for Si, C, N, H: https://www.materialscloud.org/discover/sssp/table/efficiency
- Python packages: numpy, scipy, matplotlib: numpy scipy matplotlib

## Workflow steps

### Step 1: Bulk Si and defect formation energies
- Role: scored (load-bearing)
- Action: Calculate the HSE bulk lattice constant and band gap of Si. Then, using a 512-atom supercell (4x4x4 conventional cells) with Γ-point sampling, relax the geometries of (CN)Si^0, C_Si^0, and (NSi)Si^0. Compute their formation energies using the standard formula with chemical potentials from bulk Si, diamond, and N2. Determine the charge transition level between (CN)Si^0 and (CN)Si^-1 from the formation-energy curves. Output the values in step_01_bulk_and_defect_formation.json.
- Output file: `/app/outputs/step_01_bulk_and_defect_formation.json`
- Format: json
- Contract: {"bulk_lattice_constant_A": <float>, "bulk_band_gap_eV": <float>, "defect_formation_energies": {"(CN)_Si_0": <float>, "C_Si_0": <float>, "(NSi)_Si_0": <float>}, "charge_transition_levels": {"(CN)_Si_0_to_minus1": <float>}}
- Scoring: scored by hidden verifier

### Step 2: Main results for (CN)Si
- Role: scored (load-bearing)
- Action: Using the relaxed structures from step 01, perform the following computations: (a) decomposition energy: compute ΔE^f for (CN)Si^0 → C_Si^0 + (NSi)Si^0. (b) migration barrier: calculate the CI-NEB barrier for (NSi)Si^0 migration. (c) Huang-Rhys/DW factor: perform a configurational-coordinate scan in the ground state around the equilibrium geometry of the excited state (obtained via ΔSCF with a localized-electron exciton) to extract the relaxation energy Er and phonon frequency Ω, then compute S = Er/(ħΩ) and DW factor = exp(-S). (d) Zero-phonon line: compute ZPL energies (excited-state minus ground-state total energies) for (CN)Si using supercells of 216, 512, and 1000 atoms, employing single-shot PBE0 on HSE-relaxed geometries; extrapolate to the dilute limit by a linear fit in inverse volume. (e) Radiative lifetime: calculate the ground-state transition dipole moment μ0 for the three supercell sizes, scale to the dilute limit using the hydrogenic-envelope factor t = V/[π(a0*)^3] with a0* derived from the Si heavy-hole mass and dielectric constant, then compute τ via the Weisskopf-Wigner formula using the extrapolated ZPL and scaled |μ|^2. Output all quantities in step_02_main_results.json.
- Output file: `/app/outputs/step_02_main_results.json`
- Format: json
- Contract: {"decomposition_energy_eV": <float>, "migration_barrier_eV": <float>, "dW_factor_percent": <float>, "zpl_values_meV": {"supercell_216": <float>, "supercell_512": <float>, "supercell_1000": <float>}, "extrapolated_zpl_meV": <float>, "radiative_lifetime_us": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bulk_and_defect_formation.json`
- `/app/outputs/step_02_main_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bulk_and_defect_formation.json
- path: `/app/outputs/step_01_bulk_and_defect_formation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk Si lattice constant and HSE band gap, formation energies of (CN)Si^0, C_Si^0, and (NSi)Si^0, and the 0/-1 charge transition level of (CN)Si.
- schema:
  - `type`: object
  - `required`: `bulk_lattice_constant_A`, `bulk_band_gap_eV`, `defect_formation_energies`, `charge_transition_levels`
  - `properties`:
    - `bulk_lattice_constant_A`:
      - `type`: number
    - `bulk_band_gap_eV`:
      - `type`: number
    - `defect_formation_energies`:
      - `type`: object
      - `required`: `(CN)_Si_0`, `C_Si_0`, `(NSi)_Si_0`
      - `properties`:
        - `(CN)_Si_0`:
          - `type`: number
        - `C_Si_0`:
          - `type`: number
        - `(NSi)_Si_0`:
          - `type`: number
    - `charge_transition_levels`:
      - `type`: object
      - `required`: `(CN)_Si_0_to_minus1`
      - `properties`:
        - `(CN)_Si_0_to_minus1`:
          - `type`: number

### step_02_main_results.json
- path: `/app/outputs/step_02_main_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Key reproduced properties: decomposition energy of (CN)Si^0, migration barrier of (NSi)Si^0, Debye-Waller factor, ZPL energies for three supercell sizes, the dilute-limit extrapolated ZPL, and the radiative lifetime.
- schema:
  - `type`: object
  - `required`: `decomposition_energy_eV`, `migration_barrier_eV`, `dW_factor_percent`, `zpl_values_meV`, `extrapolated_zpl_meV`, `radiative_lifetime_us`
  - `properties`:
    - `decomposition_energy_eV`:
      - `type`: number
    - `migration_barrier_eV`:
      - `type`: number
    - `dW_factor_percent`:
      - `type`: number
    - `zpl_values_meV`:
      - `type`: object
      - `required`: `supercell_216`, `supercell_512`, `supercell_1000`
      - `properties`:
        - `supercell_216`:
          - `type`: number
        - `supercell_512`:
          - `type`: number
        - `supercell_1000`:
          - `type`: number
    - `extrapolated_zpl_meV`:
      - `type`: number
    - `radiative_lifetime_us`:
      - `type`: number

Notes: All values are compared to paper-reported gold with appropriate tolerances (hidden). The checker reads both JSON files and compares each field; reward is the fraction of comparisons within tolerance. The solving agent must perform the full DFT workflow; guessing the values is possible but the task is designed to encourage honest reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bulk_and_defect_formation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "bulk_lattice_constant_A",
          "bulk_band_gap_eV",
          "defect_formation_energies",
          "charge_transition_levels"
        ],
        "properties": {
          "bulk_lattice_constant_A": {
            "type": "number"
          },
          "bulk_band_gap_eV": {
            "type": "number"
          },
          "defect_formation_energies": {
            "type": "object",
            "required": [
              "(CN)_Si_0",
              "C_Si_0",
              "(NSi)_Si_0"
            ],
            "properties": {
              "(CN)_Si_0": {
                "type": "number"
              },
              "C_Si_0": {
                "type": "number"
              },
              "(NSi)_Si_0": {
                "type": "number"
              }
            }
          },
          "charge_transition_levels": {
            "type": "object",
            "required": [
              "(CN)_Si_0_to_minus1"
            ],
            "properties": {
              "(CN)_Si_0_to_minus1": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Bulk Si lattice constant and HSE band gap, formation energies of (CN)Si^0, C_Si^0, and (NSi)Si^0, and the 0/-1 charge transition level of (CN)Si."
    },
    {
      "file": "step_02_main_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "decomposition_energy_eV",
          "migration_barrier_eV",
          "dW_factor_percent",
          "zpl_values_meV",
          "extrapolated_zpl_meV",
          "radiative_lifetime_us"
        ],
        "properties": {
          "decomposition_energy_eV": {
            "type": "number"
          },
          "migration_barrier_eV": {
            "type": "number"
          },
          "dW_factor_percent": {
            "type": "number"
          },
          "zpl_values_meV": {
            "type": "object",
            "required": [
              "supercell_216",
              "supercell_512",
              "supercell_1000"
            ],
            "properties": {
              "supercell_216": {
                "type": "number"
              },
              "supercell_512": {
                "type": "number"
              },
              "supercell_1000": {
                "type": "number"
              }
            }
          },
          "extrapolated_zpl_meV": {
            "type": "number"
          },
          "radiative_lifetime_us": {
            "type": "number"
          }
        }
      },
      "description": "Key reproduced properties: decomposition energy of (CN)Si^0, migration barrier of (NSi)Si^0, Debye-Waller factor, ZPL energies for three supercell sizes, the dilute-limit extrapolated ZPL, and the radiative lifetime."
    }
  ],
  "notes": "All values are compared to paper-reported gold with appropriate tolerances (hidden). The checker reads both JSON files and compares each field; reward is the fraction of comparisons within tolerance. The solving agent must perform the full DFT workflow; guessing the values is possible but the task is designed to encourage honest reproduction."
}
```

## How you are scored
A hidden verifier reads both JSON output files and independently scores each step’s artifact. For each quantity listed in the output contract, the verifier compares your computed value to a hidden reference value using appropriate tolerances. The final reward is the fraction of comparisons that fall within the allowed tolerance. To earn a high score you must faithfully execute the DFT workflow and produce physically meaningful results; simply hard‑coding known literature values without performing the calculations will be detected and penalised. The tolerances are set to accommodate differences between DFT implementations, pseudopotentials, and numerical settings, so a correct implementation of the described methodology will score well.
