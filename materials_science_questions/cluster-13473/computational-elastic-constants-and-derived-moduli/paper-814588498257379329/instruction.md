# Deformation and Elastic Response of a Magnetic Nanoparticle Cross-Linked Gel

## Problem background
Ferrogels are composite materials in which magnetic nanoparticles are embedded in a swollen polymer network. Their shape and mechanical properties can be controlled by external magnetic fields, making them candidates for actuation and smart materials. This work focuses on a ferrogel where the magnetic nanoparticles act as covalent cross‑linkers of the polymer network. Due to the direct coupling between the orientation of the magnetic moments and the attached polymer chains, applying a homogeneous external field causes the nanoparticles to rotate and wrap the chains around them, exerting stress on the network. In three dimensions the deformation is anisotropic: the gel shrinks more strongly parallel to the field, while the perpendicular response depends on the network topology. The resulting shape change, elastic moduli, and magnetic response are sensitive to the connectivity of the network nodes. This task quantifies these effects for two different network topologies — diamond cubic (four‑fold connectivity) and simple cubic (six‑fold connectivity) — and provides the data needed to understand the interplay between field‑induced stress and network elasticity.

## Approach
The system is studied using coarse‑grained molecular dynamics simulations with ESPResSo. The gel model consists of magnetic node particles placed on either a diamond cubic (DC) or simple cubic (SC) lattice, connected by polymer chains of 60 beads via virtual sites that enforce the covalent bonds. Interactions are described by harmonic bonds between neighbouring beads, a truncated Lennard‑Jones (WCA) repulsion between all particles, and a Langevin thermostat to maintain a temperature of kBT = 1. Only the external field–dipole interaction is included; dipole‑dipole interactions are neglected.

First, the field‑free equilibrium swelling length l0 is determined by running NVT simulations at different isotropic box sizes, computing the isotropic pressure from the diagonal stress tensor, and interpolating to zero stress. Next, for each target field strength (Langevin parameter α) an iterative stress‑matching loop is executed: the box lengths parallel and perpendicular to the field are adjusted until the residual stress components fall below a small threshold, yielding the equilibrium shape l∥ and l⊥ and the relative volume shrinkage. The elastic constants are obtained by applying small strains around the equilibrium shape and fitting a linear stress–strain model that respects the tetragonal symmetry imposed by a field parallel to one Cartesian axis. Finally, the magnetization parallel to the field is measured at the field‑free equilibrium volume for a range of α values.

## Reproduction target
Produce the following output files according to the schemas defined in the output contract:

1. `/app/outputs/equilibrium_swelling.csv` – the equilibrium swelling length *l*₀ for the diamond cubic and simple cubic topologies with chain length 60.
2. `/app/outputs/deformation_data.csv` – for each topology and each α in {0, 10, 20, 30, 40, 50, 60}, the equilibrium box lengths parallel (*l*∥) and perpendicular (*l*⊥) to the field, and the relative volume shrinkage.
3. `/app/outputs/elastic_constants.csv` – for each topology and for the field‑free (α=0) and α=20 cases, the five independent elastic constant matrix elements *a*, *b*, *c*, *d*, *e*.
4. `/app/outputs/magnetization_curve.csv` – for each topology and each α in {0, 10, 20, 30, 40, 50, 60}, the average magnetization component parallel to the field.

All simulations must be performed with the parameters given in the workflow steps; the required iterative procedures and averaging protocols are described there.

## Assets

- ESPResSo simulation package: https://espressomd.org/

## Workflow steps

### Step 1: System preparation and equilibration
- Role: process
- Action: Set up and equilibrate the coarse-grained gel model for both topologies (diamond cubic and simple cubic) with chain length 60 beads, using the model parameters: magnetic node particles (diameter σ_n=10) placed on the respective lattice, polymer chains (60 beads, σ_c=1) attached via virtual sites, harmonic bonds (k=10, r0=2^(1/6)), WCA repulsion (ε=10), and Langevin thermostat (k_B T=1). Randomize dipole moments, apply periodic boundary conditions, reshape from the initially stretched configuration to the desired volume, and relax.
- Evidence: none

### Step 2: Equilibrium swelling determination
- Role: scored
- Action: For each topology, determine the equilibrium swelling length l0 in the field-free case. Run multiple NVT simulations at different box volumes around the initially stretched volume, compute the isotropic pressure from the diagonal stress tensor, and interpolate to zero stress to obtain l0. Write the equilibrium values to equilibrium_swelling.csv.
- Output file: `/app/outputs/equilibrium_swelling.csv`
- Format: csv
- Contract: CSV with columns: topology (string, 'DC' or 'SC'), chain_length (int, 60), l0 (float). One row per topology.
- Scoring: scored by hidden verifier

### Step 3: Anisotropic deformation under magnetic field
- Role: scored (load-bearing)
- Action: For each topology and for each Langevin parameter α = 0, 10, 20, 30, 40, 50, 60, perform the iterative stress-matching procedure to find the equilibrium shape l_∥ (parallel) and l_⊥ (perpendicular) under an applied magnetic field. At each iteration, simulate with the current box lengths, average stress components over 24 independent simulations (randomized dipole orientations), and adjust box lengths using linear extrapolation from the two shapes with lowest absolute stress, limiting the change to ~2% per iteration. Terminate when both |σ_∥| and |σ_⊥| < 1e-5. Compute the relative volume shrinkage δV/V0 = 1 - (l_∥ l_⊥^2) / l0^3. Write the final l_∥, l_⊥, and volume shrinkage for each α to deformation_data.csv.
- Output file: `/app/outputs/deformation_data.csv`
- Format: csv
- Contract: CSV with columns: topology (string, 'DC' or 'SC'), alpha (float), l_parallel (float), l_perpendicular (float), volume_shrinkage (float). One row per field strength per topology.
- Scoring: scored by hidden verifier

### Step 4: Elastic constants
- Role: scored
- Action: For each topology and for both field conditions: field-free (α=0) and α=20, compute the elastic constant matrix elements a, b, c, d, e as defined in the paper's linear elasticity model for a tetragonal symmetry (field parallel to x). Apply small strains (Δε ~ 0.01) around the respective equilibrium shapes in each Cartesian direction, simulate, measure the stress tensor, and fit a linear stress-strain model to extract the constants. Write the results to elastic_constants.csv.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: CSV with columns: topology (string, 'DC' or 'SC'), field_condition (string, 'alpha_0' or 'alpha_20'), a (float), b (float), c (float), d (float), e (float). One row per topology per condition.
- Scoring: scored by hidden verifier

### Step 5: Magnetization curve
- Role: scored
- Action: For each topology, run simulations at the field‑free equilibrium swelling volume (shape from step 2) for each α = 0, 10, 20, 30, 40, 50, 60, keeping the box fixed. For each α, compute the average magnetization parallel to the external field (component of total dipole moment along the field). Write the results to magnetization_curve.csv.
- Output file: `/app/outputs/magnetization_curve.csv`
- Format: csv
- Contract: CSV with columns: topology (string, 'DC' or 'SC'), alpha (float), M (float). One row per field strength per topology.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_swelling.csv`
- `/app/outputs/deformation_data.csv`
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/magnetization_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_swelling.csv
- path: `/app/outputs/equilibrium_swelling.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Field-free equilibrium swelling length l0 for diamond cubic and simple cubic topologies with chain length 60.
- schema:
  - `type`: table
  - `required_columns`: `topology`, `chain_length`, `l0`
  - `units`:
    - `l0`: simulation length unit

### deformation_data.csv
- path: `/app/outputs/deformation_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium shape lengths parallel and perpendicular to the magnetic field and relative volume shrinkage for α=0..60 for both topologies.
- schema:
  - `type`: table
  - `required_columns`: `topology`, `alpha`, `l_parallel`, `l_perpendicular`, `volume_shrinkage`
  - `units`:
    - `l_parallel`: simulation length unit
    - `l_perpendicular`: simulation length unit
    - `volume_shrinkage`: dimensionless

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constant matrix elements a-e for the field-free case (α=0) and for α=20, for both diamond cubic and simple cubic geometries.
- schema:
  - `type`: table
  - `required_columns`: `topology`, `field_condition`, `a`, `b`, `c`, `d`, `e`
  - `units`:
    - `a`: simulation stress units
    - `b`: simulation stress units
    - `c`: simulation stress units
    - `d`: simulation stress units
    - `e`: simulation stress units

### magnetization_curve.csv
- path: `/app/outputs/magnetization_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization component parallel to the external field as a function of α for both topologies, measured at the field‑free equilibrium volume.
- schema:
  - `type`: table
  - `required_columns`: `topology`, `alpha`, `M`
  - `units`:
    - `M`: simulation magnetic moment units

Notes: All values are reported in the simulation units defined by the model (mass, length, energy, and charge scales implicit in the coarse-grained parameters). The hidden checker compares against reference values (paper-reported data) with tolerances appropriate for re‑run variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_swelling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "topology",
          "chain_length",
          "l0"
        ],
        "units": {
          "l0": "simulation length unit"
        }
      },
      "description": "Field-free equilibrium swelling length l0 for diamond cubic and simple cubic topologies with chain length 60."
    },
    {
      "file": "deformation_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "topology",
          "alpha",
          "l_parallel",
          "l_perpendicular",
          "volume_shrinkage"
        ],
        "units": {
          "l_parallel": "simulation length unit",
          "l_perpendicular": "simulation length unit",
          "volume_shrinkage": "dimensionless"
        }
      },
      "description": "Equilibrium shape lengths parallel and perpendicular to the magnetic field and relative volume shrinkage for α=0..60 for both topologies."
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "topology",
          "field_condition",
          "a",
          "b",
          "c",
          "d",
          "e"
        ],
        "units": {
          "a": "simulation stress units",
          "b": "simulation stress units",
          "c": "simulation stress units",
          "d": "simulation stress units",
          "e": "simulation stress units"
        }
      },
      "description": "Elastic constant matrix elements a-e for the field-free case (α=0) and for α=20, for both diamond cubic and simple cubic geometries."
    },
    {
      "file": "magnetization_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "topology",
          "alpha",
          "M"
        ],
        "units": {
          "M": "simulation magnetic moment units"
        }
      },
      "description": "Magnetization component parallel to the external field as a function of α for both topologies, measured at the field‑free equilibrium volume."
    }
  ],
  "notes": "All values are reported in the simulation units defined by the model (mass, length, energy, and charge scales implicit in the coarse-grained parameters). The hidden checker compares against reference values (paper-reported data) with tolerances appropriate for re‑run variability."
}
```

## How you are scored
A hidden verifier reads the CSV files you write and scores each artifact independently. For every output the verifier checks format compliance and compares the reported numeric quantities against reference results that correspond to a correct execution of the described workflow. The per‑artifact scores are combined by weight to produce the final reward. The verifier may additionally enforce physically required constraints (e.g., monotonic trends or sign relationships) to validate the consistency of the reported data. Self‑reporting numbers that coincide with the reference values is not sufficient; the artifacts must reflect a genuine reproduction of the prescribed procedures. The exact tolerances and reference values are hidden and are chosen to accommodate legitimate implementation differences while excluding trivial guesses.
