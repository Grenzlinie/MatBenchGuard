# Computation of Defect-Induced Short-Range Force Constant Change Using Lattice Green's Functions

## Problem background
When a substitutional impurity occupies a lattice site in an ionic crystal, the local vibrational spectrum can exhibit new modes (local, gap, or resonance) distinct from those of the perfect host. These modes are sensitive to both the mass of the impurity and the changes it induces in the short-range interactions with its neighbours. The lattice Green's function technique provides a powerful framework for studying such defects: the perturbed crystal's equations of motion are recast in terms of the perfect-lattice Green function G and a perturbation matrix J. For an impurity interacting with its six nearest neighbours (forming an XY₆ complex with Oₕ symmetry), the vibration problem reduces to a 21×21 determinantal condition |I − G J| = 0. The perturbation J includes the mass change at the defect site and the modification of the nearest-neighbour short-range overlap force constant A while neglecting changes in the companion parameter B. By fitting the experimentally observed infrared-active local-mode frequency, one can extract the change ΔA in that force constant, quantifying the softening or stiffening of the host–impurity bond.

## Approach
The task is carried out in two computational stages. First, the 14 independent scalar entries g₀…g₁₃ of the perfect-lattice Green function for the XY₆ defect subspace are computed at the target frequency ω = 563 cm⁻¹. This is done by evaluating the standard real-space expression for the Green function (a sum over phonon wavevectors and branches) using the NaCl shell-model force-constant parameters of Raunio & Rolandson (1970). The resulting gᵢ values are saved in a text file.

Second, the F1u mode condition – obtained by block-diagonalising the 21×21 determinant with symmetry coordinates appropriate to the Oₕ point group – is used to solve for ΔA. For a substitutional negative impurity on the cation site (e.g. H⁻ substituting Na⁺) the condition reads
  1 − εM ω² g₀ − ΔA(2g₀ + g₁ − 4g₂ + g₇) − εM ω² (g₁ g₀ + g₀ g₇ − 2 g₂²) = 0
where εM = M_host − M_defect, M_host is the mass of Na, M_defect is the mass of H, and ω = 563 cm⁻¹. The perfect-lattice short-range parameter A = 9.77 (in units of e²/(2V)) is known from the same shell-model reference. Solving the linear equation yields ΔA, and the fractional softening is reported as |ΔA|/A × 100.

## Reproduction target
Produce the file `delta_A_fit.csv` containing the fitted change in the nearest-neighbour short-range force constant for NaCl:H⁻. The CSV must have two columns:
- `Delta_A` – the value of ΔA in units of e²/(2V).
- `Softening_Pct` – the percentage softening computed as |ΔA|/A × 100 (A = 9.77).
The ΔA value must be obtained from the computational workflow described above (Green-function evaluation followed by solving the F1u condition); it must not be guessed or copied from an external source.

## Assets

- NaCl shell-model parameters from Raunio & Rolandson (1970): https://doi.org/10.1103/PhysRevB.2.2098
- Observed local-mode frequency for NaCl:H⁻ (563 cm⁻¹) from Schaefer (1960): https://doi.org/10.1016/0022-3697(60)90073-X

## Workflow steps

### Step 1: Compute perfect-lattice Green function elements at target frequency
- Role: process
- Action: Using the NaCl shell-model parameters (Raunio & Rolandson 1970), evaluate the 14 independent Green-function scalar entries g₀(ω²) to g₁₃(ω²) defined for the seven-atom XY₆ defect subspace. Perform the required Brillouin-zone sum on a sufficiently dense mesh at the observed frequency ω = 563 cm⁻¹. Save the resulting numeric values in order g₀, g₁, …, g₁₃, one per line, in a plain-text file.
- Evidence: `/app/outputs/g_values.txt`

### Step 2: Solve F1u mode equation for ΔA and compute softening
- Role: scored (load-bearing)
- Action: Load the Green-function values from the previously produced g_values.txt. For the negative substitutional impurity case, use the host mass (Na), defect mass (H), mass difference εM, the observed frequency 563 cm⁻¹, and the F1u mode condition (a scalar algebraic equation derived from block-diagonalization of the 21×21 determinantal condition) to solve for the change ΔA in the nearest-neighbour short-range overlap parameter A. Take the perfect-lattice A parameter (9.77 in units of e²/(2V)) from the shell-model reference and compute the percentage softening as |ΔA|/A × 100. Write the fitted ΔA and the softening percentage to a CSV file.
- Output file: `/app/outputs/delta_A_fit.csv`
- Format: csv
- Contract: CSV with header: Delta_A, Softening_Pct. One data row. Delta_A is a float in units of e²/(2V); Softening_Pct is a non-negative float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_A_fit.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_A_fit.csv
- path: `/app/outputs/delta_A_fit.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fitted change in nearest-neighbour short-range force constant ΔA (in e²/(2V)) and the corresponding softening percentage relative to the perfect-lattice A parameter (9.77).
- schema:
  - `type`: table
  - `required_columns`: `Delta_A`, `Softening_Pct`
  - `units`:
    - `Delta_A`: e^2/(2V)
    - `Softening_Pct`: percentage

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_A_fit.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Delta_A",
          "Softening_Pct"
        ],
        "units": {
          "Delta_A": "e^2/(2V)",
          "Softening_Pct": "percentage"
        }
      },
      "description": "Fitted change in nearest-neighbour short-range force constant ΔA (in e²/(2V)) and the corresponding softening percentage relative to the perfect-lattice A parameter (9.77)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `delta_A_fit.csv` and compares the reported `Delta_A` to a reference value (the accepted result for this system) within a tolerance that accommodates the numerical spread arising from different choices of Brillouin-zone mesh and integration scheme. The verifier also checks that `Softening_Pct` is consistent with your `Delta_A` and the fixed A = 9.77. The final reward is a weighted sum over all scored workflow stages; the fitted ΔA (Step 2) carries the largest share. Providing a number without genuinely executing the required Green-function calculation will not match the hidden reference and will result in a low score.
