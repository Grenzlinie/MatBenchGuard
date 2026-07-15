# Vacancy Formation Enthalpy Calculation via Macroscopic Cavity Model for Compound Semiconductors

## Problem background
In diamond-type semiconductors, a neutral vacancy can be treated as a macroscopic cavity: its formation enthalpy is approximated by the surface area of the cavity times its surface energy. This model splits the surface energy into a long-range metallic contribution (estimated from the liquid surface tension via the Schmit–Lucas theory) and a short-range covalent, broken-bond contribution. For compound AB crystals with zinc-blende or wurtzite structure, both cation (A) and anion (B) vacancies exist. The cavity sizes are proportional to the tetrahedral covalent radii of the constituents, differing between A and B, while the covalent bond-energy contribution is identical for both. Your task is to compute the neutral vacancy virtual-formation enthalpies ΔH(V_Aˣ) and ΔH(V_Bˣ) for a set of 17 common compound semiconductors using this extended macroscopic cavity model.

## Approach
The calculation follows the macroscopic cavity model extended to AB crystals. First, the metallic liquid surface enthalpy H_Sˡ is computed for each compound from the Schmit–Lucas theory using the same parameters as for Si (surface plasmon cutoff, density change factor 1.153, surface entropy 0.09 erg/cm²·K), evaluated at the compound's melting temperature. This enthalpy is then converted to the metallic contribution of the (111) surface energy via E_Sᵐ(111) = H_Sˡ / (1.153)^{5/6}. Next, the cavity geometry is obtained from tetrahedral covalent radii r_c(A) and r_c(B) taken from the Van Vechten & Phillips table. Effective Wigner–Seitz radii are calculated as r_w = 1.433 r_c, and the octahedral cavity surface areas Ω_S are computed as 1.1826 × 4π r_w². The covalent bond energy E_b(AB) at the melting point is retrieved from Van Vechten (1973), giving a broken-bond contribution of 4E_b. Finally, the formation enthalpies are ΔH(V_Aˣ) = Ω_S(A) E_Sᵐ(111) + 4E_b and ΔH(V_Bˣ) = Ω_S(B) E_Sᵐ(111) + 4E_b. The workflow carries out these five stages, writing intermediate evidence files before producing the final enthalpy table.

## Reproduction target
Compute the neutral vacancy formation virtual-enthalpies ΔH(V_Aˣ) and ΔH(V_Bˣ) for each of the 17 zinc-blende/wurtzite semiconductors: SiC, AlAs, AlSb, GaN, GaP, GaAs, GaSb, InP, InAs, InSb, ZnO, ZnS, ZnSe, ZnTe, CdS, CdSe, CdTe. Write the results to a CSV file with columns: compound, V_A_enthalpy (eV), V_B_enthalpy (eV). All intermediate evidence files must also be written, and the final CSV must contain exactly 17 rows, one per compound.

## Assets

- Van Vechten and Phillips (1970) tetrahedral covalent radii: https://doi.org/10.1103/PhysRevB.2.2160
- Van Vechten (1973) covalent bond energies E_b(T): https://doi.org/10.1103/PhysRevB.7.1479
- Schmit–Lucas liquid surface energy theory: https://doi.org/10.1016/0038-1098(72)90613-9
- Melting points of the 17 compounds

## Workflow steps

### Step 1: Liquid metallic surface enthalpy calculation
- Role: process
- Action: For each of the 17 compounds, compute the metallic liquid surface enthalpy H_S^l using the Schmit–Lucas theory with the same parameters as for Si: surface plasmon cutoff as for Si, density change factor of 1.153, surface entropy S_S^l = 0.09 erg/cm²·K. Use the compound's melting temperature T^F. Record the computed values.
- Evidence: `/app/outputs/step_01_liquid_surface_enthalpy.csv`

### Step 2: Effective solid surface energy E_S^m(111)
- Role: process
- Action: For each compound, convert H_S^l to the metallic contribution of the (111) surface energy using E_S^m(111) = H_S^l / (1.153)^{5/6}. Record the values.
- Evidence: `/app/outputs/step_02_ES_m.csv`

### Step 3: Cavity dimensions from covalent radii
- Role: process
- Action: For the 17 compounds, retrieve the tetrahedral covalent radii r_c(A) and r_c(B) from the Van Vechten and Phillips table. Compute effective Wigner‑Seitz radii: r_w(A) = 1.433 * r_c(A) and r_w(B) = 1.433 * r_c(B). Compute octahedral cavity surface areas: Ω_S(A) = 1.1826 * 4π * r_w(A)^2, and similarly for B. Record the areas.
- Evidence: `/app/outputs/step_03_cavity_areas.csv`

### Step 4: Covalent bond energy retrieval
- Role: process
- Action: Retrieve the covalent bond energy E_b(AB) for each compound at the melting point T^F from the Van Vechten (1973) table. Compute the covalent contribution 4 * E_b(AB). Record the values.
- Evidence: `/app/outputs/step_04_covalent_contributions.csv`

### Step 5: Formation enthalpies
- Role: scored (load-bearing)
- Action: For each compound, compute ΔH(V_A^x) = Ω_S(A) * E_S^m(111) + 4E_b(AB) and ΔH(V_B^x) = Ω_S(B) * E_S^m(111) + 4E_b(AB). Write the results to a CSV file with columns: compound, V_A_enthalpy (eV), V_B_enthalpy (eV).
- Output file: `/app/outputs/step_01_formation_enthalpies.csv`
- Format: csv
- Contract: compound (string), V_A_enthalpy (float, eV), V_B_enthalpy (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_enthalpies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_enthalpies.csv
- path: `/app/outputs/step_01_formation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed neutral vacancy formation virtual enthalpies ΔH(V_A^x) and ΔH(V_B^x) for the 17 zinc-blende/wurtzite semiconductors listed in the paper. The checker compares each value to the paper's Table II entries within a predetermined tolerance.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `V_A_enthalpy`, `V_B_enthalpy`
  - `units`:
    - `V_A_enthalpy`: eV
    - `V_B_enthalpy`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "V_A_enthalpy",
          "V_B_enthalpy"
        ],
        "units": {
          "V_A_enthalpy": "eV",
          "V_B_enthalpy": "eV"
        }
      },
      "description": "Computed neutral vacancy formation virtual enthalpies ΔH(V_A^x) and ΔH(V_B^x) for the 17 zinc-blende/wurtzite semiconductors listed in the paper. The checker compares each value to the paper's Table II entries within a predetermined tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects your output files. Each workflow step’s evidence is checked for correct execution, and the final scored artifact is compared to independently evaluated reference values. The verifier aggregates these comparisons into a single reward score. Producing the expected output files with values that agree closely with the reference yields the highest reward. You do not need to know the reference values; carrying out the prescribed computation with due care is the way to achieve a good score.
