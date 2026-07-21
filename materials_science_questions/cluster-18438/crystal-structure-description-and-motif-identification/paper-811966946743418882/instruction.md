# Crystal Structure Anion Geometry and Conformation Analysis

## Problem background
Certain thiophosphate compounds crystallise with discrete molecular anions whose conformation influences the overall structure. The compound is reported to contain P2S6^4- anions, NH4+ cations, and water molecules. Your task is to determine from the provided coordinates whether these anions are isolated, whether their geometry is ethane-like, and what conformation they adopt. This task asks you to take the provided fractional atomic coordinates and unit cell parameters and to determine the anion's identity, geometry, and conformational state through a computational geometric analysis.

## Approach
The analysis follows crystallographic distance-geometry principles. From the fractional coordinates and cell parameters, interatomic distances are computed for all atom pairs. P–S bonds are identified using a plausible bond-length window (e.g., 1.9–2.3 Å), which allows the P2S6^4- unit to be located. The unit is considered isolated when no sulfur atom of one anion lies within bonding distance of a sulfur atom from another anion. An ethane-like geometry is verified by confirming that the two phosphorus atoms are directly bonded and that each phosphorus is bonded to exactly three sulfur atoms. The torsion (dihedral) angles defined by the P–P–S planes are then calculated, and their average is used to classify the conformation as 'staggered' when the mean is near 60°, or as 'eclipsed' otherwise.

## Reproduction target
Using the atomic coordinates and cell parameters supplied in the instructions, produce a JSON file (`analysis_results.json`) that reports:
- the number of distinct P2S6^4- units found
- whether those units are isolated from each other
- whether the geometry is consistent with an ethane-like description
- the list of computed P–P–S–S torsion angles (in degrees)
- a conformation label ('staggered' or 'eclipsed').
This file is the sole scored artifact of the task.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Analyze P2S6^4- Anion Geometry
- Role: scored (load-bearing)
- Action: Read the provided fractional atomic coordinates and unit cell parameters from the instruction. Compute interatomic distances to identify P-S bonds (typical length range 1.9–2.3 Å) and locate the discrete P2S6^4- anion unit. Verify the unit is isolated (no bonds between sulfur atoms of different anions). Determine whether the geometry is ethane-like by checking that the two P atoms are directly bonded and each is bonded to three S atoms. Compute the P-P-S-S torsion angles (dihedral angles). Derive the average torsion angle and classify the conformation as 'staggered' if the average is near 60°, otherwise 'eclipsed'. Write the results to analysis_results.json.
- Output file: `/app/outputs/analysis_results.json`
- Format: json
- Contract: {"p2_s6_units": "integer", "isolated": "boolean", "ethane_like": "boolean", "torsion_angles": "[float] (degrees)", "conformation": "string"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/analysis_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### analysis_results.json
- path: `/app/outputs/analysis_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains the number of P2S6^4- units, whether they are isolated and ethane-like, the computed torsion angles in degrees, and the conformation classification ('staggered' or 'eclipsed'). The checker will verify the torsion angles meet the expected staggered threshold and the structural flags match the expected values.
- schema:
  - `type`: object
  - `required`:
    - `p2_s6_units`: integer
    - `isolated`: boolean
    - `ethane_like`: boolean
    - `torsion_angles`: array of float (degrees)
    - `conformation`: string

Notes: The atomic coordinates and cell parameters are provided in the instruction. The main scored quantity is the torsion angles; the other fields (count, flags, label) are exact deterministic outcomes from the correct analysis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "analysis_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "p2_s6_units": "integer",
          "isolated": "boolean",
          "ethane_like": "boolean",
          "torsion_angles": "array of float (degrees)",
          "conformation": "string"
        }
      },
      "description": "Contains the number of P2S6^4- units, whether they are isolated and ethane-like, the computed torsion angles in degrees, and the conformation classification ('staggered' or 'eclipsed'). The checker will verify the torsion angles meet the expected staggered threshold and the structural flags match the expected values."
    }
  ],
  "notes": "The atomic coordinates and cell parameters are provided in the instruction. The main scored quantity is the torsion angles; the other fields (count, flags, label) are exact deterministic outcomes from the correct analysis."
}
```

## How you are scored
Your submission is evaluated by a hidden, automated verifier that reads `analysis_results.json`. The verifier checks the structural flags (presence of one unit, isolation, ethane-like geometry) and compares the reported torsion angles to reference values within established tolerances. The torsion angles carry the highest weight because they directly quantify the conformation. Each field contributes to the overall reward; fabricating a plausible number is insufficient, as the verifier performs a detailed numerical comparison.
