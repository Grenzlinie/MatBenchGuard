# Rotational Transitions and Barriers of H2 in COF-1 and COF-102 via GCMC and Quantum Rotation Calculations

## Problem background
Understanding the rotational dynamics of hydrogen (H₂) molecules adsorbed in covalent organic frameworks (COFs) is essential for characterizing binding sites and evaluating the potential of these materials for hydrogen storage. COF‑1 and COF‑102 are two representative COFs with distinct pore structures. Inelastic neutron scattering (INS) spectra of H₂ adsorbed in these frameworks exhibit features that are linked to rotational excitations, but a computational analysis is required to identify the adsorption sites and compute the corresponding rotational energy levels and barriers. This task reproduces the simulation‑based pipeline that locates the primary H₂ binding sites and calculates the lowest j = 0 → 1 rotational transition energies and the rotational potential energy barriers at those sites.

## Approach
The workflow constructs a classical interaction potential for H₂ in COF‑1 and COF‑102 using Lennard‑Jones parameters taken from the universal force field (UFF) and point partial charges obtained from density‑functional theory (DFT) calculations. The H₂ molecule is described by a rigid five‑site electrostatic model. Grand canonical Monte Carlo (GCMC) simulations are run at 77 K and 87 K at low pressure to map H₂ occupancy in both frameworks. For COF‑1, a single H₂ molecule is located via NVT simulated annealing to find the global energy minimum between two eclipsed B₃O₃ clusters. For COF‑102, the two most populated binding sites—one near a B₃O₃ cluster (site 1) and one on a phenyl ring (site 2)—are extracted from the GCMC occupancy distribution. At each identified site, a two‑dimensional quantum rotation calculation is performed: the rigid‑rotor Schrödinger equation is solved on a sphere under the COF–H₂ potential to obtain rotational energy levels and extract the lowest j = 0 → 1 transition. Additionally, for the primary sites (COF‑1 and COF‑102 site 1), the rotational potential energy surface is mapped by rotating the H₂ molecule at a fixed centre‑of‑mass over a grid of angles and evaluating the interaction energy; the rotational barrier is taken as the maximum minus minimum energy on that surface.

## Reproduction target
Compute and write the following two JSON files in `/app/outputs`:

1. **transition_energies.json** – the lowest j = 0 → 1 rotational transition energies (in meV) for H₂ at three binding sites:
   - `COF1_primary`: primary site in COF‑1 (between two B₃O₃ clusters of eclipsed layers).
   - `COF102_site1`: site 1 in COF‑102 (near a B₃O₃ cluster).
   - `COF102_site2`: site 2 in COF‑102 (on a phenyl ring of a tetraphenylmethyl unit).

2. **rotational_barriers.json** – the rotational potential energy barriers (in meV) for H₂ at the primary adsorption sites:
   - `COF1_barrier`: barrier at the primary site in COF‑1.
   - `COF102_barrier`: barrier at site 1 in COF‑102.

All values must be obtained by running the complete simulation and quantum‑rotation pipeline described in the workflow steps; the numbers depend on the constructed force field, GCMC sampling, site identification, and the quantum solver implementation.

## Assets

- COF-1 crystal structure: 10.1126/science.1119226
- COF-102 crystal structure: 10.1126/science.1140271
- Electronic Supplementary Information (ESI) with force-field parameters and simulation details: 10.1039/c7cp00924k
- GCMC simulation package (RASPA or equivalent): https://github.com/piemachine/raspa
- Five-site H2 electrostatic model (Belof et al.): 10.1021/ct800155u
- 2D quantum rotation solver

## Workflow steps

### Step 1: Retrieve required materials
- Role: process
- Action: Obtain the crystal structures of COF-1 and COF-102 and the Electronic Supplementary Information (ESI) containing force-field parameters, partial charges, and simulation details.
- Evidence: `/app/outputs/cof_structures_and_esi.zip`

### Step 2: Assemble COF–H2 force field
- Role: process
- Action: Extract Lennard-Jones parameters (UFF) and point partial charges (from DFT) from the ESI. Construct the classical interaction potential for H2 in COF-1 and COF-102, incorporating the five-site H2 model of Belof et al.
- Evidence: `/app/outputs/force_field_params.json`

### Step 3: GCMC simulations of H2 adsorption
- Role: process
- Action: Run grand canonical Monte Carlo simulations for H2 in COF-1 (2×2×4 supercell) and COF-102 (unit cell) at 77 K and 87 K, pressures up to ~1.1 atm, to obtain equilibrium H2 occupancy distributions.
- Evidence: `/app/outputs/gcmc_occupancy.npy`

### Step 4: Identify primary H2 site in COF‑1 via simulated annealing
- Role: process
- Action: Perform NVT simulated annealing for a single H2 molecule in COF-1 to locate the global energy minimum between two B3O3 clusters of eclipsed layers. Output fractional coordinates.
- Evidence: `/app/outputs/cof1_primary_site.xyz`

### Step 5: Extract binding sites in COF‑102 from GCMC occupancy
- Role: process
- Action: From the GCMC occupancy map of COF-102, identify the two most populated distinct sites: site1 near a B3O3 cluster, site2 on a phenyl ring of a tetraphenylmethyl unit. Record their coordinates.
- Evidence: `/app/outputs/cof102_sites.xyz`

### Step 6: Compute j=0→1 rotational transitions for H2 at identified sites
- Role: scored (load-bearing)
- Action: For each of the three sites (COF‑1 primary, COF‑102 site1, COF‑102 site2), perform 2D quantum rotation calculations: solve the rigid‑rotor Schrödinger equation on a sphere under the COF–H2 potential grid. Extract the lowest j=0→j=1 transition energy (meV). Write transition_energies.json.
- Output file: `/app/outputs/transition_energies.json`
- Format: json
- Contract: {"COF1_primary": number (meV), "COF102_site1": number (meV), "COF102_site2": number (meV)}
- Scoring: scored by hidden verifier

### Step 7: Compute rotational barriers for primary H2 sites
- Role: scored (load-bearing)
- Action: For the primary sites in COF‑1 and COF‑102 (site1), evaluate the COF–H2 interaction energy on a grid of rotational angles (θ=0..180°, φ=0..360°) with fixed center-of-mass to obtain the rotational potential energy surface. Calculate the barrier as max − min energy. Write rotational_barriers.json.
- Output file: `/app/outputs/rotational_barriers.json`
- Format: json
- Contract: {"COF1_barrier": number (meV), "COF102_barrier": number (meV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_energies.json`
- `/app/outputs/rotational_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_energies.json
- path: `/app/outputs/transition_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lowest j=0→j=1 rotational transition energies for H2 at the primary binding site in COF-1 and at site1 and site2 in COF-102.
- schema:
  - `type`: object
  - `required`:
    - `COF1_primary`: number
    - `COF102_site1`: number
    - `COF102_site2`: number
  - `units`:
    - `COF1_primary`: meV
    - `COF102_site1`: meV
    - `COF102_site2`: meV

### rotational_barriers.json
- path: `/app/outputs/rotational_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Rotational barrier heights for H2 at the primary adsorption sites in COF-1 and COF-102 (site1).
- schema:
  - `type`: object
  - `required`:
    - `COF1_barrier`: number
    - `COF102_barrier`: number
  - `units`:
    - `COF1_barrier`: meV
    - `COF102_barrier`: meV

Notes: Each value is compared to the paper-reported reference using a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "COF1_primary": "number",
          "COF102_site1": "number",
          "COF102_site2": "number"
        },
        "units": {
          "COF1_primary": "meV",
          "COF102_site1": "meV",
          "COF102_site2": "meV"
        }
      },
      "description": "Lowest j=0→j=1 rotational transition energies for H2 at the primary binding site in COF-1 and at site1 and site2 in COF-102."
    },
    {
      "file": "rotational_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "COF1_barrier": "number",
          "COF102_barrier": "number"
        },
        "units": {
          "COF1_barrier": "meV",
          "COF102_barrier": "meV"
        }
      },
      "description": "Rotational barrier heights for H2 at the primary adsorption sites in COF-1 and COF-102 (site1)."
    }
  ],
  "notes": "Each value is compared to the paper-reported reference using a hidden tolerance."
}
```

## How you are scored
A hidden verifier evaluates your `transition_energies.json` and `rotational_barriers.json`. For each of the five scored quantities, your computed value is compared against a hidden reference value using a tolerance that accounts for acceptable differences between legitimate implementations. Meeting or exceeding the expected accuracy gives full credit for that quantity; credit decreases as the deviation grows larger. The final reward is a weighted combination of the individual scores. Simply reporting expected numbers without executing the required simulations and quantum calculations will not satisfy the verifier.
