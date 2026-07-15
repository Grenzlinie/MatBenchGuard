# DFT computation of binding energies and vibrational modes of boron-hydrogen complexes in diamond

## Problem background
The paper investigates deuterium (hydrogen) trapping in heavily boron-doped diamond. Experimental deuterium diffusion profiles in diamond epilayers with high boron concentrations (≥10¹⁹ cm⁻³) show that, in addition to the expected passivation of single boron acceptors as B-H pairs, deeper traps appear at the heaviest doping levels. The computational component uses first-principles density functional theory to study the properties of nearest-neighbor boron pairs (B₂) and their interaction with hydrogen, which may help explain the observed trapping behavior. The task is to reproduce the key DFT results—binding energies for B-H, B-B, B₂H₁, and B₂H₂ defect complexes and the highest-frequency local vibrational modes (LVMs) of selected isotopic combinations—using an open-source DFT code.

## Approach
Model diamond using a 64-atom supercell and insert the required defects: a single substitutional boron (B_s, neutral and negative), an isolated interstitial hydrogen at a bond-center site (H⁺), the B-H complex, a nearest-neighbor boron pair (B₂, neutral and charged), and the B₂H₁ and B₂H₂ complexes. Perform total-energy and geometry-optimization calculations with Quantum ESPRESSO employing the local-density approximation (LDA) and norm-conserving pseudopotentials. For charged supercells, apply a uniform compensating background charge.

From the converged total energies, compute formation energies for each species in the relevant charge states using the chemical potential of carbon from bulk diamond, boron from α‑boron, and hydrogen from the H₂ molecule, together with a point-charge Madelung correction for periodic electrostatic interactions. Binding energies are then evaluated as energy differences for the following reactions, taking care to use the appropriate charge states:
- B-H binding energy: (BH)⁰ → H⁺ + B⁻
- B-B binding energy: B₂ (neutral) → 2 × B_s (neutral)
- First H binding to B₂: (B₂H₁)⁻ → B₂²⁻ + H⁺
- B₂H₂ binding energy: B₂H₂ (neutral) → B₂ (neutral) + H₂*, where H₂* is the lowest-energy configuration of two interstitial hydrogen atoms in diamond.

After relaxing the structures, compute the vibrational modes of the B-H and neutral B₂H₁ complexes. Construct the dynamical matrix from DFT‑derived force constants for the defect‑core atoms and a valence‑force potential for the host. Diagonalize to obtain harmonic frequencies. Extract the highest-frequency H‑related mode for each isotopic combination specified in the target.

## Reproduction target
Produce the following quantitative results:
1. **Binding energies** (in eV) for four defect reactions:
   - B-H complex: the binding energy for (BH)⁰ → H⁺ + B⁻.
   - Boron pair: the binding energy for B₂ (neutral) → 2 × B_s (neutral).
   - First H to B₂: the binding energy for (B₂H₁)⁻ → B₂²⁻ + H⁺.
   - B₂H₂ complex: the binding energy for B₂H₂ (neutral) → B₂ (neutral) + H₂* (lowest-energy two-H configuration in diamond).
2. **Highest-frequency H‑related vibrational mode** (in cm⁻¹) for:
   - The B-H complex (B₁H₁), for the isotopic combinations ¹¹BH, ¹¹BD, ¹⁰BH, ¹⁰BD.
   - The neutral B₂H₁ complex, for the isotopic combinations ¹¹BH¹¹B and ¹⁰BH¹¹B.

Write the four binding energies to `/app/outputs/binding_energies.json` and the six frequencies to `/app/outputs/vibrational_frequencies.csv` with the columns `defect`, `isotope`, and `mode_frequency_cm-1`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP pseudopotentials (norm-conserving LDA for C, B, H): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Build defect supercell models
- Role: process
- Action: Construct 64-atom diamond supercells for pristine bulk, substitutional boron (neutral and -1), interstitial hydrogen (H⁺ at bond-center), B-H complex (neutral), boron pair B₂ (neutral, -1, -2), B₂H₁ (neutral, -1), and B₂H₂ (neutral) using the known diamond lattice constant and defect geometries. Output coordinate files suitable for Quantum ESPRESSO.
- Evidence: `/app/outputs/supercell_coordinates.txt`

### Step 2: Run DFT total-energy calculations
- Role: process
- Action: For each defect configuration from step 1, perform geometry optimization and total-energy calculation using Quantum ESPRESSO with LDA, norm-conserving pseudopotentials, a plane-wave cutoff of 300 Ry, and a 2×2×2 Monkhorst-Pack k-point mesh. For charged defects, use a compensating uniform background charge. Record the final relaxed geometry and total energy.
- Evidence: `/app/outputs/dft_relaxed_structures_and_energies.txt`

### Step 3: Compute defect binding energies
- Role: scored (load-bearing)
- Action: From DFT total energies, compute formation energies using chemical potentials for C (bulk diamond), B (alpha-boron), H (H₂ molecule) and a point-charge Madelung correction. Then calculate binding energies: B-H (BH⁰ → H⁺ + B⁻), B-B pair (B₂ → 2 B_s), first H to B₂ (B₂H₁⁻ → B₂²⁻ + H⁺), and B₂H₂ relative to B₂ + H₂* (lowest-energy two-H configuration in diamond). Report values in eV.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: JSON object with keys: B_H_binding_energy_eV (float), B_B_binding_energy_eV (float), B2H1_binding_energy_eV (float), B2H2_binding_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 4: Compute local vibrational mode frequencies
- Role: scored (load-bearing)
- Action: From relaxed geometries, construct dynamical matrix using DFT-derived force constants for defect core atoms and a valence-force potential for the host. Diagonalize to obtain harmonic frequencies. For B-H complex, compute the highest-frequency H-related mode for isotopic combinations ¹¹BH, ¹¹BD, ¹⁰BH, ¹⁰BD. For neutral B₂H₁, compute the highest-frequency mode for ¹¹BH¹¹B and ¹⁰BH¹¹B. Report frequencies in cm⁻¹.
- Output file: `/app/outputs/vibrational_frequencies.csv`
- Format: csv
- Contract: CSV with columns: defect (string, e.g. 'B1H1' or 'B2H1_neutral'), isotope (string, e.g. '11BH'), mode_frequency_cm-1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`
- `/app/outputs/vibrational_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Binding energies for B-H, B-B pair, first H to B₂, and B₂H₂ complexes. Compared to paper's reported values within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `B_H_binding_energy_eV`: float
    - `B_B_binding_energy_eV`: float
    - `B2H1_binding_energy_eV`: float
    - `B2H2_binding_energy_eV`: float
  - `units`:
    - `B_H_binding_energy_eV`: eV
    - `B_B_binding_energy_eV`: eV
    - `B2H1_binding_energy_eV`: eV
    - `B2H2_binding_energy_eV`: eV

### vibrational_frequencies.csv
- path: `/app/outputs/vibrational_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Highest-frequency local vibrational modes for B-H and B₂H₁ defects in specified isotopic combinations. Frequencies are compared to paper's reported values within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `isotope`, `mode_frequency_cm-1`
  - `units`:
    - `mode_frequency_cm-1`: cm^{-1}

Notes: The task covers only the computational DFT part of the paper. Experimental diffusion data are excluded.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "B_H_binding_energy_eV": "float",
          "B_B_binding_energy_eV": "float",
          "B2H1_binding_energy_eV": "float",
          "B2H2_binding_energy_eV": "float"
        },
        "units": {
          "B_H_binding_energy_eV": "eV",
          "B_B_binding_energy_eV": "eV",
          "B2H1_binding_energy_eV": "eV",
          "B2H2_binding_energy_eV": "eV"
        }
      },
      "description": "Binding energies for B-H, B-B pair, first H to B₂, and B₂H₂ complexes. Compared to paper's reported values within a tolerance."
    },
    {
      "file": "vibrational_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "isotope",
          "mode_frequency_cm-1"
        ],
        "units": {
          "mode_frequency_cm-1": "cm^{-1}"
        }
      },
      "description": "Highest-frequency local vibrational modes for B-H and B₂H₁ defects in specified isotopic combinations. Frequencies are compared to paper's reported values within a tolerance."
    }
  ],
  "notes": "The task covers only the computational DFT part of the paper. Experimental diffusion data are excluded."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that runs after your task completes. It independently reads `binding_energies.json` and `vibrational_frequencies.csv`, extracts the required numeric values, and compares each one to a set of reference values (the paper’s own reported results) using pre‑defined tolerances. For binding energies the per‑field score is the fraction of values falling within the allowed tolerance; for vibrational frequencies the score is the fraction of mode frequencies within their tolerance. The overall reward is the average of the two per‑artifact scores, each scaled to equal weight. Simply reporting the benchmarked values is not sufficient—the verifier checks the correctness and consistency of your computed outputs against the hidden gold, and any missing, incorrectly named, or improperly formatted field results in zero credit for that field.
