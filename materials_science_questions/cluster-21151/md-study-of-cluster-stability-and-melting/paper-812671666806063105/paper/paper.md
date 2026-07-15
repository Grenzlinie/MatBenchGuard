![](./images/812671666806063105_1.jpg)

# Structural transition in hot small clusters

D. I. Zhukhovitskii

Citation: *The Journal of Chemical Physics* **110**, 7770 (1999); doi: 10.1063/1.478685

View online: http://dx.doi.org/10.1063/1.478685

View Table of Contents: http://scitation.aip.org/content/aip/journal/jcp/110/16?ver=pdfcov

Published by the AIP Publishing

---

## Articles you may be interested in

[A path-integral Monte Carlo study of a small cluster: The Ar trimer](J. Chem. Phys. **132**, 244303 (2010); 10.1063/1.3445773)

[Stereographic projection path integral simulations of ( H Cl ) n clusters ( n = 2 – 5 ) : Evidence of quantum induced melting in small hydrogen bonded networks](J. Chem. Phys. **128**, 124517 (2008); 10.1063/1.2837802)

[The structure and the thermochemical properties of the H 3 + (H 2 ) n clusters (n=8–12)](J. Chem. Phys. **114**, 7066 (2001); 10.1063/1.1360198)

[Structural transitions in small molecular clusters](J. Chem. Phys. **110**, 3887 (1999); 10.1063/1.478248)

[Dynamics and instabilities near the glass transition: From clusters to crystals](J. Chem. Phys. **108**, 234 (1998); 10.1063/1.475357)

---

![](./images/812671666806063105_2.jpg)

# Structural transition in hot small clusters

D. I. Zhukhovitskiia)
Institute of High Temperatures RAS, Izhorskaya 13/19, 127412 Moscow, Russia

(Received 16 September 1998; accepted 1 February 1999)

At relatively high temperatures (higher than the melting temperature of a liquid), clusters existing in the supersaturated vapor are characterized by an intense internal motion of molecules. The virtual chains model of small ‘‘hot’’ clusters is proposed, which assumes that the number of bonds in small clusters is minimal, and that their structure is chainlike. Interpolation formulas for extensive thermodynamic functions of a cluster containing arbitrary number of atoms are found. Validity of model assumptions are verified by the molecular dynamics simulation for the ensemble with constant temperature and pressure. Simulation results are discussed, among which are the average potential energy of a cluster, the radial distribution function, and topological structure of clusters. Numerical results validate the basic assumption of proposed model. © 1999 American Institute of Physics. [S0021-9606(99)52316-7]

## I. INTRODUCTION

It is well-known that the difficulties of the classical nucleation theory $^{1–4}$ and of its modern improved versions $^{5–7}$ are related to the fact that the macroscopic liquid drop model is inappropriate for the clusters consisting of small number of molecules. The temperatures above the triple point ones appear to be relatively high for small clusters existing in the vapor. Such ‘‘hot’’ clusters are characterized by strong exci- tation of both one-particle and collective degrees of freedom of molecules that constitute the cluster. Numerical simula- tion shows that, unlike liquid droplets, small clusters are rather shapeless and are similar to the density fluctuations in nonideal gas. $^{8,9}$ The smaller the cluster, the greater is the difference between a cluster and a droplet. Since the cluster cannot be characterized by certain volume and density, and the near ordering typical for liquids is not observed for such clusters, they are sometimes called the gaslike ones.

Numerous attempts were undertaken to improve the macroscopic drop model by extension of its region of valid- ity toward small sizes (e.g., Refs. 10,11), in which this model was used as the zero approximation, and the terms in expan- sions of some thermodynamic functions of the cluster in powers of its inverse radius are calculated. It is not surprising that these attempts proved to be inefficient. To provide a relevant description of the state of the small hot cluster, a model is necessary, which is an alternative to the liquid drop model and is not based on the perturbation theory.

In this paper, the simplest system of atoms interacting via a short-range additive potential is treated. In such a sys- tem, an atom interacts only with its nearest neighbors. Since the macroscopic drop model may be treated as the extreme of maximum number of bonds in the system, the other extreme, and, therefore, an alternative to the liquid drop model is the system with minimum number of bonds. In this model, the cluster is represented as a set of connected chains. Ordering of atoms in virtual chains changes as the atoms move, hence these chains may be called virtual.

At sufficiently high temperatures, the states with high binding energy but low statistical weight (close packed struc- tures) compete with the states with low binding energy but high statistical weight. As the temperature increases, the probability of the latter increases, and the transition from close packed to gaslike structure occurs. This takes place if the difference between the binding energies of close packed and gaslike structures is not too high. This is true only for clusters containing less than ten atoms, because, due to finite cluster size, the number of bonds per atom in such clusters is noticeably lower than in bulk liquid.

The structural transition in a system with the finite num- ber of particles occurs in some finite temperature interval. The goal of this work is the investigation of cluster structure in this interval and the description of transition from the close packed to gaslike structure as the temperature in- creases. To perform this, the partition function of a small gaslike cluster is calculated. On this basis, interpolation for- mulas for cluster chemical potential and average potential energy are proposed, which join the cases of small clusters and macroscopic droplets. In such a way, the equilibrium distribution of clusters over sizes is deduced. To test pro- posed theory, molecular dynamics (MD) simulation is per- formed in the ensemble with constant temperature and pres- sure, which mimics real conditions of the supersaturated vapor.

This paper is divided in two parts. In the first one, the analytical approach is developed. The virtual chains model for small hot clusters is proposed, and the partition function of a cluster is calculated within the framework of this model in Sec. II. On this basis, an interpolation formula for the chemical potential and average potential energy of a cluster with arbitrary size are obtained in Sec. III. In the second part, MD simulation of the structural transition is performed. In Sec. IV, the simulation procedure is considered; numerical results are discussed and compared with analytical estimates in Sec. V. Section VI summarizes the results.

a)Electronic mail: dmrzh@orc.ru

## II. THE PARTITION FUNCTION OF A SMALL GASLIKE CLUSTER

Consider the cluster consisting of $g$ atoms, which interact via the pair additive potential $u(r)$. We will estimate the partition function of a cluster in two limiting cases of low and high temperatures. Let $u(r)$ be the model short-range potential,
$$
u(r)=
\begin{cases}
+\infty, & r<a-r_{0}, \\
(M \omega_{0}^{2} / 4)(r-a)^{2}-D_{0}, & a-r_{0} \leqslant r \leqslant a+r_{0}, \\
0, & r>a+r_{0},
\end{cases} \tag{1}
$$
where $M$ is the atom mass; $\omega_{0}=(2 / r_{0}) \sqrt{D_{0} / M}$, the vibration frequency of a dimer; $D_{0}$, the well depth. Potential (1) is the oscillator one in the region, where it is negative, and finite; it is assumed that the length parameters $a$ and $r_{0}$ satisfy the inequality $a / r_{0} \gg 1$ (Fig. 1).

We define a cluster as a system of atoms having at least one neighbor, which pertains to the same cluster, at the distance less than $r_{b}$. For potential (1), $r_{b}=a+r_{0}$. In the case of low temperatures, the cluster has close packed structure. Using the quasiclassical approach, which is valid even at low temperatures for argonlike system, write the cluster partition function at $g \geqslant 3$ in the form similar to the Einstein crystal model, $^{12}$
$$
\begin{aligned}
& Z_{p}^{(g)}=\frac{V}{\chi^{3}} Z_{r}^{(g)} Z_{v}^{(g)} \exp \left(\frac{D_{g}}{k_{B} T}\right), \\
& Z_{r}^{(g)}=C_{r}(g)\left(\frac{a}{\chi}\right)^{3}, \quad Z_{v}^{(g)}=C_{v}(g)\left(\frac{k_{B} T}{\hbar \omega_{0}}\right)^{3 g-6},
\end{aligned} \tag{2}
$$
where $V$ is the volume; $\chi=\sqrt{2 \pi \hbar^{2} / M k_{B} T}$ , the thermal wavelength; $k_{B}$ , the Boltzmann constant; $T$, the temperature; $Z_{r}^{(g)}$ and $Z_{v}^{(g)}$ are the rotational and vibrational partition functions, respectively; $D_{g}$ is the ground state energy of a cluster; $C_{r}(g)$ and $C_{v}(g)$ are the numerical factors defined by the close packed structure [for example, for the structures of triangle and tetrahedron, $C_{r}(3)=C_{r}(4)=2 \pi^{2} / 3, \ C_{v}(3)$ $=(4 / 3) \sqrt{2 / 3}, \ C_{v}(4)=\sqrt{2}$, respectively].

Consider the opposite limiting case (high temperatures). By definition of a cluster, the existence of a bond between two atoms means that their interaction potential is nonzero. We will call a virtual chain any subset of cluster atoms, which may be numbered so that each $i$th atom, but for the first and the last ones, is bonded only to the $(i-1)$th and $(i+1)$th atoms pertaining to this chain (and, possibly, to other atoms pertaining to other chains). The first atom has a bond with the second one in this chain; the last one, with the next to last. By definition, the ringlike configuration is no virtual chain. An atom is called the branching point if it is connected not only with the atoms pertaining to the same chain but at least with one more atom pertaining to another chain. A new chain emerges if a bond is added to the atom, which is neither the first nor the last one in some chain. It is easily verified that a cluster with the minimum number of bonds is a set of virtual chains connected by single bonds at the branching points; all chains but one have one free end. Obviously, the cluster containing $g$ atoms has $g-1$ bonds.

Assume that the probability of states with the number of bonds greater than the minimum one is negligibly small. In contrast to the polymeric molecule, which consists of a real chain, the number of atoms and their ordering vary in virtual chains. This is a consequence of the additivity of interatomic potential. The above-mentioned assumption imposes geometrical restrictions on the region of the phase space, which may be occupied by cluster atoms. We will number the atoms in the following way. Choose the virtual chain with two free ends and number the atoms pertaining to the latter from one end to the other, $1,2,..., l_{1}$. Then choose one of the branching points from the first virtual chain and assign the number $l_{1}+1$ to the atom of the second chain bonded to this point. Continue the numeration until free end of the second chain is reached; its number will be $l_{1}+l_{2}$. Then, choose another branching point, etc. As a result, we obtain $L$ virtual chains with $l_{j}$ atoms in the $j$th chain, $\sum_{j=1}^{L} l_{j}=g$.

In the virtual chains approximation, the potential energy of a cluster is written in the form
$$
\begin{aligned}
U_{c}= & \sum_{i=1}^{l_{1}-1} u\left(r_{i+1 i}\right)+u\left(r_{l_{1}+1 l_{1}}\right)+\sum_{i=l_{1}+1}^{l_{1}+l_{2}-1} u\left(r_{i+1 i}\right) \\
& +\cdots+\sum_{i=g-l_{L}+1}^{g-1} u\left(r_{i+1 i}\right),
\end{aligned} \tag{3}
$$
where $r_{i+1 i}=|\mathbf{r}_{i+1}-\mathbf{r}_{i}|$ is the bond length; $\mathbf{r}_{i}$ , the coordinate of the $i$th atom. The partition function of a cluster is
$$
Z_{c}^{(g)}=\chi^{-3 g} \int \ldots \int^{\prime} \exp \left[-\frac{U_{c}}{k_{B} T}\right] d \mathbf{r}_{1} \cdots d \mathbf{r}_{g}, \tag{4}
$$
the integral with the prime means that the integration is performed over the phase space region, where only physically different states are realized. To calculate (4) in the virtual chains approximation, substitute the variables,
$$
\begin{aligned}
& \mathbf{q}_{1}=\mathbf{r}_{1}, \\
& \mathbf{q}_{2}=\mathbf{r}_{2}-\mathbf{r}_{1}, \\
& \cdots \\
& \mathbf{q}_{l_{1}+1}=\mathbf{r}_{l_{1}+1}-\mathbf{r}_{b_{1}}, \\
& \mathbf{q}_{l_{1}+2}=\mathbf{r}_{l_{1}+2}-\mathbf{r}_{l_{1}+1}, \\
& \cdots \\
& \mathbf{q}_{g}=\mathbf{r}_{g}-\mathbf{r}_{g-1},
\end{aligned} \tag{5}
$$
where $\mathbf{r}_{b_{1}}$ is the radius of the first branching point. An inverse transform has the form
$$
\begin{aligned}
& \mathbf{r}_{1}=\mathbf{q}_{1}, \\
& \mathbf{r}_{2}=\mathbf{q}_{1}+\mathbf{q}_{2}, \\
& \cdots \\
& \mathbf{r}_{l_{1}+1}=\mathbf{r}_{b_{1}}+\mathbf{q}_{l_{1}+1}, \\
& \mathbf{r}_{l_{1}+2}=\mathbf{r}_{b_{1}}+\mathbf{q}_{l_{1}+1}+\mathbf{q}_{l_{1}+2}, \\
& \cdots \\
& \mathbf{r}_{g}=\mathbf{r}_{b_{L}-1}+\mathbf{q}_{g-l_{L}+1}+\cdots+\mathbf{q}_{g},
\end{aligned} \tag{6}
$$

![](./images/812671666806063105_3.jpg)

It is seen from (6) that the Jacobian of this transform is the determinant of a triangle matrix, whose diagonal elements are equal to unity, therefore, the Jacobian proper is equal to unity. Upon substitution, partition function (4) is expressed in terms of the partition function of a dimer $Z_{c}^{(2)}$,
$$
\begin{aligned}
Z_{c}^{(g)} & =\frac{V}{\chi^{3 g}} \int \ldots \int \prod_{i=1}^{g-1} \exp \left[-\frac{u\left(q_{i}\right)}{k_{B} T}\right] d \mathbf{q}_{1} \cdots d \mathbf{q}_{g-1} \\
& =\frac{V}{\chi^{3 g}}\left\{\int^{\prime} \exp \left[-\frac{u\left(q_{1}\right)}{k_{B} T}\right] d \mathbf{q}_{1}\right\}^{g-1}=\frac{V}{\chi^{3}}\left[Z_{c}^{(2)}\right]^{g-1}.
\end{aligned}
$$

In particular case of the absence of branching points, Eq. (7) is similar to the partition function of a macromolecule in the standard Gauss model of a polymeric chain. $^{13}$ It follows from Eq. (7) that the average potential energy of a cluster $U_{g}$ depends linearly on its size,
$$U_{g}=\left\langle U_{c}\right\rangle=(g-1) U_{2},\qquad(8)$$
where $U_{2}$ is the average potential energy of a dimer at the same temperature.

Relations (2) and (7) define the ratio of probabilities to have the structure with the minimum $P_{\min }$ or maximum $P_{\max }$ number of bonds,
$$
\begin{aligned}
\frac{P_{\min }}{P_{\max }} & =\frac{\left[Z_{c}^{(2)}\right]^{g-1}}{Z_{r}^{(g)} Z_{v}^{(g)}} \exp \left(-\frac{\Delta E_{g}}{k_{B} T}\right) \\
& =\frac{\pi^{g-1}}{C_{r} C_{v}}\left(\frac{a}{r_{0}}\right)^{2 g-5}\left(\frac{2 D_{0}}{\pi k_{B} T}\right)^{g-2.5} \exp \left(-\frac{\Delta E_{g}}{k_{B} T}\right), \quad(9)
\end{aligned}
$$
where $\Delta E_{g}=D_{g}-(g-1) D_{0}$, and the estimate $Z_{c}^{(2)}$ $\cong Z_{r}^{(2)} Z_{v}^{(2)}=\pi(a / \chi)^{2}\left(k_{B} T / \hbar \omega_{0}\right)$ was used. Since $a \gg r_{0}$, the pre-exponential factor on the right-hand side of Eq. (9) is big. However, at low temperatures, the exponent is small, and $P_{\min }<P_{\max }$. The exponent increases sharply as the temperature is increased, and the latter inequality may turn into $P_{\min }>P_{\max }$. Assume that $P_{\min }=P_{\max }$, i.e., the right-hand side of Eq. (9) is equal to unity, at some $T=T_{0}$, which will be referred to as the characteristic structural transition temperature. Then a transcendental equation with respect to $T_{0}$ follows from Eq. (9). It can be written in the form
$$
\ln \frac{a}{r_{0}}+\frac{1}{2} \ln \frac{2 D_{0}}{\pi k_{B} T_{0}}+(2 g-5)^{-1} \ln \frac{\pi^{g-1}}{C_{r} C_{v}}=\frac{\Delta E_{g}}{(2 g-5) k_{B} T_{0}}.
$$

For typical values of parameters, the second and third terms on the left-hand side of Eq. (10) are of the order of unity, and the first term is greater than unity by definition of the short-range potential. The dependence of the energy difference $\Delta E_{g}$ on cluster size is caused by the size dependence of the number of nearest neighbors in a cluster; the larger the cluster, the greater the number. Thus, for a macroscopic crystal of atoms interacting via the short-range potential $D_{g}$ $=6 D_{0},{ }^{14}$ therefore, $\Delta E_{g} /(2 g-5) \rightarrow 2.5 D_{0}$ at $g \rightarrow \infty$. Then it can be easily shown that in the case of extremely large clusters $P_{\min } / P_{\max }<1$ at $a / r_{0} \sim 10$ and temperatures below the critical one. This means that the structure of a large cluster is close to that of the spherical liquid droplet. On the contrary, for the short-range potential (1) the energy difference $\Delta E_{g}$ is noticeably lower for smallest clusters. For $g$ $=3$ and 4, the cluster has three and six bonds, respectively. Further addition of an atom to the cluster increases the number of bonds by three until $g=8$. Therefore, $D_{g}=3 g-6$ for $3 \leqslant g \leqslant 8$. Hence, $\Delta E_{g} /(2 g-5)=D_{0}$, and an appropriate solution of Eq. (10) does exist. In fact, with $D_{g}=3 g-6$, Eq. (10) can be represented in the form
$$
\frac{1}{T_{0}^{*}} \exp \left(-\frac{2}{T_{0}^{*}}\right)=\frac{\pi}{2}\left(\frac{C_{r} C_{v}}{\pi}\right)^{(g-1) /(g-2.5)}\left(\frac{r_{0}}{a}\right)^{2}, \quad(11)
$$
where $T_{0}^{*}=k_{B} T_{0} / D_{0}$. For vibrations in the neighborhood of a bottom of the Lennard-Jones 12-6 potential, we have $a / r_{0}=6$, and it follows from Eq. (11) that for trimer $(g$ $=3$) $T_{0}^{*} \cong 0.434$. At $g=4$ (tetramer) $T_{0}^{*} \cong 0.416$, which is close to the transition temperature for trimer. The greater the parameter $a / r_{0}$, the lower the temperature $T_{0}^{*}$.

The pre-exponential factor $(1 / T^{*})^{g-2.5}(a / r_{0})^{2 g-5}(T^{*}$ $=k_{B} T / D_{0}$ ) in the right-hand side of Eq. (9) may be interpreted as follows. Since for potential (1) the amplitude of vibrations of atoms is of the order of $r_{0} \sqrt{T^{*}}$, and the average distance between them, of the order of $a$, the volume of phase space accessible for the motion of atoms in a cluster with $g-1$ bonds is proportional to $\left(a^{2} r_{0} \sqrt{T^{*}}\right)^{g-1}$. Thus, $Z_{c}^{(g)} \propto a^{2 g-2} r_{0}^{g-1}(T^{*})^{0.5 g-0.5}$. For a cluster with the close packed structure $Z_{r}^{(g)} \propto a^{3}, Z_{v}^{(g)} \propto r_{0}^{3 g-6}(T^{*})^{1.5 g-3}$ (a system of $g$ atoms has 3 rotational and $3 g-6$ vibrational degrees of freedom). Therefore, $Z_{c}^{(g)} /\left[Z_{r}^{(g)} Z_{v}^{(g)}\right] \propto\left(a / r_{0}\right)^{2 g-5}$ $\times(1 / T^{*})^{g-2.5}$. Thus, $P_{\min } / P_{\max }$ is greater than unity if the accessible phase space volume for the chainlike state is much greater than that for the close packed state, i.e., at sufficiently high temperature the chainlike state successfully competes with the close packed one.

Now consider the smallest clusters in transitional temperature region. In this region, at different instants the cluster finds itself in states with different numbers of bonds ranging from $g-1$ (the minimum number) to $3 g-6$ (the maximum number), i.e., it is in a "superposition" state. An exact calculation of the probability $P_{k}^{(g)}$ to find a $g$-atomic cluster in the state with $k$ bonds is very difficult. However, simple qualitative considerations make it possible to determine its form. If a bond is broken, the binding energy is decreased by

![](./images/812671666806063105_4.jpg)

FIG. 2. Probabilities to find a tetramer in states with certain number of bonds as the function of temperature. $T_{0}^{*} \cong 0.416$.

$D_{0}$ but the phase space volume accessible for the motion of cluster atoms is increased by the factor $a r_{0}^{2} /(r_{0}^{3} \sqrt{T^{*}})$ $=a /(r_{0} \sqrt{T^{*}})$. Therefore, it must be $P_{k}^{(g)} / P_{k-1}^{(g)}=(B_{k}^{(g)} /$ $B_{k-1}^{(g)})(r_{0} \sqrt{T^{*}} / a) e^{1 / T^{*}}$, where $B_{k}^{(g)}$ is some geometric factor. In addition, the ratio $P_{g-1}^{(g)} / P_{3 g-6}^{(g)}=P_{\min } / P_{\max }$ must satisfy the equality (9). Both conditions are met if $P_{k}^{(g)}$ $=B_{k}^{(g)} \eta^{3 g-6-k}$, where $\eta^{2}=(2 / \pi)(\pi / C_{r} C_{v})^{(g-1) /(g-2.5)}$ $\times(a / r_{0})^{2}(1 / T^{*}) e^{-2 / T^{*}}$. It follows from Eq. (11) that $(2 / \pi)$ $\times(\pi / C_{r} C_{v})^{(g-1) /(g-2.5)}(a / r_{0})^{2}=T_{0}^{*} \exp (2 / T_{0}^{*})$, therefore $\eta(T^{*})$ can be written in the form

$$
\eta\left(T^{*}\right)=\sqrt{\frac{T_{0}^{*}}{T^{*}}} \exp \left(\frac{1}{T_{0}^{*}}-\frac{1}{T^{*}}\right).\qquad(12)
$$

It follows from the low-temperature expansions of the average potential energies $U_{2} \cong D_{0}(T^{*}-1)$ and $U_{g} \cong(3 g$ $-6) D_{0}(T^{*}-1) \quad(2<g<9)$ that at $T^{*} \ll 1$ the quantity $U_{g}/(g-1)U_{2}$ is temperature independent and is uniquely defined by the number of bonds $k=3g-6$. At high temperatures, $U_{g}/(g-1)U_{2}=1$ [$k=g-1$, Eq. (8)]. Assume that this quantity is also temperature independent for all intermediate $k$ and that all the coefficients $B_{k}^{(g)}$ are independent of $k$. Then, in view of the normalization $\sum_{k=g-1}^{3g-6}P_{k}^{(g)}=1$, the average potential energy of the small gaslike cluster can be written in the form

$$
\frac{U_{g}}{(g-1) U_{2}}=\frac{\sum_{k=0}^{2 g-5}(3 g-6-k) \eta^{k}}{(g-1) \sum_{k=0}^{2 g-5} \eta^{k}}.\qquad(13)
$$

The probabilities to find a tetramer in states with different $k$ are shown in Fig. 2. As is seen, at low temperatures the state with $k=6$ dominates; at high temperatures, the state with $k$ $=3$. All probabilities are equal at $T^{*}=T_{0}^{*}$. The dependence (13) is shown in Fig. 3 for $g=5$ and 7. It is seen that treated transition is rather smooth and takes place in a wide temperature range.

![](./images/812671666806063105_5.jpg)

FIG. 3. Temperature dependence of the average potential energy for different cluster sizes. Calculations by formula (13) for $g=5$ ($T_{0}^{*}=0.380$) and 7 ($T_{0}^{*}=0.417$) are indicated by solid curves.

### III. THE INTERPOLATION FORMULA FOR ARBITRARY CLUSTER SIZE

It follows from Eq. (7) that any thermodynamic function of a small cluster, which is the linear functional of $\ln Z_{c}^{(g)}$, is proportional to $g-1$. This makes it possible to construct simple interpolation formulas for the size dependence of any extensive thermodynamic function. In what follows, we will consider the chemical potential and internal energy (the average potential energy) of the cluster.

Consider the chemical potential of cluster $\mu_{g}$ in the vapor, which is considered as an ideal mixture of atoms and clusters with different sizes. It follows from (7) that for small clusters

$$
\frac{\mu_{g}}{k_{B} T}=\ln N_{g}-\ln Z_{c}^{(g)}=\ln \left(n_{g} \lambda^{3}\right)+(g-1) \ln \left(K_{2} \lambda^{3}\right),\qquad(14)
$$

where $N_{g}$ is the number of clusters with the size $g$; $n_{g}$ $=N_{g}/V$, their concentration, and the notation

$$
K_{2}(T) \equiv \frac{n_{1}^{2}}{n_{2}}=\frac{1}{\lambda^{3} Z_{c}^{(2)}}\qquad(15)
$$

is used for the equilibrium constant of the reaction of dimer formation. Note that it follows from the mass action law for the reaction of cluster formation $\mu_{g}=g \mu_{1}$, where $\mu_{1}$ $=k_{B} T \ln (n_{1} \lambda^{3})$ is the chemical potential of an atom in the vapor, and from (14) that the equilibrium constant of the reaction of formation of $g$-atomic cluster is

$$
K_{g}(T)=K_{2}^{g-1}(T).\qquad(16)
$$

In the limit of macroscopic droplet ($g\rightarrow\infty$),

$$
\mu_{g}=k_{B} T \ln \left(n_{g} \lambda^{3}\right)+(g-1) \mu_{l},\qquad(17)
$$

where $\mu_{l}=k_{B} T \ln (n_{1s} \lambda^{3})$ is the chemical potential of an atom in bulk liquid; $n_{1s}$ is the number density of atoms in saturated vapor. Relationships (14) and (17) may be combined by the linear interpolation

$$
\begin{aligned}
\mu_{g}= & k_{B} T \ln \left(n_{g} \lambda^{3}\right)+\left(g_{0}-1\right)\left[k_{B} T \ln \left(K_{2} \lambda^{3}\right)-\mu_{l}\right] \\
& +(g-1) \mu_{l},
\end{aligned}\qquad(18)
$$

where $g_0$ is the number of atoms on cluster surface; $g$, the total number of atoms. At $g<9$, all cluster atoms appear to be the surface ones, $g_0=g$, and Eq. (18) is transformed to (14). Since $g_0 \propto g^{2/3}$ at $g \to \infty$, the asymptote (17) is obtained from (18).

Relation (18) was proposed in Ref. 15 as a basis for the thermodynamic nucleation theory. It assumes that the surface energy is proportional to the number of the surface molecules rather than to the surface area. From Eq. (18) and the mass action law $\mu_g=g\mu_1$, the equilibrium distribution of clusters over sizes can be deduced,
$$
\begin{aligned}
&n_g=n_1 \exp\left(-\frac{\Delta \Phi_g}{k_B T}\right), \\
&\Delta \Phi_g=(g_0-1)k_B T \ln\left(\frac{K_2}{n_{1s}}\right)-(g-1)k_B T \ln S,
\end{aligned} \tag{19}
$$
where $S=n_1/n_{1s}$ is the supersaturation ratio. Equations (18) and (19) include the quantities $g$ and $g_0$. A relation between them is based on the model$^{15}$ of a core of the inner molecules surrounded by surface molecules,
$$g_0=3\omega(g-g_0)^{2/3}+3\omega\lambda(g-g_0)^{1/3}+\omega\lambda^2, \tag{20}$$
where
$$\omega=\frac{4\pi}{3}\frac{\sigma_f r_l^2}{k_B T \ln(K_2/n_{1s})} \cong 0.8, \tag{21}$$
$\lambda=\sqrt{z/\omega-3/4}-3/2$; $z$ is the coordination number in bulk liquid; $\sigma_f$, the surface tension of flat surface; $r_l$$=(3/4\pi n_l)^{1/3}$, $n_l$ is the molecule number density in bulk liquid.

It is convenient to introduce the effective surface tension coefficient $\sigma_\mu(R_g)$, where $R_g=r_l g^{1/3}$ is the equimolar radius. Substituting the first term in the right-hand side of (19) by $4\pi\sigma_\mu(g)R_g^2$ and using (21) we obtain$^{15}$
$$\sigma_\mu(g)=\sigma_f \gamma(g), \quad \gamma(g)=\frac{1}{3\omega g^{2/3}}[g_0(g)-1]. \tag{22}$$

Note that the effective surface tension coefficient $\sigma_\mu(g)$ is not a "true" surface tension, because it is incompatible with its conventional definition.$^{16}$ However, the function $\sigma_\mu(g)$ is convenient for the description of size effects.

Now consider the potential energy. Similar to (18), we may write
$$U_g=A_1(T)g_0(g)+A_2(T)g+A_3(T), \tag{23}$$
where $A_1$, $A_2$, and $A_3$ are the temperature functions to be found. If we introduce the potential energy of a molecule in bulk liquid $\bar{u}$, we find that $A_2(T)=\bar{u}$. Note that for the pair additive potential,
$$\bar{u}=\frac{1}{2}\lim_{g \to \infty}\left[\sum_{j=1}^{i_0-1} u(r_{i_0^j})+\sum_{j=i_0+1}^g u(r_{i_0^j})\right], \tag{24}$$
where $i_0$ indicates the "central" atom, which is the closest one to cluster center of mass. The functions $A_1(T)$ and $A_3(T)$ are found using two conditions, at $g_0=g=2$, the right-hand side of (23) is equal to $U_2$; at $g=1$, it is equal to zero. Consequently, $A_1(T)=U_2-\bar{u}$, $A_3(T)=-U_2$, and (23) may be written in the same form as (18),
$$U_g=(g_0-1)(U_2-\bar{u})+(g-1)\bar{u}. \tag{25}$$

At $g \to \infty$, a definition of the quantity $\Omega$ similar to (21) follows from Eq. (20), where $\Omega$ is substituted for $\omega$, and from Eq. (25),
$$\Omega=\frac{4\pi}{3}\frac{\sigma_0 r_l^2}{U_2-\bar{u}}, \quad \sigma_0=\sigma_f-T\frac{d\sigma_f}{dT}. \tag{26}$$

Although $\omega$ and $\Omega$ are different quantities, their values appear to be close (see below).

With due regard for Eqs. (20) and (25), rewrite Eq. (25) in the form typical for the liquid drop model,
$$
\begin{aligned}
&U_g=4\pi\sigma(g)R_g^2+(g-1)\bar{u}; \quad \sigma(g)=\sigma_0 \Gamma(g), \\
&\Gamma(g)=\frac{1}{3\Omega g^{2/3}}[g_0(g)-1].
\end{aligned} \tag{27}
$$

Thus, the surface energy $4\pi\sigma(g)R_g^2$ is equal to the difference between the potential energy of cluster and the interaction energy of its atoms in bulk liquid, and
$$\sigma(g)=\frac{1}{(36\pi)^{1/3}}\left(\frac{n_l}{g}\right)^{2/3}\left[U_g-(g-1)\bar{u}\right]. \tag{28}$$

Relationships similar to Eqs. (18) and (25) may be deduced for other extensive thermodynamic functions of the cluster as well. They are the consequences of the assumption that cluster is a set of virtual chains at $g \leqslant z$ and a core of inner atoms surrounded by the layer of surface atoms at $g>z$.

## IV. MOLECULAR DYNAMICS SIMULATION OF THE STRUCTURAL TRANSITION

To investigate the structure of small clusters, it is convenient to define a simple virtual chain. By definition, the subset of atoms forms a simple virtual chain if there is a way to enumerate them in such a way that the nearest neighbors for each $i$th atom are the $(i-1)$th and $(i+1)$th ones, and the first and last ones have only one neighbor at the distance not larger than $r_b$. In the ringlike configurations, we will assign the first and last numbers to the atoms, whose separation is the greatest. The definition introduced above may be used for arbitrary potential. Similar to Eq. (3), one may define the potential energy of a set of simple virtual chains as $U_{\text{sc}}$$=\langle\sum_i u(r_{i+1i})\rangle$, where only the interactions of each atom with the two nearest neighbors are taken into account; the interactions between ends of simple virtual chains are ignored.

Another important parameter defining the structure is the average sum $U_{\text{min}}$ of $g-1$ least energies of pair interactions (their total number is $g(g-1)/2$). $U_{\text{sc}}$ and $U_{\text{min}}$ are the upper and lower estimates of $\langle U_c\rangle$, respectively, provided that the cluster may be treated as a set of virtual chains. Obviously, if the cluster consists of a single chain, $U_{\text{sc}}$ and $U_{\text{min}}$ are close to the total energy of cluster $U_g$, and the quantity $U_g/(g-1)U_2$, to unity.

The following realistic short-range interatomic potential was used in the simulation,
$$
u(r)=
\begin{cases}
v(r)+v(2r_c - r)-2v(r_c), & r\leqslant r_c, \\
0, & r>r_c,
\end{cases} \tag{29}
$$
where $v(r)=D_0[(a/r)^{12}-2(a/r)^6]$. The shapes of potentials $u(r)$ and $v(r)$ differ only in the neighborhood of the point $r=r_c$ even for relatively low cutoff radius $r_c$, but $u(r)$ is shifted upward relative to $v(r)$. The value $r_c=1.6\ a$ was selected for the investigation of cluster structure. This value is greater than the mean interatomic distance but is less than the doubled distance. Since thermodynamic properties of the argonlike system are much more sensitive to the value of the cutoff radius for the Lennard-Jones 12-6 potential,¹⁷ the latter is not a short-range one. At relatively short cutoff, it is possible to compare simulation results with analytical estimates of Sec. II.

MD simulation was performed using the $(P,T)$-ensemble method described in Ref. 9. Evolution of clusters was investigated at different temperatures of the Berendsen thermostat¹⁸ $T^*$. The equation of motion for the $j$th atom has the form
$$
\begin{align*}
\ddot{\mathbf{r}}_j&=\frac{1}{2\tau_0^2}\sum_{i\neq j}\left[\left(\frac{a}{r_{ij}}\right)^{14}-\left(\frac{a}{r_{ij}}\right)^8\right](\mathbf{r}_j-\mathbf{r}_i) \\
&+\frac{1}{\tau_f}\left[\left(\frac{T^*}{T_a^*}\right)^{1/2}-1\right]\dot{\mathbf{r}}_j,
\end{align*} \tag{30}
$$
where $\tau_0=(a/2^{1/6})\sqrt{M/24D_0}$ is the MD time scale; $\tau_f$, the temperature relaxation time. As is known, when using the Berendsen method, energy transfer from internal to rotational and translation degrees of freedom takes place. However, in the system under consideration, this effect is small due to the interaction between cluster and vapor atoms. In addition, to make the determination of cluster temperature precise enough, the temperature was defined in the center-of-mass system of a cluster as follows:
$$
T_a^*=\frac{M}{3D_0(g-1)}\sum_{j=1}^g(\mathbf{v}_j-\mathbf{v}_{\mathrm{cm}})^2, \tag{31}
$$
where $\mathbf{v}_{\mathrm{cm}}$ is the velocity of cluster center of mass. The radius of a spherical cell was equal to 10; at $T^*\geqslant0.419$, the number of vapor atoms in the cell was about 40–50. Under these conditions, initial cluster size $g\leqslant460$ was decreased as a result of evaporation of atoms from cluster surface. The values of investigated quantities were sampled with time intervals of $\tau_0/2$, stored, and averaged. The runs for given temperature were repeated until the size of error bars for measured quantity were of the same order as the size of data point labels in Figs. 3–5. This typically required less than $10^5\tau_0$ of the total simulation time for each size $g$.

The $(P,T)$-ensemble method⁹ was modified for the low-temperature case. Since cluster evaporation rate is small at $T^*<0.4$, no vapor atoms were generated at the boundary of the cell. Otherwise, this would result in a rapid growth of the cluster. For this case, the cluster in a carrier gas was simulated. Carrier gas atoms were assumed to interact between each other and cluster atoms via the potential $0.1u(r)$ [$u(r)$ is defined by Eq. (29)]. The procedure of generation of such atoms was the same as for vapor atoms. During all runs, no adsorption of carrier gas atoms on the cluster surface was observed, and these atoms played the role of a heat bath. Since no evaporation (condensation) events occurred, and fluctuations of cluster temperature were not so high as in the high-temperature case, the interaction with the Berendsen thermostat was not required $(\tau_f=\infty)$.

![](./images/812671666806063105_6.jpg)

FIG. 4. Difference between the potential energies of the cluster calculated in different approximations; $T^*=0.71$.

In the case of low temperatures, simulation proceeded as follows. First, the cluster with the temperature above that of the thermostat was initialized in the empty cell. Then, cluster temperature was slowly decreased by applying a weak friction force to all cluster atoms. If the binding energy of the cluster generated in such a way was above the ground state energy, i.e., the cluster with metastable structure was generated, the run was ignored. As soon as the temperature reached that of a thermostat, the generation of carrier gas began. After the time of $500\tau_0$, investigated data were re-

![](./images/812671666806063105_7.jpg)

FIG. 5. Size dependence of the potential energy of the cluster calculated in different approximations; $T^*=0.71$.

corded and averaged. For each size g, an appropriate accu-racy was attained for the total simulation time of about 3 $\times 10^{5} \tau_{0}$ .

To check the simulated system for equilibrium, two cri-teria were applied; cluster temperature (31) must be equal to that of a thermostat; the potential energy of a dimer deter-mined from the simulation must be equal to that cal-culated by the formula $U_{2}=(\int_{0}^{r_{b}} r^{2} u(r) e^{-u(r) / k_{B} T} d r)$  $\times(\int_{0}^{r_{b}} r^{2} e^{-u(r) / k_{B} T} d r)^{-1}$ . Both criteria fail at the temperature T>0.21, at which cluster evaporation emerges. No simula-tion was performed in the region 0.21<T<0.42.

## V. SIMULATION RESULTS AND DISCUSSION

The temperature dependence of the average potential en-ergy $U_{g}$ is shown in Fig. 3. It is seen that a sharp decrease of the ratio $U_{g} /(g-1) U_{2}$ occurs in the temperature interval 0.2<T*<0.5. Whereas at g≥10 this ratio is noticeably greater than unity even at high temperatures, it decreases down to unity at g<10. This confirms the relation (8) ob-tained in the virtual chains approximation. Simulation data are compared with the calculations by formula (13), in which $T_{0}^{*}$ is treated as an adjustable parameter. For g=3 and 4 (not shown in Fig. 3) the values of $T_{0}^{*}=0.340$ and 0.350, respec tively, provide the best fit. The ratios of these values to the depth of potential (29) used in the simulation, which is equal to $0.789 D_{0}$ , are 0.431 and 0.444 . Thus, a good agreement between numerical simulation and the estimates of Sec. II (0.434 and 0.416) takes place. For g=5 and 7 the best fit values of $T_{0}^{*}$ are equal to 0.380 and 0.417 , respectively. Ap parently, the dependence $T_{0}^{*}(g)$ is a consequence of the as sumption that $B_{k}^{(g)}$ is k-independent and of the presence of a short tail in the potential (29), which is absent for the model short-range potential (1).

As was mentioned in the foregoing, the structural tran-sition is a consequence of the competition between entropy and binding energy. In general, this phenomenon is de-scribed by the same physics as the coil-globule transition of a polymer molecule. It is interesting to note that, according to the recent study, $^{19}$ similar transition takes place in the gas-liquid nucleation of polar fluids. Chainlike clusters are formed for cluster sizes g≤30. However, strong interaction between dipoles, which causes their alignment, seems to fa-vor "polymerization." This study is the evidence for the fact that neither polymerization, nor some other characteristic features of the interaction potential are responsible for the structural transition; instead, it is the pure effect of the en-tropy.

Figure 4 illustrates the error involved in the substitution of $U_{sc}$ or $U_{min}$ for $U_{g}$ at high temperature. It is seen that $(U_{sc}-U_{g}) / k_{B} T ≤1.4$ and $(U_{min}-U_{g}) / k_{B} T ≤0.5$ at g<8, i.e., one may substitute the approximate potential energy $U_{c}$ for the true one. Note that $U_{sc}$ is close to $U_{min}$ at g<10. This points to the fact that the probability of states with a single virtual chain is high. In contrast, at big $g,(U_{s c}-U_{g}) / k_{B} T$ ≥1, which is the evidence of transition to the close packed structure. For comparison, Fig. 4 shows the size dependence of the difference $(U_{g}-U_{p}) / k_{B} T$ , where $U_{p}$ =U₂(T)U₈(0)/U₂(0) is the potential energy of a cluster with the close packed structure, and the number of bonds was estimated as $U_{g}(0) / U_{2}(0)$ (dots $\epsilon=U_{g}-U_{p}$ ). $U_{p}$ is also the estimate of interaction energy between atoms in the macroscopic droplet. It is seen that the liquid drop model is inappropriate for small clusters. Thus, the average potential energy of a small cluster is much closer to the energy of a set of virtual chains than to the energy of the macroscopic drop-let. This is another argument in favor of the virtual chains model.

Figure 5 shows the ratios of the potential energy calcu-lated in different approximations to the energy of a set of virtual chains $(g-1) U_{2}$ as the function of cluster size. At small g, these ratios are close to unity (curves $V_{g}=U_{sc}, V_{g}$  $=U_{min }$ , and $V_{g}=U_{g}$ ), while the energy of close packed cluster is much different from $U_{g}$ (curve $V_{g}=U_{p}$ ). Calcula tion shows that $U_{g}$ approaches $U_{p}$ at $g 10^{2}$ , which is re lated to the transition to the close packed structure.

![](./images/812671666806063105_8.jpg)

FIG. 6. Typical configurations of clusters with the chainlike structure. Two configurations contain a single branching point each; the other, no branching points.

Typical cluster configurations with no more than one branching point observed in the numerical experiment are shown in Fig. 6. The average number of bonds in simple virtual chains $N_{c}$ is independent of cluster size at large g, but it increases sharply at g<20 as g decreases and reaches maximum at g=7. Then $N_{c}$ is close to g-1 (Fig. 7). This means that the probability of states with a single simple vir-tual chain is high at small g. Figure 8 is also indicative of this fact. It is seen that these states dominate for small clus-ters at high temperature, and they are practically absent al-ready at g>9. $P_{1}^{(3)}$ and $P_{1}^{(4)}$ appear to be close, which cor relates with the estimates of Sec. II. This is in a good agreement with simulation results of study, $^{20}$ where it was found by visual inspection that clusters consisting of 10-25 particles are already quite spherical (in terms of this work, they have a spherical core).

Figure 9 shows the radial distribution function for the "central" atom of the cluster G(r). To determine G(r), the number of atoms S(r) at the distance less than r from the central atom was tabulated. In so doing, G(r) $=(4 \pi n_{l} r^{2})^{-1}(d S / d r)$ . The number density of atoms in the center of cluster was defined as $n_{l}=< 3 S / 4 \pi r^{3}>$ , where aver aging was performed over three coordination spheres. Note the following peculiarities of G(r). For the large cluster (g =430), G(r) has the same shape as for bulk liquid with

![](./images/812671666806063105_9.jpg)

FIG. 7. Average number of bonds in simple virtual chains as the function of cluster size; $T^{*}=0.71$.

maxima related to three coordination spheres around an atom. At $g=60$, the size effect emerges; the third maximum disappears, while the heights of two first maxima decrease; their positions are somewhat shifted toward smaller sizes. At $g<18$, a plateau emerges, which is indicative of the rapid decay of correlations between coordinates of atoms. At the same time, the number of atoms in the first coordination sphere decreases sharply. For example, it is equal to 2.46 at $g=6$. This regularity may be accounted for by the onset of virtual chains, in which each atom correlates only with two nearest neighbors. This phenomenon is similar to the correlation decay in the free Gauss chain. $^{13}$ A comparison of the distribution functions shown in Fig. 9 with those determined in a real experiment may be of interest.

Figure 10 shows the results of the calculation of $\sigma$. These data were obtained as follows. First, $\sigma$ was calculated straightforwardly by the values of $U_{g}$ obtained during MD simulation [formula (28)]. The asymptotic value $\bar{u}$ $=3.264D_{0}$ was reached already at $g>120$; the value $n_{l}$ $=0.544a^{-3}$ was obtained for the concentration of atoms in the center of the cluster. It is seen in Fig. 10 that the asymptotic value $\sigma_{0}=0.904D_{0}/a^{2}$ is practically reached at $g>400$.

![](./images/812671666806063105_10.jpg)

FIG. 8. Probability of the state with a single simple virtual chain as the function of cluster size. MD simulation, $T^{*}=0.71$.

![](./images/812671666806063105_11.jpg)

FIG. 9. Radial distribution function for the "central" atoms for different cluster sizes. $T^{*}=0.46$; $r^{*}=2^{1/6}r/a$; cluster sizes are indicated on the right-hand side.

Since the configuration with a single virtual chain is impossible for the clusters with $g>9$ (Fig. 8), such clusters have a core. According to the discussion in Sec. III, we set $z=9$. With these values, the coefficient $\sigma=\Gamma\sigma_{0}$ was calculated by formula (27), the parameter $\Omega$ (26) being adjusted to fit the numerical experiment. The best fit value $\Omega=0.794$ is in a good agreement with the thermodynamic model. $^{15}$ The curve in Fig. 10 matches the numerical data well, which confirms the validity of interpolation formula (25) as well as of the model assumptions made in Sec. III.

![](./images/812671666806063105_12.jpg)

FIG. 10. Function $\sigma(g)$ at $T^{*}=0.46$. Curve indicates the calculation by formula (27); dots, the values of $\sigma$ related to the potential energy of the cluster determined in the numerical experiment [formula (28)].

The model short-range potential (29) was chosen so that the comparison between numerical and analytical results would be possible. At the same time, no quantitative change in the results of simulation was observed for the case of $r_c$ $=\infty$. In particular, chainlike configurations like those shown in Fig. 6 were also observed for $g<9$; formula (25) is still in a good agreement with numerical data on the surface energy. Apparently, the structural transition takes place not only for the interaction potential with a short cutoff.

## VI. CONCLUSIONS

At relatively high temperatures, small clusters behave unlike microdroplets. Three cluster size ranges should be dis- tinguished; $2 \leqslant g<10$, $10 \leqslant g \leqslant 300$, and $g>300$. In the first one, clusters are the sets of virtual chains; in the third one, they acquire the properties of macroscopic droplets; the sec- ond range is transitional. The transition from the chainlike to close packed structure as the temperature decreases or as the cluster grows is a consequence of the competition between states with high binding energy but low statistical weight and those with lower binding energy but high statistical weight. The structural transition was discovered in MD simulation for the $(P,T)$-ensemble. The interpolation formulas pro- posed for thermodynamic functions of clusters in a wide range of their sizes validate the thermodynamic model $^{15}$ and can be used for the interpretation of simulation data.

## ACKNOWLEDGMENTS

The work was supported by the Alexander von Hum- boldt Foundation and the Russian Foundation for Basic Re- search, Grant No. 96-15-96462.

$^{1}$ R. Becker and W. Döring, Ann. Phys. (Germany) 24, 719 (1935).
$^{2}$ M. Volmer, Kinetik der Phasenbildung (Theodor Steinkopff, Dresden, 1939).
$^{3}$ J. Frenkel, Kinetic Theory of Liquids (Dover, New York, 1955).
$^{4}$ Ya. B. Zeldovich, Zh. Eksp. Teor. Fiz. 12, 525 (1942).
$^{5}$ H. Reiss, A. Tabazadeh, and J. J. Talbot, J. Chem. Phys. 92, 1266 (1990).
$^{6}$ H. M. Ellerly and H. J. Reiss, J. Chem. Phys. 97, 5766 (1992).
$^{7}$ C. L. Weakliem and H. Reiss, J. Chem. Phys. 101, 2398 (1994).
$^{8}$ R. S. Dumont, S. Jain, and A. G. Basile, J. Chem. Phys. 102, 4227 (1995).
$^{9}$ D. I. Zhukhovitskii, J. Chem. Phys. 103, 9401 (1995).
$^{10}$ F. P. Buff, J. Chem. Phys. 23, 419 (1955).
$^{11}$ A. Dillmann and G. E. A. Meyer, J. Chem. Phys. 94, 3872 (1991).
$^{12}$ M. R. Hoare and P. Pal, Adv. Phys. 24, 645 (1975).
$^{13}$ A. Yu. Grossberg and A. R. Khokhlov, Statistical Physics of Macromol- ecules (Nauka, Moscow, 1989).
$^{14}$ B. M. Smirnov, Usp. Fiz. Nauk 162, 97 (1992).
$^{15}$ D. I. Zhukhovitskii, J. Chem. Phys. 101, 5076 (1994).
$^{16}$ J. S. Rowlinson and B. Widom, Molecular Theory of Capillarity (Claren- don, Oxford, 1982).
$^{17}$ M. J. P. Nijmeijer, A. F. Bakker, C. Bruin, and J. H. Sikkenk, J. Chem. Phys. 89, 3789 (1988).
$^{18}$ H. J. C. Berendsen, J. P. M. Postma, W. F. van Gunsteren, A. DiNola, and J. R. Haak, J. Chem. Phys. 81, 3684 (1984).
$^{19}$ P. R. ten Wolde, D. W. Oxtoby, and D. Frenkel, Phys. Rev. Lett. 81, 3695 (1998).
$^{20}$ P. R. ten Wolde and D. Frenkel, J. Chem. Phys. 109, 9901 (1998).