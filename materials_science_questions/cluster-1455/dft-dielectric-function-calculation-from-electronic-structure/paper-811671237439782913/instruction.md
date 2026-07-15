# Surface dielectric function of GaN (10-10) from tight-binding

## Problem background
Gallium Nitride (GaN) is a wide-bandgap semiconductor critical for near-ultraviolet optoelectronic devices such as LEDs and lasers. At the nanoscale, the surfaces of GaN can host electronic states that lie inside the bulk band gap and significantly alter the material's optical response. Understanding these surface states and their influence on the dielectric function is important for device performance. This task investigates the optical signature of the nonpolar GaN (10-10) surface by computing the surface electronic structure and dielectric response from a tight-binding model, producing the full set of band structures, densities of states, and the imaginary part of the surface dielectric function.

## Approach
The electronic structure is modelled with an sp³s* orthogonal tight-binding Hamiltonian for wurtzite GaN. The tight-binding parameters (on-site energies and interatomic matrix elements) are provided; for the surface, the interactions are scaled using Harrison's 1/d² rule based on the reconstructed atomic coordinates. The optical response is computed from the transition matrix elements between eigenstates, including intra-atomic dipole corrections, and the surface dielectric function is isolated by subtracting the bulk contribution from the slab polarizability. The workflow first validates the bulk description by computing the bulk band structure and reflectivity, then constructs a periodic slab of 8 bilayers with the relaxed surface geometry, diagonalises the slab Hamiltonian at a dense k‑point mesh, extracts surface vs. bulk character to produce the surface band structure and layer‑projected density of states, and finally computes the imaginary part of the surface dielectric function for two orthogonal in‑plane polarisations.

## Reproduction target
Produce the five scored artifacts listed in the workflow: the bulk electronic band structure along high-symmetry lines, the bulk reflectivity spectra for two polarisations, the surface band structure along Γ–J and J–K with state‑type classification, the total and layer‑projected surface density of states, and the imaginary part of the surface dielectric function for x and y polarisations. The principal target is the surface dielectric function: its onset energy, the anisotropy between polarisations, and the spectral features (e.g. the position and relative intensity of peaks). A secondary target is the validation of the bulk description: the direct band gap at Γ and the static dielectric constant derived from the low‑frequency reflectivity.

## Assets

- Tight-binding parameters for GaN
- Reconstructed GaN (10-10) slab atomic coordinates
- sp3s* tight-binding implementation: python, numpy

## Workflow steps

### Step 1: Construct slab geometry
- Role: process
- Action: Construct an 8-bilayer GaN (10-10) slab using the bulk wurtzite lattice constants and the reconstructed surface atomic coordinates from the provided slab_geometry file.
- Evidence: `/app/outputs/slab_structure.npy`

### Step 2: Compute bulk band structure
- Role: scored
- Action: Compute the electronic band structure of bulk wurtzite GaN using the provided tight-binding parameters along the high-symmetry k-path (including Γ, A, L, M). Output eigenvalues for each k-point and band.
- Output file: `/app/outputs/bulk_band_structure.csv`
- Format: csv
- Contract: k_label: str, k_x: float, k_y: float, k_z: float, band_index: int, energy: float
- Scoring: scored by hidden verifier

### Step 3: Compute bulk reflectivity
- Role: scored
- Action: Compute the reflectivity of bulk GaN for light polarized perpendicular and parallel to the wurtzite c-axis, using the calculated eigenvalues and the optical transition matrix elements including intra-atomic dipoles. Output reflectivity as a function of photon energy.
- Output file: `/app/outputs/bulk_reflectivity.csv`
- Format: csv
- Contract: energy: float, R_perp: float, R_parallel: float
- Scoring: scored by hidden verifier

### Step 4: Compute slab eigenstates
- Role: process
- Action: Set up the tight-binding Hamiltonian for the slab using Harrison's 1/d² scaling based on the constructed geometry. Diagonalize at a dense grid of k-points in the irreducible surface Brillouin zone to obtain eigenvalues and eigenvectors.
- Evidence: `/app/outputs/eigenvalues.npy`

### Step 5: Extract surface electronic band structure
- Role: scored
- Action: Using the computed slab eigenstates, project onto bulk states to classify surface vs. projected bulk states. Extract eigenvalues along the paths Γ–J (surface x direction) and J–K (surface y direction) and output the band data with state type labels.
- Output file: `/app/outputs/surface_band_structure.csv`
- Format: csv
- Contract: k_x: float, k_y: float, band_index: int, energy: float, state_type: str
- Scoring: scored by hidden verifier

### Step 6: Compute layer-projected density of states
- Role: scored
- Action: Compute the total electronic density of states and its projection onto the first, second, and third layers of the slab from the slab eigenstates.
- Output file: `/app/outputs/surface_dos.csv`
- Format: csv
- Contract: energy: float, total: float, layer1: float, layer2: float, layer3: float
- Scoring: scored by hidden verifier

### Step 7: Compute surface dielectric function
- Role: scored (load-bearing)
- Action: Compute the imaginary part of the surface dielectric function for light polarized along x and y by evaluating transition matrix elements between slab eigenstates, including intra-atomic dipole contributions, and subtracting the bulk contribution.
- Output file: `/app/outputs/surface_dielectric_function.csv`
- Format: csv
- Contract: energy: float, eps2_x: float, eps2_y: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_band_structure.csv`
- `/app/outputs/bulk_reflectivity.csv`
- `/app/outputs/surface_band_structure.csv`
- `/app/outputs/surface_dos.csv`
- `/app/outputs/surface_dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_band_structure.csv
- path: `/app/outputs/bulk_band_structure.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bulk electronic band structure along high-symmetry k-paths. The checker recomputes the direct band gap at Γ.
- schema:
  - `type`: table
  - `required_columns`: `k_label`, `k_x`, `k_y`, `k_z`, `band_index`, `energy`
  - `units`:
    - `energy`: eV
    - `k_x`: Å⁻¹
    - `k_y`: Å⁻¹
    - `k_z`: Å⁻¹

### bulk_reflectivity.csv
- path: `/app/outputs/bulk_reflectivity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bulk reflectivity for two polarizations. The checker recomputes the static dielectric constant from the low-frequency limit.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `R_perp`, `R_parallel`
  - `units`:
    - `energy`: eV
    - `R_perp`: dimensionless
    - `R_parallel`: dimensionless

### surface_band_structure.csv
- path: `/app/outputs/surface_band_structure.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface band structure along Γ–J and J–K. The checker extracts the minimum energy of empty surface states and the dispersion width along Γ–J.
- schema:
  - `type`: table
  - `required_columns`: `k_x`, `k_y`, `band_index`, `energy`, `state_type`
  - `units`:
    - `energy`: eV
    - `k_x`: Å⁻¹
    - `k_y`: Å⁻¹

### surface_dos.csv
- path: `/app/outputs/surface_dos.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Total and layer-projected density of states. The checker locates peaks assigned to surface resonances.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total`, `layer1`, `layer2`, `layer3`
  - `units`:
    - `energy`: eV
    - `total`: states/eV
    - `layer1`: states/eV
    - `layer2`: states/eV
    - `layer3`: states/eV

### surface_dielectric_function.csv
- path: `/app/outputs/surface_dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Imaginary part of the surface dielectric function for two polarizations. The checker verifies the onset energy, the position and relative intensity of the 4 eV peak, and anisotropy.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `eps2_x`, `eps2_y`
  - `units`:
    - `energy`: eV
    - `eps2_x`: dimensionless
    - `eps2_y`: dimensionless

Notes: All scored artifacts will be compared against paper-reported reference values with appropriate tolerances. The checker recomputes key quantities (band gap, static dielectric constant, onset energy, dispersion width, resonance energies, dielectric peak positions) from these CSV files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_label",
          "k_x",
          "k_y",
          "k_z",
          "band_index",
          "energy"
        ],
        "units": {
          "energy": "eV",
          "k_x": "Å⁻¹",
          "k_y": "Å⁻¹",
          "k_z": "Å⁻¹"
        }
      },
      "description": "Bulk electronic band structure along high-symmetry k-paths. The checker recomputes the direct band gap at Γ."
    },
    {
      "file": "bulk_reflectivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "R_perp",
          "R_parallel"
        ],
        "units": {
          "energy": "eV",
          "R_perp": "dimensionless",
          "R_parallel": "dimensionless"
        }
      },
      "description": "Bulk reflectivity for two polarizations. The checker recomputes the static dielectric constant from the low-frequency limit."
    },
    {
      "file": "surface_band_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_x",
          "k_y",
          "band_index",
          "energy",
          "state_type"
        ],
        "units": {
          "energy": "eV",
          "k_x": "Å⁻¹",
          "k_y": "Å⁻¹"
        }
      },
      "description": "Surface band structure along Γ–J and J–K. The checker extracts the minimum energy of empty surface states and the dispersion width along Γ–J."
    },
    {
      "file": "surface_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total",
          "layer1",
          "layer2",
          "layer3"
        ],
        "units": {
          "energy": "eV",
          "total": "states/eV",
          "layer1": "states/eV",
          "layer2": "states/eV",
          "layer3": "states/eV"
        }
      },
      "description": "Total and layer-projected density of states. The checker locates peaks assigned to surface resonances."
    },
    {
      "file": "surface_dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "eps2_x",
          "eps2_y"
        ],
        "units": {
          "energy": "eV",
          "eps2_x": "dimensionless",
          "eps2_y": "dimensionless"
        }
      },
      "description": "Imaginary part of the surface dielectric function for two polarizations. The checker verifies the onset energy, the position and relative intensity of the 4 eV peak, and anisotropy."
    }
  ],
  "notes": "All scored artifacts will be compared against paper-reported reference values with appropriate tolerances. The checker recomputes key quantities (band gap, static dielectric constant, onset energy, dispersion width, resonance energies, dielectric peak positions) from these CSV files."
}
```

## How you are scored
Each scored workflow step produces a CSV file. A hidden verifier independently parses these files, recomputes key physical quantities (band gap, onset energy of surface states, dispersion width along Γ–J, resonance energies, dielectric peak positions, static dielectric constant, and anisotropy trends), and compares them against hidden reference thresholds. Your final reward is a weighted combination of these per‑step checks; simply reporting a number is not sufficient—the submitted files must contain the raw computed data from which the quantities are derived. Precision and fidelity to the expected physical behaviour determine your score.
