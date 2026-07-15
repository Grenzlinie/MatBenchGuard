# Computational Study of a Phenylmercury Xanthate Complex: DFT, Thermodynamics, and NLO Properties

## Problem background
Organomercury complexes exhibit interesting bonding and nonlinear optical characteristics. This task investigates a specific phenylmercury xanthate compound using computational methods. The work aims to characterize the molecular geometry, relative bond strengths, vibrational and thermodynamic properties, first hyperpolarizability, and electronic absorption spectrum, employing density functional theory and semi-empirical calculations. These quantities are computed from first principles and statistical thermodynamics, providing insight into the bonding and optical behavior of the complex.

## Approach
The computational strategy relies on density functional theory (DFT) at the B3LYP level with the CEP‑121G basis set. A crystal structure serves as the starting point for geometry optimization. From the optimized geometry, harmonic vibrational frequencies are obtained, scaled, and used in standard statistical thermodynamics to calculate heat capacity, entropy, and enthalpy at multiple temperatures. Bond order analysis (e.g., Wiberg bond indices or Natural Bond Orbital analysis) quantifies the bond strengths. Semi-empirical PM3 calculations (via MOPAC) estimate the first hyperpolarizability along the dipole moment direction. Time-dependent DFT (TD‑DFT) at the same DFT level yields electronic transition wavelengths and oscillator strengths. The workflow is self-contained and uses open-source tools to replace proprietary software.

## Reproduction target
Reproduce the DFT-optimized molecular geometry of the title compound, compute bond orders for the Hg–C and Hg–S bonds, and derive the standard molar thermodynamic functions (heat capacity Cₚ, entropy S, enthalpy H) at eight temperatures: 200.0 K, 298.1 K, 300.0 K, 400.0 K, 500.0 K, 600.0 K, 700.0 K, and 800.0 K, using scaled harmonic vibrational frequencies. Additionally, compute the first hyperpolarizability βμ (in esu) from a PM3 semi-empirical calculation and report the two strongest electronic absorption wavelengths (in nm) with oscillator strengths from a TD‑DFT calculation. Write all results to the specified output files.

## Assets

- Crystal structure of (isopropylxanthato)(phenyl)mercury(I) (CCDC 254302): https://www.ccdc.cam.ac.uk/structures/
- Open-source DFT code (ORCA or NWChem): https://orcaforum.kofo.mpg.de/ (ORCA) or https://nwchemgit.github.io/ (NWChem)
- OpenMOPAC (or MOPAC): https://github.com/OpenMOPAC/MOPAC

## Workflow steps

### Step 1: DFT geometry optimization
- Role: scored
- Action: Perform DFT geometry optimization of the title compound at the B3LYP level with the CEP-121G basis set, using the crystal structure from CCDC 254302 as the initial geometry. Save the optimized Cartesian coordinates as an XYZ file.
- Output file: `/app/outputs/optimized_geometry.xyz`
- Format: txt
- Contract: Standard XYZ format: first line number of atoms, second line comment, then each line: element_symbol x y z (in Å).
- Scoring: scored by hidden verifier

### Step 2: Vibrational frequency and bond order analysis
- Role: process
- Action: Using the optimized geometry from Step 1, run a harmonic vibrational frequency calculation at B3LYP/CEP-121G. Scale the computed frequencies by 0.96. Also perform a bond order analysis (e.g., Wiberg bond indices or NBO) to obtain numerical bond orders for the Hg–C and Hg–S bonds.
- Evidence: `/app/outputs/freq_output.log`

### Step 3: Bond order trend verification
- Role: scored
- Action: Extract the computed bond orders for Hg–C and Hg–S from the analysis performed in Step 2 and write them to a CSV file.
- Output file: `/app/outputs/bond_orders.csv`
- Format: csv
- Contract: CSV with header: bond,order. Two rows: 'Hg-C',<value> and 'Hg-S',<value>.
- Scoring: scored by hidden verifier

### Step 4: Thermodynamic functions from vibrational data
- Role: scored (load-bearing)
- Action: Using the scaled harmonic vibrational frequencies from Step 2 and standard statistical thermodynamics formulas, compute the standard molar heat capacity (Cp), entropy (S), and enthalpy (H) at the temperatures: 200.0 K, 298.1 K, 300.0 K, 400.0 K, 500.0 K, 600.0 K, 700.0 K, 800.0 K. Output a CSV table.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: T (K), Cp (J mol⁻¹ K⁻¹), S (J mol⁻¹ K⁻¹), H (kJ mol⁻¹). Eight rows, one per temperature.
- Scoring: scored by hidden verifier

### Step 5: First hyperpolarizability (β_μ) by PM3
- Role: scored
- Action: Using the optimized geometry from Step 01, perform a semi-empirical PM3 calculation (MOPAC) to compute the first hyperpolarizability β_μ along the dipole moment direction. Output the value in esu.
- Output file: `/app/outputs/nlo_result.csv`
- Format: csv
- Contract: CSV with columns: property,value. One row: property='beta_mu', value=<numeric>.
- Scoring: scored by hidden verifier

### Step 6: TD‑DFT electronic absorption spectrum
- Role: scored
- Action: Run a TD‑DFT calculation on the optimized geometry at B3LYP/CEP‑121G level to obtain the two strongest electronic transitions. Output their wavelengths in nm and oscillator strengths.
- Output file: `/app/outputs/electronic_spectrum.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm,oscillator_strength. Two rows, one per transition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_geometry.xyz`
- `/app/outputs/bond_orders.csv`
- `/app/outputs/thermodynamic_functions.csv`
- `/app/outputs/nlo_result.csv`
- `/app/outputs/electronic_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_geometry.xyz
- path: `/app/outputs/optimized_geometry.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized molecular geometry from DFT, compared to experimental X-ray bond lengths via root-mean-square deviation.
- schema:
  - `type`: text
  - `description`: XYZ format atomic coordinates

### bond_orders.csv
- path: `/app/outputs/bond_orders.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Bond orders for Hg-C and Hg-S bonds.
- schema:
  - `type`: table
  - `required_columns`: `bond`, `order`

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Standard thermodynamic functions computed from scaled vibrational frequencies; compared to hidden reference values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp`, `S`, `H`
  - `units`:
    - `T`: K
    - `Cp`: J mol⁻¹ K⁻¹
    - `S`: J mol⁻¹ K⁻¹
    - `H`: kJ mol⁻¹

### nlo_result.csv
- path: `/app/outputs/nlo_result.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: First hyperpolarizability β_μ from PM3 calculation; compared to hidden reference value with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`

### electronic_spectrum.csv
- path: `/app/outputs/electronic_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: TD-DFT electronic absorption wavelengths and oscillator strengths; compared to hidden reference values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `oscillator_strength`

Notes: All scored outputs are compared against hidden gold values derived from the paper (tolerances set to absorb legitimate computational variation). The load-bearing thermodynamic step ensures that the frequency calculation (process step) was genuinely executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_geometry.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ format atomic coordinates"
      },
      "description": "Optimized molecular geometry from DFT, compared to experimental X-ray bond lengths via root-mean-square deviation."
    },
    {
      "file": "bond_orders.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bond",
          "order"
        ]
      },
      "description": "Bond orders for Hg-C and Hg-S bonds."
    },
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp",
          "S",
          "H"
        ],
        "units": {
          "T": "K",
          "Cp": "J mol⁻¹ K⁻¹",
          "S": "J mol⁻¹ K⁻¹",
          "H": "kJ mol⁻¹"
        }
      },
      "description": "Standard thermodynamic functions computed from scaled vibrational frequencies; compared to hidden reference values with tolerances."
    },
    {
      "file": "nlo_result.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ]
      },
      "description": "First hyperpolarizability β_μ from PM3 calculation; compared to hidden reference value with tolerance."
    },
    {
      "file": "electronic_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "oscillator_strength"
        ]
      },
      "description": "TD-DFT electronic absorption wavelengths and oscillator strengths; compared to hidden reference values with tolerances."
    }
  ],
  "notes": "All scored outputs are compared against hidden gold values derived from the paper (tolerances set to absorb legitimate computational variation). The load-bearing thermodynamic step ensures that the frequency calculation (process step) was genuinely executed."
}
```

## How you are scored
A hidden verifier independently evaluates each output artifact against hidden reference criteria. For the geometry, the verifier may check structural agreement with experimental X‑ray bond lengths via root‑mean‑square deviation. For bond orders, the verifier checks that the output matches the required CSV schema. For thermodynamic functions, it compares the computed values at each temperature to reference data with appropriate tolerances. The hyperpolarizability and electronic spectrum are compared to reference values within tolerances. Each scored artifact is assigned a weight, and the final reward is the weighted sum of those per‑stage scores. Simply reporting numbers from the literature without genuine execution of the computational pipeline will not pass; the verifier checks that you have carried out the procedures as described.
