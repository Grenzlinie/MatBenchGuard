# DFT Calculation of Oxygen and Hydroxyl Binding Energies on Pd and B-doped Pd Surfaces

## Problem background
The oxygen reduction reaction (ORR) is kinetically sluggish, and Pd-based catalysts are being explored as alternatives to Pt. However, the strong adsorption of oxygen-containing reaction intermediates (O and OH) on pure Pd limits its catalytic activity. Boron (B) doping of Pd has been proposed as a way to modify the electronic structure and potentially weaken such adsorption. Understanding whether B doping indeed alters the binding energies of O and OH is essential for evaluating its effect on ORR kinetics. This task requires computing the adsorption energies of atomic O and OH on clean Pd(111) and B-doped Pd(111) surfaces using density functional theory (DFT), and also measuring the structural expansion of the Pd lattice upon B doping.

## Approach
Periodic DFT slab calculations are performed with the GGA-PW91 exchange-correlation functional and spin polarization. Model the clean Pd(111) surface as a 4-layer 4×4 slab with a 16 Å vacuum gap. For the B-doped Pd-B(111) surface, insert three B atoms into octahedral interstitial sites distributed in three different layers, corresponding to ~6 at% B. Relax the geometry of the bare slabs to obtain equilibrium structures and interlayer distances. Then place O and OH adsorbates on the relaxed slabs, relax the combined system, and compute the total energies. The binding energy is defined as Eb = E_total − E_slab − E_ad, where E_ad is the energy of the isolated gas-phase O atom or OH radical. On each surface, identify the strongest binding site: fcc for O on Pd(111), hcp for O on Pd-B(111), fcc for OH on Pd(111), and bridge for OH on Pd-B(111). Compare the resulting binding energies and interlayer distances to deduce how B doping affects O and OH adsorption.

## Reproduction target
The goal is to compute and report six quantities: the binding energies (in eV) of O on Pd(111) at the fcc site, O on Pd-B(111) at the hcp site, OH on Pd(111) at the fcc site, and OH on Pd-B(111) at the bridge site; and the interlayer distances (in Å) between the first and second Pd layers in the bare Pd(111) and Pd-B(111) slabs. These values will reveal the magnitude and direction of the changes induced by B doping. The results must be written to a single JSON file with the exact field names and units specified in the workflow step.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials for Pd, B, O, H: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT calculation of O and OH adsorption on Pd(111) and Pd-B(111)
- Role: scored
- Action: Perform periodic DFT calculations using an open-source plane-wave code to compute the binding energies of O and OH on clean Pd(111) and B-doped Pd(111) surfaces, and the interlayer distance change upon B doping.
- Build 4-layer 4×4 slab models with 16 Å vacuum for Pd(111) and Pd-B(111). For Pd-B(111), insert three B atoms into octahedral interstitial sites distributed in three different layers (≈6 at% B).
- Use GGA-PW91 exchange-correlation, spin polarization, and convergence criteria appropriate for the method.
- Relax the top two layers of each bare slab; measure the interlayer distance between the first and second Pd layers.
- Place O and OH on the slabs and relax the surface + adsorbate. Compute binding energies as Eb = E_total − E_slab − E_ad, using the gas-phase atom/molecule as reference for E_ad.
- Report the strongest adsorption site values: fcc for O on Pd(111), hcp for O on Pd-B(111), fcc for OH on Pd(111), and bridge (or the strongest) for OH on Pd-B(111).
- Output all six quantities in a single JSON file.
- Output file: `/app/outputs/binding_energies_and_distances.json`
- Format: json
- Contract: {
  "type": "object",
  "required": [
    "Pd111_O_fcc_binding_energy",
    "PdB111_O_hcp_binding_energy",
    "Pd111_OH_fcc_binding_energy",
    "PdB111_OH_bridge_binding_energy",
    "Pd111_interlayer_distance",
    "PdB111_interlayer_distance"
  ],
  "properties": {
    "Pd111_O_fcc_binding_energy": {"type": "number"},
    "PdB111_O_hcp_binding_energy": {"type": "number"},
    "Pd111_OH_fcc_binding_energy": {"type": "number"},
    "PdB111_OH_bridge_binding_energy": {"type": "number"},
    "Pd111_interlayer_distance": {"type": "number"},
    "PdB111_interlayer_distance": {"type": "number"}
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies_and_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies_and_distances.json
- path: `/app/outputs/binding_energies_and_distances.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed binding energies and structural distances for Pd and Pd-B surfaces, to be compared against hidden reference values from the literature.
- schema:
  - `type`: object
  - `required`: `Pd111_O_fcc_binding_energy`, `PdB111_O_hcp_binding_energy`, `Pd111_OH_fcc_binding_energy`, `PdB111_OH_bridge_binding_energy`, `Pd111_interlayer_distance`, `PdB111_interlayer_distance`
  - `units`:
    - `Pd111_O_fcc_binding_energy`: eV
    - `PdB111_O_hcp_binding_energy`: eV
    - `Pd111_OH_fcc_binding_energy`: eV
    - `PdB111_OH_bridge_binding_energy`: eV
    - `Pd111_interlayer_distance`: Å
    - `PdB111_interlayer_distance`: Å

Notes: The hidden checker compares each numeric field to the paper-reported reference value within a small tolerance. The agent must produce the computed quantities from DFT, not simply look up the reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies_and_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Pd111_O_fcc_binding_energy",
          "PdB111_O_hcp_binding_energy",
          "Pd111_OH_fcc_binding_energy",
          "PdB111_OH_bridge_binding_energy",
          "Pd111_interlayer_distance",
          "PdB111_interlayer_distance"
        ],
        "units": {
          "Pd111_O_fcc_binding_energy": "eV",
          "PdB111_O_hcp_binding_energy": "eV",
          "Pd111_OH_fcc_binding_energy": "eV",
          "PdB111_OH_bridge_binding_energy": "eV",
          "Pd111_interlayer_distance": "Å",
          "PdB111_interlayer_distance": "Å"
        }
      },
      "description": "Computed binding energies and structural distances for Pd and Pd-B surfaces, to be compared against hidden reference values from the literature."
    }
  ],
  "notes": "The hidden checker compares each numeric field to the paper-reported reference value within a small tolerance. The agent must produce the computed quantities from DFT, not simply look up the reported values."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the JSON output. The verifier checks each numeric field against predefined reference values, using tolerances that account for small systematic differences between DFT implementations. It also verifies that the changes upon B doping (e.g., in binding energies and interlayer distances) follow a physically consistent pattern. You must perform the full DFT workflow to produce your values; copying previously published numbers is not sufficient and will not pass the hidden checks.
