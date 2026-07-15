# Magnetoelastic coupling and surface energy analysis of Fe-Ga alloys via DFT

## Problem background
Fe-Ga alloys (Galfenol) are rare-earth-free magnetostrictive materials with promising properties for sensors, actuators, and energy harvesters. Their tetragonal magnetostriction λ001 depends on the magnetoelastic coupling coefficient B1 and the tetragonal shear modulus C'. Enhancing λ001 is critical for practical applications. This work investigates two strategies: (1) substituting a small fraction of Ga with Ag or Cu to tune the total valence electron count and increase B1, and (2) using surface adsorbents (O, Os, H2S) to modify surface energies of different crystal facets, aiming to promote (001) grain alignment. Quantifying these effects requires first-principles DFT calculations of total energy, magnetocrystalline anisotropy energy, and surface energies under controlled strain and chemical potential conditions.

## Approach
The methodology is based on spin-polarized DFT with spin-orbit coupling and the projector augmented wave method. For bulk alloys, a 128-atom supercell of the base alloy Fe79.7Ga20.3 is built, and two ternary alloys (Fe79.7Ga18.7Ag1.6 and Fe79.7Ga18.7Cu1.6) are constructed by replacing two Ga atoms with Ag or Cu atoms placed far apart. Total energies and magnetocrystalline anisotropy energies (EMCA) are computed under tetragonal strains of ±1% at constant volume using the torque method. To understand the electronic origin, a rigid-band analysis is performed by shifting the Fermi level of the pristine alloy's self-consistent electronic structure and recomputing EMCA as a function of total valence electron count N_e. For surface studies, slab models with 9 atomic layers and 12 Å vacuum are built for (001), (110), and (111) facets, with Ga coverages of 0%, 50%, 75%, and 100% in the topmost layer, and adsorbents (O, Os, H2S) placed at their preferred sites. Surface energies are then computed as a function of the Ga chemical potential μGa, using the bulk D03 Fe13Ga3 chemical potential constraint. The entire workflow uses an open-source DFT code such as Quantum ESPRESSO with appropriate pseudopotentials.

## Reproduction target
Compute the following and write them to the specified output files:

- **strain_and_emca_results.csv**: For the three alloys (Fe79.7Ga20.3, Fe79.7Ga18.7Ag1.6, Fe79.7Ga18.7Cu1.6) at strains of -0.01, 0, and +0.01, report total energy (eV per supercell) and magnetocrystalline anisotropy energy EMCA (eV per supercell). From these data, the magnetoelastic coupling coefficient B1 and tetragonal shear modulus C' can be derived.

- **emca_vs_electron_count.csv**: For the pristine alloy under ±1% strain, report EMCA (eV per atom) as a function of total valence electron count N_e, for integer N_e ranging from 1140 to 1168 in steps of 2.

- **surface_energies.csv**: For each combination of surface orientation (001, 110, 111), Ga coverage (0%, 50%, 75%, 100%), and adsorbent (none, O, Os, H2S), report the surface energy (J/m²) at Ga chemical potentials μGa from -4.0 eV to 0 eV in steps of at most 0.5 eV. Use the constraint μ_Fe13Ga3 = 13 μ_Fe + 3 μ_Ga with the bulk D03 Fe13Ga3 chemical potential.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP, GBRV): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare and relax bulk Fe-Ga supercells
- Role: process
- Action: Build a 128-atom cubic supercell for Fe79.7Ga20.3 (102 Fe, 26 Ga). Create two ternary supercells Fe79.7Ga18.7Ag1.6 and Fe79.7Ga18.7Cu1.6 by replacing two Ga atoms with Ag or Cu atoms placed far apart (distance > 4.1 Å). Relax atomic positions and lattice parameters using DFT to obtain optimized structures.
- Evidence: `/app/outputs/step01_relaxation.log`

### Step 2: DFT strain-dependent total energy and magnetocrystalline anisotropy for bulk alloys
- Role: scored (load-bearing)
- Action: For each relaxed alloy (pristine, Ag, Cu), apply tetragonal strains of -1%, 0%, +1% along z under constant volume (εx = εy = -εz/2). Perform self-consistent DFT calculations with spin-orbit coupling to obtain total energy and magnetocrystalline anisotropy energy (E_MCA) using the torque method. Write the results to /app/outputs/strain_and_emca_results.csv.
- Output file: `/app/outputs/strain_and_emca_results.csv`
- Format: csv
- Contract: A CSV with columns: Alloy (string: 'Fe79.7Ga20.3', 'Fe79.7Ga18.7Ag1.6', 'Fe79.7Ga18.7Cu1.6'), Strain (float, e.g., -0.01, 0.00, 0.01), E_total (float, eV per supercell), E_MCA (float, eV per supercell).
- Scoring: scored by hidden verifier

### Step 3: Rigid-band analysis of MCA vs electron count
- Role: scored
- Action: Using the self-consistent electronic structure of pristine Fe79.7Ga20.3 at ±1% strain, shift the Fermi level to vary the total number of valence electrons N_e, and recompute E_MCA for each N_e. Record the E_MCA values for a range of N_e (e.g., 1140 to 1168 in steps of 2) for both strain states. Write the results to /app/outputs/emca_vs_electron_count.csv.
- Output file: `/app/outputs/emca_vs_electron_count.csv`
- Format: csv
- Contract: A CSV with columns: N_e (integer), strain_plus1_E_MCA (float, eV per atom), strain_minus1_E_MCA (float, eV per atom).
- Scoring: scored by hidden verifier

### Step 4: Build Fe-Ga surface slabs with adsorbates
- Role: process
- Action: Construct slab models (9 atomic layers, 12 Å vacuum) for (001), (110), (111) surfaces of Fe-Ga with Ga coverages 0%, 50%, 75%, 100% in the topmost layer. For each orientation/coverage, add an O atom, Os atom, or H2S molecule at preferred adsorption sites (O atop Ga, Os at bridge, H2S atop Ga). Also prepare clean surfaces.
- Evidence: `/app/outputs/step04_slab_build.log`

### Step 5: DFT surface energies of Fe-Ga with adsorbates
- Role: scored (load-bearing)
- Action: Perform DFT calculations for all slab models to obtain total energies. Compute surface energy γ = (1/(2A))[E_slab+ads - N_Fe μ_Fe - N_Ga μ_Ga - N_ads μ_ads] with constraint μ_Fe13Ga3 = 13 μ_Fe + 3 μ_Ga, using the bulk D0_3 Fe13Ga3 chemical potential. Evaluate γ as a function of μ_Ga from -4.0 eV to 0 eV in steps ≤0.5 eV. Write orientation, Ga coverage, adsorbent, μ_Ga, and surface energy (J/m²) to /app/outputs/surface_energies.csv.
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: A CSV with columns: Orientation (string: 001, 110, 111), Ga_coverage (string: e.g., 0%, 50%, 75%, 100%), Adsorbent (string: none, O, Os, H2S), mu_Ga (float, eV), Surface_energy (float, J/m^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strain_and_emca_results.csv`
- `/app/outputs/emca_vs_electron_count.csv`
- `/app/outputs/surface_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strain_and_emca_results.csv
- path: `/app/outputs/strain_and_emca_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Strain-dependent total energies and magnetocrystalline anisotropy energies for pristine and ternary Fe-Ga alloys. The checker recomputes the magnetoelastic coupling coefficient B1 and tetragonal shear modulus C' from these data.
- schema:
  - `type`: table
  - `required_columns`: `Alloy`, `Strain`, `E_total`, `E_MCA`
  - `units`:
    - `Strain`: unitless (fraction)
    - `E_total`: eV per supercell
    - `E_MCA`: eV per supercell

### emca_vs_electron_count.csv
- path: `/app/outputs/emca_vs_electron_count.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: E_MCA as a function of total valence electron count for the pristine Fe79.7Ga20.3 alloy under ±1% tetragonal strain. The checker verifies that the separation between the two curves increases as N_e deviates from the pristine value.
- schema:
  - `type`: table
  - `required_columns`: `N_e`, `strain_plus1_E_MCA`, `strain_minus1_E_MCA`
  - `units`:
    - `N_e`: integer (count)
    - `strain_plus1_E_MCA`: eV per atom
    - `strain_minus1_E_MCA`: eV per atom

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Surface energies for (001), (110), (111) Fe-Ga facets with O, Os, H2S adsorbents and clean, plotted against Ga chemical potential. The checker verifies that (001) becomes more stable than (110) in a Ga-poor condition for active adsorbents, and (111) remains higher.
- schema:
  - `type`: table
  - `required_columns`: `Orientation`, `Ga_coverage`, `Adsorbent`, `mu_Ga`, `Surface_energy`
  - `units`:
    - `mu_Ga`: eV
    - `Surface_energy`: J/m^2

Notes: The checker recomputes B1 and C' from strain_and_emca_results.csv using finite differences and compares against paper-reported ranges with generous tolerances. For emca_vs_electron_count.csv, it checks that the E_MCA difference between +1% and -1% strain increases when N_e decreases from 1154. For surface_energies.csv, it verifies the relative ordering of facet energies as a function of μ_Ga, confirming that (001) can be stabilized.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strain_and_emca_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Alloy",
          "Strain",
          "E_total",
          "E_MCA"
        ],
        "units": {
          "Strain": "unitless (fraction)",
          "E_total": "eV per supercell",
          "E_MCA": "eV per supercell"
        }
      },
      "description": "Strain-dependent total energies and magnetocrystalline anisotropy energies for pristine and ternary Fe-Ga alloys. The checker recomputes the magnetoelastic coupling coefficient B1 and tetragonal shear modulus C' from these data."
    },
    {
      "file": "emca_vs_electron_count.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N_e",
          "strain_plus1_E_MCA",
          "strain_minus1_E_MCA"
        ],
        "units": {
          "N_e": "integer (count)",
          "strain_plus1_E_MCA": "eV per atom",
          "strain_minus1_E_MCA": "eV per atom"
        }
      },
      "description": "E_MCA as a function of total valence electron count for the pristine Fe79.7Ga20.3 alloy under ±1% tetragonal strain. The checker verifies that the separation between the two curves increases as N_e deviates from the pristine value."
    },
    {
      "file": "surface_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Orientation",
          "Ga_coverage",
          "Adsorbent",
          "mu_Ga",
          "Surface_energy"
        ],
        "units": {
          "mu_Ga": "eV",
          "Surface_energy": "J/m^2"
        }
      },
      "description": "Surface energies for (001), (110), (111) Fe-Ga facets with O, Os, H2S adsorbents and clean, plotted against Ga chemical potential. The checker verifies that (001) becomes more stable than (110) in a Ga-poor condition for active adsorbents, and (111) remains higher."
    }
  ],
  "notes": "The checker recomputes B1 and C' from strain_and_emca_results.csv using finite differences and compares against paper-reported ranges with generous tolerances. For emca_vs_electron_count.csv, it checks that the E_MCA difference between +1% and -1% strain increases when N_e decreases from 1154. For surface_energies.csv, it verifies the relative ordering of facet energies as a function of μ_Ga, confirming that (001) can be stabilized."
}
```

## How you are scored
A hidden verifier will independently score each of the three output files. For `strain_and_emca_results.csv`, it will recompute B1 and C' from the raw strain-dependent total energy and EMCA data, and compare the resulting magnetoelastic parameters against reference values (with tolerances to accommodate differences between DFT implementations). For `emca_vs_electron_count.csv`, it will check that the separation between the EMCA curves at +1% and -1% strain changes in the expected manner as N_e deviates from the pristine value. For `surface_energies.csv`, it will verify the relative ordering of facet energies as a function of μGa, specifically that (001) can become lower than (110) under appropriate adsorbents and that (111) remains higher. The final reward is a weighted combination of these checks; simply reporting numbers consistent with the paper is not sufficient – the raw computed data must be physically plausible and self-consistent. All scoring tolerances and weighting factors are hidden.
