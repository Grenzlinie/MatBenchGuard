# DFT Electrocatalytic Mechanism Elucidation

This workflow family encompasses systematic density functional theory (DFT) calculations designed to model catalytic active sites, compute adsorption free energies of reaction intermediates, construct free‑energy profiles, identify rate‑determining steps and overpotentials, and correlate catalytic activity with electronic structure for electrocatalytic reactions. Typical target reactions include the oxygen reduction/evolution (ORR/OER), hydrogen evolution (HER), CO₂ electroreduction (CO₂RR), methanol oxidation, and related processes on a variety of catalyst classes such as single‑atom catalysts on N‑doped carbon, oxide spinels, metal–organic frameworks (MOFs), covalent organic frameworks (COFs), and bimetallic systems.

## Common Computational Pattern

1. **Model construction.** A representative structural model of the catalyst is built from crystallographic data or literature. For surface‑mediated reactions, periodic slab models are constructed with suitable terminations and vacuum gaps; for molecular-level active sites, cluster models of the catalytic center (e.g., M–N₄ moieties on graphene) are employed. Doping, defects, or adsorbates are introduced as needed.

2. **DFT energy calculations.** Spin‑polarised DFT calculations are carried out using plane‑wave codes such as VASP with projector‑augmented wave (PAW) pseudopotentials and the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional. Common additions include a Hubbard‑U correction for transition‑metal oxides (e.g., Co₃O₄ with U−J = 3 eV), Grimme’s D3 dispersion correction, and, when required, a Gaussian‑type orbital code (e.g., B3PW91) for cluster models. Geometry optimizations are performed to a tight force criterion; vibrational frequencies are computed for zero‑point energies and entropic contributions.

3. **Free‑energy landscape construction.** Using the computational hydrogen electrode (CHE) scheme, the Gibbs free energy change of each elementary proton‑coupled electron transfer step is calculated as
   \[ \Delta G = \Delta E_{\text{elec}} + \Delta E_{\text{ZPE}} - T\Delta S + \Delta G_{U} + \Delta G_{\text{pH}}, \]
   where \(\Delta G_{U} = -eU\) accounts for the applied potential and \(\Delta G_{\text{pH}} = -k_{\text{B}}T\ln 10\cdot\text{pH}\) for proton concentration. This yields a free‑energy diagram along the reaction pathway.

4. **Activity metrics.** The rate‑determining step is identified as the elementary step with the largest positive free‑energy change. The corresponding overpotential is derived as the difference between the potential at which all steps become downhill and the equilibrium potential. For CO₂RR, product selectivity is assessed by comparing the free energies of branch points (e.g., *COOH vs *HCOO formation) and by checking whether further hydrogenation or product desorption is thermodynamically preferred.

5. **Electronic structure analysis.** Adsorption energies are correlated with electronic descriptors such as Mulliken charges, Bader charges, density of states (DOS), and d‑band center positions. This analysis links chemical modifications (doping, alloying, defect creation) to changes in intermediate binding strength and catalytic performance.

## Typical Verification Style

The verification style for this family is **numeric**: computed adsorption free energies, overpotentials, and limiting potentials are compared with experimental trends (e.g., observed product selectivity, activity enhancement upon doping) or with literature DFT benchmarks. For instance, a dopant‑dependent trend in the overpotential for OOH formation or a change in the free‑energy sink for CO adsorption is checked for consistency with previously reported experimental or computational data.

## Task Organization

Each task in this family corresponds to a published paper and is stored in a directory named `paper-<paper_id>`. The public entry point is the file `instruction.md`, which specifies the exact conclusion to reproduce, the computational resources required (e.g., VASP input files, structure files), and the expected numeric outcome. The solving agent retrieves the necessary inputs, runs the DFT calculations, and reports the derived metrics for verification. The workflow family as a whole provides a library of over 70 validated DFT protocols for electrocatalytic mechanism investigation.

**Supported software and methods** (as indicated in the provided context):
- VASP (PAW, PBE, DFT+U, D3)
- Gaussian (B3PW91/LANL2DZ/6‑31G(d))
- Computational hydrogen electrode (CHE) framework
- Koutecký–Levich analysis for electron‑transfer numbers (experimental complement)
- EXAFS, XANES, XPS, HAADF‑STEM for structural validation (used in papers but not computed by the tasks).
