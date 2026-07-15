REGULAR PAPERS

First-principles calculation study of electronic structures and magnetic properties of Mn-doped perovskite crystals for solar cell applications

To cite this article: Atsushi Suzuki and Takeo Oku 2018 *Jpn. J. Appl. Phys.* **57** 02CE04

View the article online for updates and enhancements.

![](./images/813074357050933249_1.jpg)

Related content

- [Electronic structures and magnetic properties of $Sc_2YN@C_{60}(CF_3)_2$ dimer](https://iopscience.iop.org/article/10.7567/JJAP.57.02CE04)
Atsushi Suzuki and Takeo Oku

- [Electronic structures and magnetic properties of $Sc_4O_2@C_{60}(CF_3)_n$ ($n=2$ and 4)](https://iopscience.iop.org/article/10.7567/JJAP.57.02CE04)
Yuma Abe, Atsushi Suzuki and Takeo Oku

- [Electronic structure and magnetic properties of endohedral metallofullerenes based on mixed metal cluster within fullerene cage with trifluoromethyl groups](https://iopscience.iop.org/article/10.7567/JJAP.57.02CE04)
A Suzuki and T Oku

This content was downloaded from IP address 80.82.77.83 on 02/01/2018 at 00:56

# First-principles calculation study of electronic structures and magnetic properties of Mn-doped perovskite crystals for solar cell applications

Atsushi Suzuki* and Takeo Oku

Department of Materials Science, School of Engineering, The University of Shiga Prefecture, Hikone, Shiga 522-8533, Japan

*E-mail: suzuki@mat.usp.ac.jp

Received June 30, 2017; accepted September 21, 2017; published online December 19, 2017

The electronic structures and magnetic properties of manganese (Mn)-doped formamidinium lead halide perovskite compounds (FAPbI₃, where FA = NH₂CHNH₂⁺) were investigated for solar cell application. The effects of Mn doping into FAPbI₃ crystals on electronic structures, chemical shifts in nuclear magnetic resonance, and optical absorption spectra were studied by first-principles calculation on the basis of the density functional theory. The electron density distribution of the 6p orbital was delocalized on an iodine atom at the highest occupied molecular orbital, and that of the 3d orbital was localized on a Mn atom at the lowest unoccupied molecular orbital. The absorption properties in the near-infrared region originated from the first excitation process of ligand-metal charge transfer (LMCT). The chemical shifts of I-NMR and the g-tensor of Mn ions were associated with nuclear quadrupole interactions based on an electron field gradient and asymmetry parameters. The combination of LMCT with magnetic interactions is important for developing photovoltaic solar cells with a broad-band optical absorption spectrum in the near-infrared region.

© 2018 The Japan Society of Applied Physics

## 1. Introduction

Perovskite solar cells have great advantages in terms of photovoltaic performance with high efficiency of conversion and optical properties, which are optimized with perovskite compounds. Control of chemical composition ratio using organic cations from methylammonium (MA = CH₃NH₃⁺), formamidinium [FA = CH₃(NH₂)₂⁺],¹⁾²⁾ and cesium (Cs),³⁾ divalent metals (lead, tin, and bismuth),⁴⁾ chemical processes using halogen anions (Cl⁻, Br⁻, and I⁻)⁵⁻⁷⁾ in perovskite crystals, and solution processing methods⁸⁾ are important for improving photovoltaic behavior with an efficiency of conversion higher than 20%. In particular, the effects of halogen doping using bromide, iodide, and chloride halides, mixed cations, and hole-transporting layers on photovoltaic and optical properties have been investigated to improve charge transport and photovoltaic performance. From a practical view point, hybrid lead (Pb)-free perovskite and mixed tin (Sn)/Pb perovskite crystals have been developed to control band structure, bandgap, and absorption.⁹⁾¹⁰⁾ From the viewpoint of performance, mixed-cation Sn-based MA₀.₅FA₀.₅-Pb₀.₇₅Sn₀.₂₅I₃ perovskite crystals were used for the development of four-terminal all-perovskite tandem solar cells to achieve a high efficiency of conversion in a wide range of wavelengths.¹¹⁾¹²⁾ Electronic structural, optical property, and Raman spectroscopic analyses of mixed halogen hybrid perovskites have been carried out on the basis of experimental results with quantum calculation based on the density functional theory (DFT) and time-dependent (TD)-DFT.¹³⁻¹⁶⁾ For instance, the effects of CH₃NH₃⁺ in MAPbI₃ on optical transitions have been investigated on the basis of DFT. The distinct optical transitions observed in CH₃NH₃PbI₃ were attributed to the direct semiconductor-type transitions at the R, M, and X points in the pseudo cubic Brillouin zone.¹⁷⁾ For the characterization of photovoltaic materials, the photovoltaic and semi conductive mechanisms and the local order and dynamics of halogen and lead atoms in mixed-cation and halogen (MA)ₓ(FA)₁₋ₓPbX₃ (X = Cl, Br, and I) hybrid perovskite crystals were clarified using magnetic techniques including multinuclear (¹H, ¹⁴N, ²⁰⁷Pb, and ¹²⁷I) and quadrupole magnetic resonance (NMR/NQR) spectroscopies with quantum calculation.¹⁸⁻²⁰⁾ In addition, photovoltaic materials with manganese (Mn)-doped CH₃NH₃PbI₃ perovskite compounds have been characterized for applications in photovoltaic solar cells and spintronic devices.²¹⁾ The magnetic interactions between localized and itinerant spins in a Mn-doped perovskite crystal were controlled by adjusting carrier concentration. A slight perturbation of the crystal field of the 3d orbital in a transition metal will result in extremely large changes in photovoltaic properties, magnetic parameters, and resistivity. Quantum confinement of charged carriers in the sp²–3d orbital exchange interactions in Mn-doped cesium lead halide perovskite compounds will be utilized as a new platform for photovoltaic devices having optical and magnetic properties. The photovoltaic and magnetic properties, charge transfer, and electron conductivity of n-type semi conductive materials were affected by the symmetry of the crystal structure and lattice spacing in relation to the metal concentration and composition ratio in metal-doped perovskite crystals. The crystal system, lattice spacing, crystal symmetry, and tolerance factor were considered to greatly affect the ionic radii of metal and halogen atoms. In an actual case of overdoping at 10% Mn, the crystal structure changed to form a tetragonal space group, which showed Ruderman–Kittel–Kasuya–Yosida (RKKY) magnetic interactions between magnetic metal ions.²²⁾²³⁾ The magnetic interactions were related to the density of localized spins and the density of itinerant electrons as functions of metal–metal distance and the size of the Fermi surface.

The purpose of this work is to investigate the electronic structure and the photovoltaic and magnetic properties of Mn-doped formamidinium lead halide perovskite compounds (FAPbI₃, where FA = NH₂CHNH₂⁺) for solar cell applications. The effects of Mn doping into a FAPbI₃ perovskite crystal on band structures, the chemical shifts of ¹³C-, ¹⁴N-, ²⁰⁷Pb-, and I-NMR, the g-tensor, the V-tensor of an electronic field gradient, and optical absorption spectra will be studied by first-principles calculation based on the density functional theory. The slight perturbation of the electronic structure and the magnetic parameters on the octahedral crystal field splitting of the 3d orbital of the Mn atom and halogen ligand in a Mn-doped FAPbI₃ crystal as an isolated dilution system

will be discussed. The photovoltaic mechanism will be discussed on the basis of the electronic structures including the density of state (DOS), the electron density distribution of the $\text{sp}^2$ hybrid orbital of the iodine halogen atom at the highest occupied molecular orbital (HOMO), and those of the $\text{sp}^2$-$3\text{d}$ hybrid orbital of the Mn atom and the $\text{sp}^2$ hybrid orbital of the Pb atom at the lowest unoccupied molecular orbital (LUMO).$^{24)}$ The effects of Mn doping into the perovskite crystal on the chemical shift of $^{13}\text{C}$-, $^{14}\text{N}$-, $^{207}\text{Pb}$-, and I-NMR and the $g$-tensor in the Mn atom will be investigated for applications in photovoltaic solar cells and spintronic devices. Evaluation of the magnetic parameter of chemical shifts, the $g$-tensor, the $V$-tensor of an electronic field gradient, and asymmetry parameter will clarify the magnetic interactions between localized spins on the $3\text{d}$ orbital of the Mn atom and the itinerant electron of the $\text{sp}^2$ hybrid orbital of the I atom in the Mn-doped perovskite crystal. The photovoltaic and magnetic properties will be discussed on the basis of the comparison between the quantum calculation results and the reported experimental results.

## 2. Calculation methods
The electronic structures of the perovskite crystal were single-point calculated using experimental parameters obtained from X-ray diffraction patterns combined with ab initio quantum calculation based on the restricted Hartree–Fock (RHF) method and DFT using B3LYP with the hybrid function LANL2MB as the basis set (Gaussian 09). The perovskite compounds form in a cubic crystal phase with a lattice constant of $6.36\ \mathring{\text{A}}.^{25)}$ As the isolated dilution system, part of the Pb atom at the B-site was substituted with the Mn atom for one-atom substitution at the center of the cubic structure. The Mulliken charges on the Mn-doped $\text{FAPbI}_3$ and $\text{FAPbI}_3$ cubic crystal structures consisting of super cells of $2\times2\times2$ were fixed to be +8 as the positive charge. The numbers of quantum spins in Mn-doped $\text{FAPbI}_3$ and $\text{FAPbI}_3$ are assumed to be in the sextet ($S=5/2$) and singlet ($S=0$) states, respectively. Optimization of the supercells while maintaining the symmetry was unsuccessful owing to the considerable distortion of the structure caused by the Jahn–Teller effect. The single-point calculation was performed similarly to the standard case using $\text{FAPbI}_3$. The tolerance factor of $\text{FAPbI}_3$ is about $1.0.^{26,27)}$ The ionic radii of Mn and Pb atoms are 80 and $120\ \text{pm},^{28)}$ respectively. As the isolated dilution system, the mole ratio of Mn to Pb was adjusted to be 1 : 26. The concentration of the Mn atom was maintained at less than 5% so as not to generate symmetry breaking of the crystal with the suppression of strong exchange interactions in the perovskite crystal. The effect of Mn ionic radius is assumed to be weak in an isolated dilution system. The total DOS, the occupancy of the $3\text{d}$ orbital on the Mn atom, $6\text{s}$, the p orbitals of the I and Pb atoms around HOMO, LUMO, and the HOMO–LUMO band gap ($E_\text{g}$) were calculated. The Mulliken atomic charges, electron and spin density distributions, and electrostatic potential (ESP) of atoms were estimated by Mulliken population analysis. Continuously, isotropic chemical shifts of $^{127}\text{I}$, $^{207}\text{Pb}$, $^{13}\text{C}$, and $^{14}\text{N}$, the principle $g$-tensor, the $V$-tensor of electric field gradient (EFG), and the asymmetry parameter ($\eta$) of Mn atoms were calculated by DFT using NMR and gauge-including atomic orbitals (GIAOs) with the hybrid function B3LYP and LANL2MB as the basis set. Optical absorption spectra, excitation energy, wavelength, and oscillator strength were calculated by TD-DFT with the hybrid function B3LYP and LANL2MB as the basis set. The calculation conditions were applied to short-range interactions. The long-range interactions based on the periodicity of the Mn-doped $\text{FAPbI}_3$ perovskite crystal will not be taken into consideration. In the standard case using the $\text{FAPbI}_3$ crystal with the $2\times2\times2$ supercell structure, quantum calculation and experimental results will be compared and confirmed. The photovoltaic mechanism and magnetic interactions will be discussed on basis of correlation between an itinerant electron and the localized spin on the $3\text{d}$ orbital of the Mn atom and hydrogen ligand. Nuclear quadruple interactions will be discussed on the basis of EFG, $\eta$, and the atomic charge around the nucleus.

![](./images/813074357050933249_2.jpg)

Fig. 1. (Color online) Electronic structures of (a) Mn-doped $\text{FAPbI}_3$ (charge +8, spin: $S=5/2$) and (b) $\text{FAPbI}_3$ (charge +8, spin: singlet) perovskite crystals calculated by DFT using UB3LYP and LANL2MB as basic functions (cubic, $Pm\overline{3}m$, $a=6.36\ \mathring{\text{A}}$).

## 3. Results and discussion
The electronic structures at HOMO and LUMO of Mn-doped $\text{FAPbI}_3$ and $\text{FAPbI}_3$ perovskite crystals are shown in Figs. 1(a) and 1(b), respectively. As shown in Fig. 1(a), 3.7% Mn was slightly doped into a $\text{FAPbI}_3$ perovskite crystal with a cubic structure as the $2\times2\times2$ supercell. The electron density distribution at HOMO was localized on the $5\text{p}$ orbital of the I atom. The $5\text{p}$ orbital will function in the charge transfer as the electron-donating orbital at the valence band state. The electron density distribution at LUMO was localized at the $6\text{p}$ orbital of the Pb atom and the $3\text{d}$ orbital of the Mn atom combined with the $5\text{p}$ orbital of the I atom. The $6\text{p}$ orbital of the Pb atom was mixed with the $3\text{d}$ and $4\text{s}$ orbitals of the Mn atom. The orbital will function in the charge transfer as the electron-accepting orbital at the conducting band state. The electronic structure, band gap, electron density distribution, and magnetic interaction were dominated by the contribution of the exchange interaction of an itinerant electron on the $6\text{p}$ orbital of the Pb atom and the $5\text{p}$ orbital of the I atom with the localized spin on the $3\text{d}$ orbital of the Mn atom in the isolated dilution system.

Electrostatic potential images of the Mn-doped $\text{FAPbI}_3$ and $\text{FAPbI}_3$ perovskite crystals are shown in Fig. 2. The polar-

![](./images/813074357050933249_3.jpg)

Fig. 2. (Color online) Electrostatic potential images of (a) Mn-doped FAPbI₃ and (b) FAPbI₃ crystals.

ization charge and the phase between an iodine halogen atom and a FA cation were reversed by the slight doping of the Mn atom into the FAPbI₃ perovskite crystal. The reversal of the phase upon polarization in the perovskite crystal will be related to the magnetic interaction of nuclear quadrupole interaction. The magnetic interaction will be associated with the magnetic parameters with slight chemical shifts of I-NMR, $^{14}$N-NMR, and the $g$-tensor. The TDOSs of the Mn-doped FAPbI₃ and FAPbI₃ crystals with the 2×2×2 supercell structure are shown in Figs. 3(a) and 3(b), respectively. Comparison of DOSs in the Mn-doped FAPbI₃ and FAPbI₃ crystals showed that a slight doping of Mn into the FAPbI₃ perovskite crystal increased the energy levels at HOMO, and produced DOS of the 3d orbital on the Mn atom at energy levels of $E-E_{\text{F}}=1$ and 8 eV. The band gap between the 5p orbital on the I atom and the down spin of the 3d orbital on the Mn atom in the perovskite crystal was narrowed. The narrowed band gap between the HOMO and LUMO levels will correspond to a broad absorption in the near-infrared region.

The occupancy and energy levels of the 6s and 6p orbitals of the Pb atom, the 3d, 4s, and 4p orbitals of the Mn atom, and the 5p orbital of the I atom in the Mn-doped FAPbI₃ and FAPbI₃ crystals are shown in Figs. 4(a) and 4(b), respectively. In the model case using the Mn-doped FAPbI₃ crystals, there was a sixfold full occupancy on the degenerated upper ($\alpha$) spin of the 3d orbital on the Mn atom near $E-E_{\text{F}}=-6$ eV. In the standard case using the FAPbI₃ crystal, the degenerated 3d down ($\beta$) spin orbital and 4s upper ($\alpha$) and down ($\beta$) spin orbitals of the Mn atom with an occupancy of 0.2 were above the Fermi level. The 4s $\alpha$ and $\beta$ spin orbitals of the Mn atom were mixed with the 6p orbital of the Pb atom at $E-E_{\text{F}}=2$–3 eV. The photovoltaic properties depend on the electronic structure with the itinerant 5p orbital of the I atom, the 6p orbital of the Pb atom, and the localized 3d orbital of the Mn atom in the Mn-doped FAPbI₃ perovskite crystal. The electronic correlation between the 3d ($\beta$) orbital localized in the Mn atom, the itinerant electron on the 5p orbital of the I atom, and the 6p orbital of the Pb atom may be related to carrier mobility and the photovoltaic mechanism for applications in perovskite solar cells and photoinduced magnetic devices. The photovoltaic and optical properties were based on the ligand-metal charge transfer (LMCT) from the 5p orbital on the I atom to the 3d ($\beta$) orbital on the Mn atom in the perovskite crystal. LMCT caused the first excitation process between the p–d orbitals, yielding a narrowed band gap in the near-infrared region. In the standard case using the FAPbI₃ crystal, there was partial occupancy of the 6p orbital of the Pb atom, and full occupancy of the 5p orbital of the I atom near the frontier orbital. The occupied 5p orbital of the I atom was near HOMO, and the partially occupied 6p orbital of the Pb atom was near LUMO. The electronic structure with the band gap of the HOMO–LUMO levels in the FAPbI₃ crystal is associated with semi conductive behavior and photovoltaic properties, as shown by the experimental results.

![](./images/813074357050933249_4.jpg)

Fig. 3. (Color online) Total density of states of (a) Mn-doped FAPbI₃ and (b) FAPbI₃ crystals.

The calculated optical absorption spectra, excited energy, wavelength, and oscillator strength of the Mn-doped FAPbI₃ and FAPbI₃ perovskite crystals are shown in Fig. 5 and Table I. In the standard case using the FAPbI₃ crystal, the spectra of the FAPbI₃ crystal was in the range of 300–800 nm. The oscillation strength near 486 nm was estimated to be about 0.0019, as shown in Fig. 5 and Table I. The calculated results of the spectra of the FAPbI₃ crystal were in agreement with the experimental results.²⁹) It is expected that the same conditions in the Mn-doped FAPbI₃ crystal can be adopted. The spectrum of the Mn-doped FAPbI₃ perovskite crystal was broadened to a range of 800–2000 nm, which was in the infrared region. As shown in Fig. 5 and Table I, the oscillation strength in the first excitation process at 1436 nm

![](./images/813074357050933249_5.jpg)

Fig. 4. (Color online) Energy levels and occupancies of 3d, 4s, 4p, 5p, 6s, and 6p orbitals near frontier orbital of (a) Mn-doped FAPbI₃ and (b) FAPbI₃ perovskite crystals.

<table>
  <thead>
    <tr>
      <th>Sample</th>
      <th>Excited state</th>
      <th>Excited energy (eV)</th>
      <th>Wavelength (nm)</th>
      <th>Oscillation strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Mn-doped FAPbI₃</td>
      <td>1</td>
      <td>0.86</td>
      <td>1436</td>
      <td>0.0049</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.88</td>
      <td>1409</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.88</td>
      <td>1406</td>
      <td>0.0007</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.90</td>
      <td>1380</td>
      <td>0.0030</td>
    </tr>
    <tr>
      <td rowspan="5">FAPbI₃</td>
      <td>1</td>
      <td>2.43</td>
      <td>511</td>
      <td>0.0012</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2.47</td>
      <td>501</td>
      <td>0.0010</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2.55</td>
      <td>486</td>
      <td>0.0019</td>
    </tr>
    <tr>
      <td>4</td>
      <td>2.57</td>
      <td>483</td>
      <td>0.0018</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2.60</td>
      <td>476</td>
      <td>0.0018</td>
    </tr>
  </tbody>
</table>

was calculated to be 0.0049. The first excited process originated from the energy transition process from the ground levels on the 5p orbital of the iodine halogen atom to the excited levels of the 3d orbital on the Mn atom in the perovskite crystal. The first excited process corresponded to LMCT, as shown in Fig. 5. LMCT was induced to generate a broad-band optical absorption spectrum near the infrared region. The ligand-metal charge transfer process has great advantages for developing high-performance photovoltaic solar cells with wide-range spectra in the ultraviolet-visible-near-infrared region. Comparison between the experimental results and the quantum calculation results verified the validity of the isolated dilution system. As reference, the effect of the optical properties according to the composition ratio in the mixed Pb/Sn perovskite compounds was investigated.³⁰) The energy band gaps did not follow a linear trend (Vegard's law), but became narrower (<1.3 eV), suggesting light absorption in the near-infrared range.³⁰)

![](./images/813074357050933249_6.jpg)

Fig. 5. (Color online) Absorption spectra and first excited process of the perovskite crystals calculated by TD-DFT using UB3LYP and LANL2MB as basic functions.

Calculated chemical shifts of I-NMR of the Mn-doped FAPbI₃ and FAPbI₃ crystals are shown in Fig. 6. The chemical shift of the I-NMR of I atom at the location marked a in the Mn-doped FAPbI₃ crystal was slightly split, and the degeneracy was increased by the symmetry crystal field effect. The I-NMR of the I atom at the locations marked b and c in the Mn-doped FAPbI₃ crystal showed a chemical shift in the high magnetic field. The chemical shift of the nearest ligand of the I atom conjugated with the 3d orbital at the Mn atom was markedly split in the high magnetic field. The magnetic parameters were related to the magnetic interaction of nuclear quadrupole interaction based on EFG and $\eta$ of the Mn and I atoms in the Mn-doped FAPbI₃ perovskite crystals.

The calculated chemical shifts of ¹⁴N-NMR of FA in the Mn-doped FAPbI₃ and FAPbI₃ crystals are shown in Fig. 7. In the case of using the Mn-doped FAPbI₃ crystals, the chemical shift of ¹⁴N-NMR of the FA cation at the location marked a was slightly split. At the locations marked b and c, the chemical shift of ¹⁴N-NMR of the FA cation near the

![](./images/813074357050933249_7.jpg)

Fig. 6. (Color online) Chemical shifts of I-NMR of the Mn-doped FAPbI₃ and FAPbI₃ crystals determined by DFT with GIAO.

![](./images/813074357050933249_8.jpg)

![](./images/813074357050933249_9.jpg)

Fig. 7. (Color online) Chemical shifts of ¹⁴N-NMR of the Mn-doped FAPbI₃ and FAPbI₃ crystals determined by DFT with GIAO.

center Mn atom was markedly split. The magnetic mechanism originated from the magnetic interaction of the nuclear quadrupole interaction based on EFG with the $\eta$ of the nuclear spin on Mn and N atoms with nuclear spins of 5/2 and 1. The chemical shift of ¹⁴N-NMR in the perovskite crystals will depend on the crystal phase including cubic, tetragonal, and orthorhombic phases. Using the calculation model based on the experimental results, the crystal structure was assumed to have a cubic crystal system. The magnetic parameter of chemical shift depended on the magnetic interaction between the nuclear spins of Mn and N atoms in the perovskite crystals. The chemical shifts of ¹³C-NMR of the FA cation and Pb-NMR in the Mn-doped FAPbI₃ crystals are shown in Figs. 8(a) and 8(b). At the locations marked $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{c}$ as shown in Fig. 8(a), the chemical shift of ¹³C-NMR of the FA cation in the Mn-doped FAPbI₃ crystal was slightly moved to the high magnetic field. The magnetic parameter was based on the nuclear spin interactions between the 3d orbital in the Mn atom and the ¹³C of the FA cation located at the nearest site of the Mn atom. The chemical shift of ²⁰⁷Pb-NMR in the Mn-doped FAPbI₃ crystal did not affect the locations marked $\boldsymbol{a}$, $\boldsymbol{b}$, and $\boldsymbol{c}$ as shown in Fig. 8(b). The chemical shift of ²⁰⁷Pb-NMR in the Mn-doped FAPbI₃ perovskite crystal was not affected by nuclear quadrupole interaction based on EFG and $\eta$ of the Mn and Pb atoms with nuclear spins of 5/2 and 1/2.

![](./images/813074357050933249_10.jpg)

![](./images/813074357050933249_11.jpg)

Fig. 8. (Color online) Chemical shifts of (a) ¹³C-NMR and (b) Pb-NMR of the Mn-doped FAPbI₃ and FAPbI₃ crystals determined by DFT with GIAO.

The magnetic parameters of the $g$-tensor, $V$-tensor of EFG and $\eta$ of the Mn atom in the Mn-doped FAPbI₃ perovskite crystal are listed in Table II. The Mulliken atomic charge density of the Mn atom in the FAPbI₃ crystal was obtained to

<table>
<caption>Table II. Magnetic parameters of $g$-tensor, $V$-tensor of EFG and $\eta$ of the Mn atom in the Mn-doped FAPbI₃ crystal.</caption>
<thead>
<tr>
<th>Charge</th>
<th>Spin density distribution</th>
<th>$g_{xx}$</th>
<th>$g_{yy}$</th>
<th>$g_{zz}$</th>
<th>$V_{xx}$</th>
<th>$V_{yy}$</th>
<th>$V_{zz}$</th>
<th>$\eta$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.49</td>
<td>4.46</td>
<td>6.02331</td>
<td>6.48829</td>
<td>8.03356</td>
<td>0.04</td>
<td>0.08</td>
<td>0.12</td>
<td>0.30</td>
</tr>
</tbody>
</table>

be 0.49 e. This result indicates that a considerable number of charges were transferred from the 5p orbital on the I atom to the 3d orbital on the Mn atom. The spin density distribution of the Mn atom in the Mn-doped FAPbI₃ crystal was obtained to be 4.46, which was slightly smaller than the expected value of 5 owing to a slightly smaller number of electrons released to the ligand. The magnetic parameters of the principle $g$-tensor, namely, $g_{xx}$, $g_{yy}$, and $g_{zz}$ were calculated to be 6.02, 6.49, and 8.03, respectively, which indicate a high-spin state. The magnetic parameters of the principal $V$-tensor and asymmetry parameter, namely, $V_{xx}$, $V_{yy}$, $V_{zz}$, and $\eta$, were estimated to be 0.04, 0.08, 0.12, and 0.30, respectively. The magnetic parameters were related to the magnetic nuclear quadrupole interaction based on EFG and $\eta$. The magnetic parameters of the $g$-tensor at the sextet state depend on the degenerated 3d orbital of the Mn atom conjugated with the 6p orbital of the I atom in the octahedral crystal field with cubic symmetry.

The allowed ESR and NMR transitions are explained by the energy level diagram of Mn atoms. The degeneracy of the doublet splits each ground state into six different quantum states in the magnetic field. The separated states are considerably shifted by nuclear quadrupole interaction based on EFG and $\eta$ of the Mn atom at $I=5/2$. The allowed ESR and NMR transitions are due to the separated energy level. The spin Hamiltonian and $g$-tensor are expressed by Eqs. (1) and (2). The spin Hamiltonian (HQ) with regard to the nuclear quadrupole interaction is expressed by Eqs. (3) and (4). The magnetic parameters $g_{\rm e}$ and $g_{\rm N}$ represent the $g$ factors, namely, free electrons and nuclear spins, respectively. $\beta$ and $\beta_{\rm N}$ means the Bohr magneton and nuclear magneton, respectively. The $A$-tensor is the spin coupling constant in a hyperfine structure for the electron–nuclear spin interaction. $S$ and $I$ are the quantum number of electrons and nuclear spins, respectively. $H$ is the magnetic field. The parameters $\varphi$, $L$, $\varepsilon_{m}$, and $\varepsilon_{p}$ are the wave function, the operator of orbital angular momentum, the energy level of each orbital, and the energy level at the ground state, respectively. $eQ$ is the quadrupole moment, and $eq_{zz}$ is the maximum principal value of $V_{zz}$ along the $z$-axis.

As noted in Eq. (1), the spin Hamiltonian is the sum of the Zeeman effects of electron and nuclear spins under magnetic field in the first and second terms, electron–nuclear spin interaction (SAI) as dipole–dipole interaction in the third term, and nuclear quadrupole interaction (IQI) in the fourth term based on EFG and $\eta$ generated by the charge distribution around the nucleus. As noted in Eq. (2), the magnetic parameter of the $g$-tensor depends on spin local interaction, electron density distribution, and energy transition from the ground state to the excited state. Crystal splitting of the 3d orbital of the Mn atom in the Mn-doped FAPbI₃ crystal is shown in Fig. 9. The anisotropic behavior of the magnetic parameter was based on the crystal splitting of the 3d orbital of the Mn atom in the Mn-doped FAPbI₃ crystal, as shown in Fig. 9. The first excited transition process was based on LMCT from the 5p orbital of the I atom to the 3d orbital of the Mn atom in the Mn-doped FAPbI₃ perovskite crystal.

$$
H = g\beta SH - g_{\rm N}\beta_{\rm N}SH + {\rm SAI} + {\rm IQI} \tag{1}
$$

$$
g = g_{\rm e}\left(1 + \sum_{m} \frac{\langle \varphi_{m}|L|\varphi_{p}\rangle}{\varepsilon_{m} - \varepsilon_{p}}\right) \tag{2}
$$

$$
H_{\rm Q} = \frac{e^{2}q_{zz}Q}{4I(I - 1)}\left[3I_{z}^{2} - I(I + 1) + \eta(I_{x}^{2} + I_{y}^{2})\right] \tag{3}
$$

$$
|V_{zz}| \geq |V_{xx}| \geq |V_{xx}|,\quad eq = V_{xx},\quad \eta = \frac{V_{xx} - V_{yy}}{V_{zz}} \tag{4}
$$

![](./images/813074357050933249_12.jpg)
Fig. 9. (Color online) Crystal splitting of 3d orbital of Mn atom in the Mn-doped FAPbI₃ crystal.

The magnetic parameters of chemical shifts based on nuclear quadrupole interaction needs to be considered in accordance with the first and second perturbations. As noted in Eqs. (3) and (4), the nuclear quadrupole interaction is related to the nuclear quadrupole moment based on the $Q$-tensor, EFG, and $\eta$ generated by charge distribution around the nucleus. The chemical shifts of I-NMR and $^{14}$N-NMR would be markedly moved by nuclear quadrupole interaction in proportion to the extent of the $V$-tensor of EFG and $\eta$ with a lack of balance in charge density distribution. The chemical shifts of I-NMR and $^{14}$N-NMR depend on the multistate separation transition and nuclear spin interaction. Multiseparate transition states are based on the hyperfine coupling between the electrons and nuclear spins in Mn, N, and I atoms with nuclear spin numbers of $I=5/2$, 1, and $5/2$, respectively. The nuclear magnetic interaction, multisepara-

tion, and spin oscillation are important factors for controlling the magnetic parameters of chemical shifts, $g$-tensor, $V$-tensor, and $\eta$.

The electron structures and nuclear spin interaction of 3d transition metal at multistates have the great advantage in controlling the photovoltaic and magnetic properties. The relaxation mechanism is explained by the spin-lattice vibration modes (phonon) in the perovskite crystal. The spin oscillation during the spin lattice relaxation depends on the extent of electron and charge density distribution in the perovskite crystals. The Mn-doped perovskite crystals with the phase inversion of the charge distribution affected the photovoltaic and optical properties, and the magnetic parameters of chemical shifts based on nuclear quadrupole interaction. The combination of LMCT with magnetic interaction is an important factor to develop the photovoltaic solar cells with a broad absorption in the UV-vis-near-infrared region. A slight perturbation of transition metal doped into the perovskite crystal as the isolated dilution system affected the photovoltaic and semi conductive properties and magnetic parameters, suggesting the expectation of a new platform consisting of the photovoltaic devices having optical and magnetic properties.

## 4. Conclusions
The electronic structures and magnetic properties of the Mn-doped $FAPbI_3$ perovskite compounds as the isolated dilution system were investigated for solar cells and photoinduced magnetic devices. The effects of Mn doping into the perovskite crystals on the electronic structures and the magnetic parameters of chemical shifts of $^{207}$Pb-, I-, $^{14}$N-, and $^{13}$C-NMR spectra, the $g$-tensor, the $V$-tensor of EFG, and optical absorption spectra were studied by first-principles calculation based on DFT. The electronic structures near the frontier orbital had the 5p orbital on the iodine halogen atom as HOMO and the localized 3d orbital on the Mn atom as LUMO. The narrowing band gap between the 5p orbital of the I atom and the 3d orbital of the Mn atom in the Mn-doped $FAPbI_3$ crystals corresponded to a wide range of optical absorption spectra in the near-infrared region. Slight doping of Mn ions into the perovskite crystal affected the total density of state, the electron occupancy of the 3d and 4s orbitals of Mn atoms near the frontier orbital, and electrostatic potential. The photovoltaic and photoinduced magnetic mechanisms were based on the considerable contributions of itinerant electrons on the 5p orbital of the I atom at HOMO and the 6p orbital of the Pb atom and the 3d orbital of the Mn atom at LUMO. The absorption properties in the near-infrared region originated from the first excited process via LMCT from the 5p orbital of the I atom to the 3d orbital on the Mn atom in the perovskite crystal. Reversal of the phase upon polarization affected the magnetic nuclear quadrupole interactions. The chemical shifts of I-NMR and the $g$-tensor of the Mn atom were associated with the magnetic interaction with the nuclear quadrupole interaction based on EFG and $\eta$ of the Mn atom in perovskite crystals. The combination of LMCT with magnetic interaction is important for developing photovoltaic solar cells with a broad absorption in the near-infrared region. The slight perturbation of the transition metal doped into the perovskite crystal affected the photovoltaic and semi conductive properties and magnetic parameters, suggesting the expectation of a new platform consistent with the photovoltaic devices having optical and magnetic properties.

## Acknowledgment
This work was partly supported by the Satellite Cluster Program of the Japan Science and Technology Agency.

1) A. A. Zhumenekenov, M. I. Saidaminov, Md. A. Haque, E. Alarousu, S. P. Sarmah, B. Murali, I. Dursun, X.-H. Miao, A. L. Abdelhay, T. Wu, O. F. Mohammed, and O. M. Bakr, *ACS Energy Lett.* **1**, 32 (2016).
2) Y. Umemoto, A. Suzuki, and T. Oku, *AIP Conf. Proc.* **1807**, 020011 (2017).
3) M. Saliba, T. Matsu, J. Y. Seo, K. Domanski, J. P. C. Baena, M. K. Nazeeruddin, S. M. Zakeeruddin, W. Tress, A. Abate, A. Hagfeldt, and M. Grätzel, *Energy Environ. Sci.* **9**, 1989 (2016).
4) H. X. Zhu and J. M. Li, *Sci. Rep.* **6**, 37425 (2016).
5) K. Suzuki, A. Suzuki, M. Zushi, and T. Oku, *AIP Conf. Proc.* **1649**, 96 (2015).
6) A. Suzuki, H. Okada, and T. Oku, *Energies* **9**, 376 (2016).
7) C. C. Stoumpos, C. M. M. Soe, H. Tsai, W. Nie, J. C. Blancon, D. H. Cao, F. Liu, B. Traoré, C. Katan, J. Even, A. D. Mohite, and M. G. Kanatzidis, *Chem* **2**, 427 (2017).
8) X. Li, D. Bi, C. Yi, J. D. Décoppet, J. Luo, S. M. Zakeeruddin, A. Hagfeldt, and M. Grätzel, *Science* **353**, 58 (2016).
9) C. Zhang, L. Gao, S. Hayase, and T. Ma, *Chem. Lett.* **46**, 1276 (2017).
10) Q. Shen, Y. Ogomi, J. Chang, T. Toyoda, K. Fujiwara, K. Yoshino, K. Sato, K. Yamazaki, M. Akimoto, Y. Kuga, K. Katayama, and S. Hayase, *J. Mater. Chem. A* **3**, 9308 (2015).
11) D. P. McMeekin, G. Sadoughi, W. Rehman, G. E. Eperon, M. Saliba, M. T. Hörantner, A. Haghighirad, N. Sakai, L. Korte, B. Rech, M. B. Johnston, L. M. Herz, and H. J. Snaith, *Science* **351**, 151 (2016).
12) Z. Yang, A. Rajagopal, C. C. Chueh, S. B. Jo, B. Liu, T. Zhao, and A. K. Y. Jen, *Adv. Mater.* **28**, 8990 (2016).
13) A. Amat, E. Mosconi, E. Ronca, C. Quarti, P. Umari, M. K. Nazeeruddin, M. Grätzel, and F. D. Angelis, *Nano Lett.* **14**, 3608 (2014).
14) H. J. Feng, T. R. Paudel, E. Y. Tsymbal, and X. C. Zeng, *J. Am. Chem. Soc.* **137**, 8227 (2015).
15) B. W. Park, S. M. Jain, X. Zhang, A. Hagfeldt, G. Boschloo, and T. Edvinsson, *ACS Nano* **9**, 2088 (2015).
16) H. J. Feng, W. Deng, K. Yang, J. Huang, and X. C. Zeng, *J. Phys. Chem. C* **121**, 4471 (2017).
17) M. Shirayama, H. Kadowaki, T. Miyadera, T. Sugita, M. Tamakoshi, M. Kato, T. Fujiseki, D. Murata, S. Hara, T. N. Murakami, S. Fujimoto, M. Chikamatsu, and H. Fujiwara, *Phys. Rev. Appl.* **5**, 014012 (2016).
18) C. Roiland, G. T. Allard, K. Jemli, B. Alonso, J. C. Ameline, R. Gautier, T. Bataille, L. L. Pollès, E. Deleporte, J. Even, and C. Katan, *Phys. Chem. Chem. Phys.* **18**, 27133 (2016).
19) A. Senocrate, I. Moudrakovski, G. Y. Kim, T. Y. Yang, G. Gregori, M. Grätzel, and J. Maier, *Angew. Chem.* **56**, 7755 (2017).
20) D. J. Kubicki, D. Prochowicz, A. Hofstetter, P. Péchy, S. M. Zakeeruddin, M. Grätzel, and L. Emsley, *J. Am. Chem. Soc.* **139**, 10055 (2017).
21) B. Náfrádi, P. Szirmai, M. Spina, H. Lee, O. V. Yazyev, A. Arakcheeva, D. Chernyshov, M. Givert, L. Forró, and E. Horváth, *Nat. Commun.* **7**, 13406 (2016).
22) W. J. Mir, M. Jagadeeswararao, S. Das, and A. Nag, *ACS Energy Lett.* **2**, 537 (2017).
23) D. Parobek, B. J. Roman, Y. Dong, H. Jin, E. Lee, M. Sheldon, and D. H. Son, *Nano Lett.* **16**, 7376 (2016).
24) Y. Y. Pan, Y. H. Su, C. H. Hsu, L. W. Huang, K. P. Dou, and C. C. Kaun, *J. Adv. Nanomater.* **1**, 33 (2016).
25) M. T. Weller, O. J. Weber, J. M. Frost, and A. Walsh, *J. Phys. Chem. Lett.* **6**, 3209 (2015).
26) M. Saliba, T. Matsui, K. Domanski, J.-Y. Seo, A. Ummadisingu, S. M. Zakeeruddin, J. P. C. Baena, W. R. Tress, A. Abate, A. Hagfeldt, and M. Grätzel, *Science* **354**, 206 (2016).
27) Z. Li, M. Yang, J.-S. Park, S.-H. Wei, J. J. Berry, and K. Zhu, *Chem. Mater.* **28**, 284 (2016).
28) L. Pauling, *The Nature of the Chemical Bond* (Cornell University Press, Ithaca, NY, 1960) 3rd ed., p. 514.
29) J. W. Lee, D. J. Seol, A. N. Cho, and N. G. Park, *Adv. Mater.* **26**, 4991 (2014).
30) F. Hao, C. C. Stoumpos, R. P. H. Chang, and M. G. Kanatzidis, *J. Am. Chem. Soc.* **136**, 8094 (2014).
