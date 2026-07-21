# Electrostatic model for ferroelectric superlattice polarization

## Problem background
Ferroelectric oxide superlattices, especially PbTiO₃/SrTiO₃, exhibit rich polarization behavior as layer thicknesses are varied. Understanding the polarization and structural tetragonality in these heterostructures is important for designing functional materials. A simple electrostatic total-energy model, combined with Landau-type expansions of the bulk layer energies, can predict equilibrium polarizations and tetragonalities under ideal boundary conditions. This task asks you to implement that model for a PbTiO₃/SrTiO₃ superlattice with a fixed SrTiO₃ thickness of three unit cells and varying PbTiO₃ thicknesses, and to compute the resulting equilibrium properties — which will serve as a baseline for later analysis.

## Approach
The model treats each layer as having a homogeneous polarization (Pₚ⁰ for PbTiO₃, Pₛ⁰ for SrTiO₃). The total energy per unit cell area is the sum of bulk layer energies plus an electrostatic energy term that arises from the discontinuity of polarization and satisfies short‑circuit boundary conditions and continuity of electric displacement.

### Model details
The total energy per unit cell area of an nₚ/nₛ superlattice is written as  

E(Pₚ⁰, Pₛ⁰) = nₚ·Uₚ(Pₚ⁰) + nₛ·Uₛ(Pₛ⁰) + E_elec(Pₚ⁰, Pₛ⁰)

where  
- Uₚ(P) and Uₛ(P) are the bulk energies per 5‑atom unit cell (eV) of PbTiO₃ and SrTiO₃ as functions of polarization,  
- E_elec is the macroscopic electrostatic energy per unit cell area (J/m²) arising from the polarization mismatch under short‑circuit conditions.

The electrostatic energy is given explicitly by  

E_elec(Pₚ⁰, Pₛ⁰) = (lₚ·lₛ) / [ε₀·(lₚ + lₛ)] · (Pₛ⁰ − Pₚ⁰)²  

where lₚ = nₚ·cₚ₀ and lₛ = nₛ·cₛ₀ are the physical thicknesses of the PbTiO₃ and SrTiO₃ layers, constructed from the out‑of‑plane lattice constants cₚ₀ and cₛ₀ (in meters).

The bulk energies U(P) (eV per 5‑atom unit cell) are expanded as Landau polynomials:

U(P) = B·P² + C·P⁴

with coefficients obtained from first‑principles DFT calculations (Ref. [30] of the paper) under the constraint of an in‑plane lattice constant a = 3.846 Å.

The tetragonality ratio c/a (dimensionless) is given by a similar expansion:

c/a = α + β·P² + γ·P⁴

**All required coefficients are listed below.**

### Coefficients

**Landau coefficients for U(P)** (eV per 5‑atom unit cell):  
- PbTiO₃: Bₚ = −0.17175279, Cₚ = 0.16068441  
- SrTiO₃: Bₛ = 0.21046331, Cₛ = 0.30913420

**Tetragonality expansion coefficients:**  
- PbTiO₃: αₚ = 1.01566146, βₚ = 0.03609915, γₚ = 0.02209009  
- SrTiO₃: αₛ = 1.0, βₛ = 0.06076952, γₛ = 0.04820368

### Physical constants and lattice parameters

- In‑plane lattice constant (constrained): a = 3.846e−10 m  
- Unit cell area: A_cell = a²  (to convert bulk energy from eV/cell to J/m²)
- Conversion factor: 1 eV = 1.602176634e−19 J  
- Out‑of‑plane bulk lattice constants (under the in‑plane constraint):  
  cₚ₀ = 4.009e−10 m  (PbTiO₃)  
  cₛ₀ = 3.846e−10 m  (SrTiO₃ cubic)
- Vacuum permittivity: ε₀ = 8.8541878128e−12 F/m

**Important:** When constructing the total energy E (per unit cell area, J/m²), convert the bulk contributions as  

nₚ·Uₚ(Pₚ⁰) · (1.602176634e−19 J/eV) / A_cell   +   nₛ·Uₛ(Pₛ⁰) · (1.602176634e−19 J/eV) / A_cell   +   E_elec

where E_elec as given above is already in J/m².

## Reproduction target
Compute the equilibrium layer polarizations Pₚ⁰ and Pₛ⁰ (in C/m²) and the dimensionless tetragonality ratios c/a for both PbTiO₃ and SrTiO₃, for a superlattice with nₛ = 3 unit cells of SrTiO₃ and each nₚ in {1,2,3,4,5,6,7}. Output the results as a CSV file, `polarization_tetragonality.csv`, with columns: nₚ, Pₚ⁰, Pₛ⁰, tetragonality_Pb, tetragonality_Sr.

## Assets

- scipy.optimize.minimize: scipy

## Workflow steps

### Step 1: Electrostatic model minimization and output
- Role: scored (load-bearing)
- Action: Construct the energy functions Uₚ(P) and Uₛ(P) and the tetragonality functions cₚ/a(P) and cₛ/a(P) using the Landau coefficients listed above. Build the total energy per unit cell area E(Pₚ⁰, Pₛ⁰) = nₚ·Uₚ(Pₚ⁰) + nₛ·Uₛ(Pₛ⁰) + E_elec(Pₚ⁰, Pₛ⁰) with the electrostatic term as given in the Model details. For nₛ=3 and each nₚ in {1,2,3,4,5,6,7}, minimize E with respect to Pₚ⁰ and Pₛ⁰ to find equilibrium values (use reasonable initial guesses such as Pₚ ~ 0.7 C/m² and Pₛ ~ 0). From the equilibrium polarizations compute the tetragonality ratios cₚ/a and cₛ/a using the c/a expansion. Write all results to a CSV file.
- Output file: `/app/outputs/polarization_tetragonality.csv`
- Format: csv
- Contract: Columns: n_p (integer), P_p0 (float, C/m^2), P_s0 (float, C/m^2), tetragonality_Pb (float, dimensionless), tetragonality_Sr (float, dimensionless). One row per n_p from 1 to 7.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarization_tetragonality.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarization_tetragonality.csv
- path: `/app/outputs/polarization_tetragonality.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium layer polarizations and tetragonalities for n_p=1..7 computed by the electrostatic model.
- schema:
  - `type`: table
  - `required_columns`: `n_p`, `P_p0`, `P_s0`, `tetragonality_Pb`, `tetragonality_Sr`
  - `units`:
    - `P_p0`: C/m^2
    - `P_s0`: C/m^2
    - `tetragonality_Pb`: dimensionless
    - `tetragonality_Sr`: dimensionless

Notes: The hidden reference values are obtained from an independent implementation of the same electrostatic model using the same coefficients, allowing tolerance‑based comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarization_tetragonality.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_p",
          "P_p0",
          "P_s0",
          "tetragonality_Pb",
          "tetragonality_Sr"
        ],
        "units": {
          "P_p0": "C/m^2",
          "P_s0": "C/m^2",
          "tetragonality_Pb": "dimensionless",
          "tetragonality_Sr": "dimensionless"
        }
      },
      "description": "Equilibrium layer polarizations and tetragonalities for n_p=1..7 computed by the electrostatic model."
    }
  ],
  "notes": "The hidden reference values are obtained from an independent implementation of the same electrostatic model using the same coefficients, allowing tolerance‑based comparison."
}
```

## How you are scored
A hidden verifier independently implements the same electrostatic model using the identical Landau coefficients and minimization approach. It computes reference equilibrium values for each nₚ. Your submitted CSV is compared field‑by‑field against this reference. The reward for each field decays as the deviation from the reference grows beyond a tolerance; meeting or beating the reference yields full credit. The final reward is the average across all fields. The tolerances are chosen to absorb typical numerical differences between correct implementations; the exact tolerances and reference values are hidden.