# 2-D Wigner Electron Crystal Phases: Energy and Critical Density

## Problem background
In a low-density two-dimensional electron system, strong Coulomb repulsion can drive the electrons into a crystalline arrangement (Wigner crystal) rather than a fluid. The dimensionless density parameter r_s controls the average inter-electron spacing relative to the Bohr radius. The fundamental question is whether the ground state of this Wigner crystal adopts a ferromagnetic spin ordering or a nonmagnetic spin ordering, and at what critical electron density the crystallization first occurs. The present task requires computing the ground-state energies of both magnetic phases on a face-centered square lattice across a range of r_s values, for two models of the positive neutralizing background (uniform and a Yukawa-type distribution with a small screening parameter λ), and then using those energies to locate the critical density where the energy-vs-r_s slope changes abruptly, indicating the onset of crystallization.

## Approach
The calculation uses a localized representation: electrons are described by Wannier functions constructed from a single three-dimensional Gaussian orbital (optimized exponent α) via Löwdin orthogonalization. The Fock–Dirac density matrix is formed with a circular Fermi region, distinguishing nonmagnetic (equal spin-up and spin-down contributions) and ferromagnetic (all spins aligned) configurations. The Hartree–Fock energy functional includes kinetic energy, the exchange interaction, and, for the non-uniform background, the electrostatic energy from a Yukawa-type positive charge distribution p(r) = (λ²/4π) e^{-λr}/r with λ=0.01; for the uniform background the electrostatic self-cancellation yields no direct Coulomb term. The total ground-state energy is obtained by adding the Jonson–Srinivasan correlation energy interpolation, E_c = -1.103/(r_s + 4.41) Ryd. For each r_s and each background model, the Gaussian exponent α is optimized to minimize the Hartree–Fock energy. The workflow repeats this procedure for nine r_s values (10, 20, 30, 40, 50, 75, 100, 130, 200), both spin phases, and both background models. After all energies are computed, a slope analysis of the energy-vs-r_s curve for the Yukawa background identifies the r_s where a discontinuous slope decrease signals the crystallization point; these critical r_s values are then converted to electron densities n = 1/(π (r_s a_0)²) with a_0 = 0.529 Å.

## Reproduction target
Compute ground-state energies (in Rydbergs) for the nonmagnetic and ferromagnetic phases at each of the nine r_s values for both the uniform neutralizing background and the Yukawa-type background (λ=0.01). For each r_s, the optimized Hartree–Fock energy with correlation correction constitutes the reported ground-state energy. Additionally, from the Yukawa-background results, determine the critical r_s values where the slope of energy vs. r_s drops discontinuously for each spin phase, and convert these to electron densities (e cm⁻²) using the standard 2-D relation with a_0 = 0.529 Å. The task does not require reproducing the electron gas reference energies to high accuracy; their inclusion is for completeness and serves as a sanity check.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute ground-state energies with uniform background
- Role: scored
- Action: For each electron density parameter r_s from {10, 20, 30, 40, 50, 75, 100, 130, 200}, compute the Hartree-Fock ground-state energy for both nonmagnetic and ferromagnetic spin configurations using the Wannier-function method with a single Gaussian orbital (optimizing the Gaussian exponent α to minimize the Hartree-Fock energy), uniform neutralizing positive background (V_c=0), and the Jonson–Srinivasan correlation interpolation E_c = -1.103/(r_s+4.41) Ryd. Also compute the reference 2-D electron gas energy. Write results to CSV.
- Output file: `/app/outputs/energies_uniform.csv`
- Format: csv
- Contract: columns: rs (float), nonmagnetic_energy (float, Rydbergs), ferromagnetic_energy (float, Rydbergs), electron_gas_energy (float, Rydbergs)
- Scoring: scored by hidden verifier

### Step 2: Compute ground-state energies with Yukawa background
- Role: scored (load-bearing)
- Action: For each r_s from {10, 20, 30, 40, 50, 75, 100, 130, 200}, compute the Hartree-Fock ground-state energy for nonmagnetic and ferromagnetic phases using a Yukawa-type positive background (p(r) = (λ²/4π) e^{-λr}/r with λ=0.01), employing the same Wannier-function method and correlation interpolation. Optimize α for each configuration. Also compute the reference electron gas energy. Write results to CSV.
- Output file: `/app/outputs/energies_yukawa.csv`
- Format: csv
- Contract: columns: rs (float), nonmagnetic_energy (float, Ryd), ferromagnetic_energy (float, Ryd), electron_gas_energy (float, Ryd)
- Scoring: scored by hidden verifier

### Step 3: Determine critical r_s and electron densities for Wigner crystallization
- Role: scored (load-bearing)
- Action: From the energies computed with the Yukawa background (energies_yukawa.csv), calculate the slope of the energy vs. r_s curve for the nonmagnetic and ferromagnetic phases. Identify the r_s value where a discontinuous decrease in slope occurs, indicating onset of crystallization. Convert critical r_s to electron densities (e cm⁻²) using n = 1 / (π (r_s a_0)²) with a_0 = 0.529 Å. Output the critical r_s and densities as a JSON file.
- Output file: `/app/outputs/critical_densities.json`
- Format: json
- Contract: JSON object with keys: nonmagnetic_critical_r_s (float), nonmagnetic_critical_density_cm2 (float), ferromagnetic_critical_r_s (float), ferromagnetic_critical_density_cm2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies_uniform.csv`
- `/app/outputs/energies_yukawa.csv`
- `/app/outputs/critical_densities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies_uniform.csv
- path: `/app/outputs/energies_uniform.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ground-state energies for uniform neutralizing background. The hidden checker compares to the paper's Table I with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `rs`, `nonmagnetic_energy`, `ferromagnetic_energy`, `electron_gas_energy`
  - `units`:
    - `rs`: dimensionless
    - `nonmagnetic_energy`: Ryd
    - `ferromagnetic_energy`: Ryd
    - `electron_gas_energy`: Ryd

### energies_yukawa.csv
- path: `/app/outputs/energies_yukawa.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ground-state energies for Yukawa-type positive background (λ=0.01). The hidden checker compares to reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `rs`, `nonmagnetic_energy`, `ferromagnetic_energy`, `electron_gas_energy`
  - `units`:
    - `rs`: dimensionless
    - `nonmagnetic_energy`: Ryd
    - `ferromagnetic_energy`: Ryd
    - `electron_gas_energy`: Ryd

### critical_densities.json
- path: `/app/outputs/critical_densities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical electron density parameter r_s and corresponding electron density derived from the slope analysis of the Yukawa-background energies.
- schema:
  - `type`: object
  - `required`:
    - `nonmagnetic_critical_r_s`: float
    - `nonmagnetic_critical_density_cm2`: float (e/cm²)
    - `ferromagnetic_critical_r_s`: float
    - `ferromagnetic_critical_density_cm2`: float (e/cm²)

Notes: The electron gas energy column is included for completeness; its exact reproduction is not strictly required but its values must be reasonable negative numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies_uniform.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rs",
          "nonmagnetic_energy",
          "ferromagnetic_energy",
          "electron_gas_energy"
        ],
        "units": {
          "rs": "dimensionless",
          "nonmagnetic_energy": "Ryd",
          "ferromagnetic_energy": "Ryd",
          "electron_gas_energy": "Ryd"
        }
      },
      "description": "Ground-state energies for uniform neutralizing background. The hidden checker compares to the paper's Table I with tolerances."
    },
    {
      "file": "energies_yukawa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rs",
          "nonmagnetic_energy",
          "ferromagnetic_energy",
          "electron_gas_energy"
        ],
        "units": {
          "rs": "dimensionless",
          "nonmagnetic_energy": "Ryd",
          "ferromagnetic_energy": "Ryd",
          "electron_gas_energy": "Ryd"
        }
      },
      "description": "Ground-state energies for Yukawa-type positive background (λ=0.01). The hidden checker compares to reference values within tolerances."
    },
    {
      "file": "critical_densities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "nonmagnetic_critical_r_s": "float",
          "nonmagnetic_critical_density_cm2": "float (e/cm²)",
          "ferromagnetic_critical_r_s": "float",
          "ferromagnetic_critical_density_cm2": "float (e/cm²)"
        }
      },
      "description": "Critical electron density parameter r_s and corresponding electron density derived from the slope analysis of the Yukawa-background energies."
    }
  ],
  "notes": "The electron gas energy column is included for completeness; its exact reproduction is not strictly required but its values must be reasonable negative numbers."
}
```

## How you are scored
A hidden verifier will independently score each output artifact. The numerical values in `energies_uniform.csv` and `energies_yukawa.csv` are compared against reference results derived from the original publication within defined tolerances. The critical r_s and electron densities in `critical_densities.json` are also compared to reference values. Reporting only the paper's published numbers without performing the actual computation will not meet the accuracy requirements. The final reward is a weighted combination of these scores, with the main weight on the Yukawa-background energies and the critical densities.
