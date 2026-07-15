# Lattice Energies of Ice VIII Polarity Models

## Problem background
Ice VIII is the ordered low-temperature form of ice VII, consisting of two interpenetrating hydrogen-bond networks. The relative polarity of these two networks is not known experimentally but is expected to have a strong effect on the lattice energy. Three ordered models can be proposed: parallel polarity (VIII_p), opposed polarity (VIII_o), and mutually perpendicular polarity (VIII_mp). Determining the lattice energy of each model reveals which polarity arrangements are energetically plausible and consistent with the stability of ice VIII.

## Approach
Use the ST2 water model (Stillinger & Rahman, 1974), which represents each water molecule as a rigid four-point model with Lennard‑Jones 6‑12 interactions between oxygen atoms and electrostatic interactions among all charge sites, modified by a switching function to avoid close-contact singularities. Construct three ordered ice VIII models in space group I4₁/amd. Take oxygen positions from the experimental crystal structure (Kamb & Davis, 1964). Assign hydrogen positions for each of the two interpenetrating ice Ic networks according to the ordered proton arrangement (Shimaoka, 1960). Set the relative polarities of the two networks: parallel, opposed, and mutually perpendicular. For each model, compute the lattice energy by summing all pairwise interactions within a convergent scheme (e.g., Ewald summation or a direct summation with convergence), and then minimize the total energy with respect to the tetragonal cell parameters and molecular orientations while keeping the oxygen atoms fixed at the experimental positions. Report the minimized lattice energy for each model in kJ mol⁻¹.

## Reproduction target
Compute and report the lattice energies (kJ mol⁻¹) for three ordered ice VIII polarity models: parallel (VIII_p), opposed (VIII_o), and mutually perpendicular (VIII_mp). Use the ST2 water model and lattice energy minimization as described, with oxygen positions from Kamb & Davis (1964) and hydrogen ordering from Shimaoka (1960). Provide the final minimized energies in the file `ice_VIII_energies.json`.

## Assets

- ST2 potential model (Stillinger & Rahman, 1974): https://doi.org/10.1063/1.1681294
- Ice VIII oxygen positions (Kamb & Davis, 1964): https://doi.org/10.1073/pnas.52.6.1433
- Ordered Ice Ic hydrogen model (Shimaoka, 1960): https://doi.org/10.1143/JPSJ.15.106

## Workflow steps

### Step 1: Construct Ice VIII Polarity Models
- Role: process
- Action: Construct three ordered hydrogen-bond models for ice VIII (space group I4₁/amd) using the oxygen positions from Kamb & Davis (1964) and hydrogen ordering from Shimaoka (1960) for each of the two interpenetrating ice Ic networks. Assign relative polarities: parallel (VIII_p), opposed (VIII_o), and mutually perpendicular (VIII_mp). Output the three structural models.
- Evidence: `/app/outputs/ice_VIII_models.xyz`

### Step 2: Compute Lattice Energies
- Role: scored (load-bearing)
- Action: Implement the ST2 water model including Lennard‑Jones 6‑12 and electrostatic interactions with switching function. For each ice VIII model, compute the lattice energy using a convergent summation method, then minimize the total energy with respect to the tetragonal cell parameters and molecular orientations while keeping oxygen positions fixed at the experimental sites. Report the final minimized lattice energy (kJ mol⁻¹) for each polarity model.
- Output file: `/app/outputs/ice_VIII_energies.json`
- Format: json
- Contract: {"type": "object", "properties": {"VIII_p": {"type": "number", "unit": "kJ/mol"}, "VIII_o": {"type": "number", "unit": "kJ/mol"}, "VIII_mp": {"type": "number", "unit": "kJ/mol"}}, "required": ["VIII_p", "VIII_o", "VIII_mp"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ice_VIII_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ice_VIII_energies.json
- path: `/app/outputs/ice_VIII_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice energies of ice VIII models with parallel, opposed, and mutually perpendicular polarities. Both the reported energy values and their relative ordering are evaluated.
- schema:
  - `type`: object
  - `required`:
    - `VIII_p`: number (kJ/mol)
    - `VIII_o`: number (kJ/mol)
    - `VIII_mp`: number (kJ/mol)
  - `items`: object
  - `units`: object

Notes: The lattice energies are compared to a hidden reference; absolute values within tolerance and the correct ordering (parallel > perpendicular > opposed) are both required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ice_VIII_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "VIII_p": "number (kJ/mol)",
          "VIII_o": "number (kJ/mol)",
          "VIII_mp": "number (kJ/mol)"
        },
        "items": {},
        "units": {}
      },
      "description": "Lattice energies of ice VIII models with parallel, opposed, and mutually perpendicular polarities. Both the reported energy values and their relative ordering are evaluated."
    }
  ],
  "notes": "The lattice energies are compared to a hidden reference; absolute values within tolerance and the correct ordering (parallel > perpendicular > opposed) are both required."
}
```

## How you are scored
A hidden verifier reads your submitted `ice_VIII_energies.json` and evaluates it against a hidden reference. Both the absolute lattice energy values and the relative ordering of the three models (VIII_p, VIII_o, VIII_mp) are checked. Scoring combines agreement with the reference energies and satisfaction of the physically expected ordering trend. No further hints about the target values or tolerances are given; execute the workflow as faithfully as possible.
