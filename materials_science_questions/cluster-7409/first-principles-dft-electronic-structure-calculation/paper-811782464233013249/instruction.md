# DFT Band Gap and Midgap States in 3d-Substituted Bi2Ti2O7 Pyrochlore

## Problem background
Efficient solar water splitting requires photocatalysts with strong visible-light absorption and suitable band-edge positions. Bismuth titanate pyrochlore (Bi₂Ti₂O₇, BTO) is a candidate because its Bi 6s orbitals can raise the valence band maximum, potentially reducing the band gap compared to wide-gap oxides like TiO₂. Introducing 3d transition metals at the Ti site may further tune the electronic structure by creating midgap states, but the systematic effect of different 3d substituents on the band gap and midgap formation has not been established from first principles. Understanding how the band gap and the presence of midgap states vary with the identity of the substituent is central to designing more efficient pyrochlore photocatalysts.

## Approach
Use density functional theory (DFT) with a plane-wave basis set and a generalized gradient approximation (GGA) functional to describe electron exchange and correlation. First, construct the primitive unit cell of stoichiometric Bi₂Ti₂O₇ in the pyrochlore structure and relax all atomic coordinates. From the relaxed structure, compute the total density of states (TDOS) to identify the valence-band maximum and conduction-band minimum; report the full TDOS over an energy window that captures both bands and the Fermi level. Next, for each 3d transition metal M in {V, Cr, Mn, Fe, Ni}, build a supercell that replaces 25% of the Ti sites with M, yielding Bi₂Ti₁.₅M₀.₅O₇. Relax each substituted structure, compute its TDOS, and extract the electronic band gap (the energy range with negligible DOS between the highest occupied and lowest unoccupied states) as well as whether any additional DOS peaks appear inside that gap (midgap states). The pure BTO system serves as the baseline against which the changes induced by substitution are assessed.

## Reproduction target
Compute the electronic band gap of pure Bi₂Ti₂O₇ from its total density of states. For each of the five substituted systems (Bi₂Ti₁.₅M₀.₅O₇, M = V, Cr, Mn, Fe, Ni), compute its band gap and determine whether midgap states are present. Additionally, compute the optical absorption onset wavelengths for pure BTO and for anatase TiO₂ (using a suitable TiO₂ structure). The primary validation is that the computed band gaps and midgap presence for the substituted systems show expected trends, and that the optical absorption onset of BTO is red‑shifted relative to TiO₂, consistent with enhanced visible‑light absorption. Provide the required CSV files as specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare pure BTO unit cell
- Role: process
- Action: Construct the primitive unit cell of Bi2Ti2O7 pyrochlore using space group Fd-3m (No. 227), lattice constant a=10.2978 Å, and atomic positions: Bi at 16c, Ti at 16d, O1 at 48f (x≈0.375,1/8,1/8), O2 at 8a. Save the structure in a format suitable for DFT calculation.
- Evidence: `/app/outputs/pure_BTO_structure.cif`

### Step 2: DFT geometry optimization of pure BTO
- Role: process
- Action: Perform geometry optimization of the pure BTO primitive cell using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO). Use a GGA-PW91 (or equivalent) functional with a moderate plane-wave cutoff and k-point mesh to relax atomic coordinates until forces are small. Save the optimized structure.
- Evidence: `/app/outputs/pure_BTO_opt.out`

### Step 3: Compute total density of states of pure BTO
- Role: scored (load-bearing)
- Action: Using the optimized pure BTO structure, run a self-consistent field (SCF) calculation followed by a non-self-consistent (NSCF) calculation on a denser k-point grid to obtain the total density of states (TDOS). Align the energy zero to the Fermi level. Output the TDOS as a CSV file covering at least -10 eV to +10 eV relative to the Fermi level.
- Output file: `/app/outputs/pure_BTO_dos.csv`
- Format: csv
- Contract: Two columns: energy (float, eV relative to Fermi), total_dos (float, states/eV).
- Scoring: scored by hidden verifier

### Step 4: Generate and optimize substituted BTO structures
- Role: process
- Action: For each 3d transition metal M in {V, Cr, Mn, Fe, Ni}: (a) create a supercell from the optimized pure BTO structure to obtain multiple Ti sites; (b) replace one Ti atom with M to achieve composition Bi2Ti1.5M0.5O7; (c) perform geometry optimization using the same DFT settings as for pure BTO. Store the final optimized geometries.
- Evidence: `/app/outputs/substituted_BTO_opt.log`

### Step 5: Extract band gaps and midgap presence for substituted BTO
- Role: scored (load-bearing)
- Action: Compute the total density of states for each optimized substituted system (using SCF+NSCF with same DFT settings). From each TDOS, determine the electronic band gap (energy interval between the highest occupied and lowest unoccupied state) and check whether additional DOS peaks appear within the gap (midgap states). Compile the results into a CSV file with columns: system, band_gap (eV), midgap_state_flag (boolean).
- Output file: `/app/outputs/substituted_BTO_bandgaps.csv`
- Format: csv
- Contract: Columns: system (string, e.g. 'Bi2Ti1.5V0.5O7'), band_gap (float, eV), midgap_state_flag (boolean).
- Scoring: scored by hidden verifier

### Step 6: Compute optical absorption onset wavelengths
- Role: scored
- Action: Using the optimized pure BTO structure and an optimized anatase TiO₂ structure (obtain the anatase TiO₂ primitive cell from a standard source, e.g. ICSD # 82080; relax it with the same DFT settings), compute the optical absorption spectrum for both materials. From each spectrum determine the onset wavelength (the wavelength at which absorption rises above a threshold). Output a CSV file with columns: system (string), onset_wavelength_nm (float). Provide onset wavelengths for "BTO" and "TiO2_anatase".
- Output file: `/app/outputs/optical_absorption.csv`
- Format: csv
- Contract: Two columns: system (string, either "BTO" or "TiO2_anatase"), onset_wavelength_nm (float, in nm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pure_BTO_dos.csv`
- `/app/outputs/substituted_BTO_bandgaps.csv`
- `/app/outputs/optical_absorption.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pure_BTO_dos.csv
- path: `/app/outputs/pure_BTO_dos.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total density of states of pure BTO, from which the electronic band gap is recomputed.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`
  - `units`:
    - `energy`: eV
    - `total_dos`: states/eV

### substituted_BTO_bandgaps.csv
- path: `/app/outputs/substituted_BTO_bandgaps.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gaps and midgap state flags for each 3d-substituted BTO system; used to verify gap reduction and midgap state formation.
- schema:
  - `type`: table
  - `required_columns`: `system`, `band_gap`, `midgap_state_flag`
  - `units`:
    - `band_gap`: eV

Notes: Optical absorption spectra and PDOS are omitted as they are not required to verify the midgap-state and gap-reduction claims. The checker recomputes the pure BTO band gap from the TDOS and compares it to an expected value; for substituted systems, it checks that all gaps are smaller than the recomputed pure gap, that Fe has the smallest gap, and that all midgap flags are true.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pure_BTO_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos"
        ],
        "units": {
          "energy": "eV",
          "total_dos": "states/eV"
        }
      },
      "description": "Total density of states of pure BTO, from which the electronic band gap is recomputed."
    },
    {
      "file": "substituted_BTO_bandgaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "band_gap",
          "midgap_state_flag"
        ],
        "units": {
          "band_gap": "eV"
        }
      },
      "description": "Band gaps and midgap state flags for each 3d-substituted BTO system; used to verify gap reduction and midgap state formation."
    }
  ],
  "notes": "Optical absorption spectra and PDOS are omitted as they are not required to verify the midgap-state and gap-reduction claims. The checker recomputes the pure BTO band gap from the TDOS and compares it to an expected value; for substituted systems, it checks that all gaps are smaller than the recomputed pure gap, that Fe has the smallest gap, and that all midgap flags are true."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the CSV artifacts you write to `/app/outputs`. For the pure BTO stage, the verifier recomputes the electronic band gap from `pure_BTO_dos.csv` and compares it to an expected range derived from the literature. For the substituted systems, the verifier reads `substituted_BTO_bandgaps.csv` and evaluates the band gaps and midgap state flags against expected electronic‑structure trends. For the optical absorption step, the verifier reads `optical_absorption.csv` and checks the onset wavelength of pure BTO relative to anatase TiO₂ to verify a red‑shift consistent with enhanced visible‑light absorption. The final reward is a weighted combination of these checks; reporting a number without producing the required CSV artifacts will not receive credit.
