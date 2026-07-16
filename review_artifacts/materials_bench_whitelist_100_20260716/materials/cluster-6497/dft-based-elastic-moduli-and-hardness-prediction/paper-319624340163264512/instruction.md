# Dielectric and optical properties of cubic carbides via Harrison's bonding orbital model

## Problem background
Cubic carbides of group‑IV elements (SiC, GeC, SnC) are semiconductors of interest for high‑power electronics and optoelectronics. Harrison's bonding orbital model provides analytical expressions for the dielectric response of tetrahedrally bonded solids in terms of bond covalence, polarity, and electron density. Using this model one can compute linear and quadratic susceptibilities, high‑frequency and static dielectric constants, electro‑optic coefficients, photoelastic constants, bulk modulus, and pressure derivatives of the dielectric constants. In this task you will compute these properties for the three carbides using two standard sets of atomic hybrid energies.

## Approach
Harrison's bonding orbital model represents the electronic structure with sp³ hybrid orbitals on each atom, leading to a covalent bond energy V₂ and a polar energy V₃. From the lattice constant a and the atomic s and p energies one first calculates the bond distance d = a√3/4, the covalent energy V₂ = 3.22 ℏ²/(m d²), and the polar energy V₃ = |εₕᴬ − εₕᴮ|/2 where εₕ = (εₛ + 3εₚ)/4. These give the covalency αc = V₂/√(V₂²+V₃²) and polarity αₚ = √(1−αc²). The electron density is nₑ = 32/a³. The formulas for the electronic and ionic contributions to the linear and quadratic susceptibilities involve αc, αₚ, nₑ, d, and a scaling factor γ that accounts for local‑field corrections. The scaling factor γ = 1.44 is taken from the paper (obtained by fitting ε∞ of 3C‑SiC to the experimental value). After fixing γ to this value, all other quantities follow from straightforward algebraic evaluation. The work uses two sets of atomic hybrid energies: one from Mann's tables and one from Herman–Skillman's tables, which differ slightly and thereby produce two columns for each compound. You will implement the model using γ = 1.44 and compute all the quantities listed in the output schema for SiC, GeC, and SnC at the given lattice constants.

## Reproduction target
Implement the full Harrison bonding‑orbital model to compute the following quantities for each of the three compounds (SiC, GeC, SnC) and for each of the two atomic‑energy sources (Mann, Herman‑Skillman): linear electronic susceptibility χ₁⁽el⁾, total linear susceptibility χ₁, high‑frequency dielectric constant ε∞, static dielectric constant ε₀, ionic enhancement factor θ, quadratic electronic susceptibility χ₁₄⁽el⁾, total quadratic susceptibility χ₁₄, electronic electro‑optic coefficient r₄₁⁽el⁾, total electro‑optic coefficient r₄₁, photoelastic constants p₁₁, p₁₂, p₄₄, bulk modulus B, pressure derivatives ∂ε∞/∂P and ∂ε₀/∂P, and the dimensionless products (∂ε∞/∂P)B and (∂ε₀/∂P)B. All results must be written to a CSV file with columns matching the output schema. The lattice constants are a = 4.36 Å for SiC, 4.59 Å for GeC, 5.11 Å for SnC. The atomic hybrid energies (εₛ, εₚ) for C, Si, Ge, Sn from the Mann and Herman–Skillman tables are provided explicitly in the assets. The target is to produce a CSV containing six rows (3 compounds × 2 sources) that accurately reflect the model's predictions; no external data download is required.

## Assets

- Atomic hybrid energies (ε_s, ε_p) for C, Si, Ge, Sn from Mann (1967) and Herman-Skillman (1963) tables

## Workflow steps



### Step 1: Compute dielectric and optical properties
- Role: scored (load-bearing)
- Action: For each compound (SiC, GeC, SnC) and for each of the two sets of atomic hybrid energies (Mann tables and Herman-Skillman tables), compute all quantities listed in the output schema using Harrison's bonding orbital model formulas. Use the lattice constants a = 4.36, 4.59, 5.11 Å respectively, the scaling factor γ = 1.44, and the provided orbital energies. The formulas yield electronic and ionic contributions to linear and quadratic susceptibilities, dielectric constants, electro-optic coefficients, photoelastic constants, bulk modulus, and pressure derivatives. Assemble all results into a single CSV file.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: CSV with columns: compound (SiC, GeC, SnC), source (Mann, Herman-Skillman), chi1_el (dimensionless), chi1 (dimensionless), epsilon_inf (dimensionless), epsilon_0 (dimensionless), theta (dimensionless), chi14_el (10^-12 m/V), chi14 (10^-12 m/V), r41_el (10^-12 m/V), r41 (10^-12 m/V), p11 (dimensionless), p12 (dimensionless), p44 (dimensionless), B (GPa), d_epsilon_inf_dP (10^-2 GPa^-1), d_epsilon_0_dP (10^-2 GPa^-1), prod_d_epsilon_inf_dP_B (dimensionless), prod_d_epsilon_0_dP_B (dimensionless). 6 rows (3 compounds × 2 sources). All numerical values as per the model definitions.
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
- description: Computed dielectric susceptibilities, permittivities, electro‑optic coefficients, photoelastic constants, bulk modulus, and pressure derivatives for SiC, GeC, SnC using Mann and Herman‑Skillman atomic energies. The checker compares each numeric entry to the paper's reported gold with a relative tolerance of 10% (absolute tolerance 0.005 for near‑zero values). The gamma calibration process step ensures the values are derived from the model, not guessed.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `source`, `chi1_el`, `chi1`, `epsilon_inf`, `epsilon_0`, `theta`, `chi14_el`, `chi14`, `r41_el`, `r41`, `p11`, `p12`, `p44`, `B`, `d_epsilon_inf_dP`, `d_epsilon_0_dP`, `prod_d_epsilon_inf_dP_B`, `prod_d_epsilon_0_dP_B`
  - `units`:
    - `chi1_el`: dimensionless
    - `chi1`: dimensionless
    - `epsilon_inf`: dimensionless
    - `epsilon_0`: dimensionless
    - `theta`: dimensionless
    - `chi14_el`: 10^-12 m/V
    - `chi14`: 10^-12 m/V
    - `r41_el`: 10^-12 m/V
    - `r41`: 10^-12 m/V
    - `p11`: dimensionless
    - `p12`: dimensionless
    - `p44`: dimensionless
    - `B`: GPa
    - `d_epsilon_inf_dP`: 10^-2 GPa^-1
    - `d_epsilon_0_dP`: 10^-2 GPa^-1
    - `prod_d_epsilon_inf_dP_B`: dimensionless
    - `prod_d_epsilon_0_dP_B`: dimensionless

Notes: All formulas from Harrison's bonding orbital model are to be implemented by the agent. The scaling factor γ is not provided; it must be calibrated from experimental ε∞ of SiC as part of a process step. The output CSV contains 6 rows covering every combination of compound and atomic‑energy source.

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
          "source",
          "chi1_el",
          "chi1",
          "epsilon_inf",
          "epsilon_0",
          "theta",
          "chi14_el",
          "chi14",
          "r41_el",
          "r41",
          "p11",
          "p12",
          "p44",
          "B",
          "d_epsilon_inf_dP",
          "d_epsilon_0_dP",
          "prod_d_epsilon_inf_dP_B",
          "prod_d_epsilon_0_dP_B"
        ],
        "units": {
          "chi1_el": "dimensionless",
          "chi1": "dimensionless",
          "epsilon_inf": "dimensionless",
          "epsilon_0": "dimensionless",
          "theta": "dimensionless",
          "chi14_el": "10^-12 m/V",
          "chi14": "10^-12 m/V",
          "r41_el": "10^-12 m/V",
          "r41": "10^-12 m/V",
          "p11": "dimensionless",
          "p12": "dimensionless",
          "p44": "dimensionless",
          "B": "GPa",
          "d_epsilon_inf_dP": "10^-2 GPa^-1",
          "d_epsilon_0_dP": "10^-2 GPa^-1",
          "prod_d_epsilon_inf_dP_B": "dimensionless",
          "prod_d_epsilon_0_dP_B": "dimensionless"
        }
      },
      "description": "Computed dielectric susceptibilities, permittivities, electro‑optic coefficients, photoelastic constants, bulk modulus, and pressure derivatives for SiC, GeC, SnC using Mann and Herman‑Skillman atomic energies. The checker compares each numeric entry to the paper's reported gold with a relative tolerance of 10% (absolute tolerance 0.005 for near‑zero values). The gamma calibration process step ensures the values are derived from the model, not guessed."
    }
  ],
  "notes": "All formulas from Harrison's bonding orbital model are to be implemented by the agent. The scaling factor γ is not provided; it must be calibrated from experimental ε∞ of SiC as part of a process step. The output CSV contains 6 rows covering every combination of compound and atomic‑energy source."
}
```

## How you are scored
A hidden verifier will inspect your `/app/outputs/computed_properties.csv`. It will compare each numeric entry in that file to reference values (derived from the same Harrison model applied with the exact same input parameters). The reward is the weighted fraction of entries that match the references within an acceptable tolerance. The main dielectric properties (χ₁, ε∞, ε₀, B) carry double weight. Simply reporting numbers that happen to be correct without actually running the computation will not pass, because the verifier checks for internal consistency and the tolerance is tight enough that a guess is extremely unlikely to succeed. The final score reflects only the correctness of the CSV. No other artifacts are scored.
