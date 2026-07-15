# HeH²⁺ 2pσ Variational Energy Calculation

## Problem background
The $\mathrm{HeH}^{2+}$ molecular ion is a simple three-body system that serves as a testbed for approximate quantum-chemical methods. The $2p\sigma$ excited state presents a particular challenge because it is not the lowest state of its symmetry; any trial wavefunction must be orthogonal to the ground $1s\sigma$ state. Moreover, the dissociation products are an H atom and an α particle, so a good approximation must combine the united-atom (small internuclear separation $R$) and separated-atom (large $R$) limits. This task focuses on constructing a combined variational wavefunction for the $2p\sigma$ state that incorporates both limits and enforces orthogonality, then using it to compute total electronic energies $-E$ and potential energies $V$ as functions of $R$. The accuracy of the resulting energies can be assessed by comparing them against exact two-centre reference values.

## Approach
The combined trial wavefunction for the $2p\sigma$ state is built from a united-atom form and a separated-atom form, with an additional term that ensures orthogonality to the ground $1s\sigma$ state. The united-atom part consists of a $2p_z$-like function centred on the charge centre, while the separated-atom part is a $1s$ hydrogenic function on the proton. The orthogonality constraint introduces mixing with the ground state, whose wavefunction itself has to be determined first by variational optimization of a two-exponential form $\exp[-\alpha'(2r_a+r_b)] + p'\exp(-2\beta' r_a)$. Once the optimum ground-state parameters $\alpha', p', \beta'$ are found, the $2p\sigma$ trial function is constructed as a linear combination with three adjustable parameters $\alpha$, $\beta$, $p$, where $\alpha$ governs the united-atom term, $\beta$ the separated-atom term, and $p$ the relative weight between them. For each internuclear distance $R$, the electronic energy functional $E = -\int \Psi^* (\nabla^2 + 4/r_a + 2/r_b) \Psi\, d\tau / \int \Psi^* \Psi\, d\tau$ is minimized with respect to $\alpha,\beta,p$, subject to the orthogonality condition, and the potential energy $V = -\int \Psi^* (4/r_a+2/r_b) \Psi\, d\tau / \int \Psi^* \Psi\, d\tau$ is evaluated at the optimum. The computed $-E$ and $V$ are then compared with exact two-centre results. All integrals are over the electron coordinates $\mathbf{r}_a$ (relative to the helium nucleus A) and $\mathbf{r}_b$ (relative to the proton B).

## Reproduction target
Reproduce the total electronic energies $-E$ and the potential energies $V$ of the $2p\sigma$ state of $\mathrm{HeH}^{2+}$ obtained with the combined variational wavefunction (type vi) at the six internuclear separations $R = 0.5, 1.0, 2.0, 3.0, 4.0, 5.0$ a.u. Write the resulting $-E$ values to `total_energies.csv` and the resulting $V$ values to `potential_energies.csv`, both with columns `R` (a.u.) and the corresponding energy (Hartree). The hidden verifier will compare your reported energies against exact reference values to assess the accuracy of the trial wavefunction.

## Assets

- PySCF (or equivalent quantum chemistry library): pyscf

## Workflow steps

### Step 1: Optimize 1sσ ground state wavefunction
- Role: process
- Action: Variationally optimize the parameters (α', p', β') of the ground state wavefunction Ψ(1sσ) = exp{−α'(2r_a + r_b)} + p' exp(−2β' r_a) for the HeH²⁺ system at each internuclear distance R in {0.5, 1.0, 2.0, 3.0, 4.0, 5.0} a.u. by minimizing the electronic energy functional. The optimized wavefunction will later be used to enforce orthogonality in the 2pσ trial function.
- Evidence: `/app/outputs/1s_sigma_params.json`

### Step 2: Variational minimization of 2pσ wavefunction (type vi)
- Role: process
- Action: For each R, using the optimized 1sσ function, construct the combined trial wavefunction Ψ(2pσ) that mixes united-atom and separated-atom forms with an orthogonality term. Minimize the electronic energy functional with respect to the parameters α, β, p. Compute the total electronic energy (−E) and potential energy (V). Save the optimal parameters and intermediate energies for all R.
- Evidence: `/app/outputs/optimized_energies.json`

### Step 3: Output total electronic energies
- Role: scored (load-bearing)
- Action: Write the optimized total electronic energies (−E) for the six R values to a CSV file.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: Columns: R, total_energy
- Scoring: scored by hidden verifier

### Step 4: Output potential energies
- Role: scored (load-bearing)
- Action: Write the computed potential energies V for the same R values to a CSV file.
- Output file: `/app/outputs/potential_energies.csv`
- Format: csv
- Contract: Columns: R, potential_energy
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/potential_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total electronic energies (−E) of the 2pσ state for HeH²⁺ at R = 0.5, 1.0, 2.0, 3.0, 4.0, 5.0 a.u. computed with the type (vi) variational wavefunction. Scoring checks that percentage errors relative to exact reference values are ≤1% for R ≤ 2 a.u. and ≤3.5% for R = 3 a.u.
- schema:
  - `type`: table
  - `required_columns`: `R`, `total_energy`
  - `units`:
    - `R`: a.u.
    - `total_energy`: Hartree

### potential_energies.csv
- path: `/app/outputs/potential_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Potential energies (V) for the same internuclear distances, computed with the same trial wavefunction. Scoring uses a soft tolerance: percentage error ≤10% for all R.
- schema:
  - `type`: table
  - `required_columns`: `R`, `potential_energy`
  - `units`:
    - `R`: a.u.
    - `potential_energy`: Hartree

Notes: Only the variational energies for the combined wavefunction (type vi) are scored. Exact dipole moments are not part of the reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "total_energy"
        ],
        "units": {
          "R": "a.u.",
          "total_energy": "Hartree"
        }
      },
      "description": "Total electronic energies (−E) of the 2pσ state for HeH²⁺ at R = 0.5, 1.0, 2.0, 3.0, 4.0, 5.0 a.u. computed with the type (vi) variational wavefunction. Scoring checks that percentage errors relative to exact reference values are ≤1% for R ≤ 2 a.u. and ≤3.5% for R = 3 a.u."
    },
    {
      "file": "potential_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "potential_energy"
        ],
        "units": {
          "R": "a.u.",
          "potential_energy": "Hartree"
        }
      },
      "description": "Potential energies (V) for the same internuclear distances, computed with the same trial wavefunction. Scoring uses a soft tolerance: percentage error ≤10% for all R."
    }
  ],
  "notes": "Only the variational energies for the combined wavefunction (type vi) are scored. Exact dipole moments are not part of the reproduction target."
}
```

## How you are scored
A hidden checker reads the output files you write to `/app/outputs`. It compares each total electronic energy and potential energy against a hidden set of exact reference values. It computes the percentage error for each data point, then assigns a reward based on whether the errors fall within pre-defined target thresholds. The reward is a weighted sum across the output artifacts, with the strongest weight on the total energies at the distances where an accurate reproduction has the highest physical relevance. The checker expects energies that result from a genuine variational optimization; hard-coded or guessed values will not meet the required accuracy. No other output is scored.
