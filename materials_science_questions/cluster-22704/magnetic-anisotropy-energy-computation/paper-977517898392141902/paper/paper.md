RESEARCH ARTICLE | FEBRUARY 16 2024

Two-dimensional monolayer $CrGaS_3$: A ferromagnetic semiconductor with high Curie temperature and tunable magnetic anisotropy

Minghao Jia ; Zhirui Gao ; Yunfei Zhang ; Shuo Zhang ; Junguang Tao ; Lixiu Guan

![](./images/977517898392141902_1.jpg)

J. Appl. Phys. 135, 073903 (2024)
https://doi.org/10.1063/5.0191120

![](./images/977517898392141902_2.jpg)
![](./images/977517898392141902_3.jpg)
![](./images/977517898392141902_4.jpg)

![](./images/977517898392141902_5.jpg)

# Two-dimensional monolayer CrGaS₃: A ferromagnetic semiconductor with high Curie temperature and tunable magnetic anisotropy

Cite as: J. Appl. Phys. 135, 073903 (2024); doi: 10.1063/5.0191120
Submitted: 11 December 2023 · Accepted: 29 January 2024 ·
Published Online: 16 February 2024

![](./images/977517898392141902_6.jpg)

Minghao Jia,¹ Zhirui Gao,¹ Yunfei Zhang,² Shuo Zhang,² Junguang Tao,²,a and Lixiu Guan¹,a

## AFFILIATIONS
¹School of Sciences, Hebei University of Technology, Tianjin 300401, China
²School of Materials Science and Engineering, Hebei University of Technology, Tianjin 300132, China

a)Authors to whom correspondence should be addressed: jgtao@hebut.edu.cn and lixiuguan@hebut.edu.cn

## ABSTRACT
Two-dimensional (2D) intrinsic ferromagnetic (FM) materials are promising candidates for fabricating next generation high-performance spintronic devices. However, all experimentally verified 2D FM semiconductors have Curie temperature ($T_c$) far below room temperature, which hinders their practical applications. Based on first-principles calculations, a stable and previously undiscovered 2D CrGaS₃ structure is predicted, which is a semiconductor with an indirect bandgap of 1.99 eV and displays out-of-plane magnetic anisotropy. More importantly, it exhibits high-temperature ferromagnetism, with $T_c$ ranging between 520 and 814 K. The high $T_c$ is attributed to the presence of both direct-exchange and super-exchange interactions that are ferromagnetic, along with the $e_g$-$p_x$/$p_y$-$e_g$ super exchange having a zero virtual exchange gap. Furthermore, it has been observed that the magnetic anisotropy can be tuned by external strain. These findings indicate its potential as a promising candidate for the rapid development of 2D spintronic applications.

© 2024 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC) license (https://creativecommons.org/licenses/by-nc/4.0/). https://doi.org/10.1063/5.0191120

## I. INTRODUCTION
Since the discovery of graphene in 2004,¹ the family of two-dimensional (2D) materials has quickly expanded to h-BN,² Cr₂X₂Te₆ (X = Si, Ge),³⁴ MoS₂,⁵ MTe₂ (M = V, Nb, Ta),⁶ and NbSe₂,⁷ which possess unique physical and chemical properties that make them attractive for a wide range of applications, including spintronics, catalysts, energy storage, and conversion.⁸⁹ As a candidate for manufacturing spin electronic devices, 2D magnetic semiconductors allow for greater freedom in device performance regulation because of the integration of semiconductor, magnetic, and low-dimensional characteristics that can be harnessed for advancing spintronics and developing innovative electronic devices with improved functionality and performance. Compared with ferromagnetic (FM) metals, 2D FM semiconductors have better voltage-regulated carrier behavior, which allows for a precise modulation of spin states, enabling the development of more versatile and energy-efficient spintronic devices. In addition, their unique properties lend themselves to wide applications for low power consumption, high storage density, and strong data retention, which are highly desirable traits for spin-based memory and logic devices.

In 2017, Gong and Huang *et al.* made significant contributions to the understanding of long-range magnetic ordering in CrI₃ and Cr₂Ge₂Te₆.¹⁰¹¹ The ability to achieve long-range magnetic ordering in 2D materials is significant because it opens up exciting opportunities for exploring magnetic properties at nanoscale and has significant implications for various fields, including fundamental physics, magnetic heterostructures, and the advancement of spintronics. Since then, a number of high $T_c$ semiconductor materials with long-range magnetic ordering, tunable ferromagnetism, and robustness have been introduced, such as CrX (X = P, As),¹² InCrTe₃,⁹ CrSX (X = Cl/Br/I),¹³ CrSbS₃,¹⁴ VClBr₂,¹⁵ and VClI₂.¹⁶ From a fundamental physics perspective, the observation of long-range magnetic ordering in 2D materials challenges existing theoretical frameworks and provides new insights into the behavior of magnetic systems at the nanoscale. The maintenance of long-range magnetic ordering in single or few layers of these materials

represents a departure from the predictions of the Mermin-
Wagner theorem, which suggests that thermal fluctuations would disrupt the long-range magnetic order in 2D systems at finite temperatures. The ability to overcome the effects of thermal perturbation opens up new avenues for exploring and harnessing their unique magnetic properties. However, one of the critical challenges facing 2D magnetic semiconductor materials as they move toward practical applications is the issue of their Curie temperature ($T_c$) being far below room temperature. For example, the $T_c$ of monolayer (ML) $CrI_3$ is only $\sim$45 K, and it is $\sim$20 K for $Cr_2Ge_2Te_6$. Recently, 2D semiconducting CrSBr was found to be air-stable with a $T_c$ of $\sim$145 K. Under a hole doping of $n_p$$>$$4 \times 10^{12}$ cm$^{-2}$, its magnetization easy axis can be tuned from in-plane to out-of-plane. However, there are still some uncertainties in the theoretical prediction of its $T_c$ using the 2D Ising model, which ranges from 150 to 300 K. Nevertheless, raising the $T_c$ of 2D magnetic semiconductors to ambient operating conditions is crucial for their practical use.

At present, many strategies have been proposed to modify the magnetic properties of 2D materials, such as strain engineering, intercalation, electronic structure modification, magnetic element doping, interface engineering, defect introduction, Janus structure construction, and optical tuning. However, these approaches have been evaluated only for a few experimentally reported 2D magnets. For many newly discovered 2D magnets, their magnetic responses to strain, electron doping, magnetic fields, and other modifications have not been publicly documented. Therefore, further investigation is necessary to comprehend the magnetic response mechanisms of these 2D magnets. In general, transition metal elements with partially occupied $3d$ orbitals are the main source of magnetic moment in 2D FM materials. These transition metal atoms combined with nonmetal elements can be periodically arranged into 2D lattices, leading to specific long-range magnetic orders. At present, a variety of experimentally discovered 2D magnetic semiconductors are closely correlated with the Cr element. For instance, $Cr_xGa_{1-x}Te$ single crystals with highly tunable room temperature ferromagnetism were grown experimentally, and their saturation magnetic moment can be adjusted by 5.4 $-$75.9 times by changing their thickness and Cr concentration. Replacing Pt (up to 45%) in $PtTe_2$ with Cr can lead to the formation of a stable high $T_c$ (220 K) FM $Cr_xPt_{1-x}Te_2$. The magnetic properties of FM $Cr_2Te_3$ nanorods can be effectively regulated by changing the Cr:Te ratio. At Cr:Te = 1:1.8, they exhibit a large magnetic anisotropy energy, and the saturation magnetization can reach 22.7 emu/g.

On the other hand, 2D Janus materials, a new type of material with distinct properties on each side, can be exploited for various applications, such as in electronics, photonics, and catalysis. Recently, 2D Janus materials were successfully synthesized for the fabrication of field-effect transistors, ultrasensitive detectors, spintronic devices, and valley electronic devices. In 2021, Guo et al. constructed $CrBr_{1.5}I_{1.5}$ by replacing one layer of I atoms in $CrI_3$ with Br atoms and found it to be a semiconductor material with intrinsic magnetic properties and considerable magnetic anisotropy. Lu et al. demonstrated the existence of vertical dipoles in the Janus MoSSe structure by second harmonic generation and pressure-response force microscopy replacing the top S with Se atoms in ML $MoS_2$. In addition, Guan et al. found that Janus 2H-VSeTe has great valley polarization and ultrahigh $T_c$. Janus $Cr_2O_2XY$ (X = Cl, Y = Br/I) monolayers were proposed as a novel material by Jiao et al., which are FM semiconductors and can be easily synthesized experimentally. Previous studies on 2D Janus material systems mainly focused on the Rashba effect, piezoelectric properties, and photocatalytic properties because of their immediate technological relevance, while the magnetic coupling mechanism in these systems is particularly significant, as it can provide insights into their potential use in magnetic storage, magnetic sensors, and spin-based technologies. However, investigations on the magnetic coupling mechanism in Janus systems are currently scarce, which represents a significant gap in current research. Additionally, understanding the magnetic behavior of 2D Janus materials can open up new avenues for designing and engineering multifunctional materials with combined magnetic and electronic functionalities. Therefore, future research efforts should prioritize the exploration of the magnetic properties of 2D Janus materials, including their magnetic ordering, magnetic anisotropy, and spin dynamics. This will not only advance our fundamental understanding of these materials but also pave the way for their practical utilization in emerging magnetic technologies.

In this work, using first-principles calculations, we have designed and systematically studied the electronic and magnetic properties of $CrGaS_3$ ML to provide a basis for its application in spintronics; it is constructed from $\alpha-In_2Se_3$ by replacing In with Cr and Ga. Phonon spectrum and molecular dynamics simulations at room temperature confirm its structure and thermodynamic stability. It is found that $CrGaS_3$ is a FM semiconductor with an indirect bandgap of 1.99 eV. The $T_c$ is predicted to be in the range of 520$-$814 K, far above the room temperature. The magnetic anisotropy energy (MAE) is 13.82 $\mu$eV, making it robust in maintaining FM ordering. Notably, the easy magnetization axis is out-of-plane, which can be tuned into in-plane by applying biaxial stress. In addition, its $T_c$ can be adjusted with the application of biaxial strain. Our study highlights the origin of the magnetic coupling for $CrGaS_3$ and the method of regulating its $T_c$. The ultrahigh $T_c$ offers the possibility of its practical applications.

## II. COMPUTATIONAL DETAILS

In this work, all density functional theory (DFT) calculations were carried out using the Vienna ab initio simulation package (VASP). The generalized gradient approximation (GGA) in the form of Perdew$-$Burke$-$Ernzerhof (PBE) was used to handle the exchange-correlation generalized function between electrons. The projector-augmented wave (PAW) method was used to handle the interaction between ions and electrons. Plane wave cutoff was set to 550 eV. In the structure optimization process, the atomic positions and lattice constants of each system were relaxed sufficiently until the Hermann$-$Feynman force acting on each atom was less than 0.001 eV/Å, and the electron convergence criterion was set to $10^{-5}$ eV. To eliminate the interaction between the layers, a $z$-direction vacuum greater than 15 Å was introduced to prevent interlayer interactions. Because different van der Waals (vdW) forces have a strong influence on the 2D material system, for ensuring the credibility of the calculations, we considered the standard Grimme's DFT-D3 method, which allows a precise calibration of the force field and a precise optimization of the structure of molecules and solids composed of all elements of the periodic table, as well as the optB86b method, which is very accurate in the

structural characterization of layered materials. For the strong correlation effects of Cr $3d$ electrons, we adopted the GGA + U method to more accurately characterize the electronic interactions in Cr $d$-orbitals, according to Dudarev's method, $^{43}$ with an effective $U$ ($U_{\text{eff}}$) of 2, 3, and 4 eV, which are consistent with those used in previous reports for CrI$_3$, $^{44}$ CrS$_2$, $^{45}$ and CrCX (X = Cl, Br, I; C = S, Se, Te). $^{46}$ For the subsequent discussion of the electronic structure and its magnetic exchange mechanism, we chose the same $U_{\text{eff}}$ value of 3 eV as those previously reported 2D Cr compounds. $^{44-46}$ In order to obtain magnetic ground states and to validate the electronic structure of the PBE calculations, we also performed the calculations using the Heyd-Scuseria-Ernzerhof (HSE06) hybrid functionals. $^{36}$ The phonon spectrum was obtained using the PHONOPY code $^{47}$ that interfaces well with VASP using a $4 \times 4 \times 1$ supercell.

The $ab$ $initio$ molecular dynamics (AIMD) simulation was employed to evaluate the structure stability using the single $\Gamma$ $k$-point at 300 K with a time step of 3 fs, where the Nosé algorithm was used to control the temperature. $^{48}$ The Curie temperature, founded on the Heisenberg model, was estimated via Monte Carlo (MC) simulations. The simulation was performed for at least $10^5$ steps at each temperature to ensure statistical reliability using a $30 \times 30$ supercell.

## III. RESULTS AND DISCUSSIONS
### A. Geometry and structure stability of CrGaS$_3$

Recently, many experimental reports on the studies of Cr$_x$Ga$_{1- x}$Te, Cr$_x$Pt$_{1- x}$Te$_2$ systems have surfaced. $^{28,31}$ Inspired by this, we used $\alpha$-In$_2$Se$_3$ as the parent material and replaced In and Se atoms with Ga (Cr) atoms and S atoms, respectively, to construct the CrGaS$_3$ structure model. Because $\alpha$-In$_2$Se$_3$ Ml consists of five atomic layers and is stacked in the order of Se-In-Se-In-Se, $^{49}$ the positions of two In in $\alpha$-In$_2$Se$_3$ are not equivalent, with one forming a tetrahedron with the surrounding Se atoms and the other one being in an octahedron environment. As a result, two configurations can be constructed by replacing In with Cr and Ga (see Fig. 1 and Fig. S2 in the supplementary material). For the

![](./images/977517898392141902_7.jpg)

FIG. 1. (a) and (b) Top and side views of an ML CrGaS$_3$ structure. The green, blue, and yellow balls represent Ga, Cr, and S atoms, respectively. (c) Charge density plot of CrGaS$_3$ with $0.04$ e/$\text{\AA}^3$ isosurfaces. The yellow isosurfaces represent the electron aggregation region. (d) Perspective view of the FM ordered spin charge density plotted in $0.001$ e/$\text{\AA}^3$ contours. The red and blue isosurfaces correspond to spin-up and spin-down charges, respectively. (e) and (f) show the direct-exchange and superexchange schematics, respectively, for ML CrGaS$_3$.

convenience of discussion, we will name S-In-S-Cr-S as CBCAC [Fig. 1(b)] and S-Cr-S-In-S as CACBC [Fig. S2(b) in the supplementary material] based on the atomic occupancy of the atomic layer from top to bottom. Both structures have the space group of P3m1 (#156), with the upper Ga(Cr) atom sandwiched between two S atoms and forming a twisted tetrahedron with the four surrounding S atoms. The lower layer of Cr(Ga) atoms forms a graphene-like honeycomb lattice structure with a twisted octahedron with six S atoms.

To assess the structure stability of ML CrGaS₃, the analysis of the phonon spectrum is taken into consideration, which is shown in Fig. 2(a) and Fig. S2(d) in the supplementary material. In Fig. 2(a), there are some slight imaginary frequencies at the Γ point for the CBCAC configuration, which, however, have a negligible effect on the following discussions, as many other 2D materials hold the same behavior, as reported in previous studies.⁵⁰,⁵¹ In contrast, the CACBC configuration has significant imaginary frequencies near the Γ and M points of the acoustic branch, as shown in Fig. S2(d) in the supplementary material, suggesting that atoms at nearby equilibrium positions are unstable. The instability of CrGaS₃ in the CACBC configuration may be due to the strong electronic coupling effect of Cr atoms in CrGaS₃. The instability of the CACBC configuration can also be confirmed by its system energy, which is 0.61 eV/f.u. higher than that of the CACBC configuration. As shown in Figs. S2(f) and S2(g) in the supplementary material, in an octahedral crystal field, the d-orbitals of Cr atoms are split into double degeneracy e_g-orbital and triple degeneracy t_2g-orbital, where the e_g-orbital energy level is higher than that of t_2g-orbital. On the other hand, in the tetrahedral crystal field, the e_g-orbital is lower than t_2g-orbital in energy. Therefore, the energy level relationship in the tetrahedral crystal field is opposite to that in the octahedral crystal field. This indicates that when magnetic atoms are placed in different sites, the different crystal field environment may have a strong influence on its structural and magnetic stability. In the CACBC configuration, the Cr atom is in a tetrahedral crystal field, indicating that there will be excess electrons at higher energy t_2g-orbitals. The partially filled t_2g-orbitals make it easier for electron transport and render the system metallic in nature, as reflected in Fig. S2(e) in the supplementary material. While for the CBCAC configuration, the three excess electrons on the Cr atom mainly occupy the relatively low t_2g-orbitals, making the valance band fully occupied, thus exhibiting semiconductor characteristics, as shown in Fig. 3. In the following, we will mainly focus on the CBCAC configuration, which is a semiconducting system with structural and energetic stability. There are three different S atomic layers in the system. In order to distinguish them for easy discussion, we have given different names for them, namely, S_top, S_mid, and S_bott, from top to bottom.

In order to further verify the thermodynamic stability of CrGaS₃, AIMD simulation is performed at 300 K. As shown in Fig. 2(b), the total energy fluctuation of ML CrGaS₃ is almost constant with the simulation time step and the structure remains stable within 3 ps. These results indicate that the ML CrGaS₃ structure is thermodynamically stable. Because the CBCAC configuration belongs to space group of P3m1 (#156), its force constants are also obtained, which are \(C_{11}=37.491\ \text{N/m}\), \(C_{12}=8.459\ \text{N/m}\), \(C_{13}=-1.479\ \text{N/m}\), \(C_{14}=0.825\ \text{N/m}\), \(C_{33}=0.546\ \text{N/m}\), \(C_{44}=2.613\ \text{N/m}\), and \(C_{66}=14.516\ \text{N/m}\). Clearly, the force constants satisfy the Born-Huang conditions:⁵² \(C_{11}>|C_{12}|\), \(C_{44}>0\),

![](./images/977517898392141902_8.jpg)

FIG. 2. (a) Phonon spectrum of the CBCAC structural configuration of ML CrGaS₃. (b) Evolution of the total energy of the CrGaS₃ supercell with time obtained from the AIMD simulation at 300 K. The insets are the corresponding structures at a given time, which show the stability of the structure without noticeable deformation.

![](./images/977517898392141902_9.jpg)

FIG. 3. (a) Band structure of ML CrGaS₃ for DFT-D3 at Uₑff=3 eV. The red and black curves represent the spin-up and spin-down bands, respectively. (b) 3D band counter of the valance band maximum. (c) Band structure at the HSE06 level. (d) First Brillouin zone of ML CrGaS₃ (black hexagon) with high-symmetry points indicated. The area surrounded by the blue lines is the area of the 3D band structure in (b).

$$C_{13}^{2}<\frac {1}{2}C_{33}(C_{11}+C_{12}),\ \ \ \ \ C_{14}^{2}<\frac {1}{2}C_{44}(C_{11}-C_{12})=C_{44}C_{66},$$
which suggest that the system is mechanically stable. In short, the above calculations corroborate the fact that the constructed CBCAC configuration of CrGaS₃ is structurally, thermodynamically, and mechanically stable.

To evaluate the possibility of synthesizing ML CrGaS₃, we proposed three potential synthesis methods and calculated the formation energies of each scheme.
Scheme 1: $\mathrm{Cr}+\mathrm{Ga}+3\mathrm{S}\to\mathrm{CrGaS}_{3}$,
Scheme 2: $\mathrm{CrS}+\mathrm{GaS}+\mathrm{S}\to\mathrm{CrGaS}_{3}$,
Scheme 3: $\mathrm{CrS}_{2}+\mathrm{GaS}\to\mathrm{CrGaS}_{3}$.

The corresponding formation energy can be obtained by
$$E_{f1}=E(\mathrm{CrGaS}_{3})-E(\mathrm{Cr})-E(\mathrm{Ga})-3E(\mathrm{S}),\tag{1}$$

$$E_{f2}=E(\mathrm{CrGaS}_{3})-E(\mathrm{CrS})-E(\mathrm{GaS})-E(\mathrm{S}),\tag{2}$$

$$E_{f3}=E(\mathrm{CrGaS}_{3})-E(\mathrm{CrS}_{2})-E(\mathrm{GaS}).\tag{3}$$

All precursors used in the abovementioned synthesis schemes are experimentally stable crystals, demonstrating the practicality of the proposed synthesis approach. The formation energies for the three schemes are −2.26, −1.94, and −2.31 eV, respectively, all of which are significantly negative, indicating the feasibility of experimentally synthesizing the CrGaS₃ monolayer.

### B. Electronic structure of CrGaS₃
From Fig. 3(a), it can be seen that the valence band maximum (VBM) of the system is located along the $\Gamma$-$K$ path, while the conduction band minimum (CBM) is located at the $M$ point, resulting in an indirect bandgap characteristic of the system. In addition, this bandgap occurs only in the spin-up channel, which results in a fully spin-polarized bandgap of 0.77 eV at the GGA + U level. Clearly, this is of advantage in the application of spin-based electronic devices. In order to further verify the energy band characteristics of the system, we adopted the HSE06 method, and the obtained energy band structure is provided in Fig. 3(c). It is worth noting that the band dispersion features of CrInX₂ obtained through GGA + U and HSE06 are highly consistent, with the only difference being that the bandgap of the system increases to 1.99 eV at the HSE06 level.

In addition, as shown in Fig. 3(a), the band structure of
CrGaS₃ exhibits a Mexican hat-like energy band structure at the
VBM, which is contributed entirely by the spin-up electrons.
Unlike the conventional energy band structure in which the VBM
has a parabolic shape, the Mexican hat-like energy band structure
exhibits a ring of flatbands around the first Brillouin $\Gamma$ point, as
shown in Fig. 3(b), which suggests that the electrons have an isotropic and localized behavior. Moreover, the energy band structure of
the Mexican hat-like feature also indicates that CrGaS₃ has potential for use in thermoelectric applications.⁵³

In order to have a more comprehensive and accurate understanding of the electronic structure characteristics, the electronic
band structure of CrGaS₃ is accessed using two different vdW
forces, which are optB86b and DFT-D3 (see Fig. S3 in the
supplementary material). In all cases, the positions of the VBM
and CBM do not change, nor does the size of the bandgap change
significantly, suggesting that the electronic properties of the system
are not sensitive to the different vdW correction methods.

From Figs. 4 and 5(a), it can be seen that the electronic states
near the Fermi level ($E_F$) are mainly contributed by Cr, Ga, $S_{\text{mid}}$,

![](./images/977517898392141902_10.jpg)

FIG. 4. Orbital projected band structure of ML CrGaS₃ for DFT-D3 at $U_{\text{eff}}$ = 3 eV. (a)-(e) Energy band projections of the Cr $d$ orbital, the Ga $s$ orbital, and the $p$ orbitals of
$S_{\text{mid}}$, $S_{\text{top}}$, and $S_{\text{bott}}$, respectively. (f) is the overall band structure with red curves for spin-up and black curves for spin-down electrons.

![](./images/977517898392141902_11.jpg)

FIG. 5. (a) PDOS of ML CrGaS₃ in DFT-D3 with $U_{\text{eff}}$ = 3 eV. (b) Angular relationship between the magnetization direction and the MAE in the $x$-$z$ plane, $y$-$z$ plane, and $x$-$y$ plane.

and $S_{\text{bott}}$ atoms, with Cr atoms contributing the most. The VBM of the Mexican-hat structure mainly emanates from the hybridization between Cr $e_g$-orbitals and the $S_{\text{bott}}$ $p_z$ orbital. In Figs. 4(b) and 4(d), it can be seen that the Ga and $S_{\text{top}}$ atoms barely contribute to the VBM. Specifically, the valence band near the $E_F$ is dominated by the hybridization of $S_{\text{mid}}$ $p_x$ and $p_y$ orbitals, the $S_{\text{bott}}$ $p_z$ orbital, and the $e_g$ orbital of the Cr atoms. On the other hand, the conduction band near the $E_F$ is mainly constructed by Cr $d_{yz}$ and $d_{xz}$ orbitals, the Ga $s$ orbital, the $S_{\text{top}}$ $p_y$ orbital, and the $S_{\text{bott}}$ $p_z$ orbital. A comparison of the calculated density of states (DOS) with different vdW correction methods of optB86 and DFT-D3 ($U_{\text{eff}}$ = 2, 3, 4 eV) is provided in Fig. S4 in the supplementary material. It can be found that the orbital contributions have the same components near the $E_F$, while the degree of orbital contribution varies with the change of $U_{\text{eff}}$.

The exchange interaction between the magnetic atoms of a 2D magnetic material and the surrounding nonmagnetic atoms is an important factor affecting its $T_c$. From Fig. 1(d), it can be seen that Cr is the source of the magnetic moments of ML CrGaS₃, and there is barely spin distribution around Ga and $S_{\text{top}}$. By analyzing the projected density of states (PDOS) of the Cr atom, $S_{\text{mid}}$, and $S_{\text{bott}}$ atom (see Fig. S4 in the supplementary material), it is found that they show a noticeable variation with $U_{\text{eff}}$, which will lead to different FM coupling strengths at different $U_{\text{eff}}$ values. With the increase of $U_{\text{eff}}$, although the DOS distribution of the Cr $d$ spin-up orbitals changes, the spin-down states remain unoccupied. The spin-up state of the $d$ orbitals is partially occupied and the VBM is mainly contributed by the Cr $d_{z^2}$ orbitals. The state near the $E_F$ for the $S_{\text{bott}}$ atoms is mainly contributed by the spin-up $p_z$ orbitals, and the contribution increase with the increase of $U_{\text{eff}}$. On the other hand, the DOS of $S_{\text{mid}}$ near the $E_F$ is mainly contributed by the spin-up states of $p_y$, $p_x$ orbitals, with an increasing density of $p_z$ orbital states near the $E_F$ and a gradually decreasing density of the $p_y$ orbital states in the spin-down states with respect to the increase of $U_{\text{eff}}$.

### C. Magnetic properties of CrGaS₃

The magnetic ground state is an important factor in determining the physical properties of the material. In order to determine the magnetic ground state configuration of CrGaS₃, three magnetic configurations were considered, as shown in Fig. S1 in the supplementary material. To evaluate the magnetic interaction strength, the exchange energy is calculated, which is defined as $E_{ex} = (E_{\text{AFM}} - E_{\text{FM}})$, where $E_{\text{AFM}}$ and $E_{\text{FM}}$ are the corresponding energies of the AFM and FM states. As shown in Fig. 6, the FM ordered CrGaS₃ has the lowest energy among all three magnetic states regardless of the vdW correction method and the $U_{\text{eff}}$ values, which means that the CrGaS₃ FM state is the most stable.

From Fig. 1(c), the charge density of CrGaS₃ is aggregated around the S atom, and it is negligible on the Ga atom. Combining the magnetic moment distributions given in Table I and the qualitative analysis of Bader charge transfer in Table S1 in the supplementary material indicates that most of the valence electrons of the Ga atom are consumed to form bonds with $S_{\text{top}}$ and $S_{\text{mid}}$. In

![](./images/977517898392141902_12.jpg)

FIG. 6. Variations of the exchange parameters as a func- tion of Hubbard U. $J_{1}$ and $J_{2}$ of the isotropic 1NN and2NN exchange parameters are given in (a); $\lambda_{1}$ and $\lambda_{2}$ of the anisotropic 1NN and 2NN exchange parameters and single-ion anisotropy, $D$ , are given in (b). The black and red data points stand for optB86b and DFT-D3 vdW cor- rection methods, respectively.

CrGaS₃, each Cr atom transfers 2.7 electrons to the surrounding S atom, with ~3.3 electrons remaining. As some electrons from Ga occupy the outermost $p$ orbital of $S_{mid}$, the super-exchange channel between $S_{mid}$ and Cr is reduced, and therefore, the super exchange of Cr-S is mainly conducted via $S_{bott}$. As stated above, in an octahedral coordination environment, Cr $d$ orbitals are divided into two groups: the higher $e_{g}$-orbitals $(d_{x 2-y 2}, d_{z 2})$ and the lower $t_{2 g^{-}}$ -orbitals $(d_{x z}, d_{y z}, d_{x y})$. According to Hund's rule, as shown in Fig. 1(f), the three spin-up electrons of the Cr atom will occupy the lowest $t_{2 g}$-orbitals, with the remaining 0.3 electrons filling the $e_{g}$-orbitals. Therefore, the super-exchange channels in this system would be different from other Cr-based 2D FM semiconductor, such as CrI₃. In CrI₃, the $t_{2 g}$-orbitals are completely occupied, and the magnetic coupling is mediated through the virtual exchange with the empty $e_{g}$-orbital. However, the large virtual exchange gap $(G_{ex})$ between $t_{2 g}$ and $e_{g}$ orbital for $CrI_{3},^{54} \sim 2 eV$ , results in a rather low $T_{c}(\sim 50 ~K)$ . It is demonstrated that by reducing the $G_{ex}$ via W alloying can greatly promote magnetic exchange interactions. $^{54}$ As a result, $T_{c}$ is boosted from 50 to $180 ~K$ . This demonstrates that the energy barrier of virtual exchange plays an important role in improving $T_{c}$ . Based on our above analysis that the $e_{g}$-orbitals will be partially filled in CrGaS₃, it is not difficult to see that an efficient super exchange can occur through $e_{g}-e_{g}$ and $t_{2 g}-e_{g}$ , with a virtual exchange gap of 0 in the former [see the schematic drawing in Fig. 1(f)]. The zero virtual exchange gap will greatly reduce the super-exchange barrier and thus greatly improve the $T_{c}$ of the system, which will be verified in the following.

In ML CrI₃, the Mermin-Wagner theorem is violated to form a stable long-range FM order because its magnetic anisotropy overcomes the effects of thermal perturbations. Thus, magnetic anisotropy is important for forming stable 2D magnetic materials. In order to determine the MAE and easy magnetization axis of CrGaS₃, nonlinear magnetic calculations are performed with the consideration of the spin-orbit coupling (SOC) effect. In Fig. 5(b), the corresponding angular distributions of the MAE in the x-z plane, y-z plane, and x-y plane are presented, where the MAE is defined as MAE $=E_{[u v w]}-E_{[001]}$ , with $E_{[u v w]}$ and $E_{[001]}$ referring to system energies for spin aligning along the arbitrary [uvw] direc- tion and out-of-plane [001] axis, respectively. As seen, there is no energy variation in the x-y plane and the easy axis is out-of-plane with a MAE value of $13.82 \mu eV$ . The MAE can originate from the strong hybridization between Cr $d$ and S $p$ orbitals, which is in agreement with the previous analysis. Meanwhile, we calculated the MAE for the remaining cases (under the influence of both van der Waals forces in optB86b and DFT-D3, with $U_{eff }=2,3$ , and $4 eV$ ), and the results are presented in Table S2 in the supplementary material. It is observed that ML CrGaS₃ consistently maintains an out-of-plane easy magnetization axis in all cases.

$T_{c}$ is a key parameter for evaluating the magnetic coupling strength of magnetic materials. As mentioned above, the ground state of CrGaS₃ is FM, and it is necessary to obtain the magnetic exchange coupling parameter that determines the $T_{c}$ of the mag netic phase transition. Because the Ising model overestimates the anisotropy to a large extent, it leads to the much overestimated $T_{c}$ . Therefore, to make the simulation results more reliable, anisotropic Heisenberg spin Hamiltonian is used with the consideration of the non-negligible single-ion anisotropy to describe the magneticbehavior in ML CrGaS $3.^{55}$ 

$$
H=H_{0}-\left(\frac{1}{2} J_{1} \sum_{i, j} \vec{S}_{i} \cdot \vec{S}_{j}+\frac{1}{2} J_{2} \sum_{i, l} \vec{S}_{i} \cdot \vec{S}_{l}+D \sum_{i}\left(S_{i}^{z}\right)^{2}+\frac{1}{2} \lambda_{1} \sum_{i, j} \overrightarrow{S_{i}^{e}} \cdot \overrightarrow{S_{j}^{e}}+\frac{1}{2} \lambda_{2} \sum_{i, l} \overrightarrow{S_{i}^{e}} \cdot \overrightarrow{S_{l}^{e}}\right), \tag{4}
$$

where $i$, $j$, and $l$ denote the position coordinates of Cr atoms. The first and second terms are Heisenberg isotropic exchange, with $J_1$ and $J_2$ being the first nearest-neighbor (1NN) and second nearest-neighbor (2NN) exchange parameters, respectively. The 1NN and the 2NN interactions are labeled in Fig. 1(a). The third term describes the easy-axis single-ion anisotropy. The last two terms are anisotropic exchange, where $\lambda_1$ and $\lambda_2$ are 1NN and 2NN anisotropic exchange parameters. The sign convention is such that $J>0$ favors FM interactions; $D>0$ suggests that the material is an out-of-plane easy axis, and $\lambda=0$ refers to fully isotropic exchange interactions. In order to obtain all the parameters, we constructed three different magnetic configurations (see Fig. S1 in the supplementary material) and used the energy difference between six cases to calculate $J_1$, $J_2$, $D$, $\lambda_1$, and $\lambda_2$. The energy of different magnetic configurations in each unit cell can be written as follows:

$$
E(\text{FM}_x) = E_0 - 3J_1S^2 - 3J_2S^2, \tag{5}
$$

$$
E(\text{AFM1}_x) = E_0 + J_1S^2 + J_2S^2, \tag{6}
$$

$$
E(\text{AFM2}_x) = E_0 + \frac{1}{3}J_1S^2 + J_2S^2, \tag{7}
$$

$$
E(\text{FM}_z) = E_0 - 3J_1S^2 - 3J_2S^2 - DS^2 - 3\lambda_1S^2 - 3\lambda_2S^2, \tag{8}
$$

$$
E(\text{AFM1}_z) = E_0 + J_1S^2 + J_2S^2 - DS^2 + \lambda_1S^2 + \lambda_2S^2, \tag{9}
$$

$$
E(\text{AFM2}_z) = E_0 + \frac{1}{3}J_1S^2 + J_2S^2 - DS^2 + \frac{1}{3}\lambda_1S^2 + \lambda_2S^2. \tag{10}
$$

In 2D magnetic materials, in addition to magnetic anisotropy, exchange interactions also play a decisive role in $T_c$. From Fig. 6(b), it can be seen that $D$ decreases as $U_{\text{eff}}$ increases. However, for the value of $J$ ($J=J_1+J_2$), it increases with the increase of $U_{\text{eff}}$ in the DFT-D3 vdW method, while it decreases with the optB86b vdW correction method. Figures S5(a) and S5(b) in the supplementary material provide the results of the variation of the average magnetic moment and specific heat with temperature for different vdW correction methods and $U_{\text{eff}}$ values. It can be easily seen from these figures that the magnitude of the $J$ value plays a decisive role in $T_c$. It is also obvious that the effect of $J_1$ on $T_c$ is stronger than that of $J_2$ when the DFT-D3 vdW correction method is chosen, while the effect of $J_2$ is stronger than that of $J_1$ when the optB86b vdW correction method is chosen. The important point is that regardless of the vdW correction methods, the $T_c$ of $\text{CrGaS}_3$ is higher than room temperature, with the highest $T_c$ being 814 K, which is of great interest as a 2D FM semiconducting material.

Next, we will focus on the magnetic exchange mechanism in $\text{CrGaS}_3$. For 2D FM semiconductor materials, two main types of exchange interactions are commonly discussed: direct-exchange interaction that is sensitive to distance and super exchange mediated by intermediate anions. Through an analysis of $d$-orbital splitting and electron occupation in the previous discussion, the magnetic interactions in $\text{CrGaS}_3$ can be conducted through $\text{Cr}_1$ $e_g$-$\text{Cr}_2$ $e_g$ direct-exchange interactions and the $\text{Cr}_1$-S-$\text{Cr}_2$ superexchange interactions. It has been shown above in the description of the electronic structure of $\text{CrGaS}_3$ that Cr provides the magnetic moment of $3.19\mu_B$ in ML $\text{CrGaS}_3$ and loses 2.7 electrons (see Table I). In $\text{CrGaS}_3$, the Cr-Cr direct exchange of $\text{CrGaS}_3$ belongs to the strong $d$-$d$ interaction$^{56}$ via the half-filled $e_g$-orbitals, which is FM, as shown in Fig. 1(e). The super-exchange process of Cr-S-Cr is mainly realized by $\text{Cr}$-$\text{S}_{\text{bott}}$-$\text{Cr}$, as shown in the virtual exchange path diagram of Fig. 1(f). The virtual exchange gap for the $e_g$-$e_g$ orbitals is 0 eV, which greatly reduces the difficulty of the super-exchange process, thereby increasing its coupling strength.$^{54}$ Additionally, the super-exchange process of $\text{CrGaS}_3$ has three interaction processes: $t_{2g}$-$p_x$/$p_y$-$t_{2g}$, $e_g$-$p_x$/$p_y$-$e_g$, and $t_{2g}$-$p$-$e_g$. These interaction processes are maintained in the same ligand state by Pauli's exclusion principle, which can allow FM spin configurations. It is shown from the band structures and DOS spectra that there is a strong hybridization of Cr with both $S_{\text{mid}}$ and $S_{\text{bott}}$ in the energy range of $-2$ to 2 eV, which can facilitate the strong exchange interactions. Moreover, the magnitude of the magnetic moment of $S_{\text{bott}}$ reaches $0.221\mu_B$, which is quite significant and indicates that it is magnetized. The spin polarization on the ligand enhances the hopping efficiency of the Cr $e_g$-orbitals and S $p$-orbitals.$^{9,57}$ This also explains the reason that $J_1$ increases with increasing $U_{\text{eff}}$. In brief, the greatly prompted super-exchange interaction and the fact that direct-exchange interactions can also be FM are responsible for the large $J$ value, and hence the high $T_c$ of $\text{CrGaS}_3$.

<table>
<caption>TABLE I. The magnetic moments ($\mu_B$) of individual atoms in $\text{CrGaS}_3$ calculated with DFT-D3 and optB86b vdW correction methods for $U_{\text{eff}}=2,3,4$ eV.</caption>
<thead>
<tr>
<th></th>
<th>$U_{\text{eff}}$ (eV)</th>
<th>Cr</th>
<th>Ga</th>
<th>$S_{\text{mid}}$</th>
<th>$S_{\text{top}}$</th>
<th>$S_{\text{bott}}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>DFT-D3</td>
<td>2</td>
<td>3.19</td>
<td>0.002</td>
<td>−0.055</td>
<td>0.000</td>
<td>−0.185</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>3.289</td>
<td>−0.001</td>
<td>−0.067</td>
<td>−0.001</td>
<td>−0.221</td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>3.388</td>
<td>−0.003</td>
<td>−0.079</td>
<td>−0.003</td>
<td>−0.258</td>
</tr>
<tr>
<td>OptB86b</td>
<td>2</td>
<td>3.154</td>
<td>0.001</td>
<td>−0.049</td>
<td>0.000</td>
<td>−0.166</td>
</tr>
<tr>
<td></td>
<td>3</td>
<td>3.252</td>
<td>−0.002</td>
<td>−0.061</td>
<td>−0.002</td>
<td>−0.201</td>
</tr>
<tr>
<td></td>
<td>4</td>
<td>3.348</td>
<td>−0.004</td>
<td>−0.073</td>
<td>−0.003</td>
<td>−0.237</td>
</tr>
</tbody>
</table>

### D. Strain modulation effect on the magnetic properties of $\text{CrGaS}_3$

During heterostructure formation, strain can be introduced into the material due to lattice mismatch between 2D material and substrate. Also, strain is one of the easiest and most effective regulation tools available to tune the electronic characteristics of a 2D material. Therefore, biaxial stress is often used both experimentally and theoretically as a means of adjusting the electronic properties of materials. Strain can be introduced in various ways, such as bending the substrate, heating the substrate, utilizing the piezoelectric effect, and forming bubbles.$^{58}$ Specifically, strain can be induced and regulated in 2D materials by selecting appropriate

flexible substrates and applying external forces. The deformation of the substrate can lead to tensile or compressive strain in 2D materials. A wide range of flexible substrates is available, including polydimethylsiloxane (PDMS), polycarbonate (PC), polystyrene (PS), polyethylene terephthalate (PET), polyethylene naphthalate, and polyimide (PI).⁵⁸ Bending can typically be achieved through two-point or four-point bending using specially designed clamping tools. On the other hand, introducing 2D materials onto patterned substrates is a common approach to induce strain. Additionally, piezoelectric ceramics have the capability to produce mechanical deformation when an excitation electric field is applied, meaning that substrates with piezoelectric effects can induce strain in 2D materials. In this work, we also investigate the effect of biaxial stress on the electronic structure of CrGaS₃ under the DFT-D3 vdW correction method at $U_{\text{eff}} = 3$ eV. When biaxial strain $\varepsilon = \frac{b - b_0}{b_0}$ ($b$ is the lattice constant of the system after applying strain and $b_0$

![](./images/977517898392141902_13.jpg)

FIG. 7. (a) Average magnetic moment and specific heat of ML CrGaS₃ calculated using DFT-D3 at $U_{\text{eff}} = 3$ eV as a function of temperature, respectively. (b) Energy difference between FM and AFM1, AFM2 states with the different biaxial strains. (c) and (d) Variation of exchange parameters with biaxial strain. The gray and pink shadows represent in-plane and out-of-plane easy magnetization axis, respectively.

is the intrinsic one) is applied, the calculated energy difference between the AFM state and the FM state is shown in Fig. 7(b). As seen, the energy difference is positive in the range of $-6\%$ to $6\%$, indicating that there is no change in the magnetic state within this strain range. Obviously, this demonstrates that the ferromagnetism of ${\text{CrGaS}}_{3}$ is quite stable against external strain. To further verify the thermodynamic stability of ${\text{CrGaS}}_{3}$ under $-6\%$-$6\%$ strain, we performed AIMD simulations at 300 K. As depicted in Figs. S6(a) and S6(b) in the supplementary material, the total energy fluctuation of ML ${\text{CrGaS}}_{3}$ under $-6\%$ to $6\%$ strain remains almost constant throughout the simulation time, and the structure remains stable within 3 ps. These results suggest that ML ${\text{CrGaS}}_{3}$ is thermodynamically stable within the $-6\%$ to $6\%$ strain range. Moreover, in Fig. 7(c), it is shown that the energy difference between the AFM states and the FM state increases with increasing tensile strain (and decreases with increasing compressive strain), and the magnetic coupling strength of $J_{1}$ and $J_{2}$ is also the same. It is found that a $6\%$ tensile strain boosts the $T_{c}$ by $18\%$ to 667 K (see Fig. S5 in the supplementary material), which indicates a change in the magnetic coupling strength between the two near-neighboring atoms. As for $\lambda_{1}$, it is proportional to the tensile strain in the range of $0\%$-$6\%$ and is inversely proportional to the compressive strain in the range of $-6\%$ to $0\%$, which is opposite to that of $\lambda_{2}$ [see Fig. 7(d)].

More importantly, in Fig. 7(d), it can be seen that $D$ increases significantly with the strain, which shifts the easy magnetization axis from out-of-plane to in-plane during the application of compressive stress from 0 to $-2\%$. The biaxial stress causes a certain change in the bond spacing and bonding angles between atoms. Both the super-exchange and the direct-exchange interactions between magnetic atoms are strongly correlated to the bond lengths and angles. Thus, both tensile and compressive strains can affect the strength and characteristic of the coupling between the magnetic atoms, which leads to a change in the magnetic properties of the system.

## IV. CONCLUSION

In summary, through in-depth exploration using first-principles calculations, we have predicted that ML ${\text{CrGaS}}_{3}$ is a FM semiconductor with a maximum $T_{c}$ of 814 K, well above room temperature. Phonon vibrations, AIMD, and force constant calculations have affirmed its structural, thermodynamic, and mechanical stability. Its high $T_{c}$ stems from the fact that both Cr-Cr direct-exchange and Cr-S-Cr super-exchange interactions are FM. In addition, an efficient super-exchange interaction can occur through the adjacent Cr $e_{g}$-$e_{g}$ orbitals with zero virtual exchange gap. Applying biaxial strain can effectively modulate the magnetic properties of ${\text{CrGaS}}_{3}$. A tensile strain of $6\%$ increases the $T_{c}$ of ${\text{CrGaS}}_{3}$ by $18\%$ to 667 K under the DFT-D3 vdW correction method with $U_{\text{eff}} = 3$ eV.

## SUPPLEMENTARY MATERIAL

The supplementary material is available free of charge on the website, which includes additional details on the computational results, including magnetic configurations, thermodynamic structure stability, and the specifics of magnetic properties.

## ACKNOWLEDGMENTS

This work was supported by the Science and Technology Planning Project of Inner Mongolia (No. 2022YFXM0010).

## AUTHOR DECLARATIONS

### Conflicts of Interest

The authors have no conflicts to disclose.

### Author Contributions

Minghao Jia: Data curation (equal); Formal analysis (equal); Investigation (equal); Writing - original draft (equal). Zhirui Gao: Data curation (equal); Investigation (equal). Yunfei Zhang: Data curation (supporting); Formal analysis (supporting). Shuo Zhang: Data curation (equal); Formal analysis (equal); Investigation (equal); Writing - original draft (equal). Junguang Tao: Conceptualization (equal); Funding acquisition (lead); Writing - review & editing (equal). Lixiu Guan: Conceptualization (equal); Methodology (equal); Supervision (lead); Writing - review & editing (equal).

## DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## REFERENCES

$^{1}$K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, “Electric field effect in atomically thin carbon films,” *Science* **306**, 666 (2004).

$^{2}$X. Wu, R. Ge, P.-A. Chen, H. Chou, Z. Zhang, Y. Zhang, S. Banerjee, M.-H. Chiang, J. C. Lee, and D. Akinwande, “Thinnest nonvolatile memory based on monolayer h-BN,” *Adv. Mater.* **31**, 1806790 (2019).

$^{3}$N. Ito, T. Kikkawa, J. Barker, D. Hirobe, Y. Shiomi, and E. Saitoh, “Spin Seebeck effect in the layered ferromagnetic insulators ${\\text{CrSiTe}}_{3}$ and ${\\text{CrGeTe}}_{3}$,” *Phys. Rev. B* **100**, 060402 (2019).

$^{4}$Y. Sun and X. Luo, “Magnetic entropy scaling in ferromagnetic semiconductor ${\\text{CrGeTe}}_{3}$,” *Phys. Status Solidi B* **256**, 1900052 (2019).

$^{5}$J. Mao, Y. Wang, Z. Zheng, and D. Deng, “The rise of two-dimensional ${\\text{MoS}}_{2}$ for catalysis,” *Front. Phys.* **13**, 138118 (2018).

$^{6}$J. Li, B. Zhao, P. Chen, R. Wu, B. Li, Q. Xia, G. Guo, J. Luo, K. Zang, Z. Zhang, H. Ma, G. Sun, X. Duan, and X. Duan, “Synthesis of ultrathin metallic ${\\text{MTe}}_{2}$ (M = V, Nb, Ta) single-crystalline nanoplates,” *Adv. Mater.* **30**, 1801043 (2018).

$^{7}$H. Zhang, A. Rousuli, K. Zhang, L. Luo, C. Guo, X. Cong, Z. Lin, C. Bao, H. Zhang, S. Xu, R. Feng, S. Shen, K. Zhao, W. Yao, Y. Wu, S. Ji, X. Chen, P. Tan, Q.-K. Xue, Y. Xu, W. Duan, P. Yu, and S. Zhou, “Tailored Ising superconductivity in intercalated bulk ${\\text{NbSe}}_{2}$,” *Nat. Phys.* **18**, 1425 (2022).

$^{8}$C. Gong and X. Zhang, “Two-dimensional magnetic crystals and emergent heterostructure devices,” *Science* **363**, eaav4450 (2019).

$^{9}$G. Song, D. Li, H. Zhou, C. Zhang, Z. Li, G. Li, B. Zhang, X. Huang, and B. Gao, “Intrinsic room-temperature ferromagnetic semiconductor ${\\text{InCrTe}}_{3}$ monolayers with large magnetic anisotropy and large piezoelectricity,” *Appl. Phys. Lett.* **118**, 123102 (2021).

$^{10}$C. Gong, L. Li, Z. Li, H. Ji, A. Stern, Y. Xia, T. Cao, W. Bao, C. Wang, Y. Wang, Z. Q. Qiu, R. J. Cava, S. G. Louie, J. Xia, and X. Zhang, “Discovery of intrinsic ferromagnetism in two-dimensional van der Waals crystals,” *Nature* **546**, 265 (2017).

$^{11}$B. Huang, G. Clark, E. Navarro-Moratalla, D. R. Klein, R. Cheng, K. L. Seyler, D. Zhong, E. Schmidgall, M. A. McGuire, D. H. Cobden, W. Yao, D. Xiao,

P. Jarillo-Herrero, and X. Xu, "Layer-dependent ferromagnetism in a van der Waals crystal down to the monolayer limit," *Nature* **546**, 270 (2017).
¹²A.-N. Ma, P.-J. Wang, and C.-W. Zhang, "Intrinsic ferromagnetism with high temperature, strong anisotropy and controllable magnetization in the CrX (X = P, As) monolayer," *Nanoscale* **12**, 5464 (2020).
¹³Y. Guo, Y. Zhang, S. Yuan, B. Wang, and J. Wang, "Chromium sulfide halide monolayers: Intrinsic ferromagnetic semiconductors with large spin polarization and high carrier mobility," *Nanoscale* **10**, 18036 (2018).
¹⁴Q. Feng, X. Li, X. Li, and J. Yang, "Crsbs₃ monolayer: A potential phase transition ferromagnetic semiconductor," *Nanoscale* **13**, 14067 (2021).
¹⁵P. Kumari, T. Mukherjee, S. Kar, and S. J. Ray, "VClBr₂: A new two-dimensional (2D) ferromagnetic semiconductor," *J. Appl. Phys.* **133**, 183901 (2023).
¹⁶T. Mukherjee, P. Kumari, S. Kar, C. Datta, and S. J. Ray, "Robust half-metallicity and tunable ferromagnetism in two-dimensional VCl₂," *J. Appl. Phys.* **133**, 084303 (2023).
¹⁷N. D. Mermin and H. Wagner, "Absence of ferromagnetism or antiferromagnetism in one-or two-dimensional isotropic Heisenberg models," *Phys. Rev. Lett.* **17**, 1133 (1966).
¹⁸H. Wang, J. Qi, and X. Qian, "Electrically tunable high Curie temperature two-dimensional ferromagnetism in van der Waals layered crystals," *Appl. Phys. Lett.* **117**, 083102 (2020).
¹⁹Z. Jiang, P. Wang, J. Xing, X. Jiang, and J. Zhao, "Screening and design of novel 2D ferromagnetic materials with high Curie temperature above room temperature," *ACS Appl. Mater. Interface.* **10**, 39032 (2018).
²⁰P. Kumari, S. Rani, S. Kar, M. V. Kamalakar, and S. J. Ray, "Strain-controlled spin transport in a two-dimensional (2D) nanomagnet," *Sci. Rep.* **13**, 16599 (2023).
²¹Y. J. Deng, Y. J. Yu, Y. C. Song, J. Z. Zhang, N. Z. Wang, Z. Y. Sun, Y. F. Yi, Y. Z. Wu, S. W. Wu, J. Y. Zhu, J. Wang, X. H. Chen, and Y. B. Zhang, "Gate-tunable room-temperature ferromagnetism in two-dimensional Fe₃GeTe₂," *Nature* **563**, 94 (2018).
²²Y. L. Guo, S. J. Yuan, B. Wang, L. Shi, and J. L. Wang, "Half-metallicity and enhanced ferromagnetism in Li-adsorbed ultrathin chromium triiodide," *J. Mater. Chem. C* **6**, 5716 (2018).
²³P. H. Jian, L. Li, Z. L. Liao, Y. X. Zhao, and Z. C. Zhong, "Spin direction-controlled electronic band structure in two-dimensional ferromagnetic CrI₃," *Nano Lett.* **18**, 3844 (2018).
²⁴D. Weber, A. H. Trout, D. W. McComb, and J. E. Goldberger, "Decomposition-induced room-temperature magnetism of the Na-intercalated layered ferromagnet Fe₃₋ₓGeTe₂," *Nano Lett.* **19**, 5031 (2019).
²⁵Z. Pang, X. Zhou, Z. Liu, and D. Zhao, "Partially coherent quasi-airy beams with controllable acceleration," *Phys. Rev. A* **102**, 063519 (2020).
²⁶S. Zhang, R. Xu, W. Duan, and X. Zou, "Intrinsic half-metallicity in 2D ternary chalcogenides with high critical temperature and controllable magnetization direction," *Adv. Funct. Mater.* **29**, 1808380 (2019).
²⁷Z. Guan and S. Ni, "Predicted 2D ferromagnetic Janus VSeTe monolayer with high Curie temperature, large valley polarization and magnetic crystal anisotropy," *Nanoscale* **12**, 22735 (2020).
²⁸G. Zhang, H. Wu, L. Zhang, S. Zhang, L. Yang, P. Gao, X. Wen, W. Jin, F. Guo, Y. Xie, H. Li, B. Tao, W. Zhang, and H. Chang, "Highly-tunable intrinsic room-temperature ferromagnetism in 2D van der Waals semiconductor CrₓGa₁₋ₓTe," *Adv. Sci.* **9**, 2103173 (2022).
²⁹Y. Ma, D. Leng, X. Zhang, J. Fu, C. Pi, Y. Zheng, B. Gao, X. Li, N. Li, and P. K. Chu, "Enhanced activities in alkaline hydrogen and oxygen evolution reactions on MoS₂ electrocatalysts by in-plane sulfur defects coupled with transition metal doping," *Small* **18**, 2203173 (2022).
³⁰F. Wang, J. Du, F. Sun, R. F. Sabirianov, N. Al-Aqtash, D. Sengupta, H. Zeng, and X. Xu, "Ferromagnetic Cr₂Te₃ nanorods with ultrahigh coercivity," *Nanoscale* **10**, 11028 (2018).
³¹W. L. B. Huey, A. M. Ochs, A. J. Williams, Y. Zhang, S. Kraguljac, Z. Deng, C. E. Moore, W. Windl, C. N. Lau, and J. E. Goldberger, "CrₓPt₁₋ₓTe₂(x ≤ 0.45): A family of air-stable and exfoliatable van der Waals ferromagnets," *ACS Nano* **16**, 3852 (2022).
³²G. Kresse and J. Furthmüller, "Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set," *Phys. Rev. B* **54**, 11169 (1996).
³³F. Shimojo, K. Hoshino, and Y. Zempo, "*Ab initio* molecular-dynamics simulation method for complex liquids," *Comput. Phys. Commun.* **142**, 364 (2001).
³⁴J. P. Perdew, K. Burke, and M. Ernzerhof, "Generalized gradient approximation made simple," *Phys. Rev. Lett.* **77**, 3865 (1996).
³⁵P. E. Blöchl, "Projector augmented-wave method," *Phys. Rev. B* **50**, 17953 (1994).
³⁶G. Kresse, and D. Joubert, "From ultrasoft pseudopotentials to the projector augmented-wave method," *Phys. Rev. B* **59**, 1758 (1999).
³⁷J. P. Allen, D. O. Scanlon, S. C. Parker, and G. W. Watson, "Tin monoxide: Structural prediction from first principles calculations with van der waals corrections," *J. Phys. Chem. C* **115**, 19916 (2011).
³⁸S. Grimme, "Accurate description of van der waals complexes by density functional theory including empirical corrections," *J. Comput. Chem.* **25**, 1463 (2004).
³⁹S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, "A consistent and accurate *ab initio* parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu," *J. Chem. Phys.* **132**, 154104 (2010).
⁴⁰Z.-X. Hu, X. Kong, J. Qiao, B. Normand, and W. Ji, "Interlayer electronic hybridization leads to exceptional thickness-dependent vibrational properties in few-layer black phosphorus," *Nanoscale* **8**, 2740 (2016).
⁴¹Y. Zhao, J. Qiao, P. Yu, Z. Hu, Z. Lin, S. P. Lau, Z. Liu, W. Ji, and Y. Chai, "Extraordinarily strong interlayer interaction in 2D layered PtS₂," *Adv. Mater.* **28**, 2399 (2016).
⁴²F. Li, W. Wei, P. Zhao, B. Huang, and Y. Dai, "Electronic and optical properties of pristine and vertical and lateral heterostructures of Janus MoSSe and WSSe," *J. Phys. Chem. Lett.* **8**, 5959 (2017).
⁴³S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, "Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA + U study," *Phys. Rev. B* **57**, 1505 (1998).
⁴⁴P. Jiang, C. Wang, D. Chen, Z. Zhong, Z. Yuan, Z.-Y. Lu, and W. Ji, "Stacking tunable interlayer magnetism in bilayer CrI₃," *Phys. Rev. B* **99**, 144401 (2019).
⁴⁵C. Wang, X. Zhou, Y. Pan, J. Qiao, X. Kong, C.-C. Kaun, and W. Ji, "Layer and doping tunable ferromagnetic order in two-dimensional CrS₂ layers," *Phys. Rev. B* **97**, 245409 (2018).
⁴⁶C. Wang, X. Zhou, L. Zhou, N.-H. Tong, Z.-Y. Lu, and W. Ji, "A family of high-temperature ferromagnetic monolayers with locked spin-dichroism-mobility anisotropy: MnNX and CrCX (X = Cl, Br, I; C = S, Se, Te)," *Sci. Bull.* **64**, 293 (2019).
⁴⁷A. Togo and I. Tanaka, "First principles phonon calculations in materials science," *Scr. Mater.* **108**, 1 (2015).
⁴⁸S. Nosé, "Constant temperature molecular dynamics methods," *Prog. Theor. Phys. Suppl.* **103**, 1 (1991).
⁴⁹G. Küpers, P. M. Konze, A. Meledin, J. Mayer, U. Englert, M. Wuttig, and R. Dronskowski, "Controlled crystal growth of indium selenide, In₂Se₃, and the crystal structures of α-In₂Se₃," *Inorg. Chem.* **57**, 11775 (2018).
⁵⁰K. Lee, A. H. Dismukes, E. J. Telford, R. A. Wiscons, J. Wang, X. Xu, C. Nuckolls, C. R. Dean, X. Roy, and X. Zhu, "Magnetic order and symmetry in the 2D semiconductor CrSBr," *Nano Lett.* **21**, 3511 (2021).
⁵¹Z. W. Tan, J.-S. Wang, and C. K. Gan, "First-principles study of heat transport properties of graphene nanoribbons," *Nano Lett.* **11**, 214 (2011).
⁵²F. Mouhat and F.-X. Coudert, "Necessary and sufficient elastic stability conditions in various crystal systems," *Phys. Rev. B* **90**, 224104 (2014).
⁵³D. Wickramaratne, F. Zahid, and R. K. Lake, "Electronic and thermoelectric properties of van der Waals materials with ring-shaped valence bands," *J. Appl. Phys.* **118**, 075101 (2015).
⁵⁴C. Huang, J. Feng, F. Wu, D. Ahmed, B. Huang, H. Xiang, K. Deng, and E. Kan, "Toward intrinsic room-temperature ferromagnetism in two-dimensional semiconductors," *J. Am. Chem. Soc.* **140**, 11519 (2018).

---

J. Appl. Phys. **135**, 073903 (2024); doi: 10.1063/5.0191120
© Author(s) 2024
135, 073903-12

$^{55}$A.-Y. Lu, H. Zhu, J. Xiao, C.-P. Chuu, Y. Han, M.-H. Chiu, C.-C. Cheng, C.-W. Yang, K.-H. Wei, Y. Yang, Y. Wang, D. Sokaras, D. Nordlund, P. Yang, D. A. Muller, M.-Y. Chou, X. Zhang, and L.-J. Li, "Janus monolayers of transi- tion metal dichalcogenides," *Nat. Nanotech.* **12**, 744 (2017).

$^{56}$S. V. Streltsov and D. I. Khomskii, "Orbital physics in transition metal com- pounds: New trends," *Phys.-Usp* **60**, 1121 (2017).

$^{57}$J. Xiao, D. Legut, W. Luo, H. Guo, X. Liu, R. Zhang, and Q. Zhang, "Modulating superexchange strength to achieve robust ferromagnetic couplings in two-dimensional semiconductors," *Phys. Rev. B* **101**, 014431 (2020).

$^{58}$S. Yang, Y. Chen, and C. Jiang, "Strain engineering of two-dimensional materi- als: Methods, properties, and applications," *InfoMat* **3**, 397 (2021).

J. Appl. Phys. **135**, 073903 (2024); doi: 10.1063/5.0191120
© Author(s) 2024

135, 073903-13