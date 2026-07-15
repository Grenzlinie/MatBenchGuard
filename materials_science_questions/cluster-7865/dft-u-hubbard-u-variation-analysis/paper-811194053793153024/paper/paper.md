PAPER
View Article Online
View Journal | View Issue

![](./images/811194053793153024_1.jpg)

Cite this: Phys. Chem. Chem. Phys.,
2016, 18, 22154

Received 19th April 2016,
Accepted 14th July 2016

DOI: 10.1039/c6cp02617f

www.rsc.org/pccp

# Band inversion and topological aspects in a TiNI monolayer

Aizhu Wang, $^{ab}$ Zhenhai Wang, $^{cd}$ Aijun Du $^{*b}$ and Mingwen Zhao $^{*a}$

To achieve a device application of the quantum spin Hall (QSH) effect, increasing the critical temperature is crucial. A two-dimensional topological insulator (2D-TI) with a sizeable bulk band gap is one of the most promising strategies to reach this goal. Using first-principles calculations, we propose a new 2D-TI, titanium nitride iodide (TiNI) monolayer, which can be exfoliated from a bulk TiNI crystal, thanks to the weak interlayer interaction. We demonstrate that the TiNI monolayer has an inverted band structure accompanied by topologically nontrivial states characterized by a topological invariant of $Z_{2}=1$. The band gap (~50 meV) opened due to spin-orbit coupling (SOC) is available for achieving the QSH effect at room temperature. The band inversion and topologically nontrivial states are robust under external strain, suggesting that the 2D TiNI monolayer lattice could be a versatile platform for hosting nontrivial topological states with potential applications in 2D spintronics and computer technology.

## Introduction

With continuous miniaturization of electronic devices, the quantum size effect becomes more and more significant. $^{1}$ Graphene, a typical two-dimensional (2D) carbon material with single atomic thickness, exhibits a number of unusual electronic and spintronic properties. $^{2}$ Inspired by the successful preparation of graphene, $^{3}$ considerable efforts have been devoted to searching for new 2D materials, which are expected to play important roles in device applications. Until now, a large number of 2D materials have been proposed, including carbon allotropes, $^{4-7}$ carbon nitrides, $^{8-10}$ group IV elements/ compounds, $^{11-15}$ III-V elements/compounds $^{16-19}$ and so forth. Interestingly, some of them have hexagonal symmetry like graphene, while others have rectangular symmetry. Though the subsequent research of new 2D materials extends to organometallic frameworks $^{20-22}$ or transition metal dichalcogenides, $^{23,24}$ few of them have been experimentally verified, due to difficulties in synthesis.

Graphene's effectively massless state of charge carriers is closely related to the linear dispersion characterized by Dirac cones. Nevertheless, the lack of a band gap limits the on-off current ratio in planar field-effect transistors, and it is difficult to reliably achieve a sizable band gap without degrading its electronic quality. $^{25}$ Another interesting phenomenon accompanied by Dirac cones in graphene is that a topological nontrivial band gap can be opened up at the Dirac point due to spin-orbit coupling (SOC), which is implementable for achieving the quantum spin Hall (QSH) effect. Though intrinsic graphene has very weak SOC to generate an experimentally detectable band gap, $^{4,8,26}$ the work of Kou et al. showed that heterostructures can significantly increase its nontrivial gap and quantum spin Hall (QSH) effect, so that it can be used in room temperature environments. $^{27,28}$ Therefore, searching for a 2D material with a widely tuneable band gap and strong SOC becomes highly desirable from the perspective of developing realistic applications.

Recently, a new class of layered transition metal nitride halides (MNX, M = Zr, Hf, Ti; X = Cl, Br, I) has been experimentally fabricated. $^{29}$ MNX has two polytypes: $\alpha$-polymorphs (space group $D_{2h}^{13}$) with a layered structure $^{30,31}$ and $\beta$-polymorphs. In $\alpha$-polymorphs each M atom is coordinated with four N atoms and two X atoms, as shown in Fig. 1(a), while in $\beta$-polymorphs the M atom is coordinated with four N atoms and three X atoms. These two polytypes exist for all combinations of MNX (M = Zr, Hf; X = Cl, Br, I), but for titanium-based analogues TiNX (X = Cl, Br, I), only $\alpha$-polymorphs have been synthesized so far. $^{31}$ The layered structures of TiNX offer promising candidate materials for the development of 2D materials using exfoliation techniques. $^{32,33}$

Here, using first-principles calculations, we demonstrated that the TiNI monolayer exfoliated from the $\alpha$-TiNI crystal has intrinsic band-inverted states in its electronic structure. In contrast to graphene, the TiNI monolayer has a buckled rectangular lattice and distorted Dirac cones with highly anisotropic Fermi velocities. More importantly, the inverted states of the TiNI monolayer are

$^{a}$ School of Physics and State Key Laboratory of Crystal Materials, Shandong University, Jinan 250100, China. E-mail: zmw@sdu.edu.cn
$^{b}$ School of Chemistry, Physics and Mechanical Engineering, Queensland University of Technology, QLD 4001, Australia. E-mail: aijun.du@qut.edu.au
$^{c}$ Nanjing University of Posts and Telecommunications, Nanjing, 210003, China
$^{d}$ Department of Geosciences, Center for Materials by Design, and Institute for Advanced Computational Science, Stony Brook University, Stony Brook, NY 11794, USA

![](./images/811194053793153024_2.jpg)

Fig. 1 (a) Schematic illustration of the TiNI bulk crystal in FeOCl type is shown as a superlattice with a $D_{2h}^{13}$ space group. (b) Top and (c) side views of a TiNI monolayer. Phonon spectrum of the TiNI monolayer is shown in (d). The blue, gray, and purple balls represent titanium, nitrogen, and iodine atoms, respectively.

tuneable by applying external strain. For example, the band-inverted states are robust against compression along the $x$-axis and stretching along the $y$-axis, whereas a tuneable band gap is opened as a function of strain applied along opposite directions. SOC strength in the TiNI monolayer is more significant than that in graphene, leading to a sizeable topologically nontrivial band gap ($\sim$50 meV) at the Dirac points, which is quite promising for achieving the QSH effect at high temperature. The weak interlayer interaction in the $\alpha$-TiNI crystal facilitates the exfoliation, making the TiNI monolayer accessible in future experiments.

## Computational details

Our first-principles calculations were performed within the framework of density functional theory (DFT), as implemented in the Vienna $ab$ $initio$ Simulation Package (VASP).$^{34}$ Electron-electron interactions were treated within the generalized gradient approximation using the Perdew-Burke-Ernzerhof (PBE)$^{35}$ exchange-correlation functional. The energy cut off employed for the plane-wave expansion of the electron wavefunctions was set to be 520 eV and the electron-ion interaction was described by projector-augmented-wave (PAW)$^{36}$ potentials. The supercell was repeated periodically on the $x$-$y$ plane while a vacuum region of about $20$ Å was applied along the $z$-direction to avoid mirror interactions between neighbouring images. Brillouin-zone (BZ) integration was sampled on a grid of $31 \times 31 \times 1$ $k$-points and structural optimizations were carried out using a conjugate gradient (CG) method until the remaining force on each atom was less than $0.0005$ eV Å$^{-1}$. Our phonon spectrum was calculated using the Phononpy code,$^{37}$ interfaced with VASP. The optimized lattice constants ($a = 3.517$ Å, $b = 3.984$ Å, $c = 8.870$ Å) of the bulk $\alpha$-TiNI crystal obtained by using the above strategies are in good agreement with the experimental values ($a = 3.515$ Å, $b = 3.941$ Å, $c = 8.955$ Å) as shown in Table 1.$^{31}$

## Results and discussion

The TiNI monolayer obtained by exfoliating the bulk crystal is shown in Fig. 1(b) and (c). It has a buckled rectangular lattice with the lattice constants $a = 3.529$ Å, $b = 4.004$ Å, which are slightly larger than the corresponding values in the bulk crystal as shown in Table 1. Each Ti atom connects to four N atoms and two I atoms. The primitive cell consists of six atoms ($\text{Ti}_2\text{N}_2\text{I}_2$) with fourfold symmetry. The dynamical stability of the TiNI monolayer was confirmed by its phonon spectrum shown in Fig. 1(d). There are eighteen phonon dispersion bands corresponding to the total degrees of freedom of six atoms in a unit cell, and no imaginary frequency mode is found at any wave vectors.

<table>
<caption>Table 1 Lattice constants and distance between adjacent atoms of the bulk and TiNI monolayer obtained from first-principles calculations. The data from experiments are also presented for comparison</caption>
<thead>
<tr>
<th></th>
<th>$a$</th>
<th>$b$</th>
<th>$c$</th>
<th>N-N</th>
<th>Ti-Ti</th>
<th>I-I</th>
<th>Ti-N</th>
<th>N-I</th>
<th>Ti-I</th>
</tr>
</thead>
<tbody>
<tr>
<td>Exp$^{29,31}$</td>
<td>3.515</td>
<td>3.941</td>
<td>8.955</td>
<td>2.70</td>
<td>3.01</td>
<td>3.52</td>
<td>2.02</td>
<td>3.09</td>
<td>2.74</td>
</tr>
<tr>
<td>Bulk</td>
<td>3.517</td>
<td>3.984</td>
<td>8.870</td>
<td>2.74</td>
<td>3.00</td>
<td>3.64</td>
<td>2.02</td>
<td>3.22</td>
<td>2.83</td>
</tr>
<tr>
<td>Monolayer</td>
<td>3.529</td>
<td>4.004</td>
<td>—</td>
<td>2.76</td>
<td>2.99</td>
<td>3.53</td>
<td>2.03</td>
<td>3.24</td>
<td>2.84</td>
</tr>
</tbody>
</table>

![](./images/811194053793153024_3.jpg)

Fig. 2 (a) Schematic representation of the exfoliation process. (b) Energy increase $E$ (right blue) and its derivative $\sigma$ (left red) as a function of $D$.

Then, the possibility of producing TiNI monolayer using a mechanical exfoliation strategy was confirmed (Fig. 2(a)). The cleavage energy $E_{\text{cl}}$ is defined as the minimum energy required to exfoliate a monolayer from bulk.$^{38}$ We used a four-slab model to mimic a bulk material and calculated the energy increase as a monolayer is exfoliated from the slab. A vacuum layer at least 15 Å was incorporated into the four-layer slab to avoid the artificial interaction between two neighboring slabs. Fig. 2(b) gives the variation of energy (and its derivative) as a function of the interlayer distance ($D$) between the top most monolayer and the remnant trilayer, which was fixed during the exfoliation process. The calculated cleavage energy $E_{\text{cl}}$ of TiNI is about $0.22$ J m$^{-2}$. The cleavage strength ($\sigma$) was further obtained from the derivative of energy with respect to the distance. From Fig. 2(b), we can see that the cleavage strength is about 2.65 GPa. It is noteworthy that the calculated cleavage energy of TiNI is smaller than that of graphite ($0.37$ J m$^{-2}$),$^{39,40}$ suggesting high plausibility to extract a TiNI monolayer from the bulk in future experiments.

To obtain a free-standing membrane $via$ exfoliation, high in-plane stiffness is required to avoid curling. We first evaluated the

2D Young's modulus of the TiNI monolayer using the following equation:

$$
Y = \frac{1}{L_0 A} \frac{\partial^2 E}{\partial \varepsilon^2}
$$

where $E$ is the total energy per unit cell, and $L_0$, $A$ and $\varepsilon$ represent the lattice constant, surface area and axial strain, respectively. The calculated $Y$ is 0.2 TPa, which is about 20% of that of graphene.⁴¹ The in-plane stiffness was then evaluated from bending a square TiNI flake with one edge $L$ fixed. According to elastic theory, the out-of-plane deformation $h$ can be estimated by the expression $h/L \approx (\rho g L / Y)^{1/3}$, where $g$ and $\rho$ represent the gravitational acceleration and the density of the TiNI monolayer, respectively. For a large TiNI monolayer flake of length $L = 50$ μm, the ratio is $h/L \approx 10^{-4}$, implying that TiNI is strong enough to form a free-standing monolayer.

The electronic band structure of the TiNI monolayer in the absence of SOC was then investigated using first-principles calculations. From Fig. 3, we can see clearly that the valence and conduction bands meet at the Fermi level, exhibiting clear features of Dirac cones. The electron density of states projected onto different atoms (PDOS) shows that the electronic state at the Fermi level is zero, which further confirms the gapless states near the Fermi level. The Dirac bands mainly originate from I and Ti atoms. It is noteworthy that the Dirac cones of the TiNI monolayer differ significantly from those of graphene. Firstly, the Dirac points ($\Lambda$ point) of the TiNI monolayer are not at the high symmetric points of the BZ, but have a small deviation from the $\Gamma$ point along the $\Gamma$-$X$ direction, as shown in Fig. 3. Secondly, the presence of the Dirac cone of the TiNI monolayer is related to the intrinsic band inversion characterised by the camel-back shape near the $\Gamma$ point, as shown in the inset of Fig. 3. Finally, the Dirac cone of the TiNI monolayer is highly distorted in reciprocal space, leading to anisotropic energy dispersion around the Dirac point.

The electron density of states near the Fermi level was further projected onto different atomic orbitals, as shown in Fig. 4. From the orbital-resolved electronic density of states, we can see that the valence band maximum (VBM) mainly consists of the $p_x$-orbital of I atoms, while the conduction band minimum (CBM) is mainly from the $d_{xy}$-orbital of Ti atoms, which are consistent with the isosurfaces of the Kohn-Sham wavefunctions as plotted in the inset of Fig. 4.

![](./images/811194053793153024_4.jpg)

Fig. 3 Band structures and the electron density of states (PDOS) projected onto different atoms of the TiNI monolayer. Inserted first BZ with high symmetric points: $\Gamma$ (0.0, 0.0, 0.0), X (0.5, 0.0, 0.0), R (0.5, 0.5, 0.0), Y (0.0, 0.5, 0.0). Fermi level is set to zero.

![](./images/811194053793153024_5.jpg)

Fig. 4 The electron density of states projected onto the p and d atomic orbitals (PDOS-2) of Ti (up) and I (down) atoms. The energy at the Fermi level is set to zero. The insets represent the isosurfaces of the Kohn-Sham wavefunctions of the two Dirac bands nearest to the Fermi level (CBM and VBM), with an isovalue of 0.005 Å⁻³.

The effective Fermi velocity ($\nu_{\text{F}}$) is an important concept in Landau's Fermi liquid theory since it provides a direct measure of many-body interactions in the electron system,⁴² and plays the same role as the effective mass.⁴³ The $\nu_{\text{F}}$ of graphene is an essential quantity because all the observable quantities depend on it. The $\nu_{\text{F}}$ of the TiNI monolayer in the $k_x$ and $k_y$ directions can be obtained by fitting these two bands at $k_i = K_i + q$ ($i = x, y$) to the expression $\nu_{\text{F}} = E(q)/\hbar |q|$, which can be obtained from the slope of the bands. In the $k_x$ direction, the slopes of the bands are $-23.82$ eV Å and $3.01$ eV Å compared to the values of $\pm 35.20$ eV Å in graphene;⁵,⁸,⁴⁴ while in the $k_y$ direction, the slopes of the bands are $-0.34$ eV Å and $-0.35$ eV Å, suggesting direction-dependent Fermi velocities. The large slope along the $k_x$ direction comparable to that of graphene implies high carrier motilities (electron and hole) near the CBM and VBM, which is quite promising for the device applications.

It is interesting to examine the SOC effects on the electronic structures of the TiNI monolayer due to the existence of Dirac cones. By including the SOC effect, the band gap of the TiNI monolayer will open up to 50.7 meV around the $\Lambda$ point, which is significantly larger than that in graphene, silicene and germanene,⁴⁵ suggesting strong SOC strength in the TiNI monolayer.

In order to determine topological features, the parity criteria proposed by Fu and Kane⁴⁶ were then used to calculate the $Z_2$ topological index (0 or 1, indicating trivial or nontrivial band topology, respectively). The $Z_2$ index is determined by the parity of occupied bands at four time-reversal invariant momenta. The $Z_2$ invariant $\nu$ is defined by the following expression:

$$
(-1)^{\nu} = \prod_{i} \delta_{i} \text{ with } \delta_{i} = \prod_{m=1}^{N} \xi_{2m}(\Gamma_{i})
$$

For $2N$ occupied bands, $\xi_{2m}(\Gamma_i) = \pm 1$ is the parity eigenvalue of the $2m$-th occupied energy bands at the time-reversal invariant momentum $\Gamma_i$. The two states of a Kramers doublet have the same parity, $\xi_{2m} = \xi_{2m-1}$. In the presence of inversion symmetry, the $Z_2$ topological invariants can be deduced from the knowledge of the parities of the four time-reversal and parity invariant points at BZ, without having to know about the global properties of the energy bands. For the TiNI monolayer, the four time- reversal invariant points are $\Gamma$, $X$, $R$ and $Y$ as shown in Fig. 5. The parity of each band at the four time-reversal momenta can be calculated from the corresponding electron wavefunctions based on the DFT method. We found that the product of parities is $-1$, indicating that the TiNI monolayer is a QSH insulator as shown in Fig. 5.

Normally, a 2D TI is expected to demonstrate an odd number of Dirac-like edge states connecting the conduction and valence bands. To explore this, we have also examined whether edge states exist in the 2D TiNI monolayer. A one-dimensional (1D) TiNI nanoribbon is built with all the edge atoms passivated by hydrogen atoms to eliminate the dangling bonds. The ribbon width is as large as 12.1 nm to avoid the interaction between the two edges as shown in Fig. 5c. Fig. 5b presents the calculated electronic structure of the TiNI nanoribbon. The topological edge states (red lines) can be seen clearly with a single Dirac point formed around the $\Gamma$ point. Fig. 5d plots the real-space charge of edge states at the $\Gamma$ point, which are mainly distributed at edge Ti and N atoms. The existence of edge states clearly indicates that the 2D TiNI monolayer is indeed a 2D TI.

Apart from the equalitarian states, we also investigated the robustness of band inversion of the TiNI monolayer under uniaxial strain. In view that the band inversion is not due to the SOC effect, we did not include the SOC effect in our calcula- tions. Interestingly, the electronic structure of the TiNI mono- layer responds differently to compressional and tensile uniaxial strains. The band inversion is robust to compression along the $x$-direction and stretching along the $y$-direction, but can be gradually diminished for stretching along the $x$-direction and compression along the $y$-direction as shown in Fig. 6. At these states without band inversion, the TiNI lattice converts to a moderated semiconductor with a tuneable band gap as shown in Fig. 6 and 7.

Due to the huge calculation cost of HSE, we employed the DFT+$U$ scheme with a Hubbard $U$ term of 1 eV to Ti (3d) states to correct the electronic structure states. The value of $U$ was chosen to reproduce the bands under a strain of $-5\%$ based on the HSE functional. It is found that both the band inversion nature

![](./images/811194053793153024_6.jpg)

Fig. 5 (a) The enlarged view of the Dirac bands with and without SOC in close vicinity of the $\Gamma$ point. Brillouin zone with the values of $\delta_i$ associated with the time-reversal invariant momenta is listed in the right column. (b) Electronic band structure of the TiNI nanoribbon. The helical edge states (red lines) can be clearly seen around the $\Gamma$ point dispersing in the bulk gap. The top views of the TiNI nanoribbon are shown in (c). Here, $L$ represents the width of the nanoribbon. The edge atoms are passivated by H atoms represented by the small pink balls. (d) Real-space charge distribution of edge states around the $\Gamma$ point.

![](./images/811194053793153024_7.jpg)

Fig. 6 Band structures of the 2D TiNI monolayer with external strain along the $x$-direction and the $y$-direction, respectively [(a) and (b)]. Fermi level is set to zero. Here, "-" represents the condition of compressional tensile strain.

![](./images/811194053793153024_8.jpg)

Fig. 7 The variation of the band gap at the $\Gamma$ point of the TiNI monolayer under different external strain. The negative values of the band gap (blue) represent band inversion. The data obtained from the PBE and LDA+$U$ functionals are present in the top and bottom panels. The two represen- tative band structures with and without band inversion are plotted in the insets of the figure.

and band gap opening under external strain are independent of functional, as shown in Fig. 7.

We demonstrated that the magnitude of the inverted band gap increases obviously with increasing compression (stretched) strain along the $x$-axis ($y$-axis), as shown in Fig. 6 and 7. Specially, the band inversion characterised by the camelback shape remains in a semiconducting state as shown in Fig. 6. However, the dynamical stability of the strained lattices is lower than that in the unstrained state, due to the external strain. The intrinsic band inversion confirmed that the topological nontrivial electronic states revealed in the unstrained lattice would be intrinsic properties of the TiNI lattice.

To correct for the GGA$^{47}$ intrinsic self-interaction error$^{48}$ and thus penalize multiple occupancies, we also employed a more accurate hybrid functional proposed by Heyd, Scuseria, and Ernzerhof (HSE)$^{49}$ in the electronic structure calculations. Our HSE result showed that the nontrivial band gap is as high as 273.1 meV, suggesting that the QSH effect can be easily achieved at room temperature. Moreover, parity analysis$^{46}$ indicated that the topological properties calculated by the HSE functional are consistent with the PBE result, with the topological index $Z_2 = 1$.

## Conclusions

Based on first-principles calculations, we proposed a new 2D material, a titanium nitride iodide (TiNI) monolayer, which can be exfoliated from the bulk TiNI crystal due to the weak interlayer interaction. The TiNI monolayer has an inverted band structure accompanied by distorted Dirac cones with highly-anisotropic Fermi velocity. SOC opens a topological nontrivial band gap of 50.7 meV at the Dirac point, which can be characterized by a topological invariant of $Z_2 = 1$. The band inversion can be tuned by applying external strain, suggesting that the topologically nontrivial electronic states would be robust against a wide range of external strain. These above results imply that the TiNI monolayer is promising for achieving the QSH effect at high temperature.

## Acknowledgements

We acknowledge generous grants of high-performance computer time from the computing facility at Queensland University of Technology and Australian National Facility. Z. W. is thankful for the support from the Nature Science Foundation of Jiangsu Province (Grant No. BK20130859). A. D. greatly appreciates the Australian Research Council QEII Fellowship (DP110101239) and financial support of the Australian Research Council under Discovery Project (DP130102420). M. Z. is thankful for the support from the National Natural Science Foundation of China (No. 91221101, 21433006) and the 111 project (No. B13029).

## References

1 F. Schwierz, *Nat. Nanotechnol.*, 2010, **5**, 487–496.

2 A. C. Neto, F. Guinea, N. Peres, K. S. Novoselov and A. K. Geim, *Rev. Mod. Phys.*, 2009, **81**, 109.

3 K. S. Novoselov, A. K. Geim, S. Morozov, D. Jiang, Y. Zhang, S. a. Dubonos, I. Grigorieva and A. Firsov, *Science*, 2004, **306**, 666–669.

4 M. Zhao, W. Dong and A. Wang, *Sci. Rep.*, 2013, **3**, 3532.

5 D. Malko, C. Neiss, F. Viñes and A. Görling, *Phys. Rev. Lett.*, 2012, **108**, 086804.

6 Y. Liu, G. Wang, Q. Huang, L. Guo and X. Chen, *Phys. Rev. Lett.*, 2012, **108**, 225505.

7 Z. Wang, X. F. Zhou, X. Zhang, Q. Zhu, H. Dong, M. Zhao and A. R. Oganov, *Nano Lett.*, 2015, **15**, 6182–6186.

8 A. Wang, X. Zhang and M. Zhao, *Nanoscale*, 2014, **6**, 11157–11162.

9 X. Zhang, A. Wang and M. Zhao, *Carbon*, 2015, **84**, 1–8.

10 A. Du, S. Sanvito and S. C. Smith, *Phys. Rev. Lett.*, 2012, **108**, 197207.

11 S. Cahangirov, M. Topsakal, E. Aktürk, H. Şahin and S. Ciraci, *Phys. Rev. Lett.*, 2009, **102**, 236804.

12 H. Zhou, M. Zhao, X. Zhang, W. Dong, X. Wang, H. Bu and A. Wang, *J. Phys.: Condens. Matter*, 2013, **25**, 395501.

13 Z. Wang, M. Zhao, X.-F. Zhou, Q. Zhu, X. Zhang, H. Dong, A. R. Oganov, S. He and P. Grünberg, 2015, *arXiv preprint arXiv:1511.08848*.

14 M. Zhao and R. Zhang, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2014, **89**, 195427.

15 Y. Xu, B. Yan, H.-J. Zhang, J. Wang, G. Xu, P. Tang, W. Duan and S.-C. Zhang, *Phys. Rev. Lett.*, 2013, **111**, 136804.

16 X.-F. Zhou, X. Dong, A. R. Oganov, Q. Zhu, Y. Tian and H.-T. Wang, *Phys. Rev. Lett.*, 2014, **112**, 085502.

17 M. Zhao, X. Chen, L. Li and X. Zhang, *Sci. Rep.*, 2015, **5**, 8441.

18 L. Li, X. Zhang, X. Chen and M. Zhao, *Nano Lett.*, 2015, **15**, 1296–1301.

19 A. Z. Wang, A. J. Du and M. W. Zhao, *Nano Res.*, 2015, **8**, 3823–3829.

20 M. Zhao, A. Wang and X. Zhang, *Nanoscale*, 2013, **5**, 10404–10408.

21 Z. Wang, Z. Liu and F. Liu, *Phys. Rev. Lett.*, 2013, **110**, 196801.

22 Z. Wang, N. Su and F. Liu, *Nano Lett.*, 2013, **13**, 2842–2845.

23 G. Zhao, S. Han, A. Wang, Y. Wu, M. Zhao, Z. Wang and X. Hao, *Adv. Funct. Mater.*, 2015, **25**, 5292–5299.

24 S. Wang, H. Yu, H. Zhang, A. Wang, M. Zhao, Y. Chen, L. Mei and J. Wang, *Adv. Mater.*, 2014, **26**, 3538–3544.

25 J. Kim, S. S. Baik, S. H. Ryu, Y. Sohn, S. Park, B.-G. Park, J. Denlinger, Y. Yi, H. J. Choi and K. S. Kim, *Science*, 2015, **349**, 723–726.

26 Y. Yao, F. Ye, X.-L. Qi, S.-C. Zhang and Z. Fang, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2007, **75**, 041401.

27 L. Kou, B. Yan, F. Hu, S. C. Wu, T. O. Wehling, C. Felser, C. Chen and T. Frauenheim, *Nano Lett.*, 2013, **13**, 6251–6255.

28 L. Kou, S.-C. Wu, C. Felser, T. Frauenheim, C. Chen and B. Yan, *ACS Nano*, 2014, **8**, 10448–10454.

29 C. M. Schurz, L. Shlyk, T. Schleid and R. Niewa, *Z. Kristallogr.*, 2011, **226**, 395–416.

30 S. Yamanaka, *Annu. Rev. Mater. Sci.*, 2000, **30**, 53–82.

31 R. Juzatr and H. Friedrichsen, *Z. Anorg. Allg. Chem.*, 1964, **332**, 173–178.

32 S. M. Notley, *Langmuir*, 2012, **28**, 14110–14113.

33 V. Nicolosi, M. Chhowalla, M. G. Kanatzidis, M. S. Strano and J. N. Coleman, *Science*, 2013, **340**, 1226419.

34 G. Kresse and J. Hafner, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1993, **47**, 558–561.

35 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865.

36 G. Kresse and D. Joubert, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1999, **59**, 1758.

37 D. Alfè, *Comput. Phys. Commun.*, 2009, **180**, 2622–2633.

38 S. Zhao, Z. Li and J. Yang, *J. Am. Chem. Soc.*, 2014, **136**, 13313–13318.

39 R. Zacharia, H. Ulbricht and T. Hertel, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2004, **69**, 155406.

40 X. Li, X. Wu and J. Yang, *J. Am. Chem. Soc.*, 2014, **136**, 11065–11069.

41 C. Lee, X. Wei, J. W. Kysar and J. Hone, *Science*, 2008, **321**, 385–388.

42 H. Rostami and R. Asgari, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2012, **86**, 155435.

43 R. Asgari and B. Tanatar, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2006, **74**, 075301.

44 A. Wang, L. Li, X. Wang, H. Bu and M. Zhao, *Diamond Relat. Mater.*, 2014, **41**, 65–72.

45 C.-C. Liu, W. Feng and Y. Yao, *Phys. Rev. Lett.*, 2011, **107**, 076802.

46 L. Fu and C. L. Kane, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 2009, **76**, 045302.

47 J. P. Perdew, J. A. Chevary, S. H. Vosko, K. A. Jackson, M. R. Pederson, D. J. Singh and C. Fiolhais, *Phys. Rev. B: Condens. Matter Mater. Phys.*, 1992, **46**, 6671–6687.

48 E. Dagotto, *Rev. Mod. Phys.*, 1994, **66**, 763.

49 J. Heyd, G. E. Scuseria and M. Ernzerhof, *J. Chem. Phys.*, 2006, **124**, 219906.

This journal is © the Owner Societies 2016

Phys. Chem. Chem. Phys., 2016, **18**, 22154–22159 | 22159