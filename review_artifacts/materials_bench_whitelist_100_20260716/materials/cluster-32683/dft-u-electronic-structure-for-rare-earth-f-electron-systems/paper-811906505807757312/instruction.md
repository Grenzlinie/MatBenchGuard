# DFT+U calculation of density of states and f-occupation for a rare-earth Laves phase compound

## Problem background
Rare-earth intermetallic compounds containing cerium, such as the cubic Laves phase CeOs2, can exhibit heavy-fermion behaviour and superconductivity. Understanding their electronic structure—particularly the density of states (DOS) near the Fermi level and the occupation of the strongly correlated 4f states—is key to explaining these properties. This task reproduces a first-principles determination of the electronic DOS and the total Ce 4f electron count within a density-functional theory approach that includes on-site Coulomb correlations.

## Approach
The calculation uses the local spin-density approximation plus a Hubbard U (LSDA+U) applied to the Ce 4f orbitals. A spin-unpolarized, self-consistent Kohn-Sham band-structure calculation is performed for CeOs2 in its non-magnetic state, employing plane-wave pseudopotentials (with Ce 4f states in the valence) and the known crystal structure (MgCu2-type, space group Fd-3m, lattice constant 7.59 Å). From the converged results the total DOS per spin is computed via the tetrahedron method on a fine k-point mesh, and the self-consistent charge density is analysed to extract the total Ce 4f occupation. The workflow consists of a single self-consistent field (SCF) run followed by two post-processing steps.

## Reproduction target
Produce two artifacts: (i) `dos.txt` — a two-column file (energy in Ryd relative to the Fermi level, total DOS per spin in states/(Ryd·spin)) that covers at least the energy interval from -0.5 to 0.5 Ryd, and (ii) `f_occupation.txt` — a single floating-point number giving the total Ce 4f electron count (summed over both spin channels). The hidden verifier will inspect the DOS for characteristic features relative to the Fermi level and verify that the f-occupation lies within a physically plausible range.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ce pseudopotential with 4f valence: https://www.materialscloud.org/discover/sssp/table/efficiency
- Os pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of CeOs2 (MgCu2-type, space group Fd-3m, a=7.59 Å)

## Workflow steps

### Step 1: Self-consistent LSDA+U calculation
- Role: process
- Action: Perform a spin-unpolarized self-consistent LSDA+U calculation for cubic CeOs2 (lattice constant 7.59 Å, space group Fd-3m) using Quantum ESPRESSO. Use Hubbard U=0.55 Ryd on Ce 4f states and appropriate pseudopotentials with Ce 4f in valence.
- Evidence: `/app/outputs/scf.log`

### Step 2: Compute density of states
- Role: scored (load-bearing)
- Action: From the converged Kohn-Sham energies, compute the total electronic density of states (DOS) per spin using the tetrahedron method on a fine k‑point mesh. Output a two‑column file: energy in Ryd (shifted so EF=0) and DOS in states/(Ryd·spin).
- Output file: `/app/outputs/dos.txt`
- Format: txt
- Contract: Two‑column ASCII text: column 1 energy (Ryd) relative to EF, column 2 total DOS per spin (states/(Ryd·spin)).
- Scoring: scored by hidden verifier

### Step 3: Extract Ce 4f occupation
- Role: scored (load-bearing)
- Action: From the self‑consistent charge, extract the total 4f occupation on Ce (sum over both spin channels) and write it as a single floating‑point number.
- Output file: `/app/outputs/f_occupation.txt`
- Format: txt
- Contract: Single ASCII floating‑point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos.txt`
- `/app/outputs/f_occupation.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos.txt
- path: `/app/outputs/dos.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total density of states per spin direction for CeOs2. The checker verifies the presence of a pseudogap at EF and two 4f‑derived peaks.
- schema:
  - `type`: text
  - `required_columns`: `energy(Ryd)`, `DOS(states/(Ryd·spin))`
  - `units`:
    - `energy`: Ryd
    - `DOS`: states/(Ryd·spin)

### f_occupation.txt
- path: `/app/outputs/f_occupation.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total Ce 4f electron count (both spins). The checker verifies that the value falls within a physically plausible range.
- schema:
  - `type`: other
  - `description`: Single float representing the total 4f occupation on Ce.

Notes: The LSDA+U calculation must use U=0.55 Ryd on Ce 4f. The DOS must be computed with the tetrahedron method on a fine k‑mesh. All energies are in Ryd.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required_columns": [
          "energy(Ryd)",
          "DOS(states/(Ryd·spin))"
        ],
        "units": {
          "energy": "Ryd",
          "DOS": "states/(Ryd·spin)"
        }
      },
      "description": "Total density of states per spin direction for CeOs2. The checker verifies the presence of a pseudogap at EF and two 4f‑derived peaks."
    },
    {
      "file": "f_occupation.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "description": "Single float representing the total 4f occupation on Ce."
      },
      "description": "Total Ce 4f electron count (both spins). The checker verifies that the value falls within a physically plausible range."
    }
  ],
  "notes": "The LSDA+U calculation must use U=0.55 Ryd on Ce 4f. The DOS must be computed with the tetrahedron method on a fine k‑mesh. All energies are in Ryd."
}
```

## How you are scored
After your run finishes, a hidden verifier reads `dos.txt` and `f_occupation.txt`. It checks that `dos.txt` contains the required two-column ascii data and then scores the DOS based on the presence of specific structural features (local minima and maxima relative to the Fermi energy). Separately, it reads `f_occupation.txt` and verifies that the number falls within a predefined admissible interval. The two scores are combined into a final reward between 0 and 1. Simply reporting a number is not enough; the verifier audits the file content, not the value alone. No gold values or tolerances are revealed to you.
