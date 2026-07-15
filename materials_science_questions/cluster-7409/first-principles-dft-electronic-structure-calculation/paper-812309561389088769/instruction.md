# First-principles DFT electronic structure calculation for Zr-substituted PZT clusters

## Problem background
Ferroelectric Pb(Zr₁₋ₓTiₓ)O₃ (PZT) is a critical material for non‑volatile memories and electro‑mechanical devices, but repeated polarization switching leads to fatigue. It has been proposed that fatigue is linked to electrons occupying the Ti 3d states, and that Zr substitution at Ti sites modifies the electronic structure near the band edges. This task replicates the first‑principles calculation of the HOMO‑LUMO energy gap (between O 2p and Ti 3d states) for four cluster models with different Zr substitution amounts and positions. The computed gap trend is the central piece of evidence for the paper’s conclusion about fatigue susceptibility. The goal is to compute these four gaps and their relative ordering.

## Approach
Use an open‑source DFT code that supports cluster calculations (non‑periodic) to perform self‑consistent field (SCF) calculations on four finite cluster models of composition (Pb₈B₃O₄₈)⁶⁸⁻ (B = Ti or Zr). The clusters are built using the experimental PbTiO₃ lattice constants a = 3.904 Å, c = 4.152 Å with P4MM symmetry and atomic positions as described in the original study. The four substitution cases are: (1) no Zr, (2) Zr substituting the upper Ti atom, (3) Zr substituting the lower Ti atom, and (4) Zr substituting both Ti atoms. After converging the electronic structure, extract the molecular orbital energies and identify the highest occupied molecular orbital (HOMO) and lowest unoccupied molecular orbital (LUMO). The HOMO is predominantly O 2p character and the LUMO is predominantly Ti 3d character. Compute the HOMO‑LUMO gap as the absolute energy difference in eV for each case. The comparison among these four gap values constitutes the reproduction target. No external dataset is needed; the only input is the geometry specification.

## Reproduction target
Produce a JSON file at /app/outputs/energy_gaps.json containing the computed HOMO‑LUMO gaps (in eV) for all four substitution cases and a string representation of the observed relative ordering. The file must include the fields: no_substitution (float), upper_Zr (float), lower_Zr (float), both (float), and ordering (string, e.g. 'case1 < case2 < case3 < case4'). The ordering field should reflect the gap values you obtained, not a predetermined answer. The verifier will assess the correctness of the relative ordering and the consistency between the reported gaps and the ordering string.

## Assets

- Open-source DFT software for cluster calculations: http://www.cp2k.org

## Workflow steps

### Step 1: Build cluster models
- Role: process
- Action: Construct the four (Pb₈B₃O₄₈)⁶⁸⁻ cluster models: no substitution, Zr substitution on upper Ti, Zr substitution on lower Ti, Zr substitution on both Ti sites. Use the experimental PbTiO₃ lattice parameters a=3.904 Å, c=4.152 Å, P4MM symmetry, and the atomic positions as described in the paper. Use a finite cluster model with suitable vacuum or supercell.
- Evidence: `/app/outputs/cluster_models.json`

### Step 2: Run DFT calculations
- Role: process
- Action: Perform self-consistent DFT calculations for all four cluster models using an open-source DFT code capable of non-periodic cluster calculations. Converge energies and charge densities; after self-consistent field (SCF) cycles, obtain molecular orbital energies.
- Evidence: `/app/outputs/dft_calc.log`

### Step 3: Extract HOMO-LUMO gaps
- Role: scored (load-bearing)
- Action: From the converged orbital energies, identify the highest occupied molecular orbital (HOMO) and lowest unoccupied molecular orbital (LUMO) for each cluster model. Compute the HOMO-LUMO gap as the absolute energy difference in eV. Write the four gap values and the observed ordering to energy_gaps.json.
- Output file: `/app/outputs/energy_gaps.json`
- Format: json
- Contract: JSON object with keys: no_substitution (float, eV), upper_Zr (float, eV), lower_Zr (float, eV), both (float, eV), and ordering (string, e.g., 'case1 < case2 < case3 < case4')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_gaps.json
- path: `/app/outputs/energy_gaps.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: HOMO-LUMO energy gaps for the four cluster models and the claimed relative ordering. The checker validates the ordering as described in the paper; exact numerical values are not compared due to method differences.
- schema:
  - `type`: object
  - `required`: `no_substitution`, `upper_Zr`, `lower_Zr`, `both`, `ordering`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `no_substitution`: eV
    - `upper_Zr`: eV
    - `lower_Zr`: eV
    - `both`: eV

Notes: Only the relative ordering of the HOMO-LUMO gaps is scored; the exact gap magnitude is free to vary with the chosen DFT implementation. The net-charge and overlap-population analyses are omitted as they are not central to the fatigue prediction claim and are strongly method-dependent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "no_substitution",
          "upper_Zr",
          "lower_Zr",
          "both",
          "ordering"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "no_substitution": "eV",
          "upper_Zr": "eV",
          "lower_Zr": "eV",
          "both": "eV"
        }
      },
      "description": "HOMO-LUMO energy gaps for the four cluster models and the claimed relative ordering. The checker validates the ordering as described in the paper; exact numerical values are not compared due to method differences."
    }
  ],
  "notes": "Only the relative ordering of the HOMO-LUMO gaps is scored; the exact gap magnitude is free to vary with the chosen DFT implementation. The net-charge and overlap-population analyses are omitted as they are not central to the fatigue prediction claim and are strongly method-dependent."
}
```

## How you are scored
A hidden verifier inspects your submitted energy_gaps.json. It reads the four gap values and the ordering string, then checks that the ordering relations encoded in the string are internally consistent with the actual numeric gaps. Separately, it compares your observed ordering against a hidden reference ordering derived from the paper. The score is based solely on the correctness of the relative order of the four gaps; exact numerical values are not compared, because the gap magnitude depends on the chosen DFT functional and basis set. Reward is proportional to the number of correct pairwise order relations. Reporting the paper’s numbers without running the DFT calculations will not satisfy the verifier, as it also checks internal consistency between the gaps and the ordering string.
