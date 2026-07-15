Journal of Physics: Condensed Matter

ACCEPTED MANUSCRIPT

# High thermoelectric performance of half-Heusler compound BiBaK with intrinsically low lattice thermal conductivity

To cite this article before publication: Shihao Han *et al* 2020 *J. Phys.: Condens. Matter* in press https://doi.org/10.1088/1361-648X/aba2e7

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2020 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.
As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 130.237.122.245 on 12/07/2020 at 08:18

# High thermoelectric performance of half-Heusler compound BiBaK

with intrinsically low lattice thermal conductivity

S. H. Han, Z. Z. Zhou, C. Y. Sheng, J. H. Liu, L. Wang, H. M. Yuan and H. J. Liu*

Key Laboratory of Artificial Micro- and Nano-Structures of Ministry of Education and School of Physics and Technology, Wuhan University, Wuhan 430072, China

Half-Heusler compounds usually exhibit relatively higher lattice thermal conductivity that is undesirable for thermoelectric applications. Here we demonstrate by first-principles calculations and Boltzmann transport theory that the BiBaK system is an exception, which has rather low thermal conductivity as evidenced by very small phonon group velocity and relaxation time. Detailed analysis indicates that the heavy Bi and Ba atoms form a cage-like structure, inside which the light K atom rattles with larger atomic displacement parameters. In combination with its good electronic transport properties, the BiBaK shows a maximum $n$-type $ZT$ value of 1.9 at 900 K, which outperforms most half-Heusler thermoelectric materials.

## 1. Introduction

The search and development for new energy materials has become a top priority to overcome the increasingly serious energy crisis and environmental pollution. It is noteworthy that thermoelectric (TE) materials can convert heat into electricity directly, which has attracted widespread attention from the science community. The efficiency of a TE material depends on the dimensionless figure-of-merit ($ZT$), defined as
$$ZT = S^2\sigma T/(\kappa_l+\kappa_e)$$
where $S$, $\sigma$, $T$, $\kappa_l$, and $\kappa_e$ are the Seebeck coefficient, the electrical conductivity, the absolute temperature, the lattice thermal conductivity, and the electronic thermal conductivity, respectively. Over the past two decades, many strategies have been implemented successfully aiming to increase the power factor ($S^2\sigma$) and/or decrease the $\kappa_l$ [1–6]. However, it remains a challenge to significantly

*Author to whom correspondence should be addressed. Electronic mail: phlhj@whu.edu.cn

enhance the thermoelectric performance due to the inherent coupling of $S$, $\sigma$, and $\kappa_e$ [7].

Among various TE materials, half-Heusler (HH) compounds are potential candidates owing to their excellent electronic transport properties, which originate from moderate band gap and sharp density of states (DOS) around the Fermi level. For example, the $S^2\sigma T$ of HH alloys TilrAs, ZrIrSb, and ZrCoSb are more than 6 W/mK at 800 K [8], which surpass those of many good thermoelectric materials. However, a majority of HHs exhibit higher lattice thermal conductivity in the order of magnitude of 10 W/mK, which seriously restricts the improvement of their $ZT$ values [9-12]. During the past few years, more and more efforts have been focused on lowering the $\kappa_l$ to enhance the $ZT$ values by nano-structuring, doping, and alloying [9,12-18]. For example, it was found that a maximum $ZT$ of $\sim$1.5 can been obtained at 1200 K for the $p$-type $\text{FeNb}_{1-x}\text{Hf}_x\text{Sb}$ with $\kappa_l$ less than 5 W/mK [15]. Besides, a high $ZT$ of $\sim$1.2 can be achieved in the $n$-type $\text{Zr}_{1-x}\text{Hf}_x\text{NiSn}$ at 873 K, where the $\kappa_l$ is only about 2 W/mK [16]. However, these approaches may adversely affect the electronic transport properties. Hence, it is important to figure out what kind of HHs are prone to exhibit intrinsically lower $\kappa_l$.

Recently, it was reported that one of the HHs BiBaK exhibits unprecedentedly low $\kappa_l$ [19], which is calculated to be 2.19 W/mK at room temperature. It is thus interesting to check whether BiBaK could have good thermoelectric performance. In this work, we present a theoretical study on the structural, phonon, electronic and thermoelectric transport properties of BiBaK by adopting first-principles pseudopotential method and Boltzmann transport theory. We shall see that by optimizing the carrier concentration, a maximum $ZT$ value of 1.9 can be achieved at 900 K in the $n$-type system, which is much higher than those found in most HHs in their pristine form.

### 2. Computational method

In order to obtain the phonon dispersion relations of half-Heusler compound BiBaK, we combine the density functional theory (DFT) [20] calculations with the finite displacement method. The former is implemented in the Vienna *ab-initio* simulation package (VASP) [21] and the latter in the PHONOPY code [22], where a $3×3×3$ and $4×4×4$ supercell are respectively used in the second- and third-order interatomic force constants (IFCs). To obtain the phonon transport properties, we solve the linearized phonon Boltzmann transport equation embedded in the so-called ShengBTE package [23]. During the calculations, a cutoff radius of $7.7$ Å is imposed on the third-order interactions and we adopt a suitable $\boldsymbol{q}$-mesh as large as $31×31×31$ to get converged lattice thermal conductivity.

Within the framework of DFT, the calculations of electronic properties of BiBaK are performed using the projector augmented wave (PAW) method, where the exchange-correlation energy is in the form of Perdew-Burke-Ernzerhof (PBE) under the generalized gradient approximation (GGA) [24]. The hybrid functional of Heyd-Scuseria-Ernzerhof (HSE) [25] is adopted for more accurate band gap and electronic transport coefficients with the effect of spin-orbit coupling (SOC) taken into account. We use a Monkhorst-Pack $\boldsymbol{k}$-mesh of $15×15×15$ for sampling the Brillouin zone. The electronic transport coefficients including the Seebeck coefficient, the electrical conductivity, and the electronic thermal conductivity are evaluated from the semi-classical Boltzmann transport theory as implemented in the BoltzTraP code [26]. Considering the interaction between electrons and acoustic phonons, we use the deformation potential (DP) theory [27] to deal with the relaxation time.

## 3. Results and discussion

### 3.1 Structural properties

Ternary intermetallic HH compounds exhibit a crystal structure of $XYZ$ with space group $F\overline{4}3m$, where the $X$, $Y$, and $Z$ atoms are located in the Wyckoff positions of $4\mathrm{c}\left(\frac{1}{4},\ \frac{1}{4},\ \frac{1}{4}\right)$, $4\mathrm{b}\left(\frac{1}{2},\ \frac{1}{2},\ \frac{1}{2}\right)$, and $4\mathrm{a}\ (0,0,0)$, respectively. It was suggested that the 8 or 18 valence electrons per primitive cell can predict the electronic properties

of HHs [28–30], and their electronic structures are related to which of the three atoms occupies the 4c position [31]. In principle, one can have three inequivalent atomic configurations of HHs, namely, BiBaK, BaKBi, and KBiBa. Our first-principles calculations show that among them, the BiBaK exhibits the lowest energy with an optimized lattice constant of 8.45 Å. Besides, there is no imaginary frequency in the phonon spectrum, which means that the BiBaK compound is dynamically stable. To further test its stability, ab-initio molecular dynamics (AIMD) simulations have been performed. The AIMD runs for 5000 steps with a time step of 0.5 fs. Figure 1 shows the nearest Bi-Ba distance as a function of MD step at different temperatures. It can be seen that up to 900 K, there are only small fluctuations around the equilibrium bond lengths of 3.66 Å and the crystal structure remains unchanged. All these observations suggest that the BiBaK compound is rather stable. It should be mentioned that we have performed additional first-principles calculations on the total energies of other possible phases of such 1-1-1 materials. Among them, we find that the orthorhombic BiBaK is energetically unfavorable, while the energy of our cubic phase is only 0.04 eV/atom higher than that of the hexagonal one, suggesting the experimental possibility of the existence of HH compound BiBaK.

### 3.2 Phonon properties

As mentioned above, the BiBaK has ultralow lattice thermal conductivity compared with most HHs. To have a better understanding, we show in Figure 2 the phonon spectrums of BiBaK and other three HHs with $\kappa_{l}$ in excess of 10 W/mK at room temperature [32–34]. As the primitive cell of BiBaK contains three atoms, we see there are 9 phonon branches with 3 acoustic and 6 optical ones. The maximum frequency of BiBaK is no more than $120\ \mathrm{cm}^{-1}$, which is much lower than those of the other three HHs. Moreover, we observe obvious hybridization of acoustic branches and low-frequency optical branches in BiBaK, which means that phonon-phonon scatterings are more likely to occur than the other three systems. Figure 3(a) plots the phonon group velocities ($v$) of BiBaK as a function of frequency. For the TA and LA branches, the

calculated mean values are 1433 m/s and 2374 m/s, respectively. These results are comparable to those of good thermoelectric materials with lower lattice thermal conductivity, such as $Bi_2Te_3$ ($\kappa_l$=1.2 W/mK, $v_{TA}$=1630 m/s, $v_{LA}$=2650 m/s) [35] and PbTe ($\kappa_l$=2.1 W/mK, $v_{TA}$=1610 m/s, $v_{LA}$=3596 m/s) [36,37]. In contrast, the phonon group velocities of other three HHs in Fig. 2 are much higher, as indicated by their strong phonon dispersion relations. Furthermore, the calculated relaxation time of most phonon modes of BiBaK is in the range of 1~100 ps, which is comparable to that of $Bi_2Te_3$ [38]. All these findings suggest the BiBaK should have very small lattice thermal conductivity. Indeed, we see from Fig. 3(b) that the $\kappa_l$ is 1.82 at 300 K, which is very close to that calculated previously [19] and also confirms the reliability of our computational approach. As known, the $\kappa_l$ decreases with temperature and the value is only 0.60 at 900 K.

To figure out the physical origin of the intrinsically low $\kappa_l$ of the BiBaK compound, we show in Fig. 3(c) and Fig. 3(d) the projected phonon density of states (PDOS) and the cumulative lattice thermal conductivity, respectively. In the low-frequency region, we see that the Bi atom dominates the PDOS and the $\kappa_{cumu}$ increases quickly with the frequency. The rise becomes slowly in the medium-frequency region where the contribution from Ba atom is nearly the same as that of Bi atom, and the weak bonding between Bi and Ba atoms as well as the heavier atomic mass can result in lower sound velocity and Young's modulus [6,39,40]. Beyond the frequency gap in the range of 80~100 cm$^{-1}$, we find that $\kappa_{cumu}$ keeps almost unchanged where the K atom governs the PDOS, which suggests that it can lead to much stronger anharmonic scattering between phonons. To go further, we plot in Figure 4(a) the temperature dependence of the atomic displacement parameters (ADP) of BiBaK. We see that the ADP of K atom is obviously larger than those of Bi and Ba atoms, and their differences become more and more pronounced at elevated temperature. It should be mentioned that the cage-like materials such as skutterudites and clathrates have been suggested as good

thermoelectric systems [41–44] due to the well-known concept of "phonon-glass and electron-crystal" [41,45,46]. In such kind of structures, the multiple fillings of the portions in the host nanocages bring non-overlapping phonon vibrations so that the lattice thermal conductivity can be efficiently reduced [47]. The obviously larger ADP of K atom compared with those of Bi and Ba atoms is reminiscent of guest atoms "rattling" in the host cages. Indeed, we see from Fig. 4(b) that around each K atom, there is a hexadecahedron cage consisting of 4 Bi atoms and 6 Ba atoms in the crystal structure of BiBaK. Hence, it is reasonable to conclude that the heavy Bi and Ba atoms give the most contribution to $\kappa_{l}$. Meanwhile, the rattling of the guest K atoms inside the cage induces obvious phonon scattering and consequently reduces the $\kappa_{l}$.

### 3.3 Electronic properties

Figure 5 plots the electronic band structure of BiBaK, where we find an indirect band gap of ~0.75 eV with the conduction band minimum (CBM) and the valence band maximum (VBM) located at the $\Gamma$ and $X$ points, respectively. Note that both the CBM and VBM are doubly degenerated. The energy band near the CBM forms a steep valley while that around VBM is relatively flat, which suggests quite different effective mass for electrons and holes. It was previously demonstrated that high carrier mobility may stem from a steep valley at the $\Gamma$ point, where the valley-valley or peak-valley scatterings are inhibited [48]. It is thus reasonable to expect that the $n$-type BiBaK may have favorable electronic transport properties, as discussed in the following.

Before evaluating the transport coefficients, it is imperative to figure out the carrier relaxation time. As the major scattering mechanism is acoustic phonons, we adopt the deformation potential (DP) theory, where the relaxation time is given by $\tau$=$2\sqrt{2\pi}C\hbar^{4}/3(k_{\text{B}}Tm_{\text{dos}}^{*})^{3/2}E^{2}$ [49] with $C$, $m_{\text{dos}}^{*}$ and $E$ are the elastic module, the DOS effective mass, and the DP constant, respectively. Table 1 summarizes the room temperature relaxation time of BiBaK for electrons and holes. We see that the relaxation time of electrons is obviously larger than that of holes, which can be attributed to their considerably different DOS effective mass, as also evidenced by the dispersion relations

near the CBM and VBM (Fig. 5). Using the semi-classical Boltzmann theory and inserting the calculated carrier relaxation time, we can obtain the electronic transport coefficients of BiBaK ($S$, $\sigma$, and $\kappa_e$) at various temperatures and concentrations.

In particular, our calculations find that the system exhibits higher power factor ($S^2\sigma$) of $2.38\times10^{-3}\ \text{W/mK}^2$ and $7.28\times10^{-4}\ \text{W/mK}^2$ at 900 K for the $n$- and $p$-type carriers, respectively.

### 3.4 Thermoelectric properties
Combining the lattice thermal conductivity ($\kappa_l$) with the electronic transport coefficients ($S$, $\sigma$, and $\kappa_e$) discussed above, we can now evaluate the thermoelectric performance of BiBaK. Figure 6(a) shows the calculated $ZT$ values as a function of carrier concentration at two typical temperatures of 300 and 900 K. In both cases, it is clear that the $ZT$ can be maximized by optimizing the carrier concentration. If we focus on the high temperature, we see that the $p$-type system exhibits a peak $ZT$ of $\sim$0.9 at the concentration of $4.3\times10^{20}\ \text{cm}^{-3}$. For the $n$-type system, however, the $ZT$ value can be significantly optimized to 1.9 at much lower concentration of $4.2\times10^{18}\ \text{cm}^{-3}$, which outperforms many good thermoelectric materials. In Fig. 6(b), we plot the $ZT$ value as a function of temperature from 300 to 900 K. We see that the $ZT$ of $n$-type BiBaK increases almost linearly with the temperature, and is obviously higher than that of $p$-type system in the whole temperature considered. Much efforts should be thus devoted to enhance the thermoelectric performance of $p$-type BiBaK so that comparable efficiencies could be realized in the fabrication of both $n$- and $p$-legs of thermoelectric modules.

## 4. Summary
We have performed a theoretical study on the structural, electronic, phonon, and thermoelectric transport properties of the HH compound BiBaK. Among three possible atomic configurations, we identify the most stable structure with an indirect band gap

of 0.75 eV by adopting the hybrid functional and considering the SOC. Due to the rattling of K atoms inside the hexadecahedron cage formed by Bi and Ba atoms, the BiBaK exhibits unprecedentedly low lattice thermal conductivity of 1.82 W/mK at 300 K and 0.60 W/mK at 900 K. Consequently, we obtain a $ZT$ value of $\sim$0.5 at 300 K, which can be further enhanced to 1.9 at 900 K with a realistic $n$-type carrier concentration of $4.2 \times 10^{18}$ cm$^{-3}$. It would be interesting to investigate in the future work if favorable thermoelectric performance could be also found in other similar HHs such as SnBaSr, PdSrTe, and TeAgLi, which are assumed to have rather small lattice thermal conductivity at room temperature [19].

## Acknowledgements

We thank financial support from the National Natural Science Foundation (Grant Nos. 51772220 and 11574236). The numerical calculations in this work have been done on the platform in the Supercomputing Center of Wuhan University.

<table><thead><tr><th>Carrier type</th><th>$C$ ($\text{eV}/\text{Å}^3$)</th><th>$E$ ($\text{eV}$)</th><th>$m_{\text{dos}}^{\ast}$ ($m_e$)</th><th>$\tau$ ($\text{s}$)</th></tr></thead><tbody><tr><td>Electron</td><td>$0.188$</td><td>$-5.75$</td><td>$0.257$</td><td>$2.43 {\times} 10^{-13}$</td></tr><tr><td>Hole</td><td>$0.188$</td><td>$-5.18$</td><td>$1.49$</td><td>$2.15 {\times} 10^{-14}$</td></tr></tbody></table>

Table 1 The elastic constant $C$, the deformation potential constant $E$, the DOS effective mass $m_{\text{dos}}^{\ast}$ and the carrier relaxation time $\tau$ of BiBaK at room temperature.

![](./images/812591785229418498_1.jpg)

Figure 1. The AIMD results of the nearest Bi-Ba distance for BiBaK at 300 K, 900 K,
and 1000 K. The three insets correspond to the crystal structures at 4050, 4346 and 4738
MD step, respectively. The dash line indicates the equilibrium Bi-Ba distance.

![](./images/812591785229418498_2.jpg)

Figure 2. The phonon dispersion relations of (a) BiBaK, (b) CoSbZr, (c) NiSnTi, and (d) FeSbV, where the red lines indicate acoustic branches and black lines for optical ones.

![](./images/812591785229418498_3.jpg)

Figure 3. (a) The group velocity of different phonon modes in the BiBaK plotted as a function of frequency. (b) The temperature dependence of the lattice thermal conductivity. (c) The projected phonon density of states. (d) The cumulative lattice thermal conductivity at room temperature plotted as function of phonon frequency.

![](./images/812591785229418498_4.jpg)

Figure 4. (a) The calculated atomic displacement parameters of BiBaK as a function of temperature. (b) The BiBaK exhibits a cage-like structure with the guest K atom rattles inside the hexadecahedron host framework consisting of 4 Bi and 6 Ba atoms.

![](./images/812591785229418498_5.jpg)

Figure 5. The calculated energy band structure of BiBaK, where both the CBM and
VBM are doubly degenerated. The Fermi level is at 0 eV.

![](./images/812591785229418498_6.jpg)

Figure 6. (a) The calculated $ZT$ values of BiBaK as a function of carrier concentration at 300 K and 900 K. (b) Temperature dependent $ZT$ values for both $n$- and $p$-type systems.

## References

[1] K. F. Hsu, S. Loo, F. Guo, W. Chen, J. S. Dyck, C. Uher, T. Hogan, E. K. Polychroniadis, and M. G. Kanatzidis, Science **303**, 818 (2004).

[2] W. Kim, J. Zide, A. Gossard, D. Klenov, S. Stemmer, A. Shakouri, and A. Majumdar, Phys. Rev. Lett. **96**, 045901 (2006).

[3] Y. Z. Pei, X. Y. Shi, A. LaLonde, H. Wang, L. D. Chen, and G. J. Snyder, Nature **473**, 66 (2011).

[4] A. M. Dehkordi, M. Zebarjadi, J. He, and T. M. Tritt, Mater. Sci. Eng. R **97**, 1 (2015).

[5] J. He, and T. M. Tritt, Science **357**, eaak9997 (2017).

[6] J. Mao, Z. H. Liu, J. W. Zhou, H. T. Zhu, Q. Zhang, G. Chen, and Z. F. Ren, Adv. Phys. **67**, 69 (2018).

[7] A. F. Ioffe, L. S. Stil'bans, E. K. Iordanishvili, T. S. Stavitskaya, A. Gelbtuch, and G. Vineyard, Phys. Today **12**, 42 (1959).

[8] K. Berland, N. Shulumba, O. Hellman, C. Persson, and O. M. Løvvik, J. Appl. Phys. **126**, 145102 (2019).

[9] W. J. Xie, A. Weidenkaff, X. F. Tang, Q. J. Zhang, J. Poon, and T. M. Tritt, Nanomaterials **2**, 379 (2012).

[10] S. Chen, and Z. F. Ren, Mater. Today **16**, 387 (2013).

[11] H. T. Zhu, R. He, J. Mao, Q. Zhu, C. H. Li, J. F. Sun, W. Y. Ren, Y. M. Wang, Z. H. Liu, Z. J. Tang, A. Sotnikov, Z. M. Wang, D. Broido, D. J. Singh, G. Chen, K. Nielsch, and Z. F. Ren, Nat. Commun. **9**, 2497 (2018).

[12] H. T. Zhu, J. Mao, Y. W. Li, J. F. Sun, Y. M. Wang, Q. Zhu, G. N. Li, Q. C. Song, J. W. Zhou, Y. H. Fu, R. He, T. Tong, Z. H. Liu, W. Y. Ren, L. You, Z. M. Wang, J. Luo, A. Sotnikov, J. M. Bao, K. Nielsch, G. Chen, D. J. Singh, and Z. F. Ren, Nat. Commun. **10**, 270 (2019).

[13] K. Biswas, J. Q. He, I. D. Blum, C. I. Wu, T. P. Hogan, D. N. Seidman, V. P. Dravid, and M. G. Kanatzidis, Nature **489**, 414 (2012).

[14] R. J. Mehta, Y. L. Zhang, C. Karthik, B. Singh, R. W. Siegel, T. Borca-Tasciuc, and G. Ramanath, Nat. Mater. **11**, 233 (2012).

[15] C. G. Fu, S. Q. Bai, Y. T. Liu, Y. S. Tang, L. D. Chen, X. B. Zhao, and T. J. Zhu, Nat. Commun. **6**, 8144 (2015).

[16] N. S. Chauhan, S. Bathula, A. Vishwakarma, R. Bhardwaj, K. K. Johari, B. Gahtori, M. Saravanan, and A. Dhar, J. Phys. Chem. Solids **123**, 105 (2018).

[17] M. Siyar, J. Y. Cho, W. C. Jin, E. H. Hwang, M. Kim, and C. Park, Materials 12, 2040 (2019).

[18] J. Poon, J. Phys. D: Appl. Phys. 52, 493001 (2019).

[19] J. Carrete, W. Li, and N. Mingo, Phys. Rev. X 4, 011019 (2014).

[20] R. O. Jones, Rev. Mod. Phys. 87, 897 (2015).

[21] G. Kresse, and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

[22] A. Togo, and I. Tanaka, Scripta Mater. 108, 1 (2015).

[23] W. Li, J. Carrete, N. A. Katcho, and N. Mingo, Comput. Phys. Commun. 185, 1747 (2014).

[24] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[25] J. Heyd, G. E. Scuseria, and M. Ernzerhof, J. Chem. Phys. 118, 8207 (2003).

[26] G. K. H. Madsen, and D. J. Singh, Comput. Phys. Commun. 175, 67 (2006).

[27] J. Bardeen, and W. Shockley, Phys. Rev. 80, 72 (1950).

[28] B. H. Yan, and A. de Visser, MRS Bull. 39, 859 (2014).

[29] T. Fang, S. Q. Zheng, T. Zhou, L. Yan, and P. Zhang, Phys. Chem. Chem. Phys. 19, 4411 (2017).

[30] S. Chadov, X. L. Qi, J. Kübler, G. H. Fecher, C. Felser, and S. C. Zhang, Nat. Mater. 9, 541 (2010).

[31] T. Graf, C. Felser, and S. S. P. Parkin, Prog. Solid State Chem. 39, 1 (2011).

[32] C. G. Fu, T. J. Zhu, Y. Z. Pei, H. H. Xie, H. Wang, G. J. Snyder, Y. Liu, Y. T. Liu, and X. B. Zhao, Adv. Energy Mater. 4, 1400600 (2014).

[33] L. Andrea, G. Hug, and L. Chaput, J. Phys. Condens. Matter 27, 425401 (2015).

[34] A. N. Gandi, and U. Schwingenschlögl, Phys. Status Solidi B 254, 1700419 (2017).

[35] O. Hellman, and D. A. Broido, Phys. Rev. B 90, 134309 (2014).

[36] Z. T. Tian, J. Garg, K. Esfarjani, T. Shiga, J. Shiomi, and G. Chen, Phys. Rev. B 85, 184303 (2012).

[37] G. Q. Ding, J. Carrete, W. Li, G. Y. Gao, and K. L. Yao, Appl. Phys. Lett. 108, 233902 (2016).

[38] Z. Z. Zhou, H. J. Liu, D. D. Fan, B. Y. Zhao, C. Y. Sheng, G. H. Cao, and S. Huang, J. Phys. D: Appl. Phys. 51, 315501 (2018).

[39] D. Y. Wang, G. T. Wang, and W. F. Li, J. Alloys Compd. 692, 599 (2017).

[40] J. J. Dong, O. F. Sankey, and C. W. Myles, Phys. Rev. Lett. 86, 2361 (2001).

[41] M. Christensen, A. B. Abrahamsen, N. B. Christensen, F. Juranyi, N. H. Andersen,

K. Lefmann, J. Andreasson, C. R. H. Bahl, and B. B. Iversen, Nat. Mater. **7**, 811 (2008).

[42] D. Wee, B. Kozinsky, N. Marzari, and M. Fornari, Phys. Rev. B **81**, 045204 (2010).

[43] Y. L. Tang, R. Hanus, S. W. Chen, and G. J. Snyder, Nat. Commun. **6**, 7584 (2015).

[44] P. Lu, H. L. Liu, X. Yuan, F. F. Xu, X. Shi, K. P. Zhao, W. J. Qiu, W. Q. Zhang, and L. D. Chen, J. Mater. Chem. A **3**, 6901 (2015).

[45] H. L. Liu, X. Shi, F. F. Xu, L. L. Zhang, W. Q. Zhang, L. D. Chen, Q. Li, C. Uher, T. Day, and G. J. Snyder, Nat. Mater. **11**, 422 (2012).

[46] T. S. Zhu, K. Swaminathan-Gopalan, K. Stephani, and E. Ertekin, Phys. Rev. B **97**, 174201 (2018).

[47] X. Shi, J. Yang, J. R. Salvador, M. F. Chi, J. Y. Cho, H. Wang, S. Q. Bai, J. H. Yang, W. Q. Zhang, and L. D. Chen, J. Am. Chem. Soc. **133**, 7837 (2011).

[48] L. Cheng, C. Zhang, and Y. Y. Liu, J. Am. Chem. Soc. **141**, 16296 (2019).

[49] Q. Y. Xue, H. J. Liu, D. D. Fan, L. Cheng, B. Y. Zhao, and J. Shi, Phys. Chem. Chem. Phys. **18**, 17912 (2016).