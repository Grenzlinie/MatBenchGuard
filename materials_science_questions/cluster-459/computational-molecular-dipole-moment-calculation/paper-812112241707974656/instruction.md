# Semi-empirical ASMO SCF Treatment of Peptide Molecule σ-π System

## Problem background
The electronic structure of the peptide unit is central to understanding charge transfer and semiconductivity in proteins. A fully quantitative treatment must account for both σ and π electrons, because the π-electron distribution, dipole moment, and optical excitations are strongly influenced by the σ framework. Semi-empirical self-consistent field (SCF) methods provide a practical route to obtain reliable excitation energies, oscillator strengths, ionization potentials, and dipole moments that can be compared with experimental data to validate the quality of the approximations.

## Approach
We compute the electronic structure of a model peptide (formamide, HCONH₂) by the semi-empirical ASMO SCF method with explicit σ and π electrons. The molecular orbital basis consists of 10 atomic orbitals: four π-type (2pπ on O, C, N, and H) and six σ-type (H 1s, two sp² hybrids on N, two sp² hybrids on C, and O 2pσ).

One-electron core integrals are built from atomic ionization potentials using the W₂ₚ approximation and off-diagonal terms proportional to overlap integrals with a constant factor. Two-electron repulsion integrals are treated with the Pariser–Parr approximation for one-center Coulomb integrals and the Mataga–Nishimoto formula for two-center terms. Overlap integrals and effective nuclear charges for the hydrogen 2pπ orbital (three values: 0.15, 0.3625, 0.575) follow published tables; the main scored calculation uses Z* = 0.3625.

The Roothaan SCF equations are solved iteratively (initial neglect of overlap, convergence to 10⁻³ eV) for the 10-electron, 10-orbital σ-π system. From the converged wavefunction we compute:
- total dipole moment (Debye) including π and σ contributions,
- the two lowest π→π* excitation energies and oscillator strengths via a singles configuration interaction (singly excited configurations built from the occupied and vacant π orbitals),
- ionization potential via Koopmans’ theorem.

All results are written to a JSON file for the σ-π system with the hydrogen 2pπ effective nuclear charge Z* = 0.3625.

## Reproduction target
Produce a JSON file at /app/outputs/results.json containing the following six numeric quantities for the σ-π system of the peptide model with hydrogen 2pπ effective nuclear charge Z* = 0.3625:
- dipole_moment_D: total electric dipole moment in Debye,
- excitation_NV1_eV: energy of the lowest π→π* excitation (N–V₁) in eV,
- oscillator_NV1: oscillator strength of the N–V₁ transition,
- excitation_NV2_eV: energy of the second π→π* excitation (N–V₂) in eV,
- oscillator_NV2: oscillator strength of the N–V₂ transition,
- ionization_potential_eV: ionization potential from the highest occupied molecular orbital (Koopmans’ theorem) in eV.

All values must be obtained from a self-consistent ASMO SCF calculation that follows the described integral approximations and uses the prescribed basis set and Z* value.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define molecular geometry and basis set
- Role: process
- Action: Define the model peptide geometry (bond lengths, angles) and the 10-atomic-orbital basis (4 π‑type: O 2pπ, C 2pπ, N 2pπ, H 2pπ; 6 σ‑type: H 1s, two N sp² hybrids, two C sp² hybrids, O 2pσ) with orbital numbering consistent with the paper, to be used in all subsequent integrals.
- Evidence: none

### Step 2: Compute all required integrals
- Role: process
- Action: Compute one‑electron core integrals (using ionization potentials, W2p approximation, Slater orbital overlaps, off‑diagonal core integrals I_rs = l * S_rs with l = –12.65 eV, and hybrid sp² matrix elements via the given formula), two‑electron repulsion integrals (one‑center via Pariser–Parr, two‑center via Mataga–Nishimoto), and overlap integrals for the σ-π system with hydrogen 2pπ effective nuclear charge Z* = 0.3625.
- Evidence: none

### Step 3: SCF iteration for σ-π system
- Role: process
- Action: Solve the Roothaan SCF equations iteratively for the σ-π system (10 electrons, 10 MOs) with Z* = 0.3625. Start from an initial guess for MO coefficients, neglect overlap initially, construct the Fock matrix using the density matrix, diagonalize to obtain new eigenvalues and eigenvectors, and repeat until all orbital energies converge to within 10⁻³ eV. Obtain converged MO coefficients, orbital energies, and one‑electron density matrix.
- Evidence: none

### Step 4: Compute observables and write results
- Role: scored (load-bearing)
- Action: From the converged SCF wavefunction, compute (i) the total dipole moment (Debye) including both π and σ contributions, (ii) the two lowest π→π* excitation energies (eV) and oscillator strengths via a singles CI, and (iii) the ionization potential (eV) from Koopmans’ theorem. Write all values to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"dipole_moment_D": "float", "excitation_NV1_eV": "float", "oscillator_NV1": "float", "excitation_NV2_eV": "float", "oscillator_NV2": "float", "ionization_potential_eV": "float"}
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
- target_policy: reference_match
- description: JSON file with the computed σ-π system dipole moment (Debye), N-V₁ and N-V₂ excitation energies (eV) and oscillator strengths, and ionization potential (eV) for the peptide model with hydrogen 2pπ Z* = 0.3625.
- schema:
  - `type`: object
  - `required`:
    - `dipole_moment_D`: float
    - `excitation_NV1_eV`: float
    - `oscillator_NV1`: float
    - `excitation_NV2_eV`: float
    - `oscillator_NV2`: float
    - `ionization_potential_eV`: float

Notes: The CI procedure is assumed to be a singles (singly‑excited) CI built from the π orbitals. Only the σ-π system at Z*=0.3625 is scored; the π-only system and other Z* values are omitted.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "dipole_moment_D": "float",
          "excitation_NV1_eV": "float",
          "oscillator_NV1": "float",
          "excitation_NV2_eV": "float",
          "oscillator_NV2": "float",
          "ionization_potential_eV": "float"
        }
      },
      "description": "JSON file with the computed σ-π system dipole moment (Debye), N-V₁ and N-V₂ excitation energies (eV) and oscillator strengths, and ionization potential (eV) for the peptide model with hydrogen 2pπ Z* = 0.3625."
    }
  ],
  "notes": "The CI procedure is assumed to be a singles (singly‑excited) CI built from the π orbitals. Only the σ-π system at Z*=0.3625 is scored; the π-only system and other Z* values are omitted."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json and compares each of the six fields to independently determined reference values for the same system and conditions. Each field that falls within a predefined tolerance around the reference counts as correct. The total reward is the proportion of the six fields that meet the tolerance (a number between 0 and 1). The verifier does not inspect your source code or intermediate files; only the final JSON file is scored.
