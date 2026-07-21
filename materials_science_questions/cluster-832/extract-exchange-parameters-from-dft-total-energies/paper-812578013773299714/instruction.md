# Landau and bond-operator model of spin chirality in a quantum dimer magnet

## Problem background
In the quantum dimer magnet TlCuCl₃, an applied magnetic field can drive a magnon Bose-Einstein condensation (BEC) that simultaneously induces antiferromagnetic order and ferroelectricity. The spontaneous electric polarization P is proportional to the magnitude of the vector spin chirality ⟨S_l × S_r⟩ on a dimer. This chirality can be split into a contribution from the ordered magnetic moments, |⟨S_l⟩×⟨S_r⟩|, and a contribution from quantum spin fluctuations, |⟨ΔS_l×ΔS_r⟩|. Applying hydrostatic pressure changes the intra- and inter-dimer exchange interactions, which in turn modifies the magnetic ordering temperature, the balance between the ordered and fluctuation parts of the chirality, and the coercivity of the ferroelectric state. The task is to compute these pressure-dependent quantities from first principles using Landau theory and a bond-operator mean-field treatment, thereby exploring how quantum fluctuations and entanglement evolve as the system is pressured away from the quantum critical point.

## Approach
Three independent theoretical analyses are performed.

**Landau phase boundary:** A Ginzburg-Landau free energy expansion F = A m² + B m⁴ is used. The coefficient A depends on temperature T, magnetic field H, and pressure p through a known linear combination: a constant reference plus terms scaling as (T/T₀)^φ, −(H/H₀)², and −(p/p₀). The magnetic ordering transition occurs when A = 0. Solving this condition at the fixed field H = 14 T yields the critical temperature Tc as a function of pressure.

**Bond-operator calculation:** The quantum state of a single dimer is described by a coherent superposition of the singlet |0,0⟩ and the two triplet states |1,±1⟩ with real coefficients (u, v, f, g). These coefficients are obtained by solving the self-consistent mean-field equations at zero temperature and H = 14 T, using pressure-dependent exchange couplings: intradimer J(p) = J – a p and interdimer couplings J̃_k(p) = J̃_k + b p (k = 1,2,3), with J, J̃_k, a, and b given as numerical constants. From the ground-state wavefunction, the total chirality magnitude |⟨S_l × S_r⟩|, its ordered part |⟨S_l⟩×⟨S_r⟩|, and the fluctuation part are computed. The fluctuation part is obtained as the difference between the total and ordered magnitudes. The entanglement entropy s is computed from the eigenvalues of the matrix C̃ C̃ᵀ, where C̃ is formed from the wavefunction coefficients.

**Anisotropic barrier:** To model the electric-field reversal of polarization, an in-plane magnetic anisotropy is added to the Landau free energy, introducing a term –2γ m² cos 2θ. The potential barrier ΔU that must be overcome to rotate the staggered magnetisation by 180° is then a linear function of the pressure (at T = 0, H = 14 T). It is evaluated using the same Landau parameters and a given value of 2γ a₀/B.

## Reproduction target
Produce CSV tables that report the following quantities at H = 14 T for the pressure values p = 0, 2, 4, 6, 8, 10 kbar:

1. **phase_boundary.csv** — critical temperature Tc (in K) obtained from the Landau condition A = 0.

2. **chirality_pressure.csv** — from the bond-operator calculation: the total vector spin chirality magnitude, the ordered-moment contribution, the quantum-fluctuation contribution, and the entanglement entropy.

3. **barrier_pressure.csv** — the potential barrier ΔU (in J/m²) from the anisotropic Landau theory.

All values should be computed directly from the prescribed models and the given numerical constants; no external data or fitting is required.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute pressure-dependent critical temperature from Landau theory
- Role: scored
- Action: Using the Landau free energy condition A=0 with parameters H0=5.5 T, p0=0.42 kbar, T0=5.0 K, phi=3.0, and H=14 T, solve for the critical temperature Tc as a function of pressure at p = 0,2,4,6,8,10 kbar. Write the (p, Tc) pairs to CSV.
- Output file: `/app/outputs/phase_boundary.csv`
- Format: csv
- Contract: Columns: pressure_kbar (float), critical_temp_K (float).
- Scoring: scored by hidden verifier

### Step 2: Bond-operator calculation of chirality components and entanglement entropy
- Role: scored (load-bearing)
- Action: Implement the bond-operator mean-field theory for a single dimer at zero temperature and H=14 T. Use pressure-dependent exchange parameters: intradimer J(p)=5.5-0.14p meV, interdimer J1(p)=0.43+0.075p meV, J2(p)=3.16+0.075p meV, J3(p)=0.91+0.075p meV. Solve for the ground-state coefficients and compute the total vector spin chirality magnitude, ordered-moment contribution, fluctuation contribution, and entanglement entropy from the eigenvalues of the coefficient matrix. Output these values for p = 0,2,4,6,8,10 kbar as CSV.
- Output file: `/app/outputs/chirality_pressure.csv`
- Format: csv
- Contract: Columns: pressure_kbar (float), total_chirality (float), ordered_contribution (float), fluctuation_contribution (float), entanglement_entropy (float).
- Scoring: scored by hidden verifier

### Step 3: Compute potential barrier ΔU from anisotropic Landau theory
- Role: scored
- Action: Using the anisotropic Landau free energy and the constant 2γ a0/B = 0.0225 J/m², evaluate the potential barrier ΔU at T=0 K and H=14 T for pressures p = 0,2,4,6,8,10 kbar. Write the (p, ΔU) pairs to CSV.
- Output file: `/app/outputs/barrier_pressure.csv`
- Format: csv
- Contract: Columns: pressure_kbar (float), potential_barrier_J_per_m2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary.csv`
- `/app/outputs/chirality_pressure.csv`
- `/app/outputs/barrier_pressure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary.csv
- path: `/app/outputs/phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Pressure dependence of the magnetic ordering temperature at H=14 T.
- schema:
  - `type`: table
  - `required_columns`: `pressure_kbar`, `critical_temp_K`
  - `units`:
    - `pressure_kbar`: kbar
    - `critical_temp_K`: K

### chirality_pressure.csv
- path: `/app/outputs/chirality_pressure.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Pressure dependence of the vector spin chirality, its ordered and fluctuation parts, and entanglement entropy.
- schema:
  - `type`: table
  - `required_columns`: `pressure_kbar`, `total_chirality`, `ordered_contribution`, `fluctuation_contribution`, `entanglement_entropy`
  - `units`:
    - `pressure_kbar`: kbar
    - `total_chirality`: dimensionless (magnitude of cross product)
    - `ordered_contribution`: dimensionless
    - `fluctuation_contribution`: dimensionless
    - `entanglement_entropy`: dimensionless

### barrier_pressure.csv
- path: `/app/outputs/barrier_pressure.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Pressure dependence of the potential barrier for polarization reversal.
- schema:
  - `type`: table
  - `required_columns`: `pressure_kbar`, `potential_barrier_J_per_m2`
  - `units`:
    - `pressure_kbar`: kbar
    - `potential_barrier_J_per_m2`: J/m^2

Notes: All quantities are compared against the paper's digitized values with hidden absolute/relative tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_kbar",
          "critical_temp_K"
        ],
        "units": {
          "pressure_kbar": "kbar",
          "critical_temp_K": "K"
        }
      },
      "description": "Pressure dependence of the magnetic ordering temperature at H=14 T."
    },
    {
      "file": "chirality_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_kbar",
          "total_chirality",
          "ordered_contribution",
          "fluctuation_contribution",
          "entanglement_entropy"
        ],
        "units": {
          "pressure_kbar": "kbar",
          "total_chirality": "dimensionless (magnitude of cross product)",
          "ordered_contribution": "dimensionless",
          "fluctuation_contribution": "dimensionless",
          "entanglement_entropy": "dimensionless"
        }
      },
      "description": "Pressure dependence of the vector spin chirality, its ordered and fluctuation parts, and entanglement entropy."
    },
    {
      "file": "barrier_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_kbar",
          "potential_barrier_J_per_m2"
        ],
        "units": {
          "pressure_kbar": "kbar",
          "potential_barrier_J_per_m2": "J/m^2"
        }
      },
      "description": "Pressure dependence of the potential barrier for polarization reversal."
    }
  ],
  "notes": "All quantities are compared against the paper's digitized values with hidden absolute/relative tolerances."
}
```

## How you are scored
A hidden verifier independently assesses each of the three CSV files. For each quantity, it compares your reported values at the specified pressure points against a hidden set of reference values that correspond to the paper’s calculated results. The comparison uses appropriate tolerances: an absolute tolerance for the critical temperature, and relative tolerances for the chirality components and the potential barrier. The per‑stage rewards are combined by weight into a final score between 0 and 1. Correctly executing the required numerical procedures and producing self‑consistent outputs is essential; simply copying numbers without performing the computations will not pass the verifier’s format and consistency checks, and is not guaranteed to match the hidden reference.
