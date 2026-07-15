# Vacancy diffusion in $Cu\sum = 5[0\ 0\ 1]$ twist grain boundary
Yan-Ni Wen $^{a,b,*}$, Jian-Min Zhang $^{a}$, Wan-Min Yang $^{a}$, Ke-Wei Xu $^{c}$

$^{a}$ College of Physics and Information Technology, Shaanxi Normal University, Xian 710062, Shaanxi, PR China
$^{b}$ Ankang University, Ankang 725000, Shannxi, PR China
$^{c}$ State Key Laboratory for Mechanical Behavior of Materials, Xian Jiaotong University, Xian 710049, Shaanxi, PR China

---

## ARTICLE INFO
**Article history:**
Received 26 September 2008
Received in revised form 5 March 2009
Accepted 5 March 2009
Available online 17 March 2009

**Keywords:**
Cu
Vacancy
MAEAM
Diffusion
Grain boundary

---

## ABSTRACT
Both the formation energies and the diffusive activation energy of a single vacancy migrating intra- and inter-layer in the first four atomic planes near $Cu\sum = 5[0\ 0\ 1]$ twist GB have been investigated by means of MD in conjunction with MAEAM. The effects of the GB on the vacancy formation and migration are only to the third layer. The vacancy is favorable to be formed on the un-coincident site in the first, second and third layers near the GB plane and this case is enhanced successively following the third, second and first layers. A single vacancy either on un-coincident site or on coincident site in the forth, third and second layers is favorable to migrate to un-coincident site (its first-nearest-neighbor) in its adjacent layer near the GB. But for the first layer, the favorable migration path of the vacancy on the un-coincident site is between un-coincident sites of the first layer or to its nearest-neighbor of the first layer in the rotating grain, which is not the case for the vacancy on the coincident site '1' that is migrated difficultly. So, there are collective tendency of the vacancy in the GB.

© 2009 Elsevier B.V. All rights reserved.

---

## 1. Introduction
The diffusion of atoms on grain boundaries (GBs) plays an important role in many boundary phenomena such as grain growth [1,2], impurity segregation [3], deformation [4] and fracture [5], etc. A number of experiments have been conducted to investigate the basic properties of GBs, for instance the mobility, diffusivity, and basic concepts like the Read-Shockley model of low angle boundaries [6] or the compensation effect [7,8] evolved from these results. Regardless of these achievements there is virtually no theory of self-diffusion in grain boundary to date.

In this paper, both the formation energy and the activation energy of a single vacancy diffusion intra- and inter-layer in the first four atomic planes near $Cu\sum = 5[0\ 0\ 1]$ twist GB have been investigated by means of MD in conjunction with the modified analytical embedded-atom method (MAEAM) modified by Zhang et al. [9-12] from analytical embedded-atom method (AEAM) of Johnson [13-16]. In our previous paper, the MAEAM has been used successfully to the calculations of the diffusive activation energy of the vacancy in the surface [17], the surface energy [18,19], the GBs energy [20,21] and the interfaces energy [22].

---

## 2. Computational methods
In the MAEAM, the total energy of a system $E_t$ is expressed as [23]
$$
E_t = \sum_i F(\rho_i) + \frac{1}{2} \sum_i \sum_{j(\neq i)} \phi(r_{ij}) + \sum_i M(P_i) \tag{1}
$$

$$
\rho_i = \sum_{j(\neq i)} f(r_{ij}) \tag{2}
$$

$$
P_i = \sum_{j(\neq i)} f^2(r_{ij}) \tag{3}
$$

where $F(\rho_i)$ is the energy to embed an atom in site $i$ with electron density $\rho_i$, which is given by a linear superposition of the spherical averaged atomic electron density of other atoms $f(r_{ij})$, $r_{ij}$ is the separation distance of atom $j$ from atom $i$, $\phi(r_{ij})$ is the interaction potential between atoms $i$ and $j$, and $M(P_i)$ is the modified term that describes the energy deviation from the linear superposition of atomic electronic density. The embedding function $F(\rho_i)$, pair potential $\phi(r_{ij})$, modified term $M(P_i)$ and atomic electron density $f(r_{ij})$ are taken as following forms [24-26]

$$
F(\rho_i) = -F_0 \left[ 1 - n \ln\left( \frac{\rho_i}{\rho_e} \right) \right] \left( \frac{\rho_i}{\rho_e} \right)^n \tag{4}
$$

$$
\phi(r_{ij}) = k_0 + k_1 \left( \frac{r_{ij}}{r_{1e}} \right)^2 + k_2 \left( \frac{r_{ij}}{r_{1e}} \right)^4 + k_3 \left( \frac{r_{1e}}{r_{ij}} \right)^{12} \tag{5}
$$

---
* Corresponding author at: College of Physics and Information Technology, Shaanxi Normal University, Normal University Road 1#, Xian 710062, Shaanxi, PR China. Tel.: +86 15929535551.
E-mail address: wenyanni353@sohu.com (Y.-N. Wen).

0169-4332/$ - see front matter © 2009 Elsevier B.V. All rights reserved.
doi:10.1016/j.apsusc.2009.03.012

$$
M\left(P_{i}\right)=\alpha\left(\frac{P}{P_{e}}-1\right)^{2} \exp \left(-\left(\frac{P}{P_{e}}-1\right)^{2}\right)
\tag{6}
$$

$$
f\left(r_{i j}\right)=f_{e}\left(\frac{r_{1 e}}{r_{i j}}\right)^{6}
\tag{7}
$$

where the subscript $e$ indicates equilibrium state and $r_{1 e}$ is the first-nearest-neighbor distance at equilibrium. The cut-off distance of interaction potential for FCC metals $r_{c e}$, where the pair potential and its slope are zero, lies between the second- and the third-nearest-neighbor distance. That is $r_{c e}=r_{2 e}+0.75\left(r_{3 e}-r_{2 e}\right) . F_{0}$ and $f_{e}$ are the model parameters, which are chosen as [25]

$$
F_{0}=E_{c}-E_{1 v}^{f}
\tag{8}
$$

$$
f_{e}=\left[\frac{E_{c}-E_{1 v}^{f}}{\Omega}\right]^{3 / 5}
\tag{9}
$$

where $E_{c}$ and $E_{1 v}^{f}$ are measured cohesion energy and isolated vacancy formation energy and $\Omega=a^{3} / 4$ is the atomic volume in FCC metals and $a$ is the lattice constant.

Six parameters $(n, \alpha, k_{0}, k_{1}, k_{2}$ and $k_{3})$ for Cu in Eqs. (4)-(6) can be determined by fitting the cohesion energy $E_{c}$, isolated vacancy formation energy $E_{1 v}^{f}$, lattice constant $a$ and elastic constants $C_{11}$, $C_{12}$ and $C_{44}$. According to the principle that the energy vs. separation distance curve fits the Rose equation [16], we will have

$$
n=\sqrt{\frac{\Omega\left(C_{11}+2 C_{12}\right)\left(C_{11}-C_{12}\right)}{216 E_{1 v}^{f} C_{44}}}
\tag{10}
$$

$$
\alpha=\frac{\Omega\left(C_{12}-C_{44}\right)}{32}-\frac{n^{2} F_{0}}{8}
\tag{11}
$$

The potential parameters can be calculated with the following formulae [26]

$$
k_{0}=-\frac{E_{1 v}^{f}}{9}-\frac{\Omega\left(5481 C_{44}+2989 C_{12}-2989 C_{11}\right)}{42,840}
\tag{12}
$$

$$
k_{1}=\frac{\Omega\left(1311 C_{44}+939 C_{12}-939 C_{11}\right)}{9520}
\tag{13}
$$

$$
k_{2}=\frac{\Omega\left(-33 C_{44}-32 C_{12}+32 C_{11}\right)}{1020}
\tag{14}
$$

$$
k_{3}=\frac{8 \Omega\left(9 C_{44}+C_{12}-C_{11}\right)}{5355}
\tag{15}
$$

The input physical parameters and the calculated model parameters for Cu are listed in Tables 1 and 2, respectively.

<table>
<thead>
<tr>
<th colspan="6">Table 1<br>The input physical parameters of Cu [25].</th>
</tr>
</thead>
<tbody>
<tr>
<td>$a$ (nm)</td>
<td>$E_{c}$ (eV)</td>
<td>$E_{1v}^{f}$ (eV)</td>
<td>$C_{11}$ (eV nm⁻³)</td>
<td>$C_{12}$ (eV nm⁻³)</td>
<td>$C_{44}$ (eV nm⁻³)</td>
</tr>
<tr>
<td>0.36147</td>
<td>3.49</td>
<td>1.17</td>
<td>1050</td>
<td>760</td>
<td>470</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="7">Table 2<br>The calculated model parameters of Cu for MAEAM.</th>
</tr>
</thead>
<tbody>
<tr>
<td>$n$</td>
<td>$F_{0}$ (eV)</td>
<td>$\alpha$ (eV)</td>
<td>$k_{0}$ (eV)</td>
<td>$k_{1}$ (eV)</td>
<td>$k_{2}$ (eV)</td>
<td>$k_{3}$ (eV)</td>
</tr>
<tr>
<td>0.2722</td>
<td>2.32</td>
<td>0.0855</td>
<td>−0.6011</td>
<td>0.4265</td>
<td>−0.0721</td>
<td>0.0695</td>
</tr>
</tbody>
</table>

The molecular dynamics (MD) method [27] is used in the lattice relaxation resulted from the existence of the vacancies. The forces applied to the $i$ atom from other atoms are calculated by

$$
\begin{aligned}
& f_{i}^{\alpha}=-\frac{\partial E_{i}}{\partial r_{i j}^{\alpha}}= \\
& -\left[F^{\prime}\left(\rho_{i}\right) \sum_{j(\neq i)} f^{\prime}\left(r_{i j}\right) \frac{r_{i j}^{\alpha}}{r_{i j}}+\frac{1}{2} \sum_{j(\neq i)} \phi^{\prime}\left(r_{i j}\right) \frac{r_{i j}^{\alpha}}{r_{i j}}+2 M^{\prime}\left(P_{i}\right) \sum_{j(\neq i)} f\left(r_{i j}\right) f^{\prime}\left(r_{i j}\right) \frac{r_{i j}^{\alpha}}{r_{i j}}\right]
\end{aligned}
\tag{16}
$$

$$
E_{i}=F\left(\rho_{i}\right)+\frac{1}{2} \sum_{j(\neq i)} \phi\left(r_{i j}\right)+M\left(P_{i}\right)
\tag{17}
$$

where the superscript $\alpha$ (=x, y and z) in $f_{i}^{\alpha}$ and $r_{i j}^{\alpha}$ represents the $\alpha$th component of the force $f_{i}$ and the separation distance $r_{i j}$ of atom $j$ from atom $i$. $E_{i}$ is the energy contribution from atom $i$. The position vector of the $i$ atom $\vec{r}_{i}$ is a function of time. When the increment of time $\Delta t$ is minute, the $\vec{r}_{i}$ can be outspread by Taylor series. So the coordinate $\vec{r}_{i}(t+\Delta t)$ of the atom $i$ at time $t$ by the method of predictor–corrector [28],

$$
\vec{r}_{i}^{\epsilon}(t+\Delta t)=\vec{r}_{i}(t)+\dot{\vec{r}}_{i}^{*}(t) \Delta t+\frac{1}{2} \frac{\vec{f}_{i}\left(\vec{r}_{i}\right)}{m} \Delta t^{2}
\tag{18}
$$

where $\vec{r}_{i}^{\epsilon}(t+\Delta t)$ is the coordinate predicted at time $t+\Delta t, \dot{\vec{r}}_{i}^{*}(t)=\partial \vec{r}_{i}(t) / \partial t$ is the velocity of atom $i$ at time $t$ and $\vec{f}_{i}\left(\vec{r}_{i}\right)=-\partial E_{i} / \partial t$ is the resultant force applied to atom $i$.

## 3. Computational and discussion

In an infinite twist GB, the coincident site lattice (CSL) can be generated by rotating one of the two adjacent grain about their common axis (taken as z-axis here) until its lattice vector in its own coordinate becomes coincident with the vector of the un-rotating one. The reciprocal planar coincident density of crystal lattices $(\sum)$ can be represented by the atomic number in the smallest unit cell of CSL on each plane. The periodic boundary condition can be employed to reduce the number of atoms for representing the structure of the infinite twist GB. Fig. 1 shows the $\sum=5\left[\begin{array}{llll}0 & 0 & 1\end{array}\right]$ twist GB structure of the FCC metals and four identical smallest coincident unit cells. Two-dimensional coordinates $x$ and $y$ are defined for the un-rotating grain in which the atom sites on adjacent two $\left(\begin{array}{lll}0 & 0 & 1\end{array}\right)$ lattice planes are represented by open circles (the five atoms in each unit cell of CSL are indicated by red numbers '1' to '5') and open squares (the five atoms are indicated by blue

![](./images/811866560695107584_1.jpg)

Fig. 1. The $\sum=5\left[\begin{array}{llll}0 & 0 & 1\end{array}\right]$ twist grain boundary model of the FCC metal viewed along z-axis ($n$ was the natural number 1, 2, 3, etc.).

letters 'a' to 'e') for odd layer $(2n-1)$L and even layer $2n$L, respectively. Similarly, two-dimensional coordinates $x_{\text{R}}$ and $y_{\text{R}}$ are selected to be attached to the rotating grain in which the atom sites on adjacent two $(0\ 0\ 1)$ lattice planes are represented by open triangles (the five atoms in each unit cell of CSL are indicated by purple letters 'a$_{\text{R}}$' to 'e$_{\text{R}}$') and open rhombuses (the five atoms are indicated by brown numbers '1$_{\text{R}}$' to '5$_{\text{R}}$') for odd layer $(2n-1)$L$_{\text{R}}$ and even layer $2n$L$_{\text{R}}$, respectively. The subscript 'R' implies the parameter in the rotating grain throughout the paper.

Considering the equivalence between the rotating and un-rotating grains, the initial sites of a single vacancy in different layers of the un-rotating grain should be considered only. Furthermore, as can be seen easily from Fig. 1, only the vacancy sited initially at three positions such as the red numbers '1' to '3' for the odd layers or blue letters 'a' to 'c' for the even layers should be considered, since the smallest unit cell of CSL has a two-fold rotating axis paralleled z-axis through its center 'a' as well as 'a$_{\text{R}}$' and thus the sites '5' and '4' are equivalent to '2' and '3' or 'e' and 'd' are equivalent to 'b' and 'c', respectively.

A super-cell with 30 layers is used in computation for each grain, which consists of a computational cell of free atoms surrounded by a mantle of atoms fixed at their perfect lattice positions. The computational cell is a $5a \times 5a \times 10a$ ($5a \times 5a \times 5a$ for each grain) crystal, where $a$ is the lattice constant. A vacancy in different layers is created by removing an atom from corresponding layer. The formation energy of the vacancy $E_{f}$ can be calculated by [29]

$$
E_{f}=E(N-1,1)-E(N,0)+E_{c} \tag{19}
$$

where $E(N-1,1)$ is the energy of the computational cell containing $N-1$ atoms and a single vacancy, $E(N,0)$ the energy of the perfect computational cell containing $N$ atoms but without any vacancies and $E_{c}$ is the cohesion energy and compensates for the missing atom. The migrating activation energy $Q_{v}$ of the vacancy is obtained by

$$
Q_{v}=E_{sad}-E_{eq}+E_{v} \tag{20}
$$

where $E_{sad}$ and $E_{eq}$ stand for the system energy with the vacancy in the saddle point and initial equilibrium site of each path.

Calculated formation energy $E_{f}$ of a single vacancy in the first four layers near the GB and in the bulk are listed in Table 3 with the experimental [30] values for comparing. The negative formation energy $-0.2288$ eV of the vacancy on un-coincident site '2' or '3' of the 1L means that the formation of the vacancy on un-coincident site is spontaneous. This is because, as can be seen in Fig. 1, the distance between the atoms at sites 'c$_{\text{R}}$' and 'b$_{\text{R}}$' (open triangles and purple letters) on the first layer 1L$_{\text{R}}$ of rotating grain and the atoms at sites '2' and '3', respectively, is very close and thus resulting in the repulsive force. On the coincident site '1' of the 1L, 1.1814 eV energy is needed. In the 2L, the lower formation energy of 1.1669 eV on the un-coincident site ('b' or 'c') is lower than the one on coincident site '1' of the 1L that is lower than the one 1.1836 eV on coincident site 'a' of the 2L. However, in the 3L, the lower formation energy of 1.1834 eV on the un-coincident site ('2' or '3') in the 3L is higher than the higher one 1.1829 eV on the coincident site 'a' of the 2L and the higher formation energy of 1.1836 eV on coincident site '1' is lower than the value of 1.1838 eV on all sites of the 4L which is close to the experiment value of 1.17 eV [30]. So we conclude that the vacancy is favorable to be formed on the un-coincident site in each layer near the GB plane and this case is enhanced as the atomic layer closes increasingly to the GB. This is in consistent with the experimental observations [31].

<table><caption>Table 3
The calculated vacancy formation energy $E_{f}$ (eV).</caption>
<tbody>
<tr>
<th>Site</th>
<th colspan="5">Layer</th>
</tr>
<tr>
<th></th>
<th>1L</th>
<th>2L</th>
<th>3L</th>
<th>4L</th>
<th>Bulk</th>
</tr>
<tr>
<td>1(a)</td>
<td>1.1814</td>
<td>1.1829</td>
<td>1.1836</td>
<td>1.1838</td>
<td>1.1838, 1.17 (exp.)</td>
</tr>
<tr>
<td>2(b)</td>
<td>–0.2288</td>
<td>1.1669</td>
<td>1.1834</td>
<td>1.1838</td>
<td></td>
</tr>
<tr>
<td>3(e)</td>
<td>–0.2288</td>
<td>1.1669</td>
<td>1.1834</td>
<td>1.1838</td>
<td></td>
</tr>
</tbody>
</table>

As shown in Fig. 2, for intra-layer diffusion of the vacancy, only four nearest-neighbor sites of the vacancy are considered and the determined diffusive activation energies $Q_{v}$ are displayed with the red (for 1L and 3L) and blue (for 2L and 4L) values. For inter-layer diffusion of the vacancy, as shown in Fig. 3, there are four possible paths to its first-nearest-neighbor in the adjacent layer are considered and the determined diffusive activation energies $Q_{v}$ are displayed with the red (for 3L–2L), blue (for 2L–1L and 4L–3L) and purple (for 5L–4L) values. This is not the case for the vacancy sited initially on the un-coincident site in the 1L to migrate through GB plane to 1L$_{\text{R}}$, only two paths in length nearly equal to the first-nearest-neighbor distance are considered and the determined diffusive activation energies $Q_{v}$ are displayed with the red values. It can be seen that the same diffusive activation energy of 2.3738 eV, which is close to the experiment value of 2.19 eV for bulk [32], is obtained for intra-layer migration of 4L and inter-layer migration of 5L–4L. Combining the formation energy (see Table 3),

![](./images/811866560695107584_2.jpg)
![](./images/811866560695107584_3.jpg)

Fig. 2. The diffusive activation energy (eV) of the vacancy migrating in (a) 1L (red values) and 2L (blue values), and (b) 3L (red values) and 4L (blue values) of the Cu$\sum$ = 5[0 0 1] twist grain boundary. (a) 1L and 2L (b) 3L and 4L. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

![](./images/811866560695107584_4.jpg)

Fig. 3. The diffusive activation energy (eV) of the vacancy migrating between (a) 1L-1LR (red values) and 2L-1L (blue values), (b) 3L-2L (red values), 4L-3L (blue values) and 5L-4L (purple values) of the Cu$\sum$ = 5[0 0 1] twist grain boundary. (a) 1L-1LR and 2L-1L (b) 3L-2L, 4L-3L and 5L-4L. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of the article.)

we know that the effects of the GB on the vacancy formation and migration are only to the third layer.

The detail variations of system energies with the distance of a vacancy diffused intra-layer of 1L, 2L, 3L and 4L, and inter-layer of 1L-1LR, 2L-1L, 3L-2L, 4L-3L and 5L-4L are shown in Figs. 4 and 5, respectively.

It can be seen that from Fig. 4, the effects of the GB on the intra-layer migration are mainly for 1L, the favorable migration mechanisms are between un-coincident sites that is '2' and '3' or '4', '3' and '2' or '5', the highest $Q_v$ corresponding to the migration between coincident site '1' and un-coincident site '2' or '3' are resulted from the atoms 'cR' as well as 'bR' on the 1LR are very close to the migration path (see Fig. 1). Furthermore, all the saddle point of the eight energy-displacement curves deviates observably the midpoint of the migration paths. The effects of the GB on the intra-layer migration decrease for 2L-2L, 3L-3L and 4L-4L successively away from the GB plane. All the saddle points locate at the midpoint of the migration paths.

Similar results are also obtained for inter-layer migrations of 1L-1LR, 2L-1L, 3L-2L, 4L-3L and 5L-4L as can be seen from Fig. 5, the effects of the GB on the inter-layer migration are mainly for 1L-1LR and 2L-1L related to the 1L. First, for migration between 1L and 1LR, the favorable migration mechanisms are between '2' and 'cR', and '3' and 'bR'. Second, the vacancy either on coincident site 'a' or un-coincident-site 'b' or 'c' of the 2L is easily to migrate to the un-coincident site (its first-nearest-neighbor) of the 1L. Third, all the energy-displacement curves except for the ones between coincident site and un-coincident are unsymmetrical and the saddle point

![](./images/811866560695107584_5.jpg)

Fig. 4. Variations of system energies with the distance of a vacancy migrating intra-layer of 1L, 2L, 3L and 4L of the Cu$\sum$ = 5[0 0 1] twist grain boundary.

![](./images/811866560695107584_6.jpg)

Fig. 5. Variations of system energies with the distance of a vacancy migrating inter-layer of 1L-1LR, 2L-1L, 3L-2L, 4L-3L and 5L-4L of the Cu$\sum$ = 5[0 0 1] twist grain boundary.

deviate observably the midpoint of the migration paths. Further-more, the effects of the GB on the inter-layer migration decrease for 3L-2L, 4L-3L and 5L-4L successively away from the GB plane. All the saddle points locate at the midpoint of the migration paths.

Comparing the relative large number of the activation energies of the vacancy migration intra- and inter-layer, we know that a single vacancy either on un-coincident site or on coincident site in the 4L, 3L and 2L is favorable to migrate to un-coincident site (its first-nearest-neighbor) in its adjacent layer near the GB. But for the 1L, the favorable migration path of the vacancy on the un-coincident site '2' or '3' is between un-coincident sites of the 1L or from '2' or '3' to 'c_R' or 'b_R' of the 1L_R, which is not the case for the

vacancy on the coincident site '1' that is migrated difficultly. So,
there are collective tendency of the vacancy in the GB, which is the
same with the experiment [31].

## 4. Conclusion

Both the formation energies and the diffusive activation energy
of a single vacancy migrating intra- and inter-layer in the first four
atomic planes near $Cu\sum = 5[0\ 0\ 1]$ twist GB have been investigated
by means of MD in conjunction with MAEAM. The following
conclusion can be obtained.

(1) Combining the formation energy and the relative large number
of the activation energies of the vacancy migration intra- and
inter-layer, we know that the effects of the GB on the vacancy
formation and migration are only to the third layer.

(2) The vacancy is favorable to be formed on the un-coincident site
in the first, second and third layers near the GB plane and this
case is enhanced following the third, second and first layers.
This is in consistent with the experimental observations.

(3) A single vacancy either on un-coincident site or on coincident
site in the forth, third and second layers is favorable to migrate
to un-coincident site (its first-nearest-neighbor) in its adjacent
layer near the GB. But for the first layer, the favorable migration
path of the vacancy on the un-coincident site '2' or '3' is between
un-coincident sites of the first layer or from '2' or '3' to 'c_R' or 'b_R'
of the first layer in the rotating grain, which is not the case for
the vacancy on the coincident site '1' that is migrated difficultly.
So, there are collective tendency of the vacancy in the GB.

## Acknowledgements

The authors would like to acknowledge the State Key
Development Program for Basic Research of China (Grant No.
2004cb619300) and the Colleage Program (2007AKXY023) for
providing financial support for this research.

## References

[1] J.M. Zhang, K.W. Xu, Acta Phys. Sin. 52 (2003) 145.
[2] J.M. Zhang, K.W. Xu, M.R. Zhang, Acta Phys. Sin. 52 (2003) 1207.
[3] S.Y. Wang, C.Y. Wang, D.L. Zhao, J. Alloys Compd. 368 (2004) 301.
[4] C.P. Chang, P.L. Sun, P.W. Kao, Acta Mater. 48 (2000) 3377.
[5] J.M. Zhang, K.W. Xu, Chin. Phys. 13 (2004) 205.
[6] W.T. Read, W. Shockley, Phys. Rev. 78 (1950) 275-289.
[7] D.A. Molodov, Fakultät für Bergbau, Hüttenwesen und Geowissenschaften,
Institut für Metallkunde und Metallphysik, Shaker Verlag, RWTH Aachen, 1999.
[8] G. Gottstein, L.S. Shvindlerman, Interface Sci. 6 (1998) 265.
[9] B.W. Zhang, Y.F. Ouyan, Phys. Rev. B 48 (1993) 3022.
[10] B.W. Zhang, Y.F. Ouyan, S.Z. Liao, Z.P. Jin, Phys. B 262 (1999) 218.
[11] W.Y. Hu, B.W. Zhang, B.Y. Huang, F. Gao, D.J. Bacon, Phys. Condens. Mater. 13
(2001) 1193.
[12] W.Y. Hu, B.W. Zhang, X.L. Shu, B.Y. Huang, J. Alloys Compd. 287 (1999) 159.
[13] R.A. Johnson, Phys. Rev. B 37 (1988) 3924.
[14] D.J. Oh, R.A. Johnson, J. Mater. Res. 3 (1988) 471.
[15] R.A. Johnson, D.J. Oh, J. Mater. Res. 4 (1989) 1195.
[16] R.A. Johnson, Phys. Rev. B 41 (1990) 471.
[17] Y.N. Wen, J.M. Zhang, K.W. Xu, Appl. Surf. Sci. 253 (2007) 8620.
[18] Y.N. Wen, J.M. Zhang, Solid State Commun. 144 (2007) 163.
[19] Y.N. Wen, J.M. Zhang, Comp. Mater. Sci. 42 (2007) 281.
[20] J.M. Zhang, X.M. Wei, H. Xin, Appl. Surf. Sci. 242 (2005) 55.
[21] X.M. Wei, J.M. Zhang, K.W. Xu, Appl. Surf. Sci. 253 (2007) 5214.
[22] J.M. Zhang, H. Xin, X.M. Wei, Appl. Surf. Sci. 246 (2005) 14.
[23] X.L. Shu, W.Y. Hu, H.N. Xiao, H.Q. Deng, J. Mater. Sci. Technol. 17 (2001)
601.
[24] W.Y. Hu, X.L. Shu, B.W. Zhang, Comput. Mater. Sci. 23 (2002) 175.
[25] F. Fang, X.L. Shu, H.Q. Deng, W.Y. Hu, M. Ahu, Mater. Sci. Eng. A 355 (2003)
357.
[26] R.A. Johnson, Phys. Rev. B 39 (1989) 12554.
[27] R.W. Smith, D.J. Srolovitz, J. Appl. Phys. 79 (1996) 1448.
[28] J.R. Beeler Jr., Radiation Effects Computer Experiments, Amsterdam, North
Holland, New York, 1983.
[29] E.T. Chen, R.N. Barnett, U. Landman, Phys. Rev. B 41 (1990) 439.
[30] C. Kittle, Introduction to Solid Physics, 5th ed., John Wiley & Sons, 1976.
[31] S.M. Schwarz, B.W. Kempshall, L.A. Giannuzzi, F.A. Stevie, Acta Mater. 50 (2002)
5079.
[32] J.R. Cahoon, O.D. Sherby, M.S. Metall, Trans. A 23 (1992) 2491.