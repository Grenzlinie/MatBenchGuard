# Quasi-harmonic Debye Model Thermodynamics of AlB₂-type WB₂

## Problem background
The thermal properties of AlB₂-type WB₂, particularly the volumetric thermal expansion coefficient and heat capacity, are essential for engineering applications such as hard coatings, where thermal mismatch between coating and substrate can affect adhesion. Experimental data for this compound is scarce because it is only stable at high temperature and pressure, making it difficult to obtain bulk samples. A practical alternative is to predict these properties using the quasi-harmonic Debye model combined with first-principles density functional theory (DFT). This approach can provide reliable thermal expansion and heat capacity values over a wide temperature range, serving as a computational substitute for measurements.

## Approach
The reproduction follows a two-stage computational workflow. In the first stage, plane-wave pseudopotential DFT calculations with the GGA-PBE exchange-correlation functional are performed on the AlB₂-type WB₂ crystal structure to obtain the total energy as a function of volume (the E(V) curve) and the five independent elastic constants of the hexagonal lattice. The elastic constants are then used to compute the polycrystalline bulk and shear moduli via the Voigt-Reuss-Hill averaging scheme, from which the Poisson ratio is derived. In the second stage, the E(V) data and the Poisson ratio are fed into the quasi-harmonic Debye model, which minimizes the non-equilibrium Gibbs free energy with respect to volume at each temperature to obtain the equilibrium volume. From the thermal equation of state, the volumetric thermal expansion coefficient α and the constant-volume heat capacity C_V are extracted as functions of temperature at zero pressure. The model also yields the average volumetric thermal expansion coefficient over a specified temperature range. All steps are performed with publicly available open-source codes and pseudopotentials; the crystal structure parameters are taken from the literature.

## Reproduction target
The goal is to execute the DFT + quasi-harmonic Debye pipeline to compute the thermal properties of AlB₂-type WB₂ and produce the following artifacts:

1. **Poisson ratio** from DFT elastic constants, written to `poisson_ratio.json`.
2. **Average volumetric thermal expansion coefficient α_V** (in units of 10⁻⁶ K⁻¹) over the temperature interval 298–473 K at zero pressure, written to `alpha_V_avg.txt`.
3. **Temperature-dependent thermal expansion α and heat capacity C_V** at 0 GPa for the temperatures 300, 500, 1000, 1500, and 2000 K, saved as `thermal_properties.csv`.

The reported average α_V should be a physically meaningful positive value. The temperature-dependent α(T) should increase with temperature, and C_V(T) should approach the classical Dulong-Petit limit at high temperatures. The hidden verifier compares your computed results to reference data derived from first-principles calculations.

## Assets

- Quantum ESPRESSO (plane-wave DFT code): https://www.quantum-espresso.org/
- GIBBS2: http://gibbs2.uniovi.es/
- Pseudopotentials for W and B (SSSP efficiency or PseudoDojo): https://www.materialscloud.org/discover/sssp/table/pseudopotential/efficiency
- AlB₂-type WB₂ crystal structure parameters

## Workflow steps

### Step 1: DFT calculations (geometry optimization, E(V) curve, elastic constants)
- Role: process
- Action: Perform DFT geometry optimization of AlB₂-type WB₂ using GGA-PBE with plane-wave pseudopotentials. Compute the equilibrium lattice constants, then generate an energy vs. volume curve for a set of volumes (with fixed c/a ratio). Additionally, compute the five independent elastic constants C_ij via the stress-strain method. Save the E(V) data and elastic constants for later steps.
- Evidence: `/app/outputs/energy_volume.dat`

### Step 2: Poisson ratio from elastic constants
- Role: scored
- Action: Using the elastic constants obtained in step 1, compute the Voigt, Reuss, and Hill bulk (B_V, B_R, B_H) and shear (G_V, G_R, G_H) moduli. Calculate the Poisson ratio ν = (3B_H - 2G_H) / [2(3B_H + G_H)]. Write the values to poisson_ratio.json with keys 'nu', 'B_H', 'G_H'.
- Output file: `/app/outputs/poisson_ratio.json`
- Format: json
- Contract: {"nu": <float>, "B_H": <float>, "G_H": <float>}
- Scoring: scored by hidden verifier

### Step 3: Average volumetric thermal expansion coefficient
- Role: scored (load-bearing)
- Action: Run the quasi-harmonic Debye model (e.g., using GIBBS2 code) with the E(V) data and Poisson ratio ν. Compute the equilibrium volume V(T) at zero pressure over 298–473 K and derive the average volumetric thermal expansion coefficient α_V. Write the single value (in 10⁻⁶ K⁻¹) to alpha_V_avg.txt.
- Output file: `/app/outputs/alpha_V_avg.txt`
- Format: txt
- Contract: single float (e.g., 24.86)
- Scoring: scored by hidden verifier

### Step 4: Temperature-dependent thermal properties
- Role: scored
- Action: From the same GIBBS2 simulation, extract the thermal expansion α and constant-volume heat capacity C_V at 0 GPa for T = 300, 500, 1000, 1500, 2000 K. Save the data as a CSV file with columns T(K), alpha(10⁻⁶ K⁻¹), C_V(J/mol-K).
- Output file: `/app/outputs/thermal_properties.csv`
- Format: csv
- Contract: columns: T(K), alpha(10⁻⁶ K⁻¹), C_V(J/mol-K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/poisson_ratio.json`
- `/app/outputs/alpha_V_avg.txt`
- `/app/outputs/thermal_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### poisson_ratio.json
- path: `/app/outputs/poisson_ratio.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Poisson ratio ν and the Hill-averaged bulk and shear moduli.
- schema:
  - `type`: object
  - `required`:
    - `nu`: number
    - `B_H`: number (GPa)
    - `G_H`: number (GPa)

### alpha_V_avg.txt
- path: `/app/outputs/alpha_V_avg.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Average volumetric thermal expansion coefficient over 298–473 K at 0 GPa.
- schema:
  - `type`: text
  - `description`: single float value (×10⁻⁶ K⁻¹)

### thermal_properties.csv
- path: `/app/outputs/thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature-dependent thermal expansion and heat capacity at zero pressure; checked for monotonic alpha(T) and C_V approaching Dulong-Petit limit.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `alpha(10⁻⁶ K⁻¹)`, `C_V(J/mol-K)`
  - `units`:
    - `T(K)`: K
    - `alpha(10⁻⁶ K⁻¹)`: 10⁻⁶ K⁻¹
    - `C_V(J/mol-K)`: J/(mol·K)

Notes: Reproduces the computational pipeline (DFT + quasi-harmonic Debye model) from the paper. Scored artifacts include Poisson ratio, average volumetric expansion coefficient, and temperature scan. Process steps force genuine DFT and Debye simulations, not self-reported numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "poisson_ratio.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "nu": "number",
          "B_H": "number (GPa)",
          "G_H": "number (GPa)"
        }
      },
      "description": "Poisson ratio ν and the Hill-averaged bulk and shear moduli."
    },
    {
      "file": "alpha_V_avg.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "single float value (×10⁻⁶ K⁻¹)"
      },
      "description": "Average volumetric thermal expansion coefficient over 298–473 K at 0 GPa."
    },
    {
      "file": "thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "alpha(10⁻⁶ K⁻¹)",
          "C_V(J/mol-K)"
        ],
        "units": {
          "T(K)": "K",
          "alpha(10⁻⁶ K⁻¹)": "10⁻⁶ K⁻¹",
          "C_V(J/mol-K)": "J/(mol·K)"
        }
      },
      "description": "Temperature-dependent thermal expansion and heat capacity at zero pressure; checked for monotonic alpha(T) and C_V approaching Dulong-Petit limit."
    }
  ],
  "notes": "Reproduces the computational pipeline (DFT + quasi-harmonic Debye model) from the paper. Scored artifacts include Poisson ratio, average volumetric expansion coefficient, and temperature scan. Process steps force genuine DFT and Debye simulations, not self-reported numbers."
}
```

## How you are scored
A hidden verifier checks each scored artifact independently and assigns a reward based on the agreement with a reference and on physical plausibility. For `poisson_ratio.json`, the verifier confirms that the Poisson ratio is consistent with the supplied bulk and shear moduli and falls within an acceptable range. For `alpha_V_avg.txt`, the reported average thermal expansion coefficient is compared to a hidden reference value obtained from a trusted computational protocol. For `thermal_properties.csv`, the verifier inspects the structural properties of the data: α must increase monotonically with temperature, and C_V must rise toward the Dulong-Petit limit at high temperature. The total reward is a weighted combination of these checks. Simply reporting a known number without performing the required DFT and Debye model runs will not produce a valid submission, because the verifier also requires self-consistency among the artifacts and physical trends that cannot be fabricated without the underlying calculations.
