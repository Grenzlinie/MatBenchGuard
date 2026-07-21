# Monte Carlo Modeling of 2D Islanding to Extract Intermolecular and Corrugation Potentials

## Problem background
When dodecane molecules are deposited at submonolayer coverages on a clean Au(111) surface, they can form two-dimensional islands whose ordering depends on temperature. At low temperature the molecules pack into dense islands; at higher temperature they form a dilute 2D gas. Helium atom reflectivity is exquisitely sensitive to the fraction of bare gold, because a single adsorbed molecule reduces the reflectivity over an area much larger than its own footprint due to long-range scattering effects. By measuring the specular helium intensity while cooling or after a fresh dose, the degree of islanding can be tracked. This experimental system provides a route to extract two important energetic quantities: the lateral intermolecular attraction between dodecane molecules on gold, and the corrugation energy that a molecule must overcome to hop across the surface. Determining these energies from the observed ordering transitions is the goal of this task.

## Approach
A Monte Carlo lattice‑gas model captures the physics of island ordering. Molecules sit on a two‑dimensional hexagonal lattice (500×500 sites with periodic boundaries). Each molecule interacts with its six nearest neighbours: four termina contacts (methyl‑group neighbours) and two lateral contacts (molecules aligned side‑by‑side). The lateral bond energy is ε; each termina bond is ε/6. Incoming helium atoms are scattered by a single molecule’s “shadow” whose area is 9 times the molecular footprint; when molecules cluster into islands the shadows overlap and the total blocked area drops, increasing specularity.

Molecules move by random hopping to vacant neighbouring sites. A move that lowers the system energy is always accepted; a move that raises the energy by ΔE is accepted with probability P = exp(−ΔE/kB T) (a Boltzmann factor). The simulation does NOT include an explicit corrugation energy in the move acceptance; this is equivalent to setting the attempt frequency equal for all moves and only paying the lateral bond energy cost. The model can therefore reproduce the qualitative ordering behaviour, and the missing corrugation energy is later extracted by comparing simulated rates to experimental ones.

Two types of simulation are required:

(1) Cooling simulation at ~30% coverage: start from a random configuration at high temperature and cool slowly (1 million Monte Carlo iterations per unit of ε/kB). Record the specular intensity as a function of temperature in model units (temperature = T* ε/kB). The knee (inflection point) of this curve gives a dimensionless knee temperature T_knee (in model units). Using the experimentally known knee temperature of 200 K, the lateral bond energy follows from ε = (200 K × kB) / T_knee.

(2) Recovery simulations at ~5% coverage: start from a random configuration and evolve at constant temperature, recording specular intensity vs Monte Carlo iterations per molecule. Run at several temperatures spanning the range 0.18–0.22 ε/kB (at least three distinct values). For each temperature, extract the rate at which specularity rises (the recovery rate r_mod, in units of change per MC iteration).

The physical time per MC move is taken to be τ0 = 10⁻¹⁵ s. The experimentally observed recovery rates r_exp (in s⁻¹) at the corresponding temperatures are provided below. The relation r_exp = (r_mod / τ0) × exp(−E_c / kB T) allows the corrugation energy E_c to be obtained by fitting or by comparing at a single temperature. Use the following reference experimental recovery rates:

- At T = 0.18 ε/kB: r_exp ≈ 0.02 s⁻¹
- At T = 0.20 ε/kB: r_exp ≈ 0.04 s⁻¹
- At T = 0.22 ε/kB: r_exp ≈ 0.08 s⁻¹

(These values are approximate; the hidden verifier uses the standard method to check the resulting corrugation energy against a gold reference.)

## Reproduction target
Implement the Monte Carlo model and run the cooling and recovery protocols described above. From the cooling curve, determine the lateral intermolecular potential ε (in eV). From the recovery curves, determine the corrugation energy E_c (in eV). Write both values to the JSON file /app/outputs/potentials.json, under the keys "epsilon_eV" and "corrugation_eV" (both floating‑point numbers). The experimental knee temperature (200 K) and the recovery‑rate reference set given in the approach are the only external calibration data you need; all other quantities are produced by the simulation and analysis.

## Assets

- Python 3 interpreter
- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Run Monte Carlo cooling simulation
- Role: process
- Action: Implement the hexagonal lattice MC model (500×500, periodic boundaries, lateral bond ε, terminal bond ε/6, Boltzmann acceptance, shadowing rule Σ/A=9) and run a cooling simulation at ~30% coverage to produce a specularity‑versus‑temperature curve in model units (temperature in ε/k_B). The simulation should use a cooling rate of 1 million iterations per ε/k_B.
- Evidence: `/app/outputs/cooling_curve.csv`

### Step 2: Run Monte Carlo recovery simulations
- Role: process
- Action: Using the same model, run recovery simulations at ~5% coverage for several temperatures (in units of ε/k_B) to obtain specularity‑versus‑time curves. At least three temperatures in the range 0.18–0.22 ε/k_B should be simulated to allow rate extraction.
- Evidence: `/app/outputs/recovery_curves.csv`

### Step 3: Extract interaction potentials
- Role: scored (load-bearing)
- Action: From the simulated cooling curve, locate the knee temperature T_knee in model units. Compute the lateral bond energy ε in eV as ε = (200 K × k_B) / T_knee, where 200 K is the known experimental knee temperature. From the recovery curves, estimate the recovery rate at each simulated temperature, compare with the published experimental recovery rates, and calculate the corrugation energy E_c using the Boltzmann‑factor ratio. Output both values in /app/outputs/potentials.json.
- Output file: `/app/outputs/potentials.json`
- Format: json
- Contract: JSON object with keys: "epsilon_eV" (float) and "corrugation_eV" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/potentials.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### potentials.json
- path: `/app/outputs/potentials.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: To-be-reproduced lateral intermolecular potential ε (in eV) and corrugation energy E_c (in eV) for dodecane on Au(111).
- schema:
  - `type`: object
  - `required`:
    - `epsilon_eV`: float
    - `corrugation_eV`: float

Notes: The two energies are expected in eV. The checker compares them to hidden gold values within tolerances to account for stochastic run-to-run spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "potentials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_eV": "float",
          "corrugation_eV": "float"
        }
      },
      "description": "To-be-reproduced lateral intermolecular potential ε (in eV) and corrugation energy E_c (in eV) for dodecane on Au(111)."
    }
  ],
  "notes": "The two energies are expected in eV. The checker compares them to hidden gold values within tolerances to account for stochastic run-to-run spread."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/potentials.json` file. It extracts the numeric values of `epsilon_eV` and `corrugation_eV` and compares each to a hidden gold reference, using appropriate tolerances to account for the stochastic nature of the simulation. Both extracted values must fall within their respective tolerance windows to earn the full reward (1.0); if either value falls outside, the reward is 0.0. The intermediate CSV outputs (cooling_curve.csv, recovery_curves.csv) are not used for scoring; only the final JSON file matters. There is no partial credit. The verifier does not have access to the source paper and evaluates only the numbers you provide.
