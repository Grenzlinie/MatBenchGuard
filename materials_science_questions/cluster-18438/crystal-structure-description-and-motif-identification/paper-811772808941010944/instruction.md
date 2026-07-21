# Polyhedral Cluster Analysis of a Crystallographic Metallaborane: Subcluster Decomposition and Fusion Motif Identification

## Problem background
Macropolyhedral metallaborane clusters are complex structures in which polyhedral boron‑metal cages fuse together. Determining the identity and connectivity of the subclusters that compose such frameworks is a challenging structural analysis problem. This work aims to decipher the architecture of a specific iridium–boron cluster compound by extracting subcluster identities and fusion motifs from its single‑crystal X‑ray diffraction data.

## Approach
Given the deposited crystallographic information file (CIF) of the compound, we will perform a polyhedral cluster analysis. By parsing the atom coordinates and examining bond distances and connectivity, we will identify the distinct polyhedral building blocks. Each subcluster is characterised by its vertex count and polyhedral type (closo or nido), based on electron‑counting rules. The fusion motifs, such as shared triangular faces and wedge interboron linkages, will be identified from the network of inter‑cluster bonds. The result is a structured decomposition of the cluster framework.

## Reproduction target
Obtain the CIF file for [(PMe3)2IrB26H24Ir(CO)(PMe3)2] from the Cambridge Structural Database using the compound name or a known reference code. Parse the crystal structure and apply the polyhedral analysis to determine: the three fused subclusters (names like [IrBn], where n is an integer), their exact vertex counts, and whether each is closo or nido; the atom indices forming the shared [IrB2] triangular face; the atom indices involved in the wedge interboron linkage; and the total number of metal and boron atoms in the contiguous framework. Output the findings as a JSON file with the schema specified in the step contract. The scoring verifier will compare your identified subclusters, vertex counts, and connectivity motifs to the known reference, so ensure your analysis is rigorous.

## Assets

- Cambridge Structural Database entry for [(PMe3)2IrB26H24Ir(CO)(PMe3)2]: https://www.ccdc.cam.ac.uk/structures/

## Workflow steps

### Step 1: Polyhedral cluster analysis and structural description
- Role: scored
- Action: Retrieve the CIF file of [(PMe3)2IrB26H24Ir(CO)(PMe3)2] from the Cambridge Structural Database. Parse the crystal structure data. Perform polyhedral cluster analysis by examining atom connectivity and bond distances: identify discrete subclusters, determine their vertex counts and polyhedral types (closo/nido). Identify the three fused subclusters based on the polyhedral analysis, determining their types (closo or nido). Detect the shared triangular face connecting two of these subclusters, and the wedge interboron linkage that also connects the third subcluster. Compute the total number of metal and boron atoms in the contiguous framework. Output the results as a structured JSON file.
- Output file: `/app/outputs/structural_description.json`
- Format: json
- Contract: {
  "subclusters": [
    {"name": "string (e.g., [IrB11])", "vertex_count": integer, "polyhedral_type": "closo or nido"}
  ],
  "shared_face_atom_indices": ["string (atom labels from the CIF)"],
  "wedge_linkage_atom_indices": ["string"],
  "total_framework_vertex_count": integer,
  "analysis_notes": "string"
}
All keys are required. subclusters must contain exactly three entries. vertex_count is the number of vertices (Ir + B). shared_face_atom_indices lists the atom identifiers forming the [IrB2] triangular face. wedge_linkage_atom_indices lists the atoms involved in the wedge interboron linkage. total_framework_vertex_count is the total number of Ir and B atoms in the contiguous framework.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_description.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_description.json
- path: `/app/outputs/structural_description.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The result of polyhedral cluster analysis identifying the three subclusters, their vertex counts, polyhedral types, the shared [IrB2] triangular face, wedge interboron linkage, and total contiguous framework vertex count.
- schema:
  - `type`: object
  - `required`: `subclusters`, `shared_face_atom_indices`, `wedge_linkage_atom_indices`, `total_framework_vertex_count`, `analysis_notes`
  - `properties`:
    - `subclusters`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `vertex_count`:
            - `type`: integer
          - `polyhedral_type`:
            - `type`: string
    - `shared_face_atom_indices`:
      - `type`: array
      - `items`:
        - `type`: string
    - `wedge_linkage_atom_indices`:
      - `type`: array
      - `items`:
        - `type`: string
    - `total_framework_vertex_count`:
      - `type`: integer
    - `analysis_notes`:
      - `type`: string

Notes: The agent must retrieve the CIF from the Cambridge Structural Database and perform a graph-based or distance-based cluster decomposition. The result is verified against the paper-reported subcluster decomposition, vertex counts, and connectivity motifs (T0 result-level compare).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_description.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "subclusters",
          "shared_face_atom_indices",
          "wedge_linkage_atom_indices",
          "total_framework_vertex_count",
          "analysis_notes"
        ],
        "properties": {
          "subclusters": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "vertex_count": {
                  "type": "integer"
                },
                "polyhedral_type": {
                  "type": "string"
                }
              }
            }
          },
          "shared_face_atom_indices": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "wedge_linkage_atom_indices": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "total_framework_vertex_count": {
            "type": "integer"
          },
          "analysis_notes": {
            "type": "string"
          }
        }
      },
      "description": "The result of polyhedral cluster analysis identifying the three subclusters, their vertex counts, polyhedral types, the shared [IrB2] triangular face, wedge interboron linkage, and total contiguous framework vertex count."
    }
  ],
  "notes": "The agent must retrieve the CIF from the Cambridge Structural Database and perform a graph-based or distance-based cluster decomposition. The result is verified against the paper-reported subcluster decomposition, vertex counts, and connectivity motifs (T0 result-level compare)."
}
```

## How you are scored
The output file `/app/outputs/structural_description.json` is scored by a hidden verifier that compares your reported subclusters, vertex counts, linkage atom indices, and total framework vertex count against the correct values derived from the paper's structural analysis. The rubric rewards correctly identifying the three named subclusters, their vertex counts, their polyhedral types, the atoms forming the shared face and wedge linkage, and the exact total vertex count. Reporting results that match the reference earns full credit for this stage; incorrect or missing elements receive lower scores. The verifier operates independently and only evaluates the contents of your JSON file.
