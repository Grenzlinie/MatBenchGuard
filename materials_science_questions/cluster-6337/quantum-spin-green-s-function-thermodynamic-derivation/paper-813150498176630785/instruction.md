# Antiferromagnetic Ground-State Energy via Cumulant Expansion

## Problem background
In the study of quantum magnetism, calculating the ground-state energy of antiferromagnetic spin systems is challenging because spin operators obey neither fermionic nor bosonic commutation relations. Standard perturbative methods that work for electrons or phonons cannot be directly applied. This work develops a Wick‑like theorem for spin operators of arbitrary magnitude and combines it with Kubo’s cumulant expansion to obtain a compact, diagrammatic prescription for the ground‑state energy of a spin Hamiltonian. The method is applied to a two‑sublattice antiferromagnet with anisotropic exchange interaction. The energy is expressed as a perturbation series in the anisotropy parameter, with coefficients that depend on the lattice geometry and the spin magnitude. The task is to implement the derived formulas and evaluate them numerically for several common lattice types and spin values, thereby obtaining the second‑ and fourth‑order expansion coefficients as well as the isotropic ground‑state energy.

## Approach
Start from the anisotropic exchange Hamiltonian on a bipartite lattice composed of two sublattices A and B. In the alternating coordinate system, the unperturbed Hamiltonian H₀ consists only of the Ising term −2J Σ S_A^z S_B^z, and the perturbation H_I contains spin‑flip terms (1−γ)J Σ (S_A^+ S_B^+ + S_A^− S_B^−). The unperturbed ground state |0⟩ is the fully aligned antiferromagnetic configuration.

By introducing the interaction‑picture spin operators and applying the cumulant expansion theorem of Kubo, the energy shift ΔE of the ground state can be written as a sum over cumulants of time‑ordered products. A Wick theorem for spin operators is used to decompose each time‑ordered product into a sum of contractions (quasi‑c‑number propagators), giving rise to diagrams. Rules are derived to associate a numerical factor with each diagram, taking into account the spin magnitude, the number of overlapping spin deviations on the same site, and the intermediate‑state energies.

For the antiferromagnet, the ground‑state energy up to fourth order takes the form
  E = −J z N ħ² (2 j_A j_B) [1 + c₁ (1−γ)² + c₂ (1−γ)⁴ + …] ,
where z is the coordination number, N is the number of atoms per sublattice, and c₁, c₂ are dimensionless coefficients. The coefficients are expressed via closed‑form formulas in terms of ε₀ = 2 z (j_A + j_B), the spin magnitudes j_A = j_B = j, and a lattice‑specific geometric factor Q that counts certain closed four‑atom chains. The intermediate quantities d₁…d₆ are simple rational functions of j and ε₀.

For the special case γ = 0 (isotropic Heisenberg interaction) and spin‑½, the ground‑state energy per bond in units of −J z N ħ² / 2 is simply 4 j² (1 + c₁ + c₂).

The computational workflow is: for each lattice type, determine z and Q; compute ε₀; evaluate d₁…d₆, c₁, c₂; and for j = ½ also compute the energy. The results for all lattices and spin magnitudes are written to a structured JSON file.

## Reproduction target
Compute the perturbation coefficients c₁ and c₂ for the following one‑dimensional, two‑dimensional, and three‑dimensional bipartite lattices:
- chain (z = 2)
- square plane (z = 4)
- simple cubic (z = 6)
- body‑centered cubic (z = 8)

For each lattice, evaluate c₁ and c₂ for spin magnitudes j = ½, 1, ³⁄₂, 2, ⁵⁄₂ (with j_A = j_B = j). In addition, for j = ½ compute the isotropic ground‑state energy per bond in units of −J z N ħ² / 2 (i.e., for γ = 0).

Output the results as a single JSON file `/app/outputs/results.json` with the structure specified in the Output contract.

## Assets

- Python 3 with NumPy: python3, numpy

## Workflow steps

### Step 1: Compute perturbation coefficients and ground-state energy
- Role: scored (load-bearing)
- Action: For each lattice and spin magnitude j in {0.5, 1.0, 1.5, 2.0, 2.5}, use the lattice parameters (coordination number z and geometric factor Q) to evaluate the following closed-form expressions (j_A = j_B = j).
  1. Compute ε₀ = 2 z (j + j) = 4 z j.
  2. Compute the intermediate quantities:
     d₁ = (4 j²) / ((ε₀ − 2)² (ε₀ − 3)),
     d₂ = d₂′ = (4 j²) / ((ε₀ − 2)² (ε₀ − 4)),
     d₃ = 2 (2j − 1)(2j) / ((ε₀ − 2)² (ε₀ − 4)),
     d₄ = 2 (2j − 1)(2j) / ((ε₀ − 2)² (ε₀ − 4)),
     d₅ = 4 (2j − 1)² / ((ε₀ − 2)² (ε₀ − 4)),
     d₆ = (4 j²) / (ε₀ − 2)³.
  3. Compute the perturbation coefficients:
     c₁ = 2 / (ε₀ − 2),
     c₂ = 4 ((z − 1)² − Q) (d₁ − d₆) + 2 Q (d₂ − d₀ + d₂′) + 2 (z − 1) (d₃ + d₄ − 2 d₆) + (d₅ − 2 d₆),
     where d₀ = d₂.
  4. For the isotropic case γ = 0 and j = 0.5, compute the ground-state energy per bond:
     E = 4 j² (1 + c₁ + c₂)  (in units of −J z N ħ² / 2).
  The geometric factor Q is the number of closed four-atom chains A₁ B₁ A₂ B₂ (all four atoms distinct) in which each atom is a nearest neighbour of two others. The values for the four lattices are:
    - chain:            Q = 0
    - square plane:     Q = 2
    - simple cubic:     Q = 4
    - body-centred cubic: Q = 6
  Output all results as a structured JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with top-level keys 'chain', 'plane', 'sc', 'bcc'. Each value is an object with keys '0.5','1.0','1.5','2.0','2.5'. Each entry is an object: 'c1' (float), 'c2' (float). For j=0.5 only, additionally 'E_gamma0' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Perturbation coefficients c1, c2 for each lattice and spin magnitude, and ground-state energy for isotropic spin-1/2 case.
- schema:
  - `type`: object
  - `required`:
    - `chain`: object
    - `plane`: object
    - `sc`: object
    - `bcc`: object
  - `items`:
    - `0.5`: object
    - `1.0`: object
    - `1.5`: object
    - `2.0`: object
    - `2.5`: object
  - `required_columns`:
  - `units`:
    - `c1`: dimensionless
    - `c2`: dimensionless
    - `E_gamma0`: units of -J z N ħ^2/2

Notes: The scoring compares the reported values to the paper's published results using absolute tolerances: 1e-4 for c1, 1e-3 for c2, and 1e-2 for E_gamma0 (tolerances are hidden). Omission of any required field or incorrect format results in zero reward for that entry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "chain": "object",
          "plane": "object",
          "sc": "object",
          "bcc": "object"
        },
        "items": {
          "0.5": "object",
          "1.0": "object",
          "1.5": "object",
          "2.0": "object",
          "2.5": "object"
        },
        "required_columns": [],
        "units": {
          "c1": "dimensionless",
          "c2": "dimensionless",
          "E_gamma0": "units of -J z N ħ^2/2"
        }
      },
      "description": "Perturbation coefficients c1, c2 for each lattice and spin magnitude, and ground-state energy for isotropic spin-1/2 case."
    }
  ],
  "notes": "The scoring compares the reported values to the paper's published results using absolute tolerances: 1e-4 for c1, 1e-3 for c2, and 1e-2 for E_gamma0 (tolerances are hidden). Omission of any required field or incorrect format results in zero reward for that entry."
}
```

## How you are scored
A hidden verifier will load your `results.json` and compare every numeric field against the correct reference values (the published results) using absolute tolerances. For each lattice and spin magnitude, the c₁ and c₂ entries are checked; for j = ½ the energy entry is also checked. If the absolute difference from the reference is within a hidden tolerance, that entry scores 1; otherwise it scores 0. The final reward is the fraction of entries that pass (all entries weighted equally). Tolerances are set to accommodate small floating‑point differences that arise from innocent numerical choices, while being tight enough that a random guess or a drastically wrong computation will not pass. Reporting plausible numbers that are not the result of a genuine computation of the required formulas will therefore yield a low score.
