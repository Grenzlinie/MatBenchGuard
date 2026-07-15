# Calculation of Total and p_y-Orbital Density of States and Electronic Heat Capacity in Impure Chair-Like Graphane under Magnetic Field

## Problem background
Chair-like graphane is a fully hydrogenated monolayer of graphene in which the carbon atoms adopt sp³ hybridization, opening a band gap. Dilute charged impurities and an external in-plane magnetic field that couples to the electron spin modify the electronic structure, and this in turn alters the density of states (DOS) and the electronic heat capacity (EHC). Understanding how the orbital-resolved DOS — particularly the p_y orbital of carbon — and the EHC respond to impurity concentration, scattering strength, and magnetic field is important for evaluating graphane’s potential in nanoelectronic and thermoelectric applications. The present task is to compute the total and p_y-orbital DOS and EHC for chair-like graphane under a range of impurity and magnetic field conditions, so that derived quantities such as the band gap and the Schottky temperature can be quantified and compared.

## Approach
The electronic structure is described by a tight-binding Harrison model for the 20 orbitals (C 2s, 2p_x, 2p_y, 2p_z and H 1s, each with spin) in the chair-like graphane unit cell. The k-dependent Hamiltonian H(k) is built from the Harrison parametrization using the primitive lattice vectors a₁ and a₂, plus a Zeeman term gμ_B B σ_z that couples the external in-plane magnetic field to the electron spin. From this Hamiltonian, the non-interacting retarded Green’s function G₀(k, E) = [(E + i0⁺)I − H(k)]⁻¹ is constructed. Dilute charged impurities are treated within the self-consistent Born approximation (SCBA): the diagonal impurity self-energy Σ_αα(E) satisfies Σ_αα = n_i ν_i / [1 − ν_i G_αα(E + i0⁺ − Σ(E))] and is solved iteratively for each set of impurity concentration n_i and scattering strength ν_i. The disorder-renormalized Green’s function is then obtained via the Dyson equation: G(k, E) = [G₀⁻¹(k, E) − Σ(E)]⁻¹. From this interacting Green’s function, the total and p_y-orbital density of states are computed as D(E) = −(1/(10π N_c)) Σ_{μ,k} Im G_μμ(k, E), and the electronic heat capacity is evaluated from C(T) = −(1/(10π N_c T²)) Σ_{μ,k} Im ∫ dE [E² e^{E/k_B T}/(e^{E/k_B T}+1)²] G_μμ(k, E). The workflow produces DOS and EHC curves for a series of parameter sets that span different impurity concentrations, scattering potential strengths, and magnetic field values.

## Reproduction target
Compute, for the parameter combinations listed at the end of this instruction, the total density of states (DOS), the p_y-orbital DOS of carbon atoms, the total electronic heat capacity (EHC), and the p_y-orbital EHC. Store the results in a single JSON file (`dos_ehc_results.json`) that contains, for each parameter set, arrays of energy values (in eV) and temperature values (in K), together with the corresponding DOS and EHC arrays. From these curves, one should be able to extract the band gap (the energy interval where the total DOS is essentially zero) and the Schottky temperature (the temperature of the peak in the total EHC). The task is considered complete when the JSON file with the specified structure is written under `/app/outputs/`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Construct tight-binding Hamiltonian
- Role: process
- Action: Assemble the 20×20 k-dependent Hamiltonian matrix H(k) for chair-like graphane using the Harrison parametrization (provided in the instruction), lattice vectors a1, a2, and the Zeeman spin coupling. The Hamiltonian includes all orbitals: carbon 2s, 2px, 2py, 2pz and hydrogen 1s with spin.
- Evidence: none

### Step 2: Compute non-interacting Green's function
- Role: process
- Action: Construct the non-interacting Matsubara Green's function G0(k, iω_n) = (iω_n I - H(k))^{-1} and analytically continue to the real energy axis (iω_n → E + i0+) to obtain the retarded Green's function G0(k, E).
- Evidence: none

### Step 3: Solve SCBA impurity self-energy
- Role: process
- Action: For each parameter set (impurity concentration n_i, scattering strength ν_i, magnetic field gμ_B B), solve the self-consistent Born approximation for the diagonal impurity self-energy Σ_αα(E) using the scalar equation Σ_αα = n_i ν_i / (1 - ν_i G_αα(E + i0+ - Σ(E))). Iterate until convergence.
- Evidence: none

### Step 4: Compute interacting retarded Green's function
- Role: process
- Action: Construct the disorder-renormalized Green's function G(k, E) = [G0^{-1}(k, E) - Σ(E)]^{-1} for each k-point and energy grid.
- Evidence: none

### Step 5: Calculate DOS and EHC
- Role: scored (load-bearing)
- Action: For each parameter set listed in the instruction (covering variations of impurity concentration, scattering strength, and magnetic field), compute the total DOS D(E) = -1/(10π N_c) Σ_{μ,k} Im G_μμ(k,E), the p_y-orbital DOS of carbon atoms, the total EHC C(T) = -1/(10π N_c T^2) Σ_{μ,k} Im ∫ dE (E^2 e^{E/k_B T}/(e^{E/k_B T}+1)^2) G_μμ(k,E), and the p_y-orbital EHC using appropriate prefactors. Write the results to 'dos_ehc_results.json' with the structure described in the output contract.
- Output file: `/app/outputs/dos_ehc_results.json`
- Format: json
- Contract: A JSON object with key 'parameter_sets' mapping to an array of objects. Each object has: 'label' (string), 'energy' (array of float, eV), 'total_dos' (array of float), 'total_ehc' (array of float), 'p_y_dos' (array of float), 'p_y_ehc' (array of float), 'temperature' (array of float, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_ehc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_ehc_results.json
- path: `/app/outputs/dos_ehc_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Submitted DOS and EHC curves for each parameter set. The checker will compute band gaps and Schottky temperatures from these curves and compare to hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `parameter_sets`: array
  - `items`:
    - `parameter_sets[*]`:
      - `type`: object
      - `required`:
        - `label`: string
        - `energy`: array of float (eV)
        - `total_dos`: array of float
        - `total_ehc`: array of float
        - `p_y_dos`: array of float
        - `p_y_ehc`: array of float
        - `temperature`: array of float (K)
  - `units`:
    - `energy`: eV
    - `temperature`: K

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_ehc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "parameter_sets": "array"
        },
        "items": {
          "parameter_sets[*]": {
            "type": "object",
            "required": {
              "label": "string",
              "energy": "array of float (eV)",
              "total_dos": "array of float",
              "total_ehc": "array of float",
              "p_y_dos": "array of float",
              "p_y_ehc": "array of float",
              "temperature": "array of float (K)"
            }
          }
        },
        "units": {
          "energy": "eV",
          "temperature": "K"
        }
      },
      "description": "Submitted DOS and EHC curves for each parameter set. The checker will compute band gaps and Schottky temperatures from these curves and compare to hidden reference values."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads the `dos_ehc_results.json` file and, for each parameter set, computes the band gap and the Schottky temperature from the submitted total and p_y-orbital curves. These derived quantities are compared against hidden reference values obtained from a reference implementation of the same model. Each submitted curve contributes to a weighted reward that reflects how closely the extracted band gap and Schottky temperature match the references. Reporting numbers that merely reproduce the paper’s values without producing the corresponding DOS and EHC curves will not pass, because the verifier recomputes the derived quantities directly from the submitted arrays. The final score is a single float between 0 and 1 that combines the deviations across all required parameter sets.

## Parameter sets appendix

The hidden checker expects `dos_ehc_results.json` to contain curves for the following parameter sweeps. Each entry in the `parameter_sets` array must have the exact `label` as specified.

### Sweep 1: Magnetic field dependence
Fixed parameters: impurity concentration \(n_i = 0.005\), scattering potential strength \(\nu_i/t_{p_z p_z}^\pi = 0.4\) (with \(t_{p_z p_z}^\pi = 3.033\,\text{eV}\)).  
Magnetic field values (in units of \(g\mu_B B / t_{p_z p_z}^\pi\)): 0, 0.1, 0.15, 0.3.  
Labels: `"B=0"`, `"B=0.1"`, `"B=0.15"`, `"B=0.3"`.

### Sweep 2: Impurity concentration dependence
Fixed parameters: magnetic field \(g\mu_B B/t_{p_z p_z}^\pi = 0.2\), scattering potential strength \(\nu_i/t_{p_z p_z}^\pi = 0.4\).  
Impurity concentration values (\(n_i\)): 0.005, 0.05, 0.2, 0.5.  
Labels: `"ni=0.005"`, `"ni=0.05"`, `"ni=0.2"`, `"ni=0.5"`.

### Sweep 3: Scattering potential strength dependence
Fixed parameters: magnetic field \(g\mu_B B/t_{p_z p_z}^\pi = 0.2\), impurity concentration \(n_i = 0.06\).  
Scattering potential strength values (\(\nu_i/t_{p_z p_z}^\pi\)): 0.05, 0.6, 1, 2.  
Labels: `"nu/t=0.05"`, `"nu/t=0.6"`, `"nu/t=1"`, `"nu/t=2"`.
