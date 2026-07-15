# Compute temperature-dependent Young's modulus of P-doped silicon nanowires from Keating model

## Problem background
Silicon nanowires are candidate building blocks for nanoelectromechanical systems (NEMS). As device dimensions shrink, the mechanical properties of nanowires become size-dependent, and their elasticity can also change with doping and temperature. Understanding how Young's modulus of a phosphorus-doped silicon nanowire depends on the nanowire cross-section size, doping concentration, and temperature is critical for reliable design. This task addresses the computational prediction of Young's modulus for P-doped Si (001) nanowires along the [100] direction using a semi-continuum model.

## Approach
The semi-continuum method treats the nanowire as a periodic array of crystal cells, each containing a tetrahedral bond network. The strain energy of each tetrahedron is described by the Keating valence-force model, with separate bond-stretching (k_b) and bond-bending (k_θ) force constants for Si-Si and P-Si bonds. For a given nanowire size N (number of crystal-cell layers along each transverse direction) and doping concentration α (fraction of cells containing a P atom), the total strain energy is summed over the cross-section. The Young's modulus E along the nanowire length (x direction) is then obtained from the stress-strain relation σ_xx = ∂f/∂ε_xx, where f is the strain energy density and ε_xx is the axial strain.

At zero temperature, the force constants are taken as the equilibrium values. To include temperature effects, the lattice parameter a(T) of silicon is used: as temperature increases the bond length r = √3 a/4 increases, and the force constants are scaled anharmonically according to k_b = k_b^0 (r_0/r)^4 and k_θ = k_θ^0 (r_0/r)^7, where r_0 is the zero-temperature bond length. The temperature-dependent lattice parameter a(T) is provided as a digitised table covering 0 K to 1000 K. The computation is repeated for a grid of N, α, and T values to map the combined size, doping, and temperature dependence of Young's modulus.

## Reproduction target
Compute Young's modulus E (in GPa) of the P-doped Si (001) nanowire for every combination of:
- nanowire size N ∈ {1,2,3,4,5,6,7,8,9,10,20,50,100} (where width = thickness = (4N+1)a),
- doping concentration α ∈ {0, 0.01, 0.1, 1},
- temperature T ∈ {0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000} K.
Write the results to a single CSV file with columns N, α, T, E.

## Assets

- Keating model force constants for Si and P-Si bonds
- Temperature-dependent lattice parameter a(T) for silicon: The digitised a(T) values from Fig. 4 of the paper, mapping temperature to the silicon lattice parameter (in Å). Use these values for computing bond length and anharmonic scaling at T>0.

```csv
T,a
0,1.3575
100,1.357853
200,1.358206
300,1.358559
400,1.358912
500,1.359265
600,1.359618
700,1.359971
800,1.360324
900,1.360677
1000,1.36103
```

## Workflow steps

### Step 1: Compute Young's modulus of P-doped Si nanowire
- Role: scored (load-bearing)
- Action: Implement the analytic Keating model formula for the Young's modulus of a P-doped Si (001) nanowire along [100] direction, using the provided force constants and lattice parameter. For each combination of nanowire size N (integer number of crystal-cell layers along each transverse direction), doping concentration alpha (0, 0.01, 0.1, 1), and temperature T (0 K, then 100 to 1000 K step 100 K) compute the bond-length-dependent anharmonic scaling for force constants using the temperature-dependent lattice parameter a(T) from the provided table, and calculate Young's modulus E in GPa. Write all results to a CSV file.
- Output file: `/app/outputs/step_01_youngs_modulus.csv`
- Format: csv
- Contract: CSV with columns: N (integer, number of crystal-cell layers along transverse directions), alpha (float, doping fraction between 0 and 1), T (float, temperature in K), E (float, Young's modulus in GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_youngs_modulus.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_youngs_modulus.csv
- path: `/app/outputs/step_01_youngs_modulus.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed Young's modulus for all specified (N, alpha, T) combinations.
- schema:
  - `type`: table
  - `required_columns`: `N`, `alpha`, `T`, `E`
  - `units`:
    - `E`: GPa

Notes: The quasiharmonic lattice parameter a(T) is provided as a bundled input table; the solving agent is not required to perform the quasiharmonic phonon calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_youngs_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "alpha",
          "T",
          "E"
        ],
        "units": {
          "E": "GPa"
        }
      },
      "description": "Computed Young's modulus for all specified (N, alpha, T) combinations."
    }
  ],
  "notes": "The quasiharmonic lattice parameter a(T) is provided as a bundled input table; the solving agent is not required to perform the quasiharmonic phonon calculation."
}
```

## How you are scored
A hidden automated verifier will read your output CSV and compare your computed E values against expected values for a subset of (N,α,T) combinations. The comparison allows a relative tolerance to account for numerical differences. In addition, the verifier checks that your results satisfy the expected physical trends: for fixed doping and temperature, E decreases as N decreases; for fixed N and doping, E decreases as T increases. The verifier does not require re-running your computation; it only inspects the CSV file. Your submission will be scored based on agreement with the expected values and correct monotonic trends.
