# DFT Analysis of Redox Energetics in Bis(Hexamethylbenzene) Complexes of Fe, Ru, and Os

## Problem background
Bis(hexamethylbenzene) complexes of iron, ruthenium, and osmium, [M(hmb)₂]²⁺, exhibit a systematic change in redox behaviour across the group: the iron dication is reduced in two well-separated one-electron steps, the ruthenium analogue shows almost overlapping one-electron waves, and the osmium system undergoes an apparently potential-inverted two-electron transfer. Understanding why this progression occurs is challenging, because it is not simply a question of ligand-hapticity changes. The paper uses density functional theory (DFT) to separate the free energy changes of reduction into vertical electron-attachment contributions and structural relaxation components through a theoretical square scheme. This task reproduces that computational analysis to reveal how the interplay of electronic and structural factors governs the single- vs. multielectron redox behaviour.

## Approach
The approach is a two-stage DFT procedure. First, gas-phase geometries are optimized at the B3LYP*/6-31G** level, with the Los Alamos LACVP effective core potential used for Fe, Ru, and Os. All relevant oxidation states, spin states, and hapticity isomers (dication η⁶:η⁶, monocation η⁶:η⁶ and η⁴:η⁶, neutral singlet η⁴:η⁶ and triplet η⁶:η⁶ for Fe; analogous for Ru and Os) must be considered. Second, single-point energies and solvation contributions are evaluated with the larger cc-pVTZ(-f) basis for main-group elements and a decontracted LACVP for the metals, using a Poisson–Boltzmann continuum model (dielectric constant of acetonitrile, ε = 36.6) to obtain ΔE(SCF) and ΔΔG_solv. From these raw energies, approximate solution-phase free energies ΔG(sol)′ = ΔE(SCF) + ΔΔG_solv are constructed, and a theoretical square scheme is built: vertical electron-attachment steps are taken at fixed geometries, structural relaxation energies are the difference between adiabatic and vertical energies, and overall two-electron reduction and (for Fe) a spin‑crossover term are computed. The analysis compares the energy components across iron, ruthenium, and osmium to explain the contrasting electrochemical responses.

## Reproduction target
Compute, for each metal (Fe, Ru, Os), the approximate solution-phase free energies ΔG(sol)′ for all species involved in the square scheme, and then determine the energy differences for the following square-scheme steps: first vertical electron attachment (i‑a), structural relaxation after the first electron (i‑b), adiabatic first reduction (i), second vertical electron attachment at the 1+ geometry (ii‑a), structural relaxation after the second electron (ii‑b), adiabatic second reduction (ii), overall two‑electron reduction (iii), and the spin‑crossover energy for Fe (iSC). Report the results in a CSV file `step_energies.csv` with columns: metal (Fe, Ru, Os), step (i‑a, i‑b, i, ii‑a, ii‑b, ii, iii, iSC), description, and delta_G_sol_prime (float, eV). The iSC row should appear only for Fe. The generated energies show how the different contributions evolve down the triad and are the quantitative basis for understanding the observed electrochemical series.

## Assets

- Cartesian coordinates of M(hmb)₂ complexes: Available from the ACS Supporting Information.
- Basis sets (6-31G**, cc-pVTZ(-f), LACVP): Available from the Basis Set Exchange.
- Open-source quantum chemistry software (e.g., ORCA): Available from the ORCA website.

## Workflow steps

### Step 1: Compute raw energies for all M(hmb)₂ species
- Role: process
- Action: For each metal (Fe, Ru, Os), perform DFT geometry optimizations at the B3LYP*/6-31G** level (LACVP effective core potential for metals) in the gas phase for all required oxidation states and spin/hapticity configurations (dication η⁶:η⁶, monocation η⁶:η⁶ and η⁴:η⁶, neutral singlet η⁴:η⁶ and triplet η⁶:η⁶ for Fe; analogous for Ru and Os as described in the paper). Then run single-point energy and solvation calculations at the cc-pVTZ(-f)/decontracted LACVP level with a Poisson–Boltzmann continuum solvation model (acetonitrile) to obtain ΔE(SCF) and ΔΔG_solv for each species.
- Evidence: `/app/outputs/raw_energies.json`

### Step 2: Derive square-scheme free energies
- Role: scored (load-bearing)
- Action: Using the raw ΔE(SCF) and ΔΔG_solv energies from the previous step, compute the approximate solution-phase free energies ΔG(sol)' = ΔE(SCF) + ΔΔG_solv for all species, then calculate the energy differences corresponding to each square-scheme step: first vertical electron attachment (i-a), structural relaxation after first electron (i-b), adiabatic first reduction (i), second vertical electron attachment at the 1+ geometry (ii-a), structural relaxation after second electron (ii-b), adiabatic second reduction (ii), overall two-electron reduction (iii), and the spin-crossover energy for Fe (iSC). Write the results to step_energies.csv.
- Output file: `/app/outputs/step_energies.csv`
- Format: csv
- Contract: CSV with columns: metal (string: Fe, Ru, Os), step (string: i-a, i-b, i, ii-a, ii-b, ii, iii, iSC), description (short text), delta_G_sol_prime (float, eV). The iSC row is present only for Fe.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_energies.csv
- path: `/app/outputs/step_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed square-scheme free energies for all metals and steps.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `step`, `description`, `delta_G_sol_prime`
  - `units`:
    - `delta_G_sol_prime`: eV

Notes: The checker compares the reported ΔG(sol)' values against the paper's hidden gold values with tolerance and enforces the required periodic trends (first vertical attachment becomes less exergonic Fe→Ru→Os, second adiabatic reduction becomes more exergonic Fe→Ru→Os, disproportionation free energies have the correct sign).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "step",
          "description",
          "delta_G_sol_prime"
        ],
        "units": {
          "delta_G_sol_prime": "eV"
        }
      },
      "description": "Computed square-scheme free energies for all metals and steps."
    }
  ],
  "notes": "The checker compares the reported ΔG(sol)' values against the paper's hidden gold values with tolerance and enforces the required periodic trends (first vertical attachment becomes less exergonic Fe→Ru→Os, second adiabatic reduction becomes more exergonic Fe→Ru→Os, disproportionation free energies have the correct sign)."
}
```

## How you are scored
Your submission is scored by a hidden verifier that examines `step_energies.csv`. It compares each reported ΔG(sol)′ value to reference values obtained from the paper, using tolerances that account for legitimate differences arising from the choice of DFT software and numerical settings. In addition, the verifier checks that the computed energies satisfy certain periodic trends across the Fe→Ru→Os series: e.g., the relative magnitudes of vertical attachment energies, adiabatic reduction energies, and the sign of the disproportionation free energy must follow the pattern described in the original study. The final reward is a weighted combination of the per-step numerical agreement and the correctness of these inter-metal trends. Successful completion requires that both the absolute values and the qualitative ordering are reproduced.
