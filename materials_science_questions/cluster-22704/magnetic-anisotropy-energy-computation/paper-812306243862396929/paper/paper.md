# Atomic-layer stacking dependence of the magnetocrystalline anisotropy in Fe-Co multilayer thin films at MgO(001) interface

K. Nakamura $^{a,*}$, K. Nozaki $^{a}$, K. Hayashi $^{a}$, A.-M. Pradipto $^{b}$, M. Weinert $^{c}$, T. Oguchi $^{d}$

$^{a}$ Graduate School of Engineering, Mie University, Tsu, Mie 514-8507, Japan
$^{b}$ Faculty of Mathematics and Natural Sciences, Institut Teknologi Bandung, Bandung 40132, Indonesia
$^{c}$ Department of Physics, University of Wisconsin-Milwaukee, Milwaukee, Wisconsin 53201, USA
$^{d}$ Institute of Scientific and Industrial Research, Osaka University, Osaka, Ibaraki 567-0047, Japan

---

## ARTICLE INFO

**Keywords:**
Magnetocrystalline anisotropy
atomic-layer stacking dependence
first-principles calculations

## ABSTRACT

Magnetocrystalline anisotropy (MA) and electric-field-induced modification of the MA energy (E-field-induced MA modification) of Co-Fe multilayer thin films at MgO(001) interface with respect to atomic-layer stacking were investigated using first-principles calculations combined with the cluster expansion method. Although the magnetic quantities have very complicated dependence on atomic-layer stacking, we find that there are key short-range atomic-layer stackings. At the MgO interface, a double atomic-layer stacking of Fe on the MgO enhances an interfacial perpendicular MA while there is no role of the short-range stacking in the E-field-induced MA modification where a single Fe atomic-layer at the interface plays a role. The physical origins underlying these trends were subsequently elucidated by band structure calculations.

---

## 1. Introduction

The identification of promising magnetic thin-films with large perpendicular magnetocrystalline anisotropy (PMA) is an important design goal in the field of spintronics [1]. The observation of PMA at Fe (CoFeB)/MgO interface [2–5] – where spin-orbit coupling (SOC) is quite weak and interfacial $p$-$d$ hybridization enhances the PMA [2,6–8] – has led to an important research direction in developing successful perpendicular magnetic tunnel junction (pMTJ) devices. The search for materials with the large PMA has expanded to include multilayer thin films in which the PMA may be achieved by tuning atomic-layer stacking [9]. Experimentally, artificial transition-metal thin films with PMA using rare-earth and noble elements [10–12] have been synthesized, and other materials are being investigated [9,13–15]. The use of multilayer thin films has particularly an advantage where the multiple physical properties can be controlled by the atomic-layer stacking, e.g., for films with the large PMA and low magnetization to promising pMTJs. It is however difficult to search such films due to the enormous number of possible atomic-layer stackings. In addition, the magnetocrystalline anisotropy (MA) is very sensitive to the detail of atomic-layer stackings in films, substrates, and surface/interface structures, all of which are crucial in spintronic device applications. In order to treat such complexity, a comprehensive understanding of the dependence on atomic-layer stacking of the MA is highly desired.

Most theoretical investigations so far used a single atomic-layer-resolved analysis [5], which address only an atomic on-site dependence, in determining the MA. However, X-ray-absorption measurements observed an imbalance in Co-Co bonds along the in-plane and out-of-plane directions in CoPt film with the PMA, suggesting that the short range order is important for driving the PMA [16], Chemical ordering was experimentally found to be responsible for the PMA in $L1_{0}$ FePd and FeNi films [17,18]. First-principles calculations within the Korring-Kohn-Rostoker coherent potential approximation demonstrated that the compositional atomic ordering enhances the MA energy and alters the magnetization easy axis due to the lowering of lattice symmetry [19]. Recent efforts have further started to identify an inter-atomic contribution to the MA, e.g., in FePt [20] ($CrNb_{3}S_{6}$ [21]) where the inter-atomic pair contribution of Fe-Pt (Cr-Nb) is comparable (significantly large) compared to the single atomic contributions of Fe and Pt (Cr and Nb).

In the present work, we systematically investigated the atomic-layer stacking dependence of the MA energy for the prototypical Co-Fe bilayer multilayer thin films on MgO(001) by a help of the cluster expansion (CE) method [22–26] that uniquely provides a way to find trends and features of atomic configurations in material properties. We further investigate the electric-field-induced modification of the MA energy (E-

---
* Corresponding author.
E-mail address: nakamura.kohji@mie-u.ac.jp (K. Nakamura).

https://doi.org/10.1016/j.jmmm.2021.168175
Received 7 August 2020; Received in revised form 13 February 2021; Accepted 31 May 2021
Available online 10 June 2021
0304-8853/© 2021 Elsevier B.V. All rights reserved.

field-induced MA modification) [27] which is one of the challenging issues for realizing voltage-based pMTJ with ultralow-energy power consumption [27-30]. The present paper is organized as follows. In the next section, we provide model and method for treating atomic-layer configurations in the considered binary multilayer thin film systems. In Section 3, results of first-principles calculations of the MA energy and the E-field-induced MA modification, as well as the excess energy and the magnetization, for multilayers are presented. Then, the data obtained is analyzed using the CE method to extract the underlying trends. The physical origins of key atomic-layer stacking at the MgO interface are subsequently discussed based on band structure calculations. Finally, a summery is given in Section 4.

## 2. Model and method

In order to model the multilayer thin film systems, we employed slabs consisting of six atomic-layers of Fe and Co in a bcc stacking on four atomic-layers' substrate of rocksalt MgO(001), as depicted in Fig. 1(a), where there are totally 64 $(=2^6)$ atomic-layer configurations. The atomic-layer position, $L$, in the film is labeled by the number from the surface layer ($L=1$) to the interface layer ($L=6$), and an atomic-layer configuration is represented, for example, by CFCCFF/ corresponding to the CoFeCoCoFeFe/MgO, where C and F indicate Co and Fe atomic-layers, respectively. The atomic positions along the film-plane normal were fully optimized by atomic force calculations [31], and the in-plane lattice constant has been chosen to match that of calculated bulk MgO. The transition-metal (Co and Fe) atoms at the MgO interface are located on top of O atoms as found by first-principles calculations [32] and LEED experiments [33].

Calculations were carried out using full-potential linearized augmented plane-wave (FLAPW) method in a single slab geometry [34-36] in the scalar relativistic approximation (SRA) based on generalized gradient approximation [37]. A wave function cutoff of $|\mathbf{k}+\mathbf{G}| \leqslant 3.0$ a.u. and muffin-tin (MT) sphere radii of 2.2, 2.2, 2.0, and 1.4 a.u. for Co, Fe, Mg, and O, respectively, were used. The angular-momentum expansion inside the MT spheres is truncated at $\ell=8$ for Co, Fe and Mg, and 6 for O for the wave functions, charge and spin densities, and the potential. To determine the MA, the second variational method for treating the SOC was performed using the SRA eigenvectors, and the MA energy, $E^{\text{MA}}$, defined as the difference in total energy for magnetization oriented along the in-plane [100] and perpendicular [001] directions,
$$
E^{\text{MA}}=E[100]-E[001], \tag{1}
$$
was then determined by the force theorem [38,39], where 8,100 special k-points in the two-dimensional Brillouin zone (BZ) were used to suppress numerical fluctuations. The $E$-field along the film-plane normal was introduced in the vacuum regions far enough from surfaces [40,41], and the $E$-field-induced MA modification, $\eta^{\text{MA}}$, was estimated by the difference in the MA energy at $E$-fields of $\pm 0.25 \mathrm{~V} / \AA$ at the vacuum as
$$
\eta^{\mathrm{MA}}=\frac{E^{\mathrm{MA}}(0.25 \mathrm{~V} / \mathring{\mathrm{A}})-E^{\mathrm{MA}}(-0.25 \mathrm{~V} / \mathring{\mathrm{A}})}{0.5}, \tag{2}
$$
where value of $\eta^{\text{MA}}$ is not adjusted by the dielectric constant of MgO [42] for avoiding an uncertainness in determination of the dielectric constant in thin film system. The excess energy was estimated by the total energy difference,
$$
E_{i_{1} \cdots i_{L} \cdots i_{6}}^{\text{Ex}}=E_{i_{1} \cdots i_{L} \cdots i_{6}}-\left(1-\frac{m}{6}\right) E_{\text{CCCCCC}} /-\frac{m}{6} E_{\text{FFFFFF}} /, \tag{3}
$$
where $i_{L}$ represents C and F at the $L$-th atomic-layer, and $m$ is the number of Fe atomic-layers.

![](./images/812306243862396929_1.jpg)

Fig. 1. (a) Model of an Fe-Co multilayer thin film on MgO(001). The atomic-layer position, $L$, is labeled by the number from the surface layer ($L=1$) to the interface layer ($L=6$). $L=7$ represents an O layer at the MgO interface. (b) The table presents the 64 independent clusters, where $\alpha$ is a sequential number and the corresponding cluster consists of a set of atomic-layer numbers in parenthesis. (c) Examples of clusters $\alpha=21$ and 40, which consist of two ($L=5$ and 6) and three atomic-layers ($L=3$, 5 and 6), respectively.

Atomic-layer configurations are treated as a one-dimensional lattice model, $\vec{\sigma} = \{\sigma_1, ..., \sigma_L, ..., \sigma_6\}$, where $\sigma_L$ takes either $-1$ and $+1$, depending on the atom type at the $L$-th atomic-layer. In the present case, we set $-1$ and $+1$ for Co and Fe atomic-layers, respectively. The correlation function of a cluster $\alpha$ in Fig. 1(b) in the CE method can be thus expressed as

$$
\xi_{\alpha}(\vec{\sigma}) = \prod_{L \in \alpha} \{\sigma_L\}, \tag{4}
$$

where an empty cluster of $\alpha=0$ is included ($\xi_0=1$), and $L \in \alpha$ indicates the $L$-th atomic-layer in the cluster $\alpha$. With no $z$-reflection symmetry along the film-plane normal, there are $64\ (=2^6)$ independent clusters, listed in Fig. 1(b), where $\alpha$ is a sequential number representing a type of cluster and the corresponding cluster consists of a set of the atomic-layer numbers in the parenthesis. For example, in Fig. 1(c), the cluster $\alpha=21$ consists of two atomic-layers ($L=5$ and $6$) with the nearest neighbors at the interface, and the cluster $\alpha=40$ is three atomic-layers ($L=3$, $5$ and $6$) consisting of the nearest and second nearest neighbors. The $\xi_{21}$ and $\xi_{40}$ of the CFCCCFF/ are $+1$ [$σ_5σ_6=(+1)×(+1)$] and $-1$ [$σ_3σ_5σ_6=(-1)×(+1)×(+1)$], respectively. A physical property, $F(\vec{\sigma})$, may be then represented linearly by the correlation functions as

$$
F(\vec{\sigma}) = \sum_{\alpha=0}^{63} C_{\alpha} \xi_{\alpha}(\vec{\sigma}). \tag{5}
$$

We evaluated the CE coefficients, $C_a$, by the inversion matrix method [23],

$$
C_{\alpha} = \sum_{n=1}^{64} \{\xi_{\alpha}(\vec{\sigma}_n)\}^{-1} F(\vec{\sigma}_n), \tag{6}
$$

by using all 64 atomic-layer configurations.

## 3. Results and discussion

Fig. 2 summarizes the results of the calculated excess energy, $E^{\text{Ex}}$, the spin magnetization, $M$, the MA energy at $E$-fields of zero and $\pm 0.25$ V/Å, $E^{\text{MA}}$, and the $E$-field-induced MA modification, $\eta^{\text{MA}}$, for all 64 atomic-layer configurations as a function of the number of Fe atomic-layers,

![](./images/812306243862396929_2.jpg)

Fig. 2. (a) Excess energy, $E^{\text{Ex}}$, (b) spin magnetization, $M$, (c-e) MA energy at $E$-fields of zero, $-0.25$ and $0.25$ V/Å, $E^{\text{MA}}$, and (f) $E$-field-induced MA modification, $\eta^{\text{MA}}$, of all 64 atomic-layer configurations as a function of the number of Fe atomic-layers, $m$, in an unit cell. The atomic-layer configuration is represented, for instance, by CFCCCFF/ for CoFeCoCoFeFe/MgO, where C and F indicate Co and Fe atomic-layers, respectively.

$m$, in a unit cell. The calculated values with the same number of Fe atomic-layers display a large range of values and depend significantly on the atomic-layer configuration except the magnetization. The magnetization increases almost linearly with the number of Fe atomic-layers, which satisfies the Slater-Pauling rule, indicating that films with the low magnetization can be achieved in the low Fe composition, regardless of the atomic-layer configuration. In the MA energy, it varies from 1.4 meV/unit-area for the perpendicular magnetization to $-1.5$ eV/unit-area of the in-plane magnetization. The MA energy for the pure Fe film (FFFFFF/) is positive, 1.34 meV/unit-area, while for the pure Co film (CCCCCC/) it is negative, $-0.54$ meV/unit-area, the trend that the MA energy in the Fe film is larger than that in the Co film is qualitatively the same to the previous calculations [7,43] and experiments [3,4,44]. For equal Fe-Co ($m=3$), the FCCCFF/ has a large positive MA energy of 0.9 meV/unit-area, but when the atomic-layer configuration is changed to the FCCFCF/ (the atomic-layers at $L=4$ and 5 are interchanged), the MA energy is almost zero, 0.1 meV/unit-area. Although the results of MA energy contradict the previous calculations [45] of PMA in CFCFCFCFC/ MgO, this disagreement is confirmed to attribute to the different in-plane lattice constant assumed [46]. In $E$-fields, as shown in Fig. 2(d-f), although the MA energy at $\pm 0.25$ V/Å is almost same each other, the complicated behavior in the $E$-field-induced MA modification with respect to the atomic-layer configuration is observed. The excess energy [Fig. 2(a)] also depends on the atomic-layer configuration but all have negative values, as seen in that in bulk [24].

The calculated CE coefficients in Eq. 6 for the excess energy, $E^{\text{Ex}}$, the MA energy at zero field, $E^{\text{MA}}$, and the $E$-field-induced MA modification, $\eta^{\text{MA}}$, as a function of cluster $\alpha$ in Fig. 1(b) are shown in Fig. 3. It can be seen that the CE coefficients of the three quantities with respect to the cluster behave differently each others. For the excess energy, the CE coefficients decay rapidly when the cluster size increases, where the dominant contribution arises from the clusters with the nearest-neighbor atomic-layers, $\alpha=7,12,16,19$, and 21. The results indeed support a simple nearest-neighbor pairwise interaction model of the excess energy. For the MA energy, the CE coefficients predict the characteristic clusters consisting of one- and two-atomic-layers, which govern the MA energy. At the MgO interface, for instance, the cluster $\alpha=6$ has a large positive CE coefficient, which indicates that the presence of the Fe atomic-layer at the interface gives a strong interfacial PMA; the results support the single atomic-layer-resolved analysis of the MA energy [5,47]. However, the PMA is further enhanced by the cluster $\alpha=21$ at the interface; the positive value of $C_{21}$ in Fig. 3(b), corresponding to like-pairs (Fe-Fe), favors the PMA, which demonstrates an important role of the short-range atomic-layer stacking to the PMA.

It is further instructive to illustrate the energy contribution of atomic-layer configurations in clusters to the MA energy. It may be obtained by projecting a probability, $x_{\alpha,i_Li_{L'}\cdots}$, of finding an atomic-layer configuration $i_Li_{L'}\cdots$ in a cluster $\alpha$,

$$
\epsilon_{\alpha,i_Li_{L'}\cdots}=\langle x_{\alpha,i_Li_{L'}\cdots}, E^{\text{MA}}\rangle, \tag{7}
$$

where $i_L$ represents C and F at the $L$-th atomic-layer in the cluster $\alpha$. The $x_{\alpha,i_Li_{L'}\cdots}$ is expressed by a set of correlation functions, $\xi_{\beta \in \alpha}$ [48,49], the $E^{\text{MA}}$ is expressed by Eq. 5, and $\langle \rangle$ is the trace operator on all 64 atomic-

![](./images/812306243862396929_3.jpg)

Fig. 3. Calculated CE coefficients, $C_{\alpha}$, of excess energy, $E^{\text{Ex}}$ (in eV/atom), MA energy at zero field, $E^{\text{MA}}$ (in meV/unit-area), and $E$-field-induced MA modification, $\eta^{\text{MA}}$ [(meV/unit-area)/(V/Å)], as a function of cluster $\alpha$ in Fig. 1(b).

layer configurations [22]. The results of $\epsilon_{41, i_{4} i_{5} i_{6}}$ for the atomic-layer configurations in the cluster $\alpha=41$ at the MgO interface (i.e., $\epsilon_{41, CCC}$, $\epsilon_{41, CCF}$, $\epsilon_{41, CFC}$, $\epsilon_{41, CFF}$, $\epsilon_{41, FCC}$, $\epsilon_{41, FCF}$, $\epsilon_{41, FFC}$, and $\epsilon_{41, FFF}$) are shown in Fig. 4(a). These show that $\epsilon_{41, CFF}$ and $\epsilon_{41, FFF}$ have the large positive contributions that favor the PMA but $\epsilon_{41, FCF}$ has a negative one. It further demonstrates that for the cluster $\alpha=21$ at the MgO interface, $\epsilon_{21, FF}$ has a large positive contribution while $\epsilon_{21, CF}$ has almost zero. Thus, the key atomic-layer configuration for the interfacial PMA is at least the double atomic-layer stacking of Fe (FF stacking) on the MgO.

To verify the contribution of the Fe double atomic-layer stacking, the first-principles calculated (DFT) MA energy for systems having CC, CF, FC, and FF stakings at the MgO interface are replotted in Fig. 4(b). The DFT MA energy clearly shows the same trend as the energy contributions in Fig. 4(a). For example, the FFFFFF/ has the largest positive value but decreases on going to the FFFFFC/, FFFFFCF/, and FFFFCC/, where the top four atomic-layers from the surface align as FFFF (green closed circles). For the CCFFFF/, the MA energy is negative and becomes more negative for the CCFFFC/, CCFFCF/, and CCCFCC/(blue ones). The CCCCFF/ may be desired as a film with the large PMA and low magnetization.

For the $E$-field-induced MA modification, the contribution for the clusters $\alpha=21$ and $41$, $\eta_{21, i_{5} i_{6}}$ and $\eta_{41, i_{4} i_{5} i_{6}}$, were also examined and the results are shown in Fig. 4(c). The large contribution (the magnitude) arise from the CCF, CFF, and FCF stakings and the CF and FF stackings on the interface. Thus, the large contribution commonly comes from a single atomic-layer of Fe at $L=6$ and the $E$-field-induced MA modification is attributed only in the single atomic-layer at the interface, so that there is no role in the short-range atomic-layer stacking. It also notes that the DFT values of $\eta^{MA}$ in Fig. 4(d) show qualitatively the same trend as in Fig. 4(c).

In order to get a deeper insight into an origin for the role of Fe double-layer stacking to the PMA, we calculated the band structure along high symmetry k-directions for the CCCCFF/. Fig. 5(a) and (b) show the band structure and the density of states (DOS) for the sum of Fe atoms at $L=5$ and 6 in the minority-spin state. The line width in Fig. 5(a) represents the relative weights of $d_{0}$ (green), $d_{\pm 1}$ (red), and $d_{\pm 2}$ (blue) orbitals to the wave functions for the Fe atoms at $L=5$ and 6.The bands crossing the Fermi level $(E_{F})$ arise mainly from the minority-spin states, while the majority-spin bands (not shown in the figure) are almost fully occupied and are located between $-1$ to $-4$ eV below $E_{F}$. A weakly dispersing band with significant Fe $d_{z^{2}}$ $(d_{0})$ weight orbital located about $1.8$ eV above $E_{F}$ is pushed up by the hybridization to the O $p_{z}$ orbital at the MgO interface [2,6]. The bands derived from Fe $d_{x^{2}-y^{2},xy}$ $(d_{\pm 2})$ orbitals are broad, ranging between $-2$ and 2 eV, due to the strong hybridization between the neighboring Fe atoms on the same atomic-layer.

In contrast, due to the Fe atoms at $L=5$ and 6, the Fe $d_{xz,yz}$ $(d_{\pm 1})$ orbitals in both atomic layers hybridize each other, with large weight around $E_{F}$. As illustrated in Fig. 5 (c), the antibonding $d_{xz,yz}^{*}$ states at the $\Gamma$ point - which are above $E_{F}$ for both the freestanding Fe monolayer [40] and that on MgO [6] - are pushed down close to $E_{F}$, while at the M point, the bonding $d_{xz,yz}$ states below $E_{F}$ in the monolayers are pushed up above $E_{F}$. Thus, for the Fe double-layers, nearly flat $d_{xz,yz}$ bands around $E_{F}$ exist throughout the whole BZ.

A contour map of $E^{MA}(\mathbf{k})$ [50] is shown in Fig. 5(d). In most of the BZ, $E^{MA}(\mathbf{k})$ is positive, especially around $\Gamma$ point and along $\Gamma$-M. The top figure in Fig. 5(a) displays the $E^{MA}(\mathbf{k})$ (black line) along the k-directions and the energy contribution of the Fe atoms at $L=5$ and 6 (red line), calculated by switching off the SOC of the Fe atoms selectively by first principles calculations. It demonstrates that the large positive $E^{MA}(\mathbf{k})$ attributes in the Fe atoms at $L=5$ and 6. According to perturbation theory [51], the SOC between occupied and unoccupied states with the same (different) $m$ magnetic quantum number coupled through the $L_{z}$ $(L_{x}$ and $L_{y})$ operator gives a positive (negative) contribution to the $E^{MA}(\mathbf{k})$. In the present system, thus, the SOC interaction between the occupied and unoccupied $d_{xz,yz}$ $(m=\pm 1)$ states around $E_{F}$ at around $\Gamma$ point and along $\Gamma$-M, in Fig. 5(c), yields a positive $E^{MA}(\mathbf{k})$, which leads to the large interfacial PMA. Indeed, the MA energy of the CCCCFF/ is larger than that of the CCCCCCF/ by 0.43 meV/unit-area, and furthermore the large PMA due to the double-layer stacking of Fe at the MgO interface can be confirmed even in thicker films; the MA energies of CCCCCCF/, CCCCCCCFF/, and CCCCCCCCFF/ of the seven, eight, and nine atomic-layer films result in 1.26, 0.95, and 1.45 meV/unit-area of the PMA, respectively, which are larger than those of CCCCCCCF/, CCCCCCCCF/, and CCCCCCCCCF/ by 0.75, 0.71, and 0.75 meV/unit-area.

For the $E$-field-induced MA modification, as pointed out previously [6], it may be attributed to change in the interlayer distance at the MgO interface. Fig. 6(a) shows the calculated change in the interlayer distance, $\Delta d_{LL'}=d_{LL'}(0.25 \mathrm{V}/\mathring{\mathrm{A}})-d_{LL'}(-0.25 \mathrm{V}/\mathring{\mathrm{A}})$, for all 64 atomic-layer configurations. As a result of metallic screening, the application of an $E$-field leaves the interatomic distances basically unchanged with the exception of $d_{67}$, which corresponds to the inter-atomic distance between the metal (Fe and Co) layer at $L=6$ and the O layer at the MgO interface and changes by about $4 \times 10^{-3} \mathring{\mathrm{A}}$ for all atomic-layer configurations. As a consequence of the change in the Fe-O distance, the Fe $d_{z^{2}}$ band hybridization with the O $p_{z}$ orbital is modified. Fig. 6(b) shows the differences in the Fe DOS, $\Delta \mathrm{DOS}=\mathrm{DOS}(0.25 \mathrm{V}/\mathring{\mathrm{A}})-\mathrm{DOS}(-0.25 \mathrm{V}/\mathring{\mathrm{A}})$,

![](./images/812306243862396929_4.jpg)

Fig. 4. (a, c) Energy contribution of atomic-layer configurations in clusters $\alpha=41$ and 21 to the MA energy, $\epsilon_{41, i_{4} i_{5} i_{6}}$ and $\epsilon_{21, i_{5} i_{6}}$ (in meV/unit-area), and those of the $E$-field-induced MA modification, $\eta_{41, i_{4} i_{5} i_{6}}$ and $\eta_{21, i_{5} i_{6}}$ [in (meV/unit-area)/(V/Å)]. (b, d) The first principles MA energy, $E^{MA}$ (in meV/unit-area), and the $E$-field-induced MA modification, $\eta^{MA}$ [in (meV/unit-area)/(V/Å)]. Systems with CC, CF, FC, and FF stakings at the interface, represented by circles, are grouped along the horizontal axis. Closed (color) circles indicate sequences in the top four atomic-layers from the surface, aligned as CCCC (grey), CCCF (red), CCFF (blue), CFFF (orange), and FFFF (light green).

![](./images/812306243862396929_5.jpg)

at $L=5$ and 6 in the CCCCFF/. At around 1.8 eV, the Fe $d_{z^2}$ DOS for both $L=5$ and 6 are clearly modified by the application of $E$-field. However, more importantly, the Fe $d_{xz,yz}$ DOS at $L=6$, whose orbitals give the PMA, is further modified around $E_{\text{F}}$ because of the (weak) hybridization between Fe $d_{xz,yz}$ and O $p_{x,y}$ orbitals, whereas those at $L=5$ is not modified. Thus, the $E$-field-induced MA modification comes mainly from the single atomic-layer at $L=6$ that accompanies the $E$-field-induced change in the inter-atomic Fe-O distance.

Finally, we comment on the effect of intermixing between Co and Fe at the MgO interface to the MA energy. Calculations for intermixed structures of CCCXXF/ and CCXXXX, where X is Co and Fe with a checkerboard arrangement on the atomic-layers, were carried out by using an in-plane unit cell of $\sqrt{2} \times \sqrt{2}$ structure. The total energies of intermixed CCCXXF/ and CCXXXX/ are found to be lower than that of CCCCFF/ by 14 and 23 meV/atom, respectively, and the atomic intermixing drastically decreases the MA energy to $-0.01$ and $-0.12$ meV/unit-area. It may thus suggest that growth method, e.g., low temperature annealing, plays a role in controlling the large PMA.

## 4. Summary

We investigated the MA energy and the $E$-field-induced MA modification of Co-Fe multilayer thin films on MgO(001) by using first-principles calculations combined with the CE method in order to clarify the atomic-layer stacking dependence. The analysis of the CE coefficients extracts the key short-range atomic-layer stackings. At the MgO interface, the double atomic-layer stacking of Fe on the MgO enhances the interfacial PMA, while the short-range atomic-layer stacking has no effect to the $E$-field-induced MA modification where the single Fe atomic-layer at the interface plays a role. The physical origin underlying these trends was subsequently addressed by band structure calculations. In particular, the large PMA originates from the nearly flat $d_{xz,yz}$ bands around $E_{\text{F}}$ due to the Fe double atomic-layer stacking. In contrast, the $E$-field-induced MA modification is mainly attributed to the change in the Fe $d_{xz,yz}$ DOS at the single Fe atomic-layer at the interface that accompanies the $E$-field-induced change in the inter-atomic Fe-O distance.

![](./images/812306243862396929_6.jpg)

Fig. 6. (a) Change in interlayer distance, $\Delta d_{LL'}$, at $E$-fields of $\pm 0.25\ \mathrm{V/\mathring{A}}$ for all 64 atomic-layer configurations, where $d_{67}$ corresponds to the inter-atomic distance between the metal (Fe and Co) layer at $L=6$ and the O layer at the MgO interface. (b) Change in the Fe DOS at $L=5$ and 6 for CCCCFF/ by application of $E$-fields of $\pm 0.25$ eV. Green, red, and blue lines represent for $d_{z^2}$, $d_{xz,yz}$, and $d_{x^2-y^2,xy}$ orbitals, respectively.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

We thank Dr. H. Kino, Prof. K. Fukushima, and Prof. M. Okada for fruitful discussions. Work was supported by JPSJ KAKENHI Grant Nos. 16K05415, 15H05702, and 19K03716. Materials Research by Information Initiative Project, Japan Science and Technology Agency, the Cooperative Research Program of Network Joint Research Center for Materials and Devices, Osaka University, and Center for Spintronics Research Network, Osaka University. Computations were performed at Research Institute for Information Technology, Kyushu University. Work at University of Wisconsin-Milwaukee was supported by US National Science Foundation EFMA-1741673.

## References

[1] A.D. Kent, Nat. Mater. 9 (2010) 699.
[2] R. Shimabukuro, K. Nakamura, T. Akiyama, T. Ito, Physica E 42 (2010) 1014.
[3] S. Ikeda, K. Miura, H. Yamamoto, K. Mizunuma, H.D. Gan, M. Endo, S. Kanai, J. Hayakawa, F. Matsukura, H. Ohno, Nat. Mater. 9 (2010) 721.
[4] J.W. Koo, S. Mitani, T.T. Sasaki, H. Sukegawa, Z.C. Wen, T. Ohkubo, T. Niizeki, K. Inomata, K. Hono, Appl. Phys. Lett. 103 (2013), 192401.
[5] B. Dieny, M. Chshiev, Rev. Mod. Phys. 89 (2017), 025008.
[6] K. Nakamura, T. Akiyama, T. Ito, M. Weinert, A.J. Freeman, Phys. Rev. B 81 (2010) 220409(R).
[7] H.X. Yang, M. Chshiev, B. Dieny, J.H. Lee, A. Manchon, K.H. Shin, Phys. Rev. B 84 (2011), 054401.
[8] D. Odkhuuab, W.S. Yunac, S.H. Rhima, S.C. Hong, J. Magn. Magn. Mater. 414 (2016) 126.
[9] K. Hotta, K. Nakamura, T. Akiyama, T. Ito, T. Oguchi, A.J. Freeman, Phys. Rev. Lett. 110 (2013), 267206.
[10] G. Kim, Y. Sakuraba, M. Oogane, Y. Ando, T. Miyazaki, Appl. Lett. 92 (2008), 172502.
[11] K. Mizunuma, S. Ikeda, J.H. Park, H. Yamamoto, H. Gan, K. Miura, H. Hasegawa, J. Hayakawa, F. Matsukura, H. Ohno, Appl. Phys. Lett. 95 (2009), 232516.

[12] K. Yakushiji, T. Saruya, H. Kubota, A. Fukushima, T. Nagahama, S. Yuasa, K. Ando, Appl. Phys. Lett. 97 (2010), 232508.
[13] G.H.O. Daalderop, P.J. Kelly, F.J.A. den Broeder, Phys. Rev. Lett. 68 (1992) 682.
[14] T. Shima, M. Okamura, S. Mitani, K. Takanashi, J. Magn. Magn. Mater. 310 (2007) 2213.
[15] T. Burkert, L. Nordström, O. Eriksson, and O. Heinonen, Phys. Rev. Lett. 93 (2004) 027203.
[16] T.A. Tyson, S.D. Conradson, R.F.C. Farrow, B.A. Jones, Phys. Rev. B 54 (1996) R3702.
[17] P. Kamp, A. Marty, B. Gilles, R. Hoffmann, S. Marchesini, M. Belakhovsky, C. Boeglin, H.A. Dürr, S.S. Dhesi, G. van der Laan, A. Rogalev, Phys. Rev. B 59 (1999) 1105.
[18] T. Kojima, M. Mizuguchi, T. Koganezawa, K. Osaka, M. Kotsugi, K. Takanashi, Jpn. J. Appl. Phys. 51 (2012) 010204.
[19] S.S.A. Razee, J.B. Staunton, B. Ginatempo, F.J. Pinski, E. Bruno, Phys. Rev. Lett. 82 (1999) 5369.
[20] J. Inoue, T. Yoshioka, H. Tsuchiura, J. Appl. Phys. 117 (2015) 17C720.
[21] M. Mito, H. Ohsumi, T. Shishidou, F. Kuroda, M. Weinert, K. Tsuruta, Y. Kotani, T. Nakamura, Y. Togawa, J. Kishine, Y. Kousaka, J. Akimitsu, K. Inoue, Phys. Rev. B 99 (2019), 174439.
[22] J.M. Sanchez, F. Ducastelle, D. Gratias, Physica A 128 (1984) 334.
[23] J.W.D. Connolly, A.R. Williams, Phys. Rev. B 27 (1983) 5169.
[24] J.M. Sanchez, Phys. Rev. B 81 (2010) 224202.
[25] A. van de Walle, Nat. Mater. 7 (2008) 455.
[26] L.J. Nelson, V. Ozolins, C.S. Reese, F. Zhou, G.L.W. Hart, Phys. Rev. B 88 (2013), 155105.
[27] M. Weisheit, S. Fähler, A. Marty, Y. Souche, C. Poinshignon, D. Givord, Science 315 (2007) 349.
[28] T. Maruyama, K. Ohta, T. Nozaki, T. Shinjo, M. Shiraishi, S. Mizukami, Y. Ando, Y. Suzuki, Nat. Nanotechnol. 4 (2009) 158.
[29] W.-G. Wang, M. Li, S. Hageman, C.L. Chien, Nat. Mater. 11 (2012) 64.
[30] D. Odkhuuab, Sci. Rep. 6 (2016) 32742.
[31] R. Yu, D. Singh, H. Krakauer, Phys. Rev. B 43 (1991) 6411.
[32] C. Li, A.J. Freeman, Phys. Rev. B 43 (1991) 780.
[33] T. Urano, T. Kanaji, J. Phys, Soc. Jpn. 57 (1988) 3403.
[34] E. Wimmer, H. Krakauer, M. Weinert, A.J. Freeman, Phys. Rev. B 24 (1981) 864.
[35] M. Weinert, E. Wimmer, A.J. Freeman, Phys. Rev. B 26 (1982) 4571.
[36] K. Nakamura, T. Ito, A.J. Freeman, L. Zhong, J. Fernandez-de-Castro, Phys. Rev. B 67 (2003), 014420.
[37] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[38] M. Weinert, R.E. Watson, J.W. Davenport, Phys. Rev. B 32 (1985) 2115.
[39] G.H.O. Daalderop, P.J. Kelly, M.F.H. Schuurmans, Phys. Rev. B 41 (1990) 1919.
[40] K. Nakamura, R. Shimabukuro, Y. Fujiwara, T. Akiyama, T. Ito, A.J. Freeman, Phys. Rev. Lett. 102 (2009), 187201.
[41] M. Weinert, G. Schneider, R. Podloucky, J. Redinger, J. Phys.: Condens. Matter 21 (2009), 084201.

[42] P.V. Ong, N. Kioussis, D. Odkhuu, P. Khalili Amiri, K.L. Wang, G.P. Carman, Phys. Rev. B 92 (2015) 020407(R).

[43] We have carefully checked results for CCCCCC/ but we could not get an agreement in the sign of $E^{\text{MA}}$ to that in Ref. 7 even when the in-plane lattice constant was reduced by 6 % where the $E^{\text{MA}}$ results in -0.6 meV/unit-area.

[44] M.J.M. Pires, A.A.C. Cotta, M.D. Martins, A.M.A. Silva, W.A.A. Macedo, J. Magn. Magn. Mater. 323 (2011) 789.

[45] S. Peng, M. Wang, H. Yang, L. Zeng, J. Nan, J. Zhou, Y. Zhang, A. Hallal, M. Chshiev, K.L. Wang, Q. Zhang, W. Zhao, Sci. Rep. 5 (2015) 18173.

[46] By settling the in-plane lattice constant to the bulk value of CoFe in FCFCFC/, the positive MA energy of 0.87 meV/unit-area was obtained.

[47] A. Hallal, H.X. Yang, B. Dieny, M. Chshiev, Phys. Rev. B 88 (2013), 184423.

[48] R. Kikuchi, Phys. Rev. 81 (1951) 988.

[49] J.M. Sanchez, D. de Fontaine, Phys. Rev. B 17 (1978) 2926.

[50] $E_{\text{MA}}(\mathbf{k})$ in Fig. (c) is averaged for the magnetizations oriented along the <100> and <010> directions.

[51] D.S. Wang, R. Wu, A.J. Freeman, Phys. Rev. B 47 (1993) 14932.