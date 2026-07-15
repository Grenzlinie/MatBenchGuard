# Thermodynamic Calculation of Equilibrium Potentials for Bi-Pd Intermetallics

## Problem background
In electrochemistry of binary alloy deposits, the presence of multiple anodic peaks on current-voltage curves can indicate the formation of intermetallic compounds (IMCs) on the electrode surface. Selective electrooxidation of one component from an IMC may produce an additional peak that is not observed for the pure metals. In a study of bismuth-palladium electrolytic deposits, an additional anodic peak was observed at +0.15 V vs Ag/AgCl. This task reproduces the thermodynamic calculation used to identify which Bi-Pd IMC is responsible for that peak. By computing mixing heats and equilibrium potential shifts for the candidate IMCs (Bi₂Pd, BiPd, BiPd₃) using regular‑solution theory, one can predict the bismuth oxidation potential in each compound and compare it to the experimental peak value.

## Approach
The thermodynamic analysis rests on the regular‑solution approximation, which relates the equilibrium potential shift of an electroactive component in an alloy to its mole fraction and the integral mixing heat (ΔH_m). The mixing heat is estimated from a pair‑interaction model that considers metallic radii, coordination numbers, and bond energies of Bi‑Bi, Pd‑Pd, and Bi‑Pd pairs. Because the Bi‑Pd bond energy is not tabulated, it is obtained from the Pauling equation. Once ΔH_m is calculated for each IMC, the equilibrium potential of pure bismuth in the electrolyte is computed using the Nernst equation, with the standard potential (0.06 V vs Ag/AgCl), concentration (4.8×10⁻⁴ M Bi(III)), and activity coefficient (0.99). The alloy equilibrium potential E_calc is then found by subtracting the potential shift ΔE from the pure bismuth potential. By comparing E_calc for Bi₂Pd, BiPd, and BiPd₃ to the experimentally observed peak at +0.15 V, one can identify the most likely IMC.

## Reproduction target
Compute ΔH_m, ΔE, and E_calc for the three intermetallics Bi₂Pd, BiPd, and BiPd₃. Write the results to a CSV file with columns: compound, mole_fraction_Bi, number_of_Bi_atoms, mixing_heat_J_per_mol, potential_shift_delta_E_V, and equilibrium_potential_E_calc_V. Based on the computed equilibrium potentials, determine which compound’s E_calc is closest to +0.15 V vs Ag/AgCl.

## Assets
No external datasets or models are needed. All physical constants (radii, bond energies, coordination number, standard potential, Nernst parameters) are listed in the workflow step. The computation can be performed with standard Python libraries (e.g., numpy).

## Workflow steps

### Step 1: Thermodynamic Calculation of IMC Potentials
- Role: scored (load-bearing)
- Action: Using the pair-interaction model with the formula ΔH_m = z_Bi · n_Bi · (r_Bi / r_Pd) · [ε_Bi-Pd − ε_Pd-Pd/2] − z_Bi · n_Bi · ε_Bi-Bi/2 and the regular-solution expression ΔE = (RT/(zF)) ln X_Bi − ((1−X_Bi)^2/(zF)) ΔH_m (with Faraday constant F=96485 C/mol, R=8.314 J/(mol·K), z=3 for Bi(III)/Bi), the provided atomic constants (metallic radii r_Bi=1.82 Å, r_Pd=1.37 Å; coordination number z_Bi=5; bond energies ε_Bi-Bi=200406 J/mol, ε_Pd-Pd=66416 J/mol; and the Bi-Pd binding energy calculated via the Pauling equation, ε_Bi-Pd=133420 J/mol), and T=298 K, compute the mixing heat ΔH_m and equilibrium potential shift ΔE for the three candidate intermetallics Bi2Pd, BiPd, BiPd3. Apply the Nernst equation (E°_Bi = 0.06 + (0.059/3) log10(...) with given c_Bi(III)=4.8×10⁻⁴ M, γ=0.99) to obtain the pure bismuth electrode potential E°_Bi, then compute the alloy equilibrium potential E_calc = E°_Bi − ΔE. Write the three results to a CSV file.
- Output file: `/app/outputs/step_01_thermo_calc_results.csv`
- Format: csv
- Contract: CSV with header: compound (string), mole_fraction_Bi (float), number_of_Bi_atoms (int), mixing_heat_J_per_mol (float), potential_shift_delta_E_V (float), equilibrium_potential_E_calc_V (float). Contains three rows for Bi2Pd, BiPd, BiPd3.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermo_calc_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermo_calc_results.csv
- path: `/app/outputs/step_01_thermo_calc_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the computed mixing heats, potential shifts, and equilibrium potentials for the three Bi-Pd intermetallic compounds (Bi2Pd, BiPd, BiPd3). The checker will compare the mixing_heat_J_per_mol and potential_shift_delta_E_V to reference values within tolerances, and verify that the equilibrium_potential_E_calc_V for Bi2Pd is the closest to +0.15 V among the three.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `mole_fraction_Bi`, `number_of_Bi_atoms`, `mixing_heat_J_per_mol`, `potential_shift_delta_E_V`, `equilibrium_potential_E_calc_V`
  - `units`:
    - `mixing_heat_J_per_mol`: J/mol
    - `potential_shift_delta_E_V`: V
    - `equilibrium_potential_E_calc_V`: V

Notes: This task reproduces only the thermodynamic calculation. All needed physical constants are stated in the public description. No external datasets or models are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermo_calc_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "mole_fraction_Bi",
          "number_of_Bi_atoms",
          "mixing_heat_J_per_mol",
          "potential_shift_delta_E_V",
          "equilibrium_potential_E_calc_V"
        ],
        "units": {
          "mixing_heat_J_per_mol": "J/mol",
          "potential_shift_delta_E_V": "V",
          "equilibrium_potential_E_calc_V": "V"
        }
      },
      "description": "CSV file containing the computed mixing heats, potential shifts, and equilibrium potentials for the three Bi-Pd intermetallic compounds (Bi2Pd, BiPd, BiPd3). The checker will compare the mixing_heat_J_per_mol and potential_shift_delta_E_V to reference values within tolerances, and verify that the equilibrium_potential_E_calc_V for Bi2Pd is the closest to +0.15 V among the three."
    }
  ],
  "notes": "This task reproduces only the thermodynamic calculation. All needed physical constants are stated in the public description. No external datasets or models are required."
}
```

## How you are scored
A hidden verifier will read your CSV file. It will recompute the mixing heat and potential shift from the provided formulas and compare your reported values to hidden reference values within set numerical tolerances. Additionally, it will assess whether the equilibrium potential of bismuth in one of the IMCs is the closest to +0.15 V among the three, supporting the compound identification. The final reward (a float between 0 and 1) will reflect the accuracy of your computed ΔH_m and ΔE and the correctness of this comparison.
