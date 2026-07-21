# Electronic band structure of helical iodine chains

Dmitry Rybkovskiy\*,¹,², Alexander Osadchy¹, and Elena Obraztsova¹

¹A.M. Prokhorov General Physics Institute, Russian Academy of Sciences, 38 Vavilov street, 119991 Moscow, Russia
²Moscow State Institute of Radio Engineering, Electronics and Automation (Technical University), 78 Vernadskogo Prospect, 119454 Moscow, Russia

Received 18 September 2012, accepted 19 September 2012
Published online 8 November 2012

**Keywords** atomic chains, electronic structure, iodine, nanotechnology, nanotubes, tight binding

*Corresponding author: e-mail rybkovskiyd@gmail.com, Phone: +7(499)503-8362, Fax: +7(499)503-8357

The electronic band structure of helical iodine chains was calculated within the empirical tight binding approach. The screw symmetry of the system was used to reduce the size of the problem to a single atom with four atomic orbitals. The overlap parameters were fitted to reproduce the DFT results for a linear iodine chain. The obtained results for helical chains have shown the energy band splitting due to the overlap between p orbitals introduced by the structure twisting. The splitting magnitude depends on the pitch of the helix.

© 2012 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

## 1 Introduction
Various experimental investigations show that iodine can form unique one-dimensional structures inside carbon nanotubes with the geometry depending on the tube diameter [1, 2]. For a specific diameter range of the nanotubes (from $1.05 \pm 0.05$ to $1.40 \pm 0.05$ nm [2]) iodine crystallizes in form of single, double, and triple helical chains. The formation of these structures is believed to be possible due to the electron transfer from the nanotube to iodine, which tends to stabilize the iodine chain. Beside single linear chains, helices with a diameter of 0.65 nm and periodicities of 5 and 12.5 nm were observed [1, 2]. The distance between the carbon atoms of the nanotube and the iodine is about 0.35 nm, close to the graphite interlayer spacing. Doping of carbon nanotubes with iodine enhances their conductivity making such nanocomposites attractive for electronic applications. This effect is related to the Fermi energy shift of nanotubes induced by the above-mentioned charge transfer.

In this work, we study the iodine chains electronic structure and its dependence on the chain geometry. A direct calculation of an iodine helix embedded in a carbon nanotube faces the problem of incommensurability of these structures, requiring the use of large unit cells. The second problem of such approach is the lack of physical transparency of the resulting electron dispersion, which is difficult to interpret. To investigate the energy bands of the iodine helices, we consider them as stand-alone structures, neglecting the influence of the nanotubes. This approximation can be justified by the fact that the spacing between the walls of the nanotube and the iodine chain is sufficiently large (about 0.35 nm [1]) and the main formation mechanism of the chains is related to the charge transfer to iodine from the tube, with no covalent bonding between them. Furthermore, observations in Ref. [2] have not revealed any correlation between the helical structure of iodine chains and the nanotube helicity.

Further simplification of the problem can be made without loss of accuracy by using not the translational, but the screw symmetry of the atomic helices. The generalization of the Bloch theorem to the systems with screw symmetry was made by the analysis of the electronic structure of polymers [3]. Similar considerations were successfully applied to calculate the electronic structure of carbon nanotubes [4–7], reducing the size of the problem to only 2 or even 1 carbon atoms. Chiral nanotubes with point defects [8] and spin-orbit splitting effects in nanotube band structures [9] were investigated with help of screw symmetry. In the case of a helical atomic chain, the problem simplifies to a single atom independent from the translational periodicity of the helix. As it will be shown, within the empirical tight binding approach, the electron dispersions of these one-dimensional structures can be calculated by the diagonalization of a simple $4 \times 4$ Hamiltonian matrix.

© 2012 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim

2 Theory A helical atomic chain can be defined by its radius $R$, an interatomic distance $d$ and a screw angle $\theta$ (as shown in Fig. 1). By applying the screw operations (i.e. translation $h$ along $z$-axis and rotation $\theta$ around it), to a single atom one can obtain the whole helical structure. The Cartesian coordinates of the atom with a number $n$ are given by

$$
\begin{aligned}
\boldsymbol{r}_{n} &=(R \cos (n \theta), R \sin (n \theta), n h), \\
h &=n \sqrt{d^{2}-4 R^{2} \sin ^{2}(\theta / 2)}.
\end{aligned} \tag{1}
$$

In case $R \geq(d / 2)$, we have a restriction for the screw angle $0 \leq \theta \leq 2 \arcsin (d / 2 R)$.

To calculate the energy bands of the iodine chains we use the empirical tight binding model with the $\mathrm{sp}^{3}$ basis set with $\mathrm{s}, \mathrm{p}_{\eta}, \mathrm{p}_{\tau}, \mathrm{p}_{z}$ orbitals. The $\mathrm{p}_{\eta}$ and $\mathrm{p}_{\tau}$ are normal and tangential orbitals, which are decomposed into conventional $\mathrm{p}_{x}$ and $\mathrm{p}_{y}$, orbitals as follows:

$$
\begin{aligned}
p_{\eta} &=\cos (n \theta) p_{x}+\sin (n \theta) p_{y}, \\
p_{\tau} &=-\sin (n \theta) p_{x}+\cos (n \theta) p_{y}
\end{aligned} \tag{3}
$$

The tight binding Hamiltonian is built in the basis of symmetry adapted Bloch sums:

$$
\Phi_{m, \kappa}(\boldsymbol{r})=\frac{1}{\sqrt{N}} \sum_{n} \mathrm{e}^{\mathrm{i} \kappa n h} \chi_{m}\left(\boldsymbol{r}-\boldsymbol{r}_{n}\right), \tag{4}
$$

where $N$ is the number of atoms in the spiral, $n$ is the number of screw operations, i.e. the number of atom, $\chi_{m}(\boldsymbol{r}-\boldsymbol{r}_{n})$ is the Löwdin orbital, centered on atom $n$, $m$ labels the orbital type and runs over $\mathrm{p}_{\eta}, \mathrm{p}_{\tau}, \mathrm{p}_{z}, \mathrm{s}$. $\kappa$ is a continuous wave vector equal to $2 \pi k / h$ with $-1 / 2<k \leq 1 / 2$. The wavefunction is constructed as a linear combination of Bloch sums (4):

$$
\Psi_{\kappa}(\boldsymbol{r})=\sum_{m} C_{m} \Phi_{m, \kappa}(\boldsymbol{r}) \tag{5}
$$

![](./images/813271284703035393_1.jpg)

Figure 1 (online color at: www.pss-b.com) The atomic structure of a helical iodine chain.

To obtain an accurate band structure, we take into account the interaction between the first and the second nearest neighbors. Within these approximations, we derive the $4 \times 4$ Hamiltonian matrix and calculate the electronic bands $E(\boldsymbol{k})$ by solving the secular equation:

$$
\left|\begin{array}{cccc}
H_{11}-E(\boldsymbol{k}) & H_{12} & H_{13} & H_{14} \\
H_{12}^{*} & H_{22}-E(\boldsymbol{k}) & H_{23} & H_{24} \\
H_{13}^{*} & H_{23}^{*} & H_{33}-E(\boldsymbol{k}) & H_{34} \\
H_{14}^{*} & H_{24}^{*} & H_{34}^{*} & H_{44}-E(\boldsymbol{k})
\end{array}\right|=0,
$$

$$
H_{11}=E_{p}+2 \sum_{n=1}^{2} \cos (2 \pi k)\left(\cos (n \theta) E_{x, x_{n}}+\sin (n \theta) E_{x, y_{n}}\right),
$$

$$
H_{22}=E_{p}-2 \sum_{n=1}^{2} \cos (2 \pi k)\left(\sin (n \theta) E_{x, y_{n}}-\cos (n \theta) E_{y, y_{n}}\right),
$$

$$
H_{33}=E_{p}+2 \sum_{n=1}^{2} \cos (2 \pi k) E_{z, z_{n}},
$$

$$
H_{44}=E_{s}+2 \sum_{n=1}^{2} \cos (2 \pi k) E_{s, s_{n}},
$$

$$
H_{12}=-2 i \sum_{n=1}^{2} \sin (2 \pi k)\left(\sin (n \theta) E_{x, x_{n}}-\cos (n \theta) E_{x, y_{n}}\right),
$$

$$
H_{13}=-2 i \sum_{n=1}^{2} \sin (2 \pi k) E_{x, z_{n}},
$$

$$
H_{14}=-2 \sum_{n=1}^{2} \cos (2 \pi k) E_{s, x_{n}},
$$

$$
H_{23}=2 \sum_{n=1}^{2} \cos (2 \pi k) E_{y, z_{n}},
$$

$$
H_{24}=-2 i \sum_{n=1}^{2} \sin (2 \pi k) E_{s, y_{n}},
$$

$$
H_{34}=-2 i \sum_{n=1}^{2} \sin (2 \pi k) E_{s, z_{n}}.
$$

The overlap parameters $E_{i, j}$ are decomposed into $\sigma$ and $\pi$ components according to Slater and Koster [10]. The values of these parameters were obtained by fitting the energy bands to the results, obtained from a DFT computation of a linear iodine chain, performed within the ABINIT pseudopotential plane wave code [11, 12]. We used an interatomic distance $d$ equal to $2.9 \mathring{A}$, which is close to the average distances in iodine molecular ions [13].The resulting parameters are presented in Table 1. For calculations of helical chains, the interaction parameters, corresponding to the second nearest neighbors were scaled, since the interatomic distances between these neighbors depend on the geometry

<table><caption>Table 1 Overlap parameters (in eV) obtained by fitting the energy bands to DFT results.</caption>
<thead>
<tr>
<th>neighbor order</th>
<th>$V_{ss\sigma}$</th>
<th>$V_{sp\sigma}$</th>
<th>$V_{pp\sigma}$</th>
<th>$V_{pp\pi}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>I</td>
<td>−0.648</td>
<td>1.327</td>
<td>2.282</td>
<td>−0.549</td>
</tr>
<tr>
<td>II</td>
<td>−0.089</td>
<td>0.133</td>
<td>0.343</td>
<td>0.052</td>
</tr>
</tbody>
</table>

of the helix. The orbital energies $E_\text{s}$ and $E_\text{p}$ are calculated to be equal to $-17.239$ and $-6.857$ eV, respectively.

We should discuss the limitations of our approach. In case of strongly twisted helices the distance between atoms on adjacent helical turns can be comparable to the interatomic distance inside the chain and this would lead to the appearance of new interatomic interactions, not taken into account within our model. Another problem arises from the use of Löwdin orbitals, which include the overlap matrix of the atomic orbitals. The change of the atomic geometry would lead to the change of the overlap integrals, and the discrepancy will increase with the twist magnitude. However, we restrict our study to realistic chain geometries, which are known to have large periodicities, and our simple model is sufficient for qualitative description of changes in the electronic structure, introduced by the twisting of the chain.

3 Results and discussion The calculated electronic band structure of a linear iodine chain ($R=0$ Å, $\theta=0$ rad) is presented in Fig. 2a. The dotted line depicts the Fermi energy. Because of the symmetry of the linear system $\text{p}_x$ and $\text{p}_y$ orbitals are decoupled from s and $\text{p}_z$ orbitals and only the mixing between s and $\text{p}_z$ states takes place. The lowest energy band is formed predominantly by s orbitals and passes from the bonding state with lower energy in the center of the first Brillouin zone to the antibonding state with higher energy at its boundary. The double degenerated energy band, corresponding to $\text{p}_x$ and $\text{p}_y$ orbitals exhibit the same behavior. In case of linear chain geometry, the normal and tangential p orbitals ($\text{p}_\eta$ and $\text{p}_\tau$) are equal to $\text{p}_x$ and $\text{p}_y$ since no rotation is introduced. The degeneracy arises from the symmetry conditions, since $\text{p}_x$ and $\text{p}_y$ orbitals of the neighboring atoms interact in the same way and do not overlap with each other. The weak interaction between these orbitals leads to a bandwidth comparable to that of s band. Due to the spatial orientation of $\text{p}_z$ orbitals (the positive lobe of $\text{p}_z$ orbital, centered on one atom points to the negative lobe of the other) the corresponding energy curve shows an antibonding character in the center of the first Brillouin zone and a bonding character at its boundary. A strong dispersion of this band is due to a strong $\sigma$-character overlap between $\text{p}_z$ orbitals. Since iodine atoms carry seven valence electrons, there is an odd number of electrons in the unit cell. This leads to the position of the Fermi energy inside the energy band.

Using the same overlap parameters, the band structures of helical iodine chains with realistic geometries (taken from Ref. [1]) were calculated. Figure 2b presents the energy bands of an iodine helix with the pitch of $125$ Å and the radius of $3.25$ Å. The corresponding screw angle $\theta$ is equal to $0.1439$ rad. The introduction of a helicity leads to a non-zero overlap between all orbitals resulting in coupling of corresponding states. This coupling splits the energy bands of $\text{p}_\eta$ and $\text{p}_\tau$ orbitals and slightly shifts all curves. The insertion in Fig. 2b shows the small splittings of about $50$ meV of the energy bands in the vicinity of their intersection. Figure 2c shows the results of a helix with the same radius and a pitch of $50$ Å ($\theta=0.3375$ rad). The increased twist results in a stronger coupling between the electronic states. p bands are split off from each other. This will lead to the appearance of the new Van Hove singularities in the electronic density of states. However, the

![](./images/813271284703035393_2.jpg)

Figure 2 (online color at: www.pss-b.com) The atomic structures of iodine chains with realistic geometrical parameters along with the corresponding band structures, obtained within the empirical tight binding model with use of the screw symmetry. (a) A linear iodine chain ($R=0$ Å, $\theta=0$ rad), (b) a helical chain with a pitch of $125$ Å ($R=3.25$ Å, $\theta=0.1439$ rad), the insertion shows the small splitting of the energy bands in the vicinity of their intersection, not visible in the main plot, (c) a helical chain with a pitch of $50$ Å ($R=3.25$ Å, $\theta=0.3375$ rad). The absolute energy values have no direct physical meaning. The dashed line depicts the position of the Fermi energy.

curvature of the energy band in the vicinity of the Fermi energy is weakly affected by the changes in the iodine chain geometry.

The presented method can be generalized to calculate the electron dispersion of more complex structures. To obtain the energy bands of double and triple iodine helices one can use not only the screw but also the rotational symmetry. In this case, the unit cell will still contain one atom, but new overlap parameters, related to the interaction between the chains would be needed. However, the spacing between the helices is reported to be equal to 0.65 nm [1], and the corresponding interactions are expected to be negligible. It is also possible to include the presence of the nanotube in the calculation. To do this, one has to construct an atomic basis of iodine and carbon atoms with equal screw axes. Unfortunately, within the present approach such compu- tation will be restricted to systems with same helical parameters and no analytical solutions will be possible due to the complexity of the problem.

4 Conclusions In the present paper, we have reported a tight binding calculation of helical iodine chains with realistic geometries. The screw symmetry was applied to simplify the calculations and obtain transparent and simple electronic band structures. The behavior of the energy bands is explained in terms of the overlaps between the atomic orbitals. The twisting of an iodine chain introduces splitting between the p energy bands in vicinity of their intersection and the magnitude of this splitting depends on the pitch of the helix. For structures with a pitch of $50\,\text{\AA}$, the appearance of new Van Hove singularities in the electronic density of states is expected.

Acknowledgements This work was supported by RFBR-12-07-90700-mob_st project, by the Russian President Grants (MK-1777.2012.2 and MK-5618.2012.2) and by FP7 IRSES 247007 project.

## References

[1] X. Fan, E. C. Dickey, P. C. Eklund, K. A. Williams, L. Grigorian, R. Buczko, S. T. Pantelides, and S. J. Pennycook, Phys. Rev. Lett. **84**, 4621 (2000).

[2] L. Guan, K. Suenaga, Z. Shi, Z. Gu, and S. Iijima, Nano Lett. **7**, 1532 (2007).

[3] J. W. Mintmire, in: Density Functional Methods in Chemistry, edited by J. Labanowski and J. Andzelm (Springer-Verlag, Berlin, 1991), pp. 125–138.

[4] C. T. White, D. H. Robertson, and J. W. Mintmire, Phys. Rev. B **47**, 5485 (1993).

[5] P. N. D’yachkov and D. V. Makaev, Phys. Rev. B **76**, 195411 (2007).

[6] M. Damnjanović, I. Milošević, E. Dobardžić, T. Vuković, and B. Nikolić, in: Applied Physics of Nanotubes: Fundamentals of Theory, Optics and Transport Devices, edited by S. V. Rotkin and S. Subramoney (Springer-Verlag, Berlin, 2005), pp. 41–88.

[7] V. N. Popov and L. Henrard, Phys. Rev. B **70**, 115407 (2004).

[8] P. N. D’yachkov, D. Z. Kutlubaev, and D. V. Makaev, Phys. Rev. B **82**, 035426 (2010).

[9] W. Izumida, K. Saito, and R. Saito, J. Phys. Soc. Jpn. **78**, 074707 (2009).

[10] J. C. Slater and G. F. Koster, Phys. Rev. **94**, 1498 (1954).

[11] X. Gonze, B. Amadon, P.-M. Anglade, J.-M. Beuken, F. Bottin, P. Boulanger, F. Bruneval, D. Caliste, R. Caracas, M. Cote, T. Deutsch, L. Genovese, P. Ghosez, M. Giantomassi, S. Geodecker, D. Hammann, P. Hermet, F. Jollet, G. Jomard, S. Leroux, M. Mancini, S. Mazevet, M. Oliveira, G. Onida, Y. Pouillon, T. Rangel, G.-M. Rignanese, D. Sangalli, R. Shaltaf, M. Torrent, M. Verstraete, G. Zerah, and J. Zwanziger, Comput. Phys. Commun. **180**, 2582 (2009).

[12] X. Gonze, G.-M. Rignanese, M. Verstraete, J.-M. Beuken, Y. Pouillon, R. Caracas, F. Jollet, M. Torrent, G. Zerah, M. Mikami, P. Ghosez, M. Veithen, J.-Y. Raty, V. Olevano, F. Bruneval, L. Reining, R. Godby, G. Onida, D. Hamman, and D. Allan, Z. Kristallogr. **220**, 558 (2005).

[13] P. H. Svensson and L. Kloo, Chem. Rev. **94**, 1649 (2003).