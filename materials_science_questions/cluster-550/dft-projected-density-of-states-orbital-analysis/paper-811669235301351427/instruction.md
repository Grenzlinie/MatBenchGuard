# Anderson Impurity Model for GaNAs: Fractional Γ Character and Projected DOS

## Problem background
Dilute nitride GaNAs alloys exhibit a strong perturbation of the conduction band when As is replaced by N. The band-anticrossing (BAC) model describes this interaction, treating the host GaAs conduction band states and a set of localized N states as a coupled system. This work directly solves a single-particle many-impurity Anderson Hamiltonian for a large supercell with randomly placed N atoms, computing eigenstate observables to compare with the BAC model and to examine the role of disorder near the N resonant energy.

## Approach
We construct a cubic supercell of GaAs containing randomly placed substitutional N atoms. The single-particle Hamiltonian is written in a basis comprising the host GaAs conduction-band plane-wave states (up to an energy cutoff) and the M localized N states. The Hamiltonian matrix consists of diagonal host and impurity energies plus an off-diagonal coupling term with a constant matrix element. Diagonalization yields all eigenenergies and eigenstate expansion coefficients on the host basis. From these we compute: (i) the fractional Gamma character (sum of squared host-basis amplitudes) for each eigenstate; (ii) the density of states projected onto selected individual host k-states using Gaussian broadening; (iii) the total host-projected density of states; and (iv) the conduction-band localisation factor derived from the real-space wavefunction of the host component. The results are compared against the predictions of the 2-level BAC model, including the effect of an energy shift on the N level arising from the interaction with the host continuum.

## Reproduction target
Implement the supercell many-impurity Anderson Hamiltonian as described, using the specified parameters (supercell size, number of N atoms, energy cutoff, coupling constant, N level energy). Diagonalize the Hamiltonian and produce three output files: `eigenstate_properties.csv` with energy, fractional Gamma character, and localisation factor for each eigenstate; `projected_dos_selected_k.csv` containing the projected DOS onto six representative host k-states with energies EM = 0.0, 0.1, 0.2, 0.23, 0.25, 0.3 eV; and `host_projected_dos.csv` with the total host-projected DOS. The data should allow validation of the BAC model's predictions for the fractional Gamma character, the DOS splitting pattern, and the localisation behavior of states near the N energy.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Supercell setup and Hamiltonian parameter assignment
- Role: process
- Action: Define supercell parameters: L0=100, M=8000 substitutional N atoms, energy cutoff parameters l=11 giving Emax=0.857 eV, interaction parameter β=2.0 eV, N level energy EN=0.23 eV. Use GaAs effective mass m*=0.067 m0 and lattice constant a0 to set up the supercell of side L=L0 a0. Generate random N positions. Construct the host CB plane-wave basis |k⟩ with periodic boundary conditions and energies Ek ≤ Emax. Compute coupling constant VNc = β / (4 L0^3)^{1/2}.
- Evidence: none

### Step 2: Hamiltonian matrix assembly and diagonalization
- Role: process
- Action: Assemble the sparse Hamiltonian matrix H=H0+V in the basis of host CB states and N localized states using the parameters and positions from step-0. Diagonalize the matrix to obtain all eigenenergies {Ei} and the eigenstate expansion coefficients a_k^i = ⟨k|c_i⟩ on the host CB plane-wave basis.
- Evidence: none

### Step 3: Compute fractional Γ character and localisation factor
- Role: scored (load-bearing)
- Action: For each supercell eigenstate i, compute the fractional Γ character fΓ = Σ_k |a_k^i|^2 (sum over all host CB states). Compute the conduction-band localisation factor L(Ei) = V ∫ |ψ_cb(r)|^4 dr / (∫ |ψ_cb(r)|^2 dr)^2 with ψ_cb(r) = Σ_k a_k^i exp(ik·r). Write the results to eigenstate_properties.csv.
- Output file: `/app/outputs/eigenstate_properties.csv`
- Format: csv
- Contract: columns: eigenstate_index (int), energy (float, eV), fractional_Gamma (float), localisation_factor (float).
- Scoring: scored by hidden verifier

### Step 4: Projected DOS onto selected individual host k-states
- Role: scored
- Action: Select host k-states with original energies EM = 0.0, 0.1, 0.2, 0.23, 0.25, 0.3 eV. For each, compute the projected DOS D_k(E) = Σ_i δ(E-E_i) |a_k^i|^2, using a Gaussian broadening σ=3 meV. Write a CSV with columns: k_state_label, energy (eV, from 0 to 0.5 eV in 1 meV steps), projected_DOS.
- Output file: `/app/outputs/projected_dos_selected_k.csv`
- Format: csv
- Contract: columns: k_state_label (string), energy (float, eV), projected_DOS (float). Energy grid 0–0.5 eV, step 1 meV.
- Scoring: scored by hidden verifier

### Step 5: Host-projected density of states
- Role: scored
- Action: Compute the total DOS projected onto the GaAs host CB states: D_cb(E) = Σ_{i,k} δ(E-E_i) |a_k^i|^2, using a Gaussian broadening σ=20 meV. Write a CSV with columns: energy (eV, from 0 to 0.5 eV) and host_projected_DOS.
- Output file: `/app/outputs/host_projected_dos.csv`
- Format: csv
- Contract: columns: energy (float, eV), host_projected_DOS (float). Energy grid 0–0.5 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eigenstate_properties.csv`
- `/app/outputs/projected_dos_selected_k.csv`
- `/app/outputs/host_projected_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eigenstate_properties.csv
- path: `/app/outputs/eigenstate_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Eigenstate properties: energy, fractional Γ character and localisation factor for each supercell eigenstate. Used to verify BAC model trends.
- schema:
  - `type`: table
  - `required_columns`: `eigenstate_index`, `energy`, `fractional_Gamma`, `localisation_factor`
  - `units`:
    - `energy`: eV
    - `fractional_Gamma`: dimensionless
    - `localisation_factor`: dimensionless

### projected_dos_selected_k.csv
- path: `/app/outputs/projected_dos_selected_k.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Projected DOS onto six representative host k-states. Energy grid 0–0.5 eV, step 1 meV. Used to verify BAC-splitting behavior.
- schema:
  - `type`: table
  - `required_columns`: `k_state_label`, `energy`, `projected_DOS`
  - `units`:
    - `energy`: eV
    - `projected_DOS`: dimensionless

### host_projected_dos.csv
- path: `/app/outputs/host_projected_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total DOS projected onto the host GaAs conduction-band states. Used to verify the overall DOS shape near the N resonant energy.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `host_projected_DOS`
  - `units`:
    - `energy`: eV
    - `host_projected_DOS`: dimensionless

Notes: All scored artifacts are evaluated by structural audit (T3) against digitized reference curves from the paper's figures. The agent must implement the model Hamiltonian and compute observables; exact numerical agreement is not required due to randomness in N positions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eigenstate_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "eigenstate_index",
          "energy",
          "fractional_Gamma",
          "localisation_factor"
        ],
        "units": {
          "energy": "eV",
          "fractional_Gamma": "dimensionless",
          "localisation_factor": "dimensionless"
        }
      },
      "description": "Eigenstate properties: energy, fractional Γ character and localisation factor for each supercell eigenstate. Used to verify BAC model trends."
    },
    {
      "file": "projected_dos_selected_k.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_state_label",
          "energy",
          "projected_DOS"
        ],
        "units": {
          "energy": "eV",
          "projected_DOS": "dimensionless"
        }
      },
      "description": "Projected DOS onto six representative host k-states. Energy grid 0–0.5 eV, step 1 meV. Used to verify BAC-splitting behavior."
    },
    {
      "file": "host_projected_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "host_projected_DOS"
        ],
        "units": {
          "energy": "eV",
          "host_projected_DOS": "dimensionless"
        }
      },
      "description": "Total DOS projected onto the host GaAs conduction-band states. Used to verify the overall DOS shape near the N resonant energy."
    }
  ],
  "notes": "All scored artifacts are evaluated by structural audit (T3) against digitized reference curves from the paper's figures. The agent must implement the model Hamiltonian and compute observables; exact numerical agreement is not required due to randomness in N positions."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact by comparing it to hidden reference data derived from the original publication. The comparison uses structural trend checks (e.g., shape, monotonicity, peak locations) and tolerance-based numerical comparisons where appropriate. Each stage is assigned a weight, and the individual stage scores are combined linearly to produce a final reward. Simply reproducing the paper's reported numbers is not sufficient; the verifier evaluates the actual computed artifacts for consistency with the expected physical behavior.
