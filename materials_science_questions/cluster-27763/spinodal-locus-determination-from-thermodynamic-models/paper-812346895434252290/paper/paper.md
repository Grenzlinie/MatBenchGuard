This article was downloaded by: [University of York]
On: 03 December 2014, At: 06:23
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered
office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](./images/812346895434252290_1.jpg)

Phase Transitions: A Multinational
Journal

Publication details, including instructions for authors and
subscription information:
http://www.tandfonline.com/loi/gpht20

The Bulk Viscosity of a Symmetrical
Lennard-Jones Mixture above and at
Liquid-liquid Coexistence: A Computer
Simulation Study

Subir K. Das , Jürgen Horbach & Kurt Binder

ª Institut für Physik , Johannes Gutenberg Universität , Staudinger
Weg 7, D - 55099 Mainz, Germany
Published online: 01 Feb 2007.

To cite this article: Subir K. Das , Jürgen Horbach & Kurt Binder (2004) The Bulk Viscosity of
a Symmetrical Lennard-Jones Mixture above and at Liquid-liquid Coexistence: A Computer
Simulation Study, Phase Transitions: A Multinational Journal, 77:8-10, 823-834, DOI:
10.1080/01411590410001690918

To link to this article: http://dx.doi.org/10.1080/01411590410001690918

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the
"Content") contained in the publications on our platform. However, Taylor & Francis,
our agents, and our licensors make no representations or warranties whatsoever as to
the accuracy, completeness, or suitability for any purpose of the Content. Any opinions
and views expressed in this publication are the opinions and views of the authors,
and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content
should not be relied upon and should be independently verified with primary sources
of information. Taylor and Francis shall not be liable for any losses, actions, claims,
proceedings, demands, costs, expenses, damages, and other liabilities whatsoever
or howsoever caused arising directly or indirectly in connection with, in relation to or
arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any
substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing,
systematic supply, or distribution in any form to anyone is expressly forbidden. Terms &

Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

**THE BULK VISCOSITY OF A SYMMETRICAL LENNARD-JONES MIXTURE ABOVE AND AT LIQUID-LIQUID COEXISTENCE: A COMPUTER SIMULATION STUDY**

SUBIR K. DAS*, JÜRGEN HORBACH and KURT BINDER

Institut für Physik, Johannes Gutenberg Universität, Staudinger Weg 7, D – 55099 Mainz, Germany

(Received 20 February 2004)

A Lennard-Jones model of a binary (AB) dense liquid with a symmetrical miscibility gap is investigated by means of computer simulation methods. Semigrand-canonical Monte Carlo simulations yield the phase diagram in the $T$–$x$ plane ($T$: temperature, $x$: concentration of A or B particles), as well as equilibrated configurations at coexistence. Then, we undertake molecular dynamics simulations which use these configurations to determine static properties (isothermal compressibility $\kappa_T$, and concentration susceptibility $\chi$), as well as the shear and bulk viscosities $\eta_{\rm s}$ and $\eta_{\rm B}$, respectively. The latter quantities are calculated along a path approaching the coexistence line from high temperatures in the one-phase region and ending at a state at the coexistence line about 15% below the critical point. We find that $\kappa_T$ and $\chi$ increase significantly near the coexistence line, reflecting the vicinity of the critical point. Whereas $\eta_{\rm s}$ exhibits a weak temperature dependence, $\eta_{\rm B}$ increases significantly near the coexistence curve.

*Keywords:* Lennard-Jones mixture; Semigrand-canonical Monte Carlo; Molecular dynamics; Shear and bulk viscosities

## 1. INTRODUCTION

The bulk viscosity (denoted by $\eta_{\rm B}$ in the following) describes the response of a fluid to a compression or expansion. Compared to other transport coefficients such as the shear viscosity or the self-diffusion constant, it is the least-studied transport coefficient. This is surprising since $\eta_{\rm B}$ is a central quantity in the description of the damping of longitudinal sound. It is also an important quantity to probe slow dynamic processes such as the critical slowing down near the critical point of a liquid–gas transition or the liquid–liquid unmixing transition in a binary fluid. We will briefly discuss these issues below.

A microscopic expression for $\eta_{\rm B}$ is given by a Green–Kubo (GK) formula (Boon and Yip, 1980),

$$
\eta_{\rm B} = \frac{V}{k_B T} \int_0^\infty \left\langle J_{\alpha\alpha}(t) J_{\alpha\alpha}(0) \right\rangle, \tag{1}
$$

*Corresponding author. E-mail: subir@uni.mainz.de

ISSN 0141-1594 print: ISSN 1029-0338 online © 2004 Taylor & Francis Ltd
DOI: 10.1080/01411590410001690918

with $\alpha$ denoting Cartesian components ($\alpha \in \{x, y, z\}$). $V$, $T$, and $k_{B}$ are volume, temperature and Boltzmann's constant, respectively. In the microcanonical ensemble, $J_{\alpha \alpha}$ is equal to the difference between the pressure at time $t$ and average pressure $<p>$, $J_{\alpha \alpha}(t)=p(t)-<p>$, where $p(t)$ is equal to the diagonal elements of the pressure tensor $\sigma$ defined as follows:

$$
\sigma_{\alpha \beta}=\frac{1}{V} \sum_{i=1}^{N}\left[m_{i} v_{i \alpha} v_{i \beta}+r_{i \alpha} F_{i \beta}\right]. \tag{2}
$$

Here $m_{i} v_{i \alpha}$ and $r_{i \alpha}$ are respectively the $\alpha$th component of momentum and position of particle $i$, and $F_{i \alpha}$ is the $\alpha$th component of the force acting on particle $i$. Note that in order to calculate the shear viscosity, $\eta_{\mathrm{s}}$, one has to use the nondiagonal elements of the pressure tensor in the Green-Kubo integral ($\alpha \neq \beta$) (Boon and Yip, 1980):

$$
\eta_{\mathrm{s}}=\frac{V}{k_{B} T} \int_{0}^{\infty} d t\left\langle\sigma_{\alpha \beta}(t) \sigma_{\alpha \beta}(0)\right\rangle. \tag{3}
$$

Eqs. (1), (2), and (3) can be used to calculate $\eta_{\mathrm{B}}$ and $\eta_{\mathrm{s}}$ from equilibrium fluctuations in a molecular dynamics (MD) computer simulation. Indeed, in one of the pioneering MD studies of a Lennard-Jones liquid near its triple point by Levesque *et al.* (1973), the viscosities were determined by GK formulas. Note that a recently proposed formula by Okumura and Yonezawa (2002) just expresses the pressure fluctuations in Eq. (1) in terms of the pair correlation function and the interatomic potentials.

Alternative methods to determine $\eta_{\mathrm{B}}$ are based on nonequilibrium molecular dynamics (NEMD) simulations. Heyes (1984) proposed a NEMD scheme where the volume of the system is changed from $V$ to $V+\Delta V$ at $t=0$ which leads to a change of the pressure. Then one follows the relaxation of the pressure to its equilibrium value $p(\infty)$ and measures $p(t)-p(\infty)$ where $p(t)$ is the instantaneous pressure at time $t$. $\eta_{\mathrm{B}}$ is then given by

$$
\eta_{\mathrm{B}}=-\frac{V}{\Delta V} \int_{0}^{\infty}[p(t)-p(\infty)] d t. \tag{4}
$$

Certainly, Eq. (4) is only valid if $\Delta V$ is small enough to allow the application of linear response theory.

Another NEMD approach was proposed by Hoover *et al.* (1980). The latter authors imposed a frequency-dependent small perturbation by changing the volume of the system by a periodic compression and expansion with a frequency $\omega$. As a result $\eta_{\mathrm{B}}(\omega)$ is obtained for several values of $\omega$ and then an extrapolation to zero frequency may be possible. The method of Hoover *et al.* might be especially useful for liquid states where the integrand in Eq. (4) exhibits a long-time tail. However, some knowledge of the frequency-dependence of $\eta_{\mathrm{B}}(\omega)$ is required to extrapolate it accurately from finite frequencies to zero.

The above methods have been mainly used in feasibility studies where the bulk viscosity was determined, e.g., for a Lennard-Jones fluid at a single state near its triple

point (see Levesque et al., 1973; Hoover et al., 1980; Heyes, 1984; Okumura and Yonezawa, 2002). Only in a small number of simulations, $\eta_{\mathrm{B}}$ has been investigated systematically. One of these rare studies is the MD simulation of symmetrical Lennard-Jones mixtures by Vogelsang and Hoheisel (Vogelsang and Hoheisel, 1988; Hoheisel, 1993) who considered systems of 256 particles at moderate densities (i.e., far from the triple point). In this work $\eta_{\mathrm{B}}$ as well as $\eta_{\mathrm{s}}$ were calculated by means of the GK formulas, Eqs. (1) and (3). An interesting result of this study was that the ratio $\eta_{\mathrm{B}} / \eta_{\mathrm{s}}$ is (much) larger than one if the fluid mixture has a (strongly) associating character or a (strongly) demixing character. In both of the latter cases the bulk visc- osity increases quickly whereas the shear viscosity remains essentially constant. As a consequence it is expected that $\eta_{\mathrm{B}}$ shows a strong increase near the coexistence line of a fluid-fluid unmixing transition.

In contrast to the small number of simulations, there are many theoretical investiga- tions of the bulk viscosity in the context of the dynamics near the liquid-gas critical point (Kadanoff and Swift, 1968; Swift, 1968; Kawasaki, 1976; Hohenberg and Halperin, 1977; Folk and Moser, 1995; Onuki, 1997, 2002). These works predict that the bulk viscosity exhibits a strong divergence near the critical point of a gas-liquid transition. In contrast to that, the shear viscosity is expected to show a very weak diver- gence (logarithmic divergence) at the critical point (if there is at all a divergence in this quantity). The latter predictions have been confirmed experimentally. An example is $^{3} He$ in the vicinity of the critical temperature $T_{c}$ : At $T / T_{c}-1=10^{-4}$ on the critical iso chore, $\eta_{B}$ is about 50 Poise whereas $\eta_{s}$ is equal to $17 \times 10^{-6}$ Poise (Kogan and Meyer,1998; Onuki, 2002).

In the present work we consider a simple model of a dense liquid mixture near and at a liquid-liquid unmixing transition and, apart from static susceptibilities, we calculate the shear and the bulk viscosity. Although we are not able to determine these quantities very close to the critical point, we find a behaviour which agrees qualitatively with the aforementioned theoretical predictions for the critical dynamics: $\eta_{B}$ shows a stronger increase than $\eta_{s}$ when approaching a state on the coexistence line about $15 \%$ below the critical point and, furthermore, at the latter point, $\eta_{B}$ is significantly larger than $\eta_{s}$, i.e., $\eta_{B} / \eta_{s} \simeq 3.3$.

In the next section, we briefly comment on the details of the simulation as well as the Lennard-Jones model and its phase diagram. The static properties and the transport coefficients (shear and bulk viscosity) as obtained from the simulation are then pre- sented in Section 3. Finally we summarize the results in Section 4.

## 2. MODEL AND PHASE DIAGRAM

The model that we consider in this work is a binary Lennard-Jones (LJ) mixture. Thus,the interaction potential between a particle of type $\alpha$ and a particle of type $\beta$ (α, β ∈ {A, B}) is given by

$$
u_{\alpha \beta}(r)=4 \epsilon_{\alpha \beta}\left[\left(\frac{\sigma_{\alpha \beta}}{r}\right)^{12}-\left(\frac{\sigma_{\alpha \beta}}{r}\right)^{6}\right],\tag{5}
$$

$r$ being the distance between the two particles. For the Lennard-Jones parameters $\epsilon_{\alpha \beta}$ and $\sigma_{\alpha \beta}$ we choose $\sigma_{\mathrm{AA}}=\sigma_{\mathrm{BB}}=\sigma_{\mathrm{AB}}=\sigma, \epsilon_{\mathrm{AA}}=\epsilon_{\mathrm{BB}}=\epsilon$ and $\epsilon_{\mathrm{AB}}=\delta \epsilon$. Lengths, energies, and temperatures are measured respectively in units of $\sigma \equiv 1, \epsilon \equiv 1$, and $\epsilon / k_{B} \equiv 1$. In the MD simulations, equal masses are chosen for A and B particles, i.e., $m_{\mathrm{A}}=m_{\mathrm{B}}=1$. The potential is truncated and shifted at $r=2.5 \sigma$.

The model mixture that we have defined so far is obviously completely symmetrical. Whether it has the tendency toward association or demixing is controlled by the parameter $\delta$. We use $\delta=0.5$ which implies the possibility of a fluid-fluid unmixing transition. Since we are interested in the dense liquid state we have chosen a density $\rho \sigma^{3}=1$, which provides the absence of crystallization in the temperature range of interest, $T>1.0$. Note that for densities $0 \leq \rho \leq 0.7$ the phase behaviour of symmetrical LJ mixtures have been extensively investigated by Wilding (1997).

The simulations were done as follows. We started with a random mixture with an equal number of A and B particles. By using standard Monte Carlo (MC) in the canonical ensemble with trial displacements of particles in the range $[-\sigma / 20,+\sigma / 20]$, we equilibrated the system for $10^{5}$ Monte Carlo steps (MCS) per particle. Then, we switched on a MC simulation in the semigrand-canonical ensemble, i.e., at the end of each displacement sweep an identity switch of $N / 10$ randomly chosen particles was attempted, $A \rightarrow B$ or $B \rightarrow A$ ($N$ being the total number of particles). Note that in the Metropolis criterion of the semigrand-canonical moves, the chemical potential energy difference $\pm \Delta \mu=\mu_{\mathrm{A}}-\mu_{\mathrm{B}}$ ($\mu_{\alpha}$: chemical potential of species $\alpha \in\{\mathrm{A}, \mathrm{B}\}$) has to be taken into account in addition to the energy change in the Boltzmann factor. In order to localize the coexistence curve of the liquid-liquid unmixing transition in the present case, one has to just set $\Delta \mu=0$ which is simply due to the symmetry of our model. In order to determine the phase diagram, we have performed five independent runs with a length of 400000 MCS per particle where we started the averaging after 100000 MCS in each run (for more details of this calculation, see (Das et al., 2003)).

Figure 1 shows the phase diagram in the $T-x_{\mathrm{B}}$ plane for the system sizes $N=400,800,1600$, and 3200 ($x_{\mathrm{B}} \equiv N_{\mathrm{B}} / N$ is the concentration of $B$ particles). Due to the symmetry of the model we know a priori that the critical point is located at $x_{\mathrm{B}}=0.5$. As we can infer from Fig. 1, the finite size effects near the critical point are small for $N \geq 400$, and for $N \geq 1600$ the data agree within the statistical errors. We have estimated the critical temperature $T_{\mathrm{c}}$ from power law fits according to the three-dimensional Ising universality class (Binder and Ciccotti, 1996; Binder and Heermann, 2002),

$$
f\left(x_{\mathrm{B}}\right)=0.5 \pm x_{\mathrm{B}}^{\mathrm{coex}}=\hat{B}\left(1-\frac{T}{T_{\mathrm{c}}}\right)^{\beta}, \quad \beta \simeq 0.325,
\tag{6}
$$

where $\hat{B}$ is a critical amplitude which is used, as well as $T_{\mathrm{c}}$, as a fitting parameter. From the fits with Eq. (6) we obtain $T_{\mathrm{c}} \simeq 1.638 \pm 0.005$ for $N \geq 1600$. For a more accurate estimate of $T_{\mathrm{c}}$, we would have to perform a finite-size scaling analysis (Binder and Ciccotti, 1996; Binder and Heermann, 2002).

Apart from the phase diagram, the MC in the semigrand-canonical ensemble also yields equilibrated configurations exactly along the coexistence line. We used them as starting configurations for MD simulations to determine the static quantities and the

![](./images/812346895434252290_2.jpg)

FIGURE 1 Phase diagram of the symmetrical Lennard-Jones mixture for four choices of $N$ as indicated. The crosses at $x_{\mathrm{B}}=0.10375$ mark the states for which the structure and dynamics was investigated (note that also $T=3.0$ and 6.0 were studied). The solid lines are fits with Eq. (6) and the dashed lines are just guides to the eye.

transport coefficients that are presented in the next section. In the MD, the equations of motion were integrated by means of the velocity Verlet algorithm (Binder and Ciccotti, 1996) with a time-step $\delta t=0.01$ [in units of the time $t_{0}=(m \sigma^{2}/(48 \epsilon))^{1/2}$].

The starting points for the MD simulations are the configurations with 1600 particles at $T=1.4$ that correspond to the concentration $x_{\mathrm{B}}=0.10375$ at the coexistence line. Configurations in the one-phase region at the latter value of $x_{\mathrm{B}}$ were obtained by heating up the system and equilibrating it for $10^{5}$ time-steps at constant temperature with the use of an Andersen thermostat (Das et al., 2003). Then, microcanonical runs were added from which we computed the static and dynamic quantities that are shown in the next section. The path along which we determined the latter quantities is indicated in Fig. 1 by crosses: apart from the coexistence state at $T=1.4$, which is about $15\%$ below the critical point with respect to temperature, the temperatures $T=1.6, 1.7, 3.0$, and 6.0 were analyzed (note that other paths around the coexistence line are studied in Das et al., 2003).

One may wonder why we have not studied states that are much closer to the critical point. However, due to the diverging correlation length that is accompanied by the approach of the critical point, we would have to consider systems that contain many more than 1600 particles as in our work. Furthermore, the critical slowing down would require very long runs to equilibrate the system and to determine the transport coefficients with reasonable error bars. The latter point is especially a severe problem for transport coefficients such as the shear or the bulk viscosity. These are collective quantities and require many independent runs and/or a long time averaging since they are not subject to a self-averaging as one-particle quantities such as the self-diffusion constant. However, compared to many previous works, our choice of $N$ is relatively large. Even the very recent computation of the bulk viscosity by Okumura and Yonezawa (2002) was only done for a small system of 256 particles.

## 3. RESULTS

In this section, we present the results for the static and dynamic properties of the symmetrical LJ system along the path in the phase diagram which is indicated in Fig. 1. As described in the previous section, we have generated first five independent configurations at each temperature. All these configurations were used as initial configurations for microcanonical MD runs over 4.8 million time-steps (the time-step was 0.01 $t_0$, see previous section). Thus, at each temperature 24 million time-steps were done to determine the quantities of interest. As we shall see in the following, this effort was large enough to get a reasonable estimate of bulk and shear viscosities.

### 3.1. Static Properties

As we see in Fig. 1 the states at $T=1.4$ on the coexistence line are about 15% below the critical point with respect to temperature. Although these points are not very close to the critical point one may expect that the approach of the critical point is reflected in thermodynamic quantities such as the isothermal compressibility $\kappa_T$ and the concentration susceptibility $\chi$ (defined below).

The quantity $\kappa_T$ can be calculated from the static number–number density structure factor $S_{\text{nn}}(q)$ in the limit of wavenumber $q\rightarrow0$ (Hansen and McDonald, 1986),

$$
\kappa_{T}=\frac{1}{\rho k_{B} T} \lim _{q \rightarrow 0} S_{\mathrm{nn}}(q),\tag{7}
$$

with $\rho$ being the total density of the system (in our case $\rho$ as well as the Boltzmann constant $k_B$ are equal to one). The structure factor $S_{\text{nn}}(q)$ for a binary AB mixture is defined by Hansen and McDonald (1986),

$$
S_{\mathrm{nn}}(q)=S_{\mathrm{AA}}(q)+2 S_{\mathrm{AB}}(q)+S_{\mathrm{BB}}(q),\tag{8}
$$

where $S_{\alpha\beta}(q)$ ($\alpha,\beta\in[A,B]$) are the partial structure factors,

$$
S_{\alpha \beta}(q)=\frac{f_{\alpha \beta}}{N} \sum_{i, j}\left\langle\exp \left[i \mathbf{q} \cdot\left(\mathbf{r}_{i}^{\alpha}-\mathbf{r}_{j}^{\beta}\right)\right]\right\rangle,\tag{9}
$$

with $f_{\alpha\beta}=0.5$ for $\alpha\neq\beta$ and $f_{\alpha\beta}=1.0$ for $\alpha=\beta$. In Eq. (9) the indices $i,j$ run over the number of particles of species $\alpha$ and $\beta$, respectively, and $\mathbf{r}_i^\alpha$ is the position of the $i$th particle of species $\alpha$.

Figure 2 shows $S_{\text{nn}}(q)$ for $T=1.4,1.7,3.0$, and 6.0. For wavenumbers $q$ that correspond to distances smaller than or equal to the typical nearest-neighbour distance, say $q>5$, the typical behaviour of this quantity for simple dense liquids can be identified: Upon decreasing the temperature the amplitude, especially of the first peak, increases and the peaks become narrower. The small values of $S_{\text{nn}}(q)$ for $q\rightarrow0$ reflect the fact that the considered dense liquid state is hardly compressible. It might be surprising that even at coexistence $S_{\text{nn}}$ does not show any tendency to increase significantly for $q\rightarrow0$. The amplitude of $S_{\text{nn}}(q)$ at small $q$ appears to be even a monotonic decreasing

![](./images/812346895434252290_3.jpg)

FIGURE 2 Number-number density structure factor $S_{\rm nn}(q)$ for the four indicated temperatures. The inset shows the isothermal compressibility $\kappa_T$ as a function of temperature. $\kappa_T$ is estimated from the extrapolated value $S_{\rm nn}(q=0)$ (see Eq. (7)).

function with decreasing temperature. However, the relevant thermodynamic quantity in our context is $\kappa_T$, that we have extracted from $S_{\rm nn}(q)$ by extrapolating this function to $q=0$. As we see in the inset of Fig. 2, $\kappa_T$ increases significantly with decreasing temperature which shows that for states around $T=1.4$, long-ranged static correlations, i.e., the presence of the critical point, still affect the behaviour of $\kappa_T$.

The vicinity of the critical point is more pronounced in the structure factor of the concentration densities, $S_{\rm cc}(q)$, than in $S_{\rm nn}(q)$. $S_{\rm cc}(q)$ can be also expressed by a linear combination of the partial structure factors (Hansen and McDonald, 1986), i.e.,

$$
S_{\rm cc}(q) = x_{\rm B}^2 S_{\rm AA}(q) - 2x_{\rm A}x_{\rm B}S_{\rm AB}(q) + x_{\rm A}^2 S_{\rm BB}(q). \tag{10}
$$

In the limit $q \to 0$ the structure factor $S_{\rm cc}(q)$ is related to the static concentration susceptibility $\chi$ by

$$
\chi = \frac{1}{k_B T} \lim_{q \to 0} S_{\rm cc}(q). \tag{11}
$$

Note that we have determined $\chi$ directly via a fluctuation relation by semigrand- canonical MC runs (see Das et al., 2003). So, it was not necessary to extrapolate $S_{\rm cc}(q)$ to $q=0$. As we see in Fig. 3 this would be a difficult task because, in contrast to $S_{\rm nn}(q)$, $S_{\rm cc}(q)$ steeply increases for $q \to 0$. As we can infer from the inset of Fig. 3, $\chi$ is about a factor of 2 larger at the coexistence state at $T=1.4$ than at $T=1.8$. It is remarkable that $S_{\rm cc}(q)$ exhibits almost no temperature dependence for $q>5$ in the broad temperature range $1.4 \leq T \leq 6.0$.

![](./images/812346895434252290_4.jpg)

FIGURE 3 Concentration-concentration density structure factor $S_{cc}(q)$ for the four indicated temperatures. The inset shows the concentration susceptibility $\chi$ as function of temperature (see text).

### 3.2. Bulk Viscosity and Shear Viscosity

For the computation of the bulk and shear viscosities we have used the GK formulas, Eqs. (1) and (3). The alternative methods that are based on NEMD require essentially the same computational effort. Furthermore, in the Heyes method, see Eq. (4), one has to choose the perturbation $\Delta V$ small enough to ensure that this perturbation justifies the application of linear response theory. Thus, one has to study the dependence of the measured bulk viscosity $\eta_{\mathrm{B}}$ on $\Delta V$ (of course, in the linear response regime the apparent $\eta_{\mathrm{B}}$ is independent of $\Delta V$ ). The Hoover method has in addition the drawback that one has to extrapolate the frequency-dependent viscosity to zero frequency. However, a comparative study of the different NEMD and GK methods to measure transport coefficients in a simulation is an interesting future project since the NEMD methods may give additional physical insight into the microscopic mechanism of different transport processes.

Figure 4 shows $\eta_{\mathrm{s}}(t)$ and $\eta_{\mathrm{B}}(t)$ for four temperatures. These quantities are defined by Eqs. (1) and (3) where one has to replace $\infty$ in the integral by $t$. We see that $\eta_{\mathrm{s}}(t)$ and $\eta_{\mathrm{B}}(t)$ indeed approach plateaus at long times the values of which correspond to the hydrodynamic shear and bulk viscosities, respectively. At low temperatures, there is a qualitative difference in $\eta_{\mathrm{B}}(t)$ as compared to $\eta_{\mathrm{s}}(t)$, e.g., at $T=1.4$, $\eta_{\mathrm{s}}(t)$ is essentially constant for $t>10$. In contrast to that, $\eta_{\mathrm{B}}(t)$ exhibits a second strong increase and it reaches the plateau value for $t>300$. This is due to a long-time tail in the autocorrelation function of the pressure fluctuations. Note that the decrease of $\eta_{\mathrm{B}}(t)$ for $t>500$ is due to the fact that the statistics is much worse at long times.

The quantities $\eta_{\mathrm{B}}$ and $\eta_{\mathrm{s}}$ are plotted in Fig. 5(a) as a function of inverse temperature. Whereas $\eta_{\mathrm{s}}$ exhibits only a very weak temperature-dependence, $\eta_{\mathrm{B}}$ increases significantly in the vicinity of the coexistence state at $T=1.4$. As we can see in Fig. 5(b) the ratio $\eta_{\mathrm{B}} / \eta_{\mathrm{s}}$ is in the whole considered temperature range $6.0 \geq T \geq 1.4$ above

![](./images/812346895434252290_5.jpg)

FIGURE 4 (a) "Time-dependent" shear viscosity $\eta_{\mathrm{s}}(t)$ for the indicated temperatures. From the long-time plateau we read off $\eta_{\mathrm{s}}$. (b) Same as in (a), but now for the bulk viscosity.

![](./images/812346895434252290_6.jpg)

FIGURE 5 (a) Shear and bulk viscosity as a function of inverse temperature. (b) Ratio $\eta_{\mathrm{B}}/\eta_{\mathrm{s}}$ as a function of temperature.

one, and it reaches a value of about 3.3 at $T=1.4$. One expects such a behaviour from theories of the critical dynamics of the liquid–gas transition (Onuki, 2002). According to these theories, the long-ranged critical fluctuations cause a slowing down of the system's response to a compression or expansion (described by $\eta_{\mathrm{B}}$). On the other hand, the response to the shearing of the system is hardly affected by the critical fluctuations (and thus $\eta_{\mathrm{s}}$). In our case, at a state about $15\%$ below the critical point, there is already a significant increase of static correlations which makes the behaviour of $\eta_{\mathrm{B}}/\eta_{\mathrm{s}}$ plausible.

Since the data presented in this article are taken at an off-critical concentration, one could also attempt to interpret them in terms of a singular behaviour at the spinodal temperature $T_{\mathrm{s}}$ (limit of metastability) (Binder, 1987). According to the mean-field theory of symmetric binary mixtures, one should expect that the static concentration susceptibility $\chi$ for $x_{\mathrm{B}} < x_{\mathrm{B}}^{\mathrm{crit}}=0.5$ behaves as

$$
\chi(T, x_{\mathrm{B}}) \propto [T-T_{\mathrm{s}}(x_{\mathrm{B}})]^{-1} \tag{12}
$$

where near the critical temperature the spinodal temperature $T_{\mathrm{s}}(x_{\mathrm{B}})$ is the inverse function of the concentration $x_{\mathrm{B}}^{\mathrm{s}}(T)$ along the spinodal curve, given by the equation $x_{\mathrm{B}}^{\mathrm{s}}(T)-x_{\mathrm{B}}^{\mathrm{crit}}=(x_{\mathrm{B}}^{\mathrm{coex}}-x_{\mathrm{B}}^{\mathrm{crit}})/\sqrt{3}$ (Binder, 1987). Further away from $T_{\mathrm{c}}$, a simple expression for $T_{\mathrm{s}}(x_{\mathrm{B}})$ exists for the lattice (Ising) model of symmetric binary mixtures, namely

$$
x_{\mathrm{B}}^{\mathrm{s}}(T)=\frac{1}{2}\left(1 \pm \sqrt{1-\frac{T}{T_{\mathrm{c}}^{\mathrm{MF}}}}\right). \tag{13}
$$

Here we have emphasized by this notation that the mean-field estimate $T_{\mathrm{c}}^{\mathrm{MF}}$ of the critical temperature for systems with short range forces normally exceeds the actual critical temperature distinctly (also Eq. (12) then does not hold for $x_{\mathrm{B}}$ near $x_{\mathrm{B}}^{\mathrm{crit}}$ and $T$ near the actual critical temperature, since $\chi(T, x_{\mathrm{B}}^{\mathrm{crit}}) \propto (T-T_{\mathrm{c}})^{-\gamma}$, where the actual susceptibility exponent $\gamma \simeq 1.24$ (Binder and Ciccotti, 1996; Binder and Heermann, 2002)).

Although we do not really expect that Eq. (12) and a related mean-field divergence for the bulk viscosity $\eta_{\mathrm{B}}$ is a good approximation for our Lennard–Jones system, we present a plot of $\chi^{-1}$ vs. $T$ and $\eta_{\mathrm{B}}^{-1}$ vs. $T$ in Fig. 6. Mean-field theory would predict that the data fall on straight lines, and both straight lines should hit the abscissa in the same point which then is the estimate of $T_{\mathrm{s}}(x_{\mathrm{B}})$. Indeed the data which points close to the coexistence curve are compatible with such analysis, with $T_{\mathrm{s}}(x_{\mathrm{B}}) \simeq 1$. Of course, one should not put too much weight on this analysis, since the temperature range over which we need to extrapolate is larger than the temperature range where actual data are fitted. Also the estimate from Eq. (13) would be much lesser, namely $T_{\mathrm{s}}(x_{\mathrm{B}}) \simeq 0.59$, if the distinction between the actual $T_{\mathrm{c}}$ and $T_{\mathrm{c}}^{\mathrm{MF}}$ is ignored. We caution the reader that the concept of a spinodal is of doubtful validity outside of mean-field theory (Binder, 1987), although in the experimental literature on binary mixtures (both in metallic alloys and in polymer blends, for instance) it is widely used.

![](./images/812346895434252290_7.jpg)

FIGURE 6 Mean-field type extrapolation toward the spinodal. The solid lines are fit to the data sets by using the functional form in Eq. (12).

## 4. SUMMARY

We have used computer simulations to investigate transport coefficients of a dense symmetrical Lennard-Jones mixture that were calculated along a path toward a liquid-liquid miscibility gap ending at a coexistence state about 15% below the critical point. The main result of our study is that the bulk viscosity $\eta_B$ increases significantly near the coexistence state whereas the shear viscosity $\eta_s$ does not show any change near coexistence. $\eta_s$ remains to exhibit a very weak temperature-dependence also when it passes the coexistence line. The behaviour of $\eta_B$ and $\eta_s$ can be qualitatively understood by theories of critical dynamics (see Onuki, 2002).

In future studies we plan to compute the transport properties closer to the critical point. Of course, in such studies much larger system sizes than those used in this work have to be considered. Moreover, the emergence of critical slowing down requires simulations on much longer time-scales.

### Acknowledgments

The present research was supported by the Deutsche Forschungsgemeinschaft (DFG) under Grant No. Bi314/18 (SPP 1120). Horbach acknowledges the support of the DFG under Grants No. HO 2231/2-1 and HO 2231/2-2.

### References

Binder, K. (1987). Theory of first order phase transitions. *Rep. Prog. Phys.*, **50**, 783.

Binder, K. and Ciccotti, G. (Eds.) (1996). *Monte Carlo and Molecular Dynamics of Condensed Matter Systems*. Italian Physical Society, Bologna.

Binder, K. and Heermann, D.W. (2002). *Monte Carlo Simulations in Statistical Physics. An Introduction*, 4th Edn. Springer, Berlin.

Boon, J.P. and Yip, S. (1980). *Molecular Hydrodynamics*. McGraw Hill, New York.

Das, S.K., Horbach, J. and Binder, K. (2003). Transport phenomena and microscopic structure in partially miscible binary fluids: a simulation study of the symmetrical Lennard-Jones mixture. J. Chem. Phys., 119, 1547.

Folk, R. and Moser, G. (1995). Nonuniversal dynamical crossover in pure and binary fluids near a critical point. Phys. Rev. Lett., 75, 2706.

Hansen, J.P. and McDonald, I.R. (1986). *Theory of Simple Liquids*. Academic, London.

Heyes, D.M. (1984). J. Chem. Soc., Faraday Trans., 80, 1363.

Hoheisel, C. (1993). *Theoretical Treatment of Liquids and Liquid Mixtures*, pp. 292-300. Elsevier, Amsterdam.

Hohenberg, P.C. and Halperin, B.I. (1977). Theory of dynamic critical phenomena. Rev. Mod, Phys., 49, 435.

Hoover, W.G., Evans, D.J., Hickman, R.B., Ladd, A.J.C., Ashurst, W.T. and Moran, B. (1980). Lennard- Jones triple-point bulk and shear viscosities. Green-Kubo theory, Hamiltonian mechanics, and nonequi- librium molecular dynamics. Phys. Rev. A, 22, 1690.

Kadanoff, L.P. and Swift, J. (1968). Transport coefficients near the liquid-gas critical point. Phys. Rev.,166, 89.

Kawasaki, K. (1976). Mode coupling and critical dynamics. In: Domb, C. and Green, M.S. (Eds.), Phase Transitions and Critical Phenomena, Vol. 5A, pp. 166-405. Academic Press, London.

Kogan, A.B. and Meyer, H. (1998). Sound propagation in $^3$He and $^4$He above the liquid-vapor critical point. J. Low Temp. Phys., 110, 899.

Levesque, D., Verlet, L. and Kürkijarvi, J. (1973). Computer "experiments" on classical fluids. IV. Transport properties and time-correlation functions of the Lennard-Jones liquid near its triple point. Phys. Rev. A, 7, 1690.

Okumura, H. and Yonezawa, F. (2002). New formula for the bulk viscosity constructed from the interatomic potential and the pair distribution function. J. Chem. Phys., 116, 7400.

Onuki, A. (1997). Dynamic equations and bulk viscosity near the gas-liquid critical point. Phys. Rev. E,55, 403.

Onuki, A. (2002). Phase Transition Dynamics, p. 247. Cambridge University Press, Cambridge.

Swift, J. (1968). Transport coefficients near the consolute temperature of a binary liquid mixture. Phys. Rev.,173, 257.

Vogelsang, R. and Hoheisel, C. (1988). Thermal transport coefficients including the Soret coefficient for various liquid Lennard-Jones mixtures. Phys. Rev. A, 38, 6296.

Wilding, N.B. (1997). Critical end point behaviour in a binary fluid mixture. Phys. Rev. E, 55, 6624.