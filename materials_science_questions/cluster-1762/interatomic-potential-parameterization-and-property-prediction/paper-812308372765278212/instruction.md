# Compute Wurtzite Lattice Sums (Ewald Method)

## Problem background
Wurtzite-type binary compounds often exhibit small deviations of the lattice parameters c/a and internal displacement u from the ideal close-packed values. A macroscopic theory attributes these distortions to long-range electrostatic forces arising from partial ionic charges on the atoms. A key computational step in the theory is evaluating certain infinite lattice sums for the ideal wurtzite structure: the anisotropic Madelung constants α^11, α^33 and the internal ionic field coefficient, which enter the equilibrium equations that determine the distortion. These sums are evaluated using the Ewald summation technique, which converts slowly convergent real-space sums into rapidly converging sums over both direct and reciprocal lattices.

## Approach
Implement the Ewald summation method for the ideal wurtzite crystal. The unit cell contains four ions: two with effective charge +f e at fractional coordinates (1/3, 2/3, 0) and (2/3, 1/3, 1/2); two with charge −f e at (1/3, 2/3, u) and (2/3, 1/3, u+1/2) with u = 0.375. The lattice constants are a = 1 (relative units) and c = √(8/3) ≈ 1.633. Following the standard Ewald method, split each sum into two parts using a convergence parameter: one sum over the direct lattice involving φₘ functions and a second sum over the reciprocal lattice that depends on the structure factor and the reciprocal lattice vectors. Compute the required lattice sums: α^11 = α^22 from the second derivative of the Madelung sum with respect to k₁, α^33 from the second derivative with respect to k₃, the total Madelung constant α = 2α^11 + α^33, and the internal field coefficient such that E_I = coefficient × f e / c², obtained from the first derivative with respect to k₃. Use the standard φ functions defined by integral representations and their recurrences, and evaluate the sums to convergence by choosing the Ewald splitting parameter appropriately.

## Reproduction target
Produce a JSON file containing the four computed numeric values: (1) α^11, (2) α^33, (3) the internal field coefficient, and (4) the total Madelung constant α = α^11 + α^22 + α^33, with α^22 = α^11. All values correspond to the ideal wurtzite geometry described above, with the specified charge distribution and lattice parameters. The sum over the infinite lattice must be performed via the Ewald method; no finite-size cutoffs are permitted. The output file must be named lattice_sums.json and placed under /app/outputs.

## Assets
No external datasets, models, or pre‑computed tables are required. The crystal structure and charge distribution are given in the task description, and the Ewald method is a standard technique that can be implemented from first principles. The only software needed consists of publicly available scientific computing libraries (e.g., NumPy, SciPy, or equivalent) which can be installed from PyPI or via the system package manager. The paper itself is not provided and must not be consulted.

## Workflow steps

### Step 1: Compute Lattice Sums via Ewald Method
- Role: scored (load-bearing)
- Action: Implement the Ewald summation technique for the ideal wurtzite crystal structure. The unit cell contains four ions: two with effective charge +f e at fractional coordinates (1/3, 2/3, 0) and (2/3, 1/3, 1/2), two with charge -f e at (1/3, 2/3, u) and (2/3, 1/3, u+1/2) with u=0.375. The lattice constants are a=1 (relative) and c=√(8/3)≈1.633. Use the standard Ewald splitting, φ functions, structure factor, and reciprocal lattice vectors to compute the following lattice sums: α^11 (=α^22) via the method for anisotropic Madelung sums, α^33, the internal ionic field coefficient such that E_I = coefficient × f e / c², and the total Madelung constant (as a positive number, i.e., the absolute value of the sum α^11+α^22+α^33, with α^22 = α^11). Save these four numeric values in the output file.
- Output file: `/app/outputs/lattice_sums.json`
- Format: json
- Contract: {"type": "object", "required": ["alpha11", "alpha33", "EI_coefficient", "madelung_constant"], "properties": {"alpha11": {"type": "number", "description": "Anisotropic Madelung sum α^11 = α^22"}, "alpha33": {"type": "number", "description": "Anisotropic Madelung sum α^33"}, "EI_coefficient": {"type": "number", "description": "Coefficient such that E_I = coeff × f e / c²"}, "madelung_constant": {"type": "number", "description": "Total Madelung constant (positive, absolute value of the sum α^11+α^22+α^33)"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_sums.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_sums.json
- path: `/app/outputs/lattice_sums.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed lattice sums for ideal wurtzite: α^11, α^33, E_I coefficient, and positive Madelung constant.
- schema:
  - `type`: object
  - `required`: `alpha11`, `alpha33`, `EI_coefficient`, `madelung_constant`
  - `properties`:
    - `alpha11`:
      - `type`: number
      - `description`: Anisotropic Madelung sum α^11 = α^22
    - `alpha33`:
      - `type`: number
      - `description`: Anisotropic Madelung sum α^33
    - `EI_coefficient`:
      - `type`: number
      - `description`: Coefficient such that E_I = coeff × f e / c²
    - `madelung_constant`:
      - `type`: number
      - `description`: Total Madelung constant (positive, absolute value of the sum α^11+α^22+α^33)

Notes: The Madelung constant must be reported as a positive number (absolute value).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_sums.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "alpha11",
          "alpha33",
          "EI_coefficient",
          "madelung_constant"
        ],
        "properties": {
          "alpha11": {
            "type": "number",
            "description": "Anisotropic Madelung sum α^11 = α^22"
          },
          "alpha33": {
            "type": "number",
            "description": "Anisotropic Madelung sum α^33"
          },
          "EI_coefficient": {
            "type": "number",
            "description": "Coefficient such that E_I = coeff × f e / c²"
          },
          "madelung_constant": {
            "type": "number",
            "description": "Total Madelung constant (positive, absolute value of the sum α^11+α^22+α^33)"
          }
        }
      },
      "description": "Computed lattice sums for ideal wurtzite: α^11, α^33, E_I coefficient, and positive Madelung constant."
    }
  ],
  "notes": "The Madelung constant must be reported as a positive number (absolute value)."
}
```

## How you are scored
A hidden checker independently inspects your /app/outputs/lattice_sums.json. It compares the four reported numbers (α^11, α^33, the internal field coefficient, and the Madelung constant) to gold values derived from the original work, using pre‑set absolute tolerances. Each value that falls within its tolerance earns a portion of the total reward, and the partial rewards are summed to produce the final score. Reporting a number without genuine Ewald summation will be detected because the gold values are not disclosed in the task. Be sure to output the exact object structure specified in the output contract.
