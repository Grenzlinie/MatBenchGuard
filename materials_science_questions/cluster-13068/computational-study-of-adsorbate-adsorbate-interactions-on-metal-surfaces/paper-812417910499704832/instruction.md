# Monte Carlo Simulation of 2D Lattice Gas for Adatom–Adatom Interaction Energies

## Problem background
Oxygen chemisorbed on a tungsten (110) surface forms an ordered p(2×1) overlayer at low temperatures. As the temperature increases, the overlayer disorders, causing a decay in the half-order LEED beam intensities. The system can be modeled as a two-dimensional lattice gas of adatoms on a rectangular lattice of binding sites, with pairwise adatom–adatom interactions up to fourth neighbors (first and fourth neighbor interactions are attractive, second and third are repulsive). Monte Carlo simulations relate the order–disorder transition temperature at a given coverage to the underlying interaction energies; thus, experimentally measured LEED intensity–temperature (I–T) curves at different coverages can be used to determine the pairwise interaction energies.

## Approach
Implement a Monte Carlo simulation on a 30×30 rectangular lattice of binding sites (positions indexed by (i,j), where i,j = 1,…,30) with periodic boundary conditions. The adatoms experience pairwise interactions ε₁ (attractive), ε₂ = ε₃ (repulsive), and ε₄ (attractive), corresponding to the following neighbor vectors (distance‑sorted according to the physical geometry of the p(2×1) overlayer):

| Parameter | Neighbor vectors (offsets from site (i,j)) | Sign |
|-----------|--------------------------------------------|------|
| ε₁        | (±1, ±1)   (four diagonal sites)          | < 0  |
| ε₂        | (±2, 0)    (two sites along the x–axis, one site apart) | > 0  |
| ε₃        | (0, ±2)    (two sites along the y–axis, one site apart) | > 0  |
| ε₄        | (±1, 0), (0, ±1)  (four nearest axial sites)          | < 0  |

The total interaction energy of a configuration is

$$E = \frac{1}{2} \sum_{i=1}^{30} \sum_{j=1}^{30} L(i,j)\left[ N_1(i,j)\,\epsilon_1 + N_2(i,j)\,\epsilon_2 + N_3(i,j)\,\epsilon_3 + N_4(i,j)\,\epsilon_4 \right],$$

where \(L(i,j) = 1\) if site \((i,j)\) is occupied by an adatom and \(0\) otherwise, and \(N_a(i,j)\) is the number of occupied neighbors of type \(a\) around \((i,j)\).

At each simulation step a random adatom hop is proposed: an occupied site and an empty site are chosen at random. The energy change \(\Delta E\) between the two sites is calculated. The move is accepted with probability

$$P = \min\Bigl(1,\; e^{-\Delta E/(k_B T)}\Bigr),$$

which is equivalent to the Metropolis algorithm and guarantees detailed balance. (The arbitrary distance weighting mentioned in the reference does not affect equilibrium configurations and may be omitted.)

The normalized LEED intensities of the two perpendicular domains are computed as

$$I^{(1)} = \frac{1}{N^2}\left[\sum_{i=1}^{30}\sum_{j=1}^{30} L(i,j)\,(-1)^i\right]^2, \qquad
I^{(2)} = \frac{1}{N^2}\left[\sum_{i=1}^{30}\sum_{j=1}^{30} L(i,j)\,(-1)^j\right]^2,$$

where \(N\) is the total number of adatoms on the lattice.

The configurational entropy per adatom (in units of the Boltzmann constant \(k\)) is obtained from the equilibrium averages of the energy at a given temperature:

$$S(T) = \frac{\langle E(T)\rangle}{k_B T} + \ln Z(T),$$

where \(Z(T)\) is the partition function. In practice, \(S\) can be computed directly from the occupied‑site probabilities \(p_{ij} = \langle L(i,j)\rangle\) (the time‑averaged occupancy of each site) via the mean‑field approximation or, more rigorously, from the energy histogram using the relation \(C_V = (\langle E^2\rangle - \langle E\rangle^2)/(k_B T^2)\) and the thermodynamic integration

$$S(T) = S_{\rm ref} + \int_{T_{\rm ref}}^{T} \frac{C_V(\tau)}{\tau}\,d\tau,$$

where \(S_{\rm ref}\) is the entropy at a reference temperature (e.g., at very high temperature where the overlayer is fully disordered, \(S_{\rm ref} \approx k \ln 2\) per adatom). Implement one of these methods consistently for the entropy column.

The simulation is run at fixed coverage (θ = 0.5 and θ = 0.25). The order–disorder transition temperature is identified from the inflection point of the normalized LEED intensity versus temperature curve for the perpendicular domains (I₁, I₂).

First, perform a parameter sweep at half‑monolayer coverage (θ = 0.5). For many ratios of ε₁, ε₂, ε₄, compute the I–T curve and scale it so that its inflection point matches the experimentally known half‑monolayer transition temperature (which, based on published measurements, falls in the range 700–750 K). For each scaled set, record the interaction energies and the energy difference ΔE₁/₂ = 3ε₂ − 4ε₄.

Next, for a subset of parameter sets that reproduced the half‑monolayer transition, run simulations at quarter‑monolayer coverage (θ = 0.25). Compute I–T curves and determine the quarter‑monolayer transition temperature. Select the parameter set whose quarter‑monolayer transition temperature best matches the experimental value (the quarter‑monolayer transition is known to lie in the range 450–500 K).

Finally, use this chosen parameter set to produce the final I–T curves at both coverages and compute the heat capacity curve at θ = 0.5 from the energy fluctuations.

## Reproduction target
Produce a set of pairwise interaction energies ε₁, ε₂ (= ε₃), ε₄ (in kcal/mol) that, when used in the Monte Carlo simulation, yield order–disorder transition temperatures consistent with the experimental observations: half‑monolayer transition temperature in the range 700–750 K and quarter‑monolayer transition temperature in the range 450–500 K. For the final parameter set, generate the I–T curves (normalized LEED intensities I₁, I₂ and total energy per adatom) at θ = 0.5 and θ = 0.25, and the heat capacity curve at θ = 0.5. The half‑monolayer I–T curve must also include the configurational entropy per adatom (S, in units of k). The energy difference ΔE₁/₂ = 3ε₂ − 4ε₄ must be computed and saved. The goal is to verify that the simulation reproduces the transition temperatures and that the derived interaction parameters are internally consistent.

## Assets
No external datasets, pre-trained models, or proprietary software are required. The experiment is fully specified by the model described above and can be implemented using standard scientific computing tools. The solving agent should use Python with packages such as NumPy and SciPy for numerical operations. Matplotlib may be helpful for debugging but is not required for the final output.

## Workflow steps

### Step 1: Monte Carlo parameter sweep at half‑monolayer coverage
- Role: process
- Action: Implement a Monte Carlo simulation on a 30×30 rectangular lattice with periodic boundary conditions using the neighbor definitions and equations given in the Approach section. Use pairwise interactions ε1 (attractive), ε2=ε3 (repulsive), ε4 (attractive). Run at θ=0.5 for many parameter ratios. For each set record the scaled interaction energies and ΔE_½ = 3ε2 − 4ε4 after scaling the I–T curve such that the order–disorder transition temperature matches the experimental half‑monolayer transition (use the temperature range described in the Reproduction Target). Collect candidate parameter sets that reproduce this target.
- Evidence: none

### Step 2: Selection of final parameters via quarter‑monolayer transition
- Role: process
- Action: For candidate parameter sets from the half‑monolayer sweep, run Monte Carlo at θ=0.25. Compute I–T curves and determine the quarter‑monolayer transition temperature. Select the set whose quarter‑monolayer transition temperature best matches the experimental value (see Reproduction Target range). This set defines the final interaction energies to be saved in the next step.
- Evidence: none

### Step 3: Final interaction energies and constraint
- Role: scored
- Action: Save the selected interaction energies, the scaling factor, and the half‑monolayer constraint to /app/outputs/interaction_energies.json.
- Output file: `/app/outputs/interaction_energies.json`
- Format: json
- Contract: JSON object with keys: epsilon1 (number), epsilon2 (number), epsilon4 (number), scaling_factor (number), delta_E_half (number). All units kcal/mol except scaling_factor (dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Half‑monolayer intensity–temperature curve
- Role: scored (load-bearing)
- Action: Using the final interaction energies, run a Monte Carlo simulation at θ=0.5. Compute normalized LEED intensities I1, I2, the total interaction energy per adatom, and the configurational entropy per adatom S as functions of temperature. Save the table to /app/outputs/half_monolayer_IT_curve.csv.
- Output file: `/app/outputs/half_monolayer_IT_curve.csv`
- Format: csv
- Contract: CSV with columns: T (K), I1 (dimensionless 0–1), I2 (dimensionless 0–1), E_total (kcal/mol per adatom), S (units of k, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Quarter‑monolayer intensity–temperature curve
- Role: scored
- Action: Using the final interaction energies, run a Monte Carlo simulation at θ=0.25. Compute normalized LEED intensities I1, I2 and the total interaction energy per adatom as functions of temperature. Save the table to /app/outputs/quarter_monolayer_IT_curve.csv.
- Output file: `/app/outputs/quarter_monolayer_IT_curve.csv`
- Format: csv
- Contract: CSV with columns: T (K), I1 (dimensionless 0–1), I2 (dimensionless 0–1), E_total (kcal/mol per adatom).
- Scoring: scored by hidden verifier

### Step 6: Heat capacity curve at half‑monolayer coverage
- Role: scored
- Action: From the equilibrium configurations at θ=0.5, compute the heat capacity per adatom Cv = (⟨E²⟩ – ⟨E⟩²) / (k_B T²) for each temperature and save the curve to /app/outputs/heat_capacity_curve.csv.
- Output file: `/app/outputs/heat_capacity_curve.csv`
- Format: csv
- Contract: CSV with columns: T (K), Cv (kcal/(mol K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.json`
- `/app/outputs/half_monolayer_IT_curve.csv`
- `/app/outputs/quarter_monolayer_IT_curve.csv`
- `/app/outputs/heat_capacity_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.json
- path: `/app/outputs/interaction_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final scaled pairwise interaction energies and the half‑monolayer constraint ΔE_½ = 3ε2 − 4ε4.
- schema:
  - `type`: object
  - `required`:
    - `epsilon1`: number (kcal/mol)
    - `epsilon2`: number (kcal/mol)
    - `epsilon4`: number (kcal/mol)
    - `scaling_factor`: number
    - `delta_E_half`: number (kcal/mol)
  - `items`: object
  - `required_columns`:
  - `units`: object

### half_monolayer_IT_curve.csv
- path: `/app/outputs/half_monolayer_IT_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: I–T curve, energy, and configurational entropy for the final parameter set at θ=0.5. The checker infers the transition temperature from the inflection point of I1 or I2 vs T.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `T`, `I1`, `I2`, `E_total`, `S`
  - `units`:
    - `T`: K
    - `I1`: dimensionless
    - `I2`: dimensionless
    - `E_total`: kcal/mol
    - `S`: units of k (dimensionless)

### quarter_monolayer_IT_curve.csv
- path: `/app/outputs/quarter_monolayer_IT_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: I–T curve for the final parameter set at θ=0.25. The checker infers the transition temperature from the inflection point of I1 or I2 vs T.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `T`, `I1`, `I2`, `E_total`
  - `units`:
    - `T`: K
    - `I1`: dimensionless
    - `I2`: dimensionless
    - `E_total`: kcal/mol

### heat_capacity_curve.csv
- path: `/app/outputs/heat_capacity_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Heat capacity per adatom at half‑monolayer coverage. The checker verifies that the peak lies near the half‑monolayer transition temperature.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `T`, `Cv`
  - `units`:
    - `T`: K
    - `Cv`: kcal/(mol K)

Notes: The half‑monolayer I‑T curve includes configurational entropy as an auxiliary column; only the transition temperature is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon1": "number (kcal/mol)",
          "epsilon2": "number (kcal/mol)",
          "epsilon4": "number (kcal/mol)",
          "scaling_factor": "number",
          "delta_E_half": "number (kcal/mol)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Final scaled pairwise interaction energies and the half‑monolayer constraint ΔE_½ = 3ε2 − 4ε4."
    },
    {
      "file": "half_monolayer_IT_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "T",
          "I1",
          "I2",
          "E_total",
          "S"
        ],
        "units": {
          "T": "K",
          "I1": "dimensionless",
          "I2": "dimensionless",
          "E_total": "kcal/mol",
          "S": "units of k (dimensionless)"
        }
      },
      "description": "I–T curve, energy, and configurational entropy for the final parameter set at θ=0.5. The checker infers the transition temperature from the inflection point of I1 or I2 vs T."
    },
    {
      "file": "quarter_monolayer_IT_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "T",
          "I1",
          "I2",
          "E_total"
        ],
        "units": {
          "T": "K",
          "I1": "dimensionless",
          "I2": "dimensionless",
          "E_total": "kcal/mol"
        }
      },
      "description": "I–T curve for the final parameter set at θ=0.25. The checker infers the transition temperature from the inflection point of I1 or I2 vs T."
    },
    {
      "file": "heat_capacity_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "T",
          "Cv"
        ],
        "units": {
          "T": "K",
          "Cv": "kcal/(mol K)"
        }
      },
      "description": "Heat capacity per adatom at half‑monolayer coverage. The checker verifies that the peak lies near the half‑monolayer transition temperature."
    }
  ],
  "notes": "The half‑monolayer I‑T curve includes configurational entropy as an auxiliary column; only the transition temperature is scored."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file. For `interaction_energies.json`, the verifier checks the reported ΔE₁/₂ = 3ε₂ − 4ε₄ against a hidden target range. For the I–T curves (`half_monolayer_IT_curve.csv` and `quarter_monolayer_IT_curve.csv`), the verifier extracts the transition temperatures (inflection points of I₁ or I₂ vs. temperature) and compares them to hidden gold values. For `heat_capacity_curve.csv`, the verifier checks that the peak location lies close to the half‑monolayer transition temperature. Each stage carries a weight, and the final reward is a weighted sum of the per-stage scores. Simply hardcoding or guessing the paper’s reported numbers is not sufficient; the simulation must demonstrate the correct physical behavior.