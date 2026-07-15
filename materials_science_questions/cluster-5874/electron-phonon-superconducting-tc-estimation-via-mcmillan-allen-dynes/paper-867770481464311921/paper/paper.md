# Prediction of Superconductivity in Potassium-Doped Benzene

Guohua Zhong, $^{1,2}$ Xiao-Jia Chen, $^{3, *}$ and Hai-Qing Lin $^{2,1, \dagger}$

$^{1}$ Center for Photovoltaics and Solar Energy, Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences and The Chinese University of Hong Kong, Shenzhen 518055, China
$^{2}$ Beijing Computational Science Research Center, Beijing 100089, China
$^{3}$ Center for High Pressure Science and Technology Advanced Research, Shanghai 201203, China

(Dated: October 22, 2021)

To explore underlying mechanism for the superconducting phase in recent discovered aromatic hydrocarbons, we carry out the first-principles calculations on benzene, the basic and the simplest unit of the series and examine the structural and phase stability when doped by potassium, $K_x$C$_6$H$_6$ ($x=1,2,3$). We find that K$_2$C$_6$H$_6$ with the space group of $Pbca$ is the most stable phase with superconducting transition temperature around 6.2 K. Moreover, we argue that all existing hydrocarbons should have a unified superconducting phase in the same temperature range of 5–7 K, when doped by two potassium atoms. Our results indicate that the electron-phonon interaction is enough to account for the superconductivity of this unified superconducting phase.

PACS numbers: 74.10.+v, 74.25.Jb, 74.62.Fj, 74.70.Ad

Organic superconductors are unique materials with a crystal structure made primarily of a complex carbon based network. Carbon, an element associated directly with life, which was postulated to have a high transition temperature even above room temperature, from a theoretical viewpoint [1]. Organic superconductors are generally charge-transfer compounds that are made up of electron donor molecules such as tetrathiafulvalene (TTF), bis-ethylenedithrio-TTF, (BEDT-TTF, abbreviated as ET), and tetramethyltetraselenafulvalene (TMTSF) derivatives, as well as electron acceptor molecules such as tetracyanoquinodimethane (TCNQ) or fullerides [2–6]. The recent discovery of superconductivity in polycyclic aromatic hydrocarbons (PAHs) [7–10] has led to a great interest in these organic based compounds. Increasing the number of benzene rings, thus delocalizing the charge over a larger space, superconducting transition temperature, $T_c$, could be higher than 30 K and thus revitalizing the hope of realizing high-$T_c$ superconductivity in light element materials. However, there are issues to be addresses such as what the superconducting phase of these hydrocarbons is? how many carries are needed to induce superconductivity? and where the doped carriers are distributed in the unit cells, etc. Having such information is important not only for understanding the physical properties and mechanism of superconductivity in these materials but also for designing materials with higher $T_c$ in technology applications.

The simplest aromatic hydrocarbon is nothing but the benzene, which has six carbons on a ring and six hydrogens attached, C$_6$H$_6$. Other PAHs are made of more rings of carbons and hydrogens. Being the basic cell of PAH, solid benzene stands out as an ideal system to address all concerned issues mentioned above. A fundamental question is whether such a system could superconduct when doped by alkali atoms. If it superconducts, will its properties be of common features for all aromatic hydrocarbons? Thus, explore structures of doped solid benzene and examine corresponding phase stability, followed by the study of superconductivity, is the task of this work.

Solid benzene has rich phase diagram with several phases as functions of temperature and pressure, whose crystallization characteristics has been extensively investigated [11–17]. Liquid benzene crystallizes at room temperature and about 0.07 GPa, in an orthorhombic phase with space group $Pbca$ (phase I), containing four formula units (f.u.) per unit cell [11]. At 1.4 GPa, a transition occurs from phase I to phase II ($P4_32_12$), and then at 4 GPa, phase II transfers to phase III ($P2_1/c$), followed by phase IV (11 GPa) and phase V at high pressures. Solid benzene is non-metallic and non-superconductive in a very large range of pressure. Upon heavy compression, solid benzene was predicted to become a metal from insulator in the pressure range of $180-200$ GPa [18], which means that benzene is a possible superconductor under high pressure. However, extreme pressure condition brings the difficulty to experimental fabrication and observation. Hence, we choose potassium (K) to dope solid benzene at ambient pressure to explore the realization of metallization and superconductivity. If doped solid benzene superconducts at ambient pressure, it would be possible to have higher $T_c$ at high pressure.

Although experimental studies on doping K into solid benzene have not been performed yet, the interaction between benzene molecule and K$^+$ ion has been observed experimentally and studied theoretically by E. López *et al.* [19]. Their work implies the feasibility of doping potassium into solid benzene. Notably, doping potassium has been shown to be the most effective and common method to induce superconductivity in PAHs [7–10]: all aromatic hydrocarbons were found to become superconductor with K dopant. One reason is that K has a relatively low melting point as compared to other alkali elements, which enables the chemical reaction and crys-

![](./images/867770481464311921_1.jpg)

FIG. 1: (Color online) Optimized crystal structures of (a) solid benzene and (b) K-doped solid benzene, K₂C₆H₆, viewing from different directions. Purple balls represent K atoms.

tallization from liquid states of K and benzene easy to occur.

For doped solid benzene, we firstly perform structure optimization to obtain its atomic positions and lattice constants. Then we calculate corresponding electronic structures and electron-phonon interactions. All structural optimizations and electronic properties were calculated by using the Vienna ab initio simulation package (VASP) [20]. In this work, the projector augmented wave (PAW) method [21] was adopted, and the exchange correlation energy was described by the Ceperley-Alder local density approximation (LDA) [22] as parameterized by Perdew and Zunger [23], which has been confirmed to be adequate by previous studies [24–28]. An energy cutoff of 500 eV was used for the plane wave basis sets. The Brillouin zone (BZ) was sampled by 4×4×4 Monkhorst-Pack $k$-point grids during the optimization, and double $k$-point in the electronic structural calculations. The convergence thresholds were set as $10^{-6}$ eV in energy and 0.005 eV/Å in force. A conjugate-gradient algorithm was used to relax the ions into their instantaneous ground state.

To calculate electron-phonon interaction and relevant parameters, we use the QUANTUM-ESPRESSO package (QE) [29] with a cutoff energy of 60 and 450 Ry for wave functions and charge densities, respectively. Forces and stresses for the converged structures were optimized and checked to be within the error allowance of the VASP and QE codes. Troullier-Martins norm-conserving scheme [30] was used to generate the pseudopotentials for C, H, and K atoms. 8×8×8 Monkhorst-Pack $k$-point grid with Gaussian smearing of 0.03 Ry was used for the electron-phonon interaction matrix element calculations at 2×2×2 $q$-point mesh.

As a comparison and a check on accuracy, we start our investigation by looking at the solid benzene. Figure 1(a) shows the optimized crystal structure of solid benzene viewing from different directions, with crystal lattice constants being $a = 7.041$ Å, $b = 8.903$ Å, and $c = 6.357$ Å at zero temperature and the ambient pressure, which are 3-6% less than experimental values at 78 K [11]. Considering temperature effect, this error between theoretical prediction and experimental measurement is acceptable. From reported data on PAHs, the superconductivity is highly sensitive to both the doping concentration and the cation positions in the unit cell. To examine both effects, we perform optimization studies on doped solid benzene, $K_x$C₆H₆, by varying potassium contents ($x=1,2,3$) and position of K atoms in the unit cell. To check their stability, formation energy, as defined by $E_{formation}=E_{K_xC_6H_6}-E_{C_6H_6}-E_{K_x}$, is a good indication. We obtained the results of formation energy as 0.35, $-2.99$, and 1.52 eV for $x=1,2$, and 3, respectively. Thus, both K₁C₆H₆ and K₃C₆H₆ are unstable and the K₂C₆H₆ is the only stable phase in this series. Its big negative formation suggests easier synthesization.

Figure 1(b) shows the optimized K₂C₆H₆ crystal structure viewing from different directions, with lattice constants being $a = 8.605$ Å, $b = 10.705$ Å, and $c = 6.415$ Å, respectively. Comparing with the undoped case, the lattice constants expand largely in the $a$ and $b$ directions. The inserting of eight K atoms makes the volume increased by 26.9%. Under K doping, a visible layer shape structure is formed, differing from that of the solid benzene. As shown in Fig. 1(b), all benzene rings are rotated and parallel to the $bc$-plane under the interaction of dopants, and K atoms are intercalated into two layers of benzene rings, occupying on Wyckoff 8c sites. We found that the optimized structure of K₂C₆H₆ has tended to the higher symmetry of $Fmmm$ from the lower $Pbca$ symmetry. Significantly, the layered structure of K₂C₆H₆ is similar to those of YbC₆ and CaC₆ [31]. This similarity indicates the possibility of superconducting, because it is known that both YbC₆ and CaC₆ are superconductors, with the $T_c$ reaching to 6.5 K and 11.5 K, respectively [31, 32].

Once the crystal structure is determined, it is ready to obtain the electronic band structure. For K₂C₆H₆, we show 8 conduction bands (called as CB1, CB2, ..., and CB8) along a high symmetry $k$-direction, $\Gamma-Z-T-Y-S-X-U-R$, of the Brillium zone in Fig. 2(a). Specifically, under either $Pbca$ or $Fmmm$ symmetry, the LUMO and LUMO+1 orbitals split into 8 bands from $\Gamma$ to $Z$, then they merge into 4 degenerate bands along the $Z-T-Y-S-X-U$ directions, and further into two highly degenerated bands along the $U-R$ direction. Electrons transferred from the K atoms to the C₆H₆ molecule, occupying low energy orbitals and raise the Fermi level. Three bands, CB1, CB2, and CB3 are fully occupied by six of eight electrons, while the other three, CB4, CB5, and CB6 are partially filled by the remaining two electrons with Fermi level passing through. Both CB7 and

![](./images/867770481464311921_2.jpg)

FIG. 2: Electronic band structure of $K_2C_6H_6$: (a) energy band; (b) Fermi surface; and (c) projected density of states (PDOS), where zero energy denotes the Fermi level.

CB8 are empty. Thus, $K_2C_6H_6$ is metallic and it is in the low-spin state. Comparing with the solid benzene, the intermolecular distance along benzene rings becomes smaller on the $bc$-plane of $K_2C_6H_6$, which enhances the intermolecular interaction and broadens the dispersion of energy bands. Analyzing the electronic characters near the Fermi level, as shown by Fig. 2(b), the hole-like Fermi surfaces are formed by CB4 along the $\Gamma-Z$ $k$-direction, while both CB5 and CB6 contribute the electron-like Fermi surfaces around the $Y$ $k$-point. Fermi surface nesting is quite clear. Calculation of the projected density of states (PDOS) show that C-$p_y$ and C-$p_z$ states are fully occupied and far below the Fermi level, while C-$p_x$ state has a big PDOS around the Fermi level, as shown in Fig. 2(c). Most PDOS of K-$(s,p_x,p_y,p_z)$ states are above the Fermi level, which indicates that the electrons transfer from K to C-$p_x$ orbital. The large ratio of C-$p_x$ PDOS over K PDOS shows that C-$p_x$ electronic states contribute more to the Fermi surfaces.

Now we examine whether this simplest aromatic hydrocarbon could exhibit superconductivity like other PAHs wiith long benzene rings [7-10]. Assuming the pairing mechanism is still the electron-phonon interaction mediated, we evaluate the Eliashberg spectral function $\alpha^2F(\omega)$ and the electron-phonon coupling integral $\lambda(\omega)$ of $K_2C_6H_6$ as a function of frequency. The results are shown in Fig. 3. The vibration in the low frequency range of $0-250$ $\text{cm}^{-1}$ comes from K atoms and intermolecular modes, while the vibration with moderate frequencies of $300-1450$ $\text{cm}^{-1}$ mainly comes from C atoms. The total $\lambda$ is 0.67, which is comparable to that of $K_3C_{22}H_{14}$ [25]. We also noted that vibrational modes from C atoms contribute 56% to the total $\lambda$ value, and the rest 44% is provided by the dopant and intermolecular phonon modes. Following the modified McMillan equation of Allen and Dynes [34], with the obtained values of $\lambda(\omega)$ and $\omega_{log}$ for $K_2C_6H_6$, and a typical value of 0.10 for the Coulomb pseudopotential $\mu^\star$, we obtain $T_c=6.2$ K. The choice of $\mu^\star$ is appropriate for light-element systems [25, 35, 36].

![](./images/867770481464311921_3.jpg)

FIG. 3: Electron-phonon coupling of $K_2C_6H_6$: Eliashberg spectral function $\alpha^2F(\omega)$ and the electron-phonon coupling integral $\lambda(\omega)$.

We want to point out that the dominant contribution to the total $\lambda$ from the vibrational modes of the C atoms in $K_2C_6H_6$ shows some similarity with other $C_6$-based or low carbon-bearing compounds. In reality, $CaC_6$ was discovered to exhibit superconductivity at 11.5 K [31]. Superconductivity has also been discovered in intercalation compounds of graphite with alkali metals $AC_8$ ($A$ =K, Rb, or Cs) [37]. The predicted $T_c$ of 6.2 K in $K_2C_6H_6$ is comparable to the temperature range of these low carbon-based superconductors [31, 37].

A comparison of the predicted superconductivity in benzene with other aromatic hydrocarbons reveals a common feature of PAH (Fig. 4). Besides the reported high-$T_c$ phases with $T_c=18$ K for K-doped picene ($K_xC_{22}H_{14}$) [7], 15 K for K-doped coronene ($K_xC_{24}H_{12}$) [8], and 33 K for K-doped 1,2:8,9-dibenzpentacene ($K_xC_{30}H_{18}$) [10], multi-superconducting phases in long-benzene-ring hydrocarbons were generally observed. There exists a low $T_c$ phase with almost the same $T_c$ between $5-7$ K in these hydrocarbon superconductors discovered so far [7-10]: $K_xC_{14}H_{10}$ has $T_c$ 5 K [9]; $K_xC_{22}H_{14}$ has $T_c$ 7 K [7, 8]; $K_xC_{30}H_{18}$ has $T_c$ of 7.4 K [10], though several other transitions with higher $T_c$'s were observed. Moreover, $Rb_3C_{22}H_{14}$ and $Ca_{1.5}C_{22}H_{14}$ both show transition temperature around 7 K [7]. $T_c$ of $5-7$ K was reported for $K_xC_{24}H_{12}$ [8], in addition to other three more transitions. Superconductivity at 6.4 K was observed in $Sm_{1.25}$chrysene [38]. It is important to note that only in the range of $5-7$ K transition temperatures were observed in all reported superconducting aromatic hydrocarbons with various number of benzene rings, in a good agreement with our current prediction for benzene, the simplest compound of this series. In fact, the value of

![](./images/867770481464311921_4.jpg)

FIG. 4: Variation of superconducting transition temperature $T_c$ with the number of benzene rings for various aromatic hydrocarbons. The solid red square is the prediction of this work for benzene. Other symbols are taken from experiments [7–10, 38]. The dashed line is the guide for eyes.

the logarithmic average of phonon frequencies $\omega_{log}$ (199.8 K) for $\text{K}_2\text{C}_6\text{H}_6$ is exactly the same as that of $\text{K}_3\text{C}_{22}\text{H}_{14}$ [25], seemingly independent of the number of the benzene rings. A careful analysis on the 2-ring case also showed that a possible superconducting phase with $T_c$ in the same range for $\text{K}_2\text{C}_{10}\text{H}_8$. With these analysis, we are confident to conclude that the presence of the superconducting phase with $T_c$ around $5-7$ K is a common feature of aromatic hydrocarbons. In most cases, the low-$T_c$ phase was easily fabricated and more stable than the higher $T_c$ phase [7, 8, 10]. Considering the fact that the cation concentration has never been experimentally identified by using the reliable neutron scattering or single crystal X-ray diffraction techniques, all the reported doping levels are an ideal chemical estimation based on the synthesis procedure. Our phase stability examination for potassium-doped benzene pins down the doping concentration of the exact two electrons for the stabile superconducting phase of these hydrocarbons with $T_c$ of $5-7$ K.

Although a complete understanding of the mechanism of superconductivity in aromatic hydrocarbons has yet to achieve, the common feature of the $5-7$ K superconducting phase for all reported aromatic hydrocarbons may provide us some clues. Moreover, further investigations indicate that the electron-electron correlations seem to play an important role on superconductivity in these systems. This is quite similar to charge-transfer organic superconductors and fullerides [5, 40–45] where the importance of electron correlations on superconductivity was emphasized. Magnetic measurements [9] on phenanthrene suggest the existence of local spin moments, and indicate similar interplay between magnetism and superconductivity observed in fullerides [5, 40–45]. We indeed found that the electron-electron correlation becomes important as the number of benzene rings increases. Multi-ring hydrocarbons are in favor of strong correlations and thus tend to have higher $T_c$'s. It is therefore believed that both the electron-phonon interaction and electron-electron correlations work together to enhance $T_c$ of the aromatic hydrocarbons with increasing the number of benzene rings.

In summary, carrying out the first-principles calculations, we have investigated the crystal structures and possible superconductivity in potassium doped solid benzene, $\text{K}_x\text{C}_6\text{H}_6$ ($x=1,2,3$). The K dopant results in the visible change of crystal configuration and drives the system from insulator to metal. $\text{K}_2\text{C}_6\text{H}_6$ is found to be stable due to its lowest formation energy as compared to other doping. Superconductivity in doped solid benzene with a $T_c$ of 6.2 K is predicted. This superconducting phase shares the common feature of all existing aromatic hydrocarbon superconductors.

The work was supported by the Natural Science Foundation of China (Grant Nos. 11274335, 91230203, and U1230202), and the Shenzhen Basic Research Grant (Nos. KQC201109050091A and JCYJ20120617151835515).

* Electronic address: xjchen@hpstar.ac.cn
† Electronic address: haiqing0@csrc.ac.cn

[1] V. L. Ginzburg, Sov. Phys. Usp. 19, 174 (1976).
[2] D. Jerome, A. Mazaud, M. Ribault, and K. Bechgaard, J. Phys. Lett. 41 L95 (1980).
[3] A. F. Hebard, M. J. Rosseinsky, R. C. Haddon, D. W. Murphy, S. H. Glarum, T. T. M. Palstra, A. P. Ramirez, and A. R. Kortan, Nature (London) 350, 600 (1991).
[4] K. Tanigaki, T. W. Ebbesen, S. Saito, J. Mizuki, J. S. Tsai, Y. Kubo, and S. Kuroshima, Nature (London) 352, 222 (1991).
[5] A. Y. Ganin, Y. Takabayashi, Y. Z. Khimyak, S. Mar- gadonna, A. Tamai, M. J. Rosseinsky, and K. Prassides, Nature Mater. 7, 367 (2008).
[6] H. Taniguchi, M. Miyashita, K. Uchiyama, K. Satoh, N. Mori, H. Okamoto, K. Miyagawa, K. Kanoda, M. Hedo, and Y. Uwatoko, J. Phys. Soc. Jpn. 72, 468 (2003).
[7] R. Mitsuhashi, Y. Suzuki, Y. Yamanari, H. Mitamura, T. Kambe, N. Ikeda, H. Okamoto, A. Fujiwara, M. Yamaji, N. Kawasaki, Y. Maniwa, and Y. Kubozono, Nature (London) 464, 76 (2010).
[8] Y. Kubozono, M. Mitamura, X. Lee, X. He, Y. Yamanari, Y. Takahashi, Y. Suzuki, Y. Kaji, R. Eguchi, K. Akaike, T. Kambe, H. Okamoto, A. Fujiwara, T. Kato, T. Kosugi, and H. Aoki, Phys. Chem. Chem. Phys. 13, 16476 (2011).
[9] X. F. Wang, R. H. Liu, Z. Gui, Y. L. Xie, Y. J. Yan, J. J. Ying, X. G. Luo, and X. H. Chen, Nat. Commun. 2, 507 (2011).
[10] M. Q. Xue, T. B. Cao, D. M. Wang, Y. Wu, H. X. Yang, X. L. Dong, J. B. He, F. W. Li, and G. F. Chen, Sci. Rep. 2, 389 (2012).
[11] V. M. Kozhin, and A. I. Kitaigorodskii, Zh. Fiz. Khim. 29, 2074 (1955).

[12] E. G. Cox, D. W. J. Cruickshank, and J. A. S. Smith, Proc. R. Soc. Lond. A 247, 1 (1958).

[13] M. M. Thiéry and J. M. Léger, J. Chem. Phys. 89, 4255 (1988).

[14] L. Ciabini, F. A. Gorelli, M. Santoro, R. Bini, V. Schet- tino, and M. Mezouar, Phys. Rev. B 72, 094108 (2005).

[15] L. Ciabini, M. Santoro, F. A. Gorelli, R. Bini, V. Schet- tino, and S. Raugei, Nature Mater. 6, 39 (2007).

[16] A. Katrusiak, M. Podsiadlo, and A. Budzianowski, Cryst. Growth Des. 10, 3461 (2010).

[17] T. C. Fitzgibbons, M. Guthrie, E. S. Xu, V. H. Crespi, S. K. Davidowski, G. D. Cody, N. Alem, and J. V. Badding, Nature Mater. DOI: 10.1038/NMAT4088 (2014).

[18] X. D. Wen, R. Hoffmann, and N. W. Ashcroft, J. Am. Chem. Soc. 133, 9023 (2011).

[19] E. López, J. M. Lucas, J. de Andrés, M. Albertí, J. M. Bofill, D. Bassi, and A. Aguilar, Phys. Chem. Chem. Phys. 13, 15977 (2011).

[20] G. Kresse and J. Furthmuller, Comput. Mater. Sci. 6, 15 (1996).

[21] G. Kresse and D. Joubert, Phys. Rev. B 59, 1758 (1999).

[22] D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).

[23] J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981).

[24] G. H. Zhong, Z. B. Huang, C. Zhang, X. W. Yan, X. J. Chen, and H. Q. Lin, e-print arXiv:1403.1190, (unpub- lished).

[25] M. Casula, M. Calandra, G. Profeta, and F. Mauri, Phys. Rev. Lett. 107, 137006 (2011).

[26] P. L. de Andres, A. Guijarro, and J. A. Vergés, Phys. Rev. B 84, 144501 (2011).

[27] P. L. de Andres, A. Guijarro, and J. A. Vergés, Phys. Rev. B 83, 245113 (2011).

[28] T. Kosugi, T. Miyake, S. Ishibashi, R. Arita, and H. Aoki, J. Phys. Soc. Jpn. 78, 113704 (2009).

[29] P. Giannozzi, et al. J. Phys.: Condens. Matter 21, 395502 (2009).

[30] N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).

[31] T. E. Weller, M. Ellerby, S. S. Saxena, R. P. Smith, and N. T. Skipper, Nat. Phys. 1, 39 (2005).

[32] N. Emery, C. Hérold, M. d'Astuto, V. Garcia, Ch. Bellin, J. F. Marêché, P. Lagrange, and G. Loupias, Phys. Rev. Lett. 95, 087003 (2005).

[33] T. Kato, T. Kambe, and Y. Kubozono, Phys. Rev. Lett. 107, 077001 (2011).

[34] P. B. Allen and R. C. Dynes, Phys. Rev. B 12, 905 (1975).

[35] T. Kato and T. Yamabe, J. Chem. Phys. 115, 8592 (2001).

[36] N. W. Ashcroft, Phys. Rev. Lett. 92, 187002 (2004).

[37] N. N. Hannay, T. H. Geballe, B. T. Matthias, K. Andres, P. Schmidt, and D. MacNair, Phys. Rev. Lett. 14, 225 (1965).

[38] Q. W. Huang et al., unpublished.

[39] Z. B. Huang, C. Zhang, and H. Q. Lin, Sci. Rep. 2, 922 (2012).

[40] P. Duband, G. R. Darling, Y. Dubitsky, A. Zaopo, and M. J. Rosseinsky, Nature Mater. 2, 605 (2003).

[41] S. A. Kivelson and O. L. Chapman, Phys. Rev. B 28, 7236 (1983).

[42] G. Karakonstatakis, E. Berg, S. R. White, and S. A. Kivelson, Phys. Rev. B 83, 054508 (2011).

[43] G. Giovannetti and M. Capone, Phys. Rev. B 83, 134508 ( 2011).

[44] M. Kim and B. I. Min, Phys. Rev. B 83, 214510 (2011).

[45] A. Ruff, M. Sing, R. Claessen, H. Lee, M. Tomic, H. O. Jeschke, and R. Valenti, Phys. Rev. Lett. 110, 216403 (2013).