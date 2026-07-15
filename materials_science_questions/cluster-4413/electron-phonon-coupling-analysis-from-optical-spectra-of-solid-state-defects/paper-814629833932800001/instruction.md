# Two-phonon Raman spectrum calculation of bilayer graphene via non-orthogonal tight-binding model

## Problem background
Bernal-stacked bilayer graphene (BLG) is a candidate material for nanoelectronics due to its unique electronic properties, and Raman spectroscopy is a primary non-destructive tool for its characterization. The high-frequency two-phonon Raman bands (2D, 2D', D+D''), along with less intense bands in the mid-frequency range, contain detailed information about layer stacking, electronic structure, and phonon dispersion. Despite their importance, the assignment of these bands to specific overtone and combination modes has remained controversial, and a complete first-principles-level calculation of their intensities including all resonant processes has been lacking. A parameter-free theoretical procedure that can predict the full two-phonon Raman spectrum would resolve these assignments and provide a reliable reference for sample characterization.

## Approach
The computational procedure is based on a non-orthogonal tight-binding (NTB) model of BLG. Hamiltonian and overlap matrix elements for carbon are transferred from published density-functional theory studies on carbon dimers and on interlayer interactions in few-layer graphene. The model provides total energy and forces, allowing relaxation of the atomic structure to its equilibrium geometry. From the relaxed structure, the electronic band structure is obtained by solving the NTB eigenvalue problem on a fine k-point mesh. The phonon dispersion is computed from a dynamical matrix derived via perturbation theory within the same NTB model; all in-plane phonon frequencies are downscaled by a factor of 0.9 to correct the systematic tight-binding overestimation. Electron‑photon matrix elements (for electron‑hole creation and recombination) and electron‑phonon scattering matrix elements are evaluated explicitly from the NTB electronic states and orbitals. A phenomenological energy-dependent electronic linewidth, taken as twice the value for single‑layer graphene, accounts for electron‑phonon and electron‑electron scattering. The Stokes two‑phonon Raman intensity is described by the fourth‑order perturbation expression that sums over intermediate and final states containing an electron‑hole pair and two created phonons. The calculation includes all eight types of resonant processes, both intravalley and intervalley scattering, and both overtone and combination modes. The Brillouin‑zone integration for intermediate electron and final phonon wavevectors is performed on dense meshes, and the energy-conserving delta function is replaced by a Lorentzian with a small halfwidth. The resulting intensity is normalized to a maximum of 1. Finally, the dominant Raman bands are located in the computed spectrum and their peak shifts and relative intensities are extracted.

## Reproduction target
Compute the full two-phonon Stokes Raman spectrum of Bernal-stacked bilayer graphene at a laser excitation energy of 2.33 eV in parallel backscattering configuration, normalized to a maximum intensity of 1, and save it as raman_spectrum_2.33eV.csv. Separately, compute the overtone-only contribution (excluding combination modes) to the 2TO@K (2D) band region and save as overtone_only_2D_contribution.csv. From the full spectrum, identify the Raman shift (in cm⁻¹) and relative intensity (normalized to the global maximum) of the peaks corresponding to the modes: 2TO@K (2D band), 2LO@Γ (2D' band), TOLA@K (D+D'' band), LOZO'@Γ (M⁻ band), and TOZO'@K (M⁺ band). Report these values in extracted_peak_positions.json.

## Assets

- DFT-derived NTB parameters for carbon dimers (Porezag et al. 1995): 10.1103/PhysRevB.51.12947
- NTB model interlayer parameters for bilayer graphene (Popov & Alsenoy 2014): 10.1103/PhysRevB.90.245429
- Crystal structure of Bernal-stacked bilayer graphene

## Workflow steps

### Step 1: Implement NTB electronic structure model
- Role: process
- Action: Construct the non-orthogonal tight-binding Hamiltonian and overlap matrices for Bernal-stacked bilayer graphene using the parameter sets from the DFT studies (Porezag et al. 1995 and Popov & Alsenoy 2014). This yields the NTB model providing total energy, forces, electronic states, and wavefunctions.
- Evidence: `/app/outputs/ntb_parameters_loaded.json`

### Step 2: Relax atomic structure within NTB model
- Role: process
- Action: Use the NTB total energy and forces to relax the bilayer graphene geometry to the equilibrium atomic structure.
- Evidence: `/app/outputs/relaxed_structure.json`

### Step 3: Compute electronic band structure on dense k-mesh
- Role: process
- Action: Solve the NTB eigenvalue problem on a fine k-point grid to obtain energy bands and wavefunctions necessary for subsequent matrix element evaluation and Raman intensity integration.
- Evidence: `/app/outputs/band_structure_summary.json`

### Step 4: Compute raw phonon dispersion
- Role: process
- Action: Calculate phonon frequencies and eigenvectors using the dynamical matrix derived by perturbation theory within the NTB model, on the relaxed structure.
- Evidence: `/app/outputs/raw_phonon_dispersion.csv`

### Step 5: Apply frequency scaling to in-plane modes
- Role: process
- Action: Downscale all in-plane phonon frequencies by a factor of 0.9 to correct the systematic tight-binding overestimation, producing the scaled phonon dispersion used in Raman calculations.
- Evidence: `/app/outputs/scaled_phonon_dispersion.csv`

### Step 6: Compute electron-photon and electron-phonon matrix elements
- Role: process
- Action: Explicitly evaluate the momentum matrix elements for electron-hole creation/recombination and the electron/hole-phonon scattering matrix elements from the NTB electronic states and orbitals.
- Evidence: `/app/outputs/matrix_elements_computed.txt`

### Step 7: Define electronic linewidth model
- Role: process
- Action: Set the energy-dependent electronic linewidth γ = 25.2 E_L + 6.9 E_L² (γ in meV, E_L in eV), taken double the single-layer value, to account for electron-phonon and electron-electron scattering.
- Evidence: `/app/outputs/linewidth_model.txt`

### Step 8: Compute full two-phonon Raman spectrum at E_L=2.33 eV
- Role: scored
- Action: Using the fourth-order perturbation expression for Stokes Raman intensity with the NTB-derived matrix elements, scaled phonons, and linewidth model, perform the full Brillouin-zone integration over a dense mesh, including all eight resonant process types and both intravalley and intervalley scattering. Replace the energy-conserving delta with a Lorentzian of 5 cm⁻¹ halfwidth. Normalize the maximum intensity to 1. Save the full two-phonon Raman spectrum (Raman shift vs intensity).
- Output file: `/app/outputs/raman_spectrum_2.33eV.csv`
- Format: csv
- Contract: CSV with header: raman_shift_cm1, intensity
- Scoring: scored by hidden verifier

### Step 9: Compute overtone-only contribution to the 2D (2TO@K) band
- Role: scored
- Action: Restrict the Raman intensity summation to overtone modes only (exclude combination modes) for the 2TO@K band region, using the same computational model and mesh, and save the overtone-only intensity as a separate spectrum with the same two-column format.
- Output file: `/app/outputs/overtone_only_2D_contribution.csv`
- Format: csv
- Contract: CSV with header: raman_shift_cm1, intensity
- Scoring: scored by hidden verifier

### Step 10: Extract peak positions and intensities of major Raman bands
- Role: scored (load-bearing)
- Action: From the computed full Raman spectrum, identify the five target bands: 2TO@K (2D), 2LO@Γ (2D'), TOLA@K (D+D''), LOZO'@Γ (M⁻), and TOZO'@K (M⁺). For each, determine the peak Raman shift (cm⁻¹) and its relative intensity (normalized to the global maximum) and report them as a JSON object.
- Output file: `/app/outputs/extracted_peak_positions.json`
- Format: json
- Contract: {"2TO_K": {"peak_cm1": number, "relative_intensity": number}, "2LO_Gamma": {"peak_cm1": number, "relative_intensity": number}, "TOLA_K": {"peak_cm1": number, "relative_intensity": number}, "LOZO_Gamma": {"peak_cm1": number, "relative_intensity": number}, "TOZO_K": {"peak_cm1": number, "relative_intensity": number}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raman_spectrum_2.33eV.csv`
- `/app/outputs/overtone_only_2D_contribution.csv`
- `/app/outputs/extracted_peak_positions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raman_spectrum_2.33eV.csv
- path: `/app/outputs/raman_spectrum_2.33eV.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Full two-phonon Raman spectrum at laser excitation energy 2.33 eV. The checker recomputes peak positions and intensities from this file.
- schema:
  - `type`: table
  - `required_columns`: `raman_shift_cm1`, `intensity`
  - `units`:
    - `raman_shift_cm1`: cm⁻¹
    - `intensity`: arb. units (normalized max=1)

### overtone_only_2D_contribution.csv
- path: `/app/outputs/overtone_only_2D_contribution.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Overtone-only contribution to the 2D band region. Checker validates consistency with the full spectrum (peak positions must match).
- schema:
  - `type`: table
  - `required_columns`: `raman_shift_cm1`, `intensity`
  - `units`:
    - `raman_shift_cm1`: cm⁻¹
    - `intensity`: arb. units (normalized same as full spectrum)

### extracted_peak_positions.json
- path: `/app/outputs/extracted_peak_positions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported peak positions and relative intensities of five major two-phonon Raman bands, directly compared to hidden gold values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `2TO_K`:
      - `peak_cm1`: number
      - `relative_intensity`: number
    - `2LO_Gamma`:
      - `peak_cm1`: number
      - `relative_intensity`: number
    - `TOLA_K`:
      - `peak_cm1`: number
      - `relative_intensity`: number
    - `LOZO_Gamma`:
      - `peak_cm1`: number
      - `relative_intensity`: number
    - `TOZO_K`:
      - `peak_cm1`: number
      - `relative_intensity`: number

Notes: All output files are required. The checker may also recompute peaks from the submitted CSV spectra to cross-validate the reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raman_spectrum_2.33eV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "raman_shift_cm1",
          "intensity"
        ],
        "units": {
          "raman_shift_cm1": "cm⁻¹",
          "intensity": "arb. units (normalized max=1)"
        }
      },
      "description": "Full two-phonon Raman spectrum at laser excitation energy 2.33 eV. The checker recomputes peak positions and intensities from this file."
    },
    {
      "file": "overtone_only_2D_contribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "raman_shift_cm1",
          "intensity"
        ],
        "units": {
          "raman_shift_cm1": "cm⁻¹",
          "intensity": "arb. units (normalized same as full spectrum)"
        }
      },
      "description": "Overtone-only contribution to the 2D band region. Checker validates consistency with the full spectrum (peak positions must match)."
    },
    {
      "file": "extracted_peak_positions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "2TO_K": {
            "peak_cm1": "number",
            "relative_intensity": "number"
          },
          "2LO_Gamma": {
            "peak_cm1": "number",
            "relative_intensity": "number"
          },
          "TOLA_K": {
            "peak_cm1": "number",
            "relative_intensity": "number"
          },
          "LOZO_Gamma": {
            "peak_cm1": "number",
            "relative_intensity": "number"
          },
          "TOZO_K": {
            "peak_cm1": "number",
            "relative_intensity": "number"
          }
        }
      },
      "description": "Agent-reported peak positions and relative intensities of five major two-phonon Raman bands, directly compared to hidden gold values within tolerances."
    }
  ],
  "notes": "All output files are required. The checker may also recompute peaks from the submitted CSV spectra to cross-validate the reported values."
}
```

## How you are scored
Each workflow stage produces a scored artifact: the total Raman spectrum CSV, the overtone-only contribution CSV, and the extracted peak positions JSON. A hidden verifier inspects these artifacts. For the full spectrum, the verifier locates major bands within expected spectral windows and compares their peak positions and intensities to reference values derived from the literature; it also checks that the overtone‑only contribution is consistent with the full 2D band (peak positions must match within a small allowed shift). The extracted peak positions JSON is compared directly to reference peak positions and intensities. Scores are combined by weight, with the final reward reflecting the agreement of the computed results with the reference. Simply reporting the paper’s numbers without executing the full computational pipeline is not sufficient to obtain credit.
