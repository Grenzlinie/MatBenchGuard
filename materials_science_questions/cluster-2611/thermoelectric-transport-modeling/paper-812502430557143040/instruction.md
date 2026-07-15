# First-principles calculation of structural, elastic, electronic, and optical properties of AE3GaAs3 Zintl phases

## Problem background
Zintl phases are intermetallic compounds combining ionic and covalent bonding, exhibiting a wide range of technologically relevant properties. The compounds Sr3GaAs3 and Ba3GaAs3 crystallize in the orthorhombic Pnma structure and belong to this family. Accurate first-principles predictions of their structural, elastic, electronic, and optical properties are essential to assess their potential for optoelectronic and thermoelectric applications. The present task aims to compute these properties using density functional theory.

## Approach
The properties are computed via density functional theory (DFT) using two exchange-correlation functionals: the GGA-PBEsol functional for geometry optimization and elastic constant calculations, and the Tran-Blaha modified Becke-Johnson (TB-mBJ) potential for electronic structure and optical property calculations, which better reproduces band gaps. All calculations can be performed with an open-source full-potential linearized augmented plane-wave (FP-LAPW) code (e.g., Elk) or equivalent DFT packages that support these functionals.

The workflow starts from the experimentally reported orthorhombic Pnma crystal structures (space group No. 62, Z=8) of Sr3GaAs3 and Ba3GaAs3. The lattice parameters and fractional atomic coordinates are given below. Full geometry optimization (relaxation of atomic positions and lattice parameters) is performed with GGA-PBEsol to obtain equilibrium geometries. From the relaxed structures, the nine independent monocrystalline elastic constants (C11, C12, C13, C22, C23, C33, C44, C55, C66) are computed via a stress-strain method using the same GGA-PBEsol functional.

Subsequently, a self-consistent field calculation and band structure calculation are carried out with the TB-mBJ functional on the relaxed geometries. This yields the fundamental band gap at the Γ point and the band dispersion along high-symmetry directions. Effective masses for holes and electrons at the Γ point are extracted by fitting the band dispersion near the valence band maximum and conduction band minimum along three principal directions: [100] (Γ→Y), [010] (Γ→X), and [001] (Γ→Z). The real part of the dielectric function at zero photon energy, ε₁(0), is computed for light polarized along each principal axis to obtain the static dielectric constants.

**Starting crystal structures**

For **Sr3GaAs3**: a = 12.757 Å, b = 19.268 Å, c = 6.503 Å.
Atomic coordinates (fractional, from experiment):
| Atom | Wyckoff | x       | y       | z       |
|------|---------|---------|---------|---------|
| Sr1  | 8d      | 0.09634 | 0.25715 | 0.01996 |
| Sr2  | 8d      | 0.40189 | 0.29413 | 0.53380 |
| Sr3  | 4c      | 0.12390 | 0.25    | 0.50322 |
| Sr4  | 4c      | 0.40803 | 0.25    | 0.12307 |
| Ga   | 8d      | 0.02648 | 0.04743 | 0.30949 |
| As1  | 4c      | 0.13597 | 0.25    | 0.13722 |
| As2  | 4c      | 0.32829 | 0.25    | 0.26950 |
| As3  | 8d      | 0.05432 | 0.06485 | 0.81796 |
| As4  | 8d      | 0.11241 | 0.00137 | 0.58602 |

For **Ba3GaAs3**: a = 13.3589 Å, b = 19.9788 Å, c = 6.8008 Å.
Atomic coordinates (fractional, from experiment):
| Atom | Wyckoff | x       | y       | z       |
|------|---------|---------|---------|---------|
| Ba1  | 8d      | 0.09402 | 0.25735 | 0.01849 |
| Ba2  | 8d      | 0.40146 | 0.29317 | 0.53144 |
| Ba3  | 4c      | 0.12455 | 0.25    | 0.50431 |
| Ba4  | 4c      | 0.40768 | 0.25    | 0.12571 |
| Ga   | 8d      | 0.02412 | 0.04776 | 0.30757 |
| As1  | 4c      | 0.13740 | 0.25    | 0.13898 |
| As2  | 4c      | 0.32888 | 0.25    | 0.26306 |
| As3  | 8d      | 0.05430 | 0.06611 | 0.81757 |
| As4  | 8d      | 0.11190 | 0.00222 | 0.58566 |

Use these as the initial geometries for the geometry optimization step.

## Reproduction target
Reproduce the following properties for both Sr3GaAs3 and Ba3GaAs3:
- Equilibrium lattice parameters a, b, c (in Å) and unit-cell volume V (in Å³) after full geometry relaxation with GGA-PBEsol.
- Nine independent monocrystalline elastic constants C₁₁, C₁₂, C₁₃, C₂₂, C₂₃, C₃₃, C₄₄, C₅₅, C₆₆ (in GPa) from stress-strain calculations with GGA-PBEsol.
- Fundamental direct band gap (in eV) from the TB-mBJ electronic structure calculation.
- Hole and electron effective masses (in units of free electron mass m₀) along the three principal crystallographic directions [100], [010], [001] extracted from the TB-mBJ band structure.
- Static dielectric constant ε₁(0) (dimensionless) for electric field polarizations parallel to [100], [010], and [001] from the TB-mBJ optical calculation.

Output each set of results as a CSV file following the specified schema. Perform all calculations using open-source DFT codes (Elk recommended). No external dataset download is required; all needed structural data is provided above.

## Assets

- Elk FP-LAPW code: http://elk.sourceforge.net

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform full DFT geometry optimization (relaxation of atomic positions and lattice parameters) for Sr3GaAs3 and Ba3GaAs3 using the GGA-PBEsol functional, starting from the experimental orthorhombic Pnma structures (lattice parameters and fractional coordinates given in the instruction). Converge total energy, forces, and stress to obtain the equilibrium geometries.
- Evidence: `/app/outputs/geometry_opt.log`

### Step 2: Lattice parameters output
- Role: scored
- Action: Extract the optimized lattice parameters a, b, c (in Å) and unit-cell volume V (in Å³) from the relaxed geometries and save as a CSV file.
- Output file: `/app/outputs/lattice_parameters.csv`
- Format: csv
- Contract: compound,a,b,c,V
- Scoring: scored by hidden verifier

### Step 3: Elastic constant calculation
- Role: scored
- Action: Using the relaxed geometries, compute the nine independent monocrystalline elastic constants C11, C12, C13, C22, C23, C33, C44, C55, C66 (in GPa) for each compound via the stress-strain method with GGA-PBEsol. Save the results as a CSV file.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: compound,C11,C12,C13,C22,C23,C33,C44,C55,C66
- Scoring: scored by hidden verifier

### Step 4: Electronic structure calculation
- Role: process
- Action: Perform DFT self-consistent field calculation and band structure calculation for both compounds using the TB-mBJ functional on the relaxed geometries. Obtain eigenvalues along a high-symmetry path and at the Γ point to enable band gap and effective mass extraction.
- Evidence: `/app/outputs/electronic_structure.log`

### Step 5: Band gap extraction
- Role: scored (load-bearing)
- Action: Extract the fundamental band gap (direct at Γ) for each compound from the computed band structure and save as a CSV file (in eV).
- Output file: `/app/outputs/band_gap.csv`
- Format: csv
- Contract: compound,band_gap
- Scoring: scored by hidden verifier

### Step 6: Effective mass extraction
- Role: scored
- Action: Compute hole and electron effective masses along [100] (Γ→Y), [010] (Γ→X), and [001] (Γ→Z) directions by fitting the band dispersion near the VBM and CBM. Save as a CSV file with dimensionless m* (units of m0).
- Output file: `/app/outputs/effective_masses.csv`
- Format: csv
- Contract: compound,carrier_type,direction,m_star
- Scoring: scored by hidden verifier

### Step 7: Static dielectric constant calculation
- Role: scored
- Action: From the electronic structure, compute the real part of the dielectric function at zero frequency, ε₁(0), for polarizations along the three principal crystallographic axes [100], [010], [001]. Save as a CSV file (dimensionless).
- Output file: `/app/outputs/static_dielectric.csv`
- Format: csv
- Contract: compound,direction,epsilon1_0
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.csv`
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/band_gap.csv`
- `/app/outputs/effective_masses.csv`
- `/app/outputs/static_dielectric.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.csv
- path: `/app/outputs/lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters and unit-cell volume for Sr3GaAs3 and Ba3GaAs3.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a`, `b`, `c`, `V`
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `V`: Å³

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Monocrystalline elastic constants C_ij from GGA-PBEsol stress-strain calculations.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `C11`, `C12`, `C13`, `C22`, `C23`, `C33`, `C44`, `C55`, `C66`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C22`: GPa
    - `C23`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C55`: GPa
    - `C66`: GPa

### band_gap.csv
- path: `/app/outputs/band_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fundamental band gap (direct at Γ) from TB-mBJ electronic structure.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_gap`
  - `units`:
    - `band_gap`: eV

### effective_masses.csv
- path: `/app/outputs/effective_masses.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electron and hole effective masses along [100], [010], [001] directions extracted from the band structure.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `carrier_type`, `direction`, `m_star`
  - `units`:
    - `m_star`: dimensionless (m0)

### static_dielectric.csv
- path: `/app/outputs/static_dielectric.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constant ε₁(0) for three polarizations from TB-mBJ optical calculations.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `direction`, `epsilon1_0`
  - `units`:
    - `epsilon1_0`: dimensionless

Notes: All outputs are compared to the paper-reported values with predefined relative tolerances. The checker uses result-level comparison because recomputing from raw wavefunctions is heavy and the paper's own DFT numbers are the target. The band gap step is load-bearing (T0 result-level compare).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a",
          "b",
          "c",
          "V"
        ],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "V": "Å³"
        }
      },
      "description": "Optimized lattice parameters and unit-cell volume for Sr3GaAs3 and Ba3GaAs3."
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "C11",
          "C12",
          "C13",
          "C22",
          "C23",
          "C33",
          "C44",
          "C55",
          "C66"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C22": "GPa",
          "C23": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C55": "GPa",
          "C66": "GPa"
        }
      },
      "description": "Monocrystalline elastic constants C_ij from GGA-PBEsol stress-strain calculations."
    },
    {
      "file": "band_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_gap"
        ],
        "units": {
          "band_gap": "eV"
        }
      },
      "description": "Fundamental band gap (direct at Γ) from TB-mBJ electronic structure."
    },
    {
      "file": "effective_masses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "carrier_type",
          "direction",
          "m_star"
        ],
        "units": {
          "m_star": "dimensionless (m0)"
        }
      },
      "description": "Electron and hole effective masses along [100], [010], [001] directions extracted from the band structure."
    },
    {
      "file": "static_dielectric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "direction",
          "epsilon1_0"
        ],
        "units": {
          "epsilon1_0": "dimensionless"
        }
      },
      "description": "Static dielectric constant ε₁(0) for three polarizations from TB-mBJ optical calculations."
    }
  ],
  "notes": "All outputs are compared to the paper-reported values with predefined relative tolerances. The checker uses result-level comparison because recomputing from raw wavefunctions is heavy and the paper's own DFT numbers are the target. The band gap step is load-bearing (T0 result-level compare)."
}
```

## How you are scored
A hidden verifier will compare each of your CSV output files against reference values (obtained from published first-principles calculations) using tolerances that account for the spread between different DFT implementations and basis sets. Each scored artifact contributes a portion of the total reward, with the most critical properties (band gap, elastic constants, lattice parameters) weighted more heavily. The verifier checks that the reported values are physically reasonable; an exact match to a specific code’s output is not required. To achieve a high score, execute all workflow steps consistently and extract your results accurately from the DFT outputs. The final reward is computed automatically from the CSV files you produce.
