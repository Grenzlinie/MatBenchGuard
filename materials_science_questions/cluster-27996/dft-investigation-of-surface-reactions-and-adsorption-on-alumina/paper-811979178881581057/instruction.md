# DFT Simulation of Methanol Decomposition on β-Ga2O3 Tetrahedral Site

## Problem background
Understanding how methanol decomposes on defect‑free β‑Ga₂O₃ (100) surfaces is important for designing selective catalysts for hydrogen production. This work uses density functional theory (DFT) to investigate the oxidative decomposition of methanol on tetrahedral gallium sites, which produces formaldehyde. The target is to computationally determine the strength of the formaldehyde–surface interaction, the structural changes in the adsorbed molecule, the charge transfer, and the characteristic vibrational signatures — all quantities that can be reproduced by a computational simulation.

## Approach
Use density functional theory with the B3LYP hybrid exchange‑correlation functional. Model the tetrahedral (T0) surface site with a stoichiometric Ga₁₄O₂₁ cluster constructed from the bulk β‑Ga₂O₃ crystal structure; the cluster exposes a central oxygen atom coordinated to tetrahedral gallium atoms of the first layer. The oxide oxygen atoms are described with a 6‑31G basis set, the gallium atoms are treated with a small‑core effective core potential (ECP), and the methanol molecule is treated at the all‑electron level with the 6‑31G** basis set.

First, obtain reference total energies for the isolated methanol molecule (all‑electron 6‑31G**) and for the bare T0 cluster (O atoms 6‑31G, Ga atoms small‑core ECP). Then simulate the oxidative decomposition pathway on the cluster: the methanol molecule approaches the surface, a methyl hydrogen transfers to a neighbouring surface oxygen, the alcoholic hydrogen transfers to the central oxygen, and the system relaxes to a final complex in which formaldehyde (H₂CO) is bound to the surface. Fully optimize this final complex and record its total energy.

Compute the adsorption energy as the difference between the total energy of the complex and the sum of the reference energies of the isolated methanol and the bare cluster. Extract the C–H and C=O bond lengths and the H–C–H angle of the adsorbed H₂CO. Perform Natural Bond Orbital (NBO) population analysis on the complex to obtain the net atomic charge on the H₂CO fragment. Compute harmonic vibrational frequencies for the adsorbed H₂CO and apply a uniform scaling factor of 0.97 to obtain the scaled fundamental frequencies. The key vibrational modes to report are the antisymmetric and symmetric C–H stretches, the C=O stretch, and the symmetric CH₂ bending mode.

## Reproduction target
For the Ga₁₄O₂₁ cluster model that represents the tetrahedral T0 site on the β‑Ga₂O₃ (100) surface, compute and report in `/app/outputs/results.json` the following quantities:

- adsorption energy of the H₂CO‑bound complex (eV)
- C–H and C=O bond lengths (Å) and H–C–H angle (degrees) of the adsorbed H₂CO
- NBO net charge on the H₂CO fragment (e)
- the four scaled vibrational fundamentals of adsorbed H₂CO: νₐₛ(CH), νₛ(CH), ν(CO), and δₛ(CH₂) (cm⁻¹)

All values must be obtained by executing the full DFT workflow described in the steps below; the hidden verifier will compare your reported numbers against the expected reproduction target.

## Assets

- ORCA quantum chemistry package (open-source): https://orcaforum.kofo.mpg.de/
- β-Ga2O3 bulk crystal structure (CIF file): https://www.crystallography.net/cod/151072.html

## Workflow steps

### Step 1: Build T0 cluster model
- Role: process
- Action: From the bulk β-Ga2O3 crystal structure (COD 151072), construct the Ga14O21 cluster model representing the defect-free tetrahedral T0 site (central oxygen linked to tetrahedral Ga atoms of the first layer). Save the cluster atomic coordinates in XYZ format.
- Evidence: `/app/outputs/cluster.xyz`

### Step 2: Reference calculations for isolated fragments
- Role: process
- Action: Perform DFT geometry optimization and single-point energy calculation at the B3LYP level: (i) isolated methanol molecule with all-electron 6-31G** basis; (ii) bare T0 cluster (O atoms 6-31G, Ga atoms small-core ECP). Save the total energies of methanol and the bare cluster to a text file.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 3: Methanol decomposition simulation on T0 cluster
- Role: process
- Action: Using DFT/B3LYP with the same basis/ECP settings, simulate the oxidative decomposition pathway of methanol on the T0 cluster: approach, methyl H transfer to surface O, alcoholic H transfer to central O, yielding the H2CO-bound final complex. Fully optimize the final complex and save its geometry and total energy.
- Evidence: `/app/outputs/final_energy.txt`

### Step 4: Vibrational frequency and NBO charge analysis
- Role: process
- Action: On the final H2CO-bound complex, compute harmonic vibrational frequencies (scale by 0.97) and perform Natural Bond Orbital (NBO) population analysis to obtain the net atomic charge on the H2CO fragment. Save the relevant frequencies and NBO charges to a JSON file.
- Evidence: `/app/outputs/analysis_results.json`

### Step 5: Collect and report T0 site results
- Role: scored (load-bearing)
- Action: From reference_energies.txt, final_energy.txt, final_complex.xyz, and analysis_results.json, compute the adsorption energy as E(total) - E(bare cluster) - E(isolated methanol), extract the C-H and C-O bond lengths and H-C-H angle of adsorbed H2CO, the NBO net charge, and the four scaled vibrational frequencies. Write all values into /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"adsorption_energy_eV": <number>, "C-H_bond_length_angstrom": <number>, "C-O_bond_length_angstrom": <number>, "H-C-H_angle_degrees": <number>, "NBO_charge_H2CO_e": <number>, "vas_CH_cm-1": <number>, "vs_CH_cm-1": <number>, "v_CO_cm-1": <number>, "ds_CH2_cm-1": <number>}
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
- description: Final reproduction artifact containing the adsorption energy, geometric parameters, NBO charge, and scaled vibrational frequencies of the adsorbed H2CO on the T0 cluster. The checker compares each field to the paper's reported values using appropriate tolerances and rules (adsorption energy threshold-or-better, other fields exact-within-tolerance).
- schema:
  - `type`: object
  - `required`:
    - `adsorption_energy_eV`: float (eV)
    - `C-H_bond_length_angstrom`: float (Å)
    - `C-O_bond_length_angstrom`: float (Å)
    - `H-C-H_angle_degrees`: float (°)
    - `NBO_charge_H2CO_e`: float (e)
    - `vas_CH_cm-1`: float (cm⁻¹)
    - `vs_CH_cm-1`: float (cm⁻¹)
    - `v_CO_cm-1`: float (cm⁻¹)
    - `ds_CH2_cm-1`: float (cm⁻¹)

Notes: Only the T0 (tetrahedral) site results are required. The O0 site is excluded per task scope. All numeric fields will be compared to the paper-reported values with hidden tolerances.

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
        "required": {
          "adsorption_energy_eV": "float (eV)",
          "C-H_bond_length_angstrom": "float (Å)",
          "C-O_bond_length_angstrom": "float (Å)",
          "H-C-H_angle_degrees": "float (°)",
          "NBO_charge_H2CO_e": "float (e)",
          "vas_CH_cm-1": "float (cm⁻¹)",
          "vs_CH_cm-1": "float (cm⁻¹)",
          "v_CO_cm-1": "float (cm⁻¹)",
          "ds_CH2_cm-1": "float (cm⁻¹)"
        }
      },
      "description": "Final reproduction artifact containing the adsorption energy, geometric parameters, NBO charge, and scaled vibrational frequencies of the adsorbed H2CO on the T0 cluster. The checker compares each field to the paper's reported values using appropriate tolerances and rules (adsorption energy threshold-or-better, other fields exact-within-tolerance)."
    }
  ],
  "notes": "Only the T0 (tetrahedral) site results are required. The O0 site is excluded per task scope. All numeric fields will be compared to the paper-reported values with hidden tolerances."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and independently scores each of the nine required fields against a reference target derived from the paper. The adsorption energy is evaluated on a threshold‑or‑better basis: meeting or exceeding the target earns full credit, and credit only degrades for a result that is worse. The geometric parameters, NBO charge, and vibrational frequencies are compared to the reference values within numerical tolerances that account for the spread of a legitimate independent DFT re‑run. The overall reward (a floating‑point value between 0 and 1) combines the per‑field scores. Producing the correct values requires genuinely running the computational steps; fabricated numbers or guesses are not rewarded.
