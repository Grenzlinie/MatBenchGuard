![](./images/812566032433545217_1.jpg)

Applied Surface Science 537 (2021) 147883

Contents lists available at ScienceDirect

# Applied Surface Science

journal homepage: www.elsevier.com/locate/apsusc

![](./images/812566032433545217_2.jpg)

# Investigations of the stability and electronic properties of two-dimensional Ga₂O₃ nanosheet in air from first-principles calculations

![](./images/812566032433545217_3.jpg)

Linpeng Dong $^{a,*}$, Shun Zhou $^{a}$, Bin Xin $^{b}$, Chen Yang $^{a}$, Jin Zhang $^{a}$, Huan Liu $^{a}$, Lichun Zhang $^{c}$, Chuanlu Yang $^{c}$, Weiguo Liu $^{a}$

$^{a}$ Shaanxi Province Key Laboratory of Thin Films Technology & Optical Test, Xi'an Technological University, Xi'an 710032, China
$^{b}$ Physical Sciences and Engineering Division, King Abdullah University of Science and Technology (KAUST), Thuwal 23955-6900, Saudi Arabia
$^{c}$ School of Physics and Optoelectronics Engineering, Ludong University, Yantai 26425, China

---

## ARTICLE INFO

**Keywords:**
Ga₂O₃ nanosheet
Stability
Electronic properties
First-principles calculation

## ABSTRACT

2D Ga₂O₃ nanosheet with ultra-high carrier mobility and wide bandgap has gained extensively interests due to its great potential in next generation of solar-bind photodetectors, high-power devices, and gas sensors. However, the study of the stability and air-resistance of Ga₂O₃ nanosheet is scare up to now. Herein, we investigate the stability and electronic properties of Ga₂O₃ in air through first-principles calculations. It is found that $O_2$ molecule can physisorb on Ga₂O₃ nanosheet with the binding energy of −0.12 eV, while it is very hard to dissociate spontaneously due to an extremely high dissociation energy barrier of 4.78 eV. The $O_2$ molecule physisorption can introduce extra energy levels in the bandgap and affect the optical properties of Ga₂O₃ nanosheet. While $H_2O$ molecule adsorption has weak effects on the structural and electronic properties of Ga₂O₃ nanosheet. The high air-resistance of Ga₂O₃ nanosheet is attributed to the strong charge transfer between the Ga and O ions, which avoids the surplus electrons induced by the dangling bonds to interact with foreign molecules. These theoretical results indicate Ga₂O₃ nanosheet has extremely high stability to resist oxidation and humid environment, which is a very promising next-generation 2D material for high-power and ultraviolet applications.

---

## 1. Introduction

The advent of graphene has stimulated the boom of two-dimensional (2D) semiconductors beyond graphene, among which black phosphorene (BP) is the most representative one and has attracted extensive attentions in recent years [1–4]. The large surface-to-volume ratio and electron confinement effect endow these 2D materials with bizarre features such as high carrier mobility, wide bandgap, superior thermal conductivity, and strong light adsorption [5–7]. For example, graphene exhibits ultrahigh carrier mobility, superior thermal conductivity and mechanical capacity. However, the absence of bandgap and small spin–orbit coupling (SOC) greatly restrict its potential applications [8]. Compared with graphene, BP possesses a sizable direct bandgap (~0.3–2.0 eV) and high carrier mobility (~1000 cm²V⁻¹s⁻¹), thus has been successively adopted for spintronic and optoelectronic applications [3]. Unfortunately, BP is easily degraded under ambient conditions ascribed to the lone-pair electrons on the surfaces, which severely hinders its future prospective applications [9,10]. From a promising and practical view, both superior electronic properties and air-resistance are necessary for the scaling applications of the novel 2D materials. From this point, novel 2D materials possess both superior electronic properties and air-resistance at the same time are still pursued and explored. For instance, 2D group-IV monochalcogenides (GeS, GeSe, SnS, and SnSe) are found with high activation energies ranged from 1.26 to 1.60 eV, which are much higher than phosphorene and arsenene [11,12]. Optical measurements indicated both GeS and GeSe reveal indirect bandgaps of 1.58 and 1.14 eV, respectively [13]. However, this narrow and indirect bandgap of GeS and GeSe restrict these materials in high-power and ultraviolet optical devices.

Except for group-IV monochalcogenides, 2D metal oxides are considered with natural oxidation resistant ability thus are believed to have high stability in air [14]. Recently, 2D Ga₂O₃ nanosheet with wide bandgap has gained extensively interests due to its great potential in next-generation solar-bind photodetectors, high-power devices, gas sensors, and battery anodes [15–18]. Compared with bulk counterpart, 2D Ga₂O₃ exhibits ultra-high carrier mobility, wider bandgap, and is compatible with other p-type 2D materials to form high-quality heterojunctions to overcome the lattice mismatch issue of the bulk counterpart. Early fabrications of Ga₂O₃ nanosheet are through the “top-down” approach by cleaving along (100) direction of bulk β-Ga₂O₃

---

* Corresponding author.
E-mail addresses: lpdong@xatu.edu.cn (L. Dong), bin.xin@kaust.edu.sa (B. Xin).

https://doi.org/10.1016/j.apsusc.2020.147883
Received 31 July 2020; Received in revised form 30 August 2020; Accepted 11 September 2020
Available online 16 September 2020
0169-4332/ © 2020 Elsevier B.V. All rights reserved.

directly [16,19]. The devices based on these cleaved 2D or quasi-2D $Ga_2O_3$ show excellent performances compared with the bulk counterpart. For instance, the phototransistor based on the cleaved Cr-doped $Ga_2O_3$ exhibits ultra-high responsivity $(4.79 \times 10^5$ A/W) and external quantum efficiency $(2.34 \times 10^6)$ at the same time [20]. Kim et al. fabricated monolithically integrated enhancement-mode and depletion-mode field-effect transistors (FET) based on quasi-2D $Ga_2O_3$, both FETs displayed excellent electrical characteristics, and can be further monolithically integrated as a logic inverter [16]. Apart from direct cleaving method, 2D $Ga_2O_3$ nanosheet can also be fabricated through the "bottom-up" approach. Recently, Zhang et al. synthesized $Ga_2O_3$ nanosheet through a simple crystalline phase transition from the ultrathin $\gamma$-$Ga_2O_3$ nanosheets [21]. Yang et al. also reported direct preparation of $Ga_2O_3$ nanosheet via oxygenic groups contained hydrophilic graphene oxide template [18].

Despite the successful fabrications and applications of $Ga_2O_3$ nanosheet experimentally, as well as the exfoliation mechanism, optical and electronic properties were investigated theoretically [15,22-25]. However, study focus on the stability of $Ga_2O_3$ nanosheet in air is absent up to now. Beside, previous studies show that bulk $\beta$-$Ga_2O_3$ surface was stable and can interact with specific molecules [26-28], the results indicate surface play an important role in the electronic properties of $\beta$-$Ga_2O_3$. Taking the much higher specific surface area of $Ga_2O_3$ nanosheet into consideration, the stability and electronic properties of $Ga_2O_3$ nanosheet are expected more sensitive when exposes to air. As a contrast, same studies on phosphorene, graphene, and group-IV monochalcogenides are enrich in the past years [11,29-31]. What is more, seeking wide bandgap semiconductors with strong stability in air is necessary and meaningful to replenish the present 2D nanosheets for applications in harsh environment. Motivated by these issues, here we investigate the stability of $Ga_2O_3$ nanosheet in air for the first time, the $O_2$ and $H_2O$ molecules are considered as the main factors which can affect and degrade the properties of 2D nanosheets in air [29,31]. Focus on this issue, the rest of our paper is organized as follows: in Section 2, the computational methods were introduced. In Section 3, we presented and discussed our calculated results in detail, including the physisorption and chemisorption for $O_2$ and $H_2O$ molecules on $Ga_2O_3$ nanosheet, respectively. The adsorption configuration, binding energy, and electronic properties were calculated and discussed. Finally, a brief conclusion was given in Section 4.

## 2. Computational methods

All calculations of this work were performed on the basis of density functional theory (DFT) framework. The projector augmented wave (PAW) method and the Perdew-Burke-Ernzerhof (PBE) functional under generalized gradient approximation (GGA) were adopted [32,33], as implemented in the Vienna ab initio simulation package (VASP) code [34]. The DFT-D2 method of Grimme was used to take care of the contributions from the van der Waals (vdW) interactions [35]. The geometry optimizations were performed until the Hellmann-Feynman force acting on per atom was less than 0.01 eV/Å, the energy convergence criterion was set to $1 \times 10^{-6}$ eV. The kinetic energy cut-off for planewave basis set was set to 450 eV, the Monkhorst-Pack k-point mesh of $6 \times 4 \times 1$ was sampled with a resolution of $0.02 \times 2\pi$ Å$^{-1}$ in the first Brillouin zone (FBZ). The geometry optimizations were performed until the Hellmann-Feynman force acting on per atom was less than 0.01 eV/Å, the energy convergence criterion was set to $1 \times 10^{-6}$ eV. The kinetic energy cut-off for plane-wave basis set was set to 450 eV, the Monkhorst-Pack k-point mesh of $6 \times 4 \times 1$ was sampled with a resolution of $0.02 \times 2\pi$ Å$^{-1}$ in the first Brillouin zone (FBZ).

An orthorhombic $3 \times 2 \times 1$ supercell was constructed to describe the interactions between the $Ga_2O_3$ nanosheet and gas molecules. A vacuum buffer space of $20$ Å perpendicular to the in-plane of $Ga_2O_3$ nanosheet was set to avoid the spurious interaction between periodic images. The supercell was built based on the optimized pristine $Ga_2O_3$ nanosheet unit cell, whose lattice parameters are $a = 2.98$ Å and $b = 5.76$ Å, which is based on our previous result [25] and consistent with other reported results [15,36]. The climbing-image nudged elastic band (CI-NEB) method was used to determine the adsorption and dissociation path of $O_2$ molecule [37], and five imagines were inserted in the reaction path.

In analogy with the extensively studied 2D materials, the adsorption of triplet $O_2$ molecule plays an important role on the electronic and stability of pristine 2D materials. To characterize the chemical stability of $Ga_2O_3$ nanosheet in the specific atmosphere environment, the binding energies ($E_{bind}$) between the monolayer substrate and gas molecules were calculated as follows:

$$
E_{bind} = E_{Ga_2O_3+mol} - E_{Ga_2O_3} - E_{mol}
$$

where $E_{Ga2O3+mol}$, and $E_{Ga2O3}$ are the total energies of gas molecule adsorbed and pristine $Ga_2O_3$ nanosheet, respectively, $E_{mol}$ is the energy of the free gas molecule. In general, an exothermic reaction process with negative formation energy preferable in the adsorption process, which leading to a more stable adsorption configuration. In the subsequent investigations, both $O_2$ and $H_2O$ molecules physisorption (intact molecule adsorption) and chemisorption (dissociative adsorption, involving the dissociation of the O-O bond for $O_2$ molecule and O-H bond for $H_2O$ molecule) cases were studied and discussed.

## 3. Results and discussion

Different from traditional 2D materials which generally possess high symmetrical lattice structure and less adsorption sites, 2D $Ga_2O_3$ nanosheet with poor structure symmetry and rugged surfaces thus more adsorption sites are expected to participate in real adsorption process. Here, possible adsorption sites on $Ga_2O_3$ nanosheet including the top sites over the surface and interlaminar O ions (site T1 and T2), the top sites over the octahedral and tetrahedral Ga ions (site T3 and T4), the hollow sites over the bottom tetrahedral Ga ion (site H5) and the center of the octahedral Ga—surface O—octahedral Ga—surface O consisted quadrangle (site H6), the bridge sites at the midpoint of the three nonequivalent Ga-O bonds (site B7, B8, and B9), were taken as the initial guess adsorption configurations, as shown in Fig. 1(a) and (b). In addition, molecular orientation (either parallel or vertical with specific rotation angle to the baseline of $Ga_2O_3$ nanosheet) matters the adsorption results, and these factors were also taken into consideration in our calculations [38].

Fig. 2(a) presents the top and side views of the most energy favorable configuration for $O_2$ molecule physisorption on $Ga_2O_3$ nanosheet. Among various possible adsorption sites, the hollow site H5 over the bottom tetrahedral Ga ion is the most energy favorable adsorption site. The $O_2$ molecule prefers to occupy the center of the hollow site, where the O-O bond is aligned parallelly with the line between the two adjacent octahedral Ga ions. The bond length of the $O_2$ molecule is 1.23 Å, which coincides with the value of the free one. The distance between the O atom in $O_2$ molecule and the adjacent octahedral Ga ion is 3.27 Å, which is much larger than the Ga-O bonds in $Ga_2O_3$ nanosheet (1.85 and 1.98 Å). Compared with pristine $Ga_2O_3$ nanosheet, the atomic position of the structure with $O_2$ molecule physisorption changes very obscurely. All these structure profiles indicate the interaction between the $O_2$ molecule and $Ga_2O_3$ nanosheet is very weak, which exhibits typical physisorption characteristics.

To further evaluate the effects induced by $O_2$ physisorption, the binding energy $E_{bind}$ and total amount of charge transfer $\Delta Q$ were calculated, the results were listed in Table 1. The binding energy for $O_2$ is $-0.12$ eV, which is smaller than the value of phosphorene ($-0.27$ eV) [39]. However, different from the case over phosphorene, whose binding energy does not sensitively depend on the specific location or orientation of the $O_2$ molecule, the configuration presented in Fig. 2(a) possesses the most negative binding energy among the 27 initial guess configurations. Fig. 2(b) plots the $O_2$ molecular orbital-projected band

![](./images/812566032433545217_4.jpg)

Fig. 1. Perspective (a) and top views (b) of 2D Ga₂O₃ sheet, the adsorption sites are also denoted.

structure of the Ga₂O₃ nanosheet with O₂ physisorption, a wide direct bandgap with a value of 2.43 eV can be observed. The band structure and bandgap are intact compared with pristine Ga₂O₃ nanosheet (Fig. S1). It can be seen that two extra levels induced by O₂ molecule are presented in the bandgap. The weight factor of the levels induced by O₂ molecule in the bandgap distributes uniformly over the whole FBZ, which inherits the feature from the free O₂ molecule. Fig. 2(c) shows the local density of states (LDOS) for the Ga₂O₃ nanosheet with O₂ physisorption, all the states near the Fermi level induced by O₂ are highly localized and separated. The highest occupied molecular orbital (HOMO) (2π, spin-up) of O₂ molecule is 0.10 eV under the valence band maximum (VBM), and the lowest unoccupied molecular orbital (LUMO) (2π*, spin-down) is 0.16 eV under the conduction band minimum (CBM). From the band structure and LDOS, we conclude that the O₂ molecule is weakly bounded on the 2D Ga₂O₃ nanosheet through vdW interaction, and there is no further bond forming and orbital hybridization happens. In addition, the VBM and CBM inherit the trait of pristine Ga₂O₃ nanosheet, which means the carrier effective masses are almost unaffected, thus the O₂ physisorption has little impact on the transport property of Ga₂O₃ nanosheet. However, the extra states in the

<table>
<caption>Table 1
The binging energy $E_{bind}$, the shortest distance $d$ from the molecule to the Ga₂O₃ nanosheet, the total amount of charge transfer $\Delta Q$ from molecules to the Ga₂O₃ nanosheet. Note that a positive (negative) $\Delta Q$ indicates a loss (gain) of electrons.</caption>
<thead>
<tr>
<th>Molecule/ion</th>
<th>$E_{bind}$ (eV)</th>
<th>$d$ (Å)</th>
<th>$\Delta Q$ (e)</th>
</tr>
</thead>
<tbody>
<tr>
<td>O₂</td>
<td>−0.12</td>
<td>2.84</td>
<td>$1.2 × 10^{-4}$</td>
</tr>
<tr>
<td>O₂²⁻(×2)</td>
<td>4.55</td>
<td>1.89</td>
<td>$-1.9 × 10^{-3}$</td>
</tr>
<tr>
<td>H₂O</td>
<td>−0.62</td>
<td>2.03</td>
<td>$9.0 × 10^{-4}$</td>
</tr>
<tr>
<td>HO⁻/H⁺</td>
<td>–</td>
<td>–</td>
<td>–</td>
</tr>
<tr>
<td>O₂ (O₂ + H₂O, long)</td>
<td>−0.11</td>
<td>2.85</td>
<td>$1.2 × 10^{-4}$</td>
</tr>
<tr>
<td>H₂O (O₂ + H₂O, long)</td>
<td>−0.62</td>
<td>2.04</td>
<td>$9.0 × 10^{-4}$</td>
</tr>
<tr>
<td>O₂ (O₂ + H₂O, close)</td>
<td>−0.12</td>
<td>2.85</td>
<td>$1.2 × 10^{-4}$</td>
</tr>
<tr>
<td>H₂O (O₂ + H₂O, close)</td>
<td>−0.63</td>
<td>2.04</td>
<td>$9.1 × 10^{-4}$</td>
</tr>
</tbody>
</table>

Ga₂O₃ nanosheet bandgap can enhance the transition probability of the non-radiative decay during the photoexcitation process. The photogenerated electrons can transfer from the CBM to these intermediate molecular states and further be trapped by the adsorbed O₂ molecule, forming a negative O₂⁻ (positive O₂⁺) to trap extra holes (electrons).

![](./images/812566032433545217_5.jpg)

Fig. 2. 2D Ga₂O₃ nanosheet with O₂ molecule physisorption: (a) The top and side views of the lowest-energy configuration. (b) The spin-polarized O₂ molecule-orbital-projected band structure, the pink balls represent the orbital-projected from the adsorbed O₂ molecule. (c) The total DOS and LDOS distributions. (d) The charge difference isosurface distribution, the yellow and cyan regions denote the gain and loss of electrons, respectively. The value of the isosurface was set to 0.001 e/Å³. (e) The line profiles of the plane-averaged $\Delta \rho$ (green line) and the transferred charge amount $\Delta Q$ (red line) along c direction.

Actually, previous studies indicated that the photo-generated holes can be trapped by $O_2^-$ (caused by the oxygen vacancies), which prolongs the carrier lifetime and increases the photocurrent of the quasi-2D and $Ga_2O_3$ nanowire photodetector [40]. Considering the much larger specific surface area of nanosheet, the $O_2$ physisorption will have a more noteworthy effect on the photoelectric properties of $Ga_2O_3$ nanosheet. Fig. 2(d) shows the charge difference isosurface distribution, it can be seen that there is a tiny part of electrons accumulation on the $Ga_2O_3$ nanosheet side, and a loss of electrons in the proximity of the $O_2$ molecule. The transferred electrons from $O_2$ molecule mainly distribute on the adjacent O ions rather than the tetrahedral Ga ions of $Ga_2O_3$ nanosheet, which attributes to the strong electron extraction ability caused by the abruptly broken $Ga-O$ bonds in the forming of 2D $Ga_2O_3$. Fig. 2(e) plots the line profiles of the plane-averaged $\Delta\rho$ (green line) and the transferred charge amount $\Delta Q$ (red line) along c direction. There is only $1.2\times10^{-4}$ charge transferred from $O_2$ molecule to $Ga_2O_3$ nanosheet, further indicating a weak coupling interaction between the $O_2$ molecule and $Ga_2O_3$ nanosheet.

After physisorption, the adsorbed $O_2$ molecule has a potential to further dissociate on the substrate surface. Previous studies on phosphorene and monolayer group-IV monochalcogenides indicated that the physisorption $O_2$ can dissociate and chemisorb on the substrate, the structural and electronic properties of the 2D substrates were further modulated by the $O_2$ molecule chemisorption [11]. Herein, here we examine the process of the $O_2$ molecule chemisorption. Fig. 3(a) shows the top and side views of the lowest-energy configuration for $Ga_2O_3$ nanosheet with $O_2$ molecule chemisorption. The bond between the two O atoms enlarges and breaks with a distance of $2.25$ Å, subsequently these two O atoms link to the nearby octahedral Ga ions. The octahedral Ga ions are slightly extracted by $0.15$ Å perpendicular to the nanosheet, the $Ga-O$ bonds are $2.02$ Å with the $O-Ga-Ga$ bond angle of $78.13^\circ$.

Fig. 3(b) and (c) present the spin-polarized band structures and LDOS of the $Ga_2O_3$ nanosheet with $O_2$ molecule chemisorption. Different from the physisorption case, the typical molecular orbital feature of $O_2$ molecule vanishes after chemisorption, the LDOS originates from $O_2$ are non-localized and broaden significantly. Several defect-like states present in the bandgap of $Ga_2O_3$ nanosheet, the weight factor distribution induced by the extra O atoms is non-uniform over the FBZ, which indicates a typical chemical bonding between the O atoms and $Ga_2O_3$ nanosheet. The bandgap is 2.43 eV (Fig. 3(b)), which is consistent with the pristine $Ga_2O_3$ nanosheet (Fig. S1), and four defective levels distribute range from 0.15 eV above the VBM to 0.72 eV under the CBM. Fig. 3(d) shows the charge difference isosurface of the $Ga_2O_3$ nanosheet with $O_2$ molecule chemisorption, it can be seen that a stronger charge transfer happens compared with the physisorption case (Fig. 2(d)). Electrons accumulate between the chemisorbed O atoms and octahedral Ga ions, and deplete mainly on the nearby surface O ions. The net charge transfer from $Ga_2O_3$ nanosheet to O atoms is $1.9\times10^{-3}$ $e$ (Fig. 3(e)), which is significantly larger than the $O_2$ molecule physisorption case. However, this value is still smaller than the net charge transfer in the $O_2$ physisorption on phosphorene (0.036) [30], and antimonene (0.116) [41], let alone the chemisorption cases. From the energy view, the calculated binding energy for $O_2$ is as high as 4.55 eV, and this high positive binding energy is an energy unfavorable process for the $O_2$ molecule chemisorption, thus it is very hard to implement spontaneously.

Different from phosphorene and Group-IV Monochalcogenides, when these 2D nanosheets adsorbed with $O_2$ molecule, an exothermic dissociation process is expected and the substrates are liable to oxidate [11,29]. Fig. 4 plots the reaction pathway obtained from CI-NEB calculations for the dissociation process of the physisorbed $O_2$ molecule on $Ga_2O_3$ nanosheet to chemisorbed state. The $O_2$ molecule is physisorbed on the $Ga_2O_3$ nanosheet with a distance of $2.84$ Å at the initial state, then the molecule approaches the substrate until the distance is down to $2.12$ Å to reach the transition state. The bond length of the $O_2$ molecule prolongs from 1.23 to $2.00$ Å and breaks on the $Ga_2O_3$ nanosheet surface. As the reaction continues, the bond length of the $O_2$ molecule further prolongs to $2.25$ Å to reach the final state, with a distance of $2.02$ Å to the $Ga_2O_3$ nanosheet. From the dissociation process pathway, the energy barrier $E_b$ is as high as 4.78 eV, which is much higher than other 2D materials, such as phosphorene (0.54 eV) [29], GeS (1.26 eV) [11], and SnS (1.60 eV) [11]. This ultra-high $E_b$ indicate $Ga_2O_3$ nanosheet possesses extremely oxidation resistance.

Except for oxidation, the stability of $Ga_2O_3$ nanosheet when

![](./images/812566032433545217_6.jpg)

Fig. 3. 2D $Ga_2O_3$ nanosheet with $O_2$ molecule chemisorption: (a) The top and side views of the lowest-energy configuration. (b) The spin-polarized atom-orbital-projected band structure, the pink balls represent the orbital-projected from the adsorbed O atoms. (c) The total DOS and LDOS distributions. (d) The charge difference isosurface distribution, the yellow and cyan regions denote the gain and loss of electrons, respectively. The value of the isosurface was set to $0.005$ e/Å³. (e) The line profiles of the plane-averaged $\Delta\rho$ (green line) and the transferred charge amount $\Delta Q$ (red line) along c direction.

![](./images/812566032433545217_7.jpg)

Fig. 4. Reaction pathway obtained from CI-NEB calculations for the dissociation process of the physisorbed $O_2$ molecule on $Ga_2O_3$ nanosheet to chemisorbed state, the atomic configurations of the initial, transition, and final states are also presented.

exposures to moist environment is also a matter of great concern, which ensures the applicability of the $Ga_2O_3$ nanosheet-based devices in humid conditions. Here we evaluated the $H_2O$ molecule physisorption and chemisorption to examine the moist resistance of the $Ga_2O_3$ nanosheet, respectively. Compared with $O_2$ molecule, non-linear $H_2O$ molecule has more adsorption configurations when adsorbed on $Ga_2O_3$ nanosheet. There are 48 initial $H_2O$ molecule physisorption configurations, the most energy favorable configuration was picked out and presented in Fig. 5(a). It can be seen that the $H_2O$ molecule adopts a flat alignment relative to $Ga_2O_3$ nanosheet basal plane, the bond angle of the $H_2O$ molecule nearly coincides with the underneath O—Ga—O bond, the distance between the $H_2O$ molecule and substrate is 2.22 Å. This adsorption configuration is similar with the result of antimonene [41], but visibly distinguish from the result of phosphorene [31]. The bond length and angle for the adsorbed $H_2O$ molecule are 0.98 Å and $104.75^\circ$, respectively, which are comparable with the parameters in free $H_2O$ molecule (0.97 Å and $104.48^\circ$). From the feature of atomic structure, a weak interaction between the $H_2O$ molecule and $Ga_2O_3$ nanosheet is expected.

Fig. 5(b) and (c) present the band structure and LDOS of the $Ga_2O_3$ nanosheet with $H_2O$ molecule physisorption. Different from the $O_2$ molecule physisorption or chemisorption, no additional levels presented within the bandgap of the $Ga_2O_3$ nanosheet, and the bandgap is almost unchanged (2.31 eV) compared with pristine $Ga_2O_3$ nanosheet. The HOMO ($1b_1$) and second-HOMO ($3a_1$) of $H_2O$ molecule significantly broaden and coincide with the valence states of $Ga_2O_3$ nanosheet, which is also distinguished from the results of the $O_2$ molecule physisorption. While $1b_2$ orbital is highly localized and inherits the typical molecular orbital feature. From the results presented in Fig. 5(b) and (c), we conclude the interaction between the $H_2O$ molecule and $Ga_2O_3$ nanosheet is stronger than the case of the $O_2$ molecule physisorption. However, the overall interaction is still weak considering the independent molecular orbital $1b_2$. The charge difference distribution (Fig. 5(d)) indicates that electrons are exhausted on the $H_2O$ molecule and accumulated at the $Ga_2O_3$ nanosheet side. The net charge transfers from $H_2O$ molecule (Fig. 5(e)) to $Ga_2O_3$ nanosheet is $9.0\times10^{-4}\ e$, a very weak bond is formed between the O atom of $H_2O$ molecule and the underneath Ga ion. It is noted that there is a part of electrons accumulate on the nearby surface O ions of $Ga_2O_3$ nanosheet, which is attributed to the strong extraction ability of the surface O ions due to the existence of dangling bonds.

For the case of $H_2O$ molecule chemisorption, the hydrogen bond breaks at first, $H^+$ and $OH^-$ form and subsequently interact with the surface ions of $Ga_2O_3$ nanosheet. However, our calculated results indicate that the dissociative $H^+$ and $OH^-$ interact very strong and prefer to form $H_2O$ molecule rather than bond directly to the $Ga_2O_3$ nanosheet surface. Further structural optimization gives a consistent result with the physisorption case. Considering the weak interaction between $H_2O$ molecule and $Ga_2O_3$ nanosheet from our former results, $Ga_2O_3$ nanosheet thus can withstand humid environment with no obvious performance degradations.

Previous studies reveal that the electronic and optical properties of phosphorene, SnS, and GeSe degraded easier in the presence of both $O_2$ and $H_2O$ atmosphere, while the degradation process decelerated with exposure to $O_2$ atmosphere only [30,31]. For instance, the oxidized phosphorene surface becomes more super-hydrophilic, which leading to

![](./images/812566032433545217_8.jpg)

Fig. 5. 2D $Ga_2O_3$ nanosheet with $H_2O$ molecule physisorption: (a) The top and side views of the lowest-energy configuration. (b) The atom-orbital-projected band structure. (c) The total DOS and LDOS distributions. (d) The charge difference isosurface distribution, the yellow and cyan regions denote the gain and loss of electrons, respectively. The value of the isosurface was set to $0.005\ e/\mathring{A}^3$. (e) The line profiles of the plane-averaged $\Delta\rho$ (green line) and the transferred amount of charge $\Delta Q$ (red line) along c direction.

![](./images/812566032433545217_9.jpg)

Fig. 6. The $Ga_2O_3$ nanosheet adsorbed with $O_2$ and $H_2O$ molecules simultaneously, the distance between $O_2$ and $H_2O$ molecules are different: (a) The long interaction, (b) The close interaction.

the accelerated degradation process in air [31]. In order to examine whether the hydrophilia of $Ga_2O_3$ nanosheet after adsorbed with $O_2$ molecule, both $O_2$ and $H_2O$ molecules were adsorbed simultaneously on the $Ga_2O_3$ nanosheet, as presented in Fig. 6(a). The binding energies for $O_2$ ($-0.11$ eV) and $H_2O$ molecules ($-0.62$ eV) adsorptions are almost unchanged compared with the corresponding isolated adsorption, as listed in Table 1. To further investigate the coupling effect as a function of the distance between $O_2$ and $H_2O$ molecules, a close interaction case was considered in Fig. 6(b). The locations and orientations of the physisorbed $O_2$ and $H_2O$ molecules are similar with the results in Fig. 6(a), and also consistent with the corresponding isolated physisorption systems. The binding energies for $O_2$ and $H_2O$ molecules are $-0.12$ and $-0.63$ eV, respectively. These results imply that the direct interaction between the adsorbed $O_2$ and $H_2O$ molecules is very weak, and is independent with their distance. Previous results indicate neither the $O_2$ molecule nor $H_2O$ molecule is difficult to dissociate and chemisorb on the $Ga_2O_3$ nanosheet substrate, thus the indirect interaction among the $Ga_2O_3$ nanosheet, $O_2$ and $H_2O$ molecules is weak. In other words, the stability of the $Ga_2O_3$ nanosheet is kept when exposes under both oxygen-rich and humid environment.

The superior oxidation and moist resistance of $Ga_2O_3$ nanosheet is promising for practical applications, which ensures the stability and repeatability of the $Ga_2O_3$ nanosheet based devices. To disclose the essence of the resistance features, Bader charges of the $Ga_2O_3$ nanosheet were calculated [42]. The calculated Bader charges of the octahedral and tetrahedral Ga ions are $+1.849$ and $+1.769$ $e$, respectively, while those for the surface (two types) and interbedded O ions (one type) are $-1.196$, $-1.195$ and $-1.219$ $e$, respectively. Strong charge transfer happens between Ga and O ions in both the surface and interbedded layers, there is more than $2.965$ $e$ transfers from Ga to O ions. The surplus electrons induced by the dangling bonds are redistributed to avoid interacting with the foreign molecules, making $Ga_2O_3$ nanosheet possesses excellent stability. As a contrast, phosphorene with covalent P-P bonds leads to a retention of lone-pair electrons on the surfaces, making phosphorene very active and vulnerable to oxidation. The charge transfer in $Ga_2O_3$ nanosheet is also much stronger than GeS ($0.21$ $e$) [11], which possesses much stronger oxidation resistance than phosphorene. All these results further indicate $Ga_2O_3$ nanosheet has extremely high stability to resist oxidation and humid environment, making $Ga_2O_3$ nanosheet a very promising next generation 2D material in the future applications.

## 4. Conclusions

Using first-principles calculations, here we investigate the air-resistance of $Ga_2O_3$ nanosheet in both oxidation and humid environment. It is found that the $O_2$ molecule can physisorb on the $Ga_2O_3$ nanosheet, while is very hard to dissociate spontaneously due to an extremely high dissociation energy barrier of 4.78 eV. The $O_2$ molecule physisorption can introduce extra energy levels in the bandgap, which will affect the optical properties of $Ga_2O_3$ nanosheet. As for $H_2O$ molecule, the results indicate it is liable to physisorb on $Ga_2O_3$ nanosheet and has weak effects on the structural and electronic properties of $Ga_2O_3$ nanosheet. The high air-resistance of $Ga_2O_3$ nanosheet is attributed to the strong charge transfer between the Ga and O ions, which avoids the surplus electrons induced by the dangling bonds to interact with the foreign molecules. These theoretical results indicate $Ga_2O_3$ nanosheet has extremely high stability to resist oxidation and humid environment, which is a very promising next-generation 2D material for high-power and ultraviolet applications.

## Declaration of Competing Interest

There are no conflicts to declare.

## Acknowledgements

This work is supported by the Key Research and Development Program of Shaanxi Province (2019ZDLGY16-01), Xi'an Key Laboratory of Intelligent Detection and Perception (201805061ZD12CG45).

## Author Contributions

Linpeng Dong, Bin Xin, and Weiguo Liu designed this project. Linpeng Dong performed the first principles calculations, analyzed the calculated results and wrote the original manuscript. Shun Zhou and Chen Yang checked the calculation results and modified the manuscript. Jin Zhang and Huan Liu modified the manuscript. Lichun Zhang and Chuanlu Yang applied the resources.

## Appendix A. Supplementary material

Supplementary data to this article can be found online at https://doi.org/10.1016/j.apsusc.2020.147883.

## References

[1] S. Stankovich, D.A. Dikin, G.H. Dommett, K.M. Kohlhaas, E.J. Zimney, E.A. Stach, R.D. Piner, S.T. Nguyen, R.S. Ruoff, Graphene-based composite materials, Nature 442 (2006) 282-286.
[2] X. Yu, H. Cheng, M. Zhang, Y. Zhao, L. Qu, G. Shi, Graphene-based smart materials, Nat. Rev. Mater. 2 (2017) 1-13.
[3] A. Carvalho, M. Wang, X. Zhu, A.S. Rodin, H. Su, A.H.C. Neto, Phosphorene: from theory to applications, Nat. Rev. Mater. 1 (2016) 1-16.
[4] E.S. Reich, Phosphorene excites materials scientists, Nature 506 (2014) 19.
[5] M. Gibertini, M. Koperski, A. Morpurgo, K. Novoselov, Magnetic 2D materials and heterostructures, Nat. Nanotechnol. 14 (2019) 408-419.
[6] K. Novoselov, A. Mishchenko, A. Carvalho, A.C. Neto, 2D materials and van der Waals heterostructures, Science 353 (2016).

[7] R. Mas-Balleste, C. Gomez-Navarro, J. Gomez-Herrero, F. Zamora, 2D materials: to graphene and beyond, Nanoscale 3 (2011) 20-30.

[8] M.J. Allen, V.C. Tung, R.B. Kaner, Honeycomb carbon: a review of graphene, Chem. Rev. 110 (2010) 132-145.

[9] J.O. Island, G.A. Steele, H.S. van der Zant, A. Castellanos-Gomez, Environmental instability of few-layer black phosphorus, 2D Mater. 2 (2015) 011002.

[10] M. Buscema, D.J. Groenendijk, S.I. Blanter, G.A. Steele, H.S. Van Der Zant, A. Castellanos-Gomez, Fast and broadband photoresponse of few-layer black phosphorus field-effect transistors, Nano Lett. 14 (2014) 3347-3352.

[11] Y. Guo, S. Zhou, Y. Bai, J. Zhao, Oxidation resistance of monolayer Group-IV monochalcogenides, ACS Appl. Mater. Inter. 9 (2017) 12013-12020.

[12] K. Pu, X. Dai, Y. Bu, R. Guo, W. Tao, D. Jia, J. Song, T. Zhao, L. Feng, Al-doped GeS nanosheet as a promising sensing material for O-contained volatile organic com- pounds detection, Appl. Surf. Sci. 527 (2020) 146797.

[13] D.D. Vaughn, R.J. Patel, M.A. Hickner, R.E. Schaak, Single-crystal colloidal na- nosheets of GeS and GeSe, J. Am. Chem. Soc. 132 (2010) 15170-15172.

[14] Y. Zhao, N. Liu, S. Zhou, J. Zhao, Two-dimensional ZnO for the selective photo- reduction of CO2, J. Mater. Chem. A 7 (2019) 16294-16303.

[15] Y. Liao, Z. Zhang, Z. Gao, Q. Qian, M. Hua, Tunable properties of novel Ga2O3 monolayer for electronic and optoelectronic applications, ACS Appl. Mater. Inter. 12 (2020) 30659-30669.

[16] J. Kim, J. Kim, Monolithically integrated enhancement-mode and depletion-mode beta-Ga2O3 MESFETs with graphene-gate architectures and their logic applications, ACS Appl. Mater. Inter. 12 (2020) 7310-7316.

[17] Z. Wu, Z. Jiang, P. Song, P. Tian, L. Hu, R. Liu, Z. Fang, J. Kang, T.Y. Zhang, Nanowire-seeded growth of Single-Crystalline (010) beta-Ga2 O3 nanosheets with high field-effect electron mobility and on/off current ratio, Small 15 (2019) e1900580.

[18] M. Yang, C. Sun, T. Wang, F. Chen, M. Sun, L. Zhang, Y. Shao, Y. Wu, X. Hao, Graphene-oxide-assisted synthesis of Ga2O3 nanosheets/reduced graphene oxide nanocomposites anodes for advanced alkali-ion batteries, ACS Appl. Energ. Mater. 1 (2018) 4708-4715.

[19] J. Bae, H.W. Kim, I.H. Kang, G. Yang, J. Kim, High breakdown voltage quasi-two- dimensional β-Ga2O3 field-effect transistors with a boron nitride field plate, Appl. Phys. Lett. 112 (2018) 122102.

[20] Y. Liu, L. Du, G. Liang, W. Mu, Z. Jia, M. Xu, Q. Xin, X. Tao, A. Song, Ga 2 O 3 field- effect-transistor-based solar-blind photodetector with fast response and high photo- to-dark current ratio, IEEE Electr. Device L. 39 (2018) 1696-1699.

[21] X. Zhang, H. Huang, Y. Zhang, D. Liu, N. Tong, J. Lin, L. Chen, Z. Zhang, X. Wang, Phase transition of two-dimensional beta-Ga2O3 nanosheets from ultrathin gamma- Ga2O3 nanosheets and their photocatalytic hydrogen evolution activities, ACS Omega 3 (2018) 14469-14476.

[22] S.K. Barman, M.N. Huda, Mechanism behind the easy exfoliation of Ga2O3 ultra- thin film along (100) surface, Phys. Status Solidi-R. 13 (2019) 1800554.

[23] H. Peelaers, C.G. Van de Walle, Lack of quantum confinement in Ga2O3 nanolayers, Phys. Rev. B. 96 (2017) 081409(R).

[24] J. Su, R. Guo, Z. Lin, S. Zhang, J. Zhang, J. Chang, Y. Hao, Unusual electronic and optical properties of two-dimensional Ga2O3 predicted by density functional theory, J. Phys. Chem. C 122 (2018) 24592-24599.

[25] L. Dong, S. Zhou, L. Gong, W. Wang, L. Zhang, C.-L. Yang, J. Yu, W. Liu, Structural and electronic properties modulation for 2D Ga2O3 by chemical passivation, J. Mater. Chem. C (2020), https://doi.org/10.1039/D0TC03279D.

[26] M.M. Branda, G.R. Garda, H.A. Rodriguez, N.J. Castellani, Methanol decomposition on the β-Ga2O3 (100) surface: A DFT approach, Appl. Surf. Sci. 254 (2007) 120-124.

[27] T.-F. Weng, M.-S. Ho, C. Sivakumar, B. Balraj, P.-F. Chung, VLS growth of pure and Au decorated β-Ga2O3 nanowires for room temperature CO gas sensor and resistive memory applications, Appl. Surf. Sci. 533 (2020) 147476.

[28] V. Nagarajan, R. Chandiramouli, Methane adsorption characteristics on β-Ga2O3 nanostructures: DFT investigation, Appl. Surf. Sci. 344 (2015) 65-78.

[29] A. Ziletti, A. Carvalho, D.K. Campbell, D.F. Coker, A.H. Castro Neto, Oxygen defects in phosphorene, Phys. Rev. Lett. 114 (2015) 046801.

[30] A.A. Kistanov, Y. Cai, K. Zhou, S.V. Dmitriev, Y.-W. Zhang, The role of H2O and O2 molecules and phosphorus vacancies in the structure instability of phosphorene, 2D Mater. 4 (2016) 015010.

[31] G. Wang, W.J. Slough, R. Pandey, S.P. Karna, Degradation of phosphorene in air: understanding at atomic level, 2D Mater. 3 (2016).

[32] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented- wave method, Phys. Rev. B. 59 (1999) 1758.

[33] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865.

[34] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy cal- culations using a plane-wave basis set, Phys. Rev. B. 54 (1996) 11169.

[35] S. Grimme, Semiempirical GGA-type density functional constructed with a long- range dispersion correction, J. Comput. Chem. 27 (2006) 1787-1799.

[36] Y. Wei, C. Liu, Y. Zhang, C. Qi, H. Li, T. Wang, G. Ma, Y. Liu, S. Dong, M. Huo, Modulation of electronic and optical properties by surface vacancies in low-di- mensional beta-Ga2O3, Phys. Chem. Chem. Phys. 21 (2019) 14745-14752.

[37] G. Mills, H. Jónsson, G.K. Schenter, Reversible work transition state theory: ap- plication to dissociative adsorption of hydrogen, Surf. Sci. 324 (1995) 305-337.

[38] S. Ma, D. Yuan, Y. Wang, Z. Jiao, Monolayer GeS as a potential candidate for NO2 gas sensors and capturers, J. Mater. Chem. C 6 (2018) 8082-8091.

[39] Y. Cai, Q. Ke, G. Zhang, Y.-W. Zhang, Energetics, charge transfer, and magnetism of small molecules physisorbed on phosphorene, J. Phys. Chem. C 119 (2015) 3102-3110.

[40] R. Zou, Z. Zhang, Q. Liu, J. Hu, L. Sang, M. Liao, W. Zhang, High detectivity solar- blind high-temperature deep-ultraviolet photodetector based on multi-layered (100) facet-oriented beta-Ga2O3 nanobelts, Small 10 (2014) 1848-1856.

[41] A.A. Kistanov, Y. Cai, D.R. Kripalani, K. Zhou, S.V. Dmitriev, Y.-W. Zhang, A first- principles study on the adsorption of small molecules on antimonene: oxidation tendency and stability, J. Mater. Chem. C 6 (2018) 4308-4317.

[42] G. Henkelman, A. Arnaldsson, H. Jónsson, A fast and robust algorithm for Bader decomposition of charge density, Comput. Mater. Sci. 36 (2006) 354-360.