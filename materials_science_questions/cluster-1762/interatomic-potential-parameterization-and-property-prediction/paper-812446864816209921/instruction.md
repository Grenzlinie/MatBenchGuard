# Pair potential parameterization and free energy calculation for AgBr/α-AgI solid solution

## Problem background
α-AgI is a superionic conductor in which silver ions move freely through a body-centered-cubic iodine sublattice. Adding AgBr, which normally adopts the NaCl structure, alters the ionic character and stability of the conducting phase. The phase diagram of the AgI-AgBr system shows a limited solubility of AgBr in the α-AgI structure. Understanding how the ionicity and free energy of the solid solution change with composition and temperature provides insight into the stability of the superionic phase and the transition to a normal ionic conductor.

## Approach
The approach develops empirical interionic pair potentials for AgBr and α-AgI, then uses them to construct a free energy model of the α-AgI-type solid solution as a function of the mole fraction x of AgBr. The pair potentials include Coulomb interactions, short-range repulsion, polarization, dipole-dipole (van der Waals) and dipole-quadrupole terms, with a partial covalency correction for α-AgI. The potentials for pure AgBr and pure α-AgI are parameterised by fitting to experimental thermodynamic data (cohesive energy, thermal expansion coefficient, isothermal compressibility) through the Hildebrand equation of state. For the solid solution, the effective ionic charge is assumed to vary linearly with composition, z(x) = p·x + 0.75, where p is an unknown parameter. The total free energy combines the static-lattice internal energy U(x), a vibrational free energy estimated from a Debye model with a diatomic-chain sound velocity, and the configurational entropy of random anion mixing. The derivative ∂F/∂x is derived, and by calibrating it against the experimentally known solubility limit at a reference temperature, the parameter p is determined. The solubility limit itself is then obtained as the composition where ∂F/∂x = 0, and the effective valence at any given composition can be computed from the calibrated p.

## Reproduction target
Compute the effective valence number z of silver ions at a mole fraction x = 0.2 AgBr and temperature T = 600 K in the α-AgI-type solid solution, and the solubility limit x_sol (mole fraction AgBr) where ∂F/∂x = 0 at T = 600 K, using the derived interionic pair potentials and free energy model.

## Assets

- Python 3 with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Van der Waals coefficients assignment
- Role: process
- Action: Set the Van der Waals coefficients and electronic polarizabilities for AgBr and AgI to the following present data values from the paper's Table 1. For AgBr: alpha_+ = 2.40e-24 cm^3, alpha_- = 4.58e-24 cm^3, c_+- = 470e-60 erg cm^6, c_-- = 732e-60 erg cm^6, d_+- = 744e-76 erg cm^8, d_-- = 1384e-76 erg cm^8. For AgI: alpha_+ = 2.40e-24 cm^3, alpha_- = 7.50e-24 cm^3, c_+- = 751e-60 erg cm^6, c_-- = 1890e-60 erg cm^6, d_+- = 1285e-76 erg cm^8, d_-- = 4062e-76 erg cm^8. Use these coefficients in all subsequent pair potentials. Store them in the evidence file.
- Evidence: `/app/outputs/van_der_waals_coefficients.json`

### Step 2: AgBr pair potential parameterization
- Role: process
- Action: For AgBr (NaCl structure, covalency constant A=0), fit the hardness parameters b, n and effective valence z_AgBr by minimizing the error in reproducing the experimental cohesive energy, thermal expansion coefficient, and isothermal compressibility via the Hildebrand equation of state. Use the pair-potential form containing Coulomb, short-range repulsion, polarization, dipole-dipole, dipole-quadrupole interactions, with the coefficients from step 1 and ionic radii from Pauling values.
- Evidence: `/app/outputs/agbr_potential.json`

### Step 3: α-AgI pair potential parameterization
- Role: process
- Action: For α-AgI, determine the effective valence z_AgI, hardness parameters b, n, covalency constant A, and Madelung constant M by fitting to the heat of transformation from β- to α-phase, the X-ray Ag–Ag distance (≈4.0 Å), and the cohesive energy. Use the pair-potential form and the coefficients from step 1.
- Evidence: `/app/outputs/agi_potential.json`

### Step 4: Static-lattice internal energy U(x) of solid solution
- Role: process
- Action: Implement the internal energy U(x) and its volume derivative(s) as a function of Br mole fraction x using the pair potentials from steps 2 and 3 and a linear interpolation for the effective valence: z(x) = p x + 0.75, where p is an unknown parameter to be determined later. The energy also depends on volume via the Hildebrand equation of state.
- Evidence: none

### Step 5: Free energy and ∂F/∂x derivation
- Role: process
- Action: Construct the total free energy derivative ∂F/∂x at a given temperature T, using U(x), a vibrational free energy F_vib from a Debye model with diatomic-chain sound velocity (depending on ionic masses), and the configurational entropy. Include the composition-dependent harmonic force constant derived from the pair potentials. Omit the small higher-order cancelling terms as done in the original derivation.
- Evidence: none

### Step 6: Calibrate p and compute solubility limit
- Role: scored (load-bearing)
- Action: Given the experimental solubility limit x_sol_exp = 0.20 at T = 600 K, determine the interpolation parameter p such that ∂F/∂x(x_sol_exp, p) = 0 at T = 600 K. Using that calibrated p, find the root x_sol of ∂F/∂x(x,p) = 0. Write x_sol to solubility_limit.txt. Also store the calibrated p in p_value.json as evidence.
- Output file: `/app/outputs/solubility_limit.txt`
- Format: txt
- Contract: Float: mole fraction x (0 ≤ x ≤ 1)
- Scoring: scored by hidden verifier

### Step 7: Compute effective valence at x=0.2
- Role: scored
- Action: Using the calibrated p from step 6, compute the effective valence z = p * 0.2 + 0.75. Write the result to effective_valence.txt.
- Output file: `/app/outputs/effective_valence.txt`
- Format: txt
- Contract: Float: dimensionless effective valence number (typically 0.75–0.95)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/solubility_limit.txt`
- `/app/outputs/effective_valence.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### solubility_limit.txt
- path: `/app/outputs/solubility_limit.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Solubility limit composition x (mole fraction) at T=600 K
- schema:
  - `type`: text
  - `description`: a single floating-point number representing the mole fraction of AgBr in α-AgI at which ∂F/∂x=0 at T=600 K

### effective_valence.txt
- path: `/app/outputs/effective_valence.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Effective valence number z at x=0.2, T=600 K (dimensionless)
- schema:
  - `type`: text
  - `description`: a single floating-point number representing the effective valence (ionicity) of silver ions at x=0.2 AgBr and T=600 K

Notes: Both outputs are single numbers written as plain text. The solubility limit is expected to be very close to the experimental input used for calibration (0.20) as a consistency check; the effective valence is the main reproduced quantity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "solubility_limit.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "a single floating-point number representing the mole fraction of AgBr in α-AgI at which ∂F/∂x=0 at T=600 K"
      },
      "description": "Solubility limit composition x (mole fraction) at T=600 K"
    },
    {
      "file": "effective_valence.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "a single floating-point number representing the effective valence (ionicity) of silver ions at x=0.2 AgBr and T=600 K"
      },
      "description": "Effective valence number z at x=0.2, T=600 K (dimensionless)"
    }
  ],
  "notes": "Both outputs are single numbers written as plain text. The solubility limit is expected to be very close to the experimental input used for calibration (0.20) as a consistency check; the effective valence is the main reproduced quantity."
}
```

## How you are scored
A hidden verifier independently checks your submitted pipeline artifacts. The verifier reads your evidence files (agbr_potential.json, agi_potential.json, p_value.json), reconstructs the free energy derivative ∂F/∂x from your fitted potentials and free energy expressions, verifies that ∂F/∂x evaluated at the calibration composition and temperature is approximately zero, and recomputes the effective valence z and the solubility limit x_sol from your calibrated p. Your submitted output files (effective_valence.txt and solubility_limit.txt) are compared to the recomputed values; agreement within a hidden tolerance yields full credit. Each workflow step contributes a weighted share to the final reward.
