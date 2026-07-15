# Hubbard Dimer Thermodynamics and Caloric Effects

## Problem background
The Hubbard dimer is a fundamental model system for understanding electron correlation and thermodynamics in a pair of sites. When placed in external magnetic and electric fields, it exhibits rich behavior including magnetocaloric and electrocaloric effects. The system is treated in the grand canonical ensemble, allowing electron exchange with a reservoir, and its equilibrium properties are obtained by exact diagonalization of the 16-dimensional Hamiltonian. The primary goal is to compute the thermodynamic and caloric quantities—entropy, specific heat, magnetization, electric polarization, isothermal entropy changes for both magnetocaloric and electrocaloric effects, and the magnetic and electric Grüneisen ratios—at half-filling of the energy states (electron concentration x = 1). These quantities are to be evaluated for specified normalized external field and temperature parameters, providing a numerical map of the dimer's response.

## Approach
The Hubbard dimer is described by a Hamiltonian containing a hopping term between the two sites (with strength t > 0), an on-site Coulomb repulsion U ≥ 0, and couplings to external uniform magnetic field H (through spin z-component) and uniform electric field E (via an electrostatic potential difference V = E|e|d/2 between the sites). In the grand canonical ensemble, the Hamiltonian is extended with a chemical potential μ to control electron concentration. The 16 eigenenergies are obtained by numerically diagonalizing the 16×16 Hamiltonian matrix. From these eigenenergies, the grand partition function Z and grand potential Ω are calculated, yielding the entropy S = −(∂Ω/∂T)_{H,E}. The specific heat C = T(∂S/∂T) is computed from the variance of the Hamiltonian. The total magnetization M = ⟨S_a^z⟩ + ⟨S_b^z⟩ and total electric polarization P are obtained as expectation values of the corresponding operators. The magnetocaloric (ΔS_T^MCE) and electrocaloric (ΔS_T^ECE) isothermal entropy changes are defined as the entropy difference between zero and non-zero final values of the respective field, at constant temperature and the other field. The magnetic Grüneisen ratio Γ_H = −(1/C)(∂M/∂T)_{H,E} = −(1/C)(∂S/∂H)_{T,E} and electric Grüneisen ratio Γ_E = −(1/C)(∂P/∂T)_{H,E} = −(1/C)(∂S/∂E)_{T,H} are computed using finite differences. At half-filling (x = 1), the chemical potential is exactly μ = U/2 independent of temperature and fields. All computations are performed for normalized quantities (energies in units of t, magnetization in units of gμ_B, etc.) as specified in the steps.

## Reproduction target
Compute, using exact diagonalization, the thermodynamic and caloric properties listed above for the Hubbard dimer at half-filling (electron concentration x = 1) for the following normalized parameter conditions:

| condition_id | U/t | H/t | E|e|d/t | k_B T/t |
|--------------|-----|-----|----------|----------|
| cond1        | 2.0 | 0.0 | 0.0      | 0.1      |
| cond2        | 2.0 | 1.5 | 0.0      | 0.2      |
| cond3        | 5.0 | 0.0 | 0.0      | 0.1      |
| cond4        | 5.0 | 1.5 | 0.0      | 0.2      |
| cond5        | 2.0 | 2.0 | 2.0      | 0.1      |
| cond6        | 2.0 | 2.0 | 5.0      | 0.1      |
| cond7        | 5.0 | 2.0 | 0.0      | 0.05     |
| cond8        | 2.0 | 0.0 | 3.0      | 0.15     |

For each condition, output all the required quantities (eigenenergies, grand partition, entropy, specific heat, magnetization, polarization, ΔS_MCE, ΔS_ECE, Γ_H, Γ_E) in the structured JSON file as specified in the workflow steps. The isothermal entropy changes ΔS_MCE and ΔS_ECE correspond to jumps from H=0 to the listed final H (for ΔS_MCE) and from E=0 to the listed final E (for ΔS_ECE), respectively, at the constant temperature and the other field fixed as given. The Grüneisen ratios are to be evaluated at the listed condition.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Exact diagonalization of Hubbard dimer
- Role: process
- Action: Implement the two-site Hubbard Hamiltonian in the grand canonical ensemble for given parameters (t, U, H, V, mu) according to the paper's model. Construct the 16x16 Hamiltonian matrix in a suitable basis and diagonalize numerically (e.g., using numpy.linalg.eigh) to obtain the 16 normalized eigenenergies E_i.
- Evidence: `/app/outputs/eigenenergies.json`

### Step 2: Compute thermodynamic and caloric quantities
- Role: scored (load-bearing)
- Action: For each specified parameter condition (normalized values of U/t, H/t, E|e|d/t, k_B T/t, and electron concentration x, provided in the instruction), use the eigenenergies from the previous step to compute the grand partition function, grand potential, entropy, specific heat, magnetization, electric polarization, isothermal entropy changes for MCE and ECE, and magnetic and electric Grüneisen ratios. Output all quantities for each condition in a single JSON file.
- Output file: `/app/outputs/hubbard_dimer_results.json`
- Format: json
- Contract: A JSON object with a top-level key 'conditions' whose value is an array. Each element of the array is an object with the following fields: condition_id (string), eigenenergies (list of 16 floats, normalized to t), grand_partition (float), entropy (float, S/k_B), specific_heat (float, C/k_B), magnetization (float, total M), polarization (float, total P), deltaS_MCE (float), deltaS_ECE (float), magnetic_Gruneisen_ratio (float, Γ_H*t), electric_Gruneisen_ratio (float, Γ_E*t/(|e|d)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hubbard_dimer_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hubbard_dimer_results.json
- path: `/app/outputs/hubbard_dimer_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed thermodynamic and caloric quantities for the Hubbard dimer at specified parameter conditions. Each scalar must be reported for the exact condition defined in the instruction (e.g., U/t, H/t, E|e|d/t, k_B T/t, x). All quantities are computed in the grand canonical ensemble at half-filling (x=1) as per the paper's main analysis. The checker will compare each value to hidden gold references within appropriate relative tolerances: 1e-5 for normalized energies and 1e-4 for other quantities.
- schema:
  - `type`: object
  - `required`:
    - `conditions`: array
  - `items`:
    - `condition_id`: string
    - `eigenenergies`: array[16] of float
    - `grand_partition`: float
    - `entropy`: float
    - `specific_heat`: float
    - `magnetization`: float
    - `polarization`: float
    - `deltaS_MCE`: float
    - `deltaS_ECE`: float
    - `magnetic_Gruneisen_ratio`: float
    - `electric_Gruneisen_ratio`: float
  - `units`:
    - `entropy`: S/k_B
    - `specific_heat`: C/k_B
    - `magnetization`: total M
    - `polarization`: total P
    - `deltaS_MCE`: -
    - `deltaS_ECE`: -
    - `magnetic_Gruneisen_ratio`: Γ_H*t
    - `electric_Gruneisen_ratio`: Γ_E*t/(|e|d)

Notes: The output file must contain an array of conditions as described. The parameter conditions themselves are provided in the instruction. The verification compares each reported scalar directly to gold values derived from the paper; no recomputation from eigenenergies is performed by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hubbard_dimer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "conditions": "array"
        },
        "items": {
          "condition_id": "string",
          "eigenenergies": "array[16] of float",
          "grand_partition": "float",
          "entropy": "float",
          "specific_heat": "float",
          "magnetization": "float",
          "polarization": "float",
          "deltaS_MCE": "float",
          "deltaS_ECE": "float",
          "magnetic_Gruneisen_ratio": "float",
          "electric_Gruneisen_ratio": "float"
        },
        "units": {
          "entropy": "S/k_B",
          "specific_heat": "C/k_B",
          "magnetization": "total M",
          "polarization": "total P",
          "deltaS_MCE": "-",
          "deltaS_ECE": "-",
          "magnetic_Gruneisen_ratio": "Γ_H*t",
          "electric_Gruneisen_ratio": "Γ_E*t/(|e|d)"
        }
      },
      "description": "Computed thermodynamic and caloric quantities for the Hubbard dimer at specified parameter conditions. Each scalar must be reported for the exact condition defined in the instruction (e.g., U/t, H/t, E|e|d/t, k_B T/t, x). All quantities are computed in the grand canonical ensemble at half-filling (x=1) as per the paper's main analysis. The checker will compare each value to hidden gold references within appropriate relative tolerances: 1e-5 for normalized energies and 1e-4 for other quantities."
    }
  ],
  "notes": "The output file must contain an array of conditions as described. The parameter conditions themselves are provided in the instruction. The verification compares each reported scalar directly to gold values derived from the paper; no recomputation from eigenenergies is performed by the checker."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads your hubbard_dimer_results.json and compares each reported scalar value for every condition to the expected reference values (derived from exact model calculations) using appropriate numerical tolerances. Each quantity is scored separately; the overall reward is the fraction of values that fall within tolerance, equally weighted across all conditions and quantities. You must implement the exact diagonalization and compute all quantities yourself using the procedure described; reporting arbitrary numbers or copying from any external source will not yield the correct values within the required tolerance and will result in a low or zero score. The scoring ensures that only a correct reimplementation of the model and its thermodynamic formulas achieves the expected precision.
