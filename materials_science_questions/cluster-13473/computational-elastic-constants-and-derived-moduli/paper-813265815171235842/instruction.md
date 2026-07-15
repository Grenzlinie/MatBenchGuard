# Si-Ge Interatomic Potential Predictions: Elastic Constants, Superlattice Structure, Phonon Frequencies, and Ordering Energies

## Problem background
Accurate interatomic potentials for silicon-germanium systems are essential for studying lattice vibrations (phonons) and long-range atomic ordering in semiconductor superlattices. Short-range potentials often fail to reproduce the flattening of transverse acoustical (TA) phonon branches while giving correct elastic constants. This task provides a long‑range empirical potential that includes angular and dihedral interactions beyond nearest neighbours. Your job is to implement this potential and compute key physical properties for bulk Si, Ge, zinc‑blende SiGe, an epitaxial Si₂Ge₂ superlattice, and ordered/disordered SiGe phases.

## Approach
The interatomic potential gives the cohesive energy as half the sum over all pair interactions $V_{ij}$. Each pair term is a product of a coordination‑dependent attractive part and a bond‑angle many‑body factor that includes dihedral contributions. The full functional form is:

$$
\begin{aligned}
E_{\text{coh}} &= \frac{1}{2} \sum_{i,j\,(i\neq j)} V_{ij} \\
V_{ij} &= A \exp\!\bigl[-\beta(r_{ij}-R_i)^\gamma\bigr]
         \Bigl(\exp(-\Theta r_{ij}) 
           - B_0 \frac{\exp(-\lambda r_{ij})}{Z_i^{\alpha}}\Bigr) G(\Theta), \\
Z_i &= \sum_{ij} \exp\!\bigl[-\beta(r_{ij}-R_i)^\gamma\bigr], \\
G(\Theta) &= 1 + \sum_{k\neq i,j} \Bigl[
            \cos(\eta\,\Delta\Theta_{jik}) - 1 \\
            &\; - \omega \Bigl(\frac{\Delta r_{ik}}{r_{eik}} 
                       + \frac{\Delta r_{ij}}{r_{eij}}\Bigr) \sin(\Delta\Theta_{jik}) \\
            &\; - \tau \frac{\Delta r_{ij}\,\Delta r_{ik}}{r_{eij}\,r_{eik}} \\
            &\; - \mu \sin(\Delta\Theta_{jik}) \sum_{n\neq k} \sin(\Delta\Theta_{jin}) \\
            &\; - \nu \sin(\Delta\Theta_{jik}) \sum_{m} \sin(\Delta\Theta_{mji})
           \Bigr],
\end{aligned}
$$

with $\Delta\Theta_{jik}=|\Theta_{jik}-\Theta_i|$, $\Delta r_{ij}=r_{ij}-r_{eij}$, and $\Theta_i$ the equilibrium bond angle. The parameters for Si, Ge, and the Si–Ge cross interaction are given in the table below.

**Potential parameters** (eV, Å, dimensionless)

| Parameter | Si        | Ge        | Si–Ge     |
|-----------|-----------|-----------|-----------|
| $A$       | 2428.358  | 1617.9011 | 1662.4545 |
| $B_0$     | 0.073483795 | 0.40173721 | 0.18918681 |
| $\Theta$  | 3.1325915 | 2.3723891 | 2.6996348 |
| $\lambda$ | 1.2350576 | 1.6994641 | 1.4522016 |
| $\alpha$   | 0.66203207 | 0.32487985 | 0.50588024 |
| $\beta$    | 25.441210  | 17.798649  | 22.036228  |
| $\gamma$   | 3.3821766  | 3.2287695  | 3.3517561  |
| $\eta$     | 0.65721357 | 0.65027922 | 0.65467423 |
| $\tau$     | 0.75632453 | 0.54870695 | 0.66627795 |
| $\omega$   | 0.45181420 | 0.69697356 | 0.56668258 |
| $\nu$      | 0.34765068 | 0.39903975 | 0.37257239 |
| $\mu$      | -0.13168585 | -0.15485126 | -0.14286610 |

The equilibrium bond lengths for Si and Ge are 2.35 Å and 2.438 Å, respectively; for Si–Ge use the average. The equilibrium bond angle for the diamond/zinc‑blende lattice is the tetrahedral angle. Use any simulation tool of your choice (e.g., ASE, LAMMPS, custom code) capable of implementing the potential.

The computation proceeds in several stages:
1. Implement the potential and set up the three bulk crystals (diamond Si, diamond Ge, zinc‑blende SiGe).
2. Compute the elastic constants $c_{11}$, $c_{12}$, $c_{44}$, and the derived moduli $C'=(c_{11}-c_{12})/2$ and $B=(c_{11}+2c_{12})/3$ for each material.
3. Build an epitaxial $\text{Si}_2\text{Ge}_2$ superlattice on a (001) Si substrate, relax it, and extract interplanar distances, the $c/a$ ratio, and the excess energy.
4. Compute selected phonon frequencies: the $\Gamma$-point optical mode for Si, Ge, and SiGe, and the zone‑edge TA modes at $X$ and $L$ for Si and Ge.
5. Simulate the RH1 ordered phase and a random $\text{Si}_{0.5}\text{Ge}_{0.5}$ alloy on a (001) substrate, relaxing both, and report their energies per atom and $c/a$ ratios.

The detailed workflow steps with exact output formats are given below; you must follow them.

## Reproduction target
Your objective is to faithfully implement the potential described in Approach and apply it to compute the following target quantities, each written to a specified CSV file:

- **Elastic constants.** For Si, Ge, and zinc‑blende SiGe, report the cubic elastic constants $c_{11}$, $c_{12}$, $c_{44}$ and the derived quantities $C'$ and the bulk modulus $B$ (all in GPa). Output file: `elastic_constants.csv`.
- **Superlattice structure.** For an epitaxial $\text{Si}_2\text{Ge}_2$ superlattice coherent with a Si(001) substrate, report the interplanar distances $R$(Si–Si), $R$(Si–Ge), $R$(Ge–Ge) (in Å), the axial ratio $c/a$, and the excess energy per atom (meV/atom). Output file: `sls_interplanar.csv`.
- **Phonon frequencies.** Using the relaxed primitive cells, report the optical phonon frequency at the $\Gamma$ point for Si, Ge, and zinc‑blende SiGe, and the TA frequencies at the $X$ and $L$ zone‑edge points for Si and Ge. All frequencies in cm⁻¹. Output file: `phonon_frequencies.csv`.
- **Ordering energies.** Build supercells for the RH1 ordered phase (Si/Ge alternating on (111) planes) and a random $\text{Si}_{0.5}\text{Ge}_{0.5}$ alloy, relax them in the growth direction, and report the energy per atom (meV/atom) and the $c/a$ axial ratio for each. Output file: `ordering_energies.csv`.

All output files must be placed in `/app/outputs` and conform to the schemas detailed in the Workflow steps and Output contract.

## Assets

- Potential Parameters for Si, Ge, Si-Ge
- Atomic Simulation Environment (ASE) or LAMMPS: https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Implement interatomic potential and set up simulation environment
- Role: process
- Action: Implement the empirical interatomic potential defined by equations (1)-(3) using the provided parameter table (Si, Ge, Si-Ge) in a simulation framework (e.g., ASE, LAMMPS, or custom Python code). Prepare the basic crystal structures: diamond cubic for Si and Ge, zinc blende for SiGe.
- Evidence: `/app/outputs/potential_implementation.log`

### Step 2: Compute elastic constants for Si, Ge, and zinc blende SiGe
- Role: scored
- Action: For each material, obtain the equilibrium lattice constant by energy minimization, then apply small strains to compute the stress tensor. Calculate c11, c12, c44 (in GPa). Derive C_prime = (c11-c12)/2 and bulk modulus B = (c11+2c12)/3. Report one row per material.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: material (string), c11 (float, GPa), c12 (float, GPa), c44 (float, GPa), C_prime (float, GPa), B (float, GPa). Three rows.
- Scoring: scored by hidden verifier

### Step 3: Relax epitaxial Si2Ge2 superlattice on Si(001) and compute interplanar distances and excess energy
- Role: scored
- Action: Construct an epitaxial Si2Ge2 superlattice cell coherent with a Si (001) substrate (in-plane lattice constant fixed to Si equilibrium value). Relax all atomic positions and the cell dimension in the growth direction to minimize energy using the potential. Extract the interplanar distances R(Si-Si), R(Si-Ge), R(Ge-Ge), the c/a axial ratio, and the excess energy per atom (meV/atom).
- Output file: `/app/outputs/sls_interplanar.csv`
- Format: csv
- Contract: R_SiSi (float, Å), R_SiGe (float, Å), R_GeGe (float, Å), c_over_a (float), excess_energy (float, meV/atom). One row.
- Scoring: scored by hidden verifier

### Step 4: Compute selected phonon frequencies for Si, Ge, and SiGe
- Role: scored
- Action: Using the potential, compute phonon frequencies by finite-displacement or dynamical matrix method on relaxed primitive cells. For Si and Ge: report optical mode at Γ, and TA mode at X and L zone-edge points. For zinc blende SiGe: report optical mode at Γ.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: material (string), mode (string, one of Gamma_optical, X_TA, L_TA), frequency (float, cm⁻¹). Rows for Si (Gamma_optical, X_TA, L_TA), Ge (Gamma_optical, X_TA, L_TA), SiGe (Gamma_optical).
- Scoring: scored by hidden verifier

### Step 5: Simulate RH1 ordered phase and random alloy and compute energies and c/a ratio
- Role: scored (load-bearing)
- Action: Build supercells for the ordered RH1 phase (Si-Ge ordering on (111) planes) and a random SiGe alloy on a (001) substrate. Perform molecular dynamics with temperature reduction followed by steepest descent energy minimization (allowing relaxation in the growth direction). Report the final energy per atom (meV/atom) and the c/a axial ratio for each configuration.
- Output file: `/app/outputs/ordering_energies.csv`
- Format: csv
- Contract: structure (string, 'RH1' or 'random'), energy (float, meV/atom), c_over_a (float). Two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/sls_interplanar.csv`
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/ordering_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Elastic constants and derived moduli for Si, Ge, and zinc blende SiGe.
- schema:
  - `type`: table
  - `required_columns`: `material`, `c11`, `c12`, `c44`, `C_prime`, `B`
  - `units`:
    - `c11`: GPa
    - `c12`: GPa
    - `c44`: GPa
    - `C_prime`: GPa
    - `B`: GPa

### sls_interplanar.csv
- path: `/app/outputs/sls_interplanar.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Interplanar distances, axial ratio, and excess energy for the Si2Ge2 superlattice on Si(001).
- schema:
  - `type`: table
  - `required_columns`: `R_SiSi`, `R_SiGe`, `R_GeGe`, `c_over_a`, `excess_energy`
  - `units`:
    - `R_SiSi`: Å
    - `R_SiGe`: Å
    - `R_GeGe`: Å
    - `c_over_a`: dimensionless
    - `excess_energy`: meV/atom

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optical phonon frequency at Γ and zone-edge TA frequencies for Si, Ge, and SiGe.
- schema:
  - `type`: table
  - `required_columns`: `material`, `mode`, `frequency`
  - `units`:
    - `frequency`: cm⁻¹

### ordering_energies.csv
- path: `/app/outputs/ordering_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energy per atom and axial ratio for RH1 ordered and random SiGe alloy phases.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `energy`, `c_over_a`
  - `units`:
    - `energy`: meV/atom
    - `c_over_a`: dimensionless

Notes: All scored quantities are compared to the paper-reported gold values with undisclosed tolerances. The phyiscal constants are exact-match targets; tolerances are set to absorb reasonable implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "c11",
          "c12",
          "c44",
          "C_prime",
          "B"
        ],
        "units": {
          "c11": "GPa",
          "c12": "GPa",
          "c44": "GPa",
          "C_prime": "GPa",
          "B": "GPa"
        }
      },
      "description": "Elastic constants and derived moduli for Si, Ge, and zinc blende SiGe."
    },
    {
      "file": "sls_interplanar.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R_SiSi",
          "R_SiGe",
          "R_GeGe",
          "c_over_a",
          "excess_energy"
        ],
        "units": {
          "R_SiSi": "Å",
          "R_SiGe": "Å",
          "R_GeGe": "Å",
          "c_over_a": "dimensionless",
          "excess_energy": "meV/atom"
        }
      },
      "description": "Interplanar distances, axial ratio, and excess energy for the Si2Ge2 superlattice on Si(001)."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "mode",
          "frequency"
        ],
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "Optical phonon frequency at Γ and zone-edge TA frequencies for Si, Ge, and SiGe."
    },
    {
      "file": "ordering_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "energy",
          "c_over_a"
        ],
        "units": {
          "energy": "meV/atom",
          "c_over_a": "dimensionless"
        }
      },
      "description": "Energy per atom and axial ratio for RH1 ordered and random SiGe alloy phases."
    }
  ],
  "notes": "All scored quantities are compared to the paper-reported gold values with undisclosed tolerances. The phyiscal constants are exact-match targets; tolerances are set to absorb reasonable implementation spread."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the four CSV files you produce. For each scored stage the verifier compares the values you report against hidden reference results, using tolerances that account for legitimate implementation differences. The reward is a weighted combination of the scores from all stages; every stage contributes substantially, with the ordering‑energy stage acting as a load‑bearing check that the full pipeline has been genuinely executed. You must carry out the computations yourself — copying or guessing numbers will not yield a passing score.
