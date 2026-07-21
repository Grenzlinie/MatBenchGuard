# Ground State Classification and Residual Entropy of a Chiral Honeycomb Lattice Model

## Problem background
We study low-temperature phases of a two‑dimensional lattice model of chiral molecules on a honeycomb lattice. The model contains an equimolar mixture of two enantiomers (mirror‑image molecules) with nearest‑neighbour interactions: six closest‑group and two second‑closest interactions. Under periodic boundary conditions the Hamiltonian reduces to a four‑parameter effective model. The main open question is: for given sets of these effective parameters, what ground state configurations (homochiral, racemic, or an unusual racemic pattern) arise, and, for a special degenerate parameter choice, what is the exact residual entropy per site?

## Approach
Reformulate the original eight‑parameter model into a four‑parameter effective Hamiltonian (parameters Δ_AB, Δ_AC, Δ_BC, δ) by exploiting close‑packing constraints and periodic boundary conditions. Define a *triangle potential* Φ_T for each triangle of four lattice sites (one site and its three neighbours) as a linear combination of the numbers of closest‑group types and second‑closest pairs, using the ordering Δ_BC < Δ_AC < Δ_AB. Enumerate all possible configurations of the triangle sites and find the minima of Φ_T. When these minimum triangle configurations can be periodically tiled over the whole lattice, they define the system's ground states. For parameter regimes where no such tiling exists, the triangle method does not yield a ground state. In one special degenerate regime the ground‑state degeneracy is infinite; the residual entropy per site is then computed via an exact combinatorial colouring problem, giving a closed‑form expression involving the gamma function Γ(1/3).

## Reproduction target
For the six parameter regimes defined below, compute the minimal triangle potential Φ_T by enumerating all triangle configurations and determine the ground state type: 'homochiral', 'racemic', 'unusual_racemic', or 'none' (when no periodic tiling exists). Write the results, including the effective parameters and minimal Φ_T, to `/app/outputs/ground_state_results.json`.

Parameter values (satisfying Δ_BC < Δ_AC < Δ_AB):
- case_I:   Δ_AB = 3.0,  Δ_AC = 2.0,  Δ_BC = 1.0,  δ = 5.0
- case_II:  Δ_AB = 4.0,  Δ_AC = 2.0,  Δ_BC = 1.0,  δ = 3.0
- case_III: Δ_AB = -1.0, Δ_AC = -2.0, Δ_BC = -3.0, δ = -0.5
- case_IV:  Δ_AB = 3.0,  Δ_AC = 2.0,  Δ_BC = 1.0,  δ = 0.5
- case_V:   Δ_AB = 1.0,  Δ_AC = -2.0, Δ_BC = -3.0, δ = -0.5
- case_VI:  Δ_AB = 3.0,  Δ_AC = 2.0,  Δ_BC = 1.0,  δ = -0.5 For the special regime Δ_AB < 0, δ = 0, compute the exact numerical value of the residual entropy per site factor W = (√3)/(2π) [Γ(1/3)]^(3/2) and write the result to `/app/outputs/residual_entropy.txt`.

## Assets
Required Python packages: `numpy`, `scipy`. No external datasets, pretrained models, or proprietary tools are needed. Implement the triangle potential and the enumeration of configurations from the model description above.

## Workflow steps

### Step 1: Compute ground state phases
- Role: scored (load-bearing)
- Action: For each parameter set (case I through case VI), enumerate all possible triangle configurations of the central site and its three neighbours on the honeycomb lattice, compute the triangle potential Φ_T = Δ_AB N_T^AB + Δ_AC N_T^AC + Δ_BC N_T^BC + δ N_T^- using the ordering Δ_BC<Δ_AC<Δ_AB, find the minimal Φ_T value, and determine the ground state type (homochiral, racemic, unusual racemic, or none) by analysing which case the parameters belong to and whether a periodic tiling exists. Write the results to /app/outputs/ground_state_results.json.
- Output file: `/app/outputs/ground_state_results.json`
- Format: json
- Contract: A JSON object with keys 'case_I', 'case_II', 'case_III', 'case_IV', 'case_V', 'case_VI'. Each value is an object with keys: delta_AB (float), delta_AC (float), delta_BC (float), delta (float), min_phi_T (float), ground_state_type (string, one of 'homochiral', 'racemic', 'unusual_racemic', 'none').
- Scoring: scored by hidden verifier

### Step 2: Compute residual entropy
- Role: scored
- Action: For the special parameter case Δ_AB < 0, δ = 0, compute the exact value of the residual entropy per site factor W = sqrt(3)/(2π) [Γ(1/3)]^(3/2) and write the numeric result to /app/outputs/residual_entropy.txt.
- Output file: `/app/outputs/residual_entropy.txt`
- Format: txt
- Contract: A single line containing the numeric value of W (e.g., '1.2087177').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ground_state_results.json`
- `/app/outputs/residual_entropy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ground_state_results.json
- path: `/app/outputs/ground_state_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Ground state phase classification and minimal triangle potential for six parameter regimes. The checker recomputes min_phi_T and classification from the model and compares with the agent's report within a small numeric tolerance (min_phi_T) and exact string match (ground_state_type).
- schema:
  - `type`: object
  - `required`:
    - `case_I`:
      - `delta_AB`: float
      - `delta_AC`: float
      - `delta_BC`: float
      - `delta`: float
      - `min_phi_T`: float
      - `ground_state_type`: string
    - `case_II`:
      - `delta_AB`: float
      - `delta_AC`: float
      - `delta_BC`: float
      - `delta`: float
      - `min_phi_T`: float
      - `ground_state_type`: string
    - `case_III`:
      - `delta_AB`: float
      - `delta_AC`: float
      - `delta_BC`: float
      - `delta`: float
      - `min_phi_T`: float
      - `ground_state_type`: string
    - `case_IV`:
      - `delta_AB`: float
      - `delta_AC`: float
      - `delta_BC`: float
      - `delta`: float
      - `min_phi_T`: float
      - `ground_state_type`: string
    - `case_V`:
      - `delta_AB`: float
      - `delta_AC`: float
      - `delta_BC`: float
      - `delta`: float
      - `min_phi_T`: float
      - `ground_state_type`: string
    - `case_VI`:
      - `delta_AB`: float
      - `delta_AC`: float
      - `delta_BC`: float
      - `delta`: float
      - `min_phi_T`: float
      - `ground_state_type`: string

### residual_entropy.txt
- path: `/app/outputs/residual_entropy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Exact numerical value of the residual entropy factor W for the degenerate ground state case. The checker recomputes W from the gamma function expression and compares with the agent's value within a tolerance.
- schema:
  - `type`: text
  - `required`:
    - `value`: float

Notes: Parameter cases I–VI are defined in the instruction with explicit Δ and δ values satisfying the ordering assumptions. The agent must implement the triangle potential enumeration and ground state construction logic; no external datasets or models are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ground_state_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "case_I": {
            "delta_AB": "float",
            "delta_AC": "float",
            "delta_BC": "float",
            "delta": "float",
            "min_phi_T": "float",
            "ground_state_type": "string"
          },
          "case_II": {
            "delta_AB": "float",
            "delta_AC": "float",
            "delta_BC": "float",
            "delta": "float",
            "min_phi_T": "float",
            "ground_state_type": "string"
          },
          "case_III": {
            "delta_AB": "float",
            "delta_AC": "float",
            "delta_BC": "float",
            "delta": "float",
            "min_phi_T": "float",
            "ground_state_type": "string"
          },
          "case_IV": {
            "delta_AB": "float",
            "delta_AC": "float",
            "delta_BC": "float",
            "delta": "float",
            "min_phi_T": "float",
            "ground_state_type": "string"
          },
          "case_V": {
            "delta_AB": "float",
            "delta_AC": "float",
            "delta_BC": "float",
            "delta": "float",
            "min_phi_T": "float",
            "ground_state_type": "string"
          },
          "case_VI": {
            "delta_AB": "float",
            "delta_AC": "float",
            "delta_BC": "float",
            "delta": "float",
            "min_phi_T": "float",
            "ground_state_type": "string"
          }
        }
      },
      "description": "Ground state phase classification and minimal triangle potential for six parameter regimes. The checker recomputes min_phi_T and classification from the model and compares with the agent's report within a small numeric tolerance (min_phi_T) and exact string match (ground_state_type)."
    },
    {
      "file": "residual_entropy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "value": "float"
        }
      },
      "description": "Exact numerical value of the residual entropy factor W for the degenerate ground state case. The checker recomputes W from the gamma function expression and compares with the agent's value within a tolerance."
    }
  ],
  "notes": "Parameter cases I–VI are defined in the instruction with explicit Δ and δ values satisfying the ordering assumptions. The agent must implement the triangle potential enumeration and ground state construction logic; no external datasets or models are required."
}
```

## How you are scored
A hidden verifier independently recomputes the ground state energy and classification for every parameter case and recomputes the residual entropy factor W from the gamma function. Your submitted outputs are compared against these recomputed references: the minute triangle energy φ_T is checked within a small numeric tolerance, the ground state type must match exactly, and the residual entropy factor W is compared within tolerance. The total reward is a weighted sum of the scores on the two artifacts.
