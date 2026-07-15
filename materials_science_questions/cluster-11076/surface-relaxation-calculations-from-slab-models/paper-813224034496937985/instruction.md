# Surface energies, work functions, and Cl adsorption from DFT slab calculations

## Problem background
MgCa alloys are promising candidates for biodegradable orthopedic implants because both Mg and Ca are essential elements in the human body, have densities close to that of bone, and are widely available. A key material property for implant applications is corrosion resistance, which governs how the implant degrades in physiological environments. Corrosion is strongly influenced by the surface energetics of the alloy phases and by the interaction of the surfaces with aggressive ions such as chlorine (Cl) that are present in body fluids. First-principles electronic structure calculations based on density functional theory (DFT) can provide quantitative predictions of surface energies, work functions, and adsorption energies for the relevant Mg, Ca, and B2 MgCa surfaces. Such theoretical data are currently sparse, particularly for the intermetallic MgCa phase, yet they are essential for understanding and predicting the relative corrosion resistance of these materials.

## Approach
The approach uses plane-wave DFT calculations within the generalized gradient approximation (GGA-PBE) to compute the properties of bulk solids, clean low-index surfaces, and chlorine-covered surfaces of Mg, Ca, and B2 MgCa. The workflow consists of: (1) calculating bulk reference energies for hcp Mg, fcc Ca, and B2 MgCa using the known equilibrium lattice parameters; (2) constructing periodic slab models for the low-index surfaces (Mg(0001), Ca(100)/(110)/(111), and MgCa(100)/(110)/(111) – for MgCa, both Ca-terminated and Mg-terminated variants of the polar (100) and (111) surfaces are included) with sufficient vacuum and layer thickness to converge the surface properties, and then relaxing the ionic positions; (3) computing surface energies via the excess energy of the slab relative to the bulk and work functions from the difference between the vacuum electrostatic potential and the Fermi level; (4) evaluating the reference energy of a Cl atom from a Cl2 molecular calculation; (5) adsorbing Cl atoms at the high-symmetry sites on the most close-packed surfaces (hcp Mg(0001), fcc Ca(111), and B2 MgCa(110)) and relaxing the combined system to obtain adsorption energies and work function shifts; (6) calculating the equilibrium bond lengths and bond dissociation energies of the Mg-Cl and Ca-Cl diatomic molecules from potential energy scans. All calculations are performed with an open-source DFT code that provides PAW pseudopotentials (such as Quantum ESPRESSO or GPAW), using the computational parameters described in the workflow steps.

## Reproduction target
The objective is to compute, from first principles, the following numerical quantities and report them in structured CSV output files:
- Surface energy (J/m²) and work function (eV) for each clean surface: Mg(0001), Ca(100), Ca(110), Ca(111), MgCa(100)-I (Ca-terminated), MgCa(100)-II (Mg-terminated), MgCa(110), MgCa(111)-I (Ca-terminated), and MgCa(111)-II (Mg-terminated).
- Adsorption energy (eV) and work function (eV) for Cl atoms on Mg(0001), Ca(111), and MgCa(110) surfaces at the stable high-symmetry adsorption sites. For Mg(0001) and Ca(111) the sites considered are top, bridge, fcc, and hcp; for MgCa(110) they are top Ca, top Mg, long, short, and bridge. If a Cl atom relaxes away from an initial site, only the final stable site is reported.
- Equilibrium bond length (Å) and bond dissociation energy (kJ/mol) for the Mg-Cl and Ca-Cl diatomic molecules, obtained from the minimum of the respective potential energy curves.
The computed values should be consistent with those reported in the original study, accounting for the differences between the original VASP code and the open-source DFT implementation used here.

## Assets

- Open-source DFT code with PAW pseudopotentials: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Bulk DFT calculations for Mg, Ca, and B2 MgCa
- Role: process
- Action: Perform DFT calculations on the bulk unit cells of Mg, Ca, and MgCa using the lattice constants from the paper (Ca: 5.52 Å, MgCa: 3.96 Å, Mg: a=3.19 Å, c/a=1.632) to obtain the total energy per atom E_bulk for each material.
- Evidence: `/app/outputs/bulk_energies.txt`

### Step 2: Relaxation of clean slab surfaces
- Role: process
- Action: Construct periodic slab models for Mg(0001), Ca(100)/(110)/(111), and B2 MgCa(100)/(110)/(111) surfaces with the specified layer/vacuum thicknesses and terminations (Ca- and Mg-terminated for (100) and (111)). Relax atomic positions via DFT, keeping central-layer atoms fixed. After relaxation, record the total energy of each slab, the electrostatic potential in the vacuum region V_vac, and the Fermi energy E_f.
- Evidence: `/app/outputs/clean_relaxation_summary.json`

### Step 3: Compute clean surface energies and work functions
- Role: scored (load-bearing)
- Action: Using relaxed slab total energies from step 2 and bulk energies from step 1, compute the surface energy σ = 1/2 (E_slab - N*E_bulk) for each surface. Using V_vac and E_f from step 2, compute the work function Φ = V_vac - E_f. Write the results to the output file.
- Output file: `/app/outputs/clean_surface_properties.csv`
- Format: csv
- Contract: Columns: surface (string), termination (string), surface_energy_J_per_m2 (float), work_function_eV (float). Rows: Mg(0001), Ca(100), Ca(110), Ca(111), MgCa(100)-I, MgCa(100)-II, MgCa(110), MgCa(111)-I, MgCa(111)-II.
- Scoring: scored by hidden verifier

### Step 4: Calculate Cl2 molecule reference energy
- Role: process
- Action: Perform a DFT calculation on an isolated Cl2 molecule to obtain its total energy and equilibrium bond length. Compute the energy per Cl atom E_Cl (half of Cl2 total energy).
- Evidence: `/app/outputs/cl2_energy.txt`

### Step 5: Relaxation of Cl-adsorbed slab surfaces
- Role: process
- Action: Construct symmetric adsorption configurations with Cl atoms at the high-symmetry sites on Mg(0001) (top, bridge, fcc, hcp), Ca(111) (top, bridge, fcc, hcp), and MgCa(110) (top Ca, top Mg, bridge, long, short). Relax the combined system via DFT, keeping central-layer atoms fixed. For sites where the Cl atom relaxes to a different final site, record the final site. After relaxation, record the total energy of each adsorbed slab, V_vac, and E_f.
- Evidence: `/app/outputs/adsorption_relaxation_summary.json`

### Step 6: Compute Cl adsorption energies and work functions
- Role: scored (load-bearing)
- Action: Using relaxed adsorption slab energies from step 5, clean slab energies from step 2, and E_Cl from step 4, compute the adsorption energy E_ads = 1/2 (E_Cl/sur - E_sur - 2*E_Cl) for each stable final site. Compute the work function Φ_ads = V_vac - E_f from step 5. Write the results to the output file.
- Output file: `/app/outputs/adsorption_properties.csv`
- Format: csv
- Contract: Columns: surface (string), adsorption_site (string), adsorption_energy_eV (float), work_function_eV (float). Rows for stable final sites: Mg(0001) top, hcp, fcc; Ca(111) hcp, fcc; MgCa(110) top Ca, top Mg, long, short.
- Scoring: scored by hidden verifier

### Step 7: Compute Mg-Cl and Ca-Cl dimer bond energies and lengths
- Role: scored (load-bearing)
- Action: Perform DFT calculations for the Mg-Cl and Ca-Cl diatomic systems over a range of bond lengths to obtain potential energy curves. Determine the equilibrium bond length (minimum-energy separation) and bond energy (depth of the potential well). Write the results to the output file.
- Output file: `/app/outputs/dimer_properties.csv`
- Format: csv
- Contract: Columns: dimer (string), bond_length_angstrom (float), bond_energy_kJ_per_mol (float). Rows: Mg-Cl, Ca-Cl.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/clean_surface_properties.csv`
- `/app/outputs/adsorption_properties.csv`
- `/app/outputs/dimer_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### clean_surface_properties.csv
- path: `/app/outputs/clean_surface_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed surface energy and work function for each clean surface; compared against paper reference values within hidden tolerances.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `termination`, `surface_energy_J_per_m2`, `work_function_eV`
  - `units`:
    - `surface_energy_J_per_m2`: J/m^2
    - `work_function_eV`: eV

### adsorption_properties.csv
- path: `/app/outputs/adsorption_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed adsorption energy and work function for each stable Cl adsorption site; compared against paper reference values within hidden tolerances.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `adsorption_site`, `adsorption_energy_eV`, `work_function_eV`
  - `units`:
    - `adsorption_energy_eV`: eV
    - `work_function_eV`: eV

### dimer_properties.csv
- path: `/app/outputs/dimer_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium bond length and bond energy for Mg-Cl and Ca-Cl dimers; compared against paper reference values within hidden tolerances.
- schema:
  - `type`: table
  - `required_columns`: `dimer`, `bond_length_angstrom`, `bond_energy_kJ_per_mol`
  - `units`:
    - `bond_length_angstrom`: Angstrom
    - `bond_energy_kJ_per_mol`: kJ/mol

Notes: All values are derived from DFT calculations. The hidden checker uses tolerances appropriate for a re-run with a different open-source DFT code, as the original paper used VASP. Density-of-states curves and bond-strength analysis are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "clean_surface_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "termination",
          "surface_energy_J_per_m2",
          "work_function_eV"
        ],
        "units": {
          "surface_energy_J_per_m2": "J/m^2",
          "work_function_eV": "eV"
        }
      },
      "description": "Computed surface energy and work function for each clean surface; compared against paper reference values within hidden tolerances."
    },
    {
      "file": "adsorption_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "adsorption_site",
          "adsorption_energy_eV",
          "work_function_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV",
          "work_function_eV": "eV"
        }
      },
      "description": "Computed adsorption energy and work function for each stable Cl adsorption site; compared against paper reference values within hidden tolerances."
    },
    {
      "file": "dimer_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dimer",
          "bond_length_angstrom",
          "bond_energy_kJ_per_mol"
        ],
        "units": {
          "bond_length_angstrom": "Angstrom",
          "bond_energy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "Equilibrium bond length and bond energy for Mg-Cl and Ca-Cl dimers; compared against paper reference values within hidden tolerances."
    }
  ],
  "notes": "All values are derived from DFT calculations. The hidden checker uses tolerances appropriate for a re-run with a different open-source DFT code, as the original paper used VASP. Density-of-states curves and bond-strength analysis are not scored."
}
```

## How you are scored
A hidden verifier compares each quantitative entry in your three scored CSV files (clean_surface_properties.csv, adsorption_properties.csv, dimer_properties.csv) against independently determined reference values. The comparison uses physical tolerances that account for the expected spread when using a different DFT code, functional implementation, or pseudopotential set. For each quantity, if your computed value falls within the acceptable tolerance band around the reference, that entry scores one point. The overall reward is the fraction of entries that pass, so reporting the paper's numbers verbatim without actually performing the DFT calculations will not yield full credit—the verifier checks physical consistency, not exact reproduction of the original data. No single piece of helper or intermediate evidence carries separate weight; only the correctness of the final tables determines your score.
