# DFT Study of Ethane Reaction Barriers on an Acidic Zeolite Cluster

## Problem background
Zeolite catalysts are crucial for the conversion of hydrocarbons. A key step in many such processes is the activation of C–H and C–C bonds by the acidic Brønsted protons of the zeolite framework. Density functional theory (DFT) calculations on a finite cluster model can provide quantitative activation barriers for elementary reactions such as hydrogen exchange, cracking, dehydrogenation, and hydride transfer. This task reproduces the computation of those barriers on a protonated zeolite cluster model, with the aim of revealing the relative energetics of competing bond activation pathways.

## Approach
The active site is represented by the AlH cluster H3SiOAlH2OHSiH3, along with reactant molecules (ethane and methanol). Electronic structure calculations employ local density approximation (LDA) DFT with the DZVP basis set (double-zeta plus polarization). After geometry optimization of isolated reactants and of the bare cluster, transition state (TS) searches are carried out for each reaction. Saddle points are verified by the presence of exactly one imaginary frequency. To the final LDA-optimised structures, nonlocal Perdew–Becke exchange-correlation corrections are applied as energy corrections. Vibrational frequencies are computed to obtain zero-point energy (ZPE) corrections. Activation barriers are then computed as the difference between the total energy (including ZPE) of the TS and the sum of the isolated reactant energies, and reported in kJ/mol. The proprietary code originally used is replaced by an open‑source quantum chemistry package such as NWChem.

## Reproduction target
Compute and report the activation barriers (including ZPE corrections) for the following four processes on the AlH zeolite cluster:
1. Hydrogen exchange between ethane and the acidic cluster.
2. Direct cracking (path 1) of ethane, yielding methane and a surface methoxide.
3. Dehydrogenation of ethane, producing H₂ and a framework‑bound ethyl group.
4. Hydride transfer between methanol and the surface methoxide species.

The barriers (in kJ/mol) must be written to a JSON file.

## Assets

- DZVP basis set for H, C, O, Al, Si: https://www.basissetexchange.org
- NWChem quantum chemistry package: https://github.com/nwchemgit/nwchem

## Workflow steps

### Step 1: Construct initial molecular models
- Role: process
- Action: Build initial Cartesian coordinates for the AlH cluster (H3SiOAlH2OHSiH3), ethane, methanol, and the AlH methoxide surface (H3SiOAlH2OCH3SiH3).
- Evidence: none

### Step 2: Geometry optimization of isolated reactants and AlH cluster
- Role: process
- Action: Perform LDA/DZVP geometry optimization and vibrational frequency calculation for ethane, methanol, the AlH cluster, and the AlH methoxide surface. Apply nonlocal Perdew–Becke corrections to obtain total energies and zero‑point energy (ZPE) corrections.
- Evidence: none

### Step 3: Transition state search: hydrogen exchange
- Role: process
- Action: Search for the transition state of hydrogen exchange between ethane and the AlH cluster. Optimize to a saddle point, verify one imaginary frequency, and apply nonlocal Perdew–Becke corrections.
- Evidence: none

### Step 4: Transition state search: cracking
- Role: process
- Action: Search for the transition state of the direct cracking reaction (path 1) of ethane on the AlH cluster, yielding a methane molecule and a surface methoxide. Optimize to a saddle point, verify one imaginary frequency, and apply nonlocal Perdew–Becke corrections.
- Evidence: none

### Step 5: Transition state search: dehydrogenation
- Role: process
- Action: Search for the transition state of ethane dehydrogenation on the AlH cluster, leading to H₂ formation and a framework‑bound ethyl group. Optimize to a saddle point, verify one imaginary frequency, and apply nonlocal Perdew–Becke corrections.
- Evidence: none

### Step 6: Transition state search: hydride transfer
- Role: process
- Action: Search for the transition state of hydride transfer between methanol and the AlH methoxide surface. Optimize to a saddle point, verify one imaginary frequency, and apply nonlocal Perdew–Becke corrections.
- Evidence: none

### Step 7: Compute and report activation barriers
- Role: scored (load-bearing)
- Action: Calculate activation barriers in kJ/mol as E(TS) – E(reactants) including ZPE corrections from the energies obtained in previous steps. Write the barriers to a JSON file.
- Output file: `/app/outputs/activation_barriers.json`
- Format: json
- Contract: JSON object with keys: hydrogen_exchange, cracking, dehydrogenation, hydride_transfer. Each value is the barrier in kJ/mol (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_barriers.json
- path: `/app/outputs/activation_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed activation barriers for hydrogen exchange, cracking (path 1), dehydrogenation, and hydride transfer on the AlH zeolite cluster. Values in kJ/mol.
- schema:
  - `type`: object
  - `required`:
    - `hydrogen_exchange`: number
    - `cracking`: number
    - `dehydrogenation`: number
    - `hydride_transfer`: number
  - `description`: Activation barriers in kJ/mol (with ZPE)

Notes: The ordering hydrogen_exchange < hydride_transfer < cracking ≈ dehydrogenation is verified by the hidden checker, but not required to be stated in the output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hydrogen_exchange": "number",
          "cracking": "number",
          "dehydrogenation": "number",
          "hydride_transfer": "number"
        },
        "description": "Activation barriers in kJ/mol (with ZPE)"
      },
      "description": "Computed activation barriers for hydrogen exchange, cracking (path 1), dehydrogenation, and hydride transfer on the AlH zeolite cluster. Values in kJ/mol."
    }
  ],
  "notes": "The ordering hydrogen_exchange < hydride_transfer < cracking ≈ dehydrogenation is verified by the hidden checker, but not required to be stated in the output."
}
```

## How you are scored
A hidden verifier independently evaluates your submission. It compares each reported barrier to a reference value using a tolerance that accounts for legitimate computational variation, and it also examines the relative ordering of the four barriers. Each reaction contributes a weighted score; the final reward is a weighted sum in the range [0,1]. An accurate reproduction, where all barriers are within tolerance and the correct qualitative trends are captured, receives maximum credit. Errors that deviate significantly from the expected quantitative or qualitative pattern reduce the score.
