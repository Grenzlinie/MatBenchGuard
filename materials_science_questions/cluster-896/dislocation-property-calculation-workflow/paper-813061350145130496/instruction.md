# Dislocation Inhomogeneity Contribution Factor f

## Problem background
In crystalline solids, dislocations contribute to the stored elastic energy. When dislocations are distributed randomly and homogeneously, their individual stress fields are long-range and the total energy is essentially the sum of the self-energies of isolated dislocations. In real materials, however, the dislocation density often varies spatially — forming pile‑ups, cell structures, or other mesoscopic inhomogeneities. This spatial modulation introduces an additional coherent interaction term in the energy, which can dominate over the homogeneous‑random contribution. A relative contribution factor f, derived from the structural factor of the dislocation ensemble, quantifies how much larger the energy is compared to the uniformly random case for a given periodic density modulation. This task computes that factor for a specific example.

## Approach
The method builds on a Fourier representation of the deformation field of dislocations in an elastic medium. A locally random distribution is modelled as a random placement modulated by a smooth spatially varying function. The average structural factor is then expressed as the sum of a single‑dislocation term and an interference term that depends on the square of the Fourier component of the modulation. For a one‑dimensional periodic modulation of the linear density n(x) = ⟨n⟩·(1 + a·cos(2π x/l)), the relative contribution of the inhomogeneity reduces to a simple algebraic expression: f = (4·⟨n⟩·(a·l)²) / (3π·ln(d·q_D/(2π))). All parameters in this formula are given public values. The agent implements this formula, computes f, and writes the result to the designated output file. No further modelling or simulation is required; the formula is the full analytical model.

## Reproduction target
Compute the relative contribution factor f using the example parameters provided in the paper: periodic modulation with period l = 5 μm, amplitude a = 0.1, average linear dislocation density ⟨n⟩ = 10¹¹ cm⁻², and the logarithmic factor ln(d·q_D/(2π)) = 5. The result is a single floating‑point number. Write this number into /app/outputs/f_value.txt.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Compute relative inhomogeneity contribution factor f
- Role: scored
- Action: Implement the formula for the relative contribution f of the coherent term in the elastic energy (Eq. 7 of the paper) using the example parameters given in the paper: periodic modulation with period l = 5 μm, amplitude a = 0.1, average dislocation density <n> = 10^11 cm^{-2}, and ln(d q_D / 2π) = 5. Compute the numeric value of f and write it to the output file.
- Output file: `/app/outputs/f_value.txt`
- Format: txt
- Contract: A plain text file containing a single floating-point number (the computed f).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/f_value.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### f_value.txt
- path: `/app/outputs/f_value.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Numerical values of the headline quantities: f from Eq. 7, Δα from Eq. 8, and Hooke's law deviation from Section 6.3.
- schema:
  - `type`: text
  - `description`: Three lines: first line is the relative contribution factor f; second line is the effective surface energy reduction Δα in N/m; third line is the Hooke's law deviation in percent. Each line is a single floating-point number.

Notes: The file contains three lines each with a single float representing the computed f, Δα, and Hooke's law deviation respectively.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "f_value.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Three lines: first line is the relative contribution factor f; second line is the effective surface energy reduction Δα in N/m; third line is the Hooke's law deviation in percent. Each line is a single floating-point number."
      },
      "description": "Numerical values of the headline quantities: f from Eq. 7, Δα from Eq. 8, and Hooke's law deviation from Section 6.3."
    }
  ],
  "notes": "The file contains three lines each with a single float representing the computed f, Δα, and Hooke's law deviation respectively."
}
```

## How you are scored
A hidden verifier will independently recompute f from the same parameters and formula. It will read your submitted /app/outputs/f_value.txt and compare your value to the reference value. Your score for this artifact is the sole reward for the task: full credit if your value lies within an acceptable tolerance that accounts for minor implementation differences, and zero otherwise. The reference value and the exact tolerance are not disclosed. Reporting a number that matches the reference within the expected tolerance is required to pass.
