# Interstitial formation energy and entropy via discrete atomistic simulation

## Problem background
Interstitial solid solutions, such as carbon dissolved in face-centered cubic nickel, are important for understanding thermodynamic properties of alloys and impurity behavior. The partial formation energy and the partial excess vibrational entropy quantify the energy change and the perturbation of the vibrational spectrum when a single solute atom is inserted into the host lattice. These quantities are challenging to calculate because the impurity distorts the surrounding lattice, altering both the potential energy and the normal vibrational frequencies of many host atoms. This task implements an atomistically discrete simulation model to compute these quantities for a single carbon interstitial in nickel.

## Approach
We adopt a pairwise interaction model: the Ni-Ni interaction is represented by a truncated Morse potential (parameters α, D, r0 given in the assets), and the C-Ni interaction is a purely repulsive soft-sphere potential of the form A exp(-ρr) (parameters A, ρ given in the assets). The calculation proceeds in four stages. (1) For the perfect Ni crystal (f.c.c., lattice constant from the paper), we compute the per-atom potential energy and, using the Einstein approximation, the three normal-mode vibration frequencies for each Ni atom within a simulation region extending about 3.91 lattice parameters from a chosen reference site. (2) We then introduce a carbon atom at an octahedral interstitial site (0,0,½ in lattice coordinates) and relax the surrounding Ni atoms shell by shell using a Newton-Raphson procedure until convergence (typically 24 shells, 586 atoms relaxed). (3) From the relaxed defect configuration, we compute the partial formation energy E_u as the sum over all affected Ni atoms of (W_i′ − W_i⁰) plus the carbon atom's own potential energy Φ_uv. (4) Finally, we compute the three normal-mode frequencies of the carbon solute and the defect-crystal frequencies for all affected Ni atoms, and evaluate the partial excess vibrational entropy at 1000 K using the formula S_u^v/k = 3(1+log(kT/hν_u)) + Σ log(ν_i⁰/ν_i^f). All metal atoms beyond the relaxation region are assumed unaffected.

## Reproduction target
Compute and report two scalar quantities for a single carbon interstitial in f.c.c. nickel at 1000 K: (i) the partial formation energy E_u, in kilocalories per mole (kcal/mol), saved as formation_energy.txt; (ii) the partial excess vibrational entropy S_u^v/k (dimensionless), saved as excess_entropy.txt. Use the provided Morse potential parameters for Ni and the soft-sphere potential parameters for C-Ni. Follow the simulation protocol described in the workflow steps, including the perfect-crystal reference calculation and the defect relaxation, to obtain these quantities.

## Assets

- Morse potential parameters for Ni
- Soft-sphere C-Ni potential parameters

## Workflow steps

### Step 1: Perfect crystal reference
- Role: process
- Action: Construct the perfect f.c.c. nickel lattice (lattice constant from paper) and, using the Morse potential, compute the per-atom potential energy W_i^0 and the three normal-mode frequencies ν_i^0 (via the force-constant matrix) for every Ni atom in the simulation region.
- Evidence: `/app/outputs/perfect_reference.json`

### Step 2: Defect crystal relaxation (octahedral)
- Role: process
- Action: Place a carbon atom at the octahedral site (0,0,½) in the Ni lattice. Using the soft-sphere C-Ni potential and the Morse potential, iteratively relax the positions of the surrounding Ni atoms by solving the force-balance equations shell-by-shell until convergence (e.g., using the Newton-Raphson procedure described in the paper). Record the relaxed atomic coordinates.
- Evidence: `/app/outputs/relaxed_octahedral.json`

### Step 3: Partial formation energy
- Role: scored (load-bearing)
- Action: From the per-atom energies in the perfect crystal (W_i^0) and the relaxed defect crystal (W_i′), together with the carbon atom's potential energy Φ_uv, compute the partial formation energy E_u = Σ(W_i′ - W_i^0) + Φ_uv. Report the value in kcal/mol.
- Output file: `/app/outputs/formation_energy.txt`
- Format: txt
- Contract: A single floating-point number (kcal/mol).
- Scoring: scored by hidden verifier

### Step 4: Partial excess vibrational entropy
- Role: scored (load-bearing)
- Action: Compute the three normal-mode frequencies of the carbon solute (ν_u) and the defect-crystal frequencies ν_i^f for all affected Ni atoms. Using the reference frequencies ν_i^0 from step 1, calculate the partial excess vibrational entropy at T=1000 K: S_u^v/k = 3(1+log(kT/hν_u)) + Σ log(ν_i^0/ν_i^f). Report the dimensionless value S_u^v/k.
- Output file: `/app/outputs/excess_entropy.txt`
- Format: txt
- Contract: A single floating-point number (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energy.txt`
- `/app/outputs/excess_entropy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energy.txt
- path: `/app/outputs/formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Partial formation energy E_u of a carbon interstitial in nickel, computed as a single floating‑point number.
- schema:
  - `type`: text
  - `units`: kcal/mol

### excess_entropy.txt
- path: `/app/outputs/excess_entropy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Partial excess vibrational entropy S_u^v/k (dimensionless) of a carbon interstitial in nickel, computed as a single floating‑point number.
- schema:
  - `type`: text
  - `units`: dimensionless (S_u^v/k)

Notes: No gold values or tolerances are disclosed. The checker will compare the agent's reported scalars to reference values within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "kcal/mol"
      },
      "description": "Partial formation energy E_u of a carbon interstitial in nickel, computed as a single floating‑point number."
    },
    {
      "file": "excess_entropy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": "dimensionless (S_u^v/k)"
      },
      "description": "Partial excess vibrational entropy S_u^v/k (dimensionless) of a carbon interstitial in nickel, computed as a single floating‑point number."
    }
  ],
  "notes": "No gold values or tolerances are disclosed. The checker will compare the agent's reported scalars to reference values within appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that checks the two scored output files against reference values. The verifier does not run your simulation; it reads your reported numbers and compares them to the expected results, applying appropriate tolerances. The two outputs are combined by weight: the partial formation energy (formation_energy.txt) contributes 60% of the total score, and the partial excess vibrational entropy (excess_entropy.txt) contributes 40%. To earn credit, you must execute the workflow steps as described; a submission that only writes numbers without completing the intermediate process steps may be rejected. The verifier may also verify that the required intermediate evidence files (perfect_reference.json and relaxed_octahedral.json) are present and consistent.
