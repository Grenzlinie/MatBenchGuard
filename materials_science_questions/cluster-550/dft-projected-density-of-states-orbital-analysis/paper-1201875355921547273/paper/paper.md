# Electronic and thermal properties of hybridized and nanostructured forms of SnSe

Received: 2 July 2025
Accepted: 24 November 2025
Published online: 30 November 2025

Cite this article as: Gülmen M. &
Berber S. Electronic and thermal
properties of hybridized and
nanostructured forms of SnSe. Sci
Rep (2025). https://doi.org/10.1038/
s41598-025-30287-9

Mergim Gülmen & Savaş Berber

We are providing an unedited version of this manuscript to give early access to its findings. Before final publication, the manuscript will undergo further editing. Please note there may be errors present which affect the content, and all legal disclaimers apply.

If this paper is publishing under a Transparent Peer Review model then Peer Review reports will publish with the final article.

© The Author(s) 2025. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

# Electronic and thermal properties of hybridized and nanostructured forms of SnSe

Mergim Gülmen*
Corresponding Author
Department of Physics, Gebze Technical University, Gebze, 41400, Turkey
Phone: +90 262 605 1779
email: mgulmen@gtu.edu.tr
orcid: 0000-0001-6446-4371

Savaş Berber
Department of Physics, Gebze Technical University, Gebze, 41400, Turkey
Phone: +90 262 605 1779
email: savasberber@gtu.edu.tr
orcid: 0000-0003-0949-2614

## Abstract
We theoretically examine the physical properties such as electrical, structural and particularly thermoelectrical features of nanostructured and hybridized forms of tin selenide (SnSe) with selected materials by using first-principles calculation via density functional theory and semi-classic Boltzmann Transport Theory. The energy band structure and projected density of states are studied in detail. The electronic transport coefficients are then calculated within the assumption of the constant relaxation time as applied in BoltzTraP code. This study is extended to calculate the thermoelectric performance of $CsPbI_3$ with various number of layers. Our calculations show that both nanostructured and hybrid forms of SnSe (SnSe-hBN and $SnSe-CsPbI_3$) have the highest value of $ZT$ around $\sim 1$ at low temperatures and the room temperature. This study reveals that the use of hybrid SnSe-hBN and $SnSe-CsPbI_3$ can be tuned due to their notably high Seebeck coefficient with appropriate doping rate for the purpose of the thermoelectric practices. The results also give an insight into that the nanostructured $CsPbI_3$ is a promising perovskite with considerably high $ZT$ value ($ZT$=2.5) for the thermoelectric applications.

## Keywords
Thermoelectric, nanostructured material, hybrid compound, electronic transport coefficients, density functional theory

### 1. Introduction

For the centuries, exploring new materials has shaped the technology from silicon based devices to ultrathin, light-weight supplies like two-dimensional (2D) materials. Since the exfoliation a single layer from the bulk graphite via micromechanical cleavage technique, a variety of new material has been synthesized rapidly. Given that their flat-thin geometry, a single atom thickness and exhibition of distinct physical, optical, electronic properties are found to have a wide range of application in the field of nanoelectronics [1-2] , optoelectronics [3-4], thermoelectronics [5-6], energy storage [7-8] and sensing [9-10]. Besides, theoretical advances in quantum mechanical calculations are related to explore new potentials among 2D materials. *Ab-initio* calculations of new generation of low dimensional materials via density functional theory (DFT) is a reliable method to analyze their electrical, thermal, optical, chemical properties prior to its fabrication [11-12]. In accordance with the results deduced theoretically from the DFT calculations, the manipulations in such materials have the possibilities of exploring other nanostructured systems with the fit for purposes.

Thermoelectricity which is the direct conversion of the temperature differences to electrical voltage and vice versa, can be evaluated by the "figure of merit", described as $ZT = S^2\sigma T/\kappa$ where $S$, $\sigma$, T and $\kappa$ are the Seebeck coefficient, electrical conductivity, temperature and thermal conductivity, respectively [13]. Scientists have tried to enhance $ZT$ value because the parameters in the formula are difficult to control. They are related to each other such that an increase in $S$ usually results in a decrease in $\sigma$, and a decrease in $\sigma$ results in a decrease in the electronic contribution to $\kappa$ [14]. Pisarenko relation expresses that lower carrier concentration leads to larger Seebeck but lower electrical conductivity. The larger effective mass ($m^*$) triggers larger Seebeck but lower carrier mobility and so lower electrical conductivity [15]. However, the decrease in the system dimensionality causes dramatic differences in the density of electronic states, allowing new opportunities to vary $S$, $\sigma$ and $\kappa$ quasi-independently [16].

Tin selenide from the monochalcogenide family has gained so much attention in virtue of their promising potentials in various fields such as electronic, optoelectronic, optics in particularly thermoelectric material due to its unprecedented figure of merit, $ZT$ ~2.6 at $T$ ~920 K and ultralow thermal conductivity (<0.25 W/mK at >800 K) as single crystal reported by Zhao et al. in 2014

[17]. This ultralow thermal conductivity originates from strong polar covalent bonding owing to the difference of the electronegativity between the Sn and Se atoms [18]. This anharmonicity in bonding results in low lattice thermal conductivity [19]. SnSe is also an anisotropic material with orthorhombic symmetry (Pnma space group no. 62) at room temperature and orthorhombic structure (Cmcm space group no. 63) above phase transition temperature around 800 K, in which it holds a lower symmetry.

In literature, there are many attempts to improve thermoelectric properties of SnSe by doping [20], [21], [22], [23], applying pressure [24], [25], nanostructuring [26], [27], [28], [29], [30], [31], [32] etc. but the $ZT$ is still far from a satisfying value. Alongside of nanostructuring, the use of hybrid materials is one of the important method to improve the thermoelectrical properties of bulk materials, in which dispersed second phase can significantly scatter the phonons [33], [34], [35], [36], [37]. Meanwhile, the literature notably lacks of work on thermoelectric properties of particularly nanostructured-hybrid materials aside from a few organic-inorganic and polymer hybrid concepts. Therefore, we developed 2D nanosheet hybrids and a layered nanostructured material to evaluate the thermoelectric performance and to contribute for innovative research on thermoelectric materials and devices.

In this study, we aim to investigate physical properties such as electrical, structural and particularly thermoelectrical features of Cmcm No.63 space group of tin selenide by nanostructuring and hybridizing with the selected materials at the proof of first-principle level by using DFT and Boltzmann transport theory with constant scattering time approximation (CSTA). SnSe was hybridized with hexagonal boron nitride (h-BN) based on its resemblance to graphene and cesium lead iodide ($CsPbI_3$) depending on its high $ZT_{elec}$ value as a monolayer (1.6 at 650 K) resultant of our calculation. SnSe was grown along the $x$ and $z$ axes and h-BN is enlarged along the $y$-axis orthogonally by making hybrid superlattice taking into accounting van der Waals distance between the interfaces in the same way of hybrid superlattice of SnSe-CsPbI₃. The electronic structures of the compounds were derived from the DFT calculations and linked with the Boltzmann Transport Theory in order to produce transport coefficients. The *ab-initio* molecular dynamics (AIMD) analysis were performed for the stability tests.

2. Theoretical Methods

The structural and electronic properties of nanostructured SnSe-hBN and SnSe-CsPbI₃ hybrid compounds were studied using the first-principle method as employed in the Quantum Espresso code within the framework of DFT [38], [39]. The exchange-correlation functional in the form of Perdew-Burke-Ernzerhof (PBE) method was employed [40]. 4×1×16 k-mesh was set for the Irreducible Brillouin Zone (IBZ) integrations and 240 Ry was applied as plane wave cutoff energy. Van der Waals functional (vdW-DFT3) was utilized for the interlayer correction. The total energy was converged by $10^{-10}$ (Ry) estimated self-consistent field accuracy. Atomic positions were fully relaxed until the forces acting on all atoms becomes less than 0.01 Ry/au. The calculations were extended to calculate the transport coefficients by using up to 1600 k-points in IBZ by employing semi-classical Boltzmann Theory with constant scattering time approximation (CSTA) as applied in the BoltzTraP code [41]. Instead of using an explicit value for the relation time, we give the relaxation time dependent transport quantities divided by the relaxation time $\sigma/\tau$ and $\kappa_0/\tau$ as calculated by the BolzTrap code. The CSTA assumes the relaxation time $\tau$ as energy independent which results in expressions of both the thermopower and the thermoelectric $ZT$ without dependence on $\tau$. Our unit cells contain large number of atoms for lattice thermal conductivity calculations. Although it is crucial to reduce the lattice thermal conductivity for high $ZT$ values, we provide $ZT_{elec}=S^2\sigma T/\kappa_0$ as an indicator of the potential of the systems considered in thermoelectric applications.

The main expressions for obtaining the thermoelectric coefficients have been described as follow, while a detailed interpretation of the Boltzmann transport theory can be found elsewhere [42]. The electrical conductivity ($\sigma_{\alpha\beta}$) and Seebeck coefficient ($S_{\alpha\beta}$) are described as a function of chemical potential ($\mu$) as follow;

$$
\sigma_{\alpha\beta}(T,\mu)=\frac{1}{\Omega}\int\Sigma_{\alpha\beta}(\varepsilon)\left[-\frac{\partial f_0(T,\varepsilon,\mu)}{\partial\varepsilon}\right]d\varepsilon \tag{1}
$$

$$
S_{\alpha\beta}(T,\mu)=\frac{1}{eT\Omega\sigma_{\alpha\beta(T,\mu)}}\int(\varepsilon-\mu)\Sigma_{\alpha\beta}(\varepsilon)\left[-\frac{\partial f_0(T,\varepsilon,\mu)}{\partial\varepsilon}\right]d\varepsilon \tag{2}
$$

where $e$ is charge of electron, $\mu$ is chemical potential, $T$ is absolute temperature, $f_0$ the Fermi-Dirac distribution function of the carriers, $\Omega$ is the volume of the unit cell and $\alpha$ and $\beta$ are Cartesian indices of the tensor.

For simplicity, the transport distribution is defined by the term $\Sigma_{\alpha\beta}$;

$$
\Sigma_{\alpha \beta}(\varepsilon)=\frac{e^{2}}{N} \sum_{i, k} \tau v_{\alpha}(i, k) v_{\beta}(i, k) \delta\left(\varepsilon-\varepsilon_{i, k}\right) \tag{3}
$$

where $v_{\alpha}(i, k)=\frac{1}{\hbar} \frac{\partial \varepsilon_{i, k}}{\partial k_{\alpha}}$ is the group velocity and $i, k, N, \tau$ in Eq. (3) are the band index, wavevector, total number of k-points for BZ sampling and relaxation time, respectively.

## 3. Results and Discussions

Hexagonal boron nitride (h-BN) has the same atomic structure as graphene, but with a 1.8% longer lattice constant [43]. Two dimensional h-BN is emerging as a 2D material owing to its high temperature stability, chemical inertness, mechanical robustness and high carrier mobility and so on [44], [45]. The nanostructured-hybrid SnSe-hBN belongs to a class of tetragonal crystals. It has 44 atoms per unit cell containing 8 each Sn and Se atoms as well as 14 each B and N atoms in a unit cell in which crystal structures are as follows, a= 17.28 Å, b= 25.97 Å, c= 4.32 Å. Figure 1(a-b) represents crystal structure of hexagonal-BN and hybrid SnSe-hBN, respectively.

$\mathrm{CsPbX}_{3}$ (where $\mathrm{X}=\mathrm{Cl}, \mathrm{Br}$ or $\mathrm{I}$) known as ternary plumbohalide perovskites that can exist in three phases (orthorhombic, tetragonal and cubic) was discovered by Møller in 1959 [46]. $\mathrm{CsPbI}_{3}$ has four phases which are three 'black' perovskites $(\alpha, \beta$ and $\gamma)$ and one 'yellow' non-perovskite $(\delta)$. The all-inorganic $\mathrm{CsPbX}_{3}$ possesses excellent photoelectronic properties with long carrier lengths and high defect tolerance, which provides extraordinary optoelectronic qualities [47]. The SnSe was hybridized with $\alpha$-phase $\mathrm{CsPbI}_{3}$ as seen in Figure 2a and it belongs to a class of tetragonal crystals. Our unit cell has 104 atoms containing each 36 Sn and Se atoms as well as 4 Cs, 8 Pb and 20 I atoms as shown in Figure 2b. Crystal lattice parameters are as follows, a= 12.90 Å, b= 30.00 Å, c= 12.90 Å. As the individual components of our hybrid systems are mechanically robust, we expect the hybrid system to be stable as well. To verify this expectation, we performed a microcanonical molecular dynamics simulation of SnSe-hBN hybrid structure with 600 K initial temperature. Our ab-initio molecular dynamics (AIMD) analysis demonstrated the molecular stability for SnSe-hBN hybrid structure (see Supplementary Fig. S1 online), as the energy of the system fluctuates around the equilibrium value. The hybrid system does not show an immediate structural transition.

The band structure of hybrid SnSe-hBN and SnSe-CsPbI₃ explored high symmetry lines is presented in Figure 3(a-c). The Fermi energy is set to zero on the energy scale. The valence band maximum (VBM) and the conduction band minimum (CBM) in the band structure, suggests a direct band gap of 0.780 and 0.495 eV where VBM and CBM locate along the $\Gamma-X$ for SnSe-hBN and SnSe-CsPbI₃, respectively. The electronic valence band structure of hybrid SnSe-CsPbI₃ exhibits almost flat characteristic leading to high hole effective masses and low mobility. It should be noted that the band gap is not predicted reliably due to the discontinuity of the exchange-correlation potential at the Fermi level in DFT [49]. The spin-orbit coupling was only considered for SnSe-hBN which can be found as Supplementary Figure S2 online since the SnSe-hBN is relatively less dense than SnSe-CsPbI₃ configuration. The calculated band gap values for high temperature phase of SnSe-Cmcm(#63) were quite scattered in literature and the experimental data is not available. For example, the PBE, Tb-mBJ and HSE functionals give an indirect ban gap of 0.536 eV along $\Gamma Z$ and $\Gamma Y$ as well as direct band gap of 0.66 eV along $\Gamma Y$ and 1.142 eV at $\Gamma$ point of Brillouin zone (BZ) [50]. LDA functionals reveals an indirect band gap of 0.355 eV along $\Gamma Y$ [51]. Zhao et.al reported band gap of 0.39 eV along $P\Gamma$ by GGA-PBE functionals [17].

The projected density of states calculations are performed to spot the contributions from each individual atoms and/or each of their orbital contributions, in this regard the total projected density of states (PDOS) of hybrid SnSe-hBN and SnSe-CsPbI₃ are shown in Figure 3(b-d). The SnSe states appear in the energy gap of hBN. The Fermi energy is set to zero on the energy scale. Figure 3b shows that Sn and Se are bonding since their nodes are in the same location. As for Sn and B, its DOS is larger at the empty states than the occupied states owing to charge transfer from Sn to Se and B to N, respectively. The total DOS of SnSe-hBN near the valence band maximum is larger than that near the conduction band minimum. Then, this type of hybrid material may have better thermoelectric effect with p-type doping. As seen in Figure 3d, the DOS for Se and I are larger at the occupied states than the empty states suggesting the charge transfer occurred from Se and I to Sn and Pb. The calculations reveal that the density of states for SnSe-CsPbI₃ are much higher as compared to SnSe-hBN proving higher density of states close by the Fermi level leading to higher Seebeck coefficient [22].

The thermopower band gap is also estimated from Figure 4(a-b), using the Goldsmid-Sharp approach [52]. The calculated thermopower band gap of value 0.692 eV at 150 K and 0.50 eV at

100 K for SnSe-hBN and SnSe-CsPbI₃ hybrids, respectively. These estimations agreeably match to that of Kohn-Sham band gaps (0.780 eV and 0.495 eV for SnSe-hBN and SnSe-CsPbI₃, respectively) in the present study, indicating the consistency in our investigation.

The results are summarized at Table1 for the highest values of electrical conductivity $(\sigma/\tau)$, Seebeck coefficients (S), power factor (PF) and figure of merit (ZT) of the SnSe-hBN and SnSe- CsPbI₃ from 100 K to 1000 K.

The $(\sigma/\tau)$ for both SnSe-hBN and SnSe-CsPbI₃ calculated at different temperatures is shown in Figure 5(a-b). The maximum electrical conductivity $(\sigma/\tau)$ were found to be $5.57×10^{19}$ /Ωms at 100 K and $2.19×10^{19}$ /Ωms at 100 K for SnSe-hBN and SnSe-CsPbI₃, respectively. The electrical conductivity of SnSe-CsPbI₃ decreases monotonously along the increasing temperature the same as SnSe-hBN. Moreover, the electron localization function (ELF) determined that both hybrid systems have a weak interfacial bonding. As there is no charge localization between the layers, no gap states appear in the electronic structure. The bonding character between Sn and Se remains similar after hybridization. The distance between Sn-Se bond was stronger for SnSe-CsPbI₃ hybrid, resulting in the shorter bond distance $d_{Sn-Se}$= 2.755 Å compared to $d_{Sn-Se}$= 3.045 Å for SnSe-hBN hybrid (see Supplementary Fig. S3 online).

Figure 6(a-b) plots of the calculated Seebeck coefficients for SnSe-hBN and SnSe-CsPbI₃, respectively, as a function of potential $\mu$ (eV) with varying temperature from 100 to 900 K. The Seebeck coefficient reaches the peak values of $2326\ \mu V/K$ at 100 K for SnSe-hBN and $2543\ \mu V/K$ at 100 K for SnSe-CsPbI₃. The magnitude of the Seebeck coefficient increases significantly around the Fermi level as crossing the gap the sign of S switches. There are two sharp peaks with different signs in the vicinity of the Fermi level for each temperature level: the peak value $2326\ \mu V/K$ at 0.11 eV for n-type doping and $-2400\ \mu V/K$ at 0.38 eV for p-type doping. Figure 6b demonstrates the calculated Seebeck coefficient for SnSe-CsPbI₃ hybrid compound different temperature. The peak value $2543\ \mu V/K$ at 3.27 eV for n-type doping and $-2636\ \mu V/K$ at 3.60 eV for p-type doping. The large Seebeck coefficient suggests that the contribution comes from more than one valence band.

Figure 7(a-b) illustrate the variation in power factor $(S^{2}\sigma/\tau)$ as a function of chemical potential $\mu(eV)$ with the effect of temperature from 100 K to 900 K of the hybrid compounds. The

temperature increases with the chemical potential, the power factor also increases for both hybrid systems. SnSe-hBN showed the highest power factor of $11.99×10^{10}$ W/mK²s at 900 K and $12.93×10^{10}$ W/mK²s at 1000 K, respectively. For SnSe-CsPbI₃, the top power factor values were $8.85×10^{10}$ W/mK²s at 900 K and $9.46×10^{10}$ W/mK²s at 1000 K, respectively. In Figure 7b, there are plenty of peaks within the chemical potential range considered, which suggests that thermoelectric performance can be adjusted by appropriate amount of doping [23]. The power factor for SnSe-hBN was found higher (35.5%) than the SnSe-CsPbI₃. Further, both hybrid compounds have their maximum value for power factor at 900-1000 K and it increases with the increasing temperature making them useful for the spacecraft power applications where thermoelectric materials can function at high temperatures (above 900 K) [53].

Since the phonon calculation is beyond this work, we refer the figure of merit as $ZT_{elec}$ for our results henceforth. Figure 8(a-b) show the calculated figure of merit ($ZT_{elec}$) of the hybrid SnSe-hBN and SnSe-CsPbI₃ with respect to chemical potential. The highest values of $ZT_{elec}$ occurred 0.985 at 100 K for the SnSe-hBN. As regards to SnSe-CsPbI₃, Figure 8b, the highest values of $ZT_{elec}$ recorded as 0.991 at 100 K. Table 2 shows the comparison of some reported $ZT$ values for the materials used in the present study. The $ZT_{elec}$ hybridized SnSe were found to be around ~1. This is superior as compared to $\pi$-SnSe, p&n-type SnSe and SnSe-Cmcm [25], [54], [55], [56]. On the other hand, CsPbI₃ with 3 and 4 layered yielded 2.5 for $ZT_{elec}$ which is very close to the world record of single crystal of SnSe. Such high efficiency can further be tailored by nanostructuring or suitable doping to enhance the $ZT$ value.

The electronic thermal conductivity ($\kappa/\tau$) as a function of chemical potential performed with different temperatures for both hybrid SnSe-hBN and SnSe-CsPbI₃ are shown in Figure 9(a-b). The electronic thermal conductivity increases with temperature, suggesting bidirectional conduction even at low temperatures. The bidirectional conduction takes place in the narrow band gap materials, such as Bi₂Te₃, PbTe (and the present study) owing to simultaneous contribution from both electrons and holes in the transport process [57]. However, such increase in thermal conductivity with temperature conduce to reduce the figure of merit. This can be seen in Figure 9(a-b) where the $ZT$ values are minimizing while the thermal conductivity is raising, for both hybrid materials. Shafigue & Shin [58] reported the thermal conductivity of 2.44 W/mK and 2.63 W/mK along the armchair and zigzag directions for monolayer SnSe. Chang et. al. and Cao et.al.

[24], [59] declared that the anisotropic crystal structure and the specific type of chemical bonding in SnSe eases the electronic transport however the strong anharmonicity substantially impedes lattice transport in all crystal directions. The hybrid structures with high anisotropy have low lattice conductivities compare to their unhybridized versions. However, as the hybrid systems with a large unit cell like more than 40 atoms per unit cell, the lattice thermal conductivity calculations may not be tractable. The peak value of $ZT_{elec}$ around 1 at 100 K can be attributed to the relatively low thermal conductivity at that temperature but mostly due to the much higher power factor with the degree of $10^{10}$ W/mK²s for both hybrid systems avoiding $ZT_{elec} < 1$.

Our results indicate that hybridizing SnSe with h-BN and $CsPbI_3$ does not improve its thermoelectric properties. However, combining h-BN with SnSe provides a protective layer without decreasing the present thermoelectric performance. For SnSe-CsPbI₃, in the same way, SnSe may enhance the stability of $CsPbI_3$ layers since the poor stability is the main factor restraining the production of inorganic $CsPbI_3$ as a manufactured product [47]. In hybrid systems, the thermoelectric performance is determined by the strongest component in the hybrid structure namely considerably high Seebeck coefficients for the hybrid materials used in this study.

The study is extended to calculate the thermoelectric performance of $CsPbI_3$ with various number of layers which is an another strategy to optimize $ZT$. Our calculated $ZT_{elec}$ values for layered $CsPbI_3$ are shown in Figure 10. The structure of monolayer, bilayer, three-layered and four-layered of $CsPbI_3$ are depicted in Figure 11. We recorded $ZT_{elec}$=1.6 at 650 K and 200 K temperatures for monolayer and bilayer of $CsPbI_3$, respectively. The highest value of $ZT_{elec}$ was found 2.5 and 2.49 for three-layered and four-layered of cesium lead iodide at 150 K, respectively. This value is 150% higher than its bulk form of $CsPbI_3$ ($ZT_{elec}$ ~1). The calculated electronic $ZT$ values shows descending trend for the all layers with increasing temperature after reaching its own maximum value of $ZT_{elec}$. The $ZT_{elec}$ versus carrier concentration with various temperature were also demonstrated in Supplementary Figure S4 online. Furthermore, the highest value of electrical conductivity $(\sigma/\tau)$ of three-layered of $CsPbI_3$ was found as $2.04×10^{20}$ /Ωms at 50 K at ~2.42 eV and maximum value of power factor as $2.73×10^{11}$ W/mK²s at 1000 K. The Seebeck coefficient reaches to the peak value of $2608\ \mu V/K$ at 250 K. This kind of high $ZT_{elec}$ value of $CsPbI_3$ can be attributed to its high cubic symmetry, significantly high Seebeck coefficient and electrical conductivity which may result from its long carrier diffusion length. We concluded from the results

that $CsPbI_3$ emerges as a promising perovskite with notably high $ZT_{elec}$ value for thermoelectric applications. Three-layered and four-layered $CsPbI_3$ may also be combined with another layered material to overcome phase instability of the system.

4. Conclusions

In summary, we present the first ever study on thermoelectric properties of the hybrid and nanostructured compounds (SnSe-hBN and $SnSe-CsPbI_3$) of $Cmcm$ phase SnSe. The calculations were done using first-principles method by employing Quantum Espresso code and Boltzmann transport theory. The calculated band gap was found 0.780 eV and 0.495 eV for the hybrid and nanostructured $SnSe-hBN$ and $SnSe-CsPbI_3$, respectively. The computations showed that the both hybrid compounds exhibit $ZT_{elec}$ value around ~1 at relatively low temperatures (50-300 K), which is close to the bulk form value. Additionally, materials with relatively narrow band gaps and large atomic weight of the constitutes result in higher effective mass, which ending up with reduced mobility and then low $ZT_{elec}$. The effect of temperature on $ZT_{elec}$ decreases gradually with the increase in temperature. The electrical conductivity, Seebeck coefficient and power factor were also discussed as a function of chemical potential. The study concluded that the use of hybrid compounds used for this work can be tuned due to notably high Seebeck coefficient with appropriate doping rate for the purpose of the thermoelectric applications. It is likely that on-going research on tin selenide will furnish new improvements in terms of structure engineering, phase manipulation including thermoelectrical performance. Finally, we concluded that the nanostructured $CsPbI_3$ emerges as a promising perovskite with notably high $ZT_{elec}$ for thermoelectric purposes.

### Acknowledgement

The authors extend their appreciations to the TUBITAK ULAKBIM, High Performance and Grid Computing Center (TRUBA resources)

### References

[1] F. Zhong *et al.*, "Recent progress and challenges on two-dimensional material photodetectors from the perspective of advanced characterization technologies," *Nano Res.*, vol. 14, no. 6, pp. 1840–1862, 2021, doi: 10.1007/s12274-020-3247-1.

[2] P. Chen, W. Xu, Y. Gao, J. H. Warner, and M. R. Castell, "Epitaxial Growth of Monolayer MoS2 on SrTiO3 Single Crystal Substrates for Applications in Nanoelectronics," *ACS Appl. Nano Mater.*, vol. 1, no. 12, pp. 6976–6988, 2018, doi: 10.1021/acsanm.8b01792.

[3] L. Li, W. Wang, Y. Chai, H. Li, M. Tian, and T. Zhai, "Few-Layered PtS2 Phototransistor on h-BN with High Gain," *Adv. Funct. Mater.*, vol. 27, no. 27, pp. 1–8, 2017, doi: 10.1002/adfm.201701011.

[4] X. Zhou *et al.*, "Ultrathin SnSe2 Flakes Grown by Chemical Vapor Deposition for High-Performance Photodetectors," *Adv. Mater.*, vol. 27, no. 48, pp. 8035–8041, 2015, doi: 10.1002/adma.201503873.

[5] A. J. Minnich, M. S. Dresselhaus, Z. F. Ren, and G. Chen, "Bulk nanostructured thermoelectric materials: Current research and future prospects," *Energy Environ. Sci.*, vol. 2, no. 5, pp. 466–479, 2009, doi: 10.1039/b822664b.

[6] S. Walia *et al.*, "Transition metal oxides - Thermoelectric properties," *Prog. Mater. Sci.*, vol. 58, no. 8, pp. 1443–1489, 2013, doi: 10.1016/j.pmatsci.2013.06.003.

[7] G. A. Muller, J. B. Cook, H. S. Kim, S. H. Tolbert, and B. Dunn, "High performance pseudocapacitor based on 2D layered metal chalcogenide nanocrystals," *Nano Lett.*, vol. 15, no. 3, pp. 1911–1917, 2015, doi: 10.1021/nl504764m.

[8] H. Sun *et al.*, "Three-dimensional holey-graphene/niobia composite architectures for ultrahigh-rate energy storage," *Science* (80-. )., vol. 356, no. 6338, pp. 599–604, 2017, doi: 10.1126/science.aam5852.

[9] N. Parvin *et al.*, "Few-Layer Graphdiyne Nanosheets Applied for Multiplexed Real-Time DNA Detection," *Adv. Mater.*, vol. 29, no. 18, pp. 1–7, 2017, doi: 10.1002/adma.201606755.

[10] M. Park, Y. J. Park, X. Chen, Y. K. Park, M. S. Kim, and J. H. Ahn, "MoS2-Based Tactile Sensor for Electronic Skin Applications," *Adv. Mater.*, vol. 28, no. 13, pp. 2556–2562, 2016, doi: 10.1002/adma.201505124.

[11] P. Hohenberg and W. Kohn, "Inhomogeneous Electron Gas," *Phys. Rev. B*, vol. 136, no. 4, pp. 864–871, 1964, doi: https://doi.org/10.1103/PhysRev.136.B864.

[12] D. Er and K. Ghatak, *Atomistic modeling by density functional theory of two-dimensional

materials. INC, 2020. doi: 10.1016/B978-0-12-818475-2.00006-4.

[13] H. J. Goldsmid, *Thermoelectric Refrigeration*, 1st ed. Springer New York, NY, 1964. doi: https://doi.org/10.1007/978-1-4899-5723-8.

[14] A. Bejan and A. D. Kraus, *Heat Transfer Handbook*, 1st ed., vol. 1. John Wiley & Sons, 2003.

[15] G. Tan, L. D. Zhao, and M. G. Kanatzidis, “Rationally Designing High-Performance Bulk Thermoelectric Materials,” *Chem. Rev.*, vol. 116, no. 19, pp. 12123–12149, 2016, doi: 10.1021/acs.chemrev.6b00255.

[16] M. S. Dresselhaus *et al.*, “New directions for low-dimensional thermoelectric materials,” *Adv. Mater.*, vol. 19, no. 8, pp. 1043–1053, 2007, doi: 10.1002/adma.200600527.

[17] L. D. Zhao *et al.*, “Ultralow thermal conductivity and high thermoelectric figure of merit in SnSe crystals,” *Nature*, vol. 508, no. 7496, pp. 373–377, 2014, doi: 10.1038/nature13184.

[18] S. Bai, X. Zhang, and L. D. Zhao, “Rethinking SnSe Thermoelectrics from Computational Materials Science,” *Acc. Chem. Res.*, vol. 56, no. 21, pp. 3065–3075, 2023, doi: 10.1021/acs.accounts.3c00490.

[19] W. G. Zeier, A. Zevalkink, Z. M. Gibbs, G. Hautier, M. G. Kanatzidis, and G. J. Snyder, “Thinking Like a Chemist: Intuition in Thermoelectric Materials,” *Angew. Chemie - Int. Ed.*, vol. 55, no. 24, pp. 6826–6841, 2016, doi: 10.1002/anie.201508381.

[20] J. C. Li, D. Li, X. Y. Qin, and J. Zhang, “Enhanced thermoelectric performance of p-type SnSe doped with Zn,” *Scr. Mater.*, vol. 126, pp. 6–10, 2017, doi: 10.1016/j.scriptamat.2016.08.009.

[21] S. Wang *et al.*, “Low temperature thermoelectric properties of p -type doped single-crystalline SnSe,” *Appl. Phys. Lett.*, vol. 112, no. 14, 2018, doi: 10.1063/1.5023125.

[22] O. Yamashita and S. Tomiyoshi, “High performance n-type bismuth telluride with highly stable thermoelectric figure of merit,” *J. Appl. Phys.*, vol. 95, no. 11 I, pp. 6277–6283, 2004, doi: 10.1063/1.1712013.

[23] H. Y. Lv *et al.*, “Enhanced thermoelectric performance of (Sb0.75 Bi 0.25)2 Te3 compound from first-principles calculations,” *Appl. Phys. Lett.*, vol. 96, no. 14, pp. 2010–2013, 2010, doi: 10.1063/1.3372636.

[24] W. Cao, Z. Wang, L. Miao, J. Shi, and R. Xiong, “Extremely Anisotropic Thermoelectric Properties of SnSe Under Pressure,” *Energy Environ. Mater.*, vol. 6, no. 3, pp. 1–8, 2023, doi: 10.1002/eem2.12361.

[25] L. T. Yang *et al.*, “Influence of pressure on phase transition, electronic and thermoelectric properties of SnSe,” *J. Alloys Compd.*, vol. 853, p. 157362, 2021, doi: 10.1016/j.jallcom.2020.157362.

[26] W. J. Baumgardner, J. J. Choi, Y. F. Lim, and T. Hanrath, “SnSe nanocrystals: Synthesis,

structure, optical properties, and surface chemistry," *J. Am. Chem. Soc.*, vol. 132, no. 28, pp. 9519-9521, 2010, doi: 10.1021/ja1013745.

[27] H. H. Xu, N. N. Zhou, X. L. Liang, T. T. Jiang, W. T. He, and J. M. Song, "SnSe nanoparticles with the ultra-low lattice thermal conductivity: synthesis and characterization," *J. Nanoparticle Res.*, vol. 24, no. 6, 2022, doi: 10.1007/s11051-022-05490-8.

[28] J. Schulz, L. Schindelhauer, C. Ruhmlieb, M. Wehrmeister, T. Tsangas, and A. Mews, "Controlled Growth of Two-Dimensional SnSe/SnS Core/Crown Heterostructures," *Nano Lett.*, vol. 24, pp. 13624-13630, 2024, doi: 10.1021/acs.nanolett.4c03393.

[29] M. Irshad Ahamed, R. Ayyappa, E. Edward Anand, and R. Krishnamoorthy, "Investigation of thermally evaporated SnSe nano structure layer for photovoltaic use: a structural, morphological, and electrical analysis," *J. Mater. Sci. Mater. Electron.*, vol. 36, no. 3, pp. 1-11, 2025, doi: 10.1007/s10854-025-14299-9.

[30] N. Neophytou *et al.*, "Hierarchically nanostructured thermoelectric materials: challenges and opportunities for improved power factors," *Eur. Phys. J. B*, vol. 93, no. 11, 2020, doi: 10.1140/epjb/e2020-10455-0.

[31] P. Xu, K. Jin, J. Huang, Z. Yan, L. Fu, and B. Xu, "Solution-synthesized nanostructured materials with high thermoelectric performance," *Nanoscale*, vol. 17, no. 17, pp. 10531-10556, 2025, doi: 10.1039/D5NR00333D.

[32] M. Shtern *et al.*, "Mechanical properties and thermal stability of nanostructured thermoelectric materials on the basis of PbTe and GeTe," *J. Alloys Compd.*, vol. 946, p. 169364, 2023, doi: 10.1016/j.jallcom.2023.169364.

[33] C. Li *et al.*, "SnSe nanosheet hybridized with reduced graphene oxide for enhanced hydrogen revolution reaction," *Appl. Phys. A*, 2023, doi: 10.1007/s00339-023-06690-2.

[34] H. Pang *et al.*, "Hybridization-driven strong anharmonicity in Yb-filled skutterudites," *Phys. Rev. B*, vol. 105, no. March, p. 094115, 2022, doi: 10.1103/PhysRevB.105.094115.

[35] Y. Zhang *et al.*, "2D Black Phosphorus for Energy Storage and Thermoelectric Applications," *Small*, vol. 13, no. 28, pp. 1-20, 2017, doi: 10.1002/smll.201700661.

[36] F. E. Jorge, L. G. P. Tienne, M. de F. V. Marques, and S. N. Monteiro, "Evaluation of thermoelectric properties of hybrid polyaniline nanocomposites incorporated with graphene oxide and zinc oxide with different morphologies," *J. Mater. Res. Technol.*, vol. 27, no. September, pp. 6822-6832, 2023, doi: 10.1016/j.jmrt.2023.11.098.

[37] Y. Zheng *et al.*, "Designing hybrid architectures for advanced thermoelectric materials," *Mater. Chem. Front.*, vol. 1, no. 12, pp. 2457-2473, 2017, doi: 10.1039/c7qm00306d.

[38] B. S. Giannozzi P, Andreussi O, Brumme T, Bunau O, Buongiorno Nardelli M, Calandra M, Car R, Cavazzoni C, Ceresoli D, Cococcioni M, Colonna N, Carnimeo I, Dal Corso A, de Gironcoli S, Delugas P, DiStasio RA Jr, Ferretti A, Floris A, Fratesi G, Fugallo G, Gebaue, "Advanced capabilities for materials modelling with Quantum ESPRESSO," *J*.

Phys. Condens. Matter, vol. 29, no. 46, p. 465901, 2017, doi: 10.1088/1361-648X/aa8f79.

[39] P. Giannozzi *et al.*, "QUANTUM ESPRESSO: A modular and open-source software project for quantum simulations of materials," *J. Phys. Condens. Matter*, vol. 21, no. 39, 2009, doi: 10.1088/0953-8984/21/39/395502.

[40] John P. Perdew, K. Burke, and M. Ernzerhof, "Generalized Gradient Approximation Made Simple," *Phys Rev Lett.*, vol. 10, no. 48, pp. 41525-41534, 2018, doi: 10.1103/PhysRevLett.77.3865.

[41] G. K. H. Madsen and D. J. Singh, "BoltzTraP. A code for calculating band-structure dependent quantities," *Comput. Phys. Commun.*, vol. 175, no. 1, pp. 67-71, 2006, doi: 10.1016/j.cpc.2006.03.007.

[42] J. Scheidemantel, C. Ambrosch-Draxl, T. Thonhauser, V. Badding, and O. Sofo, "Transport coefficients from first-principles calculations," *Phys. Rev. B - Condens. Matter Mater. Phys.*, vol. 68, no. 12, pp. 1-6, 2003, doi: 10.1103/PhysRevB.68.125210.

[43] V. Skakalova and A. B. Kaiser, *Graphene Properties, Preparation, Characterization and Applications*, 2nd ed. Woodhead Publishing, 2021.

[44] M. J. Molaei, M. Younas, and M. Rezakazemi, "A Comprehensive Review on Recent Advances in Two-Dimensional (2D) Hexagonal Boron Nitride," *ACS Appl. Electron. Mater.*, vol. 3, no. 12, 2021, doi: 10.1021/acsaelm.1c00720.

[45] P. M. A. Soumyabrata Roy, Xiang Zhang, Anand B. Puthirath, Ashokkumar Meiyazhagan, Sohini Bhattacharyya, Muhammad M. Rahman, Ganguli Babu, Sandhya Susarla, Sreehari K. Saju, Mai Kim Tran, Lucas M. Sassi, M. A. S. R. Saadi, Jiawei Lai, Onur Sahin, Seyed Mohammad Sa, "Structure, Properties and Applications of Two-Dimensional Hexagonal Boron Nitride," *Adv. Mater.*, vol. 33, no. 44, 2021, doi: https://doi.org/10.1002/adma.202101589.

[46] C. K. N. Moller, "The Structure of Caesium Plumbo Iodide CaPbI3," *Math. - Phys. releases*, vol. 32, no. 1, 1959.

[47] Z. Yao, W. Zhao, and S. Liu, "Stability of the CsPbI3perovskite: From fundamentals to improvements," *J. Mater. Chem. A*, vol. 9, no. 18, pp. 11124-11144, 2021, doi: 10.1039/d1ta01252e.

[48] J. M. Ziman, *Z Principles of the Theoery of Solids*. Cambridge University Press, 1972. doi: https://doi.org/10.1017/CBO9781139644075.

[49] P. J. Hasnip, K. Refson, M. I. J. Probert, J. R. Yates, S. J. Clark, and C. J. Pickard, "Density functional theory in the solid state," *Philos. Trans. R. Soc. A Math. Phys. Eng. Sci.*, vol. 372, no. 2011, 2014, doi: 10.1098/rsta.2013.0270.

[50] A. Ghafari, W. Khan, and C. Janowitz, "Electronic structure and engineered thermoelectric properties of SnSe," *Phys. B Condens. Matter*, vol. 630, no. October 2021, p. 413668, 2022, doi: 10.1016/j.physb.2022.413668.

[51] K. Kutorasinski, B. Wiendlocha, S. Kaprzyk, and J. Tobola, "Electronic structure and thermoelectric properties of n - And p -type SnSe from first-principles calculations," *Phys. Rev. B - Condens. Matter Mater. Phys.*, vol. 91, no. 20, pp. 1-12, 2015, doi: 10.1103/PhysRevB.91.205201.

[52] H. J. Goldsmid and J. W. Sharp, "Estimation of the thermal band gap of a semiconductor from Seebeck measurements," *J. Electron. Mater.*, vol. 28, no. 7, pp. 869-872, 1999, doi: 10.1007/s11664-999-0211-y.

[53] S. R. Brown, S. M. Kauzlarich, F. Gascoin, and G. Jeffrey Snyder, "Yb 14MnSb 11: New high efficiency thermoelectric material for power generation," *Chem. Mater.*, vol. 18, no. 7, pp. 1873-1877, 2006, doi: 10.1021/cm060261t.

[54] X. Wang *et al.*, "Optimization of thermoelectric properties in n-type SnSe doped with BiCl3," *Appl. Phys. Lett.*, vol. 108, no. 8, pp. 1-6, 2016, doi: 10.1063/1.4942890.

[55] M. A. Sattar, N. Al Bouzieh, M. Benkraouda, and N. Amrane, "First-principles study of the structural, optoelectronic and thermophysical properties of the $\pi$-SnSe for thermoelectric applications," *Beilstein J. Nanotechnol.*, vol. 12, pp. 1101-1114, 2021, doi: 10.3762/BJNANO.12.82.

[56] C.-L. Chen, H. Wang, Y.-Y. Chen, T. Daya, and G. J. Snydera, "Thermoelectric properties of p-type polycrystalline SnSe doped with Ag," *J. Mater. Chem. C*, vol. 3, pp. 10715-10722, 2015, doi: 10.1039/b000000x.

[57] L. F. Wan and S. P. Beckman, "Complex borides based on AlLiB14 as high-temperature thermoelectric compounds," *Phys. Chem. Chem. Phys.*, vol. 16, no. 46, pp. 25337-25341, 2014, doi: 10.1039/c4cp03328k.

[58] A. Shafique and Y. H. Shin, "Thermoelectric and phonon transport properties of two-dimensional IV-VI compounds," *Sci. Rep.*, vol. 7, no. 1, pp. 1-10, 2017, doi: 10.1038/s41598-017-00598-7.

[59] C. Chang, G. Tan, J. He, M. G. Kanatzidis, and L. D. Zhao, "The Thermoelectric Properties of SnSe Continue to Surprise: Extraordinary Electron and Phonon Transport," *Chem. Mater.*, vol. 30, no. 21, pp. 7355-7367, 2018, doi: 10.1021/acs.chemmater.8b03732.

[60] F. K. Butt, B. Ul Haq, S. ur Rehman, R. Ahmed, C. Cao, and S. AlFaifi, "Investigation of thermoelectric properties of novel cubic phase SnSe: A promising material for thermoelectric applications," *J. Alloys Compd.*, vol. 715, pp. 438-444, 2017, doi: 10.1016/j.jallcom.2017.05.003.

[61] X. Guan *et al.*, "Thermoelectric properties of SnSe compound," *J. Alloys Compd.*, vol. 643, no. April, pp. 116-120, 2015, doi: 10.1016/j.jallcom.2015.04.073.

### Statements and Declarations

#### Competing Interests

The authors have no relevant financial or non-financial interests to disclose.

#### Data Availability

The datasets generated during and/or analysed during the current study are available in the
Mendeley repository, doi: 10.17632/py638t2nmg.1
(https://data.mendeley.com/datasets/py638t2nmg/1)

#### Author Contribution

All authors contributed to the study conception and design. Material preparation, data collection
and analysis were performed by Mergim Gülmen and Savaş Berber. The first draft of the
manuscript was written by Mergim Gülmen and all authors commented on previous versions of
the manuscript. All authors read and approved the final manuscript.

#### Funding

This research did not receive any specific grant from funding agencies in the public, commercial,
or not-for-profit sectors.

Figure List

Figure 1 (a) Crystal representative of hexagonal-BN and (b) crystal representative of hybrid SnSe-hBN (Sn and Se atoms are shown in orange and blue, B and N atoms are shown in green and grey, respectively).

Figure 2 (a) Crystal representative of cesium lead iodide and (b) crystal representative of hybrid SnSe-CsPbI₃ (Sn and Se atoms are shown in orange and blue, Cs, Pb and I atoms are shown in green, black and purple, respectively).

Figure 3 (a) Band structure and (b) projected total density of states of hybrid SnSe-hBN (c) Band structure and (d) projected total density of states of hybrid and SnSe-CsPbI₃.

Figure 4 (a) Seebeck coefficient as a function of temperature for SnSe-hBN and (b) SnSe-CsPbI₃.

Figure 5 (a) Electrical conductivity vs chemical potential of SnSe-hBN and (b) SnSe-CsPbI₃.

Figure 6 (a) Seebeck coefficient vs chemical potential of SnSe-hBN and (b) SnSe-CsPbI₃.

Figure 7 (a) The power factor ($S^{2}\sigma/\tau$) of SnSe-hBN and (b) SnSe-CsPbI₃.

Figure 8 (a) The electronic part of the thermoelectric figure of merit ($ZT_{elec}$) for SnSe-hBN and (b) SnSe-CsPbI₃.

Figure 9 (a) Electronic thermal conductivity as a function of chemical potential of SnSe-hBN and (b) SnSe-CsPbI₃.

Figure 10 The electronic part of the thermoelectric figure of merit ($ZT_{elec}$) of CsPbI₃ with different number of layers.

Figure 11 The structure of monolayer, bilayer, three-layered and four-layered of CsPbI₃.

Table 1. The highest values of electrical conductivity $(\sigma/\tau)$, Seebeck coefficients $(S)$, power factor $(PF)$ and figure of merit $(ZT_{elec})$ of the SnSe-hBN and SnSe-CsPbI₃ from 100 K to 1000 K.

<table>
<thead>
<tr>
<th rowspan="2">Temperature (K)</th>
<th colspan="2">$\boldsymbol{(\sigma/\tau)}$ <br> $\boldsymbol{(/\Omega ms)(\times10^{19})}$</th>
<th colspan="2">$\boldsymbol{S}$ <br> $\boldsymbol{(\mu V/K)}$</th>
<th colspan="2">$\boldsymbol{PF}$ <br> $\boldsymbol{(W/mK^{2}s)(\times10^{10})}$</th>
<th colspan="2">$\boldsymbol{ZT_{elec}}$</th>
</tr>
<tr>
<td>SnSe-hBN</td>
<td>SnSe-CsPbI₃</td>
<td>SnSe-hBN</td>
<td>SnSe-CsPbI₃</td>
<td>SnSe-hBN</td>
<td>SnSe-CsPbI₃</td>
<td>SnSe-hBN</td>
<td>SnSe-CsPbI₃</td>
</tr>
</thead>
<tbody>
<tr>
<td>100</td>
<td>5.57</td>
<td>2.19</td>
<td>2326</td>
<td>2543</td>
<td>2.43</td>
<td>1.09</td>
<td>0.985</td>
<td>0.991</td>
</tr>
<tr>
<td>200</td>
<td>5.52</td>
<td>2.15</td>
<td>1742</td>
<td>1964</td>
<td>4.13</td>
<td>2.05</td>
<td>0.966</td>
<td>0.980</td>
</tr>
<tr>
<td>300</td>
<td>5.47</td>
<td>2.12</td>
<td>1189</td>
<td>1302</td>
<td>5.33</td>
<td>2.99</td>
<td>0.950</td>
<td>0.961</td>
</tr>
<tr>
<td>400</td>
<td>5.43</td>
<td>2.08</td>
<td>910</td>
<td>975</td>
<td>6.60</td>
<td>3.97</td>
<td>0.933</td>
<td>0.944</td>
</tr>
<tr>
<td>500</td>
<td>5.39</td>
<td>2.03</td>
<td>735</td>
<td>783</td>
<td>7.93</td>
<td>5.07</td>
<td>0.912</td>
<td>0.930</td>
</tr>
<tr>
<td>600</td>
<td>5.35</td>
<td>1.98</td>
<td>615</td>
<td>657</td>
<td>9.07</td>
<td>6.21</td>
<td>0.888</td>
<td>0.913</td>
</tr>
<tr>
<td>700</td>
<td>5.32</td>
<td>1.93</td>
<td>527</td>
<td>568</td>
<td>10.01</td>
<td>7.25</td>
<td>0.861</td>
<td>0.889</td>
</tr>
<tr>
<td>800</td>
<td>5.28</td>
<td>1.88</td>
<td>461</td>
<td>502</td>
<td>11.06</td>
<td>8.13</td>
<td>0.832</td>
<td>0.876</td>
</tr>
<tr>
<td>900</td>
<td>5.24</td>
<td>1.83</td>
<td>409</td>
<td>451</td>
<td>11.99</td>
<td>8.85</td>
<td>0.802</td>
<td>0.865</td>
</tr>
<tr>
<td>1000</td>
<td>5.19</td>
<td>1.79</td>
<td>367</td>
<td>409</td>
<td>12.93</td>
<td>9.46</td>
<td>0.773</td>
<td>0.854</td>
</tr>
</tbody>
</table>

Table 2. The comparison of some $ZT$ values reported in literature for the materials used in the present study.

<table>
<thead>
<tr>
<th>Material</th>
<th>ZT</th>
<th>Temperature (K)</th>
<th>Ref.</th>
</tr>
</thead>
<tbody>
<tr>
<td>Single crystal</td>
<td>2.6</td>
<td>923</td>
<td>[17]</td>
</tr>
<tr>
<td>Cmcm-SnSe</td>
<td>0.8</td>
<td>100-850</td>
<td>[25]</td>
</tr>
<tr>
<td>$\pi$-SnSe</td>
<td>0.998-0.889</td>
<td>200-900</td>
<td>[60]</td>
</tr>
<tr>
<td>monolayer-SnSe</td>
<td>2.63</td>
<td>700</td>
<td>[58]</td>
</tr>
<tr>
<td>SnSe-compound</td>
<td>1.87</td>
<td>800</td>
<td>[61]</td>
</tr>
<tr>
<td>n type-SnSe</td>
<td>0.70</td>
<td>793</td>
<td>[54]</td>
</tr>
<tr>
<td>$\pi$-SnSe</td>
<td>0.74</td>
<td>300</td>
<td>[55]</td>
</tr>
<tr>
<td>p type-SnSe</td>
<td>0.60</td>
<td>750</td>
<td>[56]</td>
</tr>
<tr>
<td>SnSe-hBN</td>
<td>0.985-0.802</td>
<td>100-900</td>
<td>our work</td>
</tr>
<tr>
<td>SnSe-CsPbI₃</td>
<td>0.991-0.865</td>
<td>100-900</td>
<td>our work</td>
</tr>
<tr>
<td>layered-CsPbI₃</td>
<td>2.5</td>
<td>150</td>
<td>our work</td>
</tr>
</tbody>
</table>

![](./images/1201875355921547273_1.jpg)

![](./images/1201875355921547273_2.jpg)

![](./images/1201875355921547273_3.jpg)

![](./images/1201875355921547273_4.jpg)

![](./images/1201875355921547273_5.jpg)

![](./images/1201875355921547273_6.jpg)

![](./images/1201875355921547273_7.jpg)

![](./images/1201875355921547273_8.jpg)

![](./images/1201875355921547273_9.jpg)

![](./images/1201875355921547273_10.jpg)

![](./images/1201875355921547273_11.jpg)

![](./images/1201875355921547273_12.jpg)

![](./images/1201875355921547273_13.jpg)

![](./images/1201875355921547273_14.jpg)

![](./images/1201875355921547273_15.jpg)