# Computation of Magnetic Exchange Coupling, Curie Temperature, and Electronic Properties in 2D XCrY2 Monolayers

## Problem background
Two-dimensional intrinsic ferromagnetic semiconductors are highly sought after for spintronic devices because they couple charge and spin degrees of freedom. Only a handful of such materials with high Curie temperatures have been identified. This task investigates a family of monolayer alkali-based chromium chalcogenides (XCrY2 with X=Li,Na and Y=S,Se,Te) predicted from first-principles calculations to be intrinsic ferromagnetic semiconductors. The agent will compute the key physical properties that determine their magnetic and electronic behaviour, including the spin-exchange coupling, Curie temperature, band-gap type and magnitude, carrier mobility, magnetic anisotropy, and electrostatic potential asymmetry.

## Approach
The reproduction follows a first-principles workflow. Density functional theory (DFT) calculations with a Hubbard‑U correction and with a hybrid functional (HSE06) are used to obtain the electronic structure and total energies of the monolayer crystals. By comparing ferromagnetic and antiferromagnetic configurations in supercells, the magnetic exchange energy is extracted and mapped onto an effective two‑dimensional Ising model to obtain the nearest‑neighbour exchange coupling J. Monte Carlo simulations on a triangular lattice with that J and the computed magnetocrystalline anisotropy (obtained from spin‑orbit‑coupled total energies) estimate the Curie temperature under both Ising and Heisenberg descriptions. Hybrid‑functional band structures (with and without spin‑orbit coupling) give the band gaps, the direct/indirect character, and the effective masses. For the sodium‑based compounds, strained‑cell DFT calculations supply the deformation potentials and elastic moduli needed to evaluate carrier mobilities via the deformation‑potential model at 300 K. Finally, the planar‑averaged electrostatic potential provides the potential difference between the two surfaces of each monolayer.

## Reproduction target
Compute, for all six XCrY2 monolayers, the following quantities: lattice constant after optimization with PBE+U and with HSE06; nearest‑neighbour exchange coupling J (meV); HSE06 band gap without and with spin‑orbit coupling (eV) and whether the gap is direct or indirect; Curie temperature (K) from both the Ising and the Heisenberg Monte Carlo models; magnetocrystalline anisotropy energy MAE (meV); and electrostatic potential difference ΔV (eV) between the upper and lower surfaces. For the three Na‑based compounds (NaCrS2, NaCrSe2, NaCrTe2) also compute, separately for armchair and zigzag directions, the electron and hole effective masses (in units of m0), deformation potentials (eV), two‑dimensional elastic modulus (J/m²), and the resulting carrier mobilities (cm²/V·s) at 300 K. Assemble all results into the single CSV file /app/outputs/computed_properties.csv following the column specification given in the output contract.

## Assets

- DFT code (VASP or open-source equivalent like Quantum ESPRESSO): https://www.quantum-espresso.org
- Pseudopotentials (PAW) for Li, Na, Cr, S, Se, Te
- Python 3 with numpy, pandas, matplotlib: https://pypi.org/
- Monte Carlo simulation code for 2D Ising/Heisenberg model

## Workflow steps

### Step 1: Build Monolayer Structures
- Role: process
- Action: Construct the four-layer hexagonal unit cells for all six XCrY₂ (X=Li,Na; Y=S,Se,Te) monolayers using the literature crystal structure (triangular Cr lattice, asymmetric chalcogen surfaces) and the lattice constants. Generate input files for the chosen DFT code.
- Evidence: none

### Step 2: Geometry Optimization
- Role: process
- Action: Perform geometry optimization of the monolayer structures using PBE+U and HSE06 functionals to obtain relaxed lattice constants and atomic positions. Retain the relaxed geometries for all subsequent calculations.
- Evidence: none

### Step 3: Magnetic Ground State and Exchange Energy
- Role: process
- Action: Build a p(2×2) supercell from the relaxed primitive cell for each compound. Compute total energies of collinear FM and AFM configurations using PBE+U and HSE06. Confirm the FM ground state and record the magnetic moment per unit cell. Compute the exchange energy E_ex = E_AFM - E_FM.
- Evidence: none

### Step 4: Extract Nearest-Neighbor Exchange Coupling J
- Role: process
- Action: Map the total-energy differences between FM and AFM states in the p(2×2) supercell to the effective nearest-neighbor 2D Ising Hamiltonian. Solve for the nearest-neighbor exchange coupling parameter J (in meV) for each compound.
- Evidence: none

### Step 5: Calculate Magnetocrystalline Anisotropy Energy
- Role: process
- Action: For each compound, perform HSE06+spin-orbit coupling total energy calculations with magnetization oriented in-plane and out-of-plane. Compute the magnetocrystalline anisotropy energy MAE = E_in-plane - E_out-of-plane (meV per unit cell).
- Evidence: none

### Step 6: Monte Carlo Simulation of Curie Temperature
- Role: process
- Action: Using the extracted J, MAE (as single-ion anisotropy for the Heisenberg model), and spin S=3/2, perform Monte Carlo simulations on a triangular lattice for both the Ising and Heisenberg models to estimate the Curie temperature Tc for each compound. Record convergence evidence (warm-up steps, total steps, final magnetization near Tc) in an evidence file.
- Evidence: `/app/outputs/mc_convergence_log.txt`

### Step 7: HSE06 Band Structure Calculations
- Role: process
- Action: Compute HSE06 band structures for each compound without and with spin-orbit coupling. Determine band gaps (eV) and whether the gap is direct or indirect. Save raw band structure data in a compressed archive for reproducibility.
- Evidence: `/app/outputs/band_structure_data.zip`

### Step 8: Carrier Mobility Calculation (Na-based only)
- Role: process
- Action: For NaCrS₂, NaCrSe₂, NaCrTe₂: extract electron and hole effective masses from HSE06 band structures (armchair and zigzag directions). Perform strained DFT calculations to obtain deformation potentials and 2D elastic modulus. Apply the deformation potential model at 300 K to compute electron and hole carrier mobilities (cm²/V·s).
- Evidence: none

### Step 9: Electrostatic Potential Difference ΔV
- Role: process
- Action: Compute the planar-averaged electrostatic potential for each relaxed monolayer and extract the potential difference ΔV (eV) between the upper and lower surfaces.
- Evidence: none

### Step 10: Assemble Final Computed Properties
- Role: scored (load-bearing)
- Action: Compile all computed quantities into a single CSV file with the columns specified in the output contract. Ensure units match: lattice constants in Å, J in meV, band gaps in eV, Tc in K, MAE in meV, ΔV in eV, mobilities in cm²/V·s, effective masses in m₀, deformation potential in eV, elastic modulus in J/m². Missing values (e.g., mobilities for Li-based compounds) are left blank.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: Columns: compound, a_PBE_U (Å), a_HSE (Å), J (meV), Eg_without_SOC (eV), Eg_with_SOC (eV), direct_indirect (string: 'direct' or 'indirect'), Tc_Ising (K), Tc_Heisenberg (K), MAE (meV), ΔV (eV), m_e_x (m0), m_e_y (m0), m_h_x (m0), m_h_y (m0), E1e_x (eV), E1e_y (eV), E1h_x (eV), E1h_y (eV), C_2D_x (J/m²), C_2D_y (J/m²), μ_e_x (cm²/V·s), μ_e_y (cm²/V·s), μ_h_x (cm²/V·s), μ_h_y (cm²/V·s). Rows: LiCrS2, LiCrSe2, LiCrTe2, NaCrS2, NaCrSe2, NaCrTe2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Assembled CSV with one row per compound (LiCrS2, LiCrSe2, LiCrTe2, NaCrS2, NaCrSe2, NaCrTe2) containing all computed properties. Numerical values must use the indicated units; string column 'direct_indirect' must be 'direct' or 'indirect'. Mobility-related columns for Li-based compounds are left empty. The CSV is compared to the paper-reported reference values with an appropriate tolerance; correctness is measured by closeness of each numeric field to the expected gold.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a_PBE_U`, `a_HSE`, `J`, `Eg_without_SOC`, `Eg_with_SOC`, `direct_indirect`, `Tc_Ising`, `Tc_Heisenberg`, `MAE`, `ΔV`, `m_e_x`, `m_e_y`, `m_h_x`, `m_h_y`, `E1e_x`, `E1e_y`, `E1h_x`, `E1h_y`, `C_2D_x`, `C_2D_y`, `μ_e_x`, `μ_e_y`, `μ_h_x`, `μ_h_y`
  - `units`:
    - `a_PBE_U`: Å
    - `a_HSE`: Å
    - `J`: meV
    - `Eg_without_SOC`: eV
    - `Eg_with_SOC`: eV
    - `direct_indirect`: string ('direct' or 'indirect')
    - `Tc_Ising`: K
    - `Tc_Heisenberg`: K
    - `MAE`: meV
    - `ΔV`: eV
    - `m_e_x`: m0
    - `m_e_y`: m0
    - `m_h_x`: m0
    - `m_h_y`: m0
    - `E1e_x`: eV
    - `E1e_y`: eV
    - `E1h_x`: eV
    - `E1h_y`: eV
    - `C_2D_x`: J/m²
    - `C_2D_y`: J/m²
    - `μ_e_x`: cm²/V·s
    - `μ_e_y`: cm²/V·s
    - `μ_h_x`: cm²/V·s
    - `μ_h_y`: cm²/V·s

Notes: Only computed_properties.csv is scored. The evidence files (mc_convergence_log.txt and band_structure_data.zip) are required process evidence but not directly scored; their presence may be used as a structural sanity check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a_PBE_U",
          "a_HSE",
          "J",
          "Eg_without_SOC",
          "Eg_with_SOC",
          "direct_indirect",
          "Tc_Ising",
          "Tc_Heisenberg",
          "MAE",
          "ΔV",
          "m_e_x",
          "m_e_y",
          "m_h_x",
          "m_h_y",
          "E1e_x",
          "E1e_y",
          "E1h_x",
          "E1h_y",
          "C_2D_x",
          "C_2D_y",
          "μ_e_x",
          "μ_e_y",
          "μ_h_x",
          "μ_h_y"
        ],
        "units": {
          "a_PBE_U": "Å",
          "a_HSE": "Å",
          "J": "meV",
          "Eg_without_SOC": "eV",
          "Eg_with_SOC": "eV",
          "direct_indirect": "string ('direct' or 'indirect')",
          "Tc_Ising": "K",
          "Tc_Heisenberg": "K",
          "MAE": "meV",
          "ΔV": "eV",
          "m_e_x": "m0",
          "m_e_y": "m0",
          "m_h_x": "m0",
          "m_h_y": "m0",
          "E1e_x": "eV",
          "E1e_y": "eV",
          "E1h_x": "eV",
          "E1h_y": "eV",
          "C_2D_x": "J/m²",
          "C_2D_y": "J/m²",
          "μ_e_x": "cm²/V·s",
          "μ_e_y": "cm²/V·s",
          "μ_h_x": "cm²/V·s",
          "μ_h_y": "cm²/V·s"
        }
      },
      "description": "Assembled CSV with one row per compound (LiCrS2, LiCrSe2, LiCrTe2, NaCrS2, NaCrSe2, NaCrTe2) containing all computed properties. Numerical values must use the indicated units; string column 'direct_indirect' must be 'direct' or 'indirect'. Mobility-related columns for Li-based compounds are left empty. The CSV is compared to the paper-reported reference values with an appropriate tolerance; correctness is measured by closeness of each numeric field to the expected gold."
    }
  ],
  "notes": "Only computed_properties.csv is scored. The evidence files (mc_convergence_log.txt and band_structure_data.zip) are required process evidence but not directly scored; their presence may be used as a structural sanity check."
}
```

## How you are scored
A hidden verifier reads the assembled CSV and compares each numeric field to reference values (derived from the original study) with tolerances that account for the natural spread introduced by different computational implementations (choice of DFT code, pseudopotentials, Monte Carlo realization). Fields that fall within the tolerance earn full credit; credit decays smoothly for larger deviations. The verifier also checks structural consistency: the direct/indirect band‑gap classification must match the known character of each compound, and the relative ordering of exchange couplings across the six compounds should follow a physically motivated trend. No credit is given for simply reporting numbers lifted from a paper; the workflow steps must be executed genuinely to produce the CSV. The final reward is a weighted combination of per‑field and per‑compound scores, with the largest weight on the main physical properties (J, Tc, band gaps, MAE, mobilities).
