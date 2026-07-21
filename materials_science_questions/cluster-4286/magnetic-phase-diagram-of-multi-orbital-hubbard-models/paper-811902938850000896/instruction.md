# Coexistence of antiferromagnetism and superconductivity in a self-doped bilayer t-t'-J model

## Problem background
In multilayered high-Tc cuprate superconductors, charge imbalance between CuO₂ planes can create a self-doped bilayer: one plane effectively electron-doped, the other hole-doped. Understanding what electronic ground state emerges—whether antiferromagnetism (AFM) and d-wave superconductivity (SC) coexist, and what Fermi surfaces form—remains an open problem. This task investigates these questions using a bilayer t-t'-J model with interlayer hopping and a site potential that creates the charge imbalance.

## Approach
The investigation uses slave-boson mean-field theory on a bilayer t-t'-J model. The model includes nearest-neighbor hopping t, second-neighbor hopping t', superexchange J, an interlayer hopping term of amplitude t⊥ with dispersion ε_{⊥,k} = (t⊥/4)(cos kx − cos ky)², and a site potential W that biases one plane. In the mean-field decoupling, one plane is treated as hole-doped (holon representation) and the other as electron-doped (doublon representation). Self-consistency equations are solved for the order parameters: d-wave pairing amplitudes Δ₁, Δ₂, uniform bond orders χ₁, χ₂, staggered antiferromagnetic moments m₁, m₂, holon density δh₁, doublon density δd₂, and chemical potential μ. From these solutions, ground-state phases are classified (AFM, SC, or AFM+SC coexistence), and the quasiparticle band dispersions are computed to describe Fermi surface features.

## Reproduction target
For model parameters J/t = 1/3, t'/t = −0.4 and the given interlayer dispersion, your goal is to:
- Solve self-consistently the mean-field equations for a grid of total electron density n (0.85 to 1.0), site potential W/t (0 to ~0.2), and four interlayer coupling strengths t⊥/t ∈ {0.0, 0.2, 0.5, 0.8}. Write the results as order_parameters.csv.
- From the t⊥/t = 0.5 results, classify each (n,W) point into a phase (AFM, SC, or AFM+SC) based on the computed order parameters, and output phase_diagram.csv.
- For the doping points n = 0.98, 0.95, 0.90, 0.85 at fixed W/t = 0.05 and t⊥/t = 0.5, take the self-consistent parameters and build the mean-field Hamiltonian to compute the four band energies along the k-path (0,0)–(π,0)–(π/2,π/2)–(0,0). Summarize Fermi surface features (pocket geometry, flat bands, interlayer splitting in the nodal direction) as a JSON object fermi_dispersions.json.

## Assets

- Python 3 with numpy, scipy, matplotlib: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Self-consistent slave-boson mean-field solution
- Role: scored (load-bearing)
- Action: Implement the slave-boson mean-field theory for a bilayer t-t'-J model with interlayer hopping (t_perp) and site potential (W). Solve the self-consistent equations for order parameters (d-wave pairing amplitudes Δ₁, Δ₂, uniform bond orders χ₁, χ₂, antiferromagnetic moments m₁, m₂, holon density δ_h₁, doublon density δ_d₂, chemical potential μ) on a grid of total electron density n (0.85 to 1.0), site potential W/t (0 to about 0.2), and interlayer hopping strengths t_perp/t ∈ {0.0, 0.2, 0.5, 0.8}. Use J/t=1/3, t'/t=-0.4, and interlayer dispersion ε_{⊥,k} = (t_perp/4)(cos k_x - cos k_y)².
- Output file: `/app/outputs/order_parameters.csv`
- Format: csv
- Contract: Columns: n (float), W (float), t_perp_t (float), delta_1 (float), delta_2 (float), chi_1 (float), chi_2 (float), m_1 (float), m_2 (float), delta_h_1 (float), delta_d_2 (float), mu (float). One row per converged (n,W,t_perp_t) point.
- Scoring: scored by hidden verifier

### Step 2: Phase diagram construction
- Role: scored
- Action: From the order parameters in order_parameters.csv for t_perp/t=0.5, classify each (n,W) point into phases: if both m₁ and Δ₁ are non-zero (and similarly for layer 2), label 'AFM+SC'; if only Δ is non-zero, label 'SC'; if only m is non-zero, label 'AFM'. Output a CSV mapping each (n,W) to its phase label.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: n (float), W (float), t_perp_t (float, always 0.5), phase (string: 'AFM', 'SC', or 'AFM+SC'). One row per grid point.
- Scoring: scored by hidden verifier

### Step 3: Fermi surface and band dispersion calculation
- Role: scored
- Action: For doping points n=0.98, 0.95, 0.90, 0.85 with W/t=0.05 and t_perp/t=0.5, take the corresponding self-consistent parameters from order_parameters.csv. Build the mean-field Hamiltonian matrix in the magnetic Brillouin zone, compute its eigenvalues along the k-path (0,0)-(π,0)-(π/2,π/2)-(0,0), and determine Fermi surface features (pocket locations, flat bands, and the presence or absence of interlayer splitting). Output a JSON object containing k-path coordinates, band energies, and a textual description of the features.
- Output file: `/app/outputs/fermi_dispersions.json`
- Format: json
- Contract: A JSON object with keys for each doping case (e.g., 'n=0.98'). Each value is an object with 'k_path' (list of [kx,ky] coordinates), 'energies' (list of four lists of floats, one per band), and 'features' (string describing pockets, flat bands, gap opening, and nodal splitting observation).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_parameters.csv`
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/fermi_dispersions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_parameters.csv
- path: `/app/outputs/order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Converged mean-field order parameters for each (n,W,t_perp) point. The checker will compare the agent's values for a hidden set of points to paper-reported reference values with relative tolerances.
- schema:
  - `type`: table
  - `required_columns`: `n`, `W`, `t_perp_t`, `delta_1`, `delta_2`, `chi_1`, `chi_2`, `m_1`, `m_2`, `delta_h_1`, `delta_d_2`, `mu`
  - `columns`:
    - `n`: float
    - `W`: float
    - `t_perp_t`: float
    - `delta_1`: float
    - `delta_2`: float
    - `chi_1`: float
    - `chi_2`: float
    - `m_1`: float
    - `m_2`: float
    - `delta_h_1`: float
    - `delta_d_2`: float
    - `mu`: float

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase classification for each (n,W) grid point at t_perp/t=0.5. The checker compares the labels to the paper's reported phase diagram boundaries.
- schema:
  - `type`: table
  - `required_columns`: `n`, `W`, `t_perp_t`, `phase`
  - `columns`:
    - `n`: float
    - `W`: float
    - `t_perp_t`: float
    - `phase`: string

### fermi_dispersions.json
- path: `/app/outputs/fermi_dispersions.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fermi surface and band dispersion data for four doping levels. The checker audits structural features (pocket presence, flat bands, interlayer splitting) described in the 'features' field.
- schema:
  - `type`: object
  - `required_keys`: `n=0.98`, `n=0.95`, `n=0.90`, `n=0.85`
  - `per_key`:
    - `type`: object
    - `required_keys`: `k_path`, `energies`, `features`
    - `k_path`: list of [kx,ky] arrays
    - `energies`: list of four lists of floats
    - `features`: string

Notes: The first step's output is load-bearing: the checker scores order parameters at hidden (n,W,t_perp) points not explicitly given, requiring the agent to run the full solver. The other steps derive from the same solver output and are checked by label accuracy and structural audit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "W",
          "t_perp_t",
          "delta_1",
          "delta_2",
          "chi_1",
          "chi_2",
          "m_1",
          "m_2",
          "delta_h_1",
          "delta_d_2",
          "mu"
        ],
        "columns": {
          "n": "float",
          "W": "float",
          "t_perp_t": "float",
          "delta_1": "float",
          "delta_2": "float",
          "chi_1": "float",
          "chi_2": "float",
          "m_1": "float",
          "m_2": "float",
          "delta_h_1": "float",
          "delta_d_2": "float",
          "mu": "float"
        }
      },
      "description": "Converged mean-field order parameters for each (n,W,t_perp) point. The checker will compare the agent's values for a hidden set of points to paper-reported reference values with relative tolerances."
    },
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "W",
          "t_perp_t",
          "phase"
        ],
        "columns": {
          "n": "float",
          "W": "float",
          "t_perp_t": "float",
          "phase": "string"
        }
      },
      "description": "Phase classification for each (n,W) grid point at t_perp/t=0.5. The checker compares the labels to the paper's reported phase diagram boundaries."
    },
    {
      "file": "fermi_dispersions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required_keys": [
          "n=0.98",
          "n=0.95",
          "n=0.90",
          "n=0.85"
        ],
        "per_key": {
          "type": "object",
          "required_keys": [
            "k_path",
            "energies",
            "features"
          ],
          "k_path": "list of [kx,ky] arrays",
          "energies": "list of four lists of floats",
          "features": "string"
        }
      },
      "description": "Fermi surface and band dispersion data for four doping levels. The checker audits structural features (pocket presence, flat bands, interlayer splitting) described in the 'features' field."
    }
  ],
  "notes": "The first step's output is load-bearing: the checker scores order parameters at hidden (n,W,t_perp) points not explicitly given, requiring the agent to run the full solver. The other steps derive from the same solver output and are checked by label accuracy and structural audit."
}
```

## How you are scored
A hidden verifier scores each of the three artifacts independently:
- order_parameters.csv: your computed order parameters for a hidden set of (n,W,t⊥/t) points are compared against reference values with appropriate tolerances.
- phase_diagram.csv: phase labels for the W‑n plane are compared against reference phase boundaries.
- fermi_dispersions.json: the verifier audits structural features—whether pocket geometry, flat bands, and nodal splitting behavior match expectations derived from the mean-field solution.
The final reward is a weighted combination of these checks. Producing the correct numbers through a genuine self-consistent solver is required.
