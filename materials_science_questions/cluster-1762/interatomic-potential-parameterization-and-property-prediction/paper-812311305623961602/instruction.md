# Compute Static Dipole Polarizabilities of Negative Ions using Variational Density-Functional Method

## Problem background
Accurate calculation of atomic dipole polarizabilities usually requires solving the Schrödinger equation in an external electric field using orbital-based perturbation theory, which quickly becomes computationally demanding. This work presents an alternative variational density-functional method that circumvents the orbital perturbation by working directly with the ground-state electron density. The method uses a physically motivated ansatz for the field-induced density change and a kinetic energy functional expressed in terms of the density itself, making it numerically simpler while still yielding accurate polarizabilities for negative ions.

## Approach
The core idea is a variational minimization of the second-order energy change under a uniform electric field. First, the ground-state radial electron density for each ion is obtained from a Hartree–Fock calculation with a large basis set. Then the induced density is parameterized by Δ(r) = a r + b r² + c r³. The change in total energy ΔE up to order ℰ² is expressed using the kinetic energy functional T_S[ρ] = T_W[ρ] + f(N) T_TF[ρ], where T_W is the von Weizsäcker term, T_TF the Thomas–Fermi term, and f(N) = (1 – 2/N)(1 – A₁/N^{1/3} + A₂/N^{2/3}) with A₁ = 1.314, A₂ = 0.0021. Exchange is treated within the local density approximation; no correlation energy is included, consistent with the use of Hartree–Fock ground-state densities. The quantity ΔE / ℰ² is minimized with respect to a, b, c, and the static dipole polarizability follows as α = –2 ΔE / ℰ².

## Reproduction target
For the five negative ions H⁻, F⁻, Cl⁻, Br⁻, I⁻, you must first compute the spherical Hartree–Fock ground-state radial electron densities using a large basis set (e.g., aug-cc-pV5Z) and then implement the variational density-functional method described above to obtain the static dipole polarizability for each ion. Report all five polarizabilities in atomic units in a single CSV file.

## Assets

- PySCF: pyscf
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Hartree-Fock ground-state densities
- Role: process
- Action: For each ion (H⁻, F⁻, Cl⁻, Br⁻, I⁻), perform a Hartree-Fock calculation using a large basis set (e.g., aug-cc-pV5Z) with PySCF to obtain the spherically averaged radial electron density ρ⁰(r). Store the radial grid and density array for each ion in a NumPy file for use in the next step.
- Evidence: `/app/outputs/hf_densities.npy`

### Step 2: Calculate static dipole polarizabilities
- Role: scored (load-bearing)
- Action: For each ion, implement the variational density-functional method using the computed HF densities. Construct the induced density ansatz Δ(r)=ar+br²+cr³, compute the change in total energy ΔE up to second order in the electric field using the kinetic energy functional Tₛ[ρ]=T_W[ρ]+f(N)T_TF[ρ] (with f(N) given by Eq. (18) in the paper and parameters A1=1.314, A2=0.0021) and LDA exchange only (no correlation, consistent with HF densities). Minimize ΔE/ℰ² with respect to a, b, c to obtain optimal parameters, then compute the polarizability α = -2ΔE/ℰ². Write the computed polarizabilities for all five ions to a CSV file.
- Output file: `/app/outputs/polarizabilities.csv`
- Format: csv
- Contract: CSV with header: Ion,Polarizability. Each row: ion identifier (H-, F-, Cl-, Br-, I-) and its computed polarizability as a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarizabilities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarizabilities.csv
- path: `/app/outputs/polarizabilities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static dipole polarizabilities computed by the variational density-functional method for the ions H⁻, F⁻, Cl⁻, Br⁻, I⁻.
- schema:
  - `type`: table
  - `required_columns`: `Ion`, `Polarizability`
  - `units`:
    - `Polarizability`: atomic units

Notes: The checker will compare each ion's polarizability against hidden reference values using relative error tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarizabilities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ion",
          "Polarizability"
        ],
        "units": {
          "Polarizability": "atomic units"
        }
      },
      "description": "Static dipole polarizabilities computed by the variational density-functional method for the ions H⁻, F⁻, Cl⁻, Br⁻, I⁻."
    }
  ],
  "notes": "The checker will compare each ion's polarizability against hidden reference values using relative error tolerance."
}
```

## How you are scored
A hidden verifier will read your polarizabilities.csv and compare each ion's reported polarizability against a hidden reference value obtained from the same method as originally described. Scoring is based on how accurately your computed numbers match the reference, with an appropriate tolerance that accounts for legitimate numerical and implementation differences. Each ion contributes to the final score; the exact tolerance is not disclosed, but a correct implementation that faithfully follows the described procedure will produce results that fall within the acceptable range.
