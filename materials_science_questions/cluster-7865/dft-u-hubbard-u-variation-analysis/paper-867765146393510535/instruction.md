# DFT+U Study of Interfacial Octahedral Rotation Coupling in SrIrO3/SrTiO3 Heterostructures

## Problem background
Ultrathin films of the perovskite SrIrO3 grown on (001)-oriented SrTiO3 substrates exhibit a strong interplay between lattice structure and electronic properties. SrTiO3 undergoes a cubic-to-tetragonal phase transition near 105 K, forming ferroelastic domains with distinct oxygen octahedral rotation patterns. These domain patterns couple across the interface to the orthorhombic SrIrO3 film, potentially locking its domain configuration and determining the orientation of the characteristic in-phase rotation axis. Density functional theory (DFT) calculations can reveal the energetic preference between different domain orientations, how the band structure responds to the axis alignment, and what octahedral rotation angles emerge in the heterostructure. This task reproduces those DFT calculations to determine the energetic preference, the electronic band structure along specific high-symmetry directions, and the equilibrium rotation angles for a SrIrO3/SrTiO3 supercell.

## Approach
Construct atomistic supercells of the SrTiO3/SrIrO3 heterostructure with two different alignments of the in-phase rotation axis: one with the axis in the film plane and one with the axis perpendicular to the plane. For each configuration, perform structural relaxation using density functional theory (DFT) with the PBEsol exchange-correlation functional, a Hubbard U correction on Ir 5d orbitals to account for electronic correlations, spin-orbit coupling, and G-type antiferromagnetic order. After relaxation, extract the total energies to compare the two domain orientations and identify the stable configuration. Using the relaxed structure of the stable orientation, run a non-self-consistent band structure calculation along the high-symmetry path Γ–X–S–Γ–Y and output the Kohn-Sham eigenvalues. Finally, extract the in-plane (α, β) and out-of-plane (γ) octahedral rotation angles from the relaxed atomic positions of the stable configuration by fitting oxygen positions to the Glazer rotation pattern. All calculations can be performed with the open-source Quantum ESPRESSO package using publicly available crystal structures and pseudopotentials from the SSSP library.

## Reproduction target
The goal is to produce three scored artifacts that capture the key DFT results:

1. **Energy difference between domain orientations** – report the total energy per formula unit (eV) for the in-plane in-phase-axis and out-of-plane in-phase-axis supercells, compute the difference, and state which orientation is lower in energy.
2. **Band structure along Γ–X–S–Γ–Y** – provide the electronic eigenvalues along the specified k-path for the relaxed structure with the in-phase axis in-plane, with sufficient density to reveal the presence or absence of bands crossing the Fermi level on each segment.
3. **Octahedral rotation angles** – extract the in-plane (α, β) and out-of-plane (γ) Glazer rotation angles (in degrees) from the relaxed ionic positions of the stable configuration.

## Assets

- Orthorhombic SrIrO3 crystal structure
- Cubic SrTiO3 crystal structure
- SSSP efficiency pseudopotentials (PBEsol): https://www.materialscloud.org/discover/sssp/table/precision
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: DFT structural relaxation and total energy calculation
- Role: process
- Action: Construct SrTiO3/SrIrO3 heterostructure supercells with the in-phase rotation axis oriented in-plane and out-of-plane, respectively. For each orientation, perform full ionic and cell relaxation using PBEsol+U (U on Ir 5d orbitals, with a Hund's coupling JH=0.15U), spin-orbit coupling, and G-type antiferromagnetic order. Preserve the required supercell boundaries (4/4 formula units for the in-plane-axis case and 8/8 for the out-of-plane case). Collect the final total energies and the relaxed atomic coordinates for the stable (in-plane axis) configuration.
- Evidence: `/app/outputs/relaxed_outputs.tar`

### Step 2: Extract energy difference between domain orientations
- Role: scored (load-bearing)
- Action: From the total energies obtained in the relaxation step, compute the energy per formula unit (in eV) for each configuration. Calculate the difference ΔE = E_out_of_plane − E_in_plane and identify which orientation is lower in energy. Write the results to a JSON file.
- Output file: `/app/outputs/step_01_energy_difference.json`
- Format: json
- Contract: JSON object with keys: energy_in_plane_per_fu (float, eV), energy_out_of_plane_per_fu (float, eV), energy_difference (float, eV), lower_energy_configuration (string, either 'in_plane' or 'out_of_plane').
- Scoring: scored by hidden verifier

### Step 3: DFT band structure calculation
- Role: process
- Action: Using the relaxed structure with the in-plane in-phase axis, run a non-self-consistent DFT calculation (same functional, U=1.47 eV, JH=0.15U, spin-orbit coupling, AFM order) to obtain the Kohn-Sham eigenvalues along the high-symmetry path Γ–X–S–Γ–Y. Use a dense set of k-points along each segment.
- Evidence: `/app/outputs/bands_calc.log`

### Step 4: Write band structure data
- Role: scored
- Action: Extract the band eigenvalues from the DFT calculation and write them to a text file. Columns must include k-point index, k-path label (Γ, X, S, Γ, Y), k-distance along the path (in 1/Å), and energy (eV) for each band. Ensure the path contains the segments Γ–X, X–S, S–Γ, Γ–Y with at least 50 points per segment.
- Output file: `/app/outputs/step_02_band_structure.dat`
- Format: txt
- Contract: Text file with one header line then rows. Columns: k_index (int), k_label (string, e.g., 'Γ','X','S','Y'), k_distance (float, 1/Å), band_1_energy (float, eV), band_2_energy (float, eV), ... up to the highest band near the Fermi level.
- Scoring: scored by hidden verifier

### Step 5: Extract octahedral rotation angles
- Role: scored
- Action: From the relaxed ionic positions of the in-plane-axis supercell, determine the in-plane (α, β) and out-of-plane (γ) octahedral rotation angles (in degrees) by fitting oxygen positions to Glazer rotation angles.
- Output file: `/app/outputs/step_03_rotation_angles.json`
- Format: json
- Contract: JSON object with keys: alpha_deg (float), beta_deg (float, equal to alpha in square in-plane symmetry), gamma_deg (float). All in degrees.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_difference.json`
- `/app/outputs/step_02_band_structure.dat`
- `/app/outputs/step_03_rotation_angles.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_difference.json
- path: `/app/outputs/step_01_energy_difference.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The agent's reported per-formula-unit energies and their difference for the two domain orientations. The checker recomputes the difference and compares the sign and magnitude with the paper's result.
- schema:
  - `type`: object
  - `required`:
    - `energy_in_plane_per_fu`: number (eV)
    - `energy_out_of_plane_per_fu`: number (eV)
    - `energy_difference`: number (eV)
    - `lower_energy_configuration`: string

### step_02_band_structure.dat
- path: `/app/outputs/step_02_band_structure.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Band eigenvalues along the high-symmetry path Γ–X–S–Γ–Y. The checker verifies that at least one band crosses the Fermi level along the out-of-phase path (Γ–X–S) while no band crosses along the in-phase path (S–Γ–Y).
- schema:
  - `type`: text
  - `required_columns`: `k_index`, `k_label`, `k_distance`, `band_*_energy`

### step_03_rotation_angles.json
- path: `/app/outputs/step_03_rotation_angles.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: In-plane and out-of-plane octahedral rotation angles extracted from the relaxed structure. The checker compares α, β, γ against paper-derived reference values with a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `alpha_deg`: number
    - `beta_deg`: number
    - `gamma_deg`: number

Notes: The band structure audit is qualitative: presence/absence of Fermi level crossings along prescribed path segments. Energy difference and rotation angles are compared to paper-reported hidden gold values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_difference.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "energy_in_plane_per_fu": "number (eV)",
          "energy_out_of_plane_per_fu": "number (eV)",
          "energy_difference": "number (eV)",
          "lower_energy_configuration": "string"
        }
      },
      "description": "The agent's reported per-formula-unit energies and their difference for the two domain orientations. The checker recomputes the difference and compares the sign and magnitude with the paper's result."
    },
    {
      "file": "step_02_band_structure.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required_columns": [
          "k_index",
          "k_label",
          "k_distance",
          "band_*_energy"
        ]
      },
      "description": "Band eigenvalues along the high-symmetry path Γ–X–S–Γ–Y. The checker verifies that at least one band crosses the Fermi level along the out-of-phase path (Γ–X–S) while no band crosses along the in-phase path (S–Γ–Y)."
    },
    {
      "file": "step_03_rotation_angles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha_deg": "number",
          "beta_deg": "number",
          "gamma_deg": "number"
        }
      },
      "description": "In-plane and out-of-plane octahedral rotation angles extracted from the relaxed structure. The checker compares α, β, γ against paper-derived reference values with a tolerance."
    }
  ],
  "notes": "The band structure audit is qualitative: presence/absence of Fermi level crossings along prescribed path segments. Energy difference and rotation angles are compared to paper-reported hidden gold values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier checks each output artifact independently and combines the scores into a final reward (0 to 1). The verifier recomputes the energy difference from the per‑formula‑unit energies you submit and evaluates the sign and magnitude. The band structure file is audited by scanning for Fermi‑level crossings along specific high‑symmetry segments; the verifier checks whether electron‑like pockets cross the Fermi level on certain path segments and not on others. The rotation angles α, β, and γ are compared against hidden reference values derived from the paper, with allowances for the expected spread of DFT results. Reporting the paper’s numbers is not sufficient — the verifier evaluates the content of your files to ensure the required quantities were genuinely computed.
