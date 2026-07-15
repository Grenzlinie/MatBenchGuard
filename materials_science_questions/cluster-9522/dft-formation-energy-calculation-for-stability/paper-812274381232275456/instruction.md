# Formation Energies and CVM Interaction Parameters for bcc Mo-Al from FP-LAPW Total Energies

## Problem background
The bcc Mo–Al system exhibits a series of ordered superlattices—B2, B32, and D0₃—that can be derived from the disordered A2 (body-centred cubic) parent lattice. Ab initio total-energy calculations provide ground-state energies of these compounds, which serve as input for a cluster expansion description of the alloy thermodynamics. By converting the total energies into formation energies referenced to the A2 mechanical mixture and then projecting them onto the irregular-tetrahedron (IT) cluster of the cluster variation method (CVM), one obtains effective pair and excess interaction parameters that govern ordering and phase stability. This task covers the post-DFT stage: given the computed total energies, derive the formation energies and the IT-cluster interaction parameters.

## Approach
The provided FP‑LAPW total energies for six compounds (A2 Mo, A2 Al, B2 MoAl, B32 MoAl, D0₃ Mo₃Al, and D0₃ MoAl₃) are the sole input. Formation energies per mole of atoms are computed by subtracting from the compound’s total energy the weighted sum of the elemental A2 total energies, then dividing by the total number of atoms in the formula unit, and converting to kJ/mol. The formation energies are then mapped to cluster eigenenergies of the irregular tetrahedron: each ordered compound is assigned a specific occupation configuration (e.g., MoMoAlAl for B2). The eigenenergy of a tetrahedron configuration is expressed as a linear combination of nearest‑neighbour pair interactions w⁽¹⁾, next‑nearest‑neighbour pair interactions w⁽²⁾, and two excess interactions w̃_MoAlMoAl and w̃_MoAlAlAl, using fractions 1/6 and 1/4 to account for the number of pair clusters per tetrahedron. Setting up the resulting 4×4 linear system from the four compound configurations and solving yields the four CVM interaction parameters in units of k_B·K.

## Reproduction target
Compute the formation energies (kJ per mole of atoms) for the four ordered compounds B2 MoAl, D0₃ Mo₃Al, B32 MoAl, and D0₃ MoAl₃, using the given total energies and the A2 mechanical mixture reference. Subsequently, derive from these formation energies the four effective CVM interaction parameters: nearest‑neighbour pair interaction w₁, next‑nearest‑neighbour pair interaction w₂, and the excess IT interactions w̃_MoAlMoAl and w̃_MoAlAlAl (all in k_B·K). The workflow writes two JSON artifacts: step_01_formation_energies.json and step_02_interaction_parameters.json.

## Assets

The FP‑LAPW total energies (in Rydberg per formula unit) required for the computation are:

- A2 Mo: -7954.6832
- A2 Al: -484.7191
- B2 MoAl: -8439.4173
- B32 MoAl: -8439.4533
- D0₃ Mo₃Al: -24348.8143
- D0₃ MoAl₃: -9408.8444

## Workflow steps

### Step 1: Compute formation energies
- Role: scored
- Action: Using the provided FP‑LAPW total energies (in Rydberg per formula unit) for the six bcc‑based compounds, compute the formation energies per mole of atoms for the four ordered compounds (B2 MoAl, B32 MoAl, D0₃ Mo₃Al, D0₃ MoAl₃) in kJ/mol with the A2 mechanical mixture as reference. Apply the formation energy definition: ΔfU = (U_compound − x·U_Mo_A2 − y·U_Al_A2) / n, where n = x + y. Convert energies from Rydberg to kJ/mol using the conversion factor 1 Ry = 2.17987 × 10⁻¹⁸ J and Avogadro's number.
- Output file: `/app/outputs/step_01_formation_energies.json`
- Format: json
- Contract: {"B2_MoAl": float (kJ/mol), "D03_Mo3Al": float (kJ/mol), "B32_MoAl": float (kJ/mol), "D03_MoAl3": float (kJ/mol)}
- Scoring: scored by hidden verifier

### Step 2: Derive CVM interaction parameters
- Role: scored (load-bearing)
- Action: Map the four formation energies to irregular‑tetrahedron (IT) cluster eigenenergies per tetrahedron. Associate each compound with its cluster configuration: B2 → MoMoAlAl, B32 → MoAlMoAl, D0₃ Mo₃Al → MoMoMoAl, D0₃ MoAl₃ → MoAlAlAl. Express the cluster eigenenergies in terms of the four unknown CVM parameters: nearest‑neighbour pair interaction w(1), next‑nearest‑neighbour pair interaction w(2), excess interactions w̃_MoAlMoAl and w̃_MoAlAlAl, using a decomposition that distributes pair contributions (1/6 and 1/4 fractions) among nearest‑ and next‑nearest neighbours plus an excess term. Set up the resulting linear equations, solve for the four parameters, and report them in units of k_B·K.
- Output file: `/app/outputs/step_02_interaction_parameters.json`
- Format: json
- Contract: {"w1": float (kB·K), "w2": float (kB·K), "wtilde_MoAlMoAl": float (kB·K), "wtilde_MoAlAlAl": float (kB·K)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.json`
- `/app/outputs/step_02_interaction_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.json
- path: `/app/outputs/step_01_formation_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Formation energies per mole of atoms for the four ordered compounds, referenced to the A2 mechanical mixture. The checker recomputes these values from the same total energies and compares within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `B2_MoAl`: float (kJ/mol)
    - `D03_Mo3Al`: float (kJ/mol)
    - `B32_MoAl`: float (kJ/mol)
    - `D03_MoAl3`: float (kJ/mol)

### step_02_interaction_parameters.json
- path: `/app/outputs/step_02_interaction_parameters.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: CVM IT‑cluster interaction parameters derived from the formation energies via linear mapping. The checker recomputes the parameters by solving the same linear system and compares within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `w1`: float (kB·K)
    - `w2`: float (kB·K)
    - `wtilde_MoAlMoAl`: float (kB·K)
    - `wtilde_MoAlAlAl`: float (kB·K)

Notes: Both artifacts are scored via metric_recompute: the checker independently recomputes the expected values from the public total energies and assesses agent's reported values against a hidden gold (paper‑reported Table 2). Tolerances absorb legitimate numerical differences in conversion and linear solving.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "B2_MoAl": "float (kJ/mol)",
          "D03_Mo3Al": "float (kJ/mol)",
          "B32_MoAl": "float (kJ/mol)",
          "D03_MoAl3": "float (kJ/mol)"
        }
      },
      "description": "Formation energies per mole of atoms for the four ordered compounds, referenced to the A2 mechanical mixture. The checker recomputes these values from the same total energies and compares within tolerance."
    },
    {
      "file": "step_02_interaction_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "w1": "float (kB·K)",
          "w2": "float (kB·K)",
          "wtilde_MoAlMoAl": "float (kB·K)",
          "wtilde_MoAlAlAl": "float (kB·K)"
        }
      },
      "description": "CVM IT‑cluster interaction parameters derived from the formation energies via linear mapping. The checker recomputes the parameters by solving the same linear system and compares within tolerance."
    }
  ],
  "notes": "Both artifacts are scored via metric_recompute: the checker independently recomputes the expected values from the public total energies and assesses agent's reported values against a hidden gold (paper‑reported Table 2). Tolerances absorb legitimate numerical differences in conversion and linear solving."
}
```

## How you are scored
A hidden verifier independently recomputes theformation energies from the same total energies and then recomputes the interaction parameters from those formation energies by solving the same linear system. Your reported values are compared to the software‑recomputed results (with appropriate tolerances) for each of the two stages. Each stage earns a score, and the final reward is a weighted combination of the stage scores. Submitting a number without consistent computation from the given inputs will not receive full credit.
