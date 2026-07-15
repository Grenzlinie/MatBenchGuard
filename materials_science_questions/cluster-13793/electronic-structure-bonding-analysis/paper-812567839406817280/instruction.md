# TiC/γ-Fe Interface Stability by First-Principles Calculations

## Problem background
TiC-reinforced 316L stainless steel composites prepared by selective laser melting derive their mechanical performance from the stability of the interface between the reinforcing TiC particles and the γ-Fe matrix. First-principles calculations can determine the interfacial adhesion, energy, and bonding, thereby identifying which atomic-scale configuration of the TiC(001)/γ-Fe(001) interface is most stable and potentially capable of heterogeneous nucleation of γ-Fe. This task aims to compute the adhesion work, interfacial distance, and interfacial energy for four candidate interface models to resolve the most stable arrangement.

## Approach
The computational method uses density functional theory (DFT) with the GGA-PBE exchange-correlation functional and a plane-wave pseudopotential approach (e.g., Quantum ESPRESSO). Bulk γ-Fe (FCC) and TiC (NaCl-type) are optimized to obtain equilibrium lattice constants. Surface slabs of TiC(001) with C-centre and Ti-centre terminations and γ-Fe(001) with 5 atomic layers and 1 nm vacuum are constructed; surface energies are computed after relaxation. Four interface supercells are built by stacking the 5-layer slabs: Fe-on-C centre (on-site), Fe-on-Ti centre (on-site), Fe-bridge-C centre, and Fe-bridge-Ti centre. Each supercell is fully relaxed. The adhesion work is calculated from the energy difference between the interface and the separated relaxed slabs in the same supercell geometry, the interfacial distance is measured between the first layers, and the interfacial energy is obtained from the total energy, bulk chemical potentials, and surface energies via a standard thermodynamic relation.

## Reproduction target
Compute and report, for each of the four TiC(001)/γ-Fe(001) interface models (Fe-on-C centre, Fe-on-Ti centre, Fe-bridge-C centre, Fe-bridge-Ti centre) after full relaxation: (1) interfacial distance d₀ (nm), (2) adhesion work W_ad (J/m²), and (3) interfacial energy γ_int (J/m²). Also, identify the model with the largest W_ad and the smallest γ_int. Provide the bulk properties (lattice constant, volume, bulk modulus, formation enthalpy) of TiC and γ-Fe as a validation step.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard PBE pseudopotential library: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Bulk DFT optimization and property calculation
- Role: scored
- Action: Perform DFT geometry optimization of bulk TiC (NaCl-type, FM-3M) and γ-Fe (FCC, FM-3M) using the GGA-PBE functional. Determine the lattice constant, cell volume, bulk modulus, and formation enthalpy of TiC.
- Output file: `/app/outputs/step_01_bulk_properties.csv`
- Format: csv
- Contract: phase,method,lattice_constant_a_nm,volume_nm3,bulk_modulus_GPa,formation_enthalpy_eV_per_atom
- Scoring: scored by hidden verifier

### Step 2: Surface convergence and surface energy calculation
- Role: process
- Action: Construct TiC(001) slabs with C-centre and Ti-centre terminations and γ-Fe(001) slabs with 5 atomic layers and a 1 nm vacuum. Perform surface relaxations and compute surface energies using the standard slab energy formula. Record the converged surface energies (σ_TiC and σ_Fe for Ti-centre and C-centre terminations).
- Evidence: `/app/outputs/surface_energies.csv`

### Step 3: Interface model construction
- Role: process
- Action: Using the 5-layer TiC(001) and γ-Fe(001) slabs, construct four interface supercells by stacking them with a 1 nm vacuum: (a) Fe-on-C centre (on-site, C-centre termination), (b) Fe-on-Ti centre (on-site, Ti-centre termination), (c) Fe-bridge-C centre (bridge-site, C-centre), (d) Fe-bridge-Ti centre (bridge-site, Ti-centre). Each supercell should have the in-plane lattice matched to the equilibrium lattice constant of TiC (from step_bulk).
- Evidence: none

### Step 4: Interface relaxation and energetic analysis
- Role: scored (load-bearing)
- Action: Fully relax each constructed interface supercell using DFT (GGA-PBE). For fully relaxed geometries, compute (i) interfacial distance d₀ between the first layers, (ii) adhesion work W_ad = (E_total^Fe + E_total^TiC - E_total^Fe/TiC)/A using energies of isolated relaxed slabs computed in the same supercell geometry, and (iii) interfacial energy γ_int using the standard chemical-potential/surface-energy formulation with bulk chemical potentials from step_bulk and surface energies from step_surface. Report results for all four models.
- Output file: `/app/outputs/step_04_interface_energetics.csv`
- Format: csv
- Contract: termination,stacking,d0_nm,W_ad_J_per_m2,gamma_int_J_per_m2
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bulk_properties.csv`
- `/app/outputs/step_04_interface_energetics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bulk_properties.csv
- path: `/app/outputs/step_01_bulk_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bulk properties of TiC and γ-Fe computed with DFT (GGA-PBE), validating the computational setup and providing reference chemical potentials.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `method`, `lattice_constant_a_nm`, `volume_nm3`, `bulk_modulus_GPa`, `formation_enthalpy_eV_per_atom`
  - `units`:
    - `lattice_constant_a_nm`: nm
    - `volume_nm3`: nm^3
    - `bulk_modulus_GPa`: GPa
    - `formation_enthalpy_eV_per_atom`: eV/atom

### step_04_interface_energetics.csv
- path: `/app/outputs/step_04_interface_energetics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adhesion work, interfacial distance, and interfacial energy for four TiC(001)/γ-Fe(001) interface models, used to identify the most stable configuration.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `stacking`, `d0_nm`, `W_ad_J_per_m2`, `gamma_int_J_per_m2`
  - `units`:
    - `d0_nm`: nm
    - `W_ad_J_per_m2`: J/m^2
    - `gamma_int_J_per_m2`: J/m^2

Notes: The surface energy calculation (step_surface) provides intermediate quantities that enable the interfacial energy formula; the agent must record them but they are not directly scored. The unrelaxed UBER curves and electronic structure analysis are omitted per task scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bulk_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "method",
          "lattice_constant_a_nm",
          "volume_nm3",
          "bulk_modulus_GPa",
          "formation_enthalpy_eV_per_atom"
        ],
        "units": {
          "lattice_constant_a_nm": "nm",
          "volume_nm3": "nm^3",
          "bulk_modulus_GPa": "GPa",
          "formation_enthalpy_eV_per_atom": "eV/atom"
        }
      },
      "description": "Bulk properties of TiC and γ-Fe computed with DFT (GGA-PBE), validating the computational setup and providing reference chemical potentials."
    },
    {
      "file": "step_04_interface_energetics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "stacking",
          "d0_nm",
          "W_ad_J_per_m2",
          "gamma_int_J_per_m2"
        ],
        "units": {
          "d0_nm": "nm",
          "W_ad_J_per_m2": "J/m^2",
          "gamma_int_J_per_m2": "J/m^2"
        }
      },
      "description": "Adhesion work, interfacial distance, and interfacial energy for four TiC(001)/γ-Fe(001) interface models, used to identify the most stable configuration."
    }
  ],
  "notes": "The surface energy calculation (step_surface) provides intermediate quantities that enable the interfacial energy formula; the agent must record them but they are not directly scored. The unrelaxed UBER curves and electronic structure analysis are omitted per task scope."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. For Step 1, your reported lattice constant, volume, bulk modulus, and formation enthalpy are compared to hidden reference values. For Step 4, your reported d₀, W_ad, γ_int for each model are compared to hidden reference values, and the verifier also checks whether you correctly identified the model with the largest adhesion work and smallest interfacial energy. The scores are combined by weight into a final reward. The verification uses tolerances that account for the typical spread of DFT calculations performed with different codes and pseudopotentials; therefore, simply self-reporting an approximate number is unlikely to match unless a genuine first-principles relaxation was carried out.
