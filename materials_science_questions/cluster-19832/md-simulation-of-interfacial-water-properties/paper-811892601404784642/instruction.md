# Compute Alkane Wetting Film Contact Angles from Dielectric Spectra

## Problem background
When a thin film of a short-chain alkane (pentane or hexane) rests on a water or salt-solution surface, its stability is determined by the balance of long-range van der Waals forces and short-range image-charge forces from water molecules dissolved in the alkane. The image-charge interactions arise because polar water molecules adsorb at the alkane/water interface and interact with their electrostatic images in the adjacent phases. Increasing temperature or salinity shifts the disjoining pressure isotherm toward positive values, which can cause a transition from partial to complete wetting. The macroscopic contact angle of the alkane film on the aqueous substrate is a direct measure of this wetting behaviour and can be computed from the disjoining pressure isotherm using the Derjaguin–Frumkin theory. In this task you will compute these contact angles for pentane and hexane films on pure water and on NaCl solutions at two temperatures, implementing the full numerical pipeline from dielectric spectra to the final equilibrium angles.

## Approach
The approach is a compute-driven physical–chemical pipeline. You will:
1. Construct the dielectric permittivity spectra ε(iξ) for water/NaCl solutions and for pentane/hexane using the Ninham–Parsegian multi-oscillator model with tabulated UV-oscillator parameters for each temperature and salinity.
2. Compute the van der Waals component of the disjoining pressure Π_m(h) for each film/condition using the full Lifshitz (DLP) integral equation over a grid of film thicknesses (~0.2–10 nm).
3. Solve a Langmuir-type adsorption isotherm self-consistently to obtain the surface coverage of water dipoles at the alkane/water interface, accounting for hydrogen bonding, dispersion, and image-dipole energies.
4. From the coverage and the screened image-dipole formulas, compute the image-charge contribution Π_im(h).
5. Sum the two components to obtain the total disjoining pressure isotherm Π_total(h).
6. For each condition, find the equilibrium thickness h₀ where Π_total(h₀)=0, then integrate the isotherm to calculate the macroscopic contact angle via cos θ = 1 + (1/σ) ∫_{h₀}^∞ Π_total(h) dh, using the appropriate alkane surface tension σ.
The conditions span pentane and hexane at 20 °C and 40 °C on aqueous solutions with NaCl concentrations 0, 0.5, and 2.0 M. All necessary oscillator parameters, adsorption energies, and surface tensions are provided in the instruction items below.

## Reproduction target
Compute the equilibrium contact angle (in degrees) for each of the 12 combinations of alkane (pentane/hexane), temperature (20 °C / 40 °C), and NaCl concentration (0.0, 0.5, 2.0 M) and write them to `/app/outputs/contact_angles.csv`. The CSV must have a header row with columns `alkane` (string), `temperature_C` (integer), `NaCl_M` (float), `contact_angle_deg` (float). One data row per condition — exactly 12 rows. You must generate the contact angles by running the full disjoining-pressure pipeline described in the workflow steps; simply reporting the numbers without executing the physics will not meet the scoring criteria.

## Assets

- NumPy: numpy
- SciPy: scipy

## Dielectric oscillators and physical parameters

### Alkane oscillator parameters (Ninham-Parsegian representation)
For pentane and hexane, use the following parameters in Eq. (3):
- Pentane: C_IR = 0.145, ω_IR = 3.45×10^14 rad/s, C_UV = 0.539, ω_UV = 1.62×10^16 rad/s.
- Hexane: C_IR = 0.145, ω_IR = 3.45×10^14 rad/s, C_UV = 0.555, ω_UV = 1.55×10^16 rad/s.

### Water/NaCl solution dielectric spectra
The dielectric permittivity function for the aqueous phase follows Eq. (2) with three oscillators (microwave, infrared, ultraviolet). The microwave and infrared oscillator parameters are taken as approximately independent of salinity and are:

| Temperature (°C) | C_MICRO | ω_MICRO (rad/s) | C_IR  | ω_IR (rad/s)      |
|------------------|---------|-----------------|-------|--------------------|
| 20               | 73.8    | 0.67×10^11      | 0.487 | 5.68×10^13        |
| 40               | 68.3    | 1.00×10^11      | 0.487 | 5.68×10^13        |

The ultraviolet oscillator parameters C_UV and ω_UV for the required NaCl concentrations and temperatures are taken from the table below (extracted from Table 1 of the paper, only the rows needed are listed):

| NaCl (mol/L) | Temp (°C) | C_UV | ω_UV (rad/s) |
|--------------|-----------|------|--------------|
| 0.0          | 20        | 0.754 | 1.858×10^16 |
| 0.0          | 40        | 0.748 | 1.888×10^16 |
| 0.5          | 20        | 0.766 | 1.849×10^16 |
| 0.5          | 40        | 0.760 | 1.870×10^16 |
| 2.0          | 20        | 0.799 | 1.794×10^16 |
| 2.0          | 40        | 0.792 | 1.834×10^16 |

For the vapour (air) phase, ε = 1 (vacuum) for all frequencies, so C_IR=C_UV=0.

### Adsorption and image-charge parameters
- Hydrogen-bond energy U_OH = 20.86 kJ/mol.
- Distance of adsorbed water molecule from the interface: d = 0.26 nm.
- Number of adsorption sites per unit area: Γ₀ = 7.1 nm⁻².
- Dipole moment of a water molecule: |p| = 1.854 Debye (6.19×10⁻³⁰ C·m).
- The dipole moment is oriented such that the normal component p^n = |p|·cos(52.23°) and parallel component p^p = |p|·sin(52.23°).
- The water molar volume ν_m = 18.0 cm³/mol = 3.00×10⁻²⁹ m³.
- The alkane surface tensions (used in Derjaguin–Frumkin equation): σ(pentane) = 15.6 mN/m, σ(hexane) = 17.9 mN/m at 20°C; use the same values at 40°C (no temperature correction is available).

All other physical constants (Boltzmann constant, Planck constant, speed of light) should be taken from standard CODATA values.

## Workflow steps

### Step 1: Assemble dielectric permittivity functions
- Role: process
- Action: Construct the dielectric permittivity functions ε(iξ) for alkanes (pentane, hexane) and water/NaCl solutions using the Ninham–Parsegian multi-oscillator model with the oscillator parameters provided in the instruction.
- Evidence: none

### Step 2: Compute van der Waals component Π_m(h)
- Role: process
- Action: Calculate the van der Waals disjoining pressure Π_m(h) for pentane and hexane films at 20°C and 40°C with NaCl concentrations 0, 0.5, and 2.0 M over a range of film thicknesses (approx. 0.2–10 nm) using the DLP integral equation and the dielectric functions from S1.
- Evidence: `/app/outputs/vdw_pressure.csv`

### Step 3: Solve for interfacial water adsorption coverage
- Role: process
- Action: Self-consistently solve the Langmuir-type adsorption equations (including image-charge energies) to obtain the surface coverage Γ^(12)(h) of water at the alkane/water interface for the same conditions. Use hydrogen bond energy U_OH = 20.86 kJ/mol and all other required parameters given in the instruction.
- Evidence: `/app/outputs/adsorption.csv`

### Step 4: Compute image-charge contribution Π_im(h)
- Role: process
- Action: Using the coverage from S3 and the screened image-dipole formulas, compute the image-charge component of the disjoining pressure Π_im(h) for the same thickness range and conditions.
- Evidence: `/app/outputs/im_pressure.csv`

### Step 5: Compute total disjoining pressure Π(h)
- Role: process
- Action: Sum the van der Waals and image-charge contributions to obtain the total disjoining pressure isotherm Π(h) for each condition.
- Evidence: `/app/outputs/total_pressure.csv`

### Step 6: Calculate equilibrium contact angles
- Role: scored (load-bearing)
- Action: For each condition (alkane pentane or hexane, temperature 20°C or 40°C, NaCl concentration 0, 0.5, or 2.0 M) determine the equilibrium film thickness h₀ where Π(h₀)=0, then integrate the total disjoining pressure isotherm to compute the macroscopic contact angle using the Derjaguin–Frumkin relation: cos θ = 1 + (1/σ) ∫_{h₀}^∞ Π(h) dh, with alkane surface tensions σ: pentane 15.6 mN/m, hexane 17.9 mN/m at 20°C. Write the results to /app/outputs/contact_angles.csv.
- Output file: `/app/outputs/contact_angles.csv`
- Format: csv
- Contract: CSV with header row. Columns: alkane (string, 'pentane' or 'hexane'), temperature_C (integer, 20 or 40), NaCl_M (float, 0.0, 0.5, or 2.0), contact_angle_deg (float). One data row per condition (12 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contact_angles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contact_angles.csv
- path: `/app/outputs/contact_angles.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium contact angles for pentane and hexane wetting films on water/NaCl solutions. The checker compares each value to a hidden gold reference within tolerance (15% relative error or 0.5° absolute error for small angles) and checks for monotonic decreasing trend with temperature and salinity.
- schema:
  - `type`: table
  - `required_columns`: `alkane`, `temperature_C`, `NaCl_M`, `contact_angle_deg`
  - `description`: alkane: string (pentane/hexane); temperature_C: integer (20,40); NaCl_M: float (0.0,0.5,2.0); contact_angle_deg: float.

Notes: The scored output is the contact_angles.csv file. The checker performs result-level comparison against paper-reported values from Table 2 of the source (not provided to the agent). Intermediate files vdw_pressure.csv, adsorption.csv, im_pressure.csv, and total_pressure.csv are required as evidence that the pipeline was executed but are not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contact_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alkane",
          "temperature_C",
          "NaCl_M",
          "contact_angle_deg"
        ],
        "description": "alkane: string (pentane/hexane); temperature_C: integer (20,40); NaCl_M: float (0.0,0.5,2.0); contact_angle_deg: float."
      },
      "description": "Equilibrium contact angles for pentane and hexane wetting films on water/NaCl solutions. The checker compares each value to a hidden gold reference within tolerance (15% relative error or 0.5° absolute error for small angles) and checks for monotonic decreasing trend with temperature and salinity."
    }
  ],
  "notes": "The scored output is the contact_angles.csv file. The checker performs result-level comparison against paper-reported values from Table 2 of the source (not provided to the agent). Intermediate files vdw_pressure.csv, adsorption.csv, im_pressure.csv, and total_pressure.csv are required as evidence that the pipeline was executed but are not directly scored."
}
```

## How you are scored
A hidden verifier independently scores your `/app/outputs/contact_angles.csv`. It compares each contact angle you report against hidden reference values and also checks that the angles follow the physically expected monotonic behaviour (angles must decrease with increasing temperature and with increasing salinity for a given alkane). The verifier does not reward simply printing the paper’s reported numbers — the underlying physics pipeline must be executed, and the computed angles must lie within an appropriate tolerance of the hidden reference values and satisfy the trend checks. The final score is a weighted fraction of passing conditions, with penalties applied for trend violations.
