# DFT relaxation and band gap of a Mg,Li-codoped pyrochlore

## Problem background
Pyrochlore oxides (A₂B₂O₇) are promising candidates for solid oxide fuel cell electrodes and dielectric applications because their chemical and structural diversity allows tuning of electronic, ionic, and protonic conductivity. Co-doping with Li and Mg introduces oxygen vacancies and alters the distribution of cations over the A and B sites, which directly influences structural stability and optoelectronic properties. First-principles density functional theory (DFT) calculations can predict the most stable dopant configuration and the resulting structural and electronic properties for the (Bi₁.₅Li₀.₅)(Nb₁.₅Mg₀.₅)O₇ model. This task focuses on reproducing two headline DFT predictions for that model — the relaxed lattice parameter and the direct band gap — using an open‑source DFT code.

## Approach
The computational workflow follows the standard DFT protocol used in the literature: (i) build the initial crystal structure from the reported crystallographic data (space group Fd‑3m, fractional coordinates, and site occupancies); (ii) perform a full structural relaxation (cell parameters and atomic positions) with the GGA‑PBE exchange‑correlation functional to obtain the equilibrium lattice constant; (iii) on the relaxed cell, compute the electronic band structure and density of states using a screened hybrid functional (HSE06 or its closest equivalent) to obtain a reliable direct band gap at the L point of the Brillouin zone. The original study employed VASP; this reproduction uses Quantum ESPRESSO with publically available pseudopotentials. The relaxation must be converged in forces and the hybrid calculation converged in k‑points and plane‑wave cutoff; the agent chooses these convergence parameters appropriately.

## Reproduction target
The task requires you to compute the relaxed lattice parameter a (in Å) and the direct band gap E_g (in eV) for the (Bi₁.₅Li₀.₅)(Nb₁.₅Mg₀.₅)O₇ pyrochlore model. Write the two numeric values as a JSON object with keys 'lattice_parameter_a' and 'band_gap_eV' to the file /app/outputs/dft_results.json. The hidden verifier will compare your reported numbers to independently derived reference values; both quantities must fall within prescribed tolerances to earn full credit.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build initial pyrochlore structure
- Role: process
- Action: Construct the primitive cell of (Bi₁.₅Li₀.₅)(Nb₁.₅Mg₀.₅)O₇ (space group Fd‑3m, No. 227) using the ideal pyrochlore structure as starting geometry. For the initial cubic cell set the lattice constant a = 10.55 Å. Atom coordinates (Wyckoff positions for the conventional cell, origin choice 2 with origin at -3m) are:
  - A‑site (Bi, Li): 16c (0.625, 0.625, 0.625) with mixed occupancy Bi:0.75, Li:0.25.
  - B‑site (Nb, Mg): 16d (0.0, 0.0, 0.0) with mixed occupancy Nb:0.75, Mg:0.25.
  - O on 48f: (x, 0, 0) with x = 0.375; O’ on 8b: (0.375, 0.375, 0.375). All oxygen sites are fully occupied.
  Generate the primitive cell containing 22 atoms (2 formula units) from this conventional cell. Write the resulting cell to /app/outputs/initial_structure.cif.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: DFT‑PBE structural relaxation
- Role: process
- Action: Run a GGA‑PBE calculation with Quantum ESPRESSO to fully relax both the lattice parameters and atomic positions until all residual forces are below 0.5 meV/Å. Use a sufficient k‑point mesh and a plane‑wave cutoff appropriate for the chosen pseudopotentials to achieve energy convergence to within a few meV/atom. The final optimized structure and the log serve as evidence that the relaxation ran to completion.
- Evidence: `/app/outputs/pbe_relax.log`

### Step 3: Hybrid functional band‑gap calculation
- Role: process
- Action: Using the relaxed structure from step 2, perform a band‑structure and density‑of‑states calculation with a screened hybrid functional (HSE06 or PBE0) in Quantum ESPRESSO. Compute the total and projected DOS and identify the direct band gap at the L point of the Brillouin zone. A k‑mesh of at least 6×6×6 (or a band‑structure path including L) is required. Record the calculated band gap and verify it is direct at L.
- Evidence: `/app/outputs/hybrid_calc.log`

### Step 4: Extract and write final quantities
- Role: scored (load-bearing)
- Action: From the outputs of the relaxation and hybrid calculations, extract the relaxed lattice parameter a (in Å) and the direct band gap E_g (in eV). Write them as a JSON object to /app/outputs/dft_results.json with keys 'lattice_parameter_a' and 'band_gap_eV'.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: A JSON object with numeric keys 'lattice_parameter_a' (in Å) and 'band_gap_eV' (in eV). The exact values must be computed from the DFT workflow described above.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The DFT‑predicted relaxed lattice parameter (in Å) and direct band gap (in eV) for the (Bi₁.₅Li₀.₅)(Nb₁.₅Mg₀.₅)O₇ pyrochlore model. The verifier compares both values to reference values with predefined tolerances.
- schema:
  - `type`: object
  - `required`: `lattice_parameter_a`, `band_gap_eV`
  - `properties`:
    - `lattice_parameter_a`:
      - `type`: number
      - `unit`: Å
    - `band_gap_eV`:
      - `type`: number
      - `unit`: eV

Notes: Verifier applies tolerances for lattice parameter and band gap. Exact values are not required; results within tolerance earn full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "lattice_parameter_a",
          "band_gap_eV"
        ],
        "properties": {
          "lattice_parameter_a": {
            "type": "number",
            "unit": "Å"
          },
          "band_gap_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "The DFT‑predicted relaxed lattice parameter (in Å) and direct band gap (in eV) for the (Bi₁.₅Li₀.₅)(Nb₁.₅Mg₀.₅)O₇ pyrochlore model. The verifier compares both values to reference values with predefined tolerances."
    }
  ],
  "notes": "Verifier applies tolerances for lattice parameter and band gap. Exact values are not required; results within tolerance earn full credit."
}
```

## How you are scored
A hidden verifier reads the scored artifact /app/outputs/dft_results.json. It extracts the lattice parameter a and the band gap E_g, then compares each to a hidden reference value known to be reproducible by this computational protocol. The comparison applies a tolerance that accounts for legitimate differences between DFT implementations and pseudopotential choices. Full reward (1.0) is awarded only when both quantities satisfy the tolerance. If exactly one of the two passes, the reward is 0.5. No other artifacts are scored. Simply reporting a number without running the DFT pipeline will not survive the tolerance check.
