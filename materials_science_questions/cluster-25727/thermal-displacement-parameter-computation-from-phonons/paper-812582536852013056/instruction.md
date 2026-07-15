# Vibronic model of temperature-dependent spin-Hamiltonian parameters A and b2^0 for Mn2+ in Ca(OH)2

## Problem background
Electron paramagnetic resonance (EPR) measurements on Mn²⁺ substituting for Ca²⁺ in single-crystal Ca(OH)₂ show a pronounced temperature dependence of the spin-Hamiltonian parameters: the isotropic hyperfine constant A decreases markedly and the axial zero-field splitting parameter b₂⁰ changes sign as the temperature is raised from liquid-helium temperatures to about 800 K. The paper develops a vibronic model to explain these observations by treating the orbit-lattice interaction within a D₃₁ XY₆ cluster that includes both point-charge and point-dipole contributions from the surrounding OH⁻ ions. The temperature variation of A is described by an orbit-lattice mechanism that admixes ns excited configurations into the 3d⁵ ground state via the lattice vibrations, while the axial parameter b₂⁰ is attributed to phonon modulation of the crystal field. An additional covalent spin-polarisation channel is considered separately. The model computes A(T) and b₂⁰(T) from the rigid-lattice values, a set of dimensionless coupling coefficients, and phonon integrals evaluated in Debye (acoustic) and Einstein (optical) approximations. The required crystal-structure data, effective charges, dipole moment, elastic parameters, Debye temperature, sound velocities, optical phonon frequencies, and the relevant interaction sums are all supplied in this instruction. The task is to implement these calculations and produce the temperature-dependent quantities over the full experimental range.

## Approach
The computation proceeds in three independent but related threads, all built on the same set of phonon-mode integrals.

1. **Phonon integrals:** For a D₃₁ XY₆ cluster, the orbit-lattice coupling coefficients and angular factors are written down for the totally symmetric and doubly degenerate modes that can admix excited configurations. Using the given interionic distance, effective charges, dipole moment, Debye temperature, sound velocities (transverse and longitudinal), mass density, Debye cut-off wavevector, and the optical phonon frequencies, the acoustic-branch Debye integrals and optical-branch Einstein integrals are evaluated on the temperature grid 0, 100, 200, …, 800 K. The acoustic integrals are computed separately for transverse and longitudinal branches; the optical integrals use two representative frequencies (247 cm⁻¹ and 282 cm⁻¹), each contributing one longitudinal and two transverse branches.

2. **Hyperfine constant A(T) – orbit-lattice channel:** The isotropic hyperfine constant Aₒₗ(T) is expressed in terms of a rigid-lattice constant Aᵖ and a dimensionless coefficient D, multiplied by the sum of the acoustic and optical phonon integrals. A small static-axial term, estimated to be negligible, is omitted.

3. **Hyperfine constant – covalent channel:** The temperature-dependent reduction ΔÂ₂₅(T) from covalent spin polarisation is computed analogously, using a different set of integrals that involve the same acoustic and optical modes but with coefficients appropriate for the covalent overlap channel, together with a given covalency dimensionless coefficient D̂₂₅ and a covalent interaction sum.

4. **Axial parameter b₂⁰(T) – vibronic channel:** The explicit-phonon contribution to b₂⁰ is obtained by evaluating acoustic Debye integrals with symmetry-specific coupling coefficients Wᵢ that arise from the second-order expansion of the orbit-lattice potential. The result is combined with the rigid-lattice axial value b₂R⁰ and a dimensionless coefficient D' to yield b₂⁰(T) on the same temperature grid. Optical contributions to b₂⁰ are neglected in this channel, as their effect is small.

All calculations are purely algebraic and integral-based; the agent must re-implement the coupling-coefficient expressions and the required Debye/Einstein integrals from the supplied constants.

## Reproduction target
You must compute three temperature-dependent quantities at the nine temperatures 0, 100, 200, 300, 400, 500, 600, 700, and 800 K:
- The isotropic hyperfine constant from the orbit-lattice model, A_OL(T), in gauss.
- The covalency reduction of the hyperfine constant, ΔA_cov(T), in gauss.
- The vibronic contribution to the axial zero-field splitting parameter, b₂⁰_vibronic(T), in gauss.

Produce one CSV file per quantity, each containing two columns: temperature T (K) and the corresponding computed value. The files must be named A_orbit_lattice.csv, A_covalency.csv, and b2_vibronic.csv and written to the /app/outputs directory. All required physical constants and material parameters are provided in the Assets section and in the step instructions that follow; no external data retrieval is needed beyond what is stated here.

## Assets

- Ca(OH)2 crystal and phonon parameters

## Workflow steps

### Step 1: Compute acoustic and optical phonon integrals
- Role: process
- Action: Implement the orbit-lattice coupling coefficients and angular factors for the D3d XY6 cluster. Evaluate the Debye-model acoustic-branch integrals F_ac(T) and Einstein-model optical-branch integrals F_op(T) for all relevant branches at temperatures 0, 100, 200, ..., 800 K using the supplied crystal and elastic parameters. Save the total acoustic and optical contributions for later steps.
- Evidence: `/app/outputs/phonon_integrals.csv`

### Step 2: Compute orbit-lattice hyperfine constant A(T)
- Role: scored (load-bearing)
- Action: From phonon_integrals.csv and the given rigid-lattice hyperfine constant A_R and dimensionless coefficient D, compute the orbit-lattice contribution A_OL(T) at temperatures 0, 100, ..., 800 K using the formula A_OL(T) = A_R [1 - D * sum_sigma F_ac^sigma(T) + sum_r F_op^{sigma,r}(T)] (the small static axial term is neglected). Output the results.
- Output file: `/app/outputs/A_orbit_lattice.csv`
- Format: csv
- Contract: Columns: T (K), A_theory (G)
- Scoring: scored by hidden verifier

### Step 3: Compute covalency reduction of hyperfine constant
- Role: scored
- Action: Using the covalent model parameters (mixing coefficients, overlap sums, and covalency dimensionless coefficient D_cov) together with separate acoustic and optical integrals for the covalent channel, calculate the temperature-dependent reduction ΔA_cov(T) at the same temperatures and output the result.
- Output file: `/app/outputs/A_covalency.csv`
- Format: csv
- Contract: Columns: T (K), Delta_A_cov (G)
- Scoring: scored by hidden verifier

### Step 4: Compute vibronic contribution to axial parameter b2^0(T)
- Role: scored (load-bearing)
- Action: Compute the vibronic (explicit phonon) contribution to the axial zero-field splitting parameter. First evaluate the acoustic Debye integrals with the symmetry-specific coupling coefficients W_i, then combine with the rigid-lattice b2R^0 and the dimensionless D' to obtain b2^0_vibronic(T). Output the results at the same temperature grid.
- Output file: `/app/outputs/b2_vibronic.csv`
- Format: csv
- Contract: Columns: T (K), b2_vibronic_theory (G)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/A_orbit_lattice.csv`
- `/app/outputs/A_covalency.csv`
- `/app/outputs/b2_vibronic.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### A_orbit_lattice.csv
- path: `/app/outputs/A_orbit_lattice.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed temperature-dependent isotropic hyperfine constant from the orbit-lattice model. The checker recomputes A_OL(T) from the phonon_integrals.csv evidence and the given A_R and D, then compares to a hidden reference with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `A_theory`
  - `units`:
    - `T`: K
    - `A_theory`: G

### A_covalency.csv
- path: `/app/outputs/A_covalency.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent reduction of the hyperfine constant from covalent spin polarization. The checker recomputes from the covalent channel evidence and compares to a hidden reference with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Delta_A_cov`
  - `units`:
    - `T`: K
    - `Delta_A_cov`: G

### b2_vibronic.csv
- path: `/app/outputs/b2_vibronic.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Vibronic contribution to the axial zero-field splitting parameter. The checker recomputes b2^0_vibronic(T) from the phonon_integrals evidence and the given b2R^0 and D', then compares to a hidden reference with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `b2_vibronic_theory`
  - `units`:
    - `T`: K
    - `b2_vibronic_theory`: G

Notes: The hidden checker will read the agent's phonon_integrals.csv evidence to recompute the orbit-lattice A(T) and b2^0(T) using the same algebraic expressions, then compare against stored reference values with a relative tolerance of 10% for values >= 1 G and an absolute tolerance of 0.5 G for smaller values. Monotonicity trends (A decreasing, b2^0 crossing zero near 450 K) are also audited as low-weight structural checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "A_orbit_lattice.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "A_theory"
        ],
        "units": {
          "T": "K",
          "A_theory": "G"
        }
      },
      "description": "Computed temperature-dependent isotropic hyperfine constant from the orbit-lattice model. The checker recomputes A_OL(T) from the phonon_integrals.csv evidence and the given A_R and D, then compares to a hidden reference with tolerances."
    },
    {
      "file": "A_covalency.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Delta_A_cov"
        ],
        "units": {
          "T": "K",
          "Delta_A_cov": "G"
        }
      },
      "description": "Temperature-dependent reduction of the hyperfine constant from covalent spin polarization. The checker recomputes from the covalent channel evidence and compares to a hidden reference with tolerances."
    },
    {
      "file": "b2_vibronic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "b2_vibronic_theory"
        ],
        "units": {
          "T": "K",
          "b2_vibronic_theory": "G"
        }
      },
      "description": "Vibronic contribution to the axial zero-field splitting parameter. The checker recomputes b2^0_vibronic(T) from the phonon_integrals evidence and the given b2R^0 and D', then compares to a hidden reference with tolerances."
    }
  ],
  "notes": "The hidden checker will read the agent's phonon_integrals.csv evidence to recompute the orbit-lattice A(T) and b2^0(T) using the same algebraic expressions, then compare against stored reference values with a relative tolerance of 10% for values >= 1 G and an absolute tolerance of 0.5 G for smaller values. Monotonicity trends (A decreasing, b2^0 crossing zero near 450 K) are also audited as low-weight structural checks."
}
```

## How you are scored
A hidden verifier will independently recompute each of the three quantities from the raw phonon-integral evidence you submit. For the orbit-lattice A(T) and the vibronic b₂⁰(T), the verifier will use your phonon_integrals.csv together with the rigid-lattice constants and dimensionless coefficients given in the instructions; for the covalent channel it will recompute from the corresponding covalency integrals. Each recomputed value is compared to a reference derived from the paper’s reported results using appropriate tolerances. Reward is assigned based on how many temperature points fall within the tolerance window. In addition, the verifier will check that the computed temperature dependencies exhibit physically expected trends (e.g., A decreasing with temperature, b₂⁰ changing sign). The final scoring reward is a weighted combination of the scores for the three artifacts; no single reported number is sufficient to pass, and the verifier independently recomputes the quantities rather than simply reading your output.
