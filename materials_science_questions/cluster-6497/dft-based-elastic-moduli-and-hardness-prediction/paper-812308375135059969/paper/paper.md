# Total Energy Calculations in the DFT on Binary Compounds

P. E. VAN CAMP AND V. E. VAN DOREN

University of Antwerp (RUCA), Groenenborgerlaan 171, B-2020 Antwerpen, Belgium

Received October 25, 1994; accepted November 28, 1994

## ABSTRACT
Calculations are carried out using first-principles self-consistent local-density and nonlocal density theory of the electronic structure, the total energy, and the charge density of a variety of semiconducting and insulating compounds under hydrostatic and uniaxial pressure. For several cases, the transition pressure from one structure to another is determined as well as the pressure coefficients of the main band gaps. It is shown that several properties are calculated with adequate accuracy to be compared with experiment, so that values which have not yet been measured are trustworthy predictions. © 1995 John Wiley & Sons, Inc.

## Introduction
In solid-state physics, calculations are called "ab initio" if they use as input only such data as the atomic number and weight of the elements constituting the solid and the phyiscal constants such as the mass and charge of the electron and Planck's constant. Whereas a decade ago such calculations were the exception rather than the rule, they have become a basic tool of many theoretical groups in recent years. At this moment, these calculations cover mechanical, electronic, and dielectric properties at zero temperature. Thermodynamical calculations for temperatures different from zero, involving statistical averages, are as yet beyond practical reach. Most of the computations relate to the ground state of the solid and, therefore, the energy of this state must be calculated with very high precision. In the early 1970s, some groups reported results based on the Hartree-Fock approximation, but since then, the emphasis has shifted mainly to density functional theory. This theory works remarkably well despite the deficiencies concerning exchange and correlations. Recently, considerable progress to remedy this has been made by including nonlocal functionals or by using self-energy corrections into the one-particle Hamiltonian.

This density functional theory is usually combined with pseudopotential theory in which the core electrons of the atoms in the solids are taken together with their nuclei so that together they produce the effective ion potential experienced by the outer-valence electrons. Since its advent, many local pseudopotentials have been constructed, but it is only recently that ab initio self-consistent pseudopotentials are available. These pseudopotentials are angular-momentum-dependent, i.e.,

---

International Journal of Quantum Chemistry, Vol. 55, 339-345 (1995)
© 1995 John Wiley & Sons, Inc.
CCC 0020-7608/95/040339-07

VAN CAMP AND VAN DOREN

nonlocal, and produce the correct charge inside the core region. This norm-conserving property makes these ab initio atomic pseudopotentials transferable, i.e., they can be used in any configuration of condensed matter provided that the core regions of neighboring atoms do not overlap.

In this article, the electronic structure of a number of binary compounds under hydrostatic pressure is presented. These properties are obtained mainly from a local density functional but also from a nonlocal functional. All calculations use nonlocal pseudopotentials in the plane-wave basis.

## Summary of the Theory

The total ground-state energy of a crystal consists of an ionic part $E_{I}$ and an electronic part $E_{E}$:
$$
E_{T}=E_{I}+E_{E}. \tag{1}
$$

The first term is the electrostatic potential energy of the lattice and is usually evaluated by means of the Ewald summation technique. According to the Hohenberg-Kohn theorem [1], the electronic part can be written as (atomic units used throughout in this article)
$$
\begin{aligned}
E_{E}=\int d \boldsymbol{r} V(\boldsymbol{r}) \rho(\boldsymbol{r})+\frac{1}{2} \int d \boldsymbol{r} d \boldsymbol{r}^{\prime} & \frac{\rho(\boldsymbol{r}) \rho(\boldsymbol{r})}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|} \\
& +T_{S}[\rho]+E_{x c}[\rho], \quad(2)
\end{aligned}
$$
where the first term is the potential energy of the electrons in the crystal potential $V$; the second term, the electrostatic or Hartree energy; the third term, the kinetic energy of the noninteracting system; and the last term, the exchange-correlation energy. The theorem further states that the total energy is a universal functional of the electron density and that the total energy is minimal at the correct density.

Although the functionals $T_{S}[\rho]$ and $E_{x c}[\rho]$ can be derived for atoms [2], an exact and useful form is not known for solids. There are essentially two ways to proceed: to use either a local approximation or a nonlocal approximation to $E_{x c}[\rho]$. In the local density-approximation (LDA [3]), one takes
$$
E_{x c}[\rho]=\int d \boldsymbol{r} \rho(\boldsymbol{r}) \epsilon_{x c}(\rho), \tag{3}
$$
where $\epsilon_{x c}$ is the exchange-correlation energy density. There exists a large number of approximations to $\epsilon_{x c}$ (see, e.g., [4]), and in the present work,
we use
$$
\epsilon_{x c}(\rho)=\epsilon_{x}(\rho)+\epsilon_{c}(\rho), \tag{4}
$$
where we take the Kohn-Sham expression [3] for $\epsilon_{x}$ and the Wigner interpolation formula [5] for $\epsilon_{c}$. In the nonlocal density approximation, one can either use gradient expansions (see, e.g., [6]), which are usually quasi-local, or true nonlocal approximations for the correlation part $E_{c}$ of the energy, while the Kohn-Sham expression of the exchange part is still used [7,8]. Here, we start from
$$
E_{c}[\rho]=\int d \boldsymbol{r} \int d \boldsymbol{r}^{\prime} \rho(\boldsymbol{r}) K_{c}\left(\boldsymbol{r}, \boldsymbol{r}^{\prime}\right) \rho\left(\boldsymbol{r}^{\prime}\right). \tag{5}
$$

From this expression, the exchange-correlation potential $W_{c}$ can be derived:
$$
W_{c}=\frac{\delta E_{c}[\rho]}{\delta \rho}. \tag{6}
$$

To find an approximation to the kernel $K_{c}$, we need an expression for the screened potential $W_{c}$. We use a screened Coulomb interaction of the following two types:

- Exponential screening, where we take
  $$
  W_{c}(\boldsymbol{r})=-\frac{1}{2} \int d \boldsymbol{r}^{\prime} \frac{e^{-\xi\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|} \rho\left(\boldsymbol{r}^{\prime}\right), \tag{7}
  $$
  where $\xi$ is the inverse of the Thomas-Fermi screening length and is determined by the Fermi wavevector, $\xi^{2}=2 k_{F}^{2}$.
- Gaussian screening, where we take
  $$
  W_{c}(\boldsymbol{r})=-\frac{1}{2} \int d \boldsymbol{r}^{\prime} \frac{e^{-\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|^{2} / 2 \sigma^{2}}}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|} \rho\left(\boldsymbol{r}^{\prime}\right), \tag{8}
  $$
  where $\sigma^{2}$ is the Thomas-Fermi screening length, i.e., $\sigma^{2}=1 /\left(2 k_{F}^{2}\right)$.

The explicit use of the kinetic energy functional $T_{S}$ can be avoided if one replaces, formally, the many-electron problem by an equivalent set of self-consistent one-electron equations [3]—the Kohn-Sham equations:
$$
\begin{aligned}
\left\{-\frac{1}{2} \nabla^{2}+V(\boldsymbol{r})+\int d \boldsymbol{r}^{\prime} \frac{\rho\left(\boldsymbol{r}^{\prime}\right)}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}\right. & \left.+\mu_{x c}(\rho)\right\} \psi_{k n} \\
& =E_{k n} \psi_{k n}, \quad(9)
\end{aligned}
$$


TOTAL ENERGY CALCULATIONS IN DFT

with the exchange-correlation potential $\mu_{xc}$ given by

$$
\mu_{x c}(\rho)=\frac{\delta E_{x c}[\rho]}{\delta \rho}. \tag{10}
$$

Density functional theory is combined with pseudopotential theory in which the core electrons are taken together with the nucleus. In this work, the nonlocal norm-conserving pseudopotentials of Bachelet et al. [9] are employed. Here, the Kohn-Sham equations are solved in a plane wave basis, i.e.:

$$
\psi_{k n}(\boldsymbol{r})=\sum_{G} C_{k n}(\boldsymbol{G}) e^{i(\boldsymbol{k}+\boldsymbol{G}) \cdot \boldsymbol{r}}, \tag{11}
$$

so that Eq. (9) is converted to a matrix equation:

$$
H C=E C. \tag{12}
$$

With the solution of Eq. (9), the total electronic energy can be expressed as

$$
\begin{aligned}
E_{E}=\sum_{k n} E_{k n} & -\frac{1}{2} \int d \boldsymbol{r} \int d \boldsymbol{r}^{\prime} \frac{\rho(\boldsymbol{r}) \rho\left(\boldsymbol{r}^{\prime}\right)}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|} \\
& +\int d \boldsymbol{r} \rho(\boldsymbol{r})\left[\epsilon_{x c}(\rho)-\frac{\delta E_{x c}[\rho]}{\delta \rho}\right]. \quad(13)
\end{aligned}
$$

The total energy of the crystal is obtained by adding the pure electrostatic energy of the ions to the electronic term.

<table>
<thead>
  <tr>
    <th colspan="7">TABLE I<br>Valence bands and lower conduction bands of Si calculated in the LDA and using the exponential screening (for different values of the screening parameter); also shown are the experimental values [14, 15] and results from the GW approximation [16] (in eV).</th>
  </tr>
  <tr>
    <th></th>
    <th>Exp.</th>
    <th>LDA</th>
    <th>$0.5\ \xi^{2}$</th>
    <th>$\xi^{2}$</th>
    <th>$2\xi^{2}$</th>
    <th>GW</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$\Gamma_{1}$</td>
    <td>$-12.4$</td>
    <td>$-11.94$</td>
    <td>$-10.28$</td>
    <td>$-10.44$</td>
    <td>$-10.60$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$\Gamma_{25}'$</td>
    <td>$0$</td>
    <td>$0$</td>
    <td>$0$</td>
    <td>$0$</td>
    <td>$0$</td>
    <td>$0$</td>
  </tr>
  <tr>
    <td>$\Gamma_{15}$</td>
    <td>$3.4$</td>
    <td>$2.51$</td>
    <td>$3.26$</td>
    <td>$3.25$</td>
    <td>$3.22$</td>
    <td>$3.30$</td>
  </tr>
  <tr>
    <td>$\Gamma_{2}'$</td>
    <td>$4.19$</td>
    <td>$3.21$</td>
    <td>$5.69$</td>
    <td>$5.31$</td>
    <td>$4.97$</td>
    <td>$4.27$</td>
  </tr>
  <tr>
    <td>$X_{1}$</td>
    <td>—</td>
    <td>$-7.79$</td>
    <td>$-6.90$</td>
    <td>$-7.00$</td>
    <td>$-7.09$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$X_{4}$</td>
    <td>$-2.9$</td>
    <td>$-2.84$</td>
    <td>$-1.41$</td>
    <td>$-1.54$</td>
    <td>$-1.66$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$X_{1}$</td>
    <td>$1.3$</td>
    <td>$0.55$</td>
    <td>$5.43$</td>
    <td>$4.93$</td>
    <td>$4.47$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$X_{3}$</td>
    <td>—</td>
    <td>$9.94$</td>
    <td>$11.44$</td>
    <td>$11.26$</td>
    <td>$11.08$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$L_{2}'$</td>
    <td>$-9.4$</td>
    <td>$-9.59$</td>
    <td>$-8.59$</td>
    <td>$-8.71$</td>
    <td>$-8.81$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$L_{1}$</td>
    <td>$-6.8$</td>
    <td>$-6.98$</td>
    <td>$-5.19$</td>
    <td>$-5.33$</td>
    <td>$-5.48$</td>
    <td>—</td>
  </tr>
  <tr>
    <td>$L_{3}'$</td>
    <td>$-1.2$</td>
    <td>$-1.18$</td>
    <td>$-0.62$</td>
    <td>$-0.68$</td>
    <td>$-0.73$</td>
    <td>$-1.19$</td>
  </tr>
  <tr>
    <td>$L_{1}$</td>
    <td>$2.2$</td>
    <td>$1.40$</td>
    <td>$4.18$</td>
    <td>$3.86$</td>
    <td>$3.56$</td>
    <td>$2.30$</td>
  </tr>
  <tr>
    <td>$L_{3}$</td>
    <td>$4.3$</td>
    <td>$3.25$</td>
    <td>$6.98$</td>
    <td>$6.56$</td>
    <td>$6.19$</td>
    <td>$4.11$</td>
  </tr>
</tbody>
</table>

At $T=0$, the ground-state properties of the crystal are derived from the enthalpy $H$:

$$
H=E_{T}+p V. \tag{14}
$$

The equation of state, i.e., the dependence of $E_{T}$ on the crystal volume $V$, determines the pressure $p$:

$$
p=-\frac{d E_{T}}{d V}. \tag{15}
$$

The bulk modulus for hydrostatic compression $B$ is given by

$$
B=V \frac{d p}{d V}. \tag{16}
$$

All other thermodynamic quantities can be derived from these equations. To numerically calculate these quantities, the total energies are fitted to parametrized functions. In the present work, we use either the Murnaghan equation of state [10]:

$$
p=\frac{B_{0}}{B_{0}^{\prime}}\left[\left(\frac{V_{0}}{V}\right)^{B_{0}^{\prime}}-1\right], \tag{17}
$$

or the Birch equation of state [11, 12]:

$$
\begin{aligned}
p=\frac{2}{3} B_{0} & {\left[\left(\frac{V_{0}}{V}\right)^{7 / 3}-\left(\frac{V_{0}}{V}\right)^{5 / 3}\right] } \\
& \cdot\left\{1+\frac{3}{4}\left(B_{0}^{\prime}-4\right)\left[\left(\frac{V_{0}}{V}\right)^{2 / 3}-1\right]\right\}. \quad(18)
\end{aligned}
$$

INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

VAN CAMP AND VAN DOREN

Here, $V_0$ is the crystal volume at zero pressure, and $B_0$ and $B_0'$ are the bulk modulus and its pressure derivative at equilibrium. It should be noted that several other forms of the equation of state exist (see, e.g., [13]).

Discussion

Table I shows results for the valence band and for the lower conduction bands of Si calculated both in the LDA and by using the exponential screening [see Eq. (7)]. For Si, the value of $k_F$ is $1.81\ \text{\AA}^{-1}$. Because there is no easy way to fix the screening parameter, we used three values $(0.5\xi^2$, $\xi^2$, and $2\xi^2)$. The main result of using the nonlocal functional is an upward shift of the conduction bands. In the X-point, this shift is too big. On the other hand, it is in agreement with the GW approximation [16] in the $\Gamma$-point. Unfortunately, the bottom of the valence band moves up a little bit, shifting it away from the experimental values. As can be seen from Table I, the energies of the lower conduction bands and the valence bands are rather insensitive to the three values of the inverse of the Thomas-Fermi screening length chosen in this calculation. The results of a more detailed investigation will be reported elsewhere. However, it is speculated that much larger values of $k_F$, or much smaller values of the screening length, are needed in order to account correctly for the covalent bonding.

As far as the binary compounds are concerned, we did calculations on the nitrides [17-19], the Ga compounds [20], the In compounds [21], SiC [22], and $\text{TiB}_2$ [23]. In the remainder of this article, we discuss some of the results on BN and on MgTe (both materials in three different structures).

The semiconductor compound boron nitride crystallizes in three different structures: the hexagonal ($h$-BN), the cubic ($c$-BN), and the wurtzite phase ($w$-BN). The space groups of these structures are, respectively, $D_{6h}^4$, $T_d^2$, and $C_{4v}^4$. Under normal conditions, the hexagonal structure is stable, whereas the cubic structure is metastable. The wurtzite phase is metastable under all conditions. $c$-BN is the second hardest material in nature after diamond, which is also a metastable structure under normal conditions coexisting with the stable hexagonal graphite.

The total energy is calculated in the local density approximation. The total energy vs. the lattice constant is calculated in eight points and fitted to the Birch equation of state. The kinetic energy cutoffs are 29 Ry for $h$-BN and $w$-BN and 75 Ry for $c$-BN. The number of plane waves in the $\Gamma$-point at the equilibrium lattice constant corresponding to these cutoffs are, respectively, 644, 520, and 869. The number of integration points in the Brillouin zones are six for $h$-BN and $w$-BN and 10 for $c$-BN.

<table><caption>TABLE II Calculated and experimental values of the lattice constant $a$, the bulk modulus $B_0$, and its pressure derivative $B_0'$ for $h$-, $c$-, and $w$-BN.</caption>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>$a$ (Å)</th>
      <th>$c$ (Å)</th>
      <th>$B_0$ (GPa)</th>
      <th>$B_0'$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$h$-BN</td>
      <td>Theory</td>
      <td>2.5919</td>
      <td>6.8945</td>
      <td>77.</td>
      <td>4.41</td>
    </tr>
    <tr>
      <td></td>
      <td>Experiment [24]</td>
      <td>2.504</td>
      <td>6.661</td>
      <td>—</td>
      <td>—</td>
    </tr>
    <tr>
      <td>$c$-BN</td>
      <td>Theory</td>
      <td>3.6250</td>
      <td>—</td>
      <td>392.</td>
      <td>3.31</td>
    </tr>
    <tr>
      <td></td>
      <td>Experiment [25]</td>
      <td>3.615</td>
      <td>—</td>
      <td>369.</td>
      <td>4.0</td>
    </tr>
    <tr>
      <td>$w$-BN</td>
      <td>Theory</td>
      <td>2.6883</td>
      <td>4.3013</td>
      <td>107.</td>
      <td>4.24</td>
    </tr>
    <tr>
      <td></td>
      <td>Experiment [26]</td>
      <td>2.55</td>
      <td>4.20</td>
      <td>—</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

In Table II, the lattice constants, the bulk modulus, and its pressure derivatives are given for three different structures. For the hexagonal and wurtzite structures, the experimental ratios $c/a$ of 2.66 and 1.6 have been used. It should be noted that keeping the $c/a$ ratio constant is equivalent to a pressure with tetragonal symmetry. Ideally, one should calculate the $c/a$ ratio (for all $a$) by minimalization of the total energy. The distance between the basal planes in the wurtzite structure is about 38% smaller than in the hexagonal structure, while the bulk modulus of $w$-BN (1.07 Mbar) is about 28% bigger than that of $h$-BN (0.77 Mbar). However, for the cubic phase, $B_0$ is 3.98 Mbar, which is 5.1 times bigger than the bulk modulus of the hexagonal

<table><caption>TABLE III Calculated values of the pressure coefficients of the band gaps for $h$-, $c$-, and $w$-BN.</caption>
  <thead>
    <tr>
      <th></th>
      <th>$a$ (eV)</th>
      <th>$b$ (meV/GPa)</th>
      <th>$c$ (meV/GPa²)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$h$-BN</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\overline{\Gamma^v \rightarrow \Gamma^c}$</td>
      <td>5.06</td>
      <td>2.6</td>
      <td>$-0.040$</td>
    </tr>
    <tr>
      <td>$M^v \rightarrow M^c$</td>
      <td>3.97</td>
      <td>4.7</td>
      <td>$-0.022$</td>
    </tr>
    <tr>
      <td>$c$-BN</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\Gamma_{15}^v \rightarrow \Gamma_{15}^c$</td>
      <td>8.38</td>
      <td>10.6</td>
      <td>$-0.021$</td>
    </tr>
    <tr>
      <td>$\Gamma_{15}^v \rightarrow X_1^c$</td>
      <td>3.96</td>
      <td>2.5</td>
      <td>$-0.008$</td>
    </tr>
    <tr>
      <td>$w$-BN</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>$\overline{\Gamma^v \rightarrow \Gamma^c}$</td>
      <td>6.21</td>
      <td>59.0</td>
      <td>$-0.196$</td>
    </tr>
    <tr>
      <td>$M^v \rightarrow M^c$</td>
      <td>4.75</td>
      <td>5.4</td>
      <td>$-0.026$</td>
    </tr>
  </tbody>
</table>


![](./images/812308375135059969_1.jpg)

FIGURE 1. Electronic valence charge density of MgTe in the (upper left) zinc blende, (upper right) wurtzite, (lower left) nickel arsenide, and (lower right) rock salt structure (in $e/\mathring{A}^3$).

phase. The experimental values of the bulk moduli of diamond and graphite are, respectively, 4.42 [27] and 0.338 Mbar, which gives a factor of 13.1 difference.

Table III gives the coefficients of the pressure dependence of the band gaps in the three structures according to the formula $E_{0}(p)=a+bp+cp^{2}$, where $E_{0}(p)$ and $a$ are the calculated band gaps at pressure $p$ and at zero pressure. For the hexagonal and wurtzite structures, the coefficients for the direct gaps in the $\Gamma$- and $M$-points are given. It should be noted that these are not the minimum gaps. For the hexagonal $h$-BN, the calculation yields a minimum direct gap from the $H^{v}$ to the $H^{c}$ point of 4.11 eV, while the minimum indirect gap is from $H^{v}$ to $M^{c}$ with a value of 3.65 eV. This shows that $h$-BN is an indirect band gap semiconductor. The experimental measurements indicate that $h$-BN has a direct minimum gap.

However, they disagree on the value which ranges between 3.8 [28] and 5.8 eV [29].

Experimentally, the semiconducting compound MgTe appears in the wurtzite structure [30]. A recent calculation [31] showed that MgTe has a lower energy in the NiAs structure. The compounds of Mg with the VIA elements O, S, Se, and Te all crystallize in the rock salt structure, with the exception of MgTe. Mg compounds can be compared with Mn compounds because the supplementary $3d$ electrons in the latter can be considered as chemically inactive. Now, the compounds of Mn with the same VIA elements also crystallize in the rock salt structure, with the exception of MnTe, which was found in the NiAs structure. Therefore, we performed total energy calculations on MgTe, in the wurtzite, rock salt, zinc blende, and nickel arsenide structures. We used a kinetic energy cutoff of 18 Ry (corresponding to $\approx 1200$

VAN CAMP AND VAN DOREN

<table>
<caption>TABLE IV<br>Calculated and experimental ground-state properties of MgTe in the wurtzite, zinc blende, nickel arsenide, and rock salt structures.</caption>
<thead>
<tr>
<th></th>
<th>Present Work</th>
<th>[31]</th>
<th>Experiment [30]</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Wurtzite</td>
</tr>
<tr>
<td>a (Å)</td>
<td>4.7040</td>
<td>4.505</td>
<td>4.52</td>
</tr>
<tr>
<td>c (Å)</td>
<td>7.2497</td>
<td>7.358</td>
<td>7.38</td>
</tr>
<tr>
<td>c/a</td>
<td>1.6217</td>
<td>1.633</td>
<td>1.6327</td>
</tr>
<tr>
<td>u</td>
<td>0.3772</td>
<td>0.376</td>
<td>—</td>
</tr>
<tr>
<td>B₀ (GPa)</td>
<td>37.3</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>B₀'</td>
<td>3.93</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td colspan="4">Zinc blende</td>
</tr>
<tr>
<td>a (Å)</td>
<td>6.3423</td>
<td>6.364</td>
<td>—</td>
</tr>
<tr>
<td>B₀ (GPa)</td>
<td>36.2</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>B₀'</td>
<td>3.89</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td colspan="4">Nickel arsenide</td>
</tr>
<tr>
<td>a (Å)</td>
<td>4.1009</td>
<td>4.142</td>
<td>—</td>
</tr>
<tr>
<td>c (Å)</td>
<td>6.7001</td>
<td>6.724</td>
<td>—</td>
</tr>
<tr>
<td>c/a</td>
<td>1.6338</td>
<td>1.624</td>
<td>—</td>
</tr>
<tr>
<td>B₀ (GPa)</td>
<td>51.4</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>B₀'</td>
<td>3.89</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td colspan="4">Rock salt</td>
</tr>
<tr>
<td>a (Å)</td>
<td>5.8548</td>
<td>5.846</td>
<td>—</td>
</tr>
<tr>
<td>B₀ (GPa)</td>
<td>48.6</td>
<td>—</td>
<td>—</td>
</tr>
<tr>
<td>B₀'</td>
<td>3.88</td>
<td>—</td>
<td>—</td>
</tr>
</tbody>
</table>

plane waves) for all four structures. For the zinc blende and rock salt structures, we took 10 integration points and 14 for the wurtzite and nickel arsenide structures.

Table IV shows the calculated and experimental ground-state properties of MgTe in the wurtzite, zinc blende, nickel arsenide, and rock salt structures. Also given are the results of the only other ab initio calculation on this material. It can be seen that the agreement between the two calculations is very good, despite the fact that in [31] another form for the exchange-correlation contribution was employed. The agreement with the only experimental value (for wurtzite) is satisfactory.

Figure 1 displays the electronic valence charge densities of MgTe in the four structures. It should be noted that MgTe is fairly ionic (ionicity parameter $f_i = 0.421$ [32]), which is obvious in the nickel arsenide and rock salt structures.

Figure 2 shows the total energy per atom for the four structures as a function of the unit cell volume reduced with the nickel arsenide unit cell volume. It can be seen that the stable structure (at $T=0$) is nickel arsenide. The energy difference between rock salt and nickel arsenide is very small, but within the accuracy limits of the calculation. Next higher in energy, we have, first, the wurtzite structure and then the zinc blende structure. Therefore, we confirm the conclusions of [31] that the stable structure of MgTe, at $T=0$, is nickel arsenide.

![](./images/812308375135059969_2.jpg)

FIGURE 2. Total energy (in Ry/atom) as a function of the reduced volume for zinc blende, wurtzite, nickel arsenide, and rock salt structure of MgTe.

## Conclusion

In this article, ab initio calculations of electronic and mechanical properties based on the total energy of the crystal are reported for the binary compounds in several structures. On the one hand, a calculation is done using a nonlocal functional, derived from an exponentially screened Coulomb interaction. On the other hand, the total energy is calculated in the local density approximation using nonlocal norm-conserving pseudopotentials. Using BN and MgTe as examples, it is shown that several equilibrium properties are calculated with

TOTAL ENERGY CALCULATIONS IN DFT

adequate accuracy to be compared with the experimental data. This provides sufficient confidence to treat these values which have not yet been measured as trustworthy predictions.

### References

1. P. Hohenberg and W. Kohn, Phys. Rev. B **136**, 864 (1964).
2. E. S. Kryachko and E. V. Ludena, *Energy Density Functional Theory of Many-Electron Systems* (Kluwer, Dordrecht, 1989).
3. W. Kohn and L. J. Sham, Phys. Rev. A **140**, 1133 (1965).
4. R. M. Dreizler and E. K. Gross, *Density Functional Theory* (Springer-Verlag, Berlin, 1990).
5. E. Wigner, Phys. Rev. **46**, 1002 (1934).
6. J. P. Perdew and Y. Wang, Phys. Rev. B **33**, 8800 (1986).
7. O. Gunnarson and R. O. Jones, Phys. Scr. **21**, 394 (1980).
8. V. E. Van Doren, P. E. Van Camp, and G. Straub, in *Proceedings of the 22nd International Conference on the Physics of Semiconductors*, D. J. Lockwood, Ed., World Scientific, 1995, p. 185.
9. G. Bachelet, D. Hamann, and M. Schlüter, Phys. Rev. B **26**, 4199 (1982).
10. F. Murnaghan, Proc. Nat. Acad. Sci. U.S.A. **3**, 244 (1944).
11. F. Birch, J. Geophys. Res. **57**, 227 (1952).
12. F. Birch, J. Geophys. Res. **83**, 1257 (1978).
13. P. Vinet, J. Ferrante, J. Smith, and J. Rose, J. Phys. C **19**, L467 (1986).
14. D. Straub, L. Ley, and F. Himpsel, Phys. Rev. Lett. **54**, 142 (1985).

15. R. Hulthen and N. G. Nilson, Solid State Commun. **18**, 1341 (1976).
16. R. W. Godby, M. Schlüter, and L. J. Sham, Phys. Rev. Lett. **56**, 2415 (1986).
17. P. E. Van Camp, V. E. Van Doren, and J. T. Devreese, Solid State Commun. **81**, 23 (1992).
18. P. E. Van Camp, V. E. Van Doren, and J. T. Devreese, Phys. Rev. B **44**, 9056 (1991).
19. P. E. Van Camp, V. E. Van Doren, and J. T. Devreese, Solid State Commun. **71**, 1055 (1989).
20. P. E. Van Camp, V. E. Van Doren, and J. T. Devreese, Phys. Rev. B **38**, 9906 (1988).
21. P. E. Van Camp, V. E. Van Doren, and J. T. Devreese, Phys. Rev. B **41**, 1598 (1990).
22. P. E. Van Camp, V. E. Van Doren, and J. T. Devreese, Phys. Stat. Sol. (b) **146**, 73 (1988).
23. P. E. Van Camp and V. E. Van Doren, *High Press. Res.*, in press (1995).
24. R. W. Lynch and H. G. Drickamer, J. Chem. Phys. **44**, 181 (1966).
25. T. Soma, S. Sawaoka, and S. Saito, Mater. Res. Bull. **9**, 755 (1974).
26. F. P. Bundy and R. H. Wentorf, J. Chem. Phys. **38**, 1144 (1963).
27. M. Grimsditch and A. Ramdas, Phys. Rev. B **11**, 3139 (1975).
28. M. J. Rand and J. F. Roberts, J. Electrochem. Soc. **115**, 423 (1968).
29. W. Baronian, Mater. Res. Bull. **7**, 119 (1972).
30. W. Zachariasen, Z. Phys. Chem. **128**, 417 (1927).
31. C. Y. Yeh, Z. W. Lu, S. Froyen, and A. Zunger, Phys. Rev. B **46**, 10086 (1992).
32. J. C. Phillips, *Bonds and Bands in Semiconductors* (Academic Press, New York, 1973).

---
INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY
345