# The $t$-$J$ model of hard-core bosons in slave-particle representation and its Monte-Carlo simulations

Yuki Nakano¹, Takumi Ishima², Naohiro Kobayashi²,
Kazuhiko Sakakibara³, Ikuo Ichinose², Tetsuo Matsui¹

¹Department of Physics, Kinki University, Higashi-Osaka, Japan
²Department of Applied Physics, Nagoya Institute of Technology, Nagoya, Japan
³Department of Physics, Nara National College of Technology, Yamatokohriyama, Japan

E-mail: yuki@phys.kindai.ac.jp

**Abstract.** We study the system of hard-core bosons (HCB) with two species in the three-dimensional lattice at finite temperatures. In the strong-correlation limit, the system becomes the bosonic $t$-$J$ model, that is, the $t$-$J$ model of "bosonic electrons". The bosonic "electron" operator $B_{x\sigma}$ at the site $x$ with a two-component spin $\sigma(=1,2)$ is treated as a HCB operator, and represented by a composite of two slave particles; a spinon described by a Schwinger boson (CP¹ boson) $z_{x\sigma}$ and a holon described by a HCB field $\phi_x$ as $B_{x\sigma} = \phi_x^\dagger z_{x\sigma}$. This $\phi_x$ is again represented by another CP¹ quasi-spinon operator $\omega_{xa}$ ($a=1,2$). The phase diagrams of the resulting double CP¹ system obtained by Monte Carlo simulations involve first-order and second-order phase boundaries. We present in detail the techniques and algorithm to reduce the hysteresis and locate the first-order transition points.

## 1. Introduction
Hard-core bosons represent particles with very strong repulsions, and their multiple occupancies are strictly prohibited. Such bosons appear, directly or indirectly, in various systems of physics, and study of them are of general interest. For example, the $t$-$J$ model of bosonic "electrons"[1, 2, 3, 4] is interesting because it is (i) a model[1, 2] of bosons in an optical lattice with strong repulsions and (ii) a model[3, 4] with close resemblance to the original $t$-$J$ model[5] of strongly correlated electrons, i.e., doped antiferromagnets.

To study the original $t$-$J$ model, the slave-particle picture is often used to deal with the constraint on the physical states faithfully[6, 7]. In this picture, an electron is viewed as a composite of a holon, spinless particle with a charge, and a spinon, chargeless particle with a spin. It may explain the charge-spin separation phenomena in terms of deconfinement phenomenon of gauge dynamics that appears naturally in the slave-particle picture[8].

In this paper we explain the bosonic $t$-$J$ model for the bosonic electrons in a slave-particle representation, which we introduced recently[4], and also discuss a new and simple algorithm to deal with first-order transitions.

In Sec.2 we review the model explaining the relation with the related models, and in Sec.3 we present some interesting results of its phase structure obtained by Monte-Carlo simulations. We discuss the algorithm to locate the first-order transition points. Section 4 is devoted for conclusion.

## 2. Model
### 2.1. The bosonic $t$-$J$ model
We consider the bosonic operator $B_{x\sigma}$ at the site $x$ with two species $\sigma = 1,2$. $B_{x\sigma}$ is the HCB operator satisfying
$$[B_{x\sigma},B_{y\sigma'}]=[B_{x\sigma}^{\dagger},B_{y\sigma'}]=0 \text{ for } x \neq y,\ B_{x\sigma}^{\dagger}B_{x\sigma}=0,1 \text{ for each } \sigma \text{ and } x,\ [B_{x1},B_{x2}]_{+}=0. \quad (1)$$

The Hamiltonian considered in [3, 4]is written as
$$
\begin{aligned}
H_{tJ} &=-t \sum_{x,\mu,\sigma}\left(\tilde{B}_{x+\mu,\sigma}^{\dagger} \tilde{B}_{x \sigma}+\text { H.c. }\right)+J \sum_{x, \mu}\left[\vec{\tilde{S}}_{x+\mu} \cdot \vec{\tilde{S}}_{x}-\frac{1}{4} \hat{n}_{x} \hat{n}_{x+\mu}\right], \\
\tilde{B}_{x \sigma} & \equiv\left(1-B_{x \bar{\sigma}}^{\dagger} B_{x \bar{\sigma}}\right) B_{x \sigma}, \quad \vec{\tilde{S}}_{x} \equiv \frac{1}{2} \sum_{\sigma, \sigma^{\prime}} B_{x \sigma}^{\dagger} \vec{\sigma}_{\sigma \sigma^{\prime}} B_{x \sigma^{\prime}}, \quad \hat{n}_{x} \equiv \sum_{\sigma} B_{x \sigma}^{\dagger} B_{x \sigma}.
\end{aligned}
\tag{2}
$$

### 2.2. Slave-particle representation
The bosonic $t$-$J$ model allows three physical states at each $x$, $|0\rangle,B_{x1}^{\dagger}|0\rangle,B_{x2}^{\dagger}|0\rangle$, while the double-occupancy $B_{x1}^{\dagger}B_{x2}^{\dagger}|0\rangle$ is excluded. The slave-particle representation of $B_{x\sigma}$ is suggested from the slave-fermion representation[7] of the electron operator $C_{x\sigma}=\psi_{x}^{\dagger}a_{x\sigma}$ where $\psi_{x}$ is the fermionic holon operator and $a_{x\sigma}$ is the bosonic spinon operator. In Ref.[7] the constraint for the physical space, $\psi_{x}^{\dagger}\psi_{x}+\sum_{\sigma}a_{x\sigma}^{\dagger}a_{x\sigma}=1$ is solved as $a_{x\sigma}=(1-\psi_{x}^{\dagger}\psi_{x})z_{x\sigma}$ where $z_{x\sigma}$ is the Schwinger boson ($\text{CP}^1$) operator satisfying $\sum_{\sigma}z_{x\sigma}^{\dagger}z_{x\sigma}=1$.

In fact, the expression of $B_{x\sigma}$ is obtained from $C_{x\sigma}=\psi_{x}^{\dagger}a_{x\sigma}$ by replacing $\psi_{x}$ by a HCB operator $\phi_{x}$ satisfying the standard relation for HCB,
$$\left[\phi_{x},\phi_{x}^{\dagger}\right]_{+}=1,\ \left[\phi_{x},\phi_{x}\right]_{+}=0,\ \left[\phi_{x},\phi_{y}^{\dagger}\right]=\left[\phi_{x},\phi_{y}\right]=0 \text{ for } x \neq y. \tag{3}$$

Then we get
$$B_{x \sigma}=\phi_{x}^{\dagger} a_{x \sigma}^{\prime}=\phi_{x}^{\dagger} z_{x \sigma}, \quad a_{x \sigma}^{\prime} \equiv\left(1-\phi_{x}^{\dagger} \phi_{x}\right) z_{x \sigma}, \tag{4}$$
where we used $(\phi_{x}^{\dagger})^2=0$. The HCB $\phi_{x}$ is rewritten by introducing yet another $\text{CP}^1$ operator, $w_{xa}$ as $\phi_{x}=w_{x2}^{\dagger}w_{x1}$. Then we arrive at the double $\text{CP}^1$ representation,
$$B_{x \sigma}=w_{x 1}^{\dagger} w_{x 2} z_{x \sigma}, \quad \sum_{\sigma=1,2} z_{x \sigma}^{\dagger} z_{x \sigma}=1, \quad \sum_{a=1,2} w_{x a}^{\dagger} w_{x a}=1. \tag{5}$$

In fact, the two physical states $w_{xa}^{\dagger}|v\rangle$ ($w_{xa}|v\rangle=0$) correspond to $w_{x1}^{\dagger}|v\rangle=\phi_{x}^{\dagger}|0\rangle,w_{x2}^{\dagger}|v\rangle=|0\rangle$.

### 2.3. Path integral for the partition function
Let us present the path-integral expression of the partition function $Z=\text{Tr}\exp(-\beta H)$ of the 3D model at finite $T$'s. We consider the region at sufficiently high $T$ and ignore the imaginary-time dependence of $z_{x\sigma}(\tau)$ and $w_{xa}(\tau)$ keeping only the zero modes. Then we have
$$
\begin{aligned}
Z &=\int \prod_{x}\left[d z_{x} d w_{x} \prod_{\mu} d U_{x \mu}\right] \exp \left(A-\mu_{c} \sum_{x} \bar{\phi}_{x} \phi_{x}\right), \quad A=A_{\mathrm{s}}+A_{\mathrm{h}}, \\
A_{\mathrm{s}} &=\frac{c_{1}}{2} \sum_{x, \mu, \sigma} P_{x} P_{x+\mu}\left(z_{x+\mu, \sigma}^{\star} U_{x \mu} z_{x \sigma}+\text { c.c. }\right), \quad A_{\mathrm{h}}=\frac{c_{3}}{2}\left[\sum_{x, \mu, \sigma} \bar{z}_{x+\mu, \sigma} z_{x \sigma} \phi_{x+\mu} \bar{\phi}_{x}+\text { c.c. }\right], \\
P_{x} & \equiv 1-\bar{\phi}_{x} \phi_{x}, \ z_{x 1}^{\star} \equiv z_{x 2},\ z_{x 2}^{\star} \equiv-z_{x 1},\ \phi_{x} \equiv \bar{w}_{x 2} w_{x 1},\ U_{x \mu} \equiv \exp \left(i \theta_{x \mu}\right), \\
\int d z_{x} &=\int_{-\infty}^{\infty} d^{2} z_{x 1} \int_{-\infty}^{\infty} d^{2} z_{x 2} \delta\left(\sum_{\sigma} \bar{z}_{x \sigma} z_{x \sigma}-1\right) \text { etc., } \int d U_{x \mu}=\int_{0}^{2 \pi} d \theta_{x \mu} /(2 \pi).
\end{aligned}
\tag{6}
$$


Following Ref.[3], we have introduced the U(1) gauge field $U_{x\mu} \equiv \exp(i\theta_{x\mu})$ on the link $(x,x+\mu)$ as an auxiliary field to make the action simpler and the U(1) gauge invariance manifest.

The term $-\mu_c \sum_x \bar{\phi}_x \phi_x$ with the (minus of) chemical potential $\mu_c$ has been introduced to control the hole density to a given constant $\delta$, $\delta = \rho(c_1,c_3,\mu_c) \equiv \frac{1}{N} \sum_x \langle \bar{\phi}_x \phi_x \rangle$ where $N = \sum_x 1$ is the total number of the sites. As indicated, $\rho(c_1,c_3,\mu_c)$ is a function of $c_1, c_3$ and $\mu_c$.

The parameters $c_1$ and $c_3$ are related with those in the original $t$-$J$ model as

$$
c_1 \sim \left\{
\begin{aligned}
J\beta \quad & \text{for} \quad c_1 >> 1, \\
(2J\beta)^{1/2} \quad & \text{for} \quad c_1 << 1,
\end{aligned}
\right. \quad c_3 \sim t\beta,
\tag{7}
$$

where the first relation concerning to $c_1$ is obtained by integrating over the gauge field $U_{x\mu}$[3].

### 2.4. Model I and Model II
Let us call the model defined by (6) Model I. $P_x$ of (6) is the projection operator to the hole-free states. To clarify the effect of $P_x$ in $A_s$ of (6), we introduce yet another model, Model II, which is obtained by replacing $P_x$ and $P_{x+\mu}$ in $A_s$ of (6) by unity, and compare the results of the two models. We expect that the antiferromagnetic (AF) ordered state appears with stronger signals in Model II than in Model I because the assignment $P_x = 1$ in Model II keeps the AF coupling between spin pairs at $(x,x+\mu)$ intact even if holes may exist at the sites $x$ and/or $x+\mu$.

## 3. Results
### 3.1. Phase diagram
Let us present the results of MC simulations. For MC simulations, we consider a 3D cubic lattice of the size $N \equiv L^3$ ($L$ up to 36) and imposed the periodic boundary condition. Fig.1 shows the phase structure of (a) Model I in the $c_3$-$c_1$ plane for a fixed chemical potential $\mu_c = 0$ ($\rho = 0.03 \sim 0.49$ for various phases), (b) Model II in the $c_3$-$c_1$ plane for $\delta = 0.5$, (c) Model II in the $\delta$-$1/c_1$ plane for $c_3/c_1 = 3.0$. There are totally four phases, which are characterized by electron correlation functions. $\langle \bar{B}_{x\sigma} B_{y\sigma} \rangle$ has a long-range orders (LRO) in a superfluidity (SF) phase. $\langle \vec{S}_x \vec{S}_y \rangle$ distinguishes AF phase by its staggered-order, ferromagnetic (FM) phase by its LRO, and paramagnetic (PM) phase by vanishing LRO.

Fig.1(b) shows there appear all the four phases in Model II. In contrast, Fig.1(a) shows that the AF+SF phase is missing in Model I. This fact at $\mu_c = 0$ [note $\mu_c = 0$ implies $\rho (= \delta) = 0.5$ in Model II] may be understood because $P_x$ counts the effects that holes break AF bonds and its presence suppresses the AF+SF phase. We have studied Model I for various values of $\mu_c$,

![](./images/813261297972936705_1.jpg)

Figure 1. Phase structure. (a) Model I in the $c_3$-$c_1$ plane at $\mu_c = 0$, (b) Model II in the $c_3$-$c_1$ plane at $\delta = 0.5$, (c) Model II in the $\delta$-$1/c_1$ plane for $c_3/c_1 = 3.0$. The phase boundary between AF and FM+SF phases in (a) is of first order and the remaining boundaries are of second order.

![](./images/813261297972936705_2.jpg)

Figure 2. Rules to select prechoice of variables (See Eq.(8)). There are two quasistable points $\rho_1$ and $\rho_2$ of the free energy $F$. (i) Metropolis algorithm has no preferred directions for next $\rho$. (ii) Improved algorithm has a preferred direction to mix the two regions near $\rho_1$ and $\rho_2$.

and found a bound $\rho \lesssim 0.18$ for any $\mu_c$ in the AF phase[4]. Existence of such an upper bound reflects the fact that the AF phase disfavors ample holes. We expect the similar effects of $P(x)$ in Model I for general values of $\delta$, but for definite and direct comparison, one needs to calculate the phase diagram of two models for fixed values of $\delta$.

### 3.2. Algorithm for first-order transitions
The first-order transitions in Fig.1 have large hysteresis. To reduce it, we use the idea explained in Fig.2 to select the prechoice of variables such that

$$
\rho_{x} \rightarrow \rho_{x \text { new }}=\left(\rho_{1}+\rho_{2}\right)-\rho_{x},
\tag{8}
$$

which moves $\rho_x \sim \rho_1 \rightarrow \rho_{x \text{ new}} \sim \rho_2$, $\rho_x \sim \rho_2 \rightarrow \rho_{x \text{ new}} \sim \rho_1$. In Fig.3 we present the internal energy $U \equiv -\langle A \rangle /N$ and $\rho$ before and after the algorithm of (8). It yields a significant improvement. In fact, $U$ and $\rho$ calculated by (8) exhibit a sharp jump (in one unit of $\Delta c_1$) instead of hysteresis, and the critical coupling is estimated as $c_{1c} \simeq 8.25 \sim 8.30$. At the critical point, the two states with $\rho = \rho_1$ and $\rho_2$ degenerate. This degeneracy may be confirmed by a double-peak structure of the energy distribution $P(U)$ at $c_{1c}$, which is a future problem.

![](./images/813261297972936705_3.jpg)

Figure 3. Reduction of hysteresis by the algorithm (8) for $\mu_c = 16, c_3 = 24, L = 12$. (a) Internal energy $U$ by Metropolis algorithm; (b) $U$ by Eq.(8); (c) $\rho$ by Metropolis; (d) $\rho$ by Eq.(8).

## 4. Conclusion
In the present paper, we explained the bosonic $t$-$J$ model in the slave-particle representation, and its phase structure obtained by means of the MC simulations. Further comparison of the bosonic and fermionic $t$-$J$ models is of general interest and worth to study. A MC technique to reduce hysteresis is also explained. It is simple enough to be useful for other systems.

### References
[1] Long M W and Zotos X 1992 *Phys. Rev. B* **45**, 9932, Duan L-M, Demler E and Lukin M D, 2003 *Phys. Rev. Lett.* **91**, 090402, Altman E, Hofstetter W, Demler E and Lukin M D, 2003 *New J. Phys.* **5** 113.
[2] Boninsegni M 2001 *Phys. Rev. Lett.* **87** 087201; 2002 *Phys. Rev. B* **65** 134403.
[3] Aoki K, Sakakibara K, Ichinose I and Matsui T 2009 *Phys. Rev. B* **80** 144510.
[4] Nakano Y, Ishima T, Kobayashi N, Sakakibara K, Ichinose I and Matsui T 2011 *Phys. Rev. B* **83** 235116.
[5] Anderson P W 1987 *Science* **235** 1196.
[6] Kotliar G and Ruckenstein A 1987 *Phys. Rev. Lett.* **57** 2790.
[7] Ichinose I and Matsui T 1992 *Phys. Rev. B* **45** 9976.
[8] Anderson P W 1990 *Phys. Rev. Lett.* **64** 1839; Ichinose I, Matsui T and Onoda M 2001 *Phys. Rev. B* **64** 104516, and references cited therein.