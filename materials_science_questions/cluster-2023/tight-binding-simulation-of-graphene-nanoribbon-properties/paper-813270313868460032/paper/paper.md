![](./images/813270313868460032_1.jpg)
Physics Letters A 377 (2012) 112-117

Contents lists available at SciVerse ScienceDirect

# Physics Letters A
www.elsevier.com/locate/pla
![](./images/813270313868460032_2.jpg)

# Electronic and magnetic properties of chevron-type graphene nanoribbon edge-terminated by oxygen atoms
![](./images/813270313868460032_3.jpg)

Wei Fa $^{a, *}$, Jian Zhou $^{b}$

$^{a}$ Group of Computational Condensed Matter Physics, National Laboratory of Solid State Microstructures and Department of Physics, Nanjing University, Nanjing 210093, China
$^{b}$ Department of Materials Science and Engineering, Nanjing University, Nanjing 210093, China

---

## ARTICLE INFO

**Article history:**
Received 24 August 2012
Received in revised form 1 November 2012
Accepted 3 November 2012
Available online 7 November 2012
Communicated by R. Wu

**Keywords:**
Chevron-type graphene nanoribbon
O termination
Magnetic properties
First-principle calculations

---

## ABSTRACT

The electronic and magnetic properties of the O-terminated chevron-type zigzag-edge graphene nanoribbons (CZGNIR) connected by two different kinds of kink angles $(120^{\circ}$ or $60^{\circ})$ have been investigated by the first-principle calculations. It is found that the O termination on the CZGNR induces the richer electronic and magnetic features than on the straight zigzag-edge graphene nanoribbons, which are sensitive to their widths, lengths, and kink angles. Interestingly, asymmetric edge terminations with O and H atoms can be used to produce some ferromagnetic semiconductors of CZGNR, giving a new approach to tailor the GNR's properties and designing the carbon-based magnetic materials.

© 2012 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Current trends in miniaturization of electronic devices have motivated a growing interest in various nanoscale structures, among which the graphene nanoribbons (GNR) constitute an important class as possible passive and active components in carbon-based nanoelectronics [1-18]. The GNR are narrow and straight-edged stripes of graphene, or single-layer graphite, which can be thought as an unfolded single-walled carbon nanotube (SWCNT). However, the GNR possess two edges to make them showing different physical features from the SWCNT. For instance, the zigzag-edge GNR (ZGNR) is a semiconductor with two localized electronic edge states, which are ferromagnetically ordered in the same edge but antiferromagnetically coupled to each other [7,11-15]. More interestingly, these ZGNR may become half-metallic when an external electric field is applied across the ribbon, presenting a possibility of it in spintronics application [1,16-18].

The GNR's edges also bring new opportunities to functionalize it at edges by different elements and chemical groups. Theoretical studies have shown that the edge termination is highly important to make the GNR stable thermodynamically. And it can be used to further control the GNR's electronic and magnetic properties. Z. Li et al. suggested that the half-metallicity of ZGNR can be enhanced by asymmetric edge terminations, offering a new method to design spin filter devices [19]. H. Lee et al. indicated that the presence of a dangling band is most crucial to the formation of carbon magnetism, and thus the magnetic moment at the edge of bare ZGNR is much larger than that with the H passivation [20]. Compared to H termination, edge oxidation by the ketone or the ether group is energetically more favorable, suggesting that the GNR's edges will be oxidized in the presence of oxidizing species [21,22]. Previous density functional theory (DFT) calculations in the local spin-density approximation [22,23] showed that edge oxygen atoms eliminate the band gap in the ZGNR and render them metallic, that is, the oxygen-terminated ZGNR are unpolarized. However, the hybrid DFT calculations indicated that the O-terminated ZGNR become zero-band gap semiconductors with increasing ribbon width and there is a discontinuous transition from a nonmagnetic state to an antiferromagnetic ground state as the number of zigzag rows increases from 2 to 3 [24]. In spite of disagreements between standard and hybrid DFT calculations, it is certain that oxygen modification along edges can impact on the electronic and magnetic properties of ZGNR.

The GNR can be produced experimentally by using chemical, sonochemical and lithographic methods as well as through the unzipping of carbon nanotubes [3,4,25-30]. However, it has still been difficult to achieve the atomic-scale control to produce the GNR with a precise width and edge direction. Recently, J.M. Cai et al. developed a bottom-up route to make atomically precise fabrication of GNR [31]. They synthesized not only the straight armchair

* Corresponding author.
E-mail address: wfa@nju.edu.cn (W. Fa).

0375-9601/$ - see front matter © 2012 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.physleta.2012.11.009

<table>
<caption>Table 1: Relative total energies of O-terminated CZGNR under different spin configurations and the band gap in the lowest-energy spin state (all in unit of meV). The energies of NM states are set to 0. The ground states are marked with boldface. Some initial spin configurations cannot be stable, which are converged to either a NM or a metastable ferrimagnetic state, and thus the symbols “–” are used. The average binding energies (BE) of the lowest-energy spin states are also listed in the last column in unit of eV.</caption>
<thead>
<tr>
<th>Structure</th>
<th>NM</th>
<th>FM</th>
<th>AFM-S</th>
<th>AFM-LR</th>
<th>AFM-G</th>
<th>GAP</th>
<th>BE</th>
</tr>
</thead>
<tbody>
<tr>
<td>ZO (3, 6)</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>−92.10</td>
<td>−96.03</td>
<td>155.2</td>
<td>−6.94</td>
</tr>
<tr>
<td>ZO (4, 6)</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>−80.74</td>
<td>−81.71</td>
<td>146.7</td>
<td>−7.14</td>
</tr>
<tr>
<td>ZO (5, 6)</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Metallic</td>
<td>−7.28</td>
</tr>
<tr>
<td>ZO (6, 6)</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Metallic</td>
<td>−7.37</td>
</tr>
<tr>
<td>ZO (3, 8)</td>
<td>0</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Metallic</td>
<td>−6.94</td>
</tr>
<tr>
<td>ZO (3, 10)</td>
<td>0</td>
<td>–</td>
<td>−60.14</td>
<td>19.92</td>
<td>–</td>
<td>211.6</td>
<td>−6.95</td>
</tr>
<tr>
<td>ZO (3, 12)</td>
<td>0</td>
<td>–</td>
<td>−21.96</td>
<td>7.62</td>
<td>–</td>
<td>Metallic</td>
<td>−6.95</td>
</tr>
<tr>
<td>ZA (3, 8)</td>
<td>0</td>
<td>−287.83</td>
<td>−276.67</td>
<td>–</td>
<td>–</td>
<td>Metallic</td>
<td>−7.07</td>
</tr>
<tr>
<td>ZA (3, 10)</td>
<td>0</td>
<td>–</td>
<td>−11.50</td>
<td>−74.12</td>
<td>−76.46</td>
<td>41.10</td>
<td>−7.08</td>
</tr>
<tr>
<td>ZA (4, 10)</td>
<td>0</td>
<td>–</td>
<td>−38.27</td>
<td>−88.01</td>
<td>−90.34</td>
<td>30.07</td>
<td>−7.13</td>
</tr>
</tbody>
</table>

GNR with only seven carbon chains but also the chevron-type GNR (CGNR) by using surface-assisted coupling of molecular precursors into linear polyphenylenes and their subsequent cyclodehydrogen-eration.

The CGNR contains two segments of normal straight GNR, connected by a particular kink angle, in its unit cell. Its unique geometrical structure can induce distinct properties from the straight GNR. For example, thermoelectric properties of CGNR are enhanced and less sensitive to edge geometries [32–35]. Even before the experimental observations of CGNR [31], the first-principle calculations were carried out to explore its electronic properties in condition with hydrogen saturations [36]. It is found that the H-terminate chevron-type zigzag-edge GNR (CZGNR) with a $120^\circ$ kink angle are generally semiconducting with a direct band gap, which is dependent on the ribbon's width and periodic length. They also indicated that the magnetic properties of CZGNR are closely related to their ratio of width to periodic length, which differs remarkably from those of the bare CZGNR with the specific antiferromagnetical (AFM) behavior [37]. Up to date, there are no more studies of the CZGNR terminated with different chemical groups, such as oxygen that is commonly assumed to passivate the ribbon edges during the GNR fabrication processes.

Therefore, in this Letter, the first-principle DFT calculations have been done to investigate the electronic and magnetic properties of the O-terminated chevron-type GNR. For the purpose of comparison with the previous works [36,37], the CZGNR composed of two same ZGNR's segments connected by a kind angle of $120^\circ$ or $60^\circ$ in a unit cell have been considered only. On the other hand, we have also noted that the magnetic properties of armchair-edge CGNR may be probably more interesting. Contrast to the normal straight armchair-type GNR that its armchair edges are not spin polarized at all, our preliminary calculations have shown that magnetic moments can be found at the zigzag-type atoms lying at kink positions of the armchair-type CGNR. The systematical studies of bare and O-terminated armchair-edge CGNR are under further calculations. For the O-terminated CZGNR, it is found that the O termination makes their magnetic properties depend on their widths, lengths, and kink angles, showing a more complicated relationship between their geometrical structures and magnetic properties. Interestingly, asymmetric edge terminations with O and H atoms can induce the ferromagnetic behavior for some CZGNR, giving a new approach to tailor the ZGNR's physical properties and design the nanometer-ferromagnets.

## 2. Calculation method and model

Our numerical simulations were carried out by the first-principle calculations in the spin-polarized generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof exchange-correlation [38]. The Vienna $ab$ initio simulation package (VASP) is employed [39,40], in which the ion-electron interaction is described by the highly accurate full-potential projected augmented wave method [41,42]. The $2s$ and $2p$ orbitals of the carbon and oxygen atoms are treated as valence orbitals and a plane-wave cutoff of 520 eV is employed throughout. To simulate the quasi-one-dimensional CZGNR, a tetragonal supercell was adopted with at least $10$ Å of the nearest distance between two neighboring CZGNR. All atoms and the lattice constant along the ribbons are relaxed until the maximum residual forces on atoms are smaller than $0.02$ eV/Å. The CZGNR is taken to be along the $x$ direction, and a $n_k \times 1 \times 1$ $k$-point mesh is used in the energy calculation. The $n_k$ is changed for different length CZGNR, which is taken by the formula: $n_k \geqslant 50/L_x$ ($L_x$ is the lattice constant of $x$ direction). A much denser $k$ point is used to calculate the band structure and density of states.

In our calculations, the CZGNR are constructed by two same ZGNR's segments, connected by a kink angle of $120^\circ$ or $60^\circ$, which are marked as ZO- or ZA-CGNR ("Z" represents zigzag edge shape; "O" or "A" represents the obtuse ($120^\circ$) or acute ($60^\circ$) kink angle), respectively. According to the structural definition of CZGNR [37], two integers $(n, m)$ can be used to characterize its width and periodic length, which represent the number of carbon chains in its width and length direction, respectively. All edge atoms are saturated by oxygen or hydrogen atoms to remove the dangling bonds.

As is well known, the GNR's zigzag edge shows magnetic moments and the magnetic ground state of the O-terminated CZGNR is sensitive to the initial condition. To explore its magnetic couplings, we have constructed several spin configurations as the initial magnetic state: (i) nonspin polarization (NM), (ii) ferromagnetic coupling for all the edges (FM), (iii) ferromagnetic ordering along each edge but AFM coupling between the up and down edges (AFM-S), (iv) ferromagnetic coupling for the same segment but AFM coupling between the left and right segments (AFM-LR), (v) ferromagnetic ordering along each edge but AFM coupling between all the neighboring edges (AFM-G). The five above-mentioned initial magnetic configurations have also been considered for the bare CZGNR [37]. For the O-terminated CZGNR, both the ferromagnetic and AFM couplings between the neighboring C and O atoms are considered in the initial (iii) to (v) spins. Finally, we have performed the binding energy calculations to verify the structural stability of the ground states of the O-terminated CZGNR considered here. The average binding energy ($E_\text{b}$) is defined as $E_\text{b} = (E_\text{tot} - N_\text{C}*E_\text{C} - N_\text{O}*E_\text{O})/N$, where $E_\text{tot}$, $E_\text{C}$, and $E_\text{O}$ are the total energies of the O-terminated CZGNR, carbon atom, and oxygen atom, respectively. $N_\text{C}$ and $N_\text{O}$ are the atomic numbers of carbon and oxygen, respectively, and $N$ is the number of total atoms in a unit cell. The obtained results are listed in the last column of Table 1, from which it is found that all of the O-terminated CZGNR have negative binding energies of about $(-6.9)$–$(-7.4)$ eV, indicating that they are favorable in energy. Also, the frequency

![](./images/813270313868460032_4.jpg)

Fig. 1. (Color online.) Electronic and magnetic structures of O-terminated ZO (3,6) in the AFM-G configuration. (a) Band structure. The blue solid and red dashed lines represent the spin-up and spin-down band, respectively. (b) Spin polarized charge density. The spin-up and spin-down charge densities are represented by yellow and cyan, respectively. Carbon and oxygen atoms are depicted by dark grey and red balls, respectively. (c)-(e) Projected density of states to the $p_x$, $p_y$, and $p_z$ orbitals of the oxygen atom, marked by a circle in Fig. 1(b).

check has been conducted on some O-terminated CZGNR. No imaginary frequencies in the harmonic frequency calculations are found to make sure that they are real local minima on the potential energy surface.

## 3. Results and discussion
### 3.1. The influence of oxygen termination on the CZGNR with a $120^\circ$ kink angle

Firstly, we have investigated the electronic and magnetic properties of O-terminated ZO-type CGNR with different widths and periodic lengths, which are ZO (3,6) to ZO (6,6), and ZO (3,8) to ZO (3,12). The obtained relative total energies and the band gaps of the lowest-energy states (if have) have been summarized in Table 1, from which it is seen clearly that the electronic and magnetic structures of the O-terminated ZO-type CGNR are very sensitive to their widths and periodic lengths. For each O-terminated ZO-type CGNR considered here, the initial FM state could not be stable and is converged finally to a NM state or a metastable ferromagnetic state.

Taking the O-terminated ZO (3,6) as an example, we have found that its ground state is the AFM-G configuration, for which the band structure, spin charge density, and partial density of states (PDOS) of one edge oxygen atom are depicted in Fig. 1. As shown in Fig. 1(a), the O-terminated ZO (3,6) is a semiconductor with a narrow band gap of 155.2 meV, which is different from the straight O-terminated ZGNR that is a NM metal predicted by previous standard DFT calculations [23,24]. This band gap is much smaller than that of the bare ZO (3,6) (about 650 meV) [37].

Though the ZO (3,6) holds the AFM-G state after oxygen saturation, the spin charge density illustrated in Fig. 1(b) is distinct from that of the bare ZO (3,6) since the magnetic moments locate mainly on the oxygen atoms in the former but on the zigzag-edge C atoms in the latter. Oxygen termination compensates the dangling bonds of the bare ZO (3,6), making the zigzag-edge C atoms lose their magnetic moments. PDOS of the edge oxygen atom shown in Fig. 1(c) indicates that the spin-up and spin-down DOS are split obviously for the $p$ orbitals of O atom, which is responsible for the system's magnetism. The local magnetic moments have been calculated by the Bader charge analysis method to give a quantitative concept of the magnetism in the O-terminated ZO-type CGNR [43]. It is found that the absolute values of local magnetic moments at oxygen atoms of ZO (3,6) in the AFM-G configuration vary from $0.11\mu_{\text{B}}$ to $0.31\mu_{\text{B}}$, which are more than ten times larger than those induced on their next nearest-neighboring carbon atoms. The local moments in other spin configurations are also found to have similar values as in the AFM-G configuration. These magnetic moments are much smaller than those of the zigzag-edge C atoms in the bare ZO-type CGNR (about $0.9\mu_{\text{B}}$) [37], confirming that the dangling bonds at the edges contribute mainly to the local moments [20].

The effects of widths and lengths on the electronic and magnetic properties of O-terminated ZO-type CGNR have been considered. Different from the semiconductor behavior of the bare ZO (n,6) with an oscillatory band gap for $n=3$-$6$ [37], it is seen clearly from Table 1 that there exists a semiconductor-metal transition for the O-terminated ZO (n,6) as the number of carbon chains in the width direction increases from $n=4$ to $n=5$. The obtained results of the O-terminated ZO (4,6) are very similar to those of the O-terminated ZO (3,6), which is an AFM-G semiconductor with a smaller band gap of 146.7 meV. However, the O-terminated ZO (n,6) becomes a nonmagnetic metal when $n\geqslant5$, as for the straight CGNR with O saturation. The length effect of the O-terminated ZO (3,m) is more complex, showing an oscillatory behavior between semiconductor and metal, depending on the odd or even $m/2$. As listed in Table 1, the O-terminated ZO (3,6) and ZO (3,10) are semiconductor, but the O-terminated ZO (3,8) and ZO (3,12) are metal, which is quite different from the bare ZO-type CGNR and straight ZGNR. Fig. 2 shows the band structures of some O-terminated CZGNR with different widths and lengths, from which it is seen clearly that their band structures are much

![](./images/813270313868460032_5.jpg)

Fig. 2. (Color online.) Band structures of the O-terminated (a) ZO (4,6), (b) ZO (5,6), (c) ZO (3,8), and (d) ZO (3,10) in their ground-state spin configurations. The blue solid and red dashed lines represent the spin-up and spin-down band, respectively.

![](./images/813270313868460032_6.jpg)

Fig. 3. (Color online.) Spin polarized charge densities of O-terminated ZO (3,12) in two different spin configurations, obtained from the different initial states: (a) AFM-S and (b) AFM-LR, respectively. The spin-up and spin-down charge densities are denoted by yellow and cyan.

more sensitive to their geometric structures, displaying no obvious band-shift near the Fermi level.

For the longer O-terminated ZO (3,10) and ZO (3,12), the ground state becomes the AFM-S configuration. The spin polarized charge density profiles of O-terminated ZO (3,12) in two different spin configurations, obtained from the initial AFM-S, and AFM-LR states, respectively, are shown in Fig. 3(a) and 3(b), from which it is seen that the magnetic moments mainly localize on the oxygen atoms in these two different spin configurations. The initial FM and AFM-G states are not stable for the O-terminated ZO (3,12) after DFT calculations and so not presented in Fig. 3. In the lowest-energy AFM-S configuration shown in Fig. 3(a), the spin directions on the oxygen atoms at kink positions are opposite to those on other oxygen atoms lying on the same side. The AFM-LR state of O-terminated ZO (3,12) depicted in Fig. 3(b) is metastable, which is 29.58 meV higher in energy than the ground state.

The ground state of O-terminated ZO (3, m) varies from the AFM-G configuration to the NM one and then to the AFM-S spin as m increases from $m=6$ to 12, showing that the magnetic properties of O-terminated ZO-type CNGRs are very sensitive to their geometric structures, especially to their periodic lengths, which can be exploited for spin-based materials and nanodevices.

### 3.2. Seeking the FM CGNR

We have also considered the effects of oxygen saturation on some CZGNR with a kink angle of $60^\circ$, which are ZA (3,8), ZA (3,10), and ZA (4,10) (see also Table 1). It is found that the magnetic properties of O-terminated CZGNR are also dependent on their kink angle. For example, the calculated results for the O-terminated ZA (3,8) indicate interestingly that the FM configuration is its ground state, which is more stable by 11.16 and 287.83 meV in energy than the AFM-S and NM configurations, respectively. The lowest-energy FM state of the O-terminated ZA (3,8) is in contrast to the NM state of the O-terminated ZO (3,8). The different magnetic properties between the O-terminated ZO-type and ZA-type CGNR with same widths and periodic lengths are mainly caused by the different kink geometries between both ZO-type and ZA-type CGNR. The upper edge of ZA (3,8) has two pairs of armchair-type C atoms as shown in Fig. 4(a), but that of ZO (3,8) has only one [44].

For the O-terminated ZA (3,8), the local moments at the oxygen atoms labeled as "O₁", "O₂", and "O₃" in Fig. 4(a) are 0.307, 0.076, and $0\mu_B$, respectively. That is, here, the magnetic moments localize only on the O atoms bonded with two armchair-type C atoms. The oxygen atoms on the other three segments have similar magnetic moment values. There are also some induced magnetic moments on the armchair-type C atoms, which are smaller than those on their bonded O atoms. It is seen clearly from Fig. 4(a) that the oxygen atoms bonded to the armchair C atoms contribute mostly to the total magnetic moment. By analyzing its band structure and PDOS shown in Fig. 4(b)-4(e), the O-terminated ZO (3,8) is a FM metal since there is a finite density of states at the Fermi level. Some flat-bands appears around $E_F$, as shown clearly in Fig. 4(b), causing the higher local density of states at there, which would induce the FM ordering if the interaction between the band electrons is introduced. By comparing the total DOS and PDOSs contributed by the oxygen and carbon atoms, respectively (except the armchair-edge C atoms that possess induced moments), it is found that there exist the higher DOS just below $E_F$, which

![](./images/813270313868460032_7.jpg)

Fig. 4. (Color online.) Calculated results of the O-terminated ZA (3,8) in the FM configuration: (a) Spin polarized charge density, (b) band structure, and (c) total DOS, (d) PDOS of all oxygen atoms, (e) PDOS of all carbon atoms except those on the armchair edges. Here, the red and dark grey balls represent the oxygen and carbon atoms, respectively.

![](./images/813270313868460032_8.jpg)

Fig. 5. (Color online.) Electronic and magnetic structures of ZO (3,6) asymmetrically terminated by oxygen and hydrogen atoms. (a) Spin polarized charge density. Carbon, oxygen and hydrogen atoms are depicted by dark grey, red, and green balls, respectively. (b) Band structure. The blue solid and red dashed lines represent the spin-up and spin-down band, respectively.

are almost totally contributed by the terminated oxygen atoms. The PDOS of oxygen atoms are spin polarized, making the O-terminated ZA (3,8) composite a FM metal with a total magnet moment of about $2\mu_{B}$ in its one unit cell.

As is well known, it is predicted that asymmetric terminations can significantly change the electronic, magnetic, and transport properties of ZGNR [13,19,20]. It is interesting to see the effect of asymmetric edge terminations on the electronic and magnetic properties of the CZGNR. Here, we have illustrated the ZO (3,6) terminated by O on its up-left segment but H on the three others in Fig. 5. In contract to the complete H- or O-terminated ZO (3,6) that is a NM or AFM-G semiconductor [36], it is seen clearly from Fig. 5(b) that the asymmetric edge terminations create a FM semiconductor with an indirect band gap of 222.84 meV, which possesses robust magnetic properties even under ambient conditions since it is well separated from other states by above 200 meV. The charge transfer from H to C makes the zigzag-edge carbon atoms participate in the $sp^{2}$ bonding network, but the charge transfer from C to O only supplies about one electron to each terminated O atom, meaning that the oxygen atom has still one valence electron without its partnership. These unsaturated O atoms induce some flat-bands near $E_{F}$, introducing the FM ordering in the ZO (3,6)

asymmetrically terminated by O and H atoms. The Bader charge analysis indicates the local moments on three terminated O atoms are 0.17, 0.39, and $0.28\mu_B$, respectively, and its total magnetic moment in one unit cell is about $1\mu_B$.

## 4. Summary

In conclusion, the influence of oxygen terminations on the electronic and magnetic properties of CZGNR has been studied using the *ab initio* calculations. It is found that the oxygen termination can change greatly their electronic structures, showing a close relationship between their magnetic properties and geometric structures, including the widths, lengths, and kink angles. The O-terminated ZO (3, 6) and ZO (4, 6), ZA (3, 10) and ZA (4, 10) have an AFM-G ground state, but the AFM-S configuration is the lowest-energy one for the O-terminated ZO (3, 10) and ZO (3, 12), all of which oxygen atoms contributes mainly to the formation of local magnets. Interestingly, it is shown that the O-terminated ZA (3, 8) is a ferromagnetic metal and asymmetric edge termination can tailor the magnetic properties of CZGNR to produce the ferromagnetic semiconductors, which may be helpful for designing GNR-based ferromagnets.

## Acknowledgements

The work was supported by the State Key program for basic researches of China through grant No. 2009CB929504 and the Natural Science Foundation of China under grant No. 11074107.

## References

[1] Y. Son, M.L. Cohen, S.G. Louie, Nature 444 (2006) 347.
[2] C. Berger, Z. Song, X. Li, X. Wu, N. Brown, C. Naud, D. Mayou, T. Li, J. Hass, A.N. Marchenkov, E.H. Conrad, P.N. First, W.A. de Heer, Science 312 (2006) 1191.
[3] X. Li, X. Wang, L. Zhang, S. Lee, H. Dai, Science 319 (2008) 1229.
[4] L. Jiao, L. Zhang, X. Wang, G. Diankov, H. Dai, Nature 458 (2009) 877.
[5] M.Y. Han, B. Özyilmaz, Y. Zhang, Philip Kim, Phys. Rev. Lett. 98 (2007) 206805.
[6] E. Kan, Z. Li, J. Yang, J.G. Hou, J. Am. Chem. Soc. 130 (2008) 4224.
[7] V. Barone, O. Hod, G.E. Scuseria, Nano Lett. 6 (2006) 2748.
[8] P.G. Silvestrov, K.B. Efetov, Phys. Rev. Lett. 98 (2007) 016802.
[9] F. Molitor, A. Jacobsen, C. Stampfer, J. Güttinger, T. Ihn, K. Ensslin, Phys. Rev. B 79 (2009) 075426.
[10] L. Yang, C.H. Park, Y.W. Son, M.L. Cohen, S.G. Louie, Phys. Rev. Lett. 99 (2007) 186801.

[11] Y.W. Son, M.L. Cohen, S.G. Louie, Phys. Rev. Lett. 97 (2006) 216803.
[12] A. Yamashiro, Y. Shimoi, K. Harigaya, K. Wakabayashi, Phys. Rev. B 68 (2003) 193410.
[13] Z. Li, H. Qian, J. Wu, B.L. Gu, W.H. Duan, Phys. Rev. Lett. 100 (2008) 206802.
[14] L. Pisani, J.A. Chan, B. Montanari, N.M. Harrison, Phys. Rev. B 75 (2007) 064418.
[15] O. Hod, J.E. Peralta, G.E. Scuseria, Phys. Rev. B 76 (2007) 233401.
[16] E. Rudberg, P. Salek, Y. Luo, Nano Lett. 7 (2007) 2211.
[17] E.J. Kan, Z.Y. Li, J.L. Yang, J.G. Hou, Appl. Phys. Lett. 91 (2007) 243116.
[18] E.J. Kan, X.J. Wu, Z.Y. Li, X.C. Zeng, J.L. Yang, J.G. Hou, J. Chem. Phys. 129 (2008) 084712.
[19] Z. Li, B. Huang, W. Duan, J. Nanosci. Nanotechnol. 10 (2010) 5374.
[20] H. Lee, Y.W. Son, N. Park, S. Han, J. Yu, Phys. Rev. B 72 (2005) 174431.
[21] O. Hod, V. Barone, J.E. Peralta, G.E. Scuseria, Nano Lett. 7 (2007) 2295.
[22] G. Lee, K. Cho, Phys. Rev. B 79 (2009) 165440.
[23] D. Gunlycke, J. Li, J.W. Mintmire, C.T. White, Appl. Phys. Lett. 91 (2007) 112108.
[24] A. Ramasubramaniam, Phys. Rev. B 81 (2010) 245413.
[25] S.S. Datta, D.R. Strachan, S.M. Khamis, A.T.C. Johnson, Nano Lett. 8 (2008) 1912.
[26] J. Campos-Delgado, J.M. Romo-Herrera, X.T. Jia, D.A. Cullen, H. Muramatsu, Y.A. Kim, T. Hayashi, Z. Ren, D.J. Smith, Y. Okuno, T. Ohba, H. Kanoh, K. Kaneko, M. Endo, H. Terrones, M.S. Dresselhaus, M. Terrones, Nano Lett. 8 (2008) 2773.
[27] A.L. Elias, A.R. Botello-Méndez, D. Meneses-Rodríguez, V.J. González, D. Ramírez-González, L. Ci, E. Muñoz-Sandoval, P.M. Ajayan, H. Terronest, M. Terrones, Nano Lett. 10 (2010) 366.
[28] S. Masubuchi, M. Ono, K. Yoshida, K. Hirakawa, T. Machida, Appl. Phys. Lett. 94 (2008) 082107.
[29] L.Y. Jiao, X.R. Wang, G. Diankov, H.L. Wang, H.J. Dai, Nature Nanotechnol. 5 (2010) 321.
[30] L. Liu, Y.L. Zhang, W.L. Wang, C.X. Gu, X.D. Bai, E.G. Wang, Adv. Mater. 23 (2011) 1246.
[31] J. Cai, P. Ruffieux, R. Jaafar, M. Bieri, T. Braun, S. Blankenburg, M. Muoth, A.P. Seitsonen, M. Saleh, X. Feng, K. Müllen, R. Fasel, Nature 466 (2010) 470.
[32] Y. Chen, T. Jayasekera, A. Calzolari, K.W. Kim, M. Buongiorno Nardelli, J. Phys.: Condens. Matter 22 (2010) 372202.
[33] F. Mazzamuto, V. Hung Nguyen, Y. Apertet, C. Caër, C. Chassat, J. Saint-Martin, P. Dollfus, Phys. Rev. B 83 (2011) 235426.
[34] W. Huang, J.S. Wang, G. Liang, Phys. Rev. B 84 (2011) 045410.
[35] J. Haskins, A. Kinaci, C. Sevik, H. Sevincli, G. Cuniberti, T. Cağin, ACS Nano 5 (2011) 3779.
[36] X. Wu, X.C. Zeng, Nano Res. 1 (2008) 40.
[37] J. Zhou, T. Hu, J. Dong, Carbon, submitted for publication.
[38] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865.
[39] G. Kresse, J. Hafner, Phys. Rev. B 48 (1993) 13115.
[40] G. Kresse, J. Furthmüller, Comput. Mater. Sci. 6 (1996) 15.
[41] P.E. Blöchl, Phys. Rev. B 50 (1994) 17953.
[42] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758.
[43] W. Tang, E. Sanville, G. Henkelman, J. Phys.: Condens. Matter. 21 (2009) 084204.
[44] An armchair-type C atom has only two nearest-neighbor (NN) C atoms, but one of NN C atoms has three NN C atoms and the other has two NN C atoms. In contrast, a zigzag-type C atom also has two NN C atoms, but each NN atom has three NN C atoms.