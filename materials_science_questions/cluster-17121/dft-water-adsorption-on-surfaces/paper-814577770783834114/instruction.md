# Water Adsorption on Fe(100) Surface: Density Profile and Vibrational DOS from MD Simulation

## Problem background
The early stages of iron corrosion begin with water adsorption on iron surfaces. Understanding the interfacial structure and vibrational properties of water on Fe(100) is key to interpreting experimental spectra (HREELS) and the initial chemical bonding. This work develops a classical force field to describe the iron–water interaction, parameterized against DFT reference data, and uses molecular dynamics to simulate the Fe(100)–water interface at 133 K. The goal is to produce the water density profile normal to the surface and the layer‑resolved vibrational density‑of‑states (DOS) from the simulation trajectory.

## Approach
A classical force field is constructed: water molecules use the TIP3P model (partial charges, Lennard‑Jones) supplemented with a Morse potential for O–H bond stretching, a harmonic angle potential, and a short‑range repulsive exponential for Fe–H interactions. The Fe–O interaction includes a corrugation term that depends on the lateral position (top/bridge/hollow) and distance from the surface, parameterized to reproduce adsorption energies from DFT. An open‑source MD package (e.g., LAMMPS) implements the simulation: 1073 water molecules are placed above a frozen BCC Fe(100) slab of 1729 iron atoms with 100 surface atoms. After equilibration under NPT at 298 K and 1 atm, the system is cooled and equilibrated at 133 K. A production NPT run at 133 K generates a trajectory with atomic positions and velocities. From this trajectory, you will compute (a) the normalized water‑oxygen density profile along the surface‑normal direction (z), and (b) the vibrational DOS for oxygen and hydrogen atoms restricted to a water layer of thickness 1.80 Å measured from the iron surface, via the velocity autocorrelation function. The resulting spectra are compared against experimental expectations for surface‑induced shifts and new metal–water interaction features.

## Reproduction target
Compute the normalized water density profile along the z‑axis (surface normal) from your MD simulation and save it as a CSV with columns `z` (Å) and `normalized_density` (ρ/ρ₀). Compute the vibrational DOS for oxygen atoms in the first 1.80 Å water layer and save as CSV with columns `wavenumber_cm1` and `intensity`; repeat for hydrogen atoms. The verifier will independently locate and compare the positions and heights of the first two density peaks, and perform peak finding on the DOS spectra to check that expected surface‑specific peaks are present and correctly ordered relative to pure ice.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- TIP3P water model parameters

## Workflow steps

### Step 1: Fe(100)–water interface MD simulation
- Role: process
- Action: Implement the water–water and Fe–water force field as described in the paper using an open‑source MD package (e.g., LAMMPS). Place 1073 H₂O molecules above a frozen BCC Fe(100) slab of 1729 iron atoms (100 surface Fe atoms). Use periodic boundary conditions with a box height large enough to avoid interaction between slabs (≥ 24 Å). Equilibrate under NPT at 298 K and 1 atm, then cool to 133 K and equilibrate further. Run a production NPT simulation at 133 K, saving positions and velocities every 1 fs (for statistical analysis) and also at a coarser interval of 3.9 fs for the velocity autocorrelation calculation.
- Evidence: `/app/outputs/md_simulation.log`

### Step 2: Water density profile analysis
- Role: scored
- Action: From the trajectory, compute the water‑oxygen density profile along the surface‑normal direction (z) and normalize by the bulk density ρ₀ (the density in the center of the simulation box). Identify the positions and relative densities of the first two layered peaks (region I: 0–3.5 Å and region II: 3.5–6.0 Å). Save the entire normalized profile as z (Å) and ρ/ρ₀.
- Output file: `/app/outputs/density_profile.csv`
- Format: csv
- Contract: Columns: z (float, Å), normalized_density (float, unitless ρ/ρ₀)
- Scoring: scored by hidden verifier

### Step 3: Layer‑resolved vibrational DOS (oxygen)
- Role: scored (load-bearing)
- Action: Select water molecules whose oxygen atoms lie within a layer of thickness 1.80 Å measured from the iron surface. Compute the velocity autocorrelation function from the saved velocities (1154 frames at 3.9 fs intervals) and perform a Fourier transform to obtain the vibrational density of states for oxygen atoms. Output spectrum as wavenumber (cm⁻¹) vs. intensity (arbitrary units).
- Output file: `/app/outputs/vibrational_dos_oxygen.csv`
- Format: csv
- Contract: Columns: wavenumber_cm1 (float, cm⁻¹), intensity (float, arbitrary)
- Scoring: scored by hidden verifier

### Step 4: Layer‑resolved vibrational DOS (hydrogen)
- Role: scored (load-bearing)
- Action: From the same layer selection, compute the vibrational density of states for hydrogen atoms using the velocity autocorrelation function and Fourier transform. Output spectrum as wavenumber (cm⁻¹) vs. intensity (arbitrary units).
- Output file: `/app/outputs/vibrational_dos_hydrogen.csv`
- Format: csv
- Contract: Columns: wavenumber_cm1 (float, cm⁻¹), intensity (float, arbitrary)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/density_profile.csv`
- `/app/outputs/vibrational_dos_oxygen.csv`
- `/app/outputs/vibrational_dos_hydrogen.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### density_profile.csv
- path: `/app/outputs/density_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Normalized water density profile along z‑axis (normal to surface). The checker locates the first two peaks in regions 0–3.5 Å and 3.5–6.0 Å and verifies positions and heights.
- schema:
  - `type`: table
  - `required_columns`: `z`, `normalized_density`
  - `units`:
    - `z`: Angstrom
    - `normalized_density`: unitless

### vibrational_dos_oxygen.csv
- path: `/app/outputs/vibrational_dos_oxygen.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Vibrational DOS of oxygen atoms in the 1.80 Å water layer. The checker performs peak finding in low‑frequency (50–1200 cm⁻¹) and high‑frequency (2800–3600 cm⁻¹) ranges and verifies peak positions.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber_cm1`, `intensity`
  - `units`:
    - `wavenumber_cm1`: cm^-1
    - `intensity`: arbitrary

### vibrational_dos_hydrogen.csv
- path: `/app/outputs/vibrational_dos_hydrogen.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Vibrational DOS of hydrogen atoms in the 1.80 Å water layer. The checker performs peak finding and verifies surface‑specific peak positions.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber_cm1`, `intensity`
  - `units`:
    - `wavenumber_cm1`: cm^-1
    - `intensity`: arbitrary

Notes: Reverted the addition of site_occupancy.csv and angular_distribution.csv because no solve blocks could be created for them. The original three scored outputs are retained.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "density_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "normalized_density"
        ],
        "units": {
          "z": "Angstrom",
          "normalized_density": "unitless"
        }
      },
      "description": "Normalized water density profile along z‑axis (normal to surface). The checker locates the first two peaks in regions 0–3.5 Å and 3.5–6.0 Å and verifies positions and heights."
    },
    {
      "file": "vibrational_dos_oxygen.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber_cm1",
          "intensity"
        ],
        "units": {
          "wavenumber_cm1": "cm^-1",
          "intensity": "arbitrary"
        }
      },
      "description": "Vibrational DOS of oxygen atoms in the 1.80 Å water layer. The checker performs peak finding in low‑frequency (50–1200 cm⁻¹) and high‑frequency (2800–3600 cm⁻¹) ranges and verifies peak positions."
    },
    {
      "file": "vibrational_dos_hydrogen.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber_cm1",
          "intensity"
        ],
        "units": {
          "wavenumber_cm1": "cm^-1",
          "intensity": "arbitrary"
        }
      },
      "description": "Vibrational DOS of hydrogen atoms in the 1.80 Å water layer. The checker performs peak finding and verifies surface‑specific peak positions."
    }
  ],
  "notes": "Reverted the addition of site_occupancy.csv and angular_distribution.csv because no solve blocks could be created for them. The original three scored outputs are retained."
}
```

## How you are scored
A hidden verifier reads your three CSV files. For the density profile, it finds the first two peaks in the 0–6.0 Å region and compares their z‑positions and normalized densities to hidden reference targets within tolerances. For the vibrational DOS, the verifier performs peak‑finding in the low‑frequency (50–1200 cm⁻¹) and high‑frequency (2800–3600 cm⁻¹) ranges and compares the set of detected peaks to a reference list of surface‑shifted and new metal–water peaks; the reward is proportional to the fraction of correctly placed peaks and the absence of large spurious intensity above a noise threshold. The final reward is a weighted sum of the scores from these three scored artifacts — producing the correct raw spectra is essential, not merely self‑reporting a summary. The verifier does not require exact reproduction of any particular figure, but a faithful implementation of the force field and protocol.
