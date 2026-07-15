**Full paper**

# Interfacial charge behavior modulation in 2D/3D perovskite heterostructure
for potential high-performance solar cells

Biao Liu$^{\mathrm{a}}$, Mengqiu Long$^{\mathrm{a}}$, Mengqiu Cai$^{\mathrm{b}}$, Liming Ding$^{\mathrm{c},*}$, Junliang Yang$^{\mathrm{a},**}$

$^{\mathrm{a}}$ Hunan Key Laboratory for Super-microstructure and Ultrafast Process, School of Physics and Electronics, Central South University, Changsha, 410083, Hunan, China
$^{\mathrm{b}}$ School of Physics and Electronics Science, Hunan University, Changsha, 410082, Hunan, China
$^{\mathrm{c}}$ Center for Excellence in Nanoscience, Key Laboratory of Nanosystem and Hierarchical Fabrication, National Center for Nanoscience and Technology, Beijing, 100190, China

---

## ARTICLE INFO

**Keywords:**
2D/3D perovskite heterostructure
Charge recombination center
First-principle calculations
Energy level arrangement

---

## ABSTRACT

2D/3D perovskite heterostructure can combine the advantages of 2D perovskite with well stability and 3D perovskite with high efficiency. 2D BA₂PbI₄/3D MAPbI₃ heterostructures are constructed to study the interfacial electrical properties and charge transfer characteristics by first-principle calculations. 3D MAPbI₃ perovskite have two kinds of contacting interface, *i.e.*, PbI interface and I interface. The 2D/3D interface heterostructures are van der Waals contacting, and their light absorption can be enhanced as compared to pure 2D or 3D perovskite, mainly resulting from 3D perovskite part in the heterostructure. In 2D/I interface heterostructure, the band gap is 1.15 eV, and the charge recombination center is at 2D BA₂PbI₄ interface, which favor to improve the power conversion efficiency (PCE). While in 2D/PbI heterostructure, the band gap is as small as 0.53 eV, and the charge recombination center is at PbI interface, leading to a large number of recombination and low PCE. The work function difference of 2D BA₂PbI₄ and 3D MAPbI₃ is the nature of energy level shifting and interface charge oriented movement. These results demonstrate that the construction of 2D BA₂PbI₄ and 3D I interface heterostructure by interfacial engineering is a potential strategy to enhance the performance of the 2D/3D heterostructured PSCs.

---

### 1. Introduction

Organic-inorganic metal halide hybrid perovskites are the most promising photovoltaic materials due to their unique electrical and optical properties, such as long-range balanced charge-carrier diffusion length, high absorption coefficient, low density of deep trap state, small exciton binding energy and high charge-carrier mobility [1–8]. Their general formula is ABX₃ [A = MA(= CH₃NH₃) or FA (= CH₃(NH₂)₃); B = Pb, Ge or Sn; X = I, Br or Cl]. A certified power conversion efficiency (PCE) of perovskite solar cells (PSCs) has reached 23.7% [9]. However, perovskite thin films are quite sensitive to the moisture and oxygen, resulting in the obvious degradation under atmosphere, and the long-term stability issue is a major bottleneck for their further commercialization applications [10–12].

The layered two-dimensional (2D) perovskite materials have demonstrated much better stability than three-dimensional (3D) organic-inorganic metal halide hybrid perovskites [13–15]. The crystallinity of perovskite can be reduced from 3D to 2D depending on the introduction of long organic cation chains. 2D perovskites have a typical structural formula of M₂BX₄, where M is long-chain organic cation such as butylammonium (BA), phenyl ethylammonium (PEA), polyethylenimine (PEI), cyclopropylamine (CA) octadecylamine (OA) [16]. *Karunadasa et al.* reported that the 2D (PEA)₂(MA)₂Pb₃I₁₀ perovskite thin film maintained stable up to approximately 40 days under a relative humidity level of 52% [17]. Similarly, *Kanatzidis et al.* synthetized 2D (CH₃(CH₂)₃NH₃)₂(CH₃NH₃)ₙ₋₁PbₙI₃ₙ₊₁ (n = 1, 2, 3, and 4) perovskite thin films and they could remain unchanged after 2 months as exposed under a 40% humidity condition [18]. However, photovoltaic properties of 2D perovskites in PSCs are restricted by their wide band gap and low carrier mobility, resulting in a relatively low efficiency (PCE ≤ 15.4%) [19].

The construction of heterostructures, especially van der Waals (vdW) heterostructures, is a feasible way for high performance electronic devices, which can not only combine the advantages of each part but also create new functions [20–22]. In experiment, *Wu et al.* fabricated heterostructural photodetectors with MAPbI₃ perovskite films and WS₂ monolayers [23], and the devices exhibited high on/off ratios

---

* Corresponding author.
** Corresponding author.
E-mail addresses: ding@nanoctr.cn (L. Ding), junliang.yang@csu.edu.cn (J. Yang).

https://doi.org/10.1016/j.nanoen.2019.02.069
Received 18 January 2019; Received in revised form 24 February 2019; Accepted 27 February 2019
Available online 04 March 2019
2211-2855/ © 2019 Elsevier Ltd. All rights reserved.

![](./images/812797158188122113_1.jpg)
![](./images/812797158188122113_2.jpg)
![](./images/812797158188122113_3.jpg)

$(\approx 10^{5})$ and high responsivity $(\approx 17\ \text{A}\ \text{W}^{-1})$. The response speed of the hybrid $\text{WS}_{2}$/perovskite photoconductor was enhanced by four orders of magnitude as compared to the reference only perovskite device. In theory, *Yang et al.* reported the 2D vdW heterostructures constructed via $\text{BA}_{2}\text{XBr}_{4}$ (X = Pb, Sn, and Ge) perovskite and black phosphorus (BP) [24], in which the $\text{BA}_{2}\text{SnBr}_{4}$-BP and $\text{BA}_{2}\text{GeBr}_{4}$-BP heterostructures were type-II band arrangement, but the $\text{BA}_{2}\text{PbBr}_{4}$-BP heterostructure was type-I band arrangement. Furthermore, interface engineering plays an important role in the improvement of performance in the hetero-structure. The interfacial contacting has great influence on the electronic property in the whole heterostructure. For example, *Wei et al.* introduced a simple planar graphene/$\text{MAPbI}_{3}$ interface model, where graphene could be p-type or n-type doped by combining with different exposed surfaces of $\text{MAPbI}_{3}$ [25].

More importantly, the construction of 2D/3D perovskite hetero-structure has been proved to be an excellent route to improve the efficiency and stability of PSC [6,26,27]. *Zhang et al.* fabricated the 2D $\text{MA}_{3}\text{Bi}_{2}\text{I}_{9}$/3D $\text{MAPbI}_{3}$ heterostructured perovskites with remarkably reduced hysteresis and significantly improved stability, as well as the highest PCE up to 18.97% [28]. *Leong et al.* fabricated the 2D/3D $(\text{AVA})_{2}\text{PbI}_{4}$/$\text{MAPbI}_{3}$ perovskite heterostructure with significantly enhanced device stability and the PCE was as high as 18.0% [29]. However, the interfacial interaction and interface electronic transport mechanism is not fully understood in the 2D/3D perovskites heterostructure, which is directly related to the photovoltaic performance of PSCs.

Herein, 2D $\text{BA}_{2}\text{PbI}_{4}$/3D $\text{MAPbI}_{3}$ heterostructures have been constructed to study interfacial electrical properties and charge transfer characteristics by density functional theory. There are two kinds of contacting interface, *i.e.*, I interface and PbI interface in the 3D $\text{MAPbI}_{3}$ perovskite. Thus, the 2D/PbI and 2D/I interface heterostructures are constructed. The results show that the band gap of 2D/I interface heterostructure is 1.15 eV, which is beneficial for high performance PSC. But, the band gap of 2D/PbI interface heterostructure is as small as 0.53 eV that a large number of electrons and holes will be recombined in the interface. The oriented movement of interface charges is ascribed to the work function difference of 2D $\text{BA}_{2}\text{PbI}_{4}$ and 3D $\text{MAPbI}_{3}$ perovskites. Our results would contribute to the further performance improvement of 2D/3D perovskite heterostructural PSCs.

### 2. Computational method

Density functional theory (DFT) calculations are performed using the projector-augmented wave method, as implemented in the Vienna Ab initio Simulation Package (VASP) code [30]. The calculations are employed the generalized gradient approximation of Perdew-Burke-Ernzerh (PBE) exchange correlation functional. The DFT-D3 method of Grimme is applied to correct the vdW interaction [31]. The cutoff energy for the plane-wave basis set is set to 400 eV. A $4\times4\times1$ k-point mesh is used for all relax and self-consistent calculations, which is generated by Monkhorst-Pack scheme. The structure is fully relaxed and convergence until the total force on each atom is less than $0.02\ \text{eV}\ \mathring{\text{A}}^{-1}$ and the energy convergence threshold on each atom are less than $1\times10^{-4}\ \text{eV}$. To avoid the interaction between neighboring slabs, a vacuum space is set to $15\ \mathring{\text{A}}$, showed in Fig. 1. The absorption spectra are calculated by the following formula [32,33]:

$$
\alpha = (\sqrt{2})\omega\left[\sqrt{\varepsilon_{1}(\omega)^{2}+\varepsilon_{2}(\omega)^{2}}-\varepsilon_{1}(\omega)\right]^{1/2} \tag{1}
$$

where $\varepsilon_{2}(\omega)$ and $\varepsilon_{1}(\omega)$ are the imaginary and real parts of the dielectric function.

### 3. Results and discussions

The relaxed lattice parameters of 2D $\text{BA}_{2}\text{PbI}_{4}$ and 3D $\text{MAPbI}_{3}$ are listed in Table S1 that agree well with experimental parameters [34,35]. The unit cell of the heterostructure consists of $1\times1$ $\text{BA}_{2}\text{PbI}_{4}$ and $1\times1$ ![](./images/812797158188122113_4.jpg)

Fig. 1. Side view of 2D $\text{BA}_{2}\text{PbI}_{4}$/3D $\text{MAPbI}_{3}$ heterostructure with PbI interface (a) and I interface (b). $l_{1}$ and $l_{2}$ are the vertical interlayer distances of 2D-PbI interface and 2D-I interface.

$\text{MAPbI}_{3}$ and the lattice parameters of the heterostructure used the average values of the 2D and 3D perovskites, where the absolute strain of the 2D/3D heterostructure is 1.52%. Three layers thickness of 3D $\text{MAPbI}_{3}$ that including two kinds of interface are applied in the heterostructure that has similar performances with bulk material [36]. The monolayer 2D $\text{BA}_{2}\text{PbI}_{4}$ nanoplate is used. Fig. 1 shows the two contacting interface of 2D/3D heterostructure diagrams. The vertical interlayer distances between the 2D and 3D perovskites in the heterostructure intuitively associate with interfacial interaction. The vertical interlayer distances ($l_{1}$:2D-PbI interface, $l_{2}$:2D-I interface) can be calculated from the minimized interface formation energies [20,24]. Interface formation energy can be calculated by the following formula [37]:

$$
\Delta E = \frac{E_{2D}+E_{3D}-E_{2D/3D}}{S} \tag{2}
$$

where $S$ is the area of the interface, $E_{2D/3D}$, $E_{2D}$ and $E_{3D}$ represent the total energy of the heterostructure, the 2D perovskite monolayer and the 3D perovskite slab in the heterostructure lattices, respectively. The minimized interface formation energy in the 2D/PbI interface and 2D/I interface heterostructure are $2.00\ \text{meV}/\mathring{\text{A}}^{2}$ and $5.20\ \text{meV}/\mathring{\text{A}}^{2}$, respectively. These results suggest that 2D/I interface heterostructure is more likely to be formed. The interface formation energies of these two interfacial heterostructures are both positive and small, indicating that the heterostructures are more stable and easy to prepare. The calculated vertical interlayer distances are $l_{1}=2.89\ \mathring{\text{A}}$ and $l_{2}=3.16\ \mathring{\text{A}}$, respectively, which are obviously longer than the bond length of C-H ($\sim1.1\ \mathring{\text{A}}$) and N-H ($\sim1.0\ \mathring{\text{A}}$) bond length. The results reveal that the 2D and 3D perovskite are connected by weak van der Waals force (vdW) in the heterostructure. In the vdW heterostructure, the excellent properties of the 2D and 3D perovskite can be preserved [24].

The band gaps of the 2D, 3D perovskite and the heterostructures are calculated by PBE functional and Heyd, Scuseria, and Ernzerhof (HSE06) with spin-orbit coupling (SOC) functional for comparison. The results are shown in Table 1. The band gaps of the 2D and 3D perovskite are not much difference between the two functional and consistent with

<table><caption>Table 1 Calculated band gaps (in eV) of 2D BA₂PbI₄, 3D PbI and I interface and their heterostructures in pre-contact and contact states by PBE and HSE06 + SOC functional, respectively.</caption>
<thead>
<tr>
<th>Functional</th>
<th>Her.</th>
<th colspan="2">Pre-contact</th>
<th colspan="2">Contact</th>
<th>Her.</th>
</tr>
<tr>
<th></th>
<th></th>
<th>2D</th>
<th>3D</th>
<th>2D</th>
<th>3D</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">PBE</td>
<td>2D/PbI</td>
<td>2.15</td>
<td>1.70</td>
<td>2.15</td>
<td>1.70</td>
<td>0.22</td>
</tr>
<tr>
<td>2D/I</td>
<td>2.13</td>
<td>1.66</td>
<td>2.15</td>
<td>1.79</td>
<td>1.73</td>
</tr>
<tr>
<td rowspan="2">HSE06 + SOC</td>
<td>2D/PbI</td>
<td>2.05</td>
<td>1.78</td>
<td>2.05</td>
<td>1.80</td>
<td>0.53</td>
</tr>
<tr>
<td>2D/I</td>
<td>2.03</td>
<td>1.60</td>
<td>2.05</td>
<td>1.60</td>
<td>1.15</td>
</tr>
</tbody>
</table>

the experimental data [38,39]. The HSE06 functional overestimates the band gaps of the perovskites and the SOC effect underestimates the band gaps. The band gaps by PBE functional can agree well with the experimental band gaps due to fortuitously error-error cancellation. In general, in order to study the accurate electronic characteristics of halide perovskites, especially Pb-based perovskites, the SOC effect cannot be neglected [16]. Therefore, the more accurate functional (HSE06 + SOC) are mainly used to calculate the band gaps and energy levels of the 2D/3D heterostructure.

The optical properties are calculated by equation (1). The absorption spectrum is qualitatively studied using PBE functional. Both of the optical absorption coefficients of 2D BA₂PbI₄ monolayer, 3D MAPbI₃ and the heterostructures are showed in Fig. 2. The 2D/3D heterostructures have more superior optical absorption than the 2D and 3D single component perovskite, which proves that the constructed 2D/3D heterostructures can potentially improve the performance of the PSC. The absorption coefficient of 3D MAPbI₃ interface is obviously higher than 2D BA₂PbI₄ monolayer. Therefore, the 3D MAPbI₃ interface plays a major role in the light absorption in the 2D/3D heterostructures.

The energy level arrangement has great significance to the carrier migration in the perovskite heterostructure. The energy levels of 2D BA₂PbI₄ monolayer perovskite and 3D MAPbI₃ perovskite including PbI and I interface in pre-contact and contact states are both studied by the HSE06 + SOC functional. Fig. 3 shows the energy level arrangement diagrams. The vacuum levels are set to 0 in pre-contact state. The Fermi levels are set to 0 in contact state. Overall, the 2D/3D heterostructures are the type-II band arrangement. Electrons flow from 2D BA₂PbI₄ to 3D MAPbI₃ perovskite and the holes flow from 3D MAPbI₃ to 2D BA₂PbI₄ perovskite. However, the details of the energy level arrangement are very different in the 2D/PbI interface and 2D/I interface heterostructures. Firstly, the work functions of 2D, PbI interface and I interface perovskites are analyzed. The work function indicates the ability to bind electrons and can be calculated by the difference of vacuum level and Fermi level. The calculated work function by PBE and HSE06 + SOC functional of the 2D and 3D perovskite in the heterostructure lattices are showed in Table S2. The results calculated by PBE and HSE06 + SOC functional are little difference. The work functions of 3D MAPbI₃ of PbI and I interface are greater than 2D BA₂PbI₄ monolayer. The values of PbI interface are greater than I interface in the 3D MAPbI₃. Then, the carrier transfer characteristics from pre-contact state to contact state in the whole heterostructures are analyzed. The red dotted lines represent Fermi levels in Fig. 3(a) and (b). The 2D BA₂PbI₄ monolayer, PbI and I interface perovskite are p-type semiconductor characteristics. Becasue the work function of PbI interface is much bigger than 2D BA₂PbI₄ monolayer, the PbI interface binds a large number of electrons. The electrons are mainly derived from 2D BA₂PbI₄ monolayer. The electric potential of 2D BA₂PbI₄ monolayer increase, and it decreases in the PbI interface. Therefore, the Fermi level of 2D BA₂PbI₄ monolayer is reduced and it raises in the PbI interface after contacting. In the I interface and 2D BA₂PbI₄ pre-contact state, there are small amount of electrons transfer, because of the small difference in the work function of 2D BA₂PbI₄ and I interface. Their Fermi levels move weakly. In the contact state, the part of PbI interface shows n-type semiconductor characteristics in the 2D/PbI heterostructure. In addition, the interface carriers' moving will result in interfacial band bending. The band bending diagram is shown in Figure S2.

![](./images/812797158188122113_5.jpg)

Fig. 2. (a) The absorption spectra of the 2D BA₂PbI₄ monolayer, 3D PbI interface and their heterostructure, respectively. (b) The absorption spectra of the 2D BA₂PbI₄ monolayer, 3D I interface and their heterostructure, respectively.

In order to maintain electrical neutrality of the 2D/PbI heterostructure system, a large space charge region is formed at the contacting interface. Thus, there is a built-in electric field in the space charge region. As the 2D/PbI heterostructural PSCs under the light, a large number of photogenerated electrons and holes are recombined in the built-in electric field. In addition, the band gap of the 2D/PbI heterostructure is 0.53 eV, which is disadvantage to the carrier separation as well. On the other hand, in the 2D/I heterostructure, the built-in electric field is relatively small and the band gap is 1.15 eV, which is more suitable for the carrier separation. For the comparation of the calculation, the energy level arrangement diagrams by PBE functional are also calculated, as showed in Figure S1. The results are consistent with the HSE06 + SOC functional. Therefore, the 2D/PbI heterostructure is not suited to PSC devices, while the 2D/I heterostructure is a good choice for highly efficient and stable PSC devices.

The 3D charge density difference (CDD) can intuitively illustrate the detailed nature of the charge transferring at the 2D/3D heterostructure interface. That is calculated by the following formula [40]:

$$\Delta \rho=\rho_{2 D / 3 D}-\rho_{2 D}-\rho_{3 D} \tag{3}$$

where $\rho_{2D/3D}$, $\rho_{2D}$ and $\rho_{3D}$ represent the charge density of the heterostructure, the 2D perovskite monolayer and the 3D perovskite slab in the heterostructure lattices, respectively. The calculated 3D CDD of the 2D/PbI interface and 2D/I interface heterostructure is showed in Fig. 4(a) and (b). The red cloud is electron accumulation and the yellow cloud is electron depletion. The amount of the charge transfer is very large in the 2D/PbI interface heterostructure while the amount of the charge transfer is relatively small in the 2D/I interface, which is consistent with the previous analysis. At the thermal equilibrium status, the Fermi level difference will drive electrons from 2D to 3D system. A built-in electric field is formed in the heterojunction, unfortunately, the built-in electric field is not favorable for solar cell applications. The built-in electric field will drive photoelectrons from 3D to 2D system. Due to the interfacial barrier of the heterojunction, the electrons cannot move to 2D system but accumulate at the interface. Similarly, the holes also accumulate at the interface. As a result, the recombination of the accumulated photocarriers is huge at the interface. The locations of the recombination center in the two kinds of 2D/3D heterostructures attract attention. In fact, the net charge transfer region is the recombination center, as showed in Fig. 4. The net charge transfer mainly occurs in the surface of 3D MAPbI₃ in the 2D/PbI interface heterostructure. A large number of positive and negative charges gather in the

![](./images/812797158188122113_6.jpg)

Fig. 3. (a-b) and (c-d) are the energy level diagrams of 2D/PbI interface and 2D/I interface in pre-contact state and contact state. The contact state is an equilibrium state. The values for the conduction band minimum and the valence band maximum are listed in the rectangles. The red dotted lines represent Fermi levels. The vacuum levels are set to 0 in pre-contact state. The Fermi levels are set to 0 in contact state. (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

![](./images/812797158188122113_7.jpg)

Fig. 4. (a) and (b) represent 3D charge density difference (CDD) for 2D/PbI and 2D/I heterostructure, respectively (thermal equilibrium status, side views). The red cloud stands for electron accumulation and the yellow cloud for electron depletion. The black dotted circles stand for the recombination centers. The value of the isosurface is $2 \times 10^{-3}\ \text{e}/\text{\AA}^3$. (c) and (d) are the diagrams for photocarrier separation (non-equilibrium status under light illumination). The red and blue balls represent the photogenerated holes and electrons, respectively. The photocarriers are dense in 3D MAPbI₃ and loose in 2D BA₂PbI₄. The red dotted rectangles represent the recombination centers, where the photogenerated holes and electrons are annihilated. (For interpretation of the references to colour in this figure legend, the reader is referred to the Web version of this article.)

3D MAPbI₃ interface. In the 2D/3D heterostructure device, the 3D perovskite is responsible for improving efficiency and the photocarriers is dense in 3D MAPbI₃ and loose in 2D BA₂PbI₄. When putting the heterostructure device under light, a mess of photocarriers in the 3D MAPbI₃ could recombine in the recombination center, resulting in low PCE for 2D/PbI heterostructured PSCs. The schematic diagram is shown in Fig. 4(c) and the red dotted rectangles are the recombination centers. However, in the 2D/I interface heterostructure, the charge transfer mainly occurs in the surface of 2D BA₂PbI₄ monolayer. A small amount of photovoltaic carriers in the 2D BA₂PbI₄ monolayer will be recombined in the surface and more photovoltaic carriers in the 3D MAPbI₃ can be separation and transport in the 2D/I interface heterostructure device under the light. The schematic diagram is showed in Fig. 4(d). Therefore, the 2D/I interface heterostructure is more suitable for fabricating 2D/3D heterostructured PSCs.

## 4. Conclusions
The structural and electronic properties of the 2D/PbI and 2D/I vdW heterostructure have been studied by density functional theory. The I interface contacting is more stable than the PbI interface contacting in the BA₂PbI₄/MAPbI₃ heterostructure. The light absorption of the 2D/3D heterostructure is higher than 2D BA₂PbI₄ monolayer and 3D MAPbI₃. Although the 2D/PbI and 2D/I interface heterostructure are both type-II band arrangement, the band gap of 2D/PbI heterostructure is too small to favor the carrier separation. Furthermore, the charge recombination center is mainly located in the 3D MAPbI₃ part in the 2D/PbI interface heterostructure. While in the 2D/I interface heterostructure, the charge recombination center is located in the 2D BA₂PbI₄ part, which does not affect the majority carrier separation. Therefore, constructing 2D BA₂PbI₄ and 3D I interface heterostructure by interfacial engineering is a potential strategy to enhance the stability and PCE of the 2D/3D heterostructured PSCs.

## Acknowledgments
This work was supported by the National Key Research and Development Program of China (2017YFA0206600), the National Natural Science Foundation of China (51673214 and 51773045), the China Postdoctoral Science Foundation (2017M622599), and the Key Projects of Hunan Provincial Science and Technology Plan (2017GK2231).

## Appendix A. Supplementary data
There are two Figure and two Tables in Supplementary Material. Figure S1 illustrates energy level diagrams of 2D/PbI and 2D/I

heterostructure by PBE functional. Figure S2 illustrates the band bending diagram of 2D $BA_2PbI_4$/3D $MAPbI_3$ heterostructure. Table S1 is the relaxed lattice parameters of 2D $BA_2PbI_4$ monolayer and 3D $MAPbI_3$ bulk. Table S2 is the work function of 2D $BA_2PbI_4$, 3D PbI and I interface in their heterostructure lattices by PBE and HSE06 + SOC functional, respectively.

Supplementary data to this article can be found online at https://doi.org/10.1016/j.nanoen.2019.02.069.

### References

[1] A. Kojima, K. Teshima, Y. Shirai, T. Miyasaka, Organometal halide perovskites as visible-light sensitizers for photovoltaic cells, J. Am. Chem. Soc. 131 (2009) 6050-6051.

[2] C.T. Zuo, L.M. Ding, Lead-free perovskite materials $(NH_4)_3Sb_2I_xBr_{9-x}$, Angew. Chem. Int. Ed. 56 (2017) 6528-6532.

[3] W.S. Yang, J.H. Noh, N.J. Jeon, Y.C. Kim, S. Ryu, J. Seo, S.I. Seok, High-performance photovoltaic perovskite layers fabricated through intramolecular exchange, Science 348 (2015) 1234-1237.

[4] C.T. Zuo, D. Vak, D. Angmo, L.M. Ding, M. Gao, One-step roll-to-roll air processed high efficiency perovskite solar cells, Nanomater. Energy 46 (2018) 185-192.

[5] B. Liu, M.Q. Long, M.Q. Cai, J.L. Yang, Influence of the number of layers on ultrathin $CsSnI_3$ perovskite: from electronic structure to carrier mobility, J. Phys. D Appl. Phys. 51 (2018) 105101.

[6] P. Li, Y. Zhang, C. Liang, G. Xing, X. Liu, F. Li, X. Liu, X. Hu, G. Shao, Y. Song, Phase pure 2D perovskite for high-performance 2D-3D heterostructured perovskite solar cells, Adv. Mater. 30 (2018) 1805323.

[7] C.T. Zuo, H.J. Bolink, H.W. Han, J.S. Huang, D. Cahen, L.M. Ding, Advances in perovskite solar cells, Adv. Sci. 3 (2016) 1500324.

[8] Z.M. Fang, S.Z. Wang, S.F. Yang, L.M. Ding, $CsAg_2Sb_2I_9$ solar cells, Inorg. Chem. Front. 5 (2018) 1690-1693.

[9] NREL, https://www.nrel.gov/pv/assets/images/efficiency-chart.png.

[10] J. Xiong, B.C. Yang, C.H. Cao, R.S. Wu, Y.L. Huang, J. Sun, J. Zhang, C.B. Liu, S.H. Tao, Y.L. Gao, J.L. Yang, Interface degradation of perovskite solar cells and its modification using an annealing-free $TiO_2$ NPs layer, Org. Electron. 30 (2016) 30-35.

[11] R.J. Sutton, G.E. Eperon, L. Miranda, S.A. Parrott, B.A. Kamino, J.B. Patel, M.T. Hörantner, M.B. Johnston, A.A. Haghighirad, D.T. Moore, Bandgap-tunable cesium lead halide perovskites with high thermal stability for efficient solar cells, Adv. Energy Mater. 6 (2016) 1502458.

[12] A.M. Ganose, C.N. Savory, D.O. Scanlon, Beyond methylammonium lead iodide: prospects for the emergent field of $ns^2$ containing solar absorbers, Chem. Commun. 53 (2017) 20-44.

[13] L. Qian, Y.L. Sun, M.M. Wu, C. Li, D. Xie, L.M. Ding, G.Q. Shi, A lead-free two-dimensional perovskite for a high-performance flexible photoconductor and a light-stimulated synaptic device, Nanoscale 10 (2018) 6837-6843.

[14] J.-W. Lee, Z. Dai, T.-H. Han, C. Choi, S.-Y. Chang, S.-J. Lee, N. De Marco, H. Zhao, P. Sun, Y. Huang, 2D perovskite stabilized phase-pure formamidinium perovskite solar cells, Nat. Commun. 9 (2018) 3021.

[15] C. Zuo, A.D. Scully, D. Vak, W. Tan, X. Jiao, C.R. McNeill, D. Angmo, L. Ding, M. Gao, Self-assembled 2D perovskite layers for efficient printable solar cells, Adv. Energy Mater 9 (2018) 1803258.

[16] L. Ma, J. Dai, X.C. Zeng, Two-dimensional single-layer organic-inorganic hybrid perovskite semiconductors, Adv. Energy Mater. 7 (2017) 1601731.

[17] I.C. Smith, E.T. Hoke, D. Solis-Ibarra, M.D. McGehee, H.I. Karunadasa, Angew. Chem. Int. Ed. 53 (2014) 11232-11235.

[18] D.H. Cao, C.C. Stoumpos, O.K. Farha, J.T. Hupp, M.G. Kanatzidis, 2D homologous perovskites as light-absorbing materials for solar cell applications, J. Am. Chem. Soc. 137 (2015) 7843-7850.

[19] H.T. Lai, B. Kan, T.T. Liu, N. Zheng, Z.Q. Xie, T. Zhou, X.J. Wan, X.D. Zhang, Y.S. Liu, Y.S. Chen, Two-dimensional Ruddlesden−Popper perovskite with nanorodlike morphology for solar cells with efficiency exceeding 15%, J. Am. Chem. Soc. 140 (2018) 11639-11646.

[20] B. Liu, M.Q. Long, M.Q. Cai, J.L. Yang, Interface engineering of $CsPbI_3$-black phosphorus van der Waals heterostructure, Appl. Phys. Lett. 112 (2018) 043901.

[21] B.W.H. Baugher, H.O.H. Churchill, Y.F. Yang, P. Jarillo-Herrero, Optoelectronic devices based on electrically tunable p-n Diodes in a monolayer dichalcogenide, Nat. Nanotechnol. 9 (2014) 262-267.

[22] B. Liu, M. Long, M.-Q. Cai, J. Yang, Ferroelectric polarization in $CsPbI_3/CsSnI_3$ perovskite heterostructure, J. Phys. Chem. C 122 (2018) 17820-17824.

[23] C. Ma, Y.M. Shi, W.J. Hu, M.H. Chiu, Z.X. Liu, A. F. Li, H. Wang, L.J. Li, T. Wu, Heterostructured $WS_2/CH_3NH_3PbI_3$ photoconductors with suppressed Dark current and enhanced photodetectivity, Adv. Mater. 28 (2016) 3683-3689.

[24] B. Liu, M. Long, M.-Q. Cai, J. Yang, Two-dimensional van der Waals heterostructures constructed via perovskite $(C_4H_9NH_3)_2XBr_4$ and black phosphorus, J. Phys. Chem. Lett. 9 (2018) 4822-4827.

[25] Y.H. Cao, Z.Y. Deng, M.Z. Wang, J.T. Bai, S.H. Wei, H.J. Feng, Interface engineering of graphene/$CH_3NH_3PbI_3$ heterostructure for novel p-i-n structural perovskites solar cells, J. Phys. Chem C 122 (2018) 17228-17237.

[26] K. Wei, T. Jiang, Z. Xu, J. Zhou, J. You, Y. Tang, H. Li, R. Chen, X. Zheng, S. Wang, Ultrafast carrier transfer promoted by interlayer Coulomb coupling in 2D/3D perovskite heterostructures, Laser Photon. Rev. 12 (2018) 1800128.

[27] M.H. Li, H.H. Yeh, Y.H. Chiang, U.S. Jeng, C.J. Su, H.W. Shiu, Y.J. Hsu, N. Kosugi, T. Ohigashi, Y.A. Chen, Highly efficient 2D/3D hybrid perovskite solar cells via low-pressure vapor-assisted solution process, Adv. Mater. 30 (2018) 1801401.

[28] Y. Hu, T. Qiu, F. Bai, W. Ruan, S. Zhang, Highly efficient and stable solar cells with 2D $MA_3Bi_2I_9$/3D $MAPbI_3$ heterostructured perovskites, Adv. Energy Mater. 8 (2018) 1703620.

[29] T. Ye, A. Bruno, G. Han, T.M. Koh, J. Li, N.F. Jamaludin, C. Soci, S.G. Mhaisalkar, W.L. Leong, Efficient and ambient-air-stable solar cell with highly oriented 2D@ 3D perovskites, Adv. Funct. Mater. 28 (2018) 1801654.

[30] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953.

[31] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758.

[32] Z.L. Yu, Q.R. Ma, Y.Q. Zhao, B. Liu, M.Q. Cai, Surface termination-A Key factor to influence electronic and optical properties of $CsSnI_3$, J. Phys. Chem. C 122 (2018) 9275-9282.

[33] Y.Q. Zhao, Q.R. Ma, B. Liu, Z.L. Yu, J.L. Yang, M.Q. Cai, Layer-dependent transport and optoelectronic property in two-dimensional perovskite: $(PEA)_2PbI_4$, Nanoscale 10 (2018) 8677-8688.

[34] D.B. Mitzi, Synthesis, crystal structure, and optical and thermal properties of $(C_4H_9NH_3)_2MI_4$ ($M = Ge, Sn, Pb$), Chem. Mater. 8 (1996) 791-800.

[35] A.I.M. Leguy, Y. Hu, M. Campoy-Quiles, M.I. Alonso, O.J. Weber, P. Azarhoosh, M. Van Schilfgaarde, M.T. Weller, T. Bein, J. Nelson, Reversible hydration of $CH_3NH_3PbI_3$ in films, single crystals, and solar cells, Chem. Mater. 27 (2015) 3397-3407.

[36] L. Zhang, W.Z. Liang, How the structures and properties of two-dimensional layered perovskites $MAPbI_3$ and $CsPbI_3$ vary with the number of layers, J. Phys. Chem. Lett. 8 (2017) 1517-1523.

[37] Y.D. Zhou, Q.L. Liu, C. Yang, Z.Y. Zhao, Interfacial micro-structure and properties of $TiO_2/SnO_2$ heterostructures with rutile phase: a DFT calculation investigation, Appl. Surf. Sci. 451 (2018) 258-271.

[38] A. Amat, E. Mosconi, E. Ronca, C. Quarti, P. Umari, M.K. Nazeeruddin, M. Gratzel, F. De Angelis, Cation-induced band-gap tuning in organohalide perovskites: interplay of spin-orbit coupling and octahedra tilting, Nano Lett. 14 (2014) 3608-3616.

[39] T. Sheikh, A. Shinde, S. Mahamuni, A. Nag, Possible dual bandgap in $(C_4H_9NH_3)_2PbI_4$ 2D layered perovskite: single crystal and exfoliated few-layer, ACS Energy Lett 3 (2018) 2940-2946.

[40] B. Liu, Y.-Q. Zhao, Z.-L. Yu, L.-Z. Wang, M.-Q. Cai, Tuning the Schottky rectification in graphene-hexagonal boron nitride-molybdenum Disulfide heterostructure, J. Colloid Interface Sci. 513 (2017) 677-683.

![](./images/812797158188122113_8.jpg)

Biao Liu received his PhD in School of Physics and Electronics Science at Hunan University in 2017 under the supervision of Prof. Mengqiu Cai. Now he is a postdoctor in Prof. Junliang Yang's group at Central South University. His current research focuses on first-principle simulation and design of perovskite heterostructure.

![](./images/812797158188122113_9.jpg)

Mengqiu Long obtained his PhD in physics at Hunan University in 2008. He did his postdoctoral research at Tsinghua University on the charge transport properties of carbon materials with Professor Zhigang Shuai. In 2010, he joined the faculty of School of Physics and Electronics, Central South University, and now he is a professor. His research focuses on theoretical modeling of nanomaterials and molecular devices, electronic structure, electronic transport properties and spintronics of 2D materials, and he has published more than 100 papers in peer-reviewed journals.

![](./images/812797158188122113_10.jpg)

Mengqiu Cai received his PhD from National Laboratory of Solid State Microstructures and Department of Physics at Nanjing University in 2005. He then worked for two years as a postdoctor at Zhongshan University. In 2008, he moved to Hong Kong Polytechnic University as a visiting scientist. He was appointed as a full professor in School of Physics and Electronics Science at Hunan University in 2008. His research focuses on theoretical modeling of perovskite materials and 2D materials.

![](./images/812797158188122113_11.jpg)

Liming Ding got PhD from University of Science and Technology of China. He started his research on OSCs and PLEDs in Olle Inganäs Lab in 1998. Later on, he worked with Frank Karasz and Tom Russell at PSE, UMASS Amherst. He joined Konarka as a Senior Scientist in 2008. In 2010, he joined National Center for Nanoscience and Technology as a Full Professor. Currently, his work focuses on perovskite solar cells and BHJ solar cells.

![](./images/812797158188122113_12.jpg)

Junliang Yang received his PhD in 2008 from State Key Laboratory of Polymer Physics and Chemistry at Changchun Institute of Applied Chemistry. He then worked as a post-doctor at University of Warwick. In April 2011, he moved to Australia as a research fellow at University of Melbourne and as a visiting scientist in Flexible Electronics Laboratory at CSIRO. In March 2012, he was appointed as a full professor in School of Physics and Electronics at Central South University. His research interests cover solar cells, flexible electronics and printed electronics.