# SrO–NiO Quasibinary Phase Diagram with Regular Solution Model

## Problem background
The Sr–Ni–O system is important for understanding phase equilibria in perovskite-related compounds and for materials design. The SrO–NiO quasibinary section exhibits limited mutual solid solubility and an eutectic reaction between the two end-member oxides. Thermodynamic modeling of this system allows prediction of liquidus and solidus curves and of the terminal solubilities, providing insight into the phase behaviour that governs processing and stability of strontium‑nickel‑oxide materials.

## Approach
The liquid and the rocksalt-type (halite) solid solution are described by a regular solution model. For each phase, the molar Gibbs energy is expressed as a weighted sum of the pure-component Gibbs energies plus an ideal mixing term and an excess term of the form x(1−x)L, where L is a constant interaction parameter specific to that phase. The interaction parameters for the liquid and for the halite phase are given (in kJ mol⁻¹) and the Gibbs energy functions for pure SrO and NiO are taken from the literature (see Assets). Equilibrium between phases is determined by the common tangent construction, which is equivalent to minimising the total Gibbs energy of the system. The eutectic temperature and liquid composition are obtained from the intersection of the liquidus curves with the solidus, where the two solid end-members coexist with the liquid. The terminal solubility of SrO in NiO at 1350 °C is computed as the composition of the halite phase that is in equilibrium with pure SrO.

## Reproduction target
Implement the regular solution model for the SrO–NiO system with the stated interaction parameters. Using the pure-component Gibbs energy functions from the two cited references, compute the following three quantities and write them to `phase_diagram_results.json`:
- eutectic temperature (K)
- eutectic composition (mol% SrO in the liquid phase)
- solubility of SrO in NiO at 1350 °C (mol% SrO in the rocksalt phase).
The output file must be a valid JSON object with keys `eutectic_temperature_K`, `eutectic_composition_mol_percent_SrO`, and `solubility_SrO_in_NiO_mol_percent`, each a floating‑point number.

## Assets

- Gibbs energy functions for pure SrO (Taylor & Dinsdale 1990)
- Gibbs energy functions for pure NiO (Risold et al. 1996)
- pycalphad (optional open-source CALPHAD library): pycalphad

## Workflow steps

### Step 1: Calculate SrO–NiO phase equilibria and solubility
- Role: scored (load-bearing)
- Action: Obtain the Gibbs energy functions for pure SrO and NiO from the cited literature and implement them as temperature-dependent expressions. Using the regular solution model with interaction parameters ^0L_liq = -52 kJ/mol and ^0L_hal = +105 kJ/mol, compute the SrO–NiO quasibinary phase equilibria: determine the eutectic temperature and liquid composition by common tangent construction between liquid and the two solid end-members; compute the solubility of SrO in NiO at 1350°C (1669.15 K) as the halite phase composition in equilibrium with pure SrO. Output the three resulting numeric values to a JSON file.
- Output file: `/app/outputs/phase_diagram_results.json`
- Format: json
- Contract: {"eutectic_temperature_K": number, "eutectic_composition_mol_percent_SrO": number, "solubility_SrO_in_NiO_mol_percent": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_results.json
- path: `/app/outputs/phase_diagram_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The three computed thermodynamic quantities: the eutectic temperature in Kelvin, the eutectic liquid composition in mole percent SrO, and the terminal solid solubility of SrO in the halite phase at 1350°C in mole percent SrO.
- schema:
  - `type`: object
  - `required`:
    - `eutectic_temperature_K`: float (K)
    - `eutectic_composition_mol_percent_SrO`: float (mol%)
    - `solubility_SrO_in_NiO_mol_percent`: float (mol%)

Notes: The regular solution model parameters and Gibbs energy functions are publicly available from the literature cited in the task description. The agent must retrieve the required unary data and perform the common-tangent calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "eutectic_temperature_K": "float (K)",
          "eutectic_composition_mol_percent_SrO": "float (mol%)",
          "solubility_SrO_in_NiO_mol_percent": "float (mol%)"
        }
      },
      "description": "The three computed thermodynamic quantities: the eutectic temperature in Kelvin, the eutectic liquid composition in mole percent SrO, and the terminal solid solubility of SrO in the halite phase at 1350°C in mole percent SrO."
    }
  ],
  "notes": "The regular solution model parameters and Gibbs energy functions are publicly available from the literature cited in the task description. The agent must retrieve the required unary data and perform the common-tangent calculation."
}
```

## How you are scored
A hidden verifier independently recomputes the same three quantities using the identical Gibbs energy functions and interaction parameters. Your submitted JSON values are compared against the verifier’s computed reference. Each quantity is scored individually: full credit if the deviation falls within an allowed tolerance, with the reward decreasing smoothly as the deviation grows. The three scores are combined into a final reward. Reporting a value without performing the required computation will not earn credit.
