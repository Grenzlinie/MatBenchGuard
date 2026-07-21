# Kinetic Monte Carlo Simulation of Surface Catalytic Kinetics

## Problem background
Ethylene hydrogenation over palladium catalysts is an industrially important reaction whose kinetics exhibit complex coverage‑ and ensemble‑size‑dependent behaviour that is poorly captured by traditional mean‑field models. A first‑principles‑based multisite kinetic Monte Carlo (KMC) simulation can explicitly track the spatial and temporal changes of surface intermediates (H, C₂H₄, C₂H₅) on a periodic Pd(100) grid with atop, bridge, and hollow sites. The resulting simulation yields the apparent activation energy and the kinetic orders with respect to hydrogen and ethylene, which are key quantities that experimental studies try to measure.

## Approach
The simulation uses a multisite lattice representing the Pd(100) surface with atop, bridge, and hollow sites and periodic boundary conditions. Each adsorbate species (H, C₂H₄, C₂H₅) is assigned site‑specific zero‑coverage binding energies and a reaction radius (see the parameter tables in the workflow steps). Lateral interactions between adsorbates are described by a Radial Function (RF) model whose parameters cover all pairwise combinations. Coverage‑dependent activation barriers are computed from bond‑order conservation (BOC) relations that are anchored to zero‑coverage density functional theory (DFT) barriers. The KMC engine enumerates all possible adsorption, desorption, and surface reaction events, calculates their coverage‑dependent rates, advances time with a variable step, and equilibrates fast processes via Metropolis steps. From the simulation runs, ethane turnover frequencies (molecules per site per second) are extracted. The apparent activation energy is obtained by fitting the Arrhenius equation to temperature‑dependent TOF data, and the kinetic orders are determined from TOF data collected under varying gas partial pressures.

## Reproduction target
Run the implemented KMC code at the following conditions and produce the specified output files:

- Step 1: Run at six temperatures (248, 273, 298, 336, 386, 436 K) with H₂ partial pressure = 100 Torr and C₂H₄ partial pressure = 25 Torr. Record the steady‑state ethane turnover frequency (TOF) in `arrhenius_tof.csv`.
- Step 2: Fit the Arrhenius equation to the data in `arrhenius_tof.csv` and write the fitted activation energy (in kcal/mol) to `activation_energy_kcal.txt`.
- Step 3: At 298 K, run simulations for the following pressure variations: H₂ at 50, 100, 150 Torr (C₂H₄ fixed at 25 Torr) and C₂H₄ at 10, 25, 50 Torr (H₂ fixed at 100 Torr). Record the TOF for each condition in `orders_simulation.csv`.

The hidden verifier will recompute the activation energy and kinetic orders from your raw data files and compare them to reference values. Your submission will be judged on the recomputed quantities, not on any self‑reported number alone.

## Assets
No external datasets, model checkpoints, or third‑party simulation packages are required. All numerical parameters needed for the simulation (binding energies, reaction radii, interaction model constants, pre‑exponentials, and sticking coefficients) are provided in the workflow steps. You must implement the KMC algorithm from scratch in a language of your choice, using standard scientific computing libraries (e.g., NumPy, SciPy) as needed.

## Workflow steps

### Step 1: Re-implement the kinetic Monte Carlo algorithm
- Role: process
- Action: Re-implement the multisite kinetic Monte Carlo algorithm for ethylene hydrogenation on Pd(100). Follow the detailed specifications below.

**Lattice and sites:**
- Construct a periodic grid of size 20×20 metal atoms with atop, bridge, and hollow sites. Use periodic boundary conditions. Metal–metal distance = 2.75 Å. The area of one surface site = (2.75 Å)² / 4 = 1.890625 Å².

**Adsorbate properties:**
- Zero‑coverage binding energies (kcal/mol):
  - Hydrogen: atop 47.3, bridge 58.3, hollow 62.9
  - Ethylene (C₂H₄): atop 7.0, bridge 14.0 (no hollow)
  - Ethyl (C₂H₅): atop 31.0, bridge 17.9 (no hollow)
- Reaction radii: H = 1.39 Å, C₂H₄ = 2.0 Å, C₂H₅ = 2.0 Å. A reaction between two adsorbates is possible only if the distance between their site centres is less than the sum of their reaction radii.

**Radial Function (RF) interaction model:**
- Interaction energy between two adsorbates at distance r (Å):
  E_int(r) = (ζ_ij / 2) * [ exp(-(r - γ_ij)/ε_i)/r + exp(-(r - γ_ij)/ε_j)/r ]
  with γ_ij = (γ_i + γ_j)/2. All energies in kcal/mol. Parameters:
  Species | ε (Å) | γ (Å)
  --------|-------|------
  H       | 0.3   | 0.8
  C₂H₄    | 0.6   | 1.5
  C₂H₅    | 0.9   | 2.0

  Pairwise ζ_ij (kcal·mol⁻¹·Å):
    H–H       | 3.0
    C₂H₄–C₂H₄ | 1.5
    C₂H₅–C₂H₅ | 2.0
    H–C₂H₄    | 0.75
    H–C₂H₅    | 0.75
    C₂H₄–C₂H₅ | 1.2
  (Matrix is symmetric.)
- The coverage‑dependent binding energy of an adsorbate is its zero‑coverage binding energy minus the sum of all repulsive interactions from neighbours within a cut‑off radius of 2.5 times the metal–metal distance (6.875 Å). If a calculated interaction is negative, set it to zero (no attraction).

**Bond‑Order Conservation (BOC) activation barriers:**
- The coverage‑dependent activation energies are computed using the BOC relations, with a constant scaling factor γ chosen for each reaction so that the zero‑coverage limit reproduces the DFT barriers given below.
  Let Q_A, Q_B, Q_AB be the local (coverage‑dependent) binding energies of species A, B, and AB at their respective sites (kcal/mol). Define the gas‑phase bond dissociation energy D_AB (kcal/mol):
    For reaction C₂H₄* + H* ⇌ C₂H₅* + *:  D_AB = 100.0
    For reaction C₂H₅* + H* → C₂H₆(g) + 2*: D_AB = 100.0
    For reaction H* + H* ⇌ H₂(g) + 2*:        D_HH = 104.0
  The BOC reference energy is:
    ΔE*_AB,g^LJ = D_AB − (Q_A + Q_B) + (Q_A·Q_B)/(Q_A + Q_B)                      (1)
  The barrier for AB dissociation from the gas phase:
    ΔE*_AB,g = 0.5·(ΔE*_AB,g^LJ − Q_AB) + γ                                     (2)
  The barrier for AB dissociation on the surface (AB* + * → A* + B*):
    ΔE*_AB,s = ΔE*_AB,g + Q_AB                                                   (3)
  The barrier for surface recombination (A* + B* → AB* + *):
    ΔE*_A−B,s = Q_A + Q_B − D_AB + ΔE*_AB,g                                      (4)
  For recombination that directly yields a gas‑phase product (A* + B* → AB(g) + 2*):
    ΔE*_A−B,g = ΔE*_A−B,s^LJ   if  ΔE*_A−B,s^LJ ≥ 0
                = Q_A + Q_B − D_AB + γ   otherwise.                              (5)
  The parameter γ for each reaction is determined by requiring that in the zero‑coverage limit (all interactions zero) the forward activation barrier for the hydrogenation direction equals the DFT value:
    • C₂H₄(ads) + H(ads) → C₂H₅(ads) + *:  Ea⁰ = 15.0 kcal/mol  (corrected)
    • C₂H₅(ads) + H(ads) → C₂H₆(g) + 2*:   Ea⁰ = 14.5 kcal/mol (corrected)
  For H₂ desorption (2 H* → H₂(g) + 2*), use the same BOC recombination‑to‑gas formulas with D_AB=104.0 and the zero‑coverage desorption barrier set to 18.0 kcal/mol (to determine γ). For H₂ adsorption (the reverse), the barrier is taken from the BOC relation automatically.

**Rate constants:**
- Adsorption of gas‑phase species i onto a site follows:
    r_ads,i = S₀ · P_i · Area · (2π·MW_i·R·T)^{-0.5} · exp(-E_a/(R T))
  where Area = (2.75 Å)²/4, MW in kg/mol, R=1.987e-3 kcal/(mol·K). For H₂, S₀=0.1, MW=0.002; for C₂H₄, S₀=1.0, MW=0.02805. The activation energy E_a for adsorption is taken as 0 (no barrier for molecular adsorption).
- Desorption of C₂H₄ is unimolecular with preexponential 10⁹ s⁻¹ and barrier equal to the current coverage‑dependent binding energy of the adsorbate.
- Surface reaction events (hydrogenation steps) use preexponential 10¹³ s⁻¹ and barriers computed via BOC as above.
- H₂ desorption is treated as a bimolecular surface reaction (2 H* → H₂(g) + 2*) with preexponential 10¹³ s⁻¹ and BOC barrier.

**KMC algorithm:**
- 1. Build all possible events (adsorption on each empty site, desorption of each adsorbate, surface reaction for each pair of neighbours that satisfies the reaction radius condition, including H₂ desorption).
- 2. Compute rates for each event using the coverage‑dependent binding energies and BOC barriers.
- 3. Sum all rates Σr_i. Draw a uniform random number ξ ∈ (0,1]. Advance time by Δt = −ln(ξ)/Σr_i.
- 4. Choose a reaction by sampling from the cumulative probability distribution of the rates.
- 5. Execute the chosen event; update the grid species and occupancies.
- 6. Equilibrate fast processes (ethylene adsorption/desorption and hydrogen diffusion) using Metropolis Monte Carlo: attempt N_equil moves (e.g., 100) where each move consists of randomly selecting an adsorbate and a neighbouring empty site, computing the energy change, and accepting with probability min(1, exp(−ΔE/(k_B T))).
- 7. Repeat until steady‑state turnover is reached (monitor cumulative C₂H₆ molecules produced).
- The implementation will be used in later steps.
- Evidence: none

### Step 2: Simulate temperature-dependent turnover frequencies
- Role: scored
- Action: Run the KMC simulation at six temperatures (248, 273, 298, 336, 386, 436 K) while holding H2 partial pressure at 100 Torr and C2H4 partial pressure at 25 Torr. Record the steady-state ethane turnover frequency (TOF) in molecules per site per second. Output a CSV file with the results.
- Output file: `/app/outputs/arrhenius_tof.csv`
- Format: csv
- Contract: Columns: Temperature (K), TurnoverFrequency (s⁻¹). Six rows, one per temperature.
- Scoring: scored by hidden verifier

### Step 3: Fit Arrhenius law and report apparent activation energy
- Role: scored (load-bearing)
- Action: Fit the Arrhenius equation ln(TOF) = -Ea/(R*T) + constant to the data from step1 using linear regression. Output a single number representing the apparent activation energy Ea in kcal/mol.
- Output file: `/app/outputs/activation_energy_kcal.txt`
- Format: txt
- Contract: A single floating-point number representing Ea in kcal/mol.
- Scoring: scored by hidden verifier

### Step 4: Simulate kinetic order data
- Role: scored
- Action: Run the KMC simulation at 298 K while varying H2 partial pressure (50, 100, 150 Torr) at fixed C2H4 = 25 Torr, and varying C2H4 partial pressure (10, 25, 50 Torr) at fixed H2 = 100 Torr. For each condition record the steady-state TOF. Output a CSV file with the results.
- Output file: `/app/outputs/orders_simulation.csv`
- Format: csv
- Contract: Columns: experiment_label (string, e.g. 'H2_50', 'C2H4_10'), Pressure_Torr (float), TurnoverFrequency_s-1 (float). At least 6 rows covering the prescribed pressure variations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/arrhenius_tof.csv`
- `/app/outputs/activation_energy_kcal.txt`
- `/app/outputs/orders_simulation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### arrhenius_tof.csv
- path: `/app/outputs/arrhenius_tof.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw TOF vs temperature data; the checker will recompute the apparent activation energy from these points.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `TurnoverFrequency (s⁻¹)`
  - `units`:
    - `Temperature (K)`: K
    - `TurnoverFrequency (s⁻¹)`: s⁻¹

### activation_energy_kcal.txt
- path: `/app/outputs/activation_energy_kcal.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The agent-reported activation energy; used as a reference, with primary scoring via recomputation from arrhenius_tof.csv.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the fitted activation energy in kcal/mol.

### orders_simulation.csv
- path: `/app/outputs/orders_simulation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: TOF data at varying H₂ and C₂H₄ pressures; the checker will recompute the kinetic orders from these points.
- schema:
  - `type`: table
  - `required_columns`: `experiment_label`, `Pressure_Torr`, `TurnoverFrequency_s-1`
  - `units`:
    - `Pressure_Torr`: Torr
    - `TurnoverFrequency_s-1`: s⁻¹

Notes: The verifier will check activation energy and kinetic orders against acceptable ranges; the exact ranges are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "arrhenius_tof.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "TurnoverFrequency (s⁻¹)"
        ],
        "units": {
          "Temperature (K)": "K",
          "TurnoverFrequency (s⁻¹)": "s⁻¹"
        }
      },
      "description": "Raw TOF vs temperature data; the checker will recompute the apparent activation energy from these points."
    },
    {
      "file": "activation_energy_kcal.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the fitted activation energy in kcal/mol."
      },
      "description": "The agent-reported activation energy; used as a reference, with primary scoring via recomputation from arrhenius_tof.csv."
    },
    {
      "file": "orders_simulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "experiment_label",
          "Pressure_Torr",
          "TurnoverFrequency_s-1"
        ],
        "units": {
          "Pressure_Torr": "Torr",
          "TurnoverFrequency_s-1": "s⁻¹"
        }
      },
      "description": "TOF data at varying H₂ and C₂H₄ pressures; the checker will recompute the kinetic orders from these points."
    }
  ],
  "notes": "The verifier will check activation energy and kinetic orders against acceptable ranges; the exact ranges are not disclosed to the agent."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier program that reads the files you produce under `/app/outputs`. The verifier will:

- Read `arrhenius_tof.csv` and recompute the apparent activation energy from the temperature–TOF pairs by linear regression of ln(TOF) vs 1/T.
- Read `orders_simulation.csv` and recompute the kinetic orders with respect to H₂ and C₂H₄ using log‑log regression.
- Compare the recomputed activation energy to a pre‑defined acceptable range (hidden from you) and assign a partial score; full credit if the recomputed value falls within the range, decreasing otherwise.
- Compare the recomputed kinetic orders to hidden expected ranges and assign scores similarly.
- Perform basic structural checks (positive TOF values, expected monotonic trends) as a low‑weight sanity test.

The final reward is a weighted sum of these partial scores. Simply writing the paper's reported numbers in `activation_energy_kcal.txt` will not suffice because the verifier independently recomputes the key metrics from your raw data files. You must genuinely run the simulation and produce consistent TOF data that leads to activation energy and kinetic orders within the expected tolerance.
