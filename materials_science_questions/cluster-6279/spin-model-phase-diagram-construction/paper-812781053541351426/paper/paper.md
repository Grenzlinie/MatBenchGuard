Critical behavior of a non-equilibrium interacting particle system driven by an oscillatory field

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2001 Europhys. Lett. 56 400

(http://iopscience.iop.org/0295-5075/56/3/400)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 130.237.165.40
This content was downloaded on 19/08/2015 at 04:08

Please note that terms and conditions apply.

EUROPHYSICS LETTERS
1 November 2001

Europhys. Lett., 56 (3), pp. 400-406 (2001)

# Critical behavior of a non-equilibrium interacting particle system driven by an oscillatory field

R. A. MONETTI and E. V. ALBANO

Instituto de Investigaciones Fisicoquímicas Teóricas y Aplicadas (INIFTA), UNLP
CONICET, CIC (Bs. As.) - C. C. 16 Suc. 4, 1900 La Plata, Argentina

(received 15 September 2000; accepted in final form 20 August 2001)

PACS. 64.60.Cn - Order-disorder transformations, statistical mechanics of model systems.
PACS. 82.40.Bj - Oscillations, chaos, and bifurcations.
PACS. 66.30.Hs - Self-diffusion and ionic conduction in nonmetals.

Abstract. - First- and second-order temperature-driven transitions are studied, in a lattice gas driven by an oscillatory field. The short-time dynamics study provides upper and lower bounds for the first-order transition points obtained using standard simulations. The difference between upper and lower bounds is a measure for the strength of the first-order transition and becomes negligibly small for densities close to one half. In addition, we give strong evidence on the existence of multicritical points and a critical temperature gap, the latter induced by the anisotropy introduced by the driving field.

Far-from-equilibrium systems (FFES) are ubiquitous in nature and their theoretical understanding will contribute to the progress of scientific areas in physics, chemistry, biology, ecology, economy, etc. Since the theoretical development of non-equilibrium statistical mechanics is still in its infancy, a useful approach to FFES is to study simple models by means of various techniques such as numerical simulations, mean-field approximations, phenomenological scaling, field-theoretical developments, etc. Within the broad context of FFES, driven diffusive systems (DDS) [1] have very recently received growing attention [2-4]; for reviews see, e.g., [5-7]. The classical model for DDS was proposed by Katz et al. (KLS) [1] and is based on the equilibrium Ising model [8]. Using the lattice gas language, the KLS model introduces an external driving field to the Ising model. However, due to this modification, the system now evolves towards a non-equilibrium stationary state (NESS). In spite of considerable effort devoted to the study of the KLS model, there are still controversies on the understanding of numerical data [2-4] and its theoretical description is the subject of an ongoing debate [9-11].

In this work we study a DDS subjected to the action of an oscillating driving field. One of the motivations for this approach is that the periodical field can be realized in numerous practical applications such as charged colloids between the plates of a capacitor [12], electrophoresis experiments in pulsed fields [13], gas condensation in the presence of ultrasonic waves [14], segregation of granular materials in vibrating containers, etc.

The aim of this work is to perform an extensive simulation study of the dependence of the temperature-driven transitions of the model on both the density of particles and the

© EDP Sciences

magnitude of the field. Measurements of stationary properties combined to a study of the short-time dynamics allow us to draw a detailed phase diagram of the model that leads us to the discovery of a multicritical point. Furthermore, we developed a coupled mean-field approach that yields results in agreement with the simulations.

The model is defined on the square lattice assuming a rectangular geometry $L_x, L_y$, using "brick wall" (periodic) boundary conditions across (along) the $y$- ($x$-)axis where the oscillatory field is applied, respectively. A lattice configuration $\eta$ is specified by the set of occupation numbers $n_{i,j} = \{0,1\}$, corresponding to each site of coordinates $(i,j)$, *i.e.*, $\eta = \{n_{i,j}\}$. Nearest-neighbor attraction with a coupling constant $J > 0$, is considered. So, in the absence of a field the Hamiltonian $\mathcal{H}$ is given by

$$
\mathcal{H} = -4J \sum_{\langle ij,i'j'\rangle} n_{i,j}n_{i',j'} , \tag{1}
$$

where the summation is over nearest-neighbor sites only. The driving oscillatory field $E$ acts along the $\pm y$-direction with half-period $\tau$. The coupling to a thermal bath at temperature $T$ and the action of the field are considered through Metropolis jump rates, namely $\min[1, \exp -[\{\Delta\mathcal{H} - \epsilon E(\tau)\}/k_\mathrm{B}T]$, where $k_\mathrm{B}$ is the Boltzmann constant, $\Delta\mathcal{H}$ is the change in $\mathcal{H}$ after the exchange, and $\epsilon = (-1,0,1)$ for a particle attempting to hop (against, orthogonal to, along) the driving field, respectively. For $E = 0$ and half-filled lattices, the model reduces to the Ising model in the absence of magnetic field. In the thermodynamic limit the Ising model exhibits a second-order phase transition at a temperature $T_\mathrm{c}^\mathrm{I} = 2.2692....J/k_\mathrm{B}$.

Monte Carlo simulations are performed on lattices of aspect ratios $L_x/L_y = 2$ and 1, with $30 \leq L_y \leq 480$. $T$ is reported in units of $J/k_\mathrm{B}$ and $E$ is given in units of $J$. The starting configuration is obtained by randomly filling the sample with probability $\rho_0$, which is also the density of particles that remains constant. One Monte Carlo time step (mcs) involves $L_xL_y$ trials. Data are obtained disregarding $10^6$ mcs in order to allow the system to reach a NESS, and averages are taken over the subsequent $10^6$ mcs. Using this procedure, a single data point, as, *e.g.*, shown in fig. 2 below, requires $\approx 1$ day of CPU time in an AMD 700 MHz processor.

The model has also been studied by means of a coupled mean-field (CMF) approach. In order to write down the CMF equations, the local density of particles $\rho_{i,j}$ at site $(i,j)$ is defined which is the probability of finding a particle in this site. Due to normalization, one has $\rho_{i,j} + h_{i,j} = 1$, where $h_{i,j}$ is the probability for the site $(i,j)$ to be empty. Then, one has to consider all events that may cause $\rho_{i,j}$ to change. $\rho_{i,j}$ may increase by the arrival of particles due to unbiased (biased) diffusion perpendicular (parallel) to the driving field, respectively. Similarly, the density may decrease by an outgoing flux of particles to neighboring sites. The implementation of the CMF leads to a set of $L_xL_y$ coupled non-linear differential equations. Here, we will only sketch out the form of such equations for the sake of space. Let $\eta'[(i,j);(i',j')]$ be the configuration obtained from $\eta$ by interchanging the content of site $(i,j)$ with that of a neighboring site $(i',j')$. Then, the Metropolis rates are functions $F$ of $\mathcal{H}(\eta') - \mathcal{H}(\eta) - \epsilon E(\tau) = \Delta\mathcal{H}[(i,j);(i',j')] - \epsilon E(\tau)$. So, $\rho_{ij}$ evolves in time according to

$$
\begin{aligned}
\frac{\mathrm{d}\rho_{i,j}}{\mathrm{d}t} &= h_{i,j}\{\rho_{i+1,j}F\{\Delta\mathcal{H}[(i,j);(i+1,j)],T\}+\rho_{i-1,j}F\{\Delta\mathcal{H}[(i,j);(i-1,j)],T\} + \\
&+ \rho_{i,j+1}F\{\Delta\mathcal{H}[(i,j);(i,j+1)],T,E(\tau)\}+\rho_{i,j-1}F\{\Delta\mathcal{H}[(i,j);(i,j-1)],T,E(\tau)\} - \\
&- \rho_{i,j}\{h_{i+1,j}F\{\Delta\mathcal{H}[(i,j);(i+1,j)],T\}+h_{i-1,j}F\{\Delta\mathcal{H}[(i,j);(i-1,j)],T\} + \\
&+ h_{i,j+1}F\{\Delta\mathcal{H}[(i,j);(i,j+1)],T,E(\tau)\}+h_{i,j-1}F\{\Delta\mathcal{H}[(i,j);(i,j-1)],T,E(\tau)\}. \tag{2}
\end{aligned}
$$

![](./images/812781053541351426_1.jpg)

Fig. 1 – 3d plot of the density distribution characteristic of a NESS multistriped configuration obtained with the CMF method. $L_x=80$, $L_y=40$, $T=2.0$, $\rho_0=0.50$, $E=10$ and $\tau=10$.

Equation (2) is solved numerically starting from a random initial distribution of particles and using an integration time step of $\Delta t=0.25$, in arbitrary units. Numerical integrations are performed until $t=25000$ and averages are taken for $t\geq20000$. In the CMF approach the excluded-volume interaction is taken into account in a probabilistic way and stochastic fluctu- ations are disregarded, in contrast to the Monte Carlo method which has intrinsic fluctuations and excluded volume is deterministically satisfied. However, the CMF approach is derived directly form the microscopics, so it contains the same symmetries as the lattice gas model. One advantage of the CMF method is that one can obtain the spatial mass distribution. In fact, fig. 1 corresponds to a NESS where a multistriped pattern is observed. An intriguing feature of driven dissipative systems is the occurrence of highly ordered and complex patterns as shown in fig. 1. Since the system constantly gains (loses) energy from (to) the external field (thermal bath), respectively, the observed stationary states are by no means equilibrium states. In fact, they are truly non-equilibrium steady states.

In order to perform a quantitative investigation, the longitudinal order parameter ($OP_x$) is defined as the excess density, namely

$$
OP_x \equiv (RL_x)^{-1} \sum_{i=1}^{L_x} |P(i)-\rho_0|,
\tag{3}
$$

where $P(i)=(L_y)^{-1}\sum_{j=1}^{L_y}n_{ij}$ is the density profile along the $x$-direction and $R=(2\rho_0(1-\rho_0))$ is a normalization constant. Similarly, $OP_y$ can also be defined.

The dependence of the nature of the ordered phase on the period of the applied field has been investigated [15]. For temperatures below criticality, it is found that for short periods (say $\tau<4L_y$) the system exhibits NESS with striped patterns such as that shown in fig. 1. However, for larger periods (say $\tau>4L_y$) the system alternates between almost equilibrium states (AES) such as those corresponding to molecules in a gravitational field. The crossover from NESS to AES has a characteristic time of the order of $\tau\approx4L_y$. In this work, we are interested in the critical behavior of NESS so we have restricted ourselves to the case $\tau=10$ mcs, without losing generality because the same behavior will be valid for periods such as $\tau<4L_y$ for finite lattices and all periods in the thermodynamic limit. So, $\tau$ plays an important role in this model. In fact, for the case treated in this work, namely $\tau<4L_y$, $OP_x$ is a well-defined quantity independent of time $t$. However, for $\tau>4L_y$, $OP_x$ and $OP_y$ are

![](./images/812781053541351426_2.jpg)

Fig. 2 - (a) Plots of $OP_x$ vs. $T$ obtained for $L_x=240$, $L_y=120$, $E=1$, $\tau=10$ mcs and different values of $\rho_0$ $\circ, \rho_0=0.05$; $\square$ $\rho_0=0.075$; $\bigtriangleup$ $\rho_0=0.10$; $\bigtriangledown$ $\rho_0=0.15$; $+$ $\rho_0=0.20$; $\blacksquare$ $\rho_0=0.80$; $\blacktriangle$ $\rho_0=0.40$; $\bullet$ $\rho_0=0.60$ and $\star$ $\rho_0=0.50$. The inset shows results obtained solving the CMF equations for $E=10$ and $\tau=1$. $\bullet$ $\rho_0=0.15$; $\blacksquare$ $\rho_0=0.30$; $\circ$ $\rho_0=0.50$. (b) Plots of $OP_x$ vs. $T$ obtained by using the Monte Carlo method for $\rho_0=0.05$ and the values of the field indicated in the figure. (c) As in (b) but solving the CMF equations for $\rho_0=0.30$.

functions of time $t$, since the system alternates between AES as mentioned above. So, the half-period changes the nature of the problem and a crossover from NESS to AES is observed [15]. In addition, since the oscillatory field causes the current of the driven gas averaged over long times to vanish, the symmetries of the model are different from those of the KLS model. From the theoretical point of view, this fact is essential to establish the universality class of the model, as will be discussed below.

Figure 2(a) shows the results obtained for $E=1$. For low densities ($\rho_0 \leq 0.15$) the observed transitions are abrupt and exhibit strong metastability, so they are first order. In contrast, for $\rho_0 \geq 0.40$ one observes second-order or very weak first-order-like behavior. Notice that for $\rho_0=0.20$ and $\rho_0=0.40$ we have also included data which demonstrate the particle-hole exchange invariance of the results. The existence of both first- and second-order transitions can also be observed by using the CMF approach. These results are in excellent agreement with Monte Carlo data, as shown in the inset of fig. 2(a). Figures 2(b) and (c) show that, for low densities, $T_c$ depends on the amplitude of the field, so that the higher the field the lower the $T_c$. Furthermore, these figures also reveal that weaker first-order transitions are obtained for smaller amplitudes of the field. Remarkably, results obtained by means of the CMF approach exhibit the same decreasing trend as the Monte Carlo data.

Figure 3 shows the phase diagrams obtained for a fixed lattice size ($L_x/L_y=2, L_y=120$) and two values of the driving field, namely $E=1$ and $E=50 \approx \infty$. Using a method recently proposed for the study of the short-time dynamics of weak first-order transitions [16], it is possible to determine both lower and upper bounds for $T_c(\rho_0)$ valid in the thermodynamic limit and further generalize the phase diagram for $E>1$. The idea behind the proposed method is based on the existence of two pseudocritical points at $T^*$ and $T^{**}$ near the weak first-order transition point $T_c$ with $T^* < T_c < T^{**}$. These points can be obtained accurately from two short-time dynamical processes starting from fully disordered and zero-temperature states, respectively. In second-order transitions $T^*$ and $T^{**}$ overlap with the transition point $T_c$, so the difference between $T^*$ and $T^{**}$ also gives a criterion for the weakness of the first-order transition [16]. Consider a system at $T < T_c(\rho_0)$ and the evolution process from a fully

![](./images/812781053541351426_3.jpg)

Fig. 3 - Phase diagram, $T_{\rm c}$ vs. $\rho_0$, obtained from the data of fig. 2(a). Empty (filled) symbols correspond to $E=1$ ($E=\infty$), respectively. On the left side, the symbols $\bigtriangleup$ and $\bigtriangledown$ show the upper and lower bounds for $T_{\rm c}$ as obtained by means of the short-time dynamics study for $E=\infty$. $\square$ shows the location of the multicritical point. The full and the dashed curves, drawn on the right side, correspond to the best fit of the data obtained using eq. (4). $*$, $\blacksquare$ and $\diamond$ show the location of the critical temperature of the Ising model $T_{\rm c}^{\rm I}$, the critical temperature predicted by eq. (4) for $E\rightarrow0$, and the lower bound obtained for $E=0.01$ using the short-time dynamic analysis, respectively.

disordered state. Due to the geometrical constrained $L_x/L_y^\phi \gg 1$ ($\phi\approx0.2$) [17], configurations at short times exhibit multistriped patterns that are long lived, only relaxing to the single-stripe state after a time of the order $t\sim L_x^3L_y$ [17]. Even in the case of square geometry, both the present model and the KLS model display multistriped configurations up to $t\sim10^5$ mcs [17]. It is then clear that the short-time dynamics must be studied using an order parameter which takes into account multistriped configurations as that given by eq. (3).

Our results for the short-time dynamical behavior have been summarized in fig. 4. For the used density ($\rho_0=0.16$) power laws have been obtained for $T^{**}=2.76$ (fig. 4(a)) and $T^*=2.40$ (fig. 4(b)) starting from ordered and fully disordered states, respectively. Also, fig. 4(c) shows that the lower bound given by the short-time dynamics is independent of the lattice size. Notice that the curves obtained for different aspect ratios are shifted but the power law behavior is obtained at the same temperature. The same results have been obtained for the upper bound, pointing out that the bounds drawn in the phase diagram (fig. 3) are independent of the lattice size and consequently also valid in the thermodynamic limit. The transition points estimated using a finite lattice (fig. 2) satisfy $T^*<T_{\rm c}<T^{**}$ as would also do the true transition points in the $L_x,L_y\rightarrow\infty$ limit. Also, the difference $\Delta T=T^{**}-T^*$ depends on the strength of the first-order transition while $\Delta T\equiv0$ at the second-order transition point for $\rho_0=1/2$.

Coming back to the phase diagram, it is found that for $\rho_0\geq0.30$, $T_{\rm c}(E)$ steadily *increases* with the strength of the field, reaching a saturation value at $T_{\rm c}(E=\infty)\simeq1.41\ T_{\rm c}(E=0)$ for $\rho_0=1/2$, in excellent agreement with results for the KLS model [2,3]. However, for lower densities (e.g., for $\rho_0<0.1$, in fig. 3) $T_{\rm c}(E)$ steadily *decreases* when increasing the magnitude of the field. So, $T_{\rm c}(E)$ exhibits opposite trends depending on the density and, consequently, it is expected that for some characteristic density $\rho_0^{\rm M}$ ($0.20\geq\rho_0^{\rm M}\geq0.15$) the critical temperature will be the same for all magnitudes of the driving field. Therefore, the point $(\rho_0^{\rm M},T_{\rm c}(E,\rho_0^{\rm M}))$ is a *multicritical* point, in the sense that for these special values of density and temperature this point is a critical point for all values of the amplitude of the field. Due to the observed symmetry, $(1-\rho_0^{\rm M},T_{\rm c}(E,\rho_0^{\rm M}))$ is also a multicritical point.

![](./images/812781053541351426_4.jpg)

Fig. 4 – Log-log plots of the OP vs. t, as obtained by means of the short-time dynamics study. Averages are taken over $10^3$ different runs using lattices of size $L_x/L_y=2$, $L_y=120$. The following cases are shown: a) starting from an ordered state; b) starting from a fully disordered state; c) as in b) but for different lattice sizes; d) as in b) but for different driving fields.

Assuming that the critical curves have the simplest form allowed by the symmetry of the system, we propose the following expression for the critical temperature:

$$
T_{\mathrm{c}}(E, \rho_{0})=T_{\mathrm{c}}(\infty, 1 / 2)-k_{\infty} f(E)\left(\frac{1}{2} \pm \rho_{0}^{\mathrm{M}}\right)^{1 / \beta}-k_{\infty}(1-f(E))\left(\frac{1}{2} \pm \rho_{0}\right)^{1 / \beta}, \quad E>0, \quad(4)
$$

where for $E \to \infty$, $k_{\infty}$ is the coefficient of the higher-order term and $f(E) \to 0$, respectively. Equation (4) can be thought of as the first approximation to the phase coexistence curve, valid close to $\rho_{0}=1 / 2$, so that $\beta$ is the order parameter critical exponent of the second-order transition. In order to fit eq. (4) to the data, we will first summarize the symmetries present in our model. The model exhibits full translational and reflexion invariance as the Ising model, but the rotational symmetry is broken due to the anisotropy introduced by the field. If we consider short time scales, the up-down symmetry is also broken by the field. However, a renormalization group study will consider the system at a coarse-grained level. Then, we expect that the up-down symmetry will be restored at long time scales. Consequently, the present model displays the same symmetries as the randomly driven lattice gas with $\beta=\frac{1}{3}$ [11]. Taking this value for $\beta$, the critical curve for $E=\infty$ can be fitted using a single parameter, yielding $k_{\infty}=15 \pm 3$. Assuming that $f(E)=\exp [-E]$, $\rho_{0}^{\mathrm{M}}$ is the only parameter left to be fitted, yielding $\rho_{0}^{\mathrm{M}}=0.160 \pm 0.005$ for $E=1$ (see fig. 4). Discrepancies between the fit and the data for densities far from $\rho_{0}=1 / 2$ are expected, since the expansion given by eq. (4) holds close to that point only. Notice that eq. (4) satisfies the condition that $(\rho_{0}^{\mathrm{M}}=0.160 \pm 0.005$, $T_{\mathrm{c}}(\rho_{0}^{\mathrm{M}})=2.59 \pm 0.01)$ is a multicritical point. This value is in agreement with the estimation performed using the short-time dynamics study that gives $T^{* *}=2.76>T_{\mathrm{c}}(\rho_{0}^{\mathrm{M}})>T^{*}=2.40$ (see fig. 4). The existence of the multicritical point can also be confirmed by means of a short-time dynamics simulations. In fact, fig. 4(d) shows that plots of $OP_x$ vs. $t$ obtained for different fields $(1 \leq E \leq \infty)$ yield the same lower bound

for $T_{\mathrm{c}}(\rho_{0}^{\mathrm{M}})$ given by $T^{*}=2.40$, independently of the strength of the field. This behavior is characteristic of the multicritical point, as observed in fig. 3. It should be noticed that fits of the phase diagram assuming $\beta=1/2$, as theoretically expected for the KLS model [18], are far from being satisfactory. Also, an excellent fit of the curve can be obtained assuming $\beta=1/4$ (yielding $(\rho_{0}^{\mathrm{M}}=0.168\pm0.005,\ T_{\mathrm{c}}(\rho_{0}^{\mathrm{M}})=2.57\pm0.01)$), but this value of the exponent is not supported by the symmetry considerations above mentioned.

For the sake of comparison, we have included in the phase diagram the critical temperature of the Ising model $T_{\mathrm{c}}^{\mathrm{I}}$ as well as the prediction of eq. (4) in the $E\to0$ limit. The latter is in excellent agreement with the lower-bound estimate given by the short-time dynamics method for $E=0.01$. Notice that these estimations for the driven system are consistent with the location of the multicritical point that should also hold for $E\to0$. These results show that, for $\rho=1/2$, there is a gap in the critical temperature between the case $E=0$ (Ising model) and the limit $E\to0$ of the present model. Such a gap is expected to be even greater for $\rho\neq1/2$ because in this case the coexistence temperature of the Ising model is lower than $T_{\mathrm{c}}^{\mathrm{I}}$ while the coexistence temperature of the driven diffusive system has a lower bound given by the multicritical temperature. The existence of these temperature gaps dramatically reflects the anisotropy introduced by the driving field and the non-equilibrium nature of the studied model. A physical explanation of this observation remains as an open question.

In summary, the phase diagram of a DDS in the presence of an oscillatory driving field is determined for $E=1$ and $E=\infty$. We give strong evidence of the existence of a multicritical point and a critical temperature gap separating the cases $E=0$ from $E\to0$. To our best knowledge, these features have never been reported in the field of DDS.

***

This work was supported by CONICET, UNLP, ANPCyT and Fundación Antorchas (Ar- gentina). We acknowledge useful discussions with B. SCHMITTMANN.

REFERENCES

[1] KATZ S., LEBOWITZ J. and H. SPOHN, *Phys. Rev. B*, **28** (1983) 1655.
[2] LEUNG K. T., *Phys. Rev. Lett.*, **66** (1991) 453.
[3] WANG J. S., *J. Stat. Phys.*, **82** (1996) 1409.
[4] MARRO J. and A. ACHAHBAR, *J. Stat. Phys.*, **90** (1998) 817.
[5] SCHMITTMANN B. and ZIA R. K. P., *Phys. Rep.*, **301** (1998) 45.
[6] SCHMITTMANN B. and ZIA R. K. P., in *Phase Transition and Critical Phenomena*, edited by C. DOMB and J. L. LEBOWITZ, Vol. **17** (Academic, London) 1995.
[7] MARRO J. and DICKMAN R., in *Non-equilibrium Phase Transitions in Lattice Models* (Cam- bridge University Press, Cambridge) 1999.
[8] ISING E., *Z. Phys.*, **31** (1925) 253.
[9] DE LOS SANTOS F. and MUÑOZ M., *Phys. Rev. E*, **61** (2000) 1161.
[10] SCHMITTMANN B., JANSSEN H., TÄUBER U., ZIA R., LEUNG K.-T. and CARDY J., *Phys. Rev. E*, **61** (2000) 5977.
[11] GARRIDO P., MUÑOZ M. and DE LOS SANTOS F., *Phys. Rev. E*, **61** (2000) R4683.
[12] ARANSON I. S. *et al.*, *Phys. Rev. Lett.*, **84** (2000) 3306.
[13] ALON U. and D. MUKAMEL, *Phys. Rev. E*, **55** (1997) 1783.
[14] BAUERECKER S. and NEIDHART B., *J. Chem. Phys.*, **109** (1998) 3709.
[15] MONETTI R. and ALBANO E. V., unpublished.
[16] SCHÜLKE L. and ZHENG B., *Phys. Rev. E*, **62** (2000) 7482.
[17] LEVINE E., KAFRI Y. and MUKAMEL D., *Phys. Rev. E*, **62** (2000) 7619.
[18] JANSSEN H. K. and SCHMITTMANN B., *Z. Phys. B*, **64** (1986) 503.