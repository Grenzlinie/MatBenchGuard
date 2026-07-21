# Tight-Binding Band Structures of Sb/BTS and Bi/BTS Heterostructures

## Problem background
Heterostructures of topological insulators (TIs) and bilayer insulating films can give rise to emergent Dirac-cone electronic states whose character is governed by band alignment and interfacial hybridization. A minimal tight-binding model that couples the topological surface states of the TI with a Rashba-split quadratic band of the bilayer insulator captures the evolution of topological surface states, Rashba-split bands, and quantum-well-derived Dirac features. The difference in work function between the two materials determines the band offset and, consequently, the energy ordering of these Dirac-cone-like states. This task asks you to compute the band structure of that minimal model for two different material systems (Sb/BTS and Bi/BTS) to reveal how the model parameters affect the Dirac features at the Gamma point.

## Approach
Construct a 4×4 effective Hamiltonian 

$$
H = \begin{pmatrix} H_{TI} & T \\ T^{\dagger} & H_{BI} \end{pmatrix}
$$

in the spinor basis of the TI topological surface states and the bilayer insulator (BI) states. The TI block is a massless Dirac cone with helical spin texture, described by $H_{TI}=v_F (k_x \sigma_y - k_y \sigma_x)$. The BI block includes a spin-degenerate quadratic dispersion, a band offset $\delta$ that accounts for the work-function mismatch, and Rashba spin-orbit coupling:

$$
H_{BI} = \left(\frac{k^2}{2m^*} + \delta\right) I_{2\times2} + \alpha_R (k_y \sigma_x + k_x \sigma_y).
$$

The interlayer coupling is a spin-independent hopping $T = t\,\sigma_z I_{2\times2}$ with strength $t$.

You are given the concrete parameters for the two material systems:

- **Sb/BTS**: effective mass $m^* = -0.2\ \text{eV}^{-1}\text{\AA}^{-2}$, Rashba strength $\alpha_R = 0.5\ \text{eV\AA}$, hopping $t = 0.05\ \text{eV}$, band offset $\delta = 0.05\ \text{eV}$, and Fermi velocity $v_F = 5.8\times10^{5}\ \text{m/s}$.
- **Bi/BTS**: $m^* = -0.12\ \text{eV}^{-1}\text{\AA}^{-2}$, $\alpha_R = 0.2\ \text{eV\AA}$, $t = 0.1\ \text{eV}$, $\delta = 0.4\ \text{eV}$, and the same $v_F$.

For each system, diagonalize the Hamiltonian on a dense 1‑D k‑path from $\Gamma$ to $K$ ($k = 0$ to $1.2\ \text{\AA}^{-1}$). Save the four real eigenvalues (in eV) at every k‑point as described in the workflow steps. The hidden verifier will later re‑diagonalize the same Hamiltonian at its own k‑points to check the Dirac cone features at the $\Gamma$ point.

## Reproduction target
Produce two CSV files, `sb_bts_band_structure.csv` and `bi_bts_band_structure.csv`, each containing the four band eigenvalues along the $\Gamma$‑$K$ path for the corresponding parameter set. The hidden verifier will recompute the band structure at a hidden set of k‑points (including $\Gamma$) using the same Hamiltonian and parameters. It will then identify the Dirac cone crossings at the $\Gamma$ point and verify the number of Dirac-cone-like features and their relative energy ordering, without revealing the expected outcome. Your submission is accepted only if the eigenvalue data reflect the correct Dirac cone structure, as determined by the verifier's independent recomputation.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Sb/BTS tight-binding band structure
- Role: scored (load-bearing)
- Action: Implement the 4x4 effective Hamiltonian with the Sb/BTS parameters (m* = -0.2 eV⁻¹Å⁻², α_R = 0.5 eVÅ, t = 0.05 eV, v_F ≈ 5.8×10⁵ m/s) and the band offset δ=0.05 eV as inferred from the paper. Diagonalize on a dense 1D k-path along Γ-K from k=0 to 1.2 Å⁻¹ and save all four eigenvalues at each k.
- Output file: `/app/outputs/sb_bts_band_structure.csv`
- Format: csv
- Contract: CSV with columns: k (in Å⁻¹), E1 (eV), E2 (eV), E3 (eV), E4 (eV). At least 100 equally spaced k-points from 0 to 1.2 Å⁻¹.
- Scoring: scored by hidden verifier

### Step 2: Compute Bi/BTS tight-binding band structure
- Role: scored (load-bearing)
- Action: Implement the 4x4 effective Hamiltonian with the Bi/BTS parameters (m* = -0.12 eV⁻¹Å⁻², α_R = 0.2 eVÅ, t = 0.1 eV, v_F ≈ 5.8×10⁵ m/s) and the band offset δ=0.4 eV as inferred from the paper. Diagonalize on the same Γ-K k-path and save eigenvalues.
- Output file: `/app/outputs/bi_bts_band_structure.csv`
- Format: csv
- Contract: CSV with columns: k (in Å⁻¹), E1 (eV), E2 (eV), E3 (eV), E4 (eV). At least 100 equally spaced k-points from 0 to 1.2 Å⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sb_bts_band_structure.csv`
- `/app/outputs/bi_bts_band_structure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sb_bts_band_structure.csv
- path: `/app/outputs/sb_bts_band_structure.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Band structure eigenvalues for Sb/BTS model; used to verify Dirac cone features.
- schema:
  - `type`: table
  - `columns`:
    - `name`: k
    - `type`: number
    - `unit`: Å⁻¹
    - `name`: E1
    - `type`: number
    - `unit`: eV
    - `name`: E2
    - `type`: number
    - `unit`: eV
    - `name`: E3
    - `type`: number
    - `unit`: eV
    - `name`: E4
    - `type`: number
    - `unit`: eV

### bi_bts_band_structure.csv
- path: `/app/outputs/bi_bts_band_structure.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Band structure eigenvalues for Bi/BTS model; used to verify Dirac cone features.
- schema:
  - `type`: table
  - `columns`:
    - `name`: k
    - `type`: number
    - `unit`: Å⁻¹
    - `name`: E1
    - `type`: number
    - `unit`: eV
    - `name`: E2
    - `type`: number
    - `unit`: eV
    - `name`: E3
    - `type`: number
    - `unit`: eV
    - `name`: E4
    - `type`: number
    - `unit`: eV

Notes: The checker recomputes the band structure at hidden k-points and verifies the number and relative energy ordering of Dirac cone features at Γ. No gold values are given in public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sb_bts_band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "k",
            "type": "number",
            "unit": "Å⁻¹"
          },
          {
            "name": "E1",
            "type": "number",
            "unit": "eV"
          },
          {
            "name": "E2",
            "type": "number",
            "unit": "eV"
          },
          {
            "name": "E3",
            "type": "number",
            "unit": "eV"
          },
          {
            "name": "E4",
            "type": "number",
            "unit": "eV"
          }
        ]
      },
      "description": "Band structure eigenvalues for Sb/BTS model; used to verify Dirac cone features."
    },
    {
      "file": "bi_bts_band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "k",
            "type": "number",
            "unit": "Å⁻¹"
          },
          {
            "name": "E1",
            "type": "number",
            "unit": "eV"
          },
          {
            "name": "E2",
            "type": "number",
            "unit": "eV"
          },
          {
            "name": "E3",
            "type": "number",
            "unit": "eV"
          },
          {
            "name": "E4",
            "type": "number",
            "unit": "eV"
          }
        ]
      },
      "description": "Band structure eigenvalues for Bi/BTS model; used to verify Dirac cone features."
    }
  ],
  "notes": "The checker recomputes the band structure at hidden k-points and verifies the number and relative energy ordering of Dirac cone features at Γ. No gold values are given in public."
}
```

## How you are scored
A hidden verifier independently recomputes the band structure at a set of hidden k‑points (including $\Gamma=0$) using the same Hamiltonian and parameters you were given. It checks the number of Dirac cone crossings at the $\Gamma$ point and their relative energy ordering. Each of the two output files (`sb_bts_band_structure.csv` and `bi_bts_band_structure.csv`) is scored separately based on whether the recomputed Dirac features match the expectations derived from the parameters. The individual scores are combined by weight into a final reward in the range [0, 1]. Reporting numbers that happen to agree with a published table is not sufficient; the verifier only trusts a band structure produced by genuinely implementing and diagonalizing the model.
