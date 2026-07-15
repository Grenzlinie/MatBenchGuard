# DFT study of V-doped cubic BN structural and electronic properties

## Problem background
Cubic boron nitride (c-BN) is a zincblende-structured compound renowned for its exceptional hardness, high thermal stability, and chemical inertness. Doping c-BN with transition metals such as vanadium has attracted interest for potential spintronic applications, where the goal is to induce a half-metallic ferromagnetic ground state—a state in which one spin channel is metallic while the other remains semiconducting. The key open questions are (i) what are the equilibrium structural parameters (lattice constant, bulk modulus) of c-BN and its V-doped variants at low doping levels, (ii) how does the electronic structure change upon doping, in particular the minority-spin band gap, (iii) what is the resulting magnetic moment per supercell, and (iv) is the ferromagnetic phase indeed the ground state compared to competing non-magnetic or antiferromagnetic arrangements? Computing these quantities from first principles quantifies the effect of vanadium incorporation on the structural, electronic, and magnetic properties of c-BN, providing insight into the material's viability as a dilute magnetic semiconductor.

## Approach
The approach is a spin-polarized density functional theory (DFT) study carried out with the open-source Quantum ESPRESSO code. The Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation is used for exchange and correlation, with pseudopotentials describing the electron–ion interaction. A 32-atom zincblende supercell serves as the starting model. Pure c-BN is studied first, and then one or two boron atoms are replaced by vanadium to realize the doping concentrations B0.9375V0.0625N and B0.875V0.125N. For the double-doped case, several configurations (V atoms placed at different separations) are tested to locate the lowest-energy arrangement.

For each compound the total energy is computed as a function of unit-cell volume while fully relaxing the atomic positions, both for the ferromagnetic (FM) phase and, where relevant, for the non-magnetic (NM) or antiferromagnetic (AFM) phase. The energy–volume data are fitted to the Murnaghan equation of state to extract equilibrium lattice constant, bulk modulus, and total energy. At the equilibrium volume a self-consistent field (SCF) calculation is performed, followed by a non-self-consistent band-structure calculation and projected density-of-states (PDOS) analysis. The band structure gives the minority-spin band gap, the PDOS yields local magnetic moments on each species (V, B, N), and the integrated spin density provides the total magnetic moment per supercell. The energy difference between the magnetic phases identifies the most stable magnetic ordering.

## Reproduction target
Using Quantum ESPRESSO with the PBE functional and appropriate pseudopotentials, build a 32-atom zincblende supercell for pure c-BN and for the V-doped concentrations B0.9375V0.0625N and B0.875V0.125N. For the double-doped concentration, compare several V–V placement configurations and select the one with the lowest ferromagnetic total energy. For each system perform a spin-polarized energy–volume scan: for pure BN in the FM phase, for B0.9375V0.0625N in both FM and NM phases, and for the lowest-energy B0.875V0.125N configuration in both FM and AFM phases. Fit each FM energy–volume curve to the Murnaghan equation of state to obtain the equilibrium lattice constant (Å), bulk modulus (GPa), and total energy (eV) per supercell.

At the equilibrium volume, perform an SCF followed by a non-SCF band structure and PDOS calculation. From these results extract:
- For pure c-BN: a, B0, E0.
- For B0.9375V0.0625N: a, B0, E0, total magnetic moment per supercell (μB), minority-spin band gap (eV), local magnetic moments on V, B, and N (μB/atom), and the total energies of the FM and NM states.
- For B0.875V0.125N: the same set as above, but with the AFM total energy instead of NM.

Write each set of results to the corresponding JSON file (step_01_…, step_02_…, step_03_…) in the /app/outputs directory. The aim is to reproduce the structural, electronic, and magnetic fingerprints of V-doped c-BN as determined by DFT, and to determine whether the FM ground state is energetically favoured over the NM/AFM alternatives at each doping level.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency): https://www.materialcloud.org/home
- Python with numpy, scipy, matplotlib: numpy scipy matplotlib

## Workflow steps

### Step 1: Build supercell structures
- Role: process
- Action: Create a 32-atom zincblende supercell of pure cubic BN. Substitute one or two boron atoms with vanadium to generate B0.9375V0.0625N and multiple B0.875V0.125N configurations (V atoms in close and separated positions) and select the lowest-energy configuration for the double-doped case.
- Evidence: `/app/outputs/supercell_input_files.log`

### Step 2: Run DFT simulations
- Role: process
- Action: Perform spin-polarized DFT calculations using Quantum ESPRESSO with PBE exchange-correlation, appropriate pseudopotentials, plane-wave basis, and k-point sampling. For each compound: carry out full geometry relaxation; compute total energy as a function of volume for ferromagnetic (FM) and non-magnetic (for B0.9375V0.0625N) or anti-ferromagnetic (for B0.875V0.125N) phases; at the equilibrium volume run a final SCF, followed by non-SCF band structure and projected density of states (DOS) calculations.
- Evidence: `/app/outputs/dft_outputs.log`

### Step 3: Extract pure c-BN structural properties
- Role: scored
- Action: From the DFT energy-volume data of pure c-BN, fit the Murnaghan equation of state to obtain the equilibrium lattice constant a (Å), bulk modulus B0 (GPa), and total energy E0 (eV). Write the results to step_01_pure_BN_properties.json.
- Output file: `/app/outputs/step_01_pure_BN_properties.json`
- Format: json
- Contract: {"a": number (Å), "B0": number (GPa), "E0": number (eV)}
- Scoring: scored by hidden verifier

### Step 4: Extract B0.9375V0.0625N properties
- Role: scored (load-bearing)
- Action: From the DFT results for B0.9375V0.0625N: fit the Murnaghan equation of state to the FM phase data to obtain a, B0, E0; extract total magnetic moment per supercell (μB), minority-spin band gap (eV); decomposite local magnetic moments on V, B, and N from projected DOS; record FM and non-magnetic total energies. Write all values to step_02_B09375V00625N_properties.json.
- Output file: `/app/outputs/step_02_B09375V00625N_properties.json`
- Format: json
- Contract: {"a": number (Å), "B0": number (GPa), "E0": number (eV), "mag_moment": number (μB), "energy_FM": number (eV), "energy_NM": number (eV), "minority_gap": number (eV), "local_moments": {"V": number (μB/atom), "B": number (μB/atom), "N": number (μB/atom)}}
- Scoring: scored by hidden verifier

### Step 5: Extract B0.875V0.125N properties
- Role: scored
- Action: From the DFT results for the most stable configuration of B0.875V0.125N: fit the Murnaghan equation of state to the FM phase data to obtain a, B0, E0; extract total magnetic moment per supercell (μB), minority-spin band gap (eV); decomposite local magnetic moments on V, B, and N; record FM and anti-ferromagnetic total energies. Write all values to step_03_B0875V0125N_properties.json.
- Output file: `/app/outputs/step_03_B0875V0125N_properties.json`
- Format: json
- Contract: {"a": number (Å), "B0": number (GPa), "E0": number (eV), "mag_moment": number (μB), "energy_FM": number (eV), "energy_AFM": number (eV), "minority_gap": number (eV), "local_moments": {"V": number (μB/atom), "B": number (μB/atom), "N": number (μB/atom)}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_pure_BN_properties.json`
- `/app/outputs/step_02_B09375V00625N_properties.json`
- `/app/outputs/step_03_B0875V0125N_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_pure_BN_properties.json
- path: `/app/outputs/step_01_pure_BN_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Validates the DFT setup by comparing computed lattice constant, bulk modulus and total energy of pure c-BN against literature (hidden reference).
- schema:
  - `type`: object
  - `required`: `a`, `B0`, `E0`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
      - `description`: equilibrium lattice constant
    - `B0`:
      - `type`: number
      - `unit`: GPa
      - `description`: bulk modulus
    - `E0`:
      - `type`: number
      - `unit`: eV
      - `description`: total energy per supercell

### step_02_B09375V00625N_properties.json
- path: `/app/outputs/step_02_B09375V00625N_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Checks all computed quantities for the 6.25% V doping, including structural, magnetic, and electronic properties, and the FM vs NM energy ordering (hidden checker verifies energy_FM < energy_NM).
- schema:
  - `type`: object
  - `required`: `a`, `B0`, `E0`, `mag_moment`, `energy_FM`, `energy_NM`, `minority_gap`, `local_moments`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
    - `B0`:
      - `type`: number
      - `unit`: GPa
    - `E0`:
      - `type`: number
      - `unit`: eV
    - `mag_moment`:
      - `type`: number
      - `unit`: μB
      - `description`: total magnetic moment per supercell
    - `energy_FM`:
      - `type`: number
      - `unit`: eV
      - `description`: ferromagnetic total energy
    - `energy_NM`:
      - `type`: number
      - `unit`: eV
      - `description`: non-magnetic total energy
    - `minority_gap`:
      - `type`: number
      - `unit`: eV
      - `description`: minority-spin band gap
    - `local_moments`:
      - `type`: object
      - `required`: `V`, `B`, `N`
      - `properties`:
        - `V`:
          - `type`: number
          - `unit`: μB/atom
        - `B`:
          - `type`: number
          - `unit`: μB/atom
        - `N`:
          - `type`: number
          - `unit`: μB/atom

### step_03_B0875V0125N_properties.json
- path: `/app/outputs/step_03_B0875V0125N_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Checks all computed quantities for the 12.5% V doping, including structural, magnetic, and electronic properties, and the FM vs AFM energy ordering (hidden checker verifies energy_FM < energy_AFM).
- schema:
  - `type`: object
  - `required`: `a`, `B0`, `E0`, `mag_moment`, `energy_FM`, `energy_AFM`, `minority_gap`, `local_moments`
  - `properties`:
    - `a`:
      - `type`: number
      - `unit`: Å
    - `B0`:
      - `type`: number
      - `unit`: GPa
    - `E0`:
      - `type`: number
      - `unit`: eV
    - `mag_moment`:
      - `type`: number
      - `unit`: μB
    - `energy_FM`:
      - `type`: number
      - `unit`: eV
    - `energy_AFM`:
      - `type`: number
      - `unit`: eV
    - `minority_gap`:
      - `type`: number
      - `unit`: eV
    - `local_moments`:
      - `type`: object
      - `required`: `V`, `B`, `N`
      - `properties`:
        - `V`:
          - `type`: number
          - `unit`: μB/atom
        - `B`:
          - `type`: number
          - `unit`: μB/atom
        - `N`:
          - `type`: number
          - `unit`: μB/atom

Notes: All JSON values will be compared by the hidden checker against the paper-reported numbers using appropriate tolerances (lattice constant within ~1%, bulk modulus within ~5%, magnetic moments within ~0.1 μB, band gaps within ~0.1 eV). Energy orderings are enforced as separate conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_pure_BN_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B0",
          "E0"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å",
            "description": "equilibrium lattice constant"
          },
          "B0": {
            "type": "number",
            "unit": "GPa",
            "description": "bulk modulus"
          },
          "E0": {
            "type": "number",
            "unit": "eV",
            "description": "total energy per supercell"
          }
        }
      },
      "description": "Validates the DFT setup by comparing computed lattice constant, bulk modulus and total energy of pure c-BN against literature (hidden reference)."
    },
    {
      "file": "step_02_B09375V00625N_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B0",
          "E0",
          "mag_moment",
          "energy_FM",
          "energy_NM",
          "minority_gap",
          "local_moments"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å"
          },
          "B0": {
            "type": "number",
            "unit": "GPa"
          },
          "E0": {
            "type": "number",
            "unit": "eV"
          },
          "mag_moment": {
            "type": "number",
            "unit": "μB",
            "description": "total magnetic moment per supercell"
          },
          "energy_FM": {
            "type": "number",
            "unit": "eV",
            "description": "ferromagnetic total energy"
          },
          "energy_NM": {
            "type": "number",
            "unit": "eV",
            "description": "non-magnetic total energy"
          },
          "minority_gap": {
            "type": "number",
            "unit": "eV",
            "description": "minority-spin band gap"
          },
          "local_moments": {
            "type": "object",
            "required": [
              "V",
              "B",
              "N"
            ],
            "properties": {
              "V": {
                "type": "number",
                "unit": "μB/atom"
              },
              "B": {
                "type": "number",
                "unit": "μB/atom"
              },
              "N": {
                "type": "number",
                "unit": "μB/atom"
              }
            }
          }
        }
      },
      "description": "Checks all computed quantities for the 6.25% V doping, including structural, magnetic, and electronic properties, and the FM vs NM energy ordering (hidden checker verifies energy_FM < energy_NM)."
    },
    {
      "file": "step_03_B0875V0125N_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "B0",
          "E0",
          "mag_moment",
          "energy_FM",
          "energy_AFM",
          "minority_gap",
          "local_moments"
        ],
        "properties": {
          "a": {
            "type": "number",
            "unit": "Å"
          },
          "B0": {
            "type": "number",
            "unit": "GPa"
          },
          "E0": {
            "type": "number",
            "unit": "eV"
          },
          "mag_moment": {
            "type": "number",
            "unit": "μB"
          },
          "energy_FM": {
            "type": "number",
            "unit": "eV"
          },
          "energy_AFM": {
            "type": "number",
            "unit": "eV"
          },
          "minority_gap": {
            "type": "number",
            "unit": "eV"
          },
          "local_moments": {
            "type": "object",
            "required": [
              "V",
              "B",
              "N"
            ],
            "properties": {
              "V": {
                "type": "number",
                "unit": "μB/atom"
              },
              "B": {
                "type": "number",
                "unit": "μB/atom"
              },
              "N": {
                "type": "number",
                "unit": "μB/atom"
              }
            }
          }
        }
      },
      "description": "Checks all computed quantities for the 12.5% V doping, including structural, magnetic, and electronic properties, and the FM vs AFM energy ordering (hidden checker verifies energy_FM < energy_AFM)."
    }
  ],
  "notes": "All JSON values will be compared by the hidden checker against the paper-reported numbers using appropriate tolerances (lattice constant within ~1%, bulk modulus within ~5%, magnetic moments within ~0.1 μB, band gaps within ~0.1 eV). Energy orderings are enforced as separate conditions."
}
```

## How you are scored
A hidden verifier independently scores each of the three JSON artifacts you produce. For each scored file the verifier reads the numeric fields and compares them against a hidden reference (based on the expected outcome of the DFT calculations) with appropriate computational tolerances that reflect the spread of different DFT implementations. For the doped compounds it also checks the required energy ordering: energy_FM < energy_NM for B0.9375V0.0625N and energy_FM < energy_AFM for B0.875V0.125N. You do not need to know the exact reference values—simply running the protocol described and extracting the quantities correctly is sufficient. Each scored stage carries a weight, and the final reward is the weighted combination. Reporting numbers that cannot be derived from the DFT workflow is not rewarded; the verifier expects the results to be the genuine output of the prescribed calculations.
