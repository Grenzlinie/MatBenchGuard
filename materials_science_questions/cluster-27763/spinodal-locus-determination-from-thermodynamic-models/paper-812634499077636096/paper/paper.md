# Phase separation and nucleation in mixtures of particles with different temperatures

Efe Ilker $^{1}$ and Jean-François Joanny $^{1,2}$

$^{1}$Physico-Chimie Curie UMR 168, Institut Curie, PSL Research University, 26 rue d'Ulm, 75248 Paris Cedex 05, France
$^{2}$Collége de France, 11 place Marcelin Berthelot, 75005 Paris, France

![](./images/812634499077636096_1.jpg)
(Received 10 January 2020; accepted 28 April 2020; published 20 May 2020)

Differences in activities in colloidal particles are sufficient to drive phase separation between active and passive (or less active) particles, even if they have only excluded volume interactions. In this paper, we study the phase-separation kinetics and propose a theory of phase separation of colloidal mixtures in the diffusive limit. Our model considers a mixture of diffusing particles coupled to different thermostats, it thus has a nonequilibrium nature due to the temperature differences. However, we show that indeed the system recovers an effective equilibrium thermodynamics in the dilute limit. We obtain phase diagrams showing the asymmetry in concentrations due to activity differences. By using a more general approach, we show the equivalence of phase-separation kinetics with the well-known Cahn-Hilliard theory. On the other hand, higher-order expansions in concentration indicate the emergence of nonequilibrium effects leading to a breakdown of the equilibrium analogy. We lay out the general theory in terms of accessible parameters which we demonstrate by several applications. In this simple formalism, we capture a positive surface tension for hard spheres, and interesting scaling laws for interfacial properties, droplet growth dynamics, and phase segregation conditions. Several of our results are in agreement with existing numerical simulations while we also propose testable predictions.

DOI: 10.1103/PhysRevResearch.2.023200

## I. INTRODUCTION

Many-body systems self-organize and exhibit macroscopic collective behavior, which is amenable to coarse-grained dynamics [1]. The principles of equilibrium thermodynam- ics which provide the essential tools for studying equilib- rium self-assembly are not adapted to the new phenomena emerging in active systems [2]. While active systems are nonequilibrium in their nature, with each constituent having its own energy budget and objective, it is quite fascinating how these systems can display distinct characteristics which are sometimes nontrivially related to the known basic physical principles. A typical example is that of active phase separa- tion.

In living organisms, activity-driven phase separation plays an important role by promoting self-organization and in- creasing the efficiency of biological functions inside cells [3,4], which are due to operate in a very crowded and noisy environment. The constant use of energy in unequal amounts by individual cellular subcomponents reflects their varieties in dynamical and chemical activities [5] as well as with their innate physiological differences. In turn, these activity differences may enhance phase separation by creating effective attractions between alike components. Remarkably, similar characteristics and governing principles are observed at various length scales on diverse biological systems and they are now also guiding synthetic model systems [6-10].

It is now well known that activity differences in colloidal particles are sufficient to drive phase separation between active and passive (or less active) hard spheres having only excluded volume interactions. These systems can be consid- ered to have particles with two different temperatures which mimics the effect of activity differences [11-13]. In principle, the constituent particles exchange energy, the hotter ones providing extra energy for the colder ones. This, in turn, indicates a nonequilibrium behavior [14]. Similarly, in poly- meric systems, tiny activity differences in active and passive polymer mixtures enhance phase segregation [15,16]. If the system is diffusive, the effective temperature can simply be deduced from the effective diffusivity. For instance, at room temperature $T$, bacteria may reach an effective temperature $T_A \sim 10^2$-$10^3$ $T$ in translational motion by chemotaxis [17]. These realizations are not limited to biological or polymeric systems, but are also seen in plasma physics [18] and in the description of thermal phases in the interstellar medium [19,20]. Due to having different heating and cooling pro- cesses, ionized hydrogen reaches a temperature $\sim 10^2$ times larger than atomic hydrogen distributed in the interstellar medium [21]. In many other contexts, the concept of effective temperature [22] proves quite useful in understanding large- scale phenomena that originate from microscopic motility or even chemical differences between the building components [23-26]. Considering the growing interest in these systems, it is important to study and establish a theory of phase separation starting from the microscopic dynamics.

In this work, we extend the theory of mixtures of parti- cles with different temperatures introduced in Ref. [11] to inhomogeneous mixtures and we study the phase-separation

Published by the American Physical Society under the terms of the *Creative Commons Attribution 4.0 International* license. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

2643-1564/2020/2(2)/023200(18)
023200-1
Published by the American Physical Society

kinetics of solutions composed of two diffusing species, which are coupled to different thermostats. Starting from the microscopic model (Sec. II), we derive and present the theory in the dilute limit (Secs. II–IV) and obtain the scaling laws for phase behaviors. Even though the system has inherently nonequilibrium properties due to activity differences, it obeys an effective equilibrium thermodynamics in the dilute limit including the interfacial contributions, which generalizes the Cahn-Hilliard theory of solutions [27] to two temperature mixtures. We verify this comparing the equilibrium thermo- dynamic route with the mechanical one. In Sec. V, we demon- strate example applications of the theory in diverse systems, and we discuss the results in comparison to previous studies with new predictions. In Sec. VI, we consider higher-order corrections in concentrations which break the equilibrium analogy and raise the difficulty to define a scalar temperature. For purely hard-core interactions, we present higher-order corrections in density to the theory by considering depletion interactions between spheres of different activities, and obtain results, which do not seem to be easily obtainable otherwise. We summarize and discuss all these results in the Conclusion.

## II. MICROSCOPIC MODEL

We start by introducing the microscopic model and derive an effective thermodynamic description, which is valid when the solutions that we study are very dilute. We follow the lines of Ref. [11] but we extend this approach to inhomoge- neous mixtures. Thus, we study a solution of mixed particles satisfying overdamped Langevin equations, in contact with reservoirs at different temperatures

$$
\zeta_{m} \dot{x}_{m}=-\partial_{m} U+\left(2 T_{m} \zeta_{m}\right)^{1 / 2} \xi_{m}(t), \quad(1)
$$

where $U$ is the overall interaction potential between the particles. The position of particle $m$ is denoted by $x_{m}$, its friction coefficient by $\zeta_{m}$, its temperature by $T_{m}$, and $\xi_{m}(t)$ is a standard zero mean, unit variance, Gaussian white noise. Here, we consider two different species of particles, each being in contact with a thermostat at temperature $T_{\mathcal{A}}$ or $T_{\mathcal{B}}$. This dynamics presented as a Langevin equation for each particle in the system can be reformulated as a Fokker-Planck equation for a multiparticle probability distribution $P(\{\mathbf{r}\})$ where $\{\mathbf{r}\}$ is a vector whose components are the positions of all the particles. The Fokker-Planck equation is written in terms of the fluxes $J_{m}$ for each particle:

$$
\begin{gathered}
\frac{\partial P(\{\mathbf{r}\})}{\partial t}=-\sum_{m} \partial_{m} J_{m}, \\
J_{m}=-\partial_{m} U P / \zeta_{m}-T_{m} \partial_{m} P / \zeta_{m}.
\end{gathered}
$$

Distinguishing the two species of particles $\mathcal{A}$ and $\mathcal{B}$ and integrating over all coordinates except for one, we obtain the single-particle distributions $p_{\alpha}\left(\mathbf{r}_{1}\right)$ where now $\alpha, \beta=\mathcal{A}$ or $\mathcal{B}$ [11]:

$$
\begin{gathered}
\frac{\partial p_{\alpha}\left(\mathbf{r}_{1}\right)}{\partial t}=\frac{T_{\alpha}}{\zeta_{\alpha}} \nabla_{\mathbf{r}_{1}}^{2} p_{\alpha}\left(\mathbf{r}_{1}\right)-\frac{1}{\zeta_{\alpha}} \partial_{\mathbf{r}_{1}} p_{\alpha}\left(\mathbf{r}_{1}\right) \sum_{\beta} \bar{f}_{\alpha \beta}, \\
\bar{f}_{\alpha \beta}=-N_{\beta} \int \frac{\partial u_{\alpha \beta}}{\partial \mathbf{r}_{1}} \frac{p_{2}^{\alpha \beta}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)}{p_{\alpha}\left(\mathbf{r}_{1}\right)} d \mathbf{r}_{2},
\end{gathered}
$$

and $N_{\beta}$ is the number of $\beta$-type particles. We may write the two-particle densities in terms of single-particle distributions and a pair distribution function $p_{2}^{\alpha \beta}\left(\mathbf{r}_{1}, \mathbf{r}_{2}\right)=$ $p_{\alpha}\left(\mathbf{r}_{1}\right) p_{\beta}\left(\mathbf{r}_{2}\right) g_{\alpha \beta}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right)$. Accordingly, $g_{\alpha \beta}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right)$ is the pair distribution function and in the long time limit, it reaches a steady-state value, i.e., $g_{\alpha \beta}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right) \rightarrow g_{\alpha \beta}^{s s}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right)$. The knowledge of the steady-state pair distribution function is suf- ficient to close this set of equations. In general, $g_{\alpha \beta}^{s s}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right)$ depends on the particle concentrations and can be expanded in powers of the concentrations. In the dilute limit, when con- sidering only pair interactions, the solution of Eq. (2) imposes

$$
g_{\alpha \beta}^{s s}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right)=\exp \left[-u_{\alpha \beta}\left(\mathbf{r}_{1}-\mathbf{r}_{2}\right) / T_{\alpha \beta}\right], \quad(4)
$$

where $T_{\alpha \beta}$ are the mobility-weighted average temperatures and are defined as $T_{\mathcal{A} \mathcal{A}} \equiv T_{\mathcal{A}}, T_{\mathcal{B B}} \equiv T_{\mathcal{B}}$, and $T_{\mathcal{A B}}=$ $\left(\zeta_{\mathcal{B}} T_{\mathcal{A}}+\zeta_{\mathcal{A}} T_{\mathcal{B}}\right) /\left(\zeta_{\mathcal{A}}+\zeta_{\mathcal{B}}\right)$.

In order to determine the forces $\bar{f}_{\alpha \beta}$, we rewrite the two- particle distribution function as $p_{2}^{\alpha \beta}\left(\mathbf{r}_{1}, \mathbf{r}\right)=p_{\alpha}\left(\mathbf{r}_{1}\right) p_{\beta}\left(\mathbf{r}_{1}+\right.$ $\mathbf{r}) \exp \left[-u^{\alpha \beta}(\mathbf{r}) / T_{\alpha \beta}\right]$ by defining $\mathbf{r}_{2}=\mathbf{r}_{1}+\mathbf{r}$. This change of variables inside the integrals yields

$$
\bar{f}_{\alpha \beta}=-N_{\beta} T_{\alpha \beta} \int \frac{\partial}{\partial \mathbf{r}_{1}}\left(1-e^{-u_{\alpha \beta}(\mathbf{r}) / T_{\alpha \beta}}\right) p_{\beta}\left(\mathbf{r}_{1}+\mathbf{r}\right) d \mathbf{r} .
$$

Assuming that the concentrations vary slowly over a length scale much larger than the range of the pairwise interac- tions, we expand $p_{\alpha}\left(\mathbf{r}_{1}+\mathbf{r}\right) \approx p_{\alpha}\left(\mathbf{r}_{1}\right)+\mathbf{r} \cdot \nabla p_{\alpha}\left(\mathbf{r}_{1}\right)+\frac{1}{2}(\mathbf{r} \cdot$ $\nabla)^{2} p_{\alpha}\left(\mathbf{r}_{1}\right)$. While inserting in the integrand, the first term gives the uniform or homogeneous contribution to the force, the second term vanishes, and the third term provides an inhomogeneous contribution to the force.

### A. Effective thermodynamic identities

We introduce the concentrations $c_{\alpha}(\mathbf{x})=N_{\alpha} p_{\alpha}(\mathbf{x})$, and obtain closed equations for the concentrations:

$$
\frac{\partial c_{\alpha}\left(\mathbf{r}_{1}\right)}{\partial t}=\frac{T_{\alpha}}{\zeta_{\alpha}} \nabla_{\mathbf{r}_{1}}^{2} c_{\alpha}\left(\mathbf{r}_{1}\right)-\frac{1}{\zeta_{\alpha}} \nabla_{\mathbf{r}_{1}} c_{\alpha}\left(\mathbf{r}_{1}\right) \bar{f}_{\alpha}\left(\mathbf{r}_{1}\right) .
$$

We have defined here the total mean force $\bar{f}_{\alpha}=\sum_{\beta} \bar{f}_{\alpha \beta}$ acting on a particle of species $\alpha$ due to all the other particles. In this particular case, this total mean force is the gradient of a potential and we can write the conservation equation for the concentrations in the Cahn-Hilliard form

$$
\frac{\partial c_{\alpha}\left(\mathbf{r}_{1}\right)}{\partial t}=\frac{1}{\zeta_{\alpha}} \nabla_{\mathbf{r}_{1}} \cdot c_{\alpha}\left(\mathbf{r}_{1}\right) \nabla_{\mathbf{r}_{1}} \mu_{\alpha} .
$$

This equation defines the functions $\mu_{\alpha}$ as nonequilibrium analogs of chemical potentials

$$
\mu_{\alpha}=\mu_{\alpha}^{\mathrm{id}}+\Phi_{\alpha}, \quad \mu_{\alpha}^{\mathrm{id}}=T_{\alpha} \ln c_{\alpha}, \quad-\bar{f}_{\alpha}\left(\mathbf{r}_{1}\right)=\nabla_{\mathbf{r}_{1}} \Phi_{\alpha} .
$$

We decompose the nonequilibrium chemical potentials as sums of a homogeneous part, which depends only on the concentration and a nonhomogeneous part, which depends on the concentration gradients

$$
\begin{gathered}
\mu_{\alpha}=\mu_{\alpha}^{0}+\mu_{\alpha}^{\nabla}, \quad \text { (9a) } \\
\mu_{\alpha}^{0}=T_{\alpha} \ln c_{\alpha}+\sum_{\beta} T_{\alpha \beta} B_{\alpha \beta} c_{\beta}, \\
\mu_{\alpha}^{\nabla}=\sum_{\beta} T_{\alpha \beta} \Lambda_{\alpha \beta} \nabla^{2} c_{\beta} .
\end{gathered}
$$

023200-2

The quantities $B_{\alpha \beta}=\int(1-e^{-u^{\alpha \beta}(\mathbf{r}) / T_{\alpha \beta}}) d \mathbf{r}$ are the effective excluded volumes or second virial coefficients $^{1}$ and $\Lambda_{\alpha \beta}=$ $\frac{1}{6} \int r^{2}(1-e^{-u^{\alpha \beta}(\mathbf{r}) / T_{\alpha \beta}}) d \mathbf{r}$.

The nonequilibrium chemical potentials can themselves be calculated as the functional derivatives of an effective nonequilibrium free energy $\mu_{\alpha}=\delta \mathcal{F} / \delta c_{\alpha}$ which is the functional derivative of the total free energy $\mathcal{F}[c_{\mathcal{A}}, c_{\mathcal{B}}]=\int f d \mathbf{r}$ with respect to the concentration $c_{\alpha}(\mathbf{r})$. The reconstruction of free energy from the chemical potentials gives the free energy per unit volume which is given by

$$
f=f^{0}+f^{\nabla}, \quad(10 \mathrm{a})
$$

$$
f^{0}=\sum_{\alpha} T_{\alpha} c_{\alpha} \ln (c_{\alpha} / e)+\sum_{\alpha, \beta} \frac{1}{2} T_{\alpha \beta} B_{\alpha \beta} c_{\alpha} c_{\beta}, \quad(10 \mathrm{~b})
$$

$$
f^{\nabla}=\sum_{\alpha, \beta} \frac{1}{2} L_{\alpha \beta}\left(\nabla c_{\alpha}\right)\left(\nabla c_{\beta}\right), \quad(10 \mathrm{c})
$$

where $L_{\alpha \beta}=-T_{\alpha \beta} \Lambda_{\alpha \beta}$ is negative. The free energy $f^{0}$ for uniform concentrations has already been derived in Ref. [11]. It has a Flory-Huggins form with differences in interactions dictated by the two different temperatures and the effective excluded volumes $B_{\alpha \beta}$'s (second virial coefficients). The contrast in temperatures further enhances the tendency toward demixing that is inherent to the Flory-Huggins free energy. For instance, in the case where all the virial coefficients $B_{\alpha}$ are identical $(B_{\mathcal{A}}=B_{\mathcal{A B}}=B_{\mathcal{B}})$ (which corresponds in particular to equal-sized hard spheres), solely the difference in temperatures drives asymmetrically weighted interactions between particles that are responsible for phase separation. A crucial remark is that the friction coefficients $\zeta_{\alpha}$ or the mobilities, which are the inverse of the friction coefficients, only enter through the effective pairwise temperature $T_{\mathcal{A B}}$ which becomes indistinct for $T_{\mathcal{A}}=T_{\mathcal{B}}$. Hence, a difference in diffusivities $\mathcal{D}_{\alpha} \propto T_{\alpha} / \zeta_{\alpha}$ at the same temperature $T_{\mathcal{A}}=T_{\mathcal{B}}$ but $\zeta_{\mathcal{A}} \neq \zeta_{\mathcal{B}}$ has no influence on the thermodynamics. This is expected a priori since in this case the system is at thermal equilibrium.

It is remarkable that the concept of effective free energy can be extended to inhomogeneous solutions of particles with two different temperatures. In a dilute limit, at lowest order in the concentration gradients, this shows compatibility with the Landau-Ginzburg theory [28]. A major difference in this case is that the steady state is maintained at the expense of extra power input [29].

### B. Internal stress

In order to derive the local stress tensor $\sigma_{i j}$ in the solution, we first calculate it from the free energy as could be done in an equilibrium system and then give a mechanical derivation based on the Irving-Kirkwood formulation of the stress, which leads to the same results.

#### a. Effective thermodynamic construction.
In a deformation of the volume $V+\delta V$, the total work is obtained by integrating the work across each surface element. If we call $d S_{j}$ the surface element and $u_{i}$ the infinitesimal displacement along, respectively, the $i$ and $j$ direction in Cartesian coordinates, the work associated to the deformation of the volume is

$$
\delta W=\int_{\partial V} d S_{j} u_{i} \sigma_{i j}. \quad(11)
$$

On the other hand, if there is an effective free energy, the work done by the displacement is $\delta W=\delta \mathcal{F}$. Hence, we may obtain the stress tensor $\sigma_{i j}$ from the surface contribution to the change in free energy $\delta \mathcal{F}$ which can be written as

$$
\delta \mathcal{F}=\int_{\delta V} f d \mathbf{r}+\int \delta f d \mathbf{r}. \quad(12)
$$

The first term on the right-hand side gives the surface integral $\int f(\mathbf{u} \cdot \mathbf{d S})$ while the second one can be converted to a surface integral by expanding $\delta f$ in terms of the changes in the concentrations $\delta c_{\alpha}$ induced by the deformation, i.e.,

$$
\begin{aligned}
\delta f= & \mu_{\mathcal{A}} \delta c_{\mathcal{A}}+\mu_{\mathcal{B}} \delta c_{\mathcal{B}} \\
& +\nabla \cdot\left(\frac{\partial f}{\partial\left(\nabla c_{\mathcal{A}}\right)} \delta c_{\mathcal{A}}\right)+\nabla \cdot\left(\frac{\partial f}{\partial\left(\nabla c_{\mathcal{B}}\right)} \delta c_{\mathcal{B}}\right). \quad(13)
\end{aligned}
$$

We study here the stress in a steady state, and as discussed in the previous sections, the chemical potentials $\mu_{\mathcal{A}}$ and $\mu_{\mathcal{B}}$ are constant throughout the volume. We can therefore eliminate the changes in concentrations $\delta c_{\alpha}$ by using the conservation of the total numbers of particles $\mathcal{A}$ and $\mathcal{B}$ during the deformation $\int_{V} \delta c_{\alpha}+\int_{\delta V} c_{\alpha}=0$.

The total change in the free energy can then be written as a surface integral

$$
\begin{aligned}
\delta \mathcal{F}= & \int_{\partial V} d S_{j}\left[u_{i}\left(f-\mu_{\mathcal{A}} c_{\mathcal{A}}-\mu_{\mathcal{B}} c_{\mathcal{B}}\right) \delta_{i j}\right. \\
& +\delta c_{\mathcal{A}}\left(L_{\mathcal{A}} \partial_{i} c_{\mathcal{A}}+L_{\mathcal{A B}} \partial_{i} c_{\mathcal{B}}\right) \\
& \left.+\delta c_{\mathcal{B}}\left(L_{\mathcal{B}} \partial_{i} c_{\mathcal{B}}+L_{\mathcal{A B}} \partial_{i} c_{\mathcal{A}}\right)\right].
\end{aligned}
$$

Finally, the variation of the concentration on the surface is given by $\delta c_{\alpha}=-\mathbf{u} \cdot \nabla c_{\alpha}$ for both species. The resulting stress tensor reads as

$$
\begin{aligned}
\sigma_{i j}= & \left(f-\mu_{\mathcal{A}} c_{\mathcal{A}}-\mu_{\mathcal{B}} c_{\mathcal{B}}\right) \delta_{i j} \\
& -\partial_{i} c_{\mathcal{A}}\left[L_{\mathcal{A}} \partial_{j} c_{\mathcal{A}}+L_{\mathcal{A B}} \partial_{j} c_{\mathcal{B}}\right] \\
& -\partial_{i} c_{\mathcal{B}}\left[L_{\mathcal{B}} \partial_{j} c_{\mathcal{B}}+L_{\mathcal{A B}} \partial_{j} c_{\mathcal{A}}\right].
\end{aligned}
$$

Accordingly, the pressure $p$ can be deduced directly from the diagonal component of the stress $p \delta_{i i}=-\sigma_{i i}$ which gives, in three dimensions,

$$
\begin{aligned}
p= & \left(\mu_{\mathcal{A}} c_{\mathcal{A}}+\mu_{\mathcal{B}} c_{\mathcal{B}}-f\right)+\frac{1}{3}\left[L_{\mathcal{A}}\left(\nabla c_{\mathcal{A}}\right)^{2}\right. \\
& \left.+L_{\mathcal{B}}\left(\nabla c_{\mathcal{B}}\right)^{2}+2 L_{\mathcal{A B}}\left(\nabla c_{\mathcal{A}}\right)\left(\nabla c_{\mathcal{B}}\right)\right].
\end{aligned}
$$

The first term contains the locally uniform pressure $p^{0}=$ $\left(\mu_{\mathcal{A}}^{0} c_{\mathcal{A}}+\mu_{\mathcal{B}}^{0} c_{\mathcal{B}}-f^{0}\right)$ that is given by the standard GibbsDuhem equation and the gradient terms including the contributions of $\mu_{\mathcal{A}}^{\nabla}, \mu_{\mathcal{B}}^{\nabla}$, and $f^{\nabla}$ determine the interfacial contributions.

#### b. Irving-Kirkwood method.
An alternative, more general method to calculate the stress tensor without any reference to the equilibrium thermodynamics has been proposed by

$^{1}$ This differs from the standard definition of virial coefficients by a factor of 2. We chose it this way to keep the free energy in Flory-Huggins form.

Irving and Kirkwood [30], starting from the mechanical virial equation [31]. The stress tensor $\sigma_{ij}^{(v)}$ is given by

$$
\sigma_{ij}^{(v)} = \sigma_{ij}^K + \frac{1}{2} \underbrace{\left\langle \sum_{\alpha,\beta} \frac{r_i r_j}{\mathbf{r}} \left( \frac{\partial u_{\alpha\beta}(\mathbf{r})}{\partial r} \right) \right\rangle}_{\sigma_{ij}^u},
\tag{17}
$$

where $\sigma_{ij}^K$ is the stress in the absence of interactions (for an ideal gas), while the second part is the contribution to the stress due to interparticle potentials that we name $\sigma_{ij}^u$. The interaction part of the stress can be decomposed into a sum over the particle species $\alpha$ and $\beta$ and the average in Eq. (17) can be calculated using the two-particle probability distribution $p_2^{\alpha\beta}(\mathbf{r}_1, \mathbf{r})$. As in the previous paragraphs, we expand the two-particle densities around $\mathbf{r}_1$, and make a change of variables to calculate the average values. This leads to the following stress:

$$
\begin{aligned}
\sigma_{ij}^u =& \sum_{\alpha,\beta} \frac{N_\alpha N_\beta}{2} \int \frac{r_i r_j}{\mathbf{r}} \frac{\partial u_{\alpha\beta}(\mathbf{r})}{\partial r} \\
& \times \sum_{l=1}^\infty \frac{(-\mathbf{r} \cdot \nabla)^{l-1}}{l!} p_2^{\alpha\beta}(\mathbf{r}_1, \mathbf{r}) d\mathbf{r}.
\tag{18}
\end{aligned}
$$

The rest of the calculation is straightforward. We give the full result of this calculation in Appendix B. It turns out that the stress tensor calculated by the Irving-Kirkwood method is different from the stress calculated from the free energy; it can be written as $\sigma_{ij}^{(v)} = \sigma_{ij}^{(f)} + \sigma_{ij}'$ where $\sigma_{ij}^{(f)}$ is the stress obtained in the previous paragraph from the free energy (15). This shows that the stress is not defined in a unique way [32]. However, it conserves all the properties of $\sigma_{ij}^{(f)}$ for our analysis, and strictly does not alter the force-balance since $\partial_i \sigma_{ij}' = 0$. Interestingly, $\sigma_{ij}^{(v)}$ could just be obtained from a free-energy perturbation by adding surface terms $-\frac{1}{3} \nabla^2 [L_A c_A^2 + 2L_{AB} c_A c_B + L_B c_B^2]$ to the free energy given by Eq. (10a).

This result validates that in the limit of low concentrations, we can still use the thermodynamic approach to calculate the stress inside the solution. In the more general case where there is no effective free energy, one would need to rely on the Irving-Kirkwood description. A final note is that an alternative formulation of Irving-Kirkwood method can be achieved by using microscopic force balance [33,34] in the time-evolution equations (6), thus summing up all mean internal forces.

## III. PHASE LINES AND THE CRITICAL POINT

We now use the effective thermodynamic description of the solution to calculate the phase diagram of a solution of particles at two different temperatures.

### A. Dimensionless effective thermodynamic quantities

Let us introduce first the volume fractions $\phi_\alpha = c_\alpha B_\alpha / \epsilon_\alpha$ where $\epsilon_\alpha \equiv B_\alpha / v_\alpha$ is the conversion factor to molecular volume $v_\alpha$. The volume factions are well defined only if the total volume fraction is smaller than one. They must then satisfy $\phi_A + \phi_B \leqslant 1$. We also define $\beta_B = \epsilon_B B_{AB}/(B_B)$, the temperature ratio $\alpha_T = T_A/T_B$, volume ratio $\alpha_v = v_A/v_B$, and the friction ratio $\alpha_\zeta = \zeta_A/\zeta_B$. Finally, we define $\hat{L}_{\alpha\beta} = T_B^{-1} L_{\alpha\beta} v_A / (v_\alpha v_\beta)$. Accordingly, we set the dimensionless free-energy density $\hat{f} = T_B^{-1} v_A f$ while the total free energy is $\hat{\mathcal{F}} = \int \hat{f} d\mathbf{r}$. As a result, we obtain the dimensionless chemical potentials $\hat{\mu}_\alpha = \delta \hat{\mathcal{F}} / \delta \phi_\alpha$:

$$
\begin{aligned}
\hat{\mu}_A \equiv T_B^{-1} \mu_A =& \alpha_T (\ln \phi_A + \epsilon_A \phi_A) + \frac{\alpha_T + \alpha_\zeta}{1 + \alpha_\zeta} \beta_B \phi_B \\
& - \hat{L}_A \nabla^2 \phi_A - \hat{L}_{AB} \nabla^2 \phi_B,
\tag{19}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\mu}_B \equiv T_B^{-1} \alpha_v \mu_B =& \alpha_v (\ln \phi_B + \epsilon_B \phi_B) + \frac{\alpha_T + \alpha_\zeta}{1 + \alpha_\zeta} \beta_B \phi_A \\
& - \hat{L}_B \nabla^2 \phi_B - \hat{L}_{AB} \nabla^2 \phi_A,
\tag{20}
\end{aligned}
$$

where we ignored the density-independent terms. Note that $\hat{\mu}_B$ has an extra scaling factor $\alpha_v$ in order to conserve all the functional properties to construct the thermodynamic functions of the previous section. Similarly for pressure we have $\hat{p} = T_B^{-1} v_A p$. This completes our transformation to dimensionless functionals $X[c_A(\mathbf{r}), c_B(\mathbf{r})] \to \hat{X}[\phi_A(\mathbf{r}), \phi_B(\mathbf{r})]$. As in the previous case, we can separate these into locally uniform and interfacial components, i.e., $\hat{X} = \hat{X}^0 + \hat{X}^\nabla$.

### B. Two-phase coexistence

At zero-flux steady state for single-particle concentrations, we should have uniform chemical potentials and pressure. For a mixed state this would suggest to have uniform concentrations (a single phase). However, if there are any two phases coexisting, they should satisfy the following conditions at their interface:

$$
\hat{\mu}_A^0 (\phi_A^a, \phi_B^a) = \hat{\mu}_A^0 (\phi_A^b, \phi_B^b),
\tag{21a}
$$

$$
\hat{\mu}_B^0 (\phi_A^a, \phi_B^a) = \hat{\mu}_B^0 (\phi_A^b, \phi_B^b),
\tag{21b}
$$

$$
\hat{p}^0 (\phi_A^a, \phi_B^a) = \hat{p}^0 (\phi_A^b, \phi_B^b),
\tag{21c}
$$

where $a$ and $b$ denote the two coexisting phases. Together, these suggest no net particle exchange and force balance at phase boundary while concentrations continuously vary from one phase to the other. We obtain the coexistence curve (or binodal line) in our phase diagrams by numerically solving the above conditions.

### C. Spinodal line

The stability of the uniform state $\phi_A(\mathbf{r}) = \phi_A^0$ and $\phi_B(\mathbf{r}) = \phi_B^0$ can be analyzed by linearizing $\partial \phi_A / \partial t$ and $\partial \phi_B / \partial t$ around the uniform state by introducing $\phi_A(\mathbf{r}) = \phi_A^0 + \delta \phi_A(\mathbf{r})$ and $\phi_B(\mathbf{r}) = \phi_B^0 + \delta \phi_B(\mathbf{r})$ where $\phi_A^0$ and $\phi_B^0$ denote the uniform states. As a result, we obtain in Fourier space the equation of the relaxation of a perturbation of wave vector $\mathbf{q}$, $\delta \tilde{\phi}(\mathbf{q}) = (\delta \tilde{\phi}_A(\mathbf{q}), \delta \tilde{\phi}_B(\mathbf{q}))$

$$
\frac{\partial \delta \tilde{\phi}(\mathbf{q})}{\partial t} = -q^2 \Gamma \delta \tilde{\phi}(\mathbf{q}),
\tag{22}
$$


with the relaxation matrix
$$
\Gamma=T_{B}\left(\begin{array}{cc}
\phi_{\mathcal{A}}^{0} \zeta_{\mathcal{A}}^{-1} & 0 \\
0 & \alpha_{v}^{-1} \phi_{\mathcal{B}}^{0} \zeta_{\mathcal{B}}^{-1}
\end{array}\right) \kappa_{p}^{-1},
$$

$$
\kappa_{p}^{-1}=\left(\begin{array}{cc}
\alpha_{T}\left(\frac{1+\epsilon_{\mathcal{A}} \phi_{\mathcal{A}}}{\phi_{\mathcal{A}}}\right) & \frac{\alpha_{T}+\alpha_{\zeta}}{1+\alpha_{\zeta}} \beta_{\mathcal{B}} \\
\frac{\alpha_{T}+\alpha_{\zeta}}{1+\alpha_{\zeta}} \beta_{\mathcal{B}} & \alpha_{v}\left(\frac{1+\epsilon_{\mathcal{B}} \phi_{\mathcal{B}}}{\phi_{\mathcal{B}}}\right)
\end{array}\right),\qquad(23)
$$

where $\kappa_{p}^{-1}$ is the inverse of the compressibility matrix obtained from the linearization of the chemical potentials and we have neglected terms of order $q^{4}$. Note that in $\kappa_{p}^{-1}$ and for the remainder, we no longer write the superscript zero of $\phi_{\alpha}$'s. The instability occurs when at least one of the eigenvalues of $\Gamma$ becomes negative. Thus, it is enough to determine the limit where the determinant $|\kappa_{p}^{-1}|$ is negative. The nondimensionalized spinodal line equation is obtained as
$$
v_{s}=\frac{1+\epsilon_{\mathcal{A}} \phi_{\mathcal{A}}}{\phi_{\mathcal{A}}} \frac{1+\epsilon_{\mathcal{B}} \phi_{\mathcal{B}}}{\phi_{\mathcal{B}}}-\frac{\left(\alpha_{T}+\alpha_{\zeta}\right)^{2} \beta_{\mathcal{B}}^{2}}{\left(1+\alpha_{\zeta}\right)^{2} \alpha_{T} \alpha_{v}}=0 \quad(24)
$$
for vanishing wave vector $q$. The instability occurs when $v_{s}<0$. The spinodal line is symmetric if $\epsilon_{\mathcal{A}}=\epsilon_{\mathcal{B}}$. It is clear that a larger contrast of activity, i.e., a larger $\alpha_{T}$ enlarges unstable region of the phase diagram.

### D. Critical point
The critical point is calculated by finding the point where the two phases in equilibrium are identical [35]. This is the point along spinodal line where the fluctuations are maximum. Hence, we search for the point along the spinodal line where the gradient of the spinodal line in the volume fraction parameter space $\nabla v_{s}=\widetilde{\phi}_{\mathcal{A}} \partial_{\phi_{\mathcal{A}}} v_{s}+\phi_{\mathcal{B}} \partial_{\phi_{\mathcal{B}}} v_{s}$ is aligned with the eigenvector $\mathbf{e}_{0}$ of the inverse compressibility matrix, corresponding to the eigenvalue $\epsilon=0$. Accordingly, the volume fractions at the critical point $(\phi_{\mathcal{A}}^{*}, \phi_{\mathcal{B}}^{*})$ satisfy
$$
\frac{\phi_{\mathcal{B}}^{*}\left(1+\epsilon_{\mathcal{B}} \phi_{\mathcal{B}}^{*}\right)}{\left(1+\epsilon_{\mathcal{A}} \phi_{\mathcal{A}}^{*}\right)^{2}}=\frac{\alpha_{T}\left(1+\alpha_{\zeta}\right)}{\beta_{\mathcal{B}}\left(\alpha_{T}+\alpha_{\zeta}\right)},\qquad(25a)
$$

$$
v_{s}\left(\phi_{\mathcal{A}}^{*}, \phi_{\mathcal{B}}^{*}\right)=0.\qquad(25b)
$$

We observe that even at $\epsilon_{\mathcal{A}}=\epsilon_{\mathcal{B}}$ where the spinodal line is symmetric, the location of the critical point can be shifted along the spinodal line by controlling the ratio $\alpha_{T}/\alpha_{v}$. One easy way to see that is to use the conjugate of Eq. (25) and symmetrize these two forms for $\phi_{\mathcal{A}}$ and $\phi_{\mathcal{B}}$. Accordingly, choosing $\alpha_{T}>\alpha_{v}$ moves the critical point toward the $\mathcal{B}$-rich part of the phase diagram while setting $\alpha_{T}<\alpha_{v}$ moves it toward the $\mathcal{A}$-rich side. However, if $\epsilon_{\mathcal{A}} \neq \epsilon_{\mathcal{B}}$, it seems more complicated to get a sense on such symmetrization and one should follow Eq. (C2). We will investigate further the properties of such asymmetric phase diagrams in Sec. V in order to get a hint on the structure of coexisting phases that can be either both liquidlike phases or a solidlike and a gaslike phase.

### E. Condition for existence of phase separation
In the previous paragraphs, we outlined the calculation of phase diagrams using the effective free energy obtained in the limit of low concentrations, but imposing no constraints on the volume fractions and assuming that both phases remain fluid. If the volume fractions are high enough in one of the phases, this phase cannot be fluid and is solid. There is in this case equilibrium between a liquid or gaseous (very dilute) phase and a solid phase for which our concentration expansion is not accurate but approximate. Still, it qualitatively indicates a crystalline phase. Simulations show that this phase exhibits hexagonal packing in two dimensions [12], while both face-centered-cubic and hexagonal-close-packed structures in three dimensions [36]. On the other hand, for hard-sphere interactions and considering that the two phases remain fluid, we improve our approximation in Sec. VI by adding one order in concentration.

A general constraint on the volume fractions is that the total volume fraction is not space filling and that it is smaller than the critical concentration for space filling $\phi_{\text{max}}$ (for a random packing of identical spheres $\phi_{\text{max}} \simeq 0.64$). Here, for generality, we stick with $\phi_{\text{max}}=1$ following the general literature. This choice, together with low-density approximation, is sufficient to observe qualitative tendency to phase separate while varying interaction and activity parameters.

A common approach to study the conditions for phase separation [37] is to impose this space-filling condition for the spinodal line given by Eq. (24). This conjecture accepts the emergence of an instability region in the phase diagram as the sufficient condition for phase separation. An alternative more restrictive view would be that the critical point should exist inside a physical phase diagram. In this case, the valid condition is the existence of the critical point inside the physical regime. These two approaches are identical if the critical point is at the tip of the spinodal line while the latter condition delays the onset of the coexistence region. We evaluate both conditions for the cases we consider (Fig. 3).

## IV. PHASE-SEPARATION KINETICS
Knowing the coexisting phases and the effective thermodynamic description, we can develop the theory of phase-separation kinetics for two temperature mixtures. We start here by determining the surface tension between two phases at equilibrium and then discuss phase-separation kinetics. Note that the interface between the two phases is stable only if the surface tension is positive.

### A. Surface tension
We consider a mixture with two phases at equilibrium and with a flat interface between the two phases. In this geometry, the two concentrations or the volume fractions vary only along one direction, say the $z$ direction, so that $\partial_{y}c_{\alpha}=\partial_{x}c_{\alpha}=0$. The stress is isotropic in the bulk of each phase but becomes anisotropic close to the interface. The interfacial tension between the two phases can be calculated from the stress distribution in the solution
$$
\gamma=\int_{z_{a}}^{z_{b}}\left(\sigma_{x x}-\sigma_{z z}\right) d z,\qquad(26)
$$
where the integration is from one phase (phase $a$) to the other (phase $b$). Using our calculated value of the stress tensor $\sigma_{ij}$ [Eq. (15)], we see that the isotropic component of the stress proportional to $\delta_{ij}$ cancels out and that only the nondiagonal

components of the stress contribute to the surface tension: they vanish for $\sigma_{xx}$ but do not vanish for $\sigma_{zz}$. In dimensionless form, $\hat{\sigma}_{ij} \equiv v_{A} T_{B}^{-1} \sigma_{ij}$, we find

$$
\begin{aligned}
\hat{\sigma}_{x x}-\hat{\sigma}_{z z}=\hat{L}_{A}\left(\partial_{z} \phi_{A}\right)^{2}+\hat{L}_{B}\left(\partial_{z} \phi_{B}\right)^{2}+2 \hat{L}_{A B}\left(\partial_{z} \phi_{A}\right)\left(\partial_{z} \phi_{B}\right).
\end{aligned}
$$

In order to determine the surface tension $\gamma$ from Eqs. (26) and (27), we then need to determine the concentration profiles along the $z$ direction. We first introduce the boundary conditions in the two phases in equilibrium: (i) $\hat{\mu}_{A}(\phi_{A}^{a}, \phi_{B}^{a})=$ $\hat{\mu}_{A}^{\dagger}=\hat{\mu}_{A}(\phi_{A}^{b}, \phi_{B}^{b})$, (ii) $\hat{\mu}_{B}(\phi_{A}^{a}, \phi_{B}^{a})=\hat{\mu}_{B}^{\dagger}=\hat{\mu}_{B}(\phi_{A}^{b}, \phi_{B}^{b})$, and (iii) $\hat{p}(\phi_{A}^{a}, \phi_{B}^{a})=\hat{p}^{\dagger}=\hat{p}(\phi_{A}^{b}, \phi_{B}^{b})$, where the values with daggers are the constant values of the chemical potentials and the pressure at equilibrium. The concentration profiles can then be calculated from the coupled differential equations:

$$
\hat{\mu}_{A}^{0}(z)-\hat{\mu}_{A}^{\dagger}=\hat{L}_{A} \nabla^{2} \phi_{A}(z)+\hat{L}_{A B} \nabla^{2} \phi_{B}(z), \quad(28 \mathrm{a})
$$

$$
\hat{\mu}_{B}^{0}(z)-\hat{\mu}_{B}^{\dagger}=\hat{L}_{B} \nabla^{2} \phi_{B}(z)+\hat{L}_{A B} \nabla^{2} \phi_{A}(z). \quad(28 \mathrm{~b})
$$

Using the Gibbs-Duhem expression of the free energy in the phases at equilibrium, $\hat{f}^{0}=\hat{\mu}_{A}^{0} \phi_{A}+\hat{\mu}_{B}^{0} \phi_{B}-$ $\hat{p}^{0}$ and integrating Eq. (28) is consistent with $\hat{\sigma}_{x x}-\hat{\sigma}_{z z}=$ $\Delta \hat{f}[\phi_{A}(z), \phi_{B}(z)]$ where the tilted free energy is given by

$$
\Delta \hat{f}=\hat{f}-\left(\hat{\mu}_{A}^{\dagger} \phi_{A}+\hat{\mu}_{B}^{\dagger} \phi_{B}-\hat{p}^{\dagger}\right). \quad(29)
$$

While this is the generic form, the same treatment more specifically implies that $\Delta \hat{f}=2 \Delta \hat{f}^{0}$. The tilted free energy is the difference between the local free energy along the concentration profiles and the energy obtained from the so-called common tangent construction. Since the common tangent construction gives the minimal possible free energy, the tilted free energy is always positive $\Delta \hat{f}>0$ as long as one can solve the set of equations (28) with appropriate boundary conditions. We may therefore write an alternative form of the interfacial tension :

$$
\hat{\gamma} \equiv T_{B}^{-1} v_{A} \gamma=2 \int_{z_{a}}^{z_{b}} \Delta \hat{f}^{0}\left(\phi_{A}(z), \phi_{B}(z)\right) d z. \quad(30)
$$

If there is a consistent profile, the surface tension $\gamma$ is therefore always positive and the interface between the two phases is stable. The set of equations (28) can be solved numerically by linearization of the two equations around one boundary (say phase $a$) and integrating up to the other boundary (phase $b$) using a shooting method. Alternatively, an analytical approximation can be obtained by considering the system close to the critical point as done in the next paragraph. This analytical approximation is in excellent agreement with the numerical results.

Surface tension near the critical point. In the vicinity of the critical point, we show in Appendix C how the effective thermodynamics can be expressed as a function of a single order parameter $\psi$ which is a linear combination volume fractions relative to the critical point. In addition, the other normal coordinate $\eta$ gives the normal distance from the critical point, and a phase separation occurs when a solution exists $\eta_{a} \approx$ $\eta_{b}>0$. Each value of $\eta_{a}$ defines the two coexisting phases $\psi_{a}$ and $\psi_{b}$. The transformed coordinates are illustrated in Fig. 1, where at first the concentration profiles $\phi_{A}(z)$ and $\phi_{B}(z)$ are obtained by solving Eq. (28) numerically. The effective tilted free-energy density is given in (C11) as a function of the order parameter only, which is obtained by transforming (29) to normal coordinates. Minimization with respect to $\psi$ leads to

$$
\Delta \hat{f}^{0}=\frac{1}{4} k_{\psi}\left(\psi-\psi_{a}\right)^{2}\left(\psi-\psi_{b}\right)^{2}=\frac{1}{2} \hat{L}_{\psi}(\nabla \psi)^{2}. \quad(31)
$$

![](./images/812634499077636096_2.jpg)

FIG. 1. Example density profiles between coexisting phases for hard spheres with $\alpha_{v}=27$ and $\alpha_{T}=20$ and $\epsilon_{A}=\epsilon_{B}=\beta_{B}=8$ and hence $\tan \theta^{*} \approx 0.836$. We show (a) profiles of the particle volume fractions $\delta \phi_{A}=\phi_{A}(z)-\phi_{A}^{*}$ and $\delta \phi_{B}=\phi_{B}(z)-\phi_{B}^{*}$, (b) profiles of the normal coordinates $\psi(z)$ and $\eta(z)$; we observe that $\eta(z) \ll \psi(z)$. The interface width is $2 \ell$ and away from the interface the densities take constant values at two coexisting phases.

Equations (30) and (31) suggest that $\hat{\gamma}=\hat{L}_{\psi} \int(\nabla \psi)^{2}$, and hence the sign of $L_{\psi}$ determines the sign of the surface tension. It is then simple to prove that the surface tension for equal-sized hard spheres is positive for all $\alpha_{T}$ values. For hard spheres with varying size ratios, we checked by numerical evaluation of $L_{\psi}$ that it is positive for the values of the parameters $\alpha_{V}$ and $\alpha_{T}$ that lead to a phase separation except when $\alpha_{v} \ll 1$ or $\alpha_{v} \gg \alpha_{T}$ (see Appendix D for calculations, and Sec. VB for more discussion). The solution of (31) gives the concentration profile

$$
\psi=\frac{\Delta \psi_{a b}}{2} \tanh z / \ell, \quad(32)
$$

where the interface width is $\ell=\left(\frac{8 L_{\psi}}{\Delta \psi_{a b}{ }^{2} k_{\psi}}\right)^{1 / 2}$. The surface tension can then be calculated by integration of Eq. (27) where we keep only the terms involving the gradient of $\psi$ :

$$
\hat{\gamma} \approx \frac{1}{12}\left(\Delta \psi_{a b}\right)^{3}\left(2 k_{\psi} \hat{L}_{\psi}\right)^{1 / 2}. \quad(33)
$$

In order to look at the scaling variation with parameters of the mixture such as $\alpha_{T}$ or $\alpha_{v}$, one must express the dimensionless quantities that we used as functions of these parameters. Taking as an example equal-sized hard spheres

023200-6

where $\alpha_{v}=1$, and hence $\alpha_{\zeta}=1$, $\epsilon_{\mathcal{A}}=\epsilon_{\mathcal{B}}=\beta_{\mathcal{B}}=8$, the volume fractions at the critical point are given by $\phi_{\mathcal{A}}^{*}=\alpha_{T}^{-1}$, $\phi_{\mathcal{B}}^{*}=1 / 8+(5 / 4) \alpha_{T}^{-1}$ when $\alpha_{T} \gg 1$. Considering a particle mixture of given volume fractions of particles (which could be called the laboratory conditions) $\phi_{\mathcal{A}}^{0}$ and $\phi_{\mathcal{B}}^{0}$ defined by $\phi_{\alpha}^{0}=V^{-1} \int_{V} \phi_{\alpha}(\mathbf{r}) d \mathbf{r}$ and for finite volume fractions in the vicinity of the critical point, we obtain
$$
\hat{\gamma} \sim\left(\phi_{\mathcal{A}}^{0}\right)^{3 / 2} v_{0}^{1 / 3} \alpha_{T}^{3 / 2}, \quad(34)
$$
where $v_{0}$ is the volume of the particles. The real surface tension is then $\gamma=T_{\mathcal{B}} v_{0}^{-1} \hat{\gamma}$. The surface tension therefore increases as a power law of the ratio between the temperatures of the two types of particles $\alpha_{T}$ (see Appendix E for details).

### B. Kinetics of droplet growth
We consider a mixture quenched in the two-phase region which is therefore supersaturated. We focus on a spherical droplet of phase $b$ with radius $R$, growing inside the background phase which has a composition close to phase $a$. The volume fractions outside the droplet are not equal to the concentrations in the $a$ phase due to the supersaturation, i.e., $\phi_{\mathcal{A}} \rightarrow \phi_{\mathcal{A}}^{a}+\delta \phi_{\mathcal{A}}$ and $\phi_{\mathcal{B}} \rightarrow \phi_{\mathcal{B}}^{a}+\delta \phi_{\mathcal{B}}$. Note that the concentrations inside the droplet are also slightly different from the concentrations of the $b$ phase but we can ignore this difference here.

This is a multiscale problem with two well-separated length scales: the width of the interface $\ell$ is much smaller than the droplet size $R$. At the scale of the small length $\ell$, the system is still close to equilibrium with chemical potentials $\hat{\mu}_{\mathcal{A}}^{\prime}$ and $\hat{\mu}_{\mathcal{B}}^{\prime}$ which are the chemical potentials slightly shifted from the phase equilibrium values and calculated outside the droplet on its surface. The steady-state equations, which give the particle concentration profiles, are
$$
\begin{aligned}
\frac{\partial \hat{f}}{\partial \phi_{\mathcal{A}}}-\hat{\mu}_{\mathcal{A}}^{\prime}= & \hat{L}_{\mathcal{A}}\left(\frac{\partial^{2} \phi_{\mathcal{A}}}{\partial r^{2}}+\frac{2}{r} \frac{\partial \phi_{\mathcal{A}}}{\partial r}\right) \\
& +\hat{L}_{\mathcal{A B}}\left(\frac{\partial^{2} \phi_{\mathcal{B}}}{\partial r^{2}}+\frac{2}{r} \frac{\partial \phi_{\mathcal{B}}}{\partial r}\right),
\end{aligned}\quad(35)
$$

$$
\begin{aligned}
\frac{\partial \hat{f}}{\partial \phi_{\mathcal{B}}}-\hat{\mu}_{\mathcal{B}}^{\prime}= & \hat{L}_{\mathcal{B}}\left(\frac{\partial^{2} \phi_{\mathcal{B}}}{\partial r^{2}}+\frac{2}{r} \frac{\partial \phi_{\mathcal{B}}}{\partial r}\right) \\
& +\hat{L}_{\mathcal{A B}}\left(\frac{\partial^{2} \phi_{\mathcal{A}}}{\partial r^{2}}+\frac{2}{r} \frac{\partial \phi_{\mathcal{A}}}{\partial r}\right).
\end{aligned}\quad(36)
$$

In order to solve the so-called inner problem at the length scale $\ell$, we choose a length $\delta$ such that $\ell \ll \delta \ll R$. We multiply the first equation by $\partial \phi_{\mathcal{A}} / \partial r$ and the second one by $\partial \phi_{\mathcal{B}} / \partial r$, add them up and then integrate across the interface over a region of size $\delta$ such that in both phases, $\partial \phi_{\mathcal{A}} / \partial r=$ $\partial \phi_{\mathcal{B}} / \partial r=0$ away from the interface. As a result, we obtain the Gibbs-Thomson relation [38]
$$
\delta \hat{\mu}_{\mathcal{A}} \Delta \phi_{\mathcal{A}}^{a b}+\delta \hat{\mu}_{\mathcal{B}} \Delta \phi_{\mathcal{B}}^{a b}=\frac{2 \hat{\gamma}}{R}, \quad(37)
$$
where for each species, $\Delta \phi_{\alpha}^{a b}=\phi_{\alpha}^{b}-\phi_{\alpha}^{a}$ and $\delta \hat{\mu}_{\alpha}=\hat{\mu}_{\alpha}^{\dagger}-$ $\hat{\mu}_{\alpha}^{\prime}$. Note that outside the droplet, as discussed below, the volume fractions and the chemical potentials vary over the large length scale $R$ and do not change over the length $\delta$. As in the previous section, we now transform the volume fractions to normal coordinates and obtain
$$
\delta \hat{\mu}_{\eta} \Delta \eta_{a b}+\delta \hat{\mu}_{\psi} \Delta \psi_{a b}=\frac{2 \hat{\gamma}}{R}. \quad(38)
$$

The noncritical variable $\eta$ is identical in the two phases so that $\Delta \eta_{a b}=0$. The small variation of the chemical potential $\delta \hat{\mu}_{\psi}$ can be obtained from Eq. (C7) as $\delta \hat{\mu}_{\psi} \simeq 2 k_{\psi} \psi_{a}^{2} \delta \psi$ using Eq. (C10) where $\delta \psi=\psi(R)-\psi_{a}$ is the small shift of the order parameter on the surface of the droplet from its equilibrium value in phase $a$. Then, rearranging Eq. (38), we have
$$
\delta \psi(R)=\frac{\hat{\gamma}}{R k_{\psi} \psi_{a}^{2} \Delta \psi_{a b}}. \quad(39)
$$

We now study the dynamics of the growing droplet by studying the outer problem, calculating the order-parameter profile of the droplet material. As the noncritical variable $\eta$ has the same value in the two phases and as we find numerically that its variation is very small, we will assume here that there is no flux associated to this variable. The problem then has a single conserved order parameter $\psi$.

Outside the droplet, the order parameter $\psi$ follows a diffusion equation $\partial \psi / \partial t=D_{\psi} \nabla^{2} \psi$. We discuss the value of the effective diffusion constant $D_{\psi}$ in Appendix F. The boundary conditions for this diffusion equation are the value $\delta \psi(R)$ given by the Eq. (39) and the value at infinity $\psi_{\infty}$ which measures the supersaturation. The solution of the diffusion equation is
$$
\psi(r)=\psi_{\infty}-(R / r)\left[\delta \psi_{\infty}-\delta \psi(R)\right]. \quad(40)
$$

The growth of the droplet is due to the radial flux $j_{\psi}=$ $-D_{\psi} \frac{\partial \psi}{\partial r}|_{r=R}$ The conservation of the flux of the order parameter $\psi$ on the surface of the droplet leads to $\Delta \psi_{a b} \frac{d R}{d t}=$ $D_{\psi} \frac{\partial \psi}{\partial r}|_{R}$. Inserting the solution of the diffusion equation, we obtain the evolution of the radius of the droplet
$$
\frac{d R}{d t}=\frac{D_{\psi}}{R}\left(\Delta-\frac{d_{0}}{R}\right), \quad(41)
$$
where the supersaturation is defined as $\Delta=\delta \psi(\infty) / \Delta \psi_{a b}$ and $d_{0}=\hat{\gamma} /\left(k_{\psi} \psi_{a}^{2} \Delta \psi_{a b}^{2}\right)$ is a length of the order of the interfacial width $\ell$. This gives the critical nucleation radius of the droplet $R_{c}=d_{0} / \Delta$. Droplets smaller than $d_{0}$ collapse whereas droplets larger than $d_{0}$ grow.

At the early stages of the phase separation just after the quench, there are few droplets and the droplets that are larger than the critical radius grow as $R \sim t^{1 / 2}$. At long times, the value of the supersaturation decreases with time and a much more detailed analysis is required, which has been made by Lifshitz and Slyozov [39]. The supersaturation decreases as $\Delta \sim d_{0} / R$ and the average droplet radius increases as $R \sim t^{1 / 3}$. Plugging in the value of $D_{\psi}$ obtained in Appendix F gives the scaling of droplet growth with time, $R \sim\left(r_{G} t\right)^{1 / 3}$ in which the growth rate of mean droplet volume $r_{G} \sim\left(\phi_{\mathcal{A}}^{0} \alpha_{T}\right)^{1 / 2} v_{0}^{1 / 3} T_{\mathcal{B}} / \zeta$ that is linearly proportional to the geometric mean of $T_{\mathcal{A}}$ and $T_{\mathcal{B}}$.

Here, we obtain these power laws in the dilute limit of our two-temperature model (which can be mapped on an

![](./images/812634499077636096_3.jpg)

FIG. 2. Triangular phase diagrams for three-component system $\phi_A, \phi_B, \phi_s$(solvent) where $\phi_A + \phi_B + \phi_s = 1$; for every point in the triangle, the volume fractions are given by their distance from the facing triangle (exemplified on scaled inset by star). Both diagrams are for hard-sphere systems $(a_{\alpha\beta}=0, \epsilon_A = \epsilon_B = 8)$ with temperature ratio $T_A/T_B = 20$ while size ratios differ. In (a) $v_A = v_B$ whereas in (b) $v_A = 27v_B$. The purple and dashed orange lines show binodal and spinodal lines, respectively, and red dots are the critical points. The location of the critical point is asymmetric in both cases (though in opposite directions). Moreover, in (a) we mark two coexisting phases $a$ and $b$ (purple squares) which are strongly asymmetric. Starting from the initial well-mixed setup, the system phase separates into a solidlike close-packed $B$ particle (phase $b$) surrounded by an $A$ gas (phase $a$) as illustrated in top left inset. In (b) the phase diagram appears to be more symmetric, indicating both liquidlike coexisting phases though shifted slightly toward $A$-rich side. This results from having $\alpha_T/\alpha_v = 20/27 \lesssim 1$, the ratio which controls the symmetry of two phases (see Sec. III D)

equilibrium system). On the other hand, at higher order in the density expansion even though the solution parameters $(\Delta, d_0, D_\psi, r_G)$ change, there is no reason to expect a different power-law behavior than $R \sim t^{1/3}$ as long as the droplet material is transported by diffusion. Similar examples include one-component active fluids which respect the $\frac{1}{3}$ law [40,41].

## V. SOME APPLICATIONS OF THE THEORY

In this section, we show a few examples of application of the theory, to various systems. Some of these results are in accordance with existing numerical studies while some may motivate future experiments and simulations.

As discussed earlier, the intraspecies and interspecies interactions can be controlled either by modifying the interaction potentials between particles or by changing the activity difference (the temperature ratio). In the first case, one alters the virial coefficients while in the latter case, one changes both the entropic part of the effective free energy by changing the temperatures $T_\alpha$ but also the weight of the interactions through the pairwise temperatures $T_{\alpha\beta}$ as seen in Eq. (10b). In general, for short-range interactions, the second virial coefficients can be written as $B_{\alpha\beta} \approx b_{\alpha\beta} + a_{\alpha\beta}/T_{\alpha\beta}$, where $b_{\alpha\beta}$ is the effective pair excluded volume and $a_{\alpha\beta}$ is the additional interaction part. Moreover, $b_{\alpha\beta}$ can be approximated by its hard-core value. As an example, for spherical particles, $b_{\alpha\beta} \approx (4\pi/3)d_{\alpha\beta}^3$ and $a_{\alpha\beta} \approx 4\pi \int_{d_{\alpha\beta}}^\infty u_{\alpha\beta}(r)r^2 dr$ where $d_{\alpha\beta}$ is the distance between the centers of the particles at contact for an $\alpha\beta$ pair. If the additional interaction is purely attractive, $a_{\alpha\beta} < 0$ is negative whereas it is positive if the additional interaction is repulsive. For a mixture of particles with given hard-core sizes, this part of the virial coefficient can be tuned by chemical modifications. In addition, the contrast in activity which can be adjusted by the energy input per constituent, provides an extra handle [6,42] for controlling the phase separation.

### A. Colloidal hard spheres with different temperatures

Pure hard spheres interact with each other only through excluded volume interactions, which do not allow them to interpenetrate: $a_{\alpha\beta} = 0$ and $B_{\alpha\beta} = b_{\alpha\beta}$. The dramatic influence of activity contrast toward demixing is clearly observed in mixtures of hard spheres with equal sizes and hence equal mobilities [12]. In Fig. 2(a) we show the phase diagram for equal-sized hard spheres $\alpha_v = 1$, $\alpha_\zeta = 1$, then $\epsilon_A = \epsilon_B = \beta_B = 8$ with temperature ratio $\alpha_T = 20.^2$ The volume fractions of the cold and hot particles are not equal at the critical point where the volume fraction of the cold particles is larger, indicating asymmetric phases. As exemplified in the phase diagram, starting from a mixture in the unstable region, the system phase separates into a solidlike close-packed $B$ particle (phase $\beta$, which is not quantitatively well described by our low-density approximation) surrounded by an $A$ gas (phase $\alpha$) as illustrated by top left inset.

Using our formalism, we can also investigate the phase behavior of hard-sphere mixtures with different sizes. As we mentioned earlier, exclusively for active systems where $T_A \neq T_B$, do the mobilities (or the friction coefficients $\zeta_\alpha$) come into play via the effective pairwise temperature $T_{AB}$ when $\zeta_A \neq \zeta_B$. For a given size ratio $\alpha_v$, $\beta_B = (1 + \alpha_v^{1/3})^3$ and using Stoke's law $\alpha_\zeta = \alpha_v^{1/3}$. In Fig. 2(b) we plot the phase diagram for mixtures of hard spheres where the hot particles $A$ are larger with a volume ratio $\alpha_v = 27$ and a temperature ratio $\alpha_T = 20$. The evolution of the phase diagram upon increasing the size ratio can be appreciated by comparison to equal-size hard spheres at the same temperature ratio [Figs. 2(a) and 2(b)]. A more symmetrical phase diagram is predicted by increasing the volume ratio to reach $\alpha_v \approx \alpha_T$ and we

$^2$Note that $\alpha_T > 4$ is the updated demixing condition for isometric hard spheres consistent with the second-order virial expansion. In Ref. [11], the authors had obtained $\alpha_T > 34$ where they chose $\epsilon_A = \epsilon_B = 1$ for simplicity.

![](./images/812634499077636096_4.jpg)

FIG. 3. Control over mixing. (a) Phase diagram for the existence of a phase separation in the temperature ratio $\alpha_T = T_A/T_B$ and volume ratio $\alpha_v = v_A/v_B$ plane for pure hard spheres. The purple line follows the spinodal condition while the outer brown boundary more strictly requires the existence of a critical point (see Sec. III E). Inside these lines the solution remains mixed at all compositions. Interestingly, the phase diagram shows reentrance in both the lateral and vertical directions. The gray line $\alpha_T = \alpha_v$ separates the different regimes of phase compositions: (i) on lower half-plane, we expect solidlike $\mathcal{B}$-rich phase and gaslike $\mathcal{A}$-rich phase, and (ii) vice versa on upper half-plane, (iii) whereas near the gray line we expect both liquidlike phases. In (b) we use the same condition (in purple) for the existence of demixing for equal size hard spheres with short-range interactions of equal magnitude but opposing behavior (attractive vs repulsive) for intraspecies and interspecies. The inset shows the favored interactions in both regimes. If $a_0 > 0$, the molecular interactions only promote mixing while at sufficiently large temperature ratios, the system can still reach phase separation.

expect coexistence between two liquidlike phases [Fig. 2(b)].
A further increase of size ratio shifts the phase diagram toward
the $\mathcal{A}$-rich side as expected for mixtures of hard spheres
with different sizes at the same temperature. Another way to
observe the effect of tuning both size and temperature ratios is
to evaluate the conditions required for the existence of a phase
separation given in Sec. III E as a function of temperature and
size ratios. We show this phase diagram in Fig. 3(a) which
displays reentrances in both size-ratio and temperature-ratio
axes.

### B. Relation to active swimmers and active-passive particle mixtures

In dilute mixtures of active swimmers and passive parti-
cles, the run and tumble mechanism of the swimmers with
propulsion speed $V_{\mathcal{A}}$ and reorientation time $\tau_r$ dictated by
the time step between two tumbling events can be considered
at long times as entirely diffusive. If the reorientation time
of swimmers is much smaller than the mean collision time
(or mean-free time), i.e., $\tau_r \ll \tau_c$, then $(T_{\mathcal{A}} - T_{\mathcal{B}}) \approx P_{cs}\tau_r/3$
where $T_{\mathcal{B}}$ is the background temperature and $P_{cs}^{\mathcal{A}} = V_{\mathcal{A}}^2 \zeta_{\mathcal{A}}$
is the mean power required to drive chemotaxis [43] for an
active particle. Accordingly, keeping $\tau_r$ high will serve lower
dissipation rate to maintain the same translational diffusivity.
The validity range of this approximation in terms of the
Péclet number $\text{Pe} = 3V_{\mathcal{A}}\tau_r/d_{\mathcal{A}}$ where $d_{\mathcal{A}}$ is the diameter
can be obtained by estimating $\tau_c$ for active swimmers [44]
using collision theory. It suggests that the effective diffusive
approximation $(T_{\mathcal{A}} - T_{\mathcal{B}}) \approx P_{cs}\tau_r/3$ remains valid for $\text{Pe} \ll$
$\frac{3}{8\phi_{\mathcal{A}}}$ and density corrections are required as the concentra-
tion increases $(\tau_r \gg \tau_c)$. Moreover, when we consider the
emergence of the spinodal region as the demixing condition
(Sec. III E), we obtain at equal volume fractions $\phi_{\mathcal{A}} = \phi_{\mathcal{B}} =$
$\phi_s$, the phase boundary follows $\phi_s \sim \text{Pe}^{-1}$. This relation is
in accordance with simulations of mixtures of passive and
active Brownian particles in two dimensions [45], although
the simulations probe the phase separation at denser concen-
trations where both the diffusive approximation of the active
swimmers fails (high Pe) and the dilute limit approximation
of the phase separation theory is not qualitatively accurate.

One interesting aspect of our results is that we predict a
positive surface tension as discussed in the previous section.
In single-component active fluids, the contribution from the
swim pressure to the sign of surface tension is controversial.
Certain approaches report negative [46], near zero [47], or
positive [48] values, or even supporting both [49]. For the two-
temperature model, at this order, the traditional “effective”
equilibrium route coincides with the mechanical framework,
however, we discuss the breakdown of this construction on
Sec. VI while going one order higher in density. We can also
express the cluster growth rate in terms of the mean power
input. If the $\mathcal{A}$ and $\mathcal{B}$ constituents have the same volume $v_0$,
at later stages of clustering, Eq. (F5) suggests that the growth
rate of mean cluster size $r_G \sim (\phi_{\mathcal{A}}P_{cs}\tau_r)^{1/2}v_0^{1/3}T_{\mathcal{B}}^{1/2}/\zeta$ when
$P_{cs} \gg T_{\mathcal{B}}/\tau_r$. This can be generalized similarly when there are
two different types of swimmers, and so on.

### C. Interacting particles with different temperatures

Another interesting scenario appears when the interactions
between particles enhance mixing while the activity contrast
opposes and boosts demixing. To illustrate this scenario with
an example, consider a system of particles with equal strength
of interactions which are repulsive for identical particles and
attractive between different particles. This could be achieved,
for example, by mixing hot and cold particles of opposite net
electric charges in a medium with a finite screening length.
Similar other systems can be prepared by engineering chemi-
cal interactions. The interaction part of the virial coefficients

can in this case be written as $a_{\mathcal{A}\mathcal{A}} = a_{\mathcal{B}\mathcal{B}} = a_0$ and $a_{\mathcal{A}\mathcal{B}} = -a_0$. We may further simplify the problem by considering spherical particles of equal sizes such that $b_{\alpha\beta} = b_0 = 8v_0$ where $v_0$ is the molecular volume of the particles. We can evaluate the parameter range where a phase separation occurs. In Fig. 3(b), we show the phase diagram in terms of the scaled interaction parameter $a_0/(T_{\mathcal{A}}v_0)$, and the temperature ratio $\alpha_T = T_{\mathcal{A}}/T_{\mathcal{B}}$ for $T_{\mathcal{A}} > T_{\mathcal{B}}$. When $a_0 > 0$, the molecular interactions only promote mixing while at sufficiently large temperature ratios, the system can still reach phase separation.

### D. Active-passive polymer blends
Biopolymers play a key role in intracellular or intranuclear organization in many instances [50], while they often interact with active proteins which confer them an active character. In our context, such activity in biopolymers has been shown to enhance spatial segregation and maintain compaction. This is the case, for example, displayed in the structure and compaction of DNA inside the cell nucleus [51,52]. Similarly to colloidal particles, the active forces induce an effective temperature higher than the ambient one [53]. To give an example within our theory, we consider here a mixture of poly-$\mathcal{A}$ and poly-$\mathcal{B}$ chains in solution with equal lengths but with different temperatures (or activities) $T_{\mathcal{A}} > T_{\mathcal{B}}$ and having only excluded-volume interactions. For dilute solutions, one can still expect an effective thermodynamic behavior with an effective free energy given by a Flory-Huggins theory. In the spirit of the Flory-Huggins mean-field theory, we suppose here that the interaction part of the free energy does not depend on the connectivity between the monomers and that we can employ the results obtained for colloidal particles. Therefore, in order to describe the polymers, we use the chemical potentials obtained in the Sec. II A by making the transformation $\mu_{\alpha} \to \mu_{\alpha}^{id}/N_{\alpha} + \Phi_{\alpha}$, where $N_{\alpha}$ is the number of monomers in each chain. Here, we consider the size interactions to be identical such that $\epsilon_{\mathcal{A}} = \epsilon_{\mathcal{B}} = \beta_{\mathcal{B}} = \epsilon_0$. By using the phase-separation conditions described in Sec. III (both approaches agree in this case when $N_{\alpha} \gg 1$), we observe that segregation requires $(T_{\mathcal{A}} - T_{\mathcal{B}})/T_{\mathcal{B}} = \alpha_T - 1 > (2\epsilon_0^{-1/2})(N_{\mathcal{A}}^{-1/2} + N_{\mathcal{B}}^{-1/2})$. This result agrees with extensive simulations of active-passive polymer mixtures [15] where the same scaling law is observed for $N_{\mathcal{A}} = N_{\mathcal{B}} = N$ as the condition becomes $\alpha_T - 1 > (4\epsilon_0^{-1/2})N^{-1/2}$, though in terms of effective temperatures. Our mean-field exponents on the profile $\Delta\psi \sim \alpha_T^{1/2}$ and interface width $\ell \sim \alpha_T^{-1/2}$ seem close to the values obtained from simulations by the same authors in Ref. [16].

## VI. HIGHER-ORDER EXPANSIONS IN CONCENTRATION

### A. General form
Up to this point, we have studied the general phase behavior of a suspension of mixed particles with different temperatures in the dilute limit. In this limit, the theory takes into account only two-particle correlations, the system has an effective thermodynamic description and the phase behavior can be obtained from the direct analog of the equilibrium construction of phase separation, despite the existence of nonequilibrium aspects such as the violation of detailed balance that are observed at the microscopic level [11]. A natural extension of this approach is then to calculate higher-order corrections in concentration and see whether the effective thermodynamic description is preserved.
In order to answer this question, we must first obtain the steady-state pair distribution function $g_{\alpha\beta}^{ss}(\mathbf{r}_1 - \mathbf{r}_2)$ at next orders in particle densities $c_{\alpha}$. A general strategy would be to start from the Fokker-Planck equation (2) for the multiparticle probability distribution $P$, and integrate up to the desired order in densities. One can then solve the remaining coupled equations to obtain the pair distribution functions $g_{\alpha\beta}^{ss}(\mathbf{r}_1 - \mathbf{r}_2)$. This approach leads to the Bogoliubov-Born-Green-Kirkwood-Yvon (BBGKY) hierarchy [31]. For our problem, a nonequilibrium analog of this hierarchy is detailed in Ref. [11]. In the equilibrium case, the fluxes vanish and the distribution functions are found by imposing a closure relation. By contrast, in a nonequilibrium case, for $T_{\mathcal{A}} \neq T_{\mathcal{B}}$, there might exist nonvanishing fluxes associated to dissipation in the system. $^{3}$ This complication makes it difficult to obtain a systematic expansion at higher orders in densities.
A solvable example of Fokker-Planck equation (or the Langevin dynamics) at higher order has been given for pairwise harmonic potential interactions. In this case, a steady-state solution exists [54] for $\sum_m \partial_m J_m = 0$ while the fluxes $J_m \neq 0$ when $T_{\mathcal{A}} \neq T_{\mathcal{B}}$. As a result, it is not possible to formulate a solution in Boltzmann form with a scalar temperature.
Other classical approaches such as the Kirkwood superposition approximation would also fail. We refer the reader to the probabilistic interpretation of the Kirkwood closure in Ref. [55]. Nevertheless, in the following section, we demonstrate an alternative approach based on the calculation of depletion forces to obtain third-order density corrections for pure hard-sphere interactions.

### B. Hard spheres
In the case of mixtures with only hard-sphere interactions, an appropriate approach to expand at least to the next order considers the depletion interaction between two particles due to a third particle [56]. This method has been used repeatedly in colloid science [57] and recovers exactly the third virial coefficients in hard-sphere mixtures with different radii. The full details of the calculation are given in Appendix G. Here, as an example, we briefly sketch the results obtained for equal-sized hard spheres with different temperatures. The method is also applicable to particles of differing size ratios as shown in Appendix G. The resulting pressure is given by the standard virial expansion
$$
p^0 = \sum_{\alpha} T_{\alpha} c_{\alpha} + \frac{B}{2} \sum_{\alpha,\beta} T_{\alpha\beta} c_{\alpha} c_{\beta} + C \sum_{\alpha,\beta,\gamma} T_{\gamma} c_{\gamma} c_{\alpha} c_{\beta}, \quad (42)
$$
where $B$ and $C$ are the second and third virial coefficients, respectively, which are identical for all types of pairs and triplets of particles and $\alpha, \beta, \gamma = \mathcal{A}$ or $\mathcal{B}$.

$^{3}$These fluxes are already present at the level of two particle with different temperatures. As shown in Appendix A, the flux along the relative coordinate vanishes while a nonvanishing current exists along the center of friction coordinate.

![](./images/812634499077636096_5.jpg)

FIG. 4. Evolution of triangular phase diagrams by third-order contributions. The presentation on how to read the components in the phase diagrams is given in caption of Fig. 2. In (a) we only show the resulting phase diagram obtained using third-order expansion where we display binodal (purple) and spinodal (orange dashed) lines and the critical point (red) for equal-sized hard spheres with $T_A/T_B=20$. In (b) we compare the spinodal lines and the critical points (for clarity, not the binodals) obtained from second-order (orange) and third-order (light blue) expansions for equal-sized hard spheres with $T_A/T_B=40$.

In equilibrium systems, there is a direct route from pressure to chemical potentials using the Gibbs-Duhem equation $p_0 = \sum_\alpha \mu_\alpha^0 c_\alpha - f^0$, where the chemical potentials are given by $\mu_\alpha^0 = \partial f^0/\partial c_\alpha$. Our analysis for systems with two temperatures has shown that this remains applicable in the dilute limit approximation. However, without knowing explicitly the effective free energy, this approach is not founded. Thus, one should always start from the dynamic equations for the concentrations. If we insist in rewriting the interaction part of the chemical potentials defined in Eq. (8) as a series expansion in densities $\Phi_\alpha = \Phi_\alpha^{(1)} + \Phi_\alpha^{(2)}$, we only obtain the value of the chemical potential gradient at second order in the densities:

$$
\begin{aligned}
\nabla \Phi_{\mathcal{A}}^{(2)}= & C\left[\nabla\left(\frac{3}{2} T_{\mathcal{A}} c_{\mathcal{A}}^{2}+\frac{3}{2} T_{B} c_{B}^{2}\right)+\left(2 T_{B}+T_{\mathcal{A}}\right) c_{B} \nabla c_{\mathcal{A}}\right. \\
& \left.+\left(2 T_{\mathcal{A}}+T_{B}\right) c_{\mathcal{A}} \nabla c_{B}\right],
\end{aligned}
\tag{43}
$$

where $C$ is the third virial coefficient between hard spheres of the same size (see Appendix G), which is equal for all types of interactions. At this order, $\nabla \Phi_{\mathcal{B}}^{(2)}=\nabla \Phi_{\mathcal{A}}^{(2)}$ because the mixture contains particles of equal sizes. The total chemical potentials $\mu_\alpha^{(2)} = \mu_\alpha + \Phi_\alpha^{(2)}$ are then obtained from Eqs. (9) and (43). However, the gradient $\nabla \Phi_\alpha^{(2)}$ given by Eq. (43) is nonintegrable to a potential function due to the mismatch between the cross terms. This incompatibility is related to the nonequilibrium character of solutions of particles at different temperatures and hence the mismatch vanishes for an equilibrium solution, when $T_{\mathcal{A}}=T_{B}$. As a result, the nonequilibrium additional terms break down the routes to construct an effective thermodynamic theory. A similar breakdown has been previously observed in one-component active fluids with density-dependent motilities [40] where the interfacial contributions lead to terms not integrable to a free energy. That issue has then been addressed in Ref. [49], by introducing a functional transformation using an alternative scalar order parameter. By contrast, here we are not able to define even the local chemical potentials at third order in the dynamical equations (6) and (7). This could as well indicate the existence of bubbly phases [58] in which two steady-state phases exist only locally and are separated by interfaces. A more detailed study would require to extend the analysis in gradient terms presented in the previous sections. We plan to address this question in a further study.

Since the term $\nabla \Phi_{\mathcal{A}}^{(2)}$ is not integrable to a chemical potential form, it is not straightforward to determine all uniformly conserved quantities at the zero-flux steady state. At phase equilibrium, we only find two conserved quantities since $\nabla p^{0}=0$ and $\nabla(\mu_{\mathcal{A}}^{0}-\mu_{B}^{0})=0$. The latter condition exists specifically for equal-sized hard spheres because $\nabla \Phi_{\mathcal{B}}^{(2)}=\nabla \Phi_{\mathcal{A}}^{(2)}$. A third condition, however, can be obtained by linearization of one of the concentration fluxes around the critical point. Then, the calculated phase diagrams are shown in Fig. 4 in comparison to the phase diagram obtained from the previous expansion using second-order virial coefficients (dilute limit) for the same set of parameters $\alpha_v=1, \alpha_T=40$. Curiously, the contribution from the third-order terms delays the onset of demixing. We also observe that the instability occurs in physical region of the phase diagram for temperature ratios $\alpha_T>6.171$, not very far from the value obtained using second-order analysis, i.e., $\alpha_T>4$ (see Footnote 2).

### VII. CONCLUSION

To summarize, in this work, we have outlined the general framework to study the characteristics of phase equilibria in active mixtures of diffusive type where the temperatures of the constituents are different. We obtain the phase diagrams and phase growth properties using two methods in parallel which cover both the equilibrium thermodynamic description through functional analysis and a more general approach considering steady-state solutions of the Fokker-Planck equations. For each observable and method, we compare and contrast the nonequilibrium $T_{\mathcal{A}} \neq T_{B}$ scenarios to the equilibrium ones $T_{\mathcal{A}}=T_{B}$. This allows us to reexplore landmark methods and concepts developed to establish the foundational principles of equilibrium solution theory. Resemblances appear in the steady-state solutions while the nonequilibrium state when $T_{\mathcal{A}} \neq T_{B}$ is only maintained with a net power dissipation. Even though these systems have a nonequilibrium character, it turns out that they recover a direct analog of the equilibrium construction in the dilute limit. Within this approximation, the direct connection with the equilibrium thermodynamics

is linked to the closure of the hierarchy of correlation func- tions, which imposes a vanishing flux along the coordinate of interactions (the separation vector) for all two-body clusters (while this is no longer true for higher-order clusters). In this dilute limit, we were able to construct a Cahn-Hilliard theory generalized to two temperature mixtures. This also validates a reasonable ground for phenomenological studies considering active systems as a perturbation around an equivalent equilib- rium dynamics.

The analog of the equilibrium picture provides a rich palette to explore various aspects of active and passive (or less active) particle mixtures. In this case, the activity differences between the particles introduce another level of control on the phase-separation properties. As we demonstrate by examples, the theory has broad applications in diverse physical systems at different length scales. We have also introduced a transfor- mation to normal coordinates around the critical state where the phase dynamics can be described by a single critical order parameter. We obtain counterparts of mean-field exponents of profile parameter $\psi$ to express interfacial properties, while $\eta$ becomes a measure of normal distance from the critical point [similar to the temperature direction in regular solutions [27,28], but not exactly the same since $\eta \equiv \eta(z)$ is a slightly varying function of $z$ along the interface]. In this simplified formalism, we capture interesting scaling laws for interfa- cial properties, droplet growth dynamics, and for the phase segregation condition. We observe that the surface tension is always positive at the interface of two phases for binary mixtures of equal-sized hard spheres. Some of our results are in agreement with existing numerical simulations (detailed in Sec. V). Our results also suggest a means to calibrate the composition of coexisting phases (liquid-liquid vs gaslike and solidlike) by controlling the ratio $\alpha_{T} / \alpha_{v}$ which could motivate experimental applications.

Higher-order corrections (though not available for the gen- eral case) break down the direct analogy with the equilibrium construction in the case of pure hard-core interactions. How- ever, the results do not indicate significant qualitative differ- ences with the equilibrium behavior, and hence in general, the qualitative behavior of the system should be obtained fromthe simpler theory describing the dilute limit (Secs. II-IV) that gives an intuitive understanding of demixing in diffusive systems. On the other hand, the existence of nonlocal terms in the chemical potentials at the third order in a power expansion in densities might indicate the emergence of new phenomena. It would be interesting to study these cases further, including inhomogeneous terms, in order to bridge the gap between microscopic and coarse-grained models [49,58].

## ACKNOWLEDGMENTS

We thank A. Y. Grosberg, A. S. Vishen, and A. P. Solon for interesting discussions and insightful comments. E.I. ac- knowledges the financial support from the LabEx CelTisPhy- Bio.

## APPENDIX A: SOLUTION OF THE TWO-PARTICLE FOKKER-PLANCK EQUATION

By evaluating Eq. (2) for only two particles $\alpha$ and $\beta$ at positions $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$, and introducing a pairwise potential which depends only on the distance between these particles $u_{\alpha \beta} \equiv$ $u_{\alpha \beta}(|\mathbf{r}_{1}-\mathbf{r}_{2}|)$ such that $\partial_{\mathbf{r}_{1}} u_{\alpha \beta}=-\partial_{\mathbf{r}_{2}} u_{\alpha \beta}$, we can derive the steady-state solution using separation of variables where $\alpha, \beta=\mathcal{A}$ or $\mathcal{B}$. Accordingly, we set the two-particle proba- bility function $P_{\alpha \beta} \equiv G_{\alpha \beta}(\mathbf{R}) g_{\alpha \beta}(\mathbf{r})$ where $\mathbf{r}=\mathbf{r}_{2}-\mathbf{r}_{1}$ is the separation vector and $\mathbf{R}=\tau_{\alpha} \mathbf{r}_{1}+\tau_{\beta} \mathbf{r}_{2}$ is the center of motion with $\tau_{\alpha}=\zeta_{\alpha} T_{\beta} /(\zeta_{\alpha} T_{\beta}+\zeta_{\beta} T_{\alpha})$ such that the diffusions along $\mathbf{r}$ and $\mathbf{R}$ are statistically independent [11]. As a result, we obtain

$$
\frac{\partial P_{\alpha \beta}}{\partial t}=-\partial_{\boldsymbol{r}} J_{r}^{\alpha \beta}-\partial_{\boldsymbol{R}} J_{R}^{\alpha \beta} \quad \text { (A1) }
$$

with flux components

$$
\begin{array}{r}
J_{r}^{\alpha \beta}=-\left(\frac{\zeta_{\alpha}+\zeta_{\beta}}{\zeta_{\alpha} \zeta_{\beta}}\right) \frac{\partial u_{\alpha \beta}}{\partial \mathbf{r}} P_{\alpha \beta}-\left(\frac{\zeta_{\alpha} T_{\beta}+\zeta_{\beta} T_{\alpha}}{\zeta_{\alpha} \zeta_{\beta}}\right) \frac{\partial P_{\alpha \beta}}{\partial \mathbf{r}}, \\
(\mathrm{A} 2)
\end{array}
$$

$$
\begin{array}{r}
J_{R}^{\alpha \beta}=-\left(\frac{T_{\alpha}-T_{\beta}}{\zeta_{\alpha} T_{\beta}+\zeta_{\beta} T_{\alpha}}\right) \frac{\partial u_{\alpha \beta}}{\partial \mathbf{r}} P_{\alpha \beta}-\left(\frac{T_{\alpha} T_{\beta}}{\zeta_{\alpha} T_{\beta}+\zeta_{\beta} T_{\alpha}}\right) \frac{\partial P_{\alpha \beta}}{\partial \mathbf{R}} . \\
(\mathrm{A} 3)
\end{array}
$$

Setting the flux $J_{r}=0$ for the steady-state solution results [Eq. (4)] in the main text. The remaining part only requires a uniform $G(\mathbf{R})$ which satisfies the steady-state solution though $J_{R}^{\alpha \beta}$ does not necessarily vanish for $T_{\alpha} \neq T_{\beta}$.

## APPENDIX B: IRVING-KIRKWOOD METHOD FOR CALCULATION OF INTERNAL STRESS

Following the stress equation for the interaction part, Eq. (18) in the main text up to second order in separation vector $\mathbf{r}$ while using Eq. (4) and keeping only nonvanishingterms upon integration, we rewrite the internal stress $\sigma_{i j}^{(v)}$ given by Eq. (17) as

$$
\begin{aligned}
\sigma_{i j}^{(v)}= & -p_{0} \delta_{i j}+\sum_{\alpha, \beta} \frac{T_{\alpha \beta}}{2} \int\left[\frac{r_{i} r_{j}}{\mathbf{r}} \frac{\partial}{\partial r}\left(1-e^{-u_{\alpha \beta}(r) / T_{\alpha \beta}}\right)\right. \\
& \times\left(\frac{1}{6}(\mathbf{r} \cdot \nabla)^{2} c_{\alpha}\left(\mathbf{r}_{1}\right) c_{\beta}\left(\mathbf{r}_{1}\right)\right. \\
& \left.\left.-\frac{1}{2}\left[\mathbf{r} \cdot \nabla c_{\alpha}\left(\mathbf{r}_{1}\right)\right]\left[\mathbf{r} \cdot \nabla c_{\beta}\left(\mathbf{r}_{1}\right)\right]\right)\right] d \mathbf{r},
\end{aligned}
$$

where $p^{0}=\left(\mu_{\mathcal{A}}^{0} c_{\mathcal{A}}+\mu_{\mathcal{B}}^{0} c_{\mathcal{B}}-f^{0}\right)$ is the locally uniform pressure. Integrating by parts gives

$$
\begin{aligned}
\sigma_{i j}^{(v)}= & -p_{0} \delta_{i j}+\sum_{\alpha, \beta} \frac{T_{\alpha \beta}}{2} \mathcal{I}_{i j k l}\left[\frac{1}{12}\left(\partial_{k} c_{\alpha} \partial_{l} c_{\beta}+\partial_{k} c_{\beta} \partial_{l} c_{\alpha}\right)\right. \\
& \left.-\frac{1}{6}\left(c_{\alpha} \partial_{k} \partial_{l} c_{\beta}+c_{\beta} \partial_{k} \partial_{l} c_{\alpha}\right)\right],
\end{aligned}
$$

where a summation on the $k, l$ indices is performed using an Einstein summation convention, and the integral $\mathcal{I}_{i j k l}$ is given by

$$
\mathcal{I}_{i j k l}=\int \frac{r_{i} r_{j} r_{k} r_{l}}{r^{2}}\left(1-e^{-u_{\alpha \beta}(r) / T_{\alpha \beta}}\right) d \mathbf{r}. \quad \text { (B3) }
$$

Considering the symmetries and performing the sum, we finally reach an expression for the difference between stress

obtained by two different methods:

$$
\sigma_{i j}^{(v)}-\sigma_{i j}=\sum_{\alpha, \beta} L_{\alpha \beta}\left[-\frac{1}{3} \nabla^{2}\left(c_{\alpha} c_{\beta}\right) \delta_{i j}+\frac{1}{3} \partial_{i} \partial_{j}\left(c_{\alpha} c_{\beta}\right)\right],
\tag{B4}
$$

where $\sigma_{i j}$ is the result obtained by free-energy deformation given in Eq. (15). Summing over $\alpha, \beta$ suggests that the addition of the gauge term discussed in Sec. II B, i.e., $-\frac{1}{3} \nabla^{2}\left[L_{A} c_{A}^{2}+2 L_{A B} c_{A} c_{B}+L_{B} c_{B}^{2}\right]$ to the original free energy $f$, leads back to the Irving-Kirkwood formula.

## APPENDIX C: TRANSFORMATION OF ORDER PARAMETERS TO NORMAL COORDINATES AROUND THE CRITICAL POINT

Close to the critical point $\{\phi_{A}^{*}, \phi_{B}^{*}\}$, the effective thermodynamic description becomes simpler if instead of using the volume fractions measured with respect to the volume fractions at the critical point $\delta \phi_{\alpha}=\phi_{\alpha}-\phi_{\alpha}^{*}$ as variables, we make a linear transformation to the eigenvectors of the inverse compressibility matrix $\kappa_{p}^{-1}$ at the critical point. The inverse compressibility matrix is a symmetric matrix given by Eq. (24) and it can be written as

$$
\kappa_{p}^{-1}=\left(\begin{array}{cc}
c+a & b \\
b & c-a
\end{array}\right). \tag{C1}
$$

The values of the coefficients are given by Eq. (24) $c=\frac{1}{2}\left[\alpha_{T}\left(\frac{1+\epsilon_{A} \phi_{A}}{\phi_{A}}\right)+\alpha_{v}\left(\frac{1+\epsilon_{B} \phi_{B}}{\phi_{B}}\right)\right], \quad a=\frac{1}{2}\left[\alpha_{T}\left(\frac{1+\epsilon_{A} \phi_{A}}{\phi_{A}}\right)-\alpha_{v}\left(\frac{1+\epsilon_{B} \phi_{B}}{\phi_{B}}\right)\right], \quad \text { and } \quad b=\frac{\alpha_{T}+\alpha_{\zeta}}{1+\alpha_{\zeta}} \beta_{B}.
$$
We denote the two eigenvalues of the matrix by $\epsilon$ and $\lambda$. The coefficients of the matrix are real and related to the eigenvalues by $c=\frac{\lambda+\epsilon}{2}$ and $(a^{2}+b^{2})^{1 / 2}=\frac{\lambda-\epsilon}{2}$. In the vicinity of the critical point, $\epsilon$ is small and vanishes as one approaches the critical point and the other eigenvalue $\lambda$ remains finite at the critical point. The eigenvector associated with $\epsilon=0$ at the critical point gives the direction in which the fluctuations diverge. We also define an angle $\theta$ such that $a=-\frac{\lambda-\epsilon}{2} \cos 2 \theta$ and $b=\frac{\lambda-\epsilon}{2} \sin 2 \theta$. The diagonalization appears then as a rotation of angle $\theta$ and the eigenvalue matrix $D_{\epsilon, \lambda}$ with diagonal entries $\epsilon$ and $\lambda$ is obtained by rotation to the basis of eigenvectors $D_{\epsilon, \lambda}=R(\theta) \kappa_{p}^{-1} R^{T}(\theta)$ using the standard rotation matrix $R(\theta)$.

In the volume fraction space, the eigenvectors are obtained using a rotation of the natural coordinates by an angle $\theta$. The normal coordinates that we use are the coordinates along the eigenvectors of the inverse compressibility matrix at the critical point. At the critical point, the rotation angle of the eigenvectors is $\theta^{*}$ that satisfies

$$
\tan \theta^{*}=\frac{b^{*}}{c^{*}-a^{*}}=\frac{\left(\alpha_{T}+\alpha_{\zeta}\right) \beta_{B} \phi_{B}^{*}}{\alpha_{v}\left(1+\alpha_{\zeta}\right)\left(1+\epsilon_{B} \phi_{B}^{*}\right)} \tag{C2}
$$

which can also be expressed in conjugate form in terms of $\phi_{A}^{*}$ using $\tan \theta^{*}=\frac{c^{*}+a^{*}}{b^{*}}$. This angle gives the orientation of the tie lines close to the critical point. As a result, it provides an indication on the asymmetry of composition between the two phases. Thus, when $\tan \theta^{*} \approx 1$, we would have two liquidlike phases, whereas for $\tan \theta^{*} \gg 1$, the critical point is toward $\mathcal{B}$-rich side of the phase diagram with a solidlike and a gaslike phase coexisting and vice versa for $\tan \theta^{*} \ll 1$.

In the eigenbasis of the inverse compressibility matrix at the critical point, there is a coordinate $\psi$ along the eigenvector associated to the vanishing eigenvalue and a coordinate $\eta$ along the eigenvector associated to the finite eigenvalue $\lambda$. These two normal coordinates are related to the original volume fractions by the rotation matrix $R(\theta^{*})$. Accordingly, we define

$$
\left(\begin{array}{l}
\psi \\
\eta
\end{array}\right)=R\left(\theta^{*}\right)\left(\begin{array}{l}
\delta \phi_{A} \\
\delta \phi_{B}
\end{array}\right). \tag{C3}
$$

The coordinate $\psi$ is the critical variable that we call the order parameter. Along these new coordinates, differentiation is performed as

$$
\left(\begin{array}{c}
\frac{\partial}{\partial \psi} \\
\frac{\partial}{\partial \eta}
\end{array}\right)=R\left(\theta^{*}\right)\left(\begin{array}{c}
\frac{\partial}{\partial \phi_{A}} \\
\frac{\partial}{\partial \phi_{B}}
\end{array}\right). \tag{C4}
$$

Using these relations, we expand the free energy around the critical point and obtain

$$
\hat{f}_{0}=\hat{f}_{0}^{*}+\hat{\mu}_{\eta}^{*} \eta+\hat{\mu}_{\psi}^{*} \psi+\frac{k_{2}}{2} \psi^{2} \eta+\frac{k_{4}}{4} \psi^{4}+\frac{\lambda^{*}}{2} \eta^{2}, \quad(\mathrm{C} 5)
$$

where the coefficients of the expansion are the derivatives of the free energy $\hat{f}_{0}$ evaluated at the critical point: $k_{2}=\left.\frac{\partial^{3} \hat{f}_{0}}{\partial \psi^{2} \partial \eta}\right|_{*}, k_{4}=\left.\frac{1}{3!} \frac{\partial^{4} \hat{f}_{0}}{\partial \psi^{4}}\right|_{*}, \lambda^{*}=\left.\frac{\partial^{2} \hat{f}_{0}}{\partial \eta^{2}}\right|_{*}$ and we used the fact that $\eta$ is a slowly changing variable. The Hessian matrix of the second derivatives of the free energy is equal to the inverse compressibility matrix. In the coordinates $\psi, \eta$ the inverse compressibility matrix is $D_{\epsilon, \lambda}$ evaluated at the critical point where $\epsilon=0$. The two derivatives $\left.\frac{\partial^{2} \hat{f}_{0}}{\partial \psi \partial \eta}\right|_{*}$ and $\left.\frac{\partial^{2} \hat{f}_{0}}{\partial \psi^{2}}\right|_{*}$ therefore vanish. The third derivative of the free energy $\left.\frac{\partial^{3} \hat{f}_{0}}{\partial \psi^{3}}\right|_{*}$ also vanishes because $\psi$ is the tangent direction to the spinodal line at the critical point. The two chemical potentials along the new coordinates are obtained again by differentiation of the free energy $\hat{f}_{0}$:

$$
\hat{\mu}_{\eta}=\hat{\mu}_{\eta}^{*}+\lambda^{*} \eta+k_{2} \frac{\psi^{2}}{2}, \tag{C6}
$$

$$
\hat{\mu}_{\psi}=\hat{\mu}_{\psi}^{*}+k_{2} \eta \psi+k_{4} \psi^{3}. \tag{C7}
$$

The coordinates of the equilibrium phases $a$ and $b$ (the binodal line) are obtained by equating the chemical potentials $\hat{\mu}_{\psi}$ and $\hat{\mu}_{\eta}$ and the pressure in the two phases. This leads to $\eta_{a}=\eta_{b}$ and $\psi_{a}^{2}=\psi_{b}^{2}=-\frac{k_{2}}{k_{4}} \eta_{a}$. By construction of the normal coordinates, the tie lines, which are the straight lines joining the two phases at equilibrium correspond to lines of constant values of $\eta$. The binodal line has therefore a parabolic shape with $\psi_{a} \approx-\psi_{b}$. Each value of $\eta_{a} \approx \eta_{b}>0$ defines the coexisting phases $\psi_{a}$ and $\psi_{b}$. It is convenient in the following to consider a symmetrized version of the order parameter $\Delta \psi_{a b}=\psi_{b}-\psi_{a}$, which satisfies $\Delta \psi_{a b}^{2}=-\frac{4 k_{2}}{k_{4}} \eta_{a}$.

The total free-energy density is obtained by including the gradient terms which also can be transformed to the normal coordinates. In the vicinity of the critical point, as the noncritical variable $\eta$ is much smaller than the order parameter $\psi$ we only need to retain terms in $(\nabla \psi)^{2}$. The total free-energy

$$
\hat{f}=\hat{f}_{0}+\frac{\hat{L}_{\psi}}{2}(\nabla \psi)^{2},
\tag{C8}
$$

where the coefficient $\hat{L}_{\psi}$ is given by $\hat{L}_{\psi}=\hat{L}_{A} \cos ^{2} \theta^{*}-2 \hat{L}_{A B} \cos \theta^{*} \sin \theta^{*}+\hat{L}_{B} \sin ^{2} \theta^{*}$.

In order to calculate the interfacial tension, we must define the two phases at equilibrium, i.e., fix the values $\eta_{a}$ in the two phases in equilibrium. This also fixes the order parameter $\Delta \psi_{a b}$. We must then calculate what we called the tilted free energy around the critical point

$$
\begin{aligned}
\Delta \hat{f}[\psi, \eta]=& \hat{f}[\psi, \eta]-\hat{f}^{0}\left(\psi_{a}, \eta_{a}\right)-\hat{\mu}_{\psi}^{\dagger}\left(\psi-\psi_{a}\right) \\
&-\hat{\mu}_{\eta}^{\dagger}\left(\eta-\eta_{a}\right).
\tag{C9}
\end{aligned}
$$

The constants $\hat{\mu}_{\psi}^{\dagger}$ and $\hat{\mu}_{\eta}^{\dagger}$ are the chemical potentials calculated in the two phases at equilibrium. Note that the tilted free energy has a minimum and vanishes in the two phases in equilibrium. The profiles of $\psi$ and $\eta$ as a function of the coordinate $z$ perpendicular to the interface are obtained by minimization of the tilted free energy. We first minimize the tilted free energy with respect to $\eta$. This leads to

$$
\eta=\eta_{a}-\frac{k_{2}}{2 \lambda^{*}}\left(\psi^{2}-\psi_{a}^{2}\right).
\tag{C10}
$$

Inserting this result into the tilted free energy, we obtain the tilted free energy as a function of the order parameter $\psi$ only, which we write as

$$
\Delta \hat{f}(\psi)=\frac{k_{\psi}}{4}\left(\psi-\psi_{a}\right)^{2}\left(\psi-\psi_{b}\right)^{2}+\frac{\hat{L}_{\psi}}{2}(\nabla \psi)^{2}, \quad(\mathrm{C} 11)
$$

where $k_{\psi}=k_{4}-\frac{k_{2}^{2}}{2 \lambda^{*}}$. This free energy is minimal and vanishes at $\psi=\psi_{a}$ and $\psi_{b}$. Finally, minimization with respect to $\psi$ yields

$$
\Delta \hat{f}^{0}(\psi)=\frac{k_{\psi}}{4}\left(\psi-\psi_{a}\right)^{2}\left(\psi-\psi_{b}\right)^{2}=\frac{\hat{L}_{\psi}}{2}(\nabla \psi)^{2} \quad(\mathrm{C} 12)
$$

which shows that along the order-parameter profile between the two phases $\Delta \hat{f}(\psi)=2 \Delta \hat{f}^{0}(\psi)$.

## APPENDIX D: POSITIVITY OF THE SURFACE TENSION

As mentioned in the main text, since $\hat{\gamma}=L_{\psi} \int(\nabla \psi)^{2}$ integrated from one phase to the other, the sign of $L_{\psi}$ determines the sign of the surface tension. We can determine the sign of $L_{\psi}$ using our results in Sec. II. From the definition $\hat{L}_{\psi}=\hat{L}_{A} \cos ^{2} \theta^{*}-2 \hat{L}_{A B} \cos \theta^{*} \sin \theta^{*}+\hat{L}_{B} \sin ^{2} \theta^{*}$, the positivity of surface tension requires

$$
2 \tan \theta^{*}-\frac{\hat{L}_{A}}{\hat{L}_{A B}}-\frac{\hat{L}_{B}}{\hat{L}_{A B}} \tan ^{2} \theta^{*}>0.
\tag{D1}
$$

We have previously defined rescaled parameters $\hat{L}_{\alpha \beta}=T_{B}^{-1} L_{\alpha \beta} v_{A} /\left(v_{\alpha} v_{\beta}\right)$ on Sec. III A (then $\hat{L}_{A} / \hat{L}_{A B}=$ $\left.\left(L_{A} / L_{A B}\right) \alpha_{v}^{-1} \quad \text { and } \quad \hat{L}_{B} / \hat{L}_{A B}=\left(L_{B} / L_{A B}\right) \alpha_{v}\right) \quad$ whereas $L_{\alpha \beta}=-T_{\alpha \beta} \Lambda_{\alpha \beta}$ and the coefficients $\Lambda_{\alpha \beta}=\frac{1}{6} \int r^{2}(1-$ $e^{-u^{\alpha \beta}(\mathbf{r}) / T_{\alpha \beta}} d \mathbf{r}=\tilde{\sigma}_{D} B_{\alpha \beta}^{5 / 3}$ with $\tilde{\sigma}_{D}=\frac{1}{10}(3 / 4 \pi)^{2 / 3}$ for hardspheres. Bringing these together and using $\epsilon_{A}=\epsilon_{B}=8$ suggests the positivity condition for the surface tension to be

$$
2 \alpha_{v} \tan \theta^{*}-\frac{1+\alpha_{\zeta}}{\alpha_{T}+\alpha_{\zeta}}\left(\frac{8}{\beta_{B}}\right)^{5 / 3}\left(\alpha_{T} \alpha_{v}^{5 / 3}+\alpha_{v}^{2} \tan ^{2} \theta^{*}\right)>0.
\tag{D2}
$$

We can then use the definition of $\tan \theta^{*}$ from Eq. (C2), and $\alpha_{\zeta}=\alpha_{v}^{1 / 3}, \beta_{B}=\left(1+\alpha_{v}^{1 / 3}\right)^{3}$. For the specific cases $\alpha_{v}=1$ and $\alpha_{v}=\alpha_{T}$, it is easy to prove the positivity of $L_{\psi}$. For varying size ratios, a numerical evaluation shows that $L_{\psi}$ is positive in the region where demixing occurs except when $\alpha_{v} \ll 1$ or $\alpha_{v} \gg \alpha_{T}$. In these two extreme limits, the surface tension can result a negative value, although it is not clear whether this is a true behavior since for extreme size ratios, the flat interface assumption would also fail.

## APPENDIX E: SCALING RELATIONS FOR EQUAL-SIZED HARD SPHERES WHEN $\alpha_{T} \gg 1$

As shown in the main text for equal-sized hard spheres where $\alpha_{v}=1$ (and hence $\alpha_{\zeta}=1$ ), and $\epsilon_{A}=\epsilon_{B}=\beta_{B}=8$, the volume fractions at the critical point are $\phi_{A}^{*}=\alpha_{T}^{-1}$, $\phi_{B}^{*}=1 / 8+(5 / 4) \alpha_{T}^{-1}$ when $\alpha_{T} \gg 1$. Using these relations, the rotation angle at the critical point given by Eq. (C2) reads as

$$
\tan \theta^{*} \approx \frac{\alpha_{T}}{4}.
\tag{E1}
$$

We consider a mixture with average particle volume fractions $\phi_{A}^{0}$ and $\phi_{B}^{0}$ defined by $\phi_{\alpha}^{0}=V^{-1} \int_{V} \phi_{\alpha}(\mathbf{r}) d \mathbf{r}$. We determine the normal distance $\eta\left(\phi_{A}^{0}, \phi_{B}^{0}\right)$ from the critical point. Then, as discussed in Appendix C, this fixes the order parameter $\Delta \psi_{a b}^{2}=-\frac{4 k_{2}}{k_{4}} \eta\left(\phi_{A}^{0}, \phi_{B}^{0}\right)$, and hence the compositions of the coexisting phases. In the limit where $\alpha_{T} \gg 1$, the order parameter is $\Delta \psi_{a b}^{2} \approx \alpha_{T}\left(\phi_{A}^{0}-\phi_{A}^{*}\right) / 4+\left(\phi_{B}^{0}-\phi_{B}^{*}\right)$ which becomes

$$
\Delta \psi_{a b}^{2} \approx \frac{\phi_{A}^{0}}{4} \alpha_{T}
\tag{E2}
$$

at (reasonably) finite volume fractions in the vicinity of the critical point.

In order to discuss the scaling of the surface tension, we also need the expressions of the coefficients $k_{\psi}$ and $\hat{L}_{\alpha \beta}$ as functions of $\alpha_{T}$. For equal-size hard spheres, we have

$$
\begin{gathered}
\hat{L}_{A}=-\sigma_{D} \alpha_{T} v_{0}^{2 / 3}, \quad \hat{L}_{B}=-\sigma_{D} v_{0}^{2 / 3}, \\
\hat{L}_{A B}=-\sigma_{D} \frac{\left(1+\alpha_{T}\right)}{2} v_{0}^{2 / 3},
\end{gathered}
\tag{E3}
$$

where $\sigma_{D}=\frac{4}{5}(6 / \pi)^{2 / 3}$ and $v_{0}$ is the molecular volume. We can then use these results to obtain $\hat{L}_{\psi}=\hat{L}_{A} \cos ^{2} \theta^{*}-$ $2 \hat{L}_{A B} \cos \theta^{*} \sin \theta^{*}+\hat{L}_{B} \sin ^{2} \theta^{*}$. The other coefficient $k_{\psi}=$ $k_{4}-\frac{k_{2}^{2}}{2 \lambda^{*}}$ can be calculated by taking into account the definitions below Eq. (C5) and differentiating Eq. (C4). For $\alpha_{T} \gg 1, k_{4} \approx 256 \sin ^{4} \theta^{*}, k_{2} \approx-16 \alpha_{T} \sin ^{3} \theta^{*}$, and $\lambda^{*} \approx$ $\alpha_{T}^{2} \sin ^{2} \theta^{*}$. Accordingly, $k_{\psi} \approx 128$ in this limit which is independent of the temperature ratio similarly to $\hat{L}_{\psi}$. These relations using (33) lead to Eq. (34) in the main text.

### APPENDIX F: CALCULATION OF $D_\psi$ AND THE DROPLET GROWTH RATE

In order to determine the diffusion coefficient of the relevant order parameter $\psi$ given in Sec. IV B, we need first to linearize time-evolution equations (7) around one of the phases (say phase $a$). This suggests
$$
\frac{\partial}{\partial t}\left(\begin{array}{l}
\delta \phi_{A} \\
\delta \phi_{B}
\end{array}\right)=\Gamma^{a} \nabla^{2}\left(\begin{array}{l}
\delta \phi_{A} \\
\delta \phi_{B}
\end{array}\right),\qquad(\mathrm{F}1)
$$
in which we define $\delta \phi_{\alpha}=\phi_{\alpha}-\phi_{\alpha}^{*}$ and obtain $\Gamma^{a}$ by evaluating (23) at phase $a$. Then, following Appendix B, we obtain
$$
\frac{\partial}{\partial t}\left(\begin{array}{l}
\psi \\
\eta
\end{array}\right)=\Gamma^{\prime a} \nabla^{2}\left(\begin{array}{l}
\psi \\
\eta
\end{array}\right),\qquad(\mathrm{F}2)
$$
where $\Gamma^{\prime a}=R(\theta^{*}) \Gamma^{a} R^{T}(\theta^{*})$. Using $\partial \eta / \partial t \approx 0$, we have $D_{\psi}=\left|\Gamma^{\prime a}\right| / \Gamma_{22}^{\prime a}$ with $\left|\Gamma^{\prime a}\right|=\left|\Gamma^{a}\right|$ being the determinant of matrix $\Gamma^{a}$ and $\Gamma_{22}^{\prime a}$ is the second diagonal component. Around the critical point, using Eqs. (C4), (C7), and (C10), the diffusion coefficient is
$$
D_{\psi} \approx \frac{T_{B} \phi_{A}^{*} \phi_{B}^{*}}{\zeta_{B} \alpha_{v}\left(\phi_{A}^{*} \sin ^{2} \theta^{*}+\phi_{B}^{*} \cos ^{2} \theta^{*} \alpha_{v}^{-1} \alpha_{\zeta}\right)} 2 k_{\psi} \psi_{a}^{2}, \quad(\mathrm{~F} 3)
$$
where $\phi_{A}^{a}$ and $\phi_{A}^{a}$ are the values of volume fractions at phase $a$. At high-temperature ratios $\alpha_{T} \gg 1$, we see that $\sin \theta^{*} \approx 1$ and, hence,
$$
D_{\psi} \approx \frac{T_{B}}{4 \zeta} k_{\psi} \psi_{a}^{2},\qquad(\mathrm{F}4)
$$
where we consider equal-size hard spheres $\alpha_{v}=\alpha_{\zeta}=1$ and $\zeta_{A}=\zeta_{B}=\zeta$.

Next, we estimate the growth rate of average droplet size $r_{G}$ such that $R \sim(r_{G} t)^{1 / 3}$. Near saturation $\Delta \sim d_{0} / R$ and hence $r_{G} \sim D_{\psi} d_{0}$. Using the above relation and the value of $d_{0}$ from the main text, we obtain $r_{G} \sim T_{B} \Delta \psi_{a b} v_{0}^{1 / 3} / \zeta$. Finally, since $\Delta \psi_{a b} \sim\left(\phi_{A}^{0} \alpha_{T}\right)^{1 / 2} / 2$ from (E2), we have
$$
r_{G} \sim\left(\phi_{A}^{0} \alpha_{T}\right)^{1 / 2} v_{0}^{1 / 3} T_{B} / \zeta.\qquad(\mathrm{F}5)
$$

### APPENDIX G: THIRD-ORDER EXPANSION FOR PURE HARD SPHERES

#### 1. Virial expansion to third order

The strategy that we follow in this Appendix is to define a potential of mean force at a finite concentration $u_{\alpha \beta}^{\text {tot }}(r)$ for an $\alpha \beta$ pair and to insert it into the Fokker-Planck equation (A1), (A2) by replacing $u_{\alpha \beta} \to u_{\alpha \beta}^{\text {tot }}$. This results in the steady-state value of the pair distribution function written in the Boltzmann form $g_{\alpha \beta}^{\mathrm{ss}}(r)=\exp \left(-u_{\alpha \beta}^{\mathrm{tot}}(r) / T_{\alpha \beta}\right)$ where $g_{\alpha \beta}$ is the pair distribution function, $u_{\alpha \beta}^{\text {tot }}(r)$ is the potential of mean force, and $T_{\alpha \beta}$ is the pairwise temperature between the two particles under consideration. In general, we can separate the potential of mean force into two parts, $u_{\alpha \beta}^{\text {tot }}(r)=u_{\alpha \beta}(r)+$ $W_{\alpha \beta}(r)$ where $u_{\alpha \beta}(r)$ is the bare pair interaction potential for two particles while $W_{\alpha \beta}(r)$ [59] is due to the existence of other surrounding particles. The potential of mean force can be derived by geometrical considerations for hard-sphere mixtures.

When the excluded volumes between the two particles overlap such that a third particle $\gamma$ cannot enter in the space between the two particles, there is a net attractive force between the two particles known as the depletion force [56]. The mean force between an $\alpha \beta$ pair due to a third particle is given as $F_{\alpha \beta}=-p_{0}^{\text {tot }} S$ where $p_{0}^{\text {tot }}$ is the total pressure of third-body particles and $S(r)$ is the cross-sectional area loss at the overlapping region, which depends on the distance $r$ between the two particles of an $\alpha \beta$ pair. For equal-size particles with diameter $d$, this surface is given by
$$
S(r)= \begin{cases}\pi\left(d^{2}-r^{2} / 4\right), & d \leqslant r \leqslant 2 d \\ 0, & r \geqslant 2 d.\end{cases}\qquad(\mathrm{G}1)
$$

The integration of this force $F_{\alpha \beta}$ yields the potential of mean force and the interaction $W_{\alpha \beta}(r)$ between the $\alpha \beta$ pair mediated by a third particle within the region $d \leqslant r \leqslant 2 d$. By imposing continuity of the interaction potential, we obtain
$$
W_{\alpha \beta}(r)=-p_{0}^{\text {tot }} w(r),
$$
$$
w(r)=\frac{\pi}{12}\left(16 d^{3}-12 d^{2} r+r^{3}\right) \Theta(2 d-r), \quad(\mathrm{G} 2)
$$
where $w(r)$ is the overlap volume and $\Theta(x)$ is Heaviside step function. Note that since $p_{0}^{\text {tot }}$ is a function of the third particle only, the mean force and the corresponding potential are independent of the $\alpha \beta$ pair, i.e., $W_{\alpha \beta}(r)=W(r)$. In a more formal manner, this potential can be expressed as
$$
W_{\alpha \beta}=-\sum_{\gamma} \int T_{\gamma} c_{\gamma}\left(\mathbf{r}_{\gamma}\right) \Theta\left(d-r_{\alpha \gamma}\right) \Theta\left(d-r_{\beta \gamma}\right) d \mathbf{r}_{\gamma}. \quad(\mathrm{G} 3)
$$

Then, by using the piecewise definition of the hard-sphere potential we write, up to first order in concentrations,
$$
g_{\alpha \beta}(r) \approx e^{-u_{\alpha \beta}(r) / T_{\alpha \beta}}\left[1-\frac{W_{\alpha \beta}(r)}{T_{\alpha \beta}}\right],\qquad(\mathrm{G}4)
$$
where the pairwise hard-sphere potential $u_{\alpha \beta}(r)=\infty$ for $r<d$ and $u_{\alpha \beta}(r)=0$ elsewhere.

We now use this pair distribution function to obtain thermodynamic properties. The pressure is obtained from the virial equation which becomes in the case of hard spheres of equal sizes
$$
p=\sum_{\alpha} T_{\alpha} c_{\alpha}+\frac{2}{3} \pi d^{3} \sum_{\alpha, \beta} c_{\alpha} c_{\beta} g_{\alpha \beta}(d) T_{\alpha \beta}. \quad(\mathrm{G} 5)
$$

Inserting the expression of the pair distribution function (G4), we obtain the pressure as
$$
p=\sum_{\alpha} T_{\alpha} c_{\alpha}+\frac{2}{3} \pi d^{3} \sum_{\alpha, \beta} c_{\alpha} c_{\beta}\left[T_{\alpha \beta} w(d) \sum_{\gamma} c_{\gamma} T_{\gamma}\right].
$$

The second and third virial coefficients are therefore $B=$ $\frac{4 \pi}{3} d^{3}$ and $C=\frac{2 \pi}{3} d^{3} w(d)$ with $w(d)=\frac{5 \pi}{12} d^{3}$ from Eq. (G2). Rewriting in terms of the virial coefficients gives Eq. (42) in the main text. Note that the third-order terms in the expansion are weighted by the temperature of the third particle. Thus, introducing different mobilities will not alter the form of this equation.

The next task is to implement the same strategy to the time-evolution equations for the concentrations $c_{A}$ and $c_{B}$, given

by Eqs. (6) and (7). In a similar way, we define the total mean force $\bar{f}_{\alpha}$ on particles $m$, as the gradient of a potential $\bar{f}_{\alpha} = -\nabla \Phi_{\alpha}$. Using Eq. (G4), the interaction part of the chemical potentials is expanded in powers of concentrations as $\Phi_{\mathcal{A}} = \Phi_{\mathcal{A}}^{(1)} + \Phi_{\mathcal{A}}^{(2)}$. The lowest-order term $\Phi_{\mathcal{A}}^{(1)}$ has been obtained in terms of the second virial coefficients in Eq. (9). We obtain the next-order contribution using Eqs. (G3) and (G4):

$$
\begin{aligned}
\nabla_{\mathbf{r}_{1}} \Phi_{\alpha}^{(2)}= & \sum_{\beta, \gamma}\left[\int \frac{\partial}{\partial \mathbf{r}_{1}}\left(1-e^{-u_{\alpha \beta}(r) / T_{\alpha \beta}}\right) c_{\beta}\left(\mathbf{r}_{2}\right) \int T_{\gamma} c_{\gamma}\left(\mathbf{r}_{3}\right)\right. \\
& \left.\times \Theta\left(d-r_{13}\right) \Theta\left(d-r_{23}\right) d \mathbf{r}_{3} d \mathbf{r}_{2}\right].
\end{aligned}
\tag{G7}
$$

By coordinate transformation, we get

$$
\begin{aligned}
\nabla_{\mathbf{r}_{1}} \Phi_{\alpha}^{(2)}= & \sum_{\beta, \gamma}\left[\int \widehat{\mathbf{r}} \delta(r-d) c_{\beta}\left(\mathbf{r}_{1}+\mathbf{r}\right) \int T_{\gamma} c_{\gamma}\left(\mathbf{r}_{1}+\mathbf{r}^{\prime}\right)\right. \\
& \left.\times \Theta\left(d-r^{\prime}\right) \Theta\left(d-\left|\mathbf{r}-\mathbf{r}^{\prime}\right|\right) d \mathbf{r}^{\prime} d \mathbf{r}\right]
\end{aligned}
\tag{G8}
$$

with $\mathbf{r} = \mathbf{r}_{2} - \mathbf{r}_{1}$ and $\mathbf{r}' = \mathbf{r}_{3} - \mathbf{r}_{1}$ where $\widehat{\mathbf{x}}$ denotes the unit vector along the direction of a vector $\mathbf{x}$. The second integral is constrained over the overlap volume $V_{\cap}$. Taking into account the Dirac delta function $\delta(r-d)$, it can be expressed as

$$
\begin{aligned}
& \int_{V_{\cap}} T_{\gamma} c_{\gamma}\left(\mathbf{r}_{1}+\mathbf{r}^{\prime}\right) d \mathbf{r}^{\prime} \\
& \quad=\int_{0}^{2 \pi} d \phi^{\prime} \int_{0}^{d} d r^{\prime} r^{\prime 2} \int_{\frac{r^{\prime}}{2 d}}^{1} d y^{\prime} T_{\gamma} c_{\gamma}\left(\mathbf{r}_{1}+\mathbf{r}^{\prime}\right),
\end{aligned}
\tag{G9}
$$

where $y' = \cos \theta'$. Finally, by Taylor expanding the concentrations around $\mathbf{r}_{1}$ up to first order in displacement vectors, we obtain

$$
\begin{aligned}
\nabla_{\mathbf{r}_{1}} \Phi_{\alpha}^{(2)}= & \sum_{\beta, \gamma}\left[T_{\gamma} \int \widehat{\mathbf{r}} \delta(r-d)\right. \\
& \times \int_{V_{\cap}}\left[c_{\beta}\left(\mathbf{r}_{1}\right) c_{\gamma}\left(\mathbf{r}_{1}\right)+c_{\gamma}\left(\mathbf{r}_{1}\right) \mathbf{r} \cdot \nabla_{\mathbf{r}_{1}} c_{\beta}\left(\mathbf{r}_{1}\right)\right. \\
& \left.\left.+c_{\beta}\left(\mathbf{r}_{1}\right) \mathbf{r}^{\prime} \cdot \nabla_{\mathbf{r}_{1}} c_{\gamma}\left(\mathbf{r}_{1}\right)\right] d \mathbf{r}^{\prime} d \mathbf{r}\right].
\end{aligned}
\tag{G10}
$$

Clearly, the first term, i.e., $c_{\beta}(\mathbf{r}_{1}) c_{\gamma}(\mathbf{r}_{1})$, vanishes upon integration. The second term can be integrated by writing $\nabla_{\mathbf{r}_{1}} c_{\gamma}(\mathbf{r}_{1}) \equiv \widehat{\mathbf{z}} |\nabla_{\mathbf{r}_{1}} c_{\gamma}(\mathbf{r}_{1})|$. A similar implementation on the third term (using product rules) gives

$$
\nabla_{\mathbf{r}_{1}} \Phi_{\alpha}^{(2)}=C \sum_{\beta, \gamma} T_{\gamma}\left[2 c_{\gamma}\left(\mathbf{r}_{1}\right) \nabla_{\mathbf{r}_{1}} c_{\beta}\left(\mathbf{r}_{1}\right)+c_{\beta}\left(\mathbf{r}_{1}\right) \nabla_{\mathbf{r}_{1}} c_{\gamma}\left(\mathbf{r}_{1}\right)\right].
\tag{G11}
$$

For equilibrium systems with $T_{\mathcal{A}}=T_{\mathcal{B}}$, this result gives back the third-virial coefficients between hard spheres. In the general case, for mixtures of particles with two different temperatures, we obtain Eq. (43) of the main text and $\nabla \Phi_{\mathcal{B}}^{(2)} = \nabla \Phi_{\mathcal{A}}^{(2)}$. Hence, it appears that this field is not integrable to obtain $\Phi_{\mathcal{B}}^{(2)}$. On the other hand, we observe that $c_{\mathcal{A}} \nabla \mu_{\mathcal{A}} + c_{\mathcal{B}} \nabla \mu_{\mathcal{B}} = \nabla p$ consistent with the result obtained from virial equation (G6).

This method could as well be implemented for mixtures of hard spheres with different diameters $d_{\mathcal{A}} \neq d_{\mathcal{B}}$ as well as different temperatures $T_{\mathcal{A}} \neq T_{\mathcal{B}}$. This would require to solve the general form of Eq. (G8) with varying contact distances,

$$
\begin{aligned}
\nabla_{\mathbf{r}_{1}} \Phi_{\alpha}^{(2)}= & \sum_{\beta, \gamma} \int \widehat{\mathbf{r}} \delta\left(r-d_{12}\right) c_{\beta}\left(\mathbf{r}_{1}+\mathbf{r}\right) \int T_{\gamma} c_{\gamma}\left(\mathbf{r}_{1}+\mathbf{r}^{\prime}\right) \\
& \times \Theta\left(d_{13}-r^{\prime}\right) \Theta\left(d_{23}-\left|\mathbf{r}-\mathbf{r}^{\prime}\right|\right) d \mathbf{r}^{\prime} d \mathbf{r}.
\end{aligned}
\tag{G12}
$$

## 2. Phase separation and coexistence conditions
Following the procedure described in Sec. III, we determine the phase diagrams at third order in concentration. A first remark is that we find an instability when $T_{\mathcal{A}} / T_{\mathcal{B}} \gtrsim 6.171$ for equal-sized spherical particles. Hence, the third-order terms delay the onset of phase separation compared to the second-order expansion which leads to phase separation when $T_{\mathcal{A}} / T_{\mathcal{B}} > 4$ (see Footnote 2). The phase coexistence conditions can be calculated by imposing that the particle fluxes to zero as well as the momentum flux. This last condition is obtained from $c_{\mathcal{A}} \nabla \mu_{\mathcal{A}} + c_{\mathcal{B}} \nabla \mu_{\mathcal{B}} = \nabla p = 0$, which gives mechanical equilibrium, and therefore imposes that pressure is constant. The other conditions require that $\nabla \mu_{\mathcal{A}} = 0$ and $\nabla \mu_{\mathcal{B}} = 0$. However, the chemical potential gradients are not integrable. Nevertheless, since $\nabla \Phi_{\mathcal{A}}^{(2)} = \nabla \Phi_{\mathcal{B}}^{(2)}$, we can use the condition that $\nabla (\mu_{\mathcal{A}} - \mu_{\mathcal{B}}) = 0$ which would lead to two gradient free equations. Therefore, to summarize, we find two conditions for the the $a$ and $b$ phases to coexist:

$$
\mu_{\mathcal{A}}^{(1)}\left(c_{\mathcal{A}}^{a}, c_{\mathcal{B}}^{a}\right)-\mu_{\mathcal{B}}^{(1)}\left(c_{\mathcal{A}}^{a}, c_{\mathcal{B}}^{a}\right)=\mu_{\mathcal{A}}^{(1)}\left(c_{\mathcal{A}}^{b}, c_{\mathcal{B}}^{b}\right)-\mu_{\mathcal{B}}^{(1)}\left(c_{\mathcal{A}}^{b}, c_{\mathcal{B}}^{b}\right),
\tag{G13}
$$

$$
p\left(c_{\mathcal{A}}^{a}, c_{\mathcal{B}}^{a}\right)=p\left(c_{\mathcal{A}}^{b}, c_{\mathcal{B}}^{b}\right),
\tag{G14}
$$

where we defined with $\mu_{\alpha}^{(1)} = \mu_{\alpha}^{\text{id}} + \Phi_{\alpha}^{(1)}, \alpha = \mathcal{A}, \mathcal{B}$.

The third condition required to construct the phase diagrams is not directly accessible in a general form due to the lack of well-defined chemical potentials. Yet, it is possible to derive an approximate condition in the vicinity of the critical point by linearizing the time-evolution equations in concentrations.

[1] P. M. Chaikin and T. C. Lubensky, *Principles of Condensed Matter Physics* (Cambridge University Press, Cambridge, 1995), Vol. 1.

[2] M. C. Marchetti, J.-F. Joanny, S. Ramaswamy, T. B. Liverpool, J. Prost, M. Rao, and R. A. Simha, Hydrodynamics of soft active matter, *Rev. Mod. Phys.* **85**, 1143 (2013).

[3] D. Zwicker, M. Decker, S. Jaensch, A. A. Hyman, and F. Jülicher, Centrosomes are autocatalytic droplets of pericentriolar material organized by centrioles, *Proc. Natl. Acad. Sci. USA* **111**, E2636 (2014).

[4] J. B. Woodruff, B. F. Gomes, P. O. Widlund, J. Mahamid, A. Honigmann, and A. A. Hyman, The centrosome is a selective

condensate that nucleates microtubules by concentrating tubu- lin, Cell 169, 1066 (2017).

[5] J. Agudo-Canalejo and R. Golestanian, Active Phase Separation in Mixtures of Chemically Interacting Particles, Phys. Rev. Lett. 123, 018101 (2019).

[6] J. Palacci, S. Sacanna, A. P. Steinberg, D. J. Pine, and P. M. Chaikin, Living crystals of light-activated colloidal surfers, Science 339, 936 (2013).

[7] D. P. Singh, U. Choudhury, P. Fischer, and A. G. Mark, Non- equilibrium assembly of light-activated colloidal mixtures, Adv. Mater. 29, 1701328 (2017).

[8] J. Zhang, J. Guo, F. Mou, and J. Guan, Light-controlled swarm- ing and assembly of colloidal particles, Micromachines 9, 88 (2018).

[9] Z. Lin, C. Gao, M. Chen, X. Lin, and Q. He, Collective mo- tion and dynamic self-assembly of colloid motors, Curr. Opin. Colloid Interface Sci. 35, 51 (2018).

[10] M. N. Popescu, W. E. Uspal, C. Bechinger, and P. Fischer, Chemotaxis of active janus nanoparticles, Nano Lett. 18, 5345 (2018).

[11] A. Y. Grosberg and J.-F. Joanny, Nonequilibrium statistical mechanics of mixtures of particles in contact with different thermostats, Phys. Rev. E 92, 032118 (2015).

[12] S. N. Weber, C. A. Weber, and E. Frey, Binary Mixtures of Particles with Different Diffusivities Demix, Phys. Rev. Lett. 116, 058301 (2016).

[13] H. Tanaka, A. A. Lee, and M. P. Brenner, Hot particles attract in a cold bath, Phys. Rev. Fluids 2, 043103 (2017).

[14] A. Y. Grosberg and J.-F. Joanny, Dissipation in a system driven by two different thermostats, Polym. Sci. Ser. C 60, 118 (2018).

[15] J. Smrek and K. Kremer, Small Activity Differences Drive Phase Separation in Active-Passive Polymer Mixtures, Phys. Rev. Lett. 118, 098002 (2017).

[16] J. Smrek and K. Kremer, Interfacial properties of active-passive polymer mixtures, Entropy 20, 520 (2018).

[17] H. C. Berg, E. coli in Motion (Springer, New York, 2008).

[18] L. Pitaevskii and E. Lifshitz, Physical Kinetics (Butterworth- Heinemann, Oxford, 2012), Vol. 10.

[19] M. G. Wolfire, C. F. McKee, D. Hollenbach, and A. Tielens, Neutral atomic phases of the interstellar medium in the galaxy, Astrophys. J. 587, 278 (2003).

[20] D. P. Cox, The three-phase interstellar medium revisited, Annu. Rev. Astron. Astrophys. 43, 337 (2005).

[21] K. M. Ferriere, Circumstellar environment of our galaxy, Rev. Mod. Phys. 73, 1031 (2001).

[22] L. F. Cugliandolo, The effective temperature, J. Phys. A: Math. Theor. 44, 483001 (2011).

[23] R. Exartier and L. Peliti, A simple system with two tempera- tures, Phys. Lett. A 261, 94 (1999).

[24] A. Crisanti, A. Puglisi, and D. Villamaina, Nonequilibrium and information: The role of cross correlations, Phys. Rev. E 85, 061127 (2012).

[25] A. Chertovich, E. Govorun, V. Ivanov, P. Khalatur, and A. Khokhlov, Conformation-dependent sequence design: Evolu- tionary approach, Eur. Phys. J. E 13, 15 (2004).

[26] V. S. Pande, A. Y. Grosberg, and T. Tanaka, Heteropolymer freezing and design: towards physical models of protein fold- ing, Rev. Mod. Phys. 72, 259 (2000).

[27] J. W. Cahn and J. E. Hilliard, Free energy of a nonuniform system. i. interfacial free energy, J. Chem. Phys. 28, 258 (1958).

[28] A. J. Bray, Theory of phase-ordering kinetics, Adv. Phys. 51, 481 (2002).

[29] Y. Oono and M. Paniconi, Steady state thermodynamics, Suppl. Prog. Theor. Phys. 130, 29 (1998).

[30] J. Irving and J. G. Kirkwood, The statistical mechanical theory of transport processes. iv. the equations of hydrodynamics, J. Chem. Phys. 18, 817 (1950).

[31] J.-P. Hansen and I. R. McDonald, Theory of Simple Liquids (Cambridge University Press, Cambridge, 1995), Vol. 1.

[32] P. Schofield and J. R. Henderson, Statistical mechanics of inhomogeneous fluids, Proc. R. Soc. London Ser. A 379, 231 (1982).

[33] A. A. Aerov and M. Krüger, Driven colloidal suspensions in confinement and density functional theory: Microstructure and wall-slip, J. Chem. Phys. 140, 094701 (2014).

[34] M. Krüger, A. Solon, V. Démery, C. M. Rohwer, and D. S. Dean, Stresses in non-equilibrium fluids: Exact formulation and coarse-grained theory, J. Chem. Phys. 148, 084503 (2018).

[35] J. W. Gibbs, On the equilibrium of heterogeneous substances, Am J. Sci. 300 (1878).

[36] S. S. N. Chari, C. Dasgupta, and P. K. Maiti, Scalar activ- ity induced phase separation and liquid–solid transition in a lennard-jones system, Soft Matter 15, 7275 (2019).

[37] J. Lebowitz and J. Rowlinson, Thermodynamic properties of mixtures of hard spheres, J. Chem. Phys. 41, 133 (1964).

[38] J. S. Langer and C. Beenakker, Phase separation and pattern formation, Fund. Problems Stat. Mech. 6, 313 (1985).

[39] I. M. Lifshitz and V. V. Slyozov, The kinetics of precipitation from supersaturated solid solutions, J. Phys. Chem. Solids 19, 35 (1961).

[40] R. Wittkowski, A. Tiribocchi, J. Stenhammar, R. J. Allen, D. Marenduzzo, and M. E. Cates, Scalar $\varphi$ 4 field theory for active- particle phase separation, Nat. Commun. 5, 4351 (2014).

[41] C. F. Lee, Interface stability, interface fluctuations, and the gibbs–thomson relationship in motility-induced phase separa- tions, Soft Matter 13, 376 (2017).

[42] I. Theurkauff, C. Cottin-Bizonne, J. Palacci, C. Ybert, and L. Bocquet, Dynamic Clustering in Active Colloidal Suspensions with Chemical Signaling, Phys. Rev. Lett. 108, 268303 (2012).

[43] J. G. Mitchell, The influence of cell size on marine bacterial motility and energetics, Microb. Ecol. 22, 227 (1991).

[44] I. R. Bruss and S. C. Glotzer, Phase separation of self-propelled ballistic particles, Phys. Rev. E 97, 042609 (2018).

[45] J. Stenhammar, R. Wittkowski, D. Marenduzzo, and M. E. Cates, Activity-Induced Phase Separation and Self-Assembly in Mixtures of Active and Passive Particles, Phys. Rev. Lett. 114, 018301 (2015).

[46] J. Bialké, J. T. Siebert, H. Löwen, and T. Speck, Negative Inter- facial Tension in Phase-Separated Active Brownian Particles, Phys. Rev. Lett. 115, 098301 (2015).

[47] A. K. Omar, Z.-G. Wang, and J. F. Brady, Microscopic origins of the swim pressure and the anomalous surface tension of active matter, Phys. Rev. E 101, 012604 (2020).

[48] S. Hermann, D. de las Heras, and M. Schmidt, Non-Negative Interfacial Tension in Phase-Separated Active Brownian Parti- cles, Phys. Rev. Lett. 123, 268002 (2019).

[49] A. P. Solon, J. Stenhammar, M. E. Cates, Y. Kafri, and J. Tailleur, Generalized thermodynamics of motility-induced phase separation: Phase equilibria, laplace pressure, and change of ensembles, New J. Phys. 20, 075001 (2018).

[50] C. P. Brangwynne, P. Tompa, and R. V. Pappu, Polymer physics of intracellular phase transitions, *Nat. Phys.* **11**, 899 (2015).

[51] N. Ganai, S. Sengupta, and G. I. Menon, Chromosome positioning from activity-based segregation, *Nucleic Acids Res.* **42**, 4145 (2014).

[52] J. Nuebler, G. Fudenberg, M. Imakaev, N. Abdennur, and L. A. Mirny, Chromatin organization by an interplay of loop extrusion and compartmental segregation, *Proc. Natl. Acad. Sci. USA* **115**, E6697 (2018).

[53] D. Osmanović and Y. Rabin, Dynamics of active rouse chains, *Soft Matter* **13**, 963 (2017).

[54] M. Wang and A. Y. Grosberg, Three-body problem for langevin dynamics with different temperatures, *Phys. Rev. E* **101**, 032131 (2020).

[55] A. Singer, Maximum entropy formulation of the kirkwood superposition approximation, *J. Chem. Phys.* **121**, 3657 (2004).

[56] S. Asakura and F. Oosawa, Interaction between particles suspended in solutions of macromolecules, *J. Polym. Sci.* **33**, 183 (1958).

[57] Y. Mao, M. Cates, and H. Lekkerkerker, Depletion force in colloidal systems, *Physica A (Amsterdam)* **222**, 10 (1995).

[58] E. Tjhung, C. Nardini, and M. E. Cates, Cluster Phases and Bubbly Phase Separation in Active Fluids: Reversal of the Ostwald Process, *Phys. Rev. X* **8**, 031080 (2018).

[59] J. G. Kirkwood, Statistical mechanics of fluid mixtures, *J. Chem. Phys.* **3**, 300 (1935).