Accepted Manuscript

Full Length Article

Stability and charge separation of different $CH_3NH_3SnI_3/TiO_2$ interface: A first-principles study

Zhenzhen Yang, Yuanxu Wang, Yunyan Liu

<table>
  <tr>
    <td>PII:</td>
    <td>S0169-4332(18)30381-7</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>https://doi.org/10.1016/j.apsusc.2018.02.038</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>APSUSC 38496</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Applied Surface Science</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>24 November 2017</td>
  </tr>
  <tr>
    <td>Revised Date:</td>
    <td>18 January 2018</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>4 February 2018</td>
  </tr>
</table>

![](./images/813061234852102145_1.jpg)

Please cite this article as: Z. Yang, Y. Wang, Y. Liu, Stability and charge separation of different $CH_3NH_3SnI_3/TiO_2$ interface: A first-principles study, *Applied Surface Science* (2018), doi: https://doi.org/10.1016/j.apsusc.2018.02.038

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Stability and charge separation of different $\text{CH}_3\text{NH}_3\text{SnI}_3/\text{TiO}_2$ interface: A first-principles study

Zhenzhen Yang$^1$, Yuanxu Wang$^{1,2,*}$, and Yunyan Liu$^{3,*}$

$^1$Institute for Computational Materials Science, School of Physics and Electronics, Henan University, Kaifeng 475004, China

$^2$School of Physics, Anyang Normal University, Anyang 455000, China

$^3$School of Physics and Optoelectronic Engineering, Shandong University of Technology, Zibo 255049, China

*Email: wangyx@henu.edu.cn, liuyunyan@sdut.edu.cn

## ABSTRACT

Interface has an important effect on charge separation of perovskite solar cells. Using first-principles calculations, we studied several different interfaces between $\text{CH}_3\text{NH}_3\text{SnI}_3$ and $\text{TiO}_2$. The interfacial structure and electronic structure of these interfaces are thoroughly explored. We found that the $\text{SnI}_2$/anatase ($\text{SnI}_2$/A) system is more stable than the other three systems, because an anatase surface can make Sn-I bond faster restore to the pristine value than a rutile surface, and $\text{SnI}_2$/A system has a smaller standard deviation. The calculated plane-averaged electrostatic potential and the density of states suggest that $\text{SnI}_2$/anatase interface has a better separation of photo-generated electron-hole pairs.

Keywords: Perovskite solar cell; $\text{CH}_3\text{NH}_3\text{SnI}_3$ and $\text{TiO}_2$; Interface; first-principles

### Introduction

Since organic-inorganic hybrid perovskite solar cells (PSCs) were first introduced in 2009 [1], they have drawn wide concern because of the rapid rise in the power conversion efficiency (PCE) [2–7]. Other key features of these hybrid perovskites include their ease of solution-based processing at low temperature, low cost, and strong optical absorption, long diffusion length, and high charge carrier mobility [8–14]. Thus far, the power conversion efficiency of PSCs has been over 22% [15].

However, the toxicity of lead undoubtedly hinders the commercialization of this new technology because it does harm to both the human body and the environment. Thus, many efforts have been devoted to exploring lead-free PSCs [16–22]. Sn-based PSCs represented by $CH_3NH_3SnI_3$ have been suggested as lead-free PCS candidates because the nontoxic Sn element in the same group could be used to replace Pb. One of the most common strategies for exploring possible candidates is the concept suggested by Goldschmidt [25] in 1926 and adapted further by other groups [23,24], in which a semi-empirical tolerance factor, $\tau$, was introduced to evaluate ionic size mismatch that the perovskite structure will tolerate until a different structure type is formed. $\tau$ is defined by

$$
\tau{=}({\rm r_A{+}r_X})/{\sqrt{2}}({\rm r_B{+}r_X}), \tag{1}
$$

where ${\rm r_A}$, ${\rm r_B}$, and ${\rm r_X}$ are ionic radii of the A, B, and X ions, respectively. When $\tau$ is close to 1, the perovskite configuration exhibits an ideal cubic structure (space group: Pm3m). For values of $\tau$ in the range of 0.9–1.0, we can expect the forming of cubic perovskites in practice, while values of 0.80–0.89 predominantly lead to distorted

perovskites, resulting in orthorhombic, rhombohedral, or tetragonal structures.

Organic-inorganic hybrid perovskites usually consist of cation A $(A=CH_{3}NH_{3}^{+}$,
$HC(NH_{2})_{2}^{+})$ and octahedron $BX_{6}$ ($B=Si^{2+}$, $Ge^{2+}$, $Pb^{2+}$, $Sn^{2+}$; $X=Cl^{-}$, $Br^{-}$, $I^{-}$). For
example, in $CH_{3}NH_{3}PbI_{3}$, Pb forms octahedron with 6 I ions, and $CH_{3}NH_{3}^{+}$ is located
in the center of the octahedron gap [26], in which the coordination number of
$CH_{3}NH_{3}^{+}$ is 12. The length of Pb-I bond ranges from 3.14–3.22 Å, and the length of
Sn-I bond ranges from 3.07–3.18 Å. Considering that the ion radius of $Pb^{2+}$ and $I^{-}$ are
1.2 and 2.2 Å, respectively, the $\tau$ value of $CH_{3}NH_{3}PbI_{3}$ is 0.83. Since $Sn^{2+}$ ion radius
(1.1 Å) is smaller than $Pb^{2+}$, $CH_{3}NH_{3}SnI_{3}$ should have a larger $\tau$, indicating the
smaller octahedron distortion of $CH_{3}NH_{3}SnI_{3}$ than $CH_{3}NH_{3}PbI_{3}$.

Besides, $CH_{3}NH_{3}SnI_{3}$ has an optical band gap of 1.23 eV [3] implying a significant
red shift, in comparison with the optical band gap of $CH_{3}NH_{3}PbI_{3}$ (~1.55 eV) [13,
24,27]. Therefore, it can be controllably tuned to cover much of visible spectrum. In
addition, $CH_{3}NH_{3}SnI_{3}$ perovskite has a great potential for realizing stable structure
[28,29], enhancing photo responsiveness [29], long carrier-diffusion length [30], and
good carrier mobility [22]. These outstanding performances suggest that $CH_{3}NH_{3}SnI_{3}$
perovskite solar cells are very promising for environmentally friendly high-efficiency
PSCs with further device optimization. However, the PCE of Sn-based PSCs is much
lower than that of Pb-based ones [16,31] because of the high carrier recombination
rate at the interface and a lower absorption coefficient of the $ASnI_{3}$ perovskites [30].
The low stability of $Sn^{2+}$ associating with structural instability is still another
unresolved issue for poor photovoltaic performance in Sn-based PSCs [2,32]. To

further increase PCE of Sn-based PSCs, it is necessary to optimize film quality and cell structure by studying the interface properties in it.

Interface plays a key role on charge processes, and thus determines the performance of a solar cell. The charge process includes separation, extraction, transport, and recombination of carriers. Carriers recombination mainly occurs at the window/perovskite/HTM (hole transport material) interfaces of PSCs, due to the easier forming deep-level recombination center at the interface induced by the surface effect [33], which is detrimental to device performance. Carrier separation and extraction, relying on the electronic structure in interface, are supposed to have a significantly influence on the the short-circuit current densities (Jsc), fill factor (FF), and PCE of the cell [34]. For example, Jiang et al. found that a suitable interface roughness effectively weakens the leakage current and carrier recombination [35]. The different PCEs achieved by various synthetic methods and interface structures of PSCs imply the complexity and importance of the interface in a charge process. For example, the surface defect is considered to be passivated by the existence of $PbI_2$, which can improve the charge separation efficiency at the interface between $TiO_2$ and perovskite [36]. Wang et al. proposed that the remaining $PbI_2$ may slow the interfacial charge extraction [37]. Hysteresis of PSCs has drawn much attention and is also related to the interface and charge processes. The origin of hysteresis behavior of PSCs is thought to be caused by non-radiative recombination induced by a high density of traps in the window/perovskite interface [38,39]. However, the trap mechanism cannot explain the reversible poling behavior observed in PSCs. Researchers have proposed other mechanisms, such as ionic motion, for the origin of

hysteresis [40].

Thus, it is necessary to shed light on the structural and electronic properties of perovskite/TiO₂ interfaces for suppressing interfacial carrier recombination, fasting carrier separation, and efficient charge extraction. In this paper, the first-principles method was employed to investigate interface-related issues of CH₃NH₃SnI₃/TiO₂ interface. TiO₂ has three phases: anatase, rutile, and brookite. Due to the thermodynamic instability of brookite, we only consider anatase and rutile in the current work. The stability of different interface models has been estimated by comparing their binding energies. It was found that the SnI₂/anatase (SnI₂/A) interface is more stable than the other three ones (SnI₂/rutile interface, CH₃NH₃I/anatase interface, and CH₃NH₃I/rutile interface). Moreover, an analysis of calculated electrostatic potential and the density of states (DOS) suggests that SnI₂/anatase interface has a better separation of photo-generated electron-hole pairs than the other three studied interface models.

Modeling perovskite interfaces

The optimized lattice constants of anatase TiO₂ are a=3.776 Å and c=9.486 Å, and those of rutile TiO₂ are a=4.594 Å and c= 2.959 Å, which are close to the experimental values [41,42]. We also optimized tetragonal CH₃NH₃SnI₃ with a=8.69 Å and c=13.40 Å, which are close to the experimental values [24]. Previous theoretical and X-ray diffraction measurements have shown that for tetragonal CH₃NH₃PbI₃, the (001) surface is the most stable surface among various surfaces [43]. Since CH₃NH₃SnI₃ has a similar structure to CH₃NH₃PbI₃, we also select the (001)

surface to build $\text{CH}_3\text{NH}_3\text{SnI}_3/\text{TiO}_2$ interface. We consider two types of termination: (1) the $\text{CH}_3\text{NH}_3\text{I}$ termination (MAI-T) and (2) the $\text{SnI}_2$ termination ($\text{SnI}_2$-T). It is reasonable because $\text{CH}_3\text{NH}_3\text{SnI}_3$ perovskite is composed by MAI and $\text{SnI}_2$ layers along the c axis. In addition, a band gap of 1.23 eV is obtained by calculating the density of states (DOS) of the optimized $\text{CH}_3\text{NH}_3\text{SnI}_3$. This band-gap value is in agreement with one in the reported literature [3].

We used the optimized $\text{CH}_3\text{NH}_3\text{SnI}_3$ and $\text{TiO}_2$ to build interface. Previous experimental works showed that the {001} facets of $\text{TiO}_2$ are beneficial for the photovoltaic applications [44,45] and thus only the (001) surface is considered here for constructing the perovskite/$\text{TiO}_2$ interface model. To obtain a configuration with minimal interface stress, we couple the (001) surface of the perovskite with the (001) $\text{TiO}_2$ substrate. That is to say that the interfaces between rutile (001), anatase (001), and $\text{CH}_3\text{NH}_3\text{SnI}_3$ (001) have a relatively small lattice mismatch between $\text{TiO}_2$ and $\text{CH}_3\text{NH}_3\text{SnI}_3$ among many possible combinations between $\text{TiO}_2$ and perovskite surfaces. For Pb-based perovskite solar cell, previous studies about $\text{CH}_3\text{NH}_3\text{PbI}_3/\text{TiO}_2$ interface also employed $\text{CH}_3\text{NH}_3\text{PbI}_3$ (001) and $\text{TiO}_2$ (001) to build their interface for their small lattice mismatch and stability [46,47]. The rutile (001) slab consists of four layers, and the anatase $\text{TiO}_2$ (001) has five layers rotated at $26.565^\circ \sqrt{5}$ x$\sqrt{5}$ anatase surface.

To simulate the interfaces, we constructed interface models by placing perovskite (001) slabs on top of four rutile layers or five anatase layers with 20 Å vacuum above the perovskite (along z direction). The perovskite has MAI-T and $\text{SnI}_2$-T. MAI-T consists of four MAI and three $\text{SnI}_2$ layers, while $\text{SnI}_2$-T has four $\text{SnI}_2$ and three MAI

layers. Sometimes, perovskite slabs can be slightly shifted to avoid interaction between anion-anion, namely I-O. The interface systems are full relaxed, and the optimized four types of interface configurations are plotted in Fig. 1.

For building computational models for $CH_3NH_3SnI_3/TiO_2$, we followed the procedure outlined in the computational details and searched for a common supercell where the level of mismatch between $CH_3NH_3SnI_3$ and the substrate was 5.78% and -2.8%, respectively, as shown in Table 1. The binding energies of the composites were calculated by

$$E_\text{b}=E_\text{total}-E_\text{sub}-E_\text{p}, \tag{2}$$

where $E_\text{total}$, $E_\text{sub}$, and $E_\text{p}$ are the total energies of the $TiO_2$ system, isolate perovskite, and $TiO_2$ substrate, respectively. As seen from Table 1, the magnitude of the binding energies of the four structures are close, and the binding energies of MAI/R and MAI/A are higher than those of $SnI_2/R$ and $SnI_2/A$. The possible reason can be analyzed from the interaction between atoms in the interface. As we know, the interaction between $CH_3NH_3^+$ ions of the MAI-T and other ions is weak and belongs to either van der Waals (vdW) or hydrogen bond. However, the chemical bonding is formed between the Sn atom of $SnI_2$-T and other atoms.

### Computational details

The calculations were performed by the projector augmented wave (PAW) method [48], as implemented in the Vienna Ab Initio Simulation Package (VASP) [49,50]. The electron exchange correlation interactions are treated within the generalized

gradient approximation (GGA) [51] using the Perdew-Burke-Ernzerhof (PBE) functional [52]. Valence configuration for Sn, I, C, N, and H atoms are 5d6s6p, 5s5p, 2s2p, 2s2p, and 1s, respectively. The cutoff energy was set to be 400 eV. Brillouin zone integration is used with grid of 4×4×1 Monkhorst-Pack k-mesh. The studied structures were fully relaxed with conjugate-gradient algorithm until the forces on each ion are less than 0.01 eV/Å. Cages formed by four SnI₆ octahedron are large enough to accommodate MA⁺ ions and there are no obvious chemical bond formations between MA⁺ ions and the inorganic matrix. Therefore, we used vdW-DF [53] to deal with the weak interaction in these interface structures.

Results and discussion

The redistribution of atoms in an interface has an important effect on its electronic structure and charge transfer at the interface. To quantify the amount of induced changes in CH₃NH₃SnI₃, we calculated average bond length of Sn-I and its standard deviation in each layer of CH₃NH₃SnI₃. The Sn-I bonds are numbered to facilitate the description, as shown in Fig. 1. The results are listed in Table 2. Sn-Iᵦ, Sn-Iₑ, and Sn-Iₜ represent the bonds formed by the Sn atom located at the center of the octahedral and the I atom located at the bottom of the octahedron, the I atom located at the middle of the octahedron, and the I atom at the top of the octahedron. As seen in this table, the Sn-I bonds in the Sn₁ deviate from their pristine value (Sn-Iᵦ=3.0375 Å, Sn-Iₑ=3.1159 Å, Sn-Iₜ=3.1945 Å), and full recovery may occur after many more layers. In fact, the Sn-I bonds in the interface are greatly elongated and distorted although we could not prove whether any of Sn-I bonds are broken. The further Sn-I bonds in c axis are

away from the interface, the closer they will be to the pristine value. The law of change of $Sn-I_t$ and $Sn-I_b$ along c axis is analyzed separately for clearly understanding the data in Table 2. The bonds of $Sn-I_b$ of MAI/R, $SnI_2$/R, and $SnI_2$/A become more and more stable because they are getting smaller and closer to the pristine value the further away they are from the interface along c axis, and the $Sn-I_b$ bond length of MAI/A changes without obvious regularity. The $Sn-I_b$ bond of $SnI_2$/A is more stable than MAI/R, $SnI_2$/R, because the length of $Sn-I_b$ is very close to the pristine value, and the standard deviation is small. The study of the $Sn-I_t$ bond length of MAI/R and $SnI_2$/R is meaningless because their $Sn-I_t$ bond length has no obvious orderliness although they have a small standard deviation. The $SnI_2$/A, compared with the other three structures, should be a stable structure because its $Sn-I_t$ bond length is smaller and tends to be the original value, and its standard deviation is very small. To summarize, $SnI_2$/A should be the best candidate because its bond length can be quickly close to the original value from the elongated state at the interface, and the length of its bond is relatively concentrated. Figure 1 shows the bonding conditions at the interface. In $SnI_2$/A, all I and Sn atoms at the interface of $CH_3NH_3SnI_3$ are bonded to Ti and O atoms in $TiO_2$, while only a small amount of atomic bonds are bonded in MAI/R, MAI/A, and $SnI_2$/R, indicating that $SnI_2$/A has a strong electron transfer capacity at the interface.

To investigate interaction between atoms in the interface, we calculated the electron localization function (ELF), which can effectively reveal the nature of different chemical interaction directly from the charge localization between individual atoms. Figure 2 shows the calculated ELF for the four optimized $CH_3NH_3SnI_3/TiO_2$

interfaces. The value of the ELF ranges from 0–1. In Fig. 2, the red signifies the highly localized electrons, the blue represents charge accumulation, and the green with value of 0.5 corresponds to the electron-gas-like pair probability as in metallic bonds. As seen in Fig. 2, in the four systems, the electrons around H atoms of $MA^{+}$ ions, I atoms, and O atoms are more localized, while the electrons around Sn and Ti atoms show an electron gas-like feature. The blue between interface anions and cations suggests the chemical interactions between them. Comparing Figs. 1(a) and 1(b), the $SnI_{2}$-T systems show electron-gas-like features in the interface, meaning that there is a large charge transfer in it.

The degree of the potential drop on the interface between the perovskite and $TiO_{2}$ clearly shows the capability of photo-excited charge separation on the interface. Figure 3 shows the plane-averaged electrostatic potential of the four structures, which can estimate the electronic level positions. After contacting between $TiO_{2}$ and $CH_{3}NH_{3}SnI_{3}$, their different Fermi level drive electrons transfers from the $CH_{3}NH_{3}SnI_{3}$ to $TiO_{2}$ slab. Meanwhile, a built-in electric field from $CH_{3}NH_{3}SnI_{3}$ to $TiO_{2}$ slab will be formed. This electric field will hinder further charge transferring, and then the interface becomes equilibrium. The degree of charge transferring can be analyzed from the calculated Bader charge, as shown in Table 1. The negative value indicates the charge transfer direction from $CH_{3}NH_{3}SnI_{3}$ to $TiO_{2}$. As seen in Fig. 3, $CH_{3}NH_{3}SnI_{3}$ has a higher average potential than $TiO_{2}$, and thus the charge will transfer from $CH_{3}NH_{3}SnI_{3}$ to $TiO_{2}$. The difference in potential between anatase and $CH_{3}NH_{3}SnI_{3}$ is relatively larger than that between $CH_{3}NH_{3}SnI_{3}$ and rutile. Consequently, $CH_{3}NH_{3}SnI_{3}$/anatase interface has a stronger charge transfer. Because

MAI layers have a higher potential than $SnI_2$ layers, the interface of $SnI_2$-T system has a larger potential drop than that of MAI-T, especially for the $SnI_2$/anatase interface, indicating the strong capability of electron-hole separation in the $SnI_2$/anatase interface. Thus, a strong accumulation of electrons from $CH_3NH_3SnI_3$ to $TiO_2$ will happen, which will help electron-hole separation in the solar cells.

Figure 4 shows the calculated partial DOS (PDOS) of the $TiO_2$/perovskite interface. As seen in Fig. 4, the conduction band minimum (CBM) of $CH_3NH_3SnI_3$ mainly comes from Sn p, and the valence band maximum (VBM) is primarily contributed from I p and partially from Sn s. The organic cations, $CH_3NH_3^+$, have no contribution to the formation of the valence band or the conduction band. Because the band gap of $CH_3NH_3SnI_3$ is smaller than that of $TiO_2$, the photo-absorption efficiency is determined by the energy difference between I p and Sn p. Moreover, the CBM of $TiO_2$ is lower than that of $CH_3NH_3SnI_3$. Therefore, the photo-excited electrons from valence band (VB) to conduction band (CB) of $CH_3NH_3SnI_3$ (Sn-p) will transfer to the CB of $TiO_2$. The energy difference between Sn-p and Ti-d determines the efficiency of charge transfer in the interface. As seen in Fig. 4, the calculated band gap of $SnI_2$-T is slightly smaller than that of MAI-T. This is largely caused by the outflowing of electrons from the Sn atom in $SnI_2$-T leads to the left shift of Sn state, which will decrease the band gap.

To understand the microscopic mechanism of charge separation on interface, the calculated layer-resolved DOS for the $CH_3NH_3SnI_3/TiO_2$ interface are depicted in Fig. 5. The organic cations $CH_3NH_3^+$ have no contribution to the formation of the VB or CB; they only contribute to donating electrons. As shown in Fig. 5, the calculated

results show that the VBM mainly come from I p and the CBM mainly come from Sn p. As for $TiO_2$, the VBM mainly come from O p and the CBM mainly come from Ti d.
These results show how the halogen atom principally defines the VBM and the metallic cation defines the CBM, whereas the organic molecule does not contribute to the states close the Fermi level. The role of the organic molecule has been studied in some works, where the influence of molecule orientation during synthesis is little, so the main role of $CH_3NH_3$ in this type of perovskite is to provide stability to the structure and to facilitate the solution processing used for film formation. In the light irradiation, electron-hole pairs separation occurs in the perovskite, and then the electrons transfer to the electron transport layer and the holes transfer to the hole transport layer. During the transfer of electrons at the interface, the electrons on the CB of perovskite transfer to the CB of $TiO_2$. As seen in Fig. 5 (d), in $SnI_2$-T the CBM of anatase $TiO_2$ (Ti d) is much lower than that of $CH_3NH_3SnI_3$ with $SnI_2$-T (Sn p states), indicating that the photo-generated electrons can easily transfer from $CH_3NH_3SnI_3$ to anatase $TiO_2$. Moreover, there are few states on the CB of Layer 1 of MAI-T. Thus, the electron-transferring capability of $SnI_2$-T should be better than that of MAI-T.

### Conclusion

In summary, we have performed first-principles calculations to study the structure and electronic properties of the interface between $CH_3NH_3SnI_3$ and $TiO_2$. We found that Anatase (001) surface has a better lattice and atoms arrangement match with $CH_3NH_3SnI_3$. The charge transfers from $CH_3NH_3SnI_3$ to $TiO_2$ are observed for all four


systems. However, $SnI_2$/A interface is more stable than the other three interfaces.

Meanwhile, the $SnI_2$-T interface could make electron-hole pairs separate and transport more easily. Therefore, anatase $TiO_2$ may be a better candidate for electron transporting materials in $CH_3NH_3SnI_3$ perovskite solar cells.

## Acknowledgements
The authors acknowledge the Natural Science Foundation of China (Grant No. 11674083 and 11404191).

## References
1.  A. Kojima, K. Teshima, Y. Shirai, T. Miyasaka, Organometal halide perovskites as visible-light sensitizers for photovoltaic cells, J. Am. Chem. Soc. 131 (2009) 6050–6051.
2.  F. Hao, C.C. Stoumpos, D.H. Cao, R.P. Chang, M.G. Kanatzidis, Lead-free solid-state organic-inorganic halide perovskite solar cells, Nat. Photon 8 (2014) 489-494.
3.  J. Burschka, N. Pellet, S.J. Moon, R. Humphry-Baker, P. Gao, M.K. Nazeeruddin, M. Grätzel, Sequential deposition as a route to high-performance perovskite-sensitized solar cells, Nature 499 (2013) 316-319.
4.  M. Graetzel, The light and shade of perovskite solar cells, Nat. Mater. 13 (2014) 838-842.
5.  N.J. Jeon, J.H. Noh, W.S. Yang, Y.C. Kim, S. Ryu, J. Seo, S. Seok, Compositional engineering of perovskite materials for high-performance solar cells, Nature 517 (2015) 476-480.
6.  M. Saliba, T. Matsui, K. Domanski, J.Y. Seo, A. Ummadisingu, S.M. Zakeeruddin, J.P. Correa-Baena, W.R. Tress, A. Abate, A. Hagfeldt, M. Grätzel, Incorporation of rubidium cations into perovskite solar cells improves photovoltaic performance, Science 354 (2016) 206-209.
7.  S.S. Shin, E.J. Yeom, W.S. Yang, S. Hur, M.G. Kim, J. Im, J. Seo, J.H. Noh, S. Seok, Colloidally prepared La-doped $BaSnO_3$ electrodes for efficient, photostable perovskite solar cells, Science 356 (2015) 167-171.
8.  W. Nie, H. Tsai, R. Asadpour, J.C. Blancon, A.J. Neukirch, G. Gupta, J.J. Crochet, M. Chhowalla, S. Tretiak, M.A. Alam, High-efficiency solution-processed perovskite solar cells with millimeter-scale grains, Science 347 (2015) 522-525.
9.  Q. Dong, Y. Fang, Y. Shao, P. Mulligan, J. Qiu, L. Cao, J. Huang, Electron-hole diffusion lengths > 175 mu m in solution-grown $CH_3NH_3PbI_3$ single crystals, Science 347 (2015) 967-970.
10. G. Xing, N. Mathews, S. Sun, S.S. Lim, Y.M. Lam, M. Graetzel, S. Mhaisalkar, T.C. Sum, Long-range balanced electron- and hole-transport lengths in organic-inorganic $CH_3NH_3PbI_3$, Science 342 (2013) 344-347.

25. V.M. Goldschmidt, Die Gesetze der Krystallochemie, Sci. Nat. 14 (1926) 477-485.

26. N.K. McKinnon, D.C. Reeve, M.H. Akabas, 5-HT3 receptor ion size selectivity is a property of the transmembrane channel, not the cytoplasmic vestibule portals, J. Gen. Phys. 138 (2011) 453-466.

27. G.C. papaassiliou, I.B. Koutselas, Structural, optical and related properties of some natural three and lower dimensional semiconductor systems, Synthetic Met. 71 (1995) 1713-1714.

28. A. Waleed, M.M. Tavakoli, L.L. Gu, Z.Y. Wang, D.Q. Zhang, A. Manikandan, Q.P. Zhang, R.J. Zhang, Y.L. Chueh, Z.Y. Fan, Lead-free perovskite nanowire array photodetectors with drastically improved stability in nanoengineering templates, Nano Lett. 17 (2017) 523-530.

29. X.J. Lü, Y.G Wang, C.C. Stoumpos, Q.Y. Hu, X.F. Guo, H.J. Chen, L.X. Yang, J.S. Smith, W.G. Yang, Y.S. Zhao, H.W. Xu, M.G. Kanatzidis, Q.X. Jia, Enhanced structural stability and photo responsiveness of $CH_{3}NH_{3}SnI_{3}$ perovskite via pressure-induced amorphization and recrystallization, Adv. Mater. 28 (2016) 8663-8668

30. L. Ma, F. Hao, C.C. Stoumpos, B.T. Phelan, M.R. Wasielewski, M.G. Kanatzidis, Carrier diffusion lengths of over 500 nm in lead-free perovskite $CH_{3}NH_{3}SnI_{3}$ films, J. Am. Chem. Soc. 138 (2016) 14750-14755.

31. S. Lee, D.W. Kang, Highly efficient and stable Sn-rich perovskite solar cells by introducing bromine, ACS Appl. Mater. Interfaces 9 (2017) 22432-22439.

32. M.H. Kumar, S. Dharani, W.L. Leong, P.P. Boix, R.R. Prabhakar, T. Baikie, C. Shi, H. Ding, R. Ramesh, M. Asta, M. Graetzel, S.G. Mhaisalkar, N. Mathews, Lead-free halide perovskite solar cells with high photocurrents realized through vacancy modulation, Adv. Mater. 26 (2014) 7122-7127.

33. J.J. Shi, X. Xu, D.M. Li, Q.B. Meng, Interfaces in perovskite solar cells, Small, 11 (2015) 2472-2486.

34. D.H. Kim, K.G. Lim, J.H. Park, T.W. Lee, Controlling surface enrichment in polymeric hole extraction layers to achieve high-efficiency organic photovoltaic cells, ChemSusChem 5 (2012) 2053-2057.

35. L.L. Jiang, S. Cong, Y.H. Lou, Q.H. Yi, J.T. Zhu, H. Ma, G.F. Zou, Interface engineering toward enhanced efficiency of planar perovskite solar cells, J. Mater. Chem. A 4 (2016) 417.

36. Q. Chen, H. Zhou, T.B. Song, S. Luo, Z. Hong, H.S. Duan, L. Dou, Y. Liu, Y. Yang, Controllable self-induced passivation of hybrid lead iodide perovskites toward high performance solar cells, Nano Lett. 14 (2014) 4158-4163.

37. L. Wang, C. McCleese, A. Kovalsky, Y. Zhao, C. Burda, Femtosecond time-resolved transient absorption spectroscopy of $CH_{3}NH_{3}PbI_{3}$ perovskite films: evidence for passivation effect of $PbI_{2}$, J. Am. Chem. Soc. 136 (2014) 12205-12208.

38. H.J. Snaith, A. Abate, J.M. Ball, G.E. Eperon, T. Leijtens, N.K. Noel, S.D. Stranks, J.T. Wang, K. Wojciechowski, W. Zhang, Anomalous hysteresis in perovskite solar cells, J. Phys. Chem. Lett. 5 (2014) 1511-1515.

39. Y. Shao, Z. Xiao, C. Bi, Y. Yuan, J. Huang, Origin and elimination of photocurrent hysteresis by fullerene assivation in $CH_{3}NH_{3}PbI_{3}$ planar heterojunction solar cells. Nat. Commun. 5 (2014) 5784-5791.

40. T. Leijtens, G. E. Eperon, N. K. Noel, S. N. Habisreutinger, A. Petrozza, H. J. Snaith, Stability of metal halide perovskite solar cells, Adv. Energy Mater. 5 (2015) 1500963.

41. D. Eugen, C. Laurent, C. Benoît, J. Etienne, V. Cristian, K. Hyun-Joo, K. Erjun, W. Myung-Hwan, Half-metallic ferromagnetism and large negative magnetoresistance in the new lacunar spinel $GaTi_{3}VS_{8}$, J. Am. Chem. Soc. 132 (2010) 5704-5710.

42. V.I. Khitrova, M.F. Bundule, Z.G. Pinsker, An electron-diffraction investigation of titanium dioxide in thin films, Kristallografiya 22 (1977) 1253-1258

43. J. Haruyama, K. Sodeyama, L. Han, Y. Tateyama, Termination dependence of tetragonal $CH_{3}NH_{3}PbI_{3}$ surfaces for perovskite solar cells, J. Phys. Chem. Lett. 5 (2014) 2903-2909.

44. L. Etgar, P. Gao, Z. Xue, Q. Peng, A.K. Chandiran, B. Liu, Md.K. Nazeeruddin, M. Gratzel, J. Am. Chem. Soc. 134 (2012) 17396-17399.

45. A. Mei, X. Li, L. Liu, Z. Ku, T. Liu, Y. Rong, M. Xu, M. Hu, J. Chen, Y. Yang, M. Gratzel, H. Han, Science 345 (2014) 295-298.

46. W. Geng, C.J. Tong, J. Liu, W.J. Zhu, W.M. Lau, L.M. Liu, structure and electronic properties of different $CH_{3}NH_{3}PbI_{3}/TiO_{2}$ interface: A first-principles study, Sci. Rep. 6 (2016) 20131.

47. G.A. Nemnes, C. Goehry, T.L. Mitran, A. Nicolaev, L. Ion, S. Antohe, N. Plugaru, A. Manolescu, Band alignment and charge transfer in rutile-$TiO_{2}/CH_{3}NH_{3}PbI_{3-x}Cl_{x}$ interface, Phys. Chem. Chem. Phys. 17 (2015) 30417-30423.

48. P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953-17979.

49. G. Kresse, J. Furthmüller, Efficient Iterative Schemes Forab Initiototal-Energy Calculations Using a Plane- Wave Basis Set, Phys. Rev. B 54 (1996) 11169-11186.

50. G. Kresse, J. Furthmüller, Efficiency of Ab-Initio Total Energy Calculations for Metals and Semiconductors Using a Plane-Wave Basis Set, Comp. Mater. Sci. 6 (1996) 15-50.

51. J.P. Perdew, Y. Wang, Accurate and simple analytic representation of the electron-gas correlation energy, Phys. Rev. B 45 (1992) 13244-13249.

52. J.P. Perdew, K. Burke, M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77 (1996) 3865-3868.

53. M. Dion, H. Rydberg, E. Schroder, D.C. Langreth, B.I. Lundqvist, Van der Waals density functional for general geometries, Phys. Rev. Lett. 92 (2004) 246401-246405.

Table 1 The calculated binding energy and lattice mismatch of the interface structures

<table>
  <thead>
    <tr>
      <th></th>
      <th>Bader charge</th>
      <th>Lattice mismatch</th>
      <th>Binding energy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MAI/R</td>
      <td>-0.5004</td>
      <td>5.78%</td>
      <td>-0.1419</td>
    </tr>
    <tr>
      <td>MAI/A</td>
      <td>-0.5080</td>
      <td>-2.80%</td>
      <td>-0.1467</td>
    </tr>
    <tr>
      <td>SnI₂/R</td>
      <td>-0.4758</td>
      <td>5.78%</td>
      <td>-0.1646</td>
    </tr>
    <tr>
      <td>SnI₂/A</td>
      <td>-0.5226</td>
      <td>-2.80%</td>
      <td>-0.1789</td>
    </tr>
  </tbody>
</table>

Table 2 Calculated Sn-I average bond distance (in angstroms) and its standard deviation in each layer of CH₃NH₃SnI₃ for the interface systems. The amount of standard deviation is given in parenthesis. The top, equatorial, and bottom sites of the iodine ions in a Sn-I₆ cage are indicated by Iₜ, Iₑ, and Iᵦ.

<table>
  <thead>
    <tr>
      <th>Bond length (Å)</th>
      <th>MAI/R</th>
      <th>MAI/A</th>
      <th>SnI₂/R</th>
      <th>SnI₂/A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sn₄-Iₜ</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sn₄-Iₑ</td>
      <td></td>
      <td></td>
      <td>3.1796(0.1487)</td>
      <td>3.3066(0.3698)</td>
    </tr>
    <tr>
      <td>Sn₄-Iᵦ</td>
      <td></td>
      <td></td>
      <td>3.1600(0.0722)</td>
      <td>3.0310(0.0140)</td>
    </tr>
    <tr>
      <td>Sn₃-Iₜ</td>
      <td>3.2829(0.1342)</td>
      <td>3.1953(0.0247)</td>
      <td>3.3686(0.1850)</td>
      <td>3.3282(0.0145)</td>
    </tr>
    <tr>
      <td>Sn₃-Iₑ</td>
      <td>3.1563(0.0235)</td>
      <td>3.3766(0.3265)</td>
      <td>3.1567(0.0164)</td>
      <td>3.3792(0.3498)</td>
    </tr>
    <tr>
      <td>Sn₃-Iᵦ</td>
      <td>3.3528(0.1954)</td>
      <td>3.2538(0.2342)</td>
      <td>3.1889(0.1587)</td>
      <td>3.0658(0.0045)</td>
    </tr>
    <tr>
      <td>Sn₂-Iₜ</td>
      <td>3.3170(0.3091)</td>
      <td>3.1712(0.0738)</td>
      <td>3.3721(0.2463)</td>
      <td>3.3823(0.0373)</td>
    </tr>
    <tr>
      <td>Sn₂-Iₑ</td>
      <td>3.1295(0.0178)</td>
      <td>3.3019(0.2649)</td>
      <td>3.1383(0.0515)</td>
      <td>3.3057(0.2510)</td>
    </tr>
    <tr>
      <td>Sn₂-Iᵦ</td>
      <td>3.5017(0.5274)</td>
      <td>3.2182(0.0719)</td>
      <td>3.3090(0.3257)</td>
      <td>3.0660(0.0342)</td>
    </tr>
    <tr>
      <td>Sn₁-Iₜ</td>
      <td>3.3534(0.4550)</td>
      <td>3.1307(0.0072)</td>
      <td>3.3272(0.4105)</td>
      <td>3.8205(0.0223)</td>
    </tr>
    <tr>
      <td>Sn₁-Iₑ</td>
      <td>3.1700(0.0722)</td>
      <td>3.3435(0.3232)</td>
      <td>3.1960(0.1734)</td>
      <td>3.4115(0.0689)</td>
    </tr>
    <tr>
      <td>Sn₁-Iᵦ</td>
      <td>3.5832(0.8429)</td>
      <td>3.3417(0.0216)</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

![](./images/813061234852102145_2.jpg)

Figure 1 Optimized geometrical structures of (a) MAI/R, (b) MAI/A, (c) SnI₂/R, (d) SnI₂/A in polyhedron. Magnified area in the middle (different angle for better view) show the bond strengths of I, Sn, Ti, and O at the interface. (dark gray: Sn; brown: C; purple: I; blue: N; pink: H; cyan: Ti; red: O).

![](./images/813061234852102145_3.jpg)

Figure 2 ELF of (a) MAI/R, (b) MAI/A, (c) SnI₂/R, (d) SnI₂/A.

![](./images/813061234852102145_4.jpg)

Figure 3 Plane-averaged electrostatic potential for (a) MAI/R, (b) MAI/A, (c) $SnI_2$/R, (d) $SnI_2$/A.

![](./images/813061234852102145_5.jpg)

Figure 4 PDOS of (a) MAI/R, (b) MAI/A, (c) SnI₂/R, (d) SnI₂/A.

![](./images/813061234852102145_6.jpg)

Figure 5 Calculated layer-resolved density of states (DOS) of (a) MAI/R, (b) MAI/A, (c) $SnI_2$/R, (d) $SnI_2$/A. The green, blue, indigo, red, and black lines present the DOS of I, Sn, $CH_3NH_3$-, O and Ti, respectively.

![](./images/813061234852102145_7.jpg)

$SnI_2$/anatase interface is more stable than $SnI_2$/rutile interface, $CH_3NH_3I$/anatase interface, and $CH_3NH_3I$/rutile interface. Moreover, $SnI_2$/anatase interface could make electron-hole pairs separate and transport more easily