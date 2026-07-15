# DFT Calculations for Atomically Dispersed FeNC Gas Sensor

## Problem background
Gas sensors based on metal oxide semiconductors often suffer from poor selectivity and require high operating temperatures, which limits their deployment in low-power, room-temperature applications. Atomically dispersed non-precious metal catalysts offer uniform active sites with high catalytic efficiency and could provide a route to selective, room-temperature gas detection. In particular, a material consisting of single iron atoms coordinated by four nitrogen atoms on a carbon support (FeN₄) has been proposed as a candidate for sensing NO₂. The hypothesized mechanism involves catalytic decomposition of NO₂ on the FeN₄ site, enabling a detectable change in electrical resistance at ambient conditions. To understand the origin of the sensing behavior, first-principles electronic structure calculations are needed to quantify the electronic properties, gas adsorption affinities, charge transfer, and catalytic reaction barriers.

## Approach
The reproduction relies on spin‑polarized density functional theory (DFT) calculations to study the FeN₄–graphene system. A supercell model of graphene containing one FeN₄ center is constructed. First, the geometric structure is relaxed and the electronic band structure and density of states are computed to determine the band gap and the type of semiconducting character. Next, adsorption energies are calculated for six gases—NO₂, NO, NH₃, H₂, CO₂, and CH₄—by placing each molecule on the Fe site and optimizing the combined system; the adsorption energy is defined as the energy of the adsorbate–surface complex minus the energies of the separated surface and gas‑phase molecule. For the most strongly adsorbed molecule, Bader charge analysis quantifies the net electron transfer and the redistribution of charge among the atoms, and the N–O bond length in the adsorbed state is extracted and compared with the bond length of a free NO₂ molecule. Finally, the catalytic decomposition of NO to N₂ and O₂ on the FeN₄ site is investigated using the climbing‑image nudged elastic band (CI‑NEB) method to locate the minimum energy path and to determine the activation energy barrier.

## Reproduction target
Perform the full DFT workflow described in the steps above and collect the following computed quantities in a single JSON file named `dft_results.json`:

- `band_gap_eV`: the electronic band gap (eV) of the FeN₄‑embedded graphene model.
- `adsorption_energies_eV`: an object containing the adsorption energies (eV) for each gas (`NO2`, `NO`, `NH3`, `H2`, `CO2`, `CH4`), where a negative value indicates binding.
- `charge_transfer_NO2`: an object with the total electron transfer (e) from the surface to NO₂ (`total_electron_transfer`) and the per‑atom net charges for the Fe atom (`Fe_net_charge`), the N atom in NO₂ (`N_NO2_net_charge`), and the two O atoms combined (`O_NO2_net_charge`).
- `NO_bond_length_adsorbed_A`: the N–O bond length (in Å) of the adsorbed NO₂ molecule.
- `activation_barrier_eV`: the activation energy barrier (eV) for the NO + NO* → O₂ + N₂ reaction on the FeN₄ site.

All numerical values must be reported in the specified units.

## Assets

- DFT calculation package (Quantum ESPRESSO or equivalent): https://www.quantum-espresso.org/
- PAW pseudopotentials for C, N, Fe, O, H: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Geometry optimization and electronic structure of FeN₄ model
- Role: process
- Action: Construct a 5×5 supercell of graphene with one FeN₄ center (44 C, 4 N, 1 Fe). Perform spin-polarized DFT relaxation to obtain the optimized geometry. Compute the electronic band structure and density of states (DOS). Record the band gap and confirm n-type semiconducting character.
- Evidence: `/app/outputs/geometry_bandgap.log`

### Step 2: Adsorption energy calculations for six gases
- Role: process
- Action: Place each gas molecule (NO₂, NO, NH₃, H₂, CO₂, CH₄) near the Fe site of the relaxed surface and optimize the combined geometry. For each gas, compute the adsorption energy as E_ads = E(surface+gas) − E(surface) − E(gas).
- Evidence: `/app/outputs/adsorption_energies.log`

### Step 3: Bader charge analysis and bond length change upon NO₂ adsorption
- Role: process
- Action: On the optimized NO₂-adsorbed structure, perform Bader charge analysis to quantify net electron transfer from the surface to the NO₂ molecule. Compute total charge transferred and per-atom contributions (Fe, N in NO₂, O in NO₂). Also extract the N-O bond length in the adsorbed NO₂ and compare with the free-molecule length.
- Evidence: `/app/outputs/bader_analysis.log`

### Step 4: CI-NEB calculation of NO decomposition barrier
- Role: process
- Action: Set up initial and final states for the reaction NO + NO* → O₂ + N₂ on the FeN₄ site. Use the climbing-image nudged elastic band (CI-NEB) method to find the minimum energy path and determine the activation energy barrier.
- Evidence: `/app/outputs/neb_barrier.log`

### Step 5: Aggregate all computed DFT results into a single JSON
- Role: scored (load-bearing)
- Action: Collect all computed quantities from the previous steps: band gap (eV), adsorption energies (eV) for NO₂, NO, NH₃, H₂, CO₂, CH₄, total and per-atom electron transfer (e) for NO₂ adsorption, N-O bond length (Å) in adsorbed NO₂, and CI-NEB activation energy barrier (eV). Write them to dft_results.json with the specified schema.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: JSON object with keys: 'band_gap_eV' (float), 'adsorption_energies_eV': {'NO2': float, 'NO': float, 'NH3': float, 'H2': float, 'CO2': float, 'CH4': float}, 'charge_transfer_NO2': {'total_electron_transfer': float, 'Fe_net_charge': float, 'N_NO2_net_charge': float, 'O_NO2_net_charge': float}, 'NO_bond_length_adsorbed_A' (float), 'activation_barrier_eV' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated DFT calculation results for the FeN₄-based gas sensor model.
- schema:
  - `type`: object
  - `required_keys`: `band_gap_eV`, `adsorption_energies_eV`, `charge_transfer_NO2`, `NO_bond_length_adsorbed_A`, `activation_barrier_eV`
  - `properties`:
    - `band_gap_eV`: number
    - `adsorption_energies_eV`:
      - `type`: object
      - `required_keys`: `NO2`, `NO`, `NH3`, `H2`, `CO2`, `CH4`
      - `values`: number
    - `charge_transfer_NO2`:
      - `type`: object
      - `required_keys`: `total_electron_transfer`, `Fe_net_charge`, `N_NO2_net_charge`, `O_NO2_net_charge`
      - `values`: number
    - `NO_bond_length_adsorbed_A`: number
    - `activation_barrier_eV`: number

Notes: All numerical values must be in the specified units. The hidden checker will compare each field against paper-reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "band_gap_eV",
          "adsorption_energies_eV",
          "charge_transfer_NO2",
          "NO_bond_length_adsorbed_A",
          "activation_barrier_eV"
        ],
        "properties": {
          "band_gap_eV": "number",
          "adsorption_energies_eV": {
            "type": "object",
            "required_keys": [
              "NO2",
              "NO",
              "NH3",
              "H2",
              "CO2",
              "CH4"
            ],
            "values": "number"
          },
          "charge_transfer_NO2": {
            "type": "object",
            "required_keys": [
              "total_electron_transfer",
              "Fe_net_charge",
              "N_NO2_net_charge",
              "O_NO2_net_charge"
            ],
            "values": "number"
          },
          "NO_bond_length_adsorbed_A": "number",
          "activation_barrier_eV": "number"
        }
      },
      "description": "Aggregated DFT calculation results for the FeN₄-based gas sensor model."
    }
  ],
  "notes": "All numerical values must be in the specified units. The hidden checker will compare each field against paper-reported values with appropriate tolerances."
}
```

## How you are scored
Your submission will be scored automatically by a hidden verifier. The verifier reads the `dft_results.json` file you produce and compares each numerical entry against internal reference criteria. The final score is based on how many entries meet the criteria, with the primary weight on the band gap, the six adsorption energies, and the activation barrier. The verifier does not require exact matches; it allows for the systematic shifts that arise from different DFT implementations, pseudopotentials, and computational parameters. However, the criteria are derived from the underlying physical values, so guessing or reporting literature values without performing the required first‑principles calculations is extremely unlikely to succeed. The verifier does not inspect files other than the declared scored output; all intermediate evidence logs are for your own documentation.
