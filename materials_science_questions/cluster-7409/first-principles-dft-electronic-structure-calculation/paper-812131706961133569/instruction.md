# DFT structural and electronic properties of SnO2 polymorphs

## Problem background
Tin dioxide (SnO2) is a wide-band-gap semiconductor used in gas sensors, solar cells, and catalysis. At ambient conditions it crystallizes in the rutile structure; under hydrostatic pressure it transforms first to an orthorhombic CaCl2-type phase and then to a cubic pa-3 phase. Accurate first-principles determination of the equilibrium structural parameters, bulk modulus, cohesive energy, electronic band gaps, and the phase-transition pressures is essential for understanding its behaviour under compression and for guiding device design. This task computes those quantities for the three polymorphs using density functional theory (DFT) within the local-density approximation (LDA) and the generalized gradient approximation (GGA), with an additional Engel–Vosko GGA (EVGGA) for band-gap calculations.

## Approach
The reproduction uses first-principles total-energy calculations within an open-source DFT code capable of full-potential or plane-wave/pseudopotential methods. The workflow is:
- Set up unit cells for rutile, CaCl2-type, and cubic SnO2 with the known space groups and initial atomic positions.
- Perform self-consistent total-energy calculations at several volumes around equilibrium using both LDA and GGA functionals, relaxing the internal coordinates (u, v) until forces are negligible.
- Fit the resulting energy-volume data to the Murnaghan equation of state to extract equilibrium lattice constants, internal parameters, bulk modulus, and the equilibrium total energy per cell.
- Compute isolated-atom total energies in large supercells to obtain the reference energies needed for cohesive energy, and then compute the cohesive energy per formula unit for each phase and functional.
- At the optimized equilibrium geometries, perform band-structure calculations with both GGA and EVGGA functionals and extract the direct band gap at the Γ point for each phase.
- From the fitted energy-volume curves, compute the enthalpy H = E + PV for each phase and determine the two phase-transition pressures (rutile→CaCl2-type and CaCl2-type→cubic) via the common-tangent condition.
- Aggregate all computed quantities into a single JSON file for scoring. The entire pipeline requires no external dataset; the crystal structures and the DFT protocol are public knowledge.

## Reproduction target
Compute the following physical quantities for the three SnO2 polymorphs (rutile, CaCl2-type, cubic pa-3) using LDA and GGA functionals:
- Equilibrium lattice constants (a, b, c) and internal coordinates (u, v as applicable) – in Å and dimensionless.
- Bulk modulus (in GPa).
- Cohesive energy per formula unit (in eV).
- Direct band gap at the Γ point using both GGA and EVGGA (in eV).
- Phase transition pressures: rutile→CaCl2-type and CaCl2-type→cubic (in GPa) from both LDA and GGA enthalpy curves.
All values must be written into the scored artifact /app/outputs/results.json using the field names and units defined in the output contract. The objective is to re-run the computational procedure and produce these properties; the hidden verifier will compare each against reference values obtained from the original paper.

## Assets

- DFT software (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Standard crystal structure data for SnO2 polymorphs

## Workflow steps

### Step 1: DFT total-energy calculations with geometry relaxation
- Role: process
- Action: For rutile, CaCl2-type, and cubic SnO2, set up unit cells with initial lattice parameters and atomic positions. Run DFT total-energy calculations at several volumes around equilibrium using both LDA and GGA functionals. Relax internal coordinates (u, v) with a damped Newton scheme until forces < 1.0 mRy/a.u. Output the total energy vs volume and the relaxed geometries at each volume.
- Evidence: `/app/outputs/energy_vs_volume.csv`

### Step 2: Equation-of-state fitting and equilibrium parameter extraction
- Role: process
- Action: Fit the total energy vs volume data for each phase/functional to the Murnaghan equation of state. Optimize c/a ratio for rutile and b/a ratio for CaCl2-type at constant volume. Extract the equilibrium lattice constants (a, b, c), internal coordinates (u, v), bulk modulus, and equilibrium total energy per cell.
- Evidence: none

### Step 3: Isolated atom energy calculations
- Role: process
- Action: Compute the total energy of an isolated Sn atom and an isolated O atom in large cubic supercells (18 a.u. and 19 a.u., respectively) using the same LDA and GGA functionals.
- Evidence: `/app/outputs/isolated_energies.txt`

### Step 4: Cohesive energy calculation
- Role: process
- Action: Subtract the sum of isolated atom energies from the equilibrium solid total energy (per SnO2 formula unit) for each phase and functional. Store the cohesive energies.
- Evidence: none

### Step 5: Band structure and band gap extraction
- Role: process
- Action: At the equilibrium geometries obtained in step 2, perform self-consistent electronic structure calculations and non‑self‑consistent band structure runs using GGA and also EVGGA. Identify the direct band gap at the Γ point for each phase and functional. Extract the numerical band gap value.
- Evidence: `/app/outputs/band_structure_data.npy`

### Step 6: Phase transition pressure determination
- Role: process
- Action: Using the fitted EOS energy-volume relations from step 2, compute the enthalpy H = E + PV for each phase. Determine the transition pressure from rutile to CaCl2-type and from CaCl2-type to cubic by locating the common tangent (equal enthalpies) between the phases.
- Evidence: none

### Step 7: Effective mass calculation
- Role: process
- Action: Using the band structure data from step 5, fit the conduction-band minimum and valence-band maximum energies around the Γ point to a parabolic E(k) = (ħ²k²)/(2 m*) relationship. Extract the electron effective mass (m_e*) and hole effective mass (m_h*) in units of the free-electron mass for each polymorph and each functional (GGA and EVGGA). Save the results in a table.
- Evidence: `/app/outputs/effective_masses.csv`

### Step 8: Ionization factor calculation
- Role: process
- Action: From the DFT charge density of the rutile phase at the equilibrium volume, extract the valence charge density in the (110) plane. Integrate the density on the anion side (S_A) and the cation side (S_C) of the bond centre. Compute the ionicity factor f_i = (S_A / (S_A + λ S_C))^λ with λ = +1 (since SnO₂ belongs to the II‑VI family). Perform this for both the LDA and GGA charge densities and store the two numbers.
- Evidence: `/app/outputs/ionicity_factor.txt`

### Step 9: Aggregate all results into scored JSON
- Role: scored (load-bearing)
- Action: Collect all computed values from previous steps: lattice constants (a, b, c), internal coordinates (u, v), bulk modulus, cohesive energy, band gaps, effective masses, ionicity factor, and phase transition pressures. Write them into a single JSON file /app/outputs/results.json. Include every key defined in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys: rutile_LDA_a (Å), rutile_LDA_c (Å), rutile_LDA_u (dimensionless), rutile_GGA_a, rutile_GGA_c, rutile_GGA_u, CaCl2_LDA_a, CaCl2_LDA_b, CaCl2_LDA_c, CaCl2_LDA_u, CaCl2_LDA_v, CaCl2_GGA_a, CaCl2_GGA_b, CaCl2_GGA_c, CaCl2_GGA_u, CaCl2_GGA_v, cubic_LDA_a, cubic_LDA_u, cubic_GGA_a, cubic_GGA_u, rutile_LDA_B (GPa), rutile_GGA_B, CaCl2_LDA_B, CaCl2_GGA_B, cubic_LDA_B, cubic_GGA_B, rutile_LDA_Ecoh (eV per f.u.), rutile_GGA_Ecoh, CaCl2_LDA_Ecoh, CaCl2_GGA_Ecoh, cubic_LDA_Ecoh, cubic_GGA_Ecoh, rutile_GGA_gap (eV), rutile_EVGGA_gap, CaCl2_GGA_gap, CaCl2_EVGGA_gap, cubic_GGA_gap, cubic_EVGGA_gap, P_trans_rutile_CaCl2_LDA (GPa), P_trans_rutile_CaCl2_GGA, P_trans_CaCl2_cubic_LDA, P_trans_CaCl2_cubic_GGA, rutile_GGA_m_e (dimensionless), rutile_GGA_m_h, rutile_EVGGA_m_e, rutile_EVGGA_m_h, CaCl2_GGA_m_e, CaCl2_GGA_m_h, CaCl2_EVGGA_m_e, CaCl2_EVGGA_m_h, cubic_GGA_m_e, cubic_GGA_m_h, cubic_EVGGA_m_e, cubic_EVGGA_m_h, rutile_LDA_ionicity (dimensionless), rutile_GGA_ionicity. All values are numbers.
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
- target_policy: exact_match
- description: Aggregated structural and electronic quantities, including lattice constants, internal parameters, bulk modulus, cohesive energy, energy gaps, effective masses, ionicity factor, and phase transition pressures for SnO₂ polymorphs.
- schema:
  - `type`: object
  - `required`: `rutile_LDA_a`, `rutile_LDA_c`, `rutile_LDA_u`, `rutile_GGA_a`, `rutile_GGA_c`, `rutile_GGA_u`, `CaCl2_LDA_a`, `CaCl2_LDA_b`, `CaCl2_LDA_c`, `CaCl2_LDA_u`, `CaCl2_LDA_v`, `CaCl2_GGA_a`, `CaCl2_GGA_b`, `CaCl2_GGA_c`, `CaCl2_GGA_u`, `CaCl2_GGA_v`, `cubic_LDA_a`, `cubic_LDA_u`, `cubic_GGA_a`, `cubic_GGA_u`, `rutile_LDA_B`, `rutile_GGA_B`, `CaCl2_LDA_B`, `CaCl2_GGA_B`, `cubic_LDA_B`, `cubic_GGA_B`, `rutile_LDA_Ecoh`, `rutile_GGA_Ecoh`, `CaCl2_LDA_Ecoh`, `CaCl2_GGA_Ecoh`, `cubic_LDA_Ecoh`, `cubic_GGA_Ecoh`, `rutile_GGA_gap`, `rutile_EVGGA_gap`, `CaCl2_GGA_gap`, `CaCl2_EVGGA_gap`, `cubic_GGA_gap`, `cubic_EVGGA_gap`, `P_trans_rutile_CaCl2_LDA`, `P_trans_rutile_CaCl2_GGA`, `P_trans_CaCl2_cubic_LDA`, `P_trans_CaCl2_cubic_GGA`, `rutile_GGA_m_e`, `rutile_GGA_m_h`, `rutile_EVGGA_m_e`, `rutile_EVGGA_m_h`, `CaCl2_GGA_m_e`, `CaCl2_GGA_m_h`, `CaCl2_EVGGA_m_e`, `CaCl2_EVGGA_m_h`, `cubic_GGA_m_e`, `cubic_GGA_m_h`, `cubic_EVGGA_m_e`, `cubic_EVGGA_m_h`, `rutile_LDA_ionicity`, `rutile_GGA_ionicity`
  - `properties`:
    - `rutile_LDA_a`:
      - `type`: number
      - `unit`: Å
    - `rutile_LDA_c`:
      - `type`: number
      - `unit`: Å
    - `rutile_LDA_u`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_GGA_a`:
      - `type`: number
      - `unit`: Å
    - `rutile_GGA_c`:
      - `type`: number
      - `unit`: Å
    - `rutile_GGA_u`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_LDA_a`:
      - `type`: number
      - `unit`: Å
    - `CaCl2_LDA_b`:
      - `type`: number
      - `unit`: Å
    - `CaCl2_LDA_c`:
      - `type`: number
      - `unit`: Å
    - `CaCl2_LDA_u`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_LDA_v`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_GGA_a`:
      - `type`: number
      - `unit`: Å
    - `CaCl2_GGA_b`:
      - `type`: number
      - `unit`: Å
    - `CaCl2_GGA_c`:
      - `type`: number
      - `unit`: Å
    - `CaCl2_GGA_u`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_GGA_v`:
      - `type`: number
      - `unit`: dimensionless
    - `cubic_LDA_a`:
      - `type`: number
      - `unit`: Å
    - `cubic_LDA_u`:
      - `type`: number
      - `unit`: dimensionless
    - `cubic_GGA_a`:
      - `type`: number
      - `unit`: Å
    - `cubic_GGA_u`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_LDA_B`:
      - `type`: number
      - `unit`: GPa
    - `rutile_GGA_B`:
      - `type`: number
      - `unit`: GPa
    - `CaCl2_LDA_B`:
      - `type`: number
      - `unit`: GPa
    - `CaCl2_GGA_B`:
      - `type`: number
      - `unit`: GPa
    - `cubic_LDA_B`:
      - `type`: number
      - `unit`: GPa
    - `cubic_GGA_B`:
      - `type`: number
      - `unit`: GPa
    - `rutile_LDA_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `rutile_GGA_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `CaCl2_LDA_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `CaCl2_GGA_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `cubic_LDA_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `cubic_GGA_Ecoh`:
      - `type`: number
      - `unit`: eV per formula unit
    - `rutile_GGA_gap`:
      - `type`: number
      - `unit`: eV
    - `rutile_EVGGA_gap`:
      - `type`: number
      - `unit`: eV
    - `CaCl2_GGA_gap`:
      - `type`: number
      - `unit`: eV
    - `CaCl2_EVGGA_gap`:
      - `type`: number
      - `unit`: eV
    - `cubic_GGA_gap`:
      - `type`: number
      - `unit`: eV
    - `cubic_EVGGA_gap`:
      - `type`: number
      - `unit`: eV
    - `P_trans_rutile_CaCl2_LDA`:
      - `type`: number
      - `unit`: GPa
    - `P_trans_rutile_CaCl2_GGA`:
      - `type`: number
      - `unit`: GPa
    - `P_trans_CaCl2_cubic_LDA`:
      - `type`: number
      - `unit`: GPa
    - `P_trans_CaCl2_cubic_GGA`:
      - `type`: number
      - `unit`: GPa
    - `rutile_GGA_m_e`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_GGA_m_h`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_EVGGA_m_e`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_EVGGA_m_h`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_GGA_m_e`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_GGA_m_h`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_EVGGA_m_e`:
      - `type`: number
      - `unit`: dimensionless
    - `CaCl2_EVGGA_m_h`:
      - `type`: number
      - `unit`: dimensionless
    - `cubic_GGA_m_e`:
      - `type`: number
      - `unit`: dimensionless
    - `cubic_GGA_m_h`:
      - `type`: number
      - `unit`: dimensionless
    - `cubic_EVGGA_m_e`:
      - `type`: number
      - `unit`: dimensionless
    - `cubic_EVGGA_m_h`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_LDA_ionicity`:
      - `type`: number
      - `unit`: dimensionless
    - `rutile_GGA_ionicity`:
      - `type`: number
      - `unit`: dimensionless

Notes: The effective masses and ionicity factor have been added as required by the reviewer. All fields are compared to hidden gold values with appropriate tolerances.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "rutile_LDA_a",
          "rutile_LDA_c",
          "rutile_LDA_u",
          "rutile_GGA_a",
          "rutile_GGA_c",
          "rutile_GGA_u",
          "CaCl2_LDA_a",
          "CaCl2_LDA_b",
          "CaCl2_LDA_c",
          "CaCl2_LDA_u",
          "CaCl2_LDA_v",
          "CaCl2_GGA_a",
          "CaCl2_GGA_b",
          "CaCl2_GGA_c",
          "CaCl2_GGA_u",
          "CaCl2_GGA_v",
          "cubic_LDA_a",
          "cubic_LDA_u",
          "cubic_GGA_a",
          "cubic_GGA_u",
          "rutile_LDA_B",
          "rutile_GGA_B",
          "CaCl2_LDA_B",
          "CaCl2_GGA_B",
          "cubic_LDA_B",
          "cubic_GGA_B",
          "rutile_LDA_Ecoh",
          "rutile_GGA_Ecoh",
          "CaCl2_LDA_Ecoh",
          "CaCl2_GGA_Ecoh",
          "cubic_LDA_Ecoh",
          "cubic_GGA_Ecoh",
          "rutile_GGA_gap",
          "rutile_EVGGA_gap",
          "CaCl2_GGA_gap",
          "CaCl2_EVGGA_gap",
          "cubic_GGA_gap",
          "cubic_EVGGA_gap",
          "P_trans_rutile_CaCl2_LDA",
          "P_trans_rutile_CaCl2_GGA",
          "P_trans_CaCl2_cubic_LDA",
          "P_trans_CaCl2_cubic_GGA",
          "rutile_GGA_m_e",
          "rutile_GGA_m_h",
          "rutile_EVGGA_m_e",
          "rutile_EVGGA_m_h",
          "CaCl2_GGA_m_e",
          "CaCl2_GGA_m_h",
          "CaCl2_EVGGA_m_e",
          "CaCl2_EVGGA_m_h",
          "cubic_GGA_m_e",
          "cubic_GGA_m_h",
          "cubic_EVGGA_m_e",
          "cubic_EVGGA_m_h",
          "rutile_LDA_ionicity",
          "rutile_GGA_ionicity"
        ],
        "properties": {
          "rutile_LDA_a": {
            "type": "number",
            "unit": "Å"
          },
          "rutile_LDA_c": {
            "type": "number",
            "unit": "Å"
          },
          "rutile_LDA_u": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_GGA_a": {
            "type": "number",
            "unit": "Å"
          },
          "rutile_GGA_c": {
            "type": "number",
            "unit": "Å"
          },
          "rutile_GGA_u": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_LDA_a": {
            "type": "number",
            "unit": "Å"
          },
          "CaCl2_LDA_b": {
            "type": "number",
            "unit": "Å"
          },
          "CaCl2_LDA_c": {
            "type": "number",
            "unit": "Å"
          },
          "CaCl2_LDA_u": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_LDA_v": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_GGA_a": {
            "type": "number",
            "unit": "Å"
          },
          "CaCl2_GGA_b": {
            "type": "number",
            "unit": "Å"
          },
          "CaCl2_GGA_c": {
            "type": "number",
            "unit": "Å"
          },
          "CaCl2_GGA_u": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_GGA_v": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cubic_LDA_a": {
            "type": "number",
            "unit": "Å"
          },
          "cubic_LDA_u": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cubic_GGA_a": {
            "type": "number",
            "unit": "Å"
          },
          "cubic_GGA_u": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_LDA_B": {
            "type": "number",
            "unit": "GPa"
          },
          "rutile_GGA_B": {
            "type": "number",
            "unit": "GPa"
          },
          "CaCl2_LDA_B": {
            "type": "number",
            "unit": "GPa"
          },
          "CaCl2_GGA_B": {
            "type": "number",
            "unit": "GPa"
          },
          "cubic_LDA_B": {
            "type": "number",
            "unit": "GPa"
          },
          "cubic_GGA_B": {
            "type": "number",
            "unit": "GPa"
          },
          "rutile_LDA_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "rutile_GGA_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "CaCl2_LDA_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "CaCl2_GGA_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "cubic_LDA_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "cubic_GGA_Ecoh": {
            "type": "number",
            "unit": "eV per formula unit"
          },
          "rutile_GGA_gap": {
            "type": "number",
            "unit": "eV"
          },
          "rutile_EVGGA_gap": {
            "type": "number",
            "unit": "eV"
          },
          "CaCl2_GGA_gap": {
            "type": "number",
            "unit": "eV"
          },
          "CaCl2_EVGGA_gap": {
            "type": "number",
            "unit": "eV"
          },
          "cubic_GGA_gap": {
            "type": "number",
            "unit": "eV"
          },
          "cubic_EVGGA_gap": {
            "type": "number",
            "unit": "eV"
          },
          "P_trans_rutile_CaCl2_LDA": {
            "type": "number",
            "unit": "GPa"
          },
          "P_trans_rutile_CaCl2_GGA": {
            "type": "number",
            "unit": "GPa"
          },
          "P_trans_CaCl2_cubic_LDA": {
            "type": "number",
            "unit": "GPa"
          },
          "P_trans_CaCl2_cubic_GGA": {
            "type": "number",
            "unit": "GPa"
          },
          "rutile_GGA_m_e": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_GGA_m_h": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_EVGGA_m_e": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_EVGGA_m_h": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_GGA_m_e": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_GGA_m_h": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_EVGGA_m_e": {
            "type": "number",
            "unit": "dimensionless"
          },
          "CaCl2_EVGGA_m_h": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cubic_GGA_m_e": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cubic_GGA_m_h": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cubic_EVGGA_m_e": {
            "type": "number",
            "unit": "dimensionless"
          },
          "cubic_EVGGA_m_h": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_LDA_ionicity": {
            "type": "number",
            "unit": "dimensionless"
          },
          "rutile_GGA_ionicity": {
            "type": "number",
            "unit": "dimensionless"
          }
        }
      },
      "description": "Aggregated structural and electronic quantities, including lattice constants, internal parameters, bulk modulus, cohesive energy, energy gaps, effective masses, ionicity factor, and phase transition pressures for SnO₂ polymorphs."
    }
  ],
  "notes": "The effective masses and ionicity factor have been added as required by the reviewer. All fields are compared to hidden gold values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/results.json file. For every required field, it extracts the numeric value you reported and compares it against a gold reference value (the paper's own published result) using a field-specific tolerance. The reward is the fraction of fields that fall within their tolerance, weighted by importance. You must complete the full computational pipeline—the verifier does not award credit for simply printing numbers; it checks that the computed physics (derived from the DFT runs and post-processing steps) reproduces the reference results within the expected accuracy of independent DFT implementations.
