# Static Lattice Elastic Constants of NaCl from Born Model

## Problem background
The elastic properties of NaCl under high pressure and temperature are important for understanding the equation of state of ionic solids. Ultrasonic interferometry measurements provide elastic constants as functions of pressure and temperature. These data can be extrapolated to zero temperature to obtain static lattice properties, which can then be compared with predictions from a Born-type lattice model. This task focuses on computing the static lattice elastic constants of NaCl from a Born model that includes nearest-neighbor repulsion, van der Waals interactions, and second-neighbor Cl⁻ interactions.

## Approach
The Born model expresses the lattice energy as a sum of contributions: the Madelung electrostatic term, a cation-anion repulsive potential (taken as exponential form V(R)=λ e^{-R/ρ}), van der Waals interactions between cation and anion (C_AB), and anion-anion interactions modeled by the Lennard-Jones (6-12) potential for Ar (since Cl⁻ is isoelectronic with Ar). The Lennard-Jones parameters σ and ε are known, and the coefficients C_BB and D_BB can be derived from them. Using the static lattice parameters (equilibrium nearest-neighbor distance R̃=2.784 Å and bulk modulus K̃=284.7 kbar), the repulsive parameters λ and ρ are determined by the two equilibrium conditions: the pressure vanishes at R̃, and the bulk modulus matches K̃. Once the repulsive potential is fixed, the elastic constants C11, C12, C44 are evaluated from analytical expressions that are second derivatives of the lattice energy with respect to strain. The first and second pressure derivatives of the elastic constants are obtained by differentiating those expressions with respect to R and using the chain rule with dP/dR or equivalently through the relations involving K and dK/dP. The calculation is performed at zero pressure and temperature.

## Reproduction target
Using the static lattice parameters (Ṽ=26.0 cm³/mol, K̃=284.7 kbar, R̃=2.784 Å), the Lennard-Jones constants for Cl⁻ (σ=3.40 Å, ε=167×10⁻¹⁶ erg), and the van der Waals coefficients (C_AB, C_BB, D_BB; see assets), and setting ionicity φ=1.0, implement the Born model with an exponential cation-anion repulsive potential. Determine the repulsive parameters λ and ρ from the equilibrium conditions. Then compute the static lattice elastic constants C11, C12, C44 (in kbar) and their first (dimensionless) and second (kbar⁻¹) pressure derivatives at zero pressure. Output all values to the file predicted_elastic_constants.json as specified.

## Assets

- Static lattice parameters (Ṽ, K̃, R̃)
- Lennard-Jones constants for Argon (Cl⁻ model)
- Van der Waals coefficients (C_AB, C_BB, D_BB)

## Workflow steps

### Step 1: Determine exponential repulsive parameters
- Role: process
- Action: Using the static lattice parameters (Ṽ, K̃, R̃), Lennard-Jones constants for Cl⁻ (σ=3.40 Å, ε=167×10⁻¹⁶ erg), and van der Waals coefficients (C_AB, C_BB, D_BB), solve the equilibrium conditions (equations for pressure and bulk modulus at the static lattice) to determine the exponential cation-anion repulsive parameters λ and ρ for the potential V(R)=λ e^{-R/ρ}. Use ionicity φ=1.0.
- Evidence: none

### Step 2: Compute static lattice elastic constants and pressure derivatives
- Role: scored (load-bearing)
- Action: Evaluate the Born model expressions for the static lattice elastic constants C11, C12, C44 (in kbar) and their first (dCij/dP, dimensionless) and second (d²Cij/dP², in kbar⁻¹) pressure derivatives at zero pressure using the determined repulsive parameters, Lennard-Jones constants, and van der Waals coefficients. Also compute the static bulk modulus K̃ and its pressure derivative K' (optional). Write the results to predicted_elastic_constants.json.
- Output file: `/app/outputs/predicted_elastic_constants.json`
- Format: json
- Contract: JSON object with keys: C11 (kbar), C12 (kbar), C44 (kbar), dC11_dP (dimensionless), dC12_dP (dimensionless), dC44_dP (dimensionless), d2C11_dP2 (kbar⁻¹), d2C12_dP2 (kbar⁻¹), d2C44_dP2 (kbar⁻¹), and optionally K_prime (dimensionless), K_doubleprime (kbar⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_elastic_constants.json
- path: `/app/outputs/predicted_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed static lattice elastic constants and pressure derivatives; the hidden checker will compare each value to the paper's experimental extrapolated reference (Table 5) using absolute tolerances.
- schema:
  - `type`: object
  - `required`:
    - `C11`: number (kbar)
    - `C12`: number (kbar)
    - `C44`: number (kbar)
    - `dC11_dP`: number (dimensionless)
    - `dC12_dP`: number (dimensionless)
    - `dC44_dP`: number (dimensionless)
    - `d2C11_dP2`: number (kbar⁻¹)
    - `d2C12_dP2`: number (kbar⁻¹)
    - `d2C44_dP2`: number (kbar⁻¹)

Notes: All values refer to zero-pressure static lattice at T=0 K. The checker uses absolute tolerances of ±10 kbar for Cij, ±0.5 for first derivatives, ±0.02 kbar⁻¹ for second derivatives.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "number (kbar)",
          "C12": "number (kbar)",
          "C44": "number (kbar)",
          "dC11_dP": "number (dimensionless)",
          "dC12_dP": "number (dimensionless)",
          "dC44_dP": "number (dimensionless)",
          "d2C11_dP2": "number (kbar⁻¹)",
          "d2C12_dP2": "number (kbar⁻¹)",
          "d2C44_dP2": "number (kbar⁻¹)"
        }
      },
      "description": "Computed static lattice elastic constants and pressure derivatives; the hidden checker will compare each value to the paper's experimental extrapolated reference (Table 5) using absolute tolerances."
    }
  ],
  "notes": "All values refer to zero-pressure static lattice at T=0 K. The checker uses absolute tolerances of ±10 kbar for Cij, ±0.5 for first derivatives, ±0.02 kbar⁻¹ for second derivatives."
}
```

## How you are scored
A hidden verifier will read your predicted_elastic_constants.json and compare each numeric entry (C11, C12, C44, their first and second pressure derivatives) against a reference value. For each scalar, if the absolute difference is within a preset tolerance, full credit is awarded; otherwise partial credit may be given based on relative error. The final reward is the weighted sum of scores across all fields. Your workflow is considered successful if the computed numbers are sufficiently close to the hidden reference. No further comparison or analysis is required; the verifier runs automatically.
