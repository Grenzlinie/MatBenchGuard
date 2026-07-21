# Structural, electronic and optical properties of 4-monolayer ZnO thin films via DFT

## Problem background
Zinc oxide (ZnO) is a wide-gap semiconductor of technological importance. Ultrathin films cut along different crystallographic orientations exhibit distinct atomic structures that strongly modify their electronic and optical properties. This task addresses the challenge of characterizing these finite-size effects by performing first-principles calculations on 4-monolayer ZnO films with six different polymorph orientations. The goal is to quantify structural parameters (in-plane lattice constants, film thickness, bond angles), formation energies, direct band gaps at Γ, high-frequency dielectric tensor components, and the anisotropy of the absorption onset. These quantities are the key fingerprints for comparing theory with spectroscopic experiments on ultrathin ZnO layers.

## Approach
The computational workflow combines a generalized-gradient approximation (PBE) for structural relaxation with a range-separated hybrid functional (HSE03) to obtain accurate electronic structures and optical properties. After building slab models of the six orientations (including a polarity-compensated reconstructed Wurtzite (0001) termination), each geometry is fully relaxed with PBE. On the relaxed structures, static HSE03 calculations provide total energies, Kohn‑Sham eigenvalues, and the electronic building blocks for optical response. The high‑frequency dielectric tensor is obtained by performing HSE03 calculations on supercells with several vacuum thicknesses and extrapolating the macroscopic dielectric function to isolate the intrinsic film contribution. Absorption spectra are computed within the random‑phase approximation (RPA) without local‑field effects, and the first absorption peaks in the in‑plane and out‑of‑plane directions are identified. Finally, formation energies are evaluated using the HSE03 total energy of bulk wurtzite as a reference. All calculations may be carried out with any open‑source periodic DFT code that supports PAW/pseudopotentials, the PBE and HSE functionals, and linear‑response dielectric computations (e.g., Quantum ESPRESSO).

## Reproduction target
Produce the following four JSON files under `/app/outputs`, each containing the required fields for all six film orientations (BCT(010), CUB(100), h-BN(0001), ZB(110), WUR(10‑10), WUR(0001)):

- `structural_energies.json`: orientation, a_ang (Å), b_ang (Å), h_ang (Å), alpha_avg_deg (degrees), theta_deg (degrees), E_f_eV_per_A2 (eV/Å²).
- `band_gaps.json`: orientation, E_g_film_eV (eV), E_g_bulk_eV (eV), delta_E_g_eV (eV).
- `dielectric_constants.json`: orientation, epsilon_inf_xx, epsilon_inf_yy, epsilon_inf_zz (dimensionless).
- `absorption_anisotropy.json`: orientation, theta_deg (degrees), Delta_eV (eV), epsilon_ratio_xy_z (dimensionless).

The checker will compare your reported numbers against a set of hidden reference values obtained from the published work. No other outputs are required for scoring.

## Assets

- Bulk crystallographic data for ZnO polymorphs (wurtzite, zinc-blende, BCT, cubane, h-BN): https://next-gen.materialsproject.org/materials?chemsys=Zn-O
- PAW pseudopotentials for Zn and O: https://pseudopotentials.quantum-espresso.org/legacy_tables/sssp-accuracy
- Open-source periodic DFT code supporting hybrid functionals and linear response: https://www.quantum-espresso.org

## Workflow steps

### Step 1: Generate slab models
- Role: process
- Action: Build initial unrelaxed 4-monolayer ZnO slab geometries for the six orientations: BCT(010), CUB(100), h-BN(0001), ZB(110), WUR(10-10), WUR(0001). For WUR(0001), create the (2×2) surface unit cell with the necessary vacancy reconstruction to compensate polarity. Use bulk lattice parameters of each polymorph as starting points. Include ~12 Å of vacuum.
- Evidence: `/app/outputs/initial_geometries.json`

### Step 2: PBE structural relaxation
- Role: process
- Action: For each slab, perform full geometry optimization using the PBE generalized-gradient approximation with a plane-wave basis and PAW pseudopotentials. Relax atomic positions and in-plane cell parameters until convergence. Save the relaxed coordinates and lattice parameters.
- Evidence: `/app/outputs/relaxed_geometries.json`

### Step 3: HSE03 total energy and electronic structure calculation
- Role: process
- Action: Using the PBE-relaxed geometries, perform static HSE03 hybrid functional calculations for each film and for bulk wurtzite. Obtain total energies, Kohn-Sham eigenvalues, and occupations for subsequent extraction.
- Evidence: `/app/outputs/hse_results.json`

### Step 4: Structural parameters and formation energies
- Role: scored
- Action: Extract from the relaxed geometries: in-plane lattice parameters a and b, film thickness h, average surface bond angle ⟨α⟩, and dangling bond angle θ. Using the HSE03 total energies, compute the film formation energy per surface area E_f = (E_film - n * E_bulk_WUR)/S. Write a JSON array with one object per orientation.
- Output file: `/app/outputs/structural_energies.json`
- Format: json
- Contract: JSON array of objects. Each object must have keys: orientation (string), a_ang (float, Å), b_ang (float, Å), h_ang (float, Å), alpha_avg_deg (float, degrees), theta_deg (float, degrees), E_f_eV_per_A2 (float, eV/Å²).
- Scoring: scored by hidden verifier

### Step 5: Compute band gaps
- Role: scored
- Action: From the HSE03 eigenvalues, determine the direct band gap at Γ for each film and for the corresponding bulk polymorph. Compute the gap difference δEg = Eg(film) - Eg(bulk). Write the results.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON array of objects. Each object must have keys: orientation (string), E_g_film_eV (float, eV), E_g_bulk_eV (float, eV), delta_E_g_eV (float, eV).
- Scoring: scored by hidden verifier

### Step 6: Prepare dielectric constant calculations
- Role: process
- Action: For each relaxed film, perform HSE03 calculations on supercells with at least two different vacuum layer thicknesses to obtain the macroscopic dielectric function ε_sc(D) for momentum transfers along x, y, z, using the random-phase approximation without local field effects. Save the raw ε_sc(D) data.
- Evidence: `/app/outputs/dielectric_raw.json`

### Step 7: Extract high-frequency dielectric tensor
- Role: scored (load-bearing)
- Action: Apply the extrapolation formula ε_sc(D) = [h*ε_inf + (D-h)*1]/D to the raw ε_sc(D) data to extract the intrinsic film high-frequency dielectric constants ε∞_xx, ε∞_yy, ε∞_zz. Write the components for all films.
- Output file: `/app/outputs/dielectric_constants.json`
- Format: json
- Contract: JSON array of objects. Each object must have keys: orientation (string), epsilon_inf_xx (float), epsilon_inf_yy (float), epsilon_inf_zz (float).
- Scoring: scored by hidden verifier

### Step 8: Compute absorption spectra (RPA)
- Role: process
- Action: Using the HSE03 Kohn-Sham states from the film calculation, compute the imaginary part of the dielectric function ε₂(ω) via the random-phase approximation for momentum vectors along x, y, z up to 30 eV, using fine k-point grids. Save the raw spectral data.
- Evidence: `/app/outputs/absorption_spectra.json`

### Step 9: Analyze absorption peak anisotropy
- Role: scored
- Action: From the absorption spectra, identify the energy of the first absorption peaks in the in-plane (x,y) and out-of-plane (z) directions; compute the energy difference Δ = E_z_peak - E_inplane_peak. Retrieve the dangling bond angle θ from structural_energies.json and the dielectric anisotropy ratio ε∞_xy/ε∞_z from dielectric_constants.json. Report θ, Δ, and the ratio for each film.
- Output file: `/app/outputs/absorption_anisotropy.json`
- Format: json
- Contract: JSON array of objects. Each object must have keys: orientation (string), theta_deg (float, degrees), Delta_eV (float, eV), epsilon_ratio_xy_z (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_energies.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/dielectric_constants.json`
- `/app/outputs/absorption_anisotropy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_energies.json
- path: `/app/outputs/structural_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed structural parameters and film formation energies per surface area for six film orientations.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `orientation`, `a_ang`, `b_ang`, `h_ang`, `alpha_avg_deg`, `theta_deg`, `E_f_eV_per_A2`
    - `properties`:
      - `orientation`: string
      - `a_ang`: float, Å
      - `b_ang`: float, Å
      - `h_ang`: float, Å
      - `alpha_avg_deg`: float, degrees
      - `theta_deg`: float, degrees
      - `E_f_eV_per_A2`: float, eV/Å²

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gaps at Γ for films and their corresponding bulk polymorphs, and the difference.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `orientation`, `E_g_film_eV`, `E_g_bulk_eV`, `delta_E_g_eV`
    - `properties`:
      - `orientation`: string
      - `E_g_film_eV`: float, eV
      - `E_g_bulk_eV`: float, eV
      - `delta_E_g_eV`: float, eV

### dielectric_constants.json
- path: `/app/outputs/dielectric_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: High-frequency dielectric tensor components obtained via supercell extrapolation.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `orientation`, `epsilon_inf_xx`, `epsilon_inf_yy`, `epsilon_inf_zz`
    - `properties`:
      - `orientation`: string
      - `epsilon_inf_xx`: float
      - `epsilon_inf_yy`: float
      - `epsilon_inf_zz`: float

### absorption_anisotropy.json
- path: `/app/outputs/absorption_anisotropy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Correlation table: dangling bond angle, energy difference between z and in-plane first absorption peaks, and dielectric anisotropy ratio.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `orientation`, `theta_deg`, `Delta_eV`, `epsilon_ratio_xy_z`
    - `properties`:
      - `orientation`: string
      - `theta_deg`: float, degrees
      - `Delta_eV`: float, eV
      - `epsilon_ratio_xy_z`: float

Notes: All numeric comparisons are performed against hidden reference values from the paper's tables (I, II, IV, V) with tolerances that absorb systematic differences between DFT implementations. The solver must produce data for all six orientations: BCT(010), CUB(100), h-BN(0001), ZB(110), WUR(10-10), WUR(0001).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "orientation",
            "a_ang",
            "b_ang",
            "h_ang",
            "alpha_avg_deg",
            "theta_deg",
            "E_f_eV_per_A2"
          ],
          "properties": {
            "orientation": "string",
            "a_ang": "float, Å",
            "b_ang": "float, Å",
            "h_ang": "float, Å",
            "alpha_avg_deg": "float, degrees",
            "theta_deg": "float, degrees",
            "E_f_eV_per_A2": "float, eV/Å²"
          }
        }
      },
      "description": "Relaxed structural parameters and film formation energies per surface area for six film orientations."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "orientation",
            "E_g_film_eV",
            "E_g_bulk_eV",
            "delta_E_g_eV"
          ],
          "properties": {
            "orientation": "string",
            "E_g_film_eV": "float, eV",
            "E_g_bulk_eV": "float, eV",
            "delta_E_g_eV": "float, eV"
          }
        }
      },
      "description": "Direct band gaps at Γ for films and their corresponding bulk polymorphs, and the difference."
    },
    {
      "file": "dielectric_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "orientation",
            "epsilon_inf_xx",
            "epsilon_inf_yy",
            "epsilon_inf_zz"
          ],
          "properties": {
            "orientation": "string",
            "epsilon_inf_xx": "float",
            "epsilon_inf_yy": "float",
            "epsilon_inf_zz": "float"
          }
        }
      },
      "description": "High-frequency dielectric tensor components obtained via supercell extrapolation."
    },
    {
      "file": "absorption_anisotropy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "orientation",
            "theta_deg",
            "Delta_eV",
            "epsilon_ratio_xy_z"
          ],
          "properties": {
            "orientation": "string",
            "theta_deg": "float, degrees",
            "Delta_eV": "float, eV",
            "epsilon_ratio_xy_z": "float"
          }
        }
      },
      "description": "Correlation table: dangling bond angle, energy difference between z and in-plane first absorption peaks, and dielectric anisotropy ratio."
    }
  ],
  "notes": "All numeric comparisons are performed against hidden reference values from the paper's tables (I, II, IV, V) with tolerances that absorb systematic differences between DFT implementations. The solver must produce data for all six orientations: BCT(010), CUB(100), h-BN(0001), ZB(110), WUR(10-10), WUR(0001)."
}
```

## How you are scored
A hidden verifier reads your four JSON files. It checks that all six orientations are present and that each file’s schema is correct. For every numeric field (e.g., a_ang, E_f_eV_per_A2, E_g_film_eV, epsilon_inf_xx, Delta_eV, etc.) the verifier compares your reported value to a hidden reference value using a tolerance that accounts for the systematic differences between DFT implementations. Your final reward is the fraction of field‑orientation combinations that fall within tolerance, computed across all four artifacts with equal weight per file. This means each of the four scored outputs contributes equally to your final score. Simply reporting numbers that look plausible is not enough; they must result from the described computational procedure and match the underlying physics to within the allowed spread.
