# Hydration State Stability of Na-Exchanged Montmorillonite from DFT Thermodynamics

## Problem background
Na-exchanged montmorillonite is a swelling 2:1 clay mineral whose hydration and associated dielectric properties are controlled by the chemical potential of Na and water vapour. Understanding the atomic-scale structure of the water interlayer and its relative dielectric permittivity is critical for geotechnical, sensor, and materials science applications. The challenge is to determine, from first-principles simulations, how discrete water layers form at two different Na surface charge densities (−0.086 C/m² and −0.172 C/m²) and to compute the resulting hydration-state stability at realistic temperature and humidity conditions.

## Approach
Construct two periodic supercell models of Na-exchanged montmorillonite corresponding to low and high Na content. For each model, perform density functional theory (DFT) calculations using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation with a plane-wave basis, as implemented in Quantum ESPRESSO, for a series of interlayer water coverages ranging from the dry case up to three discrete water layers. From the total energies and the equilibrium basal spacings, compute the adsorption energy per water molecule, the relative dielectric permittivity of the interlayer water via a plate capacitor model using the fixed surface charge density, and the grandcanonical potential as a function of water chemical potential. Convert the chemical potential axis to a temperature–pressure phase diagram via the ideal-gas approximation to identify the stable hydration state at ambient conditions (298 K, ~50% relative humidity) for each Na content. The pipeline is entirely computational; no external experimental data are required beyond the publicly specified crystal structure and pseudopotentials.

## Reproduction target
Produce three scored artifacts: (1) a JSON file containing the DFT total energies and layer thicknesses for all water coverages in both the low-Na and high-Na systems, together with the gas-phase water reference energy; (2) a JSON file with the computed relative dielectric permittivity of the water interlayer for each water coverage; (3) a JSON file with the grandcanonical potential and the identified stable hydration state (1W or 2W) at ambient conditions for each Na content. The verifier will assess relative trends and ordering in the energies and permittivities, and the correct identification of the stable state at the given ambient conditions.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- Pseudopotentials (Si, Al, Mg, O, H, Na): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct the two Na-exchanged montmorillonite supercells: low-Na [Na1(Si16)(Al7Mg1)O40(OH)8] and high-Na [Na2(Si16)(Al6Mg2)O40(OH)8] with trans-vacant C2/m symmetry, lattice constants a0=5.18 Å, b0=8.98 Å, and appropriate c-axis spacing. Generate initial configurations for water coverages n = 0, 3, 4, 8, 11, 14 by placing water molecules in the interlayer.
- Evidence: `/app/outputs/supercells.xyz`

### Step 2: DFT total energy calculations
- Role: scored (load-bearing)
- Action: For each supercell and each water coverage (n = 0, 3, 4, 8, 11, 14), perform DFT geometry optimization and static total-energy calculation using Quantum ESPRESSO with PBE pseudopotentials. Extract total energy E_n (Hartree) and layer thickness d_layer (Å) for each configuration, and the total energy of a gas-phase water molecule E_H2O. Collect results.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: {"low_Na": [{"n": int, "E_n_hartree": float, "d_layer_A": float}], "high_Na": [...], "E_H2O_hartree": float}
- Scoring: scored by hidden verifier

### Step 3: Dielectric permittivity calculation
- Role: scored
- Action: From the layer thicknesses in total_energies.json, compute the relative dielectric permittivity ε_layer for each water coverage using the plate capacitor model: ε_layer = (Q_layer * d_layer) / (ε0 * A), where Q_layer = surface charge density × A, A = 2 × a0 × b0, ε0 = 8.8541878128e-12 F/m. Use surface charge densities -0.086 C/m² for low-Na and -0.172 C/m² for high-Na.
- Output file: `/app/outputs/dielectric_permittivity.json`
- Format: json
- Contract: {"low_Na": [{"n": int, "epsilon_layer": float}], "high_Na": [...]}
- Scoring: scored by hidden verifier

### Step 4: Ab initio thermodynamics phase diagrams
- Role: scored
- Action: Using total energies from total_energies.json and gas-phase water energy E_H2O, compute grandcanonical potential Ω = E_n - n * μ(H2O) for each coverage. Determine stable hydration state at ambient conditions (T=298 K, relative humidity ~50%) by relating μ(H2O) to temperature and pressure via ideal gas approximation. Output Ω values and identified stable states.
- Output file: `/app/outputs/phase_diagram.json`
- Format: json
- Contract: {"low_Na": {"stable_state": "1W", "Omega_minimizer": {}}, "high_Na": {"stable_state": "2W", ...}, "conditions": {"T_K": 298, "RH_percent": 50}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/dielectric_permittivity.json`
- `/app/outputs/phase_diagram.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Total energies and layer thicknesses for all water coverages in both low-Na and high-Na systems, plus the gas-phase water reference energy.
- schema:
  - `type`: object
  - `required`:
    - `low_Na`: array of objects with n (int), E_n_hartree (float), d_layer_A (float)
    - `high_Na`: array of objects with n (int), E_n_hartree (float), d_layer_A (float)
    - `E_H2O_hartree`: float
  - `items`:
    - `n`: int
    - `E_n_hartree`: float
    - `d_layer_A`: float

### dielectric_permittivity.json
- path: `/app/outputs/dielectric_permittivity.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Relative dielectric permittivity of the water interlayer computed from the plate capacitor model.
- schema:
  - `type`: object
  - `required`:
    - `low_Na`: array of objects with n (int) and epsilon_layer (float)
    - `high_Na`: array of objects with n (int) and epsilon_layer (float)
  - `items`:
    - `n`: int
    - `epsilon_layer`: float

### phase_diagram.json
- path: `/app/outputs/phase_diagram.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic phase diagram data: the stable hydration state (1W/2W) at ambient conditions and the grandcanonical potential minimizer for both systems.
- schema:
  - `type`: object
  - `required`:
    - `low_Na`: object with stable_state (string) and Omega_minimizer (object)
    - `high_Na`: object with stable_state (string) and Omega_minimizer (object)
    - `conditions`: object with T_K (float) and RH_percent (float)

Notes: Scoring is based on relative trends and ordering (T3 structural) for total_energies and dielectric_permittivity, and on correct identification of the stable state (reference match) for phase_diagram. No exact numerical match with the paper's VASP results is required due to DFT toolchain variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "low_Na": "array of objects with n (int), E_n_hartree (float), d_layer_A (float)",
          "high_Na": "array of objects with n (int), E_n_hartree (float), d_layer_A (float)",
          "E_H2O_hartree": "float"
        },
        "items": {
          "n": "int",
          "E_n_hartree": "float",
          "d_layer_A": "float"
        }
      },
      "description": "Total energies and layer thicknesses for all water coverages in both low-Na and high-Na systems, plus the gas-phase water reference energy."
    },
    {
      "file": "dielectric_permittivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "low_Na": "array of objects with n (int) and epsilon_layer (float)",
          "high_Na": "array of objects with n (int) and epsilon_layer (float)"
        },
        "items": {
          "n": "int",
          "epsilon_layer": "float"
        }
      },
      "description": "Relative dielectric permittivity of the water interlayer computed from the plate capacitor model."
    },
    {
      "file": "phase_diagram.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "low_Na": "object with stable_state (string) and Omega_minimizer (object)",
          "high_Na": "object with stable_state (string) and Omega_minimizer (object)",
          "conditions": "object with T_K (float) and RH_percent (float)"
        }
      },
      "description": "Thermodynamic phase diagram data: the stable hydration state (1W/2W) at ambient conditions and the grandcanonical potential minimizer for both systems."
    }
  ],
  "notes": "Scoring is based on relative trends and ordering (T3 structural) for total_energies and dielectric_permittivity, and on correct identification of the stable state (reference match) for phase_diagram. No exact numerical match with the paper's VASP results is required due to DFT toolchain variations."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier. Each workflow artifact is checked independently: (a) the total energies and layer thicknesses are inspected for physical ordering and consistency with the discrete water-layer model; (b) the dielectric permittivities are checked for the correct relative ordering between the two Na systems at comparable water coverages; (c) the phase diagram output is checked that the stable state at the specified ambient conditions matches the expected hydration state and that the dehydration trend follows the Na chemical potential. The verifier combines these checks into a single overall score in [0, 1]. The exact numerical values from the paper are not required—only the correct qualitative trends and the correct stable state identification are needed.
