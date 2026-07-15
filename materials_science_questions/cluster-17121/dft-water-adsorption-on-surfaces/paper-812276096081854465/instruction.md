# Static Lattice Energy Minimization of Surface and Adsorption Energies on a Triclinic Mineral

## Problem background
Wollastonite is a triclinic calcium silicate mineral whose flotation separation is strongly influenced by the atomic-scale interaction of collector molecules with its surfaces. Atomistic static-lattice energy minimisation using empirical potentials and the Tasker surface energy method can calculate surface structures and adsorption energies, giving insight into the relative stability of different crystal faces and the strength of adsorbate binding. In this task you will reproduce such a simulation study: you will build the bulk α‑wollastonite crystal, relax it to equilibrium, compute the dissociation energy of water required for hydroxylation, then create the {100}, {001} and {102} surfaces, apply charge‑neutral surface reconstruction, and compute pure surface energies and adsorption energies for water, dissociated water, methanoic acid and methylamine.

## Approach
The computational approach is static energy minimization of the crystal using a polarisable shell‑model potential. The potential energy includes long‑range Coulomb interactions (with partial charges on atoms), short‑range Buckingham repulsion‑dispersion, harmonic angle bending terms for molecular fragments, Lennard‑Jones interactions for certain cross‑species, and Morse bond‑stretching terms for molecules. In particular, oxygen anions are treated with the Dick‑Overhauser shell model (core+shell connected by a harmonic spring) to capture electronic polarisability. The full set of potential parameters is provided below; they are transferred from well‑tested force‑field sets for silicates and organic molecules.

### Potential Parameters

**Functional forms**

- Coulombic: $q_iq_j/(4\pi\epsilon_0 r_{ij})$
- Buckingham: $A_{ij}\exp(-r_{ij}/\rho_{ij}) - C_{ij}/r_{ij}^6$
- Harmonic angle: $k(\theta-\theta_0)^2/2$
- Lennard-Jones: $F_{ij}r_{ij}^{-12} - G_{ij}r_{ij}^{-6}$
- Morse: $D_{ij}[1-\exp[-\alpha_{ij}(r_{ij}-r_{ij0})]]$

**Ion types, masses, charges and shell properties**

| ion | mass (amu) | core charge (e) | shell charge (e) | K (eV/Å²) |
|-----|------------|-----------------|------------------|----------|
| Si  | 28.09      | +4.0            |                  |          |
| H   | 1.008      | +0.4            |                  |          |
| O   | 15.99      | +0.848          | -2.848           | 74.92038 |
| O_h | 15.99      | +0.90           | -2.30            | 74.92038 |
| O_w | 15.99      | +1.25           | -2.05            | 209.4496 |
| C_f | 12.01      | +0.31           |                  |          |
| O_IC| 15.99      | -0.38           |                  |          |
| O_fH| 15.99      | -0.38           |                  |          |
| H_IC| 1.008      | +0.1            |                  |          |
| H_fO| 1.008      | +0.35           |                  |          |
| N   | 14.007     | -0.5            |                  |          |
| C_a | 12.01      | -0.08           |                  |          |
| H_aC| 1.008      | +0.1            |                  |          |
| H_aN| 1.008      | =0.14           |                  |          |

(Note: O denotes oxygen of wollastonite, O_h hydroxide oxygen, O_w water oxygen, H hydroxyl/water hydrogen; C_f and C_a are carbon in methanoic acid and methylamine; O_IC and O_fH are oxygens in methanoic acid; H_IC and H_fO hydrogen in methanoic acid; N nitrogen in methylamine; H_aC and H_aN hydrogens in methylamine. The shell model applies only to oxygen species O, O_h, O_w; other ions have only core charges.)

**Harmonic angle parameters**

| interacting ions               | k (eV/rad) | θ₀ (deg) |
|--------------------------------|------------|----------|
| O_h/O–Si–O/O_h                 | 2.09724    | 109.47   |
| H–O_w–H                        | 4.19978    | 108.69   |
| H_fO–O_fH–C_f                 | 4.29       | 112.0    |
| H_IC–C_f–O_fH                | 4.72       | 110.0    |
| H_IC–C_f–O_IC                | 4.72       | 120.0    |
| O_fH–C_f–O_IC                | 12.45      | 123.0    |
| H_aN–N–C_a                   | 1.71       | 106.4    |

**Pair potential parameters (Table 4)**

| interacting ions              | A (eV) | ρ (Å) | C (eV·Å⁶) | F (eV·Å¹²) | G (eV·Å⁶) | D (eV) | α (Å⁻¹) | r₀ (Å) |
|-------------------------------|--------|------|-----------|------------|----------|--------|--------|------|
| Si–O_h                        | 983.907| 0.321| 10.662    |            |          |        |        |      |
| Si–O/O_w                     |        |      | 10.662    |            |          |        |        |      |
| O–O                          |        |      | 27.88     |            |          |        |        |      |
| Ca–O                         |        |      | 0.00      |            |          |        |        |      |
| Ca–O_h                       |        |      | 0.00      |            |          |        |        |      |
| Ca–O_w                       |        |      | 0.00      |            |          |        |        |      |
| O–O_h                        |        |      | 13.94     |            |          |        |        |      |
| O–O_w                        |        |      | 28.92     |            |          |        |        |      |
| O–H                          |        |      | 0.00      |            |          |        |        |      |
| O_h–H                        |        |      | 0.00      |            |          | 7.05   | 3.17   | 0.94  |
| O_h–O_h                      |        |      | 6.97      |            |          |        |        |      |
| O–O_w                        |        |      | 28.92     |            |          |        |        |      |
| O_w–H                        |        |      | 0.00      |            |          | 6.20   | 2.22   | 0.92  |
| Ca–O_fC/O_fW                 |        |      | 0.00      |            |          |        |        |      |
| O–O_fC/O_fH                  |        |      |           | 23430.0    | 32.12    |        |        |      |
| O–H_fC/O_fO                  |        |      |           | 5600.0     | 12.00    |        |        |      |
| O–C_f/C_a                   |        |      |           | 87327.5    | 56.32    |        |        |      |
| O_fC/O_fH–O_fC/O_fH         |        |      |           | 11822.6    | 21.61    |        |        |      |
| O_fC/O_fH–C_f               |        |      |           | 38994.3    | 35.23    |        |        |      |
| O_fC/O_fH–H_fC/H_fO         |        |      |           | 1908.1     | 5.55     |        |        |      |
| C_f–H_fC                     |        |      |           |            |          | 4.66   | 1.77   | 1.10  |
| C_f–O_fC                     |        |      |           |            |          | 6.22   | 2.06   | 1.23  |
| C_f–O_fH                     |        |      |           |            |          | 4.29   | 2.00   | 1.37  |
| H_fO–O_fH                    |        |      |           |            |          | 4.08   | 2.28   | 0.96  |
| Ca–N                         | 663.26 | 0.337| 0.00      |            |          |        |        |      |
| O–H_aC/H_aN                  |        |      |           | 5600.0     | 12.0     |        |        |      |
| O–N                          |        |      |           | 67528.4    | 50.45    |        |        |      |
| N–Ca                         |        |      |           |            |          | 2.95   | 2.29   | 1.47  |
| Ca–H_aC                      |        |      |           |            |          | 4.71   | 1.77   | 1.11  |
| N–H_aN                       |        |      |           |            |          | 3.82   | 2.28   | 1.03  |

(All parameters are taken from Tables 1–4 of the reference paper. For Lennard‑Jones interactions, the parameters given in the F, G columns are used; for Morse, D, α, r₀. The shell model parameters K, Y are provided in the ion table; polarizability α = Y²/K.)

Bulk relaxation is performed at constant pressure starting from the experimentally known triclinic unit cell. Then, for each surface, a fresh cut is made from the relaxed bulk. The Tasker method is used to partition the crystal into Region I (near‑surface atoms allowed to relax) and Region II (fixed at bulk positions), ensuring that the repeat unit has no net dipole perpendicular to the surface. Any low‑coordinated surface atoms (dangling oxygens, under‑coordinated silicon) are removed by a reconstruction protocol: lone oxygen atoms are transferred, together with charge‑compensating cations (Ca or Si), to the bottom of the slab, and hydroxylation may be applied to saturate broken bonds. The pure surface energy γ is computed as γ = (Us – Ub)/A, where Us is the energy of the surface block, Ub the energy of an equivalent number of bulk ions, and A the surface area.

For adsorption, a single molecule (H₂O, dissociated H₂O as OH⁻ + H⁺, HCOOH, or CH₃NH₂) is placed on the reconstructed surface, the whole system relaxed, and a surface energy with adsorbate, SE_X, is obtained from the same formula. The adsorption energy AE_X is computed as U_def – (U_s + U_mol), where U_def is the energy of the surface with the adsorbate, U_s the pure surface energy, and U_mol the energy of the isolated molecule. For dissociated water, the dissociation energy (the energy change of the reaction H₂O + O²⁻ → 2 OH⁻) is required to correctly reference the hydroxyl surface energy; you must compute this value with the same force field via Hess’s law using the lattice energies of Ca(OH)₂ and Si(OH)₄ and tabulated thermodynamic data.

## Reproduction target
You must produce two scored output files:

1. **relaxed_bulk_cell.json** – the fully relaxed unit cell parameters (a, b, c in Å; α, β, γ in degrees) of α‑wollastonite obtained from constant‑pressure minimisation.

2. **surface_adsorption_energies.json** – a JSON object containing, for each surface {100}, {001}, {102}, the following numeric quantities (in the specified units):
   - pure surface energy (SE_P, J/m²)
   - surface energy with water (SE_W, J/m²)
   - surface energy with hydroxyl / dissociated water (SE_H, J/m²)
   - surface energy with methanoic acid (SE_M, J/m²)
   - surface energy with methylamine (SE_A, J/m²)
   - adsorption energy of water (AE_W, kJ/mol)
   - adsorption energy of hydroxyl (AE_H, kJ/mol)
   - adsorption energy of methanoic acid (AE_M, kJ/mol)
   - adsorption energy of methylamine (AE_A, kJ/mol)

The intermediate dissociation energy of water on wollastonite must be computed and saved in /app/outputs/dissociation_energy.txt, but it is not directly scored; it is needed to derive the hydroxyl surface energies.

## Assets

- GULP: https://gulp.curtin.edu.au/

## Workflow steps

### Step 1: Relax bulk α‑wollastonite
- Role: scored
- Action: Set up the triclinic α‑wollastonite crystal with initial cell parameters a=7.93 Å, b=7.32 Å, c=7.07 Å, α=90.05°, β=95.22°, γ=103.43° and space group P-1. Using the supplied potential parameters (including the shell model for oxygen) in GULP, perform a constant‑pressure bulk relaxation. Output the relaxed cell parameters.
- Output file: `/app/outputs/relaxed_bulk_cell.json`
- Format: json
- Contract: {"a": number, "b": number, "c": number, "alpha": number, "beta": number, "gamma": number, "units": "Å and degrees"}
- Scoring: scored by hidden verifier

### Step 2: Calculate water dissociation energy on wollastonite
- Role: process
- Action: Using Hess’s law, compute the dissociation energy of a water molecule on the wollastonite surface (H₂O + O²⁻ → 2 OH⁻). Calculate the lattice energies of Ca(OH)₂ and Si(OH)₄ with the same forcefield, and combine them with the known thermodynamic data as described in the paper. Store the resulting value for use in hydroxylation energy calculations.
- Evidence: `/app/outputs/dissociation_energy.txt`

### Step 3: Compute surface and adsorption energies on {100}, {001}, {102} surfaces
- Role: scored (load-bearing)
- Action: Using the relaxed bulk structure and the dissociation energy, construct the {100}, {001}, and {102} surfaces. Apply the surface reconstruction protocol (transfer lone oxygens with Ca/Si) to eliminate low‑coordinated atoms, ensuring charge neutrality and zero dipole. Compute the pure surface energy via γ = (U_s – U_b)/A. For each reconstructed surface, place one molecule of water, dissociated water (OH⁻ + H⁺), methanoic acid, and methylamine, perform energy minimization, and compute the surface energy with adsorbate and adsorption energy. Output all energies in a single JSON file.
- Output file: `/app/outputs/surface_adsorption_energies.json`
- Format: json
- Contract: {"100": {"SE_P": number, "SE_W": number, "SE_H": number, "SE_M": number, "SE_A": number, "AE_W": number, "AE_H": number, "AE_M": number, "AE_A": number}, "001": { ... }, "102": { ... }}; SE in J/m², AE in kJ/mol
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_bulk_cell.json`
- `/app/outputs/surface_adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_bulk_cell.json
- path: `/app/outputs/relaxed_bulk_cell.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed unit cell parameters of α‑wollastonite. The checker compares each parameter to the paper‑reported values with hidden absolute tolerances.
- schema:
  - `type`: object
  - `required`: `a`, `b`, `c`, `alpha`, `beta`, `gamma`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
    - `b`:
      - `type`: number
      - `unit`: Å
    - `c`:
      - `type`: number
      - `unit`: Å
    - `alpha`:
      - `type`: number
      - `unit`: degrees
    - `beta`:
      - `type`: number
      - `unit`: degrees
    - `gamma`:
      - `type`: number
      - `unit`: degrees

### surface_adsorption_energies.json
- path: `/app/outputs/surface_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Surface energies (SE, J/m²) and adsorption energies (AE, kJ/mol) for each surface {100}, {001}, {102} with water (W), hydroxyl (H), methanoic acid (M), and methylamine (A). The checker compares each entry against hidden gold values and verifies structural trends.
- schema:
  - `type`: object
  - `required`: `100`, `001`, `102`
  - `properties`:
    - `100`:
      - `type`: object
      - `required`: `SE_P`, `SE_W`, `SE_H`, `SE_M`, `SE_A`, `AE_W`, `AE_H`, `AE_M`, `AE_A`
      - `properties`:
        - `SE_P`:
          - `type`: number
          - `unit`: J/m²
        - `SE_W`:
          - `type`: number
          - `unit`: J/m²
        - `SE_H`:
          - `type`: number
          - `unit`: J/m²
        - `SE_M`:
          - `type`: number
          - `unit`: J/m²
        - `SE_A`:
          - `type`: number
          - `unit`: J/m²
        - `AE_W`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_H`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_M`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_A`:
          - `type`: number
          - `unit`: kJ/mol
    - `001`:
      - `type`: object
      - `required`: `SE_P`, `SE_W`, `SE_H`, `SE_M`, `SE_A`, `AE_W`, `AE_H`, `AE_M`, `AE_A`
      - `properties`:
        - `SE_P`:
          - `type`: number
          - `unit`: J/m²
        - `SE_W`:
          - `type`: number
          - `unit`: J/m²
        - `SE_H`:
          - `type`: number
          - `unit`: J/m²
        - `SE_M`:
          - `type`: number
          - `unit`: J/m²
        - `SE_A`:
          - `type`: number
          - `unit`: J/m²
        - `AE_W`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_H`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_M`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_A`:
          - `type`: number
          - `unit`: kJ/mol
    - `102`:
      - `type`: object
      - `required`: `SE_P`, `SE_W`, `SE_H`, `SE_M`, `SE_A`, `AE_W`, `AE_H`, `AE_M`, `AE_A`
      - `properties`:
        - `SE_P`:
          - `type`: number
          - `unit`: J/m²
        - `SE_W`:
          - `type`: number
          - `unit`: J/m²
        - `SE_H`:
          - `type`: number
          - `unit`: J/m²
        - `SE_M`:
          - `type`: number
          - `unit`: J/m²
        - `SE_A`:
          - `type`: number
          - `unit`: J/m²
        - `AE_W`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_H`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_M`:
          - `type`: number
          - `unit`: kJ/mol
        - `AE_A`:
          - `type`: number
          - `unit`: kJ/mol

Notes: All potential parameters (Tables 1‑4) and surface reconstruction protocols are provided in instruction.md. The checker validates additional structural relations to ensure the correct energy ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_bulk_cell.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "b",
          "c",
          "alpha",
          "beta",
          "gamma"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å"
          },
          "b": {
            "type": "number",
            "unit": "Å"
          },
          "c": {
            "type": "number",
            "unit": "Å"
          },
          "alpha": {
            "type": "number",
            "unit": "degrees"
          },
          "beta": {
            "type": "number",
            "unit": "degrees"
          },
          "gamma": {
            "type": "number",
            "unit": "degrees"
          }
        }
      },
      "description": "Relaxed unit cell parameters of α‑wollastonite. The checker compares each parameter to the paper‑reported values with hidden absolute tolerances."
    },
    {
      "file": "surface_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "100",
          "001",
          "102"
        ],
        "properties": {
          "100": {
            "type": "object",
            "required": [
              "SE_P",
              "SE_W",
              "SE_H",
              "SE_M",
              "SE_A",
              "AE_W",
              "AE_H",
              "AE_M",
              "AE_A"
            ],
            "properties": {
              "SE_P": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_W": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_H": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_M": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_A": {
                "type": "number",
                "unit": "J/m²"
              },
              "AE_W": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_H": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_M": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_A": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          },
          "001": {
            "type": "object",
            "required": [
              "SE_P",
              "SE_W",
              "SE_H",
              "SE_M",
              "SE_A",
              "AE_W",
              "AE_H",
              "AE_M",
              "AE_A"
            ],
            "properties": {
              "SE_P": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_W": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_H": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_M": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_A": {
                "type": "number",
                "unit": "J/m²"
              },
              "AE_W": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_H": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_M": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_A": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          },
          "102": {
            "type": "object",
            "required": [
              "SE_P",
              "SE_W",
              "SE_H",
              "SE_M",
              "SE_A",
              "AE_W",
              "AE_H",
              "AE_M",
              "AE_A"
            ],
            "properties": {
              "SE_P": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_W": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_H": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_M": {
                "type": "number",
                "unit": "J/m²"
              },
              "SE_A": {
                "type": "number",
                "unit": "J/m²"
              },
              "AE_W": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_H": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_M": {
                "type": "number",
                "unit": "kJ/mol"
              },
              "AE_A": {
                "type": "number",
                "unit": "kJ/mol"
              }
            }
          }
        }
      },
      "description": "Surface energies (SE, J/m²) and adsorption energies (AE, kJ/mol) for each surface {100}, {001}, {102} with water (W), hydroxyl (H), methanoic acid (M), and methylamine (A). The checker compares each entry against hidden gold values and verifies structural trends."
    }
  ],
  "notes": "All potential parameters (Tables 1‑4) and surface reconstruction protocols are provided in instruction.md. The checker validates additional structural relations to ensure the correct energy ordering."
}
```

## How you are scored
The hidden verifier evaluates your work in two parts, each contributing to the final score.

- **Bulk cell parameters** (relaxed_bulk_cell.json): the verifier compares your reported a, b, c, α, β, γ against the reference equilibrium values derived from the same potential model. Credit is awarded based on absolute deviations within hidden tolerances.

- **Surface and adsorption energy table** (surface_adsorption_energies.json): the verifier checks every numeric entry (SE_P, SE_W, SE_H, SE_M, SE_A and AE_W, AE_H, AE_M, AE_A) for all three surfaces against the corresponding reference values computed from the same force field using relative tolerances. In addition, the verifier checks that the relative magnitudes of the pure surface energies and the identity of the most strongly adsorbed species on each surface are physically consistent; these trend checks ensure that your minimization protocol captured the key energetic features.

Reporting numbers without genuinely performing the required energy minimizations (or supplying values that violate the tolerance window) will result in a low score. The verifier has access to the correct reference results and applies its checks independently.
