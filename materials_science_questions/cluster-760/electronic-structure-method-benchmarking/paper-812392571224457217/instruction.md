# Energetic benchmarks for Fe(CO)5: singlet-triplet splitting and bond dissociation energy

## Problem background
The iron pentacarbonyl system [Fe(CO)₅] is a cornerstone of organometallic chemistry and a prototype for understanding photodissociation and ligand recombination dynamics. Its smallest fragment, [Fe(CO)₄], has a triplet ground state, while the saturated 18-electron complex is a singlet. The singlet–triplet energy splitting ΔE(1,3) and the first bond dissociation energy BDE(3) are critical parameters that govern the rates of spin-forbidden reactions and are needed to interpret kinetic experiments. However, previous computational estimates vary considerably due to the difficulty of treating electron correlation effects in transition-metal compounds. This work provides a carefully calibrated set of ab‑initio and density‑functional calculations that converge on best first‑principles estimates for ΔE(1,3) and BDE(3) using a hierarchical approach—from geometry optimization to high-level single-point energies—and defines a reproducible protocol to obtain these quantities.

## Approach
The reproduction employs a sequence of quantum chemistry calculations to obtain total electronic energies and zero‑point energy (ZPE) corrections at the levels described below. The general workflow is:

1. **Geometry optimization** of the four relevant species—singlet ¹[Fe(CO)₄], triplet ³[Fe(CO)₄], [Fe(CO)₅], and CO—using the modified B3PW91* hybrid functional (with 15 % exact exchange instead of the default 20 %) and the TZV basis set.
2. **Harmonic vibrational frequency calculations** at the optimized geometries, also at the B3PW91*/TZV level, to obtain ZPE corrections.
3. **Single‑point BP86/TZV calculations** at the optimized geometries to generate Kohn–Sham orbitals; these orbitals serve as the reference wavefunction for the subsequent coupled‑cluster step because they improve the quality of the CC expansion for these multi‑reference‑prone systems.
4. **CCSD(T)/VQZ‑VDZ single‑point energy calculations** using the orbitals from step 3 and a mixed basis set: a large Fe basis (VQZ) and a correlation‑consistent valence‑double‑ζ basis for C and O. This yields the high‑level total electronic energies.
5. **Collection of the final energies** into a CSV file. From the four CCSD(T) total energies and the four ZPEs, the singlet–triplet splitting ΔE(1,3) = E(singlet) − E(triplet) and the first bond dissociation energy BDE(3) = E(triplet) + E(CO) − E(pentacarbonyl) are derived, both with and without ZPE correction.

## Reproduction target
Produce a CSV file at `/app/outputs/energies.csv` containing the CCSD(T)/VQZ‑VDZ total electronic energies and the B3PW91* zero‑point energies (both in Hartrees) for the four species: `singlet_FeCO4`, `triplet_FeCO4`, `FeCO5`, and `CO`. The columns must be exactly:

- `species`
- `CCSD(T)/VQZ-VDZ_total_energy_Hartree`
- `B3PW91*_zero_point_energy_Hartree`

From this file the verifier will compute ΔE(1,3) and BDE(3) with and without zero‑point corrections and compare them against hidden reference values. The task is to execute the full computational workflow and report the resulting energies; the exact numeric targets are not disclosed.

## Assets

- Open-source quantum chemistry package: any of ORCA, Psi4, PySCF, NWChem
- Ahlrichs TZV basis set
- VQZ-VDZ basis set
- B3PW91* functional definition

## Workflow steps

### Step 1: Geometry optimization at B3PW91*/TZV
- Role: process
- Action: Perform full geometry optimization of singlet ¹[Fe(CO)₄], triplet ³[Fe(CO)₄], [Fe(CO)₅], and CO at the B3PW91*/TZV level.
- Evidence: `/app/outputs/step_01_geom_opt.out`

### Step 2: Harmonic frequency calculation at B3PW91*/TZV
- Role: process
- Action: Compute harmonic vibrational frequencies at the optimized geometries to obtain zero‑point energy corrections.
- Evidence: `/app/outputs/step_02_frequencies.out`

### Step 3: BP86/TZV orbital calculation
- Role: process
- Action: Run a single‑point BP86/TZV calculation at the optimized geometries and store the resulting Kohn–Sham orbitals for use as reference orbitals in CCSD(T).
- Evidence: `/app/outputs/step_03_bp86_orbitals.out`

### Step 4: CCSD(T)/VQZ-VDZ energy calculation
- Role: process
- Action: Perform CCSD(T) single‑point calculations using the VQZ‑VDZ basis set and the BP86 orbitals from step_03 for each species.
- Evidence: `/app/outputs/step_04_ccsdt_energies.out`

### Step 5: Collect scored energetics into energies.csv
- Role: scored (load-bearing)
- Action: Extract the CCSD(T)/VQZ‑VDZ total electronic energies and the B3PW91* ZPEs for all four species. Write a CSV with columns: species, CCSD(T)/VQZ-VDZ_total_energy_Hartree, B3PW91*_zero_point_energy_Hartree.
- Output file: `/app/outputs/energies.csv`
- Format: csv
- Contract: CSV with columns: species, CCSD(T)/VQZ-VDZ_total_energy_Hartree, B3PW91*_zero_point_energy_Hartree. Species values: singlet_FeCO4, triplet_FeCO4, FeCO5, CO. All energies in Hartree.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.csv
- path: `/app/outputs/energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total electronic energies and zero-point energies from which the checker recomputes the singlet–triplet splitting ΔE(1,3) and bond dissociation energy BDE(3) and compares each derived value to the paper's reported best estimates within hidden tolerances.
- schema:
  - `type`: table
  - `required_columns`: `species`, `CCSD(T)/VQZ-VDZ_total_energy_Hartree`, `B3PW91*_zero_point_energy_Hartree`
  - `units`:
    - `CCSD(T)/VQZ-VDZ_total_energy_Hartree`: Hartree
    - `B3PW91*_zero_point_energy_Hartree`: Hartree

Notes: The checker does not access the raw log files; it derives the headline energetics solely from this CSV. All implementation details (functionals, basis sets, orbital choice) are required to follow the paper’s protocol, but the exact values will vary by toolchain—tolerances are chosen to absorb legitimate spread while excluding fabrication.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "CCSD(T)/VQZ-VDZ_total_energy_Hartree",
          "B3PW91*_zero_point_energy_Hartree"
        ],
        "units": {
          "CCSD(T)/VQZ-VDZ_total_energy_Hartree": "Hartree",
          "B3PW91*_zero_point_energy_Hartree": "Hartree"
        }
      },
      "description": "Total electronic energies and zero-point energies from which the checker recomputes the singlet–triplet splitting ΔE(1,3) and bond dissociation energy BDE(3) and compares each derived value to the paper's reported best estimates within hidden tolerances."
    }
  ],
  "notes": "The checker does not access the raw log files; it derives the headline energetics solely from this CSV. All implementation details (functionals, basis sets, orbital choice) are required to follow the paper’s protocol, but the exact values will vary by toolchain—tolerances are chosen to absorb legitimate spread while excluding fabrication."
}
```

## How you are scored
A hidden verifier reads `energies.csv`, checks that it has the required columns and rows for the four species, extracts the total electronic energies and zero‑point energies, and computes the singlet–triplet splitting ΔE(1,3) and the bond dissociation energy BDE(3) in four forms: electronic and ZPE‑corrected for each. Each derived quantity is compared to a hidden gold standard within predetermined tolerances that account for implementation variations. The reward is a weighted sum: each of the four comparisons that falls within its tolerance contributes a proportional share (25 % each) to the final score. The verifier also performs a sanity check on the magnitude of the energies (they must be negative and of the expected order) but this carries minimal weight. Simply reporting a number without running the calculations will not satisfy these checks; the verifier does not inspect the raw log files and scores exclusively from the submitted CSV.
