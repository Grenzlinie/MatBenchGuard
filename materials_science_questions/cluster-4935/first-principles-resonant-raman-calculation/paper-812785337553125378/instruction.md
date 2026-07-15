# First-Principles Resonant Raman Scattering Calculation for GaP

## Problem background
Resonant Raman scattering in semiconductors provides a sensitive probe of electron-phonon interactions. In GaP, the first-order allowed TO(Γ) phonon and the second-order Raman spectrum show pronounced resonances when the incident photon energy approaches the direct E₀ and E₀+Δ₀ gaps. The second-order spectrum decomposes into irreducible components: Γ₁ overtones (e.g. two-LO(Γ)) and Γ₁₅ combinations (e.g. TO+LO(Γ)) exhibit sharply enhanced peaks near resonance. The quasistatic theory relates the Raman cross-section curves to electronic energy denominators and to electron-two-phonon deformation potentials D₁ and D₁₅, which can be extracted from the integrated intensities of the two-phonon peaks relative to the first-order TO(Γ) peak. Accurately computing these deformation potentials from first principles is the central challenge of this task.

## Approach
The reproduction proceeds via a first-principles computational pipeline. First, a density functional theory (DFT) self-consistent calculation provides the Kohn-Sham band structure for GaP. Next, density functional perturbation theory (DFPT) at the Γ point yields phonon frequencies and eigenvectors for the optical modes. The electron-phonon coupling is then computed with the EPW code, which performs Wannier interpolation onto a fine k/q mesh and evaluates the Raman tensor components within the quasistatic approximation, using the experimental gap parameters E₀ = 2.78 eV and spin-orbit splitting Δ₀ = 0.082 eV. From the Raman tensor, resonant cross-section curves are generated for the first-order TO(Γ) mode and for the second-order Γ₁ and Γ₁₅ components over a photon energy range spanning the E₀ resonance. Finally, the integrated intensities of the two-LO(Γ) (≈806 cm⁻¹) and TO+LO(Γ) (≈768.5 cm⁻¹) peaks are determined relative to the TO(Γ) peak, and the electron-two-phonon deformation potentials D₁ and D₁₅ are deduced using standard relations that follow from the quasistatic theory.

## Reproduction target
Two scored artifacts must be produced.
- A CSV file (`raman_cross_sections.csv`) containing the computed resonant Raman cross-section curves as functions of incident photon energy relative to E₀. The file must include columns for photon_energy_relative_E0, cross_section_first_order, cross_section_second_order_Gamma1, and cross_section_second_order_Gamma15, with at least 20 data points covering the energy range from −0.4 eV to +0.3 eV. The curves should capture the characteristic resonant features at E₀ and E₀+Δ₀.
- A JSON file (`results.json`) that reports the integrated intensity ratios of the two-LO(Γ) and TO+LO(Γ) peaks relative to the TO(Γ) peak, the corresponding ratios of the second-order to first-order energy shifts (δ₂(ω₀)/δ₁(ω₀)), and the electron-two-phonon deformation potentials D₁ and D₁₅ (in eV). All quantities are computed from the first-principles Raman tensor and the quasistatic formulas.

## Assets

- GaP zinc-blende crystal structure (lattice constant 5.45 Å, space group F-43m)
- SSSP efficiency library (PBE pseudopotentials for Ga and P): https://materialscloud.org/home/sssp
- Quantum ESPRESSO (pw.x, ph.x, epw.x): https://www.quantum-espresso.org
- EPW (Electron-Phonon Wannier) code: https://epw-code.org
- GaP absorption data from Dean et al. (1967) and Subashiev et al. (1966): 10.1063/1.1709519

## Workflow steps

### Step 1: DFT self-consistent field calculation for GaP
- Role: process
- Action: Run a DFT SCF calculation for the GaP primitive cell using Quantum ESPRESSO pw.x to obtain the Kohn-Sham eigenvalues and wavefunctions on a dense k-point grid, including the Γ point. Use the PBE functional and SSSP pseudopotentials.
- Evidence: `/app/outputs/scf.log`

### Step 2: DFPT phonon calculation at Γ
- Role: process
- Action: Run ph.x to compute the dynamical matrix at the Γ point, obtaining phonon frequencies and eigenvectors for the optical modes (TO and LO).
- Evidence: `/app/outputs/ph.out`

### Step 3: EPW Wannier interpolation and electron-phonon coupling
- Role: process
- Action: Run epw.x to perform Wannier interpolation of the electronic bands and phonon dispersions, compute the electron-phonon matrix elements on a fine k/q mesh, and evaluate the Raman tensor components using the quasistatic approximation and experimental gap parameters E0=2.78 eV, Δ0=0.082 eV.
- Evidence: `/app/outputs/epw.out`

### Step 4: Generate resonant Raman cross-section curves
- Role: scored
- Action: From the Raman tensor data produced by EPW, construct the cross-section curves for first-order TO(Γ) and second-order Γ1 and Γ15 components (in arbitrary units) and write them to a CSV file with at least 20 points spanning the energy range.
- Output file: `/app/outputs/raman_cross_sections.csv`
- Format: csv
- Contract: Header: photon_energy_relative_E0, cross_section_first_order, cross_section_second_order_Gamma1, cross_section_second_order_Gamma15. Numeric columns; rows for ≥20 distinct photon energies between -0.4 and +0.3 eV.
- Scoring: scored by hidden verifier

### Step 5: Compute deformation potentials D1 and D15
- Role: scored (load-bearing)
- Action: >-
  Identify the two-LO(Γ) (≈806 cm⁻¹) and TO+LO(Γ) (≈768.5 cm⁻¹) peaks in the
  cross-section curves (Step 4). For each peak, integrate the area under the
  second-order curve over the peak region to obtain the integrated intensity
  I₂. Integrate the first-order TO(Γ) curve over the same photon-energy
  interval at the corresponding resonance energy to obtain I₁. Compute the
  ratios r_2LO = I₂(two‑LO) / I₁ and r_TOLO = I₂(TO+LO) / I₁. Use the
  quasistatic relations below to derive the deformation potentials D₁ and D₁₅.

  **Formulas and required constants**
  - Phonon frequencies: TO(Γ) = 365.5 cm⁻¹, LO(Γ) = 403 cm⁻¹.
  - Atomic masses: M_Ga = 69.723 u, M_P = 30.974 u. For an optical mode use
    the reduced mass M_opt = (M_Ga·M_P)/(M_Ga + M_P) ≈ 21.27 u.
  - Lattice constant a₀ = 5.45 Å.
  - N is the number of unit cells participating; it cancels in the following.
  - ⟨ξ²⟩ for a phonon mode of frequency Ω, reduced mass M, at temperature
    T = 300 K: ⟨ξ²⟩ = ℏ/(2 M Ω) · ½ · coth(ℏ Ω/(2 k_B T)), where the factor ½
    accounts for the squared polarization vector (|e|²=½ for optical modes in
    zinc‑blende).
  - Degeneracy factors: η = 1 for two-LO (Γ₁ mode), η = 2 for TO‑LO (Γ₁₅
    mode).

  **For D₁ (Γ₁ mode, two-LO peak)**
  The ratio a⁽²⁾/d⁽¹⁾ is approximately r_2LO after correcting for a possible
  background. Taking a⁽²⁾/d⁽¹⁾ = r_2LO, the ratio of energy shifts is
  δ₁⁽²⁾ ω₀ / δ⁽¹⁾ ω₀ = (1/4) √[ r_2LO · ⟨ξ_TO,Γ²⟩ / (⟨ξ_LO²⟩² N (η/2)) ].
  The first‑order deformation potential is δ⁽¹⁾ ω₀ = (2/a₀) d₀, where
  d₀ = 33 eV is the optical deformation potential for GaP.
  The second‑order shift is δ₁⁽²⁾ ω₀ = (4/3 a₀²) D₁.
  Hence D₁ = (3 a₀ d₀ / 2) · (δ₁⁽²⁾ ω₀ / δ⁽¹⁾ ω₀).

  **For D₁₅ (Γ₁₅ mode, TO+LO peak)**
  δ₁₅⁽²⁾ ω₀ / δ⁽¹⁾ ω₀ = √[ r_TOLO · ⟨ξ_TO,Γ²⟩ / (⟨ξ_TO²⟩ ⟨ξ_LO²⟩ N (η/2)) ].
  The relation for D₁₅ is δ₁₅⁽²⁾ ω₀ = (4/a₀²) D₁₅, giving
  D₁₅ = (a₀ d₀ / 2) · (δ₁₅⁽²⁾ ω₀ / δ⁽¹⁾ ω₀).

  Using the ⟨ξ²⟩ formulas above with the tabulated constants, compute the
  intermediate ratios δ₂ω₀/δ₁ω₀ for Γ₁ and Γ₁₅, then compute D₁ and D₁₅
  (in eV). Finally, write a JSON file with the six keys listed in the Contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Keys: intensity_ratio_two_LO (number), intensity_ratio_TO_plus_LO (number), delta2_omega0_over_delta1_omega0_Gamma1 (number), delta2_omega0_over_delta1_omega0_Gamma15 (number), D1_eV (number), D15_eV (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raman_cross_sections.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raman_cross_sections.csv
- path: `/app/outputs/raman_cross_sections.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with resonant Raman cross-section curves as functions of photon energy relative to E0. The structure (peak positions, relative shape) is audited.
- schema:
  - `type`: table
  - `required_columns`: `photon_energy_relative_E0`, `cross_section_first_order`, `cross_section_second_order_Gamma1`, `cross_section_second_order_Gamma15`
  - `units`:
    - `photon_energy_relative_E0`: eV
    - `cross_section_first_order`: arbitrary units
    - `cross_section_second_order_Gamma1`: arbitrary units
    - `cross_section_second_order_Gamma15`: arbitrary units

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON containing computed intensity ratios and electron-two-phonon deformation potentials D1 and D15. Values are compared to the paper’s reported values within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `intensity_ratio_two_LO`: number (ratio to first-order)
    - `intensity_ratio_TO_plus_LO`: number
    - `delta2_omega0_over_delta1_omega0_Gamma1`: number
    - `delta2_omega0_over_delta1_omega0_Gamma15`: number
    - `D1_eV`: number
    - `D15_eV`: number
  - `units`:
    - `D1_eV`: eV
    - `D15_eV`: eV

Notes: The deformation potentials are compared to the paper’s published D1 and D15 with a ±30% tolerance. The cross-section curves are checked for peak positions within 0.02 eV of E0 (2.78 eV) and E0+Δ0 (2.862 eV), and for sharp features at the expected two-phonon energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raman_cross_sections.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "photon_energy_relative_E0",
          "cross_section_first_order",
          "cross_section_second_order_Gamma1",
          "cross_section_second_order_Gamma15"
        ],
        "units": {
          "photon_energy_relative_E0": "eV",
          "cross_section_first_order": "arbitrary units",
          "cross_section_second_order_Gamma1": "arbitrary units",
          "cross_section_second_order_Gamma15": "arbitrary units"
        }
      },
      "description": "CSV file with resonant Raman cross-section curves as functions of photon energy relative to E0. The structure (peak positions, relative shape) is audited."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "intensity_ratio_two_LO": "number (ratio to first-order)",
          "intensity_ratio_TO_plus_LO": "number",
          "delta2_omega0_over_delta1_omega0_Gamma1": "number",
          "delta2_omega0_over_delta1_omega0_Gamma15": "number",
          "D1_eV": "number",
          "D15_eV": "number"
        },
        "units": {
          "D1_eV": "eV",
          "D15_eV": "eV"
        }
      },
      "description": "JSON containing computed intensity ratios and electron-two-phonon deformation potentials D1 and D15. Values are compared to the paper’s reported values within a tolerance."
    }
  ],
  "notes": "The deformation potentials are compared to the paper’s published D1 and D15 with a ±30% tolerance. The cross-section curves are checked for peak positions within 0.02 eV of E0 (2.78 eV) and E0+Δ0 (2.862 eV), and for sharp features at the expected two-phonon energies."
}
```

## How you are scored
A hidden verifier scores your two outputs automatically.
- The cross-section curves are audited for structural correctness: the first-order curve must have a local maximum near E₀ and a feature near E₀+Δ₀; the second-order Γ₁ curve must show two peaks, and the Γ₁₅ curve one peak, at the expected energies.
- The deformation potentials D₁ and D₁₅ in `results.json` are compared to reference values that correspond to the results of the original experimental analysis; they are accepted if they lie within a tolerance that accounts for differences in the computational setup.
- The total reward is a weighted combination of the structural checks (lower weight) and the accuracy of D₁ and D₁₅ (higher weight). Reporting only the paper's numbers without performing the first-principles computation will not pass, because the checker verifies the consistency of the cross-section curves and the derived intensity ratios.
