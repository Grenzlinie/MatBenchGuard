# DFT investigation of spin-state-dependent electron transfer in Fe(III)-hydroperoxo complexes

## Problem background
Hydroperoxo–iron(III) species are proposed as key intermediates in biological oxygenases such as heme‑oxygenase, where heterolytic O–O bond cleavage is required for terminal oxygen‑atom transfer. The spin state of the iron(III) ion — high‑spin (S=5/2) versus low‑spin (S=1/2) — is hypothesized to influence the electron redistribution that drives bond cleavage, but the mechanistic role of the unpaired d‑electron remains an open question. This task addresses that question by using density‑functional theory to compute Mulliken atomic charges on a model complex Fe(DP)(H₂O)₃(OOH) (DP = tetramethyl‑2,2′‑dipyrromethene) as a function of geometric parameters. The computational experiments will probe how spin state, the Fe–O–O angle (α), and the proton torsion angle (β) affect the charge on the peroxide oxygens, the iron atom, and an adjacent ligand carbon. The resulting charge patterns are expected to reveal spin‑state‑dependent electron‑transfer behaviour, providing insight into the conditions that favour heterolytic O–O cleavage.

## Approach
The reproduction employs density‑functional theory (DFT) with an unrestricted hybrid functional (e.g., B3LYP, providing ~20% Hartree–Fock exchange) and a double‑zeta quality basis set (e.g., 6‑31G*). The molecular model is Fe(DP)(H₂O)₃(OOH) with the O2–O1–Fe–N(DP) dihedral fixed at 45°. For two spin states — high‑spin (sextet, S=5/2) and low‑spin (doublet, S=1/2) — single‑point calculations are carried out over a grid of geometric parameters: Fe–O1–O2 angle α ∈ {110°, 120°} and O1–O2–H torsion β from 120° to 230° in 10° steps. At each (α, β, spin) combination, Mulliken population analysis yields net atomic charges for the peroxide oxygen atoms (O1, O2), the iron atom (Fe), and the carbon atom of the DP ligand closest to O2 (C*). All charges are compiled into a single CSV file for analysis. No experimental data or pre‑existing datasets are required; the workflow relies solely on the computational protocol described.

## Reproduction target
Using an open‑source quantum chemistry package, compute unrestricted single‑point DFT calculations for the Fe(DP)(H₂O)₃(OOH) complex as specified in the Approach. For each spin state (high‑spin, low‑spin), each α (110°, 120°), and each β from 120° to 230° in increments of 10°, extract Mulliken net atomic charges for O1, O2, Fe, and the DP carbon atom closest to O2 (C*). Compile all results into a single CSV file named `mulliken_charges.csv` with columns: `alpha` (degrees), `beta` (degrees), `spin_state` (`low` or `high`), `atom_label` (`O1`, `O2`, `Fe`, or `Cstar`), and `mulliken_charge` (atomic units). The hidden verifier will read this file and verify that the charge–β profiles exhibit the required spin‑state‑dependent behaviour and α‑modulation by performing structural checks on the computed curves.

## Assets

- Quantum chemistry package (PySCF, NWChem, ORCA, or equivalent): https://github.com/pyscf/pyscf

## Workflow steps

### Step 1: Run DFT calculations on Fe(DP)(H2O)3(OOH)
- Role: process
- Action: Set up the molecular geometry for Fe(DP)(H2O)3(OOH) with a fixed O2-O1-Fe-N(DP) torsion of 45°. For each combination of spin state (high-spin sextet, low-spin doublet), Fe-O1-O2 angle α in {110°, 120°}, and O1-O2-H angle β from 120° to 230° in 10° increments, perform a single-point unrestricted DFT calculation using a hybrid functional (e.g., B3LYP) and a double-zeta basis set (e.g., 6-31G*). Save the output logs containing Mulliken population analysis.
- Evidence: `/app/outputs/dft_output_logs.zip`

### Step 2: Compile Mulliken charges into a CSV
- Role: scored (load-bearing)
- Action: Parse the DFT output logs from the previous step to extract Mulliken net atomic charges for atoms O1, O2, Fe, and the adjacent carbon C* (the carbon atom of the DP ligand closest to O2) at every calculated geometry. Write a CSV file with columns: alpha, beta, spin_state, atom_label, mulliken_charge.
- Output file: `/app/outputs/mulliken_charges.csv`
- Format: csv
- Contract: Columns: alpha (float, degrees), beta (float, degrees), spin_state (string, 'low' or 'high'), atom_label (string, one of 'O1','O2','Fe','Cstar'), mulliken_charge (float, atomic units). One row per calculation. Must cover all beta steps 120-230° in increments of 10°, for both alpha values (110,120) and both spin states.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mulliken_charges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mulliken_charges.csv
- path: `/app/outputs/mulliken_charges.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The compiled Mulliken net atomic charges for the key atoms in Fe(DP)(H2O)3(OOH) as a function of α, β, and spin state. The hidden checker will validate the structural pattern (discontinuity for high-spin, smooth for low-spin, and α-dependence) by computing consecutive differences.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `beta`, `spin_state`, `atom_label`, `mulliken_charge`
  - `units`:
    - `alpha`: degrees
    - `beta`: degrees
    - `mulliken_charge`: e

Notes: The identity of C* is the carbon atom of the DP ligand that is closest to O2; the solver must identify it by geometry inspection. Gas-phase calculations are acceptable. The octamethyl-porphyrin model is excluded because high-spin calculations did not converge in the original work.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mulliken_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "beta",
          "spin_state",
          "atom_label",
          "mulliken_charge"
        ],
        "units": {
          "alpha": "degrees",
          "beta": "degrees",
          "mulliken_charge": "e"
        }
      },
      "description": "The compiled Mulliken net atomic charges for the key atoms in Fe(DP)(H2O)3(OOH) as a function of α, β, and spin state. The hidden checker will validate the structural pattern (discontinuity for high-spin, smooth for low-spin, and α-dependence) by computing consecutive differences."
    }
  ],
  "notes": "The identity of C* is the carbon atom of the DP ligand that is closest to O2; the solver must identify it by geometry inspection. Gas-phase calculations are acceptable. The octamethyl-porphyrin model is excluded because high-spin calculations did not converge in the original work."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that acts on the scored output `mulliken_charges.csv`. The verifier first validates the schema (all required columns and rows covering every α, β, spin combination). It then examines the charge profiles as a function of β for each spin state and α value. Rather than comparing to a fixed numeric target, the verifier performs a structural audit that checks whether the variation patterns conform to the expected spin‑state‑dependent relationships — for example, whether the β‑dependence of the charges is of one character for the low‑spin state and a different character for the high‑spin state, and whether the α angle modulates the effect as described in the underlying study. The final score is a single number between 0 and 1, reflecting how well the computed charges satisfy the reference structural pattern. No other artifacts are scored; the remaining workflow steps are process steps that are required but do not directly contribute to the score.
