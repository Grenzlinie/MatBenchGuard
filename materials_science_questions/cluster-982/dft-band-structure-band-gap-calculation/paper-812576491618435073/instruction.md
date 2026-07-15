# Unfolded Optical Conductivity of Si-Doped Graphene

## Problem background
The optical properties of materials, such as optical conductivity, are fundamentally linked to electronic transitions between occupied and unoccupied states. In impurity or doped materials, these transitions are perturbed by broken symmetry and changes in the electronic band structure. A method that combines the Kubo-Greenwood formula for optical conductivity with band-structure unfolding enables projection of optical transition weights onto the unfolded electronic band structure of a reference system. This provides a tool to analyze how dopants, vacancies, or other imperfections affect optical transitions at specific k-points and bands. The present task demonstrates this method on monolayer Si-doped graphene, a material of interest for photovoltaic and optoelectronic applications. The goal is to compute the optical conductivity and unfolded optical transition weights for a supercell containing a single silicon substitution, as a way to assess the dopant's influence on optical properties.

## Approach
The core approach is to perform density functional theory (DFT) calculations on a Si-doped graphene supercell, then apply the Kubo-Greenwood formula to obtain the frequency-dependent optical conductivity tensor. The DFT calculations use localised atomic orbital basis sets, which naturally allow decomposition of the momentum matrix elements into contributions from individual atomic orbitals. From the self-consistent field results, the momentum matrix elements between all pairs of Kohn-Sham states are computed. The optical conductivity is then evaluated over a frequency range, giving a spectrum that includes both interband and intraband transitions. To connect the supercell results back to the pristine graphene reference system, an unfolding technique is employed: for each reference k-point and band in the folded Brillouin zone, the supercell optical weights are projected using overlap matrices and LCAO coefficients, yielding an unfolded partial optical conductivity. By integrating over a chosen frequency window, the integrated unfolded transition weights can be plotted on the unfolded band structure, and optionally decomposed by atomic species or orbitals. The task reproduces this entire workflow for a SiG-4×4 supercell (one Si atom replacing one C atom in a 4×4 graphene sheet), producing the optical conductivity spectrum and the unfolded weights as structured numerical files.

## Reproduction target
For the SiG-4×4 supercell, produce two scored artifacts under `/app/outputs`:

1. **Frequency-dependent optical conductivity** (`optical_conductivity_sig_4x4.csv`): a CSV file containing the real and imaginary parts of σ_xx and σ_yy (in atomic units) over the range 0–10 eV, computed using the Kubo-Greenwood formula with a broadening parameter η = 0.05 eV. The file must have columns `frequency_eV`, `sigma_xx_real`, `sigma_xx_imag`, `sigma_yy_real`, `sigma_yy_imag`.

2. **Unfolded integrated partial optical conductivity** (`unfolded_weights_siG_4x4.json`): a JSON array of objects, each representing an unfolded reference k-point and band along the Γ-K-M-Γ path. Each object must contain `k_index`, `kx` (1/Å), `ky` (1/Å), `band_index`, `energy_eV`, `unfolded_weight`, and `integrated_conductivity` (the σ_{(xx+yy)/2} integrated over 0–6 eV, in atomic units). The unfolded weights should reflect the spectral weight projection from the supercell to the reference graphene Brillouin zone using the LCAO coefficients and overlap matrices.

The hidden verifier will check that the optical conductivity spectrum exhibits physically expected features (e.g., a first peak near the band gap and a broad peak at higher energy) and that the unfolded weights show a non-zero band gap at K and meaningful integrated conductivity. The agent does not need to produce separate Si-projected decomposition; the primary target is the total unfolded weights.

## Assets

- OpenMX DFT package (v3.8): https://www.openmx-square.org/download.html
- Optimized pseudoatomic orbitals and norm-conserving pseudopotentials (C-s2p2d1, Si-s2p2d1, E-s2p2d2f1): included in the OpenMX distribution

## Workflow steps

### Step 1: DFT geometry optimization of SiG-4x4
- Role: process
- Action: Perform DFT geometry optimization of a 4×4×1 graphene supercell with one carbon substituted by silicon, using OpenMX with the GGA-PBE functional, appropriate basis sets (C-s2p2d1, Si-s2p2d1, E-s2p2d2f1) and a ghost atom at the honeycomb center. Allow atomic positions and in-plane lattice constants to relax while keeping c=18 Å fixed. Produce an optimized structure.
- Evidence: none

### Step 2: SCF calculation and momentum matrix element computation
- Role: process
- Action: Using the optimized structure from step 1, perform a self-consistent field (SCF) calculation with OpenMX to obtain Kohn-Sham eigenvalues, LCAO coefficients, and overlap matrices. Then compute the momentum matrix elements between all pairs of states using the LCAO coefficients and the gradient operator between localized orbitals.
- Evidence: none

### Step 3: Compute frequency-dependent optical conductivity
- Role: scored (load-bearing)
- Action: From the SCF results, compute the real and imaginary parts of σ_xx(ω) and σ_yy(ω) for the SiG-4x4 supercell using the Kubo-Greenwood formula with a broadening parameter η=0.05 eV, over the frequency range 0–10 eV. Save the spectrum as optical_conductivity_sig_4x4.csv.
- Output file: `/app/outputs/optical_conductivity_sig_4x4.csv`
- Format: csv
- Contract: CSV with columns: frequency_eV (float), sigma_xx_real (float), sigma_xx_imag (float), sigma_yy_real (float), sigma_yy_imag (float).
- Scoring: scored by hidden verifier

### Step 4: Unfold and integrate partial optical conductivity
- Role: scored (load-bearing)
- Action: Using the LCAO coefficients, overlap matrices, and the unfolded spectral weight formula, unfold the supercell optical weights to a graphene reference cell along the Γ-K-M-Γ path. For each reference k-point and band, compute the integrated partial optical conductivity σ_{(xx+yy)/2}(k,j,ω(0:6 eV)). Save the result as unfolded_weights_siG_4x4.json.
- Output file: `/app/outputs/unfolded_weights_siG_4x4.json`
- Format: json
- Contract: JSON array of objects, each with fields: k_index (int), kx (float, 1/Å), ky (float, 1/Å), band_index (int), energy_eV (float), unfolded_weight (float), integrated_conductivity (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_conductivity_sig_4x4.csv`
- `/app/outputs/unfolded_weights_siG_4x4.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_conductivity_sig_4x4.csv
- path: `/app/outputs/optical_conductivity_sig_4x4.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed optical conductivity spectrum of the SiG-4x4 supercell; checker verifies peak locations against reference.
- schema:
  - `type`: table
  - `required_columns`: `frequency_eV`, `sigma_xx_real`, `sigma_xx_imag`, `sigma_yy_real`, `sigma_yy_imag`
  - `units`:
    - `frequency_eV`: eV
    - `sigma_xx_real`: atomic units
    - `sigma_xx_imag`: atomic units
    - `sigma_yy_real`: atomic units
    - `sigma_yy_imag`: atomic units

### unfolded_weights_siG_4x4.json
- path: `/app/outputs/unfolded_weights_siG_4x4.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Unfolded and integrated partial optical conductivity on the reference graphene band structure; checker verifies band gap at K point and minimum conductivity threshold.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `k_index`, `kx`, `ky`, `band_index`, `energy_eV`, `unfolded_weight`, `integrated_conductivity`
    - `properties`:
      - `k_index`:
        - `type`: integer
      - `kx`:
        - `type`: number
        - `unit`: 1/Å
      - `ky`:
        - `type`: number
        - `unit`: 1/Å
      - `band_index`:
        - `type`: integer
      - `energy_eV`:
        - `type`: number
        - `unit`: eV
      - `unfolded_weight`:
        - `type`: number
      - `integrated_conductivity`:
        - `type`: number
        - `unit`: atomic units

Notes: The optical conductivity should exhibit a first peak near the band gap (about 0.2 eV) and a broad peak around 4 eV. The unfolded weights should show an unfolded band gap at K point consistent with that value and a non-negligible integrated conductivity there.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_conductivity_sig_4x4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_eV",
          "sigma_xx_real",
          "sigma_xx_imag",
          "sigma_yy_real",
          "sigma_yy_imag"
        ],
        "units": {
          "frequency_eV": "eV",
          "sigma_xx_real": "atomic units",
          "sigma_xx_imag": "atomic units",
          "sigma_yy_real": "atomic units",
          "sigma_yy_imag": "atomic units"
        }
      },
      "description": "Computed optical conductivity spectrum of the SiG-4x4 supercell; checker verifies peak locations against reference."
    },
    {
      "file": "unfolded_weights_siG_4x4.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "k_index",
            "kx",
            "ky",
            "band_index",
            "energy_eV",
            "unfolded_weight",
            "integrated_conductivity"
          ],
          "properties": {
            "k_index": {
              "type": "integer"
            },
            "kx": {
              "type": "number",
              "unit": "1/Å"
            },
            "ky": {
              "type": "number",
              "unit": "1/Å"
            },
            "band_index": {
              "type": "integer"
            },
            "energy_eV": {
              "type": "number",
              "unit": "eV"
            },
            "unfolded_weight": {
              "type": "number"
            },
            "integrated_conductivity": {
              "type": "number",
              "unit": "atomic units"
            }
          }
        }
      },
      "description": "Unfolded and integrated partial optical conductivity on the reference graphene band structure; checker verifies band gap at K point and minimum conductivity threshold."
    }
  ],
  "notes": "The optical conductivity should exhibit a first peak near the band gap (about 0.2 eV) and a broad peak around 4 eV. The unfolded weights should show an unfolded band gap at K point consistent with that value and a non-negligible integrated conductivity there."
}
```

## How you are scored
A hidden verifier independently scores each of the two scored workflow stages. For the optical conductivity CSV, the verifier reads the spectrum and checks the correspondence of key spectral features (e.g., the energy and magnitude of the first peak, the presence of a broad peak around 4 eV) against hidden reference values derived from the paper. For the unfolded weights JSON, the verifier examines the unfolded band structure along the Γ-K-M-Γ path: it verifies that the direct band gap at the K point is consistent with expectations, that the integrated conductivity at representative points is non-negligible, and that the unfolding weights produce a physically plausible fat-band pattern. Each artifact carries a weight: the optical conductivity contributes a smaller share and the unfolded weights contribute the larger share, reflecting the method’s main claim. The final reward (float between 0 and 1) is the weighted sum of the per-artifact scores. The verifier does not simply check file existence; it performs quantitative comparisons against hidden tolerances designed to accept legitimate toolchain variations while rejecting trivial answers.
