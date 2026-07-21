# Extract exchange coupling constants from DFT total energies for a bifluoride-bridged copper-pyrazine polymer

## Problem background
The bifluoride ion (FHF−) can act as a bridging ligand in magnetic coordination polymers, but its ability to mediate spin exchange between transition-metal centres is not well understood. The compound [Cu(HF2)2(pyrazine)]n forms a two-dimensional rectangular-layered structure in which adjacent Cu2+ ions are linked by pyrazine ligands in one direction and by two crystallographically distinct FHF− bridges (μ1,1‑ and μ1,3‑modes) in the orthogonal direction. This creates a natural competition between the Cu–pyrazine–Cu and Cu–(FHF)2–Cu superexchange paths. First‑principles electronic structure calculations (GGA+U) can extract the corresponding exchange coupling constants by computing the total energies of different ordered magnetic configurations and mapping them onto a Heisenberg spin Hamiltonian. The aim of this task is to determine those exchange constants and to establish which bridging motif dominates the magnetic coupling.

## Approach
The approach combines spin‑polarised density functional theory (GGA‑PBE) with on‑site Hubbard‑U corrections (Ueff = 5, 6, 7 eV) to compute the total energies of three collinear spin configurations of the compound: a ferromagnetic state (all Cu spins parallel) and two antiferromagnetic configurations – one where spins alternate along the bifluoride chains (AF1) and one where they alternate along the pyrazine chains (AF2). The crystal structure is taken from CCDC 797479 and is used without further relaxation. An open‑source plane‑wave DFT code (e.g., Quantum ESPRESSO) provides the computational engine; the calculation uses standard GGA‑PBE pseudopotentials. After converging the total energies for each (Ueff, magnetic state) pair, the exchange constants J_FHF and J_pyz are obtained by mapping the energy differences onto the Heisenberg Hamiltonian

  H = −J_FHF Σ S_i·S_j (along the bifluoride bridges)
      − J_pyz Σ S_i·S_j (along the pyrazine bridges)

for a cell containing 4 formula units (Cu2+ carries spin‑1/2). The ratio α = J_pyz / J_FHF quantifies the relative strength of the two exchange paths. Additionally, the spin‑density distributions calculated from the converged wavefunctions for one representative Ueff are examined to identify which of the two FHF− bridging modes is primarily responsible for the exchange coupling.

## Reproduction target
Perform spin‑polarised GGA+U total‑energy calculations for the three magnetic configurations (FM, AF1, AF2) at each Ueff = 5, 6, and 7 eV. Record the raw total energies (eV per 4 formula units) in a CSV file. From those energies derive the Heisenberg exchange constants J_FHF/kB (K) and J_pyz/kB (K), together with the ratio α = J_pyz / J_FHF, and write them to a second CSV file. The goal is to obtain values that reflect a realistic DFT interpretation: the relative trend should reveal whether the bifluoride‑chain or the pyrazine‑chain exchange is stronger, and which bridging mode dominates the Cu–(FHF)2–Cu coupling. In addition, produce a qualitative spin‑density analysis summary that discusses the orbital contributions of the μ1,1‑ and μ1,3‑FHF− bridges.

## Assets

- [Cu(HF2)2(pyrazine)]n crystal structure (CCDC 797479): https://www.ccdc.cam.ac.uk/structures/search?id=797479
- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP efficiency library (GGA-PBE pseudopotentials): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare DFT input files from crystal structure
- Role: process
- Action: Obtain the crystal structure CIF from CCDC 797479. Generate DFT input files (atomic positions, cell vectors, k-point grid, plane-wave cutoff) for three magnetic configurations: ferromagnetic (FM, all Cu spins up), antiferromagnetic along the bifluoride chain (AF1), and antiferromagnetic along the pyrazine chain (AF2). The configurations correspond to the three ordered spin states defined in the paper (Figure 3). Use a supercell consistent with the experimental orthorhombic unit cell containing 4 formula units.
- Evidence: none

### Step 2: Compute total energies for magnetic configurations
- Role: scored (load-bearing)
- Action: Perform spin-polarized GGA+U (PBE) calculations for each of the three magnetic configurations and for each Ueff = 5, 6, and 7 eV. Converge total energies to within at least 0.1 meV per atom. Record the total energy per unit cell (or per 4 formula units) for each (Ueff, configuration) pair in the specified CSV file.
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: Columns: U_eff (5, 6, 7 eV), state (FM, AF1, AF2), total_energy (eV per 4 formula units)
- Scoring: scored by hidden verifier

### Step 3: Map total energies onto spin Hamiltonian to extract exchange couplings
- Role: scored
- Action: From the total energies in total_energies.csv, derive the exchange constants J_FHF and J_pyz using the Heisenberg Hamiltonian mapping. Convert to kelvin (1 eV = 11604.5 K) and compute the ratio J_pyz/J_FHF. Output all derived quantities.
- Output file: `/app/outputs/exchange_parameters.csv`
- Format: csv
- Contract: Columns: U_eff, J_FHF (K), J_pyz (K), ratio_J_pyz_J_FHF
- Scoring: scored by hidden verifier

### Step 4: Spin density analysis (qualitative interpretation)
- Role: process
- Action: Using the converged wavefunctions from the DFT calculations with one representative Ueff (e.g., 6 eV), compute spin density distributions for the FM and AFM states. Compare the spin polarization on the bridging atoms to identify which bridge dominates the exchange. Generate a text summary of the analysis.
- Evidence: `/app/outputs/spin_density_analysis.txt`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/exchange_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw total energies from DFT for three magnetic configurations (FM, AF1, AF2) at U_eff = 5, 6, 7 eV. The checker will recompute exchange coupling constants J_FHF and J_pyz from these energies and compare them against the paper's DFT-calculated values.
- schema:
  - `type`: table
  - `required_columns`: `U_eff`, `state`, `total_energy`
  - `units`:
    - `U_eff`: eV
    - `total_energy`: eV per 4 formula units

### exchange_parameters.csv
- path: `/app/outputs/exchange_parameters.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Derived exchange constants (J_FHF, J_pyz) and their ratio for each U_eff. The checker will cross-check these values for consistency with the exchange constants recomputed from total_energies.csv and verify the relative trend (|J_FHF| > |J_pyz|, ratio < 1).
- schema:
  - `type`: table
  - `required_columns`: `U_eff`, `J_FHF`, `J_pyz`, `ratio_J_pyz_J_FHF`
  - `units`:
    - `J_FHF`: K
    - `J_pyz`: K
    - `ratio_J_pyz_J_FHF`: dimensionless

Notes: The spin density analysis (step_04) is a qualitative process step; it produces a text summary that is inspected for plausibility but carries negligible weight in scoring. The primary quantitative verification relies on the total_energies.csv and the recomputed exchange parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "U_eff",
          "state",
          "total_energy"
        ],
        "units": {
          "U_eff": "eV",
          "total_energy": "eV per 4 formula units"
        }
      },
      "description": "Raw total energies from DFT for three magnetic configurations (FM, AF1, AF2) at U_eff = 5, 6, 7 eV. The checker will recompute exchange coupling constants J_FHF and J_pyz from these energies and compare them against the paper's DFT-calculated values."
    },
    {
      "file": "exchange_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "U_eff",
          "J_FHF",
          "J_pyz",
          "ratio_J_pyz_J_FHF"
        ],
        "units": {
          "J_FHF": "K",
          "J_pyz": "K",
          "ratio_J_pyz_J_FHF": "dimensionless"
        }
      },
      "description": "Derived exchange constants (J_FHF, J_pyz) and their ratio for each U_eff. The checker will cross-check these values for consistency with the exchange constants recomputed from total_energies.csv and verify the relative trend (|J_FHF| > |J_pyz|, ratio < 1)."
    }
  ],
  "notes": "The spin density analysis (step_04) is a qualitative process step; it produces a text summary that is inspected for plausibility but carries negligible weight in scoring. The primary quantitative verification relies on the total_energies.csv and the recomputed exchange parameters."
}
```

## How you are scored
A hidden verifier reads your output files and independently scores the work. The primary check is on `total_energies.csv`: the verifier recomputes the exchange constants J_FHF and J_pyz from the three total energies per Ueff using the Heisenberg‑Hamiltonian mapping and compares them against a reference. It also verifies that the derived values in `exchange_parameters.csv` are consistent with those recomputed values and that the expected qualitative relationships hold (|J_FHF| > |J_pyz| and α < 1). The `spin_density_analysis.txt` file is inspected for plausibility but contributes only minor weight. The final score combines the stage‑level rewards with the dominant weight on the exchange parameters obtained from your DFT energies; simply reporting the paper’s numbers is not sufficient.
