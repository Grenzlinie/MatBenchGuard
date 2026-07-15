# Competition between isotropic and strongly anisotropic terms in the impact ionization rate of narrow- and middle-gap cubic semiconductors

A. N. Afanasiev, $^{a)}$ A. A. Greshnov, and G. G. Zegrya
Ioffe Institute, St. Petersburg 194021, Russia

(Dated: 16 December 2021)

We report on the strong anisotropy of the inter-band process of impact ionization in direct-gap cubic semiconductors with either weak or strong spin-orbit coupling at low effective temperatures of electron distribution $T$, and the crossover to isotropic behavior with increasing $T$. Such anisotropy is related to specific mechanism of the impact ionization involving coupling of the electron and heavy hole states *via* remote bands, which is vanishing for some high-symmetry propagation directions of an initial electron, namely [100] and [111]. At room temperature impact ionization rate in narrow-gap semiconductors InSb, InAs, GaSb and $\text{In}_{0.53}\text{Ga}_{0.47}\text{As}$ is isotropic while in middle-gap InP, GaAs and CdTe both terms are comparable. We propose simple and justified analytic generalization of Keldysh formula for the impact ionization rate valid for direct-gap semiconductors with $E_g$ up to 1.5 eV, which is suitable for incorporation into modelling software.

## I. INTRODUCTION

A phenomenon of the interband impact ionization consisting in generation of the electron-hole pairs forced by the Coulomb interaction between a hot conduction band electron and the electrons filling the valence band, as illustrated in Fig. 1a, plays an important role in many electronic devices. In some of them, *viz.* the conventional semiconductor diodes and MOSFETs, the avalanche breakdown caused by impact ionization restricts the operation voltages, so traditionally the effect is perceived as *negative*. Actually, it is *positive* in many other devices, for which multiplication of carriers due to impact ionization forms a principle of operation. Among them are avalanche transit-time diodes (IMPATT), avalanche photodiodes (APD)$^1$ and a transistor with field-effect control of impact ionization (I-MOS)$^2$, which demonstrates the slope of the subthreshold part of the I-V characteristics up to 5 mV/dec at $T=400$ K, leading to significant reduction of the switching times in comparison to the conventional devices.

Nowadays, numerical modelling of the physical processes occurring inside the semiconductor devices has become inherent part of engineering, but often the physical models embedded to software are phenomenological and inaccurate, with too many tuning parameters used. Since in practice the output characteristics arising from impact ionization depend on many details, including specific band structure of a given material and characteristics of the relaxation processes giving a particular form of the non-equilibrium distribution function, the problem of calculation, say, of the I-V characteristics, starting directly from a band structure model is in no sense easy, from both conceptual and technical points of view. Therefore, the most popular method for modelling is Monte Carlo$^{3-13}$, but it is obviously dependent on a particular relation between the impact ionization rate and the energy of a hot electron initiating the process, $W(E)$. Phenomenologically, the rate must grow like a power of the excess energy above a threshold,

$$
W(E)=C(E-E_{\text{th}})^n, \tag{1}
$$

but the values of $n$ and $C$ cannot be revealed without quantum-mechanical calculations, and another question is how far from a threshold this trend holds. While the most popular in literature$^{14}$, quadratic dependence $(n=2)$ was first given by Keldysh$^{15}$ from quite general arguments more than half a century ago, a coefficient before the second power of the excess energy in (1) has never been calculated analytically except for an estimation by the "f-sum" rule$^{16}$, which turned out to be much larger than a value obtained from numerical calculations using the 30-band $\mathbf{k}\cdot\mathbf{p}$ model$^{17}$. Some textbooks even advise looking at the prefactor as an adjustable parameter "to agree with experimental results" at fixed $n=2$ (see$^{18}$, p. 511). Actually, troubles with quadratic contribution stem from the fact that it vanishes within the spherically symmetric bands, which is the case of the simplest 8-band $\mathbf{k}\cdot\mathbf{p}$ model which takes into account the direct coupling between the $s$-type conduction band and the $p$-type valence band only. Therefore, calculation of the Coulomb matrix element entering analytic expression for the impact ionization rate requires going beyond this approximation and taking into account coupling to the remote bands$^{19}$, and a magnitude of the quadratic term turns out to be rather small. This fact was confirmed by some numerical studies$^{20}$, and rather cubic $(n=3)$ than quadratic dependence was found. Analytic expression for the cubic term can be found in the only paper by Gelmont *et al.*$^{21}$, but without any derivation. Thus, a proper analytic answer for $W(E)$ has been inaccessible to the specialists in Monte Carlo modelling, so they prefer using some arbitrary values of the power $n$ (and prefactor $C$) such as $n=2.5$ and $n=4.3^{22}$, $n=5^3$, $n=3^{4,6,23}$, $n=3.9^{24}$, $n=1.85^{25}$. Some theoretical studies were focused on giving efficient recipes for the proper choice and numerical solution of the band models suitable for the realistic modelling$^{26,27}$, but incorporation of

$^{a)}$Electronic mail: afanasiev.an@mail.ru

![](./images/867759472146120937_1.jpg)

FIG. 1. a) Cartoon of the elementary act of impact ionization;
b) Schematic representation of the 14-band $\mathbf{k} \cdot \mathbf{p}$ model.

the band calculations into Monte Carlo modelling seems
too complicated to be practical. So far, most real en-
gineering calculations of devices just use (1) with freely
tuned parameters $n$ and $C$, resulting in uncontrollable
results.

The aim of this paper is to shed light on real form
of $\mathcal{W}(E)$ for the direct-gap semiconductors under prac-
tically important conditions implying that the effective
temperature of the non-equilibrium distribution of elec-
trons is of the order of a few tens of meV. We provide
explicit analytical expressions for the coefficients in the
quadratic and cubic terms and give estimation for the
crossover temperature $T^{*}$ at which the carrier generation
rates due to both contributions become equal, under as-
sumption of a model isotropic classical distribution of the
non-equilibrium electrons. Our results give qualitative
explanation and quantitative criteria for strong domina-
tion of the cubic term at room temperature in the narrow-
gap semiconductors, while in middle-gap semiconductors
both terms are comparable.

## II. THEORY

Usually, the conduction band electrons are treated as
the quasi-particles, which do not interact with the elec-
trons filling the valence bands, and even the process of
(chcc-type) Auger recombination can be viewed as a re-
sult of the interaction of just two electrons, one going to
a higher state in the conduction band and another one
to a free state in the valence band. For the interband
impact ionization this is not true since it is initiated by
the Coulomb interaction between a hot conduction band
electron and all the electrons of the valence bands, the
fact easily verified within the Hartree-Fock approxima-
tion. Therefore, a partial rate due to the elementary
process sketched in Fig. 1a, given by

$$
W=\frac{2 \pi}{\hbar}\left|\left\langle\alpha_{1} \alpha_{2}\left|\frac{e^{2}}{\varkappa\left|\mathbf{r}_{1}-\mathbf{r}_{2}\right|}\right| \alpha_{0} \alpha_{3}\right\rangle\right|^{2} \delta(\Delta E), \quad (2)
$$

must be summed over the possible initial states of the
electron 3 in the valence bands and the possible final
states of the electrons 1 and 2 in the conduction band
to obtain the total impact ionization rate due to a given
hot electron "0". Here $\Delta E=E_{1}+E_{2}-E_{0}-E_{3}$ is the
energy balance and $\alpha_{i}=\{\mathbf{k}_{i}, \xi_{i}\}$ denotes a full set of
the quantum numbers - wave vector $\mathbf{k}_{i}$ and total angu-
lar momentum projection $\xi_{i}$ - in the conduction (i=0,1
or 2) or the valence band (i=3). Concerning the latter,
we consider only the processes involving the heavy hole
states since the light hole and spin-orbit split hole states
lie well below in energy for the wave vectors bigger than
the threshold one and are relevant for the very hot and
rare initial electrons only. Applying the Fourier trans-
form and integrating out the zero-$\mathbf{k}$ Bloch functions, it
is straightforward$^{16,18}$ to rewrite (2) as

$$
W=\frac{2 \pi}{\hbar}\left(\frac{4 \pi e^{2}}{\varkappa}\right)^{2} \frac{I_{c c}\left(\alpha_{0}, \alpha_{1}\right) I_{c v}\left(\alpha_{2}, \alpha_{3}\right)}{\left|\mathbf{k}_{0}-\mathbf{k}_{1}\right|^{4}} \delta_{\Delta \mathbf{k}, 0} \delta(\Delta E),
$$

where the squared overlap integrals of the Bloch func-
tions $I_{c c}$ and $I_{c v}$ can be expressed in terms of the state
vectors $|\mathcal{F}\rangle$ defined in a basis of the $\Gamma$-point Bloch func-
tions $u_{n}^{(0)}(\mathbf{r})$ as $I_{c, c / v}(\alpha_{i}, \alpha_{j})=|\langle\mathcal{F}_{\alpha_{i}}|\mathcal{F}_{\alpha_{j}}\rangle|^{2}$ and $\Delta \mathbf{k}=$
$\mathbf{k}_{0}+\mathbf{k}_{3}-\mathbf{k}_{1}-\mathbf{k}_{2}$ denotes the momentum balance. The en-
ergy and momentum conservation laws expressed by the
delta functions in (3) impose restrictions on the wave vec-
tors $\mathbf{k}_{i}$, which set the following impact ionization thresh-
old when non-parabolicity in dispersion of the initial elec-
tron is taken into account at $\mu=m_{e}/m_{hh} \ll 1^{28}$:

$$
\mathbf{k}_{0}^{\mathrm{th}}=\mathbf{k}_{g}(1+3 \mu / 2), \quad (4)
$$

$$
E_{\mathrm{th}}=E_{e}\left(\mathbf{k}_{0}^{\mathrm{th}}\right)=E_{g}(1+2 \mu), \quad (5)
$$

$$
\mathbf{k}_{3}^{\mathrm{th}}=-\mathbf{k}_{g}(1-\mu / 2), \quad (6)
$$

$$
\mathbf{k}_{1}^{\mathrm{th}}=\mathbf{k}_{2}^{\mathrm{th}}=\mu \mathbf{k}_{g}, \quad (7)
$$

where $k_{g}=\frac{2}{\hbar}\sqrt{F_{1}(\Delta_{0}/E g)m_{e}E_{g}}$ with $F_{1}(x)=$
$\frac{(1+2x/3)(1+x/2)}{(1+x)(1+x/3)}$. Since $\mathbf{k} \cdot \mathbf{p}$ coupling between the con-
duction band $\Gamma_{6 c}$ (or "c" in Fig. 1b) and valence bands
$\Gamma_{8 v}$ and $\Gamma_{7 v}$ (or "v" in Fig. 1b) does not contribute to
dispersion of the heavy holes, the smallness of $\mu$ is equiv-
alent to $E_{g}/E_{G} \ll 1$, where $E_{G}$ is a minimal distance
from $v$ to the bands contributing to the inverse heavy
hole mass ($c'$ band in the 14-band $\mathbf{k} \cdot \mathbf{p}$ model used in
this work, see Fig. 1b). Spin-orbit splittings of $c'$ and
$v$ band are also small compared to the $c' - v$ distance
$\Delta_{0,G}/E_{G} \ll 1^{29}$ (see Table I).

In practice, distribution function of the "impact ion-
ization ready" electrons extends on much smaller scale
(say, 25 meV) than the value of $E_{\mathrm{th}}$, therefore it is con-
venient to introduce the "above-threshold" components
of the wave vectors according to $\mathbf{q}_{i}=\mathbf{k}_{i}-\mathbf{k}_{i}^{\mathrm{th}}$, assuming
that $(E-E_{\mathrm{th}})/E_{\mathrm{th}} \ll 1$. Under such approximations the
rate of impact ionization due to electron in a state $\alpha_{0}$

<table>
<caption>Table 1: Band structure parameters (taken from 29–34) of narrow- and middle-gap semiconductors within the 14-band $\mathbf{k} \cdot \mathbf{p}$-model used in this work and the corresponding values of the dimensionless parameters $\beta$ (16), $x = \Delta_0/E_g$ and the crossover effective temperature (27).</caption>
<thead>
<tr>
<th>
</th>
<th>
$E_g$ (eV)a
</th>
<th>
$\Delta_0$ (eV)
</th>
<th>
$P$ ($\text{eV} \cdot \mathring{\text{A}}$)
</th>
<th>
$E_G$ (eV)
</th>
<th>
$Q$ ($\text{eV} \cdot \mathring{\text{A}}$)
</th>
<th>
$\beta$b
</th>
<th>
$x$b
</th>
<th>
$T^*$ (K)c
</th>
</tr>
</thead>
<tbody>
<tr>
<td>
InSb
</td>
<td>
0.24
</td>
<td>
0.81
</td>
<td>
9.64
</td>
<td>
3.2
</td>
<td>
8.13
</td>
<td>
18.78
</td>
<td>
4.5
</td>
<td>
3.4
</td>
</tr>
<tr>
<td>
InAs
</td>
<td>
0.42
</td>
<td>
0.39
</td>
<td>
9.2
</td>
<td>
4.4
</td>
<td>
8.33
</td>
<td>
2.72
</td>
<td>
1.09
</td>
<td>
13.4
</td>
</tr>
<tr>
<td>
GaSb
</td>
<td>
0.81
</td>
<td>
0.76
</td>
<td>
9.62
</td>
<td>
3.3
</td>
<td>
8.11
</td>
<td>
1.12
</td>
<td>
1.05
</td>
<td>
121
</td>
</tr>
<tr>
<td>
In0.53Ga0.47As
</td>
<td>
0.82
</td>
<td>
0.33
</td>
<td>
9.81
</td>
<td>
4.4
</td>
<td>
8.25
</td>
<td>
0.62
</td>
<td>
0.44
</td>
<td>
76
</td>
</tr>
<tr>
<td>
InP
</td>
<td>
1.42
</td>
<td>
0.11
</td>
<td>
8.85
</td>
<td>
4.7
</td>
<td>
7.22
</td>
<td>
0.07
</td>
<td>
0.08
</td>
<td>
304
</td>
</tr>
<tr>
<td>
In0.52Al0.48As
</td>
<td>
1.53
</td>
<td>
0.3
</td>
<td>
9.09
</td>
<td>
4.5
</td>
<td>
8.25
</td>
<td>
0.13
</td>
<td>
0.21
</td>
<td>
507
</td>
</tr>
<tr>
<td>
GaAs
</td>
<td>
1.52
</td>
<td>
0.34
</td>
<td>
10.49
</td>
<td>
4.5
</td>
<td>
8.17
</td>
<td>
0.21
</td>
<td>
0.24
</td>
<td>
306
</td>
</tr>
<tr>
<td>
CdTe
</td>
<td>
1.61
</td>
<td>
0.95
</td>
<td>
9.5
</td>
<td>
5.4
</td>
<td>
7.87
</td>
<td>
0.54
</td>
<td>
0.63
</td>
<td>
310
</td>
</tr>
</tbody>
</table>

a At $T = 0$ K.
b At $T = 296$ K.
c Calculated using the temperature-dependent values of bandgaps from 32–34.

reduces to

$$
\begin{aligned}
\mathcal{W} &= \frac{\pi \hbar F_2\left(\frac{\Delta_0}{E_g}\right)}{12 m_e E_g^2}\left(\frac{4 \pi e^2}{\varkappa}\right)^2 \int \frac{d^3 q_1 d^3 q_2}{(2 \pi)^6} [\widetilde{I}_{cv}(\mathbf{q}_1, \mathbf{q}_3) \\
&+ \widetilde{I}_{cv}(\mathbf{q}_2, \mathbf{q}_3)] \delta\left(q_1^2 + q_2^2 - \frac{2 m_e(E_0 - E_{\text{th}})}{\hbar^2}\right), \quad (8)
\end{aligned}
$$

where

$$
\begin{aligned}
\widetilde{I}_{cv}(\mathbf{q}_i, \mathbf{q}_3) &= \\
\sum_{\xi_i, \xi_3} I_{cv}(\mathbf{k}_i^{\text{th}} + \mathbf{q}_i, \xi_i; \mathbf{k}_3^{\text{th}} + \mathbf{q}_1 + \mathbf{q}_2 - \mathbf{q}_0, \xi_3), \quad (9)
\end{aligned}
$$

is the interband overlap integral summed over the total angular momentum projections (on the direction of $\mathbf{k}_3$) of heavy hole $\xi_3 = \pm \frac{3}{2}$ and final electron $\xi_i = \pm \frac{1}{2}$ states, while

$$
F_2(x) = \frac{(1 + x)^2 \left(1 + \frac{x}{3}\right)^3}{\left(1 + \frac{7}{9}x + \frac{x^2}{6}\right) \left(1 + \frac{2}{3}x\right)^2 \left(1 + \frac{x}{2}\right)} \quad (10)
$$

is equal to 1 for both $\Delta_0 \ll E_g$ and $\Delta_0 \gg E_g$ and the excess wave vector of the initial electron above the threshold one $q_0 = \left(\frac{\partial E_0}{\partial k_0}\right)_{\text{th}}^{-1} (E_0 - E_{\text{th}})$ is assumed to be collinear to $\mathbf{k}_0^{\text{th}}$. Expression (8) shows that the energy (and, actually, angular) dependence of the impact ionization rate $\mathcal{W}$ is governed by dispersion of the squared overlap integral $\widetilde{I}_{cv}$ near $\mathbf{q}_{1,2} = 0$. Since $\widetilde{I}_{cv}$ expresses a degree at which the states of the conduction and valence bands are overlapping, in practice it is strongly dependent of a particular considered multi-band model. A minimal basis for such model consists of the two $s$-type and six $p$-type $\Gamma$-point Bloch functions $u_n^{(0)}(\mathbf{r})$, and a minimal coupling is direct $\mathbf{k} \cdot \mathbf{p}$ coupling between the $s$-type and $p$-type states, described by the only matrix element $P^{35}$, which is also known as the Kane matrix element. This 8-band model nicely describes dispersion of the electron and light holes in the narrow-gap semiconductors, but not the heavy holes, which remain dispersionless. Near a threshold $k_i \ll k_3$ ($i = 1, 2$) and explicit expression for the squared overlap integral in this approximation is given by

$$
I_{cv}(\alpha_i, \alpha_3) = \frac{P^2||\mathbf{k}_i \times \mathbf{k}_3||^2}{2 E_g^2 k_3^2} \delta_{|\xi_i - \xi_3|,1}. \quad (11)
$$

The property of $I_{cv}$ for vanishing at the collinear $\mathbf{k}_i$ and $\mathbf{k}_3$ is more general and applicable to the threshold values of the wave vectors given by Eqs. (6),(7). Therefore $\widetilde{I}_{cv}$ can be approximated by

$$
\widetilde{I}_{cv}(\mathbf{q}_i, \mathbf{q}_3) = \frac{P^2 q_i^2}{E_g^2} = \frac{\hbar^2 q_{i \perp}^2}{2 m_e} \frac{1 + \frac{\Delta_0}{E_g}}{E_g + \frac{2}{3}\Delta_0}, \quad (12)
$$

where $\mathbf{q}_{i \perp}$ is a component of $\mathbf{q}_{1,2}$ in a plane perpendicular to wave vector of the initial electron. Straightforward integration of $\widetilde{I}_{cv}$ according to (8) leads to the following expression for $\mathcal{W}$, which is cubic in $E - E_{\text{th}}$:

$$
\mathcal{W}_3(E) = B(E - E_{\text{th}})^3, \quad (13)
$$

$$
B = \frac{\omega_B^*}{18 E_g^3} \frac{E_g + \Delta_0}{E_g + \frac{2}{3}\Delta_0} F_2\left(\frac{\Delta_0}{E_g}\right), \quad (14)
$$

where $\omega_B^* = \frac{m_e e^4}{2 \hbar^3 \varkappa^2}$ is the Bohr frequency for the conduction band electrons. In the limiting case of the infinite spin-orbit splitting $\Delta_0$ (corresponding to the 6-band $\mathbf{k} \cdot \mathbf{p}$ model) this answer reduces to the one given implicitly by (2) of21, while taking into account a finite value of $\Delta_0$ gives an additional factor to the latter, which goes to $2/3$ when $\Delta_0 \to 0$.

Thus, the minimal band model misses a quadratic contribution associated with the value of the interband overlap integral at threshold $\widetilde{I}_{cv}(0,0)$, which arises in more sophisticated models taking into account coupling to the remote bands and lowering the spherical symmetry to the cubic one ($\mathcal{O}_h/\mathcal{T}_d$), in particular, 14-band $\mathbf{k} \cdot \mathbf{p}$ model (so

![](./images/867759472146120937_2.jpg)
![](./images/867759472146120937_3.jpg)
![](./images/867759472146120937_4.jpg)
![](./images/867759472146120937_5.jpg)
![](./images/867759472146120937_6.jpg)
![](./images/867759472146120937_7.jpg)
![](./images/867759472146120937_8.jpg)
![](./images/867759472146120937_9.jpg)

FIG. 2. Angular plots of $\mathcal{K}(\mathbf{u}, \beta)$ representing the anisotropy of the quadratic term (23) in the impact ionization rate for the cases of a)-d) strong $\beta \gg 1$ (20) and e)-h) weak $\beta \ll 1$ (21) spin-orbit coupling; a) and e) all wave vector directions of the initial electron, $u_{x,y,z}$ denote the projections of $\mathbf{u}$ onto the [100] set of equivalent crystallographic directions; b) and f) cross sections by (001) plane; c) and g) cross sections by (110) plane; d) and h) cross sections by (111) plane.

called extended Kane model$^{29}$). In this model six additional Bloch states of $\Gamma_{7c}$ and $\Gamma_{8c}$ symmetry lying a few electron-volts above $E_c$ (the second conduction band, $c'$ in Fig. 1b) are coupled to the states of the valence band via the only matrix element $Q$, which is of the same order of magnitude as $P$ (see Table I). Inversion asymmetry induces coupling between the bands $c$ and $c'$ described by the matrix elements $P'$ and $\Delta'$, which are about an order of magnitude smaller than $P$, $Q$ and $\Delta_0$, correspondingly$^{36}$.

In order to treat coupling between $c'$ and $v$ bands perturbatively, it is convenient to divide the full $\mathbf{k}\cdot\mathbf{p}$ hamiltonian into the main part $\mathcal{H}_0(\mathbf{k})$, representing hamiltonian of the minimal 8-band model and the energies of the $c'$ band states at $k=0$, and a perturbation $\mathcal{V}(\mathbf{k})$, describing the above-mentioned $c'-v$ coupling. The six eigenstates of $\mathcal{H}_0$ at $\mathbf{k} = \mathbf{k}_3^{\text{th}} \approx -\mathbf{k}_g$ corresponding to $c'$ band lie far away from the rest eight, viz. the electron states with $E_e = E_v + 2E_g$, the heavy hole states with $E_{hh}^{(0)} = E_v$, and the light and spin-orbit split hole states with

$$
E_{lh/so} = E_v - \frac{E_g}{2} \left( 1 + x \pm \sqrt{\frac{x^3 + x^2 - x + 3}{x + 3}} \right) , \ (15)
$$

where $x = \Delta_0/E_g$. Also, expression (15) guarantees that minimal distance in energy between the heavy holes and the other hole branches is bigger than $\min(E_g,\Delta_0)/2$ for $x \geq 1$, which is the case of narrow-gap semiconductors (see Table I). Consequently, the unperturbed heavy hole state is non-degenerate and the corresponding perturbation theory can be applied. The particular method we follow to calculate the Bloch functions is described in Appendix A. However, the proper parameter which should not be small for the perturbative treatment in the form given in Appendix A to be correct is

$$
\beta = \frac{P^2 \Delta_0 E_G}{6Q^2 E_g^2} \gg 1. \tag{16}
$$

Indeed, the formulae (A1)-(A3) show that the $\mathbf{k}\cdot\mathbf{p}$ perturbation $\mathcal{V}(-\mathbf{k}_g)$ is applied to a "bare" heavy hole state $|\mathcal{F}_{hh}^{(0)}\rangle$ twice, producing a factor $\sim (Qk_g)^2 \sim E_g^2$, which is compensated by the two Green functions, i.e. the energy denominators. And while the first denominator is a distance between the bands $c'$ and $v$ given by $E_G$, the second one counts a distance between the heavy holes and either the electrons, light holes or the spin-orbit split holes. When $\Delta_0$ is much smaller than $E_g$ the spin-orbit holes behave more like the heavy holes, and the energy separation between them at finite wave vector $\mathbf{k} = \mathbf{k}_3^{\text{th}} \approx -\mathbf{k}_g$ given by $E_v - E_{so}$ after Eq. (15) tends to its value at $k=0$, $\Delta_0$. Thus, it could be deduced that the described perturbative approach does not work at $\beta \ll 1$ and it leads to divergent result at $\Delta_0 \to 0$. However, while the first is true, the second is not because the unper-

![](./images/867759472146120937_10.jpg)

FIG. 3. Average value of the cubic invariant approximated by analytical expressions (B1)-(B8) for arbitrary parameter $\beta$ (16).

turbed spin-orbit split hole states do not overlap with the $s$-type states in this limit, transforming into the sec- ond branch of the heavy holes. Therefore, for the case of middle-gap semiconductors, when $x=\Delta_{0}/E_{g}\ll 1$ (or alternatively $\beta\ll 1$) becomes another small parameter (see Table I) in addition to $m_{e}/m_{hh}\ll 1$, our previous method should be rearranged to take into account the degeneracy of heavy holes, viz. $|\mathcal{F}_{hh}^{(0)}\rangle$ in Appendix A now stands for the proper zero-order wave function, cor- responding to the topmost branch of heavy hole states split by $\mathbf{k}\cdot\mathbf{p}$ interaction between $c$ and $v$ bands.

After squaring and summing over the $\xi$-variables, we obtain explicit expression for the main ingredient of the quadratic contribution to the impact ionization rate,

$$
\tilde{I}_{cv}(0,0)=\frac{8E_{g}^{2}Q^{4}}{E_{G}^{2}P^{4}}\mathcal{K}(\mathbf{u},\beta)\frac{1+x/2}{1+x/3}\tag{17}
$$

where $\mathcal{K}(\mathbf{u},\beta)$ is a cubic invariant, which can be ex- pressed in terms of parameter $\beta$ and the polynomial in- variants $\mathcal{I}(\mathbf{u})$ and $\mathcal{J}(\mathbf{u})$ of the fourth and sixth orders

$$
\mathcal{I}(\mathbf{u})=u_{x}^{2}u_{y}^{2}+u_{x}^{2}u_{z}^{2}+u_{y}^{2}u_{z}^{2},\tag{18}
$$

$$
\mathcal{J}(\mathbf{u})=u_{x}^{2}u_{y}^{2}u_{z}^{2}.\tag{19}
$$

Here $\mathbf{u}=\mathbf{k}_{0}/k_{0}$ characterizes direction of the initial elec- tron motion with respect to crystallographic axes. For big $(\beta\rightarrow\infty)$ and small $(\beta\rightarrow 0)$ values of $\beta$, anisotropy of the quadratic contribution is described by

$$
\mathcal{K}_{\infty}(\mathbf{u})=\mathcal{I}(1-3\mathcal{I}),\tag{20}
$$

and

$$
\begin{aligned}
\mathcal{K}_{0}(\mathbf{u})=\mathcal{K}_{\infty}(\mathbf{u})-\mathcal{I}^{2}&\\
+3\mathcal{J}+\frac{\mathcal{I}^{2}(1-4\mathcal{I})-\mathcal{J}(2-9\mathcal{I})}{\sqrt{\mathcal{I}^{2}-3\mathcal{J}}},&
\end{aligned}\tag{21}
$$

respectively. Approximate form of $\mathcal{K}(\mathbf{u},\beta)$ for arbitrary $\beta$ is given in Appendix B. Earlier, a similar expression for the case $\beta\gg 1$ was given in $^{19}$ in terms of the Luttinger parameters $\gamma_{2}$ and $\gamma_{3}$ for the limiting case of $\Delta_{0}\rightarrow\infty$ with application to the problem of Auger recombination and in $^{37}$. Substituting (17) into (8) for $\tilde{I}_{cv}(\mathbf{q}_{i},\mathbf{q}_{3})$, we obtain explicit expression for the quadratic term in the impact ionization rate, namely

$$
\mathcal{W}_{2}(E,\mathbf{u})=A(E-E_{\mathrm{th}})^{2},\tag{22}
$$

$$
A=\frac{4}{3}\frac{\omega_{B}^{*}Q^{4}}{E_{G}^{2}P^{4}}\mathcal{K}(\mathbf{u},\beta)\frac{E_{g}+\frac{1}{2}\Delta_{0}}{E_{g}+\frac{1}{3}\Delta_{0}}F_{2}\left(\frac{\Delta_{0}}{E_{g}}\right).\tag{23}
$$

![](./images/867759472146120937_11.jpg)

FIG. 4. Competition between averaged cubic and quadratic contributions to the impact ionization rate of semiconduc- tors listed in Table I at various effective temperatures of hot electron distribution above the impact ionization threshold. Intersections of solid lines with dashed one correspond to crossover effective temperatures.

With $E_{G}^{2}$ in the denominator, the quadratic contribu- tion given by (23) turns out to be of the second order in small parameter $\mu=m_{e}/m_{hh}$, leading to competition with the cubic contribution given by (14) in narrow- and middle-gap semiconductors for the electrons with $E-E_{\mathrm{th}}$ of the order of a few tens of meVs, as shown below. As illustrated in Fig. $2$, $\mathcal{W}_{2}$ strongly depends on the ori- entation of the initial electron wave vector with respect to crystallographic directions. In both cases of strong $\beta\gg 1$ (see Figs. 2a-d) and weak $\beta\ll 1$ (see Figs. 2e- h) spin-orbit coupling, quadratic term vanishes along the high-symmetry directions [100] and [111]. However, the anisotropy of $\mathcal{W}_{2}$ described by $\mathcal{K}_{\infty}(\mathbf{u})$ and $\mathcal{K}_{0}(\mathbf{u})$ is dif- ferent: in the latter case the quadratic term addition- ally vanishes in the [110] direction. In the (111) crys- tallographic plane quadratic term becomes isotropic for the case of strong spin-orbit coupling (see Fig. 2d), since $\mathcal{I}(\mathbf{u}_{(111)})=1/4$, while $\mathcal{K}_{0}(\mathbf{u}_{(111)})$ reproduces the nontriv- ial angular dependence of $\mathcal{J}(\mathbf{u})$ (see Fig. 2h). Interest- ingly, the spin-orbit interaction and inversion asymmetry

![](./images/867759472146120937_12.jpg)

FIG. 5. Dependence of the averaged impact ionization rates at $T=296K$ on the bandgap. Solid red line corresponds to the total rate $\overline{\mathcal{W}}_{\text{tot}}=\overline{\mathcal{W}}_{2}+\overline{\mathcal{W}}_{3}$ deduced from analytical expressions (14) and (23); open markers denote the behavior of the numerically calculated total rate (green diamonds) and partial contributions to it: quadratic (blue circles) and cubic (orange triangles) ones.

lead to some specific contribution to $\mathcal{W}_{2}$ in the semiconductors belonging to $\mathcal{T}_{d}$ symmetry group, non-vanishing along the primary crystallographic directions. However, this contribution is small in parameter $\Delta_{c'v}/\Delta_{0}$, where $\Delta_{c'v}$ is a magnitude of the non-diagonal spin-orbit $c'-v$ coupling $^{29}$, therefore it is very small from a practical point of view.

## III. DISCUSSION

To compare the relative importance of the two contributions to total impact ionization rate
$$
\mathcal{W}_{\text{tot}}(E,\mathbf{u})=A(\mathbf{u})(E-E_{\text{th}})^{2}+B(E-E_{\text{th}})^{3},\quad(24)
$$
we consider a non-degenerate ensemble of electrons driven from equilibrium by electric field and calculate the carrier generation rates $\mathcal{R}_{2}$ and $\mathcal{R}_{3}$ (corresponding to the scattering rates given by Eqs. (23) and (14), respectively), averaged over the field direction. Since the problem of such averaging is equivalent to averaging over directions of the initiating electrons $\mathbf{u}$ under the assumption of isotropic distribution, the total rates can be written as
$$
\mathcal{R}_{i}=\overline{\mathcal{W}}_{i}\mathcal{N}_{0},\quad(25)
$$
$$
\overline{\mathcal{W}}_{i}=\int_{E_{\text{th}}}^{+\infty}\frac{dE}{T}\frac{d\mathbf{u}}{4\pi}\mathcal{W}(E,\mathbf{u})\exp\left(-\frac{E-E_{\text{th}}}{T}\right),\quad(26)
$$
where $\mathcal{N}_{0}=\mathcal{D}(E_{\text{th}})\overline{\delta f}(E_{\text{th}})T$ is the nonequilibrium concentration of hot electrons above the impact ionization threshold, $\overline{\mathcal{W}}_{i}$ is the impact ionization rate, averaged over momentum direction of initial electrons and their distribution, $\mathcal{D}(E)$ is the density of states in the conduction band, $\delta f(E)$ is the non-equilibrium component of the distribution function, $T$ is an effective temperature, determined by either the external temperature, the energy acquired by a mean free path $eEl$, or its combination with the optical phonon energy $\hbar\omega_{o}^{16}$. Performing the elementary integration of $(E-E_{\text{th}})^{n}$ with the exponential function, we obtain the crossover temperature at which $\overline{\mathcal{W}}_{2}=\overline{\mathcal{W}}_{3}$ (or $\mathcal{R}_{2}=\mathcal{R}_{3}$):
$$
T^{*}=\frac{\overline{A}}{3B}=8\frac{Q^{4}}{P^{4}}\frac{E_{g}^{3}}{E_{G}^{2}}\overline{\mathcal{K}}(\beta)F_{1}\left(\frac{\Delta_{0}}{E_{g}}\right).\quad(27)
$$

Here the averaged (over the directions of $\mathbf{u}$) value of the cubic invariant at arbitrary $\beta$ is between its limits at infinite and zero spin-orbit coupling $\overline{\mathcal{K}}_{\infty}<\overline{\mathcal{K}}(\beta)<\overline{\mathcal{K}}_{0}$, with $\overline{\mathcal{K}}_{\infty}=0.057$ and $\overline{\mathcal{K}}_{0}=0.069$. In this work we use the $\overline{\mathcal{K}}(\beta)$ dependence (see Fig. 3) deduced from the analytical approximation to $\mathcal{K}(\mathbf{u},\beta)$ by Eqs. (B1)-(B8). The definition of $F_{1}(x)$ is given after (7).

Temperature dependence of the bandgap $E_{g}(T)$ leads to non-linear scaling of $\overline{\mathcal{W}}_{3}/\overline{\mathcal{W}}_{2}$ ratio with $T$, and Eq. (27) becomes transcendental. Using band structure parameters listed in Table I and empirical temperature dependencies of the bandgaps (namely, Manoogian-Wooley equation for CdTe$^{33}$ and Varshni equation for other compounds $^{32,34}$), we calculate the $\overline{\mathcal{W}}_{3}(T)/\overline{\mathcal{W}}_{2}(T)$ dependencies for narrow- and middle-gap semiconductors (see Fig. 4) and estimate the crossover temperatures, see Table I. At low effective temperature, the impact ionization rate of any semiconductor is determined by quadratic term, and thus is strongly anisotropic. With increasing $T$, the isotropic cubic term rapidly grows and at room temperature it completely dominates over $\mathcal{W}_{2}(E,\mathbf{u})$ in narrow-gap semiconductors like InSb, InAs, GaSb and $\text{In}_{0.53}\text{Ga}_{0.47}\text{As}$, while in middle-gap InP, GaAs and CdTe both terms are comparable. In $\text{In}_{0.42}\text{Al}_{0.58}\text{As}$ the crossover takes place at much higher temperature about 500 K.

## IV. CONCLUSION

In conclusion, we would like to shortly discuss the accuracy of the obtained analytical expressions. Since the main complexity and therefore potential inaccuracy is concentrated in the proper expression for overlap integrals, determined by the specific form of multiband wave functions, we performed numerical calculation of the averaged impact ionization rate based on the numerical diagonalization of the 14-band $\mathbf{kp}$-model. In order to reduce the numerical complexity, in (8) we have ignored the inessential dependence of the numerically calculated overlap integrals on $\mathbf{q}_{3}$ and preformed the analytical integration of the total rate over magnitudes $q_{1}$ and $q_{2}$ and solid angles $\Omega_{0}$. As a result, 9-dimensional integration

over $\mathbf{q}_{0,1,2}$ was reduced to 5-dimensional integration over magnitude $q_0$ and solid angles $\Omega_{1,2}$. Finally, the infinite integration interval over $q_0$ was rearranged into $[0,1]$ by means of Lambert function substitution and the resulting integral was calculated by Monte-Carlo method. The obtained results of the averaged impact ionization rate dependence on $E_g$ at the effective temperature $T=296K$ are presented on the Fig. 5. Simple analytical expression $\overline{W}_{\text{tot}}=2\overline{A}T^2+6BT^3$ for the impact ionization rate deduced from Eqs. (24) and (26) is in good agreement with numerical results in the wide range of $E_g$ up to 1.5 eV. Namely, the corresponding mean percentage error is 11% and the maximal discrepancy with respect to numerical calculations is 15%. The values of analytical and numerical "crossover bandgaps" [when $\overline{W}_2(E_g)=\overline{W}_3(E_g)$] are also close: 1.15 eV vs 0.95 eV, respectively.

Discrepancy between analytical and numerical results originates from Eq. (23), which underestimates the quadratic term, especially for the case of wide-gap semiconductors, when the primary small parameter of our theory $\mu=m_e/m_{hh}$ approaches unity. However, 5% agreement with numerical results within the full range of bandgaps considered in this work can be achieved using analytical expressions, which include higher-order corrections to (14) and (23) by $E_g/E_G$ (up to second order). We also expect, that in the case of strongly anisotropic distribution of hot electrons in high electric fields$^{38}$, the angular dependence of carrier generation rate will replicate the anisotropy of the total impact ionization rate (24). Therefore, the obtained generalization of the conventional Keldysh formula for the impact ionization rate in direct-gap semiconductors given by (24) is suitable for incorporation into modelling software.

## CONFLICT OF INTEREST
The authors have no conflicts to disclose.

## DATA AVAILABILITY
The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Appendix A: Perturbation method description
To describe the perturbative calculation of the multiband wave function of the heavy hole state, it is convenient to introduce the "non-interacting" Green function $\mathcal{G}_0(\mathcal{E})=(\mathcal{E}-\mathcal{H}_0)^{-1}$. The first-order correction to the heavy hole eigenstate $|\mathcal{F}_{hh}^{(0)}\rangle$ is then expressed in the form
$$
\left|\mathcal{F}_{hh}^{(1)}\right\rangle=\lim _{\mathcal{E} \rightarrow \tilde{E}_{v}} \mathcal{G}_{0}\left(\mathcal{E},-\mathbf{k}_{g}\right) \mathcal{V}\left(-\mathbf{k}_{g}\right)\left|\mathcal{F}_{hh}^{(0)}\right\rangle. \qquad \text{(A1)}
$$

Due to definition of $\mathcal{V}$ and $\mathcal{G}_0$ in Section II, $|\mathcal{F}_{hh}^{(1)}\rangle$ belongs to the $c'$ subspace and is orthogonal to the eight basis states of $c$ and $v$ bands, therefore it does not contribute to $\tilde{I}_{cv}(0,0)$ as well as to the first-order correction to energy, $E_{hh}^{(1)}=0$. The second-order correction to the energy of the heavy hole state $E_{hh}$ is
$$
E_{hh}^{(2)}=\lim _{\mathcal{E} \rightarrow \tilde{E}_{v}}\left\langle\mathcal{F}_{hh}^{(0)}\left|\mathcal{V}\left(-\mathbf{k}_{g}\right)\right| \mathcal{F}_{hh}^{(1)}(\mathcal{E})\right\rangle, \qquad \text{(A2)}
$$
and the corresponding multiband wave function $|\mathcal{F}_{hh}\rangle$ can be written as
$$
\begin{aligned}
\left|\mathcal{F}_{hh}^{(2)}\right\rangle= & \lim _{\mathcal{E} \rightarrow \tilde{E}_{v}} \mathcal{G}_{0}\left(\mathcal{E},-\mathbf{k}_{g}\right) \\
& \times\left[\mathcal{V}\left(-\mathbf{k}_{g}\right)\left|\mathcal{F}_{hh}^{(1)}(\mathcal{E})\right\rangle-E_{2}(\mathcal{E})\left|\mathcal{F}_{hh}^{(0)}\right\rangle\right]. \quad \text{(A3)}
\end{aligned}
$$

Equation (A2) specifies the heavy hole energy and relation between the heavy hole mass and the 14-band model parameters $Q$ and $E_G$, while Eq. (A3) gives principal approximation for the $c-v$ overlap integral,
$$
\begin{aligned}
\left\langle\mathcal{F}_{e}\left(\mathbf{k}_{i}^{\mathrm{th}}, \xi_{i}\right)\left|\mathcal{F}_{h h}\left(\mathbf{k}_{3}^{\mathrm{th}}, \xi_{3}\right)\right\rangle\right. & \approx \\
& \left\langle\mathcal{F}_{e}^{(0)}\left(\mu \mathbf{k}_{g}, \xi_{i}\right)\left|\mathcal{F}_{h h}^{(2)}\left(-\mathbf{k}_{g}, \xi_{3}\right)\right\rangle,\right. \quad \text{(A4)}
\end{aligned}
$$
where $|\mathcal{F}_{e}^{(0)}\rangle$ is a pure $s$-type state, corresponding to a single-band approximation for the final low-energy states having much smaller wave vector than that of the initial states (0 and 3). Therefore corrections to $|\mathcal{F}_{e}^{(0)}\rangle$ do not enter Eq. (A4) in the leading order in $\mu=m_e/m_{hh}$.

## Appendix B: Approximate angular dependence of the quadratic term at arbitrary $\beta$
Even thought an exact angular dependence of the quadratic term (23) at arbitrary $\beta$ can be calculated only numerically, analytic approximation to it can be constructed via Pade-Borel method. For the cases of strong and weak spin-orbit coupling we have calculated series expansion of Eq. (23) by $1/\beta \ll 1$ and $\beta \ll 1$ up to second and third orders, respectively. The resulting approximating function for $\mathcal{K}(\mathbf{u},\beta)$ is
$$
\mathcal{K}(\mathbf{u}, \beta)=\mathcal{K}_{1}(\mathbf{u}, \beta)+\mathcal{K}_{2}(\mathbf{u}, \beta) \qquad \text{(B1)}
$$

$$
\mathcal{K}_{1}(\mathbf{u}, \beta)=\frac{K_{1}(\mathbf{u})+\beta K_{2}(\mathbf{u})+\beta^{2} K_{3}(\mathbf{u})}{S(\mathbf{u}, \beta)(\beta+S(\mathbf{u}, \beta))} \qquad \text{(B2)}
$$

$$
\mathcal{K}_{2}(\mathbf{u}, \beta)=\frac{K_{2}(\mathbf{u})+\beta \tilde{K}_{2}(\mathbf{u})}{\beta+S(\mathbf{u}, \beta)} \qquad \text{(B3)}
$$

$$
S(\mathbf{u}, \beta)=\sqrt{4 \mathcal{I}^{2}-12 \mathcal{J}+\beta^{2}} \qquad \text{(B4)}
$$

$$
K_{1}(\mathbf{u})=-4\left(\mathcal{I}^{2}-3 \mathcal{J}\right)\left(4 \mathcal{I}^{2}-\mathcal{I}-3 \mathcal{J}\right) \qquad \text{(B5)}
$$

$$
K_{2}(\mathbf{u})=-8 \mathcal{I}^{3}+2 \mathcal{I}^{2}+18 \mathcal{I} \mathcal{J}-4 \mathcal{J} \qquad \text{(B6)}
$$

$$
K_{3}(\mathbf{u})=-2 \mathcal{I}^{2}+\mathcal{I}-3 \mathcal{J} \qquad \text{(B7)}
$$

$$
\tilde{K}_{2}(\mathbf{u})=3 \mathcal{J}+\mathcal{I}-4 \mathcal{I}^{2}. \qquad \text{(B8)}
$$

$^1$S. M. Sze, Y. Li, and K. K. Ng, *Physics of Semiconductor De-vices*, 4th ed. (Wiley, 2021).

$^2$K. Gopalakrishnan, P. B. Griffin, and J. D. Plummer, “Impact ionization MOS (I-MOS)-Part I: device and circuit simulations,” *IEEE Transactions on Electron Devices* **52**, 69–76 (2005).

$^3$S. Trumm, M. Betz, F. Sotier, A. Leitenstorfer, A. Schwanhäußer, M. Eckardt, O. Schmidt, S. Malzer, G. H. Döhler, M. Hanson, D. Driscoll, and A. C. Gossard, “Ultrafast spectroscopy of impact ionization and avalanche multiplication in GaAs,” *Applied Physics Letters* **88**, 132113 (2006).

$^4$S. Chen and G. Wang, “High-field properties of carrier transport in bulk wurtzite GaN: A Monte Carlo perspective,” *Journal of Applied Physics* **103**, 023703 (2008).

$^5$F. Bertazzi, M. Moresco, and E. Bellotti, “Theory of high field carrier transport and impact ionization in wurtzite GaN. Part I: A full band Monte Carlo model,” *Journal of Applied Physics* **106**, 063718 (2009).

$^6$C. K. Chia, “Numerical simulation of impact ionization in Ge/Al$_x$Ga$_{1-x}$As avalanche photodiode,” *Applied Physics Letters* **97**, 073501 (2010).

$^7$E. Bellotti and F. Bertazzi, “A numerical study of carrier impact ionization in Al$_x$Ga$_{1-x}$N,” *Journal of Applied Physics* **111**, 103711 (2012).

$^8$S. Shishehchi, F. Bertazzi, and E. Bellotti, “A numerical study of low- and high-field carrier transport properties in In$_{0.18}$Al$_{0.82}$N lattice-matched to GaN,” *Journal of Applied Physics* **113**, 203709 (2013).

$^9$S. Ašmontas, R. Raguotis, and S. Bumelienė, “Monte Carlo calculations of the electron impact ionization in n-type InSb crystal,” *Semiconductor Science and Technology* **28**, 025019 (2013).

$^{10}$K. Kodama, H. Tokuda, and M. Kuzuhara, “A model for calculating impact ionization transition rate in wurtzite GaN for use in breakdown voltage simulation,” *Journal of Applied Physics* **114**, 044509 (2013).

$^{11}$K. Ghosh and U. Singisetti, “Impact ionization in $\beta$-Ga$_2$O$_3$,” *Journal of Applied Physics* **124**, 085707 (2018).

$^{12}$S. Ašmontas, S. Bumelienė, J. Gradauskas, R. Raguotis, and A. Sužiedėlis, “Intense terahertz pulse-induced impact ionization and electron dynamics in InAs,” *Semiconductor Science and Technology* **34**, 075016 (2019).

$^{13}$S. Ašmontas, S. Bumelienė, J. Gradauskas, R. Raguotis, and A. Sužiedėlis, “Impact ionization and intervalley electron scattering in InSb and InAs induced by a single terahertz pulse,” *Scientific Reports* **10**, 10580 (2020).

$^{14}$M. V. Fischetti and S. E. Laux, “Monte carlo analysis of electron transport in small semiconductor devices including band-structure and space-charge effects,” *Phys. Rev. B* **38**, 9721–9745 (1988).

$^{15}$L. V. Keldysh, “Kinetic Theory of Impact Ionization in Semiconductors,” Zh. Exp. Teor. Fiz. **37**, 713 (1960), [Sov. Phys. JETP **10**, 509 (1960)].

$^{16}$B. K. Ridley, *Quantum Processes in Semiconductors*, 5th ed. (Oxford University Press, 2013).

$^{17}$M. G. Burt, S. Brand, C. Smith, and R. A. Abram, “Overlap integrals for Auger recombination in direct-bandgap semiconductors: calculations for conduction and heavy-hole bands in GaAs and InP,” *Journal of Physics C: Solid State Physics* **17**, 6385–6401 (1984).

$^{18}$K. F. Brennan, *The Physics of Semiconductors: With Applications to Optoelectronic Devices* (Cambridge University Press,1999).

$^{19}$B. L. Gelmont, “Three-band Kane model and Auger recombination,” Zh. Exp. Teor. Fiz. **75**, 536 (1978), [Sov. Phys. JETP **48**, 268 (1978)].

$^{20}$A. R. Beattie, R. A. Abram, and P. Scharoch, “Realistic evaluation of impact ionisation and Auger recombination rates for the ccch transition in InSb and InGaAsP,” *Semiconductor Science and Technology* **5**, 738–744 (1990).

$^{21}$B. Gelmont, K.-S. Kim, and M. Shur, “Theory of impact ionization and Auger recombination in Hg$_{1-x}$Cd$_x$Te,” *Phys. Rev. Lett.* **69**, 1280–1282 (1992).

$^{22}$K. Y. Choo and D. S. Ong, “Analytical band Monte Carlo simulation of electron impact ionization in In$_{0.53}$Ga$_{0.47}$As,” *Journal of Applied Physics* **96**, 5649–5653 (2004).

$^{23}$C. K. Chia and G. K. Dalapati, “Monte Carlo Simulation of Hot Carrier Transport in Heterogeneous Ge/Al$_x$Ga$_{1-x}$As ($0 \le x \le 0.8$) Multilayer Avalanche Photodiodes,” *IEEE Transactions on Electron Devices* **60**, 3435–3441 (2013).

$^{24}$D. Dolgos, A. Schenk, and B. Witzigmann, “Impact ionization scattering model based on the random-k approximation for GaAs, InP, InAlAs, and InGaAs,” *Journal of Applied Physics* **111**, 073714 (2012).

$^{25}$I. C. Sandall, J. S. Ng, S. Xie, P. J. Ker, and C. H. Tan, “Temperature dependence of impact ionization in InAs,” *Opt. Express* **21**, 8630–8637 (2013).

$^{26}$P. Scharoch and R. A. Abram, “A method of determining the overlap integrals used in calculations of Auger transition rates in semiconductors,” *Semiconductor Science and Technology* **3**, 973–978 (1988).

$^{27}$S. Brand and R. A. Abram, “Calculations of overlap integrals for Auger processes involving direct band gap semiconductors,” *Journal of Physics C: Solid State Physics* **17**, L201–L206 (1984).

$^{28}$A. S. Volkov, A. A. Gutkin, and S. E. Kumekov, Sov. Phys. Semicond. **4**, 1593 (1976).

$^{29}$R. Winkler, *Spin-Orbit Coupling Effects in Two-Dimensional Electron and H* (Springer-Verlag, 2003).

$^{30}$M. Levinstein, S. Rumyantsev, and M. Shur, *Handbook Series on Semiconductor Parameters* (World Scientific Publishing, 1996).

$^{31}$M. Cardona, N. E. Christensen, and G. Fasol, “Relativistic band structure and spin-orbit splitting of zinc-blende-type semiconductors,” *Phys. Rev. B* **38**, 1806–1827 (1988).

$^{32}$“New Semiconductor Materials Database. Characteristics and Properties. Ioff

$^{33}$G. Fonthal, L. Tirado-Mejía, J. Marín-Hurtado, H. Ariza-Calderón, and J. Mendoza-Alvarez, “Temperature dependence of the band gap energy of crystalline CdTe,” *Journal of Physics and Chemistry of Solids* **61**, 579–583 (2000).

$^{34}$I. Vurgaftman, J. R. Meyer, and L. R. Ram-Mohan, “Band parameters for III–V compound semiconductors and their alloys,” *Journal of Applied Physics* **89**, 5815–5875 (2001).

$^{35}$E. O. Kane, “Band structure of indium antimonide,” *Journal of Physics and Chemistry of Solids* **1**, 249–261 (1957).

$^{36}$S. Richard, F. Aniel, and G. Fishman, “Energy-band structure of Ge, Si, and GaAs: A thirty-band $\mathbf{k} \cdot \mathbf{p}$ method,” *Phys. Rev. B* **70**, 235204 (2004).

$^{37}$A. N. Afanasiev, A. A. Greshnov, and G. G. Zegrya, “Impact ionization rate in direct gap semiconductors,” *JETP Letters* **105**, 586–590 (2017).

$^{38}$A. P. Dmitriev, M. P. Mikhailova, and I. N. Yassievich, “High Energy Distribution Function in an Electric Field and Electron Impact Ionization in A$^{\text{III}}$B$^{\text{V}}$ Semiconductors,” *physica status solidi (b)* **113**, 125–135 (1982).