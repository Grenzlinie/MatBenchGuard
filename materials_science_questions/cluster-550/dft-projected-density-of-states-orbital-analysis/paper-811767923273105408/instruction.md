# H2 Binding Energies and Occupation Numbers on Three-Coordinated Ti(III) Complexes

## Problem background
The Kubas interaction is a promising mechanism for enhancing hydrogen binding in lightweight storage materials by hybridization of metal d orbitals with H₂ states. Recent experiments have reported H₂ adsorption on three-coordinated Ti(III) complexes with benzyl ligands attached to a silica surface, raising the question of whether the benzyl group affects the binding and how many H₂ molecules can be accommodated. This task investigates, via first-principles DFT, how H₂ binds to two forms of a Ti(III) complex — one with a benzyl group (the decorated form) and one where the benzyl is released — and quantifies the resulting occupation numbers under practical temperature and pressure conditions.

## Approach
DFT calculations using the PBE-GGA functional and a plane-wave basis are performed on two molecular models: the benzyl-decorated Ti(III) complex (2SiH₃·2O·Ti·CH₂Ph) and a benzyl-released variant where the benzyl group is replaced by a hydrogen atom. After geometry optimization of both species, H₂ molecules are placed near the Ti center and the system is re‑optimized; the binding energy is computed as the total energy difference between the complex + H₂ and the separated fragments. This is repeated sequentially for up to two H₂ on the released complex to determine the maximum number of H₂ that can bind. The obtained raw DFT binding energies are then reduced by 25% to account for zero‑point vibrational effects. Using these corrected energies and the given H₂ chemical potentials, the grand partition function for multiple H₂ binding is applied to calculate the equilibrium occupation numbers at the two specified temperature–pressure conditions.

## Reproduction target
Compute the raw DFT binding energies (in eV) of: one H₂ on the benzyl‑decorated complex, one H₂ on the benzyl‑released complex, and two H₂ on the benzyl‑released complex (binding energy per H₂). Also determine the maximum number of H₂ molecules the released complex can bind. These results must be written to `/app/outputs/binding_energies.json` with keys: `decorated_1H2_binding_energy_eV`, `released_1H2_binding_energy_eV`, `released_2H2_binding_energy_per_H2_eV`, and `max_H2_released`. Next, take the raw binding energies for the released complex, reduce them by 25% for zero‑point effects, and use the grand partition function for multiple H₂ binding to calculate the equilibrium occupation numbers at two conditions: (i) 298 K (25 °C) and 60 atm, using μ(H₂) = −0.21 eV; (ii) 195 K (−78 °C) and 60 atm, using μ(H₂) = −0.10 eV. Write the results to `/app/outputs/occupation_numbers.json` with keys `occupation_25C_60atm` and `occupation_minus78C_60atm`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Geometry optimization of Ti complexes
- Role: process
- Action: Optimize the atomic structures of the benzyl-decorated Ti(III) complex (2SiH3·2O·Ti·CH2Ph) and the benzyl-released Ti(III) complex (benzyl group replaced by a hydrogen atom) using DFT with PBE-GGA and a plane-wave basis. Use a kinetic energy cutoff of 35 Ryd, relax atoms until Hellmann–Feynman forces are below 0.01 eV/Å, and separate periodic images by at least 10 Å. Save the final coordinates and total energies.
- Evidence: `/app/outputs/opt.log`

### Step 2: Calculate H2 binding energies
- Role: scored (load-bearing)
- Action: Using the optimized geometries from the previous step, perform DFT calculations to obtain the binding energies of H2 on both complexes. For the decorated complex, place one H2 molecule near the Ti atom, relax the H2 position, and compute the binding energy. For the released complex, sequentially add H2 molecules (up to two), relax each, and compute the binding energy per H2. Determine the maximum number of H2 molecules that can bind to the released complex. Write the results to /app/outputs/binding_energies.json with keys: decorated_1H2_binding_energy_eV, released_1H2_binding_energy_eV, released_2H2_binding_energy_per_H2_eV, max_H2_released.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"decorated_1H2_binding_energy_eV": "float", "released_1H2_binding_energy_eV": "float", "released_2H2_binding_energy_per_H2_eV": "float", "max_H2_released": "int"}
- Scoring: scored by hidden verifier

### Step 3: Calculate H2 occupation numbers
- Role: scored
- Action: Take the DFT binding energies for the benzyl-released complex from the previous step and reduce them by 25% to account for zero-point vibrational energy. Using the grand partition function for multiple H2 binding, compute the equilibrium occupation number of H2 molecules on the released complex at 298 K (25 °C) and 60 atm, and at 195 K (−78 °C) and 60 atm. The chemical potentials of H2 gas at these conditions are μ(298 K, 60 atm) = −0.21 eV and μ(195 K, 60 atm) = −0.10 eV. Write the results to /app/outputs/occupation_numbers.json with keys: occupation_25C_60atm, occupation_minus78C_60atm.
- Output file: `/app/outputs/occupation_numbers.json`
- Format: json
- Contract: {"occupation_25C_60atm": "float", "occupation_minus78C_60atm": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`
- `/app/outputs/occupation_numbers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT-calculated H2 binding energies (raw, without zero-point correction) on the benzyl-decorated and benzyl-released Ti(III) complexes, and the maximum number of H2 that can bind to the released complex.
- schema:
  - `type`: object
  - `required`:
    - `decorated_1H2_binding_energy_eV`: float
    - `released_1H2_binding_energy_eV`: float
    - `released_2H2_binding_energy_per_H2_eV`: float
    - `max_H2_released`: int
  - `units`:
    - `decorated_1H2_binding_energy_eV`: eV
    - `released_1H2_binding_energy_eV`: eV
    - `released_2H2_binding_energy_per_H2_eV`: eV
    - `max_H2_released`: integer

### occupation_numbers.json
- path: `/app/outputs/occupation_numbers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium H2 occupation numbers on the benzyl-released Ti(III) complex at 298 K, 60 atm and 195 K, 60 atm, computed from the DFT binding energies reduced by 25% and using the grand partition function.
- schema:
  - `type`: object
  - `required`:
    - `occupation_25C_60atm`: float
    - `occupation_minus78C_60atm`: float
  - `units`:
    - `occupation_25C_60atm`: dimensionless
    - `occupation_minus78C_60atm`: dimensionless

Notes: The binding energies are raw DFT values; the occupation numbers are computed after reducing those binding energies by 25% for zero-point energy. The checker will compare both sets of numbers to the paper's reported values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "decorated_1H2_binding_energy_eV": "float",
          "released_1H2_binding_energy_eV": "float",
          "released_2H2_binding_energy_per_H2_eV": "float",
          "max_H2_released": "int"
        },
        "units": {
          "decorated_1H2_binding_energy_eV": "eV",
          "released_1H2_binding_energy_eV": "eV",
          "released_2H2_binding_energy_per_H2_eV": "eV",
          "max_H2_released": "integer"
        }
      },
      "description": "DFT-calculated H2 binding energies (raw, without zero-point correction) on the benzyl-decorated and benzyl-released Ti(III) complexes, and the maximum number of H2 that can bind to the released complex."
    },
    {
      "file": "occupation_numbers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "occupation_25C_60atm": "float",
          "occupation_minus78C_60atm": "float"
        },
        "units": {
          "occupation_25C_60atm": "dimensionless",
          "occupation_minus78C_60atm": "dimensionless"
        }
      },
      "description": "Equilibrium H2 occupation numbers on the benzyl-released Ti(III) complex at 298 K, 60 atm and 195 K, 60 atm, computed from the DFT binding energies reduced by 25% and using the grand partition function."
    }
  ],
  "notes": "The binding energies are raw DFT values; the occupation numbers are computed after reducing those binding energies by 25% for zero-point energy. The checker will compare both sets of numbers to the paper's reported values with tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that checks each scored output file independently. For `binding_energies.json`, the verifier compares your computed binding energies and the maximum H₂ count to reference values (derived from the paper) within acceptable tolerances. For `occupation_numbers.json`, the verifier uses your submitted released‑complex binding energies (after the zero‑point reduction) to recompute the occupation numbers and compares them to reference values. The overall reward is a weighted combination of these scores. Simply reporting numbers without performing the DFT calculations and subsequent analysis is not sufficient; the verifier checks that the pipeline has been executed and that the outputs are physically plausible and consistent. No exact target values or tolerances are revealed.
