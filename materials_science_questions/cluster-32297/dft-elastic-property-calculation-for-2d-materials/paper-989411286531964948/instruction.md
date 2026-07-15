# DFT Formation Energies and Band Gaps of InSe Polytypes and Heterostructures

## Problem background
Layered van der Waals materials such as indium selenide (InSe) can crystallize in several polytypes (β, γ, ε) that differ in the stacking sequence of quadruple Se-In-In-Se layers. In addition, a centrosymmetric polymorph (S‑type) may appear when the trifold In‑Se bonds within a layer are rotated relative to one another. When InSe thin films are grown by non‑equilibrium techniques, a mixture of these polytypes and polymorphs can form, creating nanoscale domains whose electronic structure may differ from that of a single pure polytype. First‑principles calculations of the formation energies of the various configurations and of the HSE band gaps are therefore essential to understand the energy landscape of polytypism and to assess how the coexistence of different stacking arrangements could lead to electronic disorder in the films.

## Approach
The computational workflow uses density functional theory (DFT) to determine the relative stability and the electronic structure of the InSe systems. First, the crystal structures of the target systems are built from the known in‑plane lattice constant a = 4.01 Å and the stacking sequences described in the literature. Geometry optimizations are performed with the SCAN meta‑GGA functional augmented by the rVV10 van der Waals correction (SCAN+rvv10) to capture the weak interlayer bonds. The total energies obtained from these optimizations are then used to compute formation energies per formula unit, always referenced to the most stable configuration found in each subset of structures (bulk polytypes, monolayers, interfaces). After optimization, the Heyd‑Scuseria‑Ernzerhof hybrid functional (HSE06) with 35% exact exchange is employed to compute the band gaps, which corrects the systematic underestimation of the gap by semi‑local functionals. The procedure is applied to three classes of systems: (i) C‑type and S‑type InSe monolayers, (ii) bulk β‑, γ‑, and ε‑InSe, and (iii) three γ/β heterostructure interfaces with different terminations. All results are written to a single structured JSON file.

## Reproduction target
Compute and report the following quantities in `dft_results.json`:

- Formation energy difference (in meV per formula unit) between C‑type and S‑type InSe monolayers.
- Relative formation energies (in meV/fu) of bulk β‑InSe, γ‑InSe, and ε‑InSe, each expressed relative to the most stable bulk polytype found in your calculations.
- Relative formation energies (in meV/fu) of three γ/β heterostructure interfaces (γ_A/β_B, γ_A/β_C, γ_C/β_C), each expressed relative to the most stable interface among them.
- HSE06 band gaps (in eV) for the same set of systems: C‑type monolayer, S‑type monolayer, bulk β, bulk γ, bulk ε, and the three γ/β interfaces.

All formation energies must be referenced to the most stable configuration within each subset, and band gaps are obtained with the HSE06 functional containing 35% exact exchange.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency set, v1.3): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT calculation of formation energies and HSE band gaps
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO, build crystal structures for C-type (P-6m2) and S-type (P-3m) InSe monolayers (in-plane a=4.01 Å, vacuum ≥15 Å), bulk β-InSe (P6₃/mmc, c=16.64 Å), γ-InSe (R3m, c=24.95 Å), ε-InSe (P-6m2, c=16.70 Å), and three γ/β interfaces (γ_A/β_B, γ_A/β_C, γ_C/β_C) with appropriate supercells. Perform geometry optimization using the SCAN+rvv10 functional, then compute HSE06 band gaps with 35% exact exchange. Convert all total energies to formation energies per formula unit relative to the most stable configuration determined from your calculations. Write all results to dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {
  "c_s_type_formation_energy_diff_meV_fu": "float (energy difference C - S per formula unit)",
  "bulk_beta_energy_relative_meV_fu": "float (relative formation energy, meV/fu)",
  "bulk_gamma_energy_relative_meV_fu": "float",
  "bulk_epsilon_energy_relative_meV_fu": "float",
  "interface_gamma_A_beta_B_energy_relative_meV_fu": "float",
  "interface_gamma_A_beta_C_energy_relative_meV_fu": "float",
  "interface_gamma_C_beta_C_energy_relative_meV_fu": "float",
  "c_type_monolayer_bandgap_eV": "float (eV)",
  "s_type_monolayer_bandgap_eV": "float",
  "bulk_beta_bandgap_eV": "float",
  "bulk_gamma_bandgap_eV": "float",
  "bulk_epsilon_bandgap_eV": "float",
  "interface_gamma_A_beta_B_bandgap_eV": "float",
  "interface_gamma_A_beta_C_bandgap_eV": "float",
  "interface_gamma_C_beta_C_bandgap_eV": "float"
}
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
- description: DFT results: formation energies and HSE band gaps for monolayers, bulk polytypes, and γ/β heterostructure interfaces.
- schema:
  - `type`: object
  - `required`: `c_s_type_formation_energy_diff_meV_fu`, `bulk_beta_energy_relative_meV_fu`, `bulk_gamma_energy_relative_meV_fu`, `bulk_epsilon_energy_relative_meV_fu`, `interface_gamma_A_beta_B_energy_relative_meV_fu`, `interface_gamma_A_beta_C_energy_relative_meV_fu`, `interface_gamma_C_beta_C_energy_relative_meV_fu`, `c_type_monolayer_bandgap_eV`, `s_type_monolayer_bandgap_eV`, `bulk_beta_bandgap_eV`, `bulk_gamma_bandgap_eV`, `bulk_epsilon_bandgap_eV`, `interface_gamma_A_beta_B_bandgap_eV`, `interface_gamma_A_beta_C_bandgap_eV`, `interface_gamma_C_beta_C_bandgap_eV`
  - `units`:
    - `all formation energies`: meV per formula unit
    - `all band gaps`: eV

Notes: All energy values must be computed relative to the most stable configuration within each subset (bulk polytypes, interfaces) as determined by the agent's own calculations. The checker will verify numerical values against hidden gold values and also check the relative ordering of formation energies (β < ε < γ) and band gaps (β > ε ≈ γ).

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
          "c_s_type_formation_energy_diff_meV_fu",
          "bulk_beta_energy_relative_meV_fu",
          "bulk_gamma_energy_relative_meV_fu",
          "bulk_epsilon_energy_relative_meV_fu",
          "interface_gamma_A_beta_B_energy_relative_meV_fu",
          "interface_gamma_A_beta_C_energy_relative_meV_fu",
          "interface_gamma_C_beta_C_energy_relative_meV_fu",
          "c_type_monolayer_bandgap_eV",
          "s_type_monolayer_bandgap_eV",
          "bulk_beta_bandgap_eV",
          "bulk_gamma_bandgap_eV",
          "bulk_epsilon_bandgap_eV",
          "interface_gamma_A_beta_B_bandgap_eV",
          "interface_gamma_A_beta_C_bandgap_eV",
          "interface_gamma_C_beta_C_bandgap_eV"
        ],
        "units": {
          "all formation energies": "meV per formula unit",
          "all band gaps": "eV"
        }
      },
      "description": "DFT results: formation energies and HSE band gaps for monolayers, bulk polytypes, and γ/β heterostructure interfaces."
    }
  ],
  "notes": "All energy values must be computed relative to the most stable configuration within each subset (bulk polytypes, interfaces) as determined by the agent's own calculations. The checker will verify numerical values against hidden gold values and also check the relative ordering of formation energies (β < ε < γ) and band gaps (β > ε ≈ γ)."
}
```

## How you are scored
A hidden verifier reads your `dft_results.json` and compares every numerical field to a set of reference values extracted from the original study. The comparison uses absolute tolerances appropriate for DFT re‑runs with different software and pseudopotentials. In addition, the verifier checks that the relative ordering of the formation energies among the bulk polytypes and of the band gaps among those polytypes is physically correct. Each field carries a weight, and the final score is a weighted sum of the checks that pass; the combined reward is normalized to a value between 0.0 and 1.0. You do not need to reproduce the reference values exactly, but your results must fall within the expected range for a proper execution of the described protocol.
