# Spin and Charge Disproportionation and Lattice Instability in NdNiO2

## Problem background
The infinite-layer nickelate NdNiO₂ is the parent compound of recently discovered superconductors. Unlike the analogous cuprate CaCuO₂, undoped NdNiO₂ does not order antiferromagnetically (AFM) despite a formal d⁹ configuration. Understanding why the AFM state is avoided is a central question. This work investigates the hypothesis that the AFM phase is intrinsically unstable because a flat Ni band, pinned at the Fermi level, triggers coupled instabilities when the lattice is disturbed. The task is to compute the energetic, magnetic, and charge response of the AFM-ordered NdNiO₂ lattice to small oxygen displacements, and to quantify the resulting anharmonic effects and the splitting of the flat band.

## Approach
We treat the system with spin-polarized density functional theory plus Hubbard U (GGA+U) using an all-electron full-potential linearized augmented plane wave (FLAPW) code. The crystal structure is the infinite-layer P4/mmm lattice with experimental lattice constants (a = 3.92 Å, c = 3.37 Å). To model the AFM state, a √2×√2 supercell is constructed with antialigned Ni and Nd spins. Hubbard U values are applied to the Ni 3d and Nd 4f states.

The approach is a frozen-phonon study: oxygen atoms are displaced according to full-breathing (symmetric inward/outward motion on all oxygens) and half-breathing (alternating motion on neighbouring oxygen sites) patterns for a series of small amplitudes u. For each displacement, a static DFT calculation is performed starting from the undistorted AFM charge density, yielding the total energy, magnetic moments on two inequivalent Ni sites, and atomic sphere charges on those Ni sites.

From these data we construct the energy cost ΔE(u) = E(u) – E(0) and fit it to a polynomial ΔE(u) = A₂ u² + A₃ u³ to extract the harmonic (A₂) and anharmonic (A₃) coefficients. The effective stiffness K(u) = ΔE(u)/u² is derived for small u. Additionally, for one finite displacement (u = 0.03 Å) of the full-breathing mode, the band structure is computed in the flat-band region (k_z = π/c plane) to obtain the energy splitting of the van Hove singularity and the deformation potential D = band splitting / 0.03 Å.

## Reproduction target
You are required to produce three scored artifacts:

1. `energy_moment_charge_data.csv`: a CSV table containing, for each frozen-phonon mode (full-breathing, half-breathing) and each computed displacement, the total energy per formula unit (eV), the magnetic moments of the two inequivalent Ni sites (µB), and their atomic sphere charges (e).
2. `fitted_coefficients.json`: a JSON file containing the fitted harmonic coefficient A₂ (eV/Å²), anharmonic coefficient A₃ (eV/Å³), and their ratio for both breathing modes, obtained from a least-squares fit of the energy data to ΔE(u) = A₂ u² + A₃ u³.
3. `band_splitting.csv`: a CSV file reporting, for the full-breathing mode at u = 0.03 Å, the band splitting (eV) and the deformation potential (eV/Å).

All workflows must be executed and the final files placed under `/app/outputs`.

## Assets

- All-electron full-potential DFT code with GGA+U (e.g., WIEN2K, FLEUR, Elk): http://www.wien2k.at / https://www.flapw.de / https://elk.sourceforge.io
- Crystal structure data for NdNiO2
- Python packages for data fitting (scipy, numpy, pandas): scipy, numpy, pandas

## Workflow steps

### Step 1: Run static AFM GGA+U reference calculation
- Role: process
- Action: Perform a spin-polarized GGA+U DFT calculation for the antiferromagnetic (AFM) state of NdNiO2 using a √2×√2 supercell (lattice constants a=3.92 Å, c=3.37 Å) with antialigned Ni and Nd spins. Use Hubbard U parameters: U_Ni=4.0 eV, J_Ni=0.7 eV; U_Nd=8.0 eV, J_Nd=1.0 eV. Obtain the self-consistent charge density for the undistorted lattice.
- Evidence: `/app/outputs/afm_ref_calc.log`

### Step 2: Run frozen-phonon DFT calculations for breathing and half-breathing modes
- Role: process
- Action: For each displacement amplitude u in a set covering 0.001–0.05 Å (e.g., 0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05 Å) and for both full-breathing (unit cell) and half-breathing (2×2 supercell) oxygen displacement patterns, run a spin-polarized GGA+U DFT calculation starting from the reference AFM charge density. Extract the total energy, magnetic moments on the two inequivalent Ni sites (Ni1, Ni2), and atomic sphere charges on the two Ni sites.
- Evidence: none

### Step 3: Compile frozen-phonon energy, moment, and charge data
- Role: scored (load-bearing)
- Action: Create a CSV file containing for each mode (full-breathing, half-breathing) and each computed displacement the total energy (eV/f.u.), Ni1 magnetic moment (μB), Ni2 magnetic moment (μB), Ni1 charge (e), and Ni2 charge (e).
- Output file: `/app/outputs/energy_moment_charge_data.csv`
- Format: csv
- Contract: CSV with columns: mode (string), displacement (float, Å), energy (float, eV/f.u.), M_Ni1 (float, μB), M_Ni2 (float, μB), Q_Ni1 (float, e), Q_Ni2 (float, e).
- Scoring: scored by hidden verifier

### Step 4: Fit polynomial to energy-displacement data
- Role: scored (load-bearing)
- Action: Using the energy data from the previous step, fit the energy difference ΔE(u)=E(u)-E(0) to a polynomial ΔE(u)=A2 u^2 + A3 u^3 for both breathing and half-breathing modes. Output the harmonic coefficient A2 (eV/Å^2), the anharmonic coefficient A3 (eV/Å^3), and the ratio A3/A2.
- Output file: `/app/outputs/fitted_coefficients.json`
- Format: json
- Contract: JSON object with top-level keys 'breathing' and 'half_breathing'. Each value is an object with keys 'A2' (float), 'A3' (float), and 'A3_to_A2_ratio' (float).
- Scoring: scored by hidden verifier

### Step 5: Compute band splitting at u=0.03 Å for full-breathing mode
- Role: scored (load-bearing)
- Action: Run a DFT band structure calculation for the AFM state with a full-breathing oxygen displacement of u=0.03 Å on the √2×√2 supercell. On the k_z=π/c plane (the flat band region), extract the energy splitting between the two bands arising from the van Hove singularity. Compute the deformation potential as splitting/0.03 Å.
- Output file: `/app/outputs/band_splitting.csv`
- Format: csv
- Contract: CSV with columns: mode (string, e.g., 'full-breathing'), displacement (float, Å, set to 0.03), band_splitting (float, eV), deformation_potential (float, eV/Å). At least one row for displacement=0.03 Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_moment_charge_data.csv`
- `/app/outputs/fitted_coefficients.json`
- `/app/outputs/band_splitting.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_moment_charge_data.csv
- path: `/app/outputs/energy_moment_charge_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw frozen-phonon energy, magnetic moment, and charge data for each mode and displacement. The checker will compute spin disproportionation, charge disproportionation, and stiffness from this file and compare them to hidden gold values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `displacement`, `energy`, `M_Ni1`, `M_Ni2`, `Q_Ni1`, `Q_Ni2`
  - `units`:
    - `displacement`: Å
    - `energy`: eV/f.u.
    - `M_Ni1`: μB
    - `M_Ni2`: μB
    - `Q_Ni1`: e
    - `Q_Ni2`: e

### fitted_coefficients.json
- path: `/app/outputs/fitted_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted harmonic and anharmonic energy coefficients for breathing and half-breathing modes. The checker will refit the energy data from the CSV and compare its own fit to the reported coefficients within tolerance.
- schema:
  - `type`: object
  - `required`: `breathing`, `half_breathing`
  - `items`:
    - `breathing`:
      - `A2`: float (eV/Å^2)
      - `A3`: float (eV/Å^3)
      - `A3_to_A2_ratio`: float
    - `half_breathing`:
      - `A2`: float (eV/Å^2)
      - `A3`: float (eV/Å^3)
      - `A3_to_A2_ratio`: float

### band_splitting.csv
- path: `/app/outputs/band_splitting.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band splitting and deformation potential at u=0.03 Å for the full-breathing mode. The checker will compare the reported deformation potential to a hidden reference value within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `displacement`, `band_splitting`, `deformation_potential`
  - `units`:
    - `displacement`: Å
    - `band_splitting`: eV
    - `deformation_potential`: eV/Å

Notes: The hidden checker will re-derive spin/charge disproportionation and stiffness from the CSV, refit energy coefficients, and compare the reported band splitting to a hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_moment_charge_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "displacement",
          "energy",
          "M_Ni1",
          "M_Ni2",
          "Q_Ni1",
          "Q_Ni2"
        ],
        "units": {
          "displacement": "Å",
          "energy": "eV/f.u.",
          "M_Ni1": "μB",
          "M_Ni2": "μB",
          "Q_Ni1": "e",
          "Q_Ni2": "e"
        }
      },
      "description": "Raw frozen-phonon energy, magnetic moment, and charge data for each mode and displacement. The checker will compute spin disproportionation, charge disproportionation, and stiffness from this file and compare them to hidden gold values within tolerance."
    },
    {
      "file": "fitted_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "breathing",
          "half_breathing"
        ],
        "items": {
          "breathing": {
            "A2": "float (eV/Å^2)",
            "A3": "float (eV/Å^3)",
            "A3_to_A2_ratio": "float"
          },
          "half_breathing": {
            "A2": "float (eV/Å^2)",
            "A3": "float (eV/Å^3)",
            "A3_to_A2_ratio": "float"
          }
        }
      },
      "description": "Fitted harmonic and anharmonic energy coefficients for breathing and half-breathing modes. The checker will refit the energy data from the CSV and compare its own fit to the reported coefficients within tolerance."
    },
    {
      "file": "band_splitting.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "displacement",
          "band_splitting",
          "deformation_potential"
        ],
        "units": {
          "displacement": "Å",
          "band_splitting": "eV",
          "deformation_potential": "eV/Å"
        }
      },
      "description": "Band splitting and deformation potential at u=0.03 Å for the full-breathing mode. The checker will compare the reported deformation potential to a hidden reference value within tolerance."
    }
  ],
  "notes": "The hidden checker will re-derive spin/charge disproportionation and stiffness from the CSV, refit energy coefficients, and compare the reported band splitting to a hidden reference."
}
```

## How you are scored
A hidden verifier independently scores each artifact after submission. It does not compare your numbers directly to the ones in the original paper; instead it recomputes derived quantities from your raw data and checks consistency.

- From `energy_moment_charge_data.csv`, the verifier extracts the spin disproportionation |M_Ni1 – M_Ni2| and charge disproportionation |Q_Ni1 – Q_Ni2| at the smallest displacement, computes the effective stiffness K(u) = ΔE(u)/u² for the smallest few displacements, and verifies that K(u) becomes negative (indicating an instability).
- Using the energy data you supplied, it independently refits ΔE(u) to the same polynomial form and compares the obtained A₂ and A₃ to your reported values.
- From `band_splitting.csv`, it checks the deformation potential against a hidden reference obtained from the paper’s reported flat-band splitting.

Each step contributes a fraction of the final reward. Reporting a plausible number without having performed the DFT calculations will fail, because the verifier’s own recomputations and sign checks rely on the internal consistency of your raw data across multiple displacement amplitudes.
