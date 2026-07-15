# Dipole Moments of Acrylate Monomer Model Compounds via Additive Vector Model

## Problem background
The dipole moments of low‑molecular‑weight analogues of acrylate polymers with mesogenic side groups have been measured experimentally. This task focuses on three repeat‑unit model compounds: 4‑biphenyl isobutyrate (PPI), 4‑phenoxyphenyl isobutyrate (PPOI), and 4‑benzoylphenyl isobutyrate (PPCI). The experimental mean‑square dipole moments ⟨μ²⟩ for these compounds have been determined from dielectric measurements in benzene at 30 °C. An additive dipole model has been proposed to explain the observed moments in terms of distinct contributions from the ester group, a phenyl‑substitution correction, and, for PPOI and PPCI, the central ether or ketone bridging group. The goal of this task is to implement the additive vector model and compute the three ⟨μ²⟩ values, thereby testing whether the model can reproduce the experimental behaviour.


## Approach
The dipole moment of each molecule is constructed as the vector sum of separate contributions. The ester‑carbonyl region contributes a dipole μ₁ with a known magnitude and orientation. A second term μ₂ accounts for the effect of replacing the methyl group by a phenyl or substituted phenyl ring. For the oxygen‑bridged (PPOI) and carbonyl‑bridged (PPCI) compounds, a third contribution μ₃ represents the dipole of the central diphenyl‑ether or diphenyl‑ketone moiety. The orientations of μ₁ and μ₂ are fixed by the bond geometry of the ester group, while μ₃ is oriented along the bisector of the valence angle at the central bridging group. For PPI, only μ₁ and μ₂ are needed. For PPOI and PPCI, the molecule can adopt several rotational conformations around the O–Ph bond; four orientations (Ψ₁ = ±60°, ±120°) are isoenergetic and must be considered. The mean‑square dipole moment ⟨μ²⟩ is therefore computed by averaging |μ_total|² over these four states with Ψ₂ = 0. All required magnitudes and bond‑angle parameters are provided in the workflow step; the agent must implement the vector addition and rotational averaging to obtain the three ⟨μ²⟩ values.


## Reproduction target
Compute the mean‑square dipole moment ⟨μ²⟩ (in D²) at 30 °C for PPI, PPOI, and PPCI using the additive dipole model described above and in the workflow step. Output the three values as a JSON object with keys "PPI", "PPOI", and "PPCI" in the file `/app/outputs/computed_dipoles.json`.


## Assets

- Standard dipole moments of diphenyl ether and diphenyl ketone

## Workflow steps

### Step 1: Compute dipole moments for PPI, PPOI, and PPCI
- Role: scored (load-bearing)
- Action: Implement the additive dipole moment vector model using the given parameters: μ₁=1.75 D with direction angle τ=123° measured from the C(=O)-O bond; μ₂=0.3 D along the O-Ph bond direction, accounting for a bond angle difference δ=7.5° between C(=O)-O-Ph and C-C(=O) bonds; for PPOI use μ₃=1.15 D (diphenyl ether dipole) and for PPCI use μ₃=3.0 D (diphenyl ketone dipole), oriented in the bisector of the valence angle θ=112° at the central ether/ketone group. For PPI, combine μ₁ and μ₂ to obtain ⟨μ²⟩. For PPOI and PPCI, add μ₃, then rotate the μ₃ vector around the O-Ph bond direction by the four isoenergetic orientations Ψ₁ = ±60°, ±120° with Ψ₂=0, and average the squared total dipole over the four states. Output the three mean-square dipole moments ⟨μ²⟩ (in D²) as a JSON object.
- Output file: `/app/outputs/computed_dipoles.json`
- Format: json
- Contract: {"PPI": <float>, "PPOI": <float>, "PPCI": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_dipoles.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_dipoles.json
- path: `/app/outputs/computed_dipoles.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed mean-square dipole moments (in D²) for the three monomer model compounds PPI, PPOI, and PPCI at 30 °C, obtained by the additive dipole moment vector model with rotational averaging over four isoenergetic Ψ₁ states.
- schema:
  - `type`: object
  - `properties`:
    - `PPI`:
      - `type`: number
    - `PPOI`:
      - `type`: number
    - `PPCI`:
      - `type`: number
  - `required`: `PPI`, `PPOI`, `PPCI`

Notes: The values are compared to the paper's experimental measurements with a tolerance to account for rounding and minor implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_dipoles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "PPI": {
            "type": "number"
          },
          "PPOI": {
            "type": "number"
          },
          "PPCI": {
            "type": "number"
          }
        },
        "required": [
          "PPI",
          "PPOI",
          "PPCI"
        ]
      },
      "description": "Computed mean-square dipole moments (in D²) for the three monomer model compounds PPI, PPOI, and PPCI at 30 °C, obtained by the additive dipole moment vector model with rotational averaging over four isoenergetic Ψ₁ states."
    }
  ],
  "notes": "The values are compared to the paper's experimental measurements with a tolerance to account for rounding and minor implementation differences."
}
```

## How you are scored
A hidden automated verifier reads your `computed_dipoles.json` and compares each of the three computed mean‑square dipole moments to reference values obtained from the dielectric experiments. The reward is a single float between 0 and 1 that reflects the agreement between your computed values and the experimental references; full credit is awarded when all three ⟨μ²⟩ values fall within an allowed error margin. No prior knowledge of the experimental numbers is required or expected — the verifier expects results from a correct implementation of the additive vector model, not pre‑supplied constants.
