# Conformational Analysis and Dipole Moments of Dialkyl Esters

## Problem background
Dialkyl esters of dicarboxylic acids CH3OOC(CH2)nCOOCH3 (n=1–4,8) display an anomalous dipole moment for the n=2 homologue (succinate), which is substantially lower than those of the other members of the series. The dipole moment and its temperature dependence are sensitive to the conformational distribution around the C*–C bond linking the ester group to the methylene chain. Two competing rotational isomeric state descriptions have been proposed: Model I (six‑state scheme) includes reversed ester orientations, while Model II (three‑state scheme) assigns a stabilization energy to the conformation in which the carbonyl group eclipses the adjacent C–C bond. The goal is to compute the root‑mean‑square dipole moments and temperature coefficients for the five esters under both models, as well as the trans–gauche energy difference for dimethyl succinate, in order to compare how well each model accounts for the experimental observations.

## Approach
Conformational energies are evaluated with a semiempirical potential that comprises 6–12 van der Waals interactions (parameter set from Yoon et al.), a threefold torsional barrier of 2.8 kcal mol⁻¹ for C–C bonds, and Coulombic interactions with an effective dielectric constant of 3.5. Bond lengths, bond angles, and partial atomic charges are taken from Table I (C–C 1.53 Å, C*–O 1.35 Å, C*=O* 1.20 Å, O–(CH₃) 1.43 Å; angles ∠CCC = ∠CCC* = 112°, ∠CC*O = 111.4°, ∠CC*O* = 126.3°, ∠C*O(CH₃) = 116.7°; charges: C* 0.54, O* –0.43, O –0.22, (CH₃) 0.11 e). For each diester (n = 1,2,3,4,8), the statistical weight matrices for the C*–C bonds are constructed according to either the six‑state model (Model I, α = 1.0, states at ψ = 0, ±2π/3, ±π/3, π) or the three‑state model (Model II, Eβ = 1.2 kcal mol⁻¹, states at ψ = 0, ±2π/3). For molecules with internal C–C bonds, rotational isomeric states (trans, gauche ±) are adopted; in the case of succinate a two‑dimensional scan of the central C1–C2 torsion locates the trans and gauche minima and gives the energy difference ΔE = E_gauche − E_trans. The dipole moment of the ester group (1.76 D, oriented at 123° from the C*–C bond) is averaged over all rotational states at 25 °C using the rotational isomeric state formalism. The temperature coefficient d ln⟨μ²⟩^{1/2}/dT is obtained by finite difference. All final values are written to results.json.

## Reproduction target
Compute the root‑mean‑square dipole moment ⟨μ²⟩^{1/2} (in Debye) and the temperature coefficient d ln⟨μ²⟩^{1/2}/dT (in 10⁻³ K⁻¹) at 25 °C for dimethyl malonate (n = 1), succinate (n = 2), glutarate (n = 3), adipate (n = 4) and sebacate (n = 8). Do this for both Model I (α = 1.0) and Model II (Eβ = 1.2 kcal mol⁻¹). For dimethyl succinate, additionally report the trans–gauche energy difference ΔE (kcal mol⁻¹) for each model. Save all values in the JSON structure specified in the output contract (results.json).

## Assets

- Yoon et al. (1975) semiempirical potential parameters: 10.1021/ma60048a018

## Workflow steps

### Step 1: Conformational energy analysis and rotational state determination
- Role: process
- Action: Implement the semiempirical potential energy function using 6‑12 van der Waals parameters from Yoon et al., a threefold torsional barrier of 2.8 kcal mol⁻¹ for C–C bonds, and Coulombic interactions with effective dielectric constant 3.5. Build the six‑state rotational model (Model I, ψ = 0, ±2π/3, ±π/3, π) with statistical weight α=1.0 and the three‑state model (Model II, ψ = 0, ±2π/3) with stabilization energy Eβ=1.2 kcal mol⁻¹ (β = exp(Eβ/RT)). For each dimethyl ester (n=1,2,3,4,8), scan the relevant dihedral angles to locate energy minima and construct the statistical weight matrices. For dimethyl succinate, scan the central C1–C2 bond to find the trans and gauche minima and compute the energy difference ΔE = E_gauche − E_trans. Save the identified minima, statistical weights, and ΔE values to a JSON evidence file.
- Evidence: `/app/outputs/conformational_energies.json`

### Step 2: Dipole moment and temperature coefficient calculation
- Role: scored (load-bearing)
- Action: Using the rotational isomeric state formalism and the statistical weight matrices from Step 1, compute the ensemble-averaged root-mean-square dipole moment ⟨μ²⟩^{1/2} (in Debye) and the temperature coefficient d ln⟨μ²⟩^{1/2}/dT (in 10⁻³ K⁻¹) at 25 °C for each dimethyl ester (malonate, succinate, glutarate, adipate, sebacate) and for both Model I (α=1.0) and Model II (Eβ=1.2 kcal mol⁻¹). Use the ester group dipole moment of 1.76 D oriented at 123° from the C*–C bond. Write the results to a single JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys 'Model_I_alpha_1' and 'Model_II_Ebeta_1_2'. Each value is an object keyed by molecule name (malonate, succinate, glutarate, adipate, sebacate). Each molecule entry contains 'mu_rms' (float, Debye) and 'd_ln_mu_dT' (float, 10⁻³ K⁻¹). The 'succinate' entry additionally contains 'delta_E' (float, kcal mol⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed dipole moments (mu_rms in Debye), temperature coefficients (d_ln_mu_dT in 10⁻³ K⁻¹), and trans–gauche energy difference (delta_E in kcal mol⁻¹) for the five dimethyl esters under models I and II.
- schema:
  - `type`: object
  - `required`: `Model_I_alpha_1`, `Model_II_Ebeta_1_2`
  - `properties`:
    - `Model_I_alpha_1`:
      - `type`: object
      - `required`: `malonate`, `succinate`, `glutarate`, `adipate`, `sebacate`
      - `properties`:
        - `malonate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
        - `succinate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`, `delta_E`
        - `glutarate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
        - `adipate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
        - `sebacate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
    - `Model_II_Ebeta_1_2`:
      - `type`: object
      - `required`: `malonate`, `succinate`, `glutarate`, `adipate`, `sebacate`
      - `properties`:
        - `malonate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
        - `succinate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`, `delta_E`
        - `glutarate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
        - `adipate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`
        - `sebacate`:
          - `type`: object
          - `required`: `mu_rms`, `d_ln_mu_dT`

Notes: The hidden checker compares each numeric value to the paper's reported gold with predefined tolerances. No raw recomputation is performed by the checker; it relies on the agent's reported values, which must be the result of the conformational analysis pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Model_I_alpha_1",
          "Model_II_Ebeta_1_2"
        ],
        "properties": {
          "Model_I_alpha_1": {
            "type": "object",
            "required": [
              "malonate",
              "succinate",
              "glutarate",
              "adipate",
              "sebacate"
            ],
            "properties": {
              "malonate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              },
              "succinate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT",
                  "delta_E"
                ]
              },
              "glutarate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              },
              "adipate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              },
              "sebacate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              }
            }
          },
          "Model_II_Ebeta_1_2": {
            "type": "object",
            "required": [
              "malonate",
              "succinate",
              "glutarate",
              "adipate",
              "sebacate"
            ],
            "properties": {
              "malonate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              },
              "succinate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT",
                  "delta_E"
                ]
              },
              "glutarate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              },
              "adipate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              },
              "sebacate": {
                "type": "object",
                "required": [
                  "mu_rms",
                  "d_ln_mu_dT"
                ]
              }
            }
          }
        }
      },
      "description": "Computed dipole moments (mu_rms in Debye), temperature coefficients (d_ln_mu_dT in 10⁻³ K⁻¹), and trans–gauche energy difference (delta_E in kcal mol⁻¹) for the five dimethyl esters under models I and II."
    }
  ],
  "notes": "The hidden checker compares each numeric value to the paper's reported gold with predefined tolerances. No raw recomputation is performed by the checker; it relies on the agent's reported values, which must be the result of the conformational analysis pipeline."
}
```

## How you are scored
A hidden verifier independently compares each numerical entry in your results.json against the expected results for these models. The reward is proportional to the fraction of values that agree within the required tolerance. The verifier examines your output file only; the correctness of your intermediate conformational energies (conformational_energies.json) is not directly scored but is essential to generate the correct final numbers. Simply guessing or reporting numbers without executing the full conformational analysis pipeline will not match the hidden reference.
