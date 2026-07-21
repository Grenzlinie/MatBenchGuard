# Interface-Enhanced Crystal Nucleation in Immiscible Polymer Blends via Lattice Monte Carlo

## Problem background
In polymer blends, liquid-liquid phase separation (LLPS) creates diffuse interfaces between immiscible components, while crystallization is another basic phase transition. The interplay of these two processes can strongly influence the resulting morphology. A central open question is whether crystal nucleation is intrinsically enhanced at the diffuse interface of immiscible polymers, and if so, whether the enhancement arises from enthalpic or entropic contributions. Resolving this question is important for understanding and controlling the structure-property relationships in semicrystalline polymer blends.

## Approach
This task uses dynamic Monte Carlo (MC) simulations of a binary polymer blend on a cubic lattice, combined with a Flory-Huggins-based mean-field lattice theory, to investigate crystal nucleation near flat interfaces. The blend consists of equal numbers of short chains of a crystallizable (C) and a non-crystallizable (NC) component. The MC method employs Metropolis sampling with energy terms for collinear bond packing (Ec), parallel alignment of bonds (Ep), and demixing interactions (B). The workflow first produces a flat interface by running LLPS under strong demixing conditions, then samples thermal fluctuations at the same temperature to identify the largest crystalline clusters (clusters of parallel C bonds) over many observations for different demixing strengths (B/Ec values). From these ensembles, three quantities are computed: the spatial distribution of cluster center-of-mass positions normal to the interface, the distribution of cluster sizes, and the orientational order parameter P of clusters inside the interfacial zone. Separately, the mean-field partition function for a homogeneous blend is used to derive the chemical-potential equilibrium condition and compute the equilibrium melting temperature of 16-mer crystals as a function of C volume fraction for the same B/Ec set.

## Reproduction target
Implement the lattice MC simulation and the mean-field calculation to produce four quantitative relationships:
(i) The spatial distribution of the Z‑coordinate (distance from the interface) of the center of mass of the largest crystalline clusters, recorded separately for each B/Ec.
(ii) The size distribution (number of parallel bonds) of the same largest clusters, also per B/Ec.
(iii) The orientational-order parameter P = (3⟨cos²θ⟩−1)/2 for the largest clusters located within the defined interfacial zone, as a function of B/Ec.
(iv) The equilibrium melting temperature of 16‑mer crystals in a homogeneous blend as a function of the volume fraction of component C, computed from the mean-field theory for different B/Ec values.

## Assets
No external datasets, models, or pre-trained weights are required. The entire computational workflow is implemented from the method description using standard scientific Python libraries (NumPy, etc.).

## Workflow steps

### Step 1: Prepare initial homogeneous melt configuration
- Role: process
- Action: Set up a 64^3 cubic lattice with 15360 chains of length 16 (half crystallizable C, half noncrystallizable NC). Perform athermal microrelaxation to obtain an equilibrated amorphous starting configuration.
- Evidence: `/app/outputs/initial_melt_state.pkl`

### Step 2: Produce flat interface via liquid-liquid phase separation
- Role: process
- Action: Run Metropolis Monte Carlo simulation on the initial melt at reduced temperature 4.0 kT/Ec with B/Ec=0.5 for 200,000 MC cycles to achieve complete phase separation and a well-defined flat interface separating C-rich and NC-rich domains.
- Evidence: `/app/outputs/flat_interface_state.pkl`

### Step 3: Sample thermal fluctuation clusters
- Role: process
- Action: For each B/Ec value in [0, 0.1, 0.3, 0.5] (or a similar set covering the key regime), starting from the flat-interface configuration and using the same temperature 4.0 kT/Ec, run additional MC cycles. Every 20 MC cycles identify the largest crystalline cluster (cluster of C bonds with the maximum number of parallel neighbors) and record its center-of-mass Z-coordinate, size (number of parallel bonds), and chain-axis orientation relative to the interface normal. Collect 10,000 observations per B/Ec. Calibrate the C‑phase centre position to account for phase-boundary drift. Save the raw ensemble as a structured file.
- Evidence: `/app/outputs/raw_cluster_log.json`

### Step 4: Spatial distribution of largest cluster centers
- Role: scored (load-bearing)
- Action: From raw_cluster_log.json, compute for each B/Ec the histogram of the Z-coordinate of the center of mass of the largest crystalline clusters, aggregated over all observations. Output the distribution as a CSV table.
- Output file: `/app/outputs/spatial_distribution.csv`
- Format: csv
- Contract: table with columns: B_ratio (float, B/Ec), distance (int, Z-coordinate in lattice units), count (int, number of observations with that Z-coordinate)
- Scoring: scored by hidden verifier

### Step 5: Size distribution of largest clusters
- Role: scored (load-bearing)
- Action: From raw_cluster_log.json, compute for each B/Ec the histogram of the size (number of parallel bonds) of the largest crystalline clusters. Output the size distribution as a CSV table.
- Output file: `/app/outputs/size_distribution.csv`
- Format: csv
- Contract: table with columns: B_ratio (float, B/Ec), size (int, number of bonds), count (int, number of observations with that size)
- Scoring: scored by hidden verifier

### Step 6: Orientational-order parameter near the interface
- Role: scored
- Action: Using raw_cluster_log.json and the composition profile derived from the flat-interface simulation, define the interfacial zone. For each B/Ec, compute the orientational order parameter P = (3⟨cos²θ⟩-1)/2 for the largest clusters located within that zone, where θ is the angle between the chain axis and the interface normal. Output one P value per B/Ec as a CSV table.
- Output file: `/app/outputs/order_parameters.csv`
- Format: csv
- Contract: table with columns: B_ratio (float, B/Ec), order_parameter (float, P value as defined)
- Scoring: scored by hidden verifier

### Step 7: Mean-field melting temperature vs composition
- Role: scored
- Action: From the Flory-Huggins-based mean-field lattice theory described in the paper (partition function and chemical potential equilibrium condition), derive and compute the equilibrium melting temperature of 16‑mer polymer crystals as a function of the volume fraction of the crystallizable component C, for the same set of B/Ec values used in the simulation. Use Ep/Ec=1. Output a CSV curve covering volume fractions from 0.1 to 1.0 in steps of 0.1 for each B/Ec.
- Output file: `/app/outputs/melting_curve.csv`
- Format: csv
- Contract: table with columns: B_ratio (float, B/Ec), volume_fraction_C (float), melting_temperature (float, in reduced units kT/Ec)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spatial_distribution.csv`
- `/app/outputs/size_distribution.csv`
- `/app/outputs/order_parameters.csv`
- `/app/outputs/melting_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spatial_distribution.csv
- path: `/app/outputs/spatial_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Histogram of Z-coordinate (distance from interface) of the center of mass of the largest crystalline clusters for each B/Ec. The checker verifies structural consistency against reference patterns.
- schema:
  - `type`: table
  - `required_columns`: `B_ratio`, `distance`, `count`
  - `units`:
    - `B_ratio`: dimensionless
    - `distance`: lattice unit
    - `count`: integer

### size_distribution.csv
- path: `/app/outputs/size_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Histogram of the size (number of parallel bonds) of the largest crystalline clusters for each B/Ec. The checker verifies structural consistency against reference patterns.
- schema:
  - `type`: table
  - `required_columns`: `B_ratio`, `size`, `count`
  - `units`:
    - `B_ratio`: dimensionless
    - `size`: number of parallel bonds
    - `count`: integer

### order_parameters.csv
- path: `/app/outputs/order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Orientational order parameter P for the largest crystalline clusters in the interfacial zone vs B/Ec. The checker verifies structural consistency against reference patterns.
- schema:
  - `type`: table
  - `required_columns`: `B_ratio`, `order_parameter`
  - `units`:
    - `B_ratio`: dimensionless
    - `order_parameter`: dimensionless, range [-0.5, 1]

### melting_curve.csv
- path: `/app/outputs/melting_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Equilibrium melting temperature of 16-mer crystals vs volume fraction of component C for different B/Ec. The checker verifies structural consistency against reference patterns.
- schema:
  - `type`: table
  - `required_columns`: `B_ratio`, `volume_fraction_C`, `melting_temperature`
  - `units`:
    - `B_ratio`: dimensionless
    - `volume_fraction_C`: volume fraction between 0 and 1
    - `melting_temperature`: reduced temperature kT/Ec

Notes: All scored outputs are verified via structural audit against hidden reference criteria derived from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spatial_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_ratio",
          "distance",
          "count"
        ],
        "units": {
          "B_ratio": "dimensionless",
          "distance": "lattice unit",
          "count": "integer"
        }
      },
      "description": "Histogram of Z-coordinate (distance from interface) of the center of mass of the largest crystalline clusters for each B/Ec. The checker verifies structural consistency against reference patterns."
    },
    {
      "file": "size_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_ratio",
          "size",
          "count"
        ],
        "units": {
          "B_ratio": "dimensionless",
          "size": "number of parallel bonds",
          "count": "integer"
        }
      },
      "description": "Histogram of the size (number of parallel bonds) of the largest crystalline clusters for each B/Ec. The checker verifies structural consistency against reference patterns."
    },
    {
      "file": "order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_ratio",
          "order_parameter"
        ],
        "units": {
          "B_ratio": "dimensionless",
          "order_parameter": "dimensionless, range [-0.5, 1]"
        }
      },
      "description": "Orientational order parameter P for the largest crystalline clusters in the interfacial zone vs B/Ec. The checker verifies structural consistency against reference patterns."
    },
    {
      "file": "melting_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_ratio",
          "volume_fraction_C",
          "melting_temperature"
        ],
        "units": {
          "B_ratio": "dimensionless",
          "volume_fraction_C": "volume fraction between 0 and 1",
          "melting_temperature": "reduced temperature kT/Ec"
        }
      },
      "description": "Equilibrium melting temperature of 16-mer crystals vs volume fraction of component C for different B/Ec. The checker verifies structural consistency against reference patterns."
    }
  ],
  "notes": "All scored outputs are verified via structural audit against hidden reference criteria derived from the paper."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently inspects each of the four output files listed under Output files. The verifier checks structural and statistical consistency against reference criteria derived from the original study. Each artifact contributes a portion of the total reward, and the final score is the weighted sum of these per‑artifact scores. Reporting numbers alone without performing the required simulation and analysis will not suffice—the verifier checks for internal consistency that can only be obtained through faithful execution of the described workflow.
