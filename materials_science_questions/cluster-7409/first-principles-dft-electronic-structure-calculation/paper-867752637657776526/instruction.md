# Bulk and strained LaTiO₃ magnetic order and electronic structure from first-principles DFT+U calculations

## Problem background
Perovskite LaTiO3 is a prototypical Mott insulator and the parent compound of the RTiO3 family. In its bulk form, LaTiO3 adopts an orthorhombic Pbnm structure and orders magnetically into a G-type antiferromagnetic (G-AFM) arrangement. The interplay between the localized Ti 3d electrons, the GdFeO3-type structural distortions, and the oxygen octahedral rotations dictates the magnetic ground state. When LaTiO3 is grown as a thin film on different perovskite substrates, epitaxial strain distorts the crystal lattice, modifying the Ti–O–Ti bond angles and therefore the magnetic exchange interactions. First-principles electronic structure calculations can predict whether compressive or tensile biaxial strain stabilizes a magnetic order different from the bulk G-AFM, and whether the material remains insulating. The task here is to compute these strain-induced changes in magnetic order and electronic structure from first principles.

## Approach
The physics is captured by density-functional theory (DFT) within the local density approximation (LDA) augmented by a Hubbard U correction (LDA+U) to treat the strong on-site Coulomb repulsion of the Ti 3d electrons. The Hubbard correction is applied using the Dudarev implementation with an effective on-site interaction U−J = 2.3 eV on the Ti 3d states. All calculations are performed with the open-source Quantum ESPRESSO package, employing appropriate projector-augmented wave (PAW) pseudopotentials for La, Ti, and O.

The workflow first relaxes the bulk LaTiO3 crystal structure fully (lattice constants and atomic positions). Using the relaxed bulk geometry, self-consistent LDA+U calculations are carried out for five magnetic configurations: non-magnetic (NM), ferromagnetic (FM), A-type antiferromagnetic (A-AFM), C-type antiferromagnetic (C-AFM), and G-type antiferromagnetic (G-AFM). Total energies and Ti magnetic moments are extracted to identify the ground state and compare the relative stability of the different orders.

To model epitaxial strain, the in-plane lattice constants are fixed to the pseudocubic lattice parameters of five substrates: LaAlO3, LaGaO3, and SrTiO3 (compressive strain); BaTiO3 and LaScO3 (tensile strain). For each substrate the out‑of‑plane c-axis length and the internal atomic positions are relaxed while keeping the in-plane dimensions constrained, and the total energies of the most relevant magnetic orders are compared. The insulating character is assessed by computing the total density of states (DOS) and extracting the band gap across the Fermi level for each structure. Additionally, the Ti–O–Ti bond angles in-plane and out‑of‑plane can be extracted from the relaxed geometries to trace the structural origin of the magnetic transitions.

## Reproduction target
Compute the following quantities from LDA+U total-energy and electronic-structure calculations using Quantum ESPRESSO:

1. **Bulk magnetic properties** – For unstrained LaTiO3, report the total energy per Ti for each magnetic configuration (NM, FM, A‑AFM, C‑AFM, G‑AFM), the energy difference relative to the FM state (ΔE = E − E_FM, in meV/Ti), and the magnetic moment per Ti (μB/Ti). The results must be written to `/app/outputs/bulk_magnetic_properties.json`.

2. **Strain-induced magnetic energy differences** – For each compressive substrate (LaAlO3, LaGaO3, SrTiO3), after full relaxation with the in-plane lattice fixed to the substrate value, compare the energies of A‑AFM and G‑AFM orders and report ΔE = E(A‑AFM) − E(G‑AFM) (meV/Ti) together with the optimized c-axis length. For each tensile substrate (BaTiO3, LaScO3), compare C‑AFM and G‑AFM orders and report ΔE = E(C‑AFM) − E(G‑AFM) (meV/Ti) plus the optimized c-axis length. Output to `/app/outputs/strained_cases_energy_differences.json`.

3. **Band gaps** – For bulk LaTiO3 (in its G‑AFM ground state) and for each strained film in its predicted ground-state magnetic order, compute the insulating band gap (eV) from the total density of states and report it in `/app/outputs/band_gap_values.json`.

Additionally, you may record the in-plane and out‑of‑plane Ti–O–Ti bond angles from each relaxed geometry in `/app/outputs/bond_angles.csv` as process evidence.

## Assets

- Quantum ESPRESSO (QE) – open-source DFT code: https://www.quantum-espresso.org/
- PAW pseudopotentials for La, Ti, O (e.g., SSSP or PSLibrary): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Bulk LaTiO₃ structure relaxation
- Role: process
- Action: Set up the orthorhombic bulk LaTiO₃ unit cell (space group Pbnm, 4 formula units) using the experimental lattice constants as an initial guess, then perform a full DFT+U structural relaxation (cell parameters and atomic positions) to obtain the relaxed bulk geometry.
- Evidence: `/app/outputs/bulk_relaxation.json`

### Step 2: Bulk magnetic order energy comparison
- Role: scored (load-bearing)
- Action: Using the relaxed bulk structure, perform self-consistent DFT+U calculations for the non-magnetic (NM), ferromagnetic (FM), A-type antiferromagnetic (A-AFM), C-type antiferromagnetic (C-AFM), and G-type antiferromagnetic (G-AFM) magnetic configurations. Extract the total energy per formula unit and the magnetic moment per Ti for each configuration, and compute the energy difference per Ti relative to FM: ΔE = E(magnetic) – E(FM).
- Output file: `/app/outputs/bulk_magnetic_properties.json`
- Format: json
- Contract: JSON object with keys: "magnetic_orders" (list of strings), "relative_energies_meV_per_Ti" (list of numbers, same order), "magnetic_moments_muB_per_Ti" (list of numbers, same order).
- Scoring: scored by hidden verifier

### Step 3: Strain magnetic order energy comparison
- Role: scored
- Action: For each compressive substrate (LaAlO₃, LaGaO₃, SrTiO₃), fix the in-plane lattice constants to the values given in the paper, relax the c-axis lattice constant and internal coordinates for both A-AFM and G-AFM orders, compute their total energies, and determine ΔE = E(A-AFM) – E(G-AFM). For each tensile substrate (BaTiO₃, LaScO₃), fix the in-plane constants, relax for C-AFM and G-AFM, and compute ΔE = E(C-AFM) – E(G-AFM). Record the optimized c-axis lattice constant for each substrate/magnetic-order combination.
- Output file: `/app/outputs/strained_cases_energy_differences.json`
- Format: json
- Contract: JSON object with keys: "compressive" (list of objects, each with "substrate", "strain_percent", "c_axis_A", "E_A_AFM_minus_G_AFM_meVperTi") and "tensile" (list of objects, each with "substrate", "strain_percent", "c_axis_A", "E_C_AFM_minus_G_AFM_meVperTi").
- Scoring: scored by hidden verifier

### Step 4: Electronic band gap calculation
- Role: scored
- Action: Using the relaxed ground-state structures (bulk G-AFM, SrTiO₃ film with A-AFM, BaTiO₃ film with G-AFM, and the other substrates in their determined ground-state magnetic order), compute the total electronic density of states (DOS) and extract the band gap (energy difference across the Fermi level). Report the band gap for the bulk and for each strained film.
- Output file: `/app/outputs/band_gap_values.json`
- Format: json
- Contract: JSON object with keys: "bulk_band_gap_eV" (number), "strained_band_gaps" (list of objects, each with "substrate", "strain_type" ("compressive" or "tensile"), "band_gap_eV").
- Scoring: scored by hidden verifier

### Step 5: Ti–O–Ti bond angle analysis
- Role: process
- Action: From the relaxed atomic positions for the bulk and each strained film, extract the in-plane and out‑of‑plane Ti–O–Ti bond angles as a function of the biaxial strain and record them.
- Evidence: `/app/outputs/bond_angles.csv`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_magnetic_properties.json`
- `/app/outputs/strained_cases_energy_differences.json`
- `/app/outputs/band_gap_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_magnetic_properties.json
- path: `/app/outputs/bulk_magnetic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed relative energies and magnetic moments for the five magnetic configurations of bulk LaTiO₃.
- schema:
  - `type`: object
  - `required`:
    - `magnetic_orders`: array of strings
    - `relative_energies_meV_per_Ti`: array of numbers (meV/Ti)
    - `magnetic_moments_muB_per_Ti`: array of numbers (μB/Ti)

### strained_cases_energy_differences.json
- path: `/app/outputs/strained_cases_energy_differences.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy differences between competing magnetic orders and optimized c-axis values under strain.
- schema:
  - `type`: object
  - `required`:
    - `compressive`: array of objects with keys substrate, strain_percent, c_axis_A, E_A_AFM_minus_G_AFM_meVperTi
    - `tensile`: array of objects with keys substrate, strain_percent, c_axis_A, E_C_AFM_minus_G_AFM_meVperTi

### band_gap_values.json
- path: `/app/outputs/band_gap_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Insulating band gap for bulk and each strained film.
- schema:
  - `type`: object
  - `required`:
    - `bulk_band_gap_eV`: number (eV)
    - `strained_band_gaps`: array of objects with keys substrate, strain_type ("compressive" or "tensile"), band_gap_eV (number)

Notes: The hidden checker compares the agent's reported values to the paper's reference results using tolerances for energy differences, magnetic moments, and band gaps. It also enforces the expected sign and ordering of energy differences for compressive and tensile cases. No gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_magnetic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "magnetic_orders": "array of strings",
          "relative_energies_meV_per_Ti": "array of numbers (meV/Ti)",
          "magnetic_moments_muB_per_Ti": "array of numbers (μB/Ti)"
        }
      },
      "description": "Computed relative energies and magnetic moments for the five magnetic configurations of bulk LaTiO₃."
    },
    {
      "file": "strained_cases_energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compressive": "array of objects with keys substrate, strain_percent, c_axis_A, E_A_AFM_minus_G_AFM_meVperTi",
          "tensile": "array of objects with keys substrate, strain_percent, c_axis_A, E_C_AFM_minus_G_AFM_meVperTi"
        }
      },
      "description": "Energy differences between competing magnetic orders and optimized c-axis values under strain."
    },
    {
      "file": "band_gap_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_band_gap_eV": "number (eV)",
          "strained_band_gaps": "array of objects with keys substrate, strain_type (\"compressive\" or \"tensile\"), band_gap_eV (number)"
        }
      },
      "description": "Insulating band gap for bulk and each strained film."
    }
  ],
  "notes": "The hidden checker compares the agent's reported values to the paper's reference results using tolerances for energy differences, magnetic moments, and band gaps. It also enforces the expected sign and ordering of energy differences for compressive and tensile cases. No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier inspects the three JSON output files you produce under `/app/outputs`. It compares your reported values to a set of hidden reference data that capture the physical behaviour expected from the DFT+U calculations described in the literature. The verifier checks not only numerical closeness within allowed tolerances but also qualitative trends: for example, the relative ordering of magnetic energies under compressive and tensile strain must show the correct physical sign and monotonicity, and the band gap must remain finite for all configurations. Each output artifact is scored separately, and the final reward is a weighted combination of the per-artifact scores. There is no need to guess or match a specific published table; performing the calculations faithfully and writing the required JSON files according to the given schema will yield a valid reward.
