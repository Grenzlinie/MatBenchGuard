# DFT and NEB based Li-ion battery anode material evaluation for B4N systems

## Problem background
Lithium-ion batteries are the dominant energy storage technology, but commercial graphite anodes have a relatively low specific capacity (~372 mAh/g). Two-dimensional materials are being extensively explored as alternative anodes because of their large surface-to-volume ratio and potentially high Li storage capacity. The quality of an anode is assessed by several key properties: the Li adsorption energy (should be strong enough to prevent clustering but not too strong to hinder release), the specific capacity, the diffusion barriers that control charge/discharge rates, and the volume expansion during lithiation. First-principles density functional theory (DFT) calculations can predict these properties for candidate materials before experimental synthesis. This task investigates monolayer, bilayer, and bulk B₄N as anode materials for Li-ion batteries using DFT and ab initio molecular dynamics (AIMD). The target is to compute the cohesive energy, Li adsorption energy, maximum stable Li loading and its associated specific capacities, Li diffusion barriers, volume expansion upon lithiation, and structural stability at a battery-relevant temperature (350 K).

## Approach
The reproduction uses the SIESTA code to perform spin-polarised DFT calculations with the Perdew-Burke-Ernzerhof (PBE) generalised gradient approximation. Core electrons are described by norm-conserving pseudopotentials from the Abinit FHI database; valence electrons use a double-zeta numerical atomic-orbital basis set. Van der Waals interactions are included via the Grimme D2 correction. The workflow begins by optimising the geometry of a 4×1 supercell of monolayer B₄N (Cmmm symmetry) and computing reference energies of isolated B and N atoms, and of bulk bcc Li metal. Single Li adsorption is screened on eight symmetry-inequivalent sites to identify the most stable binding position. Sequential Li loading on both sides of the monolayer is then performed to determine the maximum number of Li atoms that can be stably adsorbed before the average adsorption energy turns positive; the specific capacity is derived from the maximum loading. Diffusion barriers for Li hopping between the most stable sites are computed via climbing-image nudged elastic band (CI-NEB) for two surface pathways and one pathway perpendicular to the sheet. For bilayer B₄N, four stacking orders (AA, AB1, AB2, AB3) are optimised; the most stable stacking is used to study Li intercalation between the layers. Lithiation drives a structural phase transition to a cavity-channel phase with B–B bridges; the interlayer spacing change gives the volume expansion, and the energy difference between the lithiated cavity-channel and the original layered bilayer yields the stabilisation energy. The same cavity-channel transition is investigated for bulk B₄N. Finally, AIMD simulations in the NVT ensemble at 350 K with a Nosé thermostat verify that the fully lithiated monolayer, bilayer, and bulk structures remain intact on a 5 ps timescale. All computed quantities (cohesive energy, adsorption energies, specific capacities, diffusion barriers, volume expansions, stabilisation energies) are collected and output in a single JSON file.

## Reproduction target
Compute the following numerical results from the SIESTA DFT and NEB/AIMD pipeline and write them to `/app/outputs/reproduced_values.json`:

- Monolayer B₄N cohesive energy (eV).
- Single Li atom adsorption energy on monolayer B₄N (eV).
- Specific capacity for one full Li layer adsorbed on both sides of monolayer B₄N (mAh/g).
- Specific capacity for two full Li layers adsorbed on both sides of monolayer B₄N (mAh/g).
- Li diffusion energy barrier along Path‑1 (H₁ → H₁ over N) on the monolayer (eV).
- Li diffusion energy barrier along Path‑2 (H₁ → H₁ over the B‑triangle) on the monolayer (eV).
- Volume expansion upon full lithiation of bilayer B₄N (percent).
- Li diffusion energy barrier in the bilayer cavity‑channel structure (eV).
- Specific capacity of bulk B₄N in its cavity‑channel phase (mAh/g).
- Volume expansion upon full lithiation of bulk B₄N (percent).
- Li diffusion energy barrier in the bulk cavity‑channel structure (eV).
- Cavity‑channel structure stabilisation energy for bilayer B₄N (eV).
- Cavity‑channel structure stabilisation energy for bulk B₄N (eV).

The output JSON must contain exactly these keys (with their units as shown): `monolayer_cohesive_energy_eV`, `monolayer_single_li_adsorption_energy_eV`, `monolayer_one_layer_specific_capacity_mAh_g`, `monolayer_two_layer_specific_capacity_mAh_g`, `monolayer_diffusion_barrier_path1_eV`, `monolayer_diffusion_barrier_path2_eV`, `bilayer_volume_expansion_percent`, `bilayer_cavity_channel_diffusion_barrier_eV`, `bulk_specific_capacity_mAh_g`, `bulk_volume_expansion_percent`, `bulk_cavity_channel_diffusion_barrier_eV`, `bilayer_cavity_channel_stabilization_energy_eV`, `bulk_cavity_channel_stabilization_energy_eV`. All must be floats.

## Assets

- SIESTA: https://gitlab.com/siesta/siesta
- FHI pseudopotentials (GGA-PBE): https://departments.icmab.es/leem/SIESTA_MATERIAL/Databases/Pseudopotentials/periodictable-gga-abinit.html
- Atomic masses (B, N, Li)

## Workflow steps

### Step 1: Monolayer B4N geometry optimization
- Role: process
- Action: Set up a 4x1 supercell of monolayer B4N with the reported structure and optimize the geometry using DFT with spin-polarized GGA-PBE, double-zeta basis, Grimme D2 van der Waals correction, 280 Ry mesh cutoff, 5x5x1 k-points, relaxing until forces <0.02 eV/A. Record the optimized lattice constants and atomic coordinates.
- Evidence: `/app/outputs/monolayer_optimized.xyz`

### Step 2: Reference energies of isolated B and N atoms
- Role: process
- Action: Compute total energies of an isolated B atom and an isolated N atom in a large box using the same DFT settings as for the monolayer.
- Evidence: `/app/outputs/atomic_energies.dat`

### Step 3: Bulk Li reference energy
- Role: process
- Action: Compute the total energy of bulk bcc Li and extract the per-atom energy E_M using the same DFT settings.
- Evidence: `/app/outputs/bulk_Li_energy.dat`

### Step 4: Single Li adsorption site screening
- Role: process
- Action: Place one Li atom at each of the eight symmetry-inequivalent initial sites on the monolayer surface, relax, and verify convergence to the H1 site. Record the total energy and geometry of the most stable adsorption configuration.
- Evidence: `/app/outputs/single_li_adsorption.json`

### Step 5: Sequential Li loading for maximum capacity
- Role: process
- Action: Add Li atoms step by step on both sides of the 4x1 supercell, relaxing after each addition, until two Li layers per side (16 Li atoms) are formed or average adsorption energy becomes positive. Record total energies for each loading to determine maximum stable loading.
- Evidence: `/app/outputs/sequential_loading_energies.json`

### Step 6: CI-NEB Li diffusion barriers on monolayer
- Role: process
- Action: Using climbing-image NEB with seven images, compute minimum energy paths for Li diffusion on the monolayer along Path-1 (H1 to H1 over N), Path-2 (H1 to H1 over B-triangle), and Path-3 (perpendicular penetration).
- Evidence: `/app/outputs/neb_monolayer_barriers.json`

### Step 7: Bilayer stacking optimization
- Role: process
- Action: Construct AA, AB1, AB2, AB3 bilayer stackings, optimize each with vdW-corrected DFT, and identify the most stable stacking (AB2). Record its interlayer binding energy and spacing.
- Evidence: `/app/outputs/bilayer_stacking_energies.json`

### Step 8: Bilayer lithiation and cavity-channel formation
- Role: process
- Action: Starting from the AB2 bilayer, intercalate Li atoms one by one into the interlayer region up to 8 Li (one layer), fully relaxing each structure with variable interlayer spacing. Observe the structural phase transition to a cavity-channel phase with B-B bridges. Record the lithiated geometry, interlayer expansion, and adsorption energies.
- Evidence: `/app/outputs/bilayer_lithiation_results.json`

### Step 9: Bulk B4N structure optimization
- Role: process
- Action: Build bulk B4N with AB2 stacking and perform variable-cell DFT relaxation allowing all lattice parameters to change. Obtain the equilibrium c lattice constant and interlayer spacing.
- Evidence: `/app/outputs/bulk_optimized.xyz`

### Step 10: Bulk lithiation and cavity-channel formation
- Role: process
- Action: Intercalate 16 Li atoms (8 per layer) into the bulk B4N supercell and relax with variable cell. Verify formation of a cavity-channel phase with B-B bonds connecting layers. Record the lithiated geometry, final c lattice constant, and adsorption energies.
- Evidence: `/app/outputs/bulk_lithiation_results.json`

### Step 11: AIMD thermal stability simulations
- Role: process
- Action: For the fully lithiated monolayer (two Li layers per side), lithiated bilayer cavity-channel, and lithiated bulk cavity-channel, run ab initio molecular dynamics in the NVT ensemble at 350 K for 5 ps using a Nosé thermostat and a 1 fs time step. Check that the structures remain intact.
- Evidence: `/app/outputs/aimd_stability.log`

### Step 12: Compile reproduced numerical results
- Role: scored (load-bearing)
- Action: Collect energies, geometries, barriers, lattice constants, and atomic masses from the previous steps. Compute cohesive energy using the formula (E_coh = (8E_B + 2E_N - E_{B4N})/10), adsorption energies using (E_ad = (E_{M-B4N} - E_{B4N} - n E_M)/n), specific capacities with (Capacity = n_M F / [3.6 (n_B m_B + n_N m_N)]), and volume expansions from interlayer spacings. Write all required quantities to /app/outputs/reproduced_values.json.
- Output file: `/app/outputs/reproduced_values.json`
- Format: json
- Contract: JSON object with keys: monolayer_cohesive_energy_eV (float), monolayer_single_li_adsorption_energy_eV (float), monolayer_one_layer_specific_capacity_mAh_g (float), monolayer_two_layer_specific_capacity_mAh_g (float), monolayer_diffusion_barrier_path1_eV (float), monolayer_diffusion_barrier_path2_eV (float), bilayer_volume_expansion_percent (float), bilayer_cavity_channel_diffusion_barrier_eV (float), bulk_specific_capacity_mAh_g (float), bulk_volume_expansion_percent (float), bulk_cavity_channel_diffusion_barrier_eV (float), bilayer_cavity_channel_stabilization_energy_eV (float), bulk_cavity_channel_stabilization_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_values.json
- path: `/app/outputs/reproduced_values.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored artifact containing all required numerical values for the B4N anode materials. The checker will compare each field to hidden reference values using directional tolerance (threshold_or_better).
- schema:
  - `type`: object
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `monolayer_cohesive_energy_eV`: eV
    - `monolayer_single_li_adsorption_energy_eV`: eV
    - `monolayer_one_layer_specific_capacity_mAh_g`: mAh/g
    - `monolayer_two_layer_specific_capacity_mAh_g`: mAh/g
    - `monolayer_diffusion_barrier_path1_eV`: eV
    - `monolayer_diffusion_barrier_path2_eV`: eV
    - `bilayer_volume_expansion_percent`: %
    - `bilayer_cavity_channel_diffusion_barrier_eV`: eV
    - `bulk_specific_capacity_mAh_g`: mAh/g
    - `bulk_volume_expansion_percent`: %
    - `bulk_cavity_channel_diffusion_barrier_eV`: eV
    - `bilayer_cavity_channel_stabilization_energy_eV`: eV
    - `bulk_cavity_channel_stabilization_energy_eV`: eV

Notes: AIMD evidence is required but not numerically scored. The checker verifies that the AIMD log indicates structural integrity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "monolayer_cohesive_energy_eV": "eV",
          "monolayer_single_li_adsorption_energy_eV": "eV",
          "monolayer_one_layer_specific_capacity_mAh_g": "mAh/g",
          "monolayer_two_layer_specific_capacity_mAh_g": "mAh/g",
          "monolayer_diffusion_barrier_path1_eV": "eV",
          "monolayer_diffusion_barrier_path2_eV": "eV",
          "bilayer_volume_expansion_percent": "%",
          "bilayer_cavity_channel_diffusion_barrier_eV": "eV",
          "bulk_specific_capacity_mAh_g": "mAh/g",
          "bulk_volume_expansion_percent": "%",
          "bulk_cavity_channel_diffusion_barrier_eV": "eV",
          "bilayer_cavity_channel_stabilization_energy_eV": "eV",
          "bulk_cavity_channel_stabilization_energy_eV": "eV"
        }
      },
      "description": "Scored artifact containing all required numerical values for the B4N anode materials. The checker will compare each field to hidden reference values using directional tolerance (threshold_or_better)."
    }
  ],
  "notes": "AIMD evidence is required but not numerically scored. The checker verifies that the AIMD log indicates structural integrity."
}
```

## How you are scored
A hidden verifier independently reads your `/app/outputs/reproduced_values.json`. Every field is scored individually against a hidden reference value using a directional threshold‑or‑better policy: if your computed quantity equals or exceeds the reference performance, you earn full credit for that field; if it falls below, credit is awarded proportionally to how close it is. The overall reward is a weighted combination of the individual field scores. The intermediate process evidence (such as optimised geometries, energy logs, NEB results, and the AIMD stability log) is required to be present and is checked for basic validity, but only the final numerical results in `reproduced_values.json` carry substantial weight. Fabricating numbers without running the required DFT and NEB calculations will not satisfy the intermediate evidence checks.
