# Nitrogen-induced local moments and ferromagnetic coupling in Co:BaTiO3

## Problem background
Dilute magnetic semiconductors based on oxide perovskites are explored for spintronics, but substitutional transition-metal doping alone often fails to produce strong ferromagnetic coupling. The addition of a p-type dopant such as nitrogen on an oxygen site near the magnetic ion has been proposed to alter the local electronic structure, induce spin splitting, and enhance magnetic interactions. This study investigates whether placing a substitutional nitrogen atom as a nearest neighbour to cobalt in a cubic BaTiO₃ host can create a net local magnetic moment and stabilise ferromagnetic (FM) ordering between cobalt atoms relative to antiferromagnetic (AFM) ordering. The key quantities to compute are the induced magnetic moment and Co–N bond length when N sits next to Co, the relative formation energy of N near versus far from Co, and the energy difference between FM and AFM spin arrangements in a two-Co + N bridge geometry.

## Approach
The system is modelled with spin‑polarised density functional theory using the LSDA+U functional, which adds an on‑site Hubbard U correction to treat correlation effects on the cobalt 3d electrons. A 3×3×3 cubic supercell of BaTiO₃ (135 atoms, experimental lattice constant 3.995 Å) is used. One titanium atom is replaced by cobalt to simulate Co doping; nitrogen is introduced by substituting an oxygen atom. Atomic positions are fully relaxed while keeping the lattice constant fixed. Total energies and magnetisations are obtained for several configurations: Co only, Co with a nitrogen placed far away (no direct interaction), Co with nitrogen as a nearest neighbour, and a geometry containing two Co atoms with a single N atom bridging them. For the two‑Co + N system, both FM (parallel spins) and AFM (antiparallel spins) initial spin arrangements are computed. The formation energy of nitrogen doping is evaluated using the Zhang–Northrup formalism, which compares the total energy of the doped supercell with that of the undoped reference and corrects with the chemical potentials of nitrogen and oxygen obtained from isolated N₂ and O₂ molecules. Magnetic moments are extracted from the total spin‑polarised charge density or from projected densities of states. All calculations are carried out with an open‑source DFT code (e.g., Quantum ESPRESSO) and norm‑conserving or PAW pseudopotentials, making the entire workflow reproducible with publicly available tools.

## Reproduction target
Using the modelling approach and workflow steps detailed below, compute and report the following three sets of results as specified JSON files under `/app/outputs`:

1. **Magnetic moment and bond length for N-nearest-to-Co** (`step_01_moments_bond.json`): after full ionic relaxation of the supercell containing one Co and one N on the nearest-neighbour oxygen site, extract the total magnetic moment per Co atom (sum of moments on N and Co, in μB) and the Co–N bond length (in Å).

2. **Formation energy comparison: N near vs. N far** (`step_02_formation_energy.json`): compute the formation energies (in eV) of nitrogen doping for the configurations where N is a nearest neighbour to Co (`E_near`) and where N is placed far from Co (`E_far`). Report the raw total energies of the two doped supercells, the formation energies themselves, and the difference δ = E_near − E_far (a negative difference indicates N prefers to sit near Co).

3. **FM vs. AFM energy difference in two‑Co + N bridge** (`step_03_exchange_energy.json`): build a supercell with two Co atoms and one N atom in a bridging position. Run separate DFT relaxations for FM and AFM spin orderings. Report the final total energies (eV) for each configuration and the energy difference ΔE = E_FM − E_AFM (negative means FM is more stable than AFM).

These three target quantities constitute the core reproduction claim; the remaining workflow steps (Co‑only, N‑far baseline relaxations, and reference molecule calculations) are required intermediates to obtain the final formation and exchange energies.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- PAW pseudopotentials for Ba, Ti, O, Co, N (e.g. SSSP efficiency library or PseudoDojo): https://www.materialscloud.org/discover/sssp/table/efficiency
- Cubic BaTiO3 structure (lattice constant 3.995 Å, space group Pm-3m): https://next-gen.materialsproject.org/materials/mp-2998?formula=BaTiO3

## Workflow steps

### Step 1: Prepare supercell input structures
- Role: process
- Action: Generate the 3x3x3 cubic BaTiO3 supercell (135 atoms, lattice constant 3.995 Å). Create input files for Quantum ESPRESSO for the configurations: Co-only (one Ti replaced by Co), N-far (Co plus one N on an O site far from Co), N-near (Co plus N on nearest-neighbour O site), and two-Co+N (with N as bridge, for both FM and AFM spin settings).
- Evidence: `/app/outputs/supercell_files.tar.gz`

### Step 2: Co-only supercell relaxation and total energy
- Role: process
- Action: Run spin-polarized DFT (LSDA+U, Hubbard U=4 eV on Co d orbitals) for the Co-only supercell. Perform full ionic relaxation until forces are below 0.01 eV/Å. Obtain the total energy (E_co_only) and confirm that the system is non-magnetic (total magnetization ≈ 0).
- Evidence: `/app/outputs/co_only_output.tar.gz`

### Step 3: N far from Co supercell relaxation and total energy
- Role: process
- Action: Run DFT relaxation for the supercell with one Co and one N substituted on an O site far from Co (at least third nearest neighbour). Obtain the total energy (E_far) and confirm non-magnetic ground state.
- Evidence: `/app/outputs/n_far_output.tar.gz`

### Step 4: N nearest neighbour to Co: relaxation, magnetic moments, bond length
- Role: scored (load-bearing)
- Action: Run DFT relaxation for the supercell with one Co and one N on the nearest-neighbour O site. After convergence, extract the total magnetic moment per Co atom (sum of moments on N and Co) and the Co–N bond length. Write these values to the output file.
- Output file: `/app/outputs/step_01_moments_bond.json`
- Format: json
- Contract: {"total_moment_per_Co": <float μB>, "Co_N_bond_length": <float Å>}
- Scoring: scored by hidden verifier

### Step 5: Formation energy analysis (N near vs far)
- Role: scored
- Action: Compute formation energies of N doping for the near and far configurations using the Zhang–Northrup formula: ΔE = [E_{doped} − E_{undoped}] − μ_N + μ_O. Use total energies from previous DFT runs (E_co_only as undoped, E_near from n‑near, E_far from n‑far). Obtain chemical potentials μ_N and μ_O from isolated N₂ and O₂ molecule calculations with the same functional. Output the near and far formation energies and their difference.
- Output file: `/app/outputs/step_02_formation_energy.json`
- Format: json
- Contract: {"E_near": <float eV>, "E_far": <float eV>, "formation_energy_near": <float eV>, "formation_energy_far": <float eV>, "delta_E_near_far": <float eV>}
- Scoring: scored by hidden verifier

### Step 6: Two-Co+N ferromagnetic versus antiferromagnetic energy difference
- Role: scored (load-bearing)
- Action: Build a supercell with two Co atoms and one N atom as a bridge (Co–N–Co geometry). Run DFT for ferromagnetic (parallel spins) and antiferromagnetic (antiparallel spins) configurations, each with full ionic relaxation. Extract total energies E_FM and E_AFM, and compute ΔE = E_FM − E_AFM (negative means FM favoured).
- Output file: `/app/outputs/step_03_exchange_energy.json`
- Format: json
- Contract: {"E_FM": <float eV>, "E_AFM": <float eV>, "delta_E_FM_AFM": <float eV>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_moments_bond.json`
- `/app/outputs/step_02_formation_energy.json`
- `/app/outputs/step_03_exchange_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_moments_bond.json
- path: `/app/outputs/step_01_moments_bond.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total magnetic moment per Co atom and the Co–N bond length in the N‑nearest‑neighbour configuration.
- schema:
  - `type`: object
  - `required`:
    - `total_moment_per_Co`: number (μB)
    - `Co_N_bond_length`: number (Å)

### step_02_formation_energy.json
- path: `/app/outputs/step_02_formation_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation energies for N doping near and far from Co, and their difference.
- schema:
  - `type`: object
  - `required`:
    - `E_near`: number (eV)
    - `E_far`: number (eV)
    - `formation_energy_near`: number (eV)
    - `formation_energy_far`: number (eV)
    - `delta_E_near_far`: number (eV)

### step_03_exchange_energy.json
- path: `/app/outputs/step_03_exchange_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total energies of ferromagnetic and antiferromagnetic two‑Co+N configurations and the energy difference.
- schema:
  - `type`: object
  - `required`:
    - `E_FM`: number (eV)
    - `E_AFM`: number (eV)
    - `delta_E_FM_AFM`: number (eV)

Notes: All values are compared against the paper’s reported numbers with generous tolerances to absorb DFT code/pseudopotential differences. The energy differences must follow the correct trends (N near favoured, FM favoured).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_moments_bond.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "total_moment_per_Co": "number (μB)",
          "Co_N_bond_length": "number (Å)"
        }
      },
      "description": "Total magnetic moment per Co atom and the Co–N bond length in the N‑nearest‑neighbour configuration."
    },
    {
      "file": "step_02_formation_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_near": "number (eV)",
          "E_far": "number (eV)",
          "formation_energy_near": "number (eV)",
          "formation_energy_far": "number (eV)",
          "delta_E_near_far": "number (eV)"
        }
      },
      "description": "Formation energies for N doping near and far from Co, and their difference."
    },
    {
      "file": "step_03_exchange_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_FM": "number (eV)",
          "E_AFM": "number (eV)",
          "delta_E_FM_AFM": "number (eV)"
        }
      },
      "description": "Total energies of ferromagnetic and antiferromagnetic two‑Co+N configurations and the energy difference."
    }
  ],
  "notes": "All values are compared against the paper’s reported numbers with generous tolerances to absorb DFT code/pseudopotential differences. The energy differences must follow the correct trends (N near favoured, FM favoured)."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden automated verifier that runs after your job completes. The verifier reads the three scored JSON files you produce under `/app/outputs/`:
- `step_01_moments_bond.json`
- `step_02_formation_energy.json`
- `step_03_exchange_energy.json`

For each file, the verifier compares your reported numeric values to expected reference numbers derived from the underlying study. Comparisons use tolerances that absorb legitimate run‑to‑run and toolchain variability (different DFT codes, pseudopotentials, k‑point grids, convergence settings). Both absolute values and relative trends (sign of energy differences, ordering) are checked. Good agreement across all three scored results yields a high reward; partial agreement yields partial credit. The verifier may also inspect the evidence directories (`*_output.tar.gz` archives) to confirm that the reported numbers are consistent with the raw DFT logs. Writing correct JSON files that contain physically plausible quantities after genuinely running the required calculations is the path to a maximum score.
