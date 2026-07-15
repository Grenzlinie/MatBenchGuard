# Optimized opto-electronic and mechanical properties of orthorhombic methylamunium lead halides (MAPbX₃) (X = I, Br and Cl) for photovoltaic applications

Mohammed Elmamoun Laamariⁿ, Ali Cheknaneⁿ,*, Ali Benghiaᵇ, Hikmat S. Hilalᶜ

ⁿ Laboratoire des semiconducteurs et matériaux fonctionnels, Université Amar Telidji de Laghouat, Bd des martyrs, BP37G, 03000 Laghouat, Algeria
ᵇ Laboratoire de physique des matériaux, Université Amar Telidji de Laghouat, Bd des martyrs, BP37G, 03000 Laghouat, Algeria
ᶜ SSERL, Department of Chemistry, An-Najah National University, P.O. Box 7, Nablus, West Bank, Palestine

---

## ARTICLE INFO

**Keywords:**
Perovskites
DFT
Optical absorption
Band gap tuning
Stiffness

---

## ABSTRACT

Organometallic halide perovskites (OMHPs) are absorbent materials, and can thus be employed in solar cells with power conversion efficiency (PEC) of 22% or higher. Using calculations, this work confirms earlier experimental findings and determines optimal properties to achieve maximum conversion efficiency for OMHPs. Values of energy band gap, density of states, absorption coefficient, refractive index, dielectric constant and elastic constants of orthorhombic methylamunium lead halides (MAPbX₃) (X = I, Br and Cl) family are all calculated using Density Functional Theory (DFT) method with generalized gradient approximation (GGA). The stiffness of (MAPbX₃) (X = I, Br and Cl) is investigated by calculating Young's moduli E constants. Among the series, MAPbI₃ is the stiffest material with Eₓ = 57.24 GPa. The perovskite family members are characterized by their energy band gap variation as: E₉ ᵐᴬᴾᵇᴵ₃, ᵐᴬᴾᵇᴮʳ₃, ᵐᴬᴾᵇᶜˡ₃ = 1.626, 2.207 and 2.748 eV, respectively. They also exhibit a remarkable absorption coefficient (α ᵐᴬᴾᵇˣ₃ = 10⁵ cm⁻¹) over a wide energy range particularly the visible spectrum [1.65–3.26 eV: 380–750 nm]. The anisotropy of optical properties (MAPbX₃) (X = I, Br) is proven in the near and middle ultraviolet [3.1–5 eV] energy band.

---

## 1. Introduction

Perovskites attract special interest among researchers. Perovskite structure and properties make it possible alternative in many applications. Organometallic halide perovskite (OMHP) based solar cells are being widely considered and known as light absorbers (Ji et al., 2016; Chen et al., 2015). Due to their chemical tunability, OMHP can also be tailored for various optoelectronic devices such as light emitting devices (LEDs), optical sensors (e.g. photodetectors), transistors(Zhao and Zhu, 2016); LASERS, light emitting electrochemical cells (LECs) (Chen et al., 2015) and spintronics (Hsiao et al., 2015). All in all, perovskites find their applications in different technologies, both combined and standalone systems (Yusoff and Nazeeruddin, 2016).

Emergence of OMHP in photovoltaic applications is due to their special absorptivity. OMHP absorbers are thus widely considered to enhance thin film PV cells of the 3rd generation (Kanhere et al., 2015; Ndione et al., 2016). They are among best materials with high power conversion efficiency (PCE). In dye-sensitized solar cells(Zhou et al., 2016), OMHPs have been used in devices with high PCE values (Chen et al., 2015; Hsiao et al., 2015) with high reported values of 22.7% (Qing et al., 2018). Therefore, OMHP systems have the prospect to reach commercial PV applications (Liu et al., 2018). In addition to all such features, OMHP devices can be prepared by simple methods (Quarti et al., 2015). Therefore, OMHP based photovoltaic devices have a prosperous future, and need more study aiming at enhancing their conversion efficiencies.

Methylamunium lead halides (MAPbX₃) (X = I, Br and Cl) form a sub-class of perovskites. They are characterized by excellent optoelectronic features such as high absorption coefficient, tunable energy band gap in the visible range, long range electron-hole transport length, and high carrier mobility (Ndione et al., 2016; Quarti et al., 2015) and (Song et al., 2015). Such features make these compounds good candidates for solar cells with high performance.

Iodine (I) based hybrid perovskites have been extensively studied for high PCE purposes. MAPbX₃ (X = I, Br and Cl) features can be simply monitored by changing the halide ions from one to another (Koliogiorgos et al., 2017). By knowing OMPH parameters, such as shape and band structure, which relate to the effective masses of charge

---

* Corresponding author.
E-mail address: a.cheknane@lagh-univ.dz (A. Cheknane).

https://doi.org/10.1016/j.solener.2019.02.035
Received 1 December 2018; Received in revised form 5 February 2019; Accepted 16 February 2019
0038-092X/ © 2019 Published by Elsevier Ltd on behalf of International Solar Energy Society.

![](./images/812799492062445569_1.jpg)
![](./images/812799492062445569_2.jpg)
![](./images/812799492062445569_3.jpg)

![](./images/812799492062445569_4.jpg)

Fig. 1. Orthorhombic crystal structures for: (a) $MAPbI_3$ (b) $MAPbBr_3$ and (c) $MAPbCl_3$.

carriers and dielectric constants, the device physics can be understood, and techniques to develop their PV devices can be invented (Song et al., 2015).

Perovskites are represented by the general formula $ABX_3$, where A is an inorganic or organic cation, like $CH_3NH_3^+$(MA),$CH_5N_2^+$:FA),…, B is a metal cation ($Pb^{2+}$, $Sn^{2+}$, …), and X is a halide anion ($I^-$, $Br^-$,$Cl^-$, $F^-$). This study is basically focused on $MAPbX_3$ ($X = I^-$, $Br^-$ and $Cl^-$) fundamental properties. The $MAPbX_3$ crystal structure is described in literature. A metal ion $Pb^{2+}$ with six neighbouring halide ions I, Br, or $Cl$ share $[PbI_6]^{4-}$, $[PbBr_6]^{4-}$ or $[PbCl_6]^{4-}$ octahedra, respectively. Furthermore, each organic cation is coordinated by twelve halide anions as shown in Fig. 1 (Chang et al., 2017).

X-ray diffraction patterns show that $MAPbX_3$ ($X = I$, $Br$ and $Cl$), depending on temperature, may have different phases and symmetries. As temperature increases, the structures vary from low temperature orthorhombic to tetragonal, and then to high temperature cubic per-ovskite structures (Chen et al., 2015; Manser et al., 2016). Literature also shows that when temperature increases, the symmetry of the perovskite increases too (Chen et al., 2015). $MAPbX_3$ ($X = I$, $Br$ and $Cl$) is formed at low temperature gradually in an orthorhombic structure $\gamma$ phase (pnma space group) as described in Fig. 1. For instance, such structures occur for $MAPbCl_3$ at $< 172.9$ K, for $MAPbBr_3$ at $< 144.5$ K and for $MAPbI_3$ at $< 162.2$ K) (Liu et al., 2012).

This work aims at quantitatively and qualitatively describing various intrinsic properties of $MAPbX_3$ ($X = I$, $Br$ and $Cl$) as absorbent materials. Quantitative description involves ab-initio DFT based calculation of optimized properties, for the orthorhombic structures of $MAPbX_3$ ($X = I$, $Br$ and $Cl$), such as their electronic band gap structures, density of states, dielectric constant and refraction index as well as their mechanical properties. Such studies have not been performed earlier to our knowledge. Qualitative description involves comparisons with other earlier studies. Finding optimal properties of $MAPbX_3$ that yield solar cells with higher conversion efficiency, and comparing such findings with earlier experimental studies is one main goal of this work. Such comparison has not been made earlier to our knowledge.

## 2. Computational methods

DFT theory based calculation is useful in perovskite characterization. In this study, all calculation results: bulk geometry optimization, electronic, optical and mechanical properties are acquired using plane wave basis- DFT method implemented in the Cambridge Sequential Total Energy Package (CASTEP, v 8.0) code. Ultra-soft pseudo potentials were adopted to describe the electron-ion interaction. The procedure Perdew-Burke-Ernzerhof (PBE) (Perdew et al., 1996) constructs the generalized gradient approximation (GGA) functional DFT to express the exchange - correlation energy.

Fast low energy scanning studies of $MAPbX_3$ ($X = I$, $Br$ and $Cl$) structures were performed and cutoff kinetic energies were 400 eV for ($MAPbI_3$), 450 eV for ($MAPbBr_3$), and 400 eV for ($MAPbCl_3$). After checking convergence criteria, the Monkhorst-Pack of k-point mesh grid were fixed at $7 × 5 × 7$ for ($MAPbI_3$), $8 × 6 × 8$ for ($MAPbBr_3$) and $7 × 7 × 7$ for ($MAPbCl_3$) for sampling Brillouin zone. Energy tolerance of $5 × 10^{-7}$ eV/atom was set to better probe the calculation. The electronic valence states of each atom are: MA: Pb: $5d^{10} 6s^2p^2$, I:$5s^2p^5$, Br:$4s^2p^5$, Cl:$3s^2p^5$, C: $2s^22p^2$, N: $2s^22p^2$, H:$1s^1$.

## 3. Results and discussion

### 3.1. Structural properties

Firstly, to study such $MAPbX_3$ ($X = I$, $Br$ and $Cl$) crystal systems, the equilibrium lattice parameters were calculated using BFGS method for geometry optimization (Pfrommer et al., 1997) implemented in CASTEP. It allows refining a 3D system to obtain more stable and relaxed structure. The obtained lattice parameters ($a × b × c$) and the volume

Table 1
Calculated (DFT) and experimental lattice parameters values of $MAPbX_3$ ($X = I$, Br, Cl).

<table>
<thead>
<tr>
<th>Compound calculated lattice parameters a, b, c (Å), V(Å³)</th>
<th>Experimental value</th>
<th>References</th>
</tr>
</thead>
<tbody>
<tr>
<td>$MAPbI_3$ a = 8.848, b = 12.928, c = 9.136<br>V = 1045.116</td>
<td>a = 8.861, b = 12.62, c = 8.581,<br>V = 959.5</td>
<td>Liu et al. (2012)</td>
</tr>
<tr>
<td>$MAPbBr_3$ a = 7.999, b = 12.009, c = 8.675<br>V = 833.408</td>
<td>a = 7.979, b = 11.845, c = 8.58<br>V = 811.1</td>
<td>Swainson et al. (2003)</td>
</tr>
<tr>
<td>$MAPbCl_3$ a = 11.480, b = 11.610, c = 11.545<br>V = 1538.828</td>
<td>a = 11.193, b = 11.347, c = 11.287<br>V = 1432.5</td>
<td>Chia et al. (2005)</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2 Calculated elastic constants and Young’s modulus of MAPbX₃ (X = I, Br, Cl).</caption>
<thead>
<tr>
<th>Elastic constants (GPa)</th>
<th>MAPbI₃</th>
<th>MAPbBr₃</th>
<th>MAPbCl₃</th>
</tr>
</thead>
<tbody>
<tr>
<td>c₁₁</td>
<td>65.85</td>
<td>26.44</td>
<td>48.80</td>
</tr>
<tr>
<td>c₂₂</td>
<td>29.99</td>
<td>40.21</td>
<td>54.20</td>
</tr>
<tr>
<td>c₃₃</td>
<td>34.01</td>
<td>27.32</td>
<td>52.36</td>
</tr>
<tr>
<td>c₄₄</td>
<td>3.81</td>
<td>7.12</td>
<td>14.39</td>
</tr>
<tr>
<td>c₅₅</td>
<td>18.86</td>
<td>11.62</td>
<td>17.73</td>
</tr>
<tr>
<td>c₆₆</td>
<td>0.61</td>
<td>5.20</td>
<td>14.76</td>
</tr>
<tr>
<td>c₁₂</td>
<td>0.66</td>
<td>10.97</td>
<td>3.68</td>
</tr>
<tr>
<td>c₁₃</td>
<td>16.49</td>
<td>14.27</td>
<td>6.21</td>
</tr>
<tr>
<td>c₂₃</td>
<td>9.79</td>
<td>12.67</td>
<td>3.42</td>
</tr>
<tr>
<td>Young's modulus</td>
<td>57.24</td>
<td>18.43</td>
<td>47.87</td>
</tr>
<tr>
<td>Eₓ, Eᵧ, E_z</td>
<td>26.84</td>
<td>33.33</td>
<td>53.75</td>
</tr>
<tr>
<td>(GPa)</td>
<td>26.79</td>
<td>18.34</td>
<td>51.44</td>
</tr>
</tbody>
</table>

V are summarized in Table 1. The table shows that the calculated lattice parameters of MAPbX₃ (X = I, Br and Cl) by (DFT-GGA) method are consistent with the listed experimental values. These results are thus studied here to add credibility to findings acquired in following sections.

### 3.2. Elastic constants
The stability of perovskite based solar cell is affected by various factors which determine cell degradation, stress and strain (Chen et al., 2018). For example, the design, the fabrication and the industrial processing of OMHP solar cells may affect their mechanical properties (Feng, 2014). Therefore, the anisotropy on the Young's modulus and the elastic constants of MAPbX₃ (X = I, Br, Cl) are intentionally investigated here.

Table 2 summarizes the values of calculated elastic constants and Young's moduli Eₓ, Eᵧ, E_z for MAPbX₃ (X = I, Br, Cl) compounds. After certain mathematical operations, the stability criteria for the used MAPbX₃ (X = I, Br, Cl), with orthorhombic structure, are well satisfied:
$c_{11}+c_{22}-2c_{12}>0,\ c_{11}+c_{33}-2c_{13}>0,\ c_{22}+c_{33}-2c_{23}>0,$
$c_{11}+c_{22}+c_{33}+2c_{12}+2c_{13}+2c_{23}>0,\ c_{11}>0,\ c_{22}>0,$
$c_{33}>0,\ c_{44}>0,\ c_{55}>0,\ c_{66}>0$ (Feng, 2014). The obtained elastic constants are comparable to those reported (Feng, 2014) for both MAPBX₃ (X = I,Br). Moreover, Young's modulus values of MAPbX₃ (X = I, Br and Cl), along x, y and z faces, show the anisotropic stiffness for these materials. MAPbX₃ (X = I, Br) systems exhibit a clear contrast stiffness Eₓ,I = 57.24 GPa and Eᵧ,I = 26.24 GPa, Eₓ,Br = 18.43 GPa and Eᵧ,Br = 33.33 GPa, Eₓ,Cl = 47.87 GPa and Eᵧ,Cl = 53.75 GPa, as observed in the present work. Based on Young's modulus results, the tendency $E_{y,Cl}>E_{y,Br}>E_{y,I}$, confirms earlier literature(Sun et al., 2015).

### 3.3. Electronic properties
#### 3.3.1. Electronic band structure
Since the MAPbX₃ (X = I, Br and Cl) compounds are established at their stable state, their electronic state band gaps are computed and shown in Fig. 2. The Figure shows the electronic band gap structures of MAPbX₃ (X = I, Br and Cl) along high symmetry path directions. The band gap values correspond to $E_g$ = 1.626, 2.207 and 2.748 eV for MAPbX₃ (X = I, Br and Cl), respectively. All MAPbX₃ (X = I, Br and Cl) systems show a semiconductor behavior with direct band gap at Γ point. MAPbX₃ (X = I, Br and Cl) band structures well depict that the band gap values are inversely proportional to their corresponding halogen atomic numbers (₅₃I, ₃₅Br, ₁₇Cl). The present calculated band gap values are also consistent with those reported earlier (Ji et al., 2016; Liu et al., 2012; Cui et al., 2015) and in congruence with experimental values (Quarti et al., 2015).

The present results show that MAPbI₃ is more stable (−12500.3816 eV) than the earlier reported value (−12500.1 eV) (Ji et al., 2016). When performing band gap energy calculation, the result for MAPbI₃ $E_g$ = 1.626 eV is slightly improved with respect to earlier one which showed $E_{gMAPbI3}$ = 1.656 eV value (Ji et al., 2016). Moreover, the energy band gap result for MAPbCl₃ $E_{gMAPbCl3}$ = 2.748 eV is found when performing calculation on the lattice of (a = 11.480, b = 11.610 and c = 11.545 Å) parameters. These parameters were used after screening for literature data. For example, the lattice parameters (a = 5.673, b = 5.628 and c = 11.182 Å) were cited in one earlier report for orthorhombic MAPbCl₃ (Liu et al., 2012); while they were (a = 11.193, b = 11.347, c = 11.287 Å) in another report (Sun et al., 2015). The present study thus gives more accurate values with higher credibility for parameters to be used in future calculations.

Energy diagrams found here show that gradual exchange of iodide with bromide, and then with chloride, in OMHP tunes band gap from 1.62 to 2.2 and to 2.7 eV, respectively. Such tuning, confirmed here opens a new scope for new OMHP applications, as described earlier (Jacobsson et al., 2016).

#### 3.3.2. Density of sates
Fig. 3 shows that all MAPbX₃ (X = I, Br and Cl) compounds have the same energy distribution trend. The study shows that the MA-p state is located at −5 eV, far away from the Fermi level, and has a small effect on the band gap compared to other inorganic ions. The present results confirm the calculated partial density of states (PDOS) values reported earlier (Ye et al., 2015) that show a negligible density of states effect near the band edges. Moreover, MA⁺ cation conserves the electronic equilibrium and stability of the structure. Recent literature shows that the interaction between MA⁺ cation and [PbX₃]⁴⁻ framework influences the orbital band compositions and consequently the crystal geometry (Fan et al., 2015).

The total (TDOS) and partial PDOS values are described in Fig. 3. The conduction band minimum (CBM) is mainly dominated by Pb-6p orbitals and remains unchanged for all compounds. On the other hand, the valence band maximum (VBM) is centered around halide ions p states (I-5p, Br-4p and Cl-3p) mixed with a small amount of Pb-6pPb-s states. Approximately, Pb cation and halide anions (I, Br, Cl) build the band gap energy edges (Mladenovic and Vukmirovic, 2018). No intense overlapping occurs between Pb-6p and (I-5p, Br-4p and Cl-3p) states which means weak Pb-X bonding (Yin et al., 2014).

Fig. 3 shows that the Pb-s and (I-p, Br-p and Cl-p states) are clearly visible at the same position from [−8 to −6 eV]. A hybrid state is clearly pointed between Pb-p and (I-p, Br-p and Cl-p) states over [−4 to 0 eV] energy band at the VBM and over [1.7 to 5 eV] energy band for the CBM as shown in Fig. 3.

#### 3.3.3. Electron charge density and Mullikan population analysis
To probe more intrinsic characteristics of MAPbX₃ (X = I, Br and Cl), further explanations on charge distribution are depicted in Fig. 4.

The MA⁺ cation shows very weak interaction and thus negligible overlap of electron orbitals between the organic component and the inorganic Pb-X octahedral. The behavior is present in all compounds. This feature is supported by the experimental contour plots of electron density for MAPbBr₃ reported earlier (Jishi et al., 2014). Finally, the interactions between Pb ions and X halide ions seem to be dominated by ionic character bonding.

Once such OMHP structure is optimized, assigning partial charges to atoms can be very useful to give an interpretation for charge distribution in compounds. Population analysis methods provide valuable insights into the interactions that give rise to bonding, where Mulliken's analysis is the most common population analysis method.

Electronic charges for atomic Mullikan population of Pb-X bonding are summarized in Table 3. The Table describes the partial charge value for each atom in Pb-X bonding. The more electronegative Cl, Br and I atoms attract electron density away from the less electronegative Pb atoms leaving them positively charged.

![](./images/812799492062445569_5.jpg)

Fig. 2. Electronic band gap structures of (a) MAPbI₃, (b) MAPbBr₃ and (c) MAPbCl₃.

![](./images/812799492062445569_6.jpg)

Fig. 3. Total and partial density of states (TDOS PDOS) of MAPbX₃ (X = I, Br and Cl).

### 3.4. Optical properties

The optical properties of orthorhombic MAPbX₃ (X = I, Br, Cl) can display anisotropy due to their asymmetry. This effect is included in the calculated results by taking the polarization direction of the electro- magnetic field into account.

![](./images/812799492062445569_7.jpg)

Fig. 4. Electron charge density distribution of MAPbX₃ (X = I, Br, Cl) ranging (0-1 e/A³).

#### 3.4.1. Absorption coefficient

The optical absorption coefficients of MAPbX₃ (X = I, Br, Cl) in different polarization directions are depicted in Fig. 5. The Figure shows the higher calculated absorption coefficient values ($\alpha = 10^4$-$10^5$cm⁻¹) for each OMHP in all polarization directions. From the Figure, MAPbI₃, MAPbBr₃ and MAPbCl₃ present the same $\alpha$ trend and remain isotopic in all polarization directions over the visible energy band. MAPbBr₃ and MAPbI₃ exhibit a little anisotropy effect on the

<table>
<caption>Table 3 Calculated Mulliken atomic population values in Pb-X (I, Br and Cl) bonds.</caption>
<thead>
<tr>
<th>Compound</th>
<th>Ion</th>
<th>Atomic Mullikan population</th>
<th>Ion number</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">MAPbI₃</td>
<td>I(1)</td>
<td>−0.47</td>
<td>8</td>
</tr>
<tr>
<td>I(2)</td>
<td>−0.40</td>
<td>4</td>
</tr>
<tr>
<td>Pb</td>
<td>+0.82</td>
<td>4</td>
</tr>
<tr>
<td rowspan="3">MAPbBr₃</td>
<td>Br(1)</td>
<td>−0.47</td>
<td>8</td>
</tr>
<tr>
<td>Br(2)</td>
<td>−0.41</td>
<td>4</td>
</tr>
<tr>
<td>Pb</td>
<td>+0.96</td>
<td>4</td>
</tr>
<tr>
<td rowspan="4">MAPbCl₃</td>
<td>Cl(1)</td>
<td>−0.57</td>
<td>12</td>
</tr>
<tr>
<td>Cl(2)</td>
<td>−0.58</td>
<td>8</td>
</tr>
<tr>
<td>Cl(3)</td>
<td>−0.59</td>
<td>4</td>
</tr>
<tr>
<td>Pb</td>
<td>+1.11</td>
<td>8</td>
</tr>
</tbody>
</table>

absorption peaks (4.5 and 3.5 eV) respectively in the near and middle ultraviolet [3.1-5.0 eV] energy bands with respect to polarization di- rections.

To get more insight into the absorption coefficient of MAPbX₃ (X = I, Br, Cl), a comparative presentation is shown in Fig. 6. The Figure shows that MAPbI₃ exhibits broad and high light absorbance ($\alpha = 10^{4}$ to $10^{5}\ \text{cm}^{-1}$) over the visible spectrum [1.65-3.26 eV: 380-750 nm]. Therefore, MAPbI₃ can is recommended in thin film absorber solar cells, as described earlier (Wolf et al., 2014) This ab- sorption coefficient value is greater than those observed in conventional PV inorganic p-n junction materials such as CuInGaSe₂; CdTe and GaAs (Liu et al., 2012). Fig. 6 also shows that when halogen atomic size decreases (I, Br, Cl), light absorption decreases, accompanied by low- ering of relative number of absorbed photons over the visible spectrum.

### 3.4.2. Dielectric constant
The dielectric constant or relative permittivity is a property that describes the ability of a medium to store electric field during dipole polarization. It is expressed as: $\varepsilon = \varepsilon' - \text{i}\varepsilon''$, where the real part $\varepsilon'$ represents the charge storage ability and the imaginary part $\varepsilon''$ represents the energy loss. Only electronic polarization governs the dielectric process at optical (ultrahigh) frequencies. Fig. 7 shows that MAPbI₃ has $\varepsilon_{\text{opt}}' = 7$, in congruence with literature (Fan et al., 2015). It can thus be concluded that: when halogen atomic size decreases (I, Br, Cl), the electric field storage ability decreases but accompanied with only a minimum energy loss as shown in Fig. 7.

![](./images/812799492062445569_8.jpg)

Fig. 6. Optical absorption coefficient $\alpha$ for MAPbX₃ (X = I, Br, Cl)at (0 0 1) polarization direction.

### 3.4.3. Refractive index
The refractive index values for MAPbX₃ (X = I, Br, Cl) in different polarization directions are shown in Fig. 8. MAPbI₃, MAPbBr₃ or MAPbCl₃ behave in the same way when interacting with the incident electromagnetic field but a sensible anisotropy is present when each of these materials responds to such specific polarization.

For comparison purposes, Fig. 9 shows the refraction index values for MAPbX₃ (X = I, Br, Cl) at (0 0 1) polarization direction. The values vary as $n_{\text{MAPbI3}} > n_{\text{MAPbBr3}} > n_{\text{MAPbCl3}}$ along short wavelengths. The calculated values are comparable with literature (Leguy et al., 2016) for MAPbX₃ (X = I, Br, Cl) in their pseudo cubic phase, in term of the behaviour and effect of the anisotropy on the refractive index and ex- tinction coefficient on MAPbX₃ (X = I, Br, Cl). It should be kept in mind that the present results specifically describe orthorhombic MAPbX₃ (X = I, Br, Cl) materials.

## 4. Conclusion
MAPbX₃ (X = I, Br, Cl) perovskites at their orthorhombic phase are basically described, in the present work, using DFT-GGA method im- plemented in CASTEP. The MAPbX₃ (X = I, Br, Cl) perovskites are ab- sorber materials, so their optoelectronic and mechanical properties are calculated. Firstly, the calculated elastic constant values agree with other earlier literature. Secondly, the anisotropy affects the stiffness of each compound along x, y, z orientations. MAPbI₃ is the stiffest material with $E_{\text{x}} = 57.24\ \text{GPa}$ and the trend; $E_{\text{y,Cl}} = 53.75\ \text{GPa} > E_{\text{y,Br}} = 33.33$

![](./images/812799492062445569_9.jpg)

Fig. 5. Optical absorption coefficients $\alpha$ of MAPbX₃ (X = I, Br, Cl) in different polarization directions.

![](./images/812799492062445569_10.jpg)

Fig. 7. $Re(\varepsilon)$ and $Im(\varepsilon)$ of $MAPbX_3$ (X = I, Br, Cl) at (0 0 1) polarization direction.

![](./images/812799492062445569_11.jpg)

Fig. 8. Refractive index $n$ of $MAPbX_3$ (X = I, Br, Cl) in different polarization directions.

![](./images/812799492062445569_12.jpg)

Fig. 9. Calculated refractive index and extinction coefficients of $MAPbX_3$ (X = I, Br, Cl) at (0 0 1) polarization direction.

$GPa > E_{y,I}=26.84$ GPa is observed.

The results also show that the energy band gap can be tuned (from $E_g = 1.62$ to 2.2 to 2.74 eV) by varying halogen atoms (from X = I to Br to Cl), respectively. Moreover, $MA^+$ has no significant effect on charge distribution in bonds formed strongly between $Pb^{2+}$ and (X = I, Br, Cl) atomic orbitals. The results show that $MAPbI_3$ has a wide band gap and strong absorption coefficient of $10^5$ $cm^{-1}$ in visible range [1.65-3.26 eV: 380-750 nm]. The calculated values state that anisotropy slightly affects the optical properties, particularly for $MAPbX_3$ (X = I, Br) in the near and mid ultraviolet range [3.1-5.0 eV]. Finally, the results show that when atomic number for the halide decreases, the dielectric constant and refractive index values decrease for $MAPbX_3$ (X = I, Br, Cl).

## Acknowledgement

Authors would like to thank "Université Amar Telidji de Laghouat, Algérie" for the financial support.

## References

Chang, J., Chen, H., Yuan, H., Wang, B., Chen, X., 2017. The mixing effect of organic cations on structural, electronic and optical properties of $F_{Ax}M_{A1x}Pb_13$ perovskites. PCCP.

Chen, Q., Marco, N.D., Yang, Y., Song, T.B., Chen, C.C., Zhao, H., Hong, Z., Zhou, H., Yang, Y., 2015. Under the potlight: the organic-inorganic hybrid halide perovskite for optoelectronic applications. Nano Today 10, 355-396.

Chen, A., Youssef, M., Zhang, C., 2018. Strain effect on the performance of amorphous silicon and perovskite solar cells. Sol. Energy 163, 243-250.

Chen, J., Zhou, S., Jin, S., Zhai, T., 2015. Crystal organometal halide perovskites with promising optoelectronic applications. J. Mater. Chem. C.

Chia, L., Swainsona, I., Cranswick, L., Herb, J.H., Stephens, P., Knop, O., 2005. The ordered phase of methylammonium lead chloride $CH_3NH_3PbCl_3$. J. Solid State Chem. 178, 1376-1385.

Cui, J., Yuan, H., Li, J., Xu, X., Shen, Y., Lin, H., Wang, M., 2015. Recent progress in efficient hybrid lead halide perovskite solar cells. Sci. Technol. Adv. Mater. 16 036004.

Fan, Z., Sun, K., Wang, J., 2015. Perovskites for photovoltaics: a combined review of organic-inorganic halide perovskites and ferroelectric oxide perovskites. J. Mater. Chem. A.

Feng, J., 2014. Mechanical properties of hybrid organic-inorganic $CH_3NH_3BX_3$ (B = Sn, Pb; X = Br, I) perovskites for solar cell absorbers. APL Mater. 2 081801.

Hsiao, Y., Wu, T., Li, M., Liu, Q., Qin, W., Hu, B., 2015. Fundamental physics behind high efficiency organometal halide perovskite solar cells. J. Mater. Chem. A 3, 15372.

Jacobsson, T.J., Correa-Baena, J.P., Pazoki, M., Saliba, M., Schenk, K., Grätzel, M., Hagfeldt, A., 2016. An exploration of the compositional space for mixed lead halogen perovskites for high efficiency solar cells. Energy Environ. Sci.

Ji, D., Xiao, X.J., Zhang, C.M., Liy, X.L., Hu, M.Z., Yin, 2016. Regulatory band gap of vacancy at the B sites in $CH_3NH_3Pb_{1-x}I_3$ perovskite. Mod. Phys. Lett. B 30 (23).

Jishi, R.A., Ta, O.B., Sharif, A.A., 2014. Modeling of lead halide perovskites for photovoltaic applications. Cond Mat.

Kanhere, P., Chakraborty, S., Rupp, C.J., Ahujabd, R., Chen, Z., 2015. Substitution-induced band structure shape tuning in hybrid perovskites $(CH_3 NH_3Pb_{1x}Sn_x I_3)$ for efficient solar cell applications. RSC Adv 5 (1), 07497.

Koliogiorgos, A., Baskoutas, S., Galanakis, I., 2017. Electronic and gap properties of lead-free perfect and mixed hybridhalide perovskites: an ab-initio study. Comput. Mater. Sci. 138, 92-98.

Leguу, A.M.A., Azarhoosh, P., Alonso, M.I., Quiles, M.C., Weber, O.J., Yao, J., Bryant, D., Weller, M.T., Nelson, J., Walsh, A., VSchilfgaarde, M., Barnes, P.R.F., 2016. Experimental and theoretical optical properties of methylammonium lead halide perovskites. Nanoscale 8, 6317.

Liu, D., Li, S., Bian, F., Meng, X., 2018. First principles investigation on the electronic and mechanical properties of Cs-doped $CH_3NH_3PbI_3$. Materials.

Liu, X., Zhao, W., Cui, H., Xie, Y., Wang, Y., Xu, T., Huang, F., 2012. Organic-inorganic halide perovskite based solar cells - revolutionary progress in photovoltaics. Inorg. Chem. Front.

Manser, J.S., Christians, J.A., Kamat, P.V., 2016. Intriguing optoelectronic properties of metal halide perovskites. Chem. Rev. 116, 12956-13008.

Mladenovic, M., Vukmirovic, N., 2018. Effects of thermal disorder on electronic structure of halide perovskites: insights from MD simulations. PCCP.

Ndione, P.F., Li, Z., Zhu, K., 2016. Effects of alloying on optical properties of organic-inorganic lead halide perovskite thin films. J. Mater. Chem. C.

Perdew, J.P., Burke, K., Ernzerhof, M., 1996. Generalized gradient approximation made simple. Phys. Rev. Lett 77, 3865-3868.

Pfrommer, B.G., Louie, C.M., Cohen, S.G., M. L., 1997. Relaxation of crystals with the quasi-Newton method. J. Comput. Phys 13, 233-240.

Qing, B., Wei, W., Zhou, Y., Dong, Y., 2018. Photoelectric performance and stability comparison of $MAPbI_3$ and $FAPbI_3$ perovskites solar cells. Sol. Energy 174, 933-939.

Quarti, C., Mosconi, E., Ball, J.M., D'Innocenzo, V., Tao, C., Pathak, S., Snaith, H.J., Petrozza, A., Angelis, F.D., 2015. Structural and optical properties of methylammonium lead iodide across the tetragonal to cubic phase transition: implications for perovskite solar cells. Energy Environ. Sci.

Song, T.B., Chen, Q., Zhou, H., Jiang, C., Wang, H.H., Yang, M., Liu, Y.S., You, J., Yang, Y., 2015. Perovskite solar cells: film formation and properties. J. Mater. Chem. A.

Sun, S., Fang, Y., Kieslich, G., White, T.J., Cheetham, A.K., 2015. Mechanical properties of organic-inorganic halide perovskites, $CH_3NH_3PbX_3$ (X = I, Br and Cl), by nano-indentation. J. Mater. Chem. C.

Swainson, I.P., Hammond, R.P., Soullie're, C., Knop, O., Massa, W., 2003. Phase transitions in the perovskite methylammonium lead bromide, $CH_3Nh_3PbBr$ 3. J. Solid State Chem. 176, 97-104.

Wolf, S.D., Holovsky, J., Moon, S.J., Löper, P., Niesen, B., Ledinsky, M., Haug, F.J., Yum, J.H., Ballif, C., 2014. Organometallic halide perovskites: sharp optical absorption edge and its relation to photovoltaic performance. J. Phys. Chem. Lett 5, 1035-1039.

Ye, Y., Run, X., Tao, X.H., Feng, H., Fei, X., Jun, W.L., 2015. Nature of the band gap of halide perovskites $ABX_3$(A = $CH_3NH_3$, Cs; B = Sn, Pb; X = Cl, Br, I): first-principles calculations. Chin. Phys. B 24 (11) 116302.

Yin, W.J., Yang, J.H., Kang, J., Yan, Y., Wei, S.H., 2014. Halide perovskite materials for solar cells: a theoretical review. J. Mater. Chem. A.

Yusoff, A.R.B.M., Nazeeruddin, K.M., 2016. Organohalide lead perovskites for photovoltaic applications. J. Phys. Chem Lett.

Zhao, Y., Zhu, K., 2016. Organic-inorganic hybrid lead halide perovskites for optoelectronic and electronic applications. Chem. Soc. Rev. 45, 655.

Zhou, Y., Wang, F., Fang, H.H., Loi, M.A., Xie, F.Y., Zhoa, N., Wong, C.P., 2016. Distribution of bromine in mixed iodide-bromide organolead perovskites and its impact on photovoltaic performance. J. Mater. Chem. A.