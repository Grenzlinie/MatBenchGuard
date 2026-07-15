FULL PAPER

# Halogen in materials design: Fluoroammonium lead triiodide
$(FNH_3PbI_3)$ perovskite as a newly discovered dynamical
bandgap semiconductor in 3D

Arpita Varadwaj$^{1,2}$ | Pradeep R. Varadwaj$^{1,2}$ | Koichi Yamashita$^{1,2}$

$^{1}$Department of Chemical System
Engineering, School of Engineering,
The University of Tokyo 7-3-1, Hongo,
Bunkyo-ku 113-8656, Japan
$^{2}$CREST-JST, 7 Gobancho, Chiyoda-ku,
Tokyo 102-0076, Japan

Correspondence
Pradeep R. Varadwaj, Department of
Chemical System Engineering, School of
Engineering, The University of Tokyo 7-3-1,
Hongo, Bunkyo-ku 113-8656, Japan.
Email: pradeep@t.okayama-u.ac.jp,
pradeep@tcl.t.u-tokyo.ac.jp

## Abstract
Methylammonium lead triiodide $(CH_3NH_3PbI_3)$ has been recognized as one of the record-breaking materials for photovoltaics since it can potentially convert light energy into electricity @ 23%. However, it has been suffering from serious stability and environmental issues for which it is not yet put on market. To this end, experimental and theoretical studies are underway to discover versatile halide-based perovskite compounds. In this article, we report the polymorphic geometries, stabilities, band structures, density of states spectra, and carrier effective asses of a newly identified perovskite semiconductor called fluoroammonium lead triiodide $(FNH_3PbI_3)$, obtained using compositional engineering combined with periodic density functional theory electronic structure calculations. We show that this compound is stable both in the orthorhombic and pseudocubic phases. We also show that the bandgap for this material oscillates between 1.62 eV (direct) and 1.79 (indirect) for the two polymorphs examined in the pseudocubic phase, with the former and latter values corresponding to the [111] and [110] orientations of the inorganic cation $FNH_3^+$ inside the perovskite cage, respectively. Contrariwise, it is direct at $\Gamma$-point for the polymorph examined in the orthorhombic phase. The spin orbit coupling is displayed to have profound effect on the nature and magnitude of the bandgap for this material. This, together with the very small effective masses calculated for the charge carriers comparable with those of $CH_3NH_3PbI_3$, allows us to propose that $FNH_3PbI_3$ could be a possible candidate for photovoltaics, as well as for other optoelectronic applications.

## KEYWORDS
bandgap and band structures, DFT calculations, halide perovskite, new functional materials, small effective carrier masses, ultrastrong halogen bonding, ultrastrong hydrogen bonding

---

## 1 | INTRODUCTION

Last decade has witnessed the discovery of extraordinary functional materials for photovoltaics and for other optoelectronic applications.$^{[1-3]}$ Methylammonium lead triiodide $(CH_3NH_3PbI_3/MAPbI_3)$ and its sister associates (e.g., $CH_3NH_3SnI_3$, $HC(NH_2)_2PbI_3$, $C(NH_2)_3PbI_3$, and $CH_3NH_3PbBr_3$, etc.) are a class of such innovative functional materials.$^{[2,3]}$ These belong to the $BMY_3$ perovskite family, which are structurally analogous with $CaTiO_3$, where B is an organic/inorganic species (viz. $CH_3NH_3^+/HC(NH_2)_2^+/C(NH_2)_3^+/Cs^+$), M is the divalent metal cation (viz. $Pb^{2+}/Sn^{2+}/Ge^{2+}$), and Y the halogen derivative (viz. $Y=Cl^-$, $Br^-$, $I^-$).$^{[4-6]}$

$CH_3NH_3PbI_3$ has been discovered to be one of the highest light absorbers.$^{[7]}$ Its maximum efficiency to convert light energy into electricity is certified to be 22.7%.$^{[8]}$ Despite its record-breaking performance,$^{[3,9,10]}$ this material is shown to be highly sensitive to heat, light, oxygen, water, and applied electric field, among many other things.$^{[11,12]}$ Each of these has been demonstrated to serve as a possible factor for the degradation of the material.$^{[11,12]}$

Many recent studies have routinely carried out extraordinary synthesis and report X-ray diffraction crystal data on halide based perovskites in two- and three-dimensions.$^{[6,13-16]}$ Many of them routinely perform the UV-vis and photoluminescence absorption$^{[16-20]}$ and vibrational spectral

measurements,⁽²¹·²²⁾ among others, to provide information about the (direct/indirect) nature of onset of optical absorption (bandgap), spectral signatures, and stabilities. Another important aspect of some of these studies lies in the understanding of the photocurrent density-voltage (J−V) response that demonstrates its dependence on the voltage scan direction/rate/range, voltage conditioning history, and device configuration.⁽²³·²⁴⁾ It also promotes the understanding of the nature of the hysteresis loop in the J−V curve, facilitating to gain insight into, among others, the transient capacitive current, trapping and detrapping process, ion migration, and ferroelectric polarization, thus a useful tool for determining the power conversion efficiency of any newly discovered perovskite material.⁽²³⁻²⁵⁾ Determinations of exciton binding energies, electron-hole diffusion lengths, defect tolerance, effective carrier masses, and strength of bandgap, as well as an understanding of nature of the band structure, density of states spectra, and the interplay of hydrogen bonding and other noncovalent interactions cover a major part of this area of research, thereby advancing the development of our fundamental understanding of the device chemistry and physics of halide based perovskite materials.⁽²⁶⁻²⁹⁾

Recent studies indicate a boom of scientific interest in the discovery of new single/double perovskites.⁽⁷⁻²⁶⁾ These may or may not comprise the lead content.⁽⁷·¹³⁻¹⁶⁾ These can be either all-inorganic, or a mixture of an organic moiety with an inorganic one (organic-inorganic), or metal-organic hybrids.⁽⁴·⁵·⁷⁾ A critical aspect of some of these perovskites lies in the "direct-to-indirect/indirect-to-direct" nature of their bandgap.⁽³⁰⁻³⁴⁾ The view is not very surprising since this kind of bandgap transition has shown to have a significant impact on fast/slow recombination, as well as that on the extent of power conversion efficiency.⁽³⁵·³⁶⁾ This attribute has explained the extremely long charge-carrier lifetimes and high open-circuit voltages observed for the thin films of CH₃NH₃PbI₃.⁽³⁷·³⁸⁾ Nevertheless, many thought-provoking experiments have eventually lead the synthesis and characterization of most of the newly invented optoelectronic perovskite materials.⁽¹³⁻¹⁶⁾ And, in many of such cases, experimental findings were certified by the routine results of first-principles calculations.⁽¹⁸·¹⁹⁾

In this article, we report the equilibrium geometries and electronic band structures of a newly identified BMY₃ perovskite compound called fluoroammonium lead triiodide (FNH₃PbI₃) using density functional theory electronic structure calculations. The orthorhombic (Pnma space group) and pseudocubic (Pm$\overline{3}$m space group) polymorphs of FNH₃PbI₃ are considered (hereafter, o-FNH₃PbI₃ and c-FNH₃PbI₃, respectively). We show that these are analogous to the corresponding polymorphs reported for the largely studied CH₃NH₃PbI₃ (δ₆-CH₃NH₃PbI₃) solar cell semiconductor, which are geometrically feasible in low (< 160 K) and high (> 327 K) temperatures, respectively.⁽³⁰·³¹·³⁹⁾ In addition, the electronic density of states (DOS) spectra are examined to provide insight into the nature of various orbital characters that have participated to build the valence and conduction bands of FNH₃PbI₃. An important property called carrier mass is also examined to show whether the effective mass of the electrons is competitive with that of the holes for the material, an attribute that might be useful to infer the ambipolar nature of the charge transport.⁽³²⁻³⁶⁾ The standard relationship, $m^*=\hbar^2\left[\frac{\partial^2\varepsilon(k)}{\partial^2k}\right]^{-1}$, often invoked in solid state semiconductor physics was used to evaluate the effective masses of the charge carriers, where $m^*$ is the effective mass of the charge carrier (hole/electron), $k$ is the wavenumber, and $\varepsilon(k)$ is the valence/conduction band energy in $k$-space given by: $\varepsilon(k)=\varepsilon_0\pm\frac{\hbar^2k^2}{2m^*}$.

## 2 | COMPUTATIONAL DETAILS, RESULTS, AND DISCUSSION

Figure 1 presents energy-minimized unit-cell geometries of FNH₃PbI₃ in the cubic and orthorhombic phases. The B-site cation is oriented along the [110] and [111] directions in the two polymorphs of the cubic phase. The standard Perdew-Burke-Ernzerhof (PBE) density functional⁽⁴⁰⁾a,b and the Projector Augmented Wave (PAW) method⁽⁴⁰⁾c,d were employed. A plane wave basis set energy cut-off of 520 eV, a threshold of 0.0002 eV/Å for convergence of force, and a Γ-centered $12\times12\times12$ k-point mesh for sampling the Brillouin-zone were employed to energy-minimize the two polymorphs in the cubic phase. However, for the orthorhombic polymorph, a Γ-centered $10\times8\times10$ k-point mesh for sampling the Brillouin-zone was employed, keeping all other parameters unchanged. The VASP package was employed for this purpose.⁽⁴⁰⁾e

### 2.1 | Geometric and polymorphic stabilities

FNH₃PbI₃ shown in Figure 1 possesses perovskite structure. One of the minimum requirements to verify this lies in the fulfillment of the "charge neutrality" condition.⁽³⁵⁾ Per se, FNH₃PbI₃ is the consequence of an electrical marriage between two inorganic moieties, the fluoroammonium cation ($\text{FNH}_3^+$) and the lead triiodide anion ($\text{PbI}_3^-$), showing the oxidation state of the B- and M-site cations balances those of the three metal coordinated halide anions Y.

The most important requirement to validate whether a given BMY₃ geometry does have the CaTiO₃ type perovskite stoichiometry lies in the satisfaction of two geometry based constraints. One of these is the Goldschmidt tolerance factor $t\left(t=\frac{r_B+r_Y}{\sqrt{2}(r_M+r_Y)}\right),^{[37]}$ and the other is the octahedral factor, $t_\mu(t_\mu=\frac{r_M}{r_Y}),^{[38,41,42]}$ where $r_B$ is the effective radius of the B-site cation, $r_M$ is the effective radius of the M-site cation, and $r_Y$ is the effective radius of the Y-site anion.⁽³⁸·⁴¹·⁴²⁾ For most of the known BMY₃ perovskites, $t$ covers the range 0.75-1.00 and $t_\mu$ covers the range 0.442-0.895. Since the reported radius of $\text{Pb}^{2+}$ is about 1.19 Å, and that of $\text{I}^-$ is about 2.20 Å,⁽⁴³⁾ these lead $t_\mu(t_\mu=\frac{r_{M^{2+}}}{r_{Y^-}})$ equals 0.54. In contrary, the ionic radius of the $\text{FNH}_3^+$ molecular ion is calculated in this study to be 1.80 Å. This value is consistent with the range of radii 1.60-2.50 Å recommended for B-site cations, suitable for the formation of BMY₃ perovskites.⁽³⁸·⁴¹·⁴²⁾ For instance, the ionic radius of $\text{CH}_3\text{NH}_3^+$ is suggested to vary between 1.80 Å and 2.50 Å.⁽⁴³·⁴⁴⁾ Park has used an ionic radius is 1.8 Å and has estimated the value of $t$ to be 0.83 for CH₃NH₃PbI₃, showing marginal deviation

![](./images/813048289984249856_1.jpg)

FIGURE 1 (Top) Polyhedral models of fully relaxed unit-cell geometries of FNH₃PbI₃ for the two orientations of the [FNH₃]⁺ inorganic cation inside the inorganic perovskite cage: A, [110] and B, [111]. Lattice constants (a, b, and c in Å; α, β, and γ in °) and cell volumes are shown for each case. C, The ball-and-stick model of the 2 × 2 × 2 supercell geometry of o-FNH₃PbI₃. D, Polyhedral form of o-FNH₃PbI₃. Atom labeling is shown in (B)

from an ideal cubic structure.⁽⁴³⁾ The same values of 0.54 and 0.83 for $t_{\mu}$and $t$ are applicable to FNH₃PbI₃. This is because the B-site cation has a molecular ionic radius comparable with that of CH₃NH₃⁺.

Figure 1 includes the optimized lattice constants and cell volumes for the unit cell geometries of FNH₃PbI₃ in the orthorhombic and cubic phases. As can be readily seen, the geometry of FNH₃PbI₃ is significantly distorted when the B-site cation is aligned along the [110] direction (Figure 1A), and is marginally distorted when it is aligned along the [111] direction (Figure 1B); both of them compared to the ideal $Pm\overline{3}m$ cubic symmetry. The extent of this deviation can be inferred from the lattice constants, in which, for the former polymorph, $a \neq b \neq c$ and $\alpha \neq \beta \approx \gamma$, and for the latter polymorph, $a = b = c = 6.452$ Å and $\alpha = \beta = \gamma = 89.4^\circ$ (for the ideal $Pm\overline{3}m$ cubic symmetry $a = b = c$ and $\alpha = \beta = \gamma = 90.0^\circ$). For comparison, the lattice constants for c-CH₃NH₃PbI₃ [111] calculated with the same level of theory are such that $a \approx b \approx c \approx 6.459$ Å and $\alpha \approx \beta \approx \gamma \approx 89.5^\circ$ (for experimental values see Refs. [14,30,31,39]). Clearly, the nature of the geometrical distortion listed in (B) for c-FNH₃PbI₃ [111] is matching reasonably well with that of c-CH₃NH₃PbI₃ [111], thus, conforming further the perovskite stoichiometry of c-FNH₃PbI₃. Figures S1 and S2 of Supporting Information illustrate relaxed views of polymorphs (A) and (B) of Figure 1 in 3D, respectively.

The lattice constants for o-FNH₃PbI₃ (see Figure 1C) are in line with what can be expected of the Pnma space group, with $a \neq b \neq c$ and $\alpha = \beta = \gamma = 90.0^\circ$ (orthorhombic). The $\angle$Pb—I—Pb angles in it are deviated largely from the ideal value of $180.0^\circ$. For instance, the deviation of this angle from linearity is $35.9^\circ$ along $a$- and $c$-axes, and is $17.2^\circ$ along $b$-axis. This indicates a particular pattern of rotations of the $PbI_6^{4-}$ octahedra, in which, the rotation is either in-phase or antiphase around the three I—Pb—I axes. This is coupled with the tilting of the $PbI_6^{4-}$ octahedra in o-FNH₃PbI₃, which can be described by $a^-b^+a^-$ in Glazer notation, where $a$ and $b$ are the mutually perpendicular crystallographic axes.⁽⁴⁵⁻⁴⁷⁾

![](./images/813048289984249856_2.jpg)

FIGURE 2 Comparison of the $2 \times 2 \times 2$ supercell polymorphic geometries of c-FNH₃PbI₃, illustrating the orientational topologies A, [110] and B, [111] of the $[FNH_3]^+$ inorganic cation inside the inorganic perovskite cage. Shown in (C-G) are a few selected most important local topologies of intermolecular bonding synthons responsible for the design polymorphs (A) and (B) of c-FNH₃PbI₃. Intermolecular-distances and -angles are given in Å and deg, respectively. The basis set superposition error corrected binding energies, $\Delta E$(BSSE), estimated for the molecular blocks of FNH₃PbI₃ are listed from $-135.90$ to $-64.98$ kcal mol⁻¹ (from $-5.893$ to $-2.818$ eV), obtained with PBE/DZP, in which cases, the local geometries used for single points were extracted from the $2 \times 2 \times 2$ supercell geometries illustrated in A, B. Table 1 provides a comparison of the binding energies obtained using the DZP and Def2-TZVPPD basis sets

The nature of the octahedral tilting noted above for o-FNH₃PbI₃ is in decent agreement with that was reported experimentally for o-CH₃NH₃PbI₃. For instance, Weller et al. $^{[30]}$ have reported the deviation of the $PbI_6^{4-}$ octahedra in o-CH₃NH₃PbI₃ to be $29.25^{\circ}$ along $a$- and $c$-axes, and that by $18.06^{\circ}$ along $b$-axis; both compared to the ideal value of $180.0^{\circ}$. This comparison demonstrates that octahedral tilting is by far more significant in o-FNH₃PbI₃ relative to o-CH₃NH₃PbI₃.

The polymorph (A) in Figure 1 is energetically favorable over (B) for c-FNH₃PbI₃, with a relative energy difference of 0.022 eV. This is consistent with that found for the MAPbI₃ system, in which case, the relative energy difference between the two polymorphs is estimated to be 0.011 eV (with the same level of theory).

### 2.2 | Halogen centered hydrogen bonding and its importance in the design of halide perovskites

One of the crucial features in the design of hybrid perovskite compounds lies in the understanding of the nature of intermolecular interactions. These play a vital role not only in determining the overall geometry $^{[4,5]}$ but also for the emergence of desirable materials properties such as small carrier masses and others. $^{[48,49]}$ We have identified a variety of intermolecular noncovalently bonded synthons that cooperate each other to stabilize the studied polymorphs of FNH₃PbI₃. These are illustrated in (C-G) in Figure 2. These are obtained by deleting the nearest Pb and I atoms around each $FNH_3^+ \bullet\bullet\bullet I_3Pb$ fragment contained in the polymorphs illustrated in (A) and (B). For instance, the $FNH_3^+ \bullet\bullet\bullet I_3Pb$ complex geometry depicted in (C) is constructed from the periodic relaxed geometry (B) by keeping the $FNH_3^+ \bullet\bullet\bullet I_3Pb$ motif and deleting the adjacent atoms around it in the cuboctahedron. This molecular block conceives three equivalent $I\bullet\bullet\bullet H(-N)$ hydrogen bonds with $r(I\bullet\bullet\bullet H) \approx 2.511$ Å, and was used for the evaluation of uncorrected and basis set superposition error corrected binding energies ($\Delta E$ and $\Delta E$(BSSE), respectively) with PBE/DZP, where DZP is an all-electron correlated double-$\zeta$ basis set retrieved from the EMSL basis set exchange library; $^{[50]}$ the latter two properties were evaluated using relationships given in Table 1. The $\Delta E$(BSSE) for the most stable binary complex is calculated to be $-135.90$ kcal mol⁻¹ ($-5.893$ eV). Similarly, for the next four molecular blocks (D-F), the $\Delta E$(BSSE) varies between $-124.80$ and $-97.91$ kcal mol⁻¹ ($-5.412$ and $-4.246$ eV). Clearly, the magnitudes of $\Delta E$(BSSE) estimated with the small DZP basis set are both qualitatively and quantitatively consistent with those evaluated with a relatively larger pseudopotential basis set def2-TZVPPD (see $\Delta$ values in Table 1), where def2-TZVPPD is triple-zeta valence basis set that includes two sets of polarization and diffuse basis functions, and is obtained from the EMSL basis set exchange library. $^{[50]}$ These results demonstrate that the molecular

<table><caption>TABLE 1 Comparison of uncorrected and basis set superposition error corrected binding energies (ΔE and ΔE(BSSE), respectively) for the molecular blocks of FNH₃PbI₃, obtained with PBE in conjunction with the Def2-TZVPPD and DZP basis setsᵃᵇ</caption><thead><tr><th rowspan="2">FNH₃PbI₃ blocks</th><th colspan="2">Def2-TZVPPD</th><th colspan="2">DZP</th><th rowspan="2">Δᵉ</th></tr><tr><th>ΔEᶜ</th><th>ΔE(BSSE)ᵈ</th><th>ΔEᶜ</th><th>ΔE(BSSE)ᵈ</th></tr></thead><tbody><tr><td>Figure 2C</td><td>−129.94</td><td>−129.81</td><td>−141.25</td><td>−135.9</td><td>6.09</td></tr><tr><td>Figure 2D</td><td>−121.15</td><td>−121.03</td><td>−128.86</td><td>−124.8</td><td>3.77</td></tr><tr><td>Figure 2E</td><td>−99.34</td><td>−99.28</td><td>−103.37</td><td>−100.61</td><td>1.33</td></tr><tr><td>Figure 2F</td><td>−96.55</td><td>−96.49</td><td>−100.38</td><td>−97.91</td><td>1.42</td></tr><tr><td>Figure 2G</td><td>---ᶠ</td><td>---ᶠ</td><td>−65.13</td><td>−64.98</td><td>---</td></tr></tbody><tfoot><tr><td colspan="6">ᵃSee Figure 2 for molecular blocks. Each of these blocks is constructed from the relaxed geometries shown in (A) and (B) by deleting the neighboring Pb and I atoms (see text for description).<br>ᵇValues in kcal mol⁻¹.<br>ᶜΔE = E_T(FNH₃PbI₃) − E_T(FNH₃⁺) − E_T(PbI₃⁻), where E_T is the electronic total energy of individual species.<br>ᵈΔE (BSSE)=E_T(FNH₃PbI₃)−E_T(FNH₃⁺)−E_T(PbI₃⁻)+E(BSSE), where E(BSSE) is basis set superposition error energy.<br>ᵉΔ = ΔE(BSSE)ᴰᵉᶠ²⁻ᵀᶻᵛᴾᴾᴰ − ΔE(BSSE)ᴰᶻᴾ.<br>ᶠGaussian 09⁵¹ has caused spurious convergence failure problem with the Def2-TZVPPD basis set for this geometry even after 128 cycles.</td></tr></tfoot></table>

blocks with shortest intermolecular contact distances are accompanied with strongest energy of interaction between the B- and Y-site ions. The energy strengths for these noncovalent interactions are in line with those discussed previously for analogous perovskite systems.⁴ˡ⁵

The intermolecular synthons in the molecular block illustrated in Figure 2G) are viable in the pseudocubic geometry in Figure 2B) for c-FNH₃PbI₃ [111]. The intermolecular distance of the F end of FNH₃⁺ fragment to each of the three I atoms of the PbI₃⁻ fragment is 4.654 Å, showing a very long distance of separation. This distance is also very large compared to the sum of the van der Waals radii of the F (1.46 Å) and I atoms (2.04 Å), which is 3.50 Å.⁵² This may mean that the long I∙∙∙F(−N) distance might not be characterized as a consequence of any noncovalent interaction. However, our binding energy calculation suggests that the ΔE(BSSE) for this binary complex to be −64.98 kcal mol⁻¹ (−2.818 eV), which is much more (~260 times) greater than an ordinary van der Waals interaction (−0.25 kcal mol⁻¹).⁵ This suggests that the I∙∙∙F−N intermolecular interactions, albeit long-ranged, might not be unrealistic. These can be regarded as fluorine-centered halogen bonding interactions.⁵³ All these intermolecular interactions are supposedly responsible for the marginal distortion of the PbI₆⁴⁻ octahedra in c-FNH₃PbI₃ (Figure 1B).

o-MAPbI₃ has been identified as the lowest energy structure in the low temperature phase. It maintains its low-temperature stability up to 165 K.¹⁴ˡ³⁰ˡ³¹ˡ⁵⁴ There is a particular orientation of the organic cation (fully ordered) in this geometry, in which, the center of its mass lies near at the close vicinity of the center of the cuboctahedron perovskite cage.³⁰ This has shown to be the consequence of a particular pattern of very strong hydrogen bonding interactions between the H atoms of the ammonium fragment of the CH₃NH₃⁺ cation and the cage iodides.³⁰ˡ⁴⁸ˡ⁴⁹ Interestingly, an exactly similar feature is also evident of the geometry of the o-FNH₃PbI₃ system in the orthorhombic phase. This is illustrated in Figure 3. As such, there are two equivalent I∙∙∙H(−N) hydrogen bonds that are shorter and the remaining one is longer, values 2.463 versus 2.497 Å. All these bonds are directional, with ∠ I∙∙∙H(−N) ≈ 168°. While these interactions are collectively responsible for the eventual stabilization of o-FNH₃PbI₃, there is no straightforward way to quantify the strength of individual intermolecular interactions in the various polymorphs examined. This is because these interactions are all embedded. To provide some insight into this, we have split the individual interaction part of the orthorhombic geometry into an isolated fragment. (A-C) of Figure 3 (bottom) shows three such possibilities. Similarly as discussed in Figure 2 for c-FNH₃PbI₃ [111], PBE/Def2-TZVPPD level single points were performed on each of these three clustered binary geometries to calculate the ΔE and ΔE(BSSE) values. The strength of each of the two equivalent I∙∙∙H(−N) hydrogen bonding interactions marked by a in o-FNH₃PbI₃ is calculated to be very large, with ΔE/ΔE(BSSE) ≈ −109.20 kcal mol⁻¹ (−4.737 eV). The stability of the binary complex (B) containing the noncovalent interaction motif b is about 4.0 kcal mol⁻¹ less stable than that of configuration (A). The preferential stability of conformation (A) over that of (B) is consistent with the relative difference in the intermolecular hydrogen bonded distances.

The I∙∙∙F(−N) contact distance in o-FNH₃PbI₃ is 3.541 Å. This is marginally larger than the sum of the van der Waals radii of the F(1.46 Å) and I atoms (2.04 Å),⁵² which is 3.50 Å. Based on “less than the sum of the van der Waals radii” criterion of IUPAC,⁵⁵ the I∙∙∙F(−N) contact might not represent any noncovalent interaction. However, similarly as discussed above for c-FNH₃PbI₃ [111], our calculation suggests that the I∙∙∙F(−N) interaction is competitive with the I∙∙∙H(−N) hydrogen bonds. This might be understandable since the binding energy for this binary complex in (C) is evaluated to be as large as −79.42 kcal mol⁻¹ (−3.444 eV). Note that noncovalent binding energies similar strengths have been reported elsewhere.⁴ˡ⁵

The 0.001 au isodensity mapped electrostatic surface along the outermost extension of the N−F covalent bond in [FNH₃]⁺ is positive. Since this positive region on F is engaged attractively with the negative I atoms of the perovskite cage, the I∙∙∙F(−N) interaction thus can be regarded as a halogen bond.⁵³ The directionality for this interaction is competitive with those of the I∙∙∙H(−N) hydrogen bonds mentioned above, viz. ∠ I∙∙∙F(−N) = 166.2° and ∠ I∙∙∙H(−N) = 167.2°.

![](./images/813048289984249856_3.jpg)

FIGURE 3 (Top) Illustration of short intermolecular contacts between the host and guest species in o-FNH₃PbI₃. The local topologies of intermolecular bonding synthons marked as A-C (top) are separately illustrated in molecular blocks A-C (bottom), which are responsible for the design of o-FNH₃PbI₃. Intermolecular-distances and -angles are given in Å and deg, respectively. The uncorrected and basis set superposition error corrected binding energies (ΔE and ΔE(BSSE), respectively) estimated for the three molecular blocks of o-FNH₃PbI₃ are listed in the range between −109.0 and −79.0 kcal mol⁻¹ (−4.727 and −3.426 eV). Each molecular block A-C is constructed from the relaxed geometry of o-MAPbI₃ (top) by deleting the neighboring Pb and I atoms (see text for details). The PBE/Def2-TZVPPD method was used for the calculation of ΔE and ΔE(BSSE). Atom labeling is shown in (A)

It is worth stressing that $I\bullet\bullet\bullet F(—N)$ noted above is the not just the only interaction in o-FNH₃PbI₃, there are actually several of them that are formed of the positive outer surface of the fluorine of the B-site cation with the nearest coordinated iodides of the perovskite cage. This insight is gained from the predicted bond critical point and bond path topologies of the charge density, gleaned using quantum theory of atoms in molecules analysis.[⁵⁶] Similarly, whereas there are three potentially strong hydrogen bonds (two short that are equivalent and the other the longer) formed by the —NH₃ group of the $[FNH_3]^+$ cation in o-FNH₃PbI₃, one should not conclude that these are just the interactions that are responsible for the tilting of the $PbI_6^{4-}$ octahedra. This is because there are several other coupled interactions (not shown) that are jointly involved to provide overall geometrical and energetical stability to the resulting perovskite architecture. These suggest that the tilting of the $PbI_6^{4-}$ octahedra observed in o-FNH₃PbI₃ is a result of the competitive network of very strong hydrogen and halogen bonding interactions, essentially required for the design of novel functional optoelectronic materials.

Table 2 summarizes the bandgap values ($E_g$) for the various polymorphs of FNH₃PbI₃, and Figure 4 illustrates the electronic band structures. The bandgap is calculated as the difference between the energies of the conduction band minimum (CBM) and valence bond maximum (VBM). Its

<table>
<caption>TABLE 2 Comparison of without and with-SOC estimated PBE bandgaps $E_g$ (in eV) for FNH₃PbI₃</caption>
<thead>
<tr>
<th>System</th>
<th>Directionᵃ</th>
<th>$E_g$(non-SOC)</th>
<th>Nature (non-SOC)</th>
<th>$E_g$(SOC)</th>
<th>Nature (SOC)</th>
</tr>
</thead>
<tbody>
<tr>
<td>c-FNH₃PbI₃</td>
<td>[111]</td>
<td>1.62</td>
<td>Direct</td>
<td>0.60</td>
<td>Direct</td>
</tr>
<tr>
<td>c-FNH₃PbI₃</td>
<td>[110]</td>
<td>1.79</td>
<td>Indirect</td>
<td>0.76</td>
<td>Indirect</td>
</tr>
<tr>
<td>o-FNH₃PbI₃</td>
<td>---</td>
<td>1.84</td>
<td>Direct</td>
<td>0.94</td>
<td>Direct</td>
</tr>
<tr>
<td>c-MAPbI₃</td>
<td>[111]</td>
<td>1.58ᵇ,ᶜ</td>
<td>Direct</td>
<td>0.47</td>
<td>Direct</td>
</tr>
<tr>
<td>c-MAPbI₃</td>
<td>[110]</td>
<td>1.66</td>
<td>Direct</td>
<td>0.64</td>
<td>Indirect</td>
</tr>
<tr>
<td>o-MAPbI₃</td>
<td>---</td>
<td>1.78</td>
<td>Direct</td>
<td>0.77</td>
<td>Direct</td>
</tr>
</tbody>
</table>

The corresponding bandgaps for MAPbI₃ are also listed for comparison (Γ-centered 12 × 12 × 12 k-point mesh used).
ᵃAlignment of the B-site cation in the BMI₃ perovskite cage, where B = $FNH_3^+$ and $CH_3NH_3^+$.
ᵇExperimentally reported bandgap values were about 1.65 ($T \approx 4.2$ K, orthorhombic), 1.61 ($T \approx 160$ K, tetragonal), and 1.69 ($T \approx 330$ K, pseudocubic).[⁵⁷]
ᶜTheoretically reported values: 1.81 (orthorhombic), 1.67 (tetragonal), 1.16 /1.28 (pseudocubic).[⁵⁷]

![](./images/813048289984249856_4.jpg)

FIGURE 4 The without- and with-SOC influenced electronic band structures of $FNH_{3}PbI_{3}$ in the pseudocubic phase, with the $[FNH_{3}]^{+}$ cation oriented along (A) [110] and (B) [111] directions. Shown in (C) are the corresponding band structures of $FNH_{3}PbI_{3}$ in the orthorhombic phase. For the former two cases, the geometry of the overall system is appreciably and partially distorted, respectively, which is caused by the B-site cation, and hence each of these may not be described by the ideal $Pm\overline{3}m$ cubic space group symmetry. Rather, each can formally be described by the $P1$ space group. The labels of the special points of the $Pm\overline{3}m$ space group are used for the plot of band structure in the pseudocubic phase. The relativistic Rashba-Dresselhaus splitting of the conduction and valence band at the band edges occurs for both the orientations of the $[FNH_{3}]^{+}$ cation in the pseudocubic phase, but is significantly prominent when the cation is oriented along [110] direction. This is perhaps reasonable because the polymorph with this orientation of the B-site cation is significantly more geometrically distorted. In contrary, the SOC has no influence on the character of the bandgap for $o-FNH_{3}PbI_{3}$, as well as on the splitting of either the valence or the conduction band edge, even though the energy gap is significantly down-shifted

value is 1.84 eV for $o-FNH_{3}PbI_{3}$, and is direct at $\Gamma(k = 0, 0, 0)$-point. For $c-FNH_{3}PbI_{3}$, its value is 1.62 eV for the [111] orientation of the $[FNH_{3}]^{+}$ cation, and is direct at the high symmetry R-point in $k$-space. And, changing the orientation of the $[FNH_{3}]^{+}$ cation along the [110] direction, the value of the $E_{g}$ slightly increases, viz. it becomes 1.79 eV, and is indirect in the close vicinity of the R-point. This gives some indication about the dynamical nature of the bandgap since its nature and magnitude are controlled by the orientation of the B-site cation inside the $BMY_{3}$ perovskite cage. An analogous result is also obtained for $c-CH_{3}NH_{3}PbI_{3}$ (Table 2). These are in agreement with the results of similar other studies reported for $c-CH_{3}NH_{3}PbI_{3}.^{[58,59]}$

![](./images/813048289984249856_5.jpg)

FIGURE 5 The electronic density of states spectra for $FNH_3PbI_3$, with the B-site cation oriented along the [111] direction, obtained with
PBE level of theory

<table>
<thead>
<tr>
<th>Species</th>
<th>Direction</th>
<th>Property</th>
<th>Without-SOC</th>
<th>With SOC</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">c-$FNH_3PbI_3$</td>
<td rowspan="2">[110]</td>
<td>$m_{h}^{\ast}$</td>
<td>0.50</td>
<td>0.33</td>
</tr>
<tr>
<td>$m_{e}^{\ast}$</td>
<td>0.60</td>
<td>0.17</td>
</tr>
<tr>
<td rowspan="2">c-$FNH_3PbI_3$</td>
<td rowspan="2">[111]</td>
<td>$m_{h}^{\ast}$</td>
<td>0.25</td>
<td>0.18</td>
</tr>
<tr>
<td>$m_{e}^{\ast}$</td>
<td>0.43</td>
<td>0.13</td>
</tr>
<tr>
<td rowspan="2">o-$FNH_3PbI_3$</td>
<td rowspan="2">---</td>
<td>$m_{h}^{\ast}$</td>
<td>0.37</td>
<td>0.33</td>
</tr>
<tr>
<td>$m_{e}^{\ast}$</td>
<td>0.32</td>
<td>0.24</td>
</tr>
</tbody>
</table>

$^{a}$Values are in $m_0$ (where $m_0$ is the rest mass of a free electron).

A number of recent studies indicate that spin-orbit coupling (SOC) can split the doubly spin-degenerate valence and conduction band edges in noncentrosymmetric compounds.$^{[58,59]}$ As expected, and for the pseudocubic polymorphs such as those in (A) and (B) of Figure 1, the inversion symmetry is broken due to the displacements of the Pb atom from the center of the $PbI_{6}^{4-}$ octahedra. Because of this, the spin-degenerate parabolic edge corresponding to the conduction/valence band is split into two spin-polarized bands that are shifted with respect to each other in k-space. This is connected with Rashba band splitting and has a strong dependence on $Z^{2}$, where Z is the atomic number.$^{[58]}$ A result of this is that the electron (and/or hole) dispersion relationship can now be described by the relationship given by: $\varepsilon_{\pm}(k)=\frac{\hbar^{2}k^{2}}{2m^{\ast}}\pm\alpha_{R}|k|$, where $\alpha_{R}$ is the Rashba splitting parameter.

Our calculation gave a band splitting energy of 64.7 meV for polymorph (A) of c-$FNH_3PbI_3$ (Figure 1). This is calculated by subtracting the energy of the shifted minimum on the conduction band from the minimum of the same band at the high symmetry R-point, in which, the shifted band minimum is located at $k_0 = 0.052$ $\AA^{-1}$. This result is consistent with most of the previous studies that have shown that the band splitting occurs at the conduction band edge for Pb-based compounds.$^{[60]}$ However, as shown in Figure 4A), the valence band edge also splits into two spin-

polarized bands. The VBM is shifted from the maximum on the high symmetry R-point by $0.035\ \text{Å}^{-1}$, and in this case, the band splitting energy is about 17 meV. This shows that splitting of the VB edge is comparatively less pronounced compared to that found for the conduction band edge.

A SOC-assisted splitting of both the valence and conduction band edges is also observed for $\text{c-FNH}_3\text{PbI}_3$ when the orientation of the $\text{FNH}_3^+$ cation was along the [111] direction. However, the splitting is very marginal compared to those found above for the [110] orientation of the cation in $\text{c-FNH}_3\text{PbI}_3$. This is apparently due to minimal distortion of the local geometry of polymorph (B) compared to that of (A) (Figure 1). Nevertheless, both the valence and conduction band extrema for this case are shifted from the high symmetry R point by $0.017\ \text{Å}^{-1}$ due to SOC. The band splitting energies associated with the valence and conduction bands are about 2.96 and 13.28 meV, respectively. Even though either of the bands splits at the edge and the bandgap reduces due to SOC, the nature of the gap between the VBM and CBM is found to be unaltered, meaning that it is always "direct" at R-point for $\text{c-FNH}_3\text{PbI}_3$ [111] (Figure 4B), which might be a necessary requirement better for device application. $^{[17]}$

From the band structure shown in Figure 4C for $\text{o-FNH}_3\text{PbI}_3$, one can conclude that there is no splitting for either the valence or the conduction band edge. This can be immediately understood since there is no inversion symmetry breaking in orthorhombic polymorph, even though unusually strong hydrogen bonding interactions play a predominant role in assembling the host and guest species together to form $\text{o-FNH}_3\text{PbI}_3$. Yet the SOC is found to have a profound effect on the magnitude of the bandgap for this polymorph, thus reducing substantially its value by 1.01 eV. A similar feature is notable of the data listed in Table 2 for $\text{MAPbI}_3$, in agreement with literature. $^{[60]}$

We have calculated using PBE the electronic DOS for $\text{c-FNH}_3\text{PbI}_3$. The results are presented in Figure 5, and in this case, the B-site cation is aligned along [111] direction. These show that the VBM is built mainly from the I p and Pb p (bonding) orbital states, whereas CBM is built using the Pb p (antibonding) orbital states. The contribution of $\text{FNH}_3^+$ s + p antibonding orbital states to the CB of the system is non-negligible. No matter, what is the orientation of the B-site cation inside the perovskite cage, the orbital characters of the VBM and CBM are found to be similar. This can be inferred by comparing the DOS spectra given in Figure 5 with those illustrated in Figure S3 of Supporting Information for the pseudocubic polymorph that conceives the B-site cation aligned with the [110] direction.

For $\text{MAPbI}_3$, the VBM has shown to emerge from mixed Pb (6s) and I (5p) bonding orbital characters. Similarly, the CBM has developed from the antibonding Pb p states. According to Yin et al., $^{[61]}$ even though the CBM comes from p orbitals, a cation Pb p orbital has a much higher energy level than an anion p orbital, as in p-s semiconductors. Therefore, the lower conduction band of $\text{CH}_3\text{NH}_3\text{PbI}_3$ is more dispersive than the upper valence band in p-s semiconductors. Conversely, due to the strong s-p coupling around the VBM, the upper valence band of $\text{CH}_3\text{NH}_3\text{PbI}_3$ is dispersive. The same argument might be applicable to both the valence and conductions bands of $\text{c-FNH}_3\text{PbI}_3$ since of both the bands are predominantly originated from similar orbital states (see Figures 4 and 5).

The canonical definition often used to obtain the effective mass of photo-generated charge carriers in solid state semiconductor materials is related to the curvatures of the conduction and valence bands. The effective mass of the electron associated with the conduction band minimum is given by $m_e^*=\hbar^2\left[\frac{\partial^2 \varepsilon(k)}{\partial^2 k}\right]^{-1}$, whereas that of the hole associated with the valence band maximum is given by $m_h^*=\hbar^2\left[\frac{\partial^2 \varepsilon_v(k)}{\partial^2 k}\right]^{-1}$. Since the energy dispersion curve, $\varepsilon(k)$ versus $k$, is parabolic by nature, the slopes of the lowest and highest parabolic curves accompanied with the CBM and VBM are used to estimate the mean values of the effective masses of the electrons and holes for $\text{FNH}_3\text{PbI}_3$, respectively. The results are listed in Table 3. Regardless of the nature of the orientation of the B-site cation and the polymorphs examined, the effective masses are calculated to be small. The SOC has a non-negligible effect on the carrier masses, in which, its inclusion reduces the magnitude of these masses for all the polymorphs examined. For comparison, Giorgi et al. have reported the mean values of $\frac{m_e^*}{m_0}$ and $\frac{m_h^*}{m_0}$ to be 0.32 and 0.36 for $\text{c-MAPbI}_3$ [111], respectively. $^{[34]}$ Similarly, Umari et al. have reported these masses to be 0.25 and 0.19 with SOC-GW, respectively. Also, with SOC-DFT level, these masses were reported to be 0.28 and 0.17, respectively. $^{[62]}$ These results show that although the magnitudes of the carrier masses are quantitatively perturb by changing the level of theory, the qualitative trend remains unaltered. Because of small masses for electrons and holes, it may be said that this is a useful attribute to infer about the ambipolar nature of the charge carriers in $\text{FNH}_3\text{PbI}_3$.

In summary, this study has presented the equilibrium geometries, energetic stabilities, and important electronic properties of a newly identified perovskite material called $\text{FNH}_3\text{PbI}_3$. The intermolecular hydrogen and halogen bonding interactions responsible for the formation/stability of either of the polymorphs of $\text{FNH}_3\text{PbI}_3$ were shown to be highly competitive. The binding energies associated with these noncovalent interactions were shown to be unusually large. The nature and magnitude of the bandgap were shown to be comparable with that of the high performance semiconductor, $\text{MAPbI}_3$, obtained with the same level of theory. The VBM and CBM for the perovskite material were found to be built predominantly with p-type bonding and antiorbital characters, with contributions coming predominantly from the interacting constituent Pb p and $[\text{FNH}_3]^+$ p and I p for the former and Pb p for latter species involved. The red-shifted bandgaps and small effective masses for the charge carriers were found to be comparable with those of $\text{MAPbI}_3$. These results, together with the dynamical nature of the bandgap, have allowed to propose that $\text{FNH}_3\text{PbI}_3$ could be a possible candidate for photovoltaics since halide-based perovskites such as $\text{SnPbI}_3$, $\text{CsPbI}_3$, and $\text{MAPbI}_3$ possessing similar characteristics have been offered some advantages such as enhanced light absorption and light energy conversion into electricity. The large Rashba splitting observed for both polymorphs of $\text{FNH}_3\text{PbI}_3$ in the pseudocubic phase opens some promise for application in spintronics.

ORCID

Pradeep R. Varadwaj http://orcid.org/0000-0002-7102-3133

### REFERENCES

[1] A. Polman, M. Knight, E. C. Garnett, B. Ehrler, W. C. Sinke, *Science* **2016**, 352, aad4424.

[2] M. A. Green, S. P. Bremner, *Nat. Mater.* **2017**, 16, 23.

[3] M. A. Green, A. Ho-Baillie, *ACS Energy Lett.* **2017**, 2, 822.

[4] a) P. R. Varadwaj, *Helv. Chim. Acta* **2017**, 100, e1700090; b) A. Varadwaj, P. R. Varadwaj, K. Yamashita, *ChemSusChem* **2018**, 11, 449.

[5] A. Varadwaj, P. R. Varadwaj, K. Yamashita, *J. Comput. Chem.* **2017**, 38, 2802.

[6] C. C. Stoumpos, L. Frazer, D. J. Clark, Y. Soo Kim, S. H. Rhim, A. J. Freeman, J. B. Ketterson, J. I. Jang, M. G. Kanatzidis, *J. Am. Chem. Soc.* **2015**, 137, 6804.

[7] M. Grätzel, *Nat. Mater.* **2014**, 13, 838.

[8] National Renewable Energy Laboratory (NREL) Best Research-Cell Efficiency Chart, https://www.nrel.gov/pv/assets/images/efficiency-chart.png (accessed: February 1, 2018)

[9] F. De Angelis, P. Kamat, *ACS Energy Lett.* **2017**, 2, 1674.

[10] L. K. Ono, N.-G. Park, K. Zhu, W. Huang, Y. Qi, *ACS Energy Lett.* **2017**, 2, 1749.

[11] T. A. Berhe, W.-N. Su, C.-H. Chen, C.-J. Pan, J.-H. Cheng, H.-M. Chen, M.-C. Tsai, L.-Y. Chen, A. A. Dubale, B.-J. Hwang, *Energy Environ. Sci.* **2016**, 9, 323.

[12] D. J. Slotcavage, H. I. Karunadasa, M. D. McGehee, *ACS Energy Lett.* **2016**, 1, 1199.

[13] C. C. Stoumpos, D. H. Cao, D. J. Clark, J. Young, J. M. Rondinelli, J. I. Jang, J. T. Hupp, M. G. Kanatzidis, *Chem. Mater.* **2016**, 28, 2852.

[14] C. C. Stoumpos, C. D. Malliakas, M. G. Kanatzidis, *Inorg. Chem.* **2013**, 52, 9019.

[15] F. Hao, C. C. Stoumpos, P. Guo, N. Zhou, T. J. Marks, R. P. H. Chang, M. G. Kanatzidis, *J. Am. Chem. Soc.* **2015**, 137, 11445.

[16] G. Volonakis, M. R. Filip, A. A. Haghighirad, N Sakai, B. Wenger, H. J. Snaith, F. Giustino, *J. Phys. Chem. Lett.* **2016**, 7, 1254.

[17] G. Volonakis, A. A. Haghighirad, R. L. Milot, W. H. Sio, M. R. Filip, B. Wenger, M. B. Johnston, L. M. Herz, H. J. Snaith, F. Giustino, *J. Phys. Chem. Lett.* **2017**, 8, 772.

[18] M. R. Filip, S. Hillman, A. Abbas Haghighirad, H. J. Snaith, F. Giustino, *J. Phys. Chem. Lett.* **2016**, 7, 2579.

[19] A. D. Wright, A. D. Wright, C. Verdi, R. L. Milot, G. E. Eperon, M. A. Pérez-Osorio, H. J. Snaith, F. Giustino, M. B. Johnston, L. M. Herz, *Nat. Commun.* **2016**, 7, 11755.

[20] D. Forgács, D. Pérez-del-Rey, J. Ávila, C. Momblona, L. Gil-Escrig, B. Dänekamp, M. Sessolo, H. J. Bolink, *J. Mater. Chem. A* **2017**, 5, 3203.

[21] M. A. Pérez-Osorio, R. L. Milot, M. R. Filip, J. B. Patel, L. M. Herz, M. B. Johnston, F. Giustino, *J. Phys. Chem. C* **2015**, 119, 25703.

[22] R. G. Niemann, A. G. Kontos, D. Palles, E. I. Kamitsos, A. Kaltzoglou, F. Brivio, P. Falaras, P. J. Cameron, *J. Phys. Chem. C* **2016**, 120, 2509.

[23] B. Chen, M. Yang, S. Priya, K. Zhu, *J. Phys. Chem. Lett.* **2016**, 7, 905.

[24] G. A. Nemnes, C. Besleaga, V. Stancu, D. E. Dogaru, L. N. Leonat, L. Pintilie, K. Torfason, M. Ilkov, A. Manolescu, I. Pintilie, *J. Phys. Chem. C* **2017**, 121, 11207.

[25] D. A. Jacobs, Y. Wu, H. Shen, C. Barugkin, F. J. Beck, T. P. White, K. Webera, K. R. Catchpole, *Phys. Chem. Chem. Phys.* **2017**, 19, 3094.

[26] S. D. Stranks, G. E. Eperon, G. Grancini, C. Menelaou, M. J. P. Alcocer, T. Leijtens, L. M. Herz, A. Petrozza, H. J. Snaith, *Science* **2013**, 342, 341.

[27] A. Miyata, A. Mitioglu, P. Plochocka, O. Portugall, J. T.-W. Wang, S. D. Stranks, H. J. Snaith, R. J. Nicholas, *Nat. Phys.* **2015**, 11, 582.

[28] Z. Yang, Z. Yang, A. Surrente, K. Galkowski, N. Bruyant, D. K. Maude, A. A. Haghighirad, H. J. Snaith, P. Plochocka, R. J. Nicholas, *J. Phys. Chem. Lett.* **2017**, 8, 1851.

[29] L. Q. Phuong, Y. Yamada, M. Nagai, Na. Maruyama, A. Wakamiya, Y. Kanemitsu, *J. Phys. Chem. Lett.* **2016**, 7, 2316.

[30] M. T. Weller, O. J. Weber, P. F. Henry, A. M. Di Pumpo, T. C. Hansen, *Chem. Commun.* **2015**, 51, 4180.

[31] P. S.Whitfield, N. Herron, W. E. Guise, K. Page, Y.Q. Cheng, I. Milas, M. K. Crawford, *Sci. Rep.* **2016**, 6, 35685.

[32] P. Kanhere, S. Chakraborty, C. J. Rupp, R. Ahuja, Z. Chen, *RSC Adv.* **2015**,5, 107497.

[33] S. Chakraborty, W. Xie, N. Mathews, M. Sherburne, R. Ahuja, M. Asta, S. G. Mhaisalkar, *ACS Energy Lett.* **2017**, 2, 837.

[34] G. Giorgi, J.-I. Fujisawa, H. Segawa, K. Yamashita, *J. Phys. Chem. Lett.* **2013**, 4, 4213.

[35] C. H. Hendon, R. X. Yang, L. A. Burton, A. Walsh, *J. Mater. Chem. A* **2015**, 3, 9067.

[36] N. A. Astani, S. Meloni, A. H. Salavati, G. Palermo, M. Grätzel, U. Rothlisberger, *J. Phys. Chem. C* **2017**, 121, 23886.

[37] V. M. Goldschmidt, *Die Naturwissenschaften* **1926**, 21, 477.

[38] M. A. Green, A. Ho-Baillie, H. J. Snaith, *Nat. Photon.* **2014**, 8, 506.

[39] Y. Ren, I. W. H. Oswald, X. Wang, G. T. McCandless, J. Y. Chan, *Cryst. Growth Des.* **2016**, 16, 2945.

[40] a) J. P. Perdew, K. Burke, M. Ernzerhof, *Phys. Rev. Lett.* **1996**, 77, 3865; b) J. P. Perdew, K Burke, M. Ernzerhof, *Phys. Rev. Lett.* **1997**, 78, 1396; c) P.E. Blöchl, *Phys. Rev. B* **1994**, 50, 17953; d) G. Kresse, D. Joubert, *Phys. Rev.* **1999**, 59, 1758; e) VASP, The Vienna Ab Initio Simulation Package, A Plane Wave Electronic Structure Code, https://www.vasp.at/(accessed: November 11, 2017)

[41] C. Li, X. Lu, W. Ding, L. Feng L, Y. Gao, Z. Guo, *Acta Cryst.* **2008**, B64, 702.

[42] G. Kieslich, S. Sun, A. K. Cheetham, *Chem. Sci.* **2015**, 6, 3430.

[43] N.-G., Park, *Materialstoday* **2015**, 18, 65.

[44] R. A. Jishi, AIMS Mater. Sci. 2016, 3, 149.

[45] A. M. Glazer, Acta Cryst. 1972, B28, 3384.

[46] A. M. Glazer, Acta Cryst. 1975, A31, 756.

[47] J. Young, J. M. Rondinelli, J. Phys. Chem. Lett. 2016, 7, 918.

[48] J.-H. Lee, N. C. Bristowe, P. D. Bristowe, A. K. Cheetham, Chem. Commun. 2015, 51, 6434.

[49] J.-H. Lee, N. C. Bristowe, J. H. Lee, S.-H. Lee, P. D. Bristowe, A. K. Cheetham, H. M. Jang, Chem. Mater. 2016, 28, 4259.

[50] EMSL Gaussian basis set exchange library, https://bse.pnl.gov/bse/portal (accessed: September 29, 2017)

[51] M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria, M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone, G. A. Petersson, H. Nakatsuji, X. Li, M. Caricato, A. Marenich, J. Bloino, B. G. Janesko, R. Gomperts, B. Mennucci, H. P. Hratchian, J. V. Ortiz, A. F. Izmaylov, J. L. Sonnenberg, D. Williams-Young, F. Ding, F. Lipparini, F. Egidi, J. Goings, B. Peng, A. Petrone, T. Henderson, D. Ranasinghe, V. G. Zakrzewski, J. Gao, N. Rega, G. Zheng, W. Liang, M. Hada, M. Ehara, K. Toyota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven, K. Throssell, J. A. Montgomery, Jr, J. E. Peralta, F. Ogliaro, M. Bearpark, J. J. Heyd, E. Brothers, K. N. Kudin, V. N. Staroverov, T. Keith, R. Kobayashi, J. Normand, K. Raghavachari, A. Rendell, J. C. Burant, S. S. Iyengar, J. Tomasi, M. Cossi, J. M. Millam, M. Klene, C. Adamo, R. Cammi, J. W. Ochterski, R. L. Martin, K. Morokuma, O. Farkas, J. B. Foresman, D. J. Fox, Gaussian 09, Revision D.01, Gaussian, Inc., Wallingford, CT 2013.

[52] S. Alvarez, Dalton Trans. 2013, 42, 8617.

[53] P. Metrangolo, J. S. Murray, T. Pilati, P. Politzer, G. Resnati, G. Terraneo, Cryst. Growth Des. 2011, 11, 4238.

[54] F. Brivio, J. M. Frost, J. M. Skelton, A. J. Jackson, O. J. Weber, M. T. Weller, A. R. Goni, A. M. A. Leguy, P. R. F. Barnes, A. Walsh, Phys. Rev. 2015, B92, 144308.

[55] G. R. Desiraju, P. S. Ho, L. Kloo, A. C. Legon, R. Marquardt, P. Metrangolo, P. Politzer, G. Resnati, K. Rissanen, Pure Appl. Chem. 2013, 85, 1711.

[56] R.F.W. Bader, Atoms in Molecules: A Quantum Theory, Oxford University Press, Oxford 1990.

[57] C. Quarti, E. Mosconi, J. M. Ball, V. D'Innocenzo, C. Tao, S. Pathak, H. J. Snaith, A. Petrozza, F. De Angelis, Energy Environ. Sci. 2016, 9, 155.

[58] Y. Zhai, S. Baniya, C. Zhang, J. Li, P. Haney, C.-X. Sheng, E. Ehrenfreund, Z. V. Vardeny, Sci Adv. 2017, 3, e1700704.

[59] Y. Zhai, S. Baniya, C. Zhang, J. Li, P. Haney, C.-X. Sheng, E. Ehrenfreund, Z. V. Vardeny, Y. A. Bychkov, E. I. Rashba, J. Phys. C 1984, 17, 6039.

[60] L. D. Whalley, J. M. Frost, Y. -K. Jung, A. Walsh, J. Chem. Phys. 2017, 146, 220901.

[61] W.-J. Yin, J.-H. Yang, J. Kang, Y. Yan, S.-H. We, J. Mater. Chem. A 2015, 3, 8926.

[62] P. Umari, E. Mosconi, F. De Angelis, Sci. Rep. 2014, 4, 4467.

# SUPPORTING INFORMATION
Additional Supporting Information may be found online in the supporting information tab for this article.

How to cite this article: Varadwaj A, Varadwaj PR, Yamashita K. Halogen in materials design: Fluoroammonium lead triiodide ($\text{FNH}_3\text{PbI}_3$) perovskite as a newly discovered dynamical bandgap semiconductor in 3D. Int J Quantum Chem. 2018;e25621. https://doi.org/10.1002/qua.25621