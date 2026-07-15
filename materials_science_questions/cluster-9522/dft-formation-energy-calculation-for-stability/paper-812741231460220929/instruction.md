# DFT Formation Energy Calculation for Stability

## Problem background
Lithium-rich disordered rock-salt (DRS) oxyfluorides are promising cathode materials because they can store a large amount of lithium. However, the disordered phase may be metastable with respect to an ordered arrangement of the ions, and the tendency to order can affect long-term cycling stability. Density functional theory (DFT) can quantify this thermodynamic preference by computing the energy difference between a special quasirandom structure (SQS) representing the disordered state and the most stable ordered prototype. A positive ΔE (meV/atom) indicates that the ordered structure is lower in energy, i.e., a stronger driving force for ordering. This task asks you to compute the ordering propensity ΔE for three DRS oxyfluoride compositions using DFT.

## Approach
The core idea is to compare the total energy of a disordered structural model with that of a set of ordered candidate structures. For each composition you will:
1. Build a Special Quasirandom Structure (SQS) that mimics the statistical disorder of the rock-salt lattice at the target composition.
2. Construct several ordered prototype supercells derived from known layered oxide types (α‑NaFeO₂ and γ‑LiFeO₂) by placing the cations in an ordered arrangement.
3. Perform DFT structural relaxation and total-energy calculation on every structure (SQS and ordered prototypes) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional, using PAW pseudopotentials and on-site Hubbard U corrections for the transition metals. The calculations follow a standard plane-wave protocol with a high energy cutoff and a dense k‑point mesh.
4. For each composition, identify the lowest total energy among the ordered prototypes, then compute ΔE = E_SQS − min(E_ordered) and convert to meV/atom.
The resulting three ΔE values quantify how strongly each composition prefers the ordered phase, with a smaller ΔE implying a weaker driving force for ordering.

## Reproduction target
Produce the DFT-calculated ordering propensity ΔE for the three compounds Li₂VO₂F, Li₂V₀.₅Ti₀.₅O₂F, and Li₂V₀.₅Fe₀.₅O₂F. The result must be written to `/app/outputs/dft_delta_e.json` as a JSON object with keys 'Li2VO2F', 'Li2V0.5Ti0.5O2F', and 'Li2V0.5Fe0.5O2F', each holding a floating-point number that is the ΔE value in meV/atom.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials (PBE, Hubbard U): https://www.quantum-espresso.org/pseudopotentials
- ATAT (mcsqs) or similar SQS generator: https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- pymatgen: https://pypi.org
- Ordered prototype structures (α-NaFeO₂, γ-LiFeO₂ types)

## Workflow steps

### Step 1: Build SQS and ordered structural models
- Role: process
- Action: For each composition (Li₂VO₂F, Li₂V₀.₅Ti₀.₅O₂F, Li₂V₀.₅Fe₀.₅O₂F), generate one or more Special Quasirandom Structures (SQS) representing the disordered rock-salt phase, and construct a set of candidate ordered prototype structures derived from α-NaFeO₂ and γ-LiFeO₂ types.
- Evidence: `/app/outputs/sqs_structures.zip`

### Step 2: DFT total-energy calculations
- Role: process
- Action: Perform DFT structural relaxations and total-energy calculations for all structures generated in step 1 using Quantum ESPRESSO with PAW pseudopotentials, PBE functional, Hubbard U corrections (U(V)=3.25, U(Ti)=3.50, U(Fe)=4.30), a plane-wave cutoff of 600 eV, k-point spacing ≤ 0.04 Å⁻¹, and force convergence below 0.02 eV/Å.
- Evidence: `/app/outputs/total_energies.csv`

### Step 3: Compute ordering propensity ΔE
- Role: scored (load-bearing)
- Action: For each composition, identify the lowest total energy among the fully relaxed ordered prototypes, then compute ΔE = E_SQS - min(E_ordered) and convert to meV/atom. Write the three ΔE values as a JSON file.
- Output file: `/app/outputs/dft_delta_e.json`
- Format: json
- Contract: JSON object with keys 'Li2VO2F', 'Li2V0.5Ti0.5O2F', 'Li2V0.5Fe0.5O2F'; each value is a float representing ΔE in meV/atom.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_delta_e.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_delta_e.json
- path: `/app/outputs/dft_delta_e.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ordering propensity ΔE values (meV/atom) for the three compositions, defined as the difference between the total energy of the SQS and the lowest-energy ordered prototype.
- schema:
  - `type`: object
  - `required`:
    - `Li2VO2F`: number (meV/atom)
    - `Li2V0.5Ti0.5O2F`: number (meV/atom)
    - `Li2V0.5Fe0.5O2F`: number (meV/atom)

Notes: The checker compares the three ΔE values to the paper's reported numbers with an absolute tolerance and enforces a relative trend condition: the substituted compounds must be at least 20 meV/atom lower than the unsubstituted compound.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_delta_e.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Li2VO2F": "number (meV/atom)",
          "Li2V0.5Ti0.5O2F": "number (meV/atom)",
          "Li2V0.5Fe0.5O2F": "number (meV/atom)"
        }
      },
      "description": "Ordering propensity ΔE values (meV/atom) for the three compositions, defined as the difference between the total energy of the SQS and the lowest-energy ordered prototype."
    }
  ],
  "notes": "The checker compares the three ΔE values to the paper's reported numbers with an absolute tolerance and enforces a relative trend condition: the substituted compounds must be at least 20 meV/atom lower than the unsubstituted compound."
}
```

## How you are scored
A hidden verifier examines the artifacts you produce. It will read `/app/outputs/dft_delta_e.json` and extract the three ΔE values. Each value is compared against a confidential reference that is derived from the same physical procedure. Additionally, the verifier checks whether the two substituted compounds have a ΔE that is meaningfully lower than that of the unsubstituted compound (a relative ordering condition). The reward is a weighted sum of the correctness of the three ΔE numbers and the ordering condition; reporting the paper's numbers without genuine computation is not sufficient. All other workflow evidence files (structural models, total energies) are audited to confirm that the computation was carried out, and they contribute a small weight to the final score.
