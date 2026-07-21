![](./images/812721638599557120_1.jpg)

# Atomistic analysis of the vacancy mechanism of impurity diffusion in silicon
S. List and H. Ryssel

Citation: *Journal of Applied Physics* **83**, 7585 (1998); doi: 10.1063/1.367874
View online: http://dx.doi.org/10.1063/1.367874
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/83/12?ver=pdfcov
Published by the AIP Publishing

## Articles you may be interested in
[Millisecond flash lamp annealing of shallow implanted layers in Ge](http://)
Appl. Phys. Lett. **95**, 252107 (2009); 10.1063/1.3276770

[Vacancy-impurity complexes and diffusion of Ga and Sn in intrinsic and p -doped germanium](http://)
Appl. Phys. Lett. **91**, 091922 (2007); 10.1063/1.2778540

[Effect of fluorine implantation dose on boron thermal diffusion in silicon](http://)
J. Appl. Phys. **96**, 4114 (2004); 10.1063/1.1790063

[Accurate measurements of the intrinsic diffusivities of boron and phosphorus in silicon](http://)
Appl. Phys. Lett. **77**, 1976 (2000); 10.1063/1.1313248

[Atomistic modeling of high-concentration effects of impurity diffusion in silicon](http://)
J. Appl. Phys. **83**, 7595 (1998); 10.1063/1.367875

![](./images/812721638599557120_2.jpg)

[This article is copyrighted as indicated in the article. Reuse of AIP content is subject to the terms at: http://scitation.aip.org/termsconditions. Downloaded to ] IP:
129.120.242.61 On: Sat, 29 Nov 2014 22:37:02

# Atomistic analysis of the vacancy mechanism of impurity diffusion in silicon

S. List
Lehrstuhl für Elektronische Bauelemente, Universität Erlangen-Nürnberg,
Cauerstrasse 6, 91058 Erlangen, Germany

H. Ryssela
Lehrstuhl für Elektronische Bauelemente, Universität Erlangen-Nürnberg,
Cauerstrasse 6, 91058 Erlangen, Germany and Fraunhofer-Institut für Integrierte Schaltungen,
Schottkystrasse 10, 91058 Erlangen, Germany

(Received 30 May 1997; accepted for publication 10 March 1998)

The complete set of the four macroscopic transport coefficients describing the coupled diffusion of impurity atoms and vacancies in silicon is calculated from the atomistic mechanism by accurately taking into account the effects of the microscopic forces between dopants and vacancies. The aim of these simulations is to come to a decision concerning the validity of models like the pair diffusion model [e.g., M. Yoshida, J. Appl. Phys. 48, 2169 (1977); R. B. Fair and J. C. C. Tsai, J. Electrochem. Soc. 124, 1107 (1977); F. F. Morehead and R. F. Lever, Appl. Phys. Lett. 48, 151 (1986); B. J. Mulvaney and W. B. Richardson, Appl. Phys. Lett. 51, 1439 (1987)] or the ‘‘non-Fickian diffusion’’ model [M. Kurata, Y. Morikawa, K. Nagami, and H. Kuroda, Jpn. J. Appl. Phys. 12, 472 (1973); Y. Morikawa, K. Yamamoto, and K. Nagami, Appl. Phys. Lett. 36, 997 (1980); V. V. Kozlovski, V. N. Lomasov, and L. S. Vlasenko, Radiat. Eff. 106, 37 (1988); O. V. Aleksandrov, V. V. Kozlovski, V. V. Popov, and B. E. Samorukov, Phys. Status Solidi 110, K61 (1988), K. Maser, Exp. Tech. Phys. (Berlin) 34, 213 (1986), K. Maser, Ann. Phys. (Leipzig) 45, 81 (1988), K. Maser, Exp. Tech. Phys. (Berlin) 39, 169 (1991)] that make contradicting predictions for very fundamental properties like the relative direction of the fluxes of dopants and vacancies driven by a vacancy gradient and for the relation $\alpha=T_{d}^{0}/D_{d}^{0}$ between two of the four transport coefficients. Simulation results are shown for a variety of assumed interaction potentials that establish a functional dependence between $\alpha$ and measurable quantities, like the factor $D_{d}/D_{\text{tracer}}$ of enhancement of dopant diffusivity over tracer diffusion, that holds for an arbitrary interaction. The comparison with experimental values for $D_{d}/D_{\text{tracer}}$ leads to confirmation of the pair diffusion model for boron and phosphorous. For arsenic and antimony, the large scatter of the experimental data prohibits an equally definite conclusion, but at least a qualitative confirmation of pair diffusion theory (i.e., $\alpha>0$ which means that dopant and vacancy fluxes have the same direction if caused by a vacancy gradient) is possible. © 1998 American Institute of Physics. [S0021-8979(98)00612-4]

## I. INTRODUCTION

Although it is widely accepted that dopant atoms diffuse in silicon with the help of point defects, i.e., vacancies and interstitials, there is still a large amount of disagreement about the details of the microscopic diffusion mechanisms as well as about the correct formulation of the phenomenological diffusion equations on the macroscopic scale. For diffusion via the vacancy mechanism, there has even been a long lasting controversy $^{1–8}$ about very fundamental properties such as the relative direction of the fluxes of dopants and vacancies that are driven by a vacancy gradient (see below) since, contrary to diffusion via interstitial related mechanisms, the elementary step of the vacancy mechanism involves an exchange of the positions of vacancies and diffus- ing atoms. The analysis presented here aims at resolving this latter controversy. As a starting point, we will first address the general form of the macroscopic equations for the coupled diffusion of dopants and vacancies as dictated by thermodynamics. Next we will briefly discuss the disagreeing models found in the literature for the parameters of these equations.

The laws of irreversible thermodynamics $^{9}$ give the following general form of the equations for the flux densities $\mathbf{J}_{d}$ and $\mathbf{J}_{v}$ of dopants and vacancies if gradients of the chemical potentials $\mu_{d}$ and $\mu_{v}$ of dopants and vacancies act as driving forces:
$$-\mathbf{J}_{d}=T^{AA}\nabla \mu_{d}+T^{AB}\nabla \mu_{v},\tag{1}$$

$$-\mathbf{J}_{v}=T^{BA}\nabla \mu_{d}+T^{BB}\nabla \mu_{v}.$$

The coefficients $T^{AA}$, $T^{AB}$, $T^{BA}$, and $T^{BB}$ form the so-called transport matrix which is symmetric (i.e., $T^{BA}=T^{AB}$) under very general conditions for microscopic forces. $^{9}$ Expressing $\mu_{d}$ and $\mu_{v}$ as functions of the concentrations $C_{d}$ and $C_{v}$ of dopants and vacancies and performing the corresponding lin-

aElectronic mail: ryssel@iis-b.fhg.de

ear transformation of the transport matrix, we obtain the more usual expressions for the fluxes depending on the particle profiles:
$$
\begin{aligned}
& -\mathbf{J}_{d}=D_{d}\left(C_{d}, C_{v}\right) \nabla C_{d}+T_{d}\left(C_{d}, C_{v}\right) \nabla C_{v}, \\
& -\mathbf{J}_{v}=T_{v}\left(C_{d}, C_{v}\right) \nabla C_{d}+D_{v}\left(C_{d}, C_{v}\right) \nabla C_{v}.
\end{aligned}\tag{2}
$$

The transport matrix of Eqs. (2) is not symmetric in the general case. The diagonal terms $D_{d}$ and $D_{v}$ are the diffusion coefficients of dopants and vacancies, respectively; the off-diagonal terms $T_{d}$ and $T_{v}$ account for fluxes driven by gradients of the corresponding other particle type. The four transport coefficients depend on the particle concentrations $C_{d}$ and $C_{v}$ and can be expressed in a series expansion as
$$
a_{0}+a_{1} C_{d}+a_{2} C_{v}+a_{3} C_{d} C_{v}+a_{4} C_{d}^{2} C_{v}+\ldots.
$$

The expansion coefficients $a_{0}, a_{1}, \ldots$ must of course have different values for the different transport coefficients but for the sake of simplicity we omitted additional indices in the above expression. If only diffusion via vacancies is considered, $D_{d}$ must vanish if no vacancies are present $(C_{v}=0)$ so that in the corresponding expansion only those constants $a_{i}$, can be nonzero where the expansion term contains a factor $(C_{v})^{k}$ with $k>0$. $T_{d}$ describes the dopant flux driven by a vacancy gradient and must, therefore, vanish for $C_{d}=0$. This means that the series expansion for $T_{d}$ can only contain terms with a factor $(C_{d})^{k}$ with $k>0$. With the same argument it follows that the series expansion of $T_{v}$ must contain factors $(C_{v})^{k}$; for $D_{v}$ , no such restrictions exist. By dividing through $C_{d}$ or $C_{v}$ , respectively, we obtain the following general form of the diffusion equations:
$$
\begin{aligned}
-\mathbf{J}_{d}= & D_{d}^{n}\left(C_{d}, C_{v}\right)\left(C_{v} / C_{\mathrm{Si}}\right) \nabla C_{d}+T_{d}^{n}\left(C_{d}, C_{v}\right) \\
& \times\left(C_{d} / C_{\mathrm{Si}}\right) \nabla C_{v} \\
-\mathbf{J}_{v}= & T_{v}^{n}\left(C_{d}, C_{v}\right)\left(C_{v} / C_{\mathrm{Si}}\right) \nabla C_{d}+D_{v}\left(C_{d}, C_{v}\right) \nabla C_{v}.
\end{aligned}\tag{3}
$$

The superscript $n$ here indicates normalized transport coefficients (scaled to the site fractions $C_{d}/C_{\text{Si}}$, and $C_{v}/C_{\text{Si}}$ of dopants and vacancies, respectively). We have also divided by the concentration of lattice sites $C_{\text{Si}}$ in order to retain the same units of the transport coefficients as in Eqs. (2). The normalized transport coefficients can again be written in a series expansion. For sufficiently low densities $C_{d}$ and $C_{v}$, only the constant terms $a_{0}$ will survive. We denote with a superscript 0 these limits for the transition to low particle concentrations, i.e.,
$$
\begin{array}{ll}
\lim _{C_{d}, C_{v} \rightarrow 0} D_{d}^{n}=D_{d}^{0}, & \lim _{C_{d}, C_{v} \rightarrow 0} T_{d}^{n}=T_{d}^{0}, \\
\lim _{C_{d}, C_{v} \rightarrow 0} T_{v}^{n}=T_{v}^{0}, & \lim _{C_{d}, C_{v} \rightarrow 0} D_{v}=D_{v}^{0}.
\end{array}\tag{4}
$$

So for low concentrations the diffusion equations read
$$
\begin{aligned}
& -\mathbf{J}_{d}=D_{d}^{0} \frac{C_{v}}{C_{\mathrm{Si}}} \nabla C_{d}+T_{d}^{0} \frac{C_{d}}{C_{\mathrm{Si}}} \nabla C_{v}, \\
& -\mathbf{J}_{v}=T_{v}^{0} \frac{C_{v}}{C_{\mathrm{Si}}} \nabla C_{d}+D_{v}^{0} \nabla C_{v},
\end{aligned}\tag{5}
$$
where the (normalized) transport coefficients $D_{d}^{0}, T_{d}^{0}, T_{v}^{0}$, and $D_{v}^{0}$ only depend on temperature and of course implicitly on the atomistic forces. The controversial models that will be discussed next refer to the form of the diffusion equations given by Eqs. (5).

On the one hand, pair diffusion theory $^{1}$ as usually used in process simulation tools predicts a general relation $\alpha$ $=T_{d}^{0}/D_{d}^{0}=1$ and fluxes of dopants and vacancies having the same direction if driven by a vacancy gradient. On the other hand, there exists a number of models based on some kind of simplified atomistic considerations $^{2-8}$ which are sometimes called ‘‘non-Fickian diffusion’’ models and which assume the probability for a dopant jump to be proportional to the local vacancy concentration. In the case of a vacancy gradient, this jump probability is then larger in the direction of the vacancy gradient. The resulting dopant diffusion flux is therefore predicted to have the direction of the vacancy gradient, i.e., the opposite direction of the vacancy flux. Moreover, a general relation $\alpha=T_{d}^{0}/D_{d}^{0}=-1$ is predicted. Since these results are claimed to be valid for arbitrary dopants this leads to the question of physical consistency of the pair diffusion model which has usually been the basis for determining phenomenological coefficients for process simulation from fits of experimental results. The use of physically consistent models for simulation purposes is of course very important since the experimental data are usually incomplete as the point defect properties are in most cases determined only indirectly from the dopant profiles due to the very low defect densities. Such incomplete data can often also be fitted with unphysical models, but this will not enable any predictive modeling nor will it give any insight into the underlying diffusion mechanisms.

In an earlier work $^{10}$ we have already shown that the relative direction of the fluxes of dopants and vacancies driven by a vacancy gradient as well as the relation $\alpha$ $=T_{d}^{0}/D_{d}^{0}$ depends on the atomistic forces between dopants and vacancies and that in principle both results $\alpha=1$ and $\alpha=-1$ might be possible. However, these early results suffered from a very limited accuracy so that it was not possible to come to definite conclusions concerning the validity of one of the two types of models for the usual dopants. With an improved numerical method, which is described in Sec. II, we were able to achieve precise calculations of the coefficients of Eqs. (5) for a given atomistic interaction potential. As will be shown in Sec. III, it was then possible to establish a relationship between $\alpha$ and measurable quantities from such results allowing an assessment of the two competing models even though no quantitative data for the microscopic forces were available.

## II. DESCRIPTION OF THE SIMULATION METHOD

The atomistic simulation of dopant diffusion via the vacancy mechanism could in principle be performed with the Monte-Carlo method. However, a large number of vacancy jumps must be calculated in order for one dopant jump to take place. So very large computation times are required for good statistics of the dopant fluxes. Therefore, we obtained the results shown in Sec. III with a different approach whose

basic principles have already been described in an earlier work.¹⁰ In this method, the statistical ensemble is not described by a larger number of particle configurations and jumps but analytically by a probability distribution $c(i,j,t)$. With $c(i,j,t)$ we denote the probability at time $t$ to find a dopant atom at a lattice site $i$ and a vacancy at another site $j$. For sufficiently low particle concentrations, the effect of configurations comprising more than one dopant or more than one vacancy can be neglected and $c(i,j,t)$ contains all the necessary information for the determination of the profiles and fluxes of dopants and vacancies.¹⁰ Starting from some initial condition for $c(i,j,0)$ (which is arbitrary for the final results but which can be optimized in terms of computation time as explained in Ref. 10), we obtain the time evolution of $c(i,j,t)$ by solving the Master equation

$$
\begin{aligned}
i \neq j: & \frac{d}{d t} c(i, j, t) \\
= & \sum_{j^{\prime}=n n(j)}\left[-c(i, j, t) f_{j j^{\prime}}^{i}+\left\{\begin{array}{ll}
c\left(i, j^{\prime}, t\right) f_{j^{\prime} j}^{i} & \text { for } j^{\prime} \neq i, \\
c\left(j, j^{\prime}, t\right) f_{j^{\prime} j}^{j} & \text { for } j^{\prime}=i,
\end{array}\right.\right. \text { (6) } \\
i=j: & c(i, j, t)=0,
\end{aligned}
$$

where $f_{j j^{\prime}}^{i}$ denotes the jump frequency for a vacancy jump from site $j$ to a neighboring site $j^{\prime}$ if a dopant atom lies at site $i$ before the jump (we replaced the symbol $\omega$ in Ref. 10 by the more familiar symbol $f$ ). The sum in the second line of Eq. (6) runs over the four nearest neighbor sites $j^{\prime}$ of the vacancy site $j$. For $i=j$, the probability must of course be zero for all times since a dopant and a vacancy cannot occupy the same site. The calculated time evolution finally leads to a steady state $c_{\text{stat}}(i,j)$ which corresponds to a state of local equilibrium. Only for this steady state are physically meaningful values for the particle fluxes obtained. The fluxes can be calculated by considering the probabilities $c_{\text{stat}}(i,j)$ of all configurations for which a particle jump is possible (i.e., all configurations for vacancy jumps but only those with a vacancy at a neighboring position of the dopant for dopant jumps) and by forming a weighted sum of the jump frequencies with these probabilities in which the atomic distances $r_{ij}$ between lattice sites are also accounted for. Details of this can be found in Ref. 10.

For the computation of $c_{\text{stat}}(i,j)$, we made the following modifications compared to the original method of Ref. 10 which led to a considerable improvement in terms of computation time and memory requirements.

(1) Periodic boundary conditions are applied to all surfaces of the simulation area. The constant gradients of the particle profiles are no longer created by constant surface fluxes but by discontinuities of the jump frequencies $f_{j j^{\prime}}^{i}$ for jumps leading over one of the surfaces perpendicular to the direction of the gradients (which is the $z$ direction, by definition). If we label the lower and upper $z$ surface with indices 1 and 2, respectively, the jump frequencies read

$$
f_{j j^{\prime}}^{i}(1 \rightarrow 2)=f_{j j^{\prime}}^{i} \exp \left(\frac{\mu_{v}\left(C_{d}^{2}, C_{v}^{2}\right)-\mu_{v}\left(C_{d}^{1}, C_{v}^{1}\right)}{k T}\right), \quad (7)
$$

where $f_{j j^{\prime}}^{i}(1 \rightarrow 2)$ corresponds to a vacancy jump across the lower surface which ends at the upper surface due to the periodic boundary conditions. For the opposite direction, the jump frequencies are not modified, i.e., $f_{j j^{\prime}}^{i}(2$ $\rightarrow 1)=f_{j j^{\prime}}^{i}$. With $\mu_{d}$ and $\mu_{v}$ we denote the chemical potentials of dopants and vacancies, respectively. $C_{v}^{1,2}$ and $C_{d}^{1,2}$ are the desired concentrations of dopants and vacancies at the corresponding surfaces in the steady state. If the vacancy exchanges its place with a dopant atom, the expression of Eq. (7) for the jump frequency must be multiplied by an additional factor,

$$
\exp \left(\frac{\mu_{d}\left(C_{d}^{1}, C_{v}^{1}\right)-\mu_{d}\left(C_{d}^{2}, C_{v}^{2}\right)}{k T}\right),
$$

accounting for the chemical potential of the dopants. It is possible to derive exact expressions for the chemical potentials $\mu_{d}$ and $\mu_{v}$ from the atomistic interaction potential in the case of low concentrations, as will be shown in a future publication.¹¹ A much faster convergence towards local equilibrium can then be obtained by applying the same particle profiles that are already found in the steady state in the initialization procedure. For calculation of the full transport matrix for a given interaction potential, only two simulation runs are necessary (with two linearly independent sets of particle gradients) whereas determination of the constant surface fluxes in the older method required an iterative procedure involving several runs.

(2) A large reduction in computational time and memory requirements can be achieved by making use of crystal symmetries. If the crystal is oriented in such a way that two of the three crystal vectors are lying in the $x$-$y$ plane while the discontinuities of the jump frequencies [Eq. (7)] are applied at the $z$ surfaces, the correlated probability $c(i,j,t)$ is invariant under simultaneous translation of both sites $i$ and $j$ with a crystal vector lying in the $x$-$y$ plane at any time $t$. The originally six-dimensional two-particle probability $c(i,j,t)$ can then be reduced to a four-dimensional probability if it is only stored, for example, for sites $i$ that are lying within one row of unit cells along the $z$ direction. Note that $c(i,j,t)$ is not invariant under the translation of only one of the two sites $i$ and $j$ since such a translation would affect the distance between the dopant and the vacancy. Since the dopant-vacancy interaction potential (see below) has of course no translational symmetry, the two-particle probability does in fact depend on the particle distance. Making use of the crystal symmetries as explained above would also be possible for arbitrary crystal structures where each of the transport coefficients might itself be a tensor. In any case, there are three possible orientations so that two of the crystal vectors lie in the $x$-$y$ plane and for each orientation the simulation gives one column of each tensorial transport coefficient. For silicon, we used the cubic unit cell comprised of eight atoms (size $5.43$ Å) so that the three possible orientations are equivalent. Since no fluxes were found in the $x$-$y$ plane within the accuracy of the calculation, simulations with one single orienta-

![](./images/812721638599557120_3.jpg)

FIG. 1. Schematic drawing of the potential energy as a function of the vacancy position. The dotted line shows the effect of the dopant located at coordination order 0.

tion are sufficient to prove that the transport coefficients are in fact scalars for the case of the diamond lattice.
(3) A further improvement of computational performance was achieved by storing the inhomogeneous and the homogeneous parts of the two-particle probability $c(i,j,t)$ separately. The large homogeneous and time-independent part corresponds to a total equilibrium state and can be calculated exactly using Gibb's distribution. Only the time evolution of the smaller inhomogeneous part resulting from the particle gradients must be calculated numerically. The probability $c_{\rm stat}(i,j)$ can then be approximated in a much better way already in the initialization so that the simulated diffusion time that is required to reach the steady state becomes smaller. Moreover, numerical accuracy is less critical since differences of almost equal numbers are avoided in the evaluation of the master equation, Eq. (6) [the homogeneous part does not contribute to the time derivative of $c(i,j,t)$, except at the $z$ boundaries]. Single precision data are then sufficient to represent $c(i,j,t)$ whereas the older calculations were done in double precision.

With the improved calculation scheme, almost arbitrary dopant-vacancy interaction potentials can be considered compared to only seven different jump frequencies (corresponding to a maximum range of the interaction to the 3rd coordination site) in the original method. $^{10}$ An example for an atomistic interaction potential is shown in Fig. 1. The dotted line depicts the modification $V_{vd}(i,j)$ of the total potential energy with respect to pure silicon that is caused by the dopant atom. The other two lines show the total potential energy $E_{vd}(i,j)$ as a function of the distance between the dopant site $i$ and the vacancy site $j$. As Fig. 1 shows, we consider two basic types of interactions, an attractive one (drawn line) where the presence of the dopant affects both the minima and the saddlepoints of the potential energy, and a nonattractive interaction (dash-dotted line) where only the height of the saddlepoints is reduced, i.e., the vacancy mobility is increased in the vicinity of the dopant. The attractive case corresponds to the usual assumptions found in the literature $^{12}$ since it is believed that the observed reduction of the activation energy of dopant diffusivity with respect to tracer diffusion can only be explained by a binding force between dopants and vacancies. According to absolute rate theory, $^{13}$ the jump frequencies $f_{jj'}^{i}$ are obtained from the interaction potential as
$$
f_{j j^{\prime}}^{i}=f_{0} \exp \left(-\frac{V_{v d}\left(i, j^{\prime}\right) \pm V_{v d}(i, j)}{2 k T}\right),\qquad(8)
$$
where the minus sign corresponds to the attractive case and the plus sign to nonattractive interaction. $f_{0}$ is the vacancy jump frequency in pure silicon and $k$ and $T$ have their usual meaning. Equation (8) implies the assumption that the shift of a saddlepoint is given by the average of $V_{vd}(i,j)$ at the adjacent stable positions. This assumption is of course quite arbitrary. For the attractive case, we also analyzed the results of a somewhat different approach where it is assumed that the shift of a saddlepoint is given by $V_{vd}(i,j)$ at the neighboring stable site with the higher coordination order. In this case, the jump frequencies read
$$
f_{j j^{\prime}}^{i}=f_{0} \exp \left(-\frac{V_{v d}\left(i, j^{\prime}\right)-V_{v d}(i, j)}{k T}\right)\qquad(9)
$$
for a jump to the higher coordination order. For the opposite jump direction, the jump frequencies are equal to $f_{0}$. For numerical reasons this approach is more feasible since all jump frequencies are smaller than $f_{0}$ and a larger time step for solving Eq. (6) can be used. (The master equation is solved with an explicit scheme using typical timesteps of $0.1 f_{\max }^{-1}$, where $f_{\max }$ is the maximum of all possible jump frequencies.) As the simulation results shown in Sec. III demonstrate, such details of the potential shape are only important for the special outcome of a certain interaction but do not play any role for the general conclusions drawn below.

The errors of the simulation results for a given interaction potential result from the following causes:
(1) surface effects, resulting in nonconstant gradient and fluxes;
(2) incomplete convergence into the steady state due to the limited simulated time;
(3) concentration dependence of the transport coefficients.

The first two causes of error can be estimated by evaluating the results at different locations around the center of the crystal $^{10}$ or at different subsequent times, respectively. While these errors inhibited quantitative results in the older work, $^{10}$ they can be made negligibly small without much effort with the improved method. The dominant contribution to the error now comes from the concentration dependence of the transport matrix. In order to assess the validity of the literature models discussed above, it is necessary to obtain the coefficients of Eqs. (5) for low concentrations, since both types of models are inherently based on this limiting case. The particle fluxes calculated from $c_{\rm stat}(i,j)$, however, give the coefficients of Eqs. (3) for a finite crystal size. In Fig. 2, simulation results (dotted line) for one of the normalized transport coefficients, $T_{v}^{n}$, are shown as a function of particle concen-

![](./images/812721638599557120_4.jpg)

FIG. 2. Simulation results for the normalized vacancy transport coefficient as a function of the size of the simulation area.

trations, i.e., as a function of the number $N_{\text{Si}}$ of sites in the simulation area. Since we consider a two-particle ensemble, the concentrations $C_d$ and $C_v$ are both equal to $C_{\text{Si}}/N_{\text{Si}}$. As Fig. 2 shows, even for the largest simulation area (where the computation time is already of the order of several days) the convergence is not sufficiently good. This problem can be solved since it is possible to derive a closed and exact expression for the relationship between the normalized coefficients of Eq. (3) and their limits for low concentrations from basic principles of irreversible thermodynamics, as long as only configurations of isolated particles and dopant-vacancy pairs contribute to the diffusion mechanism. Applying these considerations to the two-particle ensemble, we obtained the following set of equations for the dependence of the transport coefficients on the number of lattice sites $N_{\text{Si}}$:

$$
\begin{aligned}
D_{d}^{n}= & \frac{N_{\mathrm{Si}}}{N_{\mathrm{Si}}+Z}\left(1-\frac{Z^{2}}{\left(N_{\mathrm{Si}}+Z\right)^{2}}\right)^{-1}\left(D_{d}^{0}-T_{d}^{0} \frac{Z}{N_{\mathrm{Si}}+Z}\right), \\
T_{d}^{n}= & \frac{N_{\mathrm{Si}}}{N_{\mathrm{Si}}+Z}\left(1-\frac{Z^{2}}{\left(N_{\mathrm{Si}}+Z\right)^{2}}\right)^{-1}\left(T_{d}^{0}-D_{d}^{0} \frac{Z}{N_{\mathrm{Si}}+Z}\right), \\
T_{v}^{n}= & \frac{N_{\mathrm{Si}}}{N_{\mathrm{Si}}+Z}\left(1-\frac{Z^{2}}{\left(N_{\mathrm{Si}}+Z\right)^{2}}\right)^{-1}\left(T_{v}^{0}-T_{4} \frac{Z}{N_{\mathrm{Si}}+Z}\right), \\
D_{v}= & D_{v}^{0}+\frac{N_{\mathrm{Si}}}{N_{\mathrm{Si}}+Z}\left(1-\frac{Z^{2}}{\left(N_{\mathrm{Si}}+Z\right)^{2}}\right)^{-1} \\
& \times\left(\frac{T_{4}}{N_{\mathrm{Si}}}-T_{v}^{0} \frac{Z}{N_{\mathrm{Si}}\left(N_{\mathrm{Si}}+Z\right)}\right),
\end{aligned}
\tag{10}
$$

$$Z=z_{v d}-N_{b}-1.$$

Details of the derivation of Eqs. (10) will be published elsewhere. $^{11}$ With $z_{v d}$ we denote the sum of states of a dopant-vacancy pair:
$$
z_{v d}=\sum_{j=1}^{N_{b}} \exp \left(-\frac{E_{v d}(i, j)}{k T}\right),\qquad(11)
$$
where $N_{b}$ is the number of sites within the range of interaction. $T_4$ in Eqs. (10) is an additional constant needed for the transformation. Since $D_{v}^{0}$ is known exactly $(D_{v}^{0}$ $=0.125f_0a^2)^{10}$ and is independent of the interaction potential, we have in fact only four unknowns on the right-hand side of Eqs. (10). The line in Fig. 2 shows the results for the low concentration limit $T_{v}^{0}$ obtained with the help of Eqs. (10). Even for the smallest simulation area, the desired limiting value can thus be achieved with good accuracy. Only with the use of Eqs. (10) was it possible to obtain accurate results for a large number of potentials that is needed for the discussion in Sec. III. The range of concentrations for which these results are also valid for a real crystal comprised of a large number of particles depends on the strength of the interaction potential and can be estimated in a simple manner. $^{14}$ For the potentials discussed in Sec. III, the upper limit for $C_d$ is about $10^{18}\ \text{cm}^{-3}$; the value of $C_v$ is not important as long as we assume that it is much smaller than $C_d$.

The remaining errors of the results shown below are smaller than 1% so error bars will therefore be omitted in the graphs.

### III. RESULTS AND DISCUSSION

All simulation results shown in the following were obtained for a temperature of $1000\ ^{\circ}\text{C}$; activation energies were calculated from results in the temperature range 1000–1200 °C. We will first discuss the simulation results for attractive dopant-vacancy interactions.

Table I shows calculated values of the normalized transport coefficients for attractive potentials with a depth of 0.5 eV and a range between 0 (tracer diffusion) and 5 coordination orders in units of $f_0$ and the lattice constant $a$. For the sake of simplicity, we assumed a rectangular-well shape as depicted in Fig. 1. As mentioned above, $D_{v}^{0}$ is independent of the potential, therefore, only the remaining three coefficients are listed in Table I. As Table I shows, the dopant diffusivity $D_{d}^{0}$ is largely enhanced compared to tracer diffusion due to the interaction potential. This enhancement effect shows a

<table>
<caption>TABLE I. Simulation results for the normalized transport coefficients at $1000\ ^{\circ}\text{C}$ for attractive rectangular interaction potentials with a depth of 0.5 eV and varying ranges.</caption>
<thead>
<tr>
<th>Range</th>
<th>$D_{d}^{0}(f_0a^2)$</th>
<th>$T_{d}^{0}(f_0a^2)$</th>
<th>$T_{v}^{0}(f_0a^2)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (tracer diffusion)</td>
<td>$0.0625\pm 10^{-5}$</td>
<td>$-0.124\,98\pm 2\times 10^{-5}$</td>
<td>$-0.0001\pm 0.002$</td>
</tr>
<tr>
<td>1st coordination order</td>
<td>$0.1237\pm 10^{-4}$</td>
<td>$-0.2473\pm 10^{-4}$</td>
<td>$-47.29\pm 0.03$</td>
</tr>
<tr>
<td>2nd coordination order</td>
<td>$0.365\pm 0.003$</td>
<td>$-0.605\pm 0.003$</td>
<td>$-188.9\pm 1.1$</td>
</tr>
<tr>
<td>3rd coordination order</td>
<td>$5.31\pm 0.05$</td>
<td>$4.70\pm 0.05$</td>
<td>$-465.9\pm 4.5$</td>
</tr>
<tr>
<td>4th coordination order</td>
<td>$5.43\pm 0.04$</td>
<td>$4.61\pm 0.03$</td>
<td>$-963.0\pm 3.3$</td>
</tr>
<tr>
<td>5th coordination order</td>
<td>$5.8\pm 0.03$</td>
<td>$5.12\pm 0.02$</td>
<td>$-1719.3\pm 4.7$</td>
</tr>
</tbody>
</table>

![](./images/812721638599557120_5.jpg)

FIG. 3. Calculated relation $\alpha=T_{d}^{0}/D_{d}^{0}$ for different attractive interaction potentials as a function of the potential range.

![](./images/812721638599557120_6.jpg)

FIG. 4. Calculated reduction of the activation energy of dopant diffusivity $D_{d}$ compared to tracer diffusion as a function of the attractive potential range.

saturation beginning at a range to the 3rd coordination order. The dopant transport coefficient $T_{d}^{0}$ is negative for short range potentials and positive for potentials extending at least to the 3rd coordination order. The relation $\alpha=T_{d}^{0}/D_{d}^{0}$ is $-2$ for tracer diffusion and converges to values somewhat below the result $+1$ from pair diffusion theory for the long-ranging potentials. The vacancy transport coefficient $T_{v}^{0}$ is negative for all potentials and its absolute values are much larger than the other coefficients. This is due to the attractive force acting on the vacancies driving them in the direction of the higher dopant concentration, i.e., in the direction of the dopant gradient. For tracer diffusion, we have of course $T_{v}^{0}=0$ within the accuracy of the method since a gradient of the tracers does not cause any vacancy flux. The accuracy of the numerical calculation can be demonstrated by evaluating the correlation factor $f_{t}$ in the case of tracer diffusion which is given by the relation $f_{t}=D_{d}^{0}(\text{tracer})/D_{v}^{0}$. From the result for $D_{d}^{0}(\text{tracer})$ in Table I and with $D_{v}^{0}=0.125f_{0}a^{2}$ (see above) we get $f_{t}=0.5\pm8\times10^{-5}$ which is in very good agreement with the theoretical value$^{15}$ of $0.5$.

We used the simple rectangular potential shape as a starting point for the analysis since it is the most simple approach in the absence of more realistic data and allows easy parametrization of the interaction according to depth and range. As the following results will show, most of the important conclusions can already be derived from the variety of rectangular potential since an arbitrary potential can be written as a superposition of rectangular ones. Figure 3 shows simulation results for $\alpha$ for potentials with different depths and shapes as a function of the potential range. Beside the rectangular shape, we also considered potentials depending linearly on the dopant-vacancy distance and Coulomb potentials. The Coulomb potential was assumed to be zero outside the maximum range and to be proportional to $1/r(i,j)$ elsewhere [$r(i,j)$ is the distance between the dopant and the vacancy site]. We define the depth of the linear and Coulomb potentials at a nearest neighbor configuration of the dopant and the vacancy. As Fig. 3 shows, $\alpha$ converges with increasing potential range to values very close to $+1$ if the depth is large enough and to some positive value $<1$ for weaker potentials. A closer analysis shows that the sensitivity of $\alpha$ upon the parameters of the interaction is largest for the values of the potential around the 3rd coordination order. This explains qualitatively the differences resulting from the different potentials shapes: For the same depth at the nearest neighbor sites, the linear and the Coulomb potentials are of course weaker at the 3rd coordination order. However, the results for $\alpha$ do not only depend on the value of the potential directly at the 3rd coordination order, as is often assumed in the literature.$^{12}$ At this location, the linear and the Coulomb potentials of Fig. 3 are by coincidence almost equal but nevertheless the results for $\alpha$ significantly differ. For the same potentials as in Fig. 3, the calculated reduction $\Delta E_{\text{ac}}$ of the activation energy of dopant diffusivity with respect to tracer diffusion is shown in Fig. 4. These results were obtained by calculating the transport coefficients for different temperatures in the range 1000–1100 °C and fitting the results against an Arrhenius law. For the rectangular potentials, $\Delta E_{\text{ac}}$ is approximately equal to the potential depth if the range is at least to the 3rd coordination order but much smaller for smaller ranges. For the linear and Coulomb potentials, $\Delta E_{\text{ac}}$ lies below the maximum potential depth which is again due to the dominance of the potential around the 3rd coordination order as explained above. By comparing Fig. 3 with Fig. 4 one can already see a general relationship between $\alpha$ and $\Delta E_{\text{ac}}$: If the absolute value of $\Delta E_{\text{ac}}$ is large enough, $\alpha$ converges to the value $+1$ predicted by pair diffusion. As Fig. 3 shows, the value $-1$ from the simplified atomistic models could also be possible in principle. This value is, however, not very likely since it is achieved only for very special choices of the potential whereas the result $+1$ appears to be a limit for strong and long-ranging interactions of arbitrary shape. The drawbacks of the non-Fickian diffusion theory have already been discussed in Ref. 10. Figure 5 shows calculated values of $\alpha$ as a function of the potential depth with range as the parameter. These results clearly demonstrate that both depth *and* range must exceed certain values in order to arrive at the predic

![](./images/812721638599557120_7.jpg)

FIG. 5. Calculated relation $\alpha=T_{d}^{0}/D_{d}^{0}$ for different attractive potentials as a function of the potential depth.

tions of the pair diffusion model. For a range smaller than one to the 3rd coordination order, even strong binding does not lead to positive values for $\alpha$.

Up to now, only attractive potentials were considered. In the following, we discuss the simulation results for nonattractive interactions.

Table II shows the calculated transport coefficients for nonattractive rectangular potentials with a depth of 0.5 eV and a range up to the 5th coordination order. Compared to Table I, the results for $D_{d}^{0}$ and $T_{d}^{0}$ are very similar, except for a range to the 2nd coordination order. This difference is only due to the fact that we used Eq. (9) rather than Eq. (8) for the attractive potentials while for the nonattractive interaction it was assumed that the shift of the saddlepoints is the average of the potential $V_{vd}(i,j)$ at the two adjacent stable positions. Such details, however, do not affect the general relationships. As for the attractive case, the predictions of pair diffusion theory for $\alpha$ are fulfilled almost if the range of interaction is large enough whereas negative values for $\alpha$ result from a shorter range. Figures 6 and 7 show simulation results for $\alpha$ and $\Delta E_{\text{ac}}$ for different nonattractive rectangular potentials as a function of the range of interaction. The results are very similar to the corresponding ones shown in Figs. 3 and 4. Modeling the observed reduction of activation energy of dopant diffusivity with respect to tracer diffusion obviously does not require a true binding between dopants and vacancies as is usually assumed in the literature.

![](./images/812721638599557120_8.jpg)

FIG. 6. Calculated relation $\alpha=T_{d}^{0}/D_{d}^{0}$ for box shaped nonattractive potentials as a function of the range of interaction.

Since no reliable data for true dopant-vacancy interaction are available, the results shown so far do not prove whether pair diffusion is a valid description for the usual dopant atoms. However, we can come to some definite conclusions if we plot the simulation results for $\alpha$ versus the corresponding results for $\Delta E_{\text{ac}}$ as shown in Fig. 8. Each data point originates from one assumed interaction potential; the points as a whole show the consequences of a variety of attractive and nonattractive potentials with quite different depths, ranges, and shapes. For an arbitraty interaction, Fig. 8 shows an almost unique dependence between $\alpha$ and $\Delta E_{\text{ac}}$. This dependence is in fact a weak function of temperature. However, in the temperature range 900–1100 °C the differences are not important for the conclusions. For values of $\Delta E_{\text{ac}}$ below about $-0.6\,\text{eV}$, $\alpha$ lies very close to the value $+1$, corresponding to the prediction of pair diffusion theory. The horizontal bars above the plot indicate the intervals of the measured values for $\Delta E_{\text{ac}}$. The intrinsic dopant diffusivities were taken from Fair *et al.*,¹⁶,¹⁷ and the data for the tracer diffusion coefficient were obtained from a number of authors.¹⁸⁻²⁵ So the relatively large spread of the experimental results is due to the uncertain values for tracer diffusivity. For boron, phosphorus, and arsenic, we obtain a highly accurate value of $+1$ for $\alpha$ for the complete experimental interval of $\Delta E_{\text{ac}}$, confirming the validity of the pair diffusion model for these elements. For antimony, however, the experimental spread is too large to come to such a clear conclusion. For the lowest measured values of $\Delta E_{\text{ac}}$ we have again confirmation of the pair diffusion model; for the highest results it can only be concluded that $\alpha$ is higher than

<table>
<caption>TABLE II. Simulation results for the normalized transport coefficients at 1000 °C for nonattractive rectangular interaction potentials with a depth of 0.65 eV and varying ranges.</caption>
<thead>
<tr>
<th>Range</th>
<th>$D_{d}^{0}(f_{0}a^{2})$</th>
<th>$T_{d}^{0}(f_{0}a^{2})$</th>
<th>$T_{v}^{0}(f_{0}a^{2})$</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (tracer diffusion)</td>
<td>$0.0625\pm 10^{-5}$</td>
<td>$-0.124\,98\pm 2\times 10^{-5}$</td>
<td>$-0.0001\pm 0.002$</td>
</tr>
<tr>
<td>1st coordination order</td>
<td>$0.31\pm 0.002$</td>
<td>$-0.54\pm 0.006$</td>
<td>$-0.41\pm 0.006$</td>
</tr>
<tr>
<td>2nd coordination order</td>
<td>$1.93\pm 0.002$</td>
<td>$0.62\pm 0.01$</td>
<td>$0.74\pm 0.01$</td>
</tr>
<tr>
<td>3rd coordination order</td>
<td>$5.37\pm 0.001$</td>
<td>$4.43\pm 0.03$</td>
<td>$4.55\pm 0.03$</td>
</tr>
<tr>
<td>4th coordination order</td>
<td>$5.53\pm 0.001$</td>
<td>$4.48\pm 0.04$</td>
<td>$4.64\pm 0.1$</td>
</tr>
<tr>
<td>5th coordination order</td>
<td>$5.81\pm 0.002$</td>
<td>$5.01\pm 0.04$</td>
<td>$5.2\pm 0.1$</td>
</tr>
</tbody>
</table>

![](./images/812721638599557120_9.jpg)

FIG. 7. Calculated reduction of the activation energy of dopant diffusivity $D_d$ with respect to tracer diffusion as a function of the range of the nonattractive potentials.

about 0.5. It must be noted that the conclusions drawn so far still depend on two assumptions. First, it was assumed in the atomistic simulations that entropy effects are not important for the interaction between dopants and vacancies, i.e., only shifts of the total potential energy in the vicinity of the dopant were considered but not modifications to the vibrational frequencies around the stable positions. Only in this case does the general relationship between $\alpha$ and $\Delta E_{\text{ac}}$ shown in Fig. 8 hold. Second, it was assumed that tracer diffusion is dominated by the vacancy mechanism because otherwise the measured values of the activation energy of tracer diffusion could be different from the activation energy of the vacancy part of tracer diffusion. It is possible to come to conclusions that are free of these assumptions if the simulation results for $\alpha$ are plotted against the corresponding results for the enhancement factor $D_d/D_{\text{tracer}}$ of dopant diffusivity over tracer diffusion as shown in Fig. 9. Since on both axes only relations of calculated transport coefficients are plotted, the general relationship shown in Fig. 9 does not depend on temperature. The calculated values of transport coefficients only depend on the set of jump frequencies that are used in the simulation which are the same if both the absolute temperature and the potential depth are scaled by some factor. For the same reason, the general relationship between $\alpha$ and $D_d/D_{\text{tracer}}$ does also not depend on whether the interaction is due to energy or to entropy effects. By comparing the simulation results to the experimental results for $D_d/D_{\text{tracer}}$ (horizontal bars in Fig. 9), we again obtain confirmation for the pair diffusion model for boron and phosphorus for the whole experimental interval. If the vacancy part of tracer diffusion is smaller than 1, this conclusion is even more valid since then the enhancement factor of $D_d$ over this part of $D_{\text{tracer}}$ would be still larger than the measured relation $D_d/D_{\text{tracer}}$. For arsenic and antimony, the experimental scattering is too large to draw such a definite conclusion. For the lowest experimental values for $D_d/D_{\text{tracer}}$ it can only be concluded that $\alpha$ is non-negative; however, if we believe in the highest measured values, pair diffusion is again confirmed. Of course all the arguments given above are only valid as long as the diffusion of a dopant element being considered is at all dominated by the vacancy mechanism.

![](./images/812721638599557120_10.jpg)

FIG. 8. Simulation results for $\alpha=T_d^0/D_d^0$ and $\Delta E_{\text{ac}}$ for a variety of model potentials; the horizontal bars indicate experimental intervals for $\Delta E_{\text{ac}}$.

![](./images/812721638599557120_11.jpg)

FIG. 9. Simulation results for $\alpha=T_d^0/D_d^0$ and $D_d/D_{\text{tracer}}$ for a variety of model potentials; the horizontal bars indicate experimental intervals for $D_d/D_{\text{tracer}}$.

So far the discussion of the validity of the pair diffusion model has only considered the relation $\alpha$. Of course, the whole set of the four coefficients of Eqs. (5) can be derived from the assumptions made in pair diffusion theory. However, it will be shown in the following that the relation $\alpha=T_d^0/D_d^0$ is in fact the only general relationship between these coefficients that is predicted by the pair diffusion model: The following equations for the flux densities $\mathbf{J}_d$ and $\mathbf{J}_v$ of dopants and vacancies, respectively, can be derived from the parameters $D_p$, $D_v^f$, $k$, and $k_r$ of the pair diffusion model in the case of a local equilibrium of the reactions of pair formation and dissolution [details will be published elsewhere, $^{11}$ together with the derivation of Eqs. (10)]:

$$
\begin{aligned}
& -\mathbf{J}_{d}=D_{p} \frac{k}{k_{r}} C_{v}^{f} \nabla C_{d}^{f}+D_{p} \frac{k}{k_{r}} C_{v}^{f} \nabla C_{v}^{f}, \\
& -\mathbf{J}_{v}=D_{p} \frac{k}{k_{r}} C_{v}^{f} \nabla C_{d}^{f}+\left(D_{p} \frac{k}{k_{r}} C_{d}^{f}+D_{v}^{f}\right) \nabla C_{v}^{f}.
\end{aligned}
\tag{12}
$$

Here, $D_{p}$ denotes the diffusivity of the dopant-vacancy pairs, $D_{v}^{f}$ is the diffusion constant of the free vacancies, and $k$ and $k_{r}$ are the reaction rates for formation and dissolution of the pairs, respectively. $C_{d}^{f}$ and $C_{v}^{f}$ are the concentrations of free dopants and vacancies, respectively. For low total particle densities, we have of course $C_{d}^{f} \approx C_{d}$ and $C_{v}^{f} \approx C_{v}$ since only a small fraction of the particles is bound in pairs. For this reason one can often find in the literature the flux equations in the form of Eqs. (12) but without the index $f$ indicating free particles on the right-hand side. $^{26}$ The comparison with the general expressions of Eqs. (5) would then give a symmetric transport matrix with only two different coefficients since a further general relation $T_{v}^{0} / D_{d}^{0}=1$ would hold. This would be in obvious contradiction to the results shown in Table I where the vacancy transport coefficient $T_{v}^{0}$ is found to differ from $D_{d}^{0}$ by several orders of magnitude. This discrepancy is, however, not a true one. The reason is that the limiting case of low concentrations is not properly considered by simply omitting the distinction between free and total particle densities in Eqs. (12). A correct derivation which will be published elsewhere $^{11}$ leads to the following expressions for the dependence of the transport coefficients on the parameters of the pair diffusion model:

$$
\begin{aligned}
& D_{d}^{0}=D_{p} \frac{k}{k_{r}} C_{\mathrm{Si}}, \quad T_{d}^{0}=D_{d}^{0}, \\
& T_{v}^{0}=\left(D_{p}-D_{v}^{f}\right) \frac{k}{k_{r}} C_{\mathrm{Si}}, \quad D_{v}^{0}=D_{v}^{f}.
\end{aligned}
\tag{13}
$$

This means that the relation $\alpha=T_{d}^{0} / D_{d}^{0}$ is in fact a general consequence of the pair diffusion model but that the prediction for the second relation $T_{v}^{0} / D_{d}^{0}$ depends upon the diffusivities $D_{p}$ and $D_{v}^{f}$:

$$
T_{v}^{0} / D_{d}^{0}=1-\frac{D_{v}^{f}}{D_{p}}.
\tag{14}
$$

If the diffusivity $D_{p}$ of the pairs is smaller than that of the free vacancies $D_{v}^{f}$, the vacancy transport coefficient $T_{v}^{0}$ will be large and negative, otherwise, it will be positive and close to the value of $D_{d}^{0}$ for $D_{p} \gg D_{v}^{f}$. The simulation results clearly show (see, e.g., Tables I and II) that these two cases are in fact represented by long-ranging attractive and longranging nonattractive interactions, respectively. This can be understood as follows. For an attractive interaction, the average vacancy jump frequency within the range of interaction is of the same order of magnitude as for a free vacancy. A displacement of the pair by one lattice site requires a large number of vacancy jumps around the dopant atom so that $D_{p}<D_{v}^{f}$. For the nonattractive interaction, the mobility of the vacancy is largely enhanced in the vicinity of the dopant due to the lower potential barriers. For a sufficiently strong interaction, the diffusivity of the pair may then be larger than the diffusivity of free vacancies. Note that in the above argumentation we have used the term "pair" very generally for any configuration where the vacancy is within the range of interaction with the dopant. A precise quantitative definition from the atomistic model is of course not very useful since pair diffusion is not a valid description for arbitrary interactions. As the above analysis showed, range and depth of the potentials must exceed certain values in order for the pair diffusion theory to be applicable. In this case, the number of independent parameters in Eqs. (5) is reduced from four to three. For weaker or short-ranged potentials, no general relations between these parameters can be postulated.

## IV. CONCLUSION

The phenomenological transport coefficients for the coupled diffusion of dopants and vacancies in the presence of dopant and vacancy gradients have been calculated on the basis of the atomistic model of particle jumps whose probabilities are modified by some interaction potential between dopants and vacancies. Since no accurate data for these interaction potentials are available so far, the simulations were done with a number of model approaches for the interactions in order to analyze the general properties of the macroscopic diffusion equations and to clarify the discrepancy between the predictions of pair diffusion theory and the non-Fickian diffusion model. One result of these simulations was that the observed reduction of the activation energy of dopant diffusivity with respect to tracer diffusion and the corresponding factor of enhancement of $D_{d}$ over $D_{\text {tracer }}$ can also be explained by a nonbinding interaction that only enlarges the vacancy mobility in the neighborhood of the dopant but does not give rise to a larger vacancy density around the dopant. The simulation results obtained with a large variety of attractive and nonattractive forces with quite different parameters showed a general relationship between the relation $\alpha$ $=T_{d}^{0} / D_{d}^{0}$ to which the controversial models apply and measurable quantities like the enhancement factor $D_{d}^{0} / D_{\text {tracer }}$. In this way, it was possible to come to a definite conclusion in favor of the pair diffusion model for the usual dopant atoms even without any knowledge of the true parameters of the interaction potential. The value $\alpha=+1$ from pair diffusion could be confirmed with high accuracy for boron and phosphorus, and for arsenic and antimony at least $\alpha>0$ could be derived. A further analysis also showed that the predictions of the pair diffusion model are consistent with the atomistic vacancy mechanism not only for $\alpha$ but also for the whole set of macroscopic parameters of the diffusion equations. An assessment of the relative importance of the vacancy mechanism compared to interstitial related mechanisms for the different dopant atoms is, however, not possible in such a way. To do so would require accurate quantitative data on the atomistic interaction potentials.

## ACKNOWLEDGMENT

This work was funded by the Deutsche Forschungsgemeinschaft (DFG).

${ }^{1}$ See, for example, M. Yoshida, J. Appl. Phys. 48, 2169 (1977); R. B. Fair and J. C. C. Tsai, J. Electrochem. Soc. 124, 1107 (1977); F. F. Morehead

and R. F. Lever, Appl. Phys. Lett. **48**, 151 (1986); B. J. Mulvaney and W. B. Richardson, *ibid.* **51**, 1439 (1987).

²M. Kurata, Y. Morikawa, K. Nagami, and H. Kuroda, Jpn. J. Appl. Phys. **12**, 472 (1973).

³Y. Morikawa, K. Yamamoto, and K. Nagami, Appl. Phys. Lett. **36**, 997 (1980).

⁴V. V. Kozlovski, V. N. Lomasov, and L. S. Vlasenko, Radiat. Eff. **106**, 37 (1988).

⁵O. V. Aleksandrov, V. V. Kozlovski, V. V. Popov, and B. E. Samorukov, Phys. Status Solidi A **10**, K61 (1988).

⁶K. Maser, Exp. Tech. Phys. (Berlin) **34**, 213 (1986).

⁷K. Maser, Ann. Phys. (Leipzig) **45**, 81 (1988).

⁸K. Maser, Exp. Tech. Phys. (Berlin) **39**, 169 (1991).

⁹L. Onsager, Phys. Rev. **37**, 405 (1931); **38**, 2265 (1931).

¹⁰S. List, P. Pichler, and H. Ryssel, J. Appl. Phys. **76**, 223 (1994).

¹¹S. List, *Atomistische Beschreibung der Diffusion von Dotieratomen und Gitterleerstellen in Silicium* (Shaker, Aachen, 1997).

¹²S. M. Hu, Phys. Status Solidi B **60**, 595 (1973).

¹³G. H. Vineyard, J. Phys. Chem. Solids **3**, 121 (1957).

¹⁴S. List and H. Ryssel, J. Appl. Phys. **83**, 7595 (1998).

¹⁵M. Koiwa and S. Ishioka, Philos. Mag. A **47**, 927 (1983).

¹⁶R. B. Fair, in *Impurity Doping Processes in Silicon*, edited by F. F. Y. Wang (North-Holland, Amsterdam, 1981), p. 315.

¹⁷R. B. Fair, M. L. Manda, and J. J. Wortmann, J. Mater. Res. **1**, 705 (1986).

¹⁸R. F. Peart, Phys. Status Solidi **15**, K119 (1966).

¹⁹R. N. Ghoshtagore, Phys. Rev. Lett. **16**, 890 (1966).

²⁰B. J. Masters and J. M. Fairfield, Appl. Phys. Lett. **8**, 280 (1966).

²¹J. M. Fairfield and B. J. Masters, J. Appl. Phys. **38**, 3148 (1967).

²²H. J. Mayer, H. Mehrer, and K. Maier, Inst. Phys. Conf. Ser. **31**, 186 (1977).

²³L. Kalinowski and R. Seguin, Appl. Phys. Lett. **35**, 211 (1979).

²⁴L. Kalinowski and R. Seguin, Appl. Phys. Lett. **36**, 171 (1980).

²⁵F. J. Demond, S. Kalbitzer, S. Mannsperger, and H. Damjantschitsch, Phys. Lett. **93A**, 503 (1983).

²⁶M. Orlowski, Appl. Phys. Lett. **53**, 1323 (1988).