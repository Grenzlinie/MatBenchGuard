# Magnetic and topological properties of monolayer PdCl3

## Problem background
Two-dimensional materials that combine robust ferromagnetism with a half-metallic electronic structure and topologically nontrivial bands are highly sought after for dissipationless spintronics and low-power quantum devices. A Dirac half-metal—a material that hosts a fully spin‑polarized Dirac cone and breaks time‑reversal symmetry—can, when spin–orbit coupling is included, give rise to the quantum anomalous Hall effect with a quantized Hall conductance. However, achieving all these requirements in a single chemically stable monolayer that remains magnetically ordered well above room temperature has proven difficult. Monolayer PdCl₃, a honeycomb lattice of edge‑sharing PdCl₆ octahedra, has been proposed as a candidate that may simultaneously exhibit a high‑temperature ferromagnetic phase, a Dirac half‑metal character, and a nontrivial topology characterized by a finite Chern number. The present task is to determine, through a first‑principles computational protocol, whether PdCl₃ possesses these exotic properties and to compute the key magnetic and topological quantities that quantify them.

## Approach
The reproduction follows a multi‑stage computational workflow centred on density‑functional theory (DFT) and classical Monte Carlo simulations, all implemented with open‑source tools. A monolayer PdCl₃ unit cell (space group P31M, honeycomb Pd sublattice) is first constructed and geometrically relaxed using spin‑polarized DFT with a gradient‑corrected exchange–correlation functional. Dynamical stability is verified by computing the phonon dispersion and ensuring the absence of imaginary modes. To benchmark the magnetic interactions, total energies of ferromagnetic and two distinct antiferromagnetic spin configurations are evaluated in a supercell; these energies are then mapped onto a 2D Ising model to extract the nearest‑neighbour, next‑nearest‑neighbour, and third‑nearest‑neighbour exchange coupling constants. The magnetocrystalline anisotropy energy is obtained from constrained‑magnetization total‑energy calculations with spin–orbit coupling. With the exchange parameters in hand, a Metropolis Monte Carlo simulation on a large periodic lattice is carried out to track the average magnetic moment and heat capacity as functions of temperature, from which the Curie temperature is located. Finally, spin–orbit coupling plus an on‑site Hubbard correction is applied to the relaxed cell; the resulting band structure reveals the topological gap at the Dirac point, and the Berry curvature computed from a Wannier function projection is integrated over the Brillouin zone to yield the Chern number. Together these steps form a self‑contained protocol that reproduces the headline magnetic and topological properties of monolayer PdCl₃.

## Reproduction target
The task is to execute the full workflow and produce the following four scored results:
1. Total magnetic moment per unit cell (μB) and magnetocrystalline anisotropy energy (meV/f.u.) from spin‑polarized DFT with spin–orbit coupling.
2. Exchange coupling parameters J₁, J₂, J₃ (in meV) obtained from the total energies of the FM, AFM1, and AFM2 spin configurations via an Ising model mapping.
3. Curie temperature (K) determined as the peak of the heat capacity from a 2D Ising Monte Carlo simulation on a 200×200 lattice with periodic boundary conditions, run for 1×10⁹ Monte‑Carlo steps.
4. Spin–orbit‑coupling‑induced band gap (meV) at the Dirac point and Chern number (integer) computed from DFT+U+SOC band structure and Berry curvature integration.
The final numerical values must be written to the prescribed output files under /app/outputs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- Wannier90: http://www.wannier.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Construct a monolayer PdCl₃ unit cell (space group P31M, initial lattice parameter ~6.34 Å) and perform geometry optimization using spin‑polarized DFT (PBE functional) with a suitable plane‑wave cutoff and k‑point grid. Save the final relaxed atomic positions and lattice parameters.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Phonon stability check
- Role: process
- Action: Using the relaxed structure, compute the phonon dispersion with PHONOPY and DFPT (e.g., via Quantum ESPRESSO). Verify absence of imaginary modes across the entire Brillouin zone.
- Evidence: `/app/outputs/phonon.log`

### Step 3: Magnetic configuration energy calculations
- Role: process
- Action: Using a 2×2×1 supercell of the relaxed unit cell, construct three spin configurations: FM, AFM1, and AFM2 (as illustrated in the paper). Perform spin‑polarized DFT total energy calculations for each configuration with the same functional and convergence settings as relaxation. Record the total energies.
- Evidence: `/app/outputs/mag_energies.txt`

### Step 4: Magnetic moment and MAE
- Role: scored
- Action: From the relaxed unit cell, perform a spin‑polarized DFT calculation to extract the total magnetic moment per cell. Then, with spin‑orbit coupling, compute total energies with magnetization constrained along the x‑ and z‑axes to obtain the magnetocrystalline anisotropy energy (MAE) as E_x - E_z (in meV/f.u.). Output both values to magnetic_properties.json.
- Output file: `/app/outputs/magnetic_properties.json`
- Format: json
- Contract: {"magnetic_moment_muB": <float>, "mae_meV": <float>}
- Scoring: scored by hidden verifier

### Step 5: Exchange parameter fitting
- Role: scored (load-bearing)
- Action: Using the total energies of the FM, AFM1, and AFM2 configurations from the supercell calculations, map them to a 2D Ising model Hamiltonian to extract the nearest‑neighbor J₁, next‑nearest J₂, and third‑nearest J₃ coupling constants (in meV). Output the three values to exchange_parameters.json.
- Output file: `/app/outputs/exchange_parameters.json`
- Format: json
- Contract: {"J1_meV": <float>, "J2_meV": <float>, "J3_meV": <float>}
- Scoring: scored by hidden verifier

### Step 6: Monte Carlo Curie temperature
- Role: scored
- Action: Write a 2D Ising model Monte Carlo simulation on a 200×200 lattice with periodic boundaries, using the fitted J₁, J₂, J₃. Run for 1×10⁹ Monte‑Carlo steps and record the average magnetic moment per formula unit as a function of temperature. Compute the heat capacity C_v and locate its peak to determine the Curie temperature T_C. Output T_C (in K) to curie_temperature.txt.
- Output file: `/app/outputs/curie_temperature.txt`
- Format: txt
- Contract: A single floating‑point number representing the Curie temperature in Kelvin.
- Scoring: scored by hidden verifier

### Step 7: Topological properties (SOC gap and Chern number)
- Role: scored
- Action: On the relaxed unit cell, run DFT with SOC and a Hubbard U correction (e.g., around 3.5 eV on Pd d‑states) to compute the band structure. Extrack the direct topological band gap at the Dirac point (in meV). Then use Wannier90 to project the Pd d_{xz}/d_{yz} orbitals and compute the Berry curvature; integrate over the BZ to obtain the Chern number. Output the band gap and Chern number to topological_properties.json.
- Output file: `/app/outputs/topological_properties.json`
- Format: json
- Contract: {"soc_band_gap_meV": <float>, "chern_number": <int>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_properties.json`
- `/app/outputs/exchange_parameters.json`
- `/app/outputs/curie_temperature.txt`
- `/app/outputs/topological_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_properties.json
- path: `/app/outputs/magnetic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact reporting magnetic moment and MAE.
- schema:
  - `type`: object
  - `required`:
    - `magnetic_moment_muB`: number
    - `mae_meV`: number
  - `description`: Total magnetic moment per unit cell in μB and magnetocrystalline anisotropy energy in meV/f.u.

### exchange_parameters.json
- path: `/app/outputs/exchange_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact reporting exchange parameters from Ising model fit.
- schema:
  - `type`: object
  - `required`:
    - `J1_meV`: number
    - `J2_meV`: number
    - `J3_meV`: number
  - `description`: Exchange coupling parameters J1, J2, J3 in meV.

### curie_temperature.txt
- path: `/app/outputs/curie_temperature.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Scored artifact reporting Curie temperature from Monte Carlo simulation.
- schema:
  - `type`: text
  - `description`: A single floating‑point number on the first line, representing the Curie temperature in Kelvin.

### topological_properties.json
- path: `/app/outputs/topological_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact reporting band gap with SOC+U and Chern number.
- schema:
  - `type`: object
  - `required`:
    - `soc_band_gap_meV`: number
    - `chern_number`: integer
  - `description`: SOC-induced band gap in meV and Chern number (integer).

Notes: All scored artifacts are compared to paper‑reported values within hidden tolerances (T0 result-level comparison). The exchange_parameters step is load‑bearing to ensure the Monte Carlo process is directly linked to the fitted parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "magnetic_moment_muB": "number",
          "mae_meV": "number"
        },
        "description": "Total magnetic moment per unit cell in μB and magnetocrystalline anisotropy energy in meV/f.u."
      },
      "description": "Scored artifact reporting magnetic moment and MAE."
    },
    {
      "file": "exchange_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "J1_meV": "number",
          "J2_meV": "number",
          "J3_meV": "number"
        },
        "description": "Exchange coupling parameters J1, J2, J3 in meV."
      },
      "description": "Scored artifact reporting exchange parameters from Ising model fit."
    },
    {
      "file": "curie_temperature.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating‑point number on the first line, representing the Curie temperature in Kelvin."
      },
      "description": "Scored artifact reporting Curie temperature from Monte Carlo simulation."
    },
    {
      "file": "topological_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "soc_band_gap_meV": "number",
          "chern_number": "integer"
        },
        "description": "SOC-induced band gap in meV and Chern number (integer)."
      },
      "description": "Scored artifact reporting band gap with SOC+U and Chern number."
    }
  ],
  "notes": "All scored artifacts are compared to paper‑reported values within hidden tolerances (T0 result-level comparison). The exchange_parameters step is load‑bearing to ensure the Monte Carlo process is directly linked to the fitted parameters."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads each of the four scored output files you produce. For each file the verifier checks that the required fields are present and correctly formatted, then compares your reported numeric values to hidden reference targets using pre‑defined tolerances appropriate for the quantity (e.g., the magnetic moment, exchange parameters, Curie temperature, SOC gap, and Chern number). A scalar reward is computed as a weighted sum of the stage‑wise scores; the main reward comes from the key physical quantities. You are not informed of the reference values or the tolerances, and simply reporting a number is insufficient—the verifier expects the artifacts to be the result of executing the described computational steps. Partial credit is available even if some stages are less accurate than others, as long as each output file is present and conforms to the specified schema.
