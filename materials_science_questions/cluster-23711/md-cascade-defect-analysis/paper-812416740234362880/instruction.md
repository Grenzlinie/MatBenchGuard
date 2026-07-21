# Simulating defect cluster evolution under cascade damage using a master equation model

## Problem background
Energetic particle irradiation creates defects in dense collision cascades, where many vacancies and interstitials are produced in close proximity. A significant fraction of these defects recombine or form immobile clusters (small dislocation loops, stacking-fault tetrahedra, or three-dimensional aggregates) before they can migrate long distances. The resulting population of defect clusters acts as sinks for freely-migrating point defects and strongly reduces the number of jumps they execute, thereby influencing radiation-enhanced diffusion, radiation-induced segregation, and the eventual onset of void swelling. 

This task simulates the evolution of such defect cluster populations using a simplified master-equation model. By tracking the size distributions of vacancy and interstitial clusters under cascade-damage conditions, and by coupling them with steady-state concentrations of mobile point defects, we can explore how the cluster landscape develops with dose and temperature. The key open question is under which conditions the freely-migrating defect flux is dominated by interstitials or by vacancies, and how this balance shifts as the temperature increases. The computed cluster size distributions and the derived diffusion coefficients provide a quantitative picture of that transition.

## Approach
The computational model describes the evolution of immobile vacancy and interstitial clusters through a discrete master equation, supplemented by steady-state equations for mobile point defects. The approach treats defect clusters as sinks and sources that exchange single point defects: clusters grow by capturing free defects of the same type and shrink by capturing the opposite type or by thermally evaporating vacancies. The sink strengths are calculated self-consistently in the effective-medium approximation (Brailsford-Bullough approach), and thermal emission rates from clusters depend on the cluster-size-dependent binding energies.

Cascade damage is represented by a single characteristic cascade size. Each cascade injects a prescribed number of free interstitials and vacancies, creates new interstitial clusters of a fixed formation size, and generates a vacancy cluster whose size depends on the local defect population in the molten cascade core. Preexisting clusters inside the molten zone are dissolved and replaced by the newly formed vacancy cluster.

The model parameters are set to those of nickel: formation and migration energies for vacancies and interstitials, attempt frequencies, lattice parameter, and cascade characteristics (e.g., the fractions of defects that recombine, cluster, or escape freely, and the size of the molten zone). All parameter values are given in the workflow steps.

The simulation integrates the coupled rate equations over a displacement dose up to several dpa at a sequence of temperatures, recalculating the steady-state mobile defect concentrations and the corresponding capture/emission rates after each time step. From the resulting defect concentrations, we extract cluster size distributions at specific doses and compute the contributions of vacancies and interstitials to the total diffusion coefficient.

## Reproduction target
Produce two output files that together characterize the defect cluster population and its influence on diffusion:

- **Cluster size distributions** (`cluster_distributions.csv`): the concentrations (atomic fraction) of vacancy and interstitial clusters as a function of cluster size, for doses of 1 dpa and 5 dpa at temperatures 600 K, 650 K, and 660 K. The agent must provide data for both species and for cluster sizes from 2 up to at least 100.

- **Diffusion coefficients** (`diffusion_coefficients.csv`): the total diffusion coefficient, and the separate vacancy and interstitial contributions, at 5 dpa for temperatures 500 K and 660 K. The coefficients are defined as D_v = ν_v c_v a^2, D_i = ν_i c_i a^2, D_total = D_v + D_i, where c_v and c_i are the steady-state free defect concentrations, a = 0.352 nm, and the jump frequencies ν_v and ν_i are the same as those used in the simulation.

The simulation must cover the full dose interval [0, 5] dpa at a displacement rate of 10^{-3} dpa s^{-1} and store enough intermediate data to produce the requested snapshots. The expected qualitative behavior (the direction of the tail of the cluster distributions and the ordering of the diffusion coefficients at the two temperatures) will be evaluated by the hidden verifier against the model's physics, without requiring the agent to state those trends explicitly.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Simulate defect cluster population dynamics
- Role: process
- Action: Implement the discrete master equation (Eq. 2) for vacancy and interstitial clusters coupled with steady-state mobile defect equations (Eq. 1) using effective-medium sink strengths (Brailsford and Bullough) and thermal evaporation rates. Use reference cascade parameters (N0=200, n_i0=10, f_r0=0.77, f_vcl0=0.22, f_icl0=0.19, f_v0=0.01, f_i0=0.04, f_m0=15, n_d=40) and Ni defect parameters (E_vf=1.58 eV, S_vf=1.5k, E_vm=1.30 eV, ν_v0=1.98e15 s^{-1}, E_if=4.08 eV, S_if=1.5k, E_im=0.15 eV, ν_i0=4.23e12 s^{-1}). Set minimum immobile cluster size to 2. Integrate from 0 to 5 dpa at temperatures 500, 600, 650, 660 K with adaptive time steps. After each step solve for mobile defect steady state and update capture rates. Store all cluster concentrations and free defect concentrations at intervals sufficient to extract snapshots at 1 and 5 dpa.
- Evidence: `/app/outputs/simulation_checkpoint.npz`

### Step 2: Export cluster size distributions
- Role: scored (load-bearing)
- Action: From the simulation output, extract concentrations of vacancy and interstitial clusters of every size at doses 1 and 5 dpa for temperatures 600, 650, 660 K. Write them to a CSV file with columns Temperature, Dose, Species, ClusterSize, Concentration.
- Output file: `/app/outputs/cluster_distributions.csv`
- Format: csv
- Contract: CSV with header: Temperature (K), Dose (dpa), Species (interstitial or vacancy), ClusterSize (integer), Concentration (atomic fraction). Units: Temperature in K, Dose in dpa, Concentration dimensionless atomic fraction.
- Scoring: scored by hidden verifier

### Step 3: Compute diffusion coefficients
- Role: scored (load-bearing)
- Action: From the simulation output at 5 dpa for temperatures 500 and 660 K, extract the steady-state free vacancy and interstitial concentrations c_v and c_i. Compute D_v = ν_v c_v a^2, D_i = ν_i c_i a^2, and D_total = D_v + D_i, using lattice parameter a = 0.352 nm and the jump frequencies from the paper. Write results to a CSV file with columns Temperature, Dose, D_total, D_vacancy, D_interstitial.
- Output file: `/app/outputs/diffusion_coefficients.csv`
- Format: csv
- Contract: CSV with header: Temperature (K), Dose (dpa), D_total (m^2/s), D_vacancy (m^2/s), D_interstitial (m^2/s). Rows for (500,5) and (660,5).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cluster_distributions.csv`
- `/app/outputs/diffusion_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_distributions.csv
- path: `/app/outputs/cluster_distributions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Cluster size distribution at 1 and 5 dpa for temperatures 600, 650, 660 K. Scored on structural features such as peak position and the relative extent of tail toward larger sizes for interstitials vs vacancies at different temperatures.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Dose`, `Species`, `ClusterSize`, `Concentration`
  - `units`:
    - `Temperature`: K
    - `Dose`: dpa
    - `Species`: categories: interstitial, vacancy
    - `ClusterSize`: number of defects (integer)
    - `Concentration`: atomic fraction

### diffusion_coefficients.csv
- path: `/app/outputs/diffusion_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total, vacancy, and interstitial diffusion coefficients at 5 dpa for temperatures 500 and 660 K. The checker verifies the temperature-dependent ordering of vacancy and interstitial diffusion, and that magnitudes are physically plausible.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Dose`, `D_total`, `D_vacancy`, `D_interstitial`
  - `units`:
    - `Temperature`: K
    - `Dose`: dpa
    - `D_total`: m^2/s
    - `D_vacancy`: m^2/s
    - `D_interstitial`: m^2/s

Notes: All parameters are taken from the paper's Tables 1 and 2. The simulation is the heavy part; the agent must implement the full model including the Brailsford-Bullough effective medium sink calculation. The scored outputs are derived from the simulation; no external datasets are used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_distributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Dose",
          "Species",
          "ClusterSize",
          "Concentration"
        ],
        "units": {
          "Temperature": "K",
          "Dose": "dpa",
          "Species": "categories: interstitial, vacancy",
          "ClusterSize": "number of defects (integer)",
          "Concentration": "atomic fraction"
        }
      },
      "description": "Cluster size distribution at 1 and 5 dpa for temperatures 600, 650, 660 K. Scored on structural features such as peak position and the relative extent of tail toward larger sizes for interstitials vs vacancies at different temperatures."
    },
    {
      "file": "diffusion_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Dose",
          "D_total",
          "D_vacancy",
          "D_interstitial"
        ],
        "units": {
          "Temperature": "K",
          "Dose": "dpa",
          "D_total": "m^2/s",
          "D_vacancy": "m^2/s",
          "D_interstitial": "m^2/s"
        }
      },
      "description": "Total, vacancy, and interstitial diffusion coefficients at 5 dpa for temperatures 500 and 660 K. The checker verifies the temperature-dependent ordering of vacancy and interstitial diffusion, and that magnitudes are physically plausible."
    }
  ],
  "notes": "All parameters are taken from the paper's Tables 1 and 2. The simulation is the heavy part; the agent must implement the full model including the Brailsford-Bullough effective medium sink calculation. The scored outputs are derived from the simulation; no external datasets are used."
}
```

## How you are scored
A hidden verifier, which you will not see, independently checks each scored artifact you produce.

- `cluster_distributions.csv` is evaluated by a **structural audit** that examines properties such as the peak position of the distributions and the relative extent of the tails toward larger sizes for interstitials versus vacancies at different temperatures. The audit does not compare your numbers against a single expected value; instead, it verifies that the distributions exhibit the physically expected shape relations that follow from the model.

- `diffusion_coefficients.csv` is evaluated by a **reference match** that compares the ordering of D_i and D_v at each temperature and assesses whether the magnitudes lie within a physically plausible range (derived from the paper's model). Meeting the correct qualitative ordering and plausible magnitude earns full credit; a wrong ordering or implausible values result in partial or zero credit.

The final reward is a weighted combination of these two checks. The weight distribution reflects the central importance of the cluster distributions and the temperature-dependent diffusion trend, with the cluster distributions carrying a substantial share. You do not need to report any single metric; your task is to produce the two CSV files following the specified schemas. The verifier handles all comparisons silently.
