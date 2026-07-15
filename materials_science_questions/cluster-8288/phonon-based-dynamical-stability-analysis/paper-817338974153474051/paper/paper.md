Article

# First-Principles Investigation of Structural, Thermoelectric, and Optical Properties of Half-Heusler Compound ScRhTe under Varied Pressure

Junhong Wei $^{1,*,}$ Yongliang Guo $^{1}$ and Guangtao Wang $^{2}$

1 School of Science, Henan Institute of Technology, Xinxiang 453003, China
2 School of Physics, Henan Normal University, Xinxiang 453007, China
* Correspondence: wei_hh2006@126.com

Abstract: We thoroughly investigated the electronic structure and various properties of the half-Heusler compound ScRhTe using density functional theory calculations. The electronic structure shows that ScRhTe is a narrow-band-gap semiconductor. Owing to its characteristic conduction-band structure, ScRhTe has a higher Seebeck coefficient and a higher power factor for n-type doping than for p-type doping, with the maximum value of $-493\ \mu\text{V}\ \text{K}^{-1}$ appearing at 900 K. The optimal carrier concentration is approximately $5 \times 10^{19}\ \text{cm}^{-3}$–$1 \times 10^{20}\ \text{cm}^{-3}$. In addition, $ZT_{\text{e}}$ is estimated as 0.95 at a doping level of approximately $10^{19}\ \text{cm}^{-3}$. Under pressure, the band structure changes from a direct to an indirect band gap, and the band gap increases as the pressure changes from tensile to compressive. The thermoelectric properties of ScRhTe improve under compressive pressure, whereas the optical properties improve greatly under tensile pressure. By varying the pressure, the electronic structure and various properties of ScRhTe can be effectively adjusted, which signifies that ScRhTe has the potential to become an important optoelectronic or thermoelectric material.

Keywords: half-Heusler compound; thermoelectric property; optical property; pressure; first-principles calculations

## 1. Introduction

Thermoelectric (TE) materials have garnered considerable interest in recent years owing to their potential applications in power generation from waste heat [1–5] because they enable the direct conversion between heat and electricity. They are expected to play an important role in promoting global energy sustainability and energy harvesting. However, the low efficiency of TE materials has been the main obstacle to the replacement of traditional power generation methods with TE methods [6,7]. Therefore, it is important to improve the efficiency of TE materials, which is described using the figure of merit $ZT$. $ZT$ is given by $ZT = S^{2}\sigma T/(\kappa_{\text{e}} + \kappa_{\text{L}})$, where $S$ is the Seebeck coefficient, $T$ is the absolute temperature, $\sigma$ is the electrical conductivity, $\kappa_{\text{e}}$ is the electronic thermal conductivity, and $\kappa_{\text{L}}$ is the lattice thermal conductivity [4,8]. In addition, the power factor is given by $PF = S^{2}\sigma$. Good TE materials should have a high $ZT$ value, i.e., a high Seebeck coefficient, high electrical conductivity, and low thermal conductivity [9,10]. However, these parameters are related to each other, and changing one parameter affects the others [4,11].

Narrow-band-gap semiconductors are good candidates for use as TE materials [12–15]; they must be inexpensive and capable of sustaining high temperatures, exhibit mechanical strength, and consist of nontoxic materials [16–21]. Ternary half-Heusler compounds, which have 18 or 8 valence electrons in the per formula unit, satisfy these criteria. Many half-Heusler alloys reportedly exhibit notable TE properties [22–36]. Gautier et al. [37] recently reported ‘missing compounds’ in the 18-valence-electron ABX family; some of these materials have been found to exhibit interesting behavior, such as topological phase transitions, TE and phenomena, piezoelectric phenomena, and magnetic properties [38–41].

---

![](./images/817338974153474051_1.jpg)

Citation: Wei, J.; Guo, Y.; Wang, G. First-Principles Investigation of Structural, Thermoelectric, and Optical Properties of Half-Heusler Compound ScRhTe under Varied Pressure. Crystals 2022, 12, 1472.
https://doi.org/10.3390/cryst12101472

Academic Editor: Anna Paola Caricato

Received: 28 September 2022
Accepted: 14 October 2022
Published: 17 October 2022

Publisher’s Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](./images/817338974153474051_2.jpg)

Copyright: © 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/licenses/by/4.0/).


Ni-doped $ZrPd_{1-x}Ni_xPb$ [35] decreases the lattice thermal conductivity, which suggests that $ZrPd_{0.25}Ni_{0.75}Pb$ is a good TE material. Via strain engineering, ZrRhSb [36] obtains good TE properties, where $ZT_e$ value reaches 0.81 at room temperature. ZrNiPb [37] has been found to exhibit TE behavior, with Seebeck coefficient and power factor as large as $-153.9\ \mu\text{V K}^{-1}$ and $5.2\ \mu\text{W cm}^{-2}\text{K}^{-1}$, respectively, at room temperature. Under pressure, topological transitions in HfIrX (X = As, Sb, Bi) [38] have been confirmed, and compressive stress in the ab plane causes HfIrBi to become a Weyl semimetal. The performance of ABPb (A = Hf, Zr; B = Ni, Pd) [39] has been estimated by theoretical calculations, yielding results in good agreement with experimental results [37]. TaCoSn [40] is considered to be an important photoelectric and TE material. FeRhCrZ (Z = Si and Ge) [41] is a newly synthesized alloy, as well as it has been predicted by theoretical calculation to be a good TE material with large power factors. Moreover, many half-Heusler compounds have been documented in the Inorganic Crystal Structure Database (ICSD) [42]. However, there is still an opportunity to search for new potential half-Heusler compounds. There has been little research on ScRhTe, one of the missing compounds identified by Gautier et al. [37]. To determine its suitability as a TE material, we calculated multiple properties of ScRhTe by theoretical simulations, investigated the effects of hydrostatic pressure on these properties and analyzed the results.

## 2. Theoretical Methods

Using first-principles calculations, we studied the properties of ScRhTe via the full-potential linearized augmented plane-wave (FPLAPW) method in the WIEN2K code [43]. The properties include the electronic structure, optical properties, and TE properties under various pressures. The Perdew-Burke-Ernzerhof generalized gradient approximation [44,45] and the project-augmented wave method were employed in our study. To obtain accurate band gaps, we employed a modified Becke-Johnson (mBJ) potential [46,47]. We set the energy cutoff between the core and valence states to $-8.0$ Ry, and kept the plane-wave cutoff at $R_{MT} \times K_{MAX} = 10$. A $k$-mesh of $20 \times 20 \times 20$ was used for the self-consistency calculated in the Brillouin zone. The TE properties, such as $S$, electrical conductivity $(\sigma/\tau)$, $\kappa_e$, were evaluated from the semi-classical Boltzmann transport theory with the constant scattering time approximation (CSTA) [48] using BoltzTraP code [49,50]. Boltzmann transport calculations have been used for TEs for a long time, especially in the study of wide- and narrow-gap semiconductors [51-54]. Using the BoltzTraP code, we were able to obtain the TE properties with 20,000 $k$-points of the denser $k$-mesh. The relaxation time $\tau$ was assumed to be isotropic and constant with respect to the wave vector $k$ and energy. This assumption is widely accepted for degenerately doped semiconductors. The spin-orbit interaction (SOC) effect, which can affect the electronic structure, and thus the properties of the material, was included in our calculations.

## 3. Results and Discussion

### 3.1. Effect of SOC on Structure and TE Properties

The half-Heusler compound ScRhTe has a cubic LiAlSi-type structure with space group Fm-43 (No.216), as shown in Figure 1a. Sc, Rh, and Te atoms are located in the Wyckoff positions of 4c (0.25, 0.25, 0.25), 4b (0.5, 0.5, 0.5) and 4a (0.0, 0.0, 0.0), respectively. We first optimized the crystal structure; the relaxed equilibrium lattice constant is $\text{a} = 6.347\ \text{\AA}$, which agrees well with the value reported by Gautier et al. [38]. Using the optimized lattice constant, we calculated the band structure and projected density of states (PDOS) of ScRhTe using both mBJ and mBJ + SOC, as shown in Figure 1b,c. ScRhTe is clearly a direct band gap [37], and the conduction-band minimum (CBM) and valence band maximum (VBM) are located at the $\Gamma$ point. This structure is similar to those of half-Heusler compounds that are direct band gap semiconductors [55,56]. The band gap is 0.69 eV without SOC, and 0.73 eV with the SOC effect, which is in good agreement with the value reported by Gautier et al. [37]. Figure 1b clearly shows that the SOC affects the VBM at the high-symmetry $\Gamma$ point, resulting in spin-orbit splitting, but has a negligible effect on the conduction bands.

From the PDOS, we see that the CBM bands consist mainly of the Sc d states and the s states of Sc, Rh, Te, whereas the VBM near the Fermi level is dominated by the d states of Rh and Sc hybridized with the p-states of Rh and Te. It can be concluded that the d states of the constituent elements strongly affect the TE properties. Moreover, we find that the band at the CBM is rather flat, and that near the VBM is relatively sharp, indicating very low TE properties of the VBM. but very high TE properties of the CBM. Thus, we expect that ScRhTe has a higher S and larger PF for n-type doping.

![](./images/817338974153474051_3.jpg)

**Figure 1.** (a) Crystal structure of ScRhTe; Sc, Rh, and Te atoms are shown by green, blue, and grayfilled spheres, respectively. Band structure and projected density of states (PDOS) of ScRhTe (b) without spin-orbit interaction (SOC) and (c) with SOC.

We calculated the TE properties of ScRhTe using the Boltzmann theory to determine its TE performance. Previous reports have shown that SOC affects the structure of materials, particularly the S and PF [38,57-62]. To verify whether SOC affects the TE properties of ScRhTe, we first considered the effect of SOC on the transport coefficients of ScRhTe, including S and power factor with respect to the scattering time ($S^{2}\sigma/\tau$), for various carrier concentrations at 300 K using mBJ and mBJ + SOC. The results are shown in Figure 2. ScRhTe clearly has a larger S for n-type doping than for p-type doping, and S for p-type doping decreased when the SOC effect was included, whereas SOC had a negligible effect on S for n-type doping. However, $S^{2}\sigma/\tau$ exhibited a great influence. The reason is that SOC splitting removed the degeneracy of the VBM and CBM, and modified the band structure, causing notable changes in the p-type and n-type doping. The properties of this material depend greatly on the band structure. Therefore, we considered the SOC effect in the subsequent calculations.

![](./images/817338974153474051_4.jpg)

Figure 2. (a) S (μV K⁻¹) and (b) S²σ/τ (1 × 10¹⁰ W m⁻¹ K⁻² s⁻¹) presented with mBJ (black dotted line) and mBJ + SOC (red dotted line) at 300 K.

### 3.2. Thermoelectric Properties

We calculated the TE properties of ScRhTe as a function of carrier concentration and temperature using the Boltzmann theory. Figure 3 shows $S$, $S^{2}\sigma/\tau$, $\sigma/\tau$, and figure of merit $ZT_{e}$ at different temperatures. At $T = 300$ and 600 K, $S$ is large at low carrier concentrations for both p- and n-type doping. At $T = 900$ and 1200 K, the $S$ curves exhibit broad peaks resulting from the bipolar effect. The value for n-type doping is clearly higher than that for p-type doping at each temperature. For p-type doping, the highest $S$ at 900 and 1200 K are 390 and 301 μV K⁻¹ at concentrations of $8.6 \times 10^{18}$ and $4.4 \times 10^{19}$ cm⁻³, respectively. For n-type doping, the highest values at 900 and 1200 K are −493 and −387 μV K⁻¹ at concentrations of $2 \times 10^{19}$ cm⁻³ and $9.5 \times 10^{19}$ cm⁻³, respectively.

Figure 3a shows a clear bipolar effect at high temperatures for both n- and p-type doping. The bipolar effect often appears in materials such as wide-gap semiconductors at high temperatures and narrow-gap semiconductors or semimetals at room temperature, because holes are major carriers and electrons are minor carriers for p-type materials. $S$ is then defined as [63] $S = (S_{e}\ \sigma_{e} + S_{h}\ \sigma_{h})/(\sigma_{e} + \sigma_{h})$, where $S_{e}$ ($S_{h}$) and $\sigma_{e}$ ($\sigma_{h}$) are the electron (hole) Seebeck coefficient and conductivity, respectively. For p-type materials, electrons make up a negligible proportion of the total carriers at low temperatures because there is little thermal excitation, but at high temperatures, the minor carrier concentration cannot be ignored. Thus, $S$ reflects the bipolar effect at high temperatures. $S^{2}\sigma/\tau$ is shown as a function of carrier concentration at 300, 600, 900 and 1200 K in Figure 3b. $S^{2}\sigma/\tau$ increases with $T$ for a given carrier concentration and exhibits a peak at approximately $1.6 \times 10^{21}$ cm⁻³. The n-type $S$ and $S^{2}\sigma/\tau$ are clearly larger than the p-type values. This result indicates that n-type ScRhTe can be expected to have good TE properties.

Figure 3c shows the variation in electrical conductivity per second with respect to the scattering time ($\sigma/\tau$) at different temperatures. At all temperatures, $\sigma/\tau$ exhibits similar behavior with increasing carrier concentration. As the temperature increases, the lattice vibration increases, which hinders the movement of carriers. Therefore, the conductivity decreases with increasing temperature. For a given temperature, the conductivity increases as the carrier concentration increases. The value of $\sigma/\tau$ is higher for p-type doping than for n-type doping. We can predict that the p-type doping has higher electrical conductivity than the n-type doping.

Figure 3d shows the figure of merit $ZT_{e}$ of ScRhTe as functions of $T$ and carrier concentration for p- and n-type doping. The energy conversion efficiency $\eta$ of TE devices in applications is essentially decided by the dimensionless figure of merit ZT of the material, which is defined as [64]: $ZT = ZT_{e} \times \kappa_{e}/(\kappa_{e} + \kappa_{L})$, where $\kappa_{e}$ and $\kappa_{L}$ are the electronic and lattice thermal conductivity, respectively. The ratio $ZT_{e} = S^{2}\sigma T/\kappa_{e}$ is independent of the

relaxation time $\tau$ and is an upper limit on the TE figure of merit, which ignores only the lattice contribution to the thermal conductivity. At temperatures above room temperature, the large number of excited electrons causes an increase in the electrical thermal conductivity, whereas the lattice contribution decreases because the phonon scattering ratio is increased owing to severe lattice vibration. Thus, at higher temperatures, the effect of $\kappa_{L}$ on $ZT_{e}$ is assumed to be insignificant [36]. Therefore, $ZT_{e}$ is a good proxy for $ZT$ as the temperature increases. The figure of merit is calculated by $ZT_{e}=S^{2}\sigma T/\kappa_{e}$. When the carrier concentration is fixed, $ZT_{e}$ increases with T, and when the temperature is fixed, $ZT_{e}$ decreases with the carrier concentration. It is higher for n-type doping than for p-type doping. $ZT_{e}$ is estimated to have a large value of 0.95 at a doping level of approximately $10^{19}\ \text{cm}^{-3}$ if the bipolar effect is not considered. The obtained TE properties clearly show that ScRhTe exhibits a nearly ideal TE performance and is a promising TE material.

![](./images/817338974153474051_5.jpg)

Figure 3. $S$ ($\mu\text{V K}^{-1}$) (a), $S^{2}\sigma/\tau$ ($1\times10^{10}\ \text{W m}^{-1}\text{K}^{-2}\text{s}^{-1}$) (b), $\sigma/\tau$ (c), and $ZT_{e}$ (d) of ScRhTe at different temperatures. The black, red, green, and blue dashed lines represent $T = 300, 600, 900$, and 1200 K, respectively.

Most materials typically exhibit optimal performance at carrier concentrations above those at which the maximum $S$ occurs. To obtain a high-performance TE, we investigated the temperature dependence of $S$ at four fixed electron (hole) concentrations, as shown in Figure 4. At concentrations of $5\times10^{19}\ \text{cm}^{-3}$ and $1\times10^{20}\ \text{cm}^{-3}$, the highest $S$ are approximately $-440$ and $-400\ \mu\text{V K}^{-1}$ at 1000 and 1110 K, respectively. The optimal carrier concentration is clearly in the range $5\times10^{19}\ \text{cm}^{-3}$ to $1\times10^{20}\ \text{cm}^{-3}$. An optimal carrier concentration of approximately $10^{21}\ \text{cm}^{-3}$ has been reported for half-Heusler alloys [2,65]. Our results differ from most of those in the literature but are in good agreement with those reported by Singh [55].

![](./images/817338974153474051_6.jpg)

Figure 4. Calculated S for ScRhTe at various fixed concentrations as a function of temperature.

### 3.3. Influence of Pressure on Electronic Structure

The electronic structures of semiconductors are highly sensitive to pressure, which suggests the need for a strategy for tuning the band structure. Pressure-induced changes in the optical properties of $\beta$-Na$_{0.33}$V$_2$O$_5$ have been reported [66]. The TE properties of some TE materials improve dramatically under compression [57,58,67-69]. As the deformation behavior of materials under compression could provide considerable information about the nature of the solids, such as phase transitions and changes in physical and chemical properties, investigations under pressure are very important. To explore the properties of ScRhTe, we attempted to predict the TE and optical properties of the compound under pressure. We varied the lattice constant between 96% and 104% of the calculated value to simulate hydrostatic pressure on the compound. The applied hydrostatic pressure is defined as $\varepsilon = (a - a_0)/a_0$, where $a$ and $a_0$ are the lattice constant under pressure and the equilibrium value, respectively. Positive and negative values of $\varepsilon$ indicate tensile and compressive pressure, respectively.

The phonon dispersion of a crystal is a fundamental subject for identifying the phase dynamic stability of crystalline material. To verify the dynamic stability of ScRhTe under the applied hydrostatic pressure, we calculated the phonon dispersion spectra as shown in Figure 5a-i. If the phonon dispersion does not exhibit soft phonon modes or imaginary frequencies, the structure is dynamically stable [70].

![](./images/817338974153474051_7.jpg)

Figure 5. Phonon dispersion curves of ScRhTe at (a) $\varepsilon=-4\%$, (b) $\varepsilon=-3\%$, (c) $\varepsilon=-2\%$, (d) $\varepsilon=-1\%$, (e) $\varepsilon=0\%$, (f) $\varepsilon=1\%$, (g) $\varepsilon=2\%$, (h) $\varepsilon=3\%$, (i) $\varepsilon=4\%$ different pressure. The value of $\varepsilon$ is positive for tensile pressure and negative for compressive pressure and zero for unstrained.

ScRhTe is a direct band gap semiconductor at the equilibrium lattice constant, as shown in Figure 6b. Under pressure, the band gap increases as the pressure changes from tensile to compressive, as shown in Figure 6d. In addition, the band structure changes from a direct band gap to an indirect band gap under compressive pressure, where the CBM moves from $\Gamma$ to a point between $\Gamma$ and X. To understand this interesting change in the band structure under pressure, we focus on the projected band structure of ScRhTe in Figure 6b. The CBM (at the $\Gamma$ point) consists mainly of s-orbitals of Sc, Rh, and Te, whereas the VBM consists mainly of the hybridized p-d states of the Rh and Sc atoms. The s-like orbital exhibits greater expansion than the localized d-like orbital. When compressive pressure is applied to the compound, the band energies of both the s-like and d-like orbitals increase. However, the energy of the s-like band increases much more than that of the d-like band because of the greater expansion of the s-orbital. Therefore, as shown in Figure 6a,c, the s-like band at the $\Gamma$-point moves upward, whereas the d-like band at the X point moves very little. When $\varepsilon=-1\%$, the band structure of ScRhTe changes from a direct band gap (Figure 6c) to an indirect band gap (Figure 6a).

![](./images/817338974153474051_8.jpg)

Figure 6. Band structure of ScRhTe under varying pressure. (a-c) correspond to $\varepsilon=-2\%$, $0\%$, $2\%$, respectively. (b) Symbol sizes correspond to the projected weight of Bloch states onto the s-like (red circle) orbit and d-like (blue circle) orbit. (d) Trend of the band gap of ScRhTe under varying strain. $\varepsilon$ represents applied hydrostatic pressure.

### 3.4. Influence of Pressure on Thermoelectric Properties

The TE properties depend strongly on the electronic structure of the material. As the band structures changed under the applied pressure, the TE properties were also affected by the pressure. Thus, we examined $S$ and $S^{2}\sigma/\tau$ under different pressures, which were obtained using Boltzmann theory with the CSTA. As the variation of the properties under pressure does not depend on the temperature, we present only the properties at room temperature, as shown in Figure 7. It is interesting that the behavior of $S$, $\sigma/\tau$, and $S^{2}\sigma/\tau$ is the same as that of the band gaps for n- and p-type doping as the pressure increases from $-4\%$ to $4\%$. As shown in Figure 7a, $S$ increases gradually as the pressure increases from $4\%$ to $-4\%$ for n-and p-type doping. As $S$ makes the largest contribution to the power factor, the effects of pressure on $S^{2}\sigma/\tau$ and $S$ are the same, as shown in Figure 7b. The

effects of the pressure for n-type doping are greater than for p-type doping. The CBM band becomes increasingly flat as the pressure changes from 4% to −4% (from Figure 6c to Figure 6a). The flat band indicates very high TE properties; thus, *S* for n-type doping increases as the pressure changes from tensile to compressive. The results also show that the pressure has a negligible effect on the *S* and $S^{2}\sigma/\tau$ values for p-type doping because the pressure only slightly affects the electronic structure of the VBM. The strong pressure dependence of *S* and $S^{2}\sigma/\tau$ for n-type doping shows that the TE properties of ScRhTe increase with increasing compressive pressure; specifically, ScRhTe may become a more efficient TE material under pressure.

![](./images/817338974153474051_9.jpg)

Figure 7. Seebeck coefficient *S* (μV K⁻¹) (a), power factor with respect to scattering time $S^{2}\sigma/\tau$ ($1 \times 10^{10}$ W m⁻¹ K⁻² s⁻¹) (b), conductivity with respect to scattering time $\sigma/\tau$ (c), and figure of merit $ZTe$ (d) under varying pressure of ScRhTe at room temperature.

Figure 7d shows the calculated $ZT_{e}$ as a function of carrier concentration for p- and n-type doping at room temperature. The effect of pressure on $ZT_{e}$ is clearly negligible for p-type doping at strains of −4% to 4%. For n-type doping, $ZT_{e}$ decreases gradually with increasing tensile pressure from 0% to 4%. Overall, $ZT_{e}$ maintains a high value of approximately 0.97. When the carrier concentration is less than $10^{19}$ cm⁻³, the pressure has no effect on $ZT_{e}$ and the maximum value is approximately 0.97. When the carrier concentration exceeds $10^{19}$ cm⁻³, $ZT_{e}$ increases with increasing compressive pressure from 0% to −4%. This result shows that the application of compressive pressure is useful for improving the $ZT_{e}$ value of ScRhTe, whereas the application of tensile pressure is unfavorable.

### 3.5. Influence of Pressure on Optical Properties

Semiconductor materials are known for their important technological applications, especially in the manufacture of electronic and electro-optical devices [71]. They may have direct or indirect band gaps. In direct band gap materials, the top and bottom of the valence band appear at the same wave vector value, while for indirect band gap materials, they appear at different wave vector values. Indirect band gap materials have low absorption and therefore are optically inactive [72]. By contrast, direct band gap materials have high absorption and are optically active. Direct band gap materials should be used for optoelectronic devices such as solar cells and detectors to obtain a fast response and high efficiency. ScRhTe is a direct band gap semiconductor and an optically active material; its band structure is highly sensitive to pressure. Pressure-induced changes in optical properties have been reported [58,66]. The optical properties play a crucial role in the optoelectronic behavior of a material. We assumed that the optical properties of ScRhTe would be affected by pressure. Hence, we investigated the optical properties of ScRhTe under different pressures; the frequency-dependent dielectric function and absorption coefficient are shown in Figure 8.

![](./images/817338974153474051_10.jpg)

Figure 8. Cont.

![](./images/817338974153474051_11.jpg)

Figure 8. Real part of complex dielectric function (a), imaginary part of complex dielectric function (b), and absorption coefficient (c) for ScRhTe under varying pressure.

The optical properties can be described in terms of the dielectric function $\varepsilon(\omega)$. WIEN2K code is used to calculate the imaginary and real parts of the frequency-dependent dielectric function in the ground-state electronic configuration of ScRhTe. The real and imaginary parts of $\varepsilon(\omega)$ are often denoted as $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$, respectively [73], as shown in Figure 8a,b.

The frequency-dependent dielectric function $\varepsilon_1(\omega)$ is shown in Figure 8a. The zero-frequency limit $\varepsilon_1(0)$, which is the electric part of $\varepsilon_1(\omega)$ without pressure is 15.4. Under pressure, $\varepsilon_1(0)$ decreases monotonically from 13.82 to 17.92 as the pressure changes from $-4\%$ to $4\%$ because it is inversely proportional to the band gap [74]. Beyond the zero-

frequency limit, it increases smoothly around 18.9 eV and reaches its maximum value; it then decreases, with some notable variation, decreasing below zero in certain energy ranges. Finally, it increases from negative to positive, and the curve becomes smooth.

Figure 8b shows a plot of $\varepsilon_{2}(\omega)$. Without pressure, a threshold appears at 2.59 eV, which is the optical gap of the compound. As the compressive pressure increases, the threshold shifts towards higher energies, whereas under increasing tensile pressure, the threshold shift toward lower energies. The shift in the threshold is clearly reflected in the variation of the band gap with pressure.

As pressure modified the band structure, the optical properties of ScRhTe changed. Figure 8c shows the optical absorption under various pressures. Without pressure, ScRhTe exhibits an optical absorption peak at approximately 307 nm in the visible region, which corresponds to a band gap energy of 4.04 eV. Under compressive pressure, the band structure changes from a direct band gap to an indirect band gap. As indirect band gap materials are optically inactive, the absorption coefficient of ScRhTe decreases as the compressive pressure $\varepsilon$ is varied from 0% to $-4\%$. Under tensile pressure, the absorption coefficient of ScRhTe increases as the pressure is increased from 0% to 4%, and the absorption edge is clearly red-shifted, which is opposite to the behavior of the calculated band gaps in Figure 6d. Therefore, the results indicate that tensile pressure greatly improves the optical absorption properties of ScRhTe but that compressive pressure degrades them.

## 4. Conclusions

The electronic structure and transport properties of the ternary half-Heusler compound ScRhTe were investigated using first-principles calculations and the mBJ potential. The results indicated that ScRhTe is a direct band gap semiconductor. The TE properties $S$ and $S^{2}\sigma/\tau$ for p- and n-type doping were calculated using the Boltzmann transport theory. A high $S$ was obtained for ScRhTe, particularly for n-type doping. The optimal carrier concentration was approximately from $5 \times 10^{19}\ \text{cm}^{-3}$ to $1 \times 10^{20}\ \text{cm}^{-3}$. In addition, the highest value of $S$ was $-493\ \mu\text{V K}^{-1}$ at a concentration of $2 \times 10^{19}\ \text{cm}^{-3}$, at 900 K for n-type doping. $ZT_{e}$, a proxy for the figure of merit, had a large value of 0.95 at a doping level of approximately $10^{19}\ \text{cm}^{-3}$. The band structure changed under pressure; specifically, the band gap decreased as the pressure was varied from $-4\%$ to $4\%$. As the TE and optical properties depend strongly on the electronic structure of the material, the TE and optical properties are also affected by pressure. The $S$ and $S^{2}\sigma/\tau$ values for n-type doping increased as the compressive pressure increased from 0% to $-4\%$. The absorption coefficient of ScRhTe increased as the tensile pressure $\varepsilon$ was increased from 0% to 4%, and the absorption edge was clearly red-shifted. The results showed that compressive pressure improves the TE properties of ScRhTe, whereas tensile pressure improved the optical properties. In summary, our research indicated that ScRhTe is a promising material for TE and thin-film photovoltaic absorption applications, and the application of pressure was expected to be an effective method of improving the TE and optical properties. The theoretical prediction of new materials is easier than experimental realization, and it is hoped that our simulation can provide theoretical guidance for the preparation and application of this type of new material.

Author Contributions: J.W. designed the research, wrote and revised the manuscript, and conducted data analysis and details of the work. Y.G. and G.W. designed and guided the direction of the work. All authors have read and agreed to the published version of the manuscript.

Funding: This project was supported by the National Natural Science Foundation of China (Grant No. 11904081), the Basic Research Program of Education Bureau of Henan Province (Grant No. 20A140007) and the Research Initiation Fund of Henan Institute of Technology (Grant No. KQ1853). The calculations are supported by the High Performance Computing Center of Henan Normal University.

Data Availability Statement: Not applicable.

Conflicts of Interest: The authors declare no conflict of interest.

### References

1.  Bell, L.E. Cooling, Heating, Generating Power, and Recovering Waste Heat with Thermoelectric Systems. *Science* 2008, 321, 1457–1461. [CrossRef] [PubMed]

2.  Fu, C.; Bai, S.; Liu, Y.; Tang, Y.; Chen, L.; Zhao, X.; Zhu, T. Realizing high figure of merit in heavy-band p-type half-Heusler thermoelectric materials. *Nat. Commun.* 2015, 6, 8144. [CrossRef] [PubMed]

3.  DiSalvo, F.J. Thermoelectric Cooling and Power Generation. *Science* 1999, 285, 703–706. [CrossRef] [PubMed]

4.  Snyder, G.J.; Toberer, E.S. Complex thermoelectric materials. *Nat. Mater.* 2008, 7, 105–114. [CrossRef]

5.  Gaynera, C.; Kamal, K.K. Recent advances on thermoelectric materials. *Prog. Mater. Sci.* 2016, 83, 330–382. [CrossRef]

6.  Biswas, K.; He, J.; Blum, I.; Wu, C.-I.; Hogan, T.P.; Seidman, D.N.; Dravid, V.P.; Kanatzidis, M.G. High-performance bulk thermoelectrics with all-scale hierarchical architectures. *Nature* 2012, 489, 414–418. [CrossRef]

7.  Zhao, L.-D.; Lo, S.-H.; Zhang, Y.; Sun, H.; Tan, G.; Uher, C.; Wolverton, C.; Dravid, V.P.; Kanatzidis, M.G. Ultralow thermal conductivity and high thermoelectric figure of merit in SnSe crystals. *Nature* 2014, 508, 373–377. [CrossRef]

8.  LaLonde, A.D.; Pei, Y.; Wang, H.; Snyder, G.J. Lead telluride alloy thermoelectrics. *Mater. Today* 2011, 14, 526–532. [CrossRef]

9.  Shen, Q.; Chen, L.; Goto, T.; Hirai, T.; Yang, J.; Meisner, G.P.; Uher, C. Effects of partial substitution of Ni by Pd on the thermoelectric properties of ZrNiSn-based half-Heusler compounds. *Appl. Phys. Lett.* 2001, 79, 4165–4167. [CrossRef]

10. Xia, Y.; Bhattacharya, S.; Ponnambalam, V.; Pope, A.L.; Poon, S.J.; Tritt, T.M. Thermoelectric properties of semimetallic (Zr, Hf)CoSb half-Heusler phases. *J. Appl. Phys.* 2000, 88, 1952–1955. [CrossRef]

11. Liu, W.; Yan, X.; Chen, G.; Ren, Z. Recent advances in thermoelectric nanocomposites. *Nano Energy* 2011, 1, 42–56. [CrossRef]

12. Mahan, G.D.; Sofo, J.O. The best thermoelectric. *Proc. Natl. Acad. Sci. USA* 1996, 93, 7436–7439. [CrossRef]

13. Graf, T.; Felser, C.; Parkin, S.S. Simple rules for the understanding of Heusler compounds. *Prog. Solid State Chem.* 2011, 39, 1–50. [CrossRef]

14. Bos, J.-W.; Downie, R.A. Half-Heusler thermoelectrics: A complex class of materials. *J. Phys. Condens. Matter* 2014, 26, 433201. [CrossRef]

15. Tritt, T.M. Thermoelectric Phenomena, Materials, and Applications. *Annu. Rev. Mater. Res.* 2011, 41, 433–448. [CrossRef]

16. Tan, G.J.; Hao, S.; Zhao, J.; Wolverton, C.; Kanatzidis, M.G. High Thermoelectric Performance in Electron-Doped AgBi3S5 with Ultralow Thermal Conductivity. *J. Am. Chem. Soc.* 2017, 139, 6467–6473. [CrossRef]

17. Cerretti, G.; Schrade, M.; Song, X.; Balke, B.; Lu, H.; Weidner, T.; Lieberwirth, I.; Panthofer, M.; Norby, T.; Tremel, W. Thermal stability and enhanced thermoelectric properties of the tetragonal tungsten bronzes Nb8−xW9+xO47 (0 <x <5). *J. Mater. Chem. A* 2017, 5, 9768. [CrossRef]

18. Ge, Z.H.; Zhao, L.D.; Wu, D.; Liu, X.; Zhang, B.P.; Li, J.F.; He, J. Low-cost, abundant binary sulfides as promising thermoelectric materials. *Mater. Today* 2016, 19, 227–239. [CrossRef]

19. Misra, D.K.; Bhardwaj, A.; Singh, S. Enhanced thermoelectric performance of a new half-Heusler derivative Zr₉Ni₇Sn₈ bulk nanocomposite: Enhanced electrical conductivity and low thermal conductivity. *J. Mater. Chem. A* 2014, 2, 11913–11921. [CrossRef]

20. Chen, S.; Ren, Z. Recent progress of half-Heusler for moderate temperature thermoelectric applications. *Mater. Today* 2013, 16, 387–395. [CrossRef]

21. Huang, L.; Zhang, Q.; Yuan, B.; Lai, X.; Yan, X.; Ren, Z. Recent progress in half-Heusler thermoelectric materials. *Mater. Res. Bull.* 2015, 76, 107–112. [CrossRef]

22. Fang, T.; Zheng, S.; Zhou, T.; Yan, L.; Zhang, P. Computational prediction of high thermoelectric performance in p-type half-Heusler compounds with low band effective mass. *Phys. Chem. Chem. Phys.* 2017, 19, 4411–4417. [CrossRef] [PubMed]

23. Zhang, X.; Wang, Y.; Yan, Y.; Wang, C.; Zhang, G.; Cheng, Z.; Ren, F.; Deng, H.; Zhang, J. Origin of high thermoelectric performance of FeNb1−xZr/HfSb1−ySny alloys: A first-principles study. *Sci. Rep.* 2016, 6, 33120. [CrossRef] [PubMed]

24. Yu, C.; Zhu, T.J.; Shi, R.Z.; Zhang, Y.; Zhao, X.B.; He, J. High-performance half-Heusler thermoelectric materials Hf1−xZrxNiSn1−ySby prepared by levitation melting and spark plasma sintering. *Acta Mater.* 2009, 57, 2757–2764. [CrossRef]

25. Joshi, G.; Yan, X.; Wang, H.; Liu, W.; Chen, G.; Ren, Z. Enhancement in Thermoelectric Figure-Of-Merit of an N-Type Half-Heusler Compound by the Nanocomposite Approach. *Adv. Energy Mater.* 2011, 1, 643–647. [CrossRef]

26. Yan, X.; Liu, W.; Wang, H.; Chen, S.; Shiomi, J.; Esfarjani, K.; Wang, H.; Wang, D.; Chen, G.; Ren, Z. Stronger phonon scattering by larger differences in atomic mass and size in p-type half-Heuslers Hf1−xTixCoSb0.8Sn0.2. *Energy Environ. Sci.* 2012, 5, 7543–7548. [CrossRef]

27. Sakurada, S.; Shutoh, N. Effect of Ti substitution on the thermoelectric properties of (Zr,Hf)NiSn half-Heusler compounds. *Appl. Phys. Lett.* 2005, 86, 082105. [CrossRef]

28. Li, W.F.; Yang, G.; Zhang, J.W. Optimization of the thermoelectric properties of FeNbSb-based half-Heusler materials. *J. Phys. D Appl. Phys.* 2016, 49, 195601. [CrossRef]

29. Fang, T.; Zheng, S.; Chen, H.; Cheng, H.; Wang, L.; Zhang, P. Electronic structure and thermoelectric properties of p-type half-Heusler compound NbFeSb: A first-principles study. *RSC Adv.* 2016, 6, 10507–10512. [CrossRef]

30. Ren, Q.Y.; Fu, C.G.; Qiu, Q.Y.; Dai, S.N. Establishing the carrier scattering phase diagram for ZrNiSn-based half-Heusler thermoelectric materials. *Nat. Commun.* 2020, 11, 3142. [CrossRef]

31. Serrano-Sánchez, F.; Luo, T.; Yu, J.; Xie, W.; Le, C.; Auffermann, G.; Weidenkaff, A.; Zhu, T.; Zhao, X.; Alonso, J.A.; et al. Thermoelectric properties of n-type half-Heusler NbCoSn with heavy-element Pt substitution. *J. Mater. Chem. A* 2020, 8, 14822–14828. [CrossRef]

32. Rogl, G.; Ghosh, S.; Wang, L.; Bursik, J.; Grytsiv, A.; Kerber, M.; Bauer, E.; Mallik, R.C.; Chen, X.-Q.; Zehetbauer, M.; et al. Half-Heusler alloys: Enhancement of ZT after severe plastic deformation (ultra-low thermal conductivity). *Acta Mater.* 2019, 183, 285–300. [CrossRef]

33. Yan, R.; Xie, W.; Balke, B.; Chen, G.; Weidenkaff, A. Realizing p-type NbCoSn half-Heusler compounds with enhanced thermoelectric performance via Sc substitution. *Sci. Technol. Adv. Mater.* 2020, 21, 122–130. [CrossRef]

34. Haque, E.; Rahman, M.; Sultana, P. Effect of Bi-substitution on structural stability and improved thermoelectric performance of p-type half-Heusler TaSbRu: A first-principles study. *Comput. Mater. Sci.* 2021, 190, 110300. [CrossRef]

35. Wang, D.Y.; Wang, G.T.; Li, W.F. Khandy, Ni substitution enhanced thermoelectric properties of ZrPd1−xNixPb(x = 0, 0.25, 0.5, 0.75, 1). *J. Alloy. Compd.* 2017, 692, 599–604. [CrossRef]

36. Khandy, S.A.; Chai, J.-D. Strain engineering of electronic structure, phonon, and thermoelectric properties of p-type half-Heusler semiconductor. *J. Alloy. Compd.* 2020, 850, 156615. [CrossRef]

37. Gautier, R.; Zhang, X.; Hu, L.; Yu, L.; Lin, Y.; Sunde, T.O.L.; Chon, D.; Poeppelmeier, K.R.; Zunger, A. Prediction and accelerated laboratory discovery of previously unknown 18-electron ABX compounds. *Nat. Chem.* 2015, 7, 308–316. [CrossRef]

38. Wang, G.; Wei, J. Topological phase transition in half-Heusler compounds HfIrX (X = As, Sb, Bi). *Comput. Mater. Sci.* 2016, 124, 311–315. [CrossRef]

39. Wang, G.; Wang, D. Electronic structure and thermoelectric properties of Pb-based half-Heusler compounds: ABPb (A = Hf, Zr; B = Ni, Pd). *J. Alloy. Compd.* 2016, 682, 375–380. [CrossRef]

40. Wei, J.; Wang, G. Thermoelectric and optical properties of half-Heusler compound TaCoSn: A first-principle study. *J. Alloy. Compd.* 2018, 757, 118–123. [CrossRef]

41. Khandy, S.A.; Chai, J.D. Thermoelectric properties, phonon, and mechanical stability of new half-metallic quaternary Heusler alloys: FeRhCrZ (Z = Si and Ge). *J. Appl. Phys.* 2020, 127, 165102. [CrossRef]

42. Bergerhoff, G.; Hundt, R.; Sievers, R.; Brown, I.D. The Inorganic Crystal Structure Database (ICSD). *Chem. Inf. Comput. Sci.* 1983, 23, 66–69. [CrossRef]

43. Blaha, P.; Schwarz, K.; Tran, F.; Laskowski, R.; Madsen, G.K.H.; Marks, L.D. WIEN2k: An APW+lo program for calculating the properties of solids. *J. Chem. Phys.* 2020, 152, 074101. [CrossRef]

44. Kresse, G.; Joubert, D. Efficient iterative schemes for ab initio total-energy calculations using a planewave basis set. *Phys. Rev. B* 1999, 59, 11169. [CrossRef]

45. Perdew, J.P.; Burke, K.; Ernzerhof, M. Generalized gradient approximation made simple. *Phys. Rev. Lett.* 1996, 77, 3865. [CrossRef]

46. Tran, F.; Blaha, P. Accurate Band Gaps of Semiconductors and Insulators with a Semilocal Exchange-Correlation Potential. *Phys. Rev. Lett.* 2009, 102, 226401. [CrossRef]

47. Becke, A.D.; Johnson, E.R. A simple effective potential for exchange. *J. Chem. Phys.* 2006, 124, 221101. [CrossRef]

48. Zhang, L.; Singh, D.J. Electronic structure and thermoelectric properties of layered PbSe-WSe 2 materials. *Phys. Rev. B* 2009, 80, 075117. [CrossRef]

49. Singh, D.J. Doping-dependent thermopower of PbTe from Boltzmann transport calculations. *Phys. Rev. B* 2010, 81, 195217. [CrossRef]

50. Madsen, G.K.; Singh, D.J. BoltzTraP. A code for calculating band-structure dependent quantities. *Comput. Phys. Commun.* 2006, 175, 67–71. [CrossRef]

51. Hinsche, N.F.; Mertig, I.; Zahn, P. Effect of strain on the thermoelectric properties of silicon: An ab initio study. *J. Phys. Condens. Matter.* 2011, 23, 295502. [CrossRef]

52. Parker, D.; Singh, D.J. High-temperature thermoelectric performance of heavily doped PbSe. *Phys. Rev. B* 2010, 82, 035204. [CrossRef]

53. May, A.F.; Singh, D.J.; Snyder, G.J. Influence of band structure on the large thermoelectric performance of lanthanum telluride. *Phys. Rev. B* 2009, 79, 153101. [CrossRef]

54. Lee, M.S.; Poudeu, F.P.; Mahanti, S.D. Publisher’s Note: Electronic structure and thermoelectric properties of Sb-based semiconducting half-Heusler compounds. *Phys. Rev. B* 2011, 83, 085204. [CrossRef]

55. Singh, S. Assessing the thermoelectric properties of ScRhTe half-heusler compound. *Comput. Condens. Matter* 2017, 13, 120–126. [CrossRef]

56. Kaur, K.; Kaur, J. Exploration of thermoelectricity in ScRhTe and ZrPtPb Half Heusler compounds: A first principle study. *J. Alloy. Compd.* 2017, 715, 297–303. [CrossRef]

57. Guo, S.-D.; Wang, J.-L. Pressure enhanced thermoelectric properties in Mg2Sn. *RSC Adv.* 2016, 6, 31272–31276. [CrossRef]

58. Wei, J.; Wang, G. Properties of half-Heusler compounds TaIrGe by using first-principles calculations. *Appl. Phys. A* 2017, 123, 375. [CrossRef]

59. Kutorasinski, K.; Wiendlocha, B.; Tobola, J.; Kaprzyk, S. Importance of relativistic effects in electronic structure and thermopower calculations for Mg2Si, Mg2Ge, and Mg2Sn. *Phys. Rev. B* 2014, 89, 115205. [CrossRef]

60. Guo, S.D. Importance of spinCorbit coupling in power factor calculations for half-Heusler ANiB (A = Ti, Hf, Sc, Y.; BSn, Sb, Bi). *J. Alloys Compd.* 2016, 663, 128–133. [CrossRef]

61. Larson, P.; Mahanti, S.D.; Kanatzidis, M.G. Electronic structure and transport of Bi2Te3 and BaBiTe3. *Phys. Rev. B* **2000**, *61*, 8162. [CrossRef]

62. Scheidemantel, T.J.; Ambrosch-Draxl, C.; Thonhauser, T.; Badding, J.V.; Sofo, J.O. Transport coefficients from first-principles calculations. *Phys. Rev. B* **2003**, *68*, 125210. [CrossRef]

63. Chen, M.C. A quick thermoelectric technique for typing HgCdTe at liquid nitrogen temperature. *J. Appl. Phys.* **1992**, *71*, 3636–3638. [CrossRef]

64. Guo, S.D.; Wang, Y.H. Thermoelectric properties of orthorhombic group IV-VI monolayers from the first-principles calculations. *J. Appl. Phys.* **2017**, *121*, 034302. [CrossRef]

65. Shi, H.L.; Ming, W.M.; Parker, D.S.; Du, M.H.; Singh, D.J. Prospective high thermoelectric performance of the heavily p-doped half-Heusler compound CoVSn. *Phys. Rev. B* **2017**, *95*, 195207. [CrossRef]

66. Frank, S.; Kuntscher, C.A.; Gregora, I.; Petzelt, J.; Yamauchi, T.; Ueda, Y. Pressure-induced changes in the optical properties of quasi-one-dimensional β-Na0.33 V2O5. *Phys. Rev. B* **2007**, *76*, 075128. [CrossRef]

67. Meng, J.F.; Shekar, N.V.C.; Chung, D.-Y.; Kanatzidis, M.; Badding, J.V. Improvement in the thermoelectric properties of pressure-tuned β-K2Bi8Se13. *J. Appl. Phys.* **2003**, *94*, 4485–4488. [CrossRef]

68. Ovsyannikov, S.V.; Shchennikov, V. Pressure-tuned colossal improvement of thermoelectric efficiency of PbTe. *Appl. Phys. Lett.* **2007**, *90*, 122103. [CrossRef]

69. Ovsyannikov, S.V.; Shchennikov, V.V.; Vorontsov, G.V.; Manakov, A.Y.; Likhacheva, A.Y.; Kulbachinskii, V.A. Giant improvement of thermoelectric power factor of Bi2Te3 under pressure. *J. Appl. Phys.* **2008**, *104*, 053713. [CrossRef]

70. Weber, W. Lattice Dynamics of Transition-Metal Carbides. *Phys. Rev. B* **1973**, *8*, 5082–5092. [CrossRef]

71. Jain, S.C.; Willis, J.R.; Bullogh, R. A review of theoretical and experimental work on the structure of GexSi1−x strained layers and superlattices, with extensive bibliography. *Adv. Phys.* **1990**, *39*, 127–190. [CrossRef]

72. David, J.G. Optical Properties of Solids. *Am. J. Phys.* **2002**, *70*, 1269. [CrossRef]

73. Pourghazi, A.; Dadsetani, M. Electronic and optical properties of BaTe, BaSe and BaS from first principles. *Phys. B Condens. Matter.* **2005**, *370*, 35–45. [CrossRef]

74. Verma, A.S.; Kumar, A.; Bhardwaj, S.R. Correlation between ionic charge and the lattice constant of cubic perovskite solids. *Phys. Status Solidi B* **2008**, *245*, 1520–1526. [CrossRef]