# OER free-energy and chloride adsorption DFT analysis for Ni(OH)₂‑based catalyst surfaces

## Problem background
Photoelectrochemical seawater splitting for hydrogen production requires photoanodes that resist chloride corrosion while maintaining high oxygen evolution activity. Stainless‑steel thin films electrochemically reconstructed into chromium‑incorporated NiFe (oxy)hydroxide have been explored as protective cocatalysts. Density functional theory (DFT) is used to compare the oxygen evolution reaction (OER) energetics and chloride adsorption on the doped surface versus pure Ni(OH)₂, in order to understand the origin of any performance differences.

The computational investigation models the (0001) surface of hexagonal Ni(OH)₂ and a doped slab where surface Ni cations are partially substituted by Fe and Cr. Spin‑polarized DFT+U calculations with a dispersion correction were used to obtain total energies of the clean slabs and of the key OER intermediates (*OH, *O, *OOH) adsorbed on both surfaces, as well as the gas‑phase reference molecules and chloride‑adsorbed slabs. From these, reaction free energies are constructed within the computational hydrogen electrode model at alkaline pH (pH 14). Chloride adsorption energies are computed for several metal sites on each surface. The free‑energy profiles are evaluated at two applied potentials (0 V and 1.23 V vs. RHE) to identify the rate‑determining step and to assess how doping alters the OER barriers and halide binding.

## What you must produce
A single JSON file `/app/outputs/dft_results.json` containing the Gibbs free‑energy changes (ΔG₁–ΔG₄) for each of the four OER elementary steps on Ni(OH)₂ and on the doped (Cr/Fe‑incorporated) surface at U = 0 V and U = 1.23 V vs. RHE, as well as the average difference in chloride adsorption free energy between the doped surface and Ni(OH)₂. All free energies are reported in eV.

## DFT total energies (pre‑computed)
The DFT total energies listed below were obtained using the methodology described in the next section. **You do not need to run any DFT code** – use these values together with the corrections and formulas given later to compute the required Gibbs free‑energy changes.

### Clean slabs and OER intermediates (E_DFT / eV)
| System | Energy (eV) |
|---|---|
| clean Ni(OH)₂ slab | -1000.0000 |
| *OH on Ni(OH)₂ | -1009.6250 |
| *O on Ni(OH)₂ | -1004.3600 |
| *OOH on Ni(OH)₂ | -984.9550 |
| clean doped slab | -1000.0000 |
| *OH on doped | -1009.9250 |
| *O on doped | -1005.1600 |
| *OOH on doped | -1013.1350 |

### Gas‑phase reference molecules (E_DFT / eV)
| Molecule | Energy (eV) |
|---|---|
| H₂O (gas) | -14.0000 |
| H₂ | -6.8000 |
| O₂ | -9.9000 |
| Cl₂ | -3.5000 |

### Cl‑adsorbed slabs (E_DFT / eV)
**Ni(OH)₂ surface**
| Site | Energy (eV) |
|---|---|
| Ni top 1 | -1003.8500 |
| Ni top 2 | -1003.6500 |
| Ni top 3 | -1003.7500 |
| hollow | -1003.7500 |

**Doped surface**
| Site | Energy (eV) |
|---|---|
| Ni top | -1003.6000 |
| Fe top | -1003.5000 |
| Cr top | -1003.4000 |
| hollow | -1003.3000 |

## DFT methodology (for reference)
The energies above were obtained from spin‑polarised DFT+U calculations with the following exact settings:

- **Functional:** Perdew–Burke–Ernzerhof (PBE) exchange–correlation
- **Dispersion correction:** DFT‑D3 (Becke‑Johnson damping)
- **Hubbard U corrections (Dudarev approach, effective U‑J values):**
  - Ni: 6.45 eV
  - Fe: 5.30 eV
  - Cr: 3.50 eV
- **Basis / pseudopotentials:** Projector‑augmented wave (PAW) PBE pseudopotentials for Ni, Fe, Cr, O, H, Cl
- **Plane‑wave cutoff:** 500 eV
- **k‑point mesh:** Γ‑centred 2×2×1 for the slab
- **Vacuum:** 15 Å

## Surface slab models (for reference)
- **Ni(OH)₂ surface:** Hexagonal P‑3m1 (0001) termination, (2×2) supercell, 3‑layer slab. The bottom layer is kept fixed; the top two layers are relaxed.
- **Doped surface:** The same slab, but one surface Ni atom is replaced by Fe and one by Cr. The top two layers are relaxed; the bottom layer is fixed.

## OER elementary steps
The four proton‑coupled electron transfer steps are:

**Step 1:** H₂O(l) + * → *OH + H⁺ + e⁻  
**Step 2:** *OH → *O + H⁺ + e⁻  
**Step 3:** H₂O(l) + *O → *OOH + H⁺ + e⁻  
**Step 4:** *OOH → * + O₂(g) + H⁺ + e⁻  

where `*` denotes an empty surface site.

## Computational hydrogen electrode (CHE) model at pH 14
The free energy of a proton–electron pair is taken as ½G(H₂) – eU, with U the applied potential vs. RHE. The equilibrium potential for OER at pH 14 is 1.23 V.

The Gibbs free energy of each intermediate is obtained from its DFT total energy plus a correction from the table below. The change ΔGᵢ for step i is the difference in corrected free energies of the product and reactant intermediates (or reference molecules). All free energies are referenced to pure water and standard H₂/O₂ gas phases.

### Zero‑point energy and entropy corrections (at T = 298 K)
Apply the following ΔZPE – TΔS corrections (eV) to the DFT energies:

| Species | Correction (eV) |
|---------|----------------|
| *OH     | 0.35            |
| *O      | 0.05            |
| *OOH    | 0.40            |
| H₂O(l)  | 0.56 (relative to H₂O gas at 0.035 bar) |
| H₂(g)   | 0.27            |
| O₂(g)   | 0.00            |

*Note:* For H₂O(l) the free energy is taken as G(H₂O, gas at 0.035 bar) + 0.56 eV, which is equivalent to the experimental gaseous value plus a condensation correction. In practice you should compute:
G(H₂O(l)) = E(H₂O, gas) + 0.56 eV.
Likewise, G(H₂) = E(H₂) + 0.27 eV and G(O₂) = E(O₂) + 0.00 eV.

### Calculation of ΔGᵢ at potential U
Use the corrected free energies and the DFT energies from the tables above:

ΔG₁ = G(*OH) – G(clean) – G(H₂O(l)) + ½G(H₂) – eU  
ΔG₂ = G(*O) – G(*OH) + ½G(H₂) – eU  
ΔG₃ = G(*OOH) – G(*O) – G(H₂O(l)) + ½G(H₂) – eU  
ΔG₄ = 4.92 eV – (ΔG₁ + ΔG₂ + ΔG₃)   (this follows from the sum of the four steps being 4.92 eV at equilibrium)

where eU = 0 for U = 0 V and eU = 1.23 eV for U = 1.23 V vs. RHE.

## Chloride adsorption
- The Cl adsorption free energy for a given site is:
  ΔG_Cl = E(slab+Cl) – E(slab) – ½E(Cl₂)
  (no ZPE/TS correction is applied to the Cl₂ reference or the adsorbed Cl).
- Use the clean‑slab energies listed in the first table and the Cl‑adsorbed slab energies from the third table.
- Compute ΔG_Cl for every listed site on Ni(OH)₂ and every listed site on the doped surface.
- Calculate the **average** ΔG_Cl over all considered sites for each surface (four sites per surface).
- The required quantity is the **difference**:  
  **Cl_adsorption_difference** = ⟨ΔG_Cl⟩doped – ⟨ΔG_Cl⟩Ni(OH)₂  
  A **positive** value means that Cl⁻ binds more weakly on the doped surface.

## Output file
Write a single file `/app/outputs/dft_results.json` with the following structure:

```json
{
  "Ni(OH)2": {
    "U0": {"G1": <float>, "G2": <float>, "G3": <float>, "G4": <float>},
    "U123": {"G1": <float>, "G2": <float>, "G3": <float>, "G4": <float>}
  },
  "doped": {
    "U0": {"G1": <float>, "G2": <float>, "G3": <float>, "G4": <float>},
    "U123": {"G1": <float>, "G2": <float>, "G3": <float>, "G4": <float>}
  },
  "Cl_adsorption_difference": <float>
}
```

All values are in eV. The file will be automatically validated against a hidden reference; you must provide results consistent with the parameters and procedures described above.