# Er60 Cluster Structure Description: Vertex-sharing Cubane Units and Sodalite Topology

## Problem background
High-nuclearity lanthanide hydroxide clusters often organize their metal ions into polyhedral building blocks, notably tetrahedral [Ln4(μ3‑OH)4] cubane-like units. These units can assemble into extended cages through vertex-sharing, yielding topologies reminiscent of zeolitic frameworks. One particularly striking architecture is a sodalite (truncated octahedron) cage, whose vertices are cubane units connected by squares and hexagons. A chiral erbium(III) cluster has been reported that contains a core of 60 Er atoms arranged as vertex-sharing cubanes, forming a giant sodalite-like cage. Within this cage, a hexagonal ring of cubane units is templated by a μ6‑CO3²⁻ ion that bridges six Er atoms. The structural details—how many cubane units are present, how they connect, and the precise topology—can be deduced from the deposited crystallographic information file (CIF). This task captures that structural description computationally.

## Approach
The analysis is performed entirely from the provided CIF file using open‑source crystallographic tools. First, download the CIF and parse the crystal structure to obtain atomic positions, element types, and connectivity (bond distances). Identify all erbium atoms and the bridging hydroxide groups to locate [Er4(μ3‑OH)4] tetrahedral cubane units, each defined by four Er atoms edge‑bridged by four μ3‑OH groups. Build a graph where each cubane is a node and an edge exists between two cubanes that share exactly one erbium vertex (vertex‑sharing). From this graph, compute the vertex configuration—the sequence of ring sizes (squares and hexagons) around each vertex—and verify whether the assembly forms a truncated octahedron (sodalite topology) with a (4,6,6) configuration. Finally, search for a hexagonal wheel of six cubane units and determine whether a carbonate ion (CO3) resides at its centre, coordinating six erbium atoms in a μ6:η1:η1:η1:η1:η1:η1 fashion.

## Reproduction target
Using the CIF file from the supplementary material (URL given in Assets), write a program that extracts the structural motifs described above and produces a JSON file (`structural_analysis.json`) containing:
- A list of all tetrahedral [Er4(μ3‑OH)4] cubane units, each represented by four erbium atom indices.
- A list of vertex‑sharing connections (pairs of cubane indices that share a single erbium vertex).
- The vertex configuration string determined from the cubane connectivity graph.
- A boolean indicating whether the overall cage corresponds to a sodalite (truncated octahedron) topology.
- An object describing any ring-like arrangement of cubane units that hosts a templating ion, including the identity and coordination mode of that ion, and the indices of the erbium atoms it bridges.

## Assets

- CIF file for the Er60 cluster: https://pubs.acs.org/doi/suppl/10.1021/ja901214d/suppl_file/ja901214d_si_001.cif

## Workflow steps

### Step 1: Structural analysis of Er60 cluster CIF
- Role: scored (load-bearing)
- Action: Download the CIF file and analyse the crystal structure to identify all tetrahedral [Er4(μ3‑OH)4] cubane units (each consisting of four Er and four μ3‑OH), determine their vertex‑sharing connectivity, deduce the overall cage topology (vertex configuration), identify any templating ions bridging cubane rings, and write a JSON file with the extracted motifs.
- Output file: `/app/outputs/structural_analysis.json`
- Format: json
- Contract: {"cubane_units": [[int, ...], ...], "vertex_sharing_connections": [[int, int], ...], "vertex_configuration": "<string>", "sodalite_topology": <bool>, "hexagonal_wheel": {"center_ion": "<string>", "coordination_mode": "<string>", "bridged_er_atoms": [int, ...]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_analysis.json
- path: `/app/outputs/structural_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The extracted structural motifs: cubane units, their vertex‑sharing connectivity, the overall topology, and description of templating ion.
- schema:
  - `type`: object
  - `required`: `cubane_units`, `vertex_sharing_connections`, `vertex_configuration`, `sodalite_topology`, `hexagonal_wheel`
  - `properties`:
    - `cubane_units`:
      - `type`: array
      - `items`:
        - `type`: array
        - `items`:
          - `type`: integer
      - `description`: List of identified tetrahedral cubane units; each is a list of four Er atom indices.
    - `vertex_sharing_connections`:
      - `type`: array
      - `items`:
        - `type`: array
        - `minItems`: 2
        - `maxItems`: 2
        - `items`:
          - `type`: integer
      - `description`: Pairs of cubane indices that share a single Er vertex.
    - `vertex_configuration`:
      - `type`: string
      - `description`: Vertex configuration of the cubane assembly derived from the connectivity graph.
    - `sodalite_topology`:
      - `type`: boolean
      - `description`: True if the overall cage conforms to the sodalite (truncated octahedron) topology.
    - `hexagonal_wheel`:
      - `type`: object
      - `required`: `center_ion`, `coordination_mode`, `bridged_er_atoms`
      - `properties`:
        - `center_ion`:
          - `type`: string
          - `description`: Identity of the ion at the center of the hexagonal (or other) ring.
        - `coordination_mode`:
          - `type`: string
          - `description`: Coordination mode of that ion.
        - `bridged_er_atoms`:
          - `type`: array
          - `items`:
            - `type`: integer
          - `description`: Indices of the Er atoms bridged by the templating ion.

Notes: The output must be derived from the public CIF file. The checker will verify that the extracted cubane units, connectivity, topology, and templating ion are consistent with the expected structure, using structural comparison methods. Exact counts and identities are not disclosed in the contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "cubane_units",
          "vertex_sharing_connections",
          "vertex_configuration",
          "sodalite_topology",
          "hexagonal_wheel"
        ],
        "properties": {
          "cubane_units": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "description": "List of identified tetrahedral cubane units; each is a list of four Er atom indices."
          },
          "vertex_sharing_connections": {
            "type": "array",
            "items": {
              "type": "array",
              "minItems": 2,
              "maxItems": 2,
              "items": {
                "type": "integer"
              }
            },
            "description": "Pairs of cubane indices that share a single Er vertex."
          },
          "vertex_configuration": {
            "type": "string",
            "description": "Vertex configuration of the cubane assembly derived from the connectivity graph."
          },
          "sodalite_topology": {
            "type": "boolean",
            "description": "True if the overall cage conforms to the sodalite (truncated octahedron) topology."
          },
          "hexagonal_wheel": {
            "type": "object",
            "required": [
              "center_ion",
              "coordination_mode",
              "bridged_er_atoms"
            ],
            "properties": {
              "center_ion": {
                "type": "string",
                "description": "Identity of the ion at the center of the hexagonal (or other) ring."
              },
              "coordination_mode": {
                "type": "string",
                "description": "Coordination mode of that ion."
              },
              "bridged_er_atoms": {
                "type": "array",
                "items": {
                  "type": "integer"
                },
                "description": "Indices of the Er atoms bridged by the templating ion."
              }
            }
          }
        }
      },
      "description": "The extracted structural motifs: cubane units, their vertex‑sharing connectivity, the overall topology, and description of templating ion."
    }
  ],
  "notes": "The output must be derived from the public CIF file. The checker will verify that the extracted cubane units, connectivity, topology, and templating ion are consistent with the expected structure, using structural comparison methods. Exact counts and identities are not disclosed in the contract."
}
```

## How you are scored
A hidden verifier will parse your `structural_analysis.json` and compare each claim against the expected structural description derived from the same CIF. The verifier uses structural comparison (connectivity and distance patterns) to assess whether the correct number of cubane units was identified, whether each cubane has the expected composition and vertex‑sharing connectivity, whether the vertex configuration string and sodalite topology verdict are correct, and whether the templating carbonate ion and the hexagonal wheel are correctly located. Exact atom indices may vary between implementations, so the checker matches motifs by their connectivity and bonding rather than by exact index numbers. The reward is a weighted combination of these structural checks; the exact weights and tolerances are not disclosed. Reporting numbers without genuine structural analysis from the CIF does not pass because the verifier expects the supporting connectivity and geometry to be internally consistent with the crystal structure.
