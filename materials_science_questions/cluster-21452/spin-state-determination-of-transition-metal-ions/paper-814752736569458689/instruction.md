# Crystal-field parameter extraction from near-infrared absorption peaks of Co2+ in a defect chalcopyrite semiconductor

## Problem background
When a transition‑metal ion substitutes into a semiconductor host, the local arrangement of neighbouring atoms (the crystal field) splits the ion's d‑orbital energies. The resulting optical absorption peaks therefore encode the symmetry and strength of that field. This task reproduces a crystal‑field analysis for Co²⁺ (a d⁷ ion) in the defect‑chalcopyrite semiconductor CdGa₂Se₄. The room‑temperature near‑infrared absorption spectrum of the doped crystal shows six well‑resolved peaks that arise from d‑d transitions of Co²⁺ sitting at a site whose symmetry is reduced from perfect tetrahedral (T_d) to S₄. The challenge is to extract from those six transition energies the crystal‑field strength parameter Dq, the Racah B parameter (which describes inter‑electron repulsion), and the low‑symmetry splitting of the ⁴T₂(⁴F) level induced by the S₄ distortion.

## Approach
The analysis rests on crystal‑field theory for a d⁷ ion in a tetrahedral field. Tanabe–Sugano energy matrices map the transition energies to two key parameters, Dq and B. For the tetrahedral case the lowest‑energy excited term, ⁴T₂, is split directly by the crystal field, so Dq can be read from the energy of the ⁴A₂ → ⁴T₂ absorption. The Racah parameter B is then determined by fitting the higher‑energy transitions (to ⁴T₁(⁴F) and ⁴T₁(⁴P)) through the Tanabe–Sugano expressions. Because the actual site symmetry is S₄ rather than T_d, the ⁴T₂ state is further split into two components; the energy difference between the two lowest observed peaks gives the low‑symmetry splitting. The implementation must solve for Dq, B, and the ⁴T₂ splitting from the six input peak positions using these well‑established relations.

## Reproduction target
Use the six reported near‑infrared absorption peak positions measured at 292 K — 4132, 4332, 5970, 6329, 12903, and 13793 cm⁻¹ — to compute the crystal‑field parameter Dq (in cm⁻¹), the Racah B parameter (in cm⁻¹), and the low‑symmetry splitting of the ⁴T₂(⁴F) level (in cm⁻¹). Write the three values as a JSON object with keys "Dq", "B", and "low_symmetry_splitting_4T2" to the file fit_params.json.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Crystal-field parameter extraction for Co²⁺ in CdGa₂Se₄
- Role: scored (load-bearing)
- Action: Using the six reported near‑infrared absorption peak positions at 292 K (4132, 4332, 5970, 6329, 12903, 13793 cm⁻¹) as input, apply crystal‑field theory for d⁷ in a tetrahedral field reduced to S₄ symmetry. Determine the crystal‑field strength Dq (in cm⁻¹) from the lowest ⁴T₂ transition, the Racah parameter B (in cm⁻¹) from the Tanabe–Sugano relations for the higher lying transitions, and the low‑symmetry splitting of the ⁴T₂(⁴F) level (in cm⁻¹). Write the computed three values to fit_params.json.
- Output file: `/app/outputs/fit_params.json`
- Format: json
- Contract: { "type": "object", "required": { "Dq": "float (cm⁻¹)", "B": "float (cm⁻¹)", "low_symmetry_splitting_4T2": "float (cm⁻¹)" } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fit_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fit_params.json
- path: `/app/outputs/fit_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Crystal‑field strength Dq, Racah parameter B, and the low‑symmetry splitting of the ⁴T₂(⁴F) level, all in cm⁻¹. The hidden checker compares these values to the paper‑reported reference with generous tolerances for implementation differences.
- schema:
  - `type`: object
  - `required`:
    - `Dq`: float (cm⁻¹)
    - `B`: float (cm⁻¹)
    - `low_symmetry_splitting_4T2`: float (cm⁻¹)

Notes: The six peak positions used as input are stated directly in the agent's instruction and do not require parsing the paper. The solver is expected to implement standard crystal‑field theory for d⁷ in tetrahedral symmetry using Tanabe–Sugano relations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fit_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Dq": "float (cm⁻¹)",
          "B": "float (cm⁻¹)",
          "low_symmetry_splitting_4T2": "float (cm⁻¹)"
        }
      },
      "description": "Crystal‑field strength Dq, Racah parameter B, and the low‑symmetry splitting of the ⁴T₂(⁴F) level, all in cm⁻¹. The hidden checker compares these values to the paper‑reported reference with generous tolerances for implementation differences."
    }
  ],
  "notes": "The six peak positions used as input are stated directly in the agent's instruction and do not require parsing the paper. The solver is expected to implement standard crystal‑field theory for d⁷ in tetrahedral symmetry using Tanabe–Sugano relations."
}
```

## How you are scored
A hidden verifier independently implements the same crystal‑field analysis (d⁷ Tanabe–Sugano relations for a tetrahedral field reduced to S₄ symmetry) and recomputes Dq, B, and the low‑symmetry splitting from the same six peak positions provided in the instruction. Your output values are compared to the verifier‑recomputed reference values. The reward reflects the agreement, with generous tolerances that absorb legitimate differences due to implementation details (e.g. solving algorithm, floating‑point handling). Reporting a number without a correct derivation will not pass: the verifier checks that the values are produced by a faithful implementation of the required method, not by guesswork. The final reward combines the scores for each of the three parameters. The output file must be valid JSON with exactly the three required numeric fields.
