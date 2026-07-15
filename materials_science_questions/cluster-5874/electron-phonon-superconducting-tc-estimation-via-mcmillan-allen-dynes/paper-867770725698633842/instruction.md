# Two-band Eliashberg solver for superconducting gaps and superfluid density

## Problem background
Iron-based superconductors can host spin-glass-like phases that compete with superconductivity, giving rise to unusual temperature dependences of the superconducting properties. This task models such a system with a two-band $s\pm$ superconductor where the spin-glass state is introduced via a temperature-dependent magnetic scattering rate. The objective is to compute the superconducting gaps on the imaginary frequency axis and the normalized superfluid density as functions of temperature for a range of model parameters that approximately describe iron-pnictide compounds. The results reveal how the balance between magnetism and superconductivity can lead to non-monotonic gap behavior and, in certain regimes, reentrant superconductivity.

## Approach
The model extends the multiband Eliashberg formalism to include a static, temperature-dependent spin-glass contribution. The two-band imaginary-axis Eliashberg equations are solved self-consistently for the renormalization functions $Z_j(i\omega_n)$ and the gap functions $\Delta_j(i\omega_n)$ on a Matsubara frequency grid. The spin-glass scattering rate is taken as $\Gamma^{M}_{\mathrm{jk}}(T) = k_{\mathrm{jk}}\bigl[1 - (T/T_{\mathrm{SG}})^\beta\bigr]$, where $T_{\mathrm{SG}}$ is the spin-glass freezing temperature and $\beta$ controls the temperature dependence. The electron–spin-fluctuation spectral function is a Lorentzian centered at a characteristic energy $\Omega_0$, with half-width $Y = \Omega_0/2$, responsible for the $s\pm$ pairing. The input coupling constants and band parameters are fixed, while the magnetic scattering amplitudes $k_{\mathrm{jk}}$ are varied across several values. For each $(k_{22},\beta)$ combination, a temperature sweep is performed from well below $T_{\mathrm{SG}}$ to above the superconducting transition. At each temperature the coupled equations are iterated to convergence; from the converged solutions the lowest-Matsubara-frequency gaps $\Delta_1(i\omega_0)$ and $\Delta_2(i\omega_0)$ are recorded, and the normalized superfluid density $n_s(T)$ is computed from the generalised London formula using the band weights and the zero-temperature reference of the $k_{22}=0$ case.

## Reproduction target
Implement a numerical solver for the two-band imaginary-axis Eliashberg equations with the temperature-dependent spin-glass scattering term and the Lorentzian spin-fluctuation spectrum. Use the following fixed parameters: electron–spin-fluctuation coupling constants $\lambda_{11}=1.00$, $\lambda_{12}=-0.17$, $\lambda_{22}=2.65$; density-of-states ratio $\nu_{12}=0.8333$; characteristic spin-fluctuation energy $\Omega_0 = 2T_c/5$ with $T_c=22\,\mathrm{K}$; cutoff energy $\omega_c=180\,\mathrm{meV}$; spin-glass freezing temperature $T_{\mathrm{SG}}=15\,\mathrm{K}$; magnetic scattering ratios $k_{11}=k_{12}=0.2\,k_{22}$; and non-magnetic scattering $\Gamma^{\mathrm{N}}_{\mathrm{jk}}=0$. Compute the temperature dependence of $\Delta_1(i\omega_0)$, $\Delta_2(i\omega_0)$, and the normalized superfluid density $n_s(T)$ (band weights $w_1=0.72$, $w_2=0.28$, normalized by the $T=0$ value of the $k_{22}=0$ case) for all combinations of $k_{22} \in \{0,1,2,3,3.5,4,4.05,5\}\,\mathrm{meV}$ and $\beta \in \{1,2\}$. Perform the temperature sweep from approximately $0.125\,\mathrm{K}$ to at least $30\,\mathrm{K}$ with no fewer than $50$ temperature points per $(k_{22},\beta)$ curve. Write all results to the file `/app/outputs/results.csv` with the exact schema described in the output contract.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve Eliashberg equations and compute gaps and superfluid density
- Role: scored (load-bearing)
- Action: Implement an iterative solver for the two-band imaginary-axis Eliashberg equations with a temperature-dependent spin-glass scattering term. Use the given model parameters: electron–spin-fluctuation coupling constants (λ₁₁=1.00, λ₁₂=-0.17, λ₂₂=2.65), density-of-states ratio ν₁₂=0.8333, characteristic spin-fluctuation energy Ω₀ = 2T_c/5 with T_c=22 K, cutoff ω_c=180 meV, spin-glass freezing temperature T_SG=15 K, and Lorentzian spin-fluctuation spectral function with half-width Y=Ω₀/2. Set magnetic scattering amplitudes as k₁₁=k₁₂=0.2k₂₂ and non-magnetic scattering to zero. For each combination of k₂₂ ∈ {0,1,2,3,3.5,4,4.05,5} meV and exponent β ∈ {1,2}, perform a temperature sweep from about 0.125 K to above 30 K with at least 50 points. At each temperature, self-consistently solve for the renormalization functions Z_j(iω_n) and gap functions Δ_j(iω_n) on a sufficiently large Matsubara grid. Extract the lowest-Matsubara-frequency gaps Δ₁(iω₀) and Δ₂(iω₀). Compute the normalized superfluid density n_s(T) from the obtained functions using the formula analogous to Eq. (5) of the original work (band weights w₁=0.72, w₂=0.28, normalized by the zero-temperature value of the k₂₂=0 case). Assemble all results into a single CSV file with columns: k22, beta, T, Delta1, Delta2, ns.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV file with header: k22,beta,T,Delta1,Delta2,ns. k22: float (meV), beta: int (1 or 2), T: float (K), Delta1: float (meV), Delta2: float (meV), ns: float (dimensionless). No missing values; at least 50 temperature points per (k22,beta) pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of computed superconducting gaps and normalized superfluid density for the two-band spin-glass Eliashberg model. The checker will compare the agent’s reported Δ₁, Δ₂, and n_s values at selected temperature points against hidden reference values extracted from the paper’s figures, within defined tolerances.
- schema:
  - `type`: table
  - `required_columns`: `k22`, `beta`, `T`, `Delta1`, `Delta2`, `ns`
  - `units`:
    - `k22`: meV
    - `beta`: dimensionless
    - `T`: K
    - `Delta1`: meV
    - `Delta2`: meV
    - `ns`: dimensionless

Notes: The reference match compares against the paper’s original results (hidden). The solver implementation details (grid size, convergence criteria, solver method) are the agent’s choice; the tolerance accounts for legitimate implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k22",
          "beta",
          "T",
          "Delta1",
          "Delta2",
          "ns"
        ],
        "units": {
          "k22": "meV",
          "beta": "dimensionless",
          "T": "K",
          "Delta1": "meV",
          "Delta2": "meV",
          "ns": "dimensionless"
        }
      },
      "description": "Table of computed superconducting gaps and normalized superfluid density for the two-band spin-glass Eliashberg model. The checker will compare the agent’s reported Δ₁, Δ₂, and n_s values at selected temperature points against hidden reference values extracted from the paper’s figures, within defined tolerances."
    }
  ],
  "notes": "The reference match compares against the paper’s original results (hidden). The solver implementation details (grid size, convergence criteria, solver method) are the agent’s choice; the tolerance accounts for legitimate implementation spread."
}
```

## How you are scored
A hidden verifier independently reads `/app/outputs/results.csv` and compares your reported gaps and superfluid density against reference values at selected temperature points. The comparison uses appropriate tolerances that account for legitimate implementation differences. The verifier also checks structural properties, such as the presence of reentrant behavior in the superfluid density for certain parameter combinations. The reward is proportional to the fraction of test points that match within tolerance, with higher weight assigned to key parameter regimes. Your code must produce the required CSV file with the correct schema; no credit is given for simply printing or hard-coding the expected numbers.
