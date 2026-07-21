# Screened Hubbard model: doping-dependent Ueff and AF order in layered cuprates

## Problem background
Multilayered cuprate superconductors consist of inequivalent CuO₂ planes: outer planes with apical atoms and inner planes without. This structural difference generates charge imbalance and complex antiferromagnetic (AF) order. The on-site Hubbard interaction U is strongly renormalized by screening effects, leading to a doping-dependent effective interaction U_eff. Understanding how U_eff changes with doping and how it, together with the Madelung potential, determines the layer-resolved charge distribution and AF order is essential for explaining the electronic and magnetic phase diagrams of these materials. In this task, you will compute the doping-dependent U_eff and the resulting AF order parameters and charge imbalance for a model three-layer system.

## Approach
We adopt a mean-field treatment of the multilayered Hubbard model. The intra-layer Hamiltonian uses tight-binding parameters t=1, t'=-0.25, t''=0.1, and includes a Hubbard term with an effective on-site interaction U_eff. Inter-layer hopping is parameterized by t_perp=0.3, and an electrostatic Madelung potential W acts on the outer planes. The key ingredient is that the effective Hubbard constant U_eff is not fixed but determined self-consistently from the bare U via the screening formula U_eff = U / (1 + U * ⟨P(q,0)⟩_q), where P(q,0) is the static charge susceptibility averaged over the Brillouin zone. Because U_eff depends on the local doping and magnetization, the model must be solved iteratively. First, you will compute U_eff as a function of doping for a single layer, for both hole and electron doping, at two bare Hubbard strengths (U=5t and U=6t). Then you will solve the full three-layer system (two outer planes OP, one inner plane IP) with bare U=5t and W=1.0t, obtaining layer-resolved doping densities and AF order parameters M_α, and the charge imbalance y = n_OP - n_IP as a function of the overall average doping δ. The self-consistency loop adjusts U_eff in each layer using the local doping, and the magnetic ground state is determined by minimizing the free energy.

## Reproduction target
Your goal is to produce two CSV files: (1) effective_U.csv containing the doping-dependent U_eff for bare U=5t and 6t, separately for hole and electron doping, with at least 10 doping points covering [0,0.2]; (2) af_order_and_charge.csv containing the AF order parameters M_OP and M_IP and the charge imbalance y as functions of average doping δ for the three-layer N-based system (W=1.0t, U=5t), with at least 20 doping points covering [0,0.2]. The exact output formats are specified in the workflow steps and output contract. The results are assessed against reference values derived from the full mean-field solution using the same physical parameters.

## Assets

- Python scientific stack (NumPy, SciPy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Compute single-layer effective Hubbard constant Ueff
- Role: scored
- Action: Implement the mean-field antiferromagnetic Hamiltonian for a single layer using tight-binding parameters t=1, t'=-0.25, t''=0.1. For bare U values 5t and 6t, and a range of doping values from 0 to 0.2, self-consistently solve for the staggered magnetization M and the effective Ueff via the screening formula Ueff = U / (1 + U * ⟨P(q,0)⟩_q), where P(q,0) is the static charge susceptibility computed from the antiferromagnetic band structure and averaged over the magnetic Brillouin zone. Perform separate calculations for hole-doped and electron-doped cases by adjusting the chemical potential.
- Output file: `/app/outputs/effective_U.csv`
- Format: csv
- Contract: Columns: bare_U (float), doping (float), U_eff_hole (float), U_eff_electron (float). Row order arbitrary; at least 10 doping points per bare_U covering [0,0.2].
- Scoring: scored by hidden verifier

### Step 2: Compute multilayer AF order and charge imbalance
- Role: scored (load-bearing)
- Action: Implement the mean-field multilayered Hubbard model for N=3 (two outer planes OP and one inner plane IP) with interlayer hopping t_perp=0.3, Madelung potential W=1.0t, and bare U=5t. For a range of average doping δ from 0 to 0.2, self-consistently solve for the layer-dependent doping densities δ_α and AF order parameters M_α, using the layer-resolved effective Ueff computed from the screening formula based on the local doping. Compute the charge imbalance y = (n_OP - n_IP).
- Output file: `/app/outputs/af_order_and_charge.csv`
- Format: csv
- Contract: Columns: doping (float, average δ), M_OP (float), M_IP (float), y (float). At least 20 points covering [0,0.2].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_U.csv`
- `/app/outputs/af_order_and_charge.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_U.csv
- path: `/app/outputs/effective_U.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Doping-dependent effective Hubbard constant Ueff for hole and electron doping, computed from the static screening formula for two bare Hubbard interactions U=5t and 6t.
- schema:
  - `type`: table
  - `required_columns`: `bare_U`, `doping`, `U_eff_hole`, `U_eff_electron`
  - `units`:
    - `bare_U`: t
    - `doping`: dimensionless
    - `U_eff_hole`: t
    - `U_eff_electron`: t

### af_order_and_charge.csv
- path: `/app/outputs/af_order_and_charge.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Layer-resolved antiferromagnetic order parameters, charge imbalance, and layer charge densities for the N-based three-layer cuprate with U=5t and Madelung potential W=1.0t, as functions of average doping δ. The charge densities are required to verify the predicted anomalous increase of minority charge density upon doping.
- schema:
  - `type`: table
  - `required_columns`: `doping`, `M_OP`, `M_IP`, `y`, `n_OP`, `n_IP`
  - `units`:
    - `doping`: dimensionless
    - `M_OP`: t (staggered magnetization)
    - `M_IP`: t
    - `y`: charge imbalance
    - `n_OP`: electrons per site
    - `n_IP`: electrons per site

Notes: The agent must self-consistently solve the mean-field equations with the screening-corrected Ueff. The checker compares the submitted CSV data against structural consistency rules derived from the paper's reported behaviour (monotonicity, ordering, electron–hole asymmetry, charge density anomaly).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_U.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bare_U",
          "doping",
          "U_eff_hole",
          "U_eff_electron"
        ],
        "units": {
          "bare_U": "t",
          "doping": "dimensionless",
          "U_eff_hole": "t",
          "U_eff_electron": "t"
        }
      },
      "description": "Doping-dependent effective Hubbard constant Ueff for hole and electron doping, computed from the static screening formula for two bare Hubbard interactions U=5t and 6t."
    },
    {
      "file": "af_order_and_charge.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping",
          "M_OP",
          "M_IP",
          "y",
          "n_OP",
          "n_IP"
        ],
        "units": {
          "doping": "dimensionless",
          "M_OP": "t (staggered magnetization)",
          "M_IP": "t",
          "y": "charge imbalance",
          "n_OP": "electrons per site",
          "n_IP": "electrons per site"
        }
      },
      "description": "Layer-resolved antiferromagnetic order parameters, charge imbalance, and layer charge densities for the N-based three-layer cuprate with U=5t and Madelung potential W=1.0t, as functions of average doping δ. The charge densities are required to verify the predicted anomalous increase of minority charge density upon doping."
    }
  ],
  "notes": "The agent must self-consistently solve the mean-field equations with the screening-corrected Ueff. The checker compares the submitted CSV data against structural consistency rules derived from the paper's reported behaviour (monotonicity, ordering, electron–hole asymmetry, charge density anomaly)."
}
```

## How you are scored
Each scored output file will be inspected by a hidden verifier. The verifier compares your numerical results to reference data using appropriate tolerances and checks for consistency with the underlying physics (trends, ordering). It assigns a score for each stage, and the final reward is a weighted combination. Reporting numbers that differ from the actual physics or fabricating data without running the self-consistent solver will yield very low or zero scores. To maximize your reward, implement the mean-field model accurately, solve the self-consistency equations, and follow the output schema precisely.
