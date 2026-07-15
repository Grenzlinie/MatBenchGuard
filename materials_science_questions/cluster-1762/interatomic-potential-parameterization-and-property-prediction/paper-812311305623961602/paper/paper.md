INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY, VOL. 51, 201-209 (1994)

# A Density-Functional Method for Calculating Atomic Polarizabilities: Application to Negative Ions*

MANOJ K. HARBOLA

Laser Programme, Centre for Advanced Technology, Indore-452 013, India

## Abstract

We recently proposed a variational method for determining static polarizabilities that uses the ground-state denstiy, rather than the orbitals, of the system for calculations. Thus, the method is different from, and numerically easier than, the perturbation theory approach in which changes in each of the single-particle orbitals have to be obtained self-consistently. For neutral atoms and cations, it leads to results that are comparable to the results obtained by the perturbation theory. In this article, we apply this method, employing Hartree-Fock densities, to obtain polarizabilities for negative ions and show that for negative ions also the results are quite accurate. Thus, the method may prove useful in making quick and accurate estimates of the polarizabilities of more complex systems where orbital based self-consistent calculations become quite complicated. © 1994 John Wiley & Sons, Inc.

## I. Introduction

In this article, we discuss how to obtain electric dipole polarizabilities directly from the ground-state density of a system, thereby obviating the need to recalculate the wave function of the system in presence of the applied electric field. Our approach [1] is physically motivated and makes use of the variational principle for the energy. We first picture how the density of a system becomes distorted under the influence of a uniform electric field. Based on this, we make an ansatz for the induced density and optimize it to obtain the minimum energy when the system is in the field. Thus, once the ground-state density of a system is known, it is used directly to calculate the polarizability of the system. As such, our approach is quite different from, and numerically simpler than, the wave-functional approaches, such as those based on perturbation theory [2]. For simplicity, our discussion is restricted to spherical atoms only, although the method presented is quite general.

Electric dipole polarizability $\alpha$ for spherical systems is defined as the ratio
$$
\lim_{\mathcal{E} \to 0} p_{z}/\mathcal{E}, \tag{1}
$$
where $p_{z}$ is the induced dipole moment when the atom is put in an electric field $\mathcal{E}$ in the $z$ direction. The induced moment is given as
$$
p_{z} = \int z[\rho'(\mathbf{r}) - \rho^{0}(\mathbf{r})] d\mathbf{r}, \tag{2}
$$

*This article was originally submitted for inclusion in the issues dedicated to Dr. Robert G. Parr.

© 1994 John Wiley & Sons, Inc.
CCC 0020-7608/94/040201-09

where $\rho^0(\mathbf{r})$ is the unperturbed density, and $\rho'(\mathbf{r})$, the density in the presence of the field. The applied field also causes a change in the total energy of the system. The new energy $E'$ is given as

$$
E' = E^0 - \frac{1}{2} \alpha \mathcal{E}^2 \tag{3}
$$

up to the second order in $\mathcal{E}$. Here, $E^0$ is the unperturbed ground-state energy. (It should be pointed out that, in general, polarizability is a tensor quantity, and the equations above are simplified versions, due to the spherical symmetry, of the more general equations relating the applied field, the induced dipole moment, and the corresponding change in the energy.) Thus, the energy-based method to obtain the polarizability is to first solve the Schrödinger equation in the presence of the applied field and to calculate the resulting change in the energy up to second order in $\mathcal{E}$. $\alpha$ is then calculated by Eq. (3). This is usually done by employing the perturbation theory. One can also calculate the new density from the modified wave function and then use Eqs. (1) and (2) to calculate $\alpha$. Results of the two calculations must, of course, match. The purpose of the present article, however, was to calculate---in the spirit of density-functional theory [3]---the induced density and the resulting change in the energy directly from the ground-state density of the unperturbed system. The advantages of such an approach that uses the density as the basic variable are well known [3]. To make this clear and to bring out the differences between the wave-functional and the density-based approaches, we start with a brief discussion of the orbital-based approach of polarizability calculations with the particular example of Kohn-Sham formalism [4]. We then present our method [1] and apply it to obtain polarizabilities for the negative ions of hydrogen and the halogens by employing the Hartree-Fock wave functions [5].

## II. Kohn-Sham Formalism

In the Kohn-Sham (KS) formalism, a system of $N$ interacting electrons in an external potential $V_{\text{ext}}(\mathbf{r})$ is replaced by a system of $N$ noninteracting Fermions moving in a local effective potential. The single-particle orbitals of these noninteracting particles are obtained by solving the KS equations (atomic units are used throughout the article):

$$
\left[ -\frac{1}{2} \nabla^2 + V_{\text{ext}}(\mathbf{r}) + V_H(\mathbf{r}) + V_{xc}(\mathbf{r}) \right] \phi_i(\mathbf{r}) = \epsilon_i \phi_i(\mathbf{r}), \tag{4}
$$

where $V_H(\mathbf{r})$ is the Hartree potential and $V_{xc}(\mathbf{r})$ is the effective exchange-correlation potential. The orbitals $\varphi_i(\mathbf{r})$ themselves have no meaning but lead to the ground-state density $\rho(\mathbf{r})$ of the interacting electronic system via $\rho(\mathbf{r}) = \sum_i |\varphi_i(\mathbf{r})|^2$. As is well known, the Hartree potential and the exchange-correlation potentials are obtained [3,4] as the functional derivatives of the corresponding energy functionals. However, the exchange-correlation functional is not known exactly and one usually makes the local density approximation [3,4] for it. The total ground-state energy is calculated as the sum

$$
T_s[\rho] + \int \rho(\mathbf{r}) V_{\text{ext}}(\mathbf{r}) d\mathbf{r} + E_H[\rho] + E_{xc}[\rho], \tag{5}
$$

where

$$
T_s[\rho] = \sum_i \langle \phi_i | -\frac{1}{2} \nabla^2 | \phi_i \rangle \tag{6}
$$

is the noninteracting kinetic energy,
$$
E_{H}[\rho]=\frac{1}{2} \iint \frac{\rho(\mathbf{r}) \rho\left(\mathbf{r}^{\prime}\right)}{\left|\mathbf{r}-\mathbf{r}^{\prime}\right|} d \mathbf{r} d \mathbf{r}^{\prime}
\tag{7}
$$
is the Hartree energy, and $E_{x c}[\rho]$ is the exchange-correlation energy. The exchange energy within the local density approximation (LDA) is given in terms of the density as
$$
E_{x}^{\mathrm{LDA}}[\rho]=\int \rho(\mathbf{r}) \epsilon_{x}^{\mathrm{hom}}(\mathbf{r}) d \mathbf{r},
\tag{8a}
$$
where
$$
\epsilon_{x}^{\mathrm{hom}}(\mathbf{r})=d_{0} \rho^{1 / 3}(\mathbf{r}),
\tag{8b}
$$
with $d_{0}=-3 / 4(3 / \pi)^{1 / 3}$. For the correlation energy, there are many different functionals available. We give here the one due to Gunnarsson and Lundquist [6], which is
$$
E_{c}^{\mathrm{LDA}}[\rho]=\int \rho(\mathbf{r}) \epsilon_{c}^{\mathrm{hom}}(\mathbf{r}) d \mathbf{r},
\tag{9a}
$$
where
$$
\epsilon_{c}^{\mathrm{hom}}(\mathbf{r})=c\left\{\left(1+x^{3}\right) \ln \left(1+\frac{1}{x}\right)+\frac{x}{2}-x^{2}-\frac{1}{3}\right\},
\tag{9b}
$$
with $c=-0.0333, x=r_{s} / A, A=11.4$, and where $r_{s}=[3 / 4 \pi \rho(\mathbf{r})]^{1 / 3}$ is the local $r_{s}$ value. This particular correlation energy functional leads to results for polarizability that are closest to the experimental values [2].

Now if the system is put into a weak external electric field $\mathcal{E}$ in the $z$ direction, the external potential changes to $V_{\text {ext }}(\mathbf{r})+\mathcal{E} r \cos \theta$. This induces a change in the orbitals and, therefore, in the density. The change in the density also makes $V_{H}(\mathbf{r})$ and $V_{x c}(r)$ different from the original problem. Thus, the new KS equation is
$$
\begin{aligned}
{\left[-\frac{1}{2} \nabla^{2}+V_{\mathrm{ext}}(\mathbf{r})+\mathcal{E} r\right.} & \cos \theta+V_{H}(\mathbf{r}) \\
& \left.+\delta V_{H}(\mathbf{r})+V_{x c}(\mathbf{r})+\delta V_{x c}(\mathbf{r})\right]\left(\phi_{i}+\delta \phi_{i}\right) \\
& =\left(\epsilon_{i}+\delta \epsilon_{i}\right)\left(\phi_{i}+\delta \phi_{i}\right), \quad(10)
\end{aligned}
$$
where $\delta V_{H}(\mathbf{r})$ and $\delta V_{x c}(\mathbf{r})$ are the changes in the Hartree and the exchange-correlation potentials, respectively. This equation is to be solved self-consistently up to the desired order to obtain the new perturbed orbitals $\varphi_{i}(\mathbf{r})+\delta \varphi_{i}(\mathbf{r})$ that lead to the new density $\rho^{\prime}(\mathbf{r})$ and energy $E^{\prime}$. The polarizabilities can then be calculated from Eq. (3) or Eqs. (1) and (2). The results thus obtained are self-consistent in that the change in the effective potential due to the change in the density is fully accounted for. When the KS equation is solved within the local density approximation (LDA), this approach is usually referred to as the time-dependent local density approximation (TDLDA) method. A similar approach can also be applied within the Hartree-Fock approximation: The method is then called the coupled Hartree-Fock (CHF) approach. As is clear from this discussion, the TDLDA and the CHF approaches both require the perturbed problem self-consistent solutions for all the orbitals. In the density-based method that we discuss below, the need for such a calculation involving each orbital is circumvented because all the relevant quantities are calculated from the density itself.

## III. Density-based Approach to Calculating Polarizabilities

Our approach [1] using the density directly for calculations is based on the variational principle for the energy. First, by considering how a charge distribution gets distorted under the influence of a weak electric field, we make an ansatz for the form of the induced density. We then optimize it to obtain the minimum energy when the atom is put into the electric field. Further, since the unperturbed energy is already known, it is only the change in the energy ($E' - E^0$) that is to be minimized with respect to the induced density. However, to be able to do so, we need to express the kinetic energy of the system as a functional of the density since Eq. (6) can no longer be applied to calculate the kinetic energy. (Notice that all the other components of the total energy, using the LDA for the exchange and correlation, are expressed in terms of the density itself.) Furthermore, this functional must also give the change in the energy, when the density is altered, accurately. This is because in the polarizability calculations it is the energy change, rather than the energy itself, that is of particular significance. In this section, we discuss our ansatz for the variational form of the induced density and the kinetic energy functional that we use. The corresponding expressions for the change in the energy are also given.

### (a) Induced Density

The variational form of the induced density that we apply is motivated by the following physical considerations: Consider a distribution of electrons given by the density $\rho(\mathbf{r})$. When subjected to a uniform electric field $\mathcal{E}$, if this distribution were to just shift rigidly in the direction opposite to the field, the new density $\rho'(\mathbf{r})$ would be given as
$$
\rho'(\mathbf{r}) = \rho^0(\mathbf{r}) + a\mathcal{E} \cdot \nabla\rho(\mathbf{r}) \tag{11}
$$
to the first order in $\mathcal{E}$. Here "a" is a constant giving the amount of shift. The question that we now ask is if, in general, the new density can also be derived from such a simple physical picture. We now explain that this, indeed, is possible, at least for spherical systems, as is indicated by the hydrogen atom problem. For the hydrogen atom, the induced density can be calculated exactly [7]. To the first order in $\mathcal{E}$, the induced density in the hydrogen atom is given as
$$
\begin{align*}
\rho^{\text{ind}}(\mathbf{r}) &= \rho'(\mathbf{r}) - \rho^0(\mathbf{r}) \\
&= -\left(2r + r^2\right)\rho(\mathbf{r})\mathcal{E} \cos \theta . \tag{12}
\end{align*}
$$

However, for the hydrogen atom, $\rho(\mathbf{r})$ is proportional to $|\nabla\rho(\mathbf{r})|$ so that Eq. (12) can be rewritten as
$$
\rho'(\mathbf{r}) = \rho^0(\mathbf{r}) + (ar + br^2)\mathcal{E} \cdot \nabla\rho^0(\mathbf{r}), \tag{13}
$$
where $a$ and $b$ are two constants. Now, Eq. (13) can be interpreted physically. It represents a distortion in the density as if locally the density contours are being shifted in the direction of the field by $(ar + br^2)$. As such, we make the assumption that for any system, in general, this is how the density is distorted and, therefore, the new density can be written as Eq. (12) with $(ar + br^2)$ replaced by a more general function $\Delta(\mathbf{r})$ so that
$$
\rho'(\mathbf{r}) = \rho^0(\mathbf{r}) + \Delta(\mathbf{r})\mathcal{E} \cdot \nabla\rho^0(\mathbf{r}), \tag{14}
$$

The function $\Delta(\mathbf{r})$ is to be so chosen that the integral of the induced density vanishes. For spherically symmetric systems considered in this article, this is guaranteed with a function that depends on $r$ only. We take $\Delta(\mathbf{r})$ to be of the polynomial form $ar + br^2 + cr^3 + \dots$, where $a$, $b$, $c\dots$ are taken to be the variational parameters. It is seen [1] that three parameters are sufficient to give accurate results. Inclusion of more parameters does not change $\alpha$ significantly. We also assume that the next-order correction to the density is negligible.

### (b) Kinetic Energy Functional

The most widely used kinetic energy functional in the literature is that derived in the gradient expansion approximation (GEA) [8]. In this, the zeroth order is the Thomas-Fermi functional

$$
T_{\mathrm{TF}}[\rho]=c_{0} \int \rho^{5 / 3}(\mathbf{r}) d \mathbf{r}, \tag{15}
$$

with $c_{0}=(3 / 10)\left(3 \pi^{2}\right)^{2 / 3}$. Corrections to this term are given in terms of the gradient of the density. The first term in this series is proportional to the von Weizsäcker functional [9]

$$
T_{W}[\rho]=\frac{1}{8} \int \frac{|\nabla \rho(\mathbf{r})|^{2}}{\rho(\mathbf{r})} d \mathbf{r}. \tag{16}
$$

However, the GEA functional is derived by assuming that the corresponding densities are slowly varying. As such, it cannot be expected to be accurate when the system has large inhomogeneities. This is the situation when we are dealing with induced densities, as they tend to change rapidly over short distances. Therefore, the GEA cannot be employed to calculate kinetic energy changes associated with these densities. On the other hand, for intrinsically inhomogeneous electron gas, the von Weizsäcker term itself can be taken to be the zeroth-order term. In fact, it is exact for one- (in spin-polarized form) and two-electron systems. For other systems, corrections to it [10] are given by a term proportional to the Thomas-Fermi functional. Thus, the kinetic energy functional can also be given as [11]

$$
T_{S}[\rho]=T_{W}[\rho]+f(N) T_{\mathrm{TF}}[\rho]. \tag{17}
$$

It is this functional that we use for our calculations. It has already been shown [1] that this functional describes well the response properties of atomic systems. The reason for this is as follows: The von Weizsäcker (Thomas-Fermi) functional represents [10] accurately the change in the kinetic energy of a homogeneous electron gas in the limit of it being put in a rapidly (slowly) varying perturbing field. Thus, an optimized combination of the two can be expected to give accurately the change in the kinetic energy of a system when it is subjected to a perturbing field. We choose the factor [12]

$$
f(N)=\left(1-\frac{2}{N}\right)\left(1-\frac{A_{1}}{N^{1 / 3}}+\frac{A_{2}}{N^{2 / 3}}\right) \tag{18}
$$

with the optimized parameters [13] $A_{1}=1.314$ and $A_{2}=0.0021$.

Employing the kinetic energy functional given by Eq. (17), and the expressions for the external energy [Eq. (5)], Hartree energy [Eq. (7)], and the exchange-correlation energy [Eqs. (8) and (9)] in conjunction with the induced density given by Eq. (14), the change in the total energy is calculated up to $O(\mathcal{E}^{2})$. This is given as

$$
\Delta E=\Delta T_{S}+\Delta E_{\mathrm{ext}}+\Delta E_{H}+\Delta E_{X}+\Delta E_{C}, \tag{19}
$$

where for spherical systems,

$$
\begin{aligned}
\frac{\Delta T_{s}}{E^{2}}= & \frac{\pi}{6} \int_{0}^{\infty} d r r^{2} \frac{1}{\rho^{0}}\left[\frac{\Delta^{2}}{\rho^{02}}\left(\frac{d \rho^{0}}{d r}\right)^{4}+\left\{\left(\frac{d \rho^{0}}{d r}\right)\left(\frac{d \Delta}{d r}\right)+\Delta \frac{d^{2} \rho^{0}}{d r^{2}}\right\}\right. \\
& \left.\times\left\{\left(\frac{d \rho^{0}}{d r}\right)\left(\frac{d \Delta}{d r}\right)-2 \frac{\Delta}{\rho^{0}}\left(\frac{d \rho^{0}}{d r}\right)^{2}+\Delta \frac{d^{2} \rho^{0}}{d r^{2}}\right\}+2 \frac{\Delta^{2}}{r^{2}}\left(\frac{d \rho^{0}}{d r}\right)^{2}\right] \\
& +\frac{20 \pi}{27} f(N) c_{0} \int_{0}^{\infty} d r r^{2} \rho^{05 / 3} \Delta^{2}\left(\frac{1}{\rho^{0}} \frac{d \rho^{0}}{d r}\right)^{2},
\end{aligned}
\tag{20}
$$

$$
\frac{\Delta E_{\text {ext }}}{E^{2}}=\frac{4 \pi}{3} \int d r r^{3} \Delta(r)\left(\frac{d \rho^{0}}{d r}\right),
\tag{21}
$$

$$
\begin{aligned}
\frac{\Delta E_{H}}{E^{2}}= & \frac{8 \pi^{2}}{9} \int_{0}^{\infty} d r \int_{0}^{r} d r^{\prime} r^{\prime 3} \Delta(r) \Delta\left(r^{\prime}\right)\left(\frac{d \rho^{0}}{d r}\right)\left(\frac{d \rho^{0}}{d r^{\prime}}\right) \\
& +\frac{8 r^{2}}{9} \int_{0}^{\infty} d r r^{3} \int_{r}^{\infty} d r^{\prime} \Delta(r) \Delta\left(r^{\prime}\right)\left(\frac{d \rho^{0}}{d r}\right)\left(\frac{d \rho^{0}}{d r^{\prime}}\right),
\end{aligned}
\tag{22}
$$

$$
\frac{\Delta E_{x}}{E^{2}}=\frac{8 \pi d_{0}}{27} \int_{0}^{\infty} d r r^{2} \rho^{04 / 3} \Delta^{2}\left(\frac{1}{\rho^{0}} \frac{d \rho^{0}}{d r}\right)^{2},
\tag{23}
$$

$$
\frac{\Delta E_{c}}{E^{2}}=\frac{4 \pi}{3} c \int_{0}^{\infty} d r r^{2}\left\{-\frac{\alpha}{9 A}+\frac{\beta}{18 A^{2}}\right\} \rho^{0} \Delta^{2}\left(\frac{1}{\rho^{0}} \frac{d \rho^{0}}{d r}\right)^{2},
\tag{24a}
$$

where

$$
\alpha=\frac{1}{2}-2 x^{0}+3 x^{0} \ln \left(1+\frac{1}{x^{0}}\right)-\frac{\left(1+x^{03}\right)}{x^{0}\left(1+x^{0}\right)},
\tag{24b}
$$

and

$$
\beta=-2+6 x^{0} \ln \left(1+\frac{1}{x^{0}}\right)-\frac{6 x^{0}}{\left(1+x^{0}\right)}+\frac{\left(1+x^{03}\right)\left(1+2 x^{0}\right)}{x^{02}\left(1+x^{0}\right)^{2}},
\tag{24c}
$$

with $x^{0}$ being related to $\rho^{0}$ as given above in Eq. (9), represent the changes in the kinetic, external, Hartree, exchange, and correlation energies, respectively. Now, the quantity $\Delta E / E^{2}$ is minimized with respect to the parameters $a, b \ldots$ of $\Delta(r)$, and leads to $\alpha$ via Eq. (3). $\Delta(r)$ obtained in this manner also leads to the induced density via Eq. (14) and, therefore, to $\alpha$ through Eqs. (1) and (2). It is immediately clear from the expressions above that because the density-instead of the orbitals-is being used directly to calculate the energy the expression for the change in the total energy is much simpler than its wave-functional counterpart. As a consequence, the method presented above is also numerically easier to implement than is the TDLDA or CHF approach to calculating the polarizability.

We note here that in the past similar variational procedures in terms of the orbitals have been applied $[14,15]$ to calculate dipole and quadrupole polarizabilities of atoms and ions. Although

these calculations are quite easy for up to two-electron atoms and ions, they become rather complicated as the number of electrons increases. Not only does the number of variational parameters increase with the orbitals, but inclusion of self-consistency also becomes quite difficult [15]. On the other hand, if the density is used instead of the orbitals, the number of parameters remains the same irrespective of the number of orbitals needed to describe the system.

The procedure discussed above has already been applied in [1] to neutral atoms and positive ions. The unperturbed density was obtained by solving the KS equation within the LDA. It has been shown there that the results obtained compare well with the corresponding TDLDA values.

## IV. Application to Negative Ions

We now apply the method described above to the ions $H^-$, $F^-$, $Cl^-$, $Br^-$, and $I^-$. The unperturbed ground-state density employed is that obtained from the Hartree-Fock wave functions [5]. Thus, the effects of Coulomb correlations are not represented in the ground-state density that we are using. To be consistent, Coulomb correlation energy is also not included in the total energy functional. Furthermore, we treat the exchange energy within the LDA. Thus, the results obtained are compared with those of CHF [15,16]. In Table I, we present the results obtained with $\Delta(r) = ar + br^2 + cr^3$ along with the CHF results. We have checked the results by including more parameters in the function $\Delta(r)$. In this case, too, the results do not change significantly with a greater number of parameters. It is clear from the table that, like the neutral atoms and cations [1], the results for the anions also match well with those obtained self-consistently with the perturbation theory. In fact, for the anions, the results are more accurate than those for neutral and positively charged atoms. The reasons for this may be as follows: First, our ansatz for the induced density should be accurate when the ground-state density employed is obtained from the effective potential that has the correct asymptotic behavior, i.e., it decays as $-1/r$, as is the case for the hydrogen atom for which Eq. (14) is exact. Hartree-Fock densities employed for the negative ions indeed satisfy this criterion. On the other hand, the densities for the neutral and positive ions were obtained from the LDA KS equation for which the effective potential decays exponentially for asymptotic distances from

<table>
<caption>Table I. Dipole polarizabilities (in atomic units) of negative ions of hydrogen and the halogens; the first column gives the values obtained by applying the method of this article and the second column gives the CHF values.</caption>
<thead>
<tr>
<th rowspan="2">Ion</th>
<th colspan="2">Polarizability</th>
</tr>
<tr>
<th>Present work</th>
<th>CHF</th>
</tr>
</thead>
<tbody>
<tr>
<td>$H^-$</td>
<td>98.81</td>
<td>93.4<sup>a</sup></td>
</tr>
<tr>
<td>$F^-$</td>
<td>10.35</td>
<td>10.41<sup>b</sup></td>
</tr>
<tr>
<td>$Cl^-$</td>
<td>28.76</td>
<td>28.36<sup>b</sup></td>
</tr>
<tr>
<td>$Br^-$</td>
<td>37.53</td>
<td>38.71<sup>b</sup></td>
</tr>
<tr>
<td>$I^-$</td>
<td>55.90</td>
<td>55.75<sup>b</sup></td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="3"><sup>a</sup>[16].<br><sup>b</sup>[15].</td>
</tr>
</tfoot>
</table>

<table>
<caption>Table II. Parameters $a$, $b$, and $c$ for the function $\Delta(r) = ar + br^2 + cr^3$ [see Eq. (14) of the text] for different ions.</caption>
<thead>
<tr>
<th>Ion</th>
<th>$a$</th>
<th>$b$</th>
<th>$c$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$H^-$</td>
<td>$-1.12$</td>
<td>$1.95$</td>
<td>$2.31 \times 10^{-1}$</td>
</tr>
<tr>
<td>$F^-$</td>
<td>$-9.91 \times 10^{-4}$</td>
<td>$2.30 \times 10^{-2}$</td>
<td>$1.55 \times 10^{-1}$</td>
</tr>
<tr>
<td>$Cl^-$</td>
<td>$3.41 \times 10^{-3}$</td>
<td>$-7.56 \times 10^{-2}$</td>
<td>$1.56 \times 10^{-1}$</td>
</tr>
<tr>
<td>$Br^-$</td>
<td>$7.47 \times 10^{-3}$</td>
<td>$-1.14 \times 10^{-1}$</td>
<td>$1.57 \times 10^{-1}$</td>
</tr>
<tr>
<td>$I^-$</td>
<td>$9.29 \times 10^{-3}$</td>
<td>$-1.30 \times 10^{-1}$</td>
<td>$1.51 \times 10^{-1}$</td>
</tr>
</tbody>
</table>

the nucleus. Second, the coefficients $A_1$ and $A_2$ in Eq. (18) for the kinetic energy functional were obtained [13] for the Hartree-Fock densities, and, therefore, the functional itself should be more accurate when employed with these densities.

For completeness, we give in Table II the parameters $a$, $b$, and $c$ for the function $\Delta(r)$. It is seen that for the halogen ions the parameter $c$ is almost a constant, whereas the parameters $a$ and $b$ change from ion to ion.

### V. Concluding Remarks

An alternative method for calculating dipole polarizabilities has been presented. The method requires only the ground-state density of the atom of interest to calculate $\alpha$. In this article, the accuracy of the method in comparison with the coupled Hartree-Fock approach has been demonstrated with the examples of negatively charged ions. Although applied here to spherically symmetric systems, by choosing appropriate $\Delta(\mathbf{r})$, this method can be generalized for other systems that are not so symmetric to obtain quick and accurate estimates of the polarizabilities of those systems. It would also be useful to include in Eq. (13) higher-order corrections to the density in order to be able to obtain higher-order polarizabilities of the system of interest.

### Acknowledgments

I wish to thank the editors of the *International Journal of Quantum Chemistry* for their invitation to contribute to the special issue of the journal honoring Professor Robert G. Parr. I also wish to acknowledge with gratitude that the time I spent with Professor Parr helped me a lot in evolving as a researcher.

### Bibliography

[1] M. K. Harbola, Phys. Rev. A **48**, 2696 (1993).

[2] G. D. Mahan and K. R. Subbaswamy, *Local Density Theory of Polarizability* (Plenum, New York, 1990), and references therein.

[3] N. H. March, *Electron Density Theory of Atoms and Molecules* (Academic Press, London, 1992); R. M. Dreizler and E. K. U. Gross, *Density-Functional Theory* (Springer-Verlag, Berlin, 1990); R. G. Parr and W. Yang, *Density-Functional Theory of Atoms and Molecules* (Oxford University Press, Oxford, 1989).

[4] W. Kohn and L. J. Sham, Phys. Rev. **140**, A 1133 (1965).

[5] E. Clementi and C. Roetti, At. Data Nucl. Data Tab. 14, 177 (1974); K. D. Sen and M. K. Harbola, Chem. Phys. Lett. 178, 347 (1991) for $H^-$.

[6] O. Gunnarsson and B.I. Lundquist, Phys. Rev. B 13, 4274 (1979).

[7] L.I. Schiff, Quantum Mechanics (McGraw Hill, New York, 1968).

[8] D. A. Kirzhnits, Field Theoretical Methods in Many-Body Systems (Pergamon, London, 1967).

[9] C.F. von Weizsäcker, Z. Phys. 96, 431 (1935).

[10] W. Jones, Phys. Lett. A 34, 351 (1971); W. Jones and W.H. Young, J. Phys. C 4, 1322 (1971).

[11] P.K. Acharya, L.J. Bartolotti, S.B. Sears, and R.G. Parr, Proc. Natl. Acad. Sci. U.S.A. 77, 6978 (1980).

[12] J.L. Gázquez and J. Robles, J. Chem. Phys. 76, 1467 (1982).

[13] S.K. Ghosh and L.C. Balbás, J. Chem. Phys. 83, 5778 (1985).

[14] T.P. Das and R. Bersohn, Phys. Rev. 102, 733 (1956); E.G. Wikner and T.P. Das, Phys. Rev. 107, 497 (1957).

[15] P.C. Schmidt, A. Weiss, and T.P. Das, Phys. Rev. B 19, 5525 (1979).

[16] H.D. Cohen, J. Chem. Phys. 43, 3558 (1965).

Received March 18, 1993

Revised manuscript received March 2, 1994

Accepted for publication March 11, 1994