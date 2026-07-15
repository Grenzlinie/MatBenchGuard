# Reproduce amorphous structure of grain boundaries in nanocrystalline silicon via molecular dynamics

## Problem background
Nanocrystalline silicon exhibits grain-size-dependent properties, yet the atomic-scale structure of the grain boundaries (GBs) and grain junctions remains an open question. In particular, it is unknown whether these interfaces are ordered or whether they resemble a disordered, amorphous phase. Molecular-dynamics (MD) simulations using the Stillinger-Weber potential can synthesize fully dense nanocrystalline Si and enable direct characterization of the local atomic structure. This task aims to determine the structural nature of GBs and grain junctions in a model nanocrystalline microstructure by computing local radial distribution functions, bond-angle distributions, and plane-by-plane energy profiles, and comparing them to the corresponding bulk amorphous silicon reference.

## Approach
The workflow follows a two-step synthetic approach. First, a nanocrystalline Si microstructure is grown by crystallizing from the melt: four randomly oriented diamond-cubic seed grains are placed on an f.c.c. lattice inside a periodic simulation cell, the remaining atoms are melted, and the system is cooled under zero external pressure, allowing the seeds to grow and impinge while forming grain boundaries and grain junctions. All MD is performed with the Stillinger-Weber three-body potential. Second, the final zero-temperature configuration is analyzed locally. For a representative grain-boundary region, the radial distribution function G(r) and the bond-angle distribution P(cos θ) of nearest-neighbor vectors are computed and compared to the same distributions for bulk amorphous silicon. Additionally, the plane-by-plane average energy per atom is profiled across a GB in a cylindrical region that avoids triple lines and junctions, providing a measure of the energetic width and excess energy of the boundary. Together, these three analyses provide a structural and energetic fingerprint that distinguishes crystalline order from amorphous disorder.

## Reproduction target
Using molecular dynamics with the Stillinger-Weber potential for silicon: (1) Synthesize a fully dense nanocrystalline Si microstructure with an intermediate grain size (~5.4 nm) consisting of four grains arranged on an f.c.c. lattice. (2) From the final zero-temperature atomic configuration, compute the local radial distribution function for atoms within 0.5 a₀ of a grain-boundary plane, the bond-angle distribution of nearest-neighbor vectors (cutoff 0.570 a₀) for the same atoms, and the plane-by-plane energy profile across a representative GB in a cylindrical region of radius 2 a₀. (3) The resulting structural distributions should allow a comparison with bulk amorphous silicon to determine whether the GB region is disordered and resembles the amorphous phase.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- Stillinger-Weber potential parameters for Si (Si.sw): https://github.com/lammps/lammps/blob/develop/potentials/Si.sw

## Workflow steps

### Step 1: Generate initial nanocrystalline Si configuration (intermediate size)
- Role: process
- Action: Create a 3-D periodic cubic simulation cell of length 14 a0 (a0=0.543 nm) containing four diamond-cubic seed grains arranged on an f.c.c. lattice. Each seed comprises 15% of the atoms; the remaining atoms are melted at 3000 K while keeping the seeds fixed. The seeds are randomly rotated. Output a LAMMPS data file of the starting state.
- Evidence: `/app/outputs/start.lammpsdata`

### Step 2: MD synthesis of the nanocrystalline Si microstructure
- Role: process
- Action: Run LAMMPS with the Stillinger–Weber potential using the protocol: melt the non‑seed atoms at 3000 K, rotate seeds, cool to 1250 K under zero external pressure (NPT), allow crystal growth for 150000–300000 steps, then cool stepwise to 0 K. Output the final atomic configuration.
- Evidence: `/app/outputs/final_structure.dump`

### Step 3: Local radial distribution function for the grain‑boundary region
- Role: scored (load-bearing)
- Action: From the final 0 K structure, identify a representative grain boundary plane. Select atoms within 0.5 a0 of that plane and compute the radial distribution function G(r). Write the result to /app/outputs/local_rdf.txt.
- Output file: `/app/outputs/local_rdf.txt`
- Format: txt
- Contract: Two columns separated by whitespace: column 1 = r (Angstrom), column 2 = G(r) (dimensionless). At least 200 points covering r = 0 to 10 Å.
- Scoring: scored by hidden verifier

### Step 4: Bond‑angle distribution function for the grain‑boundary region
- Role: scored
- Action: For the same set of GB‑region atoms, construct the angular distribution function P(cos θ) using only nearest‑neighbor vectors (distance ≤ 0.570 a0). Write to /app/outputs/angular_distribution.txt.
- Output file: `/app/outputs/angular_distribution.txt`
- Format: txt
- Contract: Two columns: column 1 = cos(θ) (range −1 to 1), column 2 = P(cos θ) (normalized probability density). At least 100 bins.
- Scoring: scored by hidden verifier

### Step 5: Plane‑by‑plane energy profile across a representative grain boundary
- Role: scored
- Action: Select a cylindrical region of radius 2 a0 that traverses a GB (avoiding triple lines and junctions). Compute the average energy per atom in slices of thickness 0.25 a0 perpendicular to the boundary plane, with the origin at the GB center. Write to /app/outputs/gb_energy_profile.txt.
- Output file: `/app/outputs/gb_energy_profile.txt`
- Format: txt
- Contract: Two columns: column 1 = distance across GB (in units of a0, zero at GB center), column 2 = average energy per atom (eV). Profile sampled every 0.25 a0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/local_rdf.txt`
- `/app/outputs/angular_distribution.txt`
- `/app/outputs/gb_energy_profile.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### local_rdf.txt
- path: `/app/outputs/local_rdf.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Local radial distribution function for atoms within 0.5 a0 of a grain‑boundary plane.
- schema:
  - `type`: table
  - `required_columns`: `r (Angstrom)`, `G(r) (dimensionless)`
  - `units`:
    - `r (Angstrom)`: Angstrom
    - `G(r) (dimensionless)`: dimensionless

### angular_distribution.txt
- path: `/app/outputs/angular_distribution.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Bond‑angle distribution of nearest‑neighbor vectors for atoms in the grain‑boundary region.
- schema:
  - `type`: table
  - `required_columns`: `cos(theta)`, `P(cos theta)`
  - `units`:
    - `cos(theta)`: dimensionless
    - `P(cos theta)`: normalized probability density

### gb_energy_profile.txt
- path: `/app/outputs/gb_energy_profile.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Plane‑by‑plane average energy per atom across a representative grain boundary, sampled in cylindrical slices.
- schema:
  - `type`: table
  - `required_columns`: `distance (a0)`, `energy per atom (eV)`
  - `units`:
    - `distance (a0)`: units of a0
    - `energy per atom (eV)`: eV

Notes: The agent must synthesize a nanocrystalline Si sample of ~5.4 nm grain size using the Stillinger-Weber potential. The three scored artifacts are computed from the final zero-temperature structure. The checker will extract structural features (peak positions, widths, energy excess) and compare against hidden reference profiles derived from the paper's results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "local_rdf.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r (Angstrom)",
          "G(r) (dimensionless)"
        ],
        "units": {
          "r (Angstrom)": "Angstrom",
          "G(r) (dimensionless)": "dimensionless"
        }
      },
      "description": "Local radial distribution function for atoms within 0.5 a0 of a grain‑boundary plane."
    },
    {
      "file": "angular_distribution.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cos(theta)",
          "P(cos theta)"
        ],
        "units": {
          "cos(theta)": "dimensionless",
          "P(cos theta)": "normalized probability density"
        }
      },
      "description": "Bond‑angle distribution of nearest‑neighbor vectors for atoms in the grain‑boundary region."
    },
    {
      "file": "gb_energy_profile.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance (a0)",
          "energy per atom (eV)"
        ],
        "units": {
          "distance (a0)": "units of a0",
          "energy per atom (eV)": "eV"
        }
      },
      "description": "Plane‑by‑plane average energy per atom across a representative grain boundary, sampled in cylindrical slices."
    }
  ],
  "notes": "The agent must synthesize a nanocrystalline Si sample of ~5.4 nm grain size using the Stillinger-Weber potential. The three scored artifacts are computed from the final zero-temperature structure. The checker will extract structural features (peak positions, widths, energy excess) and compare against hidden reference profiles derived from the paper's results."
}
```

## How you are scored
Your submission is evaluated by a hidden, deterministic checker that independently reads the three scored output files (`local_rdf.txt`, `angular_distribution.txt`, `gb_energy_profile.txt`). For each artifact the checker extracts key structural features (peak positions, widths, excess energy, etc.) and compares them against hidden reference profiles derived from the published study. Scoring uses tolerance-based similarity: meeting or exceeding the required structural match earns full credit for that stage. Each scored stage carries a pre‑determined weight, and the final reward (a float between 0 and 1) is the weighted sum of the stage scores. Important: simply reporting numbers from the literature is not sufficient; the checker verifies that your computed distributions possess the expected amorphous‑like characteristics.
