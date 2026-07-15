# DFT Formation Energies and Hydrogen Adsorption on Co-Doped MoS2 Defect-Pairs

## Problem background
Molybdenum disulfide ($\text{MoS}_2$) is a promising non-precious electrocatalyst for the hydrogen evolution reaction (HER), but its basal plane is largely inert. Doping with foreign atoms is a strategy to activate the basal plane and improve catalytic performance. Co-doping with both a transition metal and a non‑metal can yield synergistic effects that further lower the kinetic barriers. This task reproduces the density functional theory (DFT) investigation of Pd and O co‑doping in $\text{MoS}_2$, focusing on the formation of a defect‑pair where Pd substitutes at a Mo site and O substitutes at a neighbouring S site ($\text{Pd}_{\text{Mo}}{+}\text{O}_{\text{S}}$) in both the 1T and 2H polytypes. The key quantities of interest are the thermodynamic formation energies of these defect‑pairs and their impact on the Gibbs free energy of hydrogen adsorption ($\Delta G_{\text{H}}$), which is a descriptor for HER activity.

## Approach
The computational approach uses plane‑wave pseudopotential DFT with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional. From standard crystal structures of 1T‑ and 2H‑$\text{MoS}_2$, supercell models are constructed and one pair of substitutional defects is created: Pd on a Mo site and O on a nearby S site. Total energies are obtained after structural relaxation, and formation energies are calculated using chemical potentials derived from bulk fcc Pd and a PBE‑corrected $\text{O}_2$ molecule reference. Subsequently, for each relaxed defect system, a hydrogen atom is placed at the most active non‑equivalent S site (denoted S1) and at the O site near the defect. Static total energies, combined with zero‑point energy and entropy corrections at $T = 298\,\text{K}$ and $\text{pH}=0$, are used to compute $\Delta G_{\text{H}}$ via the computational hydrogen electrode model. The workflow contrasts the 1T and 2H polytypes and examines the role of the defect‑pair in modifying the hydrogen binding strength at these specific sites.

## Reproduction target
Produce a single JSON file (`defect_properties.json`) containing the following six floating‑point values (all in eV):
- `formation_energy_Pd_Mo_plus_O_S_1T`: formation energy of the $\text{Pd}_{\text{Mo}}{+}\text{O}_{\text{S}}$ defect‑pair in 1T‑$\text{MoS}_2$.
- `formation_energy_Pd_Mo_plus_O_S_2H`: formation energy of the $\text{Pd}_{\text{Mo}}{+}\text{O}_{\text{S}}$ defect‑pair in 2H‑$\text{MoS}_2$.
- `deltaG_H_S1_1T`: $\Delta G_{\text{H}}$ for H adsorption at the S1 site in the defect‑containing 1T‑$\text{MoS}_2$.
- `deltaG_H_O_1T`: $\Delta G_{\text{H}}$ for H adsorption at the O site in the defect‑containing 1T‑$\text{MoS}_2$.
- `deltaG_H_S1_2H`: $\Delta G_{\text{H}}$ for H adsorption at the S1 site in the defect‑containing 2H‑$\text{MoS}_2$.
- `deltaG_H_O_2H`: $\Delta G_{\text{H}}$ for H adsorption at the O site in the defect‑containing 2H‑$\text{MoS}_2$.

The values must be calculated from first‑principles DFT as described in the workflow steps; no pre‑tabulated results may be substituted. The exact keys and the JSON structure are fixed and will be checked by the verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of 2H-MoS2: 10.1107/S0108768108028666
- Crystal structure of 1T-MoS2: https://materialsproject.org/materials/mp-1434
- Bulk Pd (fcc) reference structure: https://materialsproject.org/materials/mp-1
- O2 molecule PBE reference calculation

## Workflow steps

### Step 1: DFT Formation Energy Calculations for Pd_Mo+O_S defect-pair in MoS2
- Role: process
- Action: Build supercell models of pristine 1T- and 2H-MoS2. Create a Pd substitution at a Mo site and an O substitution at a nearby S site to form the Pd_Mo+O_S defect-pair. Perform DFT structural relaxations and total energy calculations using a plane-wave pseudopotential code with the PBE functional. Compute formation energies using standard chemical potentials: μ_Pd from bulk fcc Pd, μ_O from O2 molecule with PBE overbinding correction. Record optimized structures and formation energies.
- Evidence: `/app/outputs/formation_energies_raw.json`

### Step 2: DFT Gibbs Free Energy of Hydrogen Adsorption on Defect-Pair MoS2
- Role: process
- Action: Using the relaxed defect structures from the previous step, place a hydrogen atom at the most active non-equivalent S sites (e.g., S1) and the O site near the defect. Perform static DFT calculations to obtain total energies. Compute ΔG_H = ΔE_ads + ΔZPE − TΔS at T=298 K and pH=0 using the computational hydrogen electrode model, with zero-point energy and entropy corrections from standard tabulated values or vibrational calculations.
- Evidence: `/app/outputs/deltaG_values.json`

### Step 3: Compile and write scored defect properties
- Role: scored (load-bearing)
- Action: Collect the computed formation energies (in eV) for Pd_Mo+O_S in 1T- and 2H-MoS2, and the corresponding ΔG_H values (in eV) at the S1 and O sites. Write them into a JSON file with the exact keys specified in the output schema.
- Output file: `/app/outputs/defect_properties.json`
- Format: json
- Contract: JSON object with keys: 'formation_energy_Pd_Mo_plus_O_S_1T' (float, eV), 'formation_energy_Pd_Mo_plus_O_S_2H' (float, eV), 'deltaG_H_S1_1T' (float, eV), 'deltaG_H_O_1T' (float, eV), 'deltaG_H_S1_2H' (float, eV), 'deltaG_H_O_2H' (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_properties.json
- path: `/app/outputs/defect_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT-calculated formation energies of the Pd_Mo+O_S defect-pair in 1T- and 2H-MoS2, and Gibbs free energies of hydrogen adsorption at the most active S and O sites near the defect.
- schema:
  - `type`: object
  - `required`: `formation_energy_Pd_Mo_plus_O_S_1T`, `formation_energy_Pd_Mo_plus_O_S_2H`, `deltaG_H_S1_1T`, `deltaG_H_O_1T`, `deltaG_H_S1_2H`, `deltaG_H_O_2H`
  - `properties`:
    - `formation_energy_Pd_Mo_plus_O_S_1T`:
      - `type`: number
      - `description`: Formation energy (eV) for Pd_Mo+O_S defect-pair in 1T-MoS2
    - `formation_energy_Pd_Mo_plus_O_S_2H`:
      - `type`: number
      - `description`: Formation energy (eV) for Pd_Mo+O_S defect-pair in 2H-MoS2
    - `deltaG_H_S1_1T`:
      - `type`: number
      - `description`: ΔG_H (eV) for H adsorption at S1 site in 1T-MoS2
    - `deltaG_H_O_1T`:
      - `type`: number
      - `description`: ΔG_H (eV) for H adsorption at O site in 1T-MoS2
    - `deltaG_H_S1_2H`:
      - `type`: number
      - `description`: ΔG_H (eV) for H adsorption at S1 site in 2H-MoS2
    - `deltaG_H_O_2H`:
      - `type`: number
      - `description`: ΔG_H (eV) for H adsorption at O site in 2H-MoS2

Notes: All energies are in eV. The output file must contain exactly these six fields with numeric values. The hidden checker compares the reported values to paper reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "formation_energy_Pd_Mo_plus_O_S_1T",
          "formation_energy_Pd_Mo_plus_O_S_2H",
          "deltaG_H_S1_1T",
          "deltaG_H_O_1T",
          "deltaG_H_S1_2H",
          "deltaG_H_O_2H"
        ],
        "properties": {
          "formation_energy_Pd_Mo_plus_O_S_1T": {
            "type": "number",
            "description": "Formation energy (eV) for Pd_Mo+O_S defect-pair in 1T-MoS2"
          },
          "formation_energy_Pd_Mo_plus_O_S_2H": {
            "type": "number",
            "description": "Formation energy (eV) for Pd_Mo+O_S defect-pair in 2H-MoS2"
          },
          "deltaG_H_S1_1T": {
            "type": "number",
            "description": "ΔG_H (eV) for H adsorption at S1 site in 1T-MoS2"
          },
          "deltaG_H_O_1T": {
            "type": "number",
            "description": "ΔG_H (eV) for H adsorption at O site in 1T-MoS2"
          },
          "deltaG_H_S1_2H": {
            "type": "number",
            "description": "ΔG_H (eV) for H adsorption at S1 site in 2H-MoS2"
          },
          "deltaG_H_O_2H": {
            "type": "number",
            "description": "ΔG_H (eV) for H adsorption at O site in 2H-MoS2"
          }
        }
      },
      "description": "DFT-calculated formation energies of the Pd_Mo+O_S defect-pair in 1T- and 2H-MoS2, and Gibbs free energies of hydrogen adsorption at the most active S and O sites near the defect."
    }
  ],
  "notes": "All energies are in eV. The output file must contain exactly these six fields with numeric values. The hidden checker compares the reported values to paper reference values with appropriate tolerances."
}
```

## How you are scored
After you submit the required output files, a hidden verifier will evaluate your work. For the scored artifact `defect_properties.json`, the verifier compares each of the six reported values to an independent set of hidden reference values. The reward is proportional to the fraction of values that fall within the verifier’s acceptable tolerance range. The tolerances are chosen to account for legitimate differences arising from choice of DFT code, pseudopotentials, convergence criteria, and numerical settings, while still requiring a correct implementation of the physics. A submission that reports only the target numbers without executing the DFT pipeline will not satisfy the workflow’s process evidence requirements and will receive a low reward. The final reward is a weighted combination of scores from all load‑bearing workflow stages.
