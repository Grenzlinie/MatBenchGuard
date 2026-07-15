# Magnetic susceptibility calculation for monoclinic α-Pu via LDA+U+SO

## Problem background
α-plutonium exhibits a low-symmetry monoclinic phase with 16 atoms per unit cell and a complex electronic structure shaped by strong spin–orbit coupling and electron–electron correlations. Its magnetic susceptibility has a temperature-independent component and a low-temperature upturn, which together determine the observed magnetic response. Understanding how much the spin and orbital degrees of freedom contribute, and how a small concentration of magnetic impurities modifies the temperature dependence, is essential for interpreting experimental data. This reproduction task computes these contributions from first principles and constructs the total susceptibility curve.

## Approach
The electronic structure of α-Pu is calculated within the LDA+U+SO framework, which includes on-site Coulomb repulsion (Hubbard U) and spin–orbit coupling in a full-matrix, rotationally invariant form. From the self-consistent calculation we extract the partial densities of states at the Fermi level for f, d, and s(p) bands, together with the orbital occupations and degeneracies of the f and d bands. The spin susceptibility is then obtained from exchange-enhanced Pauli formulas for the f and d electrons and the bare Pauli term for s(p) electrons, with an inter-site f–d exchange coupling. The orbital (Van Vleck) susceptibility accounts for multiplet splittings, orbital degeneracies and occupations, and spin-fluctuation corrections. Finally, a Curie-Weiss impurity contribution (Fe with spin S=3/2, Weiss temperature θ = −4 K, concentration 200 ppm) is added to reproduce the low-temperature tail, and the total susceptibility is evaluated from 0 K to 300 K.

## Reproduction target
Perform a self-consistent LDA+U+SO DFT calculation for monoclinic α-Pu (space group P2₁/m, 16 atoms) to obtain the necessary electronic-structure quantities. From these, calculate the spin susceptibility χₛ and the orbital susceptibility χorb, both in emu/mol, and write them into `spin_orbital_susceptibility.json`. Then, using the same χₛ and χorb, compute the impurity Curie-Weiss susceptibility and the total susceptibility χₜₒₜₐₗ = χₛ + χorb + χimp for temperatures from 0 K to 300 K in steps of 10 K. Output the temperature-dependent curve in `total_susceptibility.csv` with columns T(K), chi_pure(emu/mol), chi_imp(emu/mol), chi_total(emu/mol).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Plutonium pseudopotential: SSSP
- Crystal structure of monoclinic α-Pu: 10.1103/PhysRevB.63.174111

## Workflow steps

### Step 1: LDA+U+SO electronic structure calculation
- Role: process
- Action: Perform a self-consistent LDA+U+SO DFT calculation for monoclinic α-Pu (space group P2_1/m, 16 atoms per unit cell) with U_f=4 eV, J_H=0.48 eV, and optionally U_d=2 eV, applying spin-orbit coupling in the full matrix form. From the resulting electronic structure, extract the partial densities of states at the Fermi level for f, d, and s(p) electrons, and the orbital occupations (2n_f, 2n_d) and degeneracies (N_f, N_d) for the f and d bands. Save these extracted quantities in dos_data.json.
- Evidence: `/app/outputs/dos_data.json`

### Step 2: Compute spin and orbital susceptibilities
- Role: scored (load-bearing)
- Action: Read dos_data.json to obtain the partial DOS at the Fermi level. Compute the spin susceptibility χ_s using the exchange-enhanced Pauli formulas for f and d electrons and the bare Pauli term for s(p) electrons, with U_f=4 eV, U_d=2 eV, and inter-site f-d exchange parameter I=0.1 U_f. Compute the orbital Van Vleck susceptibility χ_orb using the modified formula (which incorporates orbital degeneracies, occupations, average multiplet splittings Δ_f=4 eV and Δ_d=15 eV, and spin-fluctuation corrections). Write χ_s and χ_orb with units to spin_orbital_susceptibility.json.
- Output file: `/app/outputs/spin_orbital_susceptibility.json`
- Format: json
- Contract: {"type": "object", "required": ["chi_s", "chi_orb", "units"], "properties": {"chi_s": {"type": "number", "unit": "emu/mol"}, "chi_orb": {"type": "number", "unit": "emu/mol"}, "units": {"type": "string"}}}
- Scoring: scored by hidden verifier

### Step 3: Total susceptibility vs temperature (with impurity)
- Role: scored
- Action: Using χ_s and χ_orb from step 1, compute the impurity Curie-Weiss susceptibility for 200 ppm Fe (S=3/2, g≈2, Weiss temperature θ=-4 K). Calculate the total magnetic susceptibility χ_total = χ_s + χ_orb + χ_imp for temperatures from 0 K to 300 K in steps of 10 K. Output total_susceptibility.csv with columns: T(K), chi_pure(emu/mol), chi_imp(emu/mol), chi_total(emu/mol).
- Output file: `/app/outputs/total_susceptibility.csv`
- Format: csv
- Contract: T(K), chi_pure(emu/mol), chi_imp(emu/mol), chi_total(emu/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_orbital_susceptibility.json`
- `/app/outputs/total_susceptibility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_orbital_susceptibility.json
- path: `/app/outputs/spin_orbital_susceptibility.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static spin and orbital magnetic susceptibility contributions of α-Pu.
- schema:
  - `type`: object
  - `required`: `chi_s`, `chi_orb`, `units`
  - `properties`:
    - `chi_s`:
      - `type`: number
      - `unit`: emu/mol
    - `chi_orb`:
      - `type`: number
      - `unit`: emu/mol
    - `units`:
      - `type`: string

### total_susceptibility.csv
- path: `/app/outputs/total_susceptibility.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total magnetic susceptibility vs temperature (0–300 K) with impurity contribution.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `chi_pure(emu/mol)`, `chi_imp(emu/mol)`, `chi_total(emu/mol)`
  - `units`:
    - `T`: K
    - `chi_pure`: emu/mol
    - `chi_imp`: emu/mol
    - `chi_total`: emu/mol

Notes: The checker compares χ_s and χ_orb to paper-reported values within tolerance, and verifies the total susceptibility curve exhibits a high-temperature plateau and a Curie-Weiss low-temperature rise consistent with the specified impurity parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_orbital_susceptibility.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "chi_s",
          "chi_orb",
          "units"
        ],
        "properties": {
          "chi_s": {
            "type": "number",
            "unit": "emu/mol"
          },
          "chi_orb": {
            "type": "number",
            "unit": "emu/mol"
          },
          "units": {
            "type": "string"
          }
        }
      },
      "description": "Static spin and orbital magnetic susceptibility contributions of α-Pu."
    },
    {
      "file": "total_susceptibility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "chi_pure(emu/mol)",
          "chi_imp(emu/mol)",
          "chi_total(emu/mol)"
        ],
        "units": {
          "T": "K",
          "chi_pure": "emu/mol",
          "chi_imp": "emu/mol",
          "chi_total": "emu/mol"
        }
      },
      "description": "Total magnetic susceptibility vs temperature (0–300 K) with impurity contribution."
    }
  ],
  "notes": "The checker compares χ_s and χ_orb to paper-reported values within tolerance, and verifies the total susceptibility curve exhibits a high-temperature plateau and a Curie-Weiss low-temperature rise consistent with the specified impurity parameters."
}
```

## How you are scored
A hidden verifier independently examines each output artifact. For the static susceptibility file (`spin_orbital_susceptibility.json`) it compares the submitted values against expected results derived from the electronic-structure method employed. For the temperature sweep (`total_susceptibility.csv`) it checks that the overall trend (a nearly constant high-temperature plateau and a Curie-like low-temperature rise) is present and recomputes the impurity susceptibility at several temperatures using the prescribed Curie-Weiss law to verify internal consistency. The final score is a weighted combination of the stage-level results; simply reporting a number without executing the required workflow will not yield a correct solution.
