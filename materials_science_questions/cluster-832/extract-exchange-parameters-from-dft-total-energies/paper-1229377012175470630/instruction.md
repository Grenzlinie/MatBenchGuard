# Magnon spectrum renormalization factors of kagome-lattice antiferromagnet from Ising expansion perturbation

## Problem background
The $S=1/2$ kagome-lattice Heisenberg antiferromagnet with out-of-plane Dzyaloshinskii-Moriya (DM) interaction exhibits strong quantum spin fluctuations. Linear spin wave (LSW) theory provides a conventional description of magnon excitations, but it neglects spin-wave interactions and therefore fails to capture the full renormalization of the magnon spectrum. This task addresses the computation of magnon excitation energies and momentum-resolved renormalization factors for this system using a series expansion method that goes beyond LSW. The target is to quantify how much the true magnon spectrum deviates from the LSW prediction, focusing on the $\boldsymbol{q}=0$ ordered phase at a given DM coupling.

## Approach
The method is an Ising expansion perturbation (IEP). The Hamiltonian is written in local spin coordinates that align with the magnetic order and split into an unperturbed part $H_0$ and a perturbation $H_1$ with a parameter $\lambda$; an auxiliary local field term $t$ is added to $H_0$ and subtracted from $H_1$ to improve series convergence, and the final result is evaluated at $t/J=1$, $\lambda\to 1$. A linked-cluster expansion is performed up to ninth order: all topologically distinct clusters of up to nine links and ten sites on the kagome lattice are enumerated, and the single-spin-flip sector is diagonalised to extract irreducible matrix elements $c_{\nu,\nu'}(r,m,n)$ as power series in $\lambda$. These matrix elements are then combined with a lattice-dependent phase factor to build a $3\times3$ effective Hamiltonian $\Delta(k_x,k_y)$ for each wavevector. Diagonalising this matrix gives the IEP magnon energies $\epsilon_{\mathbf{k},\alpha}^{\mathrm{IEP}}(\lambda)$ as power series. In parallel, the Holstein–Primakoff transformation is applied to the same $H_\lambda$ to obtain the LSW magnon energies $\epsilon_{\mathbf{k},\alpha}^{\mathrm{LSW}}(\lambda)$, also expanded as power series. The momentum-resolved renormalization factor is defined as the ratio $r_{\mathbf{k},\alpha} = \epsilon_{\mathbf{k},\alpha}^{\mathrm{IEP}} / \epsilon_{\mathbf{k},\alpha}^{\mathrm{LSW}}$, evaluated at $\lambda\to 1$ by naive summation of the series. The final outputs are the renormalization factors at the $\Gamma$ and M points and the full magnon dispersion along the $\Gamma$–M path, which reveal the quantitative deviation from LSW.

## Reproduction target
For the Hamiltonian with exchange $J = 20.7~\mathrm{meV}$, DM ratio $D^{\parallel}/J = 0.12$, and local field $t/J = 1$, compute:

1. The dimensionless renormalization factors $r_{\mathbf{k},\alpha}$ for each magnon mode $\alpha = 0,1,2$ at the two high-symmetry points $\Gamma$ and M, written to `/app/outputs/renormalization_factors.csv` with columns `k_label` ("Gamma" or "M"), `mode` (integer 0–2), and `r_value` (float).

2. The magnon excitation energies (in meV) for all three modes along a dense set of wavevectors on the $\Gamma$–M path, written to `/app/outputs/magnon_dispersion.csv` with columns `k_label` (string identifier for each k-point), `kx` (float, reduced wavevector x component), `ky` (float, reduced wavevector y component), `mode` (integer 0–2), and `energy_meV` (float, in meV). The $\Gamma$–M path corresponds to the straight line from $\Gamma = (0,0)$ to $\mathrm{M} = (\pi/2, \pi/(2\sqrt{3}))$ in the kagome lattice Brillouin zone.

The IEP procedure must be implemented from scratch; the task provides only the model parameters and the required output format.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Linked-cluster expansion for irreducible matrix elements
- Role: process
- Action: Implement the linked-cluster expansion: set up the Hamiltonian in local coordinates with Eₓ=E_z=(J+√3 D∥)/2, E_y=-J, d_y=(-√3 J + D∥)/2. Split into H₀ and H₁ using perturbation parameter λ and local field t (t/J=1). Enumerate all topologically distinct clusters up to 9 links and 10 sites on the kagome lattice. Diagonalise the single-flip sector on each cluster to obtain irreducible matrix elements c_{ν,ν'}(r,m,n) up to ninth order in λ, covering all necessary unit-cell displacements (m,n).
- Evidence: none

### Step 2: Linear spin wave magnon energy series
- Role: process
- Action: Apply the Holstein–Primakoff transformation to the same H_λ to obtain the linear spin wave (LSW) magnon energies ε_{k,α}^{LSW}(λ). Expand these as power series in λ up to ninth order for all wavevectors that will be used in the scored steps (Γ, M, and a dense set along the Γ–M path). Store the series coefficients for later normaisation.
- Evidence: none

### Step 3: Renormalization factors at Γ and M points
- Role: scored (load-bearing)
- Action: For each mode α (0,1,2) at the Γ and M points, form the ratio series r_{k,α}^{(n)}(λ) = ε_{k,α}^{IEP}(λ) / ε_{k,α}^{LSW}(λ) truncated at ninth order. Evaluate the series at λ→1 by naive direct summation to obtain the renormalization factor r_{k,α}. Write the results to /app/outputs/renormalization_factors.csv with columns k_label (string, 'Gamma' or 'M'), mode (int), r_value (float).
- Output file: `/app/outputs/renormalization_factors.csv`
- Format: csv
- Contract: Columns: k_label (str, either 'Gamma' or 'M'), mode (int, 0-2), r_value (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Magnon dispersion along Γ–M path
- Role: scored
- Action: From the IEP magnon energy series, compute the excitation energy ε_{k,α} at λ=1 for every k-point along the Γ–M path, using J=20.7 meV to convert energies to meV. Write the dispersion to /app/outputs/magnon_dispersion.csv with columns k_label (str), kx (float), ky (float), mode (int), energy_meV (float). Provide a representative set of points along the path.
- Output file: `/app/outputs/magnon_dispersion.csv`
- Format: csv
- Contract: Columns: k_label (str), kx (float, reduced wavevector x), ky (float, reduced wavevector y), mode (int, 0-2), energy_meV (float, meV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/renormalization_factors.csv`
- `/app/outputs/magnon_dispersion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### renormalization_factors.csv
- path: `/app/outputs/renormalization_factors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Momentum-resolved renormalization factors r_{k,α} at the Γ and M points. Values are compared to hidden paper-reported references with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `k_label`, `mode`, `r_value`
  - `units`:
    - `r_value`: dimensionless

### magnon_dispersion.csv
- path: `/app/outputs/magnon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnon dispersion energies along the Γ–M path. Key structural features (peak positions, energy at M point) are compared to hidden paper-derived references.
- schema:
  - `type`: table
  - `required_columns`: `k_label`, `kx`, `ky`, `mode`, `energy_meV`
  - `units`:
    - `kx`: reduced wavevector units
    - `ky`: reduced wavevector units
    - `energy_meV`: meV

Notes: The solver must reimplement the entire IEP procedure from scratch; no precomputed coefficients are supplied. The required J=20.7 meV and D∥/J=0.12 are fixed inputs. All LSW calculations are part of the pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "renormalization_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_label",
          "mode",
          "r_value"
        ],
        "units": {
          "r_value": "dimensionless"
        }
      },
      "description": "Momentum-resolved renormalization factors r_{k,α} at the Γ and M points. Values are compared to hidden paper-reported references with a relative tolerance."
    },
    {
      "file": "magnon_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_label",
          "kx",
          "ky",
          "mode",
          "energy_meV"
        ],
        "units": {
          "kx": "reduced wavevector units",
          "ky": "reduced wavevector units",
          "energy_meV": "meV"
        }
      },
      "description": "Magnon dispersion energies along the Γ–M path. Key structural features (peak positions, energy at M point) are compared to hidden paper-derived references."
    }
  ],
  "notes": "The solver must reimplement the entire IEP procedure from scratch; no precomputed coefficients are supplied. The required J=20.7 meV and D∥/J=0.12 are fixed inputs. All LSW calculations are part of the pipeline."
}
```

## How you are scored
A hidden verifier evaluates your submitted CSV files by comparing your computed renormalization factors and magnon dispersion to reference values derived from the paper-reported results. The renormalization factors at $\Gamma$ and M are compared with a relative tolerance, and the dispersion is checked for key structural features (e.g., the energy at the M point for mode 2, the position of the dispersion maximum) against reference thresholds, as well as qualitative properties such as correct band ordering and monotonicity along the path. Each output receives a weighted score, and the final reward is a combination of the scores from both artifacts. Merely copying a published number without executing the perturbation computation will not pass; the verifier's tolerances require a genuine reimplementation of the linked-cluster expansion up to ninth order.
