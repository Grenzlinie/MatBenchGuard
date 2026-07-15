# Defect density scaling in a-Se and a-Si from bond constraint theory and divacancy model

## Problem background
In covalently-bonded amorphous semiconductor thin films, the densities of intrinsic dangling-bond defects can be understood through bond constraint theory. A key metric is the average coordination number N_av, which determines the number of bond-stretching and bond-bending constraints per atom. For an ideal continuous random network, N_av* = 2.4 and the defect density is minimal. In over-constrained networks (N_av > 2.4) the defect density has been observed to scale quadratically with the deviation from 2.4. This task addresses whether the same scaling relationship can also describe under-constrained materials like amorphous selenium (a-Se) with N_av ≈ 2.2, and whether it can explain the much higher defect density in amorphous silicon (a-Si) by incorporating a divacancy model that accounts for the ~6% density deficit typical of evaporated a-Si films.

## Approach
Use the semi-empirical scaling law D = D0 + D1 × (N_av − 2.4)^2 with the empirical constants D0 ≈ 1×10^16 cm⁻³ and D1 ≈ 6×10^17 cm⁻³. For a-Se, take the experimental average coordination N_av = 2.2 and directly compute the defect density D. For a-Si, model the ~6% density deficit as being accommodated by divacancies. Each divacancy (removal of two Si atoms) produces six threefold-coordinated Si atoms (effective coordination 3) and distorts the bonding of 18 neighbouring Si atoms, giving them an effective coordination of about 3.4. From the atomic density of crystalline Si (≈5.0×10^22 atoms/cm³), calculate the divacancy concentration implied by the 6% deficit. Then compute the overall average coordination N_av for the divacancy-affected region by weighting the contributions of the threefold sites, the affected neighbours, and the unchanged 4-fold bulk atoms. Finally, substitute that N_av into the same scaling law to obtain the dangling-bond defect density for a-Si. The computation is elementary arithmetic and does not require any external software beyond a basic scripting language.

## Reproduction target
Compute the dangling-bond defect density for amorphous selenium (a-Se) and for amorphous silicon (a-Si) using the bond constraint theory scaling law and the divacancy model. For a-Si, also determine the effective average coordination number N_av of the divacancy-affected region. Write the three results to a JSON file with keys "a_Se_D" (cm⁻³), "a_Si_N_av" (dimensionless), and "a_Si_D" (cm⁻³).

## Assets

- Silicon atomic density
- Average coordination N_av for a-Se

## Workflow steps

### Step 1: Compute defect densities for a-Se and a-Si and write JSON output
- Role: scored (load-bearing)
- Action: Implement the defect scaling relationship D = 1×10^16 + 6×10^17 × (N_av − 2.4)^2 cm⁻³. For a-Se, use N_av = 2.2 and compute the dangling-bond defect density D_aSe. For a-Si, model the 6% density deficit as divacancies: each divacancy (removal of 2 Si atoms) creates six threefold-coordinated Si atoms and breaks bending constraints on 18 neighboring atoms. Using the atomic density of Si (≈5.0×10^22 atoms/cm³), compute the concentration of divacancies from the deficit, count the threefold sites (effective coordination 3) and affected neighbors (effective coordination 3.4), average over all affected atoms including the remaining bulk 4‑fold Si atoms to obtain the average coordination N_av for the divacancy‑affected region, and then compute the dangling‑bond defect density D_aSi using the same scaling relation with that N_av. Write a JSON file with keys a_Se_D, a_Si_N_av, a_Si_D corresponding to D_aSe (cm⁻³), the average coordination, and D_aSi (cm⁻³).
- Output file: `/app/outputs/defect_densities.json`
- Format: json
- Contract: object with keys a_Se_D (float, units cm^-3), a_Si_N_av (float), a_Si_D (float, units cm^-3)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_densities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_densities.json
- path: `/app/outputs/defect_densities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The agent's computed dangling-bond defect density for a-Se, average coordination for the a-Si divacancy region, and dangling-bond defect density for a-Si. The checker compares these three numbers to the paper's reported values within hidden absolute tolerances.
- schema:
  - `type`: object
  - `required`:
    - `a_Se_D`: float (cm^-3)
    - `a_Si_N_av`: float
    - `a_Si_D`: float (cm^-3)
  - `items`: object

Notes: The agent must derive the three quantities from the public empirical constants and the divacancy counting procedure described in the step action. No external data files need to be downloaded; the constants (D0, D1, Nav*, Nav_aSe, Si atomic density) are either standard physical values or publicly reported in the literature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_densities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a_Se_D": "float (cm^-3)",
          "a_Si_N_av": "float",
          "a_Si_D": "float (cm^-3)"
        },
        "items": {}
      },
      "description": "The agent's computed dangling-bond defect density for a-Se, average coordination for the a-Si divacancy region, and dangling-bond defect density for a-Si. The checker compares these three numbers to the paper's reported values within hidden absolute tolerances."
    }
  ],
  "notes": "The agent must derive the three quantities from the public empirical constants and the divacancy counting procedure described in the step action. No external data files need to be downloaded; the constants (D0, D1, Nav*, Nav_aSe, Si atomic density) are either standard physical values or publicly reported in the literature."
}
```

## How you are scored
A hidden verifier will read your output file `/app/outputs/defect_densities.json`. It extracts the three values you report for a_Se_D, a_Si_N_av, and a_Si_D, compares each against reference values using pre-set tolerances, and combines the per-key scores into an overall reward in the range [0, 1]. The tolerances are chosen to accept a correct re-implementation that may differ from the reference because of minor rounding or numerical choices, while rejecting grossly unreasonable values. The reward increases as the computed numbers approach the reference; exactly reporting the correct numbers (within tolerance) earns full credit. There is no separate qualitative assessment.
