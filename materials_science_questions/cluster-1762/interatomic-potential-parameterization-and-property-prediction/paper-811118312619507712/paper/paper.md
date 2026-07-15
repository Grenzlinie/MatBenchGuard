![](./images/811118312619507712_1.jpg)

Solid State Communications 112 (1999) 49-54

![](./images/811118312619507712_2.jpg)
www.elsevier.com/locate/ssc

# Atomistic simulation of a high-pressure phase of AgI using a three-body potential

W. Sekkal$^{\mathrm{a},*}$, A. Laref$^{\mathrm{a}}$, A. Zaoui$^{\mathrm{b}}$, H. Aourag$^{\mathrm{a}}$, M. Certier$^{\mathrm{b}}$

$^{\mathrm{a}}$Computational Materials Science Laboratory, Physics Department, University of Sidi Bel-Abbes, Sidi Bel-Abbes 22000, Algeria
$^{\mathrm{b}}$L.P.L.I, 08 Rue Marconi, Technopôle 2000, 57078 Cedex 3, Metz, France

Received 1 March 1999; received in revised form 12 April 1999; accepted 30 May 1999 by M. Cardona

## Abstract

The structural properties of AgI under high pressure and high temperature have been investigated using molecular dynamics simulation based on Tersoff's potential. Superionic behaviour appears in the rocksalt-structured phase of AgI at high pressure and high temperature. Its high-diffusion coefficients are calculated from the mean squared atomic displacements. © 1999 Elsevier Science Ltd. All rights reserved.

**Keywords**: A. Insulators; C. Crystal structure and symmetry; D. Phase transitions; E. Strain, high pressure

## 1. Introduction

Superionic conductors such as AgI are fascinating condensed matter systems in which solid-like and liquid-like properties are combined in an interesting manner [1–7]. Silver iodide has a rich phase diagram with several different solid phases existing. For example, at low pressure and below a temperature of $\approx$420 K, $\alpha$-AgI undergoes a phase transformation to the non-superionic phase, $\beta$-AgI. It is often stated [8] that, at low temperatures and pressures, AgI may exist in two phases, $\beta$-AgI or $\gamma$-AgI. In $\beta$-AgI, the iodide ions are arranged in a hcp lattice with the silver ions being tetrahedrally co-ordinated to each of the iodines. Thus, in $\beta$-AgI, the system is in a wurtzite structure. In $\gamma$-AgI, the iodide ions are arranged in an fcc lattice with the silver ions also tetrahedrally co-ordinated to the iodine ions. No diffusion is shown by either species of ions in these low temperature phases.

With increasing pressure at ambient temperature, AgI transforms, via a tetragonal phase [9], to the rocksalt-structured phase. Within this phase, the conductivity increases rapidly with increasing temperature reaching a value of $0.5\ \Omega^{-1}\ \mathrm{cm}^{-1}$ at 1 GPa [8].

The structural phase transformations of AgI have been investigated using molecular dynamics simulation [10,11] based on the Parrinello–Rahman Lagrangian. However, to our knowledge, no structural calculations have been performed on AgI using a three-body potential coupled with molecular dynamics (MD) simulation. Indeed, the trend in the molecular dynamics modelling has been to tailor interatomic potentials to produce close matches between the physical properties of the real system and the model system. In this way, the models should gain predictive power with respect to those physical properties that are not directly included by an adjustment of the potential.

In this paper, we report the results of computer experiments that simulate the structural properties of AgI in the zinc blende and rocksalt structures using a three-body potential model (Tersoff's model). The main purpose of the present work is to test the transferability of this model to predict physical properties of the high-pressure phase of silver iodide. We are also interested in predicting the development of any structural disorder in the high-pressure phase of AgI with increasing temperature. In fact, neutron diffraction measurements of the rocksalt-structured phase at high pressure and temperature have been investigated by Keen et al. [12]. Their studies show fast-ionic behaviour in rocksalt-structured AgI above a diffuse transition with a small anomaly in the lattice parameter and a continuous increase in the occupation of interstitial tetrahedral sites with increasing temperature. Recently, molecular dynamics simulations

---
* Corresponding author. Fax: + 213-756-14-86.
E-mail address: haourag@mail.univ-sba.dz (W. Sekkal)

0038-1098/99/$ - see front matter © 1999 Elsevier Science Ltd. All rights reserved.
PII: S0038-1098(99)00257-4

**Table 1**
The adjusted Tersoff parameters for AgI in the zinc blende structure

<table>
  <thead>
    <tr>
      <th colspan="2">AgI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A (eV)</td>
      <td>207.500</td>
    </tr>
    <tr>
      <td>B (eV)</td>
      <td>36.160</td>
    </tr>
    <tr>
      <td>$\lambda$ ($\mathring{\text{A}}^{-1}$)</td>
      <td>1.8095</td>
    </tr>
    <tr>
      <td>$\mu$ ($\mathring{\text{A}}^{-1}$)</td>
      <td>0.9428</td>
    </tr>
    <tr>
      <td>$n$</td>
      <td>0.78734</td>
    </tr>
    <tr>
      <td>$h$</td>
      <td>$-0.57058$</td>
    </tr>
    <tr>
      <td>$\beta$</td>
      <td>$1.0999 \times 10^{-6}$</td>
    </tr>
    <tr>
      <td>$c$</td>
      <td>$1.0039 \times 10^{5}$</td>
    </tr>
    <tr>
      <td>$d$</td>
      <td>16.218</td>
    </tr>
    <tr>
      <td>$R$ ($\mathring{\text{A}}$)</td>
      <td>3.43</td>
    </tr>
    <tr>
      <td>$D$ ($\mathring{\text{A}}$)</td>
      <td>0.20</td>
    </tr>
  </tbody>
</table>

using a three-body potential predict the presence of cation disorder at elevated temperatures within the high-pressure rocksalt-structured phase of CuCl [13].

In order to understand the complex nature of ionic conduction processes at high temperatures, it is necessary to use some form of microscopic modelling. The most interesting feature that has been used in our case is the mean square displacement (MSD). According to the behaviour of the MSD for $\text{Ag}^{+}$ as a function of time, we predict a cation disorder (diffusion) which might be indicative of superionic behaviour of AgI in the high-pressure rocksalt-structure at high temperature.

### 2. Simulation details

Among the many empirical model potentials which have been developed for tetrahedral semiconductors, that of Tersoff has been the most successful in that it reproduces many of the semiconductor properties [13,14]. The form of the energy $E$, between two neighbouring atoms $i$ and $j$, is taken as [15]

$$
E = \sum_{i} E_{i} = \frac{1}{2} \sum_{i \neq j} V_{ij}, \tag{1}
$$

with

$$
V_{ij} = f_{\text{C}}(r_{ij})[a_{ij}f_{\text{R}}(r_{ij}) + b_{ij}f_{\text{A}}(r_{ij})], \tag{2}
$$

$$
f_{\text{R}}(r) = A \exp(-\lambda_{1} r),
$$

$$
f_{\text{A}}(r) = -B \exp(-\lambda_{2} r),
$$

$$
f_{\text{C}}(r) = \begin{cases}
1 & r < R - D \\
\frac{1}{2} - \frac{1}{2} \sin\left[\frac{\pi}{2} \frac{(r - R)}{D}\right] & R - D < r < R + D \\
0 & r > R + D
\end{cases}.
$$

$b_{ij}$ is the many-body-order parameter describing how the bond-formation energy is affected by the local atomic arrangement due to the presence of other neighbouring atoms (the $k$ atoms). It is a many-body function of the positions of atoms $i$, $j$ and $k$ and has the form

$$
b_{ij} = (1 + \beta^{n} \zeta_{ij}^{n})^{-1/2n} \tag{3}
$$

with

$$
\zeta_{ij} = \sum_{k(\neq i,j)} f_{\text{C}}(r_{ik})g(\theta_{ijk}) \exp[\lambda_{3}^{3}(r_{ij} - r_{ik})^{3}]
$$

$$
g(\theta) = 1 + \frac{c^{2}}{d^{2}} - \frac{c^{2}}{d^{2} + (h - \cos\theta)^{2}}
$$

$$
a_{ij} = (1 + \alpha^{n} \eta_{ij}^{n})^{-1/2n}
$$

$$
\eta_{ij} = \sum_{k(\neq i,j)} f_{\text{C}}(r_{ik}) \exp[\lambda_{3}^{3}(r_{ij} - r_{ik})^{3}]
$$

$\zeta$ is called the effective coordination number and $g(\theta)$ is a function of the angle between $r_{ij}$ and $r_{ik}$ that has been fitted to stabilize the tetrahedral structure. We note that $\lambda_{3}$ and $\alpha$ are put equal to zero [15].

$A$, $B$, $n$, $c$, $d$, $h$, $\lambda_{1}$, and $\lambda_{2}$ are constants determined by fitting to the cohesive properties of AgI [16,17]. A fitting program was used to determine the constants. The obtained parameters are given in Table 1.

Based on the Tersoff's model, we use 216 atoms arranged in a cubic simulation cell with periodic boundary conditions. This study is undertaken using a fifth-order Gear Predictor Corrector algorithm with a 1.56 fs time step. Typical calculations run for 20 000 steps.

### 3. Numerical results

The first step of our study is the calculation of the structural properties of $\gamma$-AgI in order to test the accuracy of our potential. We calculate the pair-distribution function $g(r)$, the mean square displacement (MSD)

$$
\langle r^{2}(t)\rangle = \frac{1}{N} \sum_{i=1}^{N} \langle|r_{i}(t) - r_{i}(0)|^{2}\rangle \tag{4}
$$

and the normalized velocity autocorrelation function (VAF)

$$
C(t) = \frac{\Psi(t)}{\Psi(0)} \tag{5}
$$

where

$$
\Psi(t) = \frac{1}{N} \sum_{i=1}^{N} \langle V_{i}(t) \cdot V_{i}(0)\rangle. \tag{6}
$$

The results of $g(r)$, $\langle r^{2}(t)\rangle$ and $C(t)$ are, respectively, shown in Figs. 1–3. The co-ordination numbers of the first co-ordination shell in $g(r)$ are evaluated from the standard relation

$$
N = 4\pi\rho \int_{0}^{\text{R}} r^{2}g(r)\text{d}r, \tag{7}
$$

![](./images/811118312619507712_3.jpg)

Fig. 1. The pair correlation function for AgI in the zinc blende structure.

where R denotes the position of the first minima in g(r). The values of $N$ are given in Table 2 and correspond to those expected for a zinc blende structure. Moreover, the positions of the successive peaks of the $g(r)$ are in excellent agreement with those expected in the crystal structure. The results for $\langle r^{2}(t)\rangle$ and $C(t)$ oscillate around their equilibrium positions. The mean squared displacements show an increase for small time, which may appear surprising. This feature is, in our view, due to the displacements of the cations and also because their velocities (see $c(t)$ in Fig. 3) are strongly correlated at short time.

Fig. 4 displays the cohesive energy versus volume. This

![](./images/811118312619507712_4.jpg)

Fig. 2. The mean squared displacement of AgI in the zinc blende structure.

![](./images/811118312619507712_5.jpg)

Fig. 3. The normalized velocity autocorrelation function of AgI.

<table>
<caption>Table 2 Peak distances and number of pairs for cubic AgI in the zinc blende structure</caption>
<thead>
<tr>
<th colspan="3">Peak distance (Å)</th>
<th>Number of pair</th>
</tr>
</thead>
<tbody>
<tr>
<td>1st</td>
<td>2.803</td>
<td>2.814<sup>a</sup></td>
<td>4.00</td>
</tr>
<tr>
<td>2nd</td>
<td>4.591</td>
<td>4.595<sup>a</sup></td>
<td>12.04</td>
</tr>
<tr>
<td>3rd</td>
<td>5.384</td>
<td>5.388<sup>a</sup></td>
<td>12.04</td>
</tr>
<tr>
<td>4th</td>
<td>6.483</td>
<td>6.499<sup>a</sup></td>
<td>6.02</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="4"><sup>a</sup>Calculated from experimental result taken from Ref. [9].</td>
</tr>
</tfoot>
</table>

![](./images/811118312619507712_6.jpg)

Fig. 4. Cohesive energy as a function of volume for $\gamma$-AgI.

![](./images/811118312619507712_7.jpg)

![](./images/811118312619507712_8.jpg)

![](./images/811118312619507712_9.jpg)

Fig. 5. (continued)

Fig. 5. The mean-square displacement of the rocksalt structure at:
(a) 20; (b) 30; and (c) 40 kbar.

curve is fitted to the equation of state of Murnaghan [18]
from which we obtain the equilibrium lattice parameter, the
bulk modulus, its derivative and the cohesive energy.

We have also calculated the elastic constants using the
method developed in detail in Ref. [19]. The results are
listed in Table 3 and are in good agreement with the experi-
ments [9] and with the calculations based on the BOM
method [20]. The accuracy is about 0.4% for the lattice
parameter and 2% for the bulk modulus. We notice that
the cohesive energy of the zinc blende structure, which is
equal to $-2.366$ eV/atom, is in excellent agreement with the
experimental value of $-2.360$ eV/atom [16] (with an accu-
racy of 0.25%). On the basis of these results, it should be
interesting to test this model keeping the same adjusted
parameters to study the structural properties of AgI under
pressure.

Under pressure, AgI transforms to the rocksalt phase.
Using MD simulations, we examine the behaviour of AgI

Table 3
Equilibrium properties of AgI in the zinc blende

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th colspan="3">Zinc blende phase</th>
<th colspan="2">Rocksalt phase</th>
</tr>
<tr>
<th>Present work</th>
<th>Calculated</th>
<th>Experimental</th>
<th>Present work</th>
<th>Other calculated</th>
</tr>
</thead>
<tbody>
<tr>
<td>Lattice constant (Å)</td>
<td>6.485</td>
<td>6.473ª</td>
<td>6.499ᶜ</td>
<td>5.970</td>
<td>6.067ᶜ</td>
</tr>
<tr>
<td>B (Mbar)</td>
<td>0.192</td>
<td>0.196ᵇ</td>
<td></td>
<td>0.288</td>
<td>0.305ᵈ 0.500ᵉ</td>
</tr>
<tr>
<td>B' (eV/atom)</td>
<td>2.35</td>
<td></td>
<td></td>
<td>2.38</td>
<td></td>
</tr>
<tr>
<td>(C₁₁−C₁₂)/2 (Mbar)</td>
<td>0.066</td>
<td>0.061ᵇ</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>C₄₄ (Mbar)</td>
<td>0.066</td>
<td>0.095ᵇ</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

ªFrom Ref. [17].
ᶜFrom Ref. [9].
ᵇFrom Ref. [20].
ᵈFrom Ref. [21].
ᵉFrom Ref. [22].

![](./images/811118312619507712_10.jpg)

Fig. 6. Silver-ion diffusion coefficients for the rocksalt-AgI at 20, 30 and 40 kbar.

in the pressure range from 20 to 40 kbar. The structural properties calculated using the equation of state of Murna- ghan are listed in Table 3. The obtained results agree well with experiments and other theoretical calculations [9,21,22]. We notice that the lattice parameter for the rock- salt structure is $5.970 \mathring{A}$ in good agreement with the experi mental value of $6.067 \mathring{A}$ (with an accuracy of 1.6%). The overall agreement confirms the validity of our adjusted potential parameters.

The relevant part in our work is to know whether the rocksalt phase becomes superionic at high temperatures. The most interesting feature used in this case is the MSD of $Ag^{+}$. We have plotted in Fig. 5 the MSD of cations as a function of time at 20, 30 and 40 kbar under various temperatures (900–1600 K). Heating is performed for 80 ps for each temperature using the Andersen's method [23] for temperature control.

![](./images/811118312619507712_11.jpg)

Fig. 7. Silver-ion diffusion coefficient versus pressure at 1200 K.

![](./images/811118312619507712_12.jpg)

Fig. 8. The pair correlation function of AgI at 20 kbar under temperature.

The diffusion coefficient $D$ is obtained by using the Einstein relation

$$
D = \lim_{t \to \infty} \frac{\langle r^2(t) \rangle}{6t} \tag{8}
$$

where $r(t)$ is the position vector of a cation at time $t$. Values of $D$ for $p=30$ and 40 kbar are proportional to $10^{-5}\ \text{cm}^2\text{s}^{-1}$ and increases with temperature as shown in Fig. 6. Our results agree with Tallon's calculations [10]. This phenomenon is confirmed from Fig. 5 where $Ag^{+}$ cations undergo rapid diffusion between interstitial sites formed by sub-lattice of anions. Recently, neutron diffrac- tion experiments [12] revealed a superionic behaviour of AgI in the rocksalt structure under high temperature. In a previous work, it appears that CuCl is isostructural to AgI, which presents a fast ionic behaviour at high pressures and high temperatures [24]. This fact was confirmed recently using molecular dynamics simulations based on a three- body potential [13].

It is important to notice that the MSD of cations is very sensitive to the crystal density. This effect can be seen in Fig. 7 where we plot the diffusion coefficient versus pressure at 1200 K. It appears that the ionic behaviour of AgI in the rocksalt structure decreases with increasing pressure. This is perhaps due to the effect of hydrostatic pressure, which reduces the gaps in the anion sub-lattices through which the cation migrates. In order to see the structural changes in the rocksalt structure of AgI at $p=20$ kbar under high

temperature, we run the molecular-dynamics simulation at a number of temperatures ranging from 400 to 1900 K. The pair correlation function $g(r)$, plotted in Fig. 8, exhibits sharp nearest-neighbour peaks and has an oscillatory tail around the value 1. This distribution is quite liquid-like. With $T=400$–1900 K, we see that the first peak decreases and the corresponding co-ordination number is six at $T=400$ K. This number is equal to eight at 1900 K which means that the population of $Ag^{+}$ ions is consider- able. There is no suggestion of transition to the bcc structure because of the (NVT) ensemble is limited to predict exactly the transition structure.

## 4. Conclusions

A simple empirical three-body potential coupled with molecular-dynamics method simulates well the structural properties of AgI in the zinc blende and rocksalt structures. This potential model reproduces the superionic behaviour of AgI in the rocksalt structure in the high temperature range of 900–1600 K. Our results are supported by experiments [12] and other theoretical calculations [10].

## References

[1] A.L. Laskar, S. Chandra (Eds.), Superionic Solids and Solid Electrolytes: Recent Trends Academic, New York, 1989.
[2] J. Perram (Ed.), Physics of Superionic Conductors and Elec- trode Materials Plenum Press, New York, 1983.

[3] S. Chandra, Superionic Solids: Principles and Applications, North-Holland, Amsterdam, 1981.
[4] P. Vashishta, J.N. Mundy, G.K. Shenoy (Eds.), Fast Ion Trans- port in Solids North-Holland, Amsterdam, 1979.
[5] M.B. Salamon (Ed.), Physics of Superionic Conductors Springer, Berlin, 1979.
[6] S. Geller (Ed.), Solid Electrolytes Springer, Berlin, 1977.
[7] G.D. Mahan, W.L. Roth (Eds.), Superionic Conductors Plenum, New York, 1976.
[8] B.-E. Mellander, Phys. Rev. B 26 (1982) 5886.
[9] D.A. Keen, S. Hull, J. Phys. Condens. Matter 5 (1993) 23.
[10] J.L. Tallon, Phys. Rev. B 38 (1988) 9069.
[11] C.A. Rains, J.R. Ray, P. Vashishta, Phys. Rev. B 44 (1991) 9228.
[12] D.A. Keen, S. Hull, W. Hayes, N.J.G. Gardner, Phys. Rev. Lett. 24 (1996) 4914.
[13] W. Sekkal, H. Aourag, M. Certier, J. Phys. Chem. Solids 59 (1998) 1293.
[14] W. Sekkal, B. Bouhafs, H. Aourag, M. Certier, J. Phys. Condens. Matter 10 (1998) 4975.
[15] J. Tersoff, Phys. Rev. B 37 (1988) 6991.
[16] W.A. Harrison, in: Electronic Structure and the Properties of Solids: the Physics of the Chemical Bond, vol. 176, 1989.
[17] Landolt-Börnstein, Numerical Data and Functional Relation- ships in Science and Technology, vol. 17, 1986.
[18] F.D. Murnaghan, Proc. Natl. Acad. Sci. USA 30 (1944) 5390.
[19] M.J. Mehl, Phys. Rev. B 47 (1993) 2493.
[20] S.G. Shen, J. Phys. Condens. Matter 6 (1994) 8733.
[21] G.H. Shaw, J. Geophys. Res. 83 (1978) 3519.
[22] S. Ves, D. Glötzel, M. Cardona, H. Overhof, Phys. Rev. B 24 (1981) 3073.
[23] H.C. Andersen, J. Chem. Phys. 72 (1980) 2384.
[24] S. Hull, D.A. Keen, J. Phys. Condens. Matter 8 (1996) 6191.