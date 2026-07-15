# Miscibility Gap Simulation in Ca-Fe-Ge Garnets Using Monte Carlo

## Problem background
Garnet solid solutions with coupled cation substitutions exhibit complex mixing behaviour due to charge and size mismatch. The Ca3Fe2Ge3O12–Ca4Ge4O12 solid solution is a structural analogue for pyrope–majorite, and its mixing properties, including the possible existence of a miscibility gap, have implications for understanding phase relations in Earth’s mantle. Determining the temperature–composition phase boundaries of this system through atomistic simulations provides a stringent test for computational models of mixing in complex solid solutions.

## Approach
The mixing behaviour is modelled using a cluster expansion Hamiltonian. The energy of any cation configuration on the octahedral sublattice is expressed in terms of pairwise interaction constants (J) for exchanging cations at various distances, quaternary interaction constants (Q) for tetrahedral clusters that distinguish occupancy around tetrahedral cations, and a non‑configurational term that depends on composition alone. These constants were derived from static lattice energy calculations and are provided as numerical inputs.

Using these parameters, Metropolis Monte Carlo simulations are performed on a 4×4×4 supercell of octahedral sites with periodic boundary conditions. Cation swaps are attempted and accepted according to the Metropolis criterion, sampling the equilibrium distribution over a grid of compositions and temperatures. The average excess configurational enthalpy per mole of octahedral cations is collected.

To obtain configurational free energies, the method of thermodynamic integration is employed. The interaction constants are scaled by a factor λ from 0 (complete disorder) to 1 (full interactions), and Monte Carlo simulations are run at each λ value. The λ‑averaged excess enthalpy is numerically integrated to yield the free energy of mixing. From the resulting free‑energy isotherms, the compositions marking the miscibility gap boundaries are extracted for each temperature by locating the common‑tangent points or the change in curvature of the free energy curve.

## Reproduction target
Compute the temperature–composition miscibility gap boundaries for the Ca3Fe2Ge3O12–Ca4Ge4O12 garnet solid solution at 0 GPa. Output the boundaries as a CSV file with the columns: temperature (K), x_maj_low, x_maj_high (mole fraction of Ca‑Ge majorite). The gap boundaries should span the temperature range where a miscibility gap exists, derived solely from the free energy of mixing isotherms obtained via Monte Carlo and thermodynamic integration using the provided cluster expansion parameters at 0 GPa.

## Assets

- Cluster expansion parameters (J, Q, A12, A21 at 0 GPa)

## Workflow steps

### Step 1: Monte Carlo simulation of cation ordering
- Role: process
- Action: Set up a 4×4×4 supercell (1024 octahedral sites) with periodic boundary conditions. Using the provided cluster expansion parameters (pairwise J and quaternary Q constants, plus A12, A21) to compute energy differences, perform Metropolis Monte Carlo swaps for 32 compositions across the binary (mole fraction of Ca-Ge majorite) and over temperatures 1073–3673 K in steps of 200 K, at λ=1 (full interactions). Run each (T,X) point for sufficient MC steps (e.g., 2 million equilibration + 2 million sampling). Collect the average excess configurational enthalpy (per mole of octahedral cations) for each condition.
- Evidence: `/app/outputs/mc_enthalpies.csv`

### Step 2: Thermodynamic integration to obtain free energies
- Role: process
- Action: For the same grid of compositions and temperatures, repeat Monte Carlo simulations with scaled ordering constants Jλ = λ J, Qλ = λ Q for λ ranging from 0 to 1 in steps of 0.04. At each λ, compute the average excess enthalpy using the unscaled interaction parameters (the nominal J and Q). Numerically integrate the λ‑dependent average excess enthalpy curve (e.g., via Simpson’s rule) to obtain the configurational free energy F (per mole of octahedral cations). Output the free energy of mixing isotherms (free energy vs. composition) for each temperature.
- Evidence: `/app/outputs/free_energy_isotherms.csv`

### Step 3: Derive miscibility gap boundaries
- Role: scored (load-bearing)
- Action: From the free energy of mixing isotherms, determine for each temperature the two compositions where the second derivative of the free energy with respect to composition changes sign, or equivalently the common-tangent points marking the phase boundaries. Extract the Fe‑poor and Fe‑rich side compositions (in mole fraction of Ca‑Ge majorite, x_maj) for each temperature where a gap exists, and write the boundaries to miscibility_gap_0GPa.csv.
- Output file: `/app/outputs/miscibility_gap_0GPa.csv`
- Format: csv
- Contract: columns: temperature (K), x_maj_low, x_maj_high (mole fraction of Ca‑Ge majorite). Example: 1500,0.72,0.98
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/miscibility_gap_0GPa.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### miscibility_gap_0GPa.csv
- path: `/app/outputs/miscibility_gap_0GPa.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final scored artifact: the miscibility gap phase boundaries at 0 GPa, derived from free-energy isotherms. Checker compares these boundaries to hidden reference points digitized from the paper’s Figure 8, with tolerance in mole fraction and temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `x_maj_low`, `x_maj_high`
  - `units`:
    - `temperature`: K
    - `x_maj_low`: mole fraction Ca‑Ge majorite
    - `x_maj_high`: mole fraction Ca‑Ge majorite
  - `description`: Each row represents a temperature where a miscibility gap exists. x_maj_low and x_maj_high are the Fe-poor and Fe-rich phase boundaries (0 < x < 1).

Notes: The intermediate mc_enthalpies.csv and free_energy_isotherms.csv are process evidence and are not scored. Only the gap boundaries are in the output contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "miscibility_gap_0GPa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "x_maj_low",
          "x_maj_high"
        ],
        "units": {
          "temperature": "K",
          "x_maj_low": "mole fraction Ca‑Ge majorite",
          "x_maj_high": "mole fraction Ca‑Ge majorite"
        },
        "description": "Each row represents a temperature where a miscibility gap exists. x_maj_low and x_maj_high are the Fe-poor and Fe-rich phase boundaries (0 < x < 1)."
      },
      "description": "Final scored artifact: the miscibility gap phase boundaries at 0 GPa, derived from free-energy isotherms. Checker compares these boundaries to hidden reference points digitized from the paper’s Figure 8, with tolerance in mole fraction and temperature."
    }
  ],
  "notes": "The intermediate mc_enthalpies.csv and free_energy_isotherms.csv are process evidence and are not scored. Only the gap boundaries are in the output contract."
}
```

## How you are scored
A hidden verifier independently evaluates your submission by comparing the boundaries in miscibility_gap_0GPa.csv to a set of reference values derived from the scientific literature. The verifier first checks the output format, then scores each boundary point based on agreement in composition and temperature. The final reward is a weighted combination of scores from all workflow stages, with the final gap boundaries carrying the highest weight. Simply reporting expected numbers without performing the Monte Carlo and thermodynamic integration is not sufficient.
