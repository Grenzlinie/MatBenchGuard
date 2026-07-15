# Cylindrical Ultrathin Copper Nanowire Structures

## Problem background
Ultrathin metallic nanowires exhibit novel multi-shell coaxial cylindrical structures with {111}-like surfaces, which are of fundamental interest for low-dimensional physics and potential molecular electronic devices. The structures that form for cylindrical copper nanowires under given confinement diameters are unknown—predicting the stable atomic arrangements and their shell radii is the target of this task.

## Approach
We simulate copper nanowires with an atomistic model using the second-moment approximation to tight binding (SMA-TB) potential, with parameters published by Cleri and Rosato. For each of several cylinder diameters, atoms are iteratively placed at the cylinder base and the configuration is relaxed by steepest descent until a stable multi-shell wire of ~40 Å length emerges. The radial boundary is reflective, the axial boundaries are free. From the relaxed coordinates, atoms are grouped into coaxial shells by their radial distances, and for each nanowire we extract the average shell radii and assign both the Kondo-Takayanagi (KT) index (counting helical rows per shell) and the Tosatti (T) index (orthogonal vectors per shell).

## Reproduction target
Reproduce the relaxed atomic structures of copper nanowires confined to cylindrical diameters of 4.0, 6.0, and 12.0 Å. For each diameter, perform the SMA-TB steepest descent simulation described above and output the relaxed atomic coordinates in XYZ format. Then compute, from those coordinates, the coaxial shell radii and assign the KT and T structural indices, and output a JSON summary. The XYZ files and the summary.json are the scored artifacts.

## Assets

- Cleri-Rosato SMA-TB potential parameters for copper: 10.1103/PhysRevB.48.22

## Workflow steps

### Step 1: Relaxed nanowire structure for Dc=4.0 Å
- Role: scored (load-bearing)
- Action: Simulate a Cu nanowire confined in a cylinder of 4.0 Å diameter using the SMA-TB potential and steepest descent relaxation; output relaxed atomic coordinates.
- Output file: `/app/outputs/structure_4.0.xyz`
- Format: txt
- Contract: Text file: first line = number of atoms, second line = comment, then one line per atom: 'Cu x y z' with coordinates in Ångströms, cylinder axis along z.
- Scoring: scored by hidden verifier

### Step 2: Relaxed nanowire structure for Dc=6.0 Å
- Role: scored (load-bearing)
- Action: Simulate a Cu nanowire confined in a cylinder of 6.0 Å diameter using the SMA-TB potential and steepest descent relaxation; output relaxed atomic coordinates.
- Output file: `/app/outputs/structure_6.0.xyz`
- Format: txt
- Contract: Same XYZ format as structure_4.0.xyz.
- Scoring: scored by hidden verifier

### Step 3: Relaxed nanowire structure for Dc=12.0 Å
- Role: scored (load-bearing)
- Action: Simulate a Cu nanowire confined in a cylinder of 12.0 Å diameter using the SMA-TB potential and steepest descent relaxation; output relaxed atomic coordinates.
- Output file: `/app/outputs/structure_12.0.xyz`
- Format: txt
- Contract: Same XYZ format as structure_4.0.xyz.
- Scoring: scored by hidden verifier

### Step 4: Extract structural indices and shell radii
- Role: scored
- Action: From the three XYZ files, compute radial distances of atoms from z-axis, cluster into coaxial shells based on radial gaps, calculate average shell radii, assign KT and T indices, and output a JSON summary.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys '4.0','6.0','12.0'. Each value is an object: { 'radii': [list of numbers, inner to outer, in Å], 'KT_index': string (e.g. '5-1'), 'T_indices': [list of strings (e.g. '(5,0)','(1,1)')] }.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structure_4.0.xyz`
- `/app/outputs/structure_6.0.xyz`
- `/app/outputs/structure_12.0.xyz`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structure_4.0.xyz
- path: `/app/outputs/structure_4.0.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed atomic coordinates for Dc=4.0 Å; radii are recomputed from these coordinates and compared to hidden gold.
- schema:
  - `type`: text
  - `description`: XYZ file: first line atom count, second line comment, then lines 'Cu x y z' with coordinates in Å.

### structure_6.0.xyz
- path: `/app/outputs/structure_6.0.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed atomic coordinates for Dc=6.0 Å.
- schema:
  - `type`: text
  - `description`: Same XYZ format for Dc=6.0 Å.

### structure_12.0.xyz
- path: `/app/outputs/structure_12.0.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed atomic coordinates for Dc=12.0 Å.
- schema:
  - `type`: text
  - `description`: Same XYZ format for Dc=12.0 Å.

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Summary of shell radii and indices; cross-verified against XYZ-derived radii and hidden gold.
- schema:
  - `type`: object
  - `required`:
    - `4.0`:
      - `radii`: list of numbers
      - `KT_index`: string
      - `T_indices`: list of strings
    - `6.0`:
      - `radii`: list of numbers
      - `KT_index`: string
      - `T_indices`: list of strings
    - `12.0`:
      - `radii`: list of numbers
      - `KT_index`: string
      - `T_indices`: list of strings

Notes: The angular correlation and radial distribution functions are omitted as they lack numeric validation data. The geometric explanation is a post-hoc interpretation and is verified if structural indices match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structure_4.0.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "XYZ file: first line atom count, second line comment, then lines 'Cu x y z' with coordinates in Å."
      },
      "description": "Relaxed atomic coordinates for Dc=4.0 Å; radii are recomputed from these coordinates and compared to hidden gold."
    },
    {
      "file": "structure_6.0.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Same XYZ format for Dc=6.0 Å."
      },
      "description": "Relaxed atomic coordinates for Dc=6.0 Å."
    },
    {
      "file": "structure_12.0.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Same XYZ format for Dc=12.0 Å."
      },
      "description": "Relaxed atomic coordinates for Dc=12.0 Å."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "4.0": {
            "radii": "list of numbers",
            "KT_index": "string",
            "T_indices": "list of strings"
          },
          "6.0": {
            "radii": "list of numbers",
            "KT_index": "string",
            "T_indices": "list of strings"
          },
          "12.0": {
            "radii": "list of numbers",
            "KT_index": "string",
            "T_indices": "list of strings"
          }
        }
      },
      "description": "Summary of shell radii and indices; cross-verified against XYZ-derived radii and hidden gold."
    }
  ],
  "notes": "The angular correlation and radial distribution functions are omitted as they lack numeric validation data. The geometric explanation is a post-hoc interpretation and is verified if structural indices match."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact. The XYZ files are re‑processed: atoms are sorted into shells, average radii are computed, and the radii are compared to reference values. The summary.json is cross‑checked for consistency with the XYZ‑derived radii and indices. The final reward is a weighted combination of these per‑artifact scores; reporting a number without correct underlying coordinates does not earn credit.
