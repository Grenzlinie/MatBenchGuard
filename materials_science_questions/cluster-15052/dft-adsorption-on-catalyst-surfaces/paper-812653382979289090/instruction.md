# DFT Simulation of NO Electroreduction Free Energy Landscape on a Single-Atom Catalyst

## Problem background
Electrochemical reduction of nitrogen oxides (NO) to ammonia (NH3) offers a sustainable route for clean energy conversion and ammonia synthesis. Single-atom catalysts (SACs) that anchor a transition metal on a two-dimensional support can provide high activity and selectivity, but screening for an optimal combination requires reliable evaluation of the free energy landscape. This task targets the Cu single atom on graphitic carbon nitride (g-C3N4) as a candidate electrocatalyst. The goal is to compute, from first-principles density functional theory (DFT), the Gibbs free energy diagram of the NO electroreduction reaction (NORR) to NH3 and of the competing hydrogen evolution reaction (HER). From these diagrams, the thermodynamic limiting potentials for both pathways are derived to assess whether Cu@g-C3N4 exhibits efficient NORR while suppressing parasitic HER.

## Approach
The approach uses spin-polarized plane-wave DFT calculations with an open-source code (e.g., Quantum ESPRESSO) and standard pseudopotentials. First, the pristine g-C3N4 monolayer is relaxed to its ground-state geometry. A single Cu atom is then placed at a plausible adsorption site and the whole Cu@g-C3N4 system is fully relaxed to obtain the catalyst model. Afterwards, total energies are computed for the clean catalyst and for all adsorbed reaction intermediates along two NORR branches (via *HNO and *NOH) leading to NH3, as well as for the HER intermediate *H. Gas-phase reference molecules (NO, H2, N2, H2O, NH3) are also treated. Zero-point energy and entropic contributions at 298 K are applied within the harmonic approximation. The computational hydrogen electrode (CHE) model is used to reference the free energies: the chemical potential of a proton–electron pair is linked to that of gaseous H2 at 0 V vs. the reversible hydrogen electrode, and the free energy of the final product NH3(g) is treated consistently. From the resulting free energy profile, the largest positive free energy step along NORR identifies the rate-determining step, and its magnitude (scaled by the number of electrons transferred) gives the limiting potential for NO reduction. The HER limiting potential is obtained analogously from the free energy of adsorbed *H. Comparing these two potentials provides a quantitative measure of selectivity.

## Reproduction target
Compute the Gibbs free energies of all key NORR intermediates (*NO, *HNO, *NOH, *HNOH, *H₂NO, *N, *H₂NOH, *NH, *NH₂, *NH₃) and the HER intermediate (*H) on the optimized Cu@g-C3N4 catalyst, following the CHE formalism at 298 K. Write a complete table of these free energies (including total energies, zero-point energies, and entropy corrections) to /app/outputs/free_energies_table.csv. From the free energy profile, derive the thermodynamic limiting potentials for NO electroreduction and for hydrogen evolution, identify the rate-determining step, and output these results as /app/outputs/limiting_potentials.json. The evaluation must show whether the catalyst favors NORR over HER by determining if the HER limiting potential is more cathodic (i.e., requires a larger overpotential) than the NORR limiting potential.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotentials library (efficiency set, PBEsol or PBE functional): https://www.materialscloud.org/discover/sssp/
- g-C3N4 monolayer structure (honeycomb lattice, a ≈ 7.13 Å): https://materialsproject.org/materials/mp-1106451
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Geometry optimization of pristine g-C3N4 monolayer
- Role: process
- Action: Using DFT (e.g., Quantum ESPRESSO), relax the atomic positions and lattice constants of a monolayer g-C3N4 supercell, starting from the known honeycomb structure (a ≈ 7.13 Å). Save the optimized geometry and log.
- Evidence: `/app/outputs/g-C3N4_opt.log`

### Step 2: Adsorption and optimization of Cu on g-C3N4
- Role: process
- Action: Place a Cu single atom at a plausible hollow site on the relaxed g-C3N4 monolayer and perform a full geometry relaxation of the Cu atom and the substrate to obtain the optimized Cu@g-C3N4 catalyst structure. Save the optimization log.
- Evidence: `/app/outputs/Cu_at_g-C3N4_opt.log`

### Step 3: Compute NORR and HER free energy diagrams and limiting potentials
- Role: scored (load-bearing)
- Action: On the optimized Cu@g-C3N4 structure, compute the total energies of the clean catalyst and of all adsorbed NORR intermediates: *NO, *HNO, *NOH, *HNOH, *H2NO, *N, *H2NOH, *NH, *NH2, *NH3, and the gas-phase reference NH3; also compute *H for HER. Obtain energies of gas-phase molecules NO, H2, N2, H2O, NH3. Apply zero-point energy and entropy corrections at 298 K using the harmonic approximation. Use the computational hydrogen electrode (CHE) model to calculate Gibbs free energies referenced to the clean catalyst and gas-phase references. Write the full table of free energies to /app/outputs/free_energies_table.csv. From these free energies, compute the limiting potentials (thermodynamic onset potentials) for NO reduction and HER, identify the rate-determining step, and write the results to /app/outputs/limiting_potentials.json.
- Output file: `/app/outputs/free_energies_table.csv,limiting_potentials.json`
- Format: csv
- Contract: free_energies_table.csv: header row with columns species, total_energy_eV, ZPE_eV, TS_eV, free_energy_eV (all numeric). limiting_potentials.json: object with keys NO_reduction_limiting_potential_V (float), HER_limiting_potential_V (float), rate_determining_step (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energies_table.csv`
- `/app/outputs/limiting_potentials.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energies_table.csv
- path: `/app/outputs/free_energies_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: DFT total energies, zero-point energies, entropy contributions (at 298 K), and Gibbs free energies for all NORR intermediates, HER intermediate, and gas-phase reference species, referenced to the clean Cu@g-C3N4 catalyst and gas-phase molecules via the CHE model.
- schema:
  - `type`: table
  - `required_columns`: `species`, `total_energy_eV`, `ZPE_eV`, `TS_eV`, `free_energy_eV`
  - `units`:
    - `total_energy_eV`: eV
    - `ZPE_eV`: eV
    - `TS_eV`: eV
    - `free_energy_eV`: eV

### limiting_potentials.json
- path: `/app/outputs/limiting_potentials.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Derived thermodynamic onset potentials for the NO electroreduction reaction and the hydrogen evolution reaction, along with the identifier of the rate-determining step (e.g., '*HNO -> *HNOH').
- schema:
  - `type`: object
  - `required`:
    - `NO_reduction_limiting_potential_V`: number
    - `HER_limiting_potential_V`: number
    - `rate_determining_step`: string
  - `units`:
    - `NO_reduction_limiting_potential_V`: V
    - `HER_limiting_potential_V`: V

Notes: The task focuses exclusively on the DFT thermodynamics of NORR and HER on Cu@g-C3N4. Stages from the full paper workflow that are not required for the main catalytic claim (TM screening, Bader charge analysis, band structure, N-O bond lengths across TMs, and AIMD thermal stability) are omitted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energies_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "total_energy_eV",
          "ZPE_eV",
          "TS_eV",
          "free_energy_eV"
        ],
        "units": {
          "total_energy_eV": "eV",
          "ZPE_eV": "eV",
          "TS_eV": "eV",
          "free_energy_eV": "eV"
        }
      },
      "description": "DFT total energies, zero-point energies, entropy contributions (at 298 K), and Gibbs free energies for all NORR intermediates, HER intermediate, and gas-phase reference species, referenced to the clean Cu@g-C3N4 catalyst and gas-phase molecules via the CHE model."
    },
    {
      "file": "limiting_potentials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "NO_reduction_limiting_potential_V": "number",
          "HER_limiting_potential_V": "number",
          "rate_determining_step": "string"
        },
        "units": {
          "NO_reduction_limiting_potential_V": "V",
          "HER_limiting_potential_V": "V"
        }
      },
      "description": "Derived thermodynamic onset potentials for the NO electroreduction reaction and the hydrogen evolution reaction, along with the identifier of the rate-determining step (e.g., '*HNO -> *HNOH')."
    }
  ],
  "notes": "The task focuses exclusively on the DFT thermodynamics of NORR and HER on Cu@g-C3N4. Stages from the full paper workflow that are not required for the main catalytic claim (TM screening, Bader charge analysis, band structure, N-O bond lengths across TMs, and AIMD thermal stability) are omitted."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines them by weight into a final reward. For the free energy table, the verifier checks that all required species are present and that the CHE reference scheme is applied correctly. For the limiting potentials, the verifier recomputes the NORR and HER limiting potentials directly from the free energy differences reported in the table, then compares the recomputed values against hidden reference potentials. It also verifies that the rate-determining step matches the expected pathway, that the HER limiting potential is more negative than the NORR limiting potential (indicating suppressed HER), and that the free energy profile is internally consistent. Reporting the paper’s numbers without completing the DFT workflow will not satisfy these checks; the scored reward reflects the correctness of both the raw free energies and the derived onset potentials.
