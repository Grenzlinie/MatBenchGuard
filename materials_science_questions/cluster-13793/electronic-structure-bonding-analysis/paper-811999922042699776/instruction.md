# Predicting Stable Composition of Half-Heusler Phases via Rigid-Band Analysis

## Problem background
Half-Heusler phases with general formula XYZ (AlLiSi-type, space group F-43m) are known to often deviate from the ideal 1:1:1 stoichiometry, exhibiting narrow composition ranges whose direction and extent are important for synthesis and property optimization. The valence electron content (VEC) is a key parameter. By analyzing the electronic band structure of the equiatomic compound using density functional theory (DFT) and the crystal orbital Hamilton population (COHP), one can identify whether the bonding states are optimally filled, or whether adding or removing electrons (rigid-band approximation) would improve stability. The degree of electron addition/removal determines the optimal VEC and the composition shift in the ternary phase diagram.

## Approach
For a given half-Heusler phase, compute the electronic structure of the equiatomic XYZ compound using a plane-wave DFT code (Quantum ESPRESSO) with appropriate pseudopotentials. Post-process the converged charge density with the LOBSTER code to obtain the density of states (DOS) and the COHP. From the COHP, locate the energy E_opt where the bonding states are maximally filled—typically where the COHP crosses from negative (bonding) to positive (antibonding) or at a gap. Integrate the DOS from the Fermi energy (E_F) to E_opt to obtain the number of electrons Δn that must be added (if E_opt > E_F) or removed (if E_opt < E_F) to achieve optimal bonding. The optimal valence-electron content per formula atom is VEC_st = VEC_eq + Δn / 3, where VEC_eq is the sum of the standard valence electrons of the constituent elements. Determine the direction of composition shift: 'increase' if Δn > 0, 'decrease' if Δn < 0, or 'none' if Δn ≈ 0. Repeat this procedure for each target phase.

## Reproduction target
Using the DFT+COHP+rigid-band procedure described above, compute VEC_st and the direction of composition shift for the following seven half-Heusler phases: NiTiSn, CoTiSb, PtMnSb, NiMnSb, CoMnSb, AuMnSn, and AuMnSb. Use the experimental lattice parameters (available from standard crystallographic databases) for each phase. Report the results in a CSV file at /app/outputs/predicted_VEC_st.csv with columns: phase, VEC_eq, VEC_st, direction. The verifier will compare your predictions to the expected literature values to assess agreement.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LOBSTER: https://www.cohp.de/
- SSSP/GBRV pseudopotentials: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: DFT and LOBSTER electronic structure calculation
- Role: process
- Action: For each of the seven half-Heusler phases (NiTiSn, CoTiSb, PtMnSb, NiMnSb, CoMnSb, AuMnSn, AuMnSb), set up the AlLiSi-type crystal structure (space group F-43m) using the experimental lattice parameter provided in the instruction. Perform a self-consistent DFT calculation with Quantum ESPRESSO and appropriate pseudopotentials. Then run LOBSTER on the converged charge density to generate the density of states (DOS) and the crystal orbital Hamilton population (COHP).
- Evidence: `/app/outputs/dft_summary.json`

### Step 2: Rigid-band analysis and prediction of VEC_st
- Role: scored (load-bearing)
- Action: For each phase, use the DOS and COHP obtained from the previous step. Identify the energy E_opt where bonding states are maximally filled (the energy beyond which further filling would populate antibonding states, indicated by COHP crossing from negative to positive or by a gap). Integrate the DOS from the Fermi level up to E_opt to obtain the number of electrons Δn added (if E_opt > E_F) or removed (if E_opt < E_F). Compute VEC_st = VEC_eq + Δn/3, where VEC_eq is the sum of the standard valence electrons of the constituent elements. Determine direction of shift: 'increase' (Δn > 0), 'decrease' (Δn < 0), or 'none' (Δn ≈ 0). Output all results in a CSV file.
- Output file: `/app/outputs/predicted_VEC_st.csv`
- Format: csv
- Contract: phase:string,VEC_eq:float,VEC_st:float,direction:string
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_VEC_st.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_VEC_st.csv
- path: `/app/outputs/predicted_VEC_st.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed optimal valence-electron content per formula atom and the predicted direction of composition shift relative to the equiatomic composition for each half-Heusler phase.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `VEC_eq`, `VEC_st`, `direction`
  - `description`: CSV with columns phase (string), VEC_eq (float), VEC_st (float), direction (string: 'increase', 'decrease', or 'none')

Notes: The checker will compare the reported VEC_st and direction to hidden paper reference values, with tolerances that accommodate different DFT implementations. The agent must execute the full DFT+COHP pipeline to produce this artifact; the reference values are not given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_VEC_st.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "VEC_eq",
          "VEC_st",
          "direction"
        ],
        "description": "CSV with columns phase (string), VEC_eq (float), VEC_st (float), direction (string: 'increase', 'decrease', or 'none')"
      },
      "description": "The computed optimal valence-electron content per formula atom and the predicted direction of composition shift relative to the equiatomic composition for each half-Heusler phase."
    }
  ],
  "notes": "The checker will compare the reported VEC_st and direction to hidden paper reference values, with tolerances that accommodate different DFT implementations. The agent must execute the full DFT+COHP pipeline to produce this artifact; the reference values are not given."
}
```

## How you are scored
A hidden verifier reads your predicted_VEC_st.csv and compares each phase’s computed VEC_st and direction against the expected results from the literature. The comparison uses tolerances that accommodate differences between DFT codes and functionals; you are not expected to exactly match a particular numerical value. The reward is the fraction of the seven phases whose predictions meet the acceptance criteria (typically correct direction and VEC_st within a fixed tolerance).
