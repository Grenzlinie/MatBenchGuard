# DFT-GGA Study of Sr-Si Intermediate Phases: Formation Enthalpies, High-Pressure Transitions, and Electronic Structure

## Problem background
Semiconducting silicides are attractive as environmentally friendly materials for electronic devices, replacing toxic heavy-metal compounds. The Sr-Si system forms four intermediate phases (Sr2Si, Sr5Si3, SrSi, SrSi2) whose crystal structures are known, but a comprehensive theoretical description of their thermodynamic stability, high-pressure behaviour, and electronic properties is missing. This task uses first-principles density functional theory (DFT) within the generalized-gradient approximation to compute formation enthalpies for a wide set of candidate crystal lattices, determine the ground-state structures, locate high-pressure phase transitions, and analyse the electronic density of states, band gap, and charge transfer, thereby quantifying the Sr-Si chemical bonding.

## Approach
The work employs DFT total-energy calculations with the PW91 GGA exchange-correlation functional and projector augmented wave (PAW) pseudopotentials, using an open-source DFT code. The core idea is to compute the cohesive energies of elemental Sr and Si and then, for each of 26 candidate Sr-Si crystal structures, perform full structural relaxations to obtain total energies. Formation enthalpies per atom are calculated and a convex hull analysis identifies the thermodynamically stable ground-state phases. For selected phases, energy–volume curves (binding energy curves) are computed for several candidate polymorphs; fitting an equation of state and applying a common tangent construction yields high-pressure transition pressures. Finally, non-self-consistent density-of-states calculations and Bader charge analysis are performed on the relaxed ground-state structures to extract the band gap of Sr2Si and the charge transfer (ionic character) of each stable Sr-Si phase.

## Reproduction target
Run the DFT workflow to produce three scored artefacts:
1. `heats_of_formation.json`: formation enthalpies per atom (kJ mol⁻¹-at) for the four experimentally observed ground-state phases — Sr2Si (oP12), Sr5Si3 (tI32 Cr5B3-type), SrSi (oC8), and SrSi2 (cP12).
2. `transition_pressures.json`: high-pressure transition pressures (GPa) for Sr2Si (oP12→hP6), Sr5Si3 (tI32-Cr5B3→tI32-Mo5Si3), and SrSi (oC8→oP8 and oP8→tP2).
3. `electronic_properties.json`: band gap of Sr2Si (eV) and Bader charges / percentage ionic character for the ground-state phases.

## Assets

- Open-source DFT code with PAW PW91 support: https://www.quantum-espresso.org/
- PAW pseudopotentials for Sr and Si: https://www.materialscloud.org/discover/sssp
- Crystal structure databases (Bilbao Crystallographic Server, Materials Project, ICSD): https://www.cryst.ehu.es/
- Python packages for structure manipulation and analysis: pymatgen, ase, scipy

## Workflow steps

### Step 1: Structure preparation
- Role: process
- Action: Obtain or generate the 26 crystal structures for the Sr-Si compositions listed in the paper, as well as elemental Sr (fcc) and Si (diamond), from public crystallographic databases or by constructing from Pearson symbols and prototype names.
- Evidence: `/app/outputs/structures_manifest.txt`

### Step 2: Reference energy calculations for elemental Sr and Si
- Role: process
- Action: Perform DFT total-energy calculations for fcc Sr and diamond Si using an open-source DFT code with PAW PW91-GGA functional to obtain cohesive energies per atom.
- Evidence: `/app/outputs/reference_energies.log`

### Step 3: Structural relaxations for all candidate Sr-Si structures
- Role: process
- Action: For each of the 26 candidate structures, perform a full cell and internal-coordinate relaxation at ambient pressure using the same DFT setup; collect the converged total energies and optimized structures.
- Evidence: `/app/outputs/relaxation_summary.log`

### Step 4: Energy-volume curves for high-pressure polymorphs
- Role: process
- Action: For the selected phases (Sr2Si, Sr5Si3, SrSi) and their candidate high-pressure polymorphs, compute total energies at multiple volumes around equilibrium to construct binding energy curves E(V).
- Evidence: `/app/outputs/ev_curves_summary.log`

### Step 5: Heats of formation and convex hull
- Role: scored
- Action: Using the cohesive energies from step02 and the relaxed total energies from step03, calculate formation enthalpies ΔH per atom for all 26 structures; identify the ground-state phases and output their ΔH values (kJ/mol-at).
- Output file: `/app/outputs/heats_of_formation.json`
- Format: json
- Contract: {"type": "array", "items": {"type": "object", "required": ["composition", "prototype", "value_kJ_per_mol_at"], "properties": {"composition": {"type": "string"}, "prototype": {"type": "string"}, "value_kJ_per_mol_at": {"type": "number", "description": "Formation enthalpy in kJ per mole of atoms"}}}}
- Scoring: scored by hidden verifier

### Step 6: High-pressure transition pressures
- Role: scored
- Action: From the energy-volume curves of step04, fit an equation of state (e.g., Birch-Murnaghan) and use common tangent construction to determine transition pressures (GPa) for Sr2Si (oP12→hP6), Sr5Si3 (tI32-Cr5B3→tI32-Mo5Si3), and SrSi (oC8→oP8→tP2).
- Output file: `/app/outputs/transition_pressures.json`
- Format: json
- Contract: {"type": "array", "items": {"type": "object", "required": ["phase", "from_lattice", "to_lattice", "pressure_GPa"], "properties": {"phase": {"type": "string"}, "from_lattice": {"type": "string"}, "to_lattice": {"type": "string"}, "pressure_GPa": {"type": "number"}}}}
- Scoring: scored by hidden verifier

### Step 7: Electronic structure analysis
- Role: scored (load-bearing)
- Action: For the ground-state structures, perform a non-self-consistent DOS calculation with a dense k-point grid. Compute the band gap of Sr2Si (eV) and Bader charges on Sr and Si for the ground-state phases, along with the percentage ionic character.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: {"type": "object", "required": ["band_gap_Sr2Si_eV", "charge_transfer"], "properties": {"band_gap_Sr2Si_eV": {"type": "number"}, "charge_transfer": {"type": "array", "items": {"type": "object", "required": ["phase", "Sr_charge", "Si_charge", "ionic_percent"], "properties": {"phase": {"type": "string"}, "Sr_charge": {"type": "number"}, "Si_charge": {"type": "number"}, "ionic_percent": {"type": "number"}}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heats_of_formation.json`
- `/app/outputs/transition_pressures.json`
- `/app/outputs/electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heats_of_formation.json
- path: `/app/outputs/heats_of_formation.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation enthalpies per atom for the four experimentally observed ground-state phases (Sr2Si oP12, Sr5Si3 tI32-Cr5B3-type, SrSi oC8, SrSi2 cP12).
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `type`: object
    - `required`: `composition`, `prototype`, `value_kJ_per_mol_at`
    - `properties`:
      - `composition`:
        - `type`: string
      - `prototype`:
        - `type`: string
      - `value_kJ_per_mol_at`:
        - `type`: number
        - `description`: Formation enthalpy in kJ per mole of atoms

### transition_pressures.json
- path: `/app/outputs/transition_pressures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed high-pressure transition pressures for Sr2Si, Sr5Si3, and SrSi phases.
- schema:
  - `type`: array
  - `required`:
  - `items`:
    - `type`: object
    - `required`: `phase`, `from_lattice`, `to_lattice`, `pressure_GPa`
    - `properties`:
      - `phase`:
        - `type`: string
      - `from_lattice`:
        - `type`: string
      - `to_lattice`:
        - `type`: string
      - `pressure_GPa`:
        - `type`: number
        - `description`: Transition pressure in GPa

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic properties: band gap of Sr2Si and charge transfer data for the ground-state Sr-Si phases.
- schema:
  - `type`: object
  - `required`: `band_gap_Sr2Si_eV`, `charge_transfer`
  - `properties`:
    - `band_gap_Sr2Si_eV`:
      - `type`: number
      - `description`: Band gap of Sr2Si in eV
    - `charge_transfer`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `phase`, `Sr_charge`, `Si_charge`, `ionic_percent`
        - `properties`:
          - `phase`:
            - `type`: string
          - `Sr_charge`:
            - `type`: number
            - `description`: Mean charge on Sr atoms
          - `Si_charge`:
            - `type`: number
            - `description`: Mean charge on Si atoms
          - `ionic_percent`:
            - `type`: number
            - `description`: Percentage ionic character

Notes: All scored quantities are determined from DFT calculations and checked against paper-reported reference values within appropriate numerical tolerances. The load-bearing step (step07) relies on correctly relaxed structures, enforcing that process steps 2-4 are genuinely executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heats_of_formation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "type": "object",
          "required": [
            "composition",
            "prototype",
            "value_kJ_per_mol_at"
          ],
          "properties": {
            "composition": {
              "type": "string"
            },
            "prototype": {
              "type": "string"
            },
            "value_kJ_per_mol_at": {
              "type": "number",
              "description": "Formation enthalpy in kJ per mole of atoms"
            }
          }
        }
      },
      "description": "Formation enthalpies per atom for the four experimentally observed ground-state phases (Sr2Si oP12, Sr5Si3 tI32-Cr5B3-type, SrSi oC8, SrSi2 cP12)."
    },
    {
      "file": "transition_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "required": [],
        "items": {
          "type": "object",
          "required": [
            "phase",
            "from_lattice",
            "to_lattice",
            "pressure_GPa"
          ],
          "properties": {
            "phase": {
              "type": "string"
            },
            "from_lattice": {
              "type": "string"
            },
            "to_lattice": {
              "type": "string"
            },
            "pressure_GPa": {
              "type": "number",
              "description": "Transition pressure in GPa"
            }
          }
        }
      },
      "description": "Computed high-pressure transition pressures for Sr2Si, Sr5Si3, and SrSi phases."
    },
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_Sr2Si_eV",
          "charge_transfer"
        ],
        "properties": {
          "band_gap_Sr2Si_eV": {
            "type": "number",
            "description": "Band gap of Sr2Si in eV"
          },
          "charge_transfer": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "phase",
                "Sr_charge",
                "Si_charge",
                "ionic_percent"
              ],
              "properties": {
                "phase": {
                  "type": "string"
                },
                "Sr_charge": {
                  "type": "number",
                  "description": "Mean charge on Sr atoms"
                },
                "Si_charge": {
                  "type": "number",
                  "description": "Mean charge on Si atoms"
                },
                "ionic_percent": {
                  "type": "number",
                  "description": "Percentage ionic character"
                }
              }
            }
          }
        }
      },
      "description": "Electronic properties: band gap of Sr2Si and charge transfer data for the ground-state Sr-Si phases."
    }
  ],
  "notes": "All scored quantities are determined from DFT calculations and checked against paper-reported reference values within appropriate numerical tolerances. The load-bearing step (step07) relies on correctly relaxed structures, enforcing that process steps 2-4 are genuinely executed."
}
```

## How you are scored
A hidden verifier reads the three output files and compares each numeric value against reference data using tolerance bands that account for code-to-code differences. Scores are combined into a final reward, with the formation enthalpy data carrying the most weight. The verifier does not award points for shape correctness alone; it checks that the computed numbers are physically plausible and consistent with the DFT calculations performed. Reporting a single number without the required step evidence will not receive full credit.
