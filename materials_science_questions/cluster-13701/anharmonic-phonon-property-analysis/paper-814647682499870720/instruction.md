# CrSiTe3 Phonon Frequencies via DFT and Lattice Dynamics

## Problem background
CrSiTe₃ is a layered chalcogenide semiconductor that exhibits ferromagnetic order below 33 K. Strong spin–lattice coupling in the paramagnetic phase gives rise to glassy thermal conductivity and negative thermal expansion, and the phonon modes are sensitive to the magnetic transition. Understanding these effects requires a detailed characterization of the lattice dynamics, particularly the infrared-active vibrations at the Brillouin zone center. First-principles calculations can predict the frequencies and symmetry assignments of these modes. This task asks you to compute the Γ-point phonon frequencies of the three infrared-active modes of CrSiTe₃ using density functional theory and lattice dynamics, providing a direct test of the computational methodology used to explain spin–phonon interactions.

## Approach
Use density functional theory (DFT) within the local density approximation plus a Hubbard U correction (LDA+U, with U‑J = 3.5 eV on Cr d orbitals) to perform a self-consistent field (SCF) calculation for bulk CrSiTe₃. From the SCF solution, compute the interatomic force constants using either a finite-displacement or density-functional perturbation theory (DFPT) approach. Based on the force constants, calculate the phonon dispersion and extract the zone-center (Γ-point) phonon frequencies. Perform a symmetry analysis to determine the irreducible representations of the Γ-point modes and identify the three infrared-active modes: A_u, ¹E_u, and ²E_u. The frequencies of these three modes are the reproduction target. The approach mirrors the paper’s methodology, but any plane-wave code supporting LDA+U and a compatible phonon post-processing tool (e.g., Quantum ESPRESSO with Phonopy) can be used.

## Reproduction target
Using the crystal structure of CrSiTe₃ at 293 K: space group R‑3 (No. 148), hexagonal setting, a = 6.83 Å, c = 20.87 Å; atomic positions: Cr on 6c at (2/3, 1/3, 0.0009); Si on 6c at (0, 0, 0.0545); Te on 18f at (0.9975, 0.6430, 0.0834). Perform a DFT+LDA+U (U‑J = 3.5 eV on Cr d) phonon calculation and a symmetry analysis to obtain the Γ‑point phonon frequencies of the three infrared‑active modes. Write the frequencies to a JSON file as follows:
- /app/outputs/ir_phonon_frequencies.json  
  Keys: 'A_u', '1E_u', '2E_u' – each a float representing the frequency in cm⁻¹.
The computed frequencies constitute the sole scored artifact; their agreement with the paper’s calculated values will be assessed by a hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT calculation for CrSiTe3
- Role: process
- Action: Set up and run a DFT self-consistent field (SCF) calculation and a phonon force-constant calculation (finite‑displacement or DFPT) for bulk CrSiTe3 using the crystal structure: space group R‑3, lattice parameters a=6.83 Å, c=20.87 Å at 293 K, and atomic positions: Cr on 6c (2/3, 1/3, 0.0009), Si on 6c (0, 0, 0.0545), Te on 18f (0.9975, 0.6430, 0.0834). Use the LDA+U method with U‑J=3.5 eV on Cr d orbitals. Choose a k‑mesh and energy cutoff adequate for convergence. Generate force constants and the necessary inputs for Phonopy.
- Evidence: none

### Step 2: Compute and extract IR-active phonon frequencies
- Role: scored (load-bearing)
- Action: Using the force constants from step 1, run Phonopy to compute the phonon dispersion and extract the Γ‑point phonon frequencies. Perform a symmetry analysis to identify the three infrared‑active modes with A_u, ^1E_u, and ^2E_u symmetries. Report their frequencies in cm⁻¹.
- Output file: `/app/outputs/ir_phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys 'A_u', '1E_u', '2E_u', each a float number representing the frequency in cm⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ir_phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ir_phonon_frequencies.json
- path: `/app/outputs/ir_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed Γ‑point frequencies of the three infrared‑active phonon modes of CrSiTe3.
- schema:
  - `type`: object
  - `required`:
    - `A_u`: float (cm⁻¹)
    - `1E_u`: float (cm⁻¹)
    - `2E_u`: float (cm⁻¹)

Notes: The checker compares the submitted frequencies to reference values with a tolerance. The exact tolerance is hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ir_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "A_u": "float (cm⁻¹)",
          "1E_u": "float (cm⁻¹)",
          "2E_u": "float (cm⁻¹)"
        }
      },
      "description": "The computed Γ‑point frequencies of the three infrared‑active phonon modes of CrSiTe3."
    }
  ],
  "notes": "The checker compares the submitted frequencies to reference values with a tolerance. The exact tolerance is hidden."
}
```

## How you are scored
A hidden verifier will read your ir_phonon_frequencies.json file. It compares each of the three frequencies (A_u, 1E_u, 2E_u) to reference values that are derived from the paper’s DFT+phonon calculations. To earn full credit, each frequency must fall within a tolerance of the corresponding reference; partial credit may be awarded if only some are within tolerance. The tolerance is chosen to accommodate the typical spread that arises from using a different plane-wave code and numerical settings while still distinguishing a genuinely correct calculation from an arbitrary guess. The verifier does not disclose the reference values or the tolerance; it simply returns a score between 0 and 1 based on the agreement.
