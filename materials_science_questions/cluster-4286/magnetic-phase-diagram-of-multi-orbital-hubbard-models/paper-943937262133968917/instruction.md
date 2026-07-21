# Altermagnetic Phase Diagram and Anisotropic Spin Transport in a Fermi-Hubbard Model

## Problem background
Altermagnetism is a collinear magnetic state that differs from both ferromagnetism and conventional antiferromagnetism. In an altermagnet, opposite-spin sublattices are related by real-space rotations combined with spin flips, resulting in spin-split electronic bands despite zero net magnetization. This task studies a square-lattice Fermi-Hubbard model that can stabilize a d-wave altermagnetic phase. The model has uniform nearest-neighbor hopping t and sublattice-dependent diagonal hoppings, which alternate as t±=t′(1±δ) between the two sublattices. At half-filling, repulsive on-site interactions U drive a spontaneous (π,π) magnetic order, and the interplay with the anisotropic kinetic term yields altermagnetism.

The defining experimental predictions of this model are (i) a phase diagram showing the altermagnetic order parameter as a function of the interaction U/t and the diagonal hopping strength t′/t, and (ii) strongly anisotropic spin transport that can be observed in trap-expansion experiments, where spin-up and spin-down atoms expand predominantly along orthogonal directions. The computed order parameter quantifies the magnetism, while the time-dependent ratio of geometric squeezing parameters for the two spin species encodes the transport anisotropy.

## Approach
The work relies on a self-consistent Hartree-Fock mean-field treatment of the altermagnetic Hubbard Hamiltonian. The single-particle tight-binding model is written in the magnetic Brillouin zone, and the interaction is decoupled into a staggered order parameter δm that distinguishes the two sublattices and spin directions. At each grid point (U/t, t′/t, T) the chemical potential μ is adjusted to maintain half-filling, and δm is determined iteratively until convergence. The outcome is a map of δm that reveals normal metallic, altermagnetic metallic, and altermagnetic insulating regimes.

For a selected representative altermagnetic state, the spin-resolved DC conductivity tensor is computed from the Kubo formula using the Hartree-Fock eigenstates. Because the bands are fully spin-polarized and the Hamiltonian possesses a momentum-inversion symmetry, the conductivity tensor is diagonal and spin-block-diagonal, with the diagonal elements of one spin related to those of the opposite spin by a 90-degree rotation. Diffusion constants are obtained via the Einstein relation. Finally, the two-dimensional diffusion equation is solved numerically for an initially square density profile, yielding the time evolution of the spin-resolved densities and the geometric squeezing parameters. The ratio sq↓/sq↑ as a function of dimensionless time τ characterizes the anisotropic expansion.

## Reproduction target
You are asked to compute two key quantities that together capture the altermagnetic state:

1. **Altermagnetic order parameter phase diagram** — Produce a CSV file `order_parameter_data.csv` containing the self-consistently determined order parameter δm on a grid of interaction strengths U/t and diagonal hopping strengths t′/t, at a fixed staggering δ=0.2 and half-filling, for two temperatures T=0 and T=0.2t. The columns are `U_t`, `tprime_t`, `T`, and `delta_m` (all floating-point numbers).

2. **Time-resolved anisotropic spin squeezing ratio** — Using the Hartree-Fock solution for the specific parameters U/t=3.5, t′/t=0.3, δ=0.9, T=0.2t, and half-filling, compute the conductivity, diffusion constants, and trap-expansion dynamics. Output a CSV file `squeezing_ratio_time_series.csv` with columns `time_tau` (dimensionless time in units of 1/t) and `ratio` (the ratio sq↓/sq↑ of the geometric squeezing parameters).

## Assets

- Supplementary data and simulation codes (Zenodo repository): https://zenodo.org/records/10391823

## Workflow steps

### Step 1: Compute Hartree-Fock phase diagram and order parameter
- Role: scored (load-bearing)
- Action: Implement the altermagnetic Hubbard model Hamiltonian with uniform nearest-neighbor hopping t and sublattice-dependent diagonal hoppings t±=t′(1±δ). Perform self-consistent Hartree-Fock mean-field calculations at half-filling on a grid of U/t and t′/t values at fixed δ=0.2, for temperatures T=0 and T=0.2t. Determine the chemical potential μ and the order parameter δm iteratively. Write the computed (U/t, t′/t, T, δm) tuples to a CSV file.
- Output file: `/app/outputs/order_parameter_data.csv`
- Format: csv
- Contract: CSV with header: U_t, tprime_t, T, delta_m. All columns are floating-point numbers.
- Scoring: scored by hidden verifier

### Step 2: Simulate trap expansion and compute spin squeezing ratio
- Role: scored (load-bearing)
- Action: Using the Hartree-Fock self-consistent solution for the specific parameters U/t=3.5, t′/t=0.3, δ=0.9, T=0.2t, and half-filling, compute the spin-resolved DC conductivity tensor elements σ_{xx}^{s} and σ_{yy}^{s} via the Kubo formula (broadening Γ=0.02). Derive diffusion constants D_{αα}^{s} from the Einstein relation. Solve the 2D diffusion equation numerically for an initially square box density profile of spin-up and spin-down atoms. Compute the geometric squeezing parameter sq^{s}(τ) and the ratio sq↓(τ)/sq↑(τ) over time. Output the time series as a CSV.
- Output file: `/app/outputs/squeezing_ratio_time_series.csv`
- Format: csv
- Contract: CSV with header: time_tau, ratio. Both are floating-point numbers; time_tau is in units of the nearest-neighbor hopping t.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_parameter_data.csv`
- `/app/outputs/squeezing_ratio_time_series.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_parameter_data.csv
- path: `/app/outputs/order_parameter_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Grid of self-consistently computed altermagnetic order parameter δm for a range of interaction strengths and diagonal hoppings at two temperatures. The hidden checker selects a subset of grid points and compares δm values to paper-reported references using absolute tolerance.
- schema:
  - `required_columns`: `U_t`, `tprime_t`, `T`, `delta_m`
  - `units`: object

### squeezing_ratio_time_series.csv
- path: `/app/outputs/squeezing_ratio_time_series.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time evolution of the ratio sq↓/sq↑ during trap expansion. The hidden checker compares the peak value and the ratio at early times to paper-reported reference data using relative tolerance and trend compliance.
- schema:
  - `required_columns`: `time_tau`, `ratio`
  - `units`: object

Notes: The task reproduces the key altermagnetic quantities directly from the tight-binding Hubbard model. The optical-lattice band-structure fitting and parameter-tunability stages are excluded; the agent works with the specified effective hopping parameters. The contract requires only the two scored CSV artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_parameter_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "U_t",
          "tprime_t",
          "T",
          "delta_m"
        ],
        "units": {}
      },
      "description": "Grid of self-consistently computed altermagnetic order parameter δm for a range of interaction strengths and diagonal hoppings at two temperatures. The hidden checker selects a subset of grid points and compares δm values to paper-reported references using absolute tolerance."
    },
    {
      "file": "squeezing_ratio_time_series.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "time_tau",
          "ratio"
        ],
        "units": {}
      },
      "description": "Time evolution of the ratio sq↓/sq↑ during trap expansion. The hidden checker compares the peak value and the ratio at early times to paper-reported reference data using relative tolerance and trend compliance."
    }
  ],
  "notes": "The task reproduces the key altermagnetic quantities directly from the tight-binding Hubbard model. The optical-lattice band-structure fitting and parameter-tunability stages are excluded; the agent works with the specified effective hopping parameters. The contract requires only the two scored CSV artifacts."
}
```

## How you are scored
A hidden verifier will independently score each of the two scored workflow steps by reading your output artifacts. For the order parameter data, it will extract δm at a hidden set of (U/t, t′/t, T) grid points and compare them to independently determined reference values using numerical tolerances. For the squeezing ratio time series, it will compare the values of the ratio at selected early times and the peak value to reference data, also using appropriate tolerances. The two stages are weighted and combined into a final reward between 0 and 1.

The scoring rewards faithful implementation of the described methods. Simply reporting a number that happens to match a known result without executing the required calculations will not succeed, because the verifier checks the detailed shape and internal consistency of your submitted artifacts against the expected physical behavior.
