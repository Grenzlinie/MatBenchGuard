# Liquid mercury Ziman transport coefficients and Mott density-of-states factor

## Problem background
The electrical resistivity of liquid mercury (Hg) is unusually high and decreases under pressure, contrary to the predictions of Ziman's nearly-free-electron theory for liquid metals. Mott suggested that the electronic density of states at the Fermi level is substantially reduced relative to the free-electron value, introducing a factor g = N(E_F)/N_free(E_F) that modifies the resistivity. This task investigates that hypothesis quantitatively: we compute Ziman's resistivity and thermopower for liquid Hg at several atomic volumes using a first-principles pseudopotential and a liquid structure factor, then compare the results with experimental reference values to infer the magnitude of g² and its dependence on pressure.

## Approach
We use the screened model potential of Animalu and Heine (1965) for Hg, which provides the energy-dependent scattering form factor U(q). The potential is screened with a Lindhard-type dielectric function that includes exchange. The liquid structure is described by the interference function a(q) derived by Ashcroft and Lekner (1966) from the Percus–Yevick hard-sphere solution at a packing density of 46%. With U(q) and a(q) in hand, Ziman's formulas for electrical resistivity and thermoelectric power are evaluated by numerical integration over momentum transfers up to 2k_F. The calculation is repeated at four atomic volumes (164.5, 155, 147, 140 a.u.) that span the ambient liquid state and compressed configurations. The ambient Mott g² factor is then estimated from the ratio of the experimental resistivity (98 µΩ·cm) to the computed Ziman resistivity at ambient volume, and its pressure derivative ∂ln g²/∂ln a is obtained from the volume dependence of the computed resistivity together with the experimentally observed derivative Δ_Mott ≈ +8. All intermediate functions are computed in-process; no pre‑made tables of U(q) or a(q) are provided.

## Reproduction target
Compute the Ziman electrical resistivity (µΩ·cm) and thermopower (µV/K) for liquid Hg at the four atomic volumes Ω = 164.5, 155, 147, 140 a.u., using the Animalu–Heine pseudopotential and the Ashcroft–Lekner interference function. Then, using the experimental ambient resistivity of 98 µΩ·cm and the experimental volume derivative Δ_Mott ≈ +8 (both fixed numerical inputs), derive the ambient Mott density-of-states factor g² and the logarithmic pressure derivative ∂ln g²/∂ln a. Write all computed values to `/app/outputs/ziman_results.json` following the output contract specified below.

## Assets

- Animalu and Heine (1965) screened model potential parameters for Hg: 10.1080/14786436508211948
- Ashcroft and Lekner (1966) interference function a(q) for liquid Hg: 10.1103/PhysRev.145.83
- Python scientific computing libraries (NumPy, SciPy): pip install numpy scipy

## Workflow steps

### Step 1: Compute screened model potential U(q)
- Role: process
- Action: Using the model potential parameters from Animalu and Heine (1965) for Hg, calculate the screened model potential U(q) as a function of momentum transfer q at each of the four atomic volumes Ω = 164.5, 155, 147, 140 a.u. Apply the appropriate dielectric screening function (e.g., Lindhard with exchange). Save the computed U(q) for later use.
- Evidence: `/app/outputs/u_q_values.json`

### Step 2: Obtain interference function a(q)
- Role: process
- Action: Compute or retrieve the interference function a(q) for liquid Hg from the Percus–Yevick hard-sphere solution with packing density η = 0.46, as described by Ashcroft and Lekner (1966). The function must cover the q‑range needed for integration up to 2k_F.
- Evidence: `/app/outputs/a_q.csv`

### Step 3: Compute Ziman transport coefficients and derive Mott g factor
- Role: scored (load-bearing)
- Action: Implement Ziman’s formulas for electrical resistivity and thermopower using the screened potential U(q) and interference function a(q). Compute the resistivity in µΩ·cm and thermopower in µV/K at Ω = 164.5, 155, 147, 140. Compute the volume derivative of ρ_Ziman from finite differences. Using the supplied experimental ambient resistivity 98 µΩ·cm and experimental Δ_Mott ≈ +8, estimate g² ≈ ρ_Ziman(164.5)/98 and ∂ln g²/∂ln a = 3*(Δ_Ziman − Δ_Mott). Write all computed values to a JSON file.
- Output file: `/app/outputs/ziman_results.json`
- Format: json
- Contract: {'resistivities': {'164.5': float, '155': float, '147': float, '140': float}, 'thermopowers': {'164.5': float, '155': float, '147': float, '140': float}, 'g2_ambient': float, 'dln_g2_dln_a': float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ziman_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ziman_results.json
- path: `/app/outputs/ziman_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the four Ziman resistivities (µΩ·cm), four thermopowers (µV/K), the derived ambient g², and the logarithmic pressure derivative ∂ln g²/∂ln a.
- schema:
  - `type`: object
  - `required`: `resistivities`, `thermopowers`, `g2_ambient`, `dln_g2_dln_a`
  - `properties`:
    - `resistivities`:
      - `type`: object
      - `required`: `164.5`, `155`, `147`, `140`
      - `additionalProperties`:
        - `type`: number
    - `thermopowers`:
      - `type`: object
      - `required`: `164.5`, `155`, `147`, `140`
      - `additionalProperties`:
        - `type`: number
    - `g2_ambient`:
      - `type`: number
    - `dln_g2_dln_a`:
      - `type`: number

Notes: Phonon dispersion calculation omitted per task scoping. The checker compares each numeric field to hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ziman_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "resistivities",
          "thermopowers",
          "g2_ambient",
          "dln_g2_dln_a"
        ],
        "properties": {
          "resistivities": {
            "type": "object",
            "required": [
              "164.5",
              "155",
              "147",
              "140"
            ],
            "additionalProperties": {
              "type": "number"
            }
          },
          "thermopowers": {
            "type": "object",
            "required": [
              "164.5",
              "155",
              "147",
              "140"
            ],
            "additionalProperties": {
              "type": "number"
            }
          },
          "g2_ambient": {
            "type": "number"
          },
          "dln_g2_dln_a": {
            "type": "number"
          }
        }
      },
      "description": "JSON file containing the four Ziman resistivities (µΩ·cm), four thermopowers (µV/K), the derived ambient g², and the logarithmic pressure derivative ∂ln g²/∂ln a."
    }
  ],
  "notes": "Phonon dispersion calculation omitted per task scoping. The checker compares each numeric field to hidden reference values with appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/ziman_results.json`. The verifier independently checks each numeric field — the four resistivities, the four thermopowers, the derived ambient g², and the derivative ∂ln g²/∂ln a — against reference values derived from the paper's reported results. Each quantity is compared with an appropriate tolerance that accounts for legitimate variations in numerical implementation. The final reward is a weighted combination of accuracy on these quantities; producing the correct transport coefficients and derived g-factor values earns high marks, whereas large deviations reduce the score. No other files are scored; the intermediate evidence artifacts (`u_q_values.json`, `a_q.csv`) are for your own record but do not contribute to the reward.
