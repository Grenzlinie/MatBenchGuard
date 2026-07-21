# NO₂ Adsorption Energies on MXene Configurations via DFT

## Problem background
The development of room-temperature gas sensors based on MXene composites has attracted attention. In particular, 3D crumpled MXene spheres combined with ZnO nanoparticles show enhanced response to NO₂. To understand the origin of this improvement, density functional theory (DFT) calculations are employed to evaluate how strongly NO₂ binds to different chemical environments present in the material: a flat MXene surface, an edge site of MXene, and the interface between MXene and ZnO (a heterojunction). The binding strength is quantified by the adsorption energy, and comparing these energies helps rationalize the enhanced sensing behavior. In this task, you will compute these adsorption energies.

## Approach
You will perform first-principles DFT calculations to compute the adsorption energy of a single NO₂ molecule on three atomic models. Use a generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof (PBE) functional and include van der Waals interactions via the DFT-D3 correction. The calculations should employ a plane-wave basis set with a kinetic-energy cutoff of 400 eV, and sample the Brillouin zone at the Gamma point only. For each model, relax the atomic positions until the residual forces are below 0.05 eV/Å. The adsorption energy for a given model is defined as E_ads = E_system − E_slab − E_NO₂, where E_system is the total energy of the slab with the adsorbed NO₂, E_slab is the total energy of the clean slab, and E_NO₂ is the total energy of an isolated NO₂ molecule relaxed in a large cell. Construct the three models as follows: (1) a periodic slab exposing the (001) surface of Ti₃C₂Tₓ MXene, with oxygen termination mimicking the common surface functionalization; (2) a one-dimensional or ribbon-like model that exposes edge sites of the MXene layer; (3) a heterojunction slab built by placing a ZnO slab with its (100) surface on top of the MXene (001) slab. All structural parameters of the parent materials (MXene hexagonal lattice, wurtzite ZnO) are well known from the literature and should be taken from established sources. The computations can be carried out with any open-source plane-wave DFT code that supports the required functionals and corrections (e.g., Quantum ESPRESSO) and with publicly available pseudopotentials. Report the three resulting adsorption energies in electronvolts.

## Reproduction target
Using density functional theory (DFT), compute the adsorption energy of a single NO₂ molecule on three configurations: (1) a pristine MXene Ti₃C₂Tₓ (001) surface slab, (2) an MXene edge model exposing edge sites, and (3) an MXene/ZnO heterojunction composed of a ZnO (100) slab on MXene (001). Report the three adsorption energies in electronvolts (eV) in the file `/app/outputs/adsorption_energies.json`.

## Assets

- Plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PAW pseudopotentials for Ti, C, O, H, Zn: https://www.quantum-espresso.org/pseudopotentials
- MXene Ti3C2Tx structure parameters
- ZnO wurtzite structure

## Workflow steps

### Step 1: Compute NO₂ adsorption energies on MXene surface, edge, and heterojunction
- Role: scored (load-bearing)
- Action: Perform density functional theory (DFT) calculations to compute the adsorption energy of a single NO₂ molecule on (1) a pristine MXene Ti₃C₂Tₓ (001) surface slab, (2) an MXene edge model exposing edge sites, and (3) an MXene/ZnO heterojunction composed of a ZnO (100) slab on MXene (001) with appropriate terminations. For each system, relax the geometry and compute the adsorption energy as E_ads = E_system - E_slab - E_NO2, where all energies are total energies. Report the three adsorption energies in eV.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"surface": <float in eV>, "edge": <float in eV>, "heterojunction": <float in eV>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Adsorption energies of NO₂ on MXene surface, edge, and MXene/ZnO heterojunction in eV. The checker will compare each energy to reference values with tolerance and will also verify the relative ordering edge < heterojunction < surface (more negative = stronger adsorption).
- schema:
  - `type`: object
  - `required`:
    - `surface`: float in eV
    - `edge`: float in eV
    - `heterojunction`: float in eV

Notes: The three energies are the key quantitative results from the paper's DFT calculations. The agent must construct the required atomic models from publicly known crystal structures and run the DFT simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "surface": "float in eV",
          "edge": "float in eV",
          "heterojunction": "float in eV"
        }
      },
      "description": "Adsorption energies of NO₂ on MXene surface, edge, and MXene/ZnO heterojunction in eV. The checker will compare each energy to reference values with tolerance and will also verify the relative ordering edge < heterojunction < surface (more negative = stronger adsorption)."
    }
  ],
  "notes": "The three energies are the key quantitative results from the paper's DFT calculations. The agent must construct the required atomic models from publicly known crystal structures and run the DFT simulations."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that reads the file `/app/outputs/adsorption_energies.json`. The verifier checks that the JSON contains the three required numeric fields (`surface`, `edge`, `heterojunction`) and that each value is a physically plausible adsorption energy. The verifier then compares your computed energies against reference values and also verifies that the three adsorption energies exhibit a consistent trend that reflects the different chemical nature of the three binding sites. The final reward is a weighted combination of these checks; higher reward is given when the energies agree well with the reference and the site-to-site relationships are physically sound. Note that simply reporting values without performing the DFT calculations is detectable and will result in a low reward. You must execute the computations to produce the scored artifact.
