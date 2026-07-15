# Group-theoretical classification and block diagonalization of excitonic states

## Problem background
Excitons—bound electron-hole pairs—govern the optical response of semiconductors and insulators. Their properties depend on the underlying crystal symmetries, but the group-theoretical classification of excitonic states has lagged behind that of single-particle bands. This task addresses a symmetry-based framework for excitons within an ab initio context. The goal is to classify excitonic states by irreducible representations, to block-diagonalize the Bethe-Salpeter equation (BSE) Hamiltonian using symmetry-adapted bases, and to derive optical selection rules for exciton-phonon interactions. The material studied is monolayer MoS₂, which has point group D₃h; spin-orbit coupling is included, requiring double-group representations for the one-electron states and single-group representations for the excitonic states. The challenge is to compute, from provided spinor wavefunctions and exciton expansion coefficients, the symmetry labels, the block structure of the BSE Hamiltonian at high-symmetry points, and the Kronecker product table that governs selection rules.

## Approach
Use group-theoretical methods to analyse the exciton eigenstates produced by a prior GW+BSE calculation on MoS₂. The starting point is a deposited dataset containing spinor wavefunctions, quasiparticle energies, and BSE exciton coefficients along the high-symmetry path Γ–M–K–Γ. The core steps are:

- Set up the space group P6̄m2 (point group D₃h) and obtain its irreducible representations and character tables using the SPGREP package.
- Compute the one-electron symmetry transformation matrices D_k for the valence and conduction bands at each k-point, as required for the subsequent exciton symmetry operations.
- For each exciton centre-of-mass momentum Q on the path, construct the representation matrices K_Q from the exciton coefficients and the one-electron D_k matrices, then decompose them into irreducible representations of the little group at Q, assigning a label to each of the first eight exciton states.
- At Q = Γ and Q = K, construct symmetry-adapted electron–hole product bases using projection operators; determine the number of independent basis vectors (block size) for each irreducible representation, thereby revealing the block-diagonal structure of the BSE Hamiltonian.
- For the D₃h group at Γ, compute the Kronecker product table between all pairs of irreducible representations and derive the phonon-mediated transition rules using the available phonon irreps (Γ₁, Γ₄, Γ₆, Γ₅).

The task does not require re-running the expensive DFT, GW, or BSE calculations; all necessary electronic-structure data are pre-computed and publicly available.

## Reproduction target
The objective is to produce three quantitative artifacts:

1. A CSV file (`exciton_irreps.csv`) that lists, for each high-symmetry point and for representative points along the symmetry lines Σ, T, Λ, the irreducible representation labels of the first eight excitonic states.
2. A JSON file (`block_diag_sizes.json`) that reports, for Q = Γ and Q = K, the size (number of basis vectors) of each symmetry-adapted block of the BSE Hamiltonian.
3. A JSON file (`selection_rules.json`) that contains the Kronecker product table for the D₃h group, showing for each initial exciton irrep and each phonon irrep which final exciton irreps are allowed by symmetry.

All outputs must be written under `/app/outputs`. The required inputs—spinor wavefunctions, GW energies, BSE exciton coefficients, and Q-point list—are publicly available from Figshare (doi:10.6084/m9.figshare.30025483.v1). The group-theoretical computations rely on the open-source SPGREP library.

## Assets

- MoS2 exciton symmetry dataset (Figshare): https://doi.org/10.6084/m9.figshare.30025483.v1
- SPGREP: https://github.com/atztogo/spgrep
- Python scientific computing stack: numpy scipy sympy

## Workflow steps

### Step 1: Load deposited dataset
- Role: process
- Action: Retrieve the deposited spinor wavefunctions, GW energies, BSE exciton coefficients, and the list of Q-points on the path Γ-M-K-Γ from the Figshare dataset. Parse into appropriate data structures (e.g., NumPy arrays).
- Evidence: none

### Step 2: Compute one-electron symmetry transformation matrices
- Role: process
- Action: Using SPGREP, set up the space group of monolayer MoS2 (point group D3h, space group P-6m2) and obtain the double-group irreducible representations. For each k-point in the basis, compute the transformation matrices D_{k} for the valence and conduction bands from the provided wavefunctions, as needed for exciton symmetry operators.
- Evidence: none

### Step 3: Symmetry classification of excitonic states
- Role: scored (load-bearing)
- Action: For each Q-point on the path (Γ, M, K, and points on the symmetry lines Σ, T, Λ), compute the representation matrices K_Q for the first eight exciton states using the exciton coefficients A^{S,Q} and the one-electron matrices D_k. Decompose into irreducible representations of the little group at that Q using SPGREP character tables, and assign an irrep label to each state. Write results as a CSV.
- Output file: `/app/outputs/exciton_irreps.csv`
- Format: csv
- Contract: Columns: symmetry_point (string), state_index (integer 1..8), irrep_label (string).
- Scoring: scored by hidden verifier

### Step 4: Determine symmetry-adapted block dimensions
- Role: scored
- Action: For Q=Γ and Q=K only, construct the symmetry-adapted electron-hole product basis for each irreducible representation using projection operators and the transformation matrices from the previous step. Count the number of linearly independent basis vectors (block size) for each irrep. Write a JSON object with keys 'Gamma' and 'K', each a dict mapping irrep label to block size.
- Output file: `/app/outputs/block_diag_sizes.json`
- Format: json
- Contract: Top-level keys: 'Gamma', 'K'. Each value is an object mapping irrep label (string) to block size (integer).
- Scoring: scored by hidden verifier

### Step 5: Exciton-phonon selection rules
- Role: scored
- Action: For the D3h group at Γ, compute the Kronecker product of each pair of irreducible representations (Γ1..Γ6). For each initial exciton irrep, list which final exciton irreps are allowed via each phonon irrep that appears at Γ (Γ1, Γ4, Γ6, Γ5). Write a nested JSON matching the selection rule table.
- Output file: `/app/outputs/selection_rules.json`
- Format: json
- Contract: JSON object where top-level keys are initial exciton irrep labels ('Γ1'...'Γ6'). For each initial irrep, the value is an object mapping phonon irrep (e.g., 'Γ1', 'Γ4', 'Γ6', 'Γ5') to a list of allowed final exciton irrep labels (strings).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exciton_irreps.csv`
- `/app/outputs/block_diag_sizes.json`
- `/app/outputs/selection_rules.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exciton_irreps.csv
- path: `/app/outputs/exciton_irreps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Irreducible representation labels for the first eight excitonic states at high-symmetry points and along symmetry lines.
- schema:
  - `type`: table
  - `required_columns`: `symmetry_point`, `state_index`, `irrep_label`
  - `units`: object

### block_diag_sizes.json
- path: `/app/outputs/block_diag_sizes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Block dimensions for the symmetry-adapted BSE Hamiltonian at Γ and K.
- schema:
  - `type`: object
  - `required`:
    - `Gamma`: object
    - `K`: object
  - `items`: object

### selection_rules.json
- path: `/app/outputs/selection_rules.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Kronecker product table for D3h exciton-phonon selection rules.
- schema:
  - `type`: object
  - `required`: object
  - `items`: object

Notes: The classification CSV must exactly match the pattern of irrep labels (order may vary within a symmetry point, but the set must match). Block sizes are compared within a tolerance of ±10%. Selection rules must exactly match the Kronecker product table.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exciton_irreps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "symmetry_point",
          "state_index",
          "irrep_label"
        ],
        "units": {}
      },
      "description": "Irreducible representation labels for the first eight excitonic states at high-symmetry points and along symmetry lines."
    },
    {
      "file": "block_diag_sizes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Gamma": "object",
          "K": "object"
        },
        "items": {}
      },
      "description": "Block dimensions for the symmetry-adapted BSE Hamiltonian at Γ and K."
    },
    {
      "file": "selection_rules.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {},
        "items": {}
      },
      "description": "Kronecker product table for D3h exciton-phonon selection rules."
    }
  ],
  "notes": "The classification CSV must exactly match the pattern of irrep labels (order may vary within a symmetry point, but the set must match). Block sizes are compared within a tolerance of ±10%. Selection rules must exactly match the Kronecker product table."
}
```

## How you are scored
A hidden verifier independently scores each of the three output files. For `exciton_irreps.csv`, the verifier compares the reported irrep labels against a gold standard; the set of labels at each symmetry point must match (order is not enforced). For `block_diag_sizes.json`, the block dimensions are compared to reference values within a tolerance that accounts for the finite basis-set size. For `selection_rules.json`, the Kronecker product table is checked for exact structural correctness. Each artifact contributes a fraction of the total reward, and the verifier computes the final reward as a weighted sum. Simply reporting the paper's numbers is not sufficient—the verifier expects the results to be generated by executing the described workflow.
