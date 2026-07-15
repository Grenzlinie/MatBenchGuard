# MD Study of Ion-Water Cluster Solvation and Phase Transition

## Problem background
Ion-water clusters serve as model systems for understanding solvation and thermodynamic properties across the solid-liquid phase transition. This task investigates the temperature-dependent solvation of a Na⁺ ion in a 20-water cluster using a hybrid computational algorithm. The central quantities to compute are the ion's radial distribution relative to the cluster center of mass and the cluster's average potential energy as a function of temperature, from which the melting behavior and structural solvation motif can be determined.

## Approach
The computational approach combines three stages known as the parallel basin-hopping and tempering (PBHaT) algorithm. First, parallel basin-hopping Monte Carlo on a transformed potential energy surface collects a representative set of low-energy local minima. Second, harmonic superposition weights are used to select temperature-specific starting structures for each replica. Third, parallel-tempering molecular dynamics (PT-MD) is performed on the continuous potential energy surface using a polarizable flexible water model (TTM2-F) and a pairwise polynomial ion-water interaction potential. From the PT-MD trajectories, the average potential energy and the Na⁺ radial distribution are computed. The whole pipeline yields the caloric curve (energy vs temperature) and radial distribution function, which together reveal the cluster's phase change and the ion's solvation preference as a function of temperature.

## Reproduction target
Implement the PBHaT pipeline and apply it to the Na⁺(H₂O)₂₀ cluster across the temperature range 100–450 K. Produce two scored output files:
- caloric_curve.csv: average potential energy (kcal/mol) for each replica temperature.
- ion_radial_distribution.csv: Na⁺ radial density (arbitrary units) binned by distance from the cluster center of mass, for at least the temperatures 150 K and 350 K.
A hidden verifier will assess the presence of a melting transition and the structural change in the ion's radial distribution between low and high temperature.

## Assets

- TTM2-F water model
- Na+–water polynomial coefficients

## Workflow steps

### Step 1: Parallel basin-hopping on Na+(H2O)20
- Role: process
- Action: Run parallel basin-hopping Monte Carlo on the transformed potential energy surface W(X) of Na+(H2O)20 using the TTM2-F water model and the provided Na+–water interaction parameters. Use multiple replicas with geometrically spaced inverse temperatures from 100 K to 450 K, perform replica exchange attempts, and include wormhole moves (ion-solvent swaps, proton shuffling). Run long enough to collect a representative database of low-lying local minimum geometries and energies.
- Evidence: `/app/outputs/num_minima.txt`

### Step 2: Harmonic superposition and seed selection
- Role: process
- Action: For each collected local minimum, compute normal-mode frequencies and vibrational entropies. Evaluate the harmonic superposition partition function Q^H at multiple temperatures spanning 100–450 K. Randomly select one seed structure per replica temperature according to the probability P_n from the harmonic superposition weight.
- Evidence: none

### Step 3: Parallel-tempering molecular dynamics (PT-MD)
- Role: process
- Action: Perform canonical MD on the continuous potential energy surface V(x) with multiple replicas (100–450 K) using Nosé-Hoover thermostats, a 0.2 fs timestep, and temperature swap attempts. Enclose the cluster in a repulsive confining sphere. Start each replica from the seed generated in the previous step. Run enough time steps to equilibrate and collect configuration/energy samples for analysis.
- Evidence: none

### Step 4: Compute caloric curve
- Role: scored (load-bearing)
- Action: From the PT-MD potential energy trajectories, compute the average potential energy (excluding kinetic contribution) for each replica temperature. Write a CSV file caloric_curve.csv with columns: temperature (K), avg_potential_energy (kcal/mol).
- Output file: `/app/outputs/caloric_curve.csv`
- Format: csv
- Contract: A CSV file with header row: temperature (K), avg_potential_energy (kcal/mol). Each subsequent row contains a paired value for one of the sampled temperatures.
- Scoring: scored by hidden verifier

### Step 5: Compute ion radial distribution
- Role: scored (load-bearing)
- Action: From the PT-MD configurations, compute the radial distribution of the Na+ ion with respect to the cluster center of mass at temperatures 150 K and 350 K (at minimum). Bin the distances and write a CSV file ion_radial_distribution.csv with columns: temperature (K), radius (Angstrom), ion_density (arbitrary units).
- Output file: `/app/outputs/ion_radial_distribution.csv`
- Format: csv
- Contract: A CSV file with header row: temperature (K), radius (Angstrom), ion_density (arbitrary units). Each row corresponds to a distance bin for a specific temperature. The file must contain data for at least 150 K and 350 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/caloric_curve.csv`
- `/app/outputs/ion_radial_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### caloric_curve.csv
- path: `/app/outputs/caloric_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The caloric curve (average potential energy vs temperature) for Na+(H2O)20. The hidden checker will verify the presence of a steep energy increase (melting transition) within an expected temperature window.
- schema:
  - `type`: table
  - `required_columns`: `temperature (K)`, `avg_potential_energy (kcal/mol)`
  - `units`:
    - `temperature (K)`: K
    - `avg_potential_energy (kcal/mol)`: kcal/mol

### ion_radial_distribution.csv
- path: `/app/outputs/ion_radial_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ion radial distribution function at low and high temperatures. The checker will verify that the distribution peaks at a larger radius at 150 K and a smaller radius at 350 K, consistent with a transition from surface to interior solvation.
- schema:
  - `type`: table
  - `required_columns`: `temperature (K)`, `radius (Angstrom)`, `ion_density (arbitrary units)`
  - `units`:
    - `temperature (K)`: K
    - `radius (Angstrom)`: Å
    - `ion_density (arbitrary units)`: arbitrary units

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "caloric_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature (K)",
          "avg_potential_energy (kcal/mol)"
        ],
        "units": {
          "temperature (K)": "K",
          "avg_potential_energy (kcal/mol)": "kcal/mol"
        }
      },
      "description": "The caloric curve (average potential energy vs temperature) for Na+(H2O)20. The hidden checker will verify the presence of a steep energy increase (melting transition) within an expected temperature window."
    },
    {
      "file": "ion_radial_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature (K)",
          "radius (Angstrom)",
          "ion_density (arbitrary units)"
        ],
        "units": {
          "temperature (K)": "K",
          "radius (Angstrom)": "Å",
          "ion_density (arbitrary units)": "arbitrary units"
        }
      },
      "description": "Ion radial distribution function at low and high temperatures. The checker will verify that the distribution peaks at a larger radius at 150 K and a smaller radius at 350 K, consistent with a transition from surface to interior solvation."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently inspects the content of caloric_curve.csv and ion_radial_distribution.csv. The verifier checks whether the computed caloric curve exhibits a sharp increase in potential energy indicative of a solid-liquid transition, and whether the ion radial distribution shifts from an outer-peak configuration at low temperature to an inner-peak configuration at high temperature. The two scored artifacts are weighted: the caloric curve and radial distribution both contribute to the final reward (0–1). The verifier does not require matching a specific published table; it uses hidden tolerances derived from the underlying physical expectation. Executing the full PBHaT workflow and producing physically reasonable output is necessary to receive credit.
