# DFT investigation of interface metallicity and defect effects in LaGaO3/SrTiO3

## Problem background
The interface between the two perovskite band insulators LaGaO3 (LGO) and SrTiO3 (STO) can host a metallic two-dimensional electron gas (2DEG) despite both bulk materials being insulating. This formation of interfacial metallic states has attracted strong interest for oxide electronics, including field-effect devices and superconductivity. The electronic structure of the LGO/STO interface—particularly the differences between n-type (electron-doped) and p-type (hole-doped) terminations, and the influence of oxygen vacancies—remains to be clarified by first-principles calculations. This task aims to compute the key electronic properties of these interfaces using density functional theory (DFT).

## Approach
This task employs plane-wave density functional theory (DFT) with an open-source code such as Quantum ESPRESSO and suitable pseudopotentials. The interface is modeled using a supercell containing 4 unit cells of LGO stacked on 8 unit cells of STO along the [001] direction, with an average in-plane lattice constant of 3.884 Å. Two interface terminations are considered: an n-type interface (LaO / TiO2) and a p-type interface (GaO2 / SrO).

First, the atomic positions in both supercells are relaxed by force minimization using the generalized gradient approximation (GGA). Using the relaxed structures, the electronic density of states (DOS) is then computed with the local density approximation (LDA). From these calculations, we extract the total DOS, the orbital-resolved Ti 3d projected DOS for the n-type interface, and the total and partial DOS (O 2p and Ti 3d) for the p-type interface.

To characterize the spatial confinement of the 2DEG, the layer-resolved charge density or DOS perpendicular to the interface is analysed and the thickness of the 2DEG on the STO side is determined.

Finally, the effect of oxygen deficiency is studied by creating supercells with 25% and 50% oxygen vacancies in the interfacial TiO2 layer (for the n-type case) and in the interfacial SrO layer (for the p-type case). The electronic structures of all vacancy configurations are computed and compared. All steps are carried out sequentially; the intermediate structures and wavefunctions need not be saved as separate outputs, but the final quantitative data must be written to the specified output files.

## Reproduction target
The goal is to produce five scored artifacts by performing DFT calculations on the LGO/STO interfaces:

1. **n-type total DOS** (`ntype_dos.csv`) – the total density of states vs. energy for the fully relaxed n-type interface. The data must allow a test for metallicity (finite DOS at the Fermi level).
2. **n-type Ti 3d orbital PDOS** (`ntype_pdos_ti.csv`) – the projections onto the Ti 3d sublevels d_xy, d_xz,yz, d_3z2−r2, and d_x2−y2 for the same n-type interface. The agent must resolve the relative occupation of these orbitals near the Fermi energy.
3. **p-type total and partial DOS** (`ptype_dos.csv`) – the total DOS, the O 2p partial DOS, and the Ti 3d partial DOS for the relaxed p-type interface. The aim is to see which atomic species dominates the metallic states.
4. **n-type 2DEG spatial extent** (`n_type_spatial_extent.txt`) – a single floating-point number (in Å) giving the thickness of the 2DEG on the STO side, extracted from the layer-resolved charge/DOS.
5. **Vacancy effects** (`vacancy_effects.txt`) – a structured text summary covering all four vacancy configurations (n-type 25%, n-type 50%, p-type 25%, p-type 50%). For each case, report whether the interface is metallic and which orbital character (Ti 3d or O 2p) carries the conductivity at the Fermi level, along with any notable trends.

The computations must use the LDA functional for the electronic structure and GGA for the relaxation, consistent with the described supercells and lattice constant. The obtained quantitative data will be compared against hidden reference benchmarks; the task does NOT require matching any particular previously published number.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (e.g., SSSP efficiency library): https://www.materialscloud.org/discover/sssp/
- Bulk crystal structures of LaGaO3 and SrTiO3

## Workflow steps

### Step 1: Construct supercells
- Role: process
- Action: Construct the n-type (LaO/TiO2) and p-type (GaO2/SrO) LGO/STO supercells using an average lattice constant of 3.884 Å, with 4 LGO and 8 STO layers along the (0,0,1) direction. Generate input files for DFT.
- Evidence: none

### Step 2: Structural optimization
- Role: process
- Action: Perform DFT structural optimization for both n-type and p-type supercells using GGA functional, minimizing forces until convergence.
- Evidence: none

### Step 3: N-type interface total DOS
- Role: scored
- Action: Compute total density of states at the fully relaxed n-type LGO/STO interface using LDA functional. Write ntype_dos.csv with columns energy(eV) and dos(arb. units).
- Output file: `/app/outputs/ntype_dos.csv`
- Format: csv
- Contract: energy(eV), dos(arb. units)
- Scoring: scored by hidden verifier

### Step 4: N-type interface orbitally resolved PDOS
- Role: scored
- Action: Compute projected density of states for Ti 3d sublevels at the relaxed n-type interface using LDA. Write ntype_pdos_ti.csv with columns energy(eV), d_xy(arb.), d_xz_yz(arb.), d_3z2_r2(arb.), d_x2_y2(arb.).
- Output file: `/app/outputs/ntype_pdos_ti.csv`
- Format: csv
- Contract: energy(eV), d_xy(arb.), d_xz_yz(arb.), d_3z2_r2(arb.), d_x2_y2(arb.)
- Scoring: scored by hidden verifier

### Step 5: P-type interface DOS
- Role: scored
- Action: Compute total and partial DOS at the fully relaxed p-type (GaO2/SrO) interface. Write ptype_dos.csv with columns energy(eV), total_dos(arb.), O_2p_dos(arb.), Ti_3d_dos(arb.).
- Output file: `/app/outputs/ptype_dos.csv`
- Format: csv
- Contract: energy(eV), total_dos(arb.), O_2p_dos(arb.), Ti_3d_dos(arb.)
- Scoring: scored by hidden verifier

### Step 6: n-type 2DEG spatial extent
- Role: scored
- Action: From the relaxed n-type interface calculation, extract the layer-resolved charge density or DOS perpendicular to the interface and determine the thickness of the 2DEG on the STO side. Write a single float (in Ångströms) to n_type_spatial_extent.txt.
- Output file: `/app/outputs/n_type_spatial_extent.txt`
- Format: txt
- Contract: Single float value (Angstroms).
- Scoring: scored by hidden verifier

### Step 7: Oxygen vacancy effects
- Role: scored
- Action: Create supercells with 25% and 50% O vacancies in the interfacial TiO2 layer (n-type) and SrO layer (p-type). Perform DFT electronic structure calculations for each vacancy configuration. Write a text file vacancy_effects.txt summarizing for each case: whether the interface is metallic, the dominant orbital character at EF (Ti 3d or O 2p), and any notable trends.
- Output file: `/app/outputs/vacancy_effects.txt`
- Format: txt
- Contract: Text with clear labels for each vacancy case (n-type 25%, n-type 50%, p-type 25%, p-type 50%).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ntype_dos.csv`
- `/app/outputs/ntype_pdos_ti.csv`
- `/app/outputs/ptype_dos.csv`
- `/app/outputs/n_type_spatial_extent.txt`
- `/app/outputs/vacancy_effects.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ntype_dos.csv
- path: `/app/outputs/ntype_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total DOS for the n-type interface; checker will verify finite DOS at Fermi level (metallicity).
- schema:
  - `type`: table
  - `required_columns`: `energy`, `dos`
  - `units`:
    - `energy`: eV
    - `dos`: arbitrary units

### ntype_pdos_ti.csv
- path: `/app/outputs/ntype_pdos_ti.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Orbitally resolved Ti 3d PDOS; checker will confirm d_xy and d_xz,yz are occupied at EF while d_3z2-r2 and d_x2-y2 are empty, and d_xy occupation is larger.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `d_xy`, `d_xz_yz`, `d_3z2_r2`, `d_x2_y2`
  - `units`:
    - `energy`: eV
    - `d_xy`: arbitrary units
    - `d_xz_yz`: arbitrary units
    - `d_3z2_r2`: arbitrary units
    - `d_x2_y2`: arbitrary units

### ptype_dos.csv
- path: `/app/outputs/ptype_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total and partial DOS for the p-type interface; checker will verify metallicity and O 2p dominance at EF with negligible Ti 3d.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `total_dos`, `O_2p_dos`, `Ti_3d_dos`
  - `units`:
    - `energy`: eV
    - `total_dos`: arbitrary units
    - `O_2p_dos`: arbitrary units
    - `Ti_3d_dos`: arbitrary units

### n_type_spatial_extent.txt
- path: `/app/outputs/n_type_spatial_extent.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Spatial extent of the n-type 2DEG on the STO side; checker compares to the paper-reported value within a tolerance.
- schema:
  - `type`: text
  - `description`: Single float number (Ångströms).

### vacancy_effects.txt
- path: `/app/outputs/vacancy_effects.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Textual summary of vacancy effects; checker verifies that all cases are metallic, n-type Ti 3d increased, p-type 25% O 2p-dominated, p-type 50% Ti 3d-dominated.
- schema:
  - `type`: text
  - `description`: Free text with labels for n-type 25%, n-type 50%, p-type 25%, p-type 50%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ntype_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "dos"
        ],
        "units": {
          "energy": "eV",
          "dos": "arbitrary units"
        }
      },
      "description": "Total DOS for the n-type interface; checker will verify finite DOS at Fermi level (metallicity)."
    },
    {
      "file": "ntype_pdos_ti.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "d_xy",
          "d_xz_yz",
          "d_3z2_r2",
          "d_x2_y2"
        ],
        "units": {
          "energy": "eV",
          "d_xy": "arbitrary units",
          "d_xz_yz": "arbitrary units",
          "d_3z2_r2": "arbitrary units",
          "d_x2_y2": "arbitrary units"
        }
      },
      "description": "Orbitally resolved Ti 3d PDOS; checker will confirm d_xy and d_xz,yz are occupied at EF while d_3z2-r2 and d_x2-y2 are empty, and d_xy occupation is larger."
    },
    {
      "file": "ptype_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "total_dos",
          "O_2p_dos",
          "Ti_3d_dos"
        ],
        "units": {
          "energy": "eV",
          "total_dos": "arbitrary units",
          "O_2p_dos": "arbitrary units",
          "Ti_3d_dos": "arbitrary units"
        }
      },
      "description": "Total and partial DOS for the p-type interface; checker will verify metallicity and O 2p dominance at EF with negligible Ti 3d."
    },
    {
      "file": "n_type_spatial_extent.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single float number (Ångströms)."
      },
      "description": "Spatial extent of the n-type 2DEG on the STO side; checker compares to the paper-reported value within a tolerance."
    },
    {
      "file": "vacancy_effects.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Free text with labels for n-type 25%, n-type 50%, p-type 25%, p-type 50%."
      },
      "description": "Textual summary of vacancy effects; checker verifies that all cases are metallic, n-type Ti 3d increased, p-type 25% O 2p-dominated, p-type 50% Ti 3d-dominated."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects each of the five output files listed in the workflow and output contract. The verification checks:
- **Format and structural integrity** – the files must exist, follow the specified format (CSV with the correct column headers, or plain text with the required content), and contain physically meaningful values (energy grids, DOS values, a single floating-point number, and textual labels).
- **Physical consistency checks** – for DOS files, the verifier may test for the presence of a finite DOS at the Fermi level (metallicity) and for the relative contributions of specified orbitals (e.g., whether certain Ti d orbitals are occupied while others are empty, whether O 2p dominates over Ti 3d for a given case).
- **Spatial extent comparison** – the extracted 2DEG thickness for the n-type interface is compared to a hidden reference value (derived from the same computational protocol) within an appropriate tolerance.
- **Vacancy trends** – the textual summary is parsed and cross-checked against expected trends (whether each configuration is metallic and whether the metallic character is carried by Ti 3d or O 2p states).

The reward is a weighted sum of the results from all stages, with the main electronic-structure artifacts (ntype_dos.csv, ntype_pdos_ti.csv, ptype_dos.csv) receiving the highest weight. Simply reporting a number that matches a published value is not sufficient—the verifier evaluates the actual computed data. The exact scoring thresholds and tolerances are hidden.
