# First-principles surface relaxation of PbTiO₃ (111)-Ti termination

## Problem background
PbTiO₃ is a ferroelectric perovskite with a high Curie temperature and large spontaneous polarization, widely used in thin‑film devices. A detailed understanding of its surfaces is critical because surface relaxations and reconstructions directly influence properties such as catalytic activity, epitaxial growth, and ferroelectric stability. While the (001) surfaces of PbTiO₃ have been well studied, the polar (111) orientation presents a more complex situation: its stacking sequence consists of alternating positively charged Ti⁴⁺ layers and negatively charged PbO₃⁴⁻ layers, creating an internal electric field that must be compensated by structural relaxations or compositional changes. This task investigates the stoichiometric Ti‑terminated (1×1) (111) surface of cubic PbTiO₃. The main goal is to determine from first principles how the surface and near‑surface layers relax relative to the bulk, and to quantify key geometric changes—atomic displacements, interlayer spacing modifications, bond length alterations, and rumpling of the subsurface PbO₃ layer—that characterize the electrostatically driven surface relaxation.

## Approach
The approach follows a standard first‑principles surface‑science workflow. A symmetric slab model is constructed from the cubic perovskite structure, cleaved along the [111] direction to expose Ti terminations on both sides. The slab contains 13 atomic layers, with the central layer fixed to represent the bulk‑like interior, and a 12 Å vacuum gap separates periodic images along the surface normal. The in‑plane lattice constant is set to the theoretically optimized value of 3.968 Å. Ionic relaxation is performed using density‑functional theory within the generalized‑gradient approximation (GGA‑PBE) and the projector‑augmented wave (PAW) method. While the original study used the VASP code, the same physics is captured with the open‑source Quantum ESPRESSO package, which provides GGA‑PBE PAW pseudopotentials. All atomic positions except those in the central layer are relaxed until the forces on each atom fall below a threshold. From the final relaxed coordinates, the geometry is analyzed to extract displacements of ions along the surface normal, changes in distances between consecutive layer centroids (interlayer relaxations), variations of Ti–O bond lengths relative to the bulk reference, and the rumpling (difference between cation and anion displacements) of the second PbO₃ layer. These metrics provide a complete picture of the surface relaxation phenomenon.

## Reproduction target
Produce the following quantitative structural metrics for the (111)‑Ti termination and write them into a single JSON file:
- surface_Ti_displacement: the displacement of the outermost Ti atom along the surface normal (negative if inward).
- interlayer_relaxation_d12: percentage change of the distance between the first Ti layer and the second PbO₃ layer centroid relative to the bulk interlayer spacing.
- interlayer_relaxation_d23: percentage change between the second PbO₃ layer centroid and the third Ti layer relative to the bulk interlayer spacing.
- outermost_Ti-O_bond_contraction: percentage change of the Ti–O bond length between the surface Ti and the O atom in the second layer relative to the bulk bond length of 1.984 Å (negative for contraction).
- subsurface_Ti-O_bond_expansion: percentage change of the Ti–O bond length between the second‑layer O and the third‑layer Ti relative to the bulk bond length (positive for expansion).
- rumpling_second_PbO3_layer: the absolute magnitude of the rumpling between Pb and O atoms within the second PbO₃ layer.
- layer_displacements: an array of objects describing the displacement of each atom type (Ti, Pb, O) in each layer. Each object has keys: layer (integer, counting from the surface inward), atom_type (one of "Ti", "Pb", "O"), and displacement (float, in Å, negative inward).
All values must follow the sign conventions stated above.

## Assets

- Quantum ESPRESSO (pw.x, relax routines): https://www.quantum-espresso.org/
- GGA-PBE PAW pseudopotentials for Pb, Ti, O: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Construct the (111)-Ti slab model
- Role: process
- Action: Build a symmetric 13-layer slab of cubic PbTiO₃ (111) terminated by a Ti layer, with a 12 Å vacuum gap, using the in-plane lattice constant a=3.968 Å. The central layer is treated as bulk-like and fixed. Output the atomic coordinates in a format suitable for Quantum ESPRESSO input.
- Evidence: `/app/outputs/slab_structure.pwi`

### Step 2: Perform DFT ionic relaxation of the slab
- Role: process
- Action: Using Quantum ESPRESSO (pw.x) with GGA-PBE PAW pseudopotentials for Pb, Ti, O, perform full ionic relaxation of the slab. Use a plane-wave energy cutoff of at least 400 eV, a 11×11×1 Monkhorst–Pack k-point grid, and a force convergence threshold of 0.02 eV/Å or better. All atoms except the central layer may move. Save the final relaxed atomic coordinates.
- Evidence: `/app/outputs/relaxed_coordinates.xyz`

### Step 3: Compute structural relaxation metrics
- Role: scored (load-bearing)
- Action: From the relaxed atomic positions obtained in the previous step, compute the following quantities for the (111)-Ti termination: (i) atomic displacements along the surface normal for Ti, Pb, and O atoms in each layer (negative = inward); (ii) interlayer relaxation percentages Δd₁₂ and Δd₂₃ defined as the percent change of the distance between consecutive layer centroids relative to the bulk interlayer spacing; (iii) percentage change of the outermost Ti–O bond length and of the subsurface Ti–O bond length relative to the bulk Ti–O bond length (1.984 Å); (iv) rumpling amplitude of the second PbO₃ layer (absolute value). Report all numbers in a single JSON file.
- Output file: `/app/outputs/relaxation_metrics.json`
- Format: json
- Contract: {
  "surface_Ti_displacement": <float>,
  "interlayer_relaxation_d12": <float>,
  "interlayer_relaxation_d23": <float>,
  "outermost_Ti-O_bond_contraction": <float>,
  "subsurface_Ti-O_bond_expansion": <float>,
  "rumpling_second_PbO3_layer": <float>,
  "layer_displacements": [
    { "layer": <int>, "atom_type": "Ti"|"Pb"|"O", "displacement": <float> },
    ...
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxation_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxation_metrics.json
- path: `/app/outputs/relaxation_metrics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural relaxation metrics computed for the (111)-Ti termination from the DFT ionic relaxation. The checker compares each value to the published reference values (paper's Table 1) with tolerances appropriate for the method and code.
- schema:
  - `type`: object
  - `required`:
    - `surface_Ti_displacement`: float (Å, negative indicates inward)
    - `interlayer_relaxation_d12`: float (percent, contraction negative)
    - `interlayer_relaxation_d23`: float (percent, expansion positive)
    - `outermost_Ti-O_bond_contraction`: float (percent, contraction negative)
    - `subsurface_Ti-O_bond_expansion`: float (percent, expansion positive)
    - `rumpling_second_PbO3_layer`: float (Å)
    - `layer_displacements`: array of objects with keys 'layer' (int), 'atom_type' (string), 'displacement' (float, Å)
  - `additionalProperties`: False

Notes: The checker will compare each reported metric against the paper's reported values for the (111)-Ti termination. Tolerances account for differences between DFT codes and pseudopotentials. The agent's JSON file must follow exactly the schema above; additional fields are ignored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxation_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "surface_Ti_displacement": "float (Å, negative indicates inward)",
          "interlayer_relaxation_d12": "float (percent, contraction negative)",
          "interlayer_relaxation_d23": "float (percent, expansion positive)",
          "outermost_Ti-O_bond_contraction": "float (percent, contraction negative)",
          "subsurface_Ti-O_bond_expansion": "float (percent, expansion positive)",
          "rumpling_second_PbO3_layer": "float (Å)",
          "layer_displacements": "array of objects with keys 'layer' (int), 'atom_type' (string), 'displacement' (float, Å)"
        },
        "additionalProperties": false
      },
      "description": "Structural relaxation metrics computed for the (111)-Ti termination from the DFT ionic relaxation. The checker compares each value to the published reference values (paper's Table 1) with tolerances appropriate for the method and code."
    }
  ],
  "notes": "The checker will compare each reported metric against the paper's reported values for the (111)-Ti termination. Tolerances account for differences between DFT codes and pseudopotentials. The agent's JSON file must follow exactly the schema above; additional fields are ignored."
}
```

## How you are scored
A hidden verifier examines your submitted `/app/outputs/relaxation_metrics.json`. It first validates that the file exists and conforms to the required JSON schema. Then it compares each of the six top‑level numeric fields (surface Ti displacement, Δd₁₂, Δd₂₃, outermost Ti–O bond contraction, subsurface Ti–O bond expansion, rumpling) against reference values obtained from the published computational study under the same conditions. The comparison uses tolerances that account for the expected differences arising from the use of a different DFT code and slightly different pseudopotentials, while being strict enough to distinguish a properly executed relaxation from a random or default guess. The verifier also checks that the reported signs and relative magnitudes (e.g., a strong contraction of Δd₁₂ versus a milder expansion of Δd₂₃, an inward displacement of surface Ti) are physically consistent with an electrostatically driven surface relaxation. The layer‑displacements array is inspected for completeness and consistency with the top‑level numbers, contributing a small additional weight. The overall reward is a weighted sum of these individual checks, with the main relaxation metrics carrying the dominant weight. Reporting merely the paper’s published numbers without performing the DFT calculation is unlikely to produce exact agreement with the verifier’s hidden expectations, and will not score highly.
