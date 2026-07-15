# Static vacancy properties in fcc noble-gas crystals (6-10 potential)

## Problem background
Studying the structure of a point defect (vacancy) in a face-centered cubic noble-gas crystal at static conditions (zero temperature). The atoms interact via a short-range central pair potential of the form 6-10 (σ [(b/R)^10 - (b/R)^6]) and interactions are truncated beyond first and second nearest neighbors. The presence of a vacancy induces small but anisotropic radial displacements of the surrounding atoms and a net volume change, as well as a displacement energy. Computing these quantities from first principles using a variational approach that couples an atomistic region near the vacancy to an elastic continuum provides a well-defined, self-contained problem; the results are characteristic of the material and the potential parameters. For argon and krypton, with known potential parameters, the static displacements, volume change, and displacement energy can be obtained by solving the equilibrium equations that follow from minimizing the total potential energy of the crystal containing the vacancy.

## Approach
The crystal is divided into two regions: an atomistic core containing the vacancy and several coordination shells of neighbors, and the remaining crystal treated as an anisotropic elastic continuum. In the atomistic region, the radial displacement of each symmetry-equivalent shell (first, second, third) is treated as an independent variational parameter. The continuum region is described by a radial displacement ansatz with two parameters that approximately satisfies the equilibrium conditions of the elastic continuum. The total potential energy of the system (atomistic interactions, interaction between atomistic and continuum regions, and elastic energy of the continuum) is written as a function of these parameters. Minimization yields a system of linear equations whose solution gives the equilibrium radial displacements of the atomistic shells and the continuum parameters. From these, the volume change and displacement energy are computed. For the static case (zero temperature and neglecting zero-point energy), the calculation depends only on the first and second derivatives of the potential at the ideal lattice sites, the lattice geometry, and the elastic constants derived from the same potential. The required potential parameters σ and b for argon and krypton are provided below so that the entire computation is self-contained. The third approximation (atomistic region up to the third coordination shell, continuum ansatz II) is the target accuracy level.

## Reproduction target
Compute the static radial displacements s_100, s_200, and s_211 (expressed as a percentage of the nearest-neighbor distance a0/√2 in the ideal fcc lattice), the vacancy-induced volume change ΔV (expressed as a percentage of the atomic volume a0³/4), and the displacement energy ΔE (expressed in units of 10⁻⁴ eV) for both argon and krypton. These quantities must be calculated using the third approximation: atomistic region up to the third coordination shell and the two-parameter continuum ansatz (II). Provide the results in a CSV file with the specified format. The potential parameters (σ, b) for argon and krypton are fixed as:
- Argon: b = 3.40 × 10⁻⁸ cm, σ = 6.46 × 10⁻² eV
- Krypton: b = 3.58 × 10⁻⁸ cm, σ = 9.05 × 10⁻² eV
Use the equilibrium condition that relates the first derivatives of the potential at first and second neighbor distances (derived from the static equilibrium of the ideal fcc lattice) to determine the lattice constant a0 self-consistently with the given parameters.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute static vacancy properties
- Role: scored (load-bearing)
- Action: Implement the variational model for a vacancy in an fcc lattice with the 6-10 pair potential, truncated to first and second nearest neighbours. Solve the equilibrium equations for the third approximation (atomistic region up to third coordination shell, continuum ansatz II) to obtain radial displacements s_100, s_200, s_211 (in % of a0/√2), volume change ΔV (in % of a0³/4), and displacement energy ΔE (in 10⁻⁴ eV). Run for Argon and Krypton using the potential parameters provided in the instruction. Write the results to static_results.csv.
- Output file: `/app/outputs/static_results.csv`
- Format: csv
- Contract: CSV with columns: material (string), s100_percent (float), s200_percent (float), s211_percent (float), deltaV_percent (float), deltaE_10minus4eV (float). Two rows, one per material.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_results.csv
- path: `/app/outputs/static_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Static radial displacements, volume change, and displacement energy for Ar and Kr in the third approximation (atomistic region up to third coordination shell, continuum ansatz II).
- schema:
  - `type`: table
  - `required_columns`: `material`, `s100_percent`, `s200_percent`, `s211_percent`, `deltaV_percent`, `deltaE_10minus4eV`
  - `units`:
    - `s100_percent`: % of a0/√2
    - `s200_percent`: % of a0/√2
    - `s211_percent`: % of a0/√2
    - `deltaV_percent`: % of a0³/4
    - `deltaE_10minus4eV`: 10⁻⁴ eV

Notes: The checker compares the values to the paper’s reported third‑approximation numbers with tolerances; exact reproduction of the paper’s table entries is expected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "s100_percent",
          "s200_percent",
          "s211_percent",
          "deltaV_percent",
          "deltaE_10minus4eV"
        ],
        "units": {
          "s100_percent": "% of a0/√2",
          "s200_percent": "% of a0/√2",
          "s211_percent": "% of a0/√2",
          "deltaV_percent": "% of a0³/4",
          "deltaE_10minus4eV": "10⁻⁴ eV"
        }
      },
      "description": "Static radial displacements, volume change, and displacement energy for Ar and Kr in the third approximation (atomistic region up to third coordination shell, continuum ansatz II)."
    }
  ],
  "notes": "The checker compares the values to the paper’s reported third‑approximation numbers with tolerances; exact reproduction of the paper’s table entries is expected."
}
```

## How you are scored
A hidden verifier reads your CSV file and compares each numerical value to reference values using appropriate tolerances. The score is a combination of the accuracy for argon and krypton; each material contributes equally. The file must contain exactly the required columns and two rows. Formatting errors (missing columns, extra columns, wrong delimiter) will result in a reduction of the score, possibly to zero. A value that is outside its tolerance for a given material will cause that material’s sub-score to be zero. The verifier does not examine any other files; only the CSV artifact is scored.
