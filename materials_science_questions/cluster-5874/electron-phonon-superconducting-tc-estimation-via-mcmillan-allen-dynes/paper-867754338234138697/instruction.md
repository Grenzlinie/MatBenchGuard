# Compute Superconducting Thermodynamic Parameters and Electron-Phonon Coupling from Specific-Heat Coefficients

## Problem background
In the study of superconductivity in MoTe₂ and its S-doped variant MoTe₁.₈S₀.₂, low-temperature specific-heat measurements provide the Sommerfeld coefficient γ (electronic contribution) and the lattice coefficient β. Together with the measured superconducting critical temperature Tc, these coefficients are used to derive the Debye temperature Θ_D, the electronic density of states at the Fermi level N(E_F), and the electron‑phonon coupling constant λ_ep. Reproducing these derived parameters helps clarify how doping influences the normal‑state properties and the superconducting pairing strength in this system.

## Approach
The computation uses standard solid‑state physics relations. The Debye temperature is obtained from the lattice coefficient β; the electronic density of states at the Fermi level follows from the Sommerfeld coefficient γ; and the electron‑phonon coupling constant λ_ep is evaluated with the McMillan formula, which connects Tc, Θ_D, and an assumed Coulomb pseudopotential μ*. The required inputs (γ, β, Tc) for both compounds are given, and the task is to carry out the arithmetic using the appropriate unit conversions and constants.

## Reproduction target
Given the specific‑heat coefficients and critical temperatures for MoTe₂ and MoTe₁.₈S₀.₂, compute the Debye temperature Θ_D (in K), the electronic density of states N(E_F) (in states/eV per formula unit), and the electron‑phonon coupling constant λ_ep (dimensionless) for each compound. Write the results to the JSON file `thermo_epc.json` with the structure described in the workflow step.

## Assets

- numpy: pip install numpy

## Workflow steps

### Step 1: Compute thermodynamic and electron-phonon coupling parameters
- Role: scored
- Action: Using the provided specific-heat coefficients γ (electronic) and β (lattice) and superconducting critical temperature Tc for MoTe₂ and MoTe₁.₈S₀.₂, compute the following for each compound:

- Debye temperature Θ_D from β using the standard relation β = N·(12/5)·π⁴·R·Θ_D⁻³ with N=3 atoms per formula unit, R=8.314 J mol⁻¹ K⁻¹.
- Electronic density of states at the Fermi level N(E_F) from γ using the relation γ = (π²/3)·k_B²·N_A·N(E_F)/f.u. (per mole of formula units), where N_A = 6.02214076×10²³ mol⁻¹ is Avogadro's number. Convert γ from mJ mol⁻¹ K⁻² to J mol⁻¹ K⁻² (×1e-3). Then N(E_F) = γ_J / [(π²/3)·k_B²·N_A] gives N(E_F) in J⁻¹; multiply by 1 eV = 1.602176634×10⁻¹⁹ J to obtain N(E_F) in states/eV per formula unit.
- Electron-phonon coupling constant λ_ep using the McMillan formula: λ_ep = [μ*·ln(1.45·Tc/Θ_D) - 1.04] / [1.04 + ln(1.45·Tc/Θ_D)·(1 - 0.62·μ*)] with Coulomb pseudopotential μ* = 0.1.

Inputs:
- MoTe₂: γ = 3.06 mJ mol⁻¹ K⁻², β = 0.758 mJ mol⁻¹ K⁻⁴, Tc = 0.1 K
- MoTe₁.₈S₀.₂: γ = 2.07 mJ mol⁻¹ K⁻², β = 0.635 mJ mol⁻¹ K⁻⁴, Tc = 1.3 K

Convert mJ to J appropriately before using the formulas.

Write the results to 'thermo_epc.json' with top-level keys 'MoTe2' and 'MoTe1.8S0.2', each containing numeric fields 'Theta_D' (K), 'N_EF' (states/eV), 'lambda_ep'.
- Output file: `/app/outputs/thermo_epc.json`
- Format: json
- Contract: {"MoTe2": {"Theta_D": "number", "N_EF": "number", "lambda_ep": "number"}, "MoTe1.8S0.2": {"Theta_D": "number", "N_EF": "number", "lambda_ep": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermo_epc.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermo_epc.json
- path: `/app/outputs/thermo_epc.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed Debye temperature, electronic density of states at the Fermi level, and electron-phonon coupling constant for MoTe₂ and MoTe₁.₈S₀.₂. The hidden checker recomputes the same quantities from the same fixed inputs and compares to these values within pre-defined absolute tolerances.
- schema:
  - `type`: object
  - `required`:
    - `MoTe2`:
      - `type`: object
      - `required`:
        - `Theta_D`: number
        - `N_EF`: number
        - `lambda_ep`: number
    - `MoTe1.8S0.2`:
      - `type`: object
      - `required`:
        - `Theta_D`: number
        - `N_EF`: number
        - `lambda_ep`: number
  - `description`: Object with keys for each compound, each containing the three computed numeric fields.

Notes: All constants and formulas are provided. The checker recomputes the three quantities for each compound from the same inputs and expects the submitted values to match within pre-defined absolute tolerances. The output contract now specifies metric_recompute because the verifier does not require an exact bitwise match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermo_epc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "MoTe2": {
            "type": "object",
            "required": {
              "Theta_D": "number",
              "N_EF": "number",
              "lambda_ep": "number"
            }
          },
          "MoTe1.8S0.2": {
            "type": "object",
            "required": {
              "Theta_D": "number",
              "N_EF": "number",
              "lambda_ep": "number"
            }
          }
        },
        "description": "Object with keys for each compound, each containing the three computed numeric fields."
      },
      "description": "Computed Debye temperature, electronic density of states at the Fermi level, and electron-phonon coupling constant for MoTe₂ and MoTe₁.₈S₀.₂. The hidden checker recomputes the same quantities from the same fixed inputs and compares to these values within pre-defined absolute tolerances."
    }
  ],
  "notes": "All constants and formulas are provided. The checker recomputes the three quantities for each compound from the same inputs and expects the submitted values to match within pre-defined absolute tolerances. The output contract now specifies metric_recompute because the verifier does not require an exact bitwise match."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's output artifact. For the main computation step, the verifier recomputes the three quantities from the same inputs using the identical formulas and compares the submitted values against its recomputed results within pre‑defined absolute tolerances. The agent's final reward is a weighted sum of the stage scores, with the scored arithmetic step carrying the majority of the weight. The agent must genuinely execute the calculations; merely reporting expected numbers is not sufficient to earn full credit.
