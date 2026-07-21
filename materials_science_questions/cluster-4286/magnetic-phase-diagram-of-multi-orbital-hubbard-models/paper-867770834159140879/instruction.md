# Antiferromagnetic fluctuations and dxy-wave pairing symmetry in a two-band Hubbard model

## Problem background
The recent discovery of superconductivity in nickelate-based materials has sparked intense interest in the pairing symmetry, magnetic correlations, and charge order of these systems. An effective two-band Hubbard model derived from first-principles electronic structure captures the essential low-energy physics of the nickel square lattice. Quantum Monte Carlo simulations can provide unbiased insights into these competing orders. The present task requires computing several key quantities from this model using determinant quantum Monte Carlo (DQMC): the spin susceptibility peak as a function of Hubbard U and electron filling, pairing susceptibilities for multiple symmetries and the associated effective pairing interaction, finite-size scaling of the antiferromagnetic structure factor to assess long-range order, and density-density correlations with nearest-neighbor repulsion to probe charge density wave tendencies.

## Approach
The approach is to implement the two-band Hubbard model with the tight-binding parameters at kz=0 (on-site energies, intra- and inter-sublattice hoppings) and a determinant quantum Monte Carlo (DQMC) simulation engine. DQMC expresses the partition function as a path integral over auxiliary fields and uses Monte Carlo sampling to evaluate observables. The solver must compute spin susceptibility χ(q), pairing susceptibilities for four pairing symmetries (s_xy, d_xy, s_x²+y², d_x²-y²), the effective pairing interaction by subtracting the uncorrelated single-particle contribution, the AFM spin structure factor on the B sublattice, and the density-density correlation function and its Fourier transform. Simulations are run on finite lattices (up to 2×12² sites) at specified Hubbard U, fillings, and temperatures, with periodic boundary conditions.

## Reproduction target
Compute the static spin susceptibility χ(q) at q=(π,π) on a 2×8² lattice at T/t=1/10 for on-site Hubbard U/t = 1.0, 3.0, 5.0 and electron fillings ⟨n⟩ = 1.0, 0.9, 0.8, and save the results in a JSON file. Compute the pairing susceptibilities P and effective pairing interactions P_eff for the four symmetries as a function of temperature (T/t from about 0.5 down to 0.125) at U/t=3.0 on the same lattice size for two fillings (⟨n⟩=1.0 and 0.8), and save the results. Compute the AFM structure factor S_AFM for linear lattice sizes L=8, 10, 12 at U/t=3.0, ⟨n⟩=1.0, and inverse temperature β=10, and save the values. Finally, compute the charge density wave correlation C(q) at q=(π,π) on a 2×12² lattice with nearest-neighbor repulsion V/t=0.9, U/t=3.0, ⟨n⟩=1.0, and T/t=1/6, and save the single-point result.

## Assets

- Python: python3
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Implement two-band Hubbard model and DQMC solver
- Role: process
- Action: Implement the two-band Hubbard model Hamiltonian with tight-binding parameters for kz=0 (on-site energies, intra- and inter-sublattice hoppings) and a determinant quantum Monte Carlo (DQMC) simulation engine. The engine must be capable of computing spin susceptibility χ(q), pairing susceptibilities for multiple symmetries, AFM spin structure factor, and density-density correlations at finite temperature on lattices up to 2×12^2.
- Evidence: `/app/outputs/step_00_dqmc_implementation.log`

### Step 2: Compute spin susceptibility χ(q) peak at (π,π)
- Role: scored
- Action: Run DQMC simulations on a 2×8² lattice at T/t=1/10 for U/t ∈ {1.0, 3.0, 5.0} and fillings ⟨n⟩ ∈ {1.0, 0.9, 0.8} with kz=0. Extract the static spin susceptibility χ(q) value at q=(π,π).
- Output file: `/app/outputs/step_01_chi_peak.json`
- Format: json
- Contract: Array of objects, each with keys: U_t (float, Hubbard U in units of t), n (float, electron filling), chi_pi_pi (float, χ(π,π) value).
- Scoring: scored by hidden verifier

### Step 3: Compute pairing susceptibilities and effective pairing interaction
- Role: scored (load-bearing)
- Action: Run DQMC simulations on a 2×8² lattice with U/t=3.0, kz=0, for temperatures T/t covering a range from about 0.5 down to 0.125, separately for fillings ⟨n⟩=1.0 and 0.8. For each temperature, compute the pairing susceptibilities P_α for the four symmetries s_xy, d_xy, s_{x²+y²}, d_{x²-y²} and the uncorrelated single-particle contributions to obtain the effective pairing interaction P_eff = P_α − P̃_α.
- Output file: `/app/outputs/step_02_pairing_suscept.json`
- Format: json
- Contract: Array of objects, each with keys: temperature (float, T/t), symmetry (string, one of 'sxy','dxy','sx2+y2','dx2-y2'), P (float), P_eff (float), n (float, filling 1.0 or 0.8).
- Scoring: scored by hidden verifier

### Step 4: Compute AFM structure factor finite-size scaling
- Role: scored
- Action: Run DQMC simulations on lattices of linear sizes L=8, 10, 12 (total sites N_s=2×L²) at U/t=3.0, filling ⟨n⟩=1.0, kz=0, at inverse temperature β=10. Compute the AFM spin structure factor S_AFM on the B sublattice.
- Output file: `/app/outputs/step_03_AFM_structure_factor.json`
- Format: json
- Contract: Array of objects, each with keys: L (int), beta (float), U_t (float, 3.0), n (float, 1.0), S_AFM (float).
- Scoring: scored by hidden verifier

### Step 5: Compute charge density wave correlation at q=(π,π)
- Role: scored
- Action: Run DQMC simulations on a 2×12² lattice with nearest-neighbor repulsion V/t=0.9, U/t=3.0, filling ⟨n⟩=1.0, T/t=1/6, kz=0. Compute the density-density correlation C(R) and its Fourier transform C(q), and extract the value at q=(π,π).
- Output file: `/app/outputs/step_04_CDW_charge_correlation.json`
- Format: json
- Contract: Object with keys: V_t (float, 0.9), U_t (float, 3.0), n (float, 1.0), L (int, 12), T_t (float, 0.1667), C_pi_pi (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_chi_peak.json`
- `/app/outputs/step_02_pairing_suscept.json`
- `/app/outputs/step_03_AFM_structure_factor.json`
- `/app/outputs/step_04_CDW_charge_correlation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_chi_peak.json
- path: `/app/outputs/step_01_chi_peak.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin susceptibility peak values for various U and fillings. Checker compares to hidden paper-reported values with relative tolerance and verifies monotonic trends (χ increases with U at fixed n; χ increases with doping at fixed U).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `U_t`, `n`, `chi_pi_pi`
    - `properties`:
      - `U_t`:
        - `type`: number
        - `description`: Hubbard U in units of t
      - `n`:
        - `type`: number
        - `description`: electron filling
      - `chi_pi_pi`:
        - `type`: number
        - `description`: χ(q) at q=(π,π)

### step_02_pairing_suscept.json
- path: `/app/outputs/step_02_pairing_suscept.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pairing susceptibilities and effective interactions for U/t=1.0,3.0,5.0 at n=1.0 and U/t=3.0 at n=0.8. Checker verifies that dxy dominates, P_eff increases with decreasing T, and P_eff increases with U at low T.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `temperature`, `symmetry`, `P`, `P_eff`, `n`, `U_t`
    - `properties`:
      - `temperature`:
        - `type`: number
        - `description`: T/t
      - `symmetry`:
        - `type`: string
        - `enum`: `sxy`, `dxy`, `sx2+y2`, `dx2-y2`
      - `P`:
        - `type`: number
      - `P_eff`:
        - `type`: number
      - `n`:
        - `type`: number
        - `description`: electron filling (1.0 or 0.8)
      - `U_t`:
        - `type`: number
        - `description`: Hubbard U in units of t (1.0, 3.0, or 5.0)

### step_03_AFM_structure_factor.json
- path: `/app/outputs/step_03_AFM_structure_factor.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: AFM structure factor for finite-size scaling. Checker verifies monotonic decrease of S_AFM as L increases (L=8→10→12) at β=10.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `L`, `beta`, `U_t`, `n`, `S_AFM`
    - `properties`:
      - `L`:
        - `type`: integer
      - `beta`:
        - `type`: number
        - `description`: inverse temperature 1/T
      - `U_t`:
        - `type`: number
        - `const`: 3.0
      - `n`:
        - `type`: number
        - `const`: 1.0
      - `S_AFM`:
        - `type`: number

### step_04_CDW_charge_correlation.json
- path: `/app/outputs/step_04_CDW_charge_correlation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Charge density wave correlation at a single set of parameters. Checker compares C(π,π) to hidden paper value with 30% tolerance.
- schema:
  - `type`: object
  - `required`: `V_t`, `U_t`, `n`, `L`, `T_t`, `C_pi_pi`
  - `properties`:
    - `V_t`:
      - `type`: number
      - `const`: 0.9
    - `U_t`:
      - `type`: number
      - `const`: 3.0
    - `n`:
      - `type`: number
      - `const`: 1.0
    - `L`:
      - `type`: integer
      - `const`: 12
    - `T_t`:
      - `type`: number
      - `const`: 0.1667
    - `C_pi_pi`:
      - `type`: number
      - `description`: C(q) at q=(π,π)

Notes: All outputs are produced by DQMC simulations on the two-band Hubbard model with given tight-binding parameters. The checker uses hidden reference values from the paper's figures/tables and applies appropriate tolerances (20% for spin susceptibility, 30% for CDW) plus trend checks. No external datasets are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_chi_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "U_t",
            "n",
            "chi_pi_pi"
          ],
          "properties": {
            "U_t": {
              "type": "number",
              "description": "Hubbard U in units of t"
            },
            "n": {
              "type": "number",
              "description": "electron filling"
            },
            "chi_pi_pi": {
              "type": "number",
              "description": "χ(q) at q=(π,π)"
            }
          }
        }
      },
      "description": "Spin susceptibility peak values for various U and fillings. Checker compares to hidden paper-reported values with relative tolerance and verifies monotonic trends (χ increases with U at fixed n; χ increases with doping at fixed U)."
    },
    {
      "file": "step_02_pairing_suscept.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "temperature",
            "symmetry",
            "P",
            "P_eff",
            "n",
            "U_t"
          ],
          "properties": {
            "temperature": {
              "type": "number",
              "description": "T/t"
            },
            "symmetry": {
              "type": "string",
              "enum": [
                "sxy",
                "dxy",
                "sx2+y2",
                "dx2-y2"
              ]
            },
            "P": {
              "type": "number"
            },
            "P_eff": {
              "type": "number"
            },
            "n": {
              "type": "number",
              "description": "electron filling (1.0 or 0.8)"
            },
            "U_t": {
              "type": "number",
              "description": "Hubbard U in units of t (1.0, 3.0, or 5.0)"
            }
          }
        }
      },
      "description": "Pairing susceptibilities and effective interactions for U/t=1.0,3.0,5.0 at n=1.0 and U/t=3.0 at n=0.8. Checker verifies that dxy dominates, P_eff increases with decreasing T, and P_eff increases with U at low T."
    },
    {
      "file": "step_03_AFM_structure_factor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "L",
            "beta",
            "U_t",
            "n",
            "S_AFM"
          ],
          "properties": {
            "L": {
              "type": "integer"
            },
            "beta": {
              "type": "number",
              "description": "inverse temperature 1/T"
            },
            "U_t": {
              "type": "number",
              "const": 3.0
            },
            "n": {
              "type": "number",
              "const": 1.0
            },
            "S_AFM": {
              "type": "number"
            }
          }
        }
      },
      "description": "AFM structure factor for finite-size scaling. Checker verifies monotonic decrease of S_AFM as L increases (L=8→10→12) at β=10."
    },
    {
      "file": "step_04_CDW_charge_correlation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "V_t",
          "U_t",
          "n",
          "L",
          "T_t",
          "C_pi_pi"
        ],
        "properties": {
          "V_t": {
            "type": "number",
            "const": 0.9
          },
          "U_t": {
            "type": "number",
            "const": 3.0
          },
          "n": {
            "type": "number",
            "const": 1.0
          },
          "L": {
            "type": "integer",
            "const": 12
          },
          "T_t": {
            "type": "number",
            "const": 0.1667
          },
          "C_pi_pi": {
            "type": "number",
            "description": "C(q) at q=(π,π)"
          }
        }
      },
      "description": "Charge density wave correlation at a single set of parameters. Checker compares C(π,π) to hidden paper value with 30% tolerance."
    }
  ],
  "notes": "All outputs are produced by DQMC simulations on the two-band Hubbard model with given tight-binding parameters. The checker uses hidden reference values from the paper's figures/tables and applies appropriate tolerances (20% for spin susceptibility, 30% for CDW) plus trend checks. No external datasets are required."
}
```

## How you are scored
A hidden verifier reads each output JSON file and compares the reported values to reference results from the original study. The verifier checks whether the computed quantities fall within specified tolerances and satisfy certain structural patterns (monotonicity, ordering) without revealing which pattern is expected. Each scored stage is independently assessed and contributes to the final reward according to the weights assigned in the workflow. The final score is a weighted sum of the per-stage scores, normalized to the interval [0, 1].
