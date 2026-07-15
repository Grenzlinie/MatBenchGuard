# First-principle study of electronic structure of Sn-doped amorphous $\text{In}_2\text{O}_3$ and the role of O-deficiency

Maengsuk Kim $^{a}$, Il Joon Kang $^{a}$, Chul Hong Park $^{b,*}$

$^{a}$ Research Center for Dielectric Advanced Matter Physics, Department of Physics, Pusan National University, Busan 609-735, Republic of Korea
$^{b}$ Research Center for Dielectric Advanced Matter Physics, Department of Physics Education, Pusan National University, Busan 609-735, Republic of Korea

---

## ARTICLE INFO

**Article history:**
Received 16 December 2011
Received in revised form
22 May 2012
Accepted 25 May 2012
Available online 12 June 2012

**Keywords:**
Amorphous oxide
O-deficiency
ITO
Transparent conducting oxide
Microscopic structure

---

## ABSTRACT

Through the first-principle calculations, we investigate the electronic structure of Sn-doped amorphous $\text{In}_2\text{O}_3$ (a-ITO), whose structures were obtained from the melting-and-quenching process using the *ab initio* molecular dynamics (MD) simulations. According to the analysis of the short-range ording, it is found that various sub-structures are mixed, differently from the crystalline structure. Inverse participation ratio (IPR) analysis of the wavefunctions indicates that the states around the conduction band edges (CBE) are well delocalized, i.e., only slightly changed from those of crystalline $\text{In}_2\text{O}_3$-Sn. However, the serious localized states are developed near the valence band (VB) in the a-ITO. Even by the O-deficiency, the character of the CBE is little changed, but the localization around VB is enhanced, which leads to the band-gap narrowing.

© 2012 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Transparent conducting oxides (TCOs) have attracted a great deal of interest because of the co-existence of the optical transparency in the visible region and the high electrical conductivity. This unique co-existence makes them useful for a variety of applications such as the transparent conducting oxides (TCO) in the solar cell and flat panel display, and also the active semiconductor in the thin-film transistors in the Electro-chromic windows, organic light emitting diode (OLED), and so on [1]. Among them, a tin-doped $\text{In}_2\text{O}_3$, known as ITO (indium-tin oxide), is one of the most extensively used TCOs due to its high optical transmission above 80% in the visible region and the high electrical conductivity more than $10^{3}\ \Omega^{-1}\text{m}^{-2}$ as well as easy deposition [2]. Because of the increased demand for the better and In-free TCOs, the development of new TCO is still a challengeable subject, for which it is crucial to understand the fundamental properties of the ITO as a prototype of TCOs.

It is also desirable to be aware of the basic properties of ITO in amorphous phase since thin films are not in perfect crystalline phase and easily in amorphous phase by the low-T thin-film process. Despite of its significance, theoretical works have been performed mostly for crystalline ITO. Recently, a theoretical work on the electronic structures of various amorphous phases of ITO has been reported [3]. The atomic structure of a substitutional dopant in crystalline structure should be similar to that of the host atom. However, there is litte detailed analysis of the structural properties and electronic structures of the amorphous structure.

In this work, we have examined details of structural and electronic structures of a-ITO generated from the melt-and-quench *ab initio* MD simulations based on the first-principles PAW electronic structure calculations using GGA density functional. The short-range structural order are analyzed on the basis of the calculations of the effective coordination number ($\text{CN}^{*}$), the effective bond length ($d^{*}$), and the electronic properties are investigated by the analysis of the normalized inverse participation ratio (IPR) of the wavefunctions.

## 2. Computational method

We have performed the first-principles pseudopotential total energy calculations based on the density functional theory (DFT) within the generalized gradient density approximation (GGA) as implemented in the Vienna *ab initio* simulation package (VASP) [4,5]. The electron–ion interactions are described using the projected augmented-wave (PAW) method [6]. Perdew-Burke-

---

* Corresponding author. Tel.: +82 51 510 2959; fax: +82 51 515 2390.
E-mail address: cpark@pusan.ac.kr (C.H. Park.)

1567-1739/$ – see front matter © 2012 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.cap.2012.05.038

Ernzerhof (PBE) functional [7] is used for GGA exchange correlation potential. The kinetic energy cut-offs of 300 eV and 600 eV are employed for MD simulations and static structural optimizations, respectively.

We performed also the *ab initio* molecular dynamics (MD) simulations in order to generate the amorphous structures. The process for the generation of amorphous structure is the melt-and-quench MD simulation method in canonical ensemble using a Nosé thermostat [8], and a verlet algorithm is employed with a time step of between 0.5 and 2 fs. Based on the simulated annealing using MD simulations, the crystalline ITO is melted for 5 ps at 3000 K to erase the crystalline information, and decreased slowly down to 300 K. The simulated annealing was repeated between 800 K and 0 K until the total energy and the atomic structure are converged. Here, we use a 81-atom supercell composed of $(SnO_2)_2(In_2O_3)_{15}$. A k-point of (1/4, 1/4, 1/4) is used for the Brillouin zone summations.

## 3. Results and discussions

First, we examine the structural properties of stoichiometric a-ITO using a 81-atom supercell obtained from the melt-and-quench MD simulations. The obtained cell volume and total energy of a-ITO are increased by about 6.6% and 0.120 eV per atom, respectively, as compared with those of ITO in crystalline phase. To explore the microscopic structure, we calculated the integrated radial distribution function (RDF) as shown in Fig. 1(a). The integrated radial distribution function determines the total number of atoms from a particular set of atoms within a radius $r$, and in the short-range it is related to the coordination numbers. Here, we only consider the neighboring oxygens around cations. On the whole, the integrated RDF starts to increase from a certain distance, which is related to a bond length, and it becomes flat, and then increases again. It indicates that there are about 6 neighboring oxygens around Sn and In from the integrated RDF data in the first flat region. Before the first plateau appears, the integrated radial distribution function of Sn–O increases from about 2.0 Å to roughly 2.2 Å, while that of In–O enhances from about 2.0 Å to approximately 2.5 Å. It demonstrates that bond lengths between Sn and O atoms are shorter than those of In–O and In atoms showing broader RDF curve indicate the disordering.

In order to understand the more details in the short-range order of the amorphous structure, we calculated the effective coordination numbers (CN*) [9,10] and the effective bond lengths ($d^*$). The effective coordination number use a different weight for each bond length by choosing a weight function to take into account the dependence on bond length, unlike the standard coordination number using a unique weight for all bond lengths between a particular reference atom and surrounding atoms. Here, we use a weight function of exponential with power six. The effective coordination number (CN*) is defined as follows.

$$
\mathrm{CN}^{*}=\sum \exp \left[1-\left(d_{i} / d^{*}\right)^{6}\right], \tag{1}
$$

where $d_i$ is the distance between each cation and oxygen, $d^*$ the weighted average bond length (effective bond length) defined as follows:

$$
d^{*}=\frac{\sum d_{i} \exp \left[1-\left(d_{i} / d^{*}\right)^{6}\right]}{\sum \exp \left[1-\left(d_{i} / d^{*}\right)^{6}\right]}, \tag{2}
$$

where $d^*$ is determined self-consistently. The atom with smaller bond length gives the larger contribution to the (CN*). It is known that this approach has been successfully applied to TCOs and transition-metal clusters [11]. In Fig. 1(b), the effective bond lengths with respect to the effective coordination numbers are presented. The CN* and $d^*$ of In–O are spread over between 4 and 6, and $d^*$ of between 2.09 and 2.27, which demonstrates that the local structures around In are complicated by the mixture of many sub-structures. It indicates that small energies are required for the formation of these various sub-structures, which plays a role in forming amorphous phase. The $d^*$ increases with CN*, i.e., the larger CN* gives the longer effective bond length, because of repulsion between oxygen atoms. The effective bond lengths of between In and O is noted to be well-fitted to the linear line.

![](./images/813306062718369792_1.jpg)

Fig. 1. Calculated (a) integrated radial distribution functions (RDFs) and (b) effective coordination numbers (CN*) vs. effective bond lengths ($d^*$) around In and Sn for a stoichiometric a-ITO are shown. In (b), $d^*=d_0$+0.061CN* where $d_0=1.865$ for In–O.

The average values of these calculated CN* and $d^*$ are shown in Table 1. The CN* and $d^*$ between two Sn and O atoms are also shown. The obtained sub-structures for two Sn atoms are similar, but the sub-structures of Sn are different from the sub-structures of In. It is noted that there are more oxygens around Sn compared to around In. The average CN* of In is about 5.40, that is smaller than that of Sn, about 5.91, although the bond length $d^*$ of Sn–O (about 2.1 Å) is shorter than those of In–O (about 2.19 Å). It is because the valence charge of Sn is (4+), larger than that of $\text{In}^{3+}$. On the other hand, there are about 4 cations near O atoms on average.

<table>
<caption>Table 1 Calculated average effective coordination number (&lt;CN*&gt;) and effective bond length (&lt;$d^*$&gt;) around In, Sn, and O in a stoichiometric a-ITO are shown. All cations, Sn and In, are considered for an oxygen.</caption>
<thead>
<tr>
<th></th>
<th>$\text{In}^{3+}$</th>
<th>$\text{Sn}^{4+}$</th>
<th>O</th>
</tr>
</thead>
<tbody>
<tr>
<td>&lt;CN*&gt;</td>
<td>5.40</td>
<td>5.91</td>
<td>3.55</td>
</tr>
<tr>
<td>&lt;$d^*$&gt; (Å)</td>
<td>2.19</td>
<td>2.11</td>
<td>2.19</td>
</tr>
</tbody>
</table>

We examined the electronic structure of a-ITO, and the projected density of electronic states (DOS) are shown in Fig. 2. As shown by Fig. 2(b), the valence bands show the flat band dispersion, while the conduction bands demonstrate the strong band dispersion. It shows severely localized states near valence band edge, which should lead to the low hole carrier mobility and also the localization of the orbital sensitive to a perturbation such as defect and impurity. The calculated band gap is only 0.63 eV at $\Gamma$ point, that is much smaller than the experimental value [12,13] due to the well-known GGA-error. The density of states (DOS) is obtained on the basis of tetrahedral method with Blöchl electron

![](./images/813306062718369792_2.jpg)

Fig. 2. Calculated (a) electronic band structure along $\Gamma$ point (0, 0, 0) to (1/2, 0, 0) symmetry point in the units of reciprocal basis vectors and (b) total and projected density of states (DOS) per atom together with normalized inverse participation ratio (IPR) for the stoichiometric a-ITO are illustrated. Fermi level is indicated by the short-dotted line. The density of states of the conduction bands are enlarged by a factor of 8. All the energies are given with respect to the top of the valence band. Normalized IPR values were gaussian broadened.

occupation formalism. In Fig. 2(b), the topmost panel shows the total DOS (black solid line) and the panels below present the projected DOS for each atom, Sn, In, and O. The projected DOS illustrates that the valence bands consist mainly of O-2p orbitals and the lowest conduction bands mostly show In-4s orbital characters.

We analyzed the localization behavior of the electronic wavefunctions through the calculations of the normalized inverse participation ratio (IPR) according to the following equation:

$$
\mathrm{IPR}=\frac{1 / N \sum c_{i}^{4}}{\left(1 / N \sum c_{i}^{2}\right)^{2}}, \tag{3}
$$

where $c_{i}^{2}$ is the partial weight on the i-th atom of a wavefunction and N the total number of atoms in supercell. The IPR value is larger for the more localized orbital.

The average values of the IPR versus the energy are shown in Fig. 2(b). It is noted that the normalized IPR data of the states near the valence band edge are much larger than those near the conduction bands. It indicates the existence of the strongly localized states near the valence band edge which should be the band tail state. The structural disordering in the amorphous phase leads to the strong localizations of the valence band states.

An interesting finding is that the localized band-tail states are little generated for the conduction band edge. The small IPR value indicates that the CBE states are well-delocalized free-electron-like, thus the effective mass can be defined. The experimental and calculated effective masses are compared with the values from the crystalline structure in Table 2. By the LDA calculation, both the band gap and the electron effective mass of $\mathrm{In}_{2} \mathrm{O}_{3}$ in crystalline

<table>
<caption>Table 2<br>Calculational and experimental band gaps ($E_{\text{g}}$) and effective masses ($m_{\text{e}}^{*}$) of conduction band electrons for crystalline and Sn-doped amorphous $\mathrm{In}_{2} \mathrm{O}_{3}$ (a-ITO) are presented.</caption>
<thead>
<tr>
<th></th>
<th colspan="2">Crystalline $\mathrm{In}_{2} \mathrm{O}_{3}$</th>
<th colspan="2">a-ITO</th>
</tr>
<tr>
<th></th>
<th>$E_{\text{g}}$(eV)</th>
<th>$m_{\text{e}}^{*}(m_{\text{e}})$</th>
<th>$E_{\text{g}}$(eV)</th>
<th>$m_{\text{e}}^{*}(m_{\text{e}})$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Present calc.</td>
<td>1.06</td>
<td>0.17</td>
<td>0.63</td>
<td>0.16</td>
</tr>
<tr>
<td>Other calc.$^{\text{a}}$</td>
<td>0.79–1.12</td>
<td>0.15–0.23</td>
<td>0.05–0.48</td>
<td>0.13–0.16</td>
</tr>
<tr>
<td>Experiment</td>
<td>2.6–3.75$^{\text{b}}$, &lt;2.9$^{\text{c}}$</td>
<td>0.3$^{\text{d}}$</td>
<td>–</td>
<td>0.28–0.30$^{\text{e}}$</td>
</tr>
<tr>
<td colspan="5">a Ref. [3] and references therein.<br>b Ref. [12].<br>c Ref. [13].<br>d Ref. [14–16].<br>e Ref. [17].</td>
</tr>
</tbody>
</table>

phase are underestimated compared with the experimental values [12–16]. The results are similar to the other calculations [3]. In the stoichiometric amorphous phase of the ITO, the calculated electron effective mass is only 0.16 electron mass ($m_{\text{e}}$), which is interestingly smaller than that in the $\mathrm{In}_{2} \mathrm{O}_{3}$ in crystalline phase. It shows that the effective mass of conduction band edge can be reduced even in amorphous phase through Sn doping.

Now, we turn to the electronic structures of an oxygen-missing a-ITO to see how those are influenced by oxygen deficiency. We compared the RDFs of the stoichiometric and O-deficient a-ITO for structural analysis. The change of the integrated RDFs by the O-deficiency in a-ITO is illustrated in Fig. 3, together with the case of the stoichiometric structure for comparison. Over the whole, the RDFs around In are slightly reduced when oxygen atoms are eliminated from a-ITO. In the case of one-oxygen missing a-ITO, the RDF data are slightly changed, more around In atoms. However, in the two-oxygen missing case, an interesting finding is that the RDF is quite largely reduced around Sn atoms within a radius of about 3.0 Å. It indicates that the local environment around Sn is severely changed in the serious O-deficient state.

The calculated electronic band structure and total DOS, together with normalized IPR, are illustrated in Fig. 4. As previously shown in Fig. 2, the calculated total density of states are plotted with the normalized IPR of wavefunctions, according to Eq. (1). The IPR data shows the localized tail state near valence band edge, while the states near conduction band edge are quite delocalized. It means

![](./images/813306062718369792_3.jpg)

Fig. 3. Calculated integrated radial distribution functions (RDFs) of (a) Sn–O and (b) In–O are displayed for a stoichiometric (black solid lines), one-oxygen missing (pink short-dotted lines), and two-oxygen missing (blue dashed-and-dotted lines) a-ITO. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](./images/813306062718369792_4.jpg)

Fig. 4. Calculated (a) electronic band structure along $\Gamma$ point (0, 0, 0) to (1/2, 0, 0) symmetry point in the units of reciprocal basis vectors and (b) total density of states (DOS) together with normalized inverse participation ratio (IPR) for an O-deficient crystalline $\text{In}_2\text{O}_3$ are illustrated. Fermi level is indicated by the short-dotted line. All the energies are given with respect to the top of the valence band. Normalized IPR values were gaussian broadened.

that the electrons around conduction band edges are free electron-like. As presented in Fig. 4(a), by missing one oxygen from a stoichiometric a-ITO, the band gap at $\Gamma$ point is decreased from 0.63 eV to 0.42 eV by 0.21 eV. The gap reduction is mainly due to the increase of band tail states around valence band edge. The band dispersion around the CBM is little changed, which illustrates that missing one-oxygen atom plays a role of shallow donor. In Fig. 4(b), the IPR values around the conduction band minimum is also similar to a stoichiometric one. It means that the delocalized states near conduction band are influenced hardly by missing oxygen atoms. However, the increased IPR data near VB edge shows that the more localized states are developed around valence band edge due to an enhanced disordering.

## 4. Conclusions

In summary, we have performed the detailed structural and electronic structure of a stoichiometric amorphous Sn-doped $\text{In}_2\text{O}_3$ (a-ITO) on the basis of the first-principles PAW pseudopotential total energy calculation based on GGA density functional. A stoichiometric a-ITO structures were generated by the melt-and-quench *ab initio* MD simulations. It is shown that various sub-structures are mixed in a-ITO. A lot of seriously localized tail states are developed near valence band edge, while the conduction band edge state is quite delocalized in a stoichiometric a-ITO. The localization character of wavefunction was analyzed based on the normalized inverse participation ratio. The more tail states near valence band edge are induced by the O-deficiency due to increased disorder.

## Acknowledgments

This work was supported by the National Research Foundation of Korea(NRF) grant funded by the Korea government(MEST) (No. 2012-000345).

## References

[1] A. Ambrosini, A. Duarte, K.R. Poeppelmeier, M. Lane, C.R. Kannewurf, T.O. Mason, J. Solid State Chem. 153 (2000) 41.
[2] M. Ishii, T. Mori, H. Fujikawa, S. Tokito, Y. Taga, J. Lumin. 87 (2000) 1165.
[3] J. Rosen, O. Warschkow, Phys. Rev. B 80 (2009) 115215.
[4] G. Kresse, J. Hafner, Phys. Rev. B 47 (1993) 558.
[5] G. Kresse, J. Hafner, Phys. Rev. B 49 (1994) 14251.
[6] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.
[7] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[8] S. Nosé, J. Chem. Phys. 81 (1984) 511.
[9] R. Hoppe, Angew. Chem. Internat. Edit. 9 (1970) 25.
[10] R. Hoppe, Z. Kristallogr. 150 (1979) 23.
[11] J.L.F. Da Silva, J. Appl. Phys. 109 (2011) 023502.
[12] A. Walsh, J.L.F. Da Silva, S.-H. Wei, C. Körber, A. Klein, L.F.J. Piper, A. DeMasi, K.E. Smith, G. Panaccione, P. Torelli, D.J. Payne, A. Bourlange, R.G. Egdell, Phys. Rev. Lett. 100 (2008) 167402.
[13] R.L. Weiher, R.P. Ley, J. Appl. Phys. 37 (1966) 299.
[14] Y. Ohhata, F. Shinoki, S. Yoshida, Thin Solid Films 59 (1979) 255.
[15] J.M. Jarzebski, Phys. Status Solidi A 71 (1982) 13.
[16] I. Hamberg, C.G. Granqvist, K.-F. Berggren, B.E. Sernelius, L. Engström, Phys. Rev. B 30 (1984) 3240.
[17] J.R. Bellingham, W.A. Phillips, C.J. Adkins, J. Phys. Condens. Matter 2 (1990) 6207.