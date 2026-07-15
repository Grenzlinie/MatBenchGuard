# DFT Study of V-Doped GaN Magnetic and Optical Properties

## Problem background
Wide‑bandgap semiconductors doped with transition metals are studied as dilute magnetic semiconductors (DMS) for potential spintronic applications. GaN is a prominent host material, and doping with vanadium has been proposed to induce ferromagnetic order and modify optical properties. Determining whether V‑doped GaN displays a ferromagnetic ground state and how the doping changes the optical absorption spectrum is the central problem addressed by the computational workflow.

## Approach
The approach uses first‑principles density functional theory (DFT) within the generalized gradient approximation (GGA‑PBE). The system is modelled as a 2×2×2 wurtzite GaN supercell (32 atoms) in which two Ga atoms are replaced by V atoms at the nearest‑neighbour pair positions (configuration I). Spin‑polarized calculations are performed for both ferromagnetic (FM) and antiferromagnetic (AFM) alignments to compare their total energies and extract magnetic moments. To probe electronic correlation effects, the same FM geometry is also treated with an on‑site Hubbard U applied to V‑3d states (GGA+U). For each method the dielectric function and absorption coefficient are computed, yielding the optical response of the doped material. The workflow proceeds by first relaxing a pristine GaN supercell, then relaxing the V‑doped cell in FM and AFM configurations, extracting magnetic data, performing optical single‑point calculations, and finally tabulating the spectra on a common energy grid.

## Reproduction target
Using the 12.5 % V‑doped GaN supercell (configuration I):
- Determine whether the FM or AFM spin ordering is lower in energy by computing ΔE = E(AFM) – E(FM).
- Extract the total magnetic moment of the supercell and the local moments on each V atom.
- Produce the optical absorption spectrum (imaginary part of the dielectric function ε₂ and absorption coefficient α) for the FM state using both GGA and GGA+U.
- Demonstrate how the on‑site Hubbard U changes the low‑energy optical response, particularly the presence or absence of a near‑band‑edge absorption feature.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ga PBE pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- N PBE pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- V PBE pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- Wurtzite GaN crystal structure

## Workflow steps

### Step 1: Geometry optimization of pristine GaN supercell
- Role: process
- Action: Construct a 2×2×2 wurtzite GaN supercell (32 atoms) using the standard experimental lattice parameters. Perform a full DFT structural relaxation (atomic positions and cell) with the PBE functional. Converge forces to strict tolerances. Save the optimized structure for use in subsequent steps.
- Evidence: `/app/outputs/pure_GaN_relax.log`

### Step 2: Geometry optimization of V-doped GaN for FM and AFM states
- Role: process
- Action: Using the relaxed pure GaN supercell, substitute two Ga atoms with V atoms at the nearest-neighbor pair positions (configuration I). Perform spin-polarized DFT relaxations for both ferromagnetic (FM) and antiferromagnetic (AFM) spin orderings with PBE. Save the final relaxed structures and total energies.
- Evidence: `/app/outputs/v_doped_fm_afm_relax.log`

### Step 3: Magnetic stability and moments extraction
- Role: scored
- Action: From the converged FM and AFM relaxations, extract the final total energies and the magnetic moments (total per supercell and on each V atom). Compute the total-energy difference ΔE = E_AFM - E_FM. Write the results to magnetic_data.csv.
- Output file: `/app/outputs/magnetic_data.csv`
- Format: csv
- Contract: Columns: configuration, Delta_E_eV, MM_supercell_emu, MM_V1_emu, MM_V2_emu. Configuration is string 'I'. Delta_E_eV positive scalar (eV). Magnetic moments in μB.
- Scoring: scored by hidden verifier

### Step 4: Compute optical properties for FM state (GGA and GGA+U)
- Role: process
- Action: Using the relaxed FM V-doped structure, perform two separate single-point DFT calculations: one with standard GGA-PBE, and one with GGA+U (U applied to V-3d states). For each, compute the dielectric function and derive the absorption coefficient over a wide energy range. Use a dense k-point grid for accurate spectra.
- Evidence: `/app/outputs/optical_calc.log`

### Step 5: Optical spectra table
- Role: scored (load-bearing)
- Action: Interpolate the computed imaginary part of the dielectric function ε₂ and absorption coefficient from both GGA and GGA+U calculations onto a common energy grid covering 0 to 30 eV with at least 200 points. Save the table as optical_spectra.csv.
- Output file: `/app/outputs/optical_spectra.csv`
- Format: csv
- Contract: Columns: energy_ev (eV), epsilon2_gga (dimensionless), absorption_gga_arbu (arbitrary), epsilon2_gga_u (dimensionless), absorption_gga_u_arbu (arbitrary). At least 200 energy points from 0 to 30 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_data.csv`
- `/app/outputs/optical_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_data.csv
- path: `/app/outputs/magnetic_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Extracted total-energy difference and magnetic moments for the V-doped configuration I.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `Delta_E_eV`, `MM_supercell_emu`, `MM_V1_emu`, `MM_V2_emu`
  - `units`:
    - `Delta_E_eV`: eV
    - `MM_supercell_emu`: μB
    - `MM_V1_emu`: μB
    - `MM_V2_emu`: μB

### optical_spectra.csv
- path: `/app/outputs/optical_spectra.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Optical spectra (dielectric function and absorption) computed with GGA and GGA+U.
- schema:
  - `type`: table
  - `required_columns`: `energy_ev`, `epsilon2_gga`, `absorption_gga_arbu`, `epsilon2_gga_u`, `absorption_gga_u_arbu`
  - `units`:
    - `energy_ev`: eV
    - `epsilon2_gga`: dimensionless
    - `absorption_gga_arbu`: arbitrary
    - `epsilon2_gga_u`: dimensionless
    - `absorption_gga_u_arbu`: arbitrary

Notes: The checker will verify the magnetic data against paper‑reported reference values with appropriate tolerances, and will perform a structural audit on the optical spectra to confirm the characteristic GGA low‑energy peak and its suppression under GGA+U.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "Delta_E_eV",
          "MM_supercell_emu",
          "MM_V1_emu",
          "MM_V2_emu"
        ],
        "units": {
          "Delta_E_eV": "eV",
          "MM_supercell_emu": "μB",
          "MM_V1_emu": "μB",
          "MM_V2_emu": "μB"
        }
      },
      "description": "Extracted total-energy difference and magnetic moments for the V-doped configuration I."
    },
    {
      "file": "optical_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_ev",
          "epsilon2_gga",
          "absorption_gga_arbu",
          "epsilon2_gga_u",
          "absorption_gga_u_arbu"
        ],
        "units": {
          "energy_ev": "eV",
          "epsilon2_gga": "dimensionless",
          "absorption_gga_arbu": "arbitrary",
          "epsilon2_gga_u": "dimensionless",
          "absorption_gga_u_arbu": "arbitrary"
        }
      },
      "description": "Optical spectra (dielectric function and absorption) computed with GGA and GGA+U."
    }
  ],
  "notes": "The checker will verify the magnetic data against paper‑reported reference values with appropriate tolerances, and will perform a structural audit on the optical spectra to confirm the characteristic GGA low‑energy peak and its suppression under GGA+U."
}
```

## How you are scored
A hidden verifier independently examines each of your scored output files (`magnetic_data.csv` and `optical_spectra.csv`). For the magnetic data, the verifier checks the computed energy difference and magnetic moments against expected physical values (using appropriate tolerances to account for code and pseudopotential differences). For the optical spectra, it performs a structural audit: it inspects the GGA column for a characteristic low‑energy absorption peak, then checks whether that peak is suppressed in the GGA+U column. Each check contributes a portion of the final score, and the total reward is the weighted sum of these independent evaluations. Simply reporting a number from the literature is not sufficient; you must produce the described artifacts through the DFT workflow.
