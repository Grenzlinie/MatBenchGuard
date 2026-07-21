A ferromagnet with a glass transition

This content has been downloaded from IOPscience. Please scroll down to see the full text.

2001 Europhys. Lett. 55 465

(http://iopscience.iop.org/0295-5075/55/4/465)

View the table of contents for this issue, or go to the journal homepage for more

Download details:

IP Address: 202.28.191.34
This content was downloaded on 21/02/2015 at 10:09

Please note that terms and conditions apply.

# A ferromagnet with a glass transition

S. Franz $^{1(*)}$, M. Mézard $^{2(**)}$, F. Ricci-Tersenghi $^{1(***)}$,
M. Weigt $^{3(**)}$ and R. Zecchina $^{1(**)}$

$^{1}$ The Abdus Salam International Centre for Theoretical Physics
Condensed Matter Group - Strada Costiera 11
P.O. Box 586, I-34100 Trieste, Italy

$^{2}$ LPTMS, Université de Paris Sud - Bât. 100, F-91405 Orsay, France

$^{3}$ Institute for Theoretical Physics, University of Göttingen
Bunsenstr. 9, D-37073 Göttingen, Germany

(received 15 March 2001; accepted 30 May 2001)

PACS. 05.70.Jk – Critical point phenomena.
PACS. 64.70.Pf – Glass transitions.
PACS. 75.10.Nr – Spin-glass and other random models.

**Abstract.** – We introduce a finite-connectivity ferromagnetic model with a three-spin interaction which has a crystalline (ferromagnetic) phase as well as a glass phase. The model is not frustrated, it has a ferromagnetic equilibrium phase at low temperature which is not reached dynamically in a quench from the high-temperature phase. Instead it shows a glass transition which can be studied in detail by a one-step replica-symmetry-broken calculation. This spin model exhibits the main properties of the structural glass transition at a solvable mean-field level.

Over the last decades there has been a growing interest in understanding the structural glass transition in complex materials. A major theoretical role has been played by mean-field theories based on fully connected $p$-spin-glass models [1–3]. In such models, it was possible to identify a purely dynamical transition which accounts for the off-equilibrium behaviour of the models, and which is believed to present some analogies to the structural glass transition in realistic systems [4–7].

Although this analogy is very fruitful, one must keep in mind that the mean-field spin-glass models which have been considered are rather remote from the structural glasses. Let us mention just the three most obvious differences: they have no crystalline state, their Hamiltonian has quenched-in disorder, in the form of an extensive number of quenched coupling constants, and these couplings are of infinite range. A lot of work has already been devoted to cure these defects, in order to get a much closer analogy between some lattice spin models and structural

$^{(*)}$ E-mail: franz@ictp.trieste.it
$^{(**)}$ E-mail: mezard@ipno.in2p3.fr
$^{(***)}$ E-mail: federico.ricci@ictp.trieste.it
$(^{**})$ E-mail: weigt@theorie.physik.uni-goettingen.de
$(^{**})$ E-mail: zecchina@ictp.trieste.it

© EDP Sciences

glasses. This should allow to clarify some basic issues as, for instance, the presence of heterogeneities or the role of geometrical frustration. A few years ago, it has been realized that the existence of quenched disorder is not a necessary ingredient for a system to have a spin-glass phase: several mean-field spin models were constructed which display a discontinuous spin-glass transition typical of the $p$-spin-glasses [8]. More recently, numerical simulations of some unfrustrated 3-dimensional spin problems, with purely ferromagnetic multi-spin interactions, have shown a glassy behaviour which persists for very long times [9]. A similar behaviour was found also analytically in 2 dimensions [10].

In this paper, we introduce a similar ferromagnetic model having multi-spin interactions and finite connectivity. The model is defined on a Bethe hyper-lattice (or Husimi tree, the analog of a Bethe lattice for systems with plaquette interactions), where it can be solved completely using the replica/cavity method. This model thus provides the correct mean-field (Bethe) approximation for these ferromagnetic multi-spin systems. As in the usual Bethe lattice, it is a finite-connectivity system (each spin interacts with a finite number of neighbours), but has a locally tree-like structure which makes it solvable at the mean-field level. The spin-glass version of the model, with random boundary conditions, was considered first in [11]. Our solution shows a phase diagram qualitatively similar to that of usual $p$-spin models, with a static and a dynamic glass transitions appearing at two different temperatures. On top of the glass phase, it also displays a purely ferromagnetic phase which is the analog of the crystalline phase in supercooled liquids.

The model is defined by the Hamiltonian

$$
H=-\sum_{[i, j, k] \in E} J_{i j k} S_{i} S_{j} S_{k}, \tag{1}
$$

where $S_{i}= \pm 1$ ($i=1,..., N$) are Ising spins. The model is ferromagnetic: we take $J_{i j k}=1$ for all the triples $[i, j, k]$ belonging to the set $E$ of hyper-edges (plaquettes). So the system is not frustrated and the configuration $S_{i}=1$ ($i=1,.., N$) is a ground state for every possible choice of $E$ and satisfies simultaneously all interactions. The plaquettes are chosen randomly, according to the two following ensembles:

- In the first ensemble, the only constraint is that each spin belongs exactly to $k+1$ plaquettes. The set of plaquettes builds up a hyper-graph which is locally a Husimi tree of fixed connectivity $k+1$. This structure of hyper-edges eventually loops back onto itself, but the typical length of the loops scales like $\ln(N)$. This hyper-graph was used analogously in frustrated spin models studied in the context of spin-glasses [12]. In particular one should notice that its structure is not disordered on any finite length scale: disorder comes in only through the loops which have diverging length scale and so the system is only very weakly disordered. Basically this construction amounts to having a Cayley hyper-tree with random hyper-edges closing the boundary.

- Our results can be easily generalized to hyper-trees with fluctuating connectivities. Such models, with Poisson-distributed connectivities, were introduced recently in [13,14] as a simple case of an optimization problem. As in the case of ferromagnetic systems with multi-spin interactions in finite dimensions [9,10], it was observed that purely ferromagnetic interactions may lead to an effective dynamical frustration. This was shown in [14] by comparing lowest metastable states in a ferromagnetic finite-connectivity 3-spin model with the ground states of the corresponding frustrated spin-glass version ($J_{i j k}= \pm 1$ randomly), which were found to share exactly the same statistical features. As also seen in [13] by analyzing the off-equilibrium low-temperature dynamics of both

models, the ferromagnetic system is not able to equilibrate due to the entropic domi-
nance of metastable states.

The results can also be generalized to interactions between clusters of $p$-spins ($p \geq 3$), also with spins belonging to clusters but interacting pairwise, which can be viewed as a representation of geometrical frustration.

At first we concentrate on an analytical approach to the equilibrium behaviour based on the replica trick [1]. The results will be compared later on with data obtained from Monte Carlo simulations. The free-energy density can be read off from the $n \to 0$ limit of the $n$-fold replicated free energy at temperature $T = \beta^{-1}$. The formulas are written here for a general hyper-tree with $k+1$ hyper-edges per site, we shall then discuss in more details the case $k=3$. This is the lowest value of $k$ for which ferro-magnetic and glassy behaviour are present, for $k=2$ the system is paramagnetic at all temperatures [11].

The natural order parameter in the replica approach is a probability distribution $c(\vec{\sigma})$ on the set $\vec{\sigma} \in \{\pm 1\}^n$, which counts the fraction of sites $i$ having replicated spin $S_i^a = \sigma^a$ ($a=1,...,n$). For details on this approach see refs. [12,14]. In terms of this order parameter, the replicated free energy reads

$$
-\beta f_{n}=\underset{c(\vec{\sigma})}{\operatorname{extr}}\left[\frac{k+1}{3} \ln \left(\sum_{\vec{\sigma}_{1}, \vec{\sigma}_{2}, \vec{\sigma}_{3}} c(\vec{\sigma}_{1})^{k} c(\vec{\sigma}_{2})^{k} c(\vec{\sigma}_{3})^{k} e^{\beta \sum_{a=1}^{n} \sigma_{1}^{a} \sigma_{2}^{a} \sigma_{3}^{a}}\right)-k \ln \left(\sum_{\vec{\sigma}} c(\vec{\sigma})^{k+1}\right)\right]. \quad (2)
$$

We notice that if we had considered spin-glass couplings $J_{ijk}=\pm 1$ with symmetric probability, we would have found $\cosh(\beta \sum_{a=1}^{n} \sigma_{1}^{a} \sigma_{2}^{a} \sigma_{3}^{a})$ instead of the exponential in (2).

One needs to find a distribution $c(\vec{\sigma})$ which makes this free energy stationary, which means that it must satisfy the saddle point equation

$$
c(\vec{\sigma}) \propto \sum_{\vec{\sigma}_{2}, \vec{\sigma}_{3}} c(\vec{\sigma}_{2})^{k} c(\vec{\sigma}_{3})^{k} \exp \left[\beta \sum_{a=1}^{n} \sigma^{a} \sigma_{2}^{a} \sigma_{3}^{a}\right]. \quad (3)
$$

It turns out that there exist three solutions, corresponding to a paramagnetic, a ferromagnetic and a spin-glass phase of the system.

The simplest solution is the paramagnetic one, $c_{\mathrm{pm}}(\vec{\sigma})=1 / 2^{n}$ for all $\vec{\sigma}$. This solution is expected to be valid at sufficiently high temperature. The paramagnetic free-energy density is given by

$$
-\beta f_{\mathrm{pm}}=\ln 2+\frac{k+1}{3} \ln \cosh (\beta). \quad (4)
$$

At lower temperature there appears a ferromagnetic solution. There, replica symmetry (RS) is expected to hold, and $c(\vec{\sigma})$ depends on $\vec{\sigma}$ only via $\sum_{a} \sigma^{a}$. Furthermore there are no site-to-site fluctuation since all nodes of the hyper-tree are equivalent, so one can look for a ferromagnetic solution of the type

$$
c(\vec{\sigma})=\frac{e^{\beta h \sum_{a} \sigma^{a}}}{(2 \cosh \beta h)^{n}}. \quad (5)
$$

This is indeed a stationary solution provided the effective magnetic field $h$ is a solution of the equation

$$
\tanh (\beta h)=\tanh (\beta) \tanh (\beta k h)^{2}. \quad (6)
$$

Nontrivial solutions (with $h \neq 0$) exist only for temperatures below a certain $T_{\text{ms}}$, and disappear abruptly above $T_{\text{ms}}$. The resulting free energy reads

$$
-\beta f_{\text{fm}}=\ln 2+\frac{k+1}{3} \ln \left[\cosh (\beta) \cosh (\beta k h)^{3}+\sinh (\beta) \sinh (\beta k h)^{3}\right]-k \ln [\cosh (\beta(k+1) h)]. \quad (7)
$$

The ferromagnetic transition is of first order: one needs to find the largest, *i.e.* locally stable, of the two nontrivial solutions for $h$. For temperatures slightly below $T_{\text{ms}}$ the free energy of this ferromagnetic solution is larger than that of the paramagnetic one and the latter stays globally stable. Only at a temperature $T_{\text{fm}} < T_{\text{ms}}$, the ferromagnetic solution becomes thermodynamically dominant (lower free energy), inducing a first-order transition. For the case $k=3$, one gets $T_{\text{ms}}=1.63$ and $T_{\text{fm}}=1.21$.

A third solution of (3) corresponds to a *glass* phase. As we shall see, this phase is easily accessed by Monte Carlo simulations with decreasing temperature. Its physical origin lies in the fact that if one of the spins on a plaquette is down, then the effective interaction among the other two spins in the same plaquette becomes antiferromagnetic. Therefore there is no restoring force towards the ferromagnetically ordered state. In order to find the glass phase in the replica approach, one has to look for a $c(\vec{\sigma})$ which breaks replica symmetry.

We have found a one-step replica-symmetry-breaking (RSB) solution, which is even with respect to separate changes of sign of all its variables. This solution is somewhat involved because we are dealing with a finite connectivity system. We need to build up, on each site $i$, a distribution of local fields $P_{i}(h)$. The local fields on site $i$ in the various pure states $\alpha$ are iid variables chosen from the distribution $P_{i}(h)$. This distribution fluctuates from site to site and the order parameter is a functional: the distribution of the functions $P_{i}$. In replica language, this one-step RSB amounts to a solution $c_{\text{rsb}}(\vec{\sigma})$ of the saddle point equations with the following structure:

$$
c_{\text{rsb}}(\vec{\sigma})=\int \mathrm{d} \lambda \mu(\lambda) \prod_{a=1}^{n / m}\left[\int \mathrm{d} u_{a} \phi\left(u_{a} | \lambda\right) \exp \left[\beta u_{a} \sum_{b=(a-1) m+1}^{a m} \sigma^{b}\right]\right].
\tag{8}
$$

It depends on the real (for $n \to 0$) number $m$, on the function $\mu$ which is a probability distribution, and on the functions $\phi(u | \lambda)(2 \cosh (\beta u))^{m}$ which are probability distributions on $u$ conditioned to a given value of $\lambda$. The link between the replica approach and the distributions $P_{i}(h)$ is reviewed in [15].

Despite difficulties in finding the saddle point, it is easy to see that the spin-glass solution is stable against ferromagnetic fluctuations. Indeed, the explicit computation of the replica Hessian matrix corresponding to free energy (2) shows that if $c(\vec{\sigma})$ is even, then the matrix is positive definite on the subspace of functions $v(\vec{\sigma})$ which are odd in at least one variable $(^{1})$.

We have used the method recently proposed in [15] which allows to determine the saddle point by a population dynamics of local fields. We have found that a nontrivial solution appears for $m=1$ below a certain dynamical temperature $T_{\mathrm{c}}$. This solution appears discontinuously (the fields are not small close to the transition). Below a temperature $T_{\mathrm{K}}$ this solution becomes thermodynamically relevant (letting aside the ferromagnetic state) and the saddle point value of $m$ is smaller than one (see inset of fig. 1). Between $T_{\mathrm{K}}$ and $T_{\mathrm{c}}$ the parameter $m$ sticks to one and the equilibrium free energy is that of the paramagnetic phase. This intermediate phase corresponds, as usually, to broken ergodicity with exponentially many ergodic components, *i.e.* extensive configurational entropy. For the case $k=3$ we

$(^{1})$The result holds more generally for diluted $p$-spin models for $p \geq 3$, while for $p=2$, the spin-glass solution exists, but is unstable against ferromagnetic fluctuations.

![](./images/812370178896560130_1.jpg)

Fig. 1

![](./images/812370178896560130_2.jpg)

Fig. 2

Fig. 1 – Average energy as a function of temperature for the ferromagnetic model with $k=3$.
The rightmost vertical lines are the analytic prediction for the ferromagnetic transitions, while the
leftmost vertical arrows are those for the spin-glass transitions. Continuous lines: results of simulated
annealing experiments (cooling rates from $10^2$ to $10^5$ MCS per $\Delta T=0.01$), where the magnetization
stays zero and the energy converges to the spin-glass threshold energy. Squares: static energy in the
glassy phase. Crosses: the system is initialized fully magnetized and then slowly heated. Data are
indistinguishable from the superimposed analytic curve. Inset: saddle point value for $m$ as a function
of temperature. The line is the fit $1.41T+0.138T^2$ to $T<T_{\text{K}}$ data.

Fig. 2 – Continuous (dashed) lines represent the static (dynamic) transition lines for a 3-spin model
with average connectivity $3\gamma$ calculated with a variational Ansatz. Upper (lower) lines refer to the
ferromagnetic (spin-glass) transition. Crosses (with errors): estimations of the critical lines from
Monte Carlo simulations. Squares: results of the algorithm which gives the exact 1-RSB solution.
Black dots on the $T=0$ axis mark the exact results for the ferromagnetic model.

have found $T_{\text{c}}=0.(5)745$ and $T_{\text{K}}=0.(5)660$, while the configurational entropy at $T_{\text{c}}$ equals
$S_{\text{Conf}}(T_{\text{c}})=0.(5)063$ and, as it should, vanishes at $T_{\text{K}}$.

A simple analytic approximation to this one-step RSB result can be obtained by a varia-
tional approximation. In replica language, one can use, for instance, an approximate form for
the order parameter $c(\vec{\sigma})$ of the type [16]

$$
c_{\text{rsb}}^{(\text{var})}(\vec{\sigma}) = \prod_{a=1}^{n/m} \frac{\int Du \exp\left[\beta\Delta u \sum_{b=(a-1)m+1}^{am} \sigma^b\right]}{\int Du(2\cosh\beta\Delta u)^m}, \tag{9}
$$

where $Du=du\exp[-u^2/2]/\sqrt{2\pi}$. The free-energy density resulting from this Ansatz has to
be optimized with respect to the variational parameters $\Delta$ and $m$. We find $T_{\text{c}}^{\text{var}}=0.752$
and $T_{\text{K}}^{\text{var}}=0.654$, which coincides well with the numerical solution of the exact saddle point
equation.

The temperature $T_{\text{c}}$ is a dynamical temperature where the relaxation times diverges and
the system becomes nonergodic, while the temperature $T_{\text{K}}$ is the Kauzmann temperature
where the system has a thermodynamic phase transition (as in many other cases the fact
that $T_{\text{c}}$ is different from $T_{\text{K}}$ is made possible by the mean-field nature of the problem [7]).
This spin-glass solution presents all the properties of the discontinuous spin-glasses in which

one-step RSB is exact [7]. However, we cannot exclude a second static transition with full replica symmetry breaking at a temperature even smaller than $T_{\rm K}$, as it happens in the fully connected Ising $p$-spin model [17].

Note also that the RSB solution for $c(\vec{\sigma})$ is even under reversal of all $n$ spins, and, thus, is also valid for the spin-glass version of the model, where couplings are set to $\pm 1$ randomly. The glassy and the paramagnetic phase turns out to be indistinguishable in both models.

In order to clarify the physical implications resulting from the existence of three saddle point solutions, we have performed Monte Carlo (MC) simulations. First of all we have determined $T_{\rm ms}$ as the maximum temperature at which the ferromagnetic state is locally stable. In fig. 1 the heating curves show the results of MC simulations —started a $T=0$ with all spins up— during which the temperature is slowly increased. The static transition temperature $T_{\rm fm}$ is determined as the point where the time spent by the simulation in the paramagnetic and in the ferromagnetic state are equal [9].

If we start, however, from a random configuration, the evolution of large systems ($N =$ 99999 in our simulations) is completely insensitive to the presence of a ferromagnetic ground state, the time to find it being exponentially large in the system size [14]. The system remains unmagnetized even if quenched below $T_{\rm fm}$, and may thus undergo only the glass transition. We have measured the stationary spin-spin correlation function, and have determined the critical point $T_{\rm c}$ from the divergence of the correlation time. The result $T_{\rm c}=0.(1)75$ is perfectly compatible with our analytical estimates. In this respect, the 3-spin ferromagnetic model with finite connectivity is completely different from any 2-spin unfrustrated model or any $p$-spin unfrustrated fully connected one. Indeed, in the latter cases the stability argument presented above does not hold and a simple coarsening dynamics pushes the system towards the unfrustrated ground state $(^2)$, thus ruling out the glassy off-equilibrium behaviour discussed above or in [9,10].

In fig. 1 we show the results of a set of cooling experiments on the unfrustrated model (identical curves have been obtained for the frustrated model). When the simulation goes through the ferromagnetic critical points (the 2 rightmost vertical lines) the system's evolution is completely unaffected, and the average magnetization stays near zero. The relaxation process is in fact strongly slowed down only when the spin-glass critical points are reached (marked by the 2 leftmost vertical arrows). Note also that below the spin-glass critical point the energy relaxation is almost absent and the asymptotic energy strongly depends on the cooling rate. Indeed the most effective relaxation is the one happening close to the critical point. All the above features are typical for structural glasses.

We have checked that some amount of disorder does not destroy the above picture, by studying a system with fluctuating connectivity, in which the set $E$ of hyper-edges contains $\gamma N$ randomly chosen triples $[i,j,k],\ i<j<k$. In this case the average connectivity $c=3\gamma$ can be varied continuously and critical lines in the $(\gamma,T)$ plane can be evaluated. Figure 2 summarizes our analytical and numerical findings on this model, which are in full qualitative agreement with those obtained in the case of a hyper-tree with fixed connectivity.

The analogy with supercooled liquids can be pushed forward once we identify the ferromagnetic ground state with the crystalline phase, the paramagnetic state with the liquid phase and the spin-glass state with the glassy phase. If we do not force the system towards the ferromagnetic ground state, below $T_{\rm fm}$ the system remains in the paramagnetic phase and it is thus supercooled. Decreasing further the temperature the system undergoes a glass transition, even if no quenched frustration is present. The frustration is self-induced by the

$(^2)$The same trivial dynamics applies to any unfrustrated model whose connectivity diverges with $N$, because thermal fluctuations in the magnetization are amplified, until the ground state is reached.

dynamics: being unable to find the ferromagnetic ground state, the system is typically in a configuration where a finite fraction of the interactions are unsatisfied and no long-range ferromagnetic order arises. Indeed, the ground state cannot be found (in polynomial time) by simply exploiting local information, the only one available when a spin is updated in a single spin-flip dynamics. We expect a long-lived glassy regime to be present also in short-range ver- sions of our model, where it should be destabilized by slow enucleation processes, as already seen in numerical simulation of some three-dimensional systems [9].

Spin-glasses were originally understood as intrinsically disordered and frustrated systems. A few years ago it was found that the disorder is not really necessary to induce a spin-glass phase [8]. We have shown here, studying diluted mean-field models, that quenched frustration is not necessary either. Our findings give a strong support to the use of disordered and frustrated models (e.g., $p$-spin-glasses) to describe structural glasses, which are by constitution neither disordered nor frustrated.

* * *

MW acknowledges the hospitality of the ICTP and SF that of the LPTMS. This research has been supported in part by the SPHINX project of the European Science Foundation.

## REFERENCES

[1] MÉZARD M., PARISI G. and VIRASORO M. *Spin Glass Theory and Beyond* (World Scientific, Singapore) 1987.
[2] KIRKPATRICK T. R. and THIRUMALAI D., *Phys. Rev. Lett.*, **58** (1987) 2091.
[3] YOUNG A. P. (Editor), *Spin Glasses and Random Fields* (World Scientific, Singapore) 1998.
[4] For a review, see, GÖTZE W., *Liquids, freezing and glass transition (Les Houches) 1989*, edited by HANSEN J. P., LEVESQUE D. and ZINN-JUSTIN J. (North Holland); ANGELL C. A., *Science*, **267** (1995) 1924.
[5] CRISANTI A., HORNER H. and SOMMERS H. J., *Z. Phys.*, **92** (1993) 173.
[6] CUGLIANDOLO L. F. and KURCHAN J., *Phys. Rev. Lett.*, **71** (1993) 173.
[7] BOUCHAUD J.-P., CUGLIANDOLO L. F., KURCHAN J. and MEZARD M., in [3].
[8] BOUCHAUD J. P. and MÉZARD M., *J. Phys. I*, **4** (1994) 1109; MARINARI E., PARISI G. and RITORT F., *J. Phys. A*, **27** (1994) 7615; 7647; FRANZ S. and HERTZ J., *Phys. Rev. Lett.*, **74** (1995) 2114.
[9] LIPOWSKI A. and JOHNSTON D., *Phys. Rev. E*, **61** (2000) 6375; SWIFT M. R., BOKIL H., TRAVASSO R. D. M. and BRAY A. J., *Phys. Rev. B*, **62** (2000) 11494.
[10] NEWMAN M. E. J. and MOORE C., *Phys. Rev. E*, **60** (1999) 5068; GARRAHAN J. P. and NEWMAN M. E. J., *Phys. Rev. E*, **62** (2000) 7670.
[11] RIEGER H. and KIRKPATRICK T. R., *Phys. Rev. B*, **45** (1992) 9772.
[12] VIANA L. and BRAY A. J., *J. Phys. C*, **18** (1985) 3037; KANTER I. and SOMPOLINSKY H., *Phys. Rev. Lett.*, **58** (1987) 164; MÉZARD M. and PARISI G., *Europhys. Lett.*, **3** (1987) 1067; DE DOMINICIS C. and MOTTISHAW P., *J. Phys. A*, **20** (1987) L1267; GOLDSCHMIDT Y. Y. and LAI P. Y., *J. Phys. A*, **23** (1990) L775; MONASSON R., *J. Phys. A*, **31** (1998) 513.
[13] BARRAT A. and ZECCHINA R., *Phys. Rev. E*, **59** (1999) 1299.
[14] RICCI-TERSENGHI F., WEIGT M. and ZECCHINA R., *Phys. Rev. E*, **63** (2001) 026702.
[15] MÉZARD M. and PARISI G., *Eur. Phys. J. B*, **20** (2001) 217.
[16] BIROLI G., MONASSON R. and WEIGT M., *Eur. Phys. J. B*, **14** (2000) 551.
[17] GARDNER E., *Nucl. Phys. B*, **257** (1985) 747.