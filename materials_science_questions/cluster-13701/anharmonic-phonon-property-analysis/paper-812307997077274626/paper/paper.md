PHYSICAL REVIEW E 70, 066148 (2004)

# Local versus global thermal states: Correlations and the existence of local temperatures

Michael Hartmann, $^{1,2,*}$ Günter Mahler, $^{2}$ and Ortwin Hess $^{3}$
$^{1}$ Institute of Technical Physics, DLR Stuttgart, 70569 Stuttgart, Germany
$^{2}$ Institute of Theoretical Physics I, University of Stuttgart, 70550 Stuttgart, Germany
$^{3}$ Advanced Technology Institute, University of Surrey, Guildford GU2 7XH, United Kingdom

(Received 29 April 2004; revised manuscript received 12 August 2004; published 30 December 2004)

We consider a quantum system consisting of a regular chain of elementary subsystems with nearest neighbor interactions and assume that the total system is in a canonical state with temperature $T$. We analyze under what condition the state factors into a product of canonical density matrices with respect to groups of $n$ subsystems each, and when these groups have the same temperature $T$. While in classical mechanics the validity of this procedure only depends on the size of the groups $n$, in quantum mechanics the minimum group size $n_{\text{min}}$ also depends on the temperature $T$! As examples, we apply our analysis to a harmonic chain and different types of Ising spin chains. We discuss various features that show up due to the characteristics of the models considered. For the harmonic chain, which successfully describes thermal properties of insulating solids, our approach gives a quantitative estimate of the minimal length scale on which temperature can exist: This length scale is found to be constant for temperatures above the Debye temperature and proportional to $T^{-3}$ below.

DOI: 10.1103/PhysRevE.70.066148
PACS number(s): 05.30.-d, 05.70.Ce, 65.80.+n, 65.40.-b

## I. INTRODUCTION

Thermodynamics is among the most successfully and ex- tensively applied theoretical concepts in physics. Notwith- standing, the various limits of its applicability are not fully understood [1,2].

Of particular interest is its microscopic limit. Down to which length scales can its standard concepts meaningfully be defined and employed?

Besides its general importance, this question has become increasingly relevant recently since amazing progress in the synthesis and processing of materials with structures on na- nometer length scales has created a demand for better under- standing of thermal properties of nanoscale devices, indi- vidual nanostructures, and nanostructured materials [3-6]. Experimental techniques have improved to such an extent that the measurement of thermodynamic quantities like tem- perature with a spatial resolution on the nanometer scale seems within reach [7-9].

To provide a basis for the interpretation of present day and future experiments in nanoscale physics and technology and to obtain a better understanding of the limits of thermo- dynamics, it is thus indispensable to clarify the applicability of thermodynamical concepts on small length scales starting from the most fundamental theory at hand, i.e., quantum me- chanics. In this context, one question appears to be particu- larly important and interesting: Can temperature be meaning- fully defined on nanometer length scales?

The existence of thermodynamical quantities, i.e., the ex- istence of the thermodynamic limit strongly depends on the correlations between the considered parts of a system.

With increasing size, the volume of a region in space grows faster than its surface. Thus effective interactions be- tween two regions, provided they are short ranged, become less relevant as the sizes of the regions increase. This scaling behavior is used to show that correlations between a region and its environment become negligible in the limit of infinite region size and that therefore the thermodynamic limit exists [10-12].

To explore the minimal region size needed for the appli- cation of thermodynamical concepts, situations far away from the thermodynamic limit should be analyzed. On the other hand, effective correlations between the considered parts need to be small enough [13,14].

The scaling of interactions between parts of a system compared to the energy contained in the parts themselves thus sets a minimal length scale on which correlations are still small enough to permit the definition of local tempera- tures. It is the aim of this paper to study this connection quantitatively.

Some attempts to generalize thermodynamics such that it applies to small systems have been made [15-17]. These approaches consider ensembles of independent, i.e., nonin- teracting, small systems. By introducing an additional ther- modynamical potential they take into account the surface effects of the small systems. However, since the interactions between the small systems are neglected, these concepts can- not capture the physics of the correlations. This shortcoming is also obvious from the results: The correction terms they predict do not depend on temperature, whereas it is well known that correlations become more important the lower the temperature.

Recently the impact of quantum correlations, i.e., en- tanglement on macroscopic properties of solids and phase transitions has drawn considerable attention [18-20]. Since our analysis of criteria for local temperatures is based on a study of correlations, our theoretical approach is a promising tool to provide further insight into the role of correlations in solid state physics.

We adopt here the convention that a local temperature exists if the considered part of the system is in a canonical state, where the distribution is an exponentially decaying

*Electronic address: michael.hartmann@dlr.de

1539-3755/2004/70(6)/066148(12)/$22.50
066148-1
©2004 The American Physical Society

function of energy characterized by one single parameter.
This implies that there is a one-to-one mapping between tem-
perature and the expectation values of observables, by which
temperature is usually measured. Temperature measurements
based on different observables will thus yield the same re-
sult, contrary to distributions with several parameters. In
large systems composed of very many subsystems, the den-
sity of states is a strongly growing function of energy [21]. If
the distribution were not exponentially decaying, the product
of the density of states times the distribution would not have
a pronounced peak and thus physical quantities like energy
would not have "sharp" values.

There have been attempts to describe systems which are
not in an equilibrium state but in some sense close to it with
a generalized form of thermodynamics, that has additional
system parameters. Such a situation appears for example in
glasses [22]. Our approach analyzes whether thermodynam-
ics in its standard form can apply locally. A study of whether
a generalized form of thermodynamics might apply even
more locally should be a subject of future research.

A typical setup where the minimal length scale we calcu-
late becomes relevant could be the measurement of a tem-
perature profile with very high resolution, etc. One is thus
interested in scenarios where the entire sample is expected to
be in a stationary state. In most cases this state is close to a
thermal equilibrium state [23].

Based on the above arguments and noting that a quantum
description becomes imperative at nanoscopic scales, the fol-
lowing approach appears to be reasonable: Consider a large
homogeneous quantum system, brought into a thermal state
via interaction with its environment, divide this system into
subgroups, and analyze for what subgroup size the concept
of temperature is still applicable.

Harmonic lattice models are a standard tool for the de-
scription of thermal properties of solids. We therefore apply
our theory to a harmonic chain model to get estimates that
are expected to be relevant for real materials and might be
tested by experiments.

Recently, spin chains have been subject of extensive stud-
ies in condensed matter physics and quantum information
theory. Thus correlations and possible local temperatures in
spin chains are of interest, both from a theoretical and ex-
perimental point of view [24,25]. We study spin chains with
respect to our present purpose and compare their character-
istics with the harmonic chain.

This paper is organized as follows: In Sec. II, we present
the general theoretical approach which derives two condi-
tions on the effective group interactions and the global tem-
perature. In the following two sections we apply the general
consideration to two concrete models and derive estimates
for the minimal subgroup size. Section III deals with a har-
monic chain, a model with an infinite energy spectrum. In
contrast, a spin chain has a bounded energy spectrum. Sec-
tion IV therefore discusses an Ising spin chain in a transverse
field. In the conclusions section, Sec. V, we compare the
results for the different models considered and indicate fur-
ther interesting topics.

## II. GENERAL THEORY

We consider a homogeneous (i.e., translation invariant)
chain of elementary quantum subsystems with nearest neigh-
bor interactions. The Hamiltonian of our system is thus of
the form [26]
$$
H=\sum_{i} H_{i}+I_{i, i+1}, \quad(1)
$$
where the index $i$ labels the elementary subsystems. $H_{i}$ is the
Hamiltonian of subsystem $i$ and $I_{i, i+1}$ the interaction between
subsystem $i$ and $i+1$. We assume periodic boundary condi-
tions.

We now form $N_{G}$ groups of $n$ subsystems each [index $i$
$\to(\mu-1) n+j ; \mu=1,..., N_{G} ; j=1,..., n]$ and split this Hamil-
tonian into two parts,
$$
H=H_{0}+I, \quad(2)
$$
where $H_{0}$ is the sum of the Hamiltonians of the isolated
groups,
$$
H_{0}=\sum_{\mu=1}^{N_{G}}\left(\mathcal{H}_{\mu}-I_{\mu n, \mu n+1}\right)
$$
with
$$
\mathcal{H}_{\mu}=\sum_{j=1}^{n} H_{n(\mu-1)+j}+I_{n(\mu-1)+j, n(\mu-1)+j+1} \quad(3)
$$
and $I$ contains the interaction terms of each group with its
neighbor group,
$$
I=\sum_{\mu=1}^{N_{G}} I_{\mu n, \mu n+1}. \quad(4)
$$

We label the eigenstates of the total Hamiltonian $H$ and their
energies with the Greek indices $(\varphi, \psi)$ and eigenstates and
energies of the group Hamiltonian $H_{0}$ with Latin indices
$(a, b)$,
$$
H|\varphi\rangle=E_{\varphi}|\varphi\rangle \quad \text { and } \quad H_{0}|a\rangle=E_{a}|a\rangle. \quad(5)
$$

Here, the states $|a\rangle$ are products of group eigenstates,
$$
|a\rangle=\prod_{\mu=1}^{N_{G}}\left|a_{\mu}\right\rangle, \quad(6)
$$
where $(\mathcal{H}_{\mu}-I_{\mu n, \mu n+1})|a_{\mu}\rangle=E_{\mu}|a_{\mu}\rangle$. $E_{\mu}$ is the energy of one
subsystem only and $E_{a}=\sum_{\mu=1}^{N_{G}} E_{\mu}$.

### A. Thermal state in the product basis

We assume that the total system is in a thermal state with
the density matrix
$$
\langle\varphi|\hat{\rho}| \psi\rangle=\frac{e^{-\beta E_{\varphi}}}{Z} \delta_{\varphi \psi} \quad(7)
$$
in the eigenbasis of $H$. Here, $Z$ is the partition sum and $\beta$
$=(k_{B} T)^{-1}$ the inverse temperature with Boltzmann's constant
$k_{B}$ and temperature $T$. Transforming the density matrix (7)
into the eigenbasis of $H_{0}$ we obtain

$$
\langle a|\hat{\rho}|a\rangle=\int_{E_{0}}^{E_{1}} w_{a}(E) \frac{e^{-\beta E}}{Z} d E
\tag{8}
$$

for the diagonal elements in the new basis. Here, the sum over all states $|\varphi\rangle$ has been replaced by an integral over the energy. $E_{0}$ is the energy of the ground state and $E_{1}$ the upper limit of the spectrum. For systems with an energy spectrum that does not have an upper bound, the limit $E_{1} \rightarrow \infty$ should be taken. The density of conditional probabilities $w_{a}(E)$ is given by

$$
w_{a}(E)=\frac{1}{\Delta E} \sum_{\{|\varphi\rangle: E \leqslant E_{\varphi}<E+\Delta E\}}|\langle a \mid \varphi\rangle|^{2},
\tag{9}
$$

where $\Delta E$ is small and the sum runs over all states $|\varphi\rangle$ with eigenvalues $E_{\varphi}$ in the interval $[E, E+\Delta E)$. To compute the integral of Eq. (8) we need to know the distribution of the conditional probabilities $w_{a}(E)$.

The state $|a\rangle$ is not an eigenstate of the total Hamiltonian $H$. Thus if $H$ would be measured in the state $|a\rangle$, eigenvalues of $H$ would be obtained with certain probabilities: $w_{a}(E)$ is the density of this probability distribution. Since the Hamil- tonian $H$ is the sum of Hamiltonians of the groups, the situ ation has some analogies to a sum of random variables. This indicates that there might exist a central limit theorem for the present quantum system, provided the number of groups be- comes very large [27]. Since the state $|a\rangle$ is not translation invariant and since $H$ also contains the group interactions, the central limit theorem has to be of a Lyapunov (or Linde- berg) type for mixing sequences [28]. One can indeed show that such a quantum central limit theorem exists for the present model [29,30] and that $w_{a}(E)$ thus converges to a Gaussian normal distribution in the limit of infinite number of groups $N_{G}$,

$$
\lim _{N_{G} \rightarrow \infty} w_{a}(E)=\frac{1}{\sqrt{2 \pi} \Delta_{a}} \exp \left(-\frac{\left(E-E_{a}-\varepsilon_{a}\right)^{2}}{2 \Delta_{a}^{2}}\right), \quad(10)
$$

where the quantities $\varepsilon_{a}$ and $\Delta_{a}$ are defined by

$$
\varepsilon_{a} \equiv\langle a|H| a\rangle-E_{a},
\tag{11}
$$

$$
\Delta_{a}^{2} \equiv\left\langle a\left|H^{2}\right| a\right\rangle-\langle a|H| a\rangle^{2}.
\tag{12}
$$

$\varepsilon_{a}$ is the difference between the energy expectation value of the distribution $w_{a}(E)$ and the energy $E_{a}$, while $\Delta_{a}^{2}$ is the variance of the energy $E$ for the distribution $w_{a}(E)$. Note that $\varepsilon_{a}$ has a classical counterpart while $\Delta_{a}^{2}$ is purely quantum mechanical. It appears because the commutator $[H, H_{0}]$ is nonzero, and the distribution $w_{a}(E)$ therefore has nonzero width. The two quantities $\varepsilon_{a}$ and $\Delta_{a}^{2}$ can also be expressed in terms of the interaction only [see Eq. (2)],

$$
\varepsilon_{a}=\langle a|I| a\rangle,
\tag{13}
$$

$$
\Delta_{a}^{2}=\left\langle a\left|I^{2}\right| a\right\rangle-\langle a|I| a\rangle^{2},
\tag{14}
$$

meaning that $\varepsilon_{a}$ is the expectation value and $\Delta_{a}^{2}$ the squared width of the interactions in the state $|a\rangle$.

The rigorous proof of Eq. (10) is given in Ref. [29] and based on the following two assumptions: The energy of each group $\mathcal{H}_{\mu}$ as defined in Eq. (3) is bounded, i.e.,

$$
\left\langle\chi\left|\mathcal{H}_{\mu}\right| \chi\right\rangle \leqslant C
\tag{15}
$$

for all normalized states $|\chi\rangle$ and some constant $C$, and

$$
\left\langle a\left|H^{2}\right| a\right\rangle-\langle a|H| a\rangle^{2} \geqslant N_{G} C^{\prime}
\tag{16}
$$

for some constant $C^{\prime}>0$.

In scenarios where the energy spectrum of each elemen- tary subsystem has an upper limit, such as spins, condition (15) is met a priori. For subsystems with an infinite energy spectrum, such as harmonic oscillators, we restrict our analy- sis to states where the energy of every group, including the interactions with its neighbors, is bounded. Thus our consid- erations do not apply to product states $|a\rangle$, for which all the energy was located in only one group or only a small number of groups. Since $N_{G} \gg 1$, the number of such states is vanish- ingly small compared to the number of all product states.

If conditions (15) and (16) are met, Eq. (8) can be com- puted for $N_{G} \gg 1$ [31]:

$$
\begin{aligned}
\langle a|\hat{\rho}| a\rangle= & \frac{1}{2 Z} \exp \left(-\beta y_{a}+\frac{\beta^{2} \Delta_{a}^{2}}{2}\right)\left[\operatorname{erfc}\left(\frac{E_{0}-y_{a}+\beta \Delta_{a}^{2}}{\sqrt{2} \Delta_{a}}\right)\right. \\
& \left.-\operatorname{erfc}\left(\frac{E_{1}-y_{a}+\beta \Delta_{a}^{2}}{\sqrt{2} \Delta_{a}}\right)\right],
\end{aligned}
\tag{17}
$$

where $y_{a}=E_{a}+\varepsilon_{a}$ and $\operatorname{erfc}(x)$ is the conjugate Gaussian error function,

$$
\operatorname{erfc}(x)=\frac{2}{\sqrt{\pi}} \int_{x}^{\infty} e^{-s^{2}} d s.
\tag{18}
$$

The second error function in Eq. (17) only appears if the energy is bounded and the integration extends from the en- ergy of the ground state $E_{0}$ to the upper limit of the spectrum $E_{1}$.

Note that $y_{a}$ is a sum of $N_{G}$ terms and that $\Delta_{a}$ fulfills Eq. (16). The arguments of the conjugate error functions thus grow proportional to $\sqrt{N_{G}}$ or stronger. If these arguments divided by $\sqrt{N_{G}}$ are finite (different from zero), the asymptotic expansion of the error function [32] may thus be used for $N_{G} \gg 1$:

$$
\operatorname{erfc}(x) \approx \begin{cases}\frac{\exp \left(-x^{2}\right)}{\sqrt{\pi} x} & \text { for } x \rightarrow \infty \\
2+\frac{\exp \left(-x^{2}\right)}{\sqrt{\pi} x} & \text { for } x \rightarrow-\infty.\end{cases}
\tag{19}
$$

Inserting this approximation into Eq. (17) and using $E_{0}$ $<y_{a}<E_{1}$ shows that the second conjugate error function, which contains the upper limit of the energy spectrum, can always be neglected compared to the first, which contains the ground state energy.

The same type of arguments show that the normalizations of the Gaussian in Eq. (10) is correct although the energy range does not extend over the entire real axis $(-\infty, \infty)$.

Applying the asymptotic expansion (19), Eq. (17) can be taken to read

$$
\langle a|\hat{\rho}| a\rangle=\frac{1}{Z} \exp \left[-\beta\left(E_{a}+\varepsilon_{a}-\frac{\beta \Delta_{a}^{2}}{2}\right)\right]
\tag{20}
$$

for $\left(E_{0}-E_{a}-\varepsilon_{a}+\beta \Delta_{a}^{2}\right) /\left(\sqrt{2 N_{G}} \Delta_{a}\right)<0$ and

$$
\langle a|\hat{\rho}| a\rangle=\frac{\exp \left(-\beta E_{0}-\frac{\left(E_{a}+\varepsilon_{a}-E_{0}\right)^{2}}{2 \Delta_{a}^{2}}\right)}{\sqrt{2 \pi} Z \frac{E_{0}-E_{a}-\varepsilon_{a}+\beta \Delta_{a}^{2}}{\Delta_{a}}},
\tag{21}
$$

for $\left(E_{0}-E_{a}-\varepsilon_{a}+\beta \Delta_{a}^{2}\right) /\left(\sqrt{2 N_{G}} \Delta_{a}\right)>0$.

The off diagonal elements $\langle a|\hat{\rho}| b\rangle$ vanish for $|E_{a}-E_{b}|$ $>\Delta_{a}+\Delta_{b}$ because the overlap of the two distributions of conditional probabilities becomes negligible. For $|E_{a}-E_{b}|$ $<\Delta_{a}+\Delta_{b}$, the transformation involves an integral over frequencies and thus these terms are significantly smaller than the entries on the diagonal.

### B. Conditions for local thermal states

We now test under what conditions the density matrix $\hat{\rho}$ may be approximated by a product of canonical density matrices with temperature $\beta_{l o c}$ for each subgroup $\mu$ $=1,2, \ldots, N_{G}$. Since the trace of a matrix is invariant under basis transformations, it is sufficient to verify the correct energy dependence of the product density matrix. If we assume periodic boundary conditions, all reduced density matrices are equal and their product is of the form $\langle a|\hat{\rho}| a\rangle$ $\propto \exp \left(-\beta_{l o c} E_{a}\right)$. We thus have to verify whether the logarithm of the right-hand side of Eqs. (20) and (21) is a linear function of the energy $E_{a}$,

$$
\ln (\langle a|\hat{\rho}| a\rangle) \approx-\beta_{l o c} E_{a}+c,
\tag{22}
$$

where $\beta_{l o c}$ and $c$ are constants.

Note that Eq. (22) does not imply that the occupation probability of an eigenstate $|\varphi\rangle$ with energy $E_{\varphi}$ and a product state with the same energy $E_{a} \approx E_{\varphi}$ are equal. Since $\beta_{l o c}$ and $\beta$ enter into the exponents of the respective canonical distributions, the difference between both has significant consequences for the occupation probabilities; even if $\beta_{l o c}$ and $\beta$ are equal with very high accuracy, but not exactly the same, occupation probabilities may differ by several orders of magnitude, provided that the energy range is large enough.

We exclude negative temperatures $(\beta>0)$. Equation (22) can only be true for

$$
\frac{E_{a}+\varepsilon_{a}-E_{0}}{\sqrt{N_{G}} \Delta_{a}}>\beta \frac{\Delta_{a}^{2}}{\sqrt{N_{G}} \Delta_{a}},
\tag{23}
$$

as can be seen from Eqs. (20) and (21). In this case, $\langle a|\hat{\rho}| a\rangle$ is given by Eq. (20) and to satisfy Eq. (22), $\varepsilon_{a}$ and $\Delta_{a}^{2}$ furthermore have to be of the following form:

$$
-\varepsilon_{a}+\frac{\beta}{2} \Delta_{a}^{2} \approx c_{1} E_{a}+c_{2},
\tag{24}
$$

where $c_{1}$ and $c_{2}$ are constants. Note that $\varepsilon_{a}$ and $\Delta_{a}^{2}$ need not be functions of $E_{a}$ and therefore in general cannot be expanded in a Taylor series.

![](./images/812307997077274626_1.jpg)

FIG. 1. The product of the density of states $\eta(E)$ times the occupation probabilities $\langle\varphi|\hat{\rho}| \varphi\rangle$ forms a strongly pronounced peak at $E=\bar{E}$.

To ensure that the density matrix of each subgroup $\mu$ is approximately canonical, one needs to satisfy Eq. (24) for each subgroup $\mu$ separately;

$$
-\frac{\varepsilon_{\mu-1}+\varepsilon_{\mu}}{2}+\frac{\beta}{4}\left(\Delta_{\mu-1}^{2}+\Delta_{\mu}^{2}\right)+\frac{\beta}{6} \tilde{\Delta}_{\mu}^{2} \approx c_{1} E_{\mu}+c_{2}, \quad(25)
$$

where $\varepsilon_{\mu}=\langle a|I_{\mu n, \mu n+1}| a\rangle$ with $\varepsilon_{a}=\sum_{\mu=1}^{N_{G}} \varepsilon_{\mu}, \Delta_{\mu}^{2}=\langle a|H_{\mu}^{2}| a\rangle$ $-\langle a|H_{\mu}| a\rangle^{2}$ and $\tilde{\Delta}_{\mu}^{2}=\sum_{\nu=\mu-1}^{\mu+1}\langle a|H_{\nu-1} H_{\nu}+H_{\nu} H_{\nu-1}| a\rangle$ $-2\langle a|H_{\nu-1}| a\rangle\langle a|H_{\nu}| a\rangle$.

Temperature becomes intensive, if the constant $c_{1}$ vanishes,

$$
\left|c_{1}\right| \ll 1 \Rightarrow \beta_{l o c}=\beta.
\tag{26}
$$

If this was not the case, temperature would not be intensive, although it might exist locally.

It is sufficient to satisfy conditions (23) and (25) for an adequate energy range $E_{\min } \leqslant E_{\mu} \leqslant E_{\max }$ only. For large systems with a modular structure, i.e., a system composed of a large number of subsystems, the density of states is typically a rapidly growing function of energy [21,33]. If the total system is in a thermal state, occupation probabilities decay exponentially with energy. The product of these two functions is thus sharply peaked at the expectation value of the energy $\bar{E}$ of the total system $\bar{E}+E_{0}=\operatorname{Tr}(H \hat{\rho})$, with $E_{0}$ being the ground state energy (see Fig. 1).

The energy range thus needs to be centered around this peak and large enough. On the other hand it must not be larger than the range of values $E_{\mu}$ can take on. Therefore a pertinent and "safe" choice for $E_{\min }$ and $E_{\max }$ is

$$
\begin{aligned}
& E_{\min }=\max \left(\left[E_{\mu}\right]_{\min }, \frac{1}{\alpha} \frac{\bar{E}}{N_{G}}+\frac{E_{0}}{N_{G}}\right), \\
& E_{\max }=\min \left(\left[E_{\mu}\right]_{\max }, \alpha \frac{\bar{E}}{N_{G}}+\frac{E_{0}}{N_{G}}\right),
\end{aligned}
\tag{27}
$$

where $\alpha \gg 1$ and $\bar{E}$ will in general depend on the global temperature. In Eq. (27), $\left[E_{\mu}\right]_{\min }$ and $\left[E_{\mu}\right]_{\max }$ denote the minimal and maximal values $E_{\mu}$ can take on.

Figure 2 shows the logarithm of Eq. (17) and the logarithm of a canonical distribution with the same $\beta$ for a harmonic chain as an example. The actual density matrix is

![](./images/812307997077274626_2.jpg)

more mixed than the canonical one. In the interval between the two vertical lines, both criteria (23) and (25) are satisfied. For $E<E_{low}$ Eq. (23) is violated and Eq. (25) for $E>E_{high}$. To allow for a description by means of canonical density matrices, the group size needs to be chosen such that $E_{low}$ $<E_{min}$ and $E_{high}>E_{max}$.

For a model obeying Eqs. (15) and (16), the two conditions (23) and (25), which constitute the general result of this paper, must both be satisfied. These fundamental criteria will now be applied to some concrete examples.

### III. HARMONIC CHAIN

As a representative for the class of systems with an infinite energy spectrum, we consider a harmonic chain of $N_G \cdot n$ particles of mass $m$ and spring constant $\sqrt{m}\omega_0$. In this case, the Hamiltonian reads
$$
H_i=\frac{m}{2} p_i^2+\frac{m}{2} \omega_0^2 q_i^2, \tag{28}
$$
$$
I_{i, i+1}=-m \omega_0^2 q_i q_{i+1}, \tag{29}
$$
where $p_i$ is the momentum of the particle at site $i$ and $q_i$ the displacement from its equilibrium position $i \cdot a_0$ with $a_0$ being the distance between neighboring particles at equilibrium. We divide the chain into $N_G$ groups of $n$ particles each and thus get a partition of the type considered above.

The Hamiltonian of one group is diagonalized by a Fourier transform and the definition of creation and annihilation operators $a_k^{\dagger}$ and $a_k$ for the Fourier modes (see Appendix A).
$$
E_a=\sum_{\mu=1}^{N_G} \sum_k \omega_k\left(n_k^a(\mu)+\frac{1}{2}\right), \tag{30}
$$
where $k=\pi l /[a_0(n+1)]$ ($l=1,2, \ldots, n$) and the frequencies $\omega_k$ are given by $\omega_k^2=4 \omega_0^2 \sin^2(ka/2)$. $n_k^a(\mu)$ is the occupation number of mode $k$ of group $\mu$ in the state $|a\rangle$. We chose units where $\hbar=1$.

We first verify that the harmonic chain model fulfills the conditions for the applicability of the quantum central limit theorem (10). To see that it satisfies the condition (16) one needs to express the group interaction $I_{\mu n, \mu n+1}$ in terms of $a_k^{\dagger}$ and $a_k$, which yields $\tilde{\Delta}_{\mu}=0$ for all $\mu$ and therefore
$$
\Delta_a^2=\sum_{\mu=1}^{N_G} \Delta_{\mu}^2, \tag{31}
$$
where $\Delta_{\mu}$, the width of one group interaction, reads
$$
\begin{aligned}
\Delta_{\mu}^2= & \left(\frac{2}{n+1}\right)^2\left[\sum_k \cos^2\left(\frac{k a_0}{2}\right) \omega_k\left(n_k+\frac{1}{2}\right)\right] \\
& \cdot\left[\sum_p \cos^2\left(\frac{p a_0}{2}\right) \omega_p\left(m_p+\frac{1}{2}\right)\right].
\end{aligned} \tag{32}
$$
$\Delta_{\mu}^2$ has a minimum value since all $n_k \geqslant 0$ and all $m_p \geqslant 0$. In Eq. (32), $k$ labels the modes of group $\mu$ with occupation numbers $n_k$ and $p$ the modes of group $\mu+1$ with occupation numbers $m_p$. The width $\Delta_a^2$ thus fulfills condition (16).

Since the spectrum of every single oscillator is infinite, condition (15) can only be satisfied for states, for which the energy of the system is distributed among a substantial fraction of the groups, as discussed in Sec. II.

We now turn to analyze the two criteria (23) and (25). The expectation values of the group interactions vanish, $\varepsilon_{\mu}=0$, while the widths $\Delta_{\mu}^2$ depend on the occupation numbers $n_k$ and therefore on the energies $E_{\mu}$. We thus have to consider both conditions, Eqs. (23) and (25). To analyze these, we make use of the continuum or Debye approximation [34], requiring $n \gg 1$, $a_0 \ll l$, where $l=n a_0$, and the length of the chain to be finite. In this case we have $\omega_k=vk$ with the constant velocity of sound $v=\omega_0 a_0$ and $\cos(ka_0/2) \approx 1$. The width of the group interaction thus translates into
$$
\Delta_{\mu}^2=\frac{4}{n^2} E_{\mu} E_{\mu+1}, \tag{33}
$$
where $n+1 \approx n$ has been used. The relevant energy scale is introduced by the thermal expectation value of the entire chain
$$
\overline{E}=N_G n k_B \Theta\left(\frac{T}{\Theta}\right)^2 \int_0^{\Theta / T} \frac{x}{e^x-1} d x, \tag{34}
$$
and the ground state energy is given by
$$
E_0=N_G n k_B \Theta\left(\frac{T}{\Theta}\right)^2 \int_0^{\Theta / T} \frac{x}{2} d x=\frac{N_G n k_B \Theta}{4}. \tag{35}
$$

We first consider the criterion (23).

For a given $E_a=\sum_{\mu} E_{\mu}$, the squared width $\Delta_{\mu}^2$ is largest if all $E_{\mu}$ are equal, $E_{\mu}=\widetilde{E} \forall \mu$. Thus Eq. (23) is hardest to satisfy for that case, where it reduces to
$$
\widetilde{E}-\frac{E_0}{N_G}-\frac{4 \beta}{n^2} \widetilde{E}^2>0. \tag{36}
$$

Equation (36) sets a lower bound on $n$. For temperatures where $\overline{E}<E_0$, this bound is strongest for low energies $\widetilde{E}$, while at $\overline{E}>E_0$ it is strongest for high energies $\widetilde{E}$. Since condition (25) is a stronger criterion than condition (23) for $\overline{E}>E_0$, we only consider Eq. (36) at temperatures where $\overline{E}$ $<E_0$. In this range, Eq. (36) is hardest to satisfy for low energies, i.e., at $\widetilde{E}=(\overline{E}/\alpha N_G)+(E_0/N_G)$, where it reduces to

![](./images/812307997077274626_3.jpg)

FIG. 3. Log-log-plot of $n_{min}$ from Eq. (37) (dashed line) and $n_{min}$ from Eq. (40) (solid line) for $\alpha=10$ and $\delta=0.01$ as a function of $T/\Theta$ for a harmonic chain. $\delta$ and $\alpha$ are defined in Eqs. (40) and (27), respectively. Local temperature exists in the shaded area.

$$
n>\frac{\Theta}{T} \frac{\alpha}{4 \overline{e}}\left(\frac{4 \overline{e}}{\alpha}+1\right)^{2}, \quad(37)
$$

with $\overline{e}=\overline{E} /(n N_{G} k_{B} \Theta)$.

To test condition (25) we take the derivative with respect to $E_{\mu}$ on both sides,
$$
\frac{\beta}{n^{2}}\left(E_{\mu-1}+E_{\mu+1}-2 \frac{E_{0}}{N_{G}}\right)+\frac{2 \beta}{n^{2}} \frac{E_{0}}{N_{G}} \approx c_{1}, \quad(38)
$$
where we have separated the energy dependent and the constant part in the left-hand side Eq. (38) is satisfied if the energy dependent part is much smaller than 1,
$$
\frac{\beta}{n^{2}}\left(E_{\mu-1}+E_{\mu+1}-2 \frac{E_{0}}{N_{G}}\right) \leqslant \delta \ll 1. \quad(39)
$$

This condition is hardest to satisfy for high energies. Taking $E_{\mu-1}$ and $E_{\mu+1}$ equal to the upper bound in Eq. (27), it yields
$$
n>\frac{2 \alpha}{\delta} \frac{\Theta}{T} \overline{e}, \quad(40)
$$
where the "accuracy" parameter $\delta \ll 1$ quantifies the value of the energy dependent part in Eq. (38).

Since the constant part in the left-hand side of (38) satisfies
$$
\frac{2 \beta}{n^{2}} \frac{E_{0}}{N_{G}}<\frac{\sqrt{\delta}}{\alpha}\left(\frac{1}{\sqrt{2}}-\frac{\sqrt{\delta}}{\alpha}\right) \leqslant 1, \quad(41)
$$
temperature is intensive.

Inserting Eq. (34) into Eqs. (37) and (40) one can now calculate the minimal $n$ for given $\delta, \alpha, \Theta$ and $T$. Figure 3 shows $n_{min}$ for $\alpha=10$ and $\delta=0.01$ given by criterion (37) and (40) as a function of $T/\Theta$. Hence local temperature exists, i.e., local states are canonical for all group sizes larger than the maximum of the two $n_{min}$ curves plotted in Fig. 3.

For high (low) temperatures $n_{min}$ can thus be estimated by
$$
n_{\min } \approx \begin{cases}2 \alpha / \delta & \text { for } \quad T>\Theta \\ \left(3 \alpha / 2 \pi^{2}\right)(\Theta / T)^{3} & \text { for } \quad T<\Theta.\end{cases}
$$

Equation (42) also shows the dependence of the results on the "accuracy parameters" $\alpha$ and $\delta$. In the whole temperature range, $n_{min} \propto \alpha$, in other words, the larger one chooses the energy range where Eqs. (23) and (25) should be fulfilled, the larger has to be the number of particles per group. Furthermore, for high temperatures, $n_{min} \propto \delta^{-1}$, which simply states that one needs more particles per group to obtain a canonical state with better accuracy.

Since the resulting minimal group sizes $n_{min}$ are larger than $10^{3}$ for all temperatures, the application of the Debye approximation is well justified.

## IV. ISING SPIN CHAIN IN A TRANSVERSE FIELD

In this section we consider an Ising spin chain in a transverse field. For this model the Hamiltonian reads
$$
H_{i}=-B \sigma_{i}^{z},
$$

$$
I_{i, i+1}=-\frac{J_{x}}{2} \sigma_{i}^{x} \otimes \sigma_{i+1}^{x}-\frac{J_{y}}{2} \sigma_{i}^{y} \otimes \sigma_{i+1}^{y}, \quad(43)
$$

where $\sigma_{i}^{x}, \sigma_{i}^{y}$, and $\sigma_{i}^{z}$ are the Pauli matrices. $B$ is the magnetic field and $J_{x}$ and $J_{y}$ are two coupling parameters. We will always assume $B>0$.

The entire chain with periodic boundary conditions may be diagonalized via successive Jordan-Wigner, Fourier, and Bogoliubov transformations (see Appendix B). The relevant energy scale is introduced via the thermal expectation value (without the ground state energy)
$$
\overline{E}=\frac{n N_{G}}{2 \pi} \int_{-\pi}^{\pi} d k \frac{\omega_{k}}{\exp \left(\beta \omega_{k}\right)+1}, \quad(44)
$$
where $\omega_{k}$ is given in Eq. (B9). The ground state energy $E_{0}$ is given by
$$
E_{0}=-\frac{n N_{G}}{2 \pi} \int_{-\pi}^{\pi} d k \frac{\omega_{k}}{2}. \quad(45)
$$

Since $N_{G} \gg 1$, the sums over all modes have been replaced by integrals.

If one partitions the chain into $N_{G}$ groups of $n$ subsystems each, the groups may also be diagonalized via a Jordan-Wigner and a Fourier transformation (see Appendix B). Using the abbreviations
$$
K=\frac{J_{x}+J_{y}}{2 B} \quad \text { and } \quad L=\frac{J_{x}-J_{y}}{2 B}, \quad(46)
$$
the energy $E_{a}$ reads
$$
E_{a}=2 B \sum_{\mu=1}^{N_{G}} \sum_{k}[1-K \cos (k)]\left(n_{k}^{a}(\mu)-\frac{1}{2}\right), \quad(47)
$$
where $k=\pi l /(n+1)(l=1,2, \ldots, n)$ and $n_{k}^{a}(\mu)$ is the Fermi onic occupation number of mode $k$ of group $\mu$ in the state $|a\rangle$. It can take on the values 0 and 1.

For the Ising model at hand one has, as for the harmonic chain, $\varepsilon_{a}=0$ for all states $|a\rangle$, while the squared variance $\Delta_{a}^{2}$ reads

$$
\Delta_{a}^{2}=\sum_{\mu=1}^{N_{G}} \Delta_{\mu}^{2},
\tag{48}
$$

with

$$
\begin{aligned}
\Delta_{\mu}^{2}= & B^{2}\left(\frac{K^{2}}{2}+\frac{L^{2}}{2}\right)-2 B^{2}\left(K^{2}-L^{2}\right) \\
& \times\left[\frac{2}{n+1} \sum_{k} \sin ^{2}(k)\left(n_{k}^{a}(\mu)-\frac{1}{2}\right)\right] \\
& \times\left[\frac{2}{n+1} \sum_{p} \sin ^{2}(p)\left(n_{p}^{a}(\mu+1)-\frac{1}{2}\right)\right], \quad(49)
\end{aligned}
$$

where the $n_{k}^{a}(\mu)$ are the same Fermionic occupation numbers as in Eq. (47).

The conditions for the central limit theorem are met for the Ising chain apart from two exceptions: Condition (15) is always fulfilled as the Hamiltonian of a single spin has finite dimension. As follows from Eq. (49), condition (16) is satisfied except for one single state in the case where $J_{x}=J_{y}$ ($L$ $=0$) and $J_{x}=-J_{y}$ ($K=0$), respectively. These two states have $\Delta_{\mu}^{2}=0$ and thus $\Delta_{a}^{2}<N_{G} C^{\prime}$. The state for $L=0$ is the one where all occupation numbers $n_{k}^{a}(\mu)$ vanish and the state for $K=0$ is the state with alternating occupation numbers $n_{k}^{a}(\mu)=0$, $n_{k}^{a}(\mu+1)=1$, $n_{k}^{a}(\mu+2)=0$, ... (for all $k$ each). As there is, for given parameters, at most one state that does not fulfill Eq. (16), the fraction of states where our theory does not apply is negligible for $N_{G} \gg 1$.

We now turn to analyze conditions (23) and (25). Since the spectrum of the Ising chain is limited, there is no approximation analog to the Debye approximation for the harmonic chain and $\Delta_{\mu}^{2}$ cannot be expressed in terms of $E_{\mu-1}$ and $E_{\mu}$. We therefore approximate Eqs. (23) and (25) with simpler expressions. The results are thus quantitatively not as precise as for the harmonic chain, but nevertheless yield reliable order of magnitude estimates.

Let us first analyze condition (23). Since it cannot be checked for every state $|a\rangle$ we use the stronger condition

$$
E_{\mu}-\frac{E_{0}}{N_{G}}>\beta\left[\Delta_{\mu}^{2}\right]_{\max },
\tag{50}
$$

instead, which implies that Eq. (23) holds for all states $|a\rangle$. We require Eq. (50) to be true for all states with energies in the range (27). It is hardest to satisfy for $E_{\mu}=E_{min}$, we thus get the condition on $n$:

$$
n>\beta \frac{\left[\Delta_{\mu}^{2}\right]_{\max }}{e_{\min }-e_{0}},
\tag{51}
$$

where $e_{min}=E_{min}/n$ and $e_{0}=E_{0}/(nN_{G})$.

We now turn to analyze condition (25). Equation (49) shows that the $\Delta_{\mu}^{2}$ do not contain terms which are proportional to $E_{\mu}$. One thus has to determine when the $\Delta_{\mu}^{2}$ are approximately constant which is the case if

![](./images/812307997077274626_4.jpg)

FIG. 4. Log-log plot of $n_{min}$ from Eq. (51) for $K=L=0.1$ (dashed line) and for $K=L=10$ (solid line) as a function of $T/B$. $\alpha=10$ is defined in Eq. (27).

$$
\beta \frac{\left[\Delta_{\mu}^{2}\right]_{\max }-\left[\Delta_{\mu}^{2}\right]_{\min }}{2} \ll\left[E_{\mu}\right]_{\max }-\left[E_{\mu}\right]_{\min },
\tag{52}
$$

where $[x]_{max}$ and $[x]_{min}$ denote the maximal and minimal value $x$ takes on in all states $|a\rangle$. As a direct consequence, we get

$$
\left|c_{1}\right| \ll 1
\tag{53}
$$

which means that temperature is intensive. Defining the quantity $e_{\mu}=E_{\mu}/n$, we can rewrite Eq. (52) as a condition on $n$,

$$
n \geqslant \frac{\beta}{2 \delta} \frac{\left[\Delta_{\mu}^{2}\right]_{\max }-\left[\Delta_{\mu}^{2}\right]_{\min }}{\left[e_{\mu}\right]_{\max }-\left[e_{\mu}\right]_{\min }},
\tag{54}
$$

where the accuracy parameter $\delta \ll 1$ is equal to the ratio of the left-hand side and the right-hand side of Eq. (52).

Since Eq. (52) does not take into account the energy range (27), its application needs some further discussion.

If the occupation number of one mode of a group is changed, say from $n_{k}^{a}(\mu)=0$ to $n_{k}^{a}(\mu)=1$, the corresponding $\Delta_{\mu}^{2}$ differ at most by $4 B^{2}|K^{2}-L^{2}|/(n+1)$. On the other hand, $[\Delta_{\mu}^{2}]_{max}-[\Delta_{\mu}^{2}]_{min}=B^{2}|K^{2}-L^{2}|$. The state with the maximal $\Delta_{\mu}^{2}$ and the state with the minimal $\Delta_{\mu}^{2}$ thus differ in nearly all occupation numbers and therefore their difference in energy is close to $[E_{\mu}]_{max}-[E_{\mu}]_{min}$. On the other hand, states with similar energies $E_{\mu}$ also have a similar $\Delta_{\mu}^{2}$. Hence the $\Delta_{\mu}^{2}$ only change quasicontinuously with energy and Eq. (52) ensures that the $\Delta_{\mu}^{2}$ are approximately constant even on only a part of the possible energy range.

We are now going to discuss three special coupling models.

### A. Coupling with constant width $\boldsymbol{\Delta_{a}}$: $\boldsymbol{J_y=0}$

If one of the couplings vanishes ($J_{x}=0$ or $J_{y}=0$), $K=L$ and $\Delta_{\mu}^{2}=B^{2}K^{2}$ is constant. In this case only criterion (23) has to be satisfied, which then coincides with Eq. (51).

Plugging expressions (44), (45), and (49) and with $J_{x}=J$ and $J_{y}=0$ into condition (51), one can now calculate the minimal number of systems per group.

Figure 4 shows $n_{min}$ for weak coupling $K=L=0.1$ and strong coupling $K=L=10$ with $\alpha=10$ as a function of $T/B$.

![](./images/812307997077274626_5.jpg)

FIG. 5. Log-log plot of $n_{min}$ as a function of $T/B$ from Eq. (51) for two values of the accuracy parameter $\alpha$, $\alpha=1$ and $\alpha=100$, left plot for $K$=$L$=0.1 and right plot for $K$=$L$=10. $\alpha$ is defined in Eq. (27).

We choose units where Boltzmann's constant $k_B$ is 1.

For any set of parameters, there is a finite temperature above which $n_{min}$=1.

Note that, since $\Delta_\mu$=const, condition (51) coincides with criterion (23) ($\Delta_\mu$=const=$[\Delta_\mu]_{max}$), so that using Eq. (51) does not involve any approximations.

As condition (24) is automatically satisfied for the present model, the results do not depend on the "accuracy parameter" $\delta$. The dependence of the results on $\alpha$ is shown in Fig. 5. $\alpha$ plays a role only where $E_{min}=\bar{E}/(\alpha N_G)+E_0/N_G$ [cf. Eq. (27)]. Then for smaller $\alpha$, $n_{min}$ eventually decays steeper and thus reaches $n_{min}$=1 already at lower temperatures. There is thus a temperature interval, where $n_{min}$ is larger for larger $\alpha$ and vice versa. This dependency has the same interpretation as for the harmonic chain.

### B. Fully anisotropic coupling: $J_x$=$-J_y$

If both couplings are nonzero, the variances $\Delta_\mu^2$ are not constant. As an example, we consider here the fully anisotropic coupling, where $J_x$=$-J_y$, i.e., $K$=0. Now criteria (51) and (54) have to be met.

For $K$=0, one has $[\Delta_\mu^2]_{max}$=$B^2L^2$, $[\Delta_\mu^2]_{min}$=0 and $[e_\mu]_{max}$=$-[e_\mu]_{min}$=$B$. Plugging these results into Eq. (54) as well as Eqs. (44) and (45) into Eq. (51), the minimal number of systems per group can be calculated.

Figure 6 shows $n_{min}$ from criterion (51) and from criterion (54) separately, for weak coupling $L$=0.1 and strong coupling $L$=10 with $\alpha$=10 and $\delta$=0.01 as a function of $T/B$. For each coupling strength $L$, the stronger condition, that is the higher curve in Fig. 6, sets the relevant lower bound to the group size $n$.

![](./images/812307997077274626_6.jpg)

FIG. 6. Log-log plot of $n_{min}$ for $L$=0.1 from Eq. (51) (dashed line) and from Eqs. (54) (dash-dotted line) and $n_{min}$ for $L$=10 from Eq. (51) (solid line) and from Eq. (54) (gray line) as a function of $T/B$. $K$=0, $\alpha$=10, and $\delta$=0.01. $\alpha$ and $\delta$ are defined in Eq. (27) and (54), respectively.

In the present case, all occupation numbers $n_k^a(\mu)$ are zero in the ground state of a group. In this state, $\Delta_\mu^2$ is maximal ($\Delta_\mu^2$=$B^2L^2$) as can be seen from Eq. (49). Therefore criterion (51) is equivalent to criterion (23) for low temperatures, where $E_{min}$=$[E_\mu]_{min}$. For high temperatures, where $E_{min}$=$\bar{E}/(\alpha N_G)$, condition (51) is slightly stronger than Eq. (23). For the present model, this is only the case for $L$=0.1 (dashed line) and $T\geq0.45B$.

In Fig. 6, the results obtained from Eq. (54) are proportional to $\delta^{-1}$ (dash-dotted line and gray line), while those obtained from Eq. (51) (dashed line and solid line) have the same dependency on $\alpha$ as shown in Fig. 5.

### C. Isotropic coupling: $J_x$=$J_y$

As a third example, we consider the isotropic coupling, where $J_x$=$J_y$, i.e., $L$=0. Again, both criteria (51) and (54) have to be met.

The values of $[\Delta_\mu^2]_{max}$, $[\Delta_\mu^2]_{min}$, $[e_\mu]_{max}$, and $[e_\mu]_{min}$ are given in Eqs. (B11)-(B13).

For the present model with $L$=0 and $|K|<1$ all occupation numbers $n_k^a(\mu)$ are zero in the ground state and thus $\Delta_\mu^2$=0. As a consequence, condition (51) cannot be used instead of Eq. (23). We therefore argue as follows: In the ground state $E_\mu-E_0/N_G$=0 as well as $\Delta_\mu^2$=0 and all occupation numbers $n_k^a(\mu)$ are zero. If one occupation number is then changed from 0 to 1, $\Delta_\mu^2$ changes at most by $4B^2K^2/(n+1)$ and $E_\mu$ changes at least by $2B(1-|K|)$. Therefore, Eq. (23) will hold for all states except the ground state if
$$
n>2B\beta\frac{K^2}{1-|K|}. \tag{55}
$$

If $|K|>1$, occupation numbers of modes with $\cos(k)$ $<1/|K|$ are zero in the ground state and occupation numbers of modes with $\cos(k)$ $>1/|K|$ are 1. $\Delta_\mu^2$ for the ground state then is $[\Delta_\mu^2]_{gs}\approx[\Delta_\mu^2]_{max}/2$ and Eq. (51) is a good approximation of condition (23).

Plugging these results into Eq. (54) as well as Eq. (44) and Eq. (45) into Eq. (51) for $|K|>1$ and using Eq. (55) for $|K|<1$, the minimal number of systems per group can be calculated.

Figure 7 shows $n_{min}$ from criteria (55) and (54) and for weak coupling $K$=0.1 and from criteria (51) and (54) and for strong coupling $K$=10 with $\alpha$=10 and $\delta$=0.01 as a function of $T/B$. For each coupling strength $K$, the stronger condition, that is the higher curve in Fig. 7, sets the relevant lower bound to the group size $n$.

Equation (55) does not take into account the relevant energy range (27); it is therefore possible that a weaker condition could be sufficient in that case. However, since Eq. (54) is a stronger condition than Eq. (55) for $K$=0.1, this possibility has no relevance.

For strong coupling, $K$=10, Eq. (51) is used to approximate Eq. (23). This approximation is expected to be good

![](./images/812307997077274626_7.jpg)

FIG. 7. Log-log-plot of $n_{min}$ for $K$=0.1 from Eq. (55) (dashed line), and from Eq. (54) (dash-dotted line) and $n_{min}$ for $K$=10 from Eq. (51) (solid line) and from Eq. (54) (gray line) as a function of $T/B$. $L$=0, $\alpha$=10, and $\delta$=0.01. $\alpha$ and $\delta$ are defined in Eqs. (27) and (54), respectively.

because $\Delta_\mu$ is close to its maximal value for low energy states. Furthermore, the temperature dependence we obtain here for $n_{min}$ for low temperatures is the same as for the harmonic chain, $n_{min}\propto T^{-3}$. This agreement is to be expected: The two couplings, when expressed in creation and annihilation operators, have the same structure and the upper limit of the spectrum of the spin chain becomes irrelevant at low temperatures.

For the present model, the dependence of the results on the "accuracy parameters" $\alpha$ and $\delta$ is as follows. Results obtained from Eq. (54) are proportional to $\delta^{-1}$ (dash-dotted line and gray line), while the result obtained from Eq. (51) (solid line) has the same dependency on $\alpha$ as shown in Fig. 5. For weak coupling and low temperatures (dashed line) $n_{min}$ does not depend on the two "accuracy parameters."

## V. SUMMARY AND CONCLUSIONS
We have considered a linear chain of particles interacting with their nearest neighbors. We have partitioned the chain into identical groups of $n$ adjoining particles each. Taking the number of such groups to be very large and assuming the total system to be in a thermal state with temperature $T$ we have found conditions [Eqs. (23) and (25)], which ensure that each group is approximately in a thermal state. Furthermore, we have determined when the isolated groups have the same temperature $T$, that is, when temperature is intensive.

The result shows that, in the quantum regime, these conditions depend on the temperature $T$, contrary to the classical case. The characteristics of the temperature dependence are determined by the width $\Delta_a$ of the distribution of the total energy eigenvalues in a product state and its dependence on the group energies $E_a$. The low temperature behavior, in particular, is related to the fact that $\Delta_a$ has a nonzero minimal value. This fact does not only appear in the harmonic chain or spin chains but is a general feature of quantum systems composed of interacting particles or subsystems. The commutator $[H,H_0]$ is nonzero and the ground state of the total system is energetically lower than the lowest product state, therefore $\Delta_a$ is nonzero, even at zero temperature [25,35-37].

We have then applied the general method to a harmonic chain and several types of Ising spin chains. For concrete models, the conditions (23) and (25) determine a minimal group size and thus a minimal length scale on which temperature may be defined according to the temperature concept we adopt. Grains of size below this length scale are no more in a thermal state. Thus temperature measurements with a higher resolution should no longer be interpreted in a standard way.

We have given order of magnitude estimates for the minimal group size (minimal length scale) for the models mentioned above. The most striking difference between the spin chains and the harmonic chain is that the energy spectrum of the spin chains is limited, while it is infinite for the harmonic chain.

For spins at very high global temperatures, the total density matrix is then almost completely mixed, i.e., proportional to the identity matrix, and thus does not change under basis transformations. There are thus global temperatures which are high enough, so that local temperatures exist even for single spins.

For the harmonic chain, this feature does not appear, since the size of the relevant energy range increases indefinitely with growing global temperature, leading to the constant minimal length scale in the high energy range.

For the spin chain with isotropic coupling, $J_x$=$J_y$, and the harmonic chain, the temperature dependencies of $n_{min}$ for low temperatures coincide, $n_{min}\propto T^{-3}$, because both couplings have the same structure and the upper limit of the spectrum of the spin chain becomes irrelevant at low temperatures. The spin chain with $J_x$=0 or $J_y$=0 shows the interesting feature that $\Delta_a^2$ is constant and condition (25) is automatically fulfilled.

The set of models we have discussed is by no means exhaustive. It would be particularly interesting to see whether there are systems for which local temperatures can exist although they are not intensive. This can happen if either $\varepsilon_a$ or $\Delta_a^2$ were proportional to $E_a$. $\Delta_a^2$, however, has dimension energy squared, so that it cannot be proportional to $E_a$ unless there exists another characteristic energy of the system independent of $E_a$. So far, we have not found models where $\varepsilon_a\propto E_a$.

For the models we consider here, the off diagonal elements of the density operator in the product basis, $\langle a|\hat{\rho}|b\rangle$ ($a\neq b$), are significantly smaller than the diagonal ones, $\langle a|\hat{\rho}|a\rangle$. Our general result, conditions (23) and (25), thus states that the density matrix $\hat{\rho}$ "approximately" factorizes with respect to the considered partition. This implies that the state $\hat{\rho}$ is not entangled with respect to this partition, at least within the chosen accuracy. It would therefore be interesting to see how our result relates to the scaling of entanglement in many particle systems [38].

Unfortunately, our approach only applies to nonzero temperatures. The underlying central limit theorem [29,30] is about the weak convergence of the distribution of energy eigenvalues. Weak convergence means that only integrals over energy intervals of nonzero length do converge. We thus cannot make statements about a system in its ground state, let alone about the entanglement in that state.

Since harmonic lattice models in Debye approximation have proven to be successful in modeling thermal properties

of insulators (e.g., heat capacity) [34], our calculation for the harmonic chain provides a first estimate of the minimal length scale on which intensive temperatures exist in insulating solids,

$$
l_{min}=n_{min}a_{0}. \tag{56}
$$

Let us give some numerical estimates: Choosing the "accu- racy parameters" to be $\alpha$=10 and $\delta$=0.01, we get for hot iron $(T \gg \Theta \approx 470 \mathrm{~K}, a_{0} \approx 2.5 \mathring{\mathrm{A}})$ $l_{min} \approx 50 \ \mu \mathrm{m}$, while for carbon $(\Theta \approx 2230 \mathrm{~K}, a_{0} \approx 1.5 \mathring{\mathrm{A}})$ at room temperature $(270 \mathrm{~K})$ $l_{min}$ $\approx 10 \ \mu \mathrm{m}$. The coarse graining will experimentally be most relevant at very low temperatures, where $l_{min}$ may even become macroscopic. A pertinent example is silicon $(\Theta$ $\approx 645 \mathrm{~K}, a_{0} \approx 2.4 \mathring{\mathrm{A}})$, which has $l_{min} \approx 10 \mathrm{~cm}$ at $T \approx 1 \mathrm{~K}$ (again with $\alpha$=10 and $\delta$=0.01).

Of course the validity of the harmonic lattice model will eventually break down at finite, high temperatures and our estimates will thus no longer apply there.

Measurable consequences of the local breakdown of the concept of temperature and their implications for future nanotechnology are interesting questions which arise in the context of the present discussion.

In the scenarios of global equilibrium, which we consider here, a temperature measurement with a microscopic ther- mometer, locally in thermal contact with the large chain, would not reveal the nonexistence of local temperature. One can model such a measurement with a small system, representing the thermometer, coupled to a heat bath, representing the chain. It is a known result of such system bath models [39], that the system always relaxes to a thermal state with the global temperature of the bath, no matter how local the coupling might be.

This, however, does not mean that the existence or non- existence of local temperatures had no physical relevance: There are indeed physical properties, which are determined by the local states rather than the global ones. Whether these properties are of thermal character depends on the existence of local temperatures. A detailed discussion of such properties will be given elsewhere.

The length scales, calculated in this paper, should also constrain the way one can meaningfully define temperature profiles in nonequilibrium scenarios [40]. Here, temperature measurements with a microscopic thermometer, which is lo- cally in thermal contact with the sample, might indeed be suitable to measure the local temperature. An explicit study of this possibility should be subject of future research.

## ACKNOWLEDGMENTS

We thank M. Michel, M. Henrich, H. Schmidt, M. Stoll- steimer, F. Tonner, and C. Kostoglou for fruitful discussions.

## APPENDIX A: DIAGONALIZATION OF THE HARMONIC CHAIN

The Hamiltonian of a harmonic chain is diagonalized by a Fourier transformation and the definition of creation and annihilation operators.

For the entire chain with periodic boundary conditions, the Fourier transformation reads

$$
\left. \begin{array}{l}
q_{j} \\
p_{j}
\end{array}\right\}=\frac{1}{\sqrt{n N_{G}}} \sum_{k}\left\{\begin{array}{l}
u_{k} \exp \left(i a_{0} k j\right) \\
v_{k} \exp \left(-i a_{0} k j\right)
\end{array}\right. \tag{A1}
$$

with $k=2 \pi l /(a_{0} n N_{G})$ and $(l=0, \pm 1, \ldots \pm(n N_{G}-2) / 2$, $(n N_{G}) / 2$, where $n N_{G}$ has been assumed to be even.

For the diagonalization of one single group, the Fourier transformation is

$$
\left. \begin{array}{l}
q_{j} \\
p_{j}
\end{array}\right\}=\sqrt{\frac{2}{n+1}} \sum_{k}\left\{\begin{array}{l}
u_{k} \\
v_{k}
\end{array}\right\} \times \sin \left(a_{0} k j\right) \tag{A2}
$$

with $k=\pi l /(a_{0}(n+1))$ and $(l=1,2, \ldots, n)$.

The definition of the creation and annihilation operators is in both cases

$$
\left. \begin{array}{l}
a_{k}^{\dagger} \\
a_{k}
\end{array}\right\}=\frac{1}{\sqrt{2 m \omega_{k}}}\left(m \omega_{k} u_{k}\left\{\begin{array}{l}
- \\
+
\end{array}\right\} i v_{k}\right), \tag{A3}
$$

where the corresponding $u_{k}$ and $v_{k}$ have to be inserted. The frequencies $\omega_{k}$ are given by $\omega_{k}^{2}=4 \omega_{0}^{2} \sin ^{2}(k a_{0} / 2)$ in both cases.

The operators $a_{k}^{\dagger}$ and $a_{k}$ satisfy Bosonic commutation relations

$$
\begin{aligned}
& {\left[a_{k}, a_{p}\right]=0,} \\
& {\left[a_{k}, a_{p}^{\dagger}\right]=\delta_{k p}}
\end{aligned} \tag{A4}
$$

and the diagonalized Hamiltonian reads

$$
H=\sum_{k} \omega_{k}\left(a_{k}^{\dagger} a_{k}+\frac{1}{2}\right). \tag{A5}
$$

## APPENDIX B: DIAGONALIZATION OF THE ISING CHAIN

The Hamiltonian of the Ising chain is diagonalized via Jordan-Wigner transformation which maps it to a Fermionic system [41,42],

$$
\begin{aligned}
& c_{i}=\left(\prod_{j<i} \sigma_{j}^{z}\right) \frac{\sigma_{i}^{x}+i \sigma_{i}^{y}}{2}, \\
& c_{i}^{\dagger}=\left(\prod_{j<i} \sigma_{j}^{z}\right) \frac{\sigma_{i}^{x}-i \sigma_{i}^{y}}{2}.
\end{aligned} \tag{B1}
$$

The operators $c_{i}$ and $c_{i}^{\dagger}$ fulfill Fermionic anticommutation relations

$$
\begin{aligned}
& \left\{c_{i}, c_{j}\right\}=0, \\
& \left\{c_{i}, c_{j}^{\dagger}\right\}=\delta_{i j}
\end{aligned} \tag{B2}
$$

and the Hamiltonian reads

$$
\begin{aligned}
H= & B\left[\sum_{j}\left(2 c_{j}^{\dagger} c_{j}-1\right)-K \sum_{j}\left(c_{j}^{\dagger} c_{j+1}+\text { H.c. }\right)\right. \\
& \left.-L \sum_{j}\left(c_{j}^{\dagger} c_{j+1}^{\dagger}+\text { H.c. }\right)\right]
\end{aligned}
$$

with $K=(J_{x}+J_{y})/(2B)$ and $L=(J_{x}-J_{y})/(2B)$. In the case of periodic boundary conditions a boundary term is neglected in Eq. (B3). For long chains $(nN_{G}\to\infty)$ this term is suppressed by a factor $(nN_{G})^{-1}$. The Hamiltonian now describes Fermions which interact with their nearest neighbors. As for the Bosonic system, a Fourier transformation maps the system to noninteracting fermions. For the whole chain with periodic boundary conditions
$$
\left.\begin{array}{l}
c_{j}^{\dagger} \\
c_{j}
\end{array}\right\}=\frac{1}{\sqrt{n N_{G}}} \sum_{k} e^{i k j} \times\left\{\begin{array}{l}
d_{k}^{\dagger} \\
d_{k}
\end{array}\right. \quad \text { (B4) }
$$
with $k=(2\pi l)/(nN_{G})$ where $l=0,\pm1,\dots,\pm(nN_{G}-2)/2$, $(nN_{G})/2$ for $nN_{G}$ even, and
$$
\left.\begin{array}{l}
c_{j}^{\dagger} \\
c_{j}
\end{array}\right\}=\sqrt{\frac{2}{n+1}} \sum_{k} \sin (k j) \times\left\{\begin{array}{l}
d_{k}^{\dagger} \\
d_{k}
\end{array}\right. \quad \text { (B5) }
$$
with $k=(\pi l)/(n+1)$ and $(l=1,2,\dots,n)$ for one single group.

In the case of periodic boundary conditions, fermion interactions of the form $d_{k}^{\dagger}d_{-k}^{\dagger}$ and $d_{k}d_{-k}$ remain. Therefore one still has to apply a Bogoliubov transformation to diagonalize the system, i.e.,
$$
\begin{aligned}
& d_{k}^{\dagger}=u_{k} b_{k}^{\dagger}-i v_{k} b_{-k}, \\
& d_{k}=u_{k} b_{k}+i v_{k} b_{-k}^{\dagger},
\end{aligned} \quad \text { (B6) }
$$
where $u_{k}=u_{-k}$, $v_{k}=-v_{-k}$, and $u_{k}^{2}+v_{k}^{2}=1$. With the definitions $u_{k}=\cos(\Theta_{k}/2)$ and $v_{k}=\sin(\Theta_{k}/2)$ the interaction terms disappear for
$$
\cos \left(\Theta_{k}\right)=\frac{1-K \cos k}{\sqrt{[1-K \cos k]^{2}+[L \sin k]^{2}}}. \quad \text { (B7) }
$$

In the case of the finite chain of one group, the Bogoliubov transformation is not needed since the corresponding terms are of the form $d_{k}^{\dagger}d_{k}^{\dagger}$ and $d_{k}d_{k}$ and vanish by virtue of Eq. (B2).

The Hamiltonians in the diagonal form read
$$
H=\sum_{k} \omega_{k}\left(b_{k}^{\dagger} b_{k}-\frac{1}{2}\right), \quad \text { (B8) }
$$
where the frequencies are
$$
\omega_{k}=2 B \sqrt{[1-K \cos k]^{2}+[L \sin k]^{2}} \quad \text { (B9) }
$$
with $k=(2\pi l)/(nN_{G})$ for the periodic chain and
$$
\omega_{k}=2 B(1-K \cos k) \quad \text { (B10) }
$$
with $k=(\pi l)/(n+1)$ for the finite chain.

For the finite chain the occupation number operators may also be chosen such that $\omega_{k}$ is always positive. Here, the convention at hand is more convenient, since the same occupation numbers also appear in the group interaction and thus in $\Delta_{\mu}$.

### Maxima and minima of $E_{\mu}$ and $\Delta_{\mu}^{2}$

The maximal and minimal values of $E_{\mu}$ are given by
$$
\left.\begin{array}{l}
{\left[E_{\mu}\right]_{max}} \\
{\left[E_{\mu}\right]_{min}}
\end{array}\right\}=\left\{\begin{array}{l}
+ \\
-
\end{array}\right\} n B, \quad \text { (B11) }
$$
for $|K|<1$ and by
$$
\left.\begin{array}{l}
{\left[E_{\mu}\right]_{max}} \\
{\left[E_{\mu}\right]_{min}}
\end{array}\right\}=\left\{\begin{array}{l}
+ \\
-
\end{array}\right\} n B \frac{2}{\pi}\left[\sqrt{K^{2}-1}+\arcsin \left(\frac{1}{|K|}\right)\right],
$$
for $|K|>1$, where the sum over all modes $k$ has been approximated with an integral.

The maximal and minimal values of $\Delta_{\mu}^{2}$ are given by
$$
\left.\begin{array}{l}
{\left[\Delta_{\mu}^{2}\right]_{max}} \\
{\left[\Delta_{\mu}^{2}\right]_{min}}
\end{array}\right\}=B^{2} ×\left\{\begin{array}{l}
\max \left(K^{2}, L^{2}\right) \\
\min \left(K^{2}, L^{2}\right).
\end{array}\right. \quad \text { (B13) }
$$

[1] J. Gemmer, A. Otte, and G. Mahler, Phys. Rev. Lett. 86, 1927 (2001).
[2] A. E. Allahverdyan and Th. M. Nieuwenhuizen, Phys. Rev. Lett. 85, 1799 (2000).
[3] D. Cahill, W. Ford, K. Goodson, G. Mahan, A. Majumdar, H. Maris, R. Merlin, and S. Phillpot, J. Appl. Phys. 93, 793 (2003).
[4] C. C. Williams and H. K. Wickramasinghe, Appl. Phys. Lett. 49, 1587 (1986).
[5] J. Varesi, and A. Majumdar, Appl. Phys. Lett. 72, 37 (1998).
[6] K. Schwab, E. A. Henriksen, J. M. Worlock, and M. L. Roukes, Nature (London) 404, 974 (2000).
[7] Y. Gao and Y. Bando, Nature (London) 415, 599 (2002).
[8] H. Pothier, S. Guéron, N. O. Birge, D. Esteve, and M. H. Devoret, Phys. Rev. Lett. 79, 3490 (1997).
[9] J. Aumentado, J. Eom, V. Chandrasekhar, P. M. Baldo, and L. E. Rehn, Appl. Phys. Lett. 75, 3554 (1999).
[10] M. E. Fisher, Arch. Ration. Mech. Anal. 17, 377 (1964).
[11] D. Ruelle, Statistical Mechanics (Benjamin, New York, 1969).
[12] J. L. Lebowitz and E. H. Lieb, Phys. Rev. Lett. 22, 631 (1969).
[13] M. Schmidt, R. Kusche, B. von Issendorf, and H. Haberland, Nature (London) 393, 238 (1998).
[14] M. Hartmann, J. Gemmer, G. Mahler, and O. Hess, Europhys. Lett. 65, 613 (2004).
[15] T. L. Hill, Thermodynamics of Small Systems (Dover, New York, 1994).
[16] T. L. Hill, Nano Lett. 1, 273 (2001).
[17] A. K. Rajagopal, C. S. Pande, and S. Abe, e-print cond-mat/ 0403738.
[18] A. Osterloh, L. Amico, G. Falci, and R. Facio, Nature (London) 416, 608 (2002).
[19] T. Roscilde, P. Verrucchi, A. Fubini, S. Haas, and V. Tognetti,

Phys. Rev. Lett. 93, 167203 (2004).

[20] V. Vedral, New J. Phys. 6, 22 (2004).

[21] R. C. Tolman, *The Principles of Statistical Mechanics* (Oxford University Press, London, 1967).

[22] Th. M. Nieuwenhuizen, Phys. Rev. Lett. 80, 5580 (1998).

[23] R. Kubo, M. Toda, and N. Hashitsume, *Statistical Physics II* (Springer, Berlin, 1985).

[24] M. Kenzelmann, R. Coldea, D. A. Tennant, D. Visser, M. Hof- mann, R. Smeibidl, and Z. Tylczynski, Phys. Rev. B 65, 144432 (2002).

[25] X. Wang, Phys. Rev. A 66, 064304 (2002).

[26] G. Mahler and V. Weberruß, *Quantum Networks*, 2nd ed. (Springer, Berlin, 1998).

[27] P. Billingsley, *Probability and Measure*, 3rd ed. (Wiley, New York, 1995).

[28] I. A. Ibargimov and Y. V. Linnik, *Independent and Stationary Sequences of Random Variables* (Wolters-Noordhoff, Gronin- gen, The Netherlands, 1971).

[29] M. Hartmann, G. Mahler, and O. Hess, Lett. Math. Phys. 68, 103 (2004).

[30] M. Hartmann, G. Mahler, and O. Hess, J. Stat. Phys. (to be published), e-print cond-mat/0406100.

[31] M. Hartmann, G. Mahler, and O. Hess, Phys. Rev. Lett. 93, 080402 (2004).

[32] M. Abramowitz and I. Stegun, *Handbook of Mathematical Functions*, 9th ed. (Dover, New York, 1970).

[33] J. Gemmer, M. Michel, and G. Mahler, *Quantum Thermody- namics* (Springer, Berlin, 2004).

[34] Ch. Kittel, *Einführung in die Festkörperphysik*, 5th ed. (Old- enburg, München, 1983).

[35] A. N. Jordan and M. Büttiker, Phys. Rev. Lett. 92, 247901 (2004).

[36] A. E. Allahverdyan and Th. M. Nieuwenhuizen, Phys. Rev. B 66, 115309 (2002).

[37] Th. M. Nieuwenhuizen and A. E. Allahverdyan, Phys. Rev. E 66, 036102 (2002).

[38] G. Vidal, J. I. Latorre, E. Rico, and A. Kitaev, Phys. Rev. Lett. 90, 227902 (2003).

[39] U. Weiss, *Quantum Dissipative Systems*, 2nd ed. (World Sci- entific, Singapore, 1999).

[40] M. Michel, M. Hartmann, J. Gemmer, and G. Mahler, Eur. Phys. J. B 34, 325 (2003).

[41] S. Katsura, Phys. Rev. 127, 1508 (1962).

[42] E. Lieb, T. Schultz, and D. Mattis, Ann. Phys. (N.Y.) 16, 407 (1961).