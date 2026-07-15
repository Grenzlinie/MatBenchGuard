# NaCl Cluster Formation at Solid-Liquid Interfaces via Molecular Dynamics Simulations

## Problem background
Heterogeneous nucleation of solutes at solid-liquid interfaces is a key process in surface crystallisation and composite particle synthesis. The early stages involve the formation of transient clusters of solute molecules near the crystalline surface, but the influence of surface-induced solvent ordering on cluster behaviour is not well resolved at the molecular level. This task investigates the structure and clustering of a supersaturated aqueous NaCl solution confined between two faces of a crystalline substrate, using classical molecular dynamics simulations to probe how the substrate identity affects ion aggregation and water orientation in the interfacial region.

## Approach
Two distinct surface types — a metallic Pt(100) surface and an ionic NaCl(100) surface — are considered under identical solution conditions. For each surface, a simulation cell is built with crystalline slabs on both sides of a supersaturated NaCl solution (277 water molecules and 38 ion pairs). Interatomic interactions are described by a Lennard‑Jones plus Coulomb potential with publicly available force-field parameters (SPC/E water; ion parameters from Koneshan et al.; Pt parameters from Zhu & Philpott). NVT molecular dynamics trajectories are generated at 298 K using Ewald summation. The resulting trajectories are then analysed to obtain two kinds of observable for each surface: (1) the spatial distribution of NaCl clusters along the surface‑normal direction (clusters defined by an ion–ion distance and lifetime criterion), and (2) the orientational distribution of water dipoles relative to the surface normal. Comparing these distributions between the two surfaces reveals the effect of substrate‑induced water ordering on solute clustering.

## Reproduction target
Produce, from self‑contained MD simulations of the supersaturated NaCl solution confined between Pt(100) and NaCl(100) surfaces, the following data products:

1. Cluster z‑position histograms for each surface – binned counts of NaCl clusters along the axis perpendicular to the slab, showing any preferential accumulation within the first few nanometres from the interface.
2. Water dipole orientation histograms for the interfacial water molecules – the distribution of cos(θ) where θ is the angle between the water dipole moment and the inward surface normal.

Both distributions are to be output for the Pt(100) and NaCl(100) systems, enabling a comparative assessment of how cluster spatial preference and water orientational order respond to the substrate chemistry.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- SPC/E water model parameters
- Ion Lennard-Jones parameters (Na+, Cl-): 10.1021/jp9801422
- Pt Lennard-Jones parameters: 10.1063/1.468331
- Pt crystal lattice constant
- NaCl crystal lattice constant

## Workflow steps

### Step 1: System construction and MD simulation
- Role: process
- Action: Prepare initial simulation boxes: for each surface type (Pt(100) and NaCl(100)), construct a crystalline slab at each side of the box, insert 277 water molecules, 38 Na+ and 38 Cl- ions according to the concentration. Assign force fields (SPC/E, ion LJ, Pt LJ). Run NVT MD at 298 K with Ewald summation, a 0.5 fs timestep, for at least 1 ns of production trajectory.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Cluster z-distribution for Pt(100)
- Role: scored (load-bearing)
- Action: Analyze the Pt(100) trajectory: identify NaCl clusters using a Na+---Cl- distance cutoff of 0.324 nm and a binding lifetime > 37.5 ps. Compute the histogram of cluster center-of-mass positions along the surface normal (z) with bin width 0.1 nm, starting from the surface. Output the distribution as a CSV.
- Output file: `/app/outputs/clusters_z_Pt.csv`
- Format: csv
- Contract: CSV with columns: z_bin_center (nm), count (number of clusters in that bin). Bins: 0.1 nm from the surface outward.
- Scoring: scored by hidden verifier

### Step 3: Cluster z-distribution for NaCl(100)
- Role: scored (load-bearing)
- Action: Analyze the NaCl(100) trajectory: same as step_cluster_pt but for the NaCl(100) system. Output the distribution as a CSV.
- Output file: `/app/outputs/clusters_z_NaCl.csv`
- Format: csv
- Contract: CSV with columns: z_bin_center (nm), count. Bins: 0.1 nm from the surface outward.
- Scoring: scored by hidden verifier

### Step 4: Water dipole orientation distribution for Pt(100)
- Role: scored
- Action: Analyze the Pt(100) trajectory: compute the angle θ between the water molecular dipole vector and the inward surface normal. Build a histogram of cos(θ) with bin width 0.05. Output the distribution as a CSV.
- Output file: `/app/outputs/dipole_orientation_Pt.csv`
- Format: csv
- Contract: CSV with columns: cos_theta_bin_center (unitless, from -1 to +1), count (number of water molecules per bin). Bins: 0.05 width.
- Scoring: scored by hidden verifier

### Step 5: Water dipole orientation distribution for NaCl(100)
- Role: scored
- Action: Analyze the NaCl(100) trajectory: same as step_dipole_pt but for NaCl(100). Output the distribution as a CSV.
- Output file: `/app/outputs/dipole_orientation_NaCl.csv`
- Format: csv
- Contract: CSV with columns: cos_theta_bin_center, count. Bins: 0.05 width.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/clusters_z_Pt.csv`
- `/app/outputs/clusters_z_NaCl.csv`
- `/app/outputs/dipole_orientation_Pt.csv`
- `/app/outputs/dipole_orientation_NaCl.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### clusters_z_Pt.csv
- path: `/app/outputs/clusters_z_Pt.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Histogram of NaCl cluster center-of-mass positions along the surface normal for the Pt(100) system.
- schema:
  - `type`: table
  - `required_columns`: `z_bin_center`, `count`
  - `units`:
    - `z_bin_center`: nm
    - `count`: count

### clusters_z_NaCl.csv
- path: `/app/outputs/clusters_z_NaCl.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Histogram of NaCl cluster center-of-mass positions along the surface normal for the NaCl(100) system.
- schema:
  - `type`: table
  - `required_columns`: `z_bin_center`, `count`
  - `units`:
    - `z_bin_center`: nm
    - `count`: count

### dipole_orientation_Pt.csv
- path: `/app/outputs/dipole_orientation_Pt.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Distribution of water dipole orientation angle (cos theta) near the Pt(100) interface.
- schema:
  - `type`: table
  - `required_columns`: `cos_theta_bin_center`, `count`
  - `units`:
    - `cos_theta_bin_center`: dimensionless
    - `count`: count

### dipole_orientation_NaCl.csv
- path: `/app/outputs/dipole_orientation_NaCl.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Distribution of water dipole orientation angle (cos theta) near the NaCl(100) interface.
- schema:
  - `type`: table
  - `required_columns`: `cos_theta_bin_center`, `count`
  - `units`:
    - `cos_theta_bin_center`: dimensionless
    - `count`: count

Notes: These artifacts are produced from the MD trajectories. The cluster z-distributions and water orientation distributions capture the key differences between Pt(100) and NaCl(100) interfaces, enabling verification of preferential cluster formation and water ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "clusters_z_Pt.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_bin_center",
          "count"
        ],
        "units": {
          "z_bin_center": "nm",
          "count": "count"
        }
      },
      "description": "Histogram of NaCl cluster center-of-mass positions along the surface normal for the Pt(100) system."
    },
    {
      "file": "clusters_z_NaCl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_bin_center",
          "count"
        ],
        "units": {
          "z_bin_center": "nm",
          "count": "count"
        }
      },
      "description": "Histogram of NaCl cluster center-of-mass positions along the surface normal for the NaCl(100) system."
    },
    {
      "file": "dipole_orientation_Pt.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "cos_theta_bin_center",
          "count"
        ],
        "units": {
          "cos_theta_bin_center": "dimensionless",
          "count": "count"
        }
      },
      "description": "Distribution of water dipole orientation angle (cos theta) near the Pt(100) interface."
    },
    {
      "file": "dipole_orientation_NaCl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "cos_theta_bin_center",
          "count"
        ],
        "units": {
          "cos_theta_bin_center": "dimensionless",
          "count": "count"
        }
      },
      "description": "Distribution of water dipole orientation angle (cos theta) near the NaCl(100) interface."
    }
  ],
  "notes": "These artifacts are produced from the MD trajectories. The cluster z-distributions and water orientation distributions capture the key differences between Pt(100) and NaCl(100) interfaces, enabling verification of preferential cluster formation and water ordering."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four scored output files (clusters_z_Pt.csv, clusters_z_NaCl.csv, dipole_orientation_Pt.csv, dipole_orientation_NaCl.csv). For each file the verifier checks that the artifact conforms to the expected schema and then computes metrics that capture the physical trends (e.g. fraction of clusters within a proximity threshold, strength of the dipole orientation peak). The stage scores are combined by weight into a single final reward in [0, 1]. Full credit is earned by faithfully executing the specified workflow; reporting a correct numeric value without the supporting simulation is not sufficient, as the verifier reads the raw histograms and recomputes aggregate statistics from them.
