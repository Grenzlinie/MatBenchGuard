# Quantitative COHP Bonding Analysis of a Perovskite-Like Boride

## Problem background
Intermetallic borides with perovskite-derived structures can adopt complex superstructures involving ordered vacancies and cluster formation. The compound Zr₂Ir₆B is a double perovskite variant that contains both empty Ir₆ clusters and boron-filled BIr₆ octahedra within its unit cell. To rationalise the structural stability and bonding, a quantitative analysis of the interatomic interactions is needed. Crystal orbital Hamilton population (COHP) analysis provides an energy-resolved partitioning of band-structure energies into pairwise orbital interactions, allowing the strengths of different chemical bonds to be assessed. This task computes integrated COHP (ICOHP) values for the distinct interatomic contacts in Zr₂Ir₆B to quantify their relative contributions.

## Approach
The bonding analysis is performed in two stages. First, a self-consistent density‑functional theory (DFT) calculation is carried out on the full crystal structure of Zr₂Ir₆B, using an appropriate exchange‑correlation functional and pseudopotentials. The structure is defined by the space group, lattice parameter, and fractional coordinates reported for this phase. From this calculation, the ground‑state charge density and Kohn‑Sham wavefunctions are obtained. Second, the wavefunction information is fed into a COHP post‑processing tool that projects the plane‑wave basis onto a local atomic‑orbital basis to compute the pairwise COHP curves. Integrating each curve up to the Fermi level yields the ICOHP value (eV per bond) for each bond type. The analysis focuses on four distinct contacts present in the crystal: B–Ir, Zr–Ir, the shorter Ir–Ir contacts within the empty Ir₆ cluster, and the longer Ir–Ir contacts within the BIr₆ octahedron. Open‑source DFT codes and COHP analysis packages (e.g., Quantum ESPRESSO and LOBSTER) can be employed to reproduce this procedure.

## Reproduction target
Produce a JSON file containing the four ICOHP values (in eV per bond, with negative sign for bonding) for the following interatomic contacts in Zr₂Ir₆B:
- B–Ir
- Zr–Ir
- Ir–Ir in the empty Ir₆ cluster
- Ir–Ir in the BIr₆ octahedron

The values must be computed from a self‑consistent DFT calculation followed by COHP integration. The output must follow the schema defined in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LOBSTER: https://www.cohp.de/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT electronic structure calculation
- Role: process
- Action: Perform a self-consistent DFT calculation (e.g., using Quantum ESPRESSO) on the crystal structure of Zr2Ir6B (space group Fm-3m, a = 7.9903 Å; Zr at 8c (1/4,1/4,1/4), Ir at 24e (0.25526,0,0), B at 4b (0,0,0)) to obtain ground-state charge density and Kohn-Sham wavefunctions.
- Evidence: none

### Step 2: COHP bonding analysis and ICOHP extraction
- Role: scored (load-bearing)
- Action: Using the electronic structure from the DFT calculation, compute crystal orbital Hamilton populations (COHP) via LOBSTER. Integrate COHP curves up to the Fermi level to obtain ICOHP values for B–Ir, Zr–Ir, Ir–Ir (empty Ir6 cluster), and Ir–Ir (BIr6 octahedron).
- Output file: `/app/outputs/step_02_ICOHP_values.json`
- Format: json
- Contract: Object with keys: B_Ir_ICOHP (float), Zr_Ir_ICOHP (float), Ir_Ir_empty_ICOHP (float), Ir_Ir_filled_ICOHP (float). All values in eV per bond, negative for bonding.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_ICOHP_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_ICOHP_values.json
- path: `/app/outputs/step_02_ICOHP_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed integrated crystal orbital Hamilton population (ICOHP) values for the four distinct interatomic contacts in Zr2Ir6B. All values are in eV per bond with negative sign indicating bonding.
- schema:
  - `type`: object
  - `required`: `B_Ir_ICOHP`, `Zr_Ir_ICOHP`, `Ir_Ir_empty_ICOHP`, `Ir_Ir_filled_ICOHP`
  - `properties`:
    - `B_Ir_ICOHP`:
      - `type`: number
      - `description`: ICOHP for B–Ir bond (eV per bond, negative for bonding)
    - `Zr_Ir_ICOHP`:
      - `type`: number
      - `description`: ICOHP for Zr–Ir bond (eV per bond, negative for bonding)
    - `Ir_Ir_empty_ICOHP`:
      - `type`: number
      - `description`: ICOHP for Ir–Ir contact in empty Ir6 cluster (eV per bond, negative for bonding)
    - `Ir_Ir_filled_ICOHP`:
      - `type`: number
      - `description`: ICOHP for Ir–Ir contact in BIr6 octahedron (eV per bond, negative for bonding)

Notes: The hidden checker compares the computed ICOHP values to reference values from the paper's Table 3 with an absolute tolerance that absorbs method-dependent spread. The full DFT+COHP pipeline must be executed to obtain correct results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_ICOHP_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "B_Ir_ICOHP",
          "Zr_Ir_ICOHP",
          "Ir_Ir_empty_ICOHP",
          "Ir_Ir_filled_ICOHP"
        ],
        "properties": {
          "B_Ir_ICOHP": {
            "type": "number",
            "description": "ICOHP for B–Ir bond (eV per bond, negative for bonding)"
          },
          "Zr_Ir_ICOHP": {
            "type": "number",
            "description": "ICOHP for Zr–Ir bond (eV per bond, negative for bonding)"
          },
          "Ir_Ir_empty_ICOHP": {
            "type": "number",
            "description": "ICOHP for Ir–Ir contact in empty Ir6 cluster (eV per bond, negative for bonding)"
          },
          "Ir_Ir_filled_ICOHP": {
            "type": "number",
            "description": "ICOHP for Ir–Ir contact in BIr6 octahedron (eV per bond, negative for bonding)"
          }
        }
      },
      "description": "Computed integrated crystal orbital Hamilton population (ICOHP) values for the four distinct interatomic contacts in Zr2Ir6B. All values are in eV per bond with negative sign indicating bonding."
    }
  ],
  "notes": "The hidden checker compares the computed ICOHP values to reference values from the paper's Table 3 with an absolute tolerance that absorbs method-dependent spread. The full DFT+COHP pipeline must be executed to obtain correct results."
}
```

## How you are scored
Your submitted ICOHP values will be evaluated by a hidden verifier against a confidential reference. The verifier compares each of the four values to the reference with an appropriate tolerance, and also verifies the relative ordering of the bond strengths (i.e., which bond type is strongest, second strongest, and so on). The final reward is a single float between 0 and 1, reflecting both the accuracy of the individual values and the correctness of the ordering. Simply reporting numbers without executing the required DFT‑COHP pipeline will not earn credit; the verifier expects results that are consistent with an honest re‑computation of the electronic structure.
