# Finite-Difference Calculation of Confined Surface-State Eigenvalues in an AQ Pore on Cu(111)

## Problem background
Nanoscale confinement of the Cu(111) Shockley surface-state electrons inside a molecular pore can create discrete, quantized electronic states whose spatial distribution governs adsorption of molecules at the surface. When the pore is formed by an anthraquinone (AQ) network exposing ~4 nm of substrate, the confined states become experimentally relevant for understanding and controlling molecular self-assembly. Because first-principles DFT is impractical on a pore that exposes 186 substrate atoms, a continuum effective-mass model with a finite-difference relaxation algorithm is used to obtain the confined eigenfunctions and eigenvalues. This task focuses on reproducing those eigenvalues — the three lowest-energy confined surface-state energies — from the known pore geometry and the published effective-mass Hamiltonian.

## Approach
You will implement an iterative finite‑difference relaxation algorithm on a two‑dimensional grid covering the pore interior. The approach rests on three pillars:

1. **Effective‑mass model**: The surface‑state electrons behave as free particles with effective mass m* = 0.34 mₑ inside the pore. The potential is taken as constant (zero) within the pore boundary and infinite outside.

2. **Pore boundary from AQ coordinates**: The pore boundary is defined by the 102 carbon and oxygen atoms of the anthraquinone network that are closest to the pore centre. You will extract these positions from the published network structure (Pawin et al., Science 2006). The resulting 2D boundary encloses a region of ≈4 nm across.

3. **Iterative relaxation + Gram‑Schmidt orthogonalisation**: Starting with approximate eigenfunctions of a triangular particle‑in‑a‑box, you iteratively update each eigenfunction on the grid using the finite‑difference relation
```
⟨x,y|φ_n⟩ = (⟨x+δ,y| + ⟨x-δ,y| + ⟨x,y+δ| + ⟨x,y-δ|φ_{n-1}⟩) / (4 - 2 m* δ² E_{n-1} / ħ²)
```
where δ is the grid spacing. After each iteration you enforce orthogonality among the set of trial eigenfunctions via Gram‑Schmidt. Convergence is declared when the changes in the wavefunctions or eigenvalues fall below a chosen threshold. The eigenvalues E are reported relative to the bottom of the Cu(111) surface‑state band, which lies 450 meV below the Fermi energy. You may run the calculation on any reasonable grid spacing (e.g., 1.25 Å, 0.63 Å, or 0.41 Å), and the resulting eigenvalues should be insensitive to the grid choice.

## Reproduction target
Using the pore boundary derived from the anthraquinone network coordinates, implement the continuum finite‑difference relaxation algorithm described above. Compute the **three lowest confined surface‑state eigenvalues** (E1, E2, E3) in meV measured from the bottom of the surface‑state band (450 meV below EF). One state is non‑degenerate and the other two form a twofold‑degenerate pair. Report these values, together with the grid spacing you used, in `/app/outputs/eigenvalues.json`. Additionally, during the relaxation, record per‑iteration convergence metrics (e.g., maximum absolute change in the eigenfunction or in the eigenvalue) to `/app/outputs/convergence_log.txt`. The log must demonstrate that the algorithm was executed and converged.

## Assets

- AQ network structure on Cu(111) (atomic coordinates): 10.1126/science.1130240
- NumPy: numpy

## Workflow steps

### Step 1: Construct pore boundary from AQ network coordinates
- Role: process
- Action: From the published AQ/Cu(111) network atomic coordinates, identify the 102 carbon and oxygen atoms that are closest to the pore centre and define the potential‑free interior region. Prepare a file with the coordinates of these boundary atoms for use in the continuum model.
- Evidence: `/app/outputs/pore_boundary.json`

### Step 2: Compute confined eigenfunctions and eigenvalues
- Role: scored (load-bearing)
- Action: Implement the iterative finite‑difference relaxation algorithm inside the pore boundary from step_01, using effective mass m* = 0.34 mₑ and a finite grid spacing. Start from approximate triangular‑particle‑in‑a‑box eigenfunctions, iterate the relaxation update equation (sum of neighbour values divided by the energy‑dependent denominator), and enforce orthogonality via Gram‑Schmidt after each iteration until convergence. Write the three lowest eigenvalues (one non‑degenerate and one degenerate pair, in meV) and the grid spacing used to eigenvalues.json.
- Output file: `/app/outputs/eigenvalues.json`
- Format: json
- Contract: {"E1": number, "E2": number, "E3": number, "grid_spacing_A": number}
- Scoring: scored by hidden verifier

### Step 3: Convergence evidence log
- Role: scored
- Action: During the relaxation, record per‑iteration convergence metrics (e.g., maximum absolute change in eigenfunction or eigenvalue) to a log file. Write the iteration numbers and convergence deltas to convergence_log.txt.
- Output file: `/app/outputs/convergence_log.txt`
- Format: txt
- Contract: Lines containing iteration count and delta_E (or equivalent convergence measure).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eigenvalues.json`
- `/app/outputs/convergence_log.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eigenvalues.json
- path: `/app/outputs/eigenvalues.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Eigenvalues of the three lowest confined surface states (one non‑degenerate, one twofold degenerate) in meV, measured from the bottom of the surface‑state band, and the grid spacing in Angstrom used for the calculation.
- schema:
  - `type`: object
  - `required`:
    - `E1`: number
    - `E2`: number
    - `E3`: number
    - `grid_spacing_A`: number

### convergence_log.txt
- path: `/app/outputs/convergence_log.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Convergence log demonstrating that the iterative relaxation algorithm was executed and converged.
- schema:
  - `type`: text

Notes: The eigenvalues must be computed from the pore boundary derived from the anthraquinone network atomic coordinates. The agent must implement the finite‑difference relaxation algorithm; no pre‑computed values are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eigenvalues.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E1": "number",
          "E2": "number",
          "E3": "number",
          "grid_spacing_A": "number"
        }
      },
      "description": "Eigenvalues of the three lowest confined surface states (one non‑degenerate, one twofold degenerate) in meV, measured from the bottom of the surface‑state band, and the grid spacing in Angstrom used for the calculation."
    },
    {
      "file": "convergence_log.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Convergence log demonstrating that the iterative relaxation algorithm was executed and converged."
    }
  ],
  "notes": "The eigenvalues must be computed from the pore boundary derived from the anthraquinone network atomic coordinates. The agent must implement the finite‑difference relaxation algorithm; no pre‑computed values are provided."
}
```

## How you are scored
A hidden verifier will independently inspect each of the required output files:

- **eigenvalues.json**: The verifier compares your reported E1, E2, and E3 to hidden reference eigenvalues that correspond to a correct implementation of the relaxation algorithm for the AQ pore. The comparison accounts for expected numerical variations between different implementations. A correct numerical solution will yield full credit for this artifact, which carries the majority of the reward.

- **convergence_log.txt**: The verifier checks that the log contains evidence of the iterative relaxation process (iteration numbers, convergence deltas, or similar metrics) and that the algorithm converged. Structural completeness of the log contributes a small additional fraction of the reward.

The final reward is a single number in [0,1] that is a weighted combination of the scores from the two artifacts. Simply reporting the paper's values without actually executing the algorithm will not satisfy the convergence artifact and will be severely penalised.
