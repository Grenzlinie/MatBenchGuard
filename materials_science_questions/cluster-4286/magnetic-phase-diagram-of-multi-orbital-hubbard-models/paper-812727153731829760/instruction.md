# Antiferromagnetic ground state and BCS gap scaling in a correlated fermion model

## Problem background
Understanding high-temperature superconductivity in strongly correlated electron systems is challenging. The t-J model is a candidate minimal model for the cuprates, but its phase diagram is difficult to study analytically due to competition between nearest-neighbor hopping and antiferromagnetism. This work modifies the model to improve analytical control: nearest-neighbor hopping t is replaced by next-nearest-neighbor hopping t', the Heisenberg interaction J is replaced by an Ising antiferromagnetic coupling J_z, and a nearest-neighbor repulsion V is added (parametrized as V = 1/4 J_z − V0). In the strong-coupling limit V0 ≪ |t'| ≪ J_z, the ground state can become a fully polarized Ising antiferromagnet with only spin-up electrons on one sublattice and spin-down on the other, provided the electron filling is large enough. Projecting onto this antiferromagnetic subspace yields an effective Hamiltonian of spinless fermions with an attractive nearest-neighbor interaction V0, which can be treated by BCS mean-field theory. The task is to compute the critical filling n_c above which the antiferromagnetic ground state is stable, and to solve the BCS self-consistency equations to determine the superconducting order-parameter symmetry (d-wave or s-wave) and the gap scaling parameters ω and g0 for a range of fillings.

## Approach
The numerical workflow has two independent parts.

First, the spin-flip energy bound: in the limit V0 = 0, J_z = ∞, consider a square lattice with periodic boundary conditions. The fully-polarized antiferromagnet ground state energy E_{N,0}^{AF} with N electrons (all spin-up on sublattice A, spin-down on sublattice B) is a free-fermion problem. To bound the cost of a single spin flip, construct a state with one flipped spin and a constrained background; a lower bound on its energy is obtained by computing the free-fermion ground-state energy of the t' hopping Hamiltonian on a lattice where a small cluster of sites is forbidden (the “constrained free-fermion energy” \widetilde{E}_{N-1,0}^{AF}). The lower bound E^{flip}(N) ≥ −4|t'| + \widetilde{E}_{N-1,0}^{AF} − E_{N,0}^{AF} is computed as a function of filling. The critical filling n_c is the filling where this bound first becomes positive.

Second, the BCS calculation: for the effective Hamiltonian H_AF consisting only of next-nearest-neighbor hopping t' and attractive interaction −V0 ∑_{⟨ij⟩} n_i n_j, perform a BCS mean-field decoupling assuming the order parameter Δ_δ = V0 ⟨d_i d_{i+δ}⟩ with δ = x̂, ŷ. The order parameter symmetry can be s-wave (Δ_x = Δ_y) or d-wave (Δ_x = −Δ_y). For each filling, solve the BCS self-consistency equation in the weak-coupling limit (V0 ≪ |t'|) to find the symmetry that minimizes the ground-state energy. By varying the interaction strength V0, fit the gap magnitude |Δ| to the standard BCS form |Δ| = 2ω exp(-1/(V0 g0)) to extract the scaling parameters ω/|t'| and g0. The analysis is performed for both signs of t'.

## Reproduction target
Compute the lower bound on the spin‑flip energy E^{flip} as a function of electron filling fraction for the t'‑J_z‑V model in the limit V0=0, J_z=∞ on a sufficiently large square lattice with periodic boundary conditions. From this data, determine the critical filling n_c where the bound becomes positive, indicating a stable fully‑polarized antiferromagnetic ground state. Separately, solve the BCS self‑consistency equations for the effective attractive spinless‑fermion Hamiltonian, covering fillings from 0.1 to 0.9. For each filling and for both signs of the next‑nearest‑neighbor hopping t', determine which order‑parameter symmetry (d‑wave or s‑wave) gives the lowest ground‑state energy, and extract the gap scaling parameters ω/|t'| and g0 from the weak‑coupling scaling of the gap magnitude. All results must be written to the specified output files under /app/outputs.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute spin-flip energy lower bound
- Role: scored (load-bearing)
- Action: Implement the lower-bound computation for the spin-flip energy E^flip(N). Set V0=0, Jz=∞. Use a square lattice with periodic boundary conditions and a suitable size (e.g., 2×200×200). Compute the fully-polarized antiferromagnet ground-state energy E_{N,0}^{AF} and the constrained free-fermion energy \widetilde{E}_{N-1,0}^{AF} for a range of electron fillings. Output the resulting lower bound as a function of filling.
- Output file: `/app/outputs/flip_energy_bound.csv`
- Format: csv
- Contract: Columns: filling (float, electron filling fraction), E_flip_lower_bound (float, lower bound in units of |t'|). Rows for fillings from 0.1 to 0.35 in steps of 0.01.
- Scoring: scored by hidden verifier

### Step 2: Determine critical filling
- Role: scored
- Action: From the data in flip_energy_bound.csv, find the critical filling n_c where the lower bound on E^flip first becomes positive (i.e., E^flip > 0). Output the value and the method (e.g., linear interpolation from the sign change) as a JSON object.
- Output file: `/app/outputs/critical_filling.json`
- Format: json
- Contract: {"n_c": <float>, "method": <string describing extraction method>}
- Scoring: scored by hidden verifier

### Step 3: Solve BCS self-consistency and compute gap parameters
- Role: scored (load-bearing)
- Action: Implement the BCS mean-field theory for the effective Hamiltonian H_AF with next-nearest-neighbor hopping t' and attractive interaction V0. For a range of electron fillings 0.1 to 0.9, solve the self-consistency equation in the weak-coupling limit V0 ≪ |t'|. Determine the order-parameter symmetry that gives the lowest ground-state energy. For each filling, fit the variation of the gap magnitude vs V0 to the standard BCS gap equation |Δ| = 2ω exp(-1/(V0 g0)) to extract ω and g0. Output the scaled parameters as a function of filling.
- Output file: `/app/outputs/bcs_gap_parameters.csv`
- Format: csv
- Contract: Columns: filling (float), omega_over_tprime (float, ω/|t'|), g0 (float, inverse interaction scale). Rows for fillings from 0.1 to 0.9 in steps of 0.05.
- Scoring: scored by hidden verifier

### Step 4: Report order parameter symmetry
- Role: scored
- Action: From the BCS solution, record for each filling and for both signs of t' whether the superconducting order parameter has d-wave or s-wave symmetry, based on which symmetry minimizes the ground-state energy. Write the results as a plain text file.
- Output file: `/app/outputs/symmetry_phase.txt`
- Format: txt
- Contract: Lines of the form: 'filling=<value>, t'>0 => <d-wave|s-wave>' and 'filling=<value>, t'<0 => <d-wave|s-wave>', one per filling.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/flip_energy_bound.csv`
- `/app/outputs/critical_filling.json`
- `/app/outputs/bcs_gap_parameters.csv`
- `/app/outputs/symmetry_phase.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### flip_energy_bound.csv
- path: `/app/outputs/flip_energy_bound.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Lower bound on spin-flip energy versus filling.
- schema:
  - `type`: table
  - `required_columns`: `filling`, `E_flip_lower_bound`
  - `units`:
    - `E_flip_lower_bound`: |t'|

### critical_filling.json
- path: `/app/outputs/critical_filling.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Critical filling estimate extracted from the spin-flip energy bound.
- schema:
  - `type`: object
  - `required`:
    - `n_c`: float
    - `method`: string

### bcs_gap_parameters.csv
- path: `/app/outputs/bcs_gap_parameters.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: BCS gap equation scaling parameters ω and g0 for a range of fillings.
- schema:
  - `type`: table
  - `required_columns`: `filling`, `omega_over_tprime`, `g0`

### symmetry_phase.txt
- path: `/app/outputs/symmetry_phase.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Order parameter symmetry (d-wave or s-wave) for each filling and sign of next-nearest-neighbor hopping.
- schema:
  - `type`: text
  - `description`: One line per filling and sign of t' with the format 'filling=<value>, t'>0 => <symmetry>' or 'filling=<value>, t'<0 => <symmetry>'.

Notes: The checker will recompute the spin-flip energy bound for hidden fillings and compare to the agent's values, will check that the critical filling does not exceed the paper's bound, will recompute BCS gap parameters for hidden fillings and compare within tolerance, and will verify the order parameter symmetry against the expected phase diagram.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "flip_energy_bound.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "filling",
          "E_flip_lower_bound"
        ],
        "units": {
          "E_flip_lower_bound": "|t'|"
        }
      },
      "description": "Lower bound on spin-flip energy versus filling."
    },
    {
      "file": "critical_filling.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "n_c": "float",
          "method": "string"
        }
      },
      "description": "Critical filling estimate extracted from the spin-flip energy bound."
    },
    {
      "file": "bcs_gap_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "filling",
          "omega_over_tprime",
          "g0"
        ]
      },
      "description": "BCS gap equation scaling parameters ω and g0 for a range of fillings."
    },
    {
      "file": "symmetry_phase.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "One line per filling and sign of t' with the format 'filling=<value>, t'>0 => <symmetry>' or 'filling=<value>, t'<0 => <symmetry>'."
      },
      "description": "Order parameter symmetry (d-wave or s-wave) for each filling and sign of next-nearest-neighbor hopping."
    }
  ],
  "notes": "The checker will recompute the spin-flip energy bound for hidden fillings and compare to the agent's values, will check that the critical filling does not exceed the paper's bound, will recompute BCS gap parameters for hidden fillings and compare within tolerance, and will verify the order parameter symmetry against the expected phase diagram."
}
```

## How you are scored
A hidden verifier independently checks each of the scored artifacts (flip_energy_bound.csv, critical_filling.json, bcs_gap_parameters.csv, symmetry_phase.txt). The verifier recomputes the spin‑flip energy lower bound for a few hidden fillings on a smaller lattice and compares your reported values within a tolerance. For the critical filling, it verifies that the reported n_c is consistent with an independent bound and that the extraction method is reasonable. For the BCS gap parameters, the verifier implements the same self‑consistency equation and gap‑fitting procedure and recomputes ω/|t'| and g0 for several hidden fillings, comparing within relative tolerances. The symmetry assignments are checked against the expected phase diagram by spot‑checks at several fillings. The three main load‑bearing artifacts (flip_energy_bound.csv, bcs_gap_parameters.csv, symmetry_phase.txt) carry most of the weight, while the critical_filling.json extraction carries a smaller share.
