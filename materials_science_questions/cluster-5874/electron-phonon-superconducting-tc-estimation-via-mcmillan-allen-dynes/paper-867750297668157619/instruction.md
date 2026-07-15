# DFT Electronic Structure of Stoichiometric MoB2

## Problem background
The electronic structure of stoichiometric MoB2 in the AlB2-type structure is essential for interpreting its superconducting properties. The total density of states at the Fermi energy, N(E_F), and the electronic specific heat coefficient, γ, are key quantities needed to estimate the electron–phonon coupling strength and to compare with experimental measurements. First-principles calculations can provide these numbers, serving as an independent reference.

## Approach
Perform a first-principles density-functional theory (DFT) calculation on MoB2 using the local density approximation (LDA) for exchange and correlation. The crystal structure is AlB2-type (space group P6/mmm) with lattice parameters a = 3.055 Å, c = 3.128 Å. The atomic positions are: Mo at (0,0,0) and B at the two 2d sites (1/3,2/3,1/2) and (2/3,1/3,1/2). Converge the total energy with respect to k-point sampling and planewave cutoff in a self-consistent field (SCF) run. Then compute the density of states (DOS) on a fine energy mesh. From the total DOS at the Fermi level, N(E_F), derive the electronic specific heat coefficient using the free-electron relation γ = (π²/3) k_B² N(E_F), and convert to units of mJ/(mol K^2) per formula unit of MoB2.

## Reproduction target
Produce the total density of states at the Fermi energy N(E_F) (in states per eV per unit cell) and the electronic specific heat coefficient γ (in mJ/(mol K^2)) for stoichiometric MoB2 computed with DFT-LDA as described. Save both values in the JSON file `/app/outputs/step_02_electronic_properties.json` with keys `N_EF` and `gamma`.

## Assets

- First-principles DFT code supporting LDA (e.g., Quantum ESPRESSO, ABINIT, GPAW): https://www.quantum-espresso.org/
- LDA pseudopotentials for Mo and B: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT calculation of stoichiometric MoB2
- Role: process
- Action: Perform a self-consistent field (SCF) DFT calculation on MoB2 in the AlB2 structure (space group P6/mmm, a=3.055 Å, c=3.128 Å, Mo at (0,0,0), B at (1/3,2/3,1/2) and (2/3,1/3,1/2)) using the LDA exchange-correlation functional. Converge total energy with respect to k-point sampling and plane-wave cutoff. Subsequently calculate the density of states (DOS) over a fine energy mesh. Write the detailed DFT output to the evidence file.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Extract N(E_F) and compute γ
- Role: scored (load-bearing)
- Action: From the DFT DOS output, extract the total density of states at the Fermi level N(E_F) in states per eV per unit cell. Compute the electronic specific heat coefficient γ = (π²/3) k_B² N(E_F) and convert to mJ/(mol K^2) per formula unit of MoB2. Save both values into the output JSON file.
- Output file: `/app/outputs/step_02_electronic_properties.json`
- Format: json
- Contract: {"N_EF": float (states/eV per cell), "gamma": float (mJ/(mol K^2))}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_electronic_properties.json
- path: `/app/outputs/step_02_electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic structure properties of stoichiometric MoB2 computed with DFT-LDA: the total density of states at the Fermi level N(EF) and the electronic specific heat coefficient γ.
- schema:
  - `type`: object
  - `required`: `N_EF`, `gamma`
  - `properties`:
    - `N_EF`:
      - `type`: number
      - `description`: Total density of states at the Fermi energy, in states per eV per unit cell
    - `gamma`:
      - `type`: number
      - `description`: Electronic specific heat coefficient, in mJ/(mol K^2)

Notes: The scoring compares N_EF and γ to the paper-reported reference values within a relative tolerance. The DFT code must use LDA pseudopotentials, the correct AlB2 structure, and the specified lattice parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "N_EF",
          "gamma"
        ],
        "properties": {
          "N_EF": {
            "type": "number",
            "description": "Total density of states at the Fermi energy, in states per eV per unit cell"
          },
          "gamma": {
            "type": "number",
            "description": "Electronic specific heat coefficient, in mJ/(mol K^2)"
          }
        }
      },
      "description": "Electronic structure properties of stoichiometric MoB2 computed with DFT-LDA: the total density of states at the Fermi level N(EF) and the electronic specific heat coefficient γ."
    }
  ],
  "notes": "The scoring compares N_EF and γ to the paper-reported reference values within a relative tolerance. The DFT code must use LDA pseudopotentials, the correct AlB2 structure, and the specified lattice parameters."
}
```

## How you are scored
A hidden verifier reads your output JSON and confirms that it contains both required fields. It checks that γ is internally consistent with N(E_F) via the standard free-electron formula. It then compares your computed N(E_F) and γ to a hidden reference. The scoring rewards results that are close to the reference; small deviations slightly reduce the reward, while large discrepancies yield low or zero reward for this stage. The overall task reward is a weighted combination of the scores from all stages.
