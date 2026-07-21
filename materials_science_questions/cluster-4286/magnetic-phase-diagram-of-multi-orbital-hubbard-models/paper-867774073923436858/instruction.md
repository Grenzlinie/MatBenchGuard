# Slave-Rotor Mean-Field Phase Diagram and Tunneling Density of States of a Two-Layer Hubbard-Anderson Model

## Problem background
This task addresses the competition between a spinon Fermi surface (a spin liquid) and an interlayer-coherent heavy Fermi liquid in a two-layer triangular-lattice model of correlated electrons coupled to an itinerant metallic layer. The model incorporates Hubbard repulsion U among correlated d-electrons, intra-layer hopping t_d, and inter-layer tunneling V. By tuning these parameters the system spans the periodic Anderson model (localized correlated electrons) and the Hubbard model (isolated correlated layer). A slave-rotor mean-field approach is used to study the zero-temperature phase diagram and the local density of states (LDOS) of the correlated layer, motivated by recent scanning tunneling microscopy (STM) experiments on layered transition metal dichalcogenides. The goal is to compute the phase boundary where the spin liquid gives way to a heavy metallic phase, and to characterize the shape and temperature broadening of the LDOS corresponding to what an STM tip would measure when coupled primarily to the correlated layer.

## Approach
The theoretical framework is a slave-rotor mean-field treatment. The correlated d-electron is split into a fermionic spinon (carrying spin) and a bosonic rotor (carrying charge), with a local constraint enforcing single occupancy on average. After a mean-field decoupling, the fermionic Hamiltonian describes spinons and itinerant c-electrons hybridized by a coherent amplitude V_f, while the rotor sector is treated via an effective single-site Hamiltonian plus a perturbative nearest-neighbor correlation. The order parameter for the metallic phase is Φ = ⟨e^{iθ}⟩ (coherent residue), which vanishes in the spin liquid. The fermionic bands are approximated by parabolic dispersions with a momentum cutoff corresponding to the triangular-lattice Brillouin zone; the itinerant electron density is controlled by a parameter ξ. The self-consistent equation for Φ is solved numerically together with the half-filling constraint. The local density of states of the correlated d-electrons is obtained from the spinon spectral function, computed from the hybridized quasiparticle bands. Phenomenological self-energy corrections (a Fermi-liquid type frequency‑/temperature‑dependent term and a constant disorder scattering rate) are added to account for quasiparticle interactions and disorder broadening. All required formulas, parameter values, and the parabolic band approximation are publicly specified; the workflow re‑implements the entire mean-field computation from scratch using standard scientific Python libraries.

## Reproduction target
Perform the following computational tasks and write the results as CSV files in /app/outputs:

1. **Phase diagram** – For the particle-particle dispersion case with ξ=1.2, compute the order parameter Φ on a grid: t_d/U from 0 to 0.15 (step 0.005) and V^2/U from 0 to 2 (step 0.02), with energies in units of t_c. Save every grid point with its Φ as `phase_diagram.csv`.

2. **Zero-temperature mean-field LDOS** – For two parameter points:
   - Anderson limit: t_d/U=0, V^2/U=0.5 t_c,
   - Finite hopping: t_d/U=0.04, V^2/U=0.35 t_c,
   compute the spinon spectral function A(ω) using the mean-field quasiparticle bands broadened by a small artificial η=0.01 t_c. Provide the spectra on a fine ω grid as `ldos_anderson_zeroT.csv` and `ldos_finite_td.csv`.

3. **Broadened LDOS** – For the Anderson limit point (t_d/U=0, V^2/U=0.5 t_c), include the quasi-particle self-energy Σ_FL(ω,T) that adds a temperature‑dependent lifetime (with an energy scale E0 interpolating between the Kondo temperature and the spinon bandwidth) and a constant impurity scattering rate γ0=0.05 t_c. Compute the broadened spectral function at T=0.05 t_c and save as `ldos_anderson_broadened.csv`.

4. **Temperature-dependent width** – For the same Anderson limit with self-energy and disorder, compute the broadened LDOS at temperatures T/t_c = 0.01, 0.02, 0.05, 0.1, 0.2. For each temperature, extract the half-maximum half-width Γ of the peak nearest to ω=0. Write the five pairs to `width_vs_T.csv`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute spinon nearest-neighbor correlator χ0
- Role: process
- Action: Using the uncoupled spin liquid (V=0), solve self-consistently for the nearest-neighbor spinon expectation value χ0 as a function of t_d/U. Use the parabolic band approximation and the half-filling constraint. The correlator enters as T_θ = t_d χ0 in later stages.
- Evidence: `/app/outputs/chi0_vs_td.csv`

### Step 2: Solve self-consistent equation for Φ and generate phase diagram
- Role: process
- Action: For each (t_d/U, V/U) point on a grid covering t_d/U ∈ [0,0.15] step 0.005 and V^2/U ∈ [0,2] step 0.02 (units of t_c), solve the slave-rotor mean-field self-consistent equation together with the half-filling constraint to obtain the order parameter Φ. Use the rotor interpolation formula and the nearest-neighbor rotor correlation approximation. Compute the coherent residue Φ and hybridization V_f. Save the full Φ landscape as a NumPy array.
- Evidence: `/app/outputs/order_parameter_map.npy`

### Step 3: Export phase diagram data
- Role: scored (load-bearing)
- Action: Write the computed Φ values at each grid point to a CSV file with columns t_d_div_U, V2_div_U, Phi.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: t_d_div_U (float), V2_div_U (float), Phi (float)
- Scoring: scored by hidden verifier

### Step 4: Prepare mean-field band structures for selected parameter points
- Role: process
- Action: For the parameter points (i) t_d/U=0, V^2/U=0.5 t_c and (ii) t_d/U=0.04, V^2/U=0.35 t_c, construct the hybridized quasiparticle dispersions and coherence factors using the solved Φ and V_f. Set up the momentum grid over the triangular-lattice Brillouin zone with an appropriate cutoff.
- Evidence: none

### Step 5: Compute zero-temperature mean-field LDOS for Anderson limit (t_d=0)
- Role: scored
- Action: Compute the spinon spectral function A(ω) for the Anderson limit point (t_d/U=0, V^2/U=0.5 t_c) using the mean-field quasiparticle bands with a small artificial broadening (e.g., η=0.01 t_c). Output the LDOS on a fine ω grid.
- Output file: `/app/outputs/ldos_anderson_zeroT.csv`
- Format: csv
- Contract: omega (float), A(omega) (float)
- Scoring: scored by hidden verifier

### Step 6: Compute zero-temperature mean-field LDOS for finite t_d/U
- Role: scored
- Action: Compute the spinon spectral function for the point t_d/U=0.04, V^2/U=0.35 t_c using the same mean-field approach with artificial broadening (η=0.01 t_c), and output the LDOS.
- Output file: `/app/outputs/ldos_finite_td.csv`
- Format: csv
- Contract: omega (float), A(omega) (float)
- Scoring: scored by hidden verifier

### Step 7: Compute broadened LDOS for Anderson limit at T=0.05 t_c with self-energy
- Role: process
- Action: For the Anderson limit point (t_d/U=0, V^2/U=0.5 t_c), include the quasi-particle self-energy from Fermi-liquid interactions (Σ_FL) and a constant impurity scattering rate γ0=0.05 t_c. Use the energy scale E0 that interpolates between the Kondo temperature and the spinon bandwidth. Evaluate the Green function and compute the broadened spectral function at temperature T=0.05 t_c.
- Evidence: none

### Step 8: Export broadened LDOS for Anderson limit
- Role: scored
- Action: Write the broadened LDOS spectral function for the Anderson limit at T=0.05 t_c to a CSV file with columns omega and A(omega).
- Output file: `/app/outputs/ldos_anderson_broadened.csv`
- Format: csv
- Contract: omega (float), A(omega) (float)
- Scoring: scored by hidden verifier

### Step 9: Compute temperature-dependent LDOS half-widths for Anderson limit
- Role: process
- Action: For the Anderson limit point with the same self-energy and disorder parameters, compute the broadened LDOS at each temperature T = 0.01, 0.02, 0.05, 0.1, 0.2 (in units of t_c). For each temperature, extract the half-maximum half-width Γ from the nearest zero-bias peak.
- Evidence: none

### Step 10: Export width vs temperature
- Role: scored
- Action: Write the extracted half-widths as a function of temperature to a CSV file with columns T_div_tc and half_max_width.
- Output file: `/app/outputs/width_vs_T.csv`
- Format: csv
- Contract: T_div_tc (float), half_max_width (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/ldos_anderson_zeroT.csv`
- `/app/outputs/ldos_finite_td.csv`
- `/app/outputs/ldos_anderson_broadened.csv`
- `/app/outputs/width_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase diagram data: order parameter Φ at each (t_d/U, V^2/U) point for particle-particle dispersion ξ=1.2. The grid covers t_d/U ∈ [0,0.15] step 0.005 and V^2/U ∈ [0,2] step 0.02 (units of t_c).
- schema:
  - `type`: table
  - `required_columns`: `t_d_div_U`, `V2_div_U`, `Phi`

### ldos_anderson_zeroT.csv
- path: `/app/outputs/ldos_anderson_zeroT.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Zero-temperature mean-field LDOS for Anderson limit (t_d/U=0, V^2/U=0.5 t_c) without self-energy broadening.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `A(omega)`

### ldos_finite_td.csv
- path: `/app/outputs/ldos_finite_td.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Zero-temperature mean-field LDOS for t_d/U=0.04, V^2/U=0.35 t_c without self-energy broadening.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `A(omega)`

### ldos_anderson_broadened.csv
- path: `/app/outputs/ldos_anderson_broadened.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Broadened LDOS for Anderson limit at T=0.05 t_c with self-energy and disorder.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `A(omega)`

### width_vs_T.csv
- path: `/app/outputs/width_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Half-maximum half-width of the broadened LDOS peak for the Anderson limit at temperatures T = 0.01, 0.02, 0.05, 0.1, 0.2 (in units of t_c).
- schema:
  - `type`: table
  - `required_columns`: `T_div_tc`, `half_max_width`

Notes: All scored artifacts are CSV files with headers. The LDOS files are on a fine ω grid (agent chooses appropriate resolution). The width_vs_T file contains exactly five rows for the specified temperatures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t_d_div_U",
          "V2_div_U",
          "Phi"
        ]
      },
      "description": "Phase diagram data: order parameter Φ at each (t_d/U, V^2/U) point for particle-particle dispersion ξ=1.2. The grid covers t_d/U ∈ [0,0.15] step 0.005 and V^2/U ∈ [0,2] step 0.02 (units of t_c)."
    },
    {
      "file": "ldos_anderson_zeroT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "A(omega)"
        ]
      },
      "description": "Zero-temperature mean-field LDOS for Anderson limit (t_d/U=0, V^2/U=0.5 t_c) without self-energy broadening."
    },
    {
      "file": "ldos_finite_td.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "A(omega)"
        ]
      },
      "description": "Zero-temperature mean-field LDOS for t_d/U=0.04, V^2/U=0.35 t_c without self-energy broadening."
    },
    {
      "file": "ldos_anderson_broadened.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "A(omega)"
        ]
      },
      "description": "Broadened LDOS for Anderson limit at T=0.05 t_c with self-energy and disorder."
    },
    {
      "file": "width_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_tc",
          "half_max_width"
        ]
      },
      "description": "Half-maximum half-width of the broadened LDOS peak for the Anderson limit at temperatures T = 0.01, 0.02, 0.05, 0.1, 0.2 (in units of t_c)."
    }
  ],
  "notes": "All scored artifacts are CSV files with headers. The LDOS files are on a fine ω grid (agent chooses appropriate resolution). The width_vs_T file contains exactly five rows for the specified temperatures."
}
```

## How you are scored
A hidden verifier evaluates each scored artifact independently and combines the component scores with predetermined weights into a final reward between 0 and 1. The verifier does not simply read off a reported number; it compares your computed results against reference data obtained from an independent implementation of the same mean-field equations or digitized from published theoretical spectra. The phase boundary is checked by comparing the critical V^2/U where Φ becomes positive for each t_d/U. The LDOS curves are compared via mean integrated squared error to reference spectra, and the temperature‑dependent half-widths are validated against the expected analytic Fermi‑liquid form together with your computed Kondo temperature. Exact values of tolerances are hidden. You must write exactly the CSV files described above with the specified columns; shape and format also contribute a small fraction of the score.
