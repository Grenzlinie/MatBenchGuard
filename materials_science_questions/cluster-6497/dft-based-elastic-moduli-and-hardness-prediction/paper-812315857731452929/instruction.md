# DFT Calculation of Structural and Elastic Properties of Sc2AC MAX Phases

## Problem background
MAX phases are layered carbides and nitrides that attract attention because they combine properties usually associated with both metals and ceramics. Among them, the Sc-based variants Sc₂AC (A = Al, Ga, In, Tl) have barely been explored. Their structural parameters, elastic stiffness (bulk modulus), and formation energies are key quantities that determine whether these compounds are thermodynamically accessible and how strongly the layers are coupled. In particular, comparing the bulk moduli of Sc₂AC to that of the binary carbide ScC reveals whether the carbide stiffness is preserved in the ternary phase – a signature used to classify MAX phases as strongly or weakly coupled. The present task is to compute these properties from first principles for the four candidate Sc₂AC phases and for ScC, providing the numerical values required for that classification.

## Approach
The approach relies on first‑principles density‑functional theory (DFT) with the generalized‑gradient approximation (GGA). You will use a plane‑wave pseudopotential method – for example the open‑source Quantum ESPRESSO code with PBE pseudopotentials – to perform total‑energy calculations.

The workflow consists of several stages:
1. Construct initial crystal structures for Sc₂AlC, Sc₂GaC, Sc₂InC, Sc₂TlC in the Cr₂AlC prototype (space group P6₃/mmc), for ScC in the NaCl structure (Fm‑3m), and for the elemental references Sc (hcp), C (graphite), Al, Ga, In, Tl in their ground‑state structures.
2. Optimize the geometry of each compound (atomic positions, cell shape and volume) to obtain the equilibrium lattice parameters (a, c/a) and total energy.
3. Compute total energies on a fine mesh of volumes around equilibrium to build the energy‑versus‑volume curve E(V).
4. Fit the E(V) data to a Birch–Murnaghan equation of state to extract the equilibrium volume per atom and the bulk modulus.
5. Obtain the total energies of the elemental references from separate DFT calculations, then compute the formation energy per atom for each Sc₂AC phase using the appropriate stoichiometric formula.
6. Perform the same optimisation and equation‑of‑state fitting for ScC to obtain its bulk modulus.

All steps must be executed from scratch; the final numerical results are to be collected in the JSON output file described in the workflow steps below.

## Reproduction target
Your task is to produce a single JSON file, `/app/outputs/computed_properties.json`, that contains the following quantities obtained from your DFT calculations:
- For each of Sc₂AlC, Sc₂GaC, Sc₂InC, Sc₂TlC:
    * `a` – equilibrium in‑plane lattice parameter (Å)
    * `c_over_a` – hexagonal c/a ratio (dimensionless)
    * `Vo` – equilibrium volume per atom (Å³/atom)
    * `B` – bulk modulus (GPa)
    * `Ef` – formation energy per atom (eV/atom), calculated as described in the workflow.
- For ScC:
    * `B` – bulk modulus (GPa).

The file must follow the exact JSON schema specified in Step 7 of the workflow steps and the Output contract section. All numerical values must be the result of your own DFT pipeline; they may not be looked up from a publication.

## Assets

- Quantum ESPRESSO (or other open-source DFT code): https://www.quantum-espresso.org/
- PBE pseudopotential library: https://pseudopotentials.quantum-espresso.org/
- Crystal structure prototypes

## Workflow steps

### Step 1: Prepare initial structures
- Role: process
- Action: Generate input geometry files for Sc2AC (A=Al,Ga,In,Tl) in the P63/mmc structure (Cr2AlC prototype), for ScC in the NaCl structure, and for elemental references (Sc hcp, C graphite, and the ground‑state structures of Al, Ga, In, Tl). Use approximate lattice parameters from known databases as starting guesses.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: DFT geometry optimization of Sc2AC
- Role: process
- Action: For each of the four Sc2AC compositions, perform DFT geometry optimization (relax atomic positions, cell shape, and volume) using an open‑source DFT code with the GGA functional. Obtain equilibrium total energies and lattice parameters (a, c/a).
- Evidence: `/app/outputs/sc2ac_optimized_structures.txt`

### Step 3: DFT energy-volume curves for Sc2AC
- Role: process
- Action: For each optimized Sc2AC structure, compute total energies for a series of cell volumes around equilibrium to generate E(V) data needed for equation‑of‑state fitting.
- Evidence: `/app/outputs/sc2ac_ev_data.csv`

### Step 4: Birch-Murnaghan EOS fitting
- Role: process
- Action: Fit the E(V) data to the Birch‑Murnaghan equation of state to extract the equilibrium volume per atom Vo and the bulk modulus B for each Sc2AC compound.
- Evidence: `/app/outputs/eos_fit_results.json`

### Step 5: DFT total energies for elemental references
- Role: process
- Action: Perform DFT calculations for elemental Sc (hcp), C (graphite), Al, Ga, In, Tl in their ground‑state crystal structures, obtaining total energies per formula unit or per atom for later formation‑energy computation.
- Evidence: `/app/outputs/elemental_energies.txt`

### Step 6: DFT calculation for ScC
- Role: process
- Action: Perform DFT geometry optimization and E(V)‑curve calculations for ScC in the NaCl structure, then fit the Birch‑Murnaghan equation of state to obtain its bulk modulus B(ScC).
- Evidence: `/app/outputs/scc_ev_data.csv`

### Step 7: Assemble final properties
- Role: scored (load-bearing)
- Action: Using the total energies from previous steps and the EOS results, compute the formation energy per atom for each Sc2AC via the formula Ef = (E(Sc2AC) - 2*E(Sc) - (2/n)*E(A) - 0.5*E(C)) / 8, where n is the number of A atoms in the elemental reference cell used. Combine all computed quantities — lattice parameter a, hexagonal ratio c/a, equilibrium volume per atom Vo, bulk modulus B, formation energy Ef for Sc2AlC, Sc2GaC, Sc2InC, Sc2TlC, and the bulk modulus of ScC — into a single JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: JSON object with keys 'Sc2AlC', 'Sc2GaC', 'Sc2InC', 'Sc2TlC', and 'ScC'. Each key (except 'ScC') maps to an object with numeric fields 'a' (Å), 'c_over_a' (dimensionless), 'Vo' (Å³/atom), 'B' (GPa), 'Ef' (eV/atom). 'ScC' maps to an object with field 'B' (GPa).
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
- target_policy: reference_match
- description: Computed physical properties for the four Sc2AC MAX phases and the bulk modulus of ScC. All values are to be obtained from DFT re‑runs and equation‑of‑state fits, not from literature look‑up.
- schema:
  - `type`: object
  - `required`: `Sc2AlC`, `Sc2GaC`, `Sc2InC`, `Sc2TlC`, `ScC`
  - `properties`:
    - `Sc2AlC`:
      - `type`: object
      - `required`: `a`, `c_over_a`, `Vo`, `B`, `Ef`
      - `properties`:
        - `a`:
          - `type`: number
          - `units`: Angstrom
        - `c_over_a`:
          - `type`: number
          - `units`: dimensionless
        - `Vo`:
          - `type`: number
          - `units`: Angstrom^3/atom
        - `B`:
          - `type`: number
          - `units`: GPa
        - `Ef`:
          - `type`: number
          - `units`: eV/atom
    - `Sc2GaC`:
      - `type`: object
      - `required`: `a`, `c_over_a`, `Vo`, `B`, `Ef`
      - `properties`:
        - `a`:
          - `type`: number
          - `units`: Angstrom
        - `c_over_a`:
          - `type`: number
          - `units`: dimensionless
        - `Vo`:
          - `type`: number
          - `units`: Angstrom^3/atom
        - `B`:
          - `type`: number
          - `units`: GPa
        - `Ef`:
          - `type`: number
          - `units`: eV/atom
    - `Sc2InC`:
      - `type`: object
      - `required`: `a`, `c_over_a`, `Vo`, `B`, `Ef`
      - `properties`:
        - `a`:
          - `type`: number
          - `units`: Angstrom
        - `c_over_a`:
          - `type`: number
          - `units`: dimensionless
        - `Vo`:
          - `type`: number
          - `units`: Angstrom^3/atom
        - `B`:
          - `type`: number
          - `units`: GPa
        - `Ef`:
          - `type`: number
          - `units`: eV/atom
    - `Sc2TlC`:
      - `type`: object
      - `required`: `a`, `c_over_a`, `Vo`, `B`, `Ef`
      - `properties`:
        - `a`:
          - `type`: number
          - `units`: Angstrom
        - `c_over_a`:
          - `type`: number
          - `units`: dimensionless
        - `Vo`:
          - `type`: number
          - `units`: Angstrom^3/atom
        - `B`:
          - `type`: number
          - `units`: GPa
        - `Ef`:
          - `type`: number
          - `units`: eV/atom
    - `ScC`:
      - `type`: object
      - `required`: `B`
      - `properties`:
        - `B`:
          - `type`: number
          - `units`: GPa

Notes: The agent must install an open‑source DFT code and appropriate pseudopotentials; the computational chain is self‑contained and does not rely on any pre‑computed results from the original paper.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Sc2AlC",
          "Sc2GaC",
          "Sc2InC",
          "Sc2TlC",
          "ScC"
        ],
        "properties": {
          "Sc2AlC": {
            "type": "object",
            "required": [
              "a",
              "c_over_a",
              "Vo",
              "B",
              "Ef"
            ],
            "properties": {
              "a": {
                "type": "number",
                "units": "Angstrom"
              },
              "c_over_a": {
                "type": "number",
                "units": "dimensionless"
              },
              "Vo": {
                "type": "number",
                "units": "Angstrom^3/atom"
              },
              "B": {
                "type": "number",
                "units": "GPa"
              },
              "Ef": {
                "type": "number",
                "units": "eV/atom"
              }
            }
          },
          "Sc2GaC": {
            "type": "object",
            "required": [
              "a",
              "c_over_a",
              "Vo",
              "B",
              "Ef"
            ],
            "properties": {
              "a": {
                "type": "number",
                "units": "Angstrom"
              },
              "c_over_a": {
                "type": "number",
                "units": "dimensionless"
              },
              "Vo": {
                "type": "number",
                "units": "Angstrom^3/atom"
              },
              "B": {
                "type": "number",
                "units": "GPa"
              },
              "Ef": {
                "type": "number",
                "units": "eV/atom"
              }
            }
          },
          "Sc2InC": {
            "type": "object",
            "required": [
              "a",
              "c_over_a",
              "Vo",
              "B",
              "Ef"
            ],
            "properties": {
              "a": {
                "type": "number",
                "units": "Angstrom"
              },
              "c_over_a": {
                "type": "number",
                "units": "dimensionless"
              },
              "Vo": {
                "type": "number",
                "units": "Angstrom^3/atom"
              },
              "B": {
                "type": "number",
                "units": "GPa"
              },
              "Ef": {
                "type": "number",
                "units": "eV/atom"
              }
            }
          },
          "Sc2TlC": {
            "type": "object",
            "required": [
              "a",
              "c_over_a",
              "Vo",
              "B",
              "Ef"
            ],
            "properties": {
              "a": {
                "type": "number",
                "units": "Angstrom"
              },
              "c_over_a": {
                "type": "number",
                "units": "dimensionless"
              },
              "Vo": {
                "type": "number",
                "units": "Angstrom^3/atom"
              },
              "B": {
                "type": "number",
                "units": "GPa"
              },
              "Ef": {
                "type": "number",
                "units": "eV/atom"
              }
            }
          },
          "ScC": {
            "type": "object",
            "required": [
              "B"
            ],
            "properties": {
              "B": {
                "type": "number",
                "units": "GPa"
              }
            }
          }
        }
      },
      "description": "Computed physical properties for the four Sc2AC MAX phases and the bulk modulus of ScC. All values are to be obtained from DFT re‑runs and equation‑of‑state fits, not from literature look‑up."
    }
  ],
  "notes": "The agent must install an open‑source DFT code and appropriate pseudopotentials; the computational chain is self‑contained and does not rely on any pre‑computed results from the original paper."
}
```

## How you are scored
A hidden automated verifier will evaluate your submission. It will read `/app/outputs/computed_properties.json` and compare every numerical field against reference values using internally defined tolerances. Additionally, the verifier will check that all formation energies (`Ef`) are negative (indicating thermodynamic stability). The total score is the fraction of the required numerical entries that fall within the verifier's tolerances and satisfy the negativity condition. The JSON file must conform precisely to the declared schema; any missing keys, extra fields, or structural deviations will cause the scoring to fail. Reporting values that look plausible but were not generated by the DFT workflow is not sufficient – the verifier's comparison against hidden references will penalise guesses.
