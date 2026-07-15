# First-principles structural, phonon, and property analysis of a 2D carbon monolayer

## Problem background
A novel two-dimensional carbon monolayer, propylenidene (PPD), has been proposed. It is built by arranging bicyclopropylidene units into a rectangular lattice containing three-, eight-, and ten-membered carbon rings. First-principles density functional theory calculations are used to predict its structural, electronic, mechanical, optical, and dynamical stability properties. Reproducing these predictions through an independent computational workflow is essential to verify the material's characteristics and assess its potential for applications such as energy storage, sensing, and optoelectronics. This task therefore requires computing the key material properties from the given unit-cell structure using a standard plane-wave DFT approach.

## Approach
The reproduction follows a first-principles DFT pipeline using open-source tools. Starting from an initial rectangular unit cell (space group Pmmm) with approximate lattice constants (e.g., a ≈ 7.0 Å, b ≈ 4.0 Å) and three distinct carbon atoms at rough fractional positions roughly around (0.90, 0.00, 0.00), (0.30, 0.80, 0.00), (0.60, 0.50, 0.00) that form the 3‑, 8‑, and 10‑membered ring network, the structure is first relaxed with the GGA-PBE functional plus a dispersion correction. From the relaxed geometry, the total energy is obtained and an isolated carbon atom reference energy is computed using the same DFT settings. These energies yield the cohesive energy per atom. The dynamical stability is then assessed by calculating the phonon frequencies at the Γ‑point via density functional perturbation theory (DFPT), ensuring no imaginary modes are present. The mechanical response is characterized by computing the independent elastic constants via the strain‑stress method, from which the directional Young's modulus and its extremes are derived. The electronic band structure is calculated along the high‑symmetry path Γ–X–S–Y–Γ–S to determine the material's band gap character. Finally, optical absorption spectra are computed for two independent light polarizations (xx and yy) to capture the material's optical anisotropy. All calculations are performed with Quantum ESPRESSO as the DFT engine, complemented by Phonopy for phonon post‑processing, and the final results are written to text and CIF files as specified in the workflow steps.

## Reproduction target
From the initial structure and DFT parameters provided, compute the following quantities and write them to the designated output files:
- Relaxed lattice parameters (a, b) and atomic positions in CIF format.
- Cohesive energy per atom (eV/atom).
- All phonon frequencies at the Γ point (THz); the absence of imaginary modes (i.e., no frequencies below a small negative threshold) indicates dynamical stability.
- Independent elastic constants C11, C22, C12, C66 (N/m).
- Minimum and maximum directional Young's modulus Ymin, Ymax (N/m).
- Electronic band structure along the Γ–X–S–Y–Γ–S path; from the eigenvalues, determine whether the system is metallic (gapless) or semiconducting/insulating.
- Optical absorption spectra for xx‑polarization and yy‑polarization, each as photon energy (eV) versus absorption coefficient, allowing a comparison of peak positions and relative intensities between the two polarizations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Phonopy: https://phonopy.github.io/phonopy/
- Python 3 with numpy, scipy: numpy scipy

## Workflow steps

### Step 1: DFT Structure Relaxation
- Role: scored
- Action: Perform DFT structure optimization of the PPD monolayer starting from an initial guess with approximate geometry as described in the Approach (rectangular cell, approximate lattice constants ~7.0 Å × 4.0 Å, and three atoms at rough positions). The relaxation will determine the final lattice parameters and atomic coordinates. Use GGA-PBE functional with a dispersion correction. Use GGA-PBE functional with a dispersion correction. Write the relaxed structure as a CIF file and save the final total energy to total_energy.txt.
- Output file: `/app/outputs/relaxed_structure.cif`
- Format: other
- Contract: CIF file containing unit cell parameters (a, b, c, alpha, beta, gamma) and atom sites.
- Scoring: scored by hidden verifier

### Step 2: Isolated Carbon Atom Energy
- Role: process
- Action: Compute the total energy of a single isolated carbon atom in a large supercell using the same DFT settings as the relaxation step. Write the energy in eV to /app/outputs/isolated_atom_energy.txt.
- Evidence: `/app/outputs/isolated_atom_energy.txt`

### Step 3: Cohesive Energy Calculation
- Role: scored (load-bearing)
- Action: Read the total energy of the relaxed structure (total_energy.txt) and the isolated atom energy (isolated_atom_energy.txt). Compute the cohesive energy per atom as E_coh = (E_tot - n*E_atom)/n, where n is the number of carbon atoms in the unit cell (3 atoms). Write the value in eV/atom to cohesive_energy.txt.
- Output file: `/app/outputs/cohesive_energy.txt`
- Format: txt
- Contract: Single numeric value in eV/atom.
- Scoring: scored by hidden verifier

### Step 4: Phonon Frequencies at Gamma
- Role: scored
- Action: Using density functional perturbation theory (DFPT) with the relaxed structure, compute the phonon frequencies at the Γ point. Write all frequencies (in THz) to phonon_frequencies_gamma.txt.
- Output file: `/app/outputs/phonon_frequencies_gamma.txt`
- Format: txt
- Contract: One frequency per line, in THz.
- Scoring: scored by hidden verifier

### Step 5: Elastic Constants
- Role: scored
- Action: Compute the independent elastic constants of the relaxed PPD monolayer (C11, C22, C12, C66) using the strain-stress method. Output them in N/m on a single line.
- Output file: `/app/outputs/elastic_constants.txt`
- Format: txt
- Contract: Four space-separated numbers: C11 C22 C12 C66.
- Scoring: scored by hidden verifier

### Step 6: Young's Modulus Extremes
- Role: scored
- Action: From the elastic constants, compute the angular dependence of Young's modulus and determine the minimum and maximum values. Write Ymin and Ymax (N/m) on a single line.
- Output file: `/app/outputs/young_modulus.txt`
- Format: txt
- Contract: Two space-separated numbers: Ymin Ymax.
- Scoring: scored by hidden verifier

### Step 7: Electronic Band Structure
- Role: scored
- Action: Compute the electronic band structure of the relaxed PPD monolayer along the high-symmetry path Γ–X–S–Y–Γ–S using the PBE functional. Write the eigenvalues (eV) for each k-point (including the k-point coordinates) to band_structure.txt.
- Output file: `/app/outputs/band_structure.txt`
- Format: txt
- Contract: Columns: k_index, kx, ky, kz, band1, band2, … (number of bands). Fermi level set to 0 eV.
- Scoring: scored by hidden verifier

### Step 8: Optical Absorption (XX)
- Role: scored
- Action: Compute the optical absorption coefficient for x-polarization and write the spectrum (photon energy in eV and absorption coefficient) to optical_absorption_xx.txt.
- Output file: `/app/outputs/optical_absorption_xx.txt`
- Format: txt
- Contract: Two columns: photon energy (eV) and absorption coefficient (arbitrary units).
- Scoring: scored by hidden verifier

### Step 9: Optical Absorption (YY)
- Role: scored
- Action: Compute the optical absorption coefficient for y-polarization and write the spectrum (photon energy in eV and absorption coefficient) to optical_absorption_yy.txt.
- Output file: `/app/outputs/optical_absorption_yy.txt`
- Format: txt
- Contract: Two columns: photon energy (eV) and absorption coefficient (arbitrary units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_structure.cif`
- `/app/outputs/cohesive_energy.txt`
- `/app/outputs/phonon_frequencies_gamma.txt`
- `/app/outputs/elastic_constants.txt`
- `/app/outputs/young_modulus.txt`
- `/app/outputs/band_structure.txt`
- `/app/outputs/optical_absorption_xx.txt`
- `/app/outputs/optical_absorption_yy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_structure.cif
- path: `/app/outputs/relaxed_structure.cif`
- format: other
- purpose: scored
- target_policy: exact_match
- description: Relaxed crystal structure; lattice constants a and b are compared to paper values within tolerance.
- schema:
  - `type`: other
  - `description`: CIF file containing lattice parameters a, b, c, alpha, beta, gamma and fractional atomic coordinates.

### cohesive_energy.txt
- path: `/app/outputs/cohesive_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Cohesive energy per atom; compared to paper value with tolerance.
- schema:
  - `type`: text
  - `units`: eV/atom

### phonon_frequencies_gamma.txt
- path: `/app/outputs/phonon_frequencies_gamma.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Phonon frequencies at Γ; checked for absence of imaginary modes (no frequency below a small negative threshold).
- schema:
  - `type`: text
  - `description`: List of phonon frequencies at Γ point, one per line, in THz.

### elastic_constants.txt
- path: `/app/outputs/elastic_constants.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Independent elastic constants of the monolayer.
- schema:
  - `type`: text
  - `description`: Space-separated C11, C22, C12, C66 in N/m.

### young_modulus.txt
- path: `/app/outputs/young_modulus.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Minimum and maximum directional Young's modulus.
- schema:
  - `type`: text
  - `description`: Space-separated Ymin and Ymax in N/m.

### band_structure.txt
- path: `/app/outputs/band_structure.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Electronic band structure along high-symmetry path; checked for metallic character (bands crossing Fermi level).
- schema:
  - `type`: table
  - `required_columns`: `k_index`, `kx`, `ky`, `kz`, `band1`
  - `description`: Columns: k_index, kx, ky, kz, then one column per band (eigenvalues in eV). Fermi level at 0 eV.

### optical_absorption_xx.txt
- path: `/app/outputs/optical_absorption_xx.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optical absorption spectrum for x-polarization; used to verify peak location and relative intensity trends.
- schema:
  - `type`: table
  - `required_columns`: `photon_energy`, `absorption`
  - `description`: Two columns: photon energy (eV) and absorption coefficient (arb. units).

### optical_absorption_yy.txt
- path: `/app/outputs/optical_absorption_yy.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optical absorption spectrum for y-polarization; used to verify peak location and relative intensity trends.
- schema:
  - `type`: table
  - `required_columns`: `photon_energy`, `absorption`
  - `description`: Two columns: photon energy (eV) and absorption coefficient (arb. units).

Notes: All quantities are computed from open-source DFT with public pseudopotentials. The checker will compare lattice parameters, cohesive energy, elastic constants, and Young's modulus against hidden reference values with appropriate tolerances. Phonon stability, band metallic nature, and optical peak locations are checked structurally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_structure.cif",
      "format": "other",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "other",
        "description": "CIF file containing lattice parameters a, b, c, alpha, beta, gamma and fractional atomic coordinates."
      },
      "description": "Relaxed crystal structure; lattice constants a and b are compared to paper values within tolerance."
    },
    {
      "file": "cohesive_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "eV/atom"
      },
      "description": "Cohesive energy per atom; compared to paper value with tolerance."
    },
    {
      "file": "phonon_frequencies_gamma.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "List of phonon frequencies at Γ point, one per line, in THz."
      },
      "description": "Phonon frequencies at Γ; checked for absence of imaginary modes (no frequency below a small negative threshold)."
    },
    {
      "file": "elastic_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Space-separated C11, C22, C12, C66 in N/m."
      },
      "description": "Independent elastic constants of the monolayer."
    },
    {
      "file": "young_modulus.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Space-separated Ymin and Ymax in N/m."
      },
      "description": "Minimum and maximum directional Young's modulus."
    },
    {
      "file": "band_structure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_index",
          "kx",
          "ky",
          "kz",
          "band1"
        ],
        "description": "Columns: k_index, kx, ky, kz, then one column per band (eigenvalues in eV). Fermi level at 0 eV."
      },
      "description": "Electronic band structure along high-symmetry path; checked for metallic character (bands crossing Fermi level)."
    },
    {
      "file": "optical_absorption_xx.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "photon_energy",
          "absorption"
        ],
        "description": "Two columns: photon energy (eV) and absorption coefficient (arb. units)."
      },
      "description": "Optical absorption spectrum for x-polarization; used to verify peak location and relative intensity trends."
    },
    {
      "file": "optical_absorption_yy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "photon_energy",
          "absorption"
        ],
        "description": "Two columns: photon energy (eV) and absorption coefficient (arb. units)."
      },
      "description": "Optical absorption spectrum for y-polarization; used to verify peak location and relative intensity trends."
    }
  ],
  "notes": "All quantities are computed from open-source DFT with public pseudopotentials. The checker will compare lattice parameters, cohesive energy, elastic constants, and Young's modulus against hidden reference values with appropriate tolerances. Phonon stability, band metallic nature, and optical peak locations are checked structurally."
}
```

## How you are scored
A hidden verifier independently checks each scored output file. For every scored step, the verifier either recomputes the target quantity from your raw artifact or compares your reported result against a hidden reference (the paper's own computed values) using tolerances that absorb legitimate toolchain spread, or it audits structural properties such as the absence of negative phonon frequencies, the metallic character of the band structure, and the presence and relative positions of optical absorption peaks. The per‑step scores are combined by weight to yield the final reward. Reporting only the expected numbers without executing the actual DFT workflow will not produce valid intermediate files and will therefore fail the structural checks that underpin the scoring.
