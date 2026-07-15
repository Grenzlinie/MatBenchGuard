# Compute configurational energy coefficients and order-disorder transition temperature for B2 ternary alloys

## Problem background
NiTi shape memory alloys undergo martensitic transformations that depend sensitively on the stability of the high-temperature B2 phase. Alloying additions such as Co can alter the transformation sequence, and this effect is connected to atomic site preference (ASP) behaviours – the tendency of each atomic species to occupy specific sublattice sites. To understand how Co influences B2 phase stability, it is necessary to quantify the configurational energy of the alloy and the order-disorder transition temperature (Tc) as a function of Co concentration. This task computes those quantities from first principles using an analytic ASP free energy model and density functional theory (DFT).

## Approach
The core idea is a mean-field atomic site preference model for ternary B2 alloys, in which the configurational free energy per atom is expressed as a quadratic function of two order parameters (η1, η2) with three composition-independent energy coefficients (ε1, ε2, ε3). These coefficients are extracted directly from the total energies of six specially chosen 2×2×2 B2 supercell configurations computed with DFT. For a given Co concentration y in Ni₀.₅₋ᵧTi₀.₅Coᵧ, the free energy is minimised with respect to η1, η2 at each temperature, and the order-disorder transition temperature Tc is identified as the temperature at which the equilibrium order parameters vanish. By repeating this procedure for several Co concentrations, the dependence of Tc on Co content is obtained.

## Reproduction target
Produce the three configurational energy coefficients ε1, ε2, ε3 (in eV/atom) for the NiTi–Co system from first-principles DFT calculations. Then compute the order-disorder transition temperature Tc (in Kelvin) for at least four Co concentrations y in Ni₀.₅₋ᵧTi₀.₅Coᵧ, including y = 0, and report the results as a CSV table. The Tc values are expected to show a clear trend with composition; you must provide enough points to characterise this dependence.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, GPAW, ABINIT): https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials for Ni, Ti, Co: https://www.quantum-espresso.org/pseudopotentials/
- Python scientific libraries (numpy, scipy, csv, json): numpy scipy

## Workflow steps

### Step 1: DFT total energy calculations for B2 supercells
- Role: process
- Action: Construct 2×2×2 B2 supercells for the six configurations listed below, corresponding to the Ni–Ti–Co system (Ni = species A, Ti = B, Co = X). Perform DFT total energy calculations using an open-source DFT code with GGA-PBE functional and ultrasoft pseudopotentials, plane-wave cutoff 350 eV, 4×4×4 k-point mesh. First, optimize the lattice constant for configuration #1 (η₁=1, η₂=1) to obtain a₀. Then compute total energies for all six configurations at the fixed lattice constant a₀. The configurations and their corresponding energy labels are:

1. E₁ – Ni₇Ti₈Co  (η₁=1, η₂=1): one Co atom replaces the central Ni atom in the Ni₈Ti₈ cell; Co resides on the Ni sublattice (perfect order for both Ni and Co).
2. E₂ – Ni₇Ti₈Co  (η₁=1, η₂=-1): obtained from configuration #1 by swapping the Co atom with one Ti atom, placing Co on the Ti sublattice and one Ti on the Ni sublattice.
3. E₃ – Ni₈Ti₈    (η₁=1, η₂ undefined/irrelevant because C_Co=0): perfect B2 binary NiTi.
4. E₄ – Ni₈Ti₈    (η₁=0.75): obtained from configuration #3 by swapping one Ni atom with one Ti atom, producing one anti-site on each sublattice.
5. E₅ – Co₈Ti₈    (η₂=1): replace all Ni atoms of the Ni₈Ti₈ cell with Co, yielding perfect B2 ordering with Co on the former Ni sublattice.
6. E₆ – Co₈Ti₈    (η₂=0.75): obtained from configuration #5 by swapping one Co atom with one Ti atom, introducing one anti-site pair.

Record the optimized lattice constant a₀ (in Å) and the six total energies E₁…E₆ (in eV) in the evidence file.
- Evidence: `/app/outputs/dft_energies.json`

### Step 2: Compute configurational energy coefficients
- Role: scored
- Action: Use the DFT total energies from step 1 to compute the configurational energy coefficients ε₁, ε₂, ε₃ (in eV/atom) with the following formulas (derived from the ASP model for a 2×2×2 supercell):

  ε₃ = (4 / 7) × (E₁ – E₂)
  ε₁ = (4 / 7) × (E₃ – E₄)
  ε₂ = (4 / 7) × (E₅ – E₆)

Output the three coefficients in a JSON file.
- Output file: `/app/outputs/configurational_coefficients.json`
- Format: json
- Contract: JSON object with keys "epsilon1", "epsilon2", "epsilon3", each a float (eV/atom).
- Scoring: scored by hidden verifier

### Step 3: Compute order-disorder transition temperature Tc vs. Co concentration
- Role: scored (load-bearing)
- Action: Implement the ASP free energy model using the ε coefficients from step 2. The system is Ni₀.₅₋ᵧTi₀.₅Coᵧ, where y is the Co atomic fraction. Identify species A = Ni, B = Ti, X = Co, so C_A = 0.5–y, C_B = 0.5, C_X = y.

  *Configurational energy* (eV/atom):
  ΔE(η₁,η₂) = C_A² ε₁ η₁² + C_X² ε₂ η₂² + 2 C_A C_X ε₃ η₁ η₂

  *Configurational entropy* (eV/K/atom, with k_B = 8.617333262145×10⁻⁵ eV/K):
  S = – k_B/2 [ Σ_{α} P_{aα} ln P_{aα} + Σ_{α} P_{bα} ln P_{bα} ]
  where the site occupation probabilities are:
    P_{aA} = C_A (1+η₁),   P_{aB} = 1 – C_A(1+η₁) – C_X(1+η₂),   P_{aX} = C_X (1+η₂)
    P_{bA} = C_A (1–η₁),   P_{bB} = 1 – C_A(1–η₁) – C_X(1–η₂),   P_{bX} = C_X (1–η₂)

  *Free energy*:
  ΔF(T,η₁,η₂) = ΔE(η₁,η₂) + [ S(η₁,η₂) – S(0,0) ] T

  For each chosen y, find the equilibrium η₁, η₂ that minimize ΔF at a given T (satisfying ∂ΔF/∂η_k = 0 and positive definite Hessian). Then determine the order–disorder transformation temperature T_c as the temperature at which the equilibrium order parameters (η₁, η₂) vanish continuously from above zero. Scan temperature and use root-finding or optimization to locate T_c precisely. Report T_c for at least four Co concentrations (including y=0). Use at least the concentration set y = 0, 0.02, 0.04, 0.06 (or a denser set that clearly reveals the trend).
- Output file: `/app/outputs/tc_values.csv`
- Format: csv
- Contract: CSV with columns: 'Co_concentration' (float, atomic fraction y) and 'Tc' (float, temperature in Kelvin).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/configurational_coefficients.json`
- `/app/outputs/tc_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### configurational_coefficients.json
- path: `/app/outputs/configurational_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Configurational energy coefficients ε1, ε2, ε3 in eV/atom.
- schema:
  - `type`: object
  - `required`:
    - `epsilon1`: float (eV/atom)
    - `epsilon2`: float (eV/atom)
    - `epsilon3`: float (eV/atom)
  - `units`:
    - `epsilon1`: eV/atom
    - `epsilon2`: eV/atom
    - `epsilon3`: eV/atom

### tc_values.csv
- path: `/app/outputs/tc_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Order-disorder transition temperature Tc as a function of Co concentration.
- schema:
  - `type`: table
  - `required_columns`: `Co_concentration`, `Tc`
  - `units`:
    - `Co_concentration`: atomic fraction
    - `Tc`: K

Notes: The DFT energies file is an optional evidence artifact; it is not directly scored. The hidden checker compares the submitted coefficients and Tc values against reference values derived from the paper, using tolerances appropriate for toolchain variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "configurational_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon1": "float (eV/atom)",
          "epsilon2": "float (eV/atom)",
          "epsilon3": "float (eV/atom)"
        },
        "units": {
          "epsilon1": "eV/atom",
          "epsilon2": "eV/atom",
          "epsilon3": "eV/atom"
        }
      },
      "description": "Configurational energy coefficients ε1, ε2, ε3 in eV/atom."
    },
    {
      "file": "tc_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Co_concentration",
          "Tc"
        ],
        "units": {
          "Co_concentration": "atomic fraction",
          "Tc": "K"
        }
      },
      "description": "Order-disorder transition temperature Tc as a function of Co concentration."
    }
  ],
  "notes": "The DFT energies file is an optional evidence artifact; it is not directly scored. The hidden checker compares the submitted coefficients and Tc values against reference values derived from the paper, using tolerances appropriate for toolchain variation."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. Each required output file is scored independently: the configurational coefficients (configurational_coefficients.json) are compared against reference values using appropriate tolerances; the Tc table (tc_values.csv) is checked for a correct monotonic trend and numerically sensible magnitudes relative to hidden expectations. The individual scores are weighted and combined into a single final reward. Simply hardcoding numbers is not sufficient – you must execute the described DFT and free-energy workflow and produce the outputs through genuine computation.
