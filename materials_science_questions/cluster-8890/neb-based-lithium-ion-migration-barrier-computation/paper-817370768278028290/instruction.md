# DFT-calculated Solid Electrolyte Interphase Properties for Li₂CN₂ Material

## Problem background
Lithium metal batteries are promising high-energy storage systems, but their practical use is hindered by uncontrolled dendrite growth and unstable solid electrolyte interphases (SEI) at the lithium anode. A stable SEI must possess a combination of properties: strong anti-reduction stability (so it does not decompose against the lithium electrode), good lithiophilicity (enabling uniform lithium nucleation with low overpotential), and mechanical robustness that resists dendrite propagation. These properties can be evaluated computationally via density functional theory (DFT) by calculating quantities such as HOMO/LUMO energy levels, adsorption energies of lithium on the SEI surface, interfacial energies between lithium and the SEI material, and the bulk modulus of the SEI component. This task computes these quantities for a candidate SEI material, Li₂CN₂, along with two well-known reference SEI components, Li₂CO₃ and LiF, to enable a quantitative comparison of their anti-reduction stability and dendrite suppression ability.

## Approach
The computational approach uses plane-wave density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and standard pseudopotentials, implemented in an open-source code such as Quantum ESPRESSO. Crystal structures for Li metal (bcc), Li₂CN₂ (tetragonal), Li₂CO₃, and LiF are obtained from the Materials Project database. The molecular structure of dicyandiamide (DCDA) is obtained from PubChem. Geometry optimizations and total energy calculations are performed for all reactant and product species, and Gibbs free energies are estimated using approximate thermodynamic corrections (zero-point energy and entropy). The overall reaction Gibbs free energy for the proposed formation of Li₂CN₂ and C from metallic Li and DCDA (with NH₃ as a by-product) is computed. HOMO and LUMO energies are extracted as Kohn-Sham eigenvalues from single-point DFT calculations on the relaxed bulk phases of Li₂CN₂, Li₂CO₃, and LiF. Lithium adsorption energies on the Li₂CN₂ surface are calculated by constructing a slab model and placing a lithium atom at two distinct surface sites (top and side configurations). To obtain interfacial energies, coincidence-site lattice interface models between Li metal and each SEI material (Li₂CN₂, Li₂CO₃, LiF) are constructed, relaxed, and their total energies are used to compute the energy cost of forming the interface. Bulk moduli are obtained by applying small lattice strains to the relaxed bulk phases and fitting the resulting energy–strain curves to elastic constants. Finally, the γE product (interfacial energy multiplied by bulk modulus) is derived for each Li/SEI interface as a combined measure of dendrite suppression capability.

## Reproduction target
Using DFT calculations as described in the Approach, compute and report the following quantities in a single JSON file at /app/outputs/dft_results.json:

- Gibbs free energy change (ΔG, kJ/mol) for the reaction 3 DCDA + 8 Li → 4 Li₂CN₂ + 2 C + 4 NH₃.
- HOMO and LUMO energies (eV) for bulk Li₂CN₂, Li₂CO₃, and LiF.
- Li adsorption energies (eV) on the Li₂CN₂ surface for two distinct adsorption sites (top and side).
- Interfacial energies (meV/Å²) for the Li/Li₂CN₂, Li/Li₂CO₃, and Li/LiF interfaces.
- Bulk moduli (GPa) of Li₂CN₂, Li₂CO₃, and LiF.
- The γE product (interfacial energy multiplied by bulk modulus, meV/Å²·GPa) for each of the three interfaces.

The output must follow the exact field names and units specified in the output contract. The hidden verifier will compare your computed values against reference benchmarks and will evaluate the relative trends among the three materials to assess their predicted anti-reduction stability and dendrite suppression ability. You are not provided with the reference values; your task is to perform the full computational workflow and report the results faithfully.

## Assets

- Materials Project crystal structures: Public database at https://materialsproject.org; provides CIF files for Li, Li2CN2, Li2CO3, LiF.
- Dicyandiamide molecular structure: PubChem CID 545987; accessible via https://pubchem.ncbi.nlm.nih.gov/compound/545987
- Quantum ESPRESSO: Open-source plane-wave DFT code available at https://www.quantum-espresso.org/; installable via conda or source.
- SSSP pseudopotentials: PBE efficiency library from Materials Cloud https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT total energy calculations for reaction species
- Role: process
- Action: Perform DFT geometry optimization and total energy calculations for Li metal (bcc), dicyandiamide (DCDA) molecule, Li₂CN₂ (tetragonal), carbon (graphite or diamond), and NH₃ molecule using Quantum ESPRESSO. Compute Gibbs free energies via standard thermodynamic corrections (zero-point and entropic). Store computed energies for later use.
- Evidence: `/app/outputs/reaction_energies.json`

### Step 2: HOMO-LUMO energy calculations
- Role: process
- Action: Using relaxed structures of Li₂CN₂, Li₂CO₃, and LiF, perform single-point DFT calculations to obtain Kohn-Sham eigenvalues. Extract HOMO and LUMO energies as the highest occupied and lowest unoccupied eigenvalues.
- Evidence: `/app/outputs/homo_lumo.json`

### Step 3: Li adsorption energy on Li₂CN₂ surface
- Role: process
- Action: Construct slab models of Li₂CN₂ surface; place a Li atom at two distinct adsorption sites (top and side configurations). Perform geometry relaxation for slab+Li system, clean slab, and isolated Li atom. Compute adsorption energies: E_ads = E_{slab+Li} - E_{slab} - E_{Li}.
- Evidence: `/app/outputs/adsorption_energies.json`

### Step 4: Interfacial energy and bulk modulus calculations
- Role: process
- Action: Build coincidence-site lattice interface models for Li/Li₂CN₂, Li/Li₂CO₃, Li/LiF. Relax interfaces and compute interfacial energies γ = (E_interface - E_Li_slab - E_SEI_slab)/(2A). For bulk Li₂CN₂, Li₂CO₃, LiF, apply small lattice strains to compute elastic constants and obtain bulk moduli E.
- Evidence: `/app/outputs/interface_bulk_props.json`

### Step 5: Compile DFT results into output JSON
- Role: scored (load-bearing)
- Action: Collect all computed quantities: reaction ΔG (4G(Li₂CN₂)+2G(C)+4G(NH₃) - 3G(DCDA) - 8G(Li)), HOMO/LUMO energies, Li adsorption energies, interfacial energies, bulk moduli, and γE products. Write into /app/outputs/dft_results.json following exact schema.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"reaction_delta_G_kJ_per_mol": float, "HOMO_Li2CN2_eV": float, "LUMO_Li2CN2_eV": float, "HOMO_Li2CO3_eV": float, "LUMO_Li2CO3_eV": float, "HOMO_LiF_eV": float, "LUMO_LiF_eV": float, "Li_adsorption_energy_top_eV": float, "Li_adsorption_energy_side_eV": float, "interfacial_energy_Li2CN2_meV_per_A2": float, "interfacial_energy_Li2CO3_meV_per_A2": float, "interfacial_energy_LiF_meV_per_A2": float, "bulk_modulus_Li2CN2_GPa": float, "bulk_modulus_Li2CO3_GPa": float, "bulk_modulus_LiF_GPa": float, "gamma_E_Li2CN2_meV_per_A2_GPa": float, "gamma_E_Li2CO3_meV_per_A2_GPa": float, "gamma_E_LiF_meV_per_A2_GPa": float}
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
- target_policy: reference_match
- description: Aggregate DFT results: reaction energetics, HOMO/LUMO levels, Li adsorption energies, interfacial energies, bulk moduli, and γE products for Li₂CN₂, Li₂CO₃, LiF.
- schema:
  - `type`: object
  - `required`: `reaction_delta_G_kJ_per_mol`, `HOMO_Li2CN2_eV`, `LUMO_Li2CN2_eV`, `HOMO_Li2CO3_eV`, `LUMO_Li2CO3_eV`, `HOMO_LiF_eV`, `LUMO_LiF_eV`, `Li_adsorption_energy_top_eV`, `Li_adsorption_energy_side_eV`, `interfacial_energy_Li2CN2_meV_per_A2`, `interfacial_energy_Li2CO3_meV_per_A2`, `interfacial_energy_LiF_meV_per_A2`, `bulk_modulus_Li2CN2_GPa`, `bulk_modulus_Li2CO3_GPa`, `bulk_modulus_LiF_GPa`, `gamma_E_Li2CN2_meV_per_A2_GPa`, `gamma_E_Li2CO3_meV_per_A2_GPa`, `gamma_E_LiF_meV_per_A2_GPa`
  - `properties`:
    - `reaction_delta_G_kJ_per_mol`:
      - `type`: number
      - `description`: Reaction Gibbs free energy in kJ/mol
    - `HOMO_Li2CN2_eV`:
      - `type`: number
      - `description`: HOMO energy of Li₂CN₂ in eV
    - `LUMO_Li2CN2_eV`:
      - `type`: number
      - `description`: LUMO energy of Li₂CN₂ in eV
    - `HOMO_Li2CO3_eV`:
      - `type`: number
      - `description`: HOMO energy of Li₂CO₃ in eV
    - `LUMO_Li2CO3_eV`:
      - `type`: number
      - `description`: LUMO energy of Li₂CO₃ in eV
    - `HOMO_LiF_eV`:
      - `type`: number
      - `description`: HOMO energy of LiF in eV
    - `LUMO_LiF_eV`:
      - `type`: number
      - `description`: LUMO energy of LiF in eV
    - `Li_adsorption_energy_top_eV`:
      - `type`: number
      - `description`: Li adsorption energy on top site of Li₂CN₂ in eV
    - `Li_adsorption_energy_side_eV`:
      - `type`: number
      - `description`: Li adsorption energy on side site of Li₂CN₂ in eV
    - `interfacial_energy_Li2CN2_meV_per_A2`:
      - `type`: number
      - `description`: Li/Li₂CN₂ interfacial energy in meV/Å²
    - `interfacial_energy_Li2CO3_meV_per_A2`:
      - `type`: number
      - `description`: Li/Li₂CO₃ interfacial energy in meV/Å²
    - `interfacial_energy_LiF_meV_per_A2`:
      - `type`: number
      - `description`: Li/LiF interfacial energy in meV/Å²
    - `bulk_modulus_Li2CN2_GPa`:
      - `type`: number
      - `description`: Bulk modulus of Li₂CN₂ in GPa
    - `bulk_modulus_Li2CO3_GPa`:
      - `type`: number
      - `description`: Bulk modulus of Li₂CO₃ in GPa
    - `bulk_modulus_LiF_GPa`:
      - `type`: number
      - `description`: Bulk modulus of LiF in GPa
    - `gamma_E_Li2CN2_meV_per_A2_GPa`:
      - `type`: number
      - `description`: γE product for Li/Li₂CN₂
    - `gamma_E_Li2CO3_meV_per_A2_GPa`:
      - `type`: number
      - `description`: γE product for Li/Li₂CO₃
    - `gamma_E_LiF_meV_per_A2_GPa`:
      - `type`: number
      - `description`: γE product for Li/LiF

Notes: The hidden checker will compare each numeric field to the paper's reported values within appropriate tolerances and verify that LUMO_Li2CN2 > LUMO_Li2CO3 > LUMO_LiF and that γE(Li₂CN₂) is the highest among the three interfaces. Li-ion diffusion barriers are excluded from this reproduction task.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "reaction_delta_G_kJ_per_mol",
          "HOMO_Li2CN2_eV",
          "LUMO_Li2CN2_eV",
          "HOMO_Li2CO3_eV",
          "LUMO_Li2CO3_eV",
          "HOMO_LiF_eV",
          "LUMO_LiF_eV",
          "Li_adsorption_energy_top_eV",
          "Li_adsorption_energy_side_eV",
          "interfacial_energy_Li2CN2_meV_per_A2",
          "interfacial_energy_Li2CO3_meV_per_A2",
          "interfacial_energy_LiF_meV_per_A2",
          "bulk_modulus_Li2CN2_GPa",
          "bulk_modulus_Li2CO3_GPa",
          "bulk_modulus_LiF_GPa",
          "gamma_E_Li2CN2_meV_per_A2_GPa",
          "gamma_E_Li2CO3_meV_per_A2_GPa",
          "gamma_E_LiF_meV_per_A2_GPa"
        ],
        "properties": {
          "reaction_delta_G_kJ_per_mol": {
            "type": "number",
            "description": "Reaction Gibbs free energy in kJ/mol"
          },
          "HOMO_Li2CN2_eV": {
            "type": "number",
            "description": "HOMO energy of Li₂CN₂ in eV"
          },
          "LUMO_Li2CN2_eV": {
            "type": "number",
            "description": "LUMO energy of Li₂CN₂ in eV"
          },
          "HOMO_Li2CO3_eV": {
            "type": "number",
            "description": "HOMO energy of Li₂CO₃ in eV"
          },
          "LUMO_Li2CO3_eV": {
            "type": "number",
            "description": "LUMO energy of Li₂CO₃ in eV"
          },
          "HOMO_LiF_eV": {
            "type": "number",
            "description": "HOMO energy of LiF in eV"
          },
          "LUMO_LiF_eV": {
            "type": "number",
            "description": "LUMO energy of LiF in eV"
          },
          "Li_adsorption_energy_top_eV": {
            "type": "number",
            "description": "Li adsorption energy on top site of Li₂CN₂ in eV"
          },
          "Li_adsorption_energy_side_eV": {
            "type": "number",
            "description": "Li adsorption energy on side site of Li₂CN₂ in eV"
          },
          "interfacial_energy_Li2CN2_meV_per_A2": {
            "type": "number",
            "description": "Li/Li₂CN₂ interfacial energy in meV/Å²"
          },
          "interfacial_energy_Li2CO3_meV_per_A2": {
            "type": "number",
            "description": "Li/Li₂CO₃ interfacial energy in meV/Å²"
          },
          "interfacial_energy_LiF_meV_per_A2": {
            "type": "number",
            "description": "Li/LiF interfacial energy in meV/Å²"
          },
          "bulk_modulus_Li2CN2_GPa": {
            "type": "number",
            "description": "Bulk modulus of Li₂CN₂ in GPa"
          },
          "bulk_modulus_Li2CO3_GPa": {
            "type": "number",
            "description": "Bulk modulus of Li₂CO₃ in GPa"
          },
          "bulk_modulus_LiF_GPa": {
            "type": "number",
            "description": "Bulk modulus of LiF in GPa"
          },
          "gamma_E_Li2CN2_meV_per_A2_GPa": {
            "type": "number",
            "description": "γE product for Li/Li₂CN₂"
          },
          "gamma_E_Li2CO3_meV_per_A2_GPa": {
            "type": "number",
            "description": "γE product for Li/Li₂CO₃"
          },
          "gamma_E_LiF_meV_per_A2_GPa": {
            "type": "number",
            "description": "γE product for Li/LiF"
          }
        }
      },
      "description": "Aggregate DFT results: reaction energetics, HOMO/LUMO levels, Li adsorption energies, interfacial energies, bulk moduli, and γE products for Li₂CN₂, Li₂CO₃, LiF."
    }
  ],
  "notes": "The hidden checker will compare each numeric field to the paper's reported values within appropriate tolerances and verify that LUMO_Li2CN2 > LUMO_Li2CO3 > LUMO_LiF and that γE(Li₂CN₂) is the highest among the three interfaces. Li-ion diffusion barriers are excluded from this reproduction task."
}
```

## How you are scored
Each workflow step produces an output file. A hidden verifier reads these files and independently scores your computed quantities by comparing them to reference values (derived from the original study) with appropriate tolerances, and by verifying the required relative ordering among the three SEI materials for the LUMO energies and for the γE product. The tolerances account for differences in DFT implementation and parameter choices, but the comparisons assess whether your calculations reproduce the key physical trends. The stage scores are combined by weight (with the final compilation step carrying the largest weight) to produce a single reward between 0 and 1. Simply reproducing literature values without performing the DFT workflow will not succeed — your score depends on the agreement between your own computed results and the hidden benchmarks.
