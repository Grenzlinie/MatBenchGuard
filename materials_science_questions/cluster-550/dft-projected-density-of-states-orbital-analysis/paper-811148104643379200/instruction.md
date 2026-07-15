# DFT Optical and Transport Properties of Niobium Oxide Photoelectrodes

## Problem background
Nb3O7(OH) and monoclinic H‑Nb2O5 are candidate materials for photoelectrodes in dye‑sensitized solar cells and photocatalysis. Their performance in such devices is governed by electronic structure, optical response, and charge transport properties. First‑principles calculations based on density functional theory can predict these quantities and provide insight into the intrinsic differences between the two phases. In this task you will compute, from the provided relaxed crystal structures, the key optical and thermoelectric transport properties of both compounds. The computed values allow a direct comparison of the materials’ optical anisotropy and electrical conductivity without relying on experimental measurements.

## Approach
You will perform density functional theory (DFT) calculations using the Tran–Blaha modified Becke–Johnson (TB‑mBJ) exchange‑correlation potential, which yields accurate band gaps for many semiconductors. Starting from the relaxed crystal structures (CIF files), you will carry out a self‑consistent field (SCF) calculation to obtain the Kohn–Sham eigenvalues and wavefunctions. From the electronic structure you will compute the complex dielectric function tensor for two independent polarization directions (perpendicular and parallel to the crystallographic c‑axis) using linear optical response theory and the Kramers‑Kronig relations. The imaginary part of the dielectric function gives the optical conductivity, from which you will extract the optical band gap (absorption threshold), the static dielectric constant, and the two highest conductivity peaks in the 2–12 eV range. Finally, you will use the electronic band structure in the Boltzmann transport module BoltzTraP to evaluate the average thermoelectric conductivity σ^ave of the n‑type (electron) and p‑type (hole) regions at 300 K under the constant relaxation time approximation. The workflow is applied to both Nb3O7(OH) and H‑Nb2O5, enabling a quantitative comparison of their optoelectronic and transport characteristics.

## Reproduction target
For both Nb3O7(OH) and monoclinic H‑Nb2O5, using the supplied relaxed crystal structures, compute and report:
- The optical band gap (onset energy of the imaginary dielectric function), the static dielectric constant ε1(0), and the energy and magnitude of the two highest optical conductivity peaks in the 2–12 eV range, separately for perpendicular and parallel polarizations. Write these results to optical_properties.csv.
- The average thermoelectric conductivity σ^ave for n‑type and p‑type carriers at 300 K, written to transport_properties.csv.

These two CSV files constitute the scored output; their exact schemas are detailed in the output contract below.

## Assets

- Relaxed crystal structure of Nb3O7(OH) (CIF file): https://pubs.acs.org/doi/suppl/10.1021/acs.jpcc.6b06391
- Relaxed crystal structure of monoclinic H-Nb2O5 (CIF file): https://pubs.acs.org/doi/suppl/10.1021/acs.jpcc.6b06391
- DFT code with TB-mBJ exchange-correlation functional
- BoltzTraP code: https://www.imc.tuwien.ac.at/forschungsbereich_theoretische_chemie/forschungsgruppe_prof_dr_gkh_madsen/boltztrp/

## Workflow steps

### Step 1: DFT electronic structure with TB-mBJ
- Role: process
- Action: Using the relaxed crystal structures of Nb3O7(OH) and H-Nb2O5 from CIF files, perform self-consistent field (SCF) calculations with the TB-mBJ exchange-correlation functional to obtain Kohn-Sham eigenvalues and eigenstates. Ensure convergence sufficient for subsequent optical and transport calculations.
- Evidence: `/app/outputs/scf_metadata.log`

### Step 2: Optical properties (dielectric function, conductivity)
- Role: scored (load-bearing)
- Action: From the TB-mBJ electronic structure, compute the complex dielectric tensor components for both perpendicular (⊥) and parallel (∥) polarizations for Nb3O7(OH) and H-Nb2O5. Obtain the real part ε1(ω) and imaginary part ε2(ω) via linear response and Kramers-Kronig relations. Derive the optical conductivity σ(ω) = (ω/2π)·ε2(ω). Extract the optical band gap (onset of ε2), the static dielectric constant ε1(0), and the two highest σ(ω) peaks in the 2–12 eV energy range, recording the peak energy (eV) and magnitude (s⁻¹). Write the results to optical_properties.csv.
- Output file: `/app/outputs/optical_properties.csv`
- Format: csv
- Contract: material (string), polarization (string, one of 'perpendicular' or 'parallel'), optical_band_gap_eV (float), epsilon1_static (float), sigma_peak1_eV (float), sigma_peak1_s1 (float), sigma_peak2_eV (float), sigma_peak2_s1 (float)
- Scoring: scored by hidden verifier

### Step 3: Thermoelectric conductivity
- Role: scored
- Action: Using the electronic band structure from the TB-mBJ calculation, compute the thermoelectric conductivity under the constant relaxation time approximation at 300 K with the BoltzTraP code. Extract the average transported conductivity σ^ave for the n-type (electrons) and p-type (holes) regions. Write the results to transport_properties.csv.
- Output file: `/app/outputs/transport_properties.csv`
- Format: csv
- Contract: material (string), sigma_ave_n_type (float, units (Ω m s)⁻¹), sigma_ave_p_type (float, units (Ω m s)⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_properties.csv`
- `/app/outputs/transport_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_properties.csv
- path: `/app/outputs/optical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optical band gap, static dielectric constant, and the two highest optical conductivity peaks (energy and magnitude) for each material and polarization.
- schema:
  - `type`: table
  - `required_columns`: `material`, `polarization`, `optical_band_gap_eV`, `epsilon1_static`, `sigma_peak1_eV`, `sigma_peak1_s1`, `sigma_peak2_eV`, `sigma_peak2_s1`
  - `units`:
    - `optical_band_gap_eV`: eV
    - `epsilon1_static`: dimensionless
    - `sigma_peak1_eV`: eV
    - `sigma_peak1_s1`: s^{-1}
    - `sigma_peak2_eV`: eV
    - `sigma_peak2_s1`: s^{-1}

### transport_properties.csv
- path: `/app/outputs/transport_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermoelectric conductivity σ^ave for n-type and p-type carriers at 300 K for each material.
- schema:
  - `type`: table
  - `required_columns`: `material`, `sigma_ave_n_type`, `sigma_ave_p_type`
  - `units`:
    - `sigma_ave_n_type`: (Ω m s)^{-1}
    - `sigma_ave_p_type`: (Ω m s)^{-1}

Notes: The checker compares the reported values to hidden paper gold values with appropriate tolerances. No tolerances or gold values are included in this public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "polarization",
          "optical_band_gap_eV",
          "epsilon1_static",
          "sigma_peak1_eV",
          "sigma_peak1_s1",
          "sigma_peak2_eV",
          "sigma_peak2_s1"
        ],
        "units": {
          "optical_band_gap_eV": "eV",
          "epsilon1_static": "dimensionless",
          "sigma_peak1_eV": "eV",
          "sigma_peak1_s1": "s^{-1}",
          "sigma_peak2_eV": "eV",
          "sigma_peak2_s1": "s^{-1}"
        }
      },
      "description": "Optical band gap, static dielectric constant, and the two highest optical conductivity peaks (energy and magnitude) for each material and polarization."
    },
    {
      "file": "transport_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "sigma_ave_n_type",
          "sigma_ave_p_type"
        ],
        "units": {
          "sigma_ave_n_type": "(Ω m s)^{-1}",
          "sigma_ave_p_type": "(Ω m s)^{-1}"
        }
      },
      "description": "Thermoelectric conductivity σ^ave for n-type and p-type carriers at 300 K for each material."
    }
  ],
  "notes": "The checker compares the reported values to hidden paper gold values with appropriate tolerances. No tolerances or gold values are included in this public contract."
}
```

## How you are scored
This task is scored by a hidden verifier. After you submit the output files under /app/outputs, the verifier reads optical_properties.csv and transport_properties.csv and compares the values you report against hidden reference data. The comparison uses numerical tolerances that account for legitimate differences between DFT implementations and for statistical spread. Both the absolute values and the relative trends between the two materials (e.g., differences in optical anisotropy and relative magnitude of the thermoelectric conductivity) contribute to the score. The final reward is a weighted combination of the optical and transport components; reporting values that are plausible but do not match the reference within the allowed tolerances will reduce the score.
