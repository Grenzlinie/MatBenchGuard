# Mean-field study of doping-dependent antiferromagnetism and effective hopping in the extended Hubbard model

## Problem background
Electron-doped cuprate superconductors exhibit antiferromagnetic (AF) ordering over a wide doping range. The observed Fermi surface evolution suggests that the energy gap shrinks with electron doping, which is difficult to explain with a constant on-site Hubbard U. One proposed mechanism invokes the long-range Coulomb interaction, whose exchange part generates doping-dependent excess hopping parameters that modify the effective band structure and can suppress AF order. This task investigates, within a square-lattice extended Hubbard model, how the long-range Coulomb interaction affects the antiferromagnetic instability and the effective next-nearest-neighbor hopping as a function of electron doping.

## Approach
Solve the extended Hubbard model on a two-dimensional square lattice within a mean-field approximation. The Hamiltonian contains onsite Coulomb repulsion U, a long-range Coulomb interaction v_{ij}=V exp(-|i-j|/d)/|i-j|, and electron hoppings up to fifth neighbours. In the AF spin-density-wave state, the self-consistent order parameter Δ is obtained. From the momentum occupation numbers ⟨c⁺_{k↑}c_{k↑}⟩ the exchange-induced excess hopping parameters t_l^x are computed via Fourier summation. The total next-nearest-neighbor hopping t' = t_{(1,1)} + t_{(1,1)}^x, the Néel temperature T_N (the temperature where Δ vanishes), and the staggered magnetization m = 2Δ/U are then evaluated as functions of the electron doping concentration x.

## Reproduction target
Using the parameter set: bare hoppings t_{(1,0)}=1, t_{(1,1)}=-0.325, t_{(2,0)}=0.17, t_{(2,1)}=-0.121, t_{(2,2)}=-0.07, onsite U=4.8, Coulomb strength V=1.0, screening length d=4. Produce three CSV files covering doping concentrations x = 0, 0.02, …, 0.20. The file doping_hopping.csv gives the total next-nearest-neighbor hopping t' at temperature T=0.53t. The file neel_temperature.csv gives the Néel temperature T_N as a function of x. The file order_parameter.csv gives the staggered magnetization m at T=0.1t. All outputs must follow the exact schemas declared in the output contract.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Self-consistent mean-field solution
- Role: process
- Action: Implement a mean-field solver for the extended Hubbard model on a 2D square lattice with antiferromagnetic (AF) spin-density wave order parameter Δ. Solve the self-consistent equations for a grid of electron doping concentrations x from 0 to 0.2 and a range of temperatures (including T=0.1t, T=0.53t, and a temperature scan for T_N determination). Compute the AF order parameter, quasiparticle energies, and momentum occupation numbers ⟨c⁺_{k↑}c_{k↑}⟩. Save the solutions as intermediate data for later processing.
- Evidence: `/app/outputs/mean_field_solutions.npz`

### Step 2: Excess hopping and total t' vs doping
- Role: scored (load-bearing)
- Action: Using the mean-field occupations at temperature T=0.53t, compute the exchange-induced excess hoppings t_l^x via the formula t_l^x = (v_l / 2N) ∑_k ⟨c⁺_{k↑} c_{k↑}⟩ [cos(l_x k_x)cos(l_y k_y)+cos(l_y k_x)cos(l_x k_y)] for the relevant neighbor vectors. Then compute the total next-nearest-neighbor hopping t' = t_{(1,1)} + t_{(1,1)}^x for electron doping concentrations x = 0, 0.02, ..., 0.20. Output a CSV file with columns: x (float), t_prime (float).
- Output file: `/app/outputs/doping_hopping.csv`
- Format: csv
- Contract: x (float), t_prime (float)
- Scoring: scored by hidden verifier

### Step 3: Néel temperature vs doping
- Role: scored (load-bearing)
- Action: Determine the Néel temperature T_N as a function of doping concentration x by scanning temperature and locating where the AF order parameter Δ vanishes (or extrapolating to zero). Use the full parameter set (U=4.8, V=1.0, d=4, bare hoppings as specified). Output a CSV file with columns: x (float), T_N (float).
- Output file: `/app/outputs/neel_temperature.csv`
- Format: csv
- Contract: x (float), T_N (float)
- Scoring: scored by hidden verifier

### Step 4: Staggered magnetization vs doping at T=0.1t
- Role: scored (load-bearing)
- Action: At temperature T=0.1t, compute the staggered magnetization m = 2Δ/U for the same doping grid (x = 0, 0.02, ..., 0.20). Output a CSV file with columns: x (float), m (float).
- Output file: `/app/outputs/order_parameter.csv`
- Format: csv
- Contract: x (float), m (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/doping_hopping.csv`
- `/app/outputs/neel_temperature.csv`
- `/app/outputs/order_parameter.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### doping_hopping.csv
- path: `/app/outputs/doping_hopping.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Doping dependence of the total next-nearest-neighbor hopping parameter t' at T=0.53t. The checker will compare to hidden reference points from the paper.
- schema:
  - `type`: table
  - `required_columns`: `x`, `t_prime`
  - `units`:
    - `x`: electron doping concentration (per Cu site)
    - `t_prime`: units of nearest-neighbor hopping t

### neel_temperature.csv
- path: `/app/outputs/neel_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Doping dependence of the Néel temperature T_N. The checker compares to hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `x`, `T_N`
  - `units`:
    - `x`: electron doping concentration
    - `T_N`: units of t

### order_parameter.csv
- path: `/app/outputs/order_parameter.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Staggered magnetization m vs doping at T=0.1t. The checker compares to hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `x`, `m`
  - `units`:
    - `x`: doping
    - `m`: dimensionless (staggered magnetization)

Notes: The agent must implement the mean-field solver from scratch using the published model parameters; no pre-trained model or data files are provided. Scored artifacts are compared to digitized paper values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "doping_hopping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "t_prime"
        ],
        "units": {
          "x": "electron doping concentration (per Cu site)",
          "t_prime": "units of nearest-neighbor hopping t"
        }
      },
      "description": "Doping dependence of the total next-nearest-neighbor hopping parameter t' at T=0.53t. The checker will compare to hidden reference points from the paper."
    },
    {
      "file": "neel_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "T_N"
        ],
        "units": {
          "x": "electron doping concentration",
          "T_N": "units of t"
        }
      },
      "description": "Doping dependence of the Néel temperature T_N. The checker compares to hidden reference."
    },
    {
      "file": "order_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "m"
        ],
        "units": {
          "x": "doping",
          "m": "dimensionless (staggered magnetization)"
        }
      },
      "description": "Staggered magnetization m vs doping at T=0.1t. The checker compares to hidden reference."
    }
  ],
  "notes": "The agent must implement the mean-field solver from scratch using the published model parameters; no pre-trained model or data files are provided. Scored artifacts are compared to digitized paper values."
}
```

## How you are scored
A hidden verifier reads your output files. For each artifact the verifier compares the values to a hidden reference dataset and also evaluates required structural properties (e.g., monotonicity between x points). Per‑artifact scores are combined with predetermined weights into the final reward. Values that agree with the reference and satisfy the structural constraints earn high scores; large deviations or violations of the expected relations yield lower scores. The verifier operates autonomously and its gold standard is fixed; it does not access the original paper.
