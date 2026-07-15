# Nature of the glassy transition in simulations of the ferromagnetic plaquette Ising model

S. Davatolhagh, D. Dariush, and L. Separdar

Department of Physics, College of Sciences, Shiraz University, Shiraz 71454, Iran

(Received 21 October 2009; revised manuscript received 13 January 2010; published 1 March 2010)

The homogeneous plaquette Ising model in two and three dimensions is investigated by means of Monte Carlo simulations. By introducing a suitable order parameter for the two-dimensional lattice, and the finite-size scaling of the corresponding fourth-order cumulant, it is found that, consistent with the previous theoretical indications, the model in two dimensions is disordered at finite temperature and exhibits a zero-temperature phase transition characteristic of the one-dimensional Ising model with an essential (exponential) singularity of the order-parameter susceptibility as opposed to a Curie-law (power-law) divergence. In three dimensions, however, the model is believed to have a first-order phase transition at $T_c \simeq 3.6$ screened by strong metastability leading to a so-called "glassy transition" at $T \simeq 3.4$ when subjected to slow cooling. By computing the configurational entropy $S_c \equiv S(\text{liquid}) - S(\text{crystal})$ in the supercooled temperature range via thermodynamic integration of the internal energy results, the Kauzmann temperature defined as that temperature where the extrapolated configurational entropy $S_c(T)$ vanishes, is estimated to be $T_K \simeq 3.18$. By finding ways to estimate the equilibration time of the supercooled liquid and the nucleation time of the stable crystal droplets, it is shown that $T \simeq 3.4$ is indeed the limit of stability or the *effective spinodal temperature* $T_{\text{sp}}$, at which the two time scales associated with the quasiequilibration of the supercooled liquid, $\tau_{\text{eq}}$, and the nucleation of the stable crystal droplets, $\tau_{\text{nuc}}$, cross one another, with the former rising above the latter such that the supercooled liquid state becomes physically irrelevant below $T_{\text{sp}} \simeq 3.4$ and the impending entropy crisis at $T_K \simeq 3.18$ ($< T_{\text{sp}}$) is thus avoided. Hence, what is sometimes called "glassy temperature," is really a kinetic spinodal temperature that may be regarded as the remnant of the mean-field spinodal.

DOI: 10.1103/PhysRevE.81.031501
PACS number(s): 64.70.P−, 05.50.+q

## I. INTRODUCTION

On cooling a liquid, it may either undergo a first order crystallization transition at the melting point, or else the liquid will become supercooled for temperatures below the melting point, becoming more viscous with decreasing temperature, and eventually falling out of equilibrium, thus, forming a glass [1]. In fact, the liquid is said to have fallen out of equilibrium at a glass transition temperature $T_g$, as a result of the crossing of two time scales: one associated with the structural changes that bring about the relaxation of the liquid, and the other with the duration of the experiment (observation time) that is set by the cooling rate. Clearly, the laboratory glass transition is a kinetic phenomenon as the glass formation temperature $T_g$ depends on the cooling rate, and is sometimes accompanied by a jump in the specific heat due to the freezing of the kinetic degrees of freedom at $T_g$. The slower the cooling, the larger is the region, for which the liquid may be supercooled, and the lower is the glass transition temperature [2]. Although the crystal phase is the most stable below the melting point, the supercooled liquid may be regarded as a metastable equilibrium state.

From a theoretical point of view, however, a certain class of mean field spin glass models with multispin interactions, also known as the $p$-spin glasses, exhibit characteristic behavior in common with the structural glasses [3–6]. Despite their success in reproducing some of the structural glass phenomenology [7], such models contain quenched-in disorder at the level of the Hamiltonian, as a result of which they do not present a crystalline ground state. In these models, the frustration arises from the quenched-in disorder rather than the inherent complex dynamics of the system. It is therefore useful to have homogeneous lattice models that self-induce disorder and behave in some respects like glasses [8–14]. The homogeneous plaquette Ising model, also known as the Lipowski model, is a special case of a more general class of models for interacting surfaces first proposed in the context of lattice field theories [15]. The ferromagnetic plaquette Ising model (FPIM) is represented by the following homogeneous Hamiltonian, involving four-spin interactions on elementary plaquettes of a hypercubic lattice,

$$
H=-J \sum_{[i j k l]} S_i S_j S_k S_l, \tag{1}
$$

where, $S_i = \pm 1$ are Ising spins. The model is characterized by a large ground-state degeneracy $\sim 2^{dL}$ for a hypercubic lattice of linear size $L$ in $d$ dimensions, such that flipping all the spins in any plane of the hypercubic lattice, and the many conceivable permutations of the lattice-plane flips, leave the Hamiltonian invariant. The ground state entropy density, however, is zero in the thermodynamic limit. The static properties of the three-dimensional (3D) FPIM have been studied in some detail in the context of the glass transition, as it is known to exhibit a first order transition in equilibrium analogous to crystal melting at $T_c \simeq 3.6$, and an extremely long-lived metastable supercooled liquid state followed by a jump in the specific heat at a lower temperature $T \simeq 3.4$ when subjected to slow cooling [11]. Furthermore, from the dynamical point of view, the model has many characteristic features in common with the structural glasses: (i) the stretched exponential relaxation of two-time autocorrelation functions, described by $f(t)=\exp[-(t/\tau)^\beta]$, with a temperature-dependent parameter $\beta < 1$, (ii) a relaxation time, $\tau$, that appears to diverge at a finite temperature, and (iii) a low-temperature

glassy aging regime [12]. However, there still remain funda- mental questions as to the precise nature of the so-called glassy transition at $T \simeq 3.4$, as pointed out in the following.

From another perspective, the glass transition in liquids is often associated with an entropy crisis, first discovered by Simon [16], emphasized by Kauzmann [17], and elaborated by, among others, Adam, Gibbs, and Di Marzio [18]. Accord- ing to this picture, a liquid when supercooled is approaching a situation where the entropy of the metastable liquid may become lower than that of the stable crystal, which is rather unphysical as the amorphous liquid structure must be at a higher entropy in comparison with the ordered equilibrium crystal, and if this situation were to continue (on lowering the temperature further) the entropy of the liquid becomes negative at some finite temperature, thus, violating the third law of thermodynamics. This scenario, referred to as the en- tropy crisis, is found to be the primary mechanism behind glass transition in mean field $p$ -spin glass models [3-6]. Hence, the Kauzmann temperature $T_{K}$ , where the extrapo lated excess entropy of the liquid over the equilibrium crystal(also known as the configurational entropy [19]) appears to vanish, is often regarded as a lower bound to the limit of stability of a supercooled liquid, or the lowest temperature to which a liquid can possibly be supercooled before a thermo- dynamic glass transition intervenes [20]. Thus, the configu- rational entropy can be an important clue to the behavior of a glass forming system [21]-a quantity that has been so far ignored in the literature of 3D FPIM. This is what we intend to investigate in our Monte Carlo (MC) simulations of the3D model. Furthermore, by finding ways to estimate the equilibration time of the liquid and the nucleation time of the stable crystal droplets, it is shown that what is sometimes called the glassy temperature is indeed the kinetic spinodal temperature $T_{sp}$ (as suggested in [12,14]) at which the two time-scales associated with the quasiequilibration of the su- percooled liquid, $\tau_{eq }$ , and the nucleation of the stable crystal droplets, $\tau_{nuc }$ , cross one another, with the former rising above the latter such that the supercooled liquid state becomes physically irrelevant below $T_{sp} \simeq 3.40$ and the impending en tropy crisis at $T_{K} \simeq 3.18(<T_{sp})$ is avoided. We also investi gate the model in two dimensions by introducing a suitable order parameter, thus finding that (consistent with some of the previous theoretical indications [22]) the model is disor- dered but exhibits a zero-temperature phase transition char- acteristic of the one-dimensional Ising model.

In the following, we shall adopt a set of natural units where the coupling strength $J$ , the Boltzmann constant $k_{B}$ , and the lattice spacing $a$ , are all taken as unity. The time is measured in units of Monte Carlo step (MCS), which corre- sponds to one complete lattice update.

The rest of this paper is organized as follows. In Sec. II, the thermodynamics of the two-dimensional (2D) FPIM is studied by means of MC simulation. In Sec. III, the 3D FPIM is considered, with its effective spinodal discussed in Sec. IV. The paper is concluded with a summary in Sec. V.

## II. THERMODYNAMICS IN TWO DIMENSIONS

The thermodynamics of the FPIM in two dimensions, is sometimes assumed to be as trivial as that exhibited by a paramagnetic ensemble of independent spins, characterized by a Curie-law (power-law) divergence of the susceptibility[10]. On the other hand, there are theoretical indications as to the presence of a zero-temperature phase transition [22], characterized by essential (exponential) singularities of the correlation length and the susceptibility at $T=0$ . In this sec tion, we present an independent investigation of the thermo- dynamic properties of the 2D FPIM by means of MC simu- lation. The ferromagnetic plaquette Ising model in two dimensions consists of a system of Ising spins located on the vertices of a square lattice, and interacting through four-body plaquette interactions, as in Eq. (1). Here the usual magneti- zation, defined as a sum over the Ising spins, is not a good order parameter due to the layered structure of the ground state, as pointed out in the introduction. However, a suitable order parameter involving the product of two nearest- neighbor spins on the same row of the square lattice, allows for a clear demonstration by MC simulations of the thermo- dynamic behavior exhibited by the 2D FPIM, which is found to be precisely the same as the one-dimensional Ising model with nearest neighbor interactions [23], as also indicated by some of the earlier theoretical results [22].

To this end, we define the Ising-like variable $\tau_{i j} \equiv S_{i} S_{j}$  $(= \pm 1)$ , where $S_{i}$ and $S_{j}$ are nearest neighbor spins on the same row (or, alternatively, the same column) of the square lattice. As it turns out, a suitable order parameter is defined by summing over all such pairs,
$$m=\left\langle\sum \tau_{i j}\right\rangle / N.\qquad(2)$$

In order to obtain the static properties of the 2D FPIM, we have simulated square lattices of size $N=L^{2}$ with helical boundary conditions for three different linear sizes $L=5,10$ , and 40 using the standard metropolis Monte Carlo [24]. In our simulations of the bulk properties, the helical boundary conditions are employed to reduce the edge effects. At low temperatures, the system was allowed up to $10^{5}$ Monte Carlo steps for equilibration, and the data points were then accu- mulated by averaging over up to $10^{6}$ accumulation MCS. The accumulation stage was divided into 10 bins, and the binned averages were used to estimate the statistical errors. The results for the usual thermodynamic properties, the order parameter $m$ defined by Eq. (2), the corresponding suscepti bility
$$\chi=N\left(\left\langle m^{2}\right\rangle-\langle m\rangle^{2}\right) / T,\qquad(3)$$
the internal energy per spin
$$E=\langle H\rangle / N,\qquad(4)$$
and the specific heat
$$C=\left(\left\langle H^{2}\right\rangle-\langle H\rangle^{2}\right) / N T^{2},\qquad(5)$$
for a system of linear size $L=40$ are reported in Figs. 1 and2, together with the corresponding thermodynamic functionsof the one-dimensional Ising model shown as solid curves: $m=0 \ (T>0), \ \chi=\exp (2 / T) / T, \ E=-\tanh (1 / T), \ $ and $C$ =sech2(1/T)/T2. The susceptibility and the specific heat are obtained from the fluctuations of the order parameter and the internal energy, respectively. Evidently, there is good agree-

![](./images/811802300673687553_1.jpg)

FIG. 1. The MC results for the order parameter $m$, defined by Eq. (2), and the corresponding susceptibility $\chi$ for a 2D FPIM lattice of linear size $L$=40, are plotted as a function of the temperature. The susceptibility is obtained from the order parameter fluctuations. The curves are the corresponding thermodynamic functions of the 1D Ising model.

![](./images/811802300673687553_2.jpg)

FIG. 2. The internal energy per spin $E$, and the specific heat $C$ for a 2D FPIM system of linear size $L$=40 are plotted as a function of the temperature. The specific heat is obtained from the energy fluctuations. The curves are the corresponding thermodynamic functions of the 1D Ising model.

ment except at the lowest temperatures where some discrepancy is expected as a result of the extremely large equilibration times, and the glassy single-spin-flip dynamics the 2D FPIM is known to exhibit at low temperatures [25]. In order to ascertain the low-temperature behavior of the 2D FPIM, particularly in the thermodynamic limit of the infinite lattice size, we have calculated the fourth-order cumulant

$$
U_{L}(T)=1-\frac{\left\langle m^{4}\right\rangle}{3\left\langle m^{2}\right\rangle^{2}}, \quad (6)
$$

for three different system sizes as shown in Fig. 3. In fact one may anticipate three different scenarios of a continuous phase transition [26]: (i) a finite temperature phase transition to an ordered phase at a critical temperature $T_{c}$, (ii) a finite critical temperature followed by a line of critical points at lower temperatures, the prime example of which is the Berezenskii-Kosterlitz-Thouless phase transition, (iii) a zero temperature phase transition such that the susceptibility and the correlation length diverge exponentially as $T \to 0$, as in the one-dimensional Ising model. Indeed one may employ the fourth-order cumulant $U_{L}(T)$, due to Binder [27], in order to distinguish between the different scenarios [26]. In case (i), the $U_{L}(T)$ curves as a function of the temperature intersect at $T_{c}$, independent of the lattice size $L$, and splay out at lower temperatures with the larger $L$'s having the larger (lower) values below (above) $T_{c}$ such that in the thermodynamic limit of $L \to \infty$ the cumulant tends to a step function with a jump discontinuity of two-thirds at $T_{c}$. In case (ii), the $U_{L}(T)$ curves as a function of the temperature come together at $T_{c}$ and stay together at lower temperatures, consistent with a line of critical points. In case (iii), however, the curves merge to a common value of two-thirds as soon as the temperature is such that the correlation length $\xi \gg L$, but the data for increasingly larger system sizes merge to this common value at progressively lower temperatures. From Fig. 3, it is evident that the latter is the most relevant as far as the 2D

![](./images/811802300673687553_3.jpg)

FIG. 3. Plot of the fourth-order cumulant vs temperature for various system sizes of the 2D FPIM. Clearly, the curves are consistent with the case where there is a zero temperature phase transition in the thermodynamic limit of infinite lattice size.

FPIM is concerned. In this case $U_L(T)$ is a step function in the limit $L \to \infty$ with its discontinuity at $T$=0. Despite the simple thermodynamics, interestingly, the 2D FPIM is known to exhibit nontrivial glassy single-spin-flip dynamics characterized by superArrhenius relaxation times, and a glassy aging regime at low temperatures [25].

### III. GLASSY TRANSITION IN THREE DIMENSIONS

The static and dynamic properties of the 3D FPIM have been studied in some detail as pointed out in the introduction. However, there still remain fundamental questions as to the precise nature of the so-called glassy temperature, and concerns about an impending entropy crisis that need to be addressed. We perform MC simulations to compute the thermodynamic properties of the model. It should be noted that magnetization is not a good order parameter due to the lamellar configurations of the ground state, and the order parameter introduced for the model in two dimensions cannot be generalized. Therefore, much of the investigation will focus on thermodynamic properties as the internal energy, the specific heat, the free energy, and the all important configurational entropy that has been so far ignored in the relevant literature.

We have simulated simple cubic lattices of linear size $L$=50, and 80 with periodic boundary conditions and sequential spin-flip sweeps through the lattice. The sequential spin-flip sweeps (as opposed to random spin flip), enables us to simulate larger systems than reported before. This is crucial as the critical droplet radius for homogeneous crystal nucleation is estimated to be 25 lattice spacings just below the melting temperature [12]. Hence, the simulated systems must be large enough to accommodate stable droplets of the ground state. Our results correspond to cooling experiments of the liquid (or heating of the crystal), with linear protocol $T=T_{\rm init}-rt$, where $r=|dT/dt|$ is the cooling rate and $T_{\rm init}$ is the initial temperature corresponding to either the high temperature liquid phase, or the low temperature crystal. In order to check the accuracy of our data, we compared our preliminary results with the extensive literature available on the subject [11].

The energies of the crystal, the liquid, the supercooled liquid, and the so-called glassy state of the 3D FPIM are shown in Fig. 4 as a function of the temperature, for the largest system size simulated $L$=80, and the lowest rate $r$=$2.0\times 10^{-7}$. The lines through the data points are fit functions for the metastable supercooled liquid (LQ), and the equilibrium crystal (CR),
$$
E_{\mathrm{LQ}}(T)=-a \tanh \left[b /\left(T-T^{*}\right)^{d}\right],\qquad(7)
$$
where the best fit parameters are found to be $a$=-13.9, $b$=0.07, $T^{*}$=3.13, and $d$=0.34; and
$$
E_{\mathrm{CR}}=E_{\mathrm{GS}}+c T^{n},\qquad(8)
$$
with $c=2.63\times 10^{-7}$ and $n$=9.63 as best fit parameters, and $E_{\rm GS}$=-3.0 is the ground state energy. Similar fits have been employed before in the context of the glassy behavior exhibited by a homogeneous lattice model with multispin interactions known as the homogeneous coupled two-level systems [14].

![](./images/811802300673687553_4.jpg)

FIG. 4. The internal energies per spin of the liquid, the supercooled liquid, the glassy, and the crystal phase of a 3D FPIM system of linear size $L$=80 as a function of the temperature. The solid line is an extrapolation of the quasiequilibrium liquid energy, as per Eq. (7), and the broken line is a fit through the equilibrium crystal energy as of Eq. (8).

Similarly, the specific heats of the crystal, the liquid, the supercooled liquid, and the so-called glassy state of the 3D FPIM are shown in Fig. 5. Evidently, there is a significant jump in the specific heat of the liquid at the so-called glassy temperature $T$$\simeq$3.40, thus, characterizing the liquid as fragile. This fragility is consistent with the dynamics of the model studied in [12], where a detailed study of the energy autocorrelation function in the supercooled temperature range, reveals that the relaxation time of the liquid can be well fit by a power-law divergence, thus making it appear fragile in an Angell's plot [28].

In order to find the free energies, and, subsequently, the entropies of the liquid and crystal phases, we make use of the thermodynamic integration formula,
$$
\beta F(\beta)=\beta_{0} F\left(\beta_{0}\right)+\int_{\beta_{0}}^{\beta} d \beta^{\prime} E\left(\beta^{\prime}\right),\qquad(9)
$$
where, $\beta=1/T$ is the reciprocal temperature, $\beta_0$=0 for the liquid phase, and $\beta_0=\infty$ for the crystal [14]. On substituting

![](./images/811802300673687553_5.jpg)

FIG. 5. The specific heats of the liquid, the supercooled liquid, the glassy, and the crystal phase of a 3D FPIM lattice of linear size $L$=80, plotted as a function of the temperature. The liquid appears fragile as there is a significant jump in the specific heat.

$E_{\mathrm{CR}}$ from Eq. (8) in the thermodynamic integration formula, Eq. (9), the free-energy density of the crystal as a function of the temperature is obtained,

$$
F_{\mathrm{CR}}(T)=E_{\mathrm{GS}}-\frac{c}{n-1} T^{n}. \tag{10}
$$

A direct substitution of $E_{\mathrm{LQ}}$ from Eq. (7) into Eq. (9), however, does not produce the desired free energy of the liquid, as Eq. (7) is merely an approximation meant to extrapolate the quasiequilibrium supercooled liquid energy to lower temperatures: the approximation breaks down at high temperatures. The thermodynamic integral for the liquid is thus accumulated in three stages: (i) For high temperatures ($0 \leq \beta$ $\leq 0.1$), the linear approximation $E \simeq-3.2 \beta$ is used to find the integrated area under the $E(\beta)$ curve. This approximation is validated by the high temperature expansion studies [29]. (ii) In the intermediate temperature range ($0.1 \leq \beta \leq 2.5$), the Monte Carlo results for $E(\beta)$ are integrated numerically using the Simpson's rule. (iii) At low temperatures ($\beta>2.5$), Eq. (7) is used to represent the energy of the liquid, and to extrapolate the equilibrium liquid energy down to lower temperatures. Indeed, a calculation of the free-energy densities of the liquid and crystal phases on these lines, allows for an independent determination of the melting point $T_{c}$ by requiring $F_{\mathrm{LQ}}(T_{c})=F_{\mathrm{CR}}(T_{c})$. The result is identical with that already reported in [11], namely, $T_{c} \simeq 3.60$. Once the free energies are known as a function of the temperature, one can simply find the entropies through the thermodynamic relation, $S(T)=[E(T)-F(T)] / T$. Finally, the Kauzmann temperature can be estimated by equating the (extrapolate) liquid and the crystal entropy densities, $S_{\mathrm{LQ}}(T_{K})=S_{\mathrm{CR}}(T_{K})$. The result is

$$
T_{K} \simeq 3.18. \tag{11}
$$

The configurational entropy $S_{c} \equiv S_{\mathrm{LQ}}-S_{\mathrm{CR}}$, is another important quantity for the thermodynamic and the structural characterization of the supercooled liquids as pointed out in the introduction. It is also believed to be intimately related to the dynamics of the liquid, most notably, through the Adam-Gibbs relation for the structural relaxation time [18]. The configurational entropy of the liquid for the 3D FPIM is shown in Fig. 6. $S_{c}(T_{c})$ is the entropy of fusion. Evidently, the configurational entropy at $T=3.40$, is a substantial fraction of the entropy of fusion, and the extrapolated configurational entropy appears to vanish at the Kauzmann temperature $T_{K} \simeq 3.18$.

Fig. 7 shows our results for the cooling experiments of different rates on a lattice of linear size $L=50$ with periodic boundary conditions. The solid line is the extrapolated equilibrium liquid energy, as per Eq. (7). Evidently, by reducing the cooling rate, the system enters states of lower energy. Furthermore, the observation that for temperatures below $T$ $=3.40$ the curves of cooling rates $r \geq 10^{-3}$ stay above the equilibrium liquid energy, and those with $r \leq 2.0 \times 10^{-4}$ fall below the equilibrium energy, is indicative of the fact that the equilibration time $\tau_{\text {eq }}$ of the supercooled liquid at $T$ $=3.40$ must be between $r_{>}^{-1}=10^{3}$ MCS and $r_{<}^{-1}=5 \times 10^{3}$ MCS, or $10^{3}<\tau_{\text {eq }}<5 \times 10^{3}$ at $T=3.40$. As it turns out, this is of the same order of magnitude as the nucleation time, $\tau_{\text {nuc }}$, of the stable crystal droplets at $T=3.40$, as discussed in the next section.

![](./images/811802300673687553_6.jpg)

FIG. 6. The configurational entropy densities of liquid and supercooled liquid states of a 3D FPIM system of linear size $L=80$, as a function of the temperature. The point at which the extrapolated configurational entropy appears to vanish, $T_{K} \simeq 3.18$, is known as the Kauzmann temperature.

## IV. DISCUSSION

The dynamic properties of the 3D FPIM have been investigated in [12]. A detailed study of the two-time energy autocorrelation function in the supercooled temperature range together with attempted fits to the stretched exponential functions of the form $A(t)=A_{0} \exp \left[-(t / \tau)^{\beta}\right]$, reveals that the relaxation time $\tau(T)$ increases sharply as the temperature is reduced, and can fit accurately a power-law divergence $\tau(T)=2.23 /(T-3.39)$ [12]. The equilibration time $\tau_{\text {eq }}(T)$, defined as that time-scale over which the memory function $A(t)$ becomes negligibly small, is proportional to $\tau$ and of the order $\tau_{\text {eq }} \simeq 20 \tau$. Thus, an independent estimate for the equilibration time at $T=3.40$ is obtained such that $\tau_{\text {eq }} \simeq 20 \tau$ $\simeq 4400$ MCS. Indeed, this is of the same order as our esti-

![](./images/811802300673687553_7.jpg)

FIG. 7. The energy results in cooling experiments of different rates for a 3D FPIM system of linear size $L=50$, are shown as a function of the temperature. The solid line is the extrapolated quasiequilibrium liquid energy. Evidently, by reducing the cooling rate the system enters states of lower energy.

mate for $\tau_{\text{eq}}$ at $T$=3.40, based on the cooling experiments shown in Fig. 7 and presented in Sec. III.

Furthermore, an estimate for the crystal nucleation time $\tau_{\text{nuc}}$ at a reference temperature $T_{\text{ref}}$=3.50 (i.e., midway inside the supercooled temperature range), is given in [12] based on the standard nucleation theory. This was meant to explain the strong metastability displayed by the 3D FPIM as the nucleation time at $T_{\text{ref}}$ is found to be extremely high: $\tau_{\text{nuc}}(T_{\text{ref}})$ $\sim 10^{25}$ MCS. Indeed, the standard nucleation theory in dimensions $d$=3, predicts that the activated crystal nucleation time must vary with the temperature as

$$
\tau_{\text{nuc}}(T)=\tau_{0} \exp \left[\frac{4 A^{3} \sigma^{3}(T)}{27 B^{2} \delta F^{2}(T) T}\right]
\tag{12}
$$

where, $\sigma(T)$ is the surface tension between the stable and the metastable phases, $\delta F(T)$ is the difference in the bulk free-energy densities, and $\tau_{0}$ is a high-$T$ microscopic time-scale [30]. $A$ and $B$ are constants characterizing the geometrical shape of the droplets (for spherical droplets $A$=$4\pi$, and $B$=$4\pi/3$). Thus, in order to estimate $\tau_{\text{nuc}}$ at $T$=3.40 from its known value, $\tau_{\text{nuc}}(T_{\text{ref}}) \sim 10^{25}$ MCS, one needs to know the temperature dependence of the free-energy difference $\delta F(T)$, and that of the surface tension $\sigma(T)$. The free energy difference can simply be obtained from the free energy data, where close to the melting point it can be well approximated by $\delta F(T) \simeq 0.5(T_{c}-T)$. As for the surface tension, it is sometimes assumed to depend weakly on the temperature and taken to be a constant. However, in a supercooled glassforming liquid, there are certain mechanisms that tend to "renormalize" the surface tension from its assumed constancy [31]. Thus, the surface tension separating a glassy cluster of linear size $\xi$ from the liquid background, is believed to be renormalized due to the exponentially large number of the glassy phases (that may nucleate inside one another), and to scale with the typical cluster size as $\sigma$ $\sim \xi^{-(d-2)/2}$, where the linear cluster size has a temperature dependence $\xi \sim (T-T_{K})^{-\nu}$ with an exponent $\nu \geq 2/d$ [31]. There are good reasons to believe that a more precise value of $\nu$ must be unity [32], rather than the lower bound $\nu$=2/$d$ predicted by the mean field theory [31]. This is based on the reasoning that mean field theories tend to underestimate the correlation length exponents, and that $\nu$=2/$d$ predicts glassy clusters that are significantly smaller than those actually observed in experiments near $T_{g}$ [33]. Thus, with $\nu$=1 [32], the surface tension is found to vary with the temperature as

$$
\sigma(T) \sim\left(T-T_{K}\right)^{d-2 / 2}.
\tag{13}
$$

Hence, in estimating the crystal nucleation time of 3D FPIM at $T$=3.40 from that at a reference temperature $T_{\text{ref}}$=3.50, one must not only take the temperature variation of the free energy difference $\delta F(T)$=$0.5(T_{c}-T)$ into account, but also that of the renormalized surface tension $\sigma(T) \sim (T-T_{K})^{1/2}$, in $d$=3 dimensions. In going from the reference temperature $T_{\text{ref}}$=3.50 to the so-called glassy temperature $T$=3.40, the free energy difference is doubled, $\delta F(T)/\delta F(T_{\text{ref}})$=2, while the surface tension is reduced by about %17, $\sigma(T)/\sigma(T_{\text{ref}})$=0.83. As the exponent in Eq. (12), depends on the second power of $\delta F$, and the third power of $\sigma$, the nucleation time at $T$=3.40 is reduced drastically from its value at $T_{\text{ref}}$. In fact, we find $\tau_{\text{nuc}} \simeq 4600$ MCS at $T$=3.40, which is indeed comparable to our estimate for $\tau_{\text{eq}} \approx 4400$ MCS at the same temperature,

$$
\tau_{\text{eq}}(T=3.40) \simeq \tau_{\text{nuc}}(T=3.40).
\tag{14}
$$

The effective spinodal temperature $T_{\text{sp}}$, by definition, is that temperature at which $\tau_{\text{eq}}(T_{\text{sp}})$=$\tau_{\text{nuc}}(T_{\text{sp}})$. Thus, the supercooled liquid state in 3D FPIM reaches its limit of stability at a temperature that must be more precisely called an effective/ kinetic spinodal temperature $T_{\text{sp}}$, rather than a glassy temperature $T_{g}$, as by definition $T_{g}$ is a cooling rate dependent temperature and the anomaly at $T$=3.40 clearly does not qualify. $T_{\text{sp}}$ as defined above is of course independent of the cooling rate. As $\tau_{\text{eq}}$ rises above $\tau_{\text{nuc}}$ below $T_{\text{sp}}$, the supercooled liquid can no longer equilibrate, and the system is dominated by fast nucleation of tiny droplets of the many crystalline ground states. This also is the reason why in Fig. 4 the supercooled liquid energy suddenly drops to a value close to that of the equilibrium crystal at $T_{\text{sp}}$=3.40. Evidently, the supercooled phase of the 3D FPIM loses stability at $T_{\text{sp}}$, as a result of which the impending entropy crisis at $T_{K}$ ($<T_{\text{sp}}$) is avoided. Below $T_{\text{sp}}$, however, the system is believed to enter an off-equilibrium dynamics regime, akin to glassy aging [12], where fast crystal nucleation is followed by extremely slow activated growth of the many mismatched droplets of the competing crystalline ground states [14]. In such a situation, a mixture of many mismatched tiny crystallites becomes kinetically indistinguishable from a truly disordered glass. This limit of stability, however, may prove impossible to observe in laboratory experiments if the equilibration time at $T_{\text{sp}}$ is larger than the observation time such that the glass transition temperature exceeds the effective spinodal temperature [14], a situation similar to that depicted by the curves of cooling rate $r \geq 10^{-3}$ in Fig. 7.

### V. SUMMARY
The ferromagnetic plaquette Ising model in two and three dimensions is investigated by means of MC simulations. By introducing a suitable order parameter in two dimensions, it is indeed shown that the 2D FPIM exhibits a zero-temperature phase transition characterized by exponentially diverging susceptibility and correlation length.

The nature of the so-called glassy transition in 3D FPIM is clarified: it is indeed the case that what is sometimes called glassy temperature, is really a kinetic spinodal temperature independent of the cooling rate that may be viewed as the remnant of the mean-field spinodal as suggested in [12,14]. By extrapolating the configurational entropy of the liquid, the Kauzmann temperature is estimated to be $T_{K} \simeq 3.18$. Furthermore, by finding ways to estimate the equilibration time of the supercooled liquid $\tau_{\text{eq}}$, and the nucleation time of the stable crystal droplets $\tau_{\text{nuc}}$ at $T$=3.40, it is argued that $T$=3.40 must be more precisely interpreted as an effective spinodal temperature, $T_{\text{sp}}$, at which the two time-scales associated with the quasiequilibration of the supercooled liquid, and the nucleation of the stable crystal droplets, cross one


another, with the former rising above the latter such that the supercooled liquid state becomes physically irrelevant below $T_{sp}$=3.40 and the impending entropy crisis at $T_K$=3.18 ($<T_{sp}$) is avoided.

Based on scaling arguments [31], and certain phenomenological considerations [32], a temperature dependence for the surface tension separating a glassy cluster from the liquid background, Eq. (13), is obtained for the supercooled glass-forming liquids that appears to work well for fragile liquids in three dimensions, such as the 3D FPIM, as well as those in two dimensions, in particular, the 2D coupled two-level systems for which Eq. (13) predicts a constant surface tension, which is assumed and shown to work in [14].

[1] S. R. Elliott, *Physics of Amorphous Materials*, 2nd ed. (Longman Scientific, London, 1990).

[2] M. D. Ediger, C. A. Angell, and S. R. Nagel, J. Phys. Chem. 100, 13200 (1996); P. G. Debenedetti, *Metastable liquids* (Princeton University Press, Princeton, 1996).

[3] B. Derrida, Phys. Rev. B 24, 2613 (1981); D. J. Gross and M. Mezard, Nucl. Phys. B 240, 431 (1984).

[4] T. R. Kirkpatrick and P. G. Wolynes, Phys. Rev. A 35, 3072 (1987); T. R. Kirkpatrick and D. Thirumalai, Phys. Rev. Lett. 58, 2091 (1987).

[5] A. Crisanti, H. Horner, and H. J. Sommers, Z. Phys. B 92, 257 (1993).

[6] L. F. Cugliandolo and J. Kurchan, Phys. Rev. Lett. 71, 173 (1993).

[7] T. R. Kirkpatrick and D. Thirumalai, Transp. Theory Stat. Phys. 24, 927 (1995); A. Crisanti and F. Ritort, Physica A 280, 155 (2000).

[8] J. P. Bouchaud and M. Mezard, J. Phys. I (France) 4, 1109 (1994); E. Marinari, G. Paris, and F. Ritort, J. Phys. A 27, 7615 (1994).

[9] J. D. Shore and J. P. Sethna, Phys. Rev. B 43, 3782 (1991).

[10] A. Lipowski, J. Phys. A 30, 7365 (1997).

[11] D. Espriu, M. Baig, D. A. Johnston, and R. P. C. K. Malmini, J. Phys. A 30, 405 (1997); A. Lipowski and D. A. Johnston, ibid. 33, 4451 (2000); A. Lipowski and D. A. Johnston, Phys. Rev. E 61, 6375 (2000).

[12] M. R. Swift, H. Bokil, R. D. M. Travasso, and A. J. Bray, Phys. Rev. B 62, 11494 (2000).

[13] S. Franz, M. Mezard, F. Ricci-Teresenghi, M. Weigt, and R. Zecchina, Europhys. Lett. 55, 465 (2001).

[14] A. Cavagna, I. Giardina, and T. S. Grigera, Europhys. Lett. 61, 74 (2003); J. Chem. Phys. 118, 6974 (2003).

[15] G. K. Savvidy and F. J. Wegner, Nucl. Phys. B 413, 609 (1994).

[16] F. E. Simon, Z. Anorg. Allgemein. Chem. 203, 217 (1931).

[17] W. Kauzmann, Chem. Rev. 43, 219 (1948).

[18] G. Adam and J. H. Gibbs, J. Chem. Phys. 43, 139 (1965); J. H. Gibbs and E. A. DiMarzio, ibid. 28, 373 (1958).

[19] In this paper, we do not distinguish between the configurational entropy, i.e., the entropic contribution due to the presence of an exponentially large number of different glassy states, and the excess entropy of the liquid over the crystal as the two are believed to be proportional [20].

[20] C. A. Angell and S. Borick, J. Non-Cryst. Solids 307-310, 393 (2002).

[21] P. G. Wolynes, J. Res. Natl. Inst. Stand. Technol. 102, 187 (1997).

[22] G. K. Savvidy and K. G. Savvidy, Phys. Lett. B 324, 72 (1994).

[23] E. Ising, Z. Phys. 31, 253 (1925).

[24] See, e.g., D. P. Landau and K. Binder, *A Guide to Monte Carlo Simulations in Statistical Physics*, 2nd ed. (Cambridge University Press, Cambridge, 2005).

[25] A. Buhot and J. P. Garrahan, Phys. Rev. Lett. 88, 225702 (2002).

[26] N. Kawashima and A. P. Young, Phys. Rev. B 53, R484 (1996).

[27] K. Binder, Phy. Rev. Lett. 47, 693 (1981); Z. Phys. B 43, 119 (1981).

[28] C. A. Angell, J. Non-Cryst. Solids 102, 205 (1988); Science 267, 1924 (1995).

[29] K. Farakos and G. K. Savvidy, Mod. Phys. Lett. A 14, 1753 (1999).

[30] See, e.g., F. F. Abraham, *Homogeneous Nucleation Theory* (Academic, New York, 1974).

[31] T. R. Kirkpatrick, D. Thirumalai, and P. G. Wolynes, Phys. Rev. A 40, 1045 (1989); X. Xia and P. G. Wolynes, Phys. Rev. Lett. 86, 5526 (2001).

[32] S. Davatolhagh, Eur. Phys. J. B 59, 291 (2007); J. Phys.: Condens. Matter 17, S1275 (2005).

[33] L. Berthier *et al.*, Science 310, 1797 (2005); M. D. Ediger, Annu. Rev. Phys. Chem. 51, 99 (2000).