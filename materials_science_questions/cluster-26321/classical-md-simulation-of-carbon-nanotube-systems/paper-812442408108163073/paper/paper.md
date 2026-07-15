![](./images/812442408108163073_1.jpg)

Available online at www.sciencedirect.com

![](./images/812442408108163073_2.jpg)

Chemical Physics Letters 365 (2002) 536-541

# Reorientational motions in sub- and supercritical water under extreme confinement

J. Martí $^{a, *}$, E. Guàrdia $^{b}$, M.C. Gordillo $^{c}$

$^{a}$ Departament de Física i Enginyeria Nuclear, Universitat Politècnica de Catalunya, B5-206 Campus Nord, 08034 Barcelona, Catalonia, Spain
$^{b}$ Departament de Física i Enginyeria Nuclear, Universitat Politècnica de Catalunya, B4-205 Campus Nord, 08034 Barcelona, Catalonia, Spain
$^{c}$ Departamento de Ciencias Ambientales, Facultad de Ciencias Experimentales, Universidad Pablo de Olavide, Carretera de Utrera Km 1, 41013 Sevilla, Spain

Received 18 July 2002; in final form 26 September 2002

## Abstract

Molecular reorientational motions in confined water at sub- and supercritical conditions have been studied by molecular dynamics simulations. Carbon nanotubes were chosen as confining devices because their extremely narrow diameters. We employed a flexible version of the classical simple point charge potential to model water-water interactions and Lennard-Jones-type potentials to describe water-carbon forces. Molecular rotations in the confined systems are markedly faster than in water at room conditions. At temperatures above the boiling point and in all supercritical states, reorientational motions are basically independent of the radius of the confining tube. We can distinguish two energy domains, below and above 373 K, with an activation energy of around 15 kJ/mol.

© 2002 Elsevier Science B.V. All rights reserved.

## 1. Introduction

Molecular microscopic dynamics is crucial for the understanding of the physical and chemical properties of a substance. That type of knowledge is specially relevant in the case of liquid water, due to its particular and fascinating properties [1], especially in supercritical conditions [2]. At room temperature, water is organized forming tetrahedral units of five molecules linked by hydrogen-bonds (HBs), but when temperature is raised and/or density is reduced, part of the HBs do not survive. Most of dominant order is then lost and the remaining structures are linear and bifurcated chains of H-bonded water molecules which can be regarded as parts of broken tetrahedrals [3]. Recently much attention has been paid to the mechanisms of molecular reorientation, specially in the case of supercritical systems [4–6].

The confinement of water near surfaces or inside pores is also a relevant aspect to consider. In nature, water is confined in geological and biological systems like rocks, sands, in cellular membranes or in the surface of proteins. In order to

*Corresponding author. Fax: +34-934017100.
E-mail address: jordi.marti@upc.es (J. Martí).

0009-2614/02/$ - see front matter © 2002 Elsevier Science B.V. All rights reserved.
PII: S0009-2614(02)01529-4

![](./images/812442408108163073_3.jpg)
www.elsevier.com/locate/cplett

investigate the role of confinement in molecular reorientational motions, we have considered samples of water at different thermodynamic conditions placed inside carbon nanotubes with radii between 5.45 and 8.15 Å. Carbon nanotubes (CNs) are quasi-one dimensional rolled graphite sheets with interesting mechanical and electrical properties [7]. In previous works, we have analyzed the structure and hydrogen-bond populations of confined water at room conditions [8], as well as time-dependent properties [9,10] and the HB network of supercritical water (SW) confined in CNs [11].

In this work we have performed a series of molecular dynamics (MD) simulations with a reliable flexible potential which considers changes in the molecular geometry. We expect this property of the model will help us to take into account the fluctuations of the molecular dipole moment of water as a response to changes in the polarizability, together with changes in the orientational order due to the influence of the environment. Reorientational motions along different molecular directions and the residence time of a molecule in the shell of its first neighbors have been considered, up to our knowledge, for the first time for constrained water.

## 2. Method

A series of MD simulations for water samples at temperatures between 298 and 773 K and at densities between 0.49 and 0.83 g/cm³ have been performed for three confining cylindrical CNs of length 7.45 nm and internal radii 2.65, 4 and 5.33 Å, which, respectively, correspond to the (8,8), (10,10) and (12,12) tubes in the standard nomenclature [12]. To model CN walls we have considered Lennard-Jones-type potentials (see full discussion in [8]). Water-water interactions have been modeled by means of a flexible version [13] of the simple point charge (SPC) model [14]. This flexible potential includes internal atomic forces and it has been tested for sub- and supercritical water [3,15] being able to reproduce the main trends of the experimental structure and vibrational bands of the infrared spectrum of ambient water [16].

Periodic boundary conditions and the Ewald sum rule to compute Coulombic forces have been considered in all simulations. Our integration algorithm was a leap-frog Verlet with a time step of 0.5 fs. We applied a thermal bath [17] for the control of temperature. Translational and internal degrees of freedom were separately equilibrated [18]. Statistically meaningful properties were computed from MD runs of 250 ps after equilibration periods of 500 ps for all simulations.

## 3. Results

The reorientational motions which have been studied here are related with time correlation functions of a series of relevant unit vectors. We have computed the first and second Legendre polynomials of the unit vector associated with the molecular dipole moment $\hat{u}_{\mu}(t) \equiv \vec{\mu}(t)/\mu(t)$, the unit vector associated to the hydrogen-hydrogen distance $\hat{u}_{\text{HH}}(t) \equiv \vec{r}_{\text{HH}}(t)/r_{\text{HH}}(t)$ and the unit vector perpendicular to the instantaneous molecular plane $\hat{u}_{\perp}(t) \equiv \vec{r}_{\perp}(t)/r_{\perp}(t)$. Those vectors are depicted in Fig. 1.

The correlation functions associated with the Legendre polynomials are:

$$
\begin{aligned}
C_{1}(t)=\langle\cos \theta(t)\rangle, \quad C_{2}(t)=\frac{1}{2}\left\langle 3 \cos ^{2} \theta(t)-1\right\rangle, \\
(1)
\end{aligned}
$$

![](./images/812442408108163073_4.jpg)

Fig. 1. Auxiliary unit vectors along relevant molecular directions: $\hat{u}_{\mu}$, $\hat{u}_{\text{HH}}$ and $\hat{u}_{\perp}$. Oxygen and hydrogen atoms are also indicated.

where
$$
\theta(t) \equiv \hat{\boldsymbol{u}}(t) \cdot \hat{\boldsymbol{u}}(0) \tag{2}
$$
for each of the three unit vectors defined above.
The characteristic reorientational times $(\tau_{1}, \tau_{2})$
along each direction have been computed by:
$$
\tau_{i}=\int_{0}^{\infty} \mathrm{d} t \ C_{i}(t), \quad (i=1,2). \tag{3}
$$

The results found for the reorientational times of
the molecular dipole moment derived from the two
Legendre polynomials are displayed in Fig. 2. In
the bottom panel we observe that the value for
bulk water at room temperature is roughly the
same than the $\tau_{1}$ obtained for water confined in the
largest CN considered. For smaller CNs, we find
lower values of the reorientational time, i.e., con-
finement tends to speed up molecular reorienta-
tions. The thinner the confining CN, the faster the
reorientational motion. This effect could be at-
tributed to the partial breakdown of the tetrahe-
dral hydrogen-bond network, typical of bulk sub-
critical water, when water is severely constrained
such as in thin CN. This HB breaking can be ob-
served from the calculated hydrogen-bond popu-
lations [8,11]. It should be also noted that
rotational motions in non-hydrogen-bonded liq-
uids are faster than those of H-bonded ones
[19,20].

![](./images/812442408108163073_5.jpg)

Fig. 2. Molecular dipole moment reorientation times $\tau_{1,2}^{\mu}$ as a
function of temperature at the density of $0.83\ \text{g/cm}^3$. Compu-
tation with first (bottom) and second (top) Legendre poly-
nomials.

When we study the temperature influence we
observe that increasing the temperature quickly
reinforces the amount of disorder in the rotational
dynamics, in such a way that confinement plays
only a secondary role. That thermal effect has been
also found in MD simulations of bulk supercritical
water [6]. The upper panel of Fig. 2 shows a very
similar behavior of the time $\tau_{2}$ computed from the
second Legendre polynomial. In this case, the bulk
value is neatly larger than the values obtained for
confined samples. It is also noticeable that the re-
orientational times $\tau_{1}$ in sub-critical water are
about twice the corresponding $\tau_{2}$ values, whereas
in SW both times are very similar. To our
knowledge, no experimental measures of $\tau_{1,2}$ as-
sociated with the dipole moment reorientation
have been reported yet.

The calculation of $\tau_{1,2}$ associated with the hy-
drogen–hydrogen distance and with the perpen-
dicular direction to the instantaneous molecular
plane as a function of temperature produces
functions with a shape very similar to the ones
presented in Fig. 2 as it can be observed from data
of Table 1. $\tau_{2}$ is usually understood as the closest
observable to the experimental reorientational
time found in NMR measurements [5]. The be-
havior of reorientational motions in bulk SW has
been also observed not to be very dependent of the
temperature, showing a tendency to the reduction
of reorientational times with increasing tempera-
tures [6].

Full results of all reorientational times for both
Legendre polynomials are presented in Table 1.
Density dependence is not represented in Fig. 2. In
SW at 673 K, we considered a reduction in density
up to $40\%$: we observe a tendency to the decreasing
of characteristic times for both $\tau_{1}$ and $\tau_{2}$ when
density is lowered. This fact was also observed in
MD simulations of unconstrained SW states [6]. It
can be observed that the ratio $\tau_{1}/\tau_{2}$ is close to 2 in
most of sub-critical states, instead to be 3 (hy-
drodynamic limit). This was also found in bulk
water simulations [21] and it can be due to finite-
size effects.

We can distinguish two types of regimes for all
reorientational times as a function of temperature.
A first group for states at room temperature (and
presumably for close values) and a second group

Table 1
Reorientational times $\tau_{1}$ and $\tau_{2}$ (in ps) for sub- and supercritical water at different thermodynamic conditions

<table>
<thead>
<tr>
<th>Tube</th>
<th>$T$
(K)</th>
<th>$\rho$
(g/cm³)</th>
<th colspan="2">$\hat{u}_{\mu}$</th>
<th colspan="2">$\hat{u}_{\text{HH}}$</th>
<th colspan="2">$\hat{u}_{\perp}$</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th>$\tau_{1}$</th>
<th>$\tau_{2}$</th>
<th>$\tau_{1}$</th>
<th>$\tau_{2}$</th>
<th>$\tau_{1}$</th>
<th>$\tau_{2}$</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="8">(12,12)</td>
<td>298</td>
<td>0.83</td>
<td>5.22</td>
<td>1.76</td>
<td>2.79</td>
<td>1.58</td>
<td>2.33</td>
<td>1.46</td>
</tr>
<tr>
<td>373</td>
<td>0.83</td>
<td>1.15</td>
<td>0.37</td>
<td>0.67</td>
<td>0.34</td>
<td>0.78</td>
<td>0.28</td>
</tr>
<tr>
<td>473</td>
<td>0.83</td>
<td>0.59</td>
<td>0.22</td>
<td>0.35</td>
<td>0.20</td>
<td>0.27</td>
<td>0.17</td>
</tr>
<tr>
<td>*573</td>
<td>0.83</td>
<td>0.35</td>
<td>0.10</td>
<td>0.17</td>
<td>0.09</td>
<td>0.12</td>
<td>0.08</td>
</tr>
<tr>
<td>*673</td>
<td>0.83</td>
<td>0.15</td>
<td>0.05</td>
<td>0.09</td>
<td>0.05</td>
<td>0.08</td>
<td>0.05</td>
</tr>
<tr>
<td>*673</td>
<td>0.66</td>
<td>0.16</td>
<td>0.05</td>
<td>0.09</td>
<td>0.06</td>
<td>0.09</td>
<td>0.05</td>
</tr>
<tr>
<td>*673</td>
<td>0.49</td>
<td>0.11</td>
<td>0.04</td>
<td>0.04</td>
<td>0.05</td>
<td>0.06</td>
<td>0.04</td>
</tr>
<tr>
<td>*773</td>
<td>0.83</td>
<td>0.10</td>
<td>0.03</td>
<td>0.07</td>
<td>0.05</td>
<td>0.05</td>
<td>0.03</td>
</tr>
<tr>
<td rowspan="8">(10,10)</td>
<td>298</td>
<td>0.83</td>
<td>4.11</td>
<td>1.53</td>
<td>2.25</td>
<td>1.37</td>
<td>1.86</td>
<td>1.24</td>
</tr>
<tr>
<td>373</td>
<td>0.83</td>
<td>1.03</td>
<td>0.33</td>
<td>0.57</td>
<td>0.31</td>
<td>0.63</td>
<td>0.25</td>
</tr>
<tr>
<td>473</td>
<td>0.83</td>
<td>0.57</td>
<td>0.21</td>
<td>0.31</td>
<td>0.19</td>
<td>0.25</td>
<td>0.16</td>
</tr>
<tr>
<td>*573</td>
<td>0.83</td>
<td>0.28</td>
<td>0.07</td>
<td>0.10</td>
<td>0.06</td>
<td>0.09</td>
<td>0.06</td>
</tr>
<tr>
<td>*673</td>
<td>0.83</td>
<td>0.18</td>
<td>0.04</td>
<td>0.08</td>
<td>0.05</td>
<td>0.06</td>
<td>0.04</td>
</tr>
<tr>
<td>*673</td>
<td>0.66</td>
<td>0.15</td>
<td>0.05</td>
<td>0.08</td>
<td>0.05</td>
<td>0.07</td>
<td>0.04</td>
</tr>
<tr>
<td>*673</td>
<td>0.49</td>
<td>0.09</td>
<td>0.04</td>
<td>0.06</td>
<td>0.05</td>
<td>0.05</td>
<td>0.04</td>
</tr>
<tr>
<td>*773</td>
<td>0.83</td>
<td>0.10</td>
<td>0.03</td>
<td>0.06</td>
<td>0.03</td>
<td>0.05</td>
<td>0.03</td>
</tr>
<tr>
<td rowspan="8">(8,8)</td>
<td>298</td>
<td>0.83</td>
<td>3.04</td>
<td>1.12</td>
<td>2.05</td>
<td>1.09</td>
<td>1.63</td>
<td>0.91</td>
</tr>
<tr>
<td>373</td>
<td>0.83</td>
<td>1.00</td>
<td>0.41</td>
<td>0.65</td>
<td>0.36</td>
<td>0.59</td>
<td>0.24</td>
</tr>
<tr>
<td>473</td>
<td>0.83</td>
<td>0.42</td>
<td>0.17</td>
<td>0.28</td>
<td>0.19</td>
<td>0.23</td>
<td>0.16</td>
</tr>
<tr>
<td>*573</td>
<td>0.83</td>
<td>0.15</td>
<td>0.08</td>
<td>0.12</td>
<td>0.07</td>
<td>0.08</td>
<td>0.05</td>
</tr>
<tr>
<td>*673</td>
<td>0.83</td>
<td>0.08</td>
<td>0.04</td>
<td>0.07</td>
<td>0.04</td>
<td>0.05</td>
<td>0.03</td>
</tr>
<tr>
<td>*673</td>
<td>0.66</td>
<td>0.08</td>
<td>0.04</td>
<td>0.07</td>
<td>0.05</td>
<td>0.06</td>
<td>0.03</td>
</tr>
<tr>
<td>*673</td>
<td>0.49</td>
<td>0.06</td>
<td>0.03</td>
<td>0.06</td>
<td>0.05</td>
<td>0.05</td>
<td>0.03</td>
</tr>
<tr>
<td>*773</td>
<td>0.83</td>
<td>0.07</td>
<td>0.03</td>
<td>0.06</td>
<td>0.03</td>
<td>0.04</td>
<td>0.02</td>
</tr>
<tr>
<td>Bulk</td>
<td>298</td>
<td>0.83</td>
<td>5.28</td>
<td>2.31</td>
<td>4.38</td>
<td>2.51</td>
<td>3.21</td>
<td>2.01</td>
</tr>
<tr>
<td>Bulk</td>
<td>298</td>
<td>1.00</td>
<td>4.91</td>
<td>2.24</td>
<td>4.25</td>
<td>2.47</td>
<td>3.11</td>
<td>1.83</td>
</tr>
</tbody>
</table>

Estimated uncertainty is about 0.01 ps in all cases. The $\hat{u}_{\mu}, \hat{u}_{\text{HH}}$ and $\hat{u}_{\perp}$ vectors are fully described in the text. Starred temperatures indicate supercritical states.

for states from 373 to 773 K. It is not relevant whether or not the latter are supercritical states. To have a measure of this two classes, we have estimated the activation energy $\Delta E$ required to move on from the first to the second group. We considered an Arrhenius-like behavior of $\tau_{1}$ and $\tau_{2}$:

$$
\tau_{i}(T) \approx \alpha(T) \exp \left\{-\frac{\Delta E}{k_{\mathrm{B}} T}\right\} \quad(i=1,2),\qquad(4)
$$

where $k_{\mathrm{B}}$ is the Boltzmann constant. This procedure has provided an activation energy of about $\Delta E=15 \pm 2$ kJ/mol for all considered times, regardless of the tube class. This result is quite surprising and, in our opinion, indicates the existence of two marked groups of thermodynamic conditions concerning orientational order: below and above the boiling point. As a general feature, we observed that the characteristic time of molecular reorientation is highly correlated with H-bond populations [8,11] since at high temperatures and/or inside CNs (for the most significant changes in $\tau$) the HB network is markedly weakened.

The mean time spent by a water molecule in its first coordination shell can be calculated [21,22] from a residence time function $C_{\text{res}}(t)$, defined for a given molecule as the number of water molecules in the first coordination shell of the tagged molecule during a time interval of length $t$. The initial value of $C_{\text{res}}(t)$ is the coordination number $c$, defined as the plateau value obtained from the running coordination number $n(r)$:

$$
n(r) \equiv 4 \pi \rho \int_{0}^{r} \mathrm{d} r^{\prime} g\left(r^{\prime}\right) r^{\prime 2}. \tag{5}
$$

Here $\rho$ is the water density. The position of the first minimum in the radial distribution function $g(r)$ indicates the size (radius) of the first coordination shell. An exponential-like behavior of $C_{\text{res}}(t)$ is observed and a residence time $\tau_{\text{res}}$ can be obtained from the fit of $C_{\text{res}}(t)$ to a pure single exponential:

$$
C_{\text{res}}(t) \approx c \exp \left\{\frac{-t}{\tau_{\text{res}}}\right\}. \tag{6}
$$

The results found for confined water systems are depicted in Fig. 3 and compared with the bulk value. The classification of all samples in two different regimes is not clear: the fitting to a single exponential is not evident and it could depend on the tube size. It is also remarkable that at room temperature the confined samples are ordered inversely than in the classification found for reorientational motions: now the bulk value is the lowest and indicates that when confinement is very important, namely in the (8,8) tube, water molecules spend longer time in its neighborhood than in larger tubes and, as expected, in bulk water.

Finally we analyzed the temperature dependence of the diffusion coefficients $D$. As it is shown in Fig. 4, again an Arrhenius-like dependence is found. The values corresponding to SW are taken from [10]. In this case the activation energy which can characterize a different behavior for states below and above the boiling point is lower and estimated to be about $\Delta E=1.2 \pm 0.5 \mathrm{~kJ} / \mathrm{mol}$.

![](./images/812442408108163073_6.jpg)

Fig. 3. Residence time $\tau_{\text{res}}$ of a water molecule in its first coordination shell as a function of temperature at the density of $0.83 \mathrm{~g} / \mathrm{cm}^{3}$.

![](./images/812442408108163073_7.jpg)

Fig. 4. Diffusion coefficients $D$ as a function of temperature at the density of $0.83 \mathrm{~g} / \mathrm{cm}^{3}$.

In summary, we presented MD simulations of sub- and supercritical water inside CNs of different radii and studied orientational order, residence times and diffusion coefficients and compared to the values corresponding to bulk room temperature. We observed the effect of confinement on those properties is specially relevant in water at ambient conditions. When the boiling point is reached, there are significant changes basically consisted in a remarkable rise of the velocity of the reorientational motions and a marked reduction of the residence time in the water first coordination shell. From those results we have estimated that an activation energy of about $\Delta E=15 \pm 2 \mathrm{~kJ} / \mathrm{mol}$ is required to the system in order to access the regime of quick reorientations. Fast diffusion also requires some energy, about ten times smaller than the former.

### Acknowledgements

We are indebted to Prof. M.Yao for fruitful discussions. We also thank the Direcció General de

Recerca of the Generalitat de Catalunya, project
2001SGR-00222 and the Ministerio de Educación y
Cultura of Spain, grants BFM2000-0596-C03-02
and PB98-0922 for financial support. Funds of
project PR99-05 of the Universitat Politècnica de
Catalunya have partially supported this work.

## References
[1] F. Franks, in: F. Franks (Ed.), Water: A Comprehensive Treatise, Plenum Press, New York, 1972.

[2] C.A. Eckert, B.L. Knutson, P.G. Debenedetti, Nature (London) 383 (1996) 313.

[3] J. Martí, J. Chem. Phys. 110 (1999) 6876.

[4] M.S. Skaf, D. Laria, J. Chem. Phys. 113 (2000) 3499.

[5] N. Matubayashi, N. Nakao, M. Nakahara, J. Chem. Phys. 114 (2001) 4107.

[6] E. Guàrdia, J. Martí, J. Mol. Liq. 101 (2002) 137.

[7] R. Saito, G. Dresselhaus, M.S. Dresselhaus, Physical properties of carbon nanotubes, Imperial College Press, London, 1998.

[8] M.C. Gordillo, J. Martí, Chem. Phys. Lett. 329 (2000) 341.

[9] J. Martí, M.C. Gordillo, Phys. Rev. B 63 (2001) 165430.

[10] J. Martí, M.C. Gordillo, Phys. Rev. E 64 (2001) 021504.

[11] M.C. Gordillo, J. Martí, Chem. Phys. Lett. 341 (2001) 250.

[12] N. Hamada, S. Sawada, A. Oshiyama, Phys. Rev. Lett. 68 (1992) 1579.

[13] J. Martí, J.A. Padró, E. Guàrdia, J. Mol. Liq. 62 (1994) 17.

[14] H.J.C. Berendsen, J.P.M. Postma, W.F. van Gunsteren, J. Hermans, in: B. Pullman (Ed.), Intermolecular forces, Reidel, Dordretch, Holland, 1981.

[15] J. Martí, J.A. Padró, E. Guàrdia, J. Chem. Phys. 105 (1996) 639.

[16] J. Martí, E. Guàrdia, J.A. Padró, J. Chem. Phys. 101 (1994) 10883.

[17] H.J.C. Berendsen, J.P.M. Postma, W.F. van Gunsteren, A. DiNola, J.R. Haak, J. Phys. Chem. 81 (1984) 3684.

[18] A. Wallqvist, O. Telemann, Mol. Phys. 74 (1991) 515.

[19] L. Saiz, J.A. Padró, E. Guàrdia, Mol. Phys. 97 (1999) 897.

[20] E. Guàrdia, J. Martí, J.A. Padró, L. Saiz, A. Kulminskii, J. Mol. Liq. 96-97 (2002) 3, and references therein.

[21] E. Guàrdia, J.A. Padró, J. Phys. Chem. 94 (1990) 6049.

[22] R.W. Impey, P.A. Madden, I.R. McDonald, J. Phys. Chem. 87 (1983) 5071.