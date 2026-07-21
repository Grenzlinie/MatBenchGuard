# DFT Study of Cs-NF3 Co-Adsorption on GaAs(100) Surface

## Problem background
NEA GaAs photocathodes, central to night vision and spin‑polarized electron sources, are commonly activated with Cs and NF₃ to achieve better stability than Cs/O₂. The atomic‑scale mechanism of Cs–NF₃ co‑adsorption on the As‑terminated GaAs(100)-β2(2×4) reconstructed surface — the most stable and widely studied GaAs(100) phase — remains poorly understood. In particular, it is unknown how the vertical order of the Cs and NF₃ adsorbates (Cs above vs. below NF₃) and the adsorption site affect surface energetics, charge redistribution, and the formation of surface dipoles that lower the work function. A quantitative, first‑principles understanding of these factors is essential for rational optimization of the activation process.

## Approach
A slab model of the Zn‑doped GaAs(100)-β2(2×4) surface with a 15 Å vacuum gap is constructed and its geometry relaxed using plane‑wave DFT with the PBE functional, a Tkatchenko–Scheffler van der Waals correction, ultra‑soft pseudopotentials, and well‑converged numerical settings. Isolated Cs and NF₃ reference energies and charge densities are computed in the same functional setup. For five high‑symmetry adsorption sites (H′, T3, T3′, T4, T4′) and both vertical orderings (Cs‑up and NF₃‑up), co‑adsorption configurations are built and fully relaxed. From the converged structures, the adsorption energy is obtained from total‑energy differences. The work function is extracted from the electrostatic potential across the slab. Mulliken population analysis provides atomic charges, while the charge‑density‑difference method of Hogan et al. yields quantitative dipole descriptors: the average dipole length d_z, the magnitude of separated charge |Q±|, and the surface dipole moment P_z = |Q±|·d_z. Geometric parameters (bilayer thicknesses, inter‑layer spacing, and Cs–NF₃ distance) are measured directly from the relaxed coordinates. Comparing these quantities across sites and orientations reveals how the vertical order controls charge transfer and dipole strength.

## Reproduction target
Using an open‑source DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials, perform the geometry optimizations and electronic‑structure analyses described above for all five adsorption sites in both Cs‑up and NF₃‑up configurations. Produce the four output files:
- `adsorption_workfunction.csv`: adsorption energy E_ads (eV), work function Φ (eV), and change ΔΦ (eV) relative to the clean surface for each configuration.
- `mulliken_charges.csv`: averaged Mulliken charges (e) for the first‑ and second‑bilayer As and Ga, the Cs atom, and the NF₃ molecule.
- `dipole_descriptors.csv`: average dipole length d_z (Å), charge magnitude |Q±| (e), and surface dipole moment P_z (e·Å).
- `geometric_structure.csv`: bilayer thicknesses D₁ (Å), D₂ (Å), inter‑bilayer spacing D₁₂ (Å), and Cs–NF₃ distance (Å).

## Assets

- Open-source DFT program (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Ultra-soft pseudopotentials for Ga, As, Zn, Cs, N, F (SSSP or equivalent): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Build and optimize clean GaAs(100)-β2(2×4) slab
- Role: process
- Action: Construct the GaAs(100)-β2(2×4) surface slab model containing 28 As atoms, 21 Ga atoms, and 1 Zn dopant, with bottom As dangling bonds passivated by pseudo-hydrogen atoms (charge 0.75 e). Unit cell dimensions: 7.99 Å × 15.99 Å × 22.89 Å with a 15 Å vacuum layer. Perform DFT geometry optimization using the PBE functional, TS van der Waals correction, a 6×3×1 k-point mesh, 400 eV plane-wave cutoff, and BFGS algorithm until forces are below 0.03 eV/Å and energy tolerance 1e-5 eV/atom.
- Evidence: `/app/outputs/clean_slab_optim.log`

### Step 2: Calculate isolated Cs atom and NF3 molecule
- Role: process
- Action: Compute the total energy and electron density (charge density) of an isolated Cs atom and an isolated NF3 molecule in a large vacuum cell, using the same DFT settings (functional, cutoff, k-points, pseudopotentials) as the slab.
- Evidence: `/app/outputs/isolated_species.log`

### Step 3: Optimize Cs-NF3 co-adsorption models across all sites and vertical orders
- Role: process
- Action: For all five selected adsorption sites (H', T3, T3', T4, T4') and both vertical orderings (Cs-up: Cs above NF3; NF3-up: NF3 above Cs), build the co-adsorption configuration on the optimized slab and perform full DFT geometry optimization with the same settings. This yields 10 relaxed structures, their total energies, and charge densities.
- Evidence: `/app/outputs/coadsorption_optimizations.log`

### Step 4: Compute adsorption energies and work functions
- Role: scored (load-bearing)
- Action: From the total energies of the clean slab, isolated Cs/NF3, and each co-adsorbed system, calculate the adsorption energy as E_ads = E_{GaAs:Cs/NF3} - E_{GaAs} - E_{Cs} - E_{NF3}. For each relaxed system, extract the vacuum level from the electrostatic potential and the Fermi level to obtain the work function Φ; compute the change ΔΦ relative to the clean surface. Output a CSV with columns: site, orientation, adsorption_energy_eV, work_function_eV, work_function_change_eV.
- Output file: `/app/outputs/adsorption_workfunction.csv`
- Format: csv
- Contract: CSV with columns: site (str), orientation (str), adsorption_energy_eV (float), work_function_eV (float), work_function_change_eV (float). 10 rows (5 sites × 2 orientations).
- Scoring: scored by hidden verifier

### Step 5: Perform Mulliken charge analysis
- Role: scored (load-bearing)
- Action: For each optimized co-adsorption model, compute Mulliken atomic charges (or the equivalent population analysis available in your DFT code). Average the charges for the specified groups: first-bilayer As, first-bilayer Ga, second-bilayer As, second-bilayer Ga, the Cs atom, and the NF3 molecule. Output a CSV with columns: site, orientation, As_first_bilayer, Ga_first_bilayer, As_second_bilayer, Ga_second_bilayer, Cs, NF3.
- Output file: `/app/outputs/mulliken_charges.csv`
- Format: csv
- Contract: CSV with columns: site (str), orientation (str), As_first_bilayer (float), Ga_first_bilayer (float), As_second_bilayer (float), Ga_second_bilayer (float), Cs (float), NF3 (float). 10 rows.
- Scoring: scored by hidden verifier

### Step 6: Calculate dipole length, charge magnitude, and surface dipole moment
- Role: scored (load-bearing)
- Action: Construct the electron density difference: Δρ(r) = ρ_{Cs} + ρ_{NF3} + ρ_{GaAs} - ρ_{Cs/NF3/GaAs}. Use this to compute total positive and negative charge magnitudes (Q+, Q−) by summing over grid points. Determine the average dipole length d_z using z-coordinate weighted by Δρ (with z=0 at the midpoint of the clean surface). The surface dipole moment is P_z = |Q±| × d_z. Apply the method in Hogan et al. (Eqs. 3–6 of the paper). Output a CSV with columns: site, orientation, dz_Ang, Q_abs_e, Pz_eAng.
- Output file: `/app/outputs/dipole_descriptors.csv`
- Format: csv
- Contract: CSV with columns: site (str), orientation (str), dz_Ang (float), Q_abs_e (float), Pz_eAng (float). 10 rows.
- Scoring: scored by hidden verifier

### Step 7: Extract geometric parameters
- Role: scored (load-bearing)
- Action: From the optimized geometries, measure the following distances: thickness of the first bilayer (D1), thickness of the second bilayer (D2), interlayer spacing between first and second bilayer (D12), and the distance between Cs and NF3 (using the average position of the NF3 atoms). Output a CSV with columns: site, orientation, D1_Ang, D2_Ang, D12_Ang, D_Cs_NF3_Ang.
- Output file: `/app/outputs/geometric_structure.csv`
- Format: csv
- Contract: CSV with columns: site (str), orientation (str), D1_Ang (float), D2_Ang (float), D12_Ang (float), D_Cs_NF3_Ang (float). 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_workfunction.csv`
- `/app/outputs/mulliken_charges.csv`
- `/app/outputs/dipole_descriptors.csv`
- `/app/outputs/geometric_structure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_workfunction.csv
- path: `/app/outputs/adsorption_workfunction.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energy and work function results for the 10 co-adsorption configurations (5 sites × 2 orientations).
- schema:
  - `type`: table
  - `required_columns`: `site`, `orientation`, `adsorption_energy_eV`, `work_function_eV`, `work_function_change_eV`
  - `units`:
    - `adsorption_energy_eV`: eV
    - `work_function_eV`: eV
    - `work_function_change_eV`: eV

### mulliken_charges.csv
- path: `/app/outputs/mulliken_charges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mulliken charge distribution for substrate and adsorbates across the 10 models.
- schema:
  - `type`: table
  - `required_columns`: `site`, `orientation`, `As_first_bilayer`, `Ga_first_bilayer`, `As_second_bilayer`, `Ga_second_bilayer`, `Cs`, `NF3`
  - `units`:
    - `As_first_bilayer`: e
    - `Ga_first_bilayer`: e
    - `As_second_bilayer`: e
    - `Ga_second_bilayer`: e
    - `Cs`: e
    - `NF3`: e

### dipole_descriptors.csv
- path: `/app/outputs/dipole_descriptors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dipole descriptors d_z, |Q±|, and P_z derived from charge density difference analysis.
- schema:
  - `type`: table
  - `required_columns`: `site`, `orientation`, `dz_Ang`, `Q_abs_e`, `Pz_eAng`
  - `units`:
    - `dz_Ang`: Ang
    - `Q_abs_e`: e
    - `Pz_eAng`: e*Ang

### geometric_structure.csv
- path: `/app/outputs/geometric_structure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface geometric parameters (layer thicknesses and adsorbate distance) from the optimized structures.
- schema:
  - `type`: table
  - `required_columns`: `site`, `orientation`, `D1_Ang`, `D2_Ang`, `D12_Ang`, `D_Cs_NF3_Ang`
  - `units`:
    - `D1_Ang`: Ang
    - `D2_Ang`: Ang
    - `D12_Ang`: Ang
    - `D_Cs_NF3_Ang`: Ang

Notes: All outputs are compared to the corresponding paper-reported values using appropriate tolerances (absorption of method differences between CASTEP and the chosen open-source DFT code). In addition to direct value comparison, the checker verifies key trends: Cs-up models yield lower (more negative) adsorption energy and larger work function reduction than NF3-up models; NF3 molecule is significantly negatively charged in Cs-up but near neutral in NF3-up; larger dipole moments in Cs-up; and site-specific orderings consistent with the paper's conclusions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_workfunction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "orientation",
          "adsorption_energy_eV",
          "work_function_eV",
          "work_function_change_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV",
          "work_function_eV": "eV",
          "work_function_change_eV": "eV"
        }
      },
      "description": "Adsorption energy and work function results for the 10 co-adsorption configurations (5 sites × 2 orientations)."
    },
    {
      "file": "mulliken_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "orientation",
          "As_first_bilayer",
          "Ga_first_bilayer",
          "As_second_bilayer",
          "Ga_second_bilayer",
          "Cs",
          "NF3"
        ],
        "units": {
          "As_first_bilayer": "e",
          "Ga_first_bilayer": "e",
          "As_second_bilayer": "e",
          "Ga_second_bilayer": "e",
          "Cs": "e",
          "NF3": "e"
        }
      },
      "description": "Mulliken charge distribution for substrate and adsorbates across the 10 models."
    },
    {
      "file": "dipole_descriptors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "orientation",
          "dz_Ang",
          "Q_abs_e",
          "Pz_eAng"
        ],
        "units": {
          "dz_Ang": "Ang",
          "Q_abs_e": "e",
          "Pz_eAng": "e*Ang"
        }
      },
      "description": "Dipole descriptors d_z, |Q±|, and P_z derived from charge density difference analysis."
    },
    {
      "file": "geometric_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "orientation",
          "D1_Ang",
          "D2_Ang",
          "D12_Ang",
          "D_Cs_NF3_Ang"
        ],
        "units": {
          "D1_Ang": "Ang",
          "D2_Ang": "Ang",
          "D12_Ang": "Ang",
          "D_Cs_NF3_Ang": "Ang"
        }
      },
      "description": "Surface geometric parameters (layer thicknesses and adsorbate distance) from the optimized structures."
    }
  ],
  "notes": "All outputs are compared to the corresponding paper-reported values using appropriate tolerances (absorption of method differences between CASTEP and the chosen open-source DFT code). In addition to direct value comparison, the checker verifies key trends: Cs-up models yield lower (more negative) adsorption energy and larger work function reduction than NF3-up models; NF3 molecule is significantly negatively charged in Cs-up but near neutral in NF3-up; larger dipole moments in Cs-up; and site-specific orderings consistent with the paper's conclusions."
}
```

## How you are scored
Each of the four output files is evaluated independently by a hidden verifier. The verifier compares your reported numerical values to reference values (the corresponding computed quantities from the published study) with predefined tolerances that account for method‑dependent differences between DFT codes. In addition, the verifier checks that the qualitative physical trends among the configurations (e.g., relative ordering of adsorption energies and dipole moments across sites and orientations, charge distribution patterns) are internally consistent and match the expected physical picture. The final reward is a weighted sum of the scores from the four artifacts, where each artifact carries a substantial share of the total weight.
