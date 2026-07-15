# Γ-Point Electron-Phonon Coupling and Total λ Estimation for Cu-substituted Lead Phosphate Apatite

## Problem background
Copper-substituted lead phosphate apatite (commonly known as LK99) was recently proposed as a candidate for room-temperature ambient-pressure superconductivity. A key quantity to assess superconductivity is the electron–phonon coupling strength λ. For the copper-substituted variants Pb₉Cu(PO₄)₆X₂ (X = O, OH) with Cu substituted at the Pb(1) site, the full Brillouin-zone λ is computationally expensive to obtain directly. Instead, a proxy based on the electron–phonon coupling at the Γ point, λ_Γ, can be computed and then scaled to estimate the total λ. Determining λ_Γ and the estimated total λ for these materials provides insight into the viability of electron–phonon-mediated superconductivity.

## Approach
The approach uses density functional theory (DFT) and density-functional perturbation theory (DFPT) as implemented in Quantum Espresso. In this workflow, the crystal structures are first fully relaxed using the PBE functional. Then DFPT calculations are performed at the Γ point to compute λ_Γ as a function of electronic smearing. The λ_Γ at the finest smearing is taken as the representative value. To convert λ_Γ into an estimate of the total electron–phonon coupling λ, a scaling factor f is introduced: λ ≈ f·λ_Γ. This factor is derived from a reference calculation on a related compound, Pb₉Cu(PO₄)₆O₂ with Cu at the Pb(2) site, for which the total λ is available from an independent study. The final task computes λ_Γ at Γ for the Pb(1) compounds (X=O and X=OH) and then multiplies by the determined f to obtain the estimated total λ.

## Reproduction target
Produce a CSV file containing the computed λ_Γ (at the smallest electronic smearing) and the estimated total λ for Pb₉Cu(PO₄)₆O₂ and Pb₉Cu(PO₄)₆(OH)₂ (both with Cu at the Pb(1) site). The file must have columns: compound, lambda_Gamma, lambda. The scaling factor f must be determined from your own DFPT calculation on the Pb(2) compound and the known reference total λ, not taken as a predefined constant.

## Assets

- Crystal structures of LK99 variants from Griffin (arXiv:2307.16892): https://arxiv.org/abs/2307.16892
- Full electron-phonon coupling λ for Pb(2) compound from Paudyal et al. (arXiv:2308.14294): https://arxiv.org/abs/2308.14294
- Quantum Espresso: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP efficiency library or similar): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax Pb₉Cu(PO₄)₆O₂ (Cu at Pb(2))
- Role: process
- Action: Starting from the unrelaxed structure from Griffin (arXiv:2307.16892), relax the crystal structure of Pb₉Cu(PO₄)₆O₂ with Cu substituted at the Pb(2) site using DFT (Quantum Espresso, PBE functional) without spin-orbit coupling and without Hubbard U. Converge forces to a strict threshold.
- Evidence: `/app/outputs/relaxed_pb2.xyz`

### Step 2: Relax Pb₉Cu(PO₄)₆X₂ (Cu at Pb(1)) for X=O and X=OH
- Role: process
- Action: For X=O and X=OH, take the unrelaxed structures from Griffin (arXiv:2307.16892) with Cu at Pb(1) and relax them using the same DFT settings as for Pb(2).
- Evidence: `/app/outputs/relaxed_pb1_o.xyz, relaxed_pb1_oh.xyz`

### Step 3: DFPT at Γ for Pb(2) compound – smearing scan
- Role: process
- Action: Using the relaxed Pb(2) structure, perform DFPT calculations at the Γ point with Quantum Espresso to compute the electron-phonon coupling λ_Γ as a function of electronic smearing. Sample a range of smearing values and record each smearing and the corresponding λ_Γ in a CSV file.
- Evidence: `/app/outputs/smearing_scan_pb2.csv`

### Step 4: Compute scaling factor f
- Role: process
- Action: From smearing_scan_pb2.csv, identify the λ_Γ at the smallest smearing value. Obtain the full electron-phonon coupling λ for Pb₉Cu(PO₄)₆O₂ (Cu at Pb(2)) from Paudyal et al. (arXiv:2308.14294). Compute f = λ_Γ / λ and save the factor as a single number.
- Evidence: `/app/outputs/scaling_factor.txt`

### Step 5: DFPT at Γ for Pb(1) compounds – smearing scans
- Role: process
- Action: For each X=O and X=OH, using the relaxed Pb(1) structures, perform DFPT calculations at the Γ point to compute λ_Γ as a function of electronic smearing (same range as for Pb(2)). Save a CSV file for each compound with columns smearing (Ry) and lambda_Gamma.
- Evidence: `/app/outputs/smearing_scan_pb1_o.csv, smearing_scan_pb1_oh.csv`

### Step 6: Extract λ_Γ at finest smearing and estimate λ
- Role: scored (load-bearing)
- Action: For X=O, load smearing_scan_pb1_o.csv; for X=OH, load smearing_scan_pb1_oh.csv. In each file, locate the row with the smallest smearing value and read its lambda_Gamma. Read the scaling factor f from scaling_factor.txt. Compute lambda = f * lambda_Gamma for each compound. Write a CSV file with columns: compound, lambda_Gamma, lambda. Two rows: one for O, one for OH.
- Output file: `/app/outputs/table_1.csv`
- Format: csv
- Contract: CSV with header: compound,lambda_Gamma,lambda. Each row contains the compound label (O or OH) and the corresponding floating-point values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_1.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_1.csv
- path: `/app/outputs/table_1.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of Γ-point electron-phonon coupling λ_Γ and estimated total electron-phonon coupling λ for Pb₉Cu(PO₄)₆X₂ with X=O, O, Cu at Pb(1). The λ values are derived using the scaling factor f computed from the Pb(2) compound. Values are at the finest electronic smearing used in the DFPT calculations.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `lambda_Gamma`, `lambda`
  - `units`:
    - `lambda_Gamma`: dimensionless
    - `lambda`: dimensionless

Notes: The scaling factor f is computed by the agent from a separate DFPT run on the Pb(2) compound and an external reference λ. The hidden checker will compare the reported λ_Γ and λ values against paper targets with tolerances to account for pseudopotential and code-version variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "lambda_Gamma",
          "lambda"
        ],
        "units": {
          "lambda_Gamma": "dimensionless",
          "lambda": "dimensionless"
        }
      },
      "description": "Table of Γ-point electron-phonon coupling λ_Γ and estimated total electron-phonon coupling λ for Pb₉Cu(PO₄)₆X₂ with X=O, O, Cu at Pb(1). The λ values are derived using the scaling factor f computed from the Pb(2) compound. Values are at the finest electronic smearing used in the DFPT calculations."
    }
  ],
  "notes": "The scaling factor f is computed by the agent from a separate DFPT run on the Pb(2) compound and an external reference λ. The hidden checker will compare the reported λ_Γ and λ values against paper targets with tolerances to account for pseudopotential and code-version variations."
}
```

## How you are scored
A hidden verifier will read your submitted scored artifact at /app/outputs/table_1.csv and compare the values of lambda_Gamma and lambda for each compound against reference values derived from the peer-reviewed study. The verifier will assign a reward in [0,1] based on how accurately your computed values match the reference, with tolerances that account for legitimate differences arising from pseudopotential choice and code version. Only the values in table_1.csv are scored; intermediate output files (relaxed structures, smearing scans, scaling factor file) are required as process evidence but do not directly affect the reward. A correct reproduction that falls within the expected tolerances will receive full credit; systematic deviations reduce the score.
