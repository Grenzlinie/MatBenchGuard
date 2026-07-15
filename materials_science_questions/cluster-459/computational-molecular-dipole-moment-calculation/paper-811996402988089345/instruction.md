# Ab Initio Absolute pKa Calculation of Halogenated Pyridines

## Problem background
The protonation behavior of halogenated pyridine derivatives governs their reactivity, nucleophilicity, and biological interactions. Absolute acidity constants (pKa) are essential for understanding reaction mechanisms and structure–activity relationships, but their experimental measurement can be challenging for heavily substituted heterocycles. First-principles computational chemistry offers a pathway to predict pKa from the thermodynamics of proton transfer in solution, enabling a direct comparison between theory and experiment.

## Approach
The task uses a thermodynamic cycle to compute absolute pKa values. For each compound, the neutral base (B) and its protonated cation (BH⁺) are modeled with quantum chemistry. Gas-phase thermal free energies G_g are obtained from geometry optimizations and vibrational frequency calculations. Solvation free energies ΔG_s are computed with an implicit solvent model (continuum dielectric). The solution-phase free energy change for B + H⁺ → BH⁺ is approximated as ΔG_aq = ΔG_g + ΔG_a, where ΔG_g = G_g(BH⁺) – G_g(B) and ΔG_a = ΔG_s(B) – ΔG_s(BH⁺) + ΔG_s(H⁺). The proton solvation free energy ΔG_s(H⁺) is taken from the literature as a constant within the range −250 to −275 kcal/mol. Finally, pKa = ΔG_aq / (2.303 R T) at T = 298.15 K. The calculations are performed at two levels of theory – Hartree–Fock (HF) and density functional theory (B3LYP) – both with the 6-31G(d) basis set, to assess consistency and methodological dependence. The molecular structures for the 12 target pyridines and their cations are built from physical principles or chemical informatics tools.

## Reproduction target
Compute the absolute pKa values for the 12 halogenated pyridine derivatives (numbered 1–12 in the original publication, corresponding to pyridine and its mono‑ to penta‑halogenated variants) using both HF/6‑31G(d) and B3LYP/6‑31G(d) with an implicit solvent model. Write the results to /app/outputs/pKa_results.csv with three columns: molecule (integer), pKa_HF (float), and pKa_B3LYP (float), in the same order as the original numbering. The file will be evaluated against hidden experimental pKa data.

## Assets

- Psi4 (or ORCA): https://psicode.org/
- RDKit: rdkit

## Workflow steps

### Step 1: Construct initial geometries
- Role: process
- Action: Generate 3D starting structures for the 12 halogenated pyridine neutral bases and their protonated cations as listed in the paper's Scheme 2.
- Evidence: none

### Step 2: Perform quantum chemical calculations
- Role: process
- Action: For each neutral base and protonated cation, execute geometry optimization, frequency calculation, and solvation free energy calculation at HF/6-31G(d) and B3LYP/6-31G(d) levels using an implicit solvent model (e.g., CPCM, SMD) with an open-source quantum chemistry package (Psi4 or ORCA).
- Evidence: none

### Step 3: Compute pKa values
- Role: scored (load-bearing)
- Action: Extract gas-phase thermal free energies (G_g) and solvation free energies (ΔG_s) from the calculations. Compute the gas-phase ionization free energy ΔG_g and the solvation contribution ΔG_a = ΔG_s(B) − ΔG_s(BH⁺) + ΔG_s(H⁺), using a constant ΔG_s(H⁺) taken from the range −250 to −275 kcal/mol. Then compute pKa = (ΔG_g + ΔG_a) / (2.303 R T) at T = 298.15 K. Write the results to a CSV file with columns: molecule (integer 1–12), pKa_HF (float), pKa_B3LYP (float), following the molecule order in the paper's Scheme 2.
- Output file: `/app/outputs/pKa_results.csv`
- Format: csv
- Contract: CSV with columns: molecule (integer 1-12), pKa_HF (float), pKa_B3LYP (float). Rows correspond to molecules in the order of the paper's Scheme 2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pKa_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pKa_results.csv
- path: `/app/outputs/pKa_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed absolute pKa values for 12 halogenated pyridine derivatives at HF/6-31G(d) and B3LYP/6-31G(d) levels. The checker will recompute Pearson R² and mean absolute error (MAE) against hidden experimental pKa values for each method.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `pKa_HF`, `pKa_B3LYP`

Notes: The agent may use any consistent ΔG_s(H⁺) value within the stated range; the checker tolerates different choices. The experimental pKa values are used only as hidden gold for metric recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pKa_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "pKa_HF",
          "pKa_B3LYP"
        ]
      },
      "description": "Computed absolute pKa values for 12 halogenated pyridine derivatives at HF/6-31G(d) and B3LYP/6-31G(d) levels. The checker will recompute Pearson R² and mean absolute error (MAE) against hidden experimental pKa values for each method."
    }
  ],
  "notes": "The agent may use any consistent ΔG_s(H⁺) value within the stated range; the checker tolerates different choices. The experimental pKa values are used only as hidden gold for metric recomputation."
}
```

## How you are scored
After the workflow completes, a hidden verifier reads your pKa_results.csv. It calculates the Pearson correlation coefficient (R²) and the mean absolute error (MAE) between your computed values and experimentally measured pKa values (separately for the HF and B3LYP columns). The final score reflects the quality of agreement: the verifier uses a threshold‑or‑better policy, granting full credit when the reproduction meets a predetermined performance level (high correlation, low error) and scaling the reward down smoothly as the agreement deteriorates. No prior knowledge of the experimental numbers is needed; just compute the pKa values honestly from the protocol.
