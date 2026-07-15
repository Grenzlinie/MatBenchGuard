# Hückel-type electron counting model for valence structure prediction of even carbon chain bridged metal complexes

## Problem background
Organometallic complexes where two transition-metal fragments are bridged by an even-numbered linear carbon chain, M–C_x–M, can adopt three different valence structures depending on the metal's d-electron count, the chain length, and the nature of the supporting ligands. The three structures are:
- Polyyne-like **A**: `M(–C≡C–)_{x/2}M` (alternating single and triple bonds)
- Cumulene-like **B**: `M(=C=C=)_{x/2}M` (all double bonds)
- Polyyne-like **C**: `M(≡C–C≡)_{x/2}M` (alternating triple and single bonds)

A simple Hückel-type molecular orbital model was proposed to predict which structure is expected from the electron count in the frontier π and δ orbitals. The model uses only the d^n configuration of the metal fragments, the even chain length x (2–8), and whether strong σ-donor ligands are present, making it a purely deterministic prediction. In this task you will implement that electron-counting scheme to assign the valence structure to a set of provided test cases.

## Approach
Implement a Hückel-type electron-counting algorithm that, for a given metal fragment d^n configuration (n = 5, 6, 7), even chain length x (x = 4 or 6), and a boolean flag indicating whether strong σ-donor ligands are present (`strong_sigma_donor` = true), decides the highest occupied molecular orbital (HOMO) and its electron occupancy, from which the valence structure follows. The core rules are:

1. **Total π/δ electrons**: `N_e = 2(n−1) + 2x`. One electron from each metal fragment is consumed in the M–C σ bond; each carbon atom contributes one p_π electron. The remaining electrons fill the π and δ frontier orbitals.

2. **Orbital ordering without strong σ-donors** (`strong_sigma_donor = false`): the dδ orbitals lie *below* the `(x/2+2)π` orbital. Occupancy of that `(x/2+2)π` orbital determines the structure:
   - `d^7`: the orbital is fully occupied → structure **A**.
   - `d^6`: the orbital is half-filled → structure **B**.
   - `d^5`: the orbital is empty; the HOMO is `(x/2+1)π` → structure **C**.

3. **Orbital ordering with strong σ-donors** (`strong_sigma_donor = true`): the dδ orbitals are destabilised and lie *above* the π set. The `(x/2+2)π` orbital is always fully occupied regardless of d^n, giving structure **A** for all d^n. For `d^6`, this configuration yields an open‑shell diradical; in that case record a radical note `"diradical"`; otherwise the note is an empty string.

Apply these rules to each test case and produce a JSON file containing the predicted structure and optional radical note.

## Reproduction target
Apply the model to the following test cases (d_n, x, strong_sigma_donor):
- (5, 4, false)
- (6, 4, false)
- (7, 4, false)
- (6, 4, true)
- (5, 6, false)
- (6, 6, false)
- (7, 6, false)
- (6, 6, true)

For each case, compute the predicted valence structure as one of the strings `"A"`, `"B"`, `"C"`, and set `radical_note` to `"diradical"` only for the d^6 strong‑donor case; otherwise use an empty string `""`. Write the predictions as a JSON file `/app/outputs/predictions.json` containing an array of objects, each with the keys `d_n` (integer), `x` (integer), `strong_sigma_donor` (boolean), `predicted_structure` (string), and `radical_note` (string).

## Assets

- Python 3 interpreter: python3

## Workflow steps

### Step 1: Predict Valence Structures
- Role: scored (load-bearing)
- Action: Implement the Hückel-type electron-counting rules that predict the valence structure (A, B, or C) of even carbon-chain bridged M-C_x-M complexes based on the metal fragment d^n configuration, chain length x, and the presence of strong σ-donor ligands. For each given test case (d_n, x, strong_sigma_donor), compute the predicted_structure and an optional radical_note (if any). Write the results to predictions.json.
- Output file: `/app/outputs/predictions.json`
- Format: json
- Contract: [{"d_n": int, "x": int, "strong_sigma_donor": bool, "predicted_structure": "A"|"B"|"C", "radical_note": ""}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.json
- path: `/app/outputs/predictions.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Array of objects, each giving the predicted valence structure and, if applicable, a radical note for one test case.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `d_n`, `x`, `strong_sigma_donor`, `predicted_structure`, `radical_note`
    - `properties`:
      - `d_n`:
        - `type`: integer
      - `x`:
        - `type`: integer
      - `strong_sigma_donor`:
        - `type`: boolean
      - `predicted_structure`:
        - `type`: string
        - `enum`: `A`, `B`, `C`
      - `radical_note`:
        - `type`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "d_n",
            "x",
            "strong_sigma_donor",
            "predicted_structure",
            "radical_note"
          ],
          "properties": {
            "d_n": {
              "type": "integer"
            },
            "x": {
              "type": "integer"
            },
            "strong_sigma_donor": {
              "type": "boolean"
            },
            "predicted_structure": {
              "type": "string",
              "enum": [
                "A",
                "B",
                "C"
              ]
            },
            "radical_note": {
              "type": "string"
            }
          }
        }
      },
      "description": "Array of objects, each giving the predicted valence structure and, if applicable, a radical note for one test case."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently implements the same Hückel electron‑counting rules described above. For each test case the verifier computes the correct `predicted_structure` and `radical_note` and compares them to your submitted entries. Both fields must match *exactly* (string equality). A case that matches exactly earns 1 point; a case that fails to match earns 0. Your final score is the fraction of correctly predicted cases (a number between 0 and 1). The verifier’s expected values are derived solely from the model rules; no external data or experimental measurements are used.
