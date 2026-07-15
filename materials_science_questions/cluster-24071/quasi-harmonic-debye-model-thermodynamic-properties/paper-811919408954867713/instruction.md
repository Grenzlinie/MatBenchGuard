# First-principles study of pressure-induced phase transition and elastic properties in SiC

## Problem background
Silicon carbide (SiC) is a technologically important wide-bandgap semiconductor that undergoes a pressure-induced structural phase transition from the cubic zinc blende (ZB) to the cubic rocksalt (RS) phase. Accurately predicting the transition pressure, volume change, elastic constants, and the mechanical stability limit of the ZB phase is fundamental for understanding SiC's behavior under extreme conditions and for validating first-principles computational methods. The key quantity to determine is the zero-temperature transition pressure, which can be obtained from total-energy volume data and enthalpy equality. Additionally, the pressure dependence of elastic constants provides the pressure at which the ZB structure becomes mechanically unstable, and the quasi-harmonic Debye model extends the equation of state to finite temperatures, giving the relative volume as a function of pressure at T = 0 K and T = 1400 K.

## Approach
The reproduction uses plane-wave pseudopotential density functional theory (DFT) with the Perdew-Wang 1991 generalized gradient approximation (GGA-PW91) and ultrasoft pseudopotentials. Constant-pressure simulations are performed for both ZB and RS structures over a range of volumes to obtain total energy vs volume curves E(V). A Birch-Murnaghan equation of state is fitted to extract equilibrium lattice constant, bulk modulus, and its pressure derivative for each phase. The zero-temperature transition pressure is determined by two methods: the slope of the common tangent to the E(V) curves, and the pressure at which the enthalpies H = E + PV of the two phases are equal; the volume reduction and relative volumes at the transition are computed. For the ZB structure, elastic constants C11, C12, C44 are computed at zero pressure and at a series of applied pressures using the stress-strain method. From these, the pressure-dependent difference ΔC11−12 = (C11−P) − |C12 + P| is calculated; a quadratic fit to ΔC11−12(P) and its zero-crossing gives the mechanical instability pressure. Finally, a quasi-harmonic Debye model (using the static E(V) data) is employed to obtain the relative volume V/V0 as a function of pressure at T = 0 K and T = 1400 K for both phases. The entire workflow uses an open-source DFT code (Quantum ESPRESSO) and the Gibbs2 Debye model code.

## Reproduction target
Produce the following verifiable artifacts from first-principles calculations:
- Equilibrium lattice constants (a in Å), zero-pressure bulk moduli (B0 in GPa), and pressure derivatives B0' for both ZB and RS structures.
- Zero-temperature phase transition pressure from ZB to RS via the common tangent method and via enthalpy equality, the volume reduction (ΔV/V in %), the transition volumes relative to the equilibrium ZB volume (Vt/V0 for ZB and RS), and the equilibrium ZB volume V0 in Bohrs.
- Elastic constants C11, C12, C44 (in GPa) at zero pressure for ZB and RS, and their pressure dependence for ZB up to ~140 GPa.
- The pressure at which the ZB structure becomes mechanically unstable, determined from the vanishing of ΔC11−12, together with the quadratic fit coefficients.
- Relative volume V/V0 as a function of pressure at T = 0 K and T = 1400 K for both phases, for pressures from 0 to at least 100 GPa.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSlibrary pseudopotentials for GGA-PW91 (Si and C): https://www.quantum-espresso.org/pseudopotentials
- Gibbs2 quasi-harmonic Debye model code: http://gibbs2.sourceforge.net/
- Crystal structures of zinc blende and rocksalt SiC

## Workflow steps

### Step 1: DFT total-energy vs volume calculations
- Role: process
- Action: Run constant-pressure ab initio simulations for zinc blende (ZB) and rocksalt (RS) structures of SiC using an open-source DFT code (e.g., Quantum ESPRESSO) with GGA-PW91 functional and ultrasoft pseudopotentials. Converge total energy vs. primitive cell volume over a range of pressures to obtain E(V) data.
- Evidence: `/app/outputs/energy_volume.csv`

### Step 2: Equation of state fitting and equilibrium properties
- Role: scored
- Action: Fit the Birch-Murnaghan equation of state to the E-V data for ZB and RS to obtain equilibrium lattice constant a (Å), zero-pressure bulk modulus B0 (GPa), and its pressure derivative B0'.
- Output file: `/app/outputs/eos_properties.json`
- Format: json
- Contract: {"ZB": {"a_Angstrom": float, "B0_GPa": float, "B0_prime": float}, "RS": {"a_Angstrom": float, "B0_GPa": float, "B0_prime": float}}
- Scoring: scored by hidden verifier

### Step 3: Phase transition pressure and volume analysis
- Role: scored (load-bearing)
- Action: Using the E-V data and the equilibrium ZB volume, compute the zero-temperature transition pressure from ZB to RS by the common tangent method and the equal-enthalpy method, and determine the volume reduction and relative volumes V_t/V_0.
- Output file: `/app/outputs/transition_parameters.json`
- Format: json
- Contract: {"transition_pressure_common_tangent_GPa": float, "transition_pressure_enthalpy_GPa": float, "volume_reduction_percent": float, "Vt_over_V0_ZB": float, "Vt_over_V0_RS": float, "V0_ZB_Bohr3": float}
- Scoring: scored by hidden verifier

### Step 4: DFT elastic constant calculations for ZB under pressure
- Role: process
- Action: Using the same DFT setup, compute elastic constants C11, C12, C44 for the ZB structure at zero pressure and at a series of applied pressures via the stress-strain method.
- Evidence: `/app/outputs/elastic_constants_raw.csv`

### Step 5: Elastic constants analysis
- Role: scored (load-bearing)
- Action: Compile C11, C12, C44 (in GPa) for ZB and RS at zero pressure and as a function of pressure for ZB.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"ZB_at_0GPa": {"C11_GPa": float, "C12_GPa": float, "C44_GPa": float}, "RS_at_0GPa": {"C11_GPa": float, "C12_GPa": float, "C44_GPa": float}, "ZB_pressure_dependence": [{"pressure_GPa": float, "C11_GPa": float, "C12_GPa": float, "C44_GPa": float}]}
- Scoring: scored by hidden verifier

### Step 6: Mechanical stability analysis of ZB SiC
- Role: scored (load-bearing)
- Action: From the pressure-dependent elastic constants, compute the pressure-corrected difference ΔC11-12 = Č11 - |Č12| (using Č11 = C11 - P, Č12 = C12 + P), fit a quadratic polynomial, and find the pressure where ΔC11-12 = 0.
- Output file: `/app/outputs/stability_analysis.json`
- Format: json
- Contract: {"pressure_unstable_GPa": float, "Delta_C11_12_fit": {"intercept": float, "linear_coeff": float, "quadratic_coeff": float}}
- Scoring: scored by hidden verifier

### Step 7: Quasi-harmonic Debye model calculations
- Role: process
- Action: Run the Gibbs2 quasi-harmonic Debye model code using the static E-V data for ZB and RS structures to compute the relative volume V/V0 as a function of pressure at T=0 K and T=1400 K.
- Evidence: `/app/outputs/debye_raw_output.csv`

### Step 8: Pressure-volume curves from Debye model
- Role: scored
- Action: From the Debye model results, extract the relative volume V/V0 as a function of pressure for T=0 K and T=1400 K.
- Output file: `/app/outputs/eos_curves.csv`
- Format: csv
- Contract: temperature_K (float), pressure_GPa (float), V_over_V0 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_properties.json`
- `/app/outputs/transition_parameters.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/stability_analysis.json`
- `/app/outputs/eos_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_properties.json
- path: `/app/outputs/eos_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constants, bulk moduli, and pressure derivatives for ZB and RS structures.
- schema:
  - `type`: object
  - `required`: `ZB`, `RS`
  - `properties`:
    - `ZB`:
      - `type`: object
      - `required`: `a_Angstrom`, `B0_GPa`, `B0_prime`
    - `RS`:
      - `type`: object
      - `required`: `a_Angstrom`, `B0_GPa`, `B0_prime`

### transition_parameters.json
- path: `/app/outputs/transition_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero-temperature transition pressure (common tangent and enthalpy methods), volume reduction, and relative volumes.
- schema:
  - `type`: object
  - `required`: `transition_pressure_common_tangent_GPa`, `transition_pressure_enthalpy_GPa`, `volume_reduction_percent`, `Vt_over_V0_ZB`, `Vt_over_V0_RS`, `V0_ZB_Bohr3`

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero-pressure elastic constants for ZB and RS, and pressure-dependent elastic constants for ZB.
- schema:
  - `type`: object
  - `required`: `ZB_at_0GPa`, `RS_at_0GPa`, `ZB_pressure_dependence`
  - `properties`:
    - `ZB_at_0GPa`:
      - `type`: object
      - `required`: `C11_GPa`, `C12_GPa`, `C44_GPa`
    - `RS_at_0GPa`:
      - `type`: object
      - `required`: `C11_GPa`, `C12_GPa`, `C44_GPa`
    - `ZB_pressure_dependence`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `pressure_GPa`, `C11_GPa`, `C12_GPa`, `C44_GPa`

### stability_analysis.json
- path: `/app/outputs/stability_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Mechanical instability pressure of ZB SiC and the quadratic fit coefficients for ΔC11-12(P).
- schema:
  - `type`: object
  - `required`: `pressure_unstable_GPa`, `Delta_C11_12_fit`
  - `properties`:
    - `Delta_C11_12_fit`:
      - `type`: object
      - `required`: `intercept`, `linear_coeff`, `quadratic_coeff`

### eos_curves.csv
- path: `/app/outputs/eos_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative volume V/V0 as a function of pressure at T=0 and 1400 K; compared against the paper's reference curve at specific pressure points.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_GPa`, `V_over_V0`

Notes: All scored quantities are compared against the paper's reported values with appropriate tolerances. The hidden gold values are taken from the paper's text and tables.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "ZB",
          "RS"
        ],
        "properties": {
          "ZB": {
            "type": "object",
            "required": [
              "a_Angstrom",
              "B0_GPa",
              "B0_prime"
            ]
          },
          "RS": {
            "type": "object",
            "required": [
              "a_Angstrom",
              "B0_GPa",
              "B0_prime"
            ]
          }
        }
      },
      "description": "Equilibrium lattice constants, bulk moduli, and pressure derivatives for ZB and RS structures."
    },
    {
      "file": "transition_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "transition_pressure_common_tangent_GPa",
          "transition_pressure_enthalpy_GPa",
          "volume_reduction_percent",
          "Vt_over_V0_ZB",
          "Vt_over_V0_RS",
          "V0_ZB_Bohr3"
        ]
      },
      "description": "Zero-temperature transition pressure (common tangent and enthalpy methods), volume reduction, and relative volumes."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "ZB_at_0GPa",
          "RS_at_0GPa",
          "ZB_pressure_dependence"
        ],
        "properties": {
          "ZB_at_0GPa": {
            "type": "object",
            "required": [
              "C11_GPa",
              "C12_GPa",
              "C44_GPa"
            ]
          },
          "RS_at_0GPa": {
            "type": "object",
            "required": [
              "C11_GPa",
              "C12_GPa",
              "C44_GPa"
            ]
          },
          "ZB_pressure_dependence": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "pressure_GPa",
                "C11_GPa",
                "C12_GPa",
                "C44_GPa"
              ]
            }
          }
        }
      },
      "description": "Zero-pressure elastic constants for ZB and RS, and pressure-dependent elastic constants for ZB."
    },
    {
      "file": "stability_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "pressure_unstable_GPa",
          "Delta_C11_12_fit"
        ],
        "properties": {
          "Delta_C11_12_fit": {
            "type": "object",
            "required": [
              "intercept",
              "linear_coeff",
              "quadratic_coeff"
            ]
          }
        }
      },
      "description": "Mechanical instability pressure of ZB SiC and the quadratic fit coefficients for ΔC11-12(P)."
    },
    {
      "file": "eos_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_GPa",
          "V_over_V0"
        ]
      },
      "description": "Relative volume V/V0 as a function of pressure at T=0 and 1400 K; compared against the paper's reference curve at specific pressure points."
    }
  ],
  "notes": "All scored quantities are compared against the paper's reported values with appropriate tolerances. The hidden gold values are taken from the paper's text and tables."
}
```

## How you are scored
A hidden automated verifier checks each scored output independently. For each stage, the verifier compares your computed numeric values (or curves at specified pressure points) against a set of hidden reference values with pre-defined tolerances. Credits are combined into a final reward in [0,1] according to weights assigned to each stage. The check is a result-level comparison: the verifier does NOT re-run your simulations or re-fit any equations; it reads your reported numbers and assesses how close they are to the hidden targets. Submitting numbers that happen to be close to the reference is not sufficient — the workflow must produce them from the pipeline described. The verifier will penalize outputs that are out of tolerance, missing, or structurally malformed.
