# DFT Energetics for Methanol Electro-oxidation on Pt₁Cu₂ Supported by Doped Graphene/CNT

## Problem background
Direct methanol fuel cells need efficient anode catalysts that can oxidize methanol while resisting CO poisoning. Platinum‑based catalysts are widely used but are expensive and easily deactivated. Doping carbon supports with heteroatoms such as sulfur and nitrogen is a strategy to alter catalyst‑support interactions and improve dispersion. Density functional theory (DFT) calculations can quantify how co‑doping influences the adsorption of a Pt₁Cu₂ cluster, the thermodynamics of the stepwise methanol electro‑oxidation to CO₂, and the propensity for CO poisoning. This task re‑computes those key energetic quantities for Pt₁Cu₂ on three model graphene supports (pristine, N‑doped, S,N‑doped) and on an S,N‑doped carbon nanotube, providing a theoretical foundation for the experimental observations.

## Approach
The catalyst system is modeled with a Pt₁Cu₂ cluster adsorbed on graphene (Gr), N‑doped graphene (N‑Gr), S,N‑doped graphene (S,N‑Gr), and on an S,N‑doped carbon nanotube. Electronic structure is described by DFT at the B3PW91 level of theory: LANL2DZ for Pt and Cu, and 6‑31G(d) for C, H, O, N, S. Atomic models for all supports, isolated cluster, adsorbed intermediates along the complete methanol oxidation path, and gas‑phase reference molecules (H₂, CH₃OH, CO, etc.) are built. Geometry optimizations and vibrational frequency calculations yield total energies, zero‑point energy corrections, and thermal contributions from which Gibbs free energies are obtained. The adsorption energy of Pt₁Cu₂ on a support is the difference between the total energy of the adsorbed complex and the sum of the energies of the isolated cluster and the bare support. The methanol electro‑oxidation Gibbs free energy profile is constructed using the computational hydrogen electrode (CHE) model, where the free energy of a proton‑electron pair is taken as half the free energy of gaseous H₂. Stepwise oxidation from CH₃OH to CO₂ is evaluated on each graphene support; the overall ΔG and the highest barrier along the path are extracted. The CO adsorption Gibbs free energy sink on each support is also computed.

## Reproduction target
Produce the file reproduced_results.json containing the following quantities in eV:

1. Pt₁Cu₂ adsorption energy on S,N‑doped carbon nanotube and on S,N‑doped graphene.
2. Overall Gibbs free energy change for the complete oxidation of methanol to CO₂ catalyzed by Pt₁Cu₂ supported on pristine graphene (Gr), N‑doped graphene (N‑Gr), and S,N‑doped graphene (S,N‑Gr).
3. The highest Gibbs free energy barrier along the stepwise oxidation pathway on each of the three graphene supports.
4. The Gibbs free energy sink of CO adsorption on Pt₁Cu₂ supported by Gr, N‑Gr, and S,N‑Gr.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Basis Set Exchange: https://www.basissetexchange.org/
- Atomic Simulation Environment: https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: DFT calculations and electronic structure analysis
- Role: process
- Action: Build atomic models for all pristine and doped carbon supports (pristine CNT, N‑CNT, S,N‑CNT, pristine Gr, N‑Gr, S,N‑Gr), the Pt₁Cu₂ cluster, the cluster‑supported complexes, all methanol oxidation intermediates (CH₃OH*, CH₃O*, CH₂O, CHO*, CO*, CO₂*, etc.) on each support, and gas‑phase reference molecules (H₂, CH₃OH, CO, etc.) as described in the paper. Use a quantum chemistry program to perform DFT geometry optimisations and vibrational frequency analyses at the B3PW91 level with LANL2DZ for Pt/Cu and 6‑31G(d) for light atoms. Compute total energies, zero‑point energy corrections, and thermal contributions for every system. From the optimised wavefunction, extract HOMO/LUMO energies and partial atomic charges for the pristine and S,N‑doped supports. Save all raw energies (total, ZPE, thermal corrections) and electronic‑structure data to a structured JSON file.
- Evidence: `/app/outputs/dft_energies.json`

### Step 2: Compute key energetic quantities
- Role: scored (load-bearing)
- Action: From the data in dft_energies.json, compute the following quantities using the thermodynamic cycle defined in the paper: (1) adsorption energy of Pt₁Cu₂ on S,N‑CNT and on S,N‑Gr (Eq. 1); (2) overall Gibbs free energy change for complete methanol oxidation to CO₂ on Pt₁Cu₂ supported by pristine Gr, N‑Gr, and S,N‑Gr using the computational hydrogen electrode model; (3) the highest Gibbs free energy barrier along the stepwise pathway on each support; (4) the Gibbs free energy sink of CO adsorption on Pt₁Cu₂ supported by Gr, N‑Gr, and S,N‑Gr. Write all results as a single JSON object.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: JSON object with keys and numeric values (eV): Pt1Cu2_adsorption_energy_S_N_CNT, Pt1Cu2_adsorption_energy_S_N_Gr, overall_delta_G_S_N_Gr, highest_barrier_S_N_Gr, CO_sink_S_N_Gr, overall_delta_G_Gr, highest_barrier_Gr, CO_sink_Gr, overall_delta_G_N_Gr, highest_barrier_N_Gr, CO_sink_N_Gr.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: DFT‑computed energetic quantities: adsorption energies, overall Gibbs free energy changes, highest energy barriers, and CO adsorption free energy sinks for the three support models.
- schema:
  - `type`: object
  - `required`: `Pt1Cu2_adsorption_energy_S_N_CNT`, `Pt1Cu2_adsorption_energy_S_N_Gr`, `overall_delta_G_S_N_Gr`, `highest_barrier_S_N_Gr`, `CO_sink_S_N_Gr`, `overall_delta_G_Gr`, `highest_barrier_Gr`, `CO_sink_Gr`, `overall_delta_G_N_Gr`, `highest_barrier_N_Gr`, `CO_sink_N_Gr`
  - `properties`:
    - `Pt1Cu2_adsorption_energy_S_N_CNT`:
      - `type`: number
      - `units`: eV
    - `Pt1Cu2_adsorption_energy_S_N_Gr`:
      - `type`: number
      - `units`: eV
    - `overall_delta_G_S_N_Gr`:
      - `type`: number
      - `units`: eV
    - `highest_barrier_S_N_Gr`:
      - `type`: number
      - `units`: eV
    - `CO_sink_S_N_Gr`:
      - `type`: number
      - `units`: eV
    - `overall_delta_G_Gr`:
      - `type`: number
      - `units`: eV
    - `highest_barrier_Gr`:
      - `type`: number
      - `units`: eV
    - `CO_sink_Gr`:
      - `type`: number
      - `units`: eV
    - `overall_delta_G_N_Gr`:
      - `type`: number
      - `units`: eV
    - `highest_barrier_N_Gr`:
      - `type`: number
      - `units`: eV
    - `CO_sink_N_Gr`:
      - `type`: number
      - `units`: eV

Notes: All quantities are in eV. The values are compared to hidden reference values from the paper with direction‑aware tolerances. Better‑than‑paper performance (more negative adsorption/overall ΔG, lower barriers and CO sinks) earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "Pt1Cu2_adsorption_energy_S_N_CNT",
          "Pt1Cu2_adsorption_energy_S_N_Gr",
          "overall_delta_G_S_N_Gr",
          "highest_barrier_S_N_Gr",
          "CO_sink_S_N_Gr",
          "overall_delta_G_Gr",
          "highest_barrier_Gr",
          "CO_sink_Gr",
          "overall_delta_G_N_Gr",
          "highest_barrier_N_Gr",
          "CO_sink_N_Gr"
        ],
        "properties": {
          "Pt1Cu2_adsorption_energy_S_N_CNT": {
            "type": "number",
            "units": "eV"
          },
          "Pt1Cu2_adsorption_energy_S_N_Gr": {
            "type": "number",
            "units": "eV"
          },
          "overall_delta_G_S_N_Gr": {
            "type": "number",
            "units": "eV"
          },
          "highest_barrier_S_N_Gr": {
            "type": "number",
            "units": "eV"
          },
          "CO_sink_S_N_Gr": {
            "type": "number",
            "units": "eV"
          },
          "overall_delta_G_Gr": {
            "type": "number",
            "units": "eV"
          },
          "highest_barrier_Gr": {
            "type": "number",
            "units": "eV"
          },
          "CO_sink_Gr": {
            "type": "number",
            "units": "eV"
          },
          "overall_delta_G_N_Gr": {
            "type": "number",
            "units": "eV"
          },
          "highest_barrier_N_Gr": {
            "type": "number",
            "units": "eV"
          },
          "CO_sink_N_Gr": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "DFT‑computed energetic quantities: adsorption energies, overall Gibbs free energy changes, highest energy barriers, and CO adsorption free energy sinks for the three support models."
    }
  ],
  "notes": "All quantities are in eV. The values are compared to hidden reference values from the paper with direction‑aware tolerances. Better‑than‑paper performance (more negative adsorption/overall ΔG, lower barriers and CO sinks) earns full credit."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/reproduced_results.json and compares each of the 11 energy fields against unseen reference values. Directional metrics (adsorption energy, overall ΔG, highest barrier, CO sink) are scored on a “meet‑or‑beat’’ basis: your value receives full credit when it falls within a tolerance of the reference and does not degrade relative to the expected trend; the reward decreases only when the value is substantially worse. An overall reward between 0 and 1 is computed by combining the per‑field scores. The verifier may also inspect the intermediate raw‑data file dft_energies.json for completeness and self‑consistency. Simply reporting the paper’s numbers without actually running the DFT calculations is not sufficient — the verifier checks that the submitted raw results are plausible and coherent.
