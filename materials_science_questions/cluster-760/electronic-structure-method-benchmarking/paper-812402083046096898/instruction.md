# Zero-point-corrected binding energies of K+·H2O, K+·N2, and K+·CO2

## Problem background
Potassium-cation/ligand complexes (K+·H2O, K+·N2, K+·CO2) are important for understanding atmospheric ion-neutral chemistry and sporadic metal layers. Accurate binding energies are needed for thermodynamic and kinetic models, but experimental data are scarce. This task reproduces the computational determination of reliable zero‑point–corrected binding energies (D0) for each complex.

## Approach
The binding energies are computed via a three-step ab initio protocol:

1. Geometry optimization and harmonic vibrational frequency calculations at the MP2 level of theory using a moderately sized basis set (Basis B). This yields equilibrium geometries and zero‑point vibrational energy (ZPVE) corrections.
2. Single‑point energy calculations at the CCSD(T) level with a larger basis set (Basis C) and full counterpoise correction. Accurate electronic energies are obtained for the complex, the isolated K+ (with ligand ghost functions), and the isolated ligand (with K ghost functions).
3. The electronic binding energy De = E(complex) – E(K+) – E(ligand) is corrected by the difference of ZPVEs to obtain D0 = De – [ZPVE(complex) – ZPVE(K+) – ZPVE(ligand)].

Effective core potentials are used for potassium, while all other atoms are treated with standard correlation-consistent basis sets. All basis sets and ECPs are publicly available from the EMSL Basis Set Exchange. The workflow can be implemented with any open‑source quantum chemistry package supporting MP2, CCSD(T), ECPs, and counterpoise corrections (e.g., Psi4, PySCF, ORCA).

## Reproduction target
For each of the three complexes (K+·H2O, K+·N2, K+·CO2), carry out the protocol described in the Approach and Workflow steps to obtain the zero‑point‑corrected binding energy D0 (kcal/mol). Write the three D0 values into the JSON file `/app/outputs/binding_energies.json` with the keys `K+_H2O_D0`, `K+_N2_D0`, and `K+_CO2_D0`.

## Assets

- Basis B: LANL2 ECP + (8s8p4d2f) for K, aug-cc-pVTZ for other atoms: https://www.basissetexchange.org
- Basis C: ECP10MWB + [10s9p6d4f3g] for K, aug-cc-pV5Z (no h/g) for others: https://www.basissetexchange.org
- Open-source quantum chemistry package (e.g., Psi4, PySCF, ORCA): psi4 or pyscf or orca

## Workflow steps

### Step 1: Geometry optimization and harmonic frequency calculations
- Role: process
- Action: For each complex (K+·H2O, K+·N2, K+·CO2), optimize the geometry at the MP2(full) level using Basis B and compute harmonic vibrational frequencies to obtain the zero-point vibrational energy (ZPVE). Correlate all electrons except the K 1s2s2p ECP core.
- Evidence: `/app/outputs/geometries_and_zpve.json`

### Step 2: Single-point CCSD(T) energy calculations with counterpoise correction
- Role: process
- Action: At the optimized geometries, perform single-point CCSD(T) calculations using Basis C with full counterpoise correction. For each complex, compute the energy of the complex, the energy of K+ with ligand ghost functions, and the energy of the ligand with K ghost functions.
- Evidence: `/app/outputs/energies.json`

### Step 3: Compute zero-point-corrected binding energies D0
- Role: scored (load-bearing)
- Action: Using the ZPVE from the frequency calculation and the CCSD(T) energies, compute the electronic binding energy De = E(complex) - E(K+) - E(ligand) with counterpoise correction, then apply the ZPVE correction: D0 = De - (ZPVE(complex) - ZPVE(K+) - ZPVE(ligand)). Report D0 (kcal/mol) for K+·H2O, K+·N2, and K+·CO2.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {"K+_H2O_D0": float, "K+_N2_D0": float, "K+_CO2_D0": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zero-point-corrected binding energies in kcal/mol for the three complexes.
- schema:
  - `type`: object
  - `required`:
    - `K+_H2O_D0`: number
    - `K+_N2_D0`: number
    - `K+_CO2_D0`: number
  - `units`:
    - `K+_H2O_D0`: kcal/mol
    - `K+_N2_D0`: kcal/mol
    - `K+_CO2_D0`: kcal/mol

Notes: The checker compares each D0 value against reference binding energies with tolerance and verifies the structural ordering D0(H2O) > D0(CO2) > D0(N2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "K+_H2O_D0": "number",
          "K+_N2_D0": "number",
          "K+_CO2_D0": "number"
        },
        "units": {
          "K+_H2O_D0": "kcal/mol",
          "K+_N2_D0": "kcal/mol",
          "K+_CO2_D0": "kcal/mol"
        }
      },
      "description": "Zero-point-corrected binding energies in kcal/mol for the three complexes."
    }
  ],
  "notes": "The checker compares each D0 value against reference binding energies with tolerance and verifies the structural ordering D0(H2O) > D0(CO2) > D0(N2)."
}
```

## How you are scored
A hidden verifier will read your `binding_energies.json` and compare the three reported D0 values against reference values. Full credit is awarded only if all three values agree within acceptable tolerances AND the relative ordering of the binding energies among the three complexes is correct. Partial credit may be assigned when some, but not all, of the values are satisfactory. The specific tolerances and the expected ordering are not disclosed; you must compute the values accurately from the given protocol.
