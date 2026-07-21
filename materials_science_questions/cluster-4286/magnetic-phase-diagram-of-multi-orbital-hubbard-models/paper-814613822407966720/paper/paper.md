PHYSICAL REVIEW B, VOLUME 65, 184421

Possible ferromagnetism in divalent boride systems

Chisa Hotta* and Hidetoshi Fukuyama
Institute for Solid State Physics, University of Tokyo, Chiba 277-8581, Japan

Masao Ogata
Department of Physics, Faculty of Science, University of Tokyo, Tokyo 11-0033, Japan

(Received 31 July 2001; revised manuscript received 5 November 2001; published 29 April 2002)

The possibility of ferromagnetic ground states of divalent boride systems has been theoretically investigated by taking into account realistic three-dimensional structures with three pairs of valence and conduction bands which overlap at the $X$ points. It is indicated that because of the particular relationships between on-site Coulomb and exchange interactions, metallic ferromagnetism is difficult to stabilize even within a mean-field calculation. On the other hand, the ferromagnetic metal is seen to be more easily stabilized in the model of a single pair of semimetallic bands, suggesting the preference of tetragonal symmetry for ferromagnetism. Also, a comment is made against excitonic ferromagnetism.

DOI: 10.1103/PhysRevB.65.184421
PACS number(s): 75.50.Cc, 75.10.Lp, 78.40.Kc

## I. INTRODUCTION

After the first striking observation of high-temperature weak ferromagnetism in La-doped $CaB_{6}$ by Young $et al.,^{1}$ many experimental studies have been carried out leading to sometimes contradictory results with a large sample dependence not only in their magnetic aspect but in their transport property as well. $^{2}$ The effect of impurities, surfaces, $^{3}$ and $Ca$ defects $^{4}$ are examined to elucidate whether this ferromagnetism is intrinsic or not, which still remains an open question.

Theoretical studies have also been developed suggesting that the semimetallic band structure lies behind such novel phenomena, which try to relate the ferromagnetism to the excitonic one $^{5}$ or to that of the double-exchange mechanism, $^{6}$ and so forth.

In this paper, we pursue the possibility of ferromagnetism on molecular orbitals (MO's) of hexaborides on the basis of the realistic models which reproduce the precise band structures and the exact relationship between several electronic interaction parameters on MO's. It turns out that the threefold degeneracy of MO's due to cubic symmetry does not favor ferromagnetic metals (FM's) and that FM's can possibly appear if the system is transformed from a cubic to a tetragonal one. However, even in the latter system, the parameter space where this FM is realized is confined to a certain range, which may be consistent with experimental results suggesting a delicate condition for FM.

## II. MODEL HAMILTONIAN

The crystal structure of $CaB_{6}$ is schematically shown in Fig. 1(a). With cubic structure in mind, we take into account the effect of the precise three-dimensional (3D) band structure of the valence and conduction bands. The top of the valence band and the bottom of the conduction band consists of $t_{2g}$ and $t_{2u}$ orbitals, respectively, which are a linear combination of $p$ orbitals on a $B_{6}$ cluster as shown in Fig. 1(b). Both types of orbitals have threefold degeneracy due to the cubic symmetry of this system, and all three pairs have tetragonal shapes which spread on the $xy$, $yz$, and $zx$ planes (i.e., pointing towards the $z$, $x$, and $y$ directions), respectively. Since these orbitals are orthogonal to each other, mixing between them is absent. Hence, there exist six independent bands in the cubic system which are expressed by the kinetic term of the Hamiltonian,

$$
\begin{aligned}
H_{o}= & \sum_{k, \sigma=\uparrow \downarrow} \sum_{\gamma} \epsilon_{\gamma} c_{k \gamma \sigma}^{\dagger} c_{k \gamma \sigma}, \\
= & \sum_{\langle i, j\rangle} \sum_{\lambda=1}^{3} \sum_{\gamma=a_{\lambda}, b_{\lambda}} \sum_{\sigma=\uparrow \downarrow} t_{i j}^{\gamma} c_{i \gamma \sigma}^{\dagger} c_{j \gamma \sigma},
\end{aligned}\quad (2.1)
$$

where $c_{j \gamma \sigma}^{\dagger}$ denotes the creation operator of an electron with spin $\sigma$ in the orbital $\gamma(=a_{\lambda},b_{\lambda},\lambda=1-3)$. The orbitals $a_{\lambda}$ stand for the three $t_{2g}$ orbitals constructing the valence band, while $b_{\lambda}$ for the $t_{2u}$'s of the conduction bands. The corre-

![](./images/814613822407966720_1.jpg)

FIG. 1. Schematic illustration of (a) the unit cell of $CaB_{6}$, (b) $t_{2g}$ and $t_{2u}$ orbitals on $B_{6}$ cluster and (c) the transfer integrals, $t_{i j}^{\gamma}$ $=t_{0},t_{g},t_{u}$, between neighboring sites of each orbital.

![](./images/814613822407966720_2.jpg)

FIG. 2. Valence $(\epsilon_{a})$ and con duction $(\epsilon_{b})$ bands in Eq. (2.2). The dashed and solid lines of the conduction band correspond to $t_{\text{eff}}=0$ and 0.2, respectively.

sponding transfer integrals $t_{i j}^{\gamma}$ are chosen so as to reflect the band structures of the actual $CaB_{6}$ system. For example, the transfer integrals for the $t_{2 \mathrm{~g}}-t_{2 \mathrm{u}}$ pair with $\lambda=1$ (in the $x y$ plane) are shown in Fig. 1(c). The sign of $t_{i j}^{\gamma}$ is determined from the sign of the wave functions of the orbitals. $^{7}$ Throughout this study, we fixed the ratio of transfer integrals to $t_{g} / t_{0}=0.2$ and $t_{u} / t_{0}=0.6$ which are estimated from the distances between the corresponding wave functions of the orbitals, $^{7}$ where $t_{0}$ is taken as an energy unit. Taking into account the energy splitting $2 E_{0}$, we obtain the following energy bands:

$$
\epsilon_{a_{1}}=-E_{0}+2 t_{0}\left[\cos \left(k_{x}\right)+\cos \left(k_{y}\right)\right]-2 t_{g} \cos \left(k_{z}\right),
$$

$$
\begin{aligned}
\epsilon_{b_{1}}= & +E_{0}-2 t_{0}\left[\cos \left(k_{x}\right)+\cos \left(k_{y}\right)\right]+2 t_{u} \cos \left(k_{z}\right), \\
& +t_{\mathrm{eff}}\left[-\cos \left(k_{x}+k_{y}\right)-\cos \left(k_{x}-k_{y}\right)+\cos \left(k_{y}+k_{z}\right)\right. \\
& \left.+\cos \left(k_{y}-k_{z}\right)+\cos \left(k_{z}+k_{x}\right)+\cos \left(k_{z}-k_{x}\right)\right] \\
& +\frac{t_{\mathrm{eff}}}{2}\left[\cos \left(k_{x}+k_{y}+k_{z}\right)+\cos \left(k_{x}-k_{y}+k_{z}\right)\right. \\
& \left.+\cos \left(k_{x}+k_{y}-k_{z}\right)+\cos \left(k_{x}-k_{y}-k_{z}\right)\right].
\end{aligned}
$$

Here, the indirect transfer integral $t_{\text {eff }}$ is also introduced, which originates from the finite mixing between the $t_{2 u}$ and the Ca orbitals. In fact, a local density approximation (LDA) band structural calculation suggests that the shape of the bands at the $X$ point is dramatically modified by the mixing of $t_{2 u}$ with Ca $e_{\mathrm{g}}$ orbitals and that this mixing is the origin of the semimetallic structure. $^{8}$ Since such mixing is not so large, we considered the second-order perturbation process from each MO on hexaboride to its nearest, next-nearest, and third-nearest-neighboring MO's through the nearest Ca sites and summed up all these contributions. Although the relative values of these contributions are made clear, we cannot estimate a reasonable value of $t_{\text {eff }}$ itself since the energy difference between the Ca and $t_{2 u}$ levels is absent. Hence, we choose $t_{\text {eff }} / t_{0}=0.2$ so as to reproduce the results of the band calculation. $^{9}$ The resultant tight-binding bands of $\epsilon_{a_{1}}$ and $\epsilon_{b_{1}}$ are shown in Fig. 2. For comparison, the $\epsilon_{b_{1}}$ band without $t_{\text {eff }}$ is also shown by dashed lines. In the presence of $t_{\text {eff }}$, there exists a finite overlap $-G / t_{0}=0.4$ between valence and conduction bands at the $X$ point [denoted as $X_{1}=(0,0$, $\pm \pi)$ ]. In the following we regard the value of $E_{0}$ as a parameter in order to see the effect of the magnitude of band gap, $G$. The other two pairs of bands pointing towards $x$ and $y$ directions, i.e., $\lambda=2$ and 3 , have the same shape of energy dispersions but with their $k$ values in cyclic permutation. Thus they have an overlap at the $X_{2}=( \pm \pi, 0,0)$ and $X_{3}$ $=(0, \pm \pi, 0)$ points, respectively.

We speculate that the FM occurs through the competition between three different types of electronic interactions $U$, $U_{\gamma \bar{\gamma}^{-}}$, and $J_{\gamma \bar{\gamma}^{-}}$, which are the intraorbital, interorbital Coulomb interactions, and interorbital exchange (Hund) interaction, respectively. Thus, we introduce the following on-site electronic interaction term:

$$
\begin{aligned}
H_{\mathrm{int}}= & \sum_{j}\left(\sum_{m=1}^{3} \sum_{\gamma=a_{m}, b_{m}} U n_{j \gamma \uparrow} n_{j \gamma \downarrow}+\frac{1}{2} \sum_{\gamma \neq \bar{\gamma}} U_{\gamma \bar{\gamma}} n_{j \gamma} n_{j \bar{\gamma}}\right. \\
& \left.-\frac{1}{2} \sum_{\gamma \neq \bar{\gamma}} \sum_{\sigma, \sigma^{\prime}} J_{\gamma \bar{\gamma}} c_{j \gamma \sigma}^{\dagger} c_{j \gamma \sigma^{\prime}} c_{j \bar{\gamma} \sigma^{\prime}}^{\dagger} c_{j \bar{\gamma} \sigma}\right).
\end{aligned}
$$

Further, as regards the discussion of the stability of FM state, we need to keep the exact relations between the values of $U$, $U_{\gamma \bar{\gamma}^{-}}$, and $J_{\gamma \bar{\gamma}^{-}}$, which are derived microscopically from the Slater integrals. $^{10}$ First, we define $U^{\prime}$ and $J_{H}$ by $U^{\prime}$ $=U_{a \lambda b \lambda}$ and $J_{H}=J_{a \lambda b \lambda}$. By using the Slater integrals

$$
U=\frac{1}{2} \int d \vec{r}_{1} d \vec{r}_{2} \Psi_{t_{2 \mathrm{~g}}}^{*}\left(r_{1}\right) \Psi_{t_{2 \mathrm{~g}}}^{*}\left(r_{2}\right) \frac{e^{2}}{r_{12}} \Psi_{t_{2 \mathrm{~g}}}\left(r_{2}\right) \Psi_{t_{2 \mathrm{~g}}}\left(r_{1}\right),
$$

$$
U^{\prime}=\frac{1}{2} \int d \vec{r}_{1} d \vec{r}_{2} \Psi_{t_{2 \mathrm{~g}}}^{*}\left(r_{1}\right) \Psi_{t_{2 \mathrm{u}}}^{*}\left(r_{2}\right) \frac{e^{2}}{r_{12}} \Psi_{t_{2 \mathrm{~g}}}\left(r_{2}\right) \Psi_{t_{2 \mathrm{u}}}\left(r_{1}\right),
$$

$$
J_{H}=\frac{1}{2} \int d \vec{r}_{1} d \vec{r}_{2} \Psi_{t_{2 \mathrm{~g}}}^{*}\left(r_{1}\right) \Psi_{t_{2 \mathrm{u}}}^{*}\left(r_{2}\right) \frac{e^{2}}{r_{12}} \Psi_{t_{2 \mathrm{u}}}\left(r_{2}\right) \Psi_{t_{2 \mathrm{~g}}}\left(r_{1}\right),
$$

it is seen that a relation $U=U^{\prime}+2 J_{H}$ holds. Here, each $\Psi_{\gamma}$ is a linear combination of four different $p$ orbitals among the six vertices of $B_{6}$ octahedron as shown in Figs. 1(a) and 1(b). Further, by considering the tetragonal shape of the orbitals, we get the relations between the other interactions, $U_{\gamma \bar{\gamma}}, J_{\gamma \bar{\gamma}}$, which are summarized in Table I. On the basis of such particular relationships, we investigate the phase diagram on the plane of $U / t_{0}$ and $J_{H} / t_{0}$ by fixing $U^{\prime}=U$

<table>
<caption>TABLE I. The on-site Coulomb ($U_{\gamma\gamma'}$) and exchange ($J_{\gamma\gamma'}$) interactions between orbitals belonging to different pairs, i.e., between $\gamma=a_{\lambda},b_{\lambda}$ and $\gamma'=a_{\bar{\lambda}},b_{\bar{\lambda}}$, where $\lambda\neq\bar{\lambda}$. The values estimated by the Slater integrals are described by the parameters $U$, $U'$, and $J_H$, which are the intra- and interorbital Coulomb interactions and exchange interaction between orbitals within the same pair.</caption>
<tr><th>$\gamma$-$\gamma'$</th><th>$\gamma_{\lambda}$-$\gamma_{\bar{\lambda}}$ ($\gamma=a,b$)</th><th>$a_{\lambda}$-$b_{\bar{\lambda}}$</th></tr>
<tr><td>$U_{\gamma\gamma'}$</td><td>$U'/2$</td><td>$U/2$</td></tr>
<tr><td>$J_{\gamma\gamma'}$</td><td>$J_H/2$</td><td>$U/2$</td></tr>
</table>

$-2J_H$. Note that only the region $U>2J_H$ physically makes sense, since $U'$ should be positive. We focus on the ground state for the nondoped case by use of these interactions within the mean-field theory. It should be mentioned that the multicenter contributions to the exchange and Coulomb integrals, which arise from the possible inequivalency in the weight of the $p$ orbitals forming $\Psi_{\gamma}$, are neglected here. Even if the relationships among $U_{\gamma\bar{\gamma}}$ and $J_{\gamma\bar{\gamma}}$ deviate from those given above due to such contributions, it does not measurably affect our formulation, since the importance lies in the existence of relationships itself.

### III. MULTI-$X$-POINT MODEL

In this section, we consider the model including six different bands, i.e., three pairs of $a_{\lambda}$ and $b_{\lambda}$ bands ($\lambda=1-3$), which we refer to as the *multi-$X$-point model*. It turns out that this model does not favor the FM state.

Within the mean-field Hartree approximation, we assume the order parameters defined as
$$
\begin{aligned}
\delta= & 2-\langle n_{a\uparrow}\rangle-\langle n_{a\downarrow}\rangle=\langle n_{b\uparrow}\rangle+\langle n_{b\downarrow}\rangle, \\
m_{a}= & \langle n_{a\uparrow}\rangle-\langle n_{a\downarrow}\rangle, \\
m_{b}= & \langle n_{b\uparrow}\rangle-\langle n_{b\downarrow}\rangle,
\end{aligned}\tag{3.1}
$$
where $\delta$ is the self-doped charge and $m_{a}$ and $m_{b}$ ($>0$) are the magnetization per each band which will be determined self-consistently. Here, we focus on the uniform solutions, and thus we take the common $\delta$, $m_{a}$, and $m_{b}$ for $\lambda=1-3$. We define the chemical potential $\mu_{\gamma\sigma}$ such that the states $\epsilon_{\gamma}\leqslant\mu_{\gamma\sigma}$ is occupied or
$$
\mu_{\gamma\sigma}=\frac{\partial E_{\text{kin}}}{\partial n_{\gamma\sigma}},\tag{3.2}
$$
where $E_{\text{kin}}$ is the kinetic energy,
$$
E_{\text{kin}}=\sum_{k,\gamma,\sigma}\epsilon_{\gamma}\langle c_{k\gamma\sigma}^{\dagger}c_{k\gamma\sigma}\rangle,\tag{3.3}
$$
since the interaction parameters just give the chemical potential shift. The self-consistent equations for these order parameters become
$$
\mu_{b\uparrow}-\mu_{a\downarrow}=(U+J_{H})(m_{a}+m_{b}).\tag{3.4}
$$

The relations
$$
\mu_{a\sigma}=\mu_{b\sigma}\quad(\sigma=\uparrow,\downarrow)\tag{3.5}
$$
are also required in the case of the partial polarization where each band joining the equation has finite number of electron or hole. The total energy is expressed as
$$
E=E_{\text{kin}}+E_{\text{int}},\tag{3.6}
$$
where the interaction part $E_{\text{int}}$ can be decomposed into two different kinds of interaction energy terms, i.e.,
$$
E_{\text{int}}=3(E_{\text{int}}^{\lambda\lambda}+E_{\text{int}}^{\lambda\bar{\lambda}}).\tag{3.7}
$$

![](./images/814613822407966720_3.jpg)

FIG. 3. Schematic descriptions of partial FM [I] ($m_{\gamma}<\delta$), [II] ($m_{b}<\delta$, $m_{a}=\delta$), fully polarized FM [III] ($m_{a}=m_{b}=\delta$), and FI states. Paramagnetic states, PM and PI, are shown together.

The former is the interaction between the electrons within the pair bands (i.e., the same $\lambda$) and the latter is the one between the electrons belonging to different pair bands. In terms of the order parameters, they become
$$
\begin{aligned}
E_{\text{int}}^{\lambda\lambda}= & U\left(1-\delta+\frac{\delta^{2}}{2}-\frac{m_{a}^{2}+m_{b}^{2}}{4}\right) \\
& +\left(U'-\frac{J_{H}}{2}\right)\delta(2-\delta)-\frac{J_{H}}{2}m_{a}m_{b},
\end{aligned}
$$
$$
\begin{aligned}
E_{\text{int}}^{\lambda\bar{\lambda}}= & \left(U_{\gamma_{\lambda}\gamma_{\bar{\lambda}}}-\frac{J_{\gamma_{\lambda}\gamma_{\bar{\lambda}}}}{2}\right)(4-4\delta+2\delta^{2})+2U_{a_{\lambda}b_{\bar{\lambda}}}\delta(2-\delta) \\
& -\frac{1}{2}J_{\gamma_{\lambda}\gamma_{\bar{\lambda}}}(m_{a}^{2}+m_{b}^{2})-J_{a_{\lambda}b_{\bar{\lambda}}}m_{a}m_{b}.\tag{3.8}
\end{aligned}
$$

For the single-$X$-point model which we discuss shortly, only $E_{\text{int}}^{\lambda\lambda}$ appears. However, in the present multi-$X$-point model, the total interaction energy becomes as simple as
$$
E_{\text{int}}=3\left(3U-5J_{H}-\frac{1}{4}(U+J_{H})(m_{a}+m_{b})^{2}\right).\quad(3.9)
$$

Figure 3 schematically shows the six possible solutions obtained in the phase diagram; three different kinds of FM states (I), (II), and (III), a ferromagnetic insulator (FI), and the paramagnetic metal and insulator (PM and PI). The FM states (I) and (II) correspond to two different kinds of partial

![](./images/814613822407966720_4.jpg)

FIG. 4. (a) The ground-state phase diagram of the multi-$X$-point model on the plane of $J_H$ and $U$ and (b) the energy of FM with respect to PM as functions of $\delta$ together with the value of $U + J_H$.

polarization, and (III) to the fully polarized FM. In the following, in searching the self-consistent solutions, we calculate $U$ and $J_H$ by fixing $\delta$, $m_a$, and $m_b$, instead of finding these order parameters under the fixed value of $U$ and $J_H$.

For the PM state with $m_a=m_b=0$, a unique value of $\delta$ is obtained irrespective of $U$ and $J_H$. Thus the PM energy does not depend on the values of $U$ and $J_H$. On the other hand, the FM solution depends only on the summation $U+J_H$ which is evident from the form of $E_{\text{int}}$ in Eq. (3.9). Figure 4(a) gives the value of $U+J_H$ which satisfies the self-consistent equations for a fixed value of $\delta$ within the FM solutions (i.e., $\delta<1$, $m_\gamma\neq0$). The energy differences between the FM and the PM, $\Delta E_{\text{int}}$ and $\Delta E_{\text{kin}}$, are shown together. We can see that the solutions with small moments (FM[I] and [II] in the inset) are obtained for quite large values of $U+J_H$. However, the energy gain in $\Delta E_{\text{int}}$ cannot overcome the loss of kinetic energy, $\Delta E_{\text{kin}}$, in this range. This means that the FM phase does not appear in the ground state. On the other hand, we find that the FI solution becomes a local minimum when the interactions become as large as half the bandwidth, $U+J_H>(W/2)$ ($\sim11$). This state becomes the ground state when $U+J_H$ increases further to exceed the critical value $U+J_H\sim12$. The transition from the PM state to the FI state is first order. The resultant ground state phase diagram is shown in Fig. 4(b).

Finally, it should be mentioned that we searched for the nonuniform solutions or the solution where the only one pair of bands among the originally equivalent three pairs is ferromagnetic and the other two remain paramagnetic, i.e., $\delta_1\neq\delta_2=\delta_3$, $m_{a1},m_{b1}>0$, and $m_{\gamma\lambda}=0$ for $\lambda=2,3$. We found, however, that there are no such solutions which give the local minimum of the free energy. This may indicate that there is no spontaneous symmetry breaking in this cubic system.

![](./images/814613822407966720_5.jpg)

FIG. 5. (a) The ground-state phase diagram of the single-$X$-point model on the plane of $J_H$ and $U$. (b) The detailed distribution of the ferromagnetic solutions in the FM phase. The dashed lines in the inset show the FM states with a fixed value of $\delta$.

## IV. SINGLE-$X$-POINT MODEL

Now, we introduce the single-$X$-point model which contains only one pair of valence and conduction bands, $\lambda=1$. We will show shortly that this model has the FM ground state in a certain parameter region, which is in contrast with the case of the multi-$X$-point model. The appearance of the FM is expected in analogy with other theories which claim the existence of the ferromagnetism in semimetallic two-band models. $^{6,5}$ Then, through the contrasting results based on the single- and multi-$X$-point models, the role of threefold-degenerate orbitals to suppress FM becomes clear in this paper.

In the single-$X$-point model, the self-consistent equation for the order parameters $\delta$, $m_a$, and $m_b$ becomes

$$
\sum_{\sigma}\left(-\mu_{a\sigma}+\mu_{b\sigma}\right)+2\left(U-5J_H\right)(1-\delta)=0. \tag{4.1}
$$

For the system with partial polarization, i.e., $m_\gamma<\delta_\gamma$, the following two self-consistent equations should also be satisfied:

$$
\begin{aligned}
& \mu_{a\uparrow}-\mu_{a\downarrow}-Um_a-J_Hm_b=0, \\
& \mu_{b\uparrow}-\mu_{b\downarrow}-Um_b-J_Hm_a=0.
\end{aligned} \tag{4.2}
$$

The energy is expressed in terms of Eq. (3.8) as

$$
E=E_{\text{kin}}+E_{\text{int}}^{\lambda\lambda}. \tag{4.3}
$$

![](./images/814613822407966720_6.jpg)

FIG. 6. The phase diagram of the single-$X$-point model for $t_{\text{eff}}$ $=0$ and 0.25, with a fixed value of $G$.

The ground-state phase diagram of the single-$X$-point model is given in Fig. 5(a). This time, the $J_H$-$U$ plane is divided into five different regions, PI, PM, FM, FI, and excitonic insulator (EI); the paramagnetic state which spreads around the small region of $J_H$ is separated into the insulating (PI) and the metallic (PM) states by a line, $U=5J_H-G$. The PM state undergoes a second-order transition into the FM phase with further increasing $J_H$. Then the FI is stabilized at $U+J_H>W$. This metal-insulator boundary is located at twice as large value as that in the multi-$X$-point model. The EI, which extends from $U\sim4J_H-5$ towards the region of larger $J_H$, will be discussed in the next section.

Figure 5(b) shows the detailed structure in the FM region. We find three different kinds of FM states classified in Fig. 3. The dashed lines represent the state with the same value of $\delta$, for $\delta=0.1-0.9$. Along each of these lines, the magnetic moment $m_a+m_b$ becomes larger as $J_H$ (and also $U$) increases. This stabilization of FM by the Hund coupling, $J_H$, is consistent with the idea of the double-exchange mechanism. $^6$

Finally, we examine the detailed structural variation of semimetallic bands near the $X$ point, which seems to be a particular feature of this system. The electron-hole asymmetry is enhanced by increasing $t_{\text{eff}}$. So we study the effect of $t_{\text{eff}}$ on the phase diagram, which is shown in Fig. 6. The range of FM remains unchanged by varying $t_{\text{eff}}$. However, within the FM phase the partial FM [I] region becomes wider at larger $t_{\text{eff}}$ which represents the lighter effective mass of the valence band. Therefore, it is suggested that a contribution from the Ca orbital is essential for the small moment to appear. We note that hardly any change is observed by varying $E_0$ (or $G$), which is because the difference in the band overlap can easily be compensated by just changing the value of $J_H$.

![](./images/814613822407966720_7.jpg)

FIG. 7. Schematic descriptions of the quasiparticle spectrum, $E_{k\sigma}^{\pm}$, in (a) the excitonic metal (EM) and (b) the excitonic insulator (EI).

## V. DISCUSSIONS

### A. Comparison of multi- and single-$X$-point models

We have seen in the previous section that the FM ground state does not appear in the multi-$X$-point model, while it is stabilized in the case of single-$X$-point model over a certain range in the $J_H$-$U$ phase diagram. This can be understood as follows: in the single-$X$-point model, $U$ and $J_H$ together stabilize FM, while $U'$ does not favor FM. In such a situation, $U$ and $J_H$ compete with $U'$ and give rise to a magnetic moment within the range of small $U'$ as seen in the FM phase of Fig. 5 around $U-2J_H=0-2J_H$. The multi-$X$-point model, on the other hand, has extra contributions, $J_{\gamma\bar{\gamma}}$ and $U'_{\gamma\bar{\gamma}}$, between orbitals of different pairs $(\lambda\neq\bar{\lambda})$. The former supports the FM but the latter does not. Since $J_{\gamma\bar{\gamma}}$'s are smaller than $U_{\gamma\bar{\gamma}}$'s, the FM is destabilized compared with the single-$X$-point case. This is evident from the interaction energy term; in addition to the $E_{\text{int}}^{\lambda\lambda}$ of the single-$X$-point case, the multi-$X$-point model has an extra term $E_{\text{int}}^{\lambda\bar{\lambda}}$ whose positive contribution at $m_a,m_b\neq0$ enhances $E_{\text{int}}$. Then the gain of $E_{\text{int}}$ in the FM solution cannot overcome the loss of $E_{\text{kin}}$; thus, FM state disappears from the phase diagram of the multi-$X$-point model.

### B. Excitonic instability

There has been a region of EI in the phase diagram of the single-$X$-point model in Fig. 5. Now, we discuss this phase in connection with other theories and verify that the excitonic ferromagnetism is a rather unrealistic one to be realized.

The idea of excitonic ferromagnetism was first mentioned a long time ago $^{11}$ and has been developed recently in many ways. $^5$ In these theories, the nonmagnetic excitonic insulator in the nondoped semimetallic system transforms into the ferromagnetic state by doping. There, the triplet or the coexistent singlet-triplet electron-hole pairs condense. We examined whether this kind of excitonic condensation takes place in our realistic model. We introduce an excitonic order parameter which is derived from Eq. (2.3) within the Hartree-Fock average,

$$
\Delta_{\sigma}=\frac{1}{\sqrt{N^{3}}} \sum_{k}\left[\left(3 J_{H}-U\right)\left\langle c_{a k \sigma}^{\dagger} c_{b k \sigma}\right\rangle+J_{H}\left\langle c_{a k \bar{\sigma}}^{\dagger} c_{b k \bar{\sigma}}\right\rangle\right].
\tag{5.1}
$$

Here, $\Delta_{\sigma}$ corresponds to half the excitonic gap where the quasiparticle dispersion behaves as

$$E_{k \sigma}^{ \pm}=\eta_{k \sigma} \pm \sqrt{\xi_{k}^{2}+\Delta^{2}},$$

$$
\begin{aligned}
\eta_{k}= & \frac{1}{2}\left(\epsilon_{a k}+\epsilon_{b k}\right) \pm \frac{1}{4}\left(U+J_{H}\right)\left(m_{a}+m_{b}\right), \\
\xi_{k}= & \frac{1}{2}\left(\epsilon_{a k}-\epsilon_{b k}+\left(U-5 J_{H}\right)(1-\delta)-\frac{1}{2}\left(U-J_{H}\right)\left(m_{a}-m_{b}\right),\right.
\end{aligned}
\tag{5.2}
$$

which is shown schematically in Fig. 7. Since the nondoped semimetal favors either the pure singlet or the pure triplet exciton, $^{5}$ we set $\Delta \equiv \Delta_{\uparrow}=\Delta_{\downarrow}$ . The gap equation becomes

$$\frac{1}{4 J_{H}-U}=\int_{E^{+}>E_{F}, E^{-}<E_{F}} \frac{d k}{2 \sqrt{\xi^{2}-\Delta^{2}}}, \tag{5.3}$$

where $E_{F}$ is the Fermi level. The right-hand side (RHS) of this equation is always positive, thus $U<4 J_{H}$ is required for $\Delta$ to be finite.

The obtained EI phase appears in the phase diagram of Fig. 5. In correspondence to the fact that LHS of Eq. (5.3) depends only on $4 J_{H}-U$ , the solutions of the same $\Delta$ 's are aligned along the line parallel to $U=4 J_{H}$ . We found that there exists a parameter region near $U \sim 4 J_{H}$ where the excitonic metallic (EM) solution appears. However, the EM remains a local minimum in almost all over this region, which yields to the FM or PM as shown in Fig. 5, where EM appears only within a small region just above EI. As $4 J_{H}$  $-U$ becomes as large as $4 J_{H}-U \sim 4.8$ the EI becomes a ground state. The boundary of excitonic phases with other FM or PM phases, is always a first-order transition.

Although these excitonic phases appear in the phase diagram, we consider that these states can hardly be realized in the actual system, because the most part of the EI is very close to $U=2 J_{H}$ . This means that the EI is realized only when $U^{\prime}(=U-2 J_{H})$ is very small, i.e., $U^{\prime}<J_{H}$ , which is quite unnatural. The excitonic ferromagnetism arises by doping into these nonmagnetic excitonic states; thus, we expect that its possibility is little. Our FM phase, on the other hand, is located within the range, $(U'-J_{H}) / t_{0}=0-7$ , which is the quite reasonable value.

### C. Relevance to the actual divalent boride systems

The existence of semimetallic band structure near the $X$ point is the most significant feature of divalent boride systems, such as $CaB_{6}$ or $CaB_{2} C_{2}$ . This feature is believed to play a certain role in the appearance of ferromagnetism. In fact, without the semimetallic structure in the $X$ point, a FM with small moments cannot be expected, since the carrier number $\delta$ is always kept constant.

Keeping this in mind, let us relate our results with actual systems. We consider that our multi-X-point model reflects the $CaB_{6}$ system of perfect cubic symmetry. This model, however, cannot afford ferromagnetic metal as shown in Fig. 4. It is natural to consider that the $CaB_{6}$ system is located within the PM phase of Fig. 4, since the value of $U+J_{H}$ of molecular orbitals should not be regarded as the strong coupling ones as in the FI phase. Thus, the ferromagnetism of $CaB_{6}$ reported in several experiments cannot be explained within this model. On the other hand, we speculate that the ferromagnetism of $CaB_{2} C_{2}$ (Ref. 2) is due to the lowered symmetry; i.e., this system is described by the single-$X$-point model of tetragonal symmetry, which exhibits a FM ground state. Actually, the two irreducible MO's on $B_{2} C_{2}$ tetragon exhibit similar band structures with one of these pairs in $CaB_{6}.^{9}$ The small magnetic moment here is due to the effect of mixing between MO and Ca $d$ orbitals.

We speculate further that if the ferromagnetism reported in several experiments $^{1-4}$ on $CaB_{6}$ were an intrinsic one, it might originate from an external symmetry breaking effect such as defects or surfaces, which transforms the system from the multi-$X$-point to the single-$X$-point one. Spontaneous symmetry breaking of cubic electronic systems alone does not seem to take place. Therefore, an external force is required by all means for the appearance of such ferromagnetism.

One might suspect that the value of $U$ and $J_{H}$ in such a FM phase falls into a physically reasonable magnitude. Although exact values of $U$ and $J_{H}$ cannot be easily estimated, it is generally believed that the magnitude of $U$ is of the order of the bandwidth in the case of molecular orbitals similar to organic conductors. The bandwidth of this boride system is $8 t_{0}+12 t_{eff }$ for the $t_{2 u}$ orbital and $8 t_{0}$ for the $t_{2 g}$ orbital; thus, $U / t_{0} \sim 8-15$ is expected, which corresponds to the lower part of the FM phase. The mean-field calculation adopted here could be quite appropriate since we are dealing with a three-dimensional system where the fluctuation is not that large.

As regards the effect of doping, it is clear from our results that the phase diagram yields only a minor change; the FI becomes the FM just because of the presence of doped carriers without any significant change in the location of the other phase boundaries. Therefore the effect of doping is not important in this system.

Finally, we mention that $CaB_{6}$ tends to become cation deficient when synthesized with stoichiometric amounts of constituent elements. If the samples are made with excess Ca, which correspond to the truly stoichiometric hexaborides, it behaves as a diamagnetic semiconductor with a rather large band gap. $^{12}$ The band structure near the Fermi level is, however, extremely sensitive to the different boron bond lengths, $^{13}$ which may be related to the largely sampledependent properties of this system. If we take into account this large band gap as a starting noninteracting bands, we obtain the paramagnetic insulating phase instead of the paramagnetic metal in the phase diagram of the multi-$X$-point model. In either case, we conclude that pure $CaB_{6}$ does not have ferromagnetism.

## VI. CONCLUSION

In this paper, the possibility of the ferromagnetism is theoretically searched for based on the Hartree-Fock approximation stimulated by the experimental reports on $CaB_{6}$ and $CaB_{2} C_{2}$ . We have taken full account of the three-dimensional band structures with the semimetallic overlap of valence and conduction bands at the $X$ points. We think that the particular relationships between the Coulomb and ex-

change (Hund) interactions are important factors to be taken into account. Then, in the presence of cubic symmetry, it is found that ferromagnetism is very difficult to be realized for realistic values of the interaction parameters.

In conclusion, we found that metallic ferromagnetism is not stabilized in a regular cubic system with three different pairs of semimetallic valence and conduction bands. Hence experimental reports on the ferromagnetism of $CaB_6$ are not understood theoretically if it is the bulk property. On the other hand, the ferromagnetic metal is seen to be stabilized relatively easily (i.e., for a certain range of parameter values which are considered to be realistic) under the assumption that there exists only one pair of semimetallic bands. The latter tetragonal model may apply to $CaB_2C_2$. In this way, ferromagnetism can possibly appear only when cubic symmetry is removed to become tetragonal. These considerations will also indicate that the reported ferromagnetism of $CaB_6$ could be caused by the possible local removal of the cubic symmetry due to extrinsic effects such as surfaces or Ca defects. The reason why this ferromagnetism has a high transition temperature still remains unclarified, though we cannot deny its existence.

In the course of our study, the stability of the excitonic state is also studied for the case of a single pair of semimetallic bands. It turned out that this state is not stabilized for realistic values of the interaction parameters.

## ACKNOWLEDGMENTS

We thank H. Harima for providing information indispensable for this study. C.H. was supported by RIKEN during the course of this study. This work was supported by the Grant-in-Aid for Scientific Research (No. 12046218) from the Ministry of Education, Culture, Sports, Science and Technology of Japan.

*Present address: RIKEN, 2-1 Hirosawa, Wako, Saitama 351-0198, Japan. Electronic address: chisa@postman.riken.go.jp

$^{1}$D.P. Young, D. Hall, M.E. Torelli, Z. Fisk, J.L. Sarrao, J.D. Thompson, H.-R. Ott, S.B. Oseroff, R.G. Goodrich, and R. Zysler, Nature (London) 397, 412 (1999).

$^{2}$J. Akimitsu, K. Takenawa, K. Suzuki, H. Harima, and Y. Kuramoto, Science 293, 1125 (2001).

$^{3}$S. Kunii, J. Phys. Soc. Jpn. 70, 3789 (2001).

$^{4}$T. Moriwaka, T. Nishioka, and N. Sato, J. Phys. Soc. Jpn. 70, 341 (2001).

$^{5}$M.E. Zhitomirsky, T.M. Rice, and V.I. Anisimov, Nature (London) 402, 251 (1999); V. Barzykin and L.P. Gor'kov, Phys. Rev. Lett. 84, 2207 (2000); D.F. Agterberg, V. Barzykin, and L.P. Gor'kov, Phys. Rev. B 60, 14 868 (1999); M.E. Zhitomirsky and T.M. Rice, ibid. 62, 1492 (2000); L. Balents, ibid. 62, 2346 (2001).

$^{6}$S. Watanabe, K. Kusakabe, and Y. Kuramoto (unpublished).

$^{7}$J.C. Slater and G.F. Koster, Phys. Rev. 94, 1498 (1954).

$^{8}$A. Hasegawa and A. Yanase, J. Phys. C 12, 5431 (1979).

$^{9}$H. Harima (private communication).

$^{10}$J. Kanamori, Prog. Theor. Phys. 30, 275 (1963).

$^{11}$ B.I. Halperin and T. M. Rice, in Solid State Physics, edited by F. Seitz, D. Turnbull, and H. Ehrenerich (Academic Press, New York, 1968), Vol. 21; B.A. Volkov, Yu.V. Kopaev, and A.I. Rusinov, Sov. Phys. JETP 41, 952 (1975).

$^{12}$J.D. Denlinger, J.A. Clark, J.W. Allen, G.-H. Gweon, D.M. Poirier, C.G. Olson, J.L. Sarrao, and Z. Fisk, cond-mat/0009022 (unpublished); J.D. Denlinger, J.A. Clark, J.W. Allen, G.-H. Gweon, D.M. Poirier, C.G. Olson, J.L. Sarrao, A.D. Bianchi, and Z. Fisk, cond-mat/0107429 (unpublished); H.J. Tromp, P. van Gelderen, P.J. Kelly, G. Brocks, and P.A. Bobbert, cond-mat/0011109 (unpublished).

$^{13}$S. Massidda, A. Continenza, T.M. de Pascale, and R. Monnier, Z. Phys. B: Condens. Matter 102, 83 (1997).