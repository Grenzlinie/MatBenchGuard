# A Superparamagnetic State Induced by a Spin Reorientation Transition in Ultrathin Magnetic Films
Yousuke NORIZUKI and Munetaka SASAKI

Department of Applied Physics, Tohoku University, Sendai 980-8579

We investigate a spin reorientation transition (SRT) in ultrathin magnetic films by Monte-Carlo simulations. We assume that the lateral size of the film is relatively small and it has a single-domain structure. To gain insights into the SRT, we measure a free-energy as a function of perpendicular and in-plane magnetizations. As a result, we find that the system is in a *superparamagnetic state* at the SRT temperature. The disappearance of magnetization around the SRT temperature, which is observed in experiments, emerges due to dynamical fluctuations in magnetization which are inherent in the superparamagnetic state. This observation is in contrast to that in large ultrathin magnetic films that the disappearance of magnetization is caused by a static magnetic structure with many complex domains.

KEYWORDS: spin reorientation transition, ultrathin magnetic film, Monte-Carlo simulation

## 1. Introduction
In the last several decades, ultrathin magnetic films have studied extensively due to both the fundamental interest of low-dimensional magnetism and the numerous perspectives of applications. These studies have revealed that complex magnetic order and curious phenomena are induced in ultrathin magnetic films by competition among several interactions such as ferromagnetic exchange interactions, magnetic anisotropy energies, and magnetic dipolar interactions. A spin reorientation transition $^{1-5)}$ (SRT) is one of such phenomena. This is a transition from a in-plane magnetized state to a perpendicularly magnetized state. This transition is induced by decreasing the thickness of the film or by decreasing the temperature. The SRT has been extensively investigated both experimentally and theoretically until now (see reviews 6,7 and references therein).

The main issue we address in the present study is the disappearance of magnetization around the SRT temperature $T_{\text{SRT}}.^{1,4)}$ This abrupt drop in magnetization around $T_{\text{SRT}}$ is called *pseudogap*. $^{4)}$ Papas *et al.* proposed that there are two possible origins which cause this pseudogap. The first is a dynamical origin that the system is in a paramagnetic state because perpendicular and in-plane anisotropies compensate with each other around $T_{\text{SRT}}$. As a result, magnetization heavily fluctuates with time, and the time average of each component of magnetization, which is measured in experiments, becomes zero. The second is a static origin that complex magnetic domains, which cause an almost complete loss in the total magnetization of the sample, emerge in the vicinity of $T_{\text{SRT}}$. For large ultrathin films with the lateral size of several tens of micrometers, it was observed that a complex domain structure appears near the SRT temperature. $^{3,5)}$ Such behavior was also observed in Monte-Carlo (MC) study$^{8)}$ if the corresponding system size is large enough. $^{9)}$ These results strongly indicate that the pseudogap is caused by the static origin for large films. However, it has not been clarified whether the pseudogap emerges due to the dynamical origin even if the lateral size of the film is not large and the system has a single-domain structure.

To address this issue, we examine the SRT of ultrathin magnetic films with focusing on the pseudogap around $T_{\text{SRT}}$.

The corresponding size of the film is chosen to be relatively small so that the system has a single-domain structure. To gain insights into the properties of the SRT, we measure a free-energy as a function of the two order parameters of the SRT, i.e., perpendicular magnetization $m_{\perp}$ and in-plane magnetization $m_{\parallel}$. To our knowledge, this is the first time that such free-energy is measured in the study of the SRT. The free-energy is calculated numerically by using the method proposed in ref. 10. As a result, we found that the free-energy around $T_{\text{SRT}}$ has a structure that low free-energy region widely spreads in the $(m_{\perp}, m_{\parallel})$ space. Because the amplitude of the magnetization $m \equiv (m_{\perp}^2 + m_{\parallel}^2)^{1/2}$ is non-zero in the low free-energy region, spins are aligned in the same direction. However, the direction of the magnetization heavily fluctuates with time as a result of the exploration inside the low free-energy region. In short, the system is in a *superparamagnetic state* at $T_{\text{SRT}}$. Our results indicate that the pseudogap emerges due to the dynamical origin even in relatively small ultrathin magnetic films with a single-domain structure.

## 2. Model
In the present work, we consider a spin model on a $32 \times 32 \times 1$ square lattice with open boundaries. The Hamiltonian of the model is described as

$$
\begin{aligned}
\mathcal{H} = & -J \sum_{\langle i,j \rangle} S_i \cdot S_j + C_{\text{d}} \sum_{i<j} \left( \frac{S_i \cdot S_j}{r_{ij}^3} - 3 \frac{(S_i \cdot \boldsymbol{r}_{ij})(S_j \cdot \boldsymbol{r}_{ij})}{r_{ij}^5} \right) \\
& - C_{\text{u}} \sum_i (S_i^z)^2,
\end{aligned} \tag{1}
$$

where $S_i$ is a classical Heisenberg spin with an absolute value of unity, $\boldsymbol{r}_{ij} \equiv \boldsymbol{r}_i - \boldsymbol{r}_j$, $\boldsymbol{r}_i$ is the position vector of a site $i$ in the unit of the lattice constant, and $r_{ij} \equiv |\boldsymbol{r}_{ij}|$. In the right hand side of eq. (1), the first term, the second term, and the third term denote ferromagnetic exchange interactions, dipolar interactions, and magnetic anisotropy energies, respectively. The sum of exchange interactions runs over all of the nearest-neighboring pairs. We assume that magnetic anisotropy is uniaxial and its easy axis is parallel to the $z$-axis, where the $z$-axis is perpendicular to the film. This type of model has been often used in the study of the SRT. $^{8,11-17)}$

The three parameters $J$, $C_{\text{d}}$, and $C_{\text{u}}$ in eq. (1) represent the

Table I. The four sets of parameters used in the present study. The mesh
size $\delta$ is calculated from eq. (2) and the ratio $C_{\mathrm{d}} / J$ by assuming that $A=$
$30.2 \times 10^{-12} \mathrm{~J} / \mathrm{m}$ and $J_{\mathrm{s}}=1.79 \mathrm{~T}$. The size is calculated from the mesh
size $\delta$ and the lattice size $32 \times 32 \times 1$.

|         | $C_{\mathrm{d}}/J$ | $C_{\mathrm{u}}/J$ | $\delta$ [nm] | size [nm$^3$]          |
|---------|--------------------|--------------------|---------------|------------------------|
| case 1  | 0.007              | 0.05               | 1.44          | $46.1 \times 46.1 \times 1.44$ |
| case 2  | 0.028              | 0.2                | 2.89          | $92.5 \times 92.5 \times 2.89$ |
| case 3  | 0.056              | 0.4                | 4.08          | $131 \times 131 \times 4.08$ |
| case 4  | 0.070              | 0.5                | 4.56          | $146 \times 146 \times 4.56$ |

strength of each energy term. In the present work, we per-
formed simulations for four different sets of the parameters.
The values of $C_{\mathrm{d}} / J$ and $C_{\mathrm{u}} / J$ in the four cases are shown in
Table I. The ratio $C_{\mathrm{d}} / C_{\mathrm{u}}$, which is 0.14 in all of the four cases,
is chosen so that the SRT is clearly observed. In micromag-
netic calculations, the three parameters in eq. (1) are calcu-
lated from the material parameters and the mesh size as

$$
J=2 \delta A, \quad C_{\mathrm{d}}=J_{\mathrm{s}}^{2} \delta^{3} /\left(4 \pi \mu_{0}\right), \quad C_{\mathrm{u}}=K_{\mathrm{u}} \delta^{3}, \tag{2}
$$

where $\delta$ is the mesh size, $A$ is the exchange stiffness con-
stant in continuous limit, $J_{\mathrm{s}}$ is the saturation polarization, $K_{\mathrm{u}}$
is the magnetic anisotropy constant, and $\mu_{0}$ is the vacuum
permeability. The mesh size $\delta$ shown in Table I is calculated
from the ratio $C_{\mathrm{d}} / J$ by assuming that $A=30.2 \times 10^{-12} \mathrm{~J} / \mathrm{m}$
and $J_{\mathrm{s}}=1.79 \mathrm{~T}$. These values are the same as the mate-
rial parameters of cobalt, $^{18)}$ which is one of the representa-
tive magnetic materials. The sizes of the film shown in Ta-
ble I are calculated from the mesh size and the lattice size.
The magnetic anisotropy constant $K_{\mathrm{u}}$ is calculated from the
ratio $C_{\mathrm{d}} / C_{\mathrm{u}}=0.14$ as $1.45 \times 10^{6} \mathrm{~J} / \mathrm{m}^{3}$. Since the magnetic
anisotropy constant of cobalt is $4.53 \times 10^{5} \mathrm{~J} / \mathrm{m}^{3},^{18)}$ this value
is about three times larger than that of cobalt. In the present
study, we examine the mesh-size dependence by comparing
the data of these four cases.

### 3. Method

We next explain how we measure free-energy as a function
of $m_{\perp}$ and $m_{\|}$. The free-energy is defined by

$$
\begin{aligned}
\exp \left[-\beta F\left(\beta ; m_{\perp}, m_{\|}\right)\right] & \equiv \operatorname{Tr}_{\left\{\mathbf{S}_{i}\right\}} \exp \left[-\beta \mathcal{H}\left\{\mathbf{S}_{i}\right\}\right] \\
& \times \delta\left(m_{\perp}-m_{\perp}^{*}\left\{\mathbf{S}_{i}\right\}\right) \delta\left(m_{\|}-m_{\|}^{*}\left\{\mathbf{S}_{i}\right\}\right), \tag{3}
\end{aligned}
$$

where $\beta$ is the inverse temperature and $\mathcal{H}\left\{\mathbf{S}_{i}\right\}$ is the Hamil-
tonian defined by eq. (1). The trace in the right-hand side of
eq. (3) runs over all of possible configurations. Note that the
right-hand side of the equation is proportional to the proba-
bility that spin configurations with magnetizations $(m_{\perp}, m_{\|})$
are observed. $m_{\perp}^{*}\{\mathbf{S}_{i}\}$ and $m_{\|}^{*}\{\mathbf{S}_{i}\}$ are the perpendicular and in-
plane magnetizations calculated from a configuration $\{\mathbf{S}_{i}\}$, re-
spectively, i.e.,

$$
m_{\perp}^{*}\{\mathbf{S}_{i}\}=\frac{1}{N}\left|\sum_{i} S_{i}^{z}\right|, \tag{4}
$$

$$
m_{\|}^{*}\{\mathbf{S}_{i}\}=\frac{1}{N} \sqrt{\left(\sum_{i} S_{i}^{x}\right)^{2}+\left(\sum_{i} S_{i}^{y}\right)^{2}}, \tag{5}
$$

where $N$ is the number of spins.

We used the method proposed in ref. 10 to calculate
$F\left(\beta ; m_{\perp}, m_{\|}\right)$ numerically. In this method, a variant of the
Wang-Landau method $^{19,20)}$ is combined with the stochas-
tic cutoff (SCO) method, $^{21)}$ which was recently invented for
long-range interacting systems. This method enables us to
calculate $F\left(\beta ; m_{\perp}, m_{\|}\right)$ with reasonable computational time.
Furthermore, long-range dipolar interactions are taken into
account without any approximations by the use of the SCO
method. The detailed conditions of free-energy measurements
are as follows. We set the initial value of the modification
constant $\Delta F$ in ref. 10, which is related with the modification
factor $f$ in the Wang-Landau method $^{19,20)}$ by $f=\exp (\Delta F)$,
to unity. We stopped our simulation after we halved $\Delta F$ 20
times. Therefore, the final $\Delta F$ is $2^{-20}$. The magnetization
space $(m_{\perp}, m_{\|})$ was divided into 10,000 bins with the area
of $0.01 \times 0.01$, and free-energy was calculated for each bin
which satisfies the inequalities $0 \leq (m_{\perp}^{2}+m_{\|}^{2})^{1/2} \leq 0.85$.
The histogram of two magnetizations $H(m_{\perp}, m_{\|})$ was checked
every 10,000 MC steps. We regarded the histogram as flat
when $H(m_{\perp}, m_{\|})$'s for all the magnetizations are not less than
80% of the average value of the histogram. The SCO method
was applied only to dipolar interactions. A potential switch-
ing procedure in the SCO method was performed every 10
MC steps. We performed the free-energy measurement for 10
different runs with different initial states and random num-
ber sequences to estimate the means and errorbars of the free-
energy. The estimated error bars were rather small. They were
smaller than 0.03 $J$ for all of the data we will show hereafter.

![](./images/867763551001903953_1.jpg)

Fig. 1. (Color online) The temperature dependences of the perpendicu-
lar magnetization $m_{\perp}$ (open circles) and in-plane magnetization $m_{\|}$ (open
squares) in the case 1 (upper left), 2 (upper right), and 3 (lower left) in Ta-
ble I. In the measurement, the temperature was gradually cooled from $2.0\ J$
to $0.025\ J$ in steps of $\Delta T=0.025\ J$. The system was kept for 100,000 MC
steps at each temperature. The data of the latter 50,000 MC steps were
used to calculate the thermal averages of the two magnetizations. The av-
erage was also taken over 10 different runs with different initial states and
random number sequences.

### 4. Results

To check whether this model exhibits the SRT or not, we
first measured the perpendicular and in-plane magnetizations
as a function of the temperature in the three cases 1, 2, and
3 in Table I. Figure 1 shows the result. We hereafter set the
Boltzmann constant $k_{\mathrm{B}}$ to unity and use $J$ as a unit of tem-
perature. In this measurement, the temperature was gradually
cooled from $2.0\ J$ to $0.025\ J$ in steps of $\Delta T=0.025\ J$, and the

![](./images/867763551001903953_2.jpg)

Fig. 2. (Color online) Free-energy difference $F_{\rm diff}$ in the case 2 is plotted as a function of $(m_\perp,m_\parallel)$ for two different temperatures. $F_{\rm diff}$ is defined by eq. (6). The left and right panels show the data for $T = T_{\rm SRT} - 0.04\ J$ and those for $T = T_{\rm SRT} + 0.04\ J$, respectively. $T_{\rm SRT}$ is $0.33\ J$. In both figures, $F_{\rm diff}$ is plotted only for a region in which $F_{\rm diff}$ is smaller than $2.5\ J$. The low free-energy region defined by the inequality $F_{\rm diff} \leq T$ is denoted by a solid white line. The average was taken over 10 different runs.

thermal averages of the two magnetizations were measured at each temperature. As the temperature decreases, $m_\parallel$ starts to increase rapidly around $T \approx 0.8\ J$. On the contrary, such rapid increase does not occur in $m_\perp$ around this temperature. Therefore, $m_\parallel$ is dominant at intermediate temperatures. However, $m_\parallel$ starts to drop around $0.4\ J$, and $m_\perp$ overtakes $m_\parallel$ around $0.3\ J$. These data clearly show that the present model exhibits the SRT. We also see that the SRT temperature $T_{\rm SRT}$, which is defined by the temperature where $m_\perp$ is equal to $m_\parallel$, is around $0.3\ J$ in all of the three cases. This means that $T_{\rm SRT}$ mainly depends on the ratio $C_{\rm d}/C_{\rm u}$. Recall that the ratio is fixed to 0.14 in all the four cases (see Table I). We also performed MC simulation in the case 4, and found that a two-domain structure emerges in this case. Because the purpose of the present study is to investigate the SRT in single-domain magnetic films, we hereafter show the results of the three cases 1-3. Since the size of the case 3 is close to that of the case 4, the three cases 1-3 cover almost the whole range of the size in which a single-domain structure is retained.

One may consider that a pseudogap does not exist in this model because neither $m_\perp$ nor $m_\parallel$ is zero at $T_{\rm SRT}$. However, this result is not incompatible with the presence of a pseudogap due to the dynamical origin. It should be recalled that each component of magnetization $m_\mu$ ($\mu = x, y, z$), which can be both positive and negative, disappears at $T_{\rm SRT}$. When spins are aligned in the same direction and the direction changes with time, the time average of $m_\mu$ becomes zero. However, the time averages of $m_\perp$ and $m_\parallel$ do not become zero because they are always positive by definition.

We next measured the free-energy $F(\beta; m_\perp, m_\parallel)$ defined by eq. (3). In Fig. 2, free-energy difference $F_{\rm diff}$ in the case 2 is plotted as a function of $(m_\perp, m_\parallel)$, where $F_{\rm diff}$ is defined by
$$
F_{\rm diff}(\beta; m_\perp, m_\parallel) \equiv F(\beta; m_\perp, m_\parallel) - F_{\rm min}(\beta), \tag{6}
$$
and
$$
F_{\rm min}(\beta) \equiv \min_{(m_\perp, m_\parallel)} F(\beta; m_\perp, m_\parallel). \tag{7}
$$

Figures 2(a) and 2(b) show the data for $T < T_{\rm SRT}$ and those for $T > T_{\rm SRT}$, respectively. We see that $F_{\rm diff}$ for $T < T_{\rm SRT}$ has a global minimum around $(m_\perp, m_\parallel) \approx (0.75, 0.15)$. In contrast, when $T > T_{\rm SRT}$, $F_{\rm diff}$ has a global minimum around $(m_\perp, m_\parallel) \approx (0, 0.6)$. The location of the global minimum shifts discontinuously as the temperature is changed across $T_{\rm SRT}$. In this sense, we can regard the SRT as a first-order transition. This discontinuous shift of the global minimum explains the reason why $m_\perp$ and $m_\parallel$ in Fig. 1 change abruptly around $T_{\rm SRT}$. This result is consistent with the previous results that single monolayer magnetic films with a single-domain structure exhibit a first-order transition. $^{12,17,22)}$ A similar discontinuous shift in the global minimum was observed in the other two cases 1 and 3.

![](./images/867763551001903953_3.jpg)

Fig. 3. (Color online) Free-energy difference $F_{\rm diff}$ at $T_{\rm SRT}$ is plotted as a function of $(m_\perp, m_\parallel)$ for the case 1 (upper left), 2 (upper right), and 3 (lower left). $F_{\rm diff}$ is plotted only for a region in which $F_{\rm diff}$ is smaller than $2.5\ J$. The low free-energy region defined by the inequality $F_{\rm diff} \leq T$ is denoted by a solid white line. The average was taken over 10 different runs.

We next focus our attention to the free-energy structure at $T_{\rm SRT}$. In Fig. 3, we show $F_{\rm diff}$ for all of the three cases. There are several differences in the free-energy structure among the three cases. When $C_{\rm d}$ and $C_{\rm u}$ are small (case 1), the free-energy has a circular structure. In the case 2, this free-energy structure is slightly deformed into a elliptical one. For large $C_{\rm d}$ and $C_{\rm u}$ (case 3), the deformation proceeds further, and the free-energy has two local minima and a free-energy barrier in between. However, a common feature among the three free-energy structures is that a low free-energy region defined by the inequality $F_{\rm diff} \leq T$, which is denoted by a solid white line in Fig. 3, widely spreads in the $(m_\perp, m_\parallel)$ space. In the cases 1 and 2, low free-energy region involves both the perpendicularly magnetized state with $m_\parallel \approx 0$ and the in-plane magnetized state with $m_\perp \approx 0$. There is no (or vanishingly small) barrier between the two states. In the case 3, there is a free-energy barrier like an ordinary first-order phase transition. However, the barrier is rather small. Because single-domain magnets are known to exhibit large fluctuations in magnetization if the energy barrier is small in comparison with $k_{\rm B}T,^{23)}$

![](./images/867763551001903953_4.jpg)

Fig. 4. (Color online) The amplitude of magnetization $m \equiv (m_{\perp}^{2} + m_{\parallel}^{2})^{1/2}$ and the $z$-component of magnetization $m_{z}$ measured at $T_{\text{SRT}}$ are plotted as a function of time for the two cases 1 (upper panel) and 3 (lower panel).

![](./images/867763551001903953_5.jpg)

Fig. 5. (Color online) In-plane components of magnetizations $m_{x}$ and $m_{y}$ measured at $T = 0.4\ J$ are plotted as a function of time for the two cases 1 (upper panel) and 3 (lower panel).

we can expect that magnetization at $T_{\text{SRT}}$ heavily fluctuates with time.

To verify weather this reasoning is correct or not, we performed a standard MC simulation at $T_{\text{SRT}}$ and measured the amplitude of magnetization $m \equiv (m_{\perp}^{2} + m_{\parallel}^{2})^{1/2}$ and the $z$-component of magnetization $m_{z}$. Figure 4 shows the result. The data in the case 1 and those in the case 3 are shown in Figs. 4(a) and 4(b), respectively. We see that $m_{z}$'s in both the cases heavily fluctuate with time, as expected. A similar behavior was observed in the other two components of magnetization $m_{x}$ and $m_{y}$. However, the amplitude of magnetization $m$ is always non-zero because $m$ is non-zero in the low free-energy region of $F_{\text{diff}}$. Especially, in the case 1, $m$ in the low free-energy region is almost constant because $F_{\text{diff}}$ has a circular structure. This is the reason why fluctuations in $m$ are rather small in the case 1. These results show that, at the SRT temperature, spins are aligned in the same direction, and the direction changes with time. In other words, the system is in a superparamagnetic state at $T_{\text{SRT}}$. Therefore, the pseudogap in magnetization emerges around the SRT temperature because of dynamical fluctuations in magnetization which are inherent in the superparamagnetic state.

One may consider that, even if the system is in a in-plane magnetized state and $m_{\parallel} \neq 0$, the time averages of two magnetizations $m_{x}$ and $m_{y}$ become zero if magnetization freely fluctuates in the plane of the film. To examine whether such fluctuations occur or not, we measured the time evolutions of $m_{x}$ and $m_{y}$ at $T = 0.4\ J$ for the two cases 1 and 3. Note that the system is in a in-plane magnetized state at this temperature (see Fig. 1). The result is shown in Fig. 5. We see that $m_{x}$ and $m_{y}$ heavily fluctuate with time. This result means that the four-fold magnetic anisotropy on square lattice, which is induced by magnetic dipolar interactions, is not sufficient to prevent in-plane fluctuations of magnetization. To prevent these fluctuations, some additional anisotropies such as the shape magnetic anisotropy and induced magnetic anisotropy which stabilize magnetization to a direction in the plane are necessary.

Lastly, it may be worth pointing out the similarities and differences between our model and the normal ferromagnetic model which involves only exchange interactions, i.e., our model with $C_{\text{d}} = C_{\text{u}} = 0$. A wide spread of low free-energy region in the magnetization space and large fluctuations in magnetization are also observed in the normal ferromagnetic model. However, because exchange interactions are isotropic, such behavior is observed at *any* temperatures in this model. On the contrary, this behavior is observed only around $T_{\text{SRT}}$ in our model. This is the difference between the two models. Because the pseudogap emerges only around $T_{\text{SRT}}$ in experiments, the normal ferromagnetic model is not proper to describe the SRT.

## 5. Conclusions
We investigated the spin reorientation transition (SRT) in ultrathin magnetic films by Monte-Carlo simulations. We concentrated ourselves on the case that the lateral size of the film is relatively small and the system has a single-domain structure. As a result of free-energy measurement, we found that the system is in a superparamagnetic state at $T_{\text{SRT}}$ and the disappearance (pseudogap) of magnetization around $T_{\text{SRT}}$ emerges due to dynamical fluctuations in magnetization. This observation is in contrast to that in large ultrathin magnetic films that the pseudogap is caused by a static magnetic structure with many complex domains.

## Acknowledgment
The authors would like to thank Professor K. Sasaki for valuable discussions and comments.

1) D. P. Pappas, K.-P. Kämper, and H. Hopster: Phys. Rev. Lett. **64** (1990) 3179.
2) R. Allenspach, M. Stampanoni, and A. Bischof: Phys. Rev. Lett. **65** (1990) 3344.
3) R. Allenspach and A. Bischof: Phys. Rev. Lett. **69** (1992) 3385.
4) Z. Q. Qiu, J. Pearson, and S. D. Bader: Phys. Rev. Lett. **70** (1993) 1006.
5) M. Speckmann, H. P. Oepen, and H. Ibash: Phys. Rev. Lett. **75** (1995) 2035.
6) K. De'Bell, A. B. MacIsaac, and J. P. Whitehead: Rev. Mod. Phys. **72** (2000) 225.
7) P. J. Jensen and K. H. Bennemann: Surf. Sci. Rep. **61** (2006) 129.
8) M. Carubelli, O. V. Billoni, S. A. Pighín, S. A. Cannas, D. A. Stariolo, and F. A. Tamarit: Phys. Rev. B **77** (2008) 134417.
9) In ref. 8, the authors used the same Hamiltonian as eq. (1) and set the ratio $C_{\text{d}}/J$ to be 0.33. By assuming that the material parameters $A$ and $J_{\text{s}}$ are the same as those used in the calculation shown in Table I, the mesh size $\delta$ is calculated to be about 10 nm from eq. (2) and the ratio $C_{\text{d}}/J$. Because the lattice size is $40 \times 40 \times 1$, the corresponding system size is estimated to be 400 nm $\times$ 400 nm $\times$ 10 nm.
10) K. Watanabe and M. Sasaki: J. Phys. Soc. Jpn. **80** (2011) 093001.
11) S. T. Chui: Phys. Rev. B **50** (1994) 12559.
12) A. Hucht, A. Moschel, and K. D. Usadel: J. Magn. Magn. Mater. **148** (1995) 32.
13) A. B. MacIsaac, K. De'Bell, and J. P. Whitehead: Phys. Rev. Lett. **80** (1998) 616.
14) E. Y. Vedmedenko, A. Ghazali, and J. C. Lévy: Phys. Rev. B **59** (1999) 3329.
15) E. Y. Vedmedenko, H. P. Oepen, A. Ghazali, J. C. Lévy, and J. Kirschner: Phys. Rev. Lett. **84** (2000) 5884.
16) E. Y. Vedmedenko, H. P. Oepen, and J. Kirschner: Phys. Rev. B **66** (2002) 214401.
17) C. Santamaria and H. T. Diep: J. Magn. Magn. Mater. **212** (2000) 23.
18) H. Kronmüller and M. Fähnle: *Micromagnetism and the Microstructure of Ferromagnetic Solids* (Cambridge University Press, Cambridge, 2003), Chapter 2.
19) F. Wang and D. P. Landau: Phys. Rev. Lett. **86** (2001) 2050.
20) F. Wang and D. P. Landau: Phys. Rev. E **64** (2001) 056101.
21) M. Sasaki and F. Matsubara: J. Phys. Soc. Jpn. **77** (2008) 024004.
22) A. Moschel and K. D. Usadel: Phys. Rev. B **51** (1995) 16111.
23) For example, the relaxation time $\tau$ of a single-domain nano-particle with uniaxial anisotropy is well described by the Arrhenius law

$$
\tau = f_{0}^{-1} \exp[\Delta B/k_{\text{B}}T],
$$

where $\Delta B$ is the energy barrier between the two stable states and $f_{0}$ is the attempt frequency which is of the order of $10^{9} \sim 10^{11}$ s$^{-1}$.