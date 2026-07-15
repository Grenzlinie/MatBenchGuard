# Tight-Binding Simulation of Quantum Confinement in Patterned Silicon Substrates

## Problem background
Fabrication of ordered arrays of quantum wires by etching a hole pattern into a silicon substrate aims to create electronically decoupled one‑dimensional conduction channels. Mechanical interconnects between the interstitial pillars can, however, allow electronic coupling that spoils confinement. This task studies the electronic structure of such patterned Si structures to determine the interconnect thicknesses for which the lowest conduction‑band eigenstates are spatially confined to the interstitial regions, enabling quantum‑wire behaviour. You will compute the relevant eigenstates for a Si [110] substrate with centred‑rectangular holes at two different interconnect thicknesses, and quantify the degree of localization within the pillars.

## Approach
We use the empirical tight‑binding method within the antibonding orbital model (ABOM) for silicon. The ABOM basis consists of four antibonding (conduction‑band) orbitals per fcc lattice site: |s>, |px>, |py>, |pz>. The fcc lattice constant is 0.543 nm. Tight‑binding parameters are taken from the literature. For the patterned structure, a supercell is constructed with hole pitch p = 44.8 nm, interstitial size d = 10.9 nm, and two interconnect thicknesses: t = 7.8 nm and t = 12.2 nm. For each thickness you will: (i) build the full tight‑binding Hamiltonian matrix, (ii) diagonalize it to obtain the lowest five conduction eigenvalues and eigenvectors, (iii) compute the charge density from the eigenvector coefficients, and (iv) evaluate the fraction of charge density that falls inside the interstitial pillar volume. The first and fifth eigenstates are of particular interest; comparing their energy splitting and localization fractions across the two interconnect thicknesses reveals the effect of coupling on confinement.

## Reproduction target
Produce a JSON file `/app/outputs/electronic_results.json` containing, for each interconnect thickness, the lowest five conduction‑band eigenvalues (in eV) and the charge‑density localization fractions for the first and fifth eigenstates. The JSON must have the structure:
{
  "t_7_8": {
    "eigenvalues": [e1, e2, e3, e4, e5],
    "localization_fraction_1st": f1,
    "localization_fraction_5th": f5
  },
  "t_12_2": {
    "eigenvalues": [e1, e2, e3, e4, e5],
    "localization_fraction_1st": f1,
    "localization_fraction_5th": f5
  }
}
All eigenvalues are in eV; the list must be sorted ascending. Each localization fraction is a number between 0 and 1. The target is to obtain these quantitative outputs from the tight‑binding simulation described above.

## Assets

- ABOM tight-binding parameters for silicon: 10.1063/1.351347
- Theory of intervalley coupling in reduced dimensionality silicon: 10.1103/PhysRevB.72.125330
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute eigenvalues and confinement fractions
- Role: scored (load-bearing)
- Action: Build the empirical tight-binding Hamiltonian matrices for the Si [110] patterned structure with centred-rectangular holes (p=44.8 nm, d=10.9 nm) for interconnect thicknesses t=7.8 nm and t=12.2 nm using the antibonding orbital model (ABOM) with parameters from Chang et al. (1992). The fcc lattice constant is 0.543 nm. For each thickness, diagonalize to obtain the lowest five conduction eigenvalues. Compute the charge density from eigenvector components and determine the fraction of charge density within the interstitial pillar volume (defined by the hole geometry). For the first and fifth eigenstates, record the localization fraction. Output a JSON file containing eigenvalues and localization fractions for both thicknesses.
- Output file: `/app/outputs/electronic_results.json`
- Format: json
- Contract: JSON object with keys t_7_8 and t_12_2. Each value is an object with keys: eigenvalues (list of 5 numbers, in eV), localization_fraction_1st (number between 0 and 1), localization_fraction_5th (number between 0 and 1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_results.json
- path: `/app/outputs/electronic_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed eigenvalues and charge-density localization fractions for the first and fifth conduction-band states at two interconnect thicknesses. The checker will compare eigenvalues (from which Δ5-1 is derived) and localization fractions to hidden reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `t_7_8`:
      - `eigenvalues`: list of 5 float (eV)
      - `localization_fraction_1st`: float (0-1)
      - `localization_fraction_5th`: float (0-1)
    - `t_12_2`:
      - `eigenvalues`: list of 5 float (eV)
      - `localization_fraction_1st`: float (0-1)
      - `localization_fraction_5th`: float (0-1)

Notes: The target policy is exact_match because the scored quantities are deterministic outputs of the tight-binding simulation; the checker will accept results within specified absolute tolerances. Localization fraction thresholds are verified as part of the same comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "t_7_8": {
            "eigenvalues": "list of 5 float (eV)",
            "localization_fraction_1st": "float (0-1)",
            "localization_fraction_5th": "float (0-1)"
          },
          "t_12_2": {
            "eigenvalues": "list of 5 float (eV)",
            "localization_fraction_1st": "float (0-1)",
            "localization_fraction_5th": "float (0-1)"
          }
        }
      },
      "description": "Computed eigenvalues and charge-density localization fractions for the first and fifth conduction-band states at two interconnect thicknesses. The checker will compare eigenvalues (from which Δ5-1 is derived) and localization fractions to hidden reference values with tolerances."
    }
  ],
  "notes": "The target policy is exact_match because the scored quantities are deterministic outputs of the tight-binding simulation; the checker will accept results within specified absolute tolerances. Localization fraction thresholds are verified as part of the same comparison."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/electronic_results.json`. For each thickness it will compute the energy splitting Δ5‑1 = eigenvalue[4] − eigenvalue[0] and compare both Δ5‑1 and the localization fractions to reference values (from the paper’s original calculations) using tolerances that account for legitimate implementation differences. You earn credit when Δ5‑1 is within tolerance and the localization fractions meet the expected confinement thresholds. Scoring is per thickness; the final reward is a weighted sum across both thicknesses. Simply reporting numbers without actually building the Hamiltonian and diagonalizing it will not pass the underlying checks.
