# Extended Hückel energy differences for Rh(I)(CO)2 coordination on oxide model surfaces

## Problem background
Oxide-supported Rh(I)(CO)2 species are important in heterogeneous catalysis. EXAFS experiments have suggested a five-coordinate Rh(I) center bound to three surface oxygens on alumina, contrasting with the usual square-planar four-coordinate geometry of molecular Rh(I) complexes. This problem investigates which coordination geometry is more stable for Rh(I)(CO)2 bound to oxide models of silica and alumina.

## Approach
We use extended Hückel molecular orbital theory. Four oxyanion models are constructed as idealized supports: tetrahedral Si (model I), tetrahedral Al (II), octahedral Si (III), and octahedral Al (IV). Each model has three surface oxygens forming a trigonal face, with the remaining oxygens terminated by pseudoatoms L (a single 1s orbital). For each model, two binding geometries are evaluated: the Rh(I)(CO)2 fragment bound to two surface oxygens (2-O coordination) and bound to all three (3-O coordination). Total electronic energies are computed for all eight configurations and the energy difference ΔE = E(3-O) – E(2-O) is obtained for each model to assess relative stability.

## Reproduction target
Compute the energy differences for all four oxyanion models using extended Hückel calculations and write them to `/app/outputs/energy_differences.json`. The file must be a JSON array of objects, each with fields: `model` (string: `'I'`,`'II'`,`'III'`,`'IV'`), `delta_E` (float, eV), `E_2O` (float, eV), `E_3O` (float, eV), where `delta_E = E_3O - E_2O`. Report the values obtained from your calculations.

## Assets

- YAeHMOP (or any open-source extended Hückel molecular orbital program): http://yaehmop.sourceforge.net/
- Extended Hückel parameters for Rh, C, O, Si, Al, H (from Summerville and Hoffmann, JACS 1976): 10.1021/ja00438a048
- Crystal structure of Rh2(CO)4Cl2 (Dahl et al., JACS 1961): 10.1021/ja01444a011

## Workflow steps

### Step 1: Construct oxyanion models
- Role: process
- Action: Build the four oxyanion model structures (I–IV): tetrahedral Si (I), tetrahedral Al (II), octahedral Si (III), octahedral Al (IV). Each model has three surface oxygens forming a trigonal face, with the remaining oxygens (one for tetrahedral, three for octahedral) terminated by pseudoatoms L (1s orbital only, ionization energy –13.6 eV). Use idealized tetrahedral/octahedral bond angles and bond lengths: Si–O = 1.60 Å, Al–O = 1.82 Å, O–L = 0.96 Å.
- Evidence: `/app/outputs/models_structure.txt`

### Step 2: Generate 2-O and 3-O coordination geometries
- Role: process
- Action: For each model (I–IV), create the Rh(I)(CO)2 fragment in the 2-O coordination (Rh bonded to two surface oxygens, C2v symmetry) and in the 3-O coordination (Rh bonded to all three surface oxygens, Cs symmetry). Use fixed Rh–O = 2.12 Å, OC–Rh–CO angle = 90°, and Rh–CO internal bond distances from the crystal structure of Rh2(CO)4Cl2. The plane of the Rh(CO)2 fragment must be perpendicular to the trigonal plane of the surface oxygens.
- Evidence: `/app/outputs/coordinations.txt`

### Step 3: Run extended Hückel calculations
- Role: process
- Action: Using an open-source extended Hückel molecular orbital program (e.g., YAeHMOP), compute molecular orbitals and total electronic energies for all eight configurations: I‑2O, I‑3O, II‑2O, II‑3O, III‑2O, III‑3O, IV‑2O, IV‑3O. Use the extended Hückel parameters for Rh, C, O, Si, Al, and H from Summerville & Hoffmann (1976). Treat the pseudoatom L as a hydrogen atom with ionization energy –13.6 eV. Record the total electronic energy for each configuration.
- Evidence: `/app/outputs/energies.txt`

### Step 4: Compute and report energy differences
- Role: scored (load-bearing)
- Action: From the total energies obtained in step 3, calculate ΔE = E(3‑O) – E(2‑O) for each model. Write a JSON file `energy_differences.json` containing the results.
- Output file: `/app/outputs/energy_differences.json`
- Format: json
- Contract: A JSON array of objects. Each object has fields: model (string: 'I','II','III','IV'), delta_E (float, eV), E_2O (float, eV), E_3O (float, eV). delta_E = E_3O - E_2O.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_differences.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_differences.json
- path: `/app/outputs/energy_differences.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Energy differences between 3-O and 2-O coordinations for the four oxyanion models (I, II, III, IV). The checker verifies that delta_E > 0 for every model and that the values are consistent with the paper within tolerance (threshold_or_better). Also checks structural trend: tetrahedral models (I,II) have larger delta_E than octahedral models (III,IV).
- schema:
  - `type`: array
  - `items`:
    - `model`: string
    - `delta_E`:
      - `type`: number
      - `unit`: eV
    - `E_2O`:
      - `type`: number
      - `unit`: eV
    - `E_3O`:
      - `type`: number
      - `unit`: eV
  - `required_fields`: `model`, `delta_E`, `E_2O`, `E_3O`

Notes: The intermediate pathway geometries (Walsh diagrams) and rotational barrier calculations are not required for scoring. Only the endpoint energy differences for the four models are scored. The agent must re-run the extended Hückel calculations; no pre-made output files are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "model": "string",
          "delta_E": {
            "type": "number",
            "unit": "eV"
          },
          "E_2O": {
            "type": "number",
            "unit": "eV"
          },
          "E_3O": {
            "type": "number",
            "unit": "eV"
          }
        },
        "required_fields": [
          "model",
          "delta_E",
          "E_2O",
          "E_3O"
        ]
      },
      "description": "Energy differences between 3-O and 2-O coordinations for the four oxyanion models (I, II, III, IV). The checker verifies that delta_E > 0 for every model and that the values are consistent with the paper within tolerance (threshold_or_better). Also checks structural trend: tetrahedral models (I,II) have larger delta_E than octahedral models (III,IV)."
    }
  ],
  "notes": "The intermediate pathway geometries (Walsh diagrams) and rotational barrier calculations are not required for scoring. Only the endpoint energy differences for the four models are scored. The agent must re-run the extended Hückel calculations; no pre-made output files are provided."
}
```

## How you are scored
A hidden verifier checks the output file. It verifies that the JSON structure matches the contract, that each `delta_E` is correctly derived from the provided `E_3O` and `E_2O`, and that the reported values agree with a hidden reference within tolerance. Additional structural consistency checks are performed. Each required output contributes to a weighted score; accurate reproduction yields maximum reward.
