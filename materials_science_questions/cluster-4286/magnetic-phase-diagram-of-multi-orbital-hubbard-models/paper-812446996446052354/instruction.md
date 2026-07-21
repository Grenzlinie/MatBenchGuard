# Optimized single‑hole cluster properties and phase boundaries in doped cuprate

## Problem background
The ground state of doped holes in the high‑Tc cuprate (La1−xSrx)2CuO4 is investigated by a variational analysis on the Anderson lattice Hamiltonian for the CuO2 sheet. The central physical question is the spatial localization and energy of a single hole introduced on the oxygen sublattice, and how the antiferromagnetic background and the conductivity evolve with doping. Understanding these phases provides insight into the mechanism of superconductivity.

## Approach
The analysis considers a single doped hole residing on oxygen sites of the CuO2 plane, with the copper spins forming a Heisenberg antiferromagnet in the undoped limit. A trial wave function is assumed in which the hole is spread over a linear cluster of n oxygen sites oriented at 45° to the copper–oxygen bonds. The energy shift ΔE of the system relative to the undoped state is obtained by summing three contributions: (i) a copper–oxygen hybridization term arising from virtual hopping between the cluster and copper 3d orbitals, (ii) an oxygen–oxygen direct hopping term, and (iii) the energy cost of breaking antiferromagnetic correlations (links) disrupted by the hole cluster. The size n of the cluster is treated as a continuous variable, and the optimal value is found by minimizing ΔE. From the optimized cluster, the thermal hopping barrier v and the critical doping densities that mark transitions among the antiferromagnetic, spin‑glass, liquid, and alloy phases are derived. The method is entirely analytic; the solver must implement the variational energy expression and the phase‑boundary formulas using the supplied model parameters.

## Reproduction target
Compute the optimal single‑hole cluster size n, its formation energy ΔE, the thermal hopping barrier v (the energy required to move a hole between neighbouring clusters), and the critical doping densities x_AF‑SG (AF to spin‑glass), x_SG‑L (spin‑glass to liquid), and x_L‑A (liquid to alloy) from the variational model. The model parameters to use are: t1 = 0.2 eV, t2 = 1.0 eV, εp − εd = 4 eV, U = 7 eV, J = 0.12 eV. The quantities must be written to a JSON file as described in the workflow steps.

## Assets
None. The task requires only the model parameter values listed in the workflow steps; no external datasets, pre‑trained models, or special software packages are needed. The solver may implement the variational energy minimisation and the algebraic expressions for the phase boundaries using standard scientific computing libraries (e.g., numpy, scipy) that are freely available.

## Workflow steps

### Step 1: Compute variational cluster properties and phase boundaries
- Role: scored
- Action: Using the given model parameters (t1=0.2 eV, t2=1.0 eV, εp−εd=4 eV, U=7 eV, J=0.12 eV), form the total variational energy ΔE(n) = –2 t1 + (t2²/(εd+U–εp))·(3/n – 4) + 2 t2²/(n·(εp–εd)) + 0.19 n J. Minimize with respect to n to obtain the optimal cluster size n and the formation energy ΔE. Then compute v = 0.19 J, x_AF_SG = 1/n², ε_link = 0.19 J, ε_bond = 0.75 J, and the critical doping densities x_SG_L = max(ε_link/(4 t1), (3 ε_link)/(4 t1 + 8 n ε_link)) and x_L_A = ε_bond/(4 t1). Write all six values to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: { "n": float, "Delta_E": float, "v": float, "x_AF_SG": float, "x_SG_L": float, "x_L_A": float }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The JSON file contains the six headline quantities of the variational analysis: optimal single‑hole cluster size n, its formation energy ΔE, the thermal hopping barrier v, and the critical doping densities x_AF_SG, x_SG_L, x_L_A. All values are computed from the specified literature parameters using the analytic expressions derived in the paper.
- schema:
  - `type`: object
  - `required`:
    - `n`: float
    - `Delta_E`: float
    - `v`: float
    - `x_AF_SG`: float
    - `x_SG_L`: float
    - `x_L_A`: float
  - `units`:
    - `n`: dimensionless
    - `Delta_E`: eV
    - `v`: eV
    - `x_AF_SG`: dimensionless
    - `x_SG_L`: dimensionless
    - `x_L_A`: dimensionless

Notes: The solver is expected to implement the variational energy and evaluate the closed‑form expressions at the given parameter set. No external dataset or model is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "n": "float",
          "Delta_E": "float",
          "v": "float",
          "x_AF_SG": "float",
          "x_SG_L": "float",
          "x_L_A": "float"
        },
        "units": {
          "n": "dimensionless",
          "Delta_E": "eV",
          "v": "eV",
          "x_AF_SG": "dimensionless",
          "x_SG_L": "dimensionless",
          "x_L_A": "dimensionless"
        }
      },
      "description": "The JSON file contains the six headline quantities of the variational analysis: optimal single‑hole cluster size n, its formation energy ΔE, the thermal hopping barrier v, and the critical doping densities x_AF_SG, x_SG_L, x_L_A. All values are computed from the specified literature parameters using the analytic expressions derived in the paper."
    }
  ],
  "notes": "The solver is expected to implement the variational energy and evaluate the closed‑form expressions at the given parameter set. No external dataset or model is required."
}
```

## How you are scored
A hidden verifier reads the file `/app/outputs/results.json` and compares the six numeric fields (n, ΔE, v, x_AF_SG, x_SG_L, x_L_A) to reference values obtained from a correct implementation of the variational model with the same parameter set. Each field is checked individually, and credit is awarded when the computed value falls within the expected numerical tolerance of the reference. Full credit requires all fields to meet the tolerance; partial credit is proportional to the number of correctly computed fields. The verifier does not inspect the source code, only the output file.
