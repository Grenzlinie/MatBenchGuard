# DFT Study of Ni-Doped Spinel Mg1.5Ni0.5TiO4: Electronic Structure, Redox Activity, and Deintercalation Voltage

## Problem background
Mg2TiO4 is a spinel oxide that is electrochemically inactive. Partial substitution of tetrahedral Mg by Ni to form Mg1.5Ni0.5TiO4 may introduce redox-active centers, potentially enabling its use as a cathode material for Mg-ion batteries. First‑principles density‑functional‑theory (DFT) calculations can be used to compute the de‑intercalation voltage upon removal of tetrahedral Mg, the Ni magnetic moments that fingerprint the oxidation state of Ni, and the formation energies of the doped phase from precursor oxides. These computed quantities are the target of the reproduction effort — they must be derived from the DFT results and written to the final output file.

## Approach
The reproduction uses DFT within the GGA+U formalism, applying Hubbard‑U corrections on the d orbitals of Ni (Ueff = 6 eV) and Ti (Ueff = 3 eV for TiO2 polymorphs) to account for strong electron correlation. The workflow begins by constructing the crystal structures of the parent spinel Mg2TiO4 (space group Fd‑3m, lattice parameter about 8.482 Å), the Ni‑doped Mg1.5Ni0.5TiO4 (by replacing half of the tetrahedral Mg with Ni), and the de‑intercalated product MgNi0.5TiO4 (by removing the remaining tetrahedral Mg). Total energies and Ni atomic magnetic moments are obtained from self‑consistent field (SCF) calculations after geometry optimization for each of these three materials. In addition, SCF calculations are performed on the precursor oxides MgO, NiO, rutile TiO2, and anatase TiO2. From the DFT total energies, the de‑intercalation voltage V is computed as V = [E(Mg1.5Ni0.5TiO4) − E(MgNi0.5TiO4) − 0.5 μ(Mg metal)] / (0.5 F), where F is Faraday's constant and μ(Mg metal) is the chemical potential of Mg metal in its standard reference state. The formation energy per formula unit of Mg1.5Ni0.5TiO4 is calculated from the reaction stoichiometry Ef = [E(Mg12Ni4Ti8O32) − 12 E(MgO) − 4 E(NiO) − 4 E(Ti2O4)] / 8, with E(Ti2O4) taken for both rutile and anatase TiO2. All calculations are performed with an open‑source plane‑wave DFT code (Quantum ESPRESSO) using pseudopotentials from the SSSP library.

## Reproduction target
The target is to produce a JSON file, /app/outputs/computed_properties.json, containing five numeric quantities computed from the DFT calculations: the de‑intercalation voltage (in V) for the removal of 0.5 Mg from Mg1.5Ni0.5TiO4 to form MgNi0.5TiO4; the Ni magnetic moments (in μB) in both Mg1.5Ni0.5TiO4 and MgNi0.5TiO4; and the formation energies (in eV per formula unit) of Mg1.5Ni0.5TiO4 with rutile and anatase TiO2 as precursors. All values must be derived from the DFT runs described in the workflow steps and written to the JSON file with the exact keys specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency or precision): https://www.materialscloud.org/discover/sssp/table/efficiency
- Spinel Mg2TiO4 crystal structure reference

## Workflow steps

### Step 1: Construct crystal structures
- Role: process
- Action: Construct the initial unit cells for spinel Mg2TiO4, Mg1.5Ni0.5TiO4 (substituting 4 of the 8 tetrahedral Mg with Ni), and MgNi0.5TiO4 (removing remaining tetrahedral Mg from the doped structure). The parent structure has space group Fd-3m with approximate lattice parameter 8.482 Å.
- Evidence: none

### Step 2: DFT calculations for Mg1.5Ni0.5TiO4
- Role: process
- Action: Perform GGA+U geometry optimization followed by a self-consistent field (SCF) calculation on the Mg1.5Ni0.5TiO4 cell. Use a Hubbard U correction on Ni d states. Obtain the total energy and the Ni atomic magnetic moment.
- Evidence: `/app/outputs/dft_Mg15Ni05TiO4_out.txt`

### Step 3: DFT calculations for MgNi0.5TiO4
- Role: process
- Action: Perform GGA+U geometry optimization and SCF on the MgNi0.5TiO4 cell (tetragonal after Mg removal). Use Hubbard U on Ni d states. Obtain total energy and the Ni atomic magnetic moment.
- Evidence: `/app/outputs/dft_MgNi05TiO4_out.txt`

### Step 4: DFT calculations for precursor oxides
- Role: process
- Action: Perform SCF calculations on MgO (Fm-3m), NiO (Fm-3m, GGA+U on Ni d), rutile TiO2 (P4_2/mnm, GGA+U on Ti d), and anatase TiO2 (I4_1/amd, GGA+U on Ti d). Obtain the total energy for each compound.
- Evidence: `/app/outputs/dft_precursors_out.txt`

### Step 5: Compute target properties
- Role: scored (load-bearing)
- Action: Using the total energies and magnetic moments from the previous DFT runs, compute: (a) the de-intercalation voltage V = [E(Mg1.5Ni0.5TiO4) – E(MgNi0.5TiO4) – 0.5*μ(Mg metal)] / (0.5*F), where F is Faraday's constant and μ(Mg metal) is the chemical potential of Mg metal in its standard reference state; (b) the Ni magnetic moments in Bohr magnetons; (c) the formation energy per formula unit of Mg1.5Ni0.5TiO4 with rutile and anatase TiO2 using the stoichiometric relations (formation energy = E(Mg12Ni4Ti8O32) – 12E(MgO) – 4E(NiO) – 4E(Ti2O4), then divided by 8). Write the results as a JSON object to /app/outputs/computed_properties.json.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: object with keys: deintercalation_voltage (float V), magnetic_moment_Mg15Ni05TiO4 (float μB), magnetic_moment_MgNi05TiO4 (float μB), formation_energy_rutile (float eV/formula unit), formation_energy_anatase (float eV/formula unit)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored JSON file containing the computed de-intercalation voltage, Ni magnetic moments, and formation energies of Mg1.5Ni0.5TiO4 per formula unit.
- schema:
  - `type`: object
  - `required`: `deintercalation_voltage`, `magnetic_moment_Mg15Ni05TiO4`, `magnetic_moment_MgNi05TiO4`, `formation_energy_rutile`, `formation_energy_anatase`
  - `units`:
    - `deintercalation_voltage`: V
    - `magnetic_moment_Mg15Ni05TiO4`: μB
    - `magnetic_moment_MgNi05TiO4`: μB
    - `formation_energy_rutile`: eV/formula unit
    - `formation_energy_anatase`: eV/formula unit

Notes: All quantities are computed from DFT total energies and magnetic moments obtained using an open-source code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials. The chemical potential of Mg metal can be taken from a standard reference or computed. The formation energies use total energies of the precursor oxides per the paper's reaction stoichiometry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "deintercalation_voltage",
          "magnetic_moment_Mg15Ni05TiO4",
          "magnetic_moment_MgNi05TiO4",
          "formation_energy_rutile",
          "formation_energy_anatase"
        ],
        "units": {
          "deintercalation_voltage": "V",
          "magnetic_moment_Mg15Ni05TiO4": "μB",
          "magnetic_moment_MgNi05TiO4": "μB",
          "formation_energy_rutile": "eV/formula unit",
          "formation_energy_anatase": "eV/formula unit"
        }
      },
      "description": "Scored JSON file containing the computed de-intercalation voltage, Ni magnetic moments, and formation energies of Mg1.5Ni0.5TiO4 per formula unit."
    }
  ],
  "notes": "All quantities are computed from DFT total energies and magnetic moments obtained using an open-source code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials. The chemical potential of Mg metal can be taken from a standard reference or computed. The formation energies use total energies of the precursor oxides per the paper's reaction stoichiometry."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/computed_properties.json and compares each field to a confidential reference value. Each quantity is scored independently using an appropriate tolerance; reporting the paper's numbers is not sufficient — the submitted JSON must be the result of genuine DFT calculations as outlined in the workflow. The total reward is the weighted sum of the scores for the five quantities. The exact tolerances and weights are not disclosed, but obtaining correct computed values from the DFT pipeline is essential to achieve a high reward.
