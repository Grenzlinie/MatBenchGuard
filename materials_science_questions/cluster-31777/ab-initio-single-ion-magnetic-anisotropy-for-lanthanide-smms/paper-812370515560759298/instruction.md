# Ising-like Exchange Barrier for Heteronuclear Dimer

## Problem background
Single-molecule magnets (SMMs) require a spin-reorientation barrier between the two opposite magnetization states to exhibit magnetic bistability. The blocking temperature — the maximum temperature at which the magnetization is retained — is determined by the size of this barrier. A central challenge in molecular magnetism is to design clusters with significantly larger barriers than those found in conventional SMMs, where the anisotropy originates primarily from single-ion zero-field splitting. An alternative strategy is to use orbitally degenerate metal ions that give rise to strongly anisotropic exchange interactions. This task explores the spin spectrum and spin-reorientation barrier of a conceptual heteronuclear dimer in which an orbitally degenerate centre (effective spin S1 = 1/2) is coupled to a spin-only ion (S2 = 5/2) by an Ising-like exchange Hamiltonian. The aim is to compute, for a given antiferromagnetic coupling constant, the energy levels and the resulting barrier, thereby testing whether such a dimer can support a large barrier governed by the exchange interaction alone.

## Approach
The dimer is described by the Ising-like exchange Hamiltonian H = -J S1^z S2^z, where J is the exchange coupling constant and S1^z, S2^z are the z-components of the effective spins S1 = 1/2 and S2 = 5/2. The coupling is antiferromagnetic (J < 0). Because the Hamiltonian involves only Sz operators, the product basis states |m⟩|M_S⟩ — with m ∈ {+1/2, -1/2} and M_S ∈ {+5/2, +3/2, +1/2, -1/2, -3/2, -5/2} — are exact eigenstates with energies -J · m · M_S. The computation consists of enumerating all 12 basis states, collecting the distinct energy values (each appears twice, corresponding to doubly degenerate Kramers doublets), and sorting the six distinct energies in ascending order. The ground doublet is the lowest energy, and the first excited doublet is the next highest. The spin-reorientation barrier ΔE is defined as the difference between these two levels, ΔE = E_first − E_ground. No further parameters, external datasets, or complex numerical methods are needed; the problem is fully specified by the spin values and the given J, and can be solved by a short program using only basic arithmetic.

## Reproduction target
For a single, specified antiferromagnetic exchange coupling constant J (J < 0), produce the energy spectrum and the spin-reorientation barrier of the S1 = 1/2, S2 = 5/2 Ising-like dimer. Specifically:
- Compute the six distinct doubly degenerate energy eigenvalues.
- Sort them in ascending order.
- Determine the ground doublet (lowest energy) and the first excited doublet (second lowest).
- Calculate the barrier ΔE = E_first − E_ground.
Write the results to a file named `energies_and_barrier.json` inside the directory `/app/outputs`. The file must contain exactly the following keys: `J` (the input coupling constant, in cm⁻¹), `energies` (a list of six numbers representing the sorted distinct energies, in cm⁻¹), and `barrier` (a single number for ΔE, in cm⁻¹). The correctness of your submission will be assessed by comparing these values against the exact analytic results for the same Hamiltonian and J.

## Assets

- Python 3 Standard Library: python3

## Workflow steps

### Step 1: Compute dimer energy levels and barrier
- Role: scored (load-bearing)
- Action: Construct the Ising-like exchange Hamiltonian H = -J S1^z S2^z for effective spins S1=1/2 and S2=5/2. Enumerate all product basis states |m>|M_S> with m in {+1/2, -1/2} and M_S in {+5/2, +3/2, +1/2, -1/2, -3/2, -5/2}. Compute the energy for each product state as -J * m * M_S. Collect the distinct energy values (each doubly degenerate because flipping both spins yields the same product). Sort the six distinct energies in ascending order. Identify the ground doublet (lowest energy) and the first excited doublet (second lowest). Compute the spin-reorientation barrier ΔE = E_first - E_ground. Output the results to energies_and_barrier.json.
- Output file: `/app/outputs/energies_and_barrier.json`
- Format: json
- Contract: {"J": "float (cm⁻¹)", "energies": "array of 6 floats (cm⁻¹) sorted ascending", "barrier": "float (cm⁻¹)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies_and_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies_and_barrier.json
- path: `/app/outputs/energies_and_barrier.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Artifact containing the input J, the six distinct doubly-degenerate energy eigenvalues in ascending order, and the spin-reorientation barrier ΔE = E_first - E_ground. The checker validates that J matches the hidden test J, that the energies correspond exactly (within tolerance) to the analytic values -5|J|/4, -3|J|/4, -|J|/4, |J|/4, 3|J|/4, 5|J|/4, and that the barrier equals |J|/2.
- schema:
  - `type`: object
  - `required`:
    - `J`: number (cm⁻¹)
    - `energies`: array of 6 numbers (cm⁻¹) sorted ascending
    - `barrier`: number (cm⁻¹)

Notes: The hidden test J is an arbitrary antiferromagnetic coupling (J < 0) provided in the instruction. The agent must use that exact value. The analytic energy spectrum and barrier are derived from that J; the checker computes the expected values from the hidden J and compares with absolute tolerance 1e-6 cm⁻¹. The task does not require any external datasets or packages beyond Python stdlib.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies_and_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "J": "number (cm⁻¹)",
          "energies": "array of 6 numbers (cm⁻¹) sorted ascending",
          "barrier": "number (cm⁻¹)"
        }
      },
      "description": "Artifact containing the input J, the six distinct doubly-degenerate energy eigenvalues in ascending order, and the spin-reorientation barrier ΔE = E_first - E_ground. The checker validates that J matches the hidden test J, that the energies correspond exactly (within tolerance) to the analytic values -5|J|/4, -3|J|/4, -|J|/4, |J|/4, 3|J|/4, 5|J|/4, and that the barrier equals |J|/2."
    }
  ],
  "notes": "The hidden test J is an arbitrary antiferromagnetic coupling (J < 0) provided in the instruction. The agent must use that exact value. The analytic energy spectrum and barrier are derived from that J; the checker computes the expected values from the hidden J and compares with absolute tolerance 1e-6 cm⁻¹. The task does not require any external datasets or packages beyond Python stdlib."
}
```

## How you are scored
A hidden verifier will inspect your `/app/outputs/energies_and_barrier.json` file. It first checks that the `J` value you recorded matches the coupling constant provided in this task. It then compares your `energies` array and `barrier` value against the expected exact eigenvalues and barrier derived from that J. Both the list of six distinct energies and the barrier value are evaluated; the final score reflects how accurately you reproduce the energy spectrum and the spin-reorientation gap. The verifier uses a strict numerical tolerance, so precise computation is required. No manual interpretation or qualitative assessment is involved — the score is based solely on the numeric agreement with the reference results.
