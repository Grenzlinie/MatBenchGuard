## Problem background

The question of whether otherwise nonmagnetic bulk elements can become magnetic when reduced to clusters or assembled into two-dimensional structures is of fundamental interest. This task addresses that question for systems composed of uranium and a coinage metal (gold). Using density functional theory, we investigate the magnetic properties of a neutral and anionic UAu₆ cluster and of a periodic UAu₄ monolayer, as well as the effect of hydrogenation on the magnetic coupling. The objectives are to determine the ground-state spin multiplicity and magnetic moment of the clusters, the magnetic moment, anisotropy energy and exchange coupling of the pristine monolayer, the exchange coupling of the fully hydrogenated monolayer, and to estimate the Curie temperature of the ferromagnetic hydrogenated phase.

## Approach

We adopt a two‑part computational approach: (1) isolated cluster calculations using spin‑unrestricted hybrid DFT to obtain relaxed geometries for several candidate spin states, identify the ground state by total energy, and extract the magnetic moment from population analysis; (2) periodic DFT calculations on the monolayer and its hydrogenated derivative with a Hubbard‑U correction and spin–orbit coupling (SOC) to obtain lattice parameters, on‑site moments, magnetic anisotropy energy, and exchange coupling constants from supercell total energies. Finally, a classical Ising Monte Carlo simulation uses the exchange constant to estimate the Curie temperature.

**Cluster part (UAu₆ / UAu₆⁻):**  
Perform spin‑unrestricted B3LYP/cc‑pVDZ‑PP geometry optimizations using a quantum chemistry code. The scalar relativistic effects of core electrons are treated with 60‑electron energy‑consistent effective core potentials (ECP60MDF). Optimize the neutral cluster at singlet, triplet, and quintet multiplicities, and the anionic cluster at doublet and quartet. From the set of total energies, determine the ground‑state spin multiplicity for each. For the ground‑state geometries, compute natural population analysis (NPA) spins to obtain the total magnetic moment (the sum of atomic spin populations, in units of μB) for the neutral and anionic clusters. Report the spin multiplicities and the magnetic moments.

**Monolayer part (UAu₄ / UAu₄H₄):**  
Construct a hexagonal unit cell for UAu₄ (space group P6/MMM) that matches the cluster motif: a triangular network of U atoms sandwiched between two honeycomb Au layers. Use a periodic DFT code with the generalized gradient approximation (PBE), a Hubbard‑U correction (U_eff = 4 eV) on the U 5f orbitals, and spin–orbit coupling (SOC). Use projector‑augmented wave (PAW) pseudopotentials.  
*Pristine monolayer:* optimize the lattice constant and atomic positions. Build a 2×2 supercell and compute total energies for ferromagnetic (FM) and antiferromagnetic (AFM) spin configurations. The exchange coupling constant per unit cell is obtained from the energy difference. Compute the magnetic anisotropy energy (MAE) by performing non‑collinear SOC calculations with the magnetization oriented perpendicular to the layer (z) and in the layer plane; take MAE = E_perp − E_parallel. Extract the on‑site magnetic moment from the charge/spin density.  
*Hydrogenated monolayer:* fully hydrogenate the monolayer by placing one H atom on each side of the unit cell (i.e., UAu₄H₄). Re‑optimize the lattice constant and atomic positions. Repeat the FM/AFM energy calculation on a 2×2 supercell to obtain the new exchange coupling constant J.

**Curie temperature estimation:**  
Implement a classical spin‑½ Ising model on a 30 × 30 square lattice with the J value obtained for the hydrogenated monolayer. Perform a Monte Carlo simulation (Metropolis algorithm) recording the average magnetization as a function of temperature. The Curie temperature is the temperature at which the magnetization approaches zero (e.g., by fitting or the inflection point). Report this temperature in kelvin.

## Reproduction target

Produce four JSON artefacts under `/app/outputs`:
- `cluster_results.json` – spin multiplicities and magnetic moments for the neutral and anionic UAu₆ clusters.
- `monolayer_pristine_results.json` – lattice constant, U–Au bond length, on‑site magnetic moment, MAE, exchange energy difference, and exchange coupling J for the pristine UAu₄ monolayer.
- `monolayer_hydrogenated_results.json` – exchange energy difference and J for the fully hydrogenated UAu₄H₄ monolayer.
- `curie_temperature.json` – the estimated Curie temperature of the ferromagnetic UAu₄H₄ phase.

The solving agent must compute these numbers from the described DFT and Monte Carlo workflow; the checker compares each reported value against a hidden reference with appropriate tolerances.

## Assets

The following publicly available tools and datasets are required; the agent is responsible for installation and retrieval at runtime.

1. **NWChem** – quantum chemistry code for cluster DFT calculations.  
   Access: `https://nwchemgit.github.io/`
2. **Quantum ESPRESSO** – plane‑wave periodic DFT code for monolayer calculations.  
   Access: `https://www.quantum-espresso.org/`
3. **cc‑pVDZ‑PP basis sets** – correlation‑consistent polarized valence double‑ζ basis sets with pseudopotentials for U and Au.  
   Access: Basis Set Exchange (`https://www.basissetexchange.org/`)
4. **ECP60MDF effective core potentials** – scalar relativistic pseudopotentials for U and Au.  
   Access: available from the Stuttgart/Cologne pseudopotential library (e.g., `https://molcalc.org/pseudopotentials`)
5. **PAW pseudopotentials** – projector‑augmented wave datasets for U and Au suitable for PBE+U and SOC calculations.  
   Access: within the Quantum ESPRESSO distribution or `http://www.quantum-espresso.org/pseudopotentials`

## Workflow steps

### Step 1: Geometry Optimization of Neutral UAu₆ Cluster for All Spin States
- Role: process
- Action: Perform spin‑unrestricted DFT (B3LYP/cc‑pVDZ‑PP/ECP60MDF) geometry optimizations for the neutral UAu₆ cluster at singlet, triplet, and quintet spin multiplicities. Keep the convergence logs.
- Evidence: `/app/outputs/neutral_cluster_opt.log`

### Step 2: Geometry Optimization of Anionic UAu₆⁻ Cluster for All Spin States
- Role: process
- Action: Perform the same DFT calculations for the anionic UAu₆⁻ cluster at doublet and quartet spin multiplicities. Keep the convergence logs.
- Evidence: `/app/outputs/anion_cluster_opt.log`

### Step 3: Determine Ground States and Magnetic Moments of UAu₆ and UAu₆⁻
- Role: scored (load‑bearing)
- Action: From the total energies obtained in Steps 1 and 2, identify the lowest‑energy spin state for the neutral and for the anion. For those ground‑state geometries, run single‑point calculations and natural population analysis (NPA) to compute the total magnetic moment (sum of atomic spin populations) in units of μB. Write the results to `cluster_results.json`.
- Output file: `/app/outputs/cluster_results.json`
- Format: json
- Contract:
  `neutral_ground_state_spin_multiplicity` (integer)
  `anion_ground_state_spin_multiplicity` (integer)
  `neutral_total_magnetic_moment_muB` (float)
  `anion_total_magnetic_moment_muB` (float)
- Scoring: scored by hidden verifier

### Step 4: Construct UAu₄ Monolayer Unit Cell
- Role: process
- Action: Assemble a hexagonal unit cell for UAu₄ based on the cluster motif (U atom sandwiched between two Au honeycomb layers; space group P6/MMM). Export the initial structure to a CIF file.
- Evidence: `/app/outputs/uau4_initial.cif`

### Step 5: Geometry Optimization of Pristine UAu₄ Monolayer
- Role: process
- Action: Using Quantum ESPRESSO with PBE+U (U_eff = 4 eV on U 5f), SOC, and PAW pseudopotentials, relax the lattice constant and atomic positions of the UAu₄ monolayer. Keep the output log.
- Evidence: `/app/outputs/uau4_opt.log`

### Step 6: Compute Magnetic Moment, MAE, and Exchange Coupling J for Pristine UAu₄ Monolayer
- Role: scored
- Action: From the relaxed unit cell, (i) construct a 2×2 supercell; (ii) run non‑collinear spin‑polarized SOC calculations with magnetization along the out‑of‑plane (z) and in‑plane directions to obtain the total energies; compute MAE = E_perp – E_parallel; (iii) extract the on‑site magnetic moment from the spin density; (iv) run FM and AFM spin configurations on the supercell and compute ΔE_ex = E_AFM – E_FM and the exchange coupling constant J per unit cell. Write all quantities to `monolayer_pristine_results.json`.
- Output file: `/app/outputs/monolayer_pristine_results.json`
- Format: json
- Contract:
  `lattice_constant_a_A` (float)
  `bond_length_UAu_A` (float)
  `magnetic_moment_muB` (float)
  `MAE_meV_per_atom` (float)
  `delta_E_ex_meV` (float)
  `J_meV_per_unit_cell` (float)
- Scoring: scored by hidden verifier

### Step 7: Hydrogenate and Optimize UAu₄ Monolayer to UAu₄H₄
- Role: process
- Action: Place one H atom on each side of the UAu₄ monolayer (one per unit cell per side) to create UAu₄H₄. Re‑optimize the lattice constant and atomic positions using the same QE settings as in Step 5. Keep the output log.
- Evidence: `/app/outputs/uau4h4_opt.log`

### Step 8: Compute Exchange Coupling J for UAu₄H₄ Monolayer
- Role: scored
- Action: Build a 2×2 supercell of the relaxed hydrogenated structure. Run FM and AFM SOC calculations. Compute ΔE_ex = E_AFM – E_FM and J per unit cell. Write the values to `monolayer_hydrogenated_results.json`.
- Output file: `/app/outputs/monolayer_hydrogenated_results.json`
- Format: json
- Contract:
  `delta_E_ex_meV` (float)
  `J_meV_per_unit_cell` (float)
- Scoring: scored by hidden verifier

### Step 9: Estimate Curie Temperature via Ising Model Monte Carlo
- Role: scored
- Action: Implement a classical spin‑½ Ising model on a 30 × 30 lattice with the J value from Step 8. Perform Metropolis Monte Carlo simulation at a range of temperatures, recording the average magnetization. Extract the Curie temperature (the temperature at which the magnetization approaches zero) and report it in K in `curie_temperature.json`.
- Output file: `/app/outputs/curie_temperature.json`
- Format: json
- Contract:
  `Curie_temperature_K` (float)
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/cluster_results.json`
- `/app/outputs/monolayer_pristine_results.json`
- `/app/outputs/monolayer_hydrogenated_results.json`
- `/app/outputs/curie_temperature.json`

Additional evidence files (logs, structure files) may be produced as described in the process steps.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_results.json
- path: `/app/outputs/cluster_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spin multiplicities and total magnetic moments for neutral and anionic UAu6 clusters.
- schema:
  - `type`: object
  - `required`:
    - `neutral_ground_state_spin_multiplicity`: integer
    - `anion_ground_state_spin_multiplicity`: integer
    - `neutral_total_magnetic_moment_muB`: float
    - `anion_total_magnetic_moment_muB`: float

### monolayer_pristine_results.json
- path: `/app/outputs/monolayer_pristine_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice constant, bond length, magnetic moment, MAE, exchange energy difference, and exchange coupling constant for pristine UAu4 monolayer.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_a_A`: float
    - `bond_length_UAu_A`: float
    - `magnetic_moment_muB`: float
    - `MAE_meV_per_atom`: float
    - `delta_E_ex_meV`: float
    - `J_meV_per_unit_cell`: float

### monolayer_hydrogenated_results.json
- path: `/app/outputs/monolayer_hydrogenated_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Exchange energy difference and exchange coupling constant for fully hydrogenated UAu4H4 monolayer.
- schema:
  - `type`: object
  - `required`:
    - `delta_E_ex_meV`: float
    - `J_meV_per_unit_cell`: float

### curie_temperature.json
- path: `/app/outputs/curie_temperature.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Curie temperature of the ferromagnetic UAu4H4 phase estimated from Monte Carlo simulation.
- schema:
  - `type`: object
  - `required`:
    - `Curie_temperature_K`: float

Notes: All values are compared to hidden paper-reported reference values with appropriate tolerances. Spin multiplicities are expected to be exact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "neutral_ground_state_spin_multiplicity": "integer",
          "anion_ground_state_spin_multiplicity": "integer",
          "neutral_total_magnetic_moment_muB": "float",
          "anion_total_magnetic_moment_muB": "float"
        }
      },
      "description": "Spin multiplicities and total magnetic moments for neutral and anionic UAu6 clusters."
    },
    {
      "file": "monolayer_pristine_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_a_A": "float",
          "bond_length_UAu_A": "float",
          "magnetic_moment_muB": "float",
          "MAE_meV_per_atom": "float",
          "delta_E_ex_meV": "float",
          "J_meV_per_unit_cell": "float"
        }
      },
      "description": "Lattice constant, bond length, magnetic moment, MAE, exchange energy difference, and exchange coupling constant for pristine UAu4 monolayer."
    },
    {
      "file": "monolayer_hydrogenated_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_E_ex_meV": "float",
          "J_meV_per_unit_cell": "float"
        }
      },
      "description": "Exchange energy difference and exchange coupling constant for fully hydrogenated UAu4H4 monolayer."
    },
    {
      "file": "curie_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Curie_temperature_K": "float"
        }
      },
      "description": "Curie temperature of the ferromagnetic UAu4H4 phase estimated from Monte Carlo simulation."
    }
  ],
  "notes": "All values are compared to hidden paper-reported reference values with appropriate tolerances. Spin multiplicities are expected to be exact."
}
```

## How you are scored

A hidden verifier reads the submitted JSON files and compares each numeric value to a reference (the paper’s reported result) using pre‑defined tolerances. Spin multiplicity values are expected to be exact integers. All other values are compared with a small tolerance that accounts for the different computational implementation. The final reward is the fraction of fields that fall within their tolerance; partial credit is given. Simply writing the reference numbers without performing the calculation does not produce the required intermediate evidence and will not pass a consistency check.
