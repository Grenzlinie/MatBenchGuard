# First-principles reproduction of monolayer FeCl2: structural, electronic, magnetic and vibrational properties

## Problem background
Two-dimensional transition-metal dichalcogenides (TMDs) are prime candidates for next-generation nanoelectronics and spintronics. The structural, electronic, magnetic, and vibrational properties of monolayer iron dichloride (FeCl2) are of particular interest because they govern its potential as an intrinsic half-metallic ferromagnet. In this task, you will compute these key properties from first principles using density functional theory (DFT). The reproduction objective is to determine, by direct calculation, the structural parameters of the 1T phase, its cohesive energy, magnetic moment, charge distribution, phonon frequencies, electronic band structure near the Fermi level, and the energy cost of reversing the magnetic order—all of which together characterise the material’s stability, half-metallic nature, and magnetic ordering.

## Approach
The reproduction uses spin-polarised DFT within the Perdew-Burke-Ernzerhof (PBE) generalised-gradient approximation and projector augmented-wave (PAW) potentials. The workflow consists of five main computational stages:

1. **Geometry relaxation and total energies**: The 1T and 1H monolayer structures, as well as isolated Fe and Cl atoms, are relaxed until forces and stresses are small. This gives optimised lattice constants, atomic positions, total energies, magnetic moments, and charge densities. A Bader charge analysis on the relaxed charge densities provides atomic charges.

2. **Structural, magnetic, and charge reporting**: From the relaxed 1T structure you extract the hexagonal lattice constant, bond lengths, bond angle, total magnetic moment per unit cell, Bader charges, and the cohesive energy per atom (from the total energies of the monolayer and the isolated atoms).

3. **Electronic band structure and half-metallicity**: A non-self-consistent PBE band structure calculation is performed for the optimised 1T structure along a high‑symmetry path. The minority‑spin band gap is determined, and you verify whether at least one majority‑spin band crosses the Fermi level.

4. **Phonon dispersion**: Using the finite‑displacement method, a supercell is built, forces are computed from DFT, and the phonon dispersion is obtained. All Γ‑point frequencies are extracted and classified as Raman‑active (E′, A1′) or IR‑active (A2″, E″) according to symmetry.

5. **Magnetic exchange and Curie temperature**: A 2×2 supercell of the 1T structure is used for two spin‑polarised total‑energy calculations: one with ferromagnetic (FM) and one with antiferromagnetic (AFM) alignment of Fe moments. The energy difference per primitive cell is used to calculate the Heisenberg exchange parameter J, and the Curie temperature is estimated via the mean‑field approximation.

All calculations can be performed with open‑source codes; you will need a DFT engine capable of spin‑polarised PBE with PAW potentials (e.g., Quantum ESPRESSO), the Phonopy package for phonon calculations, and the Bader charge analysis code from the Henkelman group. The required pseudopotentials for Fe and Cl are available from standard public libraries (e.g., SSSP).

## Reproduction target
You must produce four JSON files under `/app/outputs` that each contain a specific set of quantities computed from your DFT and phonon calculations:

- **step_01_structure.json** – the structural, magnetic, charge, and cohesive properties of the 1T phase.
- **step_04_band_gap.json** – the minority‑spin PBE gap and a boolean indicating whether majority bands cross the Fermi level.
- **step_02_phonon_frequencies.json** – all nine Γ‑point phonon frequencies with their Raman/IR activity flags.
- **step_03_magnetic_energy.json** – the FM and AFM supercell energies, the energy difference per primitive cell, the exchange parameter J, and the estimated Curie temperature.

The precise schema and units for each file are specified in the workflow steps and the output contract. Your objective is to run the full computational pipeline and write these files with the values obtained from your own calculations.

## Assets

- Quantum ESPRESSO (or any open-source DFT code supporting PAW/PBE): https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Bader charge analysis code (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/
- PBE pseudopotentials for Fe and Cl: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT geometry optimization and total energy calculations
- Role: process
- Action: Perform spin-polarized DFT calculations using PBE functional and PAW potentials to relax the 1T and 1H monolayer structures, as well as isolated Fe and Cl atoms. Compute total energies, magnetic moments, and charge density files. Convergence criteria should yield well-relaxed structures. Additionally, run Bader analysis on the relaxed charge densities to obtain atomic charges.
- Evidence: `/app/outputs/relaxation_summary.log`

### Step 2: Report structural, magnetic, and charge properties
- Role: scored (load-bearing)
- Action: Extract from Step 0 outputs for the 1T phase: lattice constant a, Fe-Cl bond length, Cl-Cl distance, Cl-Fe-Cl bond angle, total magnetic moment per unit cell, Bader charges for Fe and Cl, and cohesive energy per atom (Ec = (E_T[Fe] + 2 E_T[Cl] - E_T[FeCl2]) / number of atoms). Write all results to the specified file.
- Output file: `/app/outputs/step_01_structure.json`
- Format: json
- Contract: JSON object with keys: phase (string '1T'), lattice_constant_a (float, angstrom), bond_length_Fe_Cl (float, angstrom), bond_length_Cl_Cl (float, angstrom), angle_Cl_Fe_Cl (float, deg), total_magnetic_moment (float, mu_B), Bader_charge_Fe (float, e), Bader_charge_Cl (float, e), cohesive_energy_per_atom (float, eV/atom), total_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 3: Compute PBE band structure and half-metallicity
- Role: scored
- Action: Using the optimized 1T structure from Step 0, perform a non-self-consistent PBE band structure calculation along a high-symmetry path. Determine the minority-spin band gap (top of valence to bottom of conduction in the minority channel) and verify that at least one majority-spin band crosses the Fermi level.
- Output file: `/app/outputs/step_04_band_gap.json`
- Format: json
- Contract: JSON object with keys: minority_gap (float, eV), majority_has_bands_at_Fermi (bool).
- Scoring: scored by hidden verifier

### Step 4: Compute phonon dispersion and identify Raman/IR active modes
- Role: scored
- Action: For the relaxed 1T structure from Step 0, use the finite-displacement method (Phonopy) to generate a supercell, compute forces from DFT, and obtain the phonon dispersion. At the Gamma point, extract all 9 branch frequencies. Classify optical modes as Raman-active (E', A1') or IR-active (A2'', E'') based on symmetry. Write all frequencies and activity flags.
- Output file: `/app/outputs/step_02_phonon_frequencies.json`
- Format: json
- Contract: JSON array of objects, each with keys: branch (string), frequency (float, cm-1), Raman_active (bool), IR_active (bool). Must contain all 9 branches at Gamma, including acoustic modes.
- Scoring: scored by hidden verifier

### Step 5: Compute magnetic exchange and Curie temperature
- Role: scored
- Action: Construct a 2x2 supercell of the optimized 1T structure. Perform spin-polarized total-energy calculations for ferromagnetic (FM) and antiferromagnetic (AFM) arrangements. Compute energy difference per primitive cell ΔE = E_AFM - E_FM (meV). Calculate exchange parameter J = (1/12) * ΔE / (2 * m^2) with m = 4 μB. Estimate Curie temperature via mean-field: T_c = (3*J)/(2*k_B). Report energies and derived values.
- Output file: `/app/outputs/step_03_magnetic_energy.json`
- Format: json
- Contract: JSON object with keys: energy_FM (float, eV per supercell), energy_AFM (float, eV per supercell), energy_difference_per_primitive_cell (float, meV), exchange_parameter_J (float, meV), Curie_temperature (float, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structure.json`
- `/app/outputs/step_04_band_gap.json`
- `/app/outputs/step_02_phonon_frequencies.json`
- `/app/outputs/step_03_magnetic_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structure.json
- path: `/app/outputs/step_01_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural parameters, magnetic moment, Bader charges, and cohesive energy for 1T-FeCl2, compared to the paper’s reported values.
- schema:
  - `type`: object
  - `required`: `phase`, `lattice_constant_a`, `bond_length_Fe_Cl`, `bond_length_Cl_Cl`, `angle_Cl_Fe_Cl`, `total_magnetic_moment`, `Bader_charge_Fe`, `Bader_charge_Cl`, `cohesive_energy_per_atom`, `total_energy`
  - `properties`:
    - `phase`:
      - `type`: string
    - `lattice_constant_a`:
      - `type`: number
      - `unit`: angstrom
    - `bond_length_Fe_Cl`:
      - `type`: number
      - `unit`: angstrom
    - `bond_length_Cl_Cl`:
      - `type`: number
      - `unit`: angstrom
    - `angle_Cl_Fe_Cl`:
      - `type`: number
      - `unit`: deg
    - `total_magnetic_moment`:
      - `type`: number
      - `unit`: mu_B
    - `Bader_charge_Fe`:
      - `type`: number
      - `unit`: e
    - `Bader_charge_Cl`:
      - `type`: number
      - `unit`: e
    - `cohesive_energy_per_atom`:
      - `type`: number
      - `unit`: eV/atom
    - `total_energy`:
      - `type`: number
      - `unit`: eV

### step_04_band_gap.json
- path: `/app/outputs/step_04_band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: PBE minority-spin gap and majority-spin Fermi crossing, confirming half-metallicity as reported.
- schema:
  - `type`: object
  - `required`: `minority_gap`, `majority_has_bands_at_Fermi`
  - `properties`:
    - `minority_gap`:
      - `type`: number
      - `unit`: eV
    - `majority_has_bands_at_Fermi`:
      - `type`: boolean

### step_02_phonon_frequencies.json
- path: `/app/outputs/step_02_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All nine Gamma-point phonon frequencies with Raman/IR activity assignments.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `branch`, `frequency`, `Raman_active`, `IR_active`
    - `properties`:
      - `branch`:
        - `type`: string
      - `frequency`:
        - `type`: number
        - `unit`: cm-1
      - `Raman_active`:
        - `type`: boolean
      - `IR_active`:
        - `type`: boolean

### step_03_magnetic_energy.json
- path: `/app/outputs/step_03_magnetic_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic exchange energies and mean-field Curie temperature compared to the paper’s values.
- schema:
  - `type`: object
  - `required`: `energy_FM`, `energy_AFM`, `energy_difference_per_primitive_cell`, `exchange_parameter_J`, `Curie_temperature`
  - `properties`:
    - `energy_FM`:
      - `type`: number
      - `unit`: eV per supercell
    - `energy_AFM`:
      - `type`: number
      - `unit`: eV per supercell
    - `energy_difference_per_primitive_cell`:
      - `type`: number
      - `unit`: meV
    - `exchange_parameter_J`:
      - `type`: number
      - `unit`: meV
    - `Curie_temperature`:
      - `type`: number
      - `unit`: K

Notes: All scored artifacts are JSON files with explicitly declared fields and units. The reference gold values (with tolerances) are hidden from the solving agent; the checker compares each required quantity to the paper’s reported results with generous tolerances to absorb legitimate code/toolchain differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "phase",
          "lattice_constant_a",
          "bond_length_Fe_Cl",
          "bond_length_Cl_Cl",
          "angle_Cl_Fe_Cl",
          "total_magnetic_moment",
          "Bader_charge_Fe",
          "Bader_charge_Cl",
          "cohesive_energy_per_atom",
          "total_energy"
        ],
        "properties": {
          "phase": {
            "type": "string"
          },
          "lattice_constant_a": {
            "type": "number",
            "unit": "angstrom"
          },
          "bond_length_Fe_Cl": {
            "type": "number",
            "unit": "angstrom"
          },
          "bond_length_Cl_Cl": {
            "type": "number",
            "unit": "angstrom"
          },
          "angle_Cl_Fe_Cl": {
            "type": "number",
            "unit": "deg"
          },
          "total_magnetic_moment": {
            "type": "number",
            "unit": "mu_B"
          },
          "Bader_charge_Fe": {
            "type": "number",
            "unit": "e"
          },
          "Bader_charge_Cl": {
            "type": "number",
            "unit": "e"
          },
          "cohesive_energy_per_atom": {
            "type": "number",
            "unit": "eV/atom"
          },
          "total_energy": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Structural parameters, magnetic moment, Bader charges, and cohesive energy for 1T-FeCl2, compared to the paper’s reported values."
    },
    {
      "file": "step_04_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "minority_gap",
          "majority_has_bands_at_Fermi"
        ],
        "properties": {
          "minority_gap": {
            "type": "number",
            "unit": "eV"
          },
          "majority_has_bands_at_Fermi": {
            "type": "boolean"
          }
        }
      },
      "description": "PBE minority-spin gap and majority-spin Fermi crossing, confirming half-metallicity as reported."
    },
    {
      "file": "step_02_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "branch",
            "frequency",
            "Raman_active",
            "IR_active"
          ],
          "properties": {
            "branch": {
              "type": "string"
            },
            "frequency": {
              "type": "number",
              "unit": "cm-1"
            },
            "Raman_active": {
              "type": "boolean"
            },
            "IR_active": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "All nine Gamma-point phonon frequencies with Raman/IR activity assignments."
    },
    {
      "file": "step_03_magnetic_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "energy_FM",
          "energy_AFM",
          "energy_difference_per_primitive_cell",
          "exchange_parameter_J",
          "Curie_temperature"
        ],
        "properties": {
          "energy_FM": {
            "type": "number",
            "unit": "eV per supercell"
          },
          "energy_AFM": {
            "type": "number",
            "unit": "eV per supercell"
          },
          "energy_difference_per_primitive_cell": {
            "type": "number",
            "unit": "meV"
          },
          "exchange_parameter_J": {
            "type": "number",
            "unit": "meV"
          },
          "Curie_temperature": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Magnetic exchange energies and mean-field Curie temperature compared to the paper’s values."
    }
  ],
  "notes": "All scored artifacts are JSON files with explicitly declared fields and units. The reference gold values (with tolerances) are hidden from the solving agent; the checker compares each required quantity to the paper’s reported results with generous tolerances to absorb legitimate code/toolchain differences."
}
```

## How you are scored
A hidden verifier will inspect each of the four scored output files independently. It will compare the numeric quantities you report against hidden reference values that were obtained from a correct execution of the same workflow. The comparison is tolerant to the spread that naturally arises from different DFT codes, pseudopotential choices, and numerical settings. Scoring is monotonic: if your computed result is as good as or better than the reference (e.g., a smaller numerical error, a larger band gap where larger is more insulating), you receive full credit for that quantity. Results worse than the reference earn partial credit according to a pre‑defined schedule. The final reward is a weighted sum of the scores from all four stages; reporting a number without actually performing the calculations will not suffice.
