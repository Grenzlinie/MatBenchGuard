# DFT vibrational frequencies and binding energies of *OCHCH2 on distorted Cu sites

## Problem background
Electrochemical reduction of CO2 (CO2RR) to multi-carbon products like ethylene and ethanol offers a way to store renewable energy in chemical bonds. Copper is the most selective catalyst, but the mechanisms that control the branching between ethylene and ethanol are not well understood. A key aspect is the stabilization of specific reaction intermediates on different Cu surface sites. In particular, the intermediate *OCHCH2 has been proposed as the last common precursor before the pathway splits toward ethylene or ethanol, and its adsorption on distorted Cu sites with low coordination and compressive strain is thought to open the ethanol route. This task reproduces a core DFT calculation: the vibrational fingerprint and binding energy of *OCHCH2 on a representative distorted Cu site, providing a quantitative benchmark for the computational claim that such sites stabilize this intermediate.

## Approach
The computation uses plane-wave density functional theory (DFT) to model a Cu slab with the adsorbed *OCHCH2 intermediate. The key ingredients are the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional, Grimme's D2 dispersion correction, projector augmented wave (PAW) pseudopotentials, and an implicit solvation model (e.g., VASPsol, Environ, or equivalent). The atomic coordinates for the Cu site OD-Cu-297 and the adsorbed intermediate are taken from a publicly deposited dataset (DOI: 10.19061/iochem-bd-1-251). The calculation proceeds by first preparing input files for the adsorbed system, the clean Cu slab, and the gas-phase reference molecules (CO2, H2, H2O). A vibrational frequency calculation is then performed to obtain harmonic frequencies; the four modes associated with the CCO backbone are extracted. Separately, the total energies of the clean slab and the gas-phase references are computed with the same settings, and the binding/formation energy of *OCHCH2 is evaluated relative to those references. The results are written to two CSV files as specified in the workflow steps.

## Reproduction target
Perform DFT calculations to determine the harmonic vibrational frequencies of the *OCHCH2 intermediate adsorbed on the Cu site labelled OD-Cu-297 (a site with a Cu–Cu coordination number of 5.00). Specifically, extract the frequencies (in cm⁻¹) for the four CCO-related modes: CCO symmetric stretching, CCO antisymmetric stretching, C–C stretching, and C–O (or C=C) stretching. Also compute the binding energy of *OCHCH2 relative to a clean Cu slab and gas-phase CO2, H2, and H2O, and report the binding energy in eV. Save the vibrational frequencies to `/app/outputs/vibrational_frequencies.csv` and the binding energy to `/app/outputs/binding_energies.csv`, following the exact column schemas given in the workflow steps.

## Assets

- DFT-optimized structures of Cu surfaces and CO2RR intermediates (ioChem-BD): https://doi.org/10.19061/iochem-bd-1-251
- Plane-wave DFT code (e.g., Quantum Espresso, GPAW, ABINIT)

## Workflow steps

### Step 1: Prepare DFT inputs
- Role: process
- Action: Download the optimized geometry for the *OCHCH2 intermediate on the OD-Cu-297 site from ioChem-BD (DOI: 10.19061/iochem-bd-1-251). Convert the atomic coordinates to the input format of the chosen DFT code. Prepare input files for the adsorbed system, the clean Cu slab, and the gas-phase reference molecules (CO2, H2, H2O). Set calculation parameters consistent with the paper's methods: PBE functional, DFT-D2 dispersion, PAW pseudopotentials, implicit solvation, kinetic energy cutoff, and k-point mesh.
- Evidence: `/app/outputs/dft_input_preparation.log`

### Step 2: Vibrational frequency calculation
- Role: scored (load-bearing)
- Action: Run the DFT vibrational frequency calculation for the *OCHCH2/OD-Cu-297 system using the prepared input. Parse the output to extract harmonic frequencies for the four key CCO-related vibrational modes: CCO symmetric stretching, CCO antisymmetric stretching, C-C stretching, and C-O (or C=C) stretching. Write the results to a CSV file.
- Output file: `/app/outputs/vibrational_frequencies.csv`
- Format: csv
- Contract: intermediate (str), site_label (str), mode (str), frequency_cm-1 (float)
- Scoring: scored by hidden verifier

### Step 3: Binding energy calculation
- Role: scored (load-bearing)
- Action: Run DFT total energy calculations for the clean slab and the gas-phase references (CO2, H2, H2O) using the same parameters. Determine the formation/binding energy of *OCHCH2 relative to these references. Write the binding energy (in eV) to a CSV file.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: intermediate (str), site_label (str), binding_energy_eV (float), formation_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vibrational_frequencies.csv`
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vibrational_frequencies.csv
- path: `/app/outputs/vibrational_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the four vibrational mode frequencies for *OCHCH2 on OD-Cu-297, as computed by DFT.
- schema:
  - `type`: table
  - `required_columns`: `intermediate`, `site_label`, `mode`, `frequency_cm-1`
  - `units`:
    - `frequency_cm-1`: cm^-1

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the binding and formation energy of *OCHCH2 on OD-Cu-297, as computed by DFT.
- schema:
  - `type`: table
  - `required_columns`: `intermediate`, `site_label`, `binding_energy_eV`, `formation_energy_eV`
  - `units`:
    - `binding_energy_eV`: eV
    - `formation_energy_eV`: eV

Notes: The hidden checker compares the reported frequencies and binding energy to the paper's gold values for site OD-Cu-297 within tolerances that absorb code-to-code differences (vibrational tolerance 10 cm⁻¹, energy tolerance 0.15 eV).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vibrational_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "intermediate",
          "site_label",
          "mode",
          "frequency_cm-1"
        ],
        "units": {
          "frequency_cm-1": "cm^-1"
        }
      },
      "description": "CSV file containing the four vibrational mode frequencies for *OCHCH2 on OD-Cu-297, as computed by DFT."
    },
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "intermediate",
          "site_label",
          "binding_energy_eV",
          "formation_energy_eV"
        ],
        "units": {
          "binding_energy_eV": "eV",
          "formation_energy_eV": "eV"
        }
      },
      "description": "CSV file containing the binding and formation energy of *OCHCH2 on OD-Cu-297, as computed by DFT."
    }
  ],
  "notes": "The hidden checker compares the reported frequencies and binding energy to the paper's gold values for site OD-Cu-297 within tolerances that absorb code-to-code differences (vibrational tolerance 10 cm⁻¹, energy tolerance 0.15 eV)."
}
```

## How you are scored
After you submit your output files, a hidden verifier reads `vibrational_frequencies.csv` and `binding_energies.csv` and compares the reported values to reference values obtained from the original study. The verifier checks each vibrational mode against a hidden tolerance and compares the binding energy against a hidden tolerance. The final reward is a weighted sum: partial credit is given for each mode within its tolerance band and for the binding energy within its tolerance, with the total capped at 1.0. The tolerances are chosen to absorb typical variations due to the choice of DFT code, pseudopotentials, and solvation model. You do not need to replicate the exact numbers from the original VASP calculation; any open-source DFT code that faithfully implements the specified functional and dispersion model can achieve the reward.
