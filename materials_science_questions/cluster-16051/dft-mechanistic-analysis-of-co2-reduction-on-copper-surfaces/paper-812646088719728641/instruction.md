# Voltage-Induced CO Adsorption Site Switching on Cu(100) via DFT-Continuum Solvation

## Problem background
The electrochemical reduction of CO₂ into fuels and chemicals on copper catalysts is promising but limited by poor selectivity. The electrolyte microenvironment (pH, ionic composition, applied voltage) can strongly influence the binding of reaction intermediates such as CO, yet standard theoretical approaches often treat the interface under vacuum. A recently developed DFT-continuum method based on the effective screening medium and reference interaction site model (ESM-RISM) explicitly models the electrical double layer and allows computation of free energies under realistic electrochemical conditions. In this task, we will use ESM-RISM to compute the CO binding free energies on a Cu(100) terrace as a function of voltage and pH, and determine how the site preference changes across the conditions studied.

## Approach
We will perform grand-canonical density functional theory (DFT) calculations using Quantum ESPRESSO with the ESM-RISM module and the BEEF-vdw exchange-correlation functional. For a Cu(100) surface slab, we will compute the electronic grand potentials Ω(Φ) for the clean surface and for CO adsorbed at atop, bridge, and hollow sites across a range of applied voltages. Additionally, we will compute the free energy of a solvated CO molecule in each electrolyte (0.1 M KCl at pH 7 and 0.1 M KOH at pH 13). Vibrational frequencies will be calculated to obtain zero-point energy, entropy, and heat capacity corrections for both adsorbed and solvated CO. The CO binding free energy ΔG_b(Φ) follows from the difference of the electrochemical Gibbs free energies of the CO-covered surface, the clean surface, and the solvated CO. This yields site-specific binding free energies as a function of voltage for the two electrolyte conditions.

## Reproduction target
Compute the CO binding free energies for atop, bridge, and hollow sites on Cu(100) at the voltages -0.5, -0.75, -1.0, -1.25, -1.5 V/RHE for 0.1 M KCl (pH 7) and 0.1 M KOH (pH 13). Produce a CSV file `/app/outputs/binding_energies_cu100.csv` with columns pH, voltage_V_RHE, site, delta_G_b_eV. The verifier will evaluate the energies against a hidden reference, check relative site preferences as a function of voltage and pH, and assign a score based on the agreement.

## Assets

- Quantum ESPRESSO with ESM-RISM module: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP or GBRV): https://www.materialscloud.org/discover/sssp/table/efficiency
- BEEF-vdw exchange-correlation functional (LibXC): https://www.tddft.org/programs/libxc/
- Copper bulk crystal structure

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Construct a Cu(100) surface slab model and define the atop, bridge, and hollow CO adsorption sites. Create ESM-RISM input files for the 0.1 M KCl (pH 7) and 0.1 M KOH (pH 13) electrolytes, specifying ion concentrations and the solvated CO molecule.
- Evidence: none

### Step 2: ESM-RISM DFT grand potential calculations
- Role: process
- Action: Run grand-canonical DFT calculations with Quantum ESPRESSO, ESM-RISM, and BEEF-vdw for the clean Cu(100) surface, CO-covered surfaces (atop, bridge, hollow), and solvated CO at the voltages -0.5, -0.75, -1.0, -1.25, -1.5 V/RHE for both electrolyte conditions. Extract the electronic grand potential Ω(Φ) for each configuration.
- Evidence: `/app/outputs/grand_potentials.json`

### Step 3: Vibrational and thermodynamic corrections
- Role: process
- Action: Compute vibrational frequencies for adsorbed CO on each site and for solvated CO. Determine zero-point energies, vibrational entropies (adsorbed CO) and rotational/translational entropies (solvated CO), and heat capacity corrections. Calculate the free energy of solvated CO (G_CO).
- Evidence: `/app/outputs/thermo_corrections.json`

### Step 4: Binding free energy assembly and output
- Role: scored (load-bearing)
- Action: For each voltage and pH condition, compute the CO binding free energy ΔG_b(Φ) = G_CO*(Φ) - G_*(Φ) - G_CO, where G_CO*(Φ) = Ω_CO*(Φ) + ZPE + ∫C_v dT - T S, G_*(Φ) = Ω_*(Φ), and G_CO is the free energy of solvated CO. Write the results to /app/outputs/binding_energies_cu100.csv.
- Output file: `/app/outputs/binding_energies_cu100.csv`
- Format: csv
- Contract: Columns: pH (integer), voltage_V_RHE (float), site (string, values: atop/bridge/hollow), delta_G_b_eV (float). Each row corresponds to one site at one voltage and one pH.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies_cu100.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies_cu100.csv
- path: `/app/outputs/binding_energies_cu100.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CO binding free energies for atop, bridge, hollow sites on Cu(100) as a function of voltage and pH.
- schema:
  - `type`: table
  - `required_columns`: `pH`, `voltage_V_RHE`, `site`, `delta_G_b_eV`
  - `units`:
    - `voltage_V_RHE`: V
    - `delta_G_b_eV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies_cu100.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pH",
          "voltage_V_RHE",
          "site",
          "delta_G_b_eV"
        ],
        "units": {
          "voltage_V_RHE": "V",
          "delta_G_b_eV": "eV"
        }
      },
      "description": "CO binding free energies for atop, bridge, hollow sites on Cu(100) as a function of voltage and pH."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be scored by a hidden verifier that reads your output artifacts. The main scoring is based on the accuracy of the binding free energies in `binding_energies_cu100.csv` relative to a hidden reference, including the relative ordering of sites at different voltages and pH values. The intermediate files `grand_potentials.json` and `thermo_corrections.json` are generated as part of the workflow but are not directly scored. The final reward is a weighted combination across these components.
