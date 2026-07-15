# CNDO/S Molecular Dipole Moment Calculation

## Problem background
Stark spectroscopy can measure the change in dipole moment upon electronic excitation, but the experiment only yields the modulus of the vector difference, losing directional information. Understanding the nature of electronic transitions and comparing with experimental data requires knowledge of the individual ground- and excited-state dipole moments and their Cartesian components along molecular principal axes. This task addresses that need by computing these dipole moments for a set of five C_s-symmetry organic molecules using a semiempirical quantum-chemical method.

## Approach
The calculations are carried out within the CNDO/S (Complete Neglect of Differential Overlap – Spectroscopic) framework. The method computes the electronic wavefunction via a self-consistent field procedure and then evaluates the dipole moment as the sum of two contributions: a net atomic charge term arising from the difference between core charges and valence electron densities, and an atomic polarization term from the mixing of 2s and 2p orbitals on each atom. The resulting Cartesian dipole vector is projected onto the molecule's in-plane principal (a) and minor (b) axes obtained from the inertia tensor. Excited-state dipole moments are obtained by constructing the lowest singlet excited state using virtual orbitals from the ground-state SCF (single-excitation CI). From these, the absolute component changes |Δμ_a| = |μ*_a – μ_a| and |Δμ_b| = |μ*_b – μ_b| are computed. The workflow is applied to five molecules: formyl fluoride, propynal, phenol, p-fluorophenol, and styrene.

## Reproduction target
For formyl fluoride, propynal, phenol, p-fluorophenol, and styrene, compute the ground-state dipole moment (total modulus and a,b components) and the lowest singlet excited-state dipole moment (total modulus and a,b components) using the CNDO/S method. Also compute the absolute component changes |Δμ_a| and |Δμ_b|. Report all quantities in Debye in a single CSV file with one row per molecule, containing columns: molecule (name), mu_ground, mu_ground_a, mu_ground_b, mu_excited, mu_excited_a, mu_excited_b, delta_mu_a, delta_mu_b.

## Assets

- PySCF: pyscf
- Molecular geometries of formyl fluoride, propynal, phenol, p-fluorophenol, and styrene: https://cccbdb.nist.gov/

## Workflow steps

### Step 1: Obtain molecular geometries
- Role: process
- Action: Retrieve Cartesian coordinates for formyl fluoride, propynal, phenol, p-fluorophenol, and styrene from a public chemistry database (e.g., NIST CCCBDB) or construct them from published experimental structures. Save the geometries in a format suitable for CNDO/S input (e.g., XYZ or internal coordinates) and determine the principal axis transformation needed to align dipole components with the in-plane principal (a) and minor (b) axes.
- Evidence: none

### Step 2: Ground-state CNDO/S SCF and dipole calculation
- Role: process
- Action: For each molecule, perform a ground-state CNDO/S self-consistent field calculation using the spectroscopic parametrization. Compute the ground-state dipole moment vector using the net atomic charge and atomic polarization formulas described in the CNDO method. Determine the total modulus |μ| and the Cartesian components projected onto the molecule's principal in-plane axes a and b.
- Evidence: none

### Step 3: Excited-state CNDO/S dipole and component change calculation
- Role: process
- Action: Construct the lowest singlet excited state for each molecule using virtual orbitals from the ground-state SCF (single-excitation CI). Compute the excited-state dipole moment vector, its modulus |μ*|, and the a,b components. Also compute the absolute component changes |Δμ_a| = |μ*_a - μ_a| and |Δμ_b| = |μ*_b - μ_b|.
- Evidence: none

### Step 4: Compile final dipole results into scored CSV
- Role: scored (load-bearing)
- Action: Write dipole_results.csv containing one row per molecule with the computed ground-state total dipole, ground a and b components, excited-state total dipole, excited a and b components, |Δμ_a|, and |Δμ_b|. All dipole moments are in Debye. The rows may be in any order.
- Output file: `/app/outputs/dipole_results.csv`
- Format: csv
- Contract: CSV with header: molecule, mu_ground, mu_ground_a, mu_ground_b, mu_excited, mu_excited_a, mu_excited_b, delta_mu_a, delta_mu_b. All numeric fields are floats in Debye.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_results.csv
- path: `/app/outputs/dipole_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed dipole moments and absolute component changes for the five C_s-symmetry molecules: formyl fluoride, propynal, phenol, p-fluorophenol, and styrene. The checker compares each numeric field against the correct values (derived from the original computation) within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `mu_ground`, `mu_ground_a`, `mu_ground_b`, `mu_excited`, `mu_excited_a`, `mu_excited_b`, `delta_mu_a`, `delta_mu_b`
  - `units`:
    - `mu_ground`: Debye (D)
    - `mu_ground_a`: D
    - `mu_ground_b`: D
    - `mu_excited`: D
    - `mu_excited_a`: D
    - `mu_excited_b`: D
    - `delta_mu_a`: D
    - `delta_mu_b`: D

Notes: Only the five molecules from Table 2 are required. The agent must run the full CNDO/S workflow; pre-computed values are not provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "mu_ground",
          "mu_ground_a",
          "mu_ground_b",
          "mu_excited",
          "mu_excited_a",
          "mu_excited_b",
          "delta_mu_a",
          "delta_mu_b"
        ],
        "units": {
          "mu_ground": "Debye (D)",
          "mu_ground_a": "D",
          "mu_ground_b": "D",
          "mu_excited": "D",
          "mu_excited_a": "D",
          "mu_excited_b": "D",
          "delta_mu_a": "D",
          "delta_mu_b": "D"
        }
      },
      "description": "Computed dipole moments and absolute component changes for the five C_s-symmetry molecules: formyl fluoride, propynal, phenol, p-fluorophenol, and styrene. The checker compares each numeric field against the correct values (derived from the original computation) within a tolerance."
    }
  ],
  "notes": "Only the five molecules from Table 2 are required. The agent must run the full CNDO/S workflow; pre-computed values are not provided."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact. For the primary scored artifact (dipole_results.csv), the verifier extracts all numeric fields and compares them against hidden reference values using an appropriate tolerance. Each correct field contributes to the final reward, which is the fraction of fields correctly reproduced. The verifier combines scores from all scored steps into a single 0–1 reward.
