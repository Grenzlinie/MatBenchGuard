# DFT Reaction Mechanism Energetics for Silicon Systems

## Problem background
Kinetic experiments have shown that ground‑state silicon atoms (³P) react with ethylene and acetylene at rates approaching unit collisional efficiency, which implies that the collisions form one or more stable complexes with little or no activation barrier. To rationalize this fast chemistry, it is necessary to explore the triplet potential energy surfaces of SiC₂H₄ and SiC₂H₂ and identify which geometric isomers are the lowest in energy. Understanding the relative stabilities of the possible triplet structures, and the ordering of their energies with respect to the separated fragments, explains why the reactions proceed so efficiently and provides insight into the preferred bonding motifs in organosilicon intermediates.

## Approach
The calculations employ spin‑unrestricted Møller‑Plesset second‑order perturbation theory (UMP2) together with spin projection that removes the two largest spin contaminants (PUMP2). Geometries of candidate triplet isomers and the dissociation fragments (Si(³P) + C₂H₄ / C₂H₂) are optimized with a double‑ζ plus polarization (DZP) basis set. For selected low‑lying isomers, single‑point PUMP2 energies are also computed with a larger triple‑ζ plus double‑polarization (TZ2P) basis set, using the DZP‑optimized geometries. The target quantities are total electronic energies in hartrees and relative enthalpies in kcal/mol, always referenced to the separated ground‑state fragments. The method workflow therefore steps from initial structure generation, through cheap pre‑screening, geometry optimization, and finally energy evaluation at two levels of theory.

## Reproduction target
The task is to produce two JSON files that contain the computed PUMP2 energies for a set of triplet isomers of SiC₂H₄ and SiC₂H₂.
- For SiC₂H₄: compute PUMP2/DZP energies for isomers 1a, 1b, 2, 3, 4b, 6, and for the reference fragments Si(³P) and C₂H₄. Additionally, for isomers 1a, 2, and 3 compute PUMP2/TZ2P energies.
- For SiC₂H₂: compute PUMP2/DZP energies for isomers 19, 20, 21, 22, and for Si(³P) and C₂H₂. For isomers 19 and 20 also compute PUMP2/TZ2P energies.
For every entry report the total energy (in hartree) and the relative energy (kcal/mol) with respect to the appropriate dissociation limit. The two output files must be written to `/app/outputs/sic2h4_energies.json` and `/app/outputs/sic2h2_energies.json` with the exact structure described in the **Output files** section below.

## Assets

- Psi4 (or PySCF) open-source quantum chemistry package: https://psicode.org/

## Basis set definitions

You must use exactly the basis sets described below. All basis functions are Cartesian (6 Cartesian d functions, 3 Cartesian p functions).

### Double‑Zeta plus Polarization (DZP)
- **Carbon**: Dunning (9s5p/4s2p) contraction of Huzinaga's 9s5p primitive set, plus one d polarization function with exponent 0.8.
- **Hydrogen**: Dunning (4s)/[2s] contraction of Huzinaga's 4s primitive set, plus one p polarization function with exponent 1.0.
- **Silicon**: Dunning (11s7p/6s4p) contraction of Huzinaga's 11s7p primitive set, plus one d polarization function with exponent 0.4.

### Triple‑Zeta plus Double‑Polarization (TZ2P)
- **Silicon**: Huzinaga (12s9p) primitive set contracted to [9s6p], plus three d polarization functions with exponents 1.86, 0.59, 0.20.
- **Carbon**: Huzinaga (10s6p) primitive set contracted to [5s4p], plus two d polarization functions with exponents 1.2, 0.4.
- **Hydrogen**: Dunning (5s) primitive set contracted to [3s], plus two p polarization functions with exponents 1.0, 0.33.

The DZP basis corresponds to the one labelled “DZP” in the paper. The TZ2P basis corresponds to the “TZ2P” basis used for the final single‑point energies.

## PUMP2 energy calculation

The spin‑projected MP2 energy, PUMP2 (the “(2)” variant of Knowles and Handy that removes the two worst spin contaminants), is obtained by post‑processing the UHF and UMP2 results. For triplet systems (s=1, ideal ⟨Ŝ²⟩=2):

1. Perform an unrestricted HF calculation to obtain the total energy E_UHF and the expectation value ⟨Ŝ²⟩_UHF.
2. Perform an unrestricted MP2 calculation using the same reference to obtain the correlation‑corrected energy E_UMP2.
3. Compute the PUMP2 energy as:

   E_PUMP2 = E_UMP2 – (E_UHF · (⟨Ŝ²⟩_UHF – 2)) / 4

This formula follows the standard spin‑projection approximation that removes the leading (quintet) contamination and is consistent with the Knowles–Handy method (J. Chem. Phys. 1988, 88, 6991). Use it for both the DZP and TZ2P single‑point evaluations.

For the dissociation fragments Si(³P) and C₂H₄ / C₂H₂, the spin contamination is negligible (⟨Ŝ²⟩ ≈ 2.0), so E_PUMP2 ≈ E_UMP2. You must still compute them with the same procedure; the practical difference will be small.

## Workflow steps

### Step 1: Build initial molecular geometries
- Role: process
- Action: Generate initial Cartesian coordinates for all required SiC₂H₄ and SiC₂H₂ triplet isomers and the dissociation fragments (Si(³P), C₂H₄, C₂H₂) using the structural descriptions provided below. These internal coordinates (Z‑matrix templates) give the correct atomic connectivity and approximate bond lengths/angles that place you in the correct basin of the potential energy surface. After constructing the Cartesian coordinates, you may optionally perform a quick force‑field or semi‑empirical pre‑relaxation, but this is not required.
- Evidence: none

#### Initial molecular geometry templates

The unit for bond lengths is Angstrom (Å) and for angles is degrees (°). All dihedral angles are listed as the absolute value; the sign (0 or 180) follows the standard Z‑matrix convention: 0 means cis, 180 means trans.  
For each species, build the corresponding Z‑matrix and then convert it to Cartesian coordinates using any linear algebra library or built‑in converter in your quantum chemistry package.

**Fragment: Si(³P)**  
A single silicon atom. No geometry specification needed.

**Fragment: C₂H₄**
```
C1
C2  C1  1.33
H1  C1  1.08  C2  121.0
H2  C1  1.08  C2  121.0  H1  180.0
H3  C2  1.08  C1  121.0  H1  0.0
H4  C2  1.08  C1  121.0  H3  180.0
```

**Fragment: C₂H₂**
```
C1
C2  C1  1.21
H1  C1  1.06  C2  180.0
H2  C2  1.06  C1  180.0  H1  0.0
```

**Isomer 1a (³A₂ symmetry) – silacyclopropylidene (cyclic)**
Three‑membered Si‑C‑C ring with a short C=C double bond. All atoms lie in a plane.
```
Si
C1  Si  1.85
C2  C1  1.35  Si  60.0
H1a C1  1.09  Si  120.0  C2  180.0
H1b C1  1.09  Si  120.0  C2    0.0
H2a C2  1.09  Si  120.0  C1  180.0
H2b C2  1.09  Si  120.0  C1    0.0
```

**Isomer 1b (³B₁ symmetry) – silacyclopropylidene (cyclic)**
Same connectivity as 1a but with a longer C‑C bond and slightly different ring geometry (UMP2/DZP optimized structure from the paper, Figure 1).
```
Si
C1  Si  1.85
C2  C1  1.48  Si  59.0
H1a C1  1.09  Si  121.0  C2  180.0
H1b C1  1.09  Si  121.0  C2    0.0
H2a C2  1.09  Si  120.0  C1  180.0
H2b C2  1.09  Si  120.0  C1    0.0
```

**Isomer 2 (³A″ symmetry) – trans‑vinylsilylene (HSi–CH=CH₂)**
Planar structure with Si inserted into a C–H bond, trans orientation.
```
C1
C2  C1  1.34
Si  C2  1.85  C1  125.0
H1  Si  1.48  C2  95.0  C1  180.0
H2  C1  1.09  C2  121.0  Si    0.0
H3  C1  1.09  C2  121.0  H2  180.0
H4  C2  1.09  C1  122.0  Si  180.0
```

**Isomer 3 (³A″ symmetry) – cis‑vinylsilylene (HSi–CH=CH₂)**
Same connectivity as 2 but with the SiH group on the same side of the C=C bond (cis).
```
C1
C2  C1  1.34
Si  C2  1.85  C1  125.0
H1  Si  1.48  C2  95.0  C1    0.0
H2  C1  1.09  C2  121.0  Si    0.0
H3  C1  1.09  C2  121.0  H2  180.0
H4  C2  1.09  C1  122.0  Si  180.0
```

**Isomer 4b (³A₂ symmetry) – bent silaallene form**
Si bridges two CH₂ groups; the C–Si–C angle is about 75° and the molecule is planar.
```
C1
C2  C1  2.20
Si  C1  1.85  C2  37.5
H1a C1  1.09  Si  121.0  C2  180.0
H1b C1  1.09  Si  121.0  C2    0.0
H2a C2  1.09  Si  121.0  C1  180.0
H2b C2  1.09  Si  121.0  C1    0.0
```
*(Note: the dummy C–C distance is not a bond; the atoms Si, C1, C2 form an isosceles triangle.)*

**Isomer 6 (³A″ symmetry) – ethylidenesilylene (CH₃–CH=Si)**
A methyl group attached to a silylidene carbon; the C=Si bond is short (~1.70 Å).
```
C1
C2  C1  1.50
Si  C2  1.70  C1  125.0
H1  C2  1.09  C1  118.0  Si  180.0
H2  C1  1.09  C2  110.0  Si  180.0
H3  C1  1.09  C2  110.0  H2  120.0
H4  C1  1.09  C2  110.0  H2 -120.0
```

#### SiC₂H₂ templates

**Isomer 19 (³A symmetry) – silacyclopropenylidene (short C–C)**
A three‑membered Si–C–C ring with a short C–C bond; both hydrogens bound to carbons.
```
Si
C1  Si  1.85
C2  C1  1.35  Si  60.0
H1  C1  1.07  Si  150.0  C2  180.0
H2  C2  1.07  Si  150.0  C1  180.0
```

**Isomer 20 (³A₂ symmetry) – silacyclopropenylidene (long C–C)**
Same connectivity as 19 but with a longer C–C bond.
```
Si
C1  Si  1.85
C2  C1  1.48  Si  59.0
H1  C1  1.07  Si  150.0  C2  180.0
H2  C2  1.07  Si  150.0  C1  180.0
```

**Isomer 21 (³A symmetry) – silylenylacetylene (H–Si–C≡C–H)**
Linear heavy‑atom backbone with a Si–H bond.
```
Si
C1  Si  1.70
C2  C1  1.22  Si  180.0
H1  Si  1.48  C1  95.0  C2  180.0
H2  C2  1.06  C1  180.0  Si    0.0
```

**Isomer 22 (³A″ symmetry) – vinylidenesilene (H₂C=C=Si)**
A cumulene‑like structure; the H–C–H plane is perpendicular to the C=C=Si axis.
```
C1
C2  C1  1.31
Si  C2  1.69  C1  180.0
H1  C1  1.09  C2  121.0  Si  180.0
H2  C1  1.09  C2  121.0  H1    0.0
```

### Step 2: Geometry optimization (DZP)
- Role: process
- Action: Optimize the geometry of each isomer and fragment at the UMP2/DZP level of theory. The fragment geometries (Si(³P), C₂H₄, C₂H₂) must also be optimized separately. Verify that the optimized structures correspond to the desired electronic state (triplet) and have no imaginary frequencies.
- Evidence: none

### Step 3: Single‑point PUMP2/DZP energies
- Role: process
- Action: At the optimized DZP geometries, compute UHF and UMP2 energies, then evaluate the PUMP2 energy using the formula above. Record the total PUMP2 energy for each species.
- Evidence: none

### Step 4: Single‑point PUMP2/TZ2P energies (selected isomers)
- Role: process
- Action: For the isomers listed in the **Reproduction target** section that require TZ2P energies, perform a single‑point calculation at the DZP‑optimized geometry using the TZ2P basis set. Compute UHF, UMP2, and then PUMP2 energy. Do **not** re‑optimize geometry.
- Evidence: none

### Step 5: Compute relative energies and write output files
- Role: process
- Action: For each isomer, compute the relative energy with respect to the appropriate dissociation fragments: ΔH (kcal/mol) = [E_PUMP2(isomer) – E_PUMP2(Si) – E_PUMP2(partner)] × 627.509474. For the fragments themselves, the relative energy is defined as 0.0. Write the results to the two JSON files exactly as specified below.
- Evidence: The output JSON files (`sic2h4_energies.json` and `sic2h2_energies.json`)

## Output files

Both output files must be **JSON arrays** of objects. Each object represents one computed entry and contains exactly the following keys:

- `"isomer"`: a string identifying the species (e.g. `"1a"`, `"Si"`, `"C2H4"`, `"19"`).
- `"symmetry"`: the electronic state symmetry label as a string (e.g. `"3A2"`, `"3A''"`, `"3P"`, `"1Ag"`). Use the symmetry labels that correspond to the optimized wavefunction.
- `"basis"`: either `"DZP"` or `"TZ2P"`.
- `"total_energy_hartree"`: the PUMP2 total electronic energy in hartree, as a float.
- `"relative_energy_kcal_per_mol"`: the relative energy in kcal/mol computed as described in Step 5, as a float.

Example entry:
```json
{
  "isomer": "1a",
  "symmetry": "3A2",
  "basis": "DZP",
  "total_energy_hartree": -367.316615,
  "relative_energy_kcal_per_mol": -17.15
}
```

The array for SiC₂H₄ must contain entries for all fragments and isomers listed in **Reproduction target** (including DZP and TZ2P entries). The array for SiC₂H₂ must contain the corresponding entries. The order of objects in the array does not matter. The file names must be **exactly** `/app/outputs/sic2h4_energies.json` and `/app/outputs/sic2h2_energies.json`.