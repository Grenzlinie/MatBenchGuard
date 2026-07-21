# DFT Calibration of Fermi Level Shift vs Electron Doping in Monolayer HfTe₂

## Problem background
Epitaxial monolayers of HfTe₂ have been shown to exhibit a Dirac-like band structure. Substrate-induced electron doping can shift the Fermi level of the monolayer, potentially bringing the Dirac point closer to the Fermi energy and enabling access to its unique electronic properties. To quantify the relationship between substrate electron doping and the observed Fermi level shift, it is necessary to perform first-principles electronic structure calculations on a freestanding monolayer. Density functional theory (DFT) is used to compute the Fermi energy as a function of added electron surface density, providing a calibration curve that links the amount of doping to the resulting Fermi shift. This task aims to compute that calibration table, which serves as the quantitative bridge between ARPES-observed shifts and the underlying doping density.

## Approach
The method is based on plane-wave DFT using the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional. The system is a freestanding monolayer of HfTe₂ with an in-plane lattice constant of 3.967 Å and a vacuum spacing of at least 20 Å to avoid spurious interactions between periodic images. A dense k-point grid of 30 × 30 × 1 is used to sample the Brillouin zone.

To guarantee reproducibility and agreement with the hidden reference data, the following **mandatory computational parameters** must be used:

- **Plane-wave cutoffs**:
  - Wavefunction cutoff (ecutwfc): 60 Ry
  - Density cutoff (ecutrho): 480 Ry
- **Pseudopotentials** (PAW, PBE functional, from PSLibrary 1.0.0, available at pseudodojo.org):
  - Hafnium: `Hf.pbe-spn-kjpaw_psl.1.0.0.UPF`
  - Tellurium: `Te.pbe-n-kjpaw_psl.1.0.0.UPF`
  Download URLs:
    - http://pseudodojo.org/pseudopotentials/Hf.pbe-spn-kjpaw_psl.1.0.0.UPF
    - http://pseudodojo.org/pseudopotentials/Te.pbe-n-kjpaw_psl.1.0.0.UPF
- **Occupation scheme**: Methfessel-Paxton smearing with a broadening of 0.01 Ry.
- **Charge handling for doping**: Extra electrons are added to the unit cell using a background charge compensation (homogeneous jellium background). For a desired added electron surface density **n₂D** (electrons/cm²), the number of extra electrons per unit cell is calculated as:

  \[
  N_{\text{extra}} = n_{\text{2D}} \times A_{\text{cell}}
  \]

  where \(A_{\text{cell}}\) is the in-plane area of the unit cell in cm²:

  \[
  A_{\text{cell}} = a^2 \sin(60^\circ) = (3.967 \times 10^{-8}\,\text{cm})^2 \times \frac{\sqrt{3}}{2}
                 \approx 1.364 \times 10^{-15}\,\text{cm}^2
  \]

  Therefore, \(N_{\text{extra}} = n_{\text{2D}} \times 1.364 \times 10^{-15}\) (dimensionless).  
  In Quantum ESPRESSO, this is set via `tot_charge = N_extra` (total extra electrons).  
  Example: for \(n_{\text{2D}} = 1.0 \times 10^{13}\) e/cm², \(N_{\text{extra}} \approx +0.01364\).  
  **Note**: The neutral (undoped) calculation corresponds to `tot_charge = 0.0`.

For each doping level, perform a self-consistent calculation and extract the Fermi energy. The Fermi shift is defined as the Fermi energy of the doped system minus the Fermi energy of the neutral system.

## Crystal structure
The freestanding monolayer HfTe₂ adopts the 1T phase (CdI₂-type) with a hexagonal lattice. Use the following unit cell:

- Lattice parameters: a = b = 3.967 Å, c = 20.0 Å (α = β = 90°, γ = 120°).
- Atomic positions (fractional coordinates):
  - Hf: (0.000, 0.000, 0.500)
  - Te: (0.667, 0.333, 0.580)
  - Te: (0.333, 0.667, 0.420)

These positions place the monolayer at the center of the cell and provide >20 Å vacuum along the c direction. The corresponding lattice vectors (in Å) are:
a1 = (3.967, 0, 0), a2 = (−1.9835, 3.435, 0), a3 = (0, 0, 20).

## Reproduction target
Produce a CSV file (`doping_calibration.csv`) containing at least five data points that map the added electron surface density (in electrons/cm²) to the resulting Fermi energy shift (in eV) relative to the neutral monolayer. The table should cover a range of densities sufficient to include Fermi shifts from zero up to at least about 0.5 eV. The calibration CSV must have a header row with the exact column names `density (electrons/cm^2)` and `fermi_shift (eV)`. This table is the only scored artifact; it will be used downstream to derive doping densities that correspond to specific experimentally observed Fermi shifts, but you do not need to compute those derived densities yourself — only the calibration table is required.

## Assets

- Plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE pseudopotentials for Hf and Te:  
  - http://pseudodojo.org/pseudopotentials/Hf.pbe-spn-kjpaw_psl.1.0.0.UPF  
  - http://pseudodojo.org/pseudopotentials/Te.pbe-n-kjpaw_psl.1.0.0.UPF

## Workflow steps

### Step 1: Prepare the neutral calculation
- Role: process
- Action: Set up a self-consistent DFT calculation for the neutral monolayer HfTe₂ using the structure, pseudopotentials, cutoffs, k‑point grid, and smearing described above. Set `tot_charge = 0.0`. Run the calculation and record the Fermi energy \(E_F^{(0)}\).

### Step 2: Run DFT calculations for doped systems
- Role: process
- Action: Choose several added electron surface densities that cover the range from zero up to a density that yields a Fermi shift of at least about 0.5 eV. You must evaluate at least five distinct densities. For each density, calculate the corresponding `tot_charge` using the formula above and run the self-consistent calculation. Extract the Fermi energy \(E_F(n_{\text{2D}})\). The Fermi shift is \(\Delta E_F = E_F(n_{\text{2D}}) - E_F^{(0)}\).

### Step 3: Produce calibration CSV
- Role: scored (load-bearing)
- Action: Compile the results into a CSV table with columns `density (electrons/cm^2)` and `fermi_shift (eV)`. The density column must contain the surface densities in electrons/cm² (floating-point numbers), and the Fermi shift column must contain the computed Fermi shifts in eV.
- Output file: `/app/outputs/doping_calibration.csv`
- Format: csv
- Contract: Two columns: `density (electrons/cm^2)` (float) and `fermi_shift (eV)` (float). Header row required. At least 5 data rows. The Fermi shift must be non-decreasing (monotonically increasing) with doping density.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/doping_calibration.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### doping_calibration.csv
- path: `/app/outputs/doping_calibration.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Calibration table relating added electron surface density (electrons/cm²) to Fermi energy shift (eV). The checker will interpolate from this table to derive the densities corresponding to specific hidden Fermi shift values and compare them to hidden paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `density (electrons/cm^2)`, `fermi_shift (eV)`

Notes: The agent must not include the derived doping densities in this file; the checker does its own interpolation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "doping_calibration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "density (electrons/cm^2)",
          "fermi_shift (eV)"
        ]
      },
      "description": "Calibration table relating added electron surface density (electrons/cm²) to Fermi energy shift (eV). The checker will interpolate from this table to derive the densities corresponding to specific hidden Fermi shift values and compare them to hidden paper-reported values."
    }
  ],
  "notes": "The agent must not include the derived doping densities in this file; the checker does its own interpolation."
}
```

## How you are scored
A hidden verifier will score your calibration CSV based on two groups of checks. First, a structural audit ensures that the file is a valid CSV with the required columns, contains at least five data rows, and that the Fermi shift is non-decreasing with increasing doping density. Second, the verifier will interpolate the data points you provide to find the doping densities that correspond to two specific Fermi shift values (these values are hidden and you do not need to know them). Each derived density is compared to a hidden reference value that was reported in the original work. The comparison uses a relative tolerance; densities that fall within the tolerance band earn full credit. The final reward is a weighted combination of the structural audit and the accuracy of the derived densities. Merely reporting numbers that look plausible is not enough — the verifier checks whether your DFT-calibrated table actually reproduces the correct doping-Fermi shift relationship.