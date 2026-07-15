# Phase competition in solid-state reactive diffusion revisited—Stochastic kinetic mean-field approach

Cite as: J. Chem. Phys. 150, 174109 (2019); https://doi.org/10.1063/1.5086046
Submitted: 17 December 2018 . Accepted: 05 April 2019 . Published Online: 06 May 2019

Andriy Gusak, Tetiana Zaporozhets, and Nadiia Storozhuk

![](./images/812778938383204352_1.jpg) ![](./images/812778938383204352_2.jpg) ![](./images/812778938383204352_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

Mean first passage times in variational coarse graining using Markov state models
The Journal of Chemical Physics 150, 134107 (2019); https://doi.org/10.1063/1.5083924

Configurational entropy of glass-forming liquids
The Journal of Chemical Physics 150, 160902 (2019); https://doi.org/10.1063/1.5091961

Identification of kinetic order parameters for non-equilibrium dynamics
The Journal of Chemical Physics 150, 164120 (2019); https://doi.org/10.1063/1.5083627

![](./images/812778938383204352_4.jpg)

J. Chem. Phys. 150, 174109 (2019); https://doi.org/10.1063/1.5086046
150, 174109

© 2019 Author(s).

# Phase competition in solid-state reactive diffusion revisited—Stochastic kinetic mean-field approach

Cite as: J. Chem. Phys. 150, 174109 (2019); doi: 10.1063/1.5086046
Submitted: 17 December 2018 • Accepted: 5 April 2019 •
Published Online: 3 May 2019

![](./images/812778938383204352_5.jpg) ![](./images/812778938383204352_6.jpg) ![](./images/812778938383204352_7.jpg)

Andriy Gusak, ${}^{a)}$ Tetiana Zaporozhets, and Nadiia Storozhuk

## AFFILIATIONS
The Bohdan Khmelnytsky National University of Cherkasy, Blvd. Shevchenko 81, Cherkassy 18031, Ukraine

${}^{a)}$E-mail: amgusak@ukr.net

## ABSTRACT
Kinetic mean-field method for description of diffusion (introduced in 1990 by George Martin) is developed to 3D with the inclusion of the frequency noise. After this, it is applied to modeling of reactive diffusion—formation, competition, and growth of the ordered intermediate phases during interdiffusion. Results seem reasonable; hence, the method can be used for qualitative study of complicated cases of the competitive first-order transitions in closed and open systems with rigid lattices.

Published under license by AIP Publishing. https://doi.org/10.1063/1.5086046

## I. INTRODUCTION: GENERAL PROBLEM OF PHASE COMPETITION AND THE CHOICE OF EVOLUTION PATH

Reactions between two solid materials or between solid and liquid materials with formation of several solid phases (reaction products) provide us with a problem which simultaneously is of fundamental importance in physics, chemistry, and materials science, and is a key to existing and developing technologies of joining, with basic concern about reliability, production and exploitation of composite materials, 3D-printers technologies, etc. When two elements A and B react, they can, as a rule, demonstrate (simultaneously or following some time sequence) the formation of several intermediate phases $A_mB_n$, each of which has its own composition range determined by the interphase equilibrium conditions. For example, reactions between liquid tin-based solder and copper lead to almost simultaneous formation of two intermediate compounds $Cu_6Sn_5$ and $Cu_3Sn$. $^{1}$ Scallops of the $Cu_6S_5$ compound actually form and keep the contact after crystallization of solder. The second phase layer—that of $Cu_3Sn$, on the contrary, is a place of the Kirkendall voids formation and, hence, finally leads to the mechanical failure of solder joint. Thus, the dream of an engineer would be to influence the phase formation, helping "useful" intermediate phases to reach optimal sizes and suppressing "harmful" phases.

From the physical point of view, solid state reactions are just the phase transformations in the highly inhomogeneous open system—contact zone, under sharp concentration gradient. Historically, phase transformations had been studied as the processes driven by the change of temperature or pressure. The phase transformations driven by the change of concentration (due to diffusion) are also very interesting. Moreover, the temperature time derivative $dT/dt$ (temperature ramp in a fixed time) is a very important factor deciding what transformations will actually happen. High rate of temperature lowering (quenching) may suppress practically all phase transformations. We claim that the concentration gradient value $dC/dx$ also provides a very important factor governing the phase formation and competition in the contact zone.

From a physical point of view, competitive solid-state reactions present a vivid example of the general problem of the choice of evolution path. $^{2}$ Discussion of this problem was started by Ostwald with his famous rule of stages $^{3}$ and recently was generalized in terms of nucleation properties with account of generalized Gibbs' approach. $^{4-6}$ We will concentrate on the choice of evolution path in the contact zone (in the field of concentration gradients).

For example, in the thin film couple (or multilayer) A-B, in the case of two intermediate compounds 1, 2 at the equilibrium phase diagram, and with average composition corresponding to

compound 2, the possible evolution paths can be, in general, the following:

$$\mathrm{A} + \mathrm{B} \rightarrow \mathrm{A} + 1 + 2 + \mathrm{B} \rightarrow 1 + 2 + \mathrm{B} \rightarrow 2,$$

$$\mathrm{A} + \mathrm{B} \rightarrow \mathrm{A} + 1 + \mathrm{B} \rightarrow 1 + \mathrm{B} \rightarrow 1 + 2 + \mathrm{B} \rightarrow 2,$$

$$\mathrm{A} + \mathrm{B} \rightarrow \mathrm{A} + 2 + \mathrm{B} \rightarrow \mathrm{A} + 1 + 2 + \mathrm{B} \rightarrow 2,$$

$$\mathrm{A} + \mathrm{B} \rightarrow \mathrm{A} + 2 + \mathrm{B} \rightarrow 2.$$

How does nature choose one of these paths? Our starting points of analysis are as follows:

1.  Usually, intermediate phase formation is a first-order transition starting from overcoming the nucleation barriers. So, the first phase to appear should be the phase with minimal incubation period. And this, as a rule, corresponds to minimal sum of nucleation barrier and activation energy of growth.
2.  Even if all nucleation barriers are low, it does not mean that nucleation stage is not important, since the minimum of incubation period determines the phase which forms first.
3.  Formation of the first phase may drastically change the conditions for nucleation of the further phases. For example, let intermediate compounds 1, 2 have large and close Gibbs free energies of formation from pure A and B and, hence, have similar chances to nucleate. Yet, if by some kinetic reason phase 1 nucleated and grew as a layer first, then phase 2 can form only in the reaction $1 + \mathrm{B} \rightarrow 2$, and for this reaction, the driving force is substantially less. In this case, phase 2 may appear after rather long waiting time.
4.  Fastest nucleation of some phase does not mean that we will observe it in the coarsened mesoscopic scale since diffusive interaction of the new-born medium may, in some cases, lead to the collapse of the already nucleated phase.
5.  Choice of evolution path, at least in the contact zone, is determined by nucleation in the sharp concentration gradient, by diffusive interaction with the new-born nuclei of other phases and with inhomogeneous surrounding materials in the contact zone.

The problem of the first phase to form and, in general, of the phase formation sequence became popular with development of thin films and multilayers technologies, $^{7}$ especially in application to silicides in microelectronics. $^{8}$ It was very important to understand the typical sequential, one-by-one phase growth in thin film reactions. The story became even more interesting after discovery of solid-state amorphization reactions, $^{9,10}$ which demonstrated the growth of metastable amorphous layer (absent at the equilibrium phase diagram) instead of stable, "legal" intermetallics. Until 1979, the typical explanation of the sequential growth was that the growth is in fact simultaneous for all phases but most of the growing phases grow so slowly (much slower than the fastest phase layer) that it is not possible to fix and measure these phases. Such explanation could be used in times of "micron-scale" reactive diffusion studies when the standard tools of diffusion zone study had the resolution less than one micron. Now, when 3D atomic tomography and HRTEM are used, $^{11,12}$ we know for sure that this explanation was wrong—most of the intermediate phases which we do not see are indeed absent in the thin-film diffusion couples. The first reasonable explanation of the temporal absence of some phases was suggested in semi-quantitative form by Geguzin *et al.* in Refs. 13 and 14. Explanation was based on the possibility of interface-controlled kinetics of reactive growth at the initial growth stage. The same idea, but in mathematically more full and rigorous way was realized by Goesele and Tu three years later, in $1982.^{15}$ Alternative analytic theories of kinetic and thermodynamic suppression of nucleation by the neighboring phases and by sharp concentration gradients were suggested and developed by our group jointly with Desre, Hodaj, and Schmitz. $^{16-28}$

The abovementioned theoretical predictions of the first phase to grow and of the critical concentration gradient may well explain the phase formation in Ni-Zr, Co-Al, Ni-Si, Cu-Si, Ni-Al, and other systems. $^{29-35}$ Yet, we still cannot see *in situ* the details of phase competition and we still need some simulation tools which could verify the existing theories of phase competition by computer experiment, in addition to the real experiment.

It looks like in the last two years we got the necessary (fast and effective) tool. It is a so-called SKMF (Stochastic Kinetic Mean Field) method developed by the Cherkasy team jointly with a team from Debrecen University. $^{36}$ (Recently, the coauthor of the SKMF method, Prof. Erdelyi, suggested an alternative transcript—Stochastic Kinetic Modeling Framework.) This method is a natural development of the nonlinear kinetic mean-field model (KMF) suggested by Martin in $1990.^{37}$ As was physically clear from the very beginning and as rigorously proven in the present paper, the KMF model can describe only processes with a continuous decrease of the free energy up to a minimum. It means that in the KMF model, the role and meaning of temperature are realized only partially—providing atomic jumps, each of which requires overcoming an activation barrier by some atomic-scale fluctuations, but it does not provide the long-range fluctuations leading to overcoming, say, the nucleation barriers. Therefore, KMF cannot be used for a correct description of the first-order phase transitions. To improve this obvious drawback, we suggested introducing some noise—like a noise of forces in Brownian motion. In our case, we decided to introduce the noise of fluxes between sites (in terms of the noise of jump frequencies) as the random deviations from the Boltzmann-like exponential expressions. In this paper, we apply this new method to reactive diffusion with several phase layers growing and competing in the diffusion zone.

The paper is organized in the following way. In Sec. II, we analyze the main ideas of KMF-SKMF approach, especially the necessity of noise for description of nucleation stage. In Sec. III, we construct the phase diagram using self-consistently the KMF for the diffusion couples consisting of neighboring crystalline FCC phases at the phase diagram: A-ordered $\mathrm{A_3B}$, ordered $\mathrm{A_3B}$-ordered $\mathrm{AB}$, ordered $\mathrm{AB}$-ordered $\mathrm{AB_3}$, and ordered $\mathrm{AB_3}$-B. To have a good and distinct phase diagram for such a system, we use interatomic interactions in two coordination shells—12 nearest neighbors and 6 next-nearest neighbors. Then, we apply SKMF to reactive diffusion in the incremental diffusion couples $\mathrm{A-AB}$, $\mathrm{A_3B-AB_3}$, $\mathrm{AB-B}$ (with one growing intermediate phase), $\mathrm{A-AB_3}$, $\mathrm{A_3B-B}$ (with two competing intermediate phases), and $\mathrm{A-B}$ (with three competing intermediate phases).

## II. FROM KMF TO SKMF—WHY AND HOW

Well-known quasi-1D kinetic mean-field approach to the problems of atomic migration in solids was suggested by George

Martin in 1990.³⁷ Namely, the master equation was constructed for the probability $C_p$ of finding atom A at the site belonging to plane number "$p$." This master equation implemented the balance of local in- and out-fluxes for any site. Moreover, it self-consistently used the mean-field approximation for calculation of energy barriers in the jump frequencies (exchange mechanism was considered as an example):

This model was applied by the Debrecen team to asymmetric diffusion (big difference $|V_{AA}-V_{BB}|$) in nanofilms with sharp gradients of the jump frequencies. Among other effects, this approach predicted a possibility of the sharpening of diffusion profiles (instead of traditional smoothening) and other nonlinear effects at the initial stages of interdiffusion, in case of large diffusional asymmetry.³⁸,³⁹

In Ref. 40, the generalization of Martin's equations to the 3D-case was suggested. Namely, the following kinetic equations have been suggested for "concentration" (probability) at the site "$i$" surrounded by nearest neighbors (the sites indicated by "$in$"):

$$
\begin{aligned}
\frac{d C_{A}[i]}{d t}= & \sum_{i n=1}^{Z}\left(-C_{A}[i] C_{B}[i n] \Gamma[i(A), i n(B)]\right. \\
& \left.+C_{B}[i] C_{A}[i n] \Gamma[i n(A), i(B)]\right).
\end{aligned}
\tag{1}
$$

Here, the jumps are restricted (within Martin's model) only to the first coordination shell (exchanges between nearest neighbors). Exchange frequencies between A and B in the neighboring sites "$i$" and "$in$" are determined in Refs. 37 and 40 via Arrhenius law like

$$
\begin{aligned}
\Gamma[i(A), i n(B)] & =v_{0} \exp \left(-\frac{Q_{i, i n}}{k T}\right) \\
& =v_{0} \exp \left(-\frac{E^{s}-\left(E_{A}[i]+E_{B}[i n]\right)}{k T}\right),
\end{aligned}
\tag{2}
$$

with the saddle-point assumed the same for all jumps, and with energies before jump calculated taking into account interaction only with $Z$ nearest neighbors ($V_{AA}$, $V_{BB}$, and $V_{AB}$) and without any account of correlations—in the mean-field approximation

$$
\begin{aligned}
E_{A}[i] & =\sum_{i n=1}^{Z}\left(C_{A}[i n] \cdot V_{A A}+C_{B}[i n] \cdot V_{A B}\right), E_{B}[i n] \\
& =\sum_{i n n=1}^{Z}\left(C_{A}[i n n] \cdot V_{B A}+C_{B}[i n n] \cdot V_{B B}\right).
\end{aligned}
\tag{3}
$$

## A. Steady-state limit of 3D-modification of the KMF

In Ref. 37, the steady-state case of the kinetic equations in the quasi-1D-scheme was considered. In the general 3D-case, we also start from the steady-state solutions of Eqs. (1)-(3). Obviously, all time derivatives (for all sites "$i$") in Eq. (1) are equal to zero if the detailed balance is satisfied

$$
C_{A}[i] C_{B}[i n] \Gamma[i(A), i n(B)]=C_{B}[i] C_{A}[i n] \Gamma[i n(A), i(B)]. \tag{4}
$$

To make the detailed balance closer to thermodynamics, one can reformulate Eq. (4) as

$$
\frac{C_{A}[i]}{C_{B}[i]} \exp \left(\frac{E_{A}[i]-E_{B}[i]}{k T}\right)=\frac{C_{A}[i n]}{C_{B}[i n]} \exp \left(\frac{E_{A}[i n]-E_{B}[i n]}{k T}\right). \tag{5}
$$

Equation (18) can be interpreted as the equalizing of the reduced chemical potentials within the system. (We remind that the reduced chemical potential $\tilde{\mu}=\mu_{A}-\mu_{B}$ means the change of Gibbs free energy due to the substitution of atom B by the atom A)

$$
\tilde{\mu}[i]=\tilde{\mu}[i n] \equiv \tilde{\mu}=const. \tag{6}
$$

The reduced chemical potential, obtained from the condition Ref. 5 coincides with expressions obtained from the regular solution model in the approximation of the nearest neighbors' interaction.

$$
\begin{aligned}
\tilde{\mu}[i] & =\mu_{A}[i]-\mu_{B}[i]=k T \ln \frac{C_{A}[i]}{C_{B}[i]}+E_{A}[i]-E_{B}[i] \\
& =k T \ln \frac{C_{A}[i]}{C_{B}[i]}-2 V^{m i x} \sum_{i n=1}^{Z} C_{A}[i n]+Z \cdot\left(V_{A B}-V_{B B}\right),
\end{aligned}
\tag{7}
$$

$\mu_{A}[i]=k T \ln C_{A}[i]+E_{A}[i]+const, \mu_{B}[i]=k T \ln C_{B}[i]+E_{B}[i]+const,$

$V^{mix}=V_{AB}-(V_{AA}+V_{BB})/2$-mixing energy.

Martin's kinetic equations tend to steady-state, and steady-state in the closed system means equilibrium—stable or metastable. Thus, Eq. (7) leads to the self-consistent set of non-linear algebraic equations

$$
\begin{aligned}
C_{A}[i]= & \left(1-C_{A}[i]\right) \exp \left(\frac{2 V^{m i x}}{k T} \sum_{i n=1}^{Z} C_{A}[i n]\right) \\
& \times \exp \left(\frac{\tilde{\mu}-Z \cdot\left(V_{A B}-V_{B B}\right)}{k T}\right), i=1, \ldots, N,
\end{aligned}
\tag{8}
$$

with the constraint of matter conservation

$$
\sum_{i=1}^{N} C_{A}[i]=N \bar{C}_{A}. \tag{9}
$$

Equation analogic to Eq. (8) was suggested by Khachaturyan, not using the steady-state condition but instead with arguments of the Fermi-Dirac-type equation. He used this equation for his method of concentration waves.⁴¹,⁴² Thus, limiting (steady-state) case of Martin's kinetic approach provides self-consistent mean-field thermodynamics. In our applications in Sec. III, we will modify all mentioned schemes including interactions in the second coordination shell.

## B. Time evolution of free energy - Analog of H-theorem

It is convenient to represent the kinetic equation (1) in terms of exchanges between pairs of sites "$i$," "$in$," then the matter conservation will be guaranteed automatically

$$
\frac{d C_{A}[i]}{d t}=\sum_{i n=1}^{Z} \frac{d C_{A}^{(i, i n)}}{d t},
$$

$$
\begin{aligned}
\frac{d C_{A}^{(i, i n)}}{d t}= & -C_{A}[i] C_{B}[i n] \Gamma[i(A), i n(B)] \\
& +C_{B}[i] C_{A}[i n] \Gamma[i n(A), i(B).
\end{aligned}
\tag{10}
$$

We call expressions $d C_{A}^{(i, i n)} / d t$ the "partial" time derivatives. They determine the rate of change of concentration in site "$i$" (and

simultaneously the opposite change of concentration in neighboring site “in” due to the exchanges only between these two sites. In case of direct exchange between atom A at the site “in” and atom B at the site “in” (change of $C_A[i]$ from zero to 1), change of Gibbs free energy consists of two changes: $\tilde{\mu}_{AB}[i] = \mu_A[i] - \mu_B[i]$ (change from A to B) and $-\tilde{\mu}_{AB}[in] = -\mu_A[in] + \mu_B[in]$. For infinitesimal changes and for their rate one obtains

$$
\frac{d G}{d t}=\sum_{(i, i n)}^{N Z / 2}\left(\tilde{\mu}_{A B}[i]-\tilde{\mu}_{A B}[i n]\right) \frac{d C_{A}^{(i, i n)}}{d t}. \tag{11}
$$

$$
\frac{d G}{d t}=-v_{0} \exp \left(-\frac{E^{s}}{k T}\right) k T \sum_{(i, i n)}^{N Z / 2}\left[\begin{array}{l}
C_{B}[i] C_{B}[i n] \exp \left(\frac{E_{B}[i]+E_{B}[i n]}{k T}\right) \\
\times\left(\ln \left(\frac{C_{A}[i]}{C_{B}[i]} \exp \left(\frac{E_{A}[i]-E_{B}[i]}{k T}\right)\right)-\ln \left(\frac{C_{A}[i n]}{C_{B}[i n]} \exp \left(\frac{E_{A}[i n]-E_{B}[i n]}{k T}\right)\right)\right) \\
\times\left(\frac{C_{A}[i]}{C_{B}[i]} \exp \left(\frac{E_{A}[i]-E_{B}[i]}{k T}\right)-\frac{C_{A}[i n]}{C_{B}[i n]} \exp \left(\frac{E_{A}[i n]-E_{B}[i n]}{k T}\right)\right)
\end{array}\right]. \tag{12}
$$

This expression for the Gibbs free energy evolution looks more transparent in terms of the reduced chemical potentials [introduced according to Eq. (7)]:

$$
\begin{aligned}
\frac{d G}{d t}= & -v_{0} \exp \left(-\frac{E^{s}}{k T}\right) \sum_{(i, i n)}^{N Z / 2} C_{B}[i] C_{B}[i n] \exp \left(\frac{E_{B}[i]+E_{B}[i n]}{k T}\right) \\
& \times\left(\tilde{\mu}_{A B}[i]-\tilde{\mu}_{A B}[i n]\right)\left(\exp \left(\frac{\tilde{\mu}_{A B}[i]}{k T}\right)-\exp \left(\frac{\tilde{\mu}_{A B}[i n]}{k T}\right)\right). \tag{13}
\end{aligned}
$$

Obviously, the product $(f1 - f2)(\exp(f1) - \exp(f2))$ is positive for any values $f1, f2$, except the case $f1 = f2$ when this product is zero. Therefore, expression $\left(\frac{\tilde{\mu}_{A B}[i]}{k T}-\frac{\tilde{\mu}_{A B}[i n]}{k T}\right)\left(\exp \left(\frac{\tilde{\mu}_{A B}[i]}{k T}\right)-\exp \left(\frac{\tilde{\mu}_{A B}[i n]}{k T}\right)\right)$ in Eq. (13) is always positive except the case of equilibrium, when it is zero. Therefore, in a kinetic mean-field model

$$
\left.\frac{d G}{d t}\right|_{K M F} \leq 0\left(=0 \text { at equilibrium }\right). \tag{14}
$$

Thus, indeed, overcoming of nucleation barriers in KMF-model is impossible. In the mentioned product, the first factor (difference of reduced chemical potential between neighboring sites) is the driving force of exchange, and the second factor (the difference between exponents of reduced chemical potentials divided by $kT$) corresponds to the general nonlinear expression for the flux of exchanging atom. Thus, one has a common structure of nonequilibrium thermodynamics (products of driving forces and fluxes), but in the nonlinear version. Therefore, the nonlinear Martin's model works effectively for the initial stages of diffusion in case of sharp concentration gradients. It could predict a possibility of concentration profile sharpening instead of smoothening. $^{38,39}$ Thus, we just proved that the KMF equation may describe only the minimization of the free energy. Any other process related to overcoming the free energy barrier, cannot be described by KMF. To model the evolution from the metastable state to the stable state by overcoming of the nucleation barrier, one should introduce some noise.

Substituting Eq. (7) for the reduced chemical potentials, and Eq. (10) for the partial time derivatives, one gets, after elementary transformations,

In principle, noise can be added (2) only for initial conditions (this version was initially suggested in Ref. 40) and (2) dynamically, at each time moment.

### C. Stochastic development of KMF

In linear theories of nonequilibrium thermodynamics, the noise of concentration and of order parameter is usually introduced within the Onsager approach, using the FDT (fluctuation-dissipation theorem)—see, for example, Khachaturyan *et al.*. $^{41,42}$ Yet, this method has some limitations:

(1) Onsager approach for atomic local fluxes is not fully self-consistent: Onsager coefficients and their activation energies are not related to the local compositions. Conditions of zero fluxes or of steady-state in such schemes never provide any equation of state like Eq. (21) or (11), contrary to the KMF approach.
(2) Order parameter fluctuations in standard stochastic approaches are introduced independently of concentration fluctuations. On the contrary, in Martin's approach the order is not something independent—we do not need to introduce it additionally, it is contained fully in the unary probabilities at the sites and sublattices.
(3) It seems natural to introduce the fluctuations of the jump frequencies as a true source of the noise.

In 2016, the SKMF-method based on the introduction of the noise of intersite fluxes was suggested $^{19}$ (see also skmf.eu)

$$
\frac{d C_{i}}{d t}=-\sum_{j=1}^{Z}\left[C_{i}\left(1-C_{j}\right)\left(\Gamma_{i, j}+\delta \Gamma_{i, j}^{L a n g}\right)-\left(1-C_{i}\right) C_{j}\left(\Gamma_{j, i}+\delta \Gamma_{j, i}^{L a n g}\right)\right], \tag{15}
$$

$$
\delta \Gamma_{i, k}^{L a n g}=\frac{A_{n}}{\sqrt{d t}} \sqrt{3}(2 r a n d o m-1). \tag{16}
$$

This Langevin noise of local fluxes (in terms of the noise of frequencies) is introduced without any time or spatial correlations
$$
\left\langle\delta \Gamma_{i, j}^{\text {Lang }}(t) \delta \Gamma_{k, m}^{\text {Lang }}\left(t^{\prime}\right)\right\rangle=A_{n}^{2} \delta_{i k} \delta_{j m} \delta\left(t-t^{\prime}\right).
\tag{17}
$$

We started by checking the model for the simplest case of an ideal solution and found that
(a) composition dispersion is proportional to the squared frequency noise amplitude, $A_{n}$;
(b) fixed non-zero frequency noise amplitude in SKMF is equivalent to the averaging over certain finite number $M^{runs}$ of runs of Monte Carlo simulation, inversely proportional to the squared noise amplitude;
(c) zero noise is equivalent to the infinite number of copies in the canonical ensemble, and it is a mean-field limit of SKMF.

SKMF was used to describe the peculiarities of spinodal decomposition, nucleation, precipitation, and ordering. $^{36,43-45}$ Here, we check the applicability of the method to the phase growth and competition in reactive diffusion.

### III. APPLICATION OF SKMF TO THE MODELING OF PHASE GROWTH AND COMPETITION DURING REACTIVE DIFFUSION

In this paper, we simulate by SKMF method an interdiffusion with the formation of ordered intermediate phases in the diffusion couple consisting of two FCC-materials with the coherent interface between them. At the phase diagram, we expect 3 intermediate ordered phases—$\mathrm{A}_{3} \mathrm{B}, \mathrm{AB}_{3}$ (with ordered $\mathrm{L1}_{2}$-structure), and $\mathrm{AB}$ (with ordered $\mathrm{L1}_{0}$-structure). Our plan is the following:

1.  Construction of the phase diagram, including the equilibrium concentration steps in the couples containing the neighboring phases: $\mathrm{A}-\mathrm{A}_{3} \mathrm{B}, \mathrm{A}_{3} \mathrm{B}-\mathrm{AB}, \mathrm{AB}-\mathrm{AB}_{3}$, and $\mathrm{AB}_{3}-\mathrm{B}$.
2.  Study of single intermediate phase formation and growth kinetics in the incremental diffusion couples: a growth of $\mathrm{A}_{3} \mathrm{B}$-phase in the couple $\mathrm{A}-\mathrm{AB}$ [Fig. 1(b)], a growth of $\mathrm{AB}$ in the couple $\mathrm{A}_{3} \mathrm{B}-\mathrm{AB}_{3}$ [Fig. 1(a)], and growth of the phase $\mathrm{AB}_{3}$ in the couple $\mathrm{AB}-\mathrm{B}$. We state in advance that after averaging over some evolution details, the growth well obeys a parabolic time law, indicating that the quasi-equilibrium conditions are satisfied.
3.  Therefore, it seems natural to further study the interdiffusion within the intermediate ordered phases $\mathrm{A}_{3} \mathrm{B}, \mathrm{AB}$, and $\mathrm{AB}_{3}$. In particular, the interdiffusion coefficient inside each phase will be determined by the standard Matano method, using the concentration profiles obtained by simulation.
4.  After this, we study the competition between two intermediate phases—namely, between $\mathrm{A}_{3} \mathrm{B}$ and $\mathrm{AB}$ in the couple $\mathrm{A}-\mathrm{AB}_{3}$ [Fig. 1(c)] and between $\mathrm{AB}$ and $\mathrm{A}_{3} \mathrm{B}$ in the couple A “B-B.” In particular, we study the influence of the diffusion asymmetry $M=(V_{AA}-V_{BB})/2$ on such competition (this parameter correlates with lower and higher melting points for A and B).
5.  Finally, we study competition of all three intermediate phases $\mathrm{A}_{3} \mathrm{B}, \mathrm{AB}$ and $\mathrm{AB}_{3}$ in the diffusion couple $\mathrm{A}-\mathrm{B}$.

![](./images/812778938383204352_8.jpg)

FIG. 1. General pictures of the phase formation in the incremental diffusion couples: (a) formation of AB (two antiphase domains) between $\mathrm{A}_{3} \mathrm{B}$ and $\mathrm{AB}_{3}$, (b) formation of $\mathrm{A}_{3} \mathrm{B}$ between A and AB, (c) formation of two phase layers $\mathrm{A}_{3} \mathrm{B}$ and AB between A and $\mathrm{AB}_{3}$, (d) formation of three phase layers $\mathrm{A}_{3} \mathrm{B}, \mathrm{AB}$ and $\mathrm{AB}_{3}$ between A and B.

6. We study phase competition at (a) far stages when growth becomes parabolic but before reaching the depletion stage of the marginal materials; (b) initial stage when only one phase is growing and others are still suppressed.

7. The results of the simulation are compared with the existing phenomenological theories and hypotheses.

### A. Peculiarities of SKMF application to interdiffusion and ordering in FCC structures with an account of interactions in two coordination shells

In Ref. 46, an application of KMF to interdiffusion with ordering in BCC diffusion couple with very high concentration gradients and high diffusion asymmetry. It was found that under such conditions, the ordered B2 phase may appear first with the composition which is rather far from the stoichiometric on (50/50). This result was obtained only for the second-order transitions since KMF cannot describe the nucleation of the first-order transformations (as discussed in Sec. III).

Thus, it is natural to study the first-order transitions, including reactive diffusion, using our SKMF method. To have more distinct phases, we modified the above-described SKMF method to include the interactions in two coordination shells. So, our kinetic equations remain the same as in Eq. (15),

$$
\begin{aligned}
\frac{d C_{i}}{d t}= & -\sum_{j=1}^{Z}\left[C_{i}\left(1-C_{j}\right)\left(\Gamma_{i, j}^{\text {mean-field }}+\delta \Gamma_{i, j}^{\text {Lang }}\right)\right. \\
& \left.-C_{j}\left(1-C_{i}\right)\left(\Gamma_{j, i}^{\text {mean-field }}+\delta \Gamma_{j, i}^{\text {Lang }}\right)\right],
\end{aligned}
$$

but the energies under exponents of frequencies are now calculated in a modified way

$$
\Gamma_{i, j}^{\text {mean-field }}=\Gamma_{0} \exp \left(-\frac{\overline{E_{i, j}}}{k T}\right),\qquad(18)
$$

where the energies are calculated in the middle field approximation for the two coordination spheres

$$
\begin{aligned}
\overline{E_{i j}}= & \left(M^{I}-V^{I}\right) \sum_{l=1}^{Z^{I}=12} C_{l}+\left(M^{I}+V^{I}\right) \sum_{n=1}^{Z^{I}=12} C_{n} \\
& +\left(M^{I I}-V^{I I}\right) \sum_{l=1}^{Z^{I I}=6} C_{l}+\left(M^{I I}+V^{I I}\right) \sum_{n=1}^{Z^{I I}=6} C_{n},
\end{aligned}\qquad(19)
$$

where $V_{\alpha, \beta}^{I(I I)}(\alpha, \beta=A, B)$ pair interaction energies with $Z^{I}=12$ nearest (I) and $Z^{I I}=6$ next nearest (II) neighbors in, respectively, first and second coordination shells, $M^{I(I I)}=\left(V_{A A}^{I(I I)}-V_{B B}^{I(I I)}\right) / 2$-asymmetry parameters, $V_{A B}^{I(I I)}=V_{A B}^{I(I I)}-\left(V_{A A}^{I(I I)}+V_{B B}^{I(I I)}\right) / 2$-mixing energies, $\Gamma_{0}=v_{0} \exp \left(\frac{-E^{s}+Z^{I}\left(V_{A B}^{I}+V_{B B}^{I}\right)+Z^{I I}\left(V_{A B}^{I I}+V_{B B}^{I I}\right)}{k T}\right)$ ($v_0$-attempts frequency, $E^{S}$-saddle-point energy, taken in KMF the same for all jumps), $\delta \Gamma_{i, j}^{Lang}$-noise of jump frequency. As before, we take $\delta \Gamma_{i, j}^{Lang}=\frac{A_{n}}{\sqrt{d t}} \sqrt{3}(2 random-1)$, where $A_{n}$ is a noise amplitude, $dt$-nondimensional time step. Alternatively, we may choose the noise distribution as Gaussian with the same dispersion—it gives the same results.

### 1. Local order parameter

Binary FCC-alloy with negative mixing energy in the first coordination shell and positive mixing energy in the second coordination shell has the tendency to the ordering of $\text{L1}_2$ type or $\text{L1}_0$ type, depending on composition. In our model, we do not need to introduce order parameter field and write some special, Landau-Khalatnikov-type kinetic equations for it, since in KMF and SKMF, the order parameter $\eta$ can be always calculated from the local values of concentrations at sites belonging to different sublattices. Here, we have two problems. The first problem is that usually, we do not know in advance to what sublattice this or this site belongs. The second problem is the contradiction between the general definition of the order parameter, formulated for large crystals, containing the macroscopic number of sites,

$$
\eta=\frac{p_{A}^{I}-\tilde{C}_{A}}{1-N^{I} /\left(N^{I}+N^{I I}\right)}\qquad(20)
$$

and local character of our new-defined order parameters in the contact zone, often changing strongly from one site to the neighboring one.

According to Refs. 43 and 44, for example, for the phase $\text{L1}_2$ ($\text{A}_3\text{B}$ or $\text{AB}_3$) of FCC-lattice the local order parameter can be introduced in the following way. Minority sublattice is a simple cubic array of sites (vertexes). Majority sublattice consists of other three simple cubic sublattices forming the centers of the cube facets. Since we do not know to what simple cubic sublattice the arbitrary chosen site belongs, we should calculate four versions of the order parameter and then to choose the version with maximal absolute value

$$
\eta=\max \left(\eta_{1}, \eta_{2}, \eta_{3}, \eta_{4}\right),\qquad(21)
$$

$$
\eta_{1,2,3}=\frac{\left(C(i)+\left(e_{2,3,1}+e_{3,1,2}\right) / 4\right) / 3-(C(i)+e / 4) / 4}{4},\quad(22)
$$

$$
\eta_{4}=-4 \frac{(C(i)-(C(i)+e / 4) / 4)}{3},\qquad(23)
$$

where $e=e_1+e_2+e_3$, $e_1$, $e_2$, $e_3$-three sums, each over 4 neighboring sites in one of the planes (100), (010), (001).

We introduce some threshold value $\eta_{cr}$ of order parameter: if $\eta(i)>\eta_{cr}$, then site $i$ belongs to the ordered phase. The extent of ordering is measured as the ratio of the number of sites with overcritical order parameter to the total number of sites

$$
\xi=\sum_{1}^{\frac{1}{2}\left(N_{x} \cdot N_{y} \cdot N_{z}\right)} \theta\left(\eta-\eta_{c r}\right) / \frac{1}{2}\left(N_{x} \cdot N_{y} \cdot N_{z}\right),\qquad(24)
$$

where $\theta(x)\equiv\begin{cases} 1, x>0 \\ 0, x<0 \end{cases}$-Heaviside step function.

We will see below that the abovementioned way of description allows us to distinguish clearly the different phases to measure the position and the shift of the interphase boundaries. All this can be done substantially faster than Monte Carlo simulation.

### B. Choice of parameters: Construction of the phase diagram

#### 1. Thermodynamic mean-field model and parameters

As mentioned above, we introduced additional interactions with the second coordination shell—without this addition, the ordering in L1₀ phase would be second-order transition and also two-phase regions between phases would have too narrow concentration interval, and the intermediate phases homogeneity concentration ranges will be unrealistically broad, in comparison with typical phase diagrams Our initial choice of energies was following: $V_{AA}^I = V_{BB}^I = -10^{-21}$ J, $V_{AB}^I = -3.9 \cdot 10^{-21}$ J, $V_{AA}^{II} = V_{BB}^{II} = -8.76 \cdot 10^{-21}$ J, and $V_{AB}^{II} = -2 \cdot 10^{-21}$ J.

It is easy to construct the Gibbs free energy per atom dependence on composition for all 5 phases. For solid solutions on the basis of A and on the basis of B (actually, they are two parts of the same phase), the dependence $g(C)$ can be found just from regular solid solution model but including interactions with next-nearest neighbors

$$
\begin{aligned}
g^{disordered} &= 6\left(C_{A} \cdot V_{AA}^I + C_{B} \cdot V_{BB}^I\right) + 3\left(C_{A} \cdot V_{AA}^{II} + C_{B} \cdot V_{BB}^{II}\right) \\
&+ 12C_{A}C_{B} \cdot V_{mix}^I + 6C_{A}C_{B} \cdot V_{mix}^{II} \\
&+ kT\left((C_{A})\ln(C_{A}) + (C_{B})\ln(C_{B})\right).
\end{aligned}
\tag{25}
$$

For the ordered L1₂ phase one gets, in mean-field approximation (but also with an account of the second shell)

$$
\begin{aligned}
g^{L1_2} &= 6\left(C_{A} \cdot V_{AA}^I + C_{B} \cdot V_{BB}^I\right) + 3\left(C_{A} \cdot V_{AA}^{II} + C_{B} \cdot V_{BB}^{II}\right) + 12C_{A}C_{B} \cdot V_{mix}^I + 6C_{A}C_{B} \cdot V_{mix}^{II} + \frac{3}{4}\left(V_{mix}^I - \frac{3}{2}V_{mix}^{II}\right)\eta^2 \\
&+\frac{kT}{4}\left(
\begin{aligned}
&\left(C_{A} - 3\frac{\eta}{4}\right)\ln\left(C_{A} - 3\frac{\eta}{4}\right) + \left(C_{B} + 3\frac{\eta}{4}\right)\ln\left(C_{B} + 3\frac{\eta}{4}\right) \\
&+3\left(C_{B} - \frac{\eta}{4}\right)\ln\left(C_{B} - \frac{\eta}{4}\right) + 3\left(C_{A} + \frac{\eta}{4}\right)\ln\left(C_{A} + \frac{\eta}{4}\right)
\end{aligned}
\right).
\end{aligned}
\tag{26}
$$

For the ordered L1₀ phase one gets, also in mean-field approximation,

$$
\begin{aligned}
g^{L1_0} &= 6\left(C_{A} \cdot V_{AA}^I + C_{B} \cdot V_{BB}^I\right) + 3\left(C_{A} \cdot V_{AA}^{II} + C_{B} \cdot V_{BB}^{II}\right) + 12C_{A}C_{B} \cdot V_{mix}^I + 6C_{A}C_{B} \cdot V_{mix}^{II} + \left(V_{mix}^I - \frac{3}{2}V_{mix}^{II}\right)\eta^2 \\
&+\frac{kT}{2}\left(
\begin{aligned}
&\left(C_{A} + \frac{\eta}{2}\right)\ln\left(C_{A} + \frac{\eta}{2}\right) + \left(C_{A} - \frac{\eta}{2}\right)\ln\left(C_{A} - \frac{\eta}{2}\right) \\
&+\left(C_{B} - \frac{\eta}{2}\right)\ln\left(C_{B} - \frac{\eta}{2}\right) + \left(C_{B} + \frac{\eta}{2}\right)\ln\left(C_{B} + \frac{\eta}{2}\right)
\end{aligned}
\right).
\end{aligned}
\tag{27}
$$

#### 2. Construction of phase diagram according to common tangents rule

Naturally, in Eqs. (26) and (27), we optimize $g$ in respect to order parameter at any fixed composition. Resulting curves at some fixed temperature, together with common tangents, are demonstrated at Fig. 2.

Respectively, at Fig. 3, one can find the part of the phase diagram for the temperature interval (Tmin = 350 K, Tmax = 1350 K) built according to the common tangents rule.

![](./images/812778938383204352_9.jpg)

FIG. 2. Concentration dependences of Gibbs free energy per atom for basic solutions and for three intermediate phases at temperature T = 750 K, and the common tangents. Parameters: $V_{AA}^I = V_{BB}^I = -10^{-21}$ J, $V_{AB}^I = -3.9 \cdot 10^{-21}$ J, $V_{AA}^{II} = V_{BB}^{II} = -8.76 \cdot 10^{-21}$ J, $V_{AB}^{II} = -2 \cdot 10^{-21}$ J.

![](./images/812778938383204352_10.jpg)

FIG. 3. Dependencies T–C for the margins of the concentration ranges of all existing phases in AB system calculated by the common tangents rule.

We check the validity of the calculated equilibrium marginal concentrations within our mean-field model by the alternative method—the method of diffusion couples.

### 3. Measuring of equilibrium solubilities and concentration ranges by simulation of two-phase diffusion couples A-A₃B, A₃B-AB, AB-AB₃, and AB₃-B

We constructed two diffusion couples consisting of neighboring phases (say, A-A₃B or A₃B-B) and "annealed" them in computer experiment until reaching the final step-wise profiles, each plateau of which corresponds to the composition of one phase, which is in equilibrium with another plateau— composition of neighboring phase. As a result, at temperature 750 K, we got the concentration intervals for all three intermediate phases and for two marginal solutions—solution A(B) of B in A and solution B(A) of A in B, which are presented in Table I and compared with the results of common tangents method.

### C. Measuring of Wagner integrated diffusion coefficient $D_W = \bar{\tilde{D}} \cdot \Delta C$

Kinetics of the phase growth and competition is determined not just by the interdiffusion coefficients of the intermediate phases but by their products with concentration ranges, $\bar{\tilde{D}}_i \cdot \Delta C_i$ (Wagner diffusivities). We know that the Wagner diffusivities are, strictly speaking, the integrals over the concentration ranges of the intermediate phases $^{4,47,48}$

$$
D_W = \bar{\tilde{D}} \cdot \Delta C = \int_{C_L}^{C_R} \tilde{D}(C)dC, \tag{28}
$$

where $(C_L, C_R)$ is the equilibrium concentration range of the intermediate phase. If we construct the diffusion couple consisting of two halves with initial concentrations $C_L$, $C_R$ we may apply the Matano method for the diffusivity at composition within the mentioned concentration range

$$
\tilde{D}(C) = -\frac{1}{2t\left.\frac{dc}{dx}\right|_C} \int_{C_L}^{C} (x - x_M)dc,\ x_M = \frac{\int_{C_L}^{C_R} xdC}{C_R - C_L}. \tag{29}
$$

To calculate the Wagner diffusivity, one has to integrate the Eq. (29) once more over the concentration range

$$
D_W \equiv \int_{C_L}^{C_R} \tilde{D}(C)dC = \frac{1}{2t} \int_{x_L}^{x_R} dx \int_{C_L}^{C(x)} (x_M - x(c'))dc'. \tag{30}
$$

In numeric form, it means

$$
D_W = \frac{(dx)^2}{2t} \sum_{i=iL}^{iR-1} \sum_{j=iL}^{i+1} (iM - j)(C[j+1] - C[j]), \tag{31}
$$

where $dx = x[i+1]-x[i],\ iM \equiv \sum_{i=iL}^{iR-1} i \cdot (C[i+1] - C[i])/(C_R - C_L)$.

To avoid the disturbance of the Matano results by the simultaneous reordering process, the unary probabilities at sublattices for the initial moment is better to choose with an account of equilibrium order parameter at given temperature and composition (to have a shorter time of relaxation to the quasi-equilibrium order values during interdiffusion).

For minority sublattice, $C(i) = C_L - 3\eta_0/4$, at $iL \leqslant i < (iL + iR)/2$
and $C(i) = C_R - 3\eta_0/4$, at $(iL + iR)/2 \leqslant i < iR$.

For majority sublattice, $C(i) = C_L + \eta_0/4$, at $iL \leqslant i < (iL + iR)/2$
and $C(i) = C_R + \eta_0/4$, at $(iL + iR)/2 \leqslant i < iR$.

We arranged three diffusion couples with compositions corresponding to the marginal left and right compositions of each phase A₃B (0.737-0.754), AB (0.488-0.512), and AB₃ (0.246-0.263) at 750 K. Calculations according to Eq. (31) give the following values of $D_W = \bar{\tilde{D}} \cdot \Delta C$ for these three intermediate phases:

$$
\begin{aligned}
D_W(A_3B) &= 7.0 \cdot 10^{-14}\ \text{m}^2/\text{s},\ D_W(AB) = 7.8 \cdot 10^{-14}\ \text{m}^2/\text{s}, \\
D_W(AB_3) &= 7.0 \cdot 10^{-14}\ \text{m}^2/\text{s}.
\end{aligned}
$$

### D. The growth of single intermediate phase in the incremental couple A-AB

#### 1. Simulation of the growth by SKMF method

We start simulation of reactive diffusion with the case of A₃B phase formation and growth in the incremental diffusion couple A-AB. As we will see below, simulation results look very reasonable producing formation and growth of the almost horizontal concentration plateau with the width increasing with time according to parabolic law. Intermediate concentration profile along the diffusion direction (averaged over the planes perpendicular to this direction) is shown at Fig. 4. Two plateau of A₃B are present due to periodic boundary conditions. A-B-A-B-...

<table>
<caption>TABLE I. Comparison of boundary concentrations (mole fraction of species A) obtained by two methods—diffusion couples and common tangents rule—at the temperature 750 K. For each phase, the concentration range is representation by two marginal concentrations $C_L$ (closer to B) and $C_R$ (closer to A).</caption>
<thead>
<tr>
<th>Phase</th>
<th colspan="3">B(A)</th>
<th colspan="3">AB₃</th>
<th colspan="3">AB</th>
<th colspan="3">A₃B</th>
<th>A(B)</th>
</tr>
<tr>
<th>Concentration of A</th>
<td></td>
<td>$C_L$</td>
<td>$C_R$</td>
<td>Width of phase</td>
<td>$C_L$</td>
<td>$C_R$</td>
<td>Width of phase</td>
<td>$C_L$</td>
<td>$C_R$</td>
<td>Width of phase</td>
<td></td>
</tr>
</thead>
<tbody>
<tr>
<td>Method of diffusion couple</td>
<td>0.022</td>
<td>0.246</td>
<td>0.263</td>
<td>0.017</td>
<td>0.488</td>
<td>0.512</td>
<td>0.024</td>
<td>0.737</td>
<td>0.754</td>
<td>0.017</td>
<td>0.978</td>
</tr>
<tr>
<td>Common tangents rule</td>
<td>0.021</td>
<td>0.246</td>
<td>0.264</td>
<td>0.018</td>
<td>0.491</td>
<td>0.509</td>
<td>0.018</td>
<td>0.736</td>
<td>0.754</td>
<td>0.018</td>
<td>0.979</td>
</tr>
</tbody>
</table>

![](./images/812778938383204352_11.jpg)

FIG. 4. Concentration profile along X-axis, obtained by averaging over Y and Z ("i" counts the atomic planes.) We observe two-phase layers due to the periodic boundary condition for the thin-film system.

Roughly speaking, the volume of the ordered intermediate phase may be characterized just by the width of the plateau—if the phases form parallel layers. Yet, at least at the initial stage, the phase may grow laterally from the small island (nucleus), like in the Stranski–Krastanov model. Therefore, more correct is to characterize the phase quantity by the number of sites with the local order parameter larger than the adopted critical order value—see Eq. (24). Local order for each site was calculated according to Eqs. (22) and (23). We chose $\eta_{cr}=0.85$ as the threshold value. In the computer experiment, we were measuring the time dependences of the phase A₃B squared relative quantity $\xi^{2}(t)$. Such dependences at various temperatures are given at Fig. 5(a). They are indeed parabolic after some averaging over some "stop-and-go-like" details.

Alternatively, we try to measure the phase growth kinetics, considering composition instead of order. For phase A₃B, it means that we admit the concentration plane to belong to phase A₃B if its average concentration lies in the interval between $(0.5 + 0.75)/2 = 0.625$ and $(0.75 + 1)/2 = 0.875$. Actually, most of these planes (except the interface planes at the boundaries with neighboring phases) have an average concentration between 0.737 and 0.754 (as in Table I). Results for 750 K are shown in Fig. 5(b). One can see that the results of the two methods are practically identical.

One can see that the growth is parabolic after some coarsening procedure. In the detailed time scale this smooth growth looks like step-like. At first, we were happy to imagine that we reproduced the mode of growth with nucleation of each new atomic plane and further lateral propagation of some local 2D-nucleus. Yet, the situation looks more trivial and related to the introduction of threshold order parameter: From time to time, the criterion $\eta \geq \eta_{cr}=0.85$ becomes valid for the large group of atoms (say, whole atomic plane, due to one-dimensional diffusion front), but the value $\eta(t)$ was growing steadily simultaneously all the time. Step proceeds just in the moment of simultaneous reaching the threshold. After approximation by the standard least squares regression procedure, one gets parabolic law in the form

$$
\xi_{A_{3} B}^{2}=k_{A_{3} B} \cdot \frac{t}{d t}. \tag{32}
$$

The parabolic rate constant $k_{A_{3} B}$ satisfies (as expected) the Arrhenius law (Fig. 6)

$$
\ln \left(k_{A_{3} B}(T)\right)=-Q_{A_{3} B} \cdot \frac{1}{T}+\text { const. } \tag{33}
$$

### 2. The analytic solution for the growth of single-phase A₃B in A-AB couple

If one neglects the solubilities of A in B and B in A, and takes the concentration range of A₃B phase to be narrow, then the flux balance equations for two interface boundaries and for the intermediate phase width are following:

![](./images/812778938383204352_12.jpg)

FIG. 5. Check of parabolic phase growth: (a) the squared relative quantity of intermediate ordered phase with $\eta \geq \eta_{cr}=0.85$ vs time at various temperatures, (b) the squared relative number of atomic planes with corresponding average compositions vs time, at temperature 750 K.

![](./images/812778938383204352_13.jpg)

FIG. 6. The logarithm of the parabolic rate constant $k_{A_{3}B}$ vs inverse temperature.

$$
\begin{cases}
\left(\frac{1}{4}-0\right)\frac{dx_{L}}{dt}=-\frac{\tilde{D}\Delta C}{\Delta x} \Rightarrow \frac{dx_{L}}{dt}=-4\frac{\tilde{D}\Delta C}{\Delta x} \\
\left(\frac{1}{2}-\frac{1}{4}\right)\frac{dx_{R}}{dt}=+\frac{\tilde{D}\Delta C}{\Delta x} \Rightarrow \frac{dx_{R}}{dt}=+4\frac{\tilde{D}\Delta C}{\Delta x}
\end{cases}
\Rightarrow \Delta x^{2}=16(\tilde{D}\Delta C)^{A_{3}B}t.
\tag{34}
$$

In case of parallel layers of intermediate phases in the diffusion couple with the periodic boundary condition, its squared relative quantity is $\xi=2\Delta x/L$ so that

$$
\xi^{2}=4\frac{\Delta x^{2}}{L^{2}}=\frac{64dt}{L^{2}}(\tilde{D}\Delta C)^{A_{3}B}\frac{t}{dt}.
\tag{35}
$$

Equation (35) is a theoretical prediction under the condition of negligible solubilities. On the other hand, in simulation by SKMF, the Eq. (32) is valid. Comparing Eqs. (32) and (35), one may predict

$$
k_{1}^{A_{3}B}=(\tilde{D}\Delta C)^{A_{3}B}\frac{64dt}{L^{2}}.
\tag{36}
$$

From Eq. (36), one can estimate the Wagner integrated diffusion coefficient (Wagner diffusivity)

$$
(\tilde{D}\Delta C)^{A_{3}B}=k_{1}^{A_{3}B}\frac{L^{2}}{64dt}.
$$

Let us compare the results of our SKMF modeling and of theoretical calculations

$$
\frac{\left(N_{x}\right)^{2}dX^{2}}{64dt}k=\frac{10^{4}\cdot\left(1.25\cdot10^{-10}\right)^{2}}{64\cdot10^{-9}}\cdot3.19\cdot10^{-5}=7.8\cdot10^{-14}\ \text{m}^{2}/\text{s}.
$$

As shown in Subsection III C, direct measurement of the Wagner diffusivity by the modified Matano method gives

$$
\tilde{D}\Delta C=7.0\cdot10^{-14}\ \text{m}^{2}/\text{s}.
$$

## E. The growth of single intermediate phase AB in the couple $A_3B$-$AB_3$

### 1. Simulation of AB formation by SKMF method

We construct our diffusion couple from two ordered phases—$A_{3}B$ and $AB_{3}$. We observe the formation and growth of the ordered L1₀ phase. Characteristic concentration profile after some time is shown at Fig. 7. The existence of peak at the plateau of the new growing phase is described very well by the formation of two antiphase domains of AB-phase, and the peak corresponds to the boundary between these two antiphase domains. See also Fig. 1(a).

Again, for the coarsened time scale, the growth law is parabolic:
$\xi_{AB}^{2}=k_{AB}t/dt$.

At that, the parabolic growth rate obeys the Arrhenius law
$\ln(k_{A_{3}B}(T))=-11762/T+const.$

### 2. The analytic solution for AB growth kinetics in $A_3B$-$AB_3$ couple

Flux balance at the moving interphase boundaries gives

$$
\begin{cases}
\left(\frac{1}{2}-\frac{1}{4}\right)\frac{dx_{L}}{dt}=-\frac{\tilde{D}_{AB}\Delta c}{\Delta x} \\
\left(\frac{3}{4}-\frac{1}{2}\right)\frac{dx_{R}}{dt}=+\frac{\tilde{D}\Delta c}{\Delta x}
\end{cases}
\Rightarrow \Delta x^{2}=16(\tilde{D}_{AB}\Delta C)^{AB}t.
\tag{37}
$$

Thus, the squared relative quantity of AB phase in the couple with periodic boundary conditions (two plateaux) should depend on time according to

$$
k_{1}^{AB}=(\tilde{D}\Delta c)^{AB}\frac{64dt}{L^{2}}.
\tag{38}
$$

From Eq. (38), one can estimate the Wagner integrated diffusion coefficient (Wagner diffusivity)

$$
(\tilde{D}\Delta C)^{AB}=k_{1}^{AB}\frac{L^{2}}{64dt}.
$$

Let us compare the results of our SKMF modeling and of theoretical calculations $\frac{(N_{x})^{2}dX^{2}}{64dt}k_{1}^{AB}=7.4\cdot10^{-14}\ \text{m}^{2}/\text{s}$.

As shown in Subsection III D 2, direct measurement of the Wagner diffusivity by the modified Matano method gives $\overline{\tilde{D}}\Delta C=7.8\cdot10^{-14}\ \text{m}^{2}/\text{s}$.

Thus, SKMF method seems to be fully consistent with phenomenological theory.

![](./images/812778938383204352_14.jpg)

FIG. 7. Concentration profile, "$i$"—serial number of the atomic plane. Phase layer AB consists of two antiphase sublayers.

![](./images/812778938383204352_15.jpg)

FIG. 8. Squared relative phases A₃B and AB quantities vs time. Diffusion asymmetry parameter M = 0.

F. Growth and competition of two intermediate phases in the couple A-AB₃

1. Kinetics of simultaneous two-phase growth in the symmetric case, M = 0

Now, let us proceed with the case of two phases simultaneously trying to nucleate and grow. When interactions A-A and B-B are symmetric in both coordination shells, M = 0, the growth is indeed simultaneous and practically with the equal rate at each temperature—see Fig. 8.

2. Influence of diffusion asymmetry parameter on the competition of A₃B and AV phases at the late (parabolic) growth stage

Now, we start to play with the reduced asymmetry parameter $\tilde{M} \equiv 2M/kT = (V_{AA}^I - V_{BB}^I)/kT$ (so far we "play" only with parameters for the first coordination shell, to avoid too many regulating parameters). We will not change the $V_{AB}^I$ and will change $V_{AA}^I$, $V_{BB}^I$ symmetrically in opposite directions. If, say, M > 0, it means that the absolute value of $V_{AA}^I$ is less so that atoms A are expected to be less bonded (low-melting) and therefore, more mobile. On the other hand, high mobility of low melting component A increases compatibility of A-rich phase only if A forms the majority sublattice of the ordered phase—and it is the case for A₃B. The ratio of the phase growth rates in usual (a) and in logarithmic scales (b) as a function of diffusion asymmetry is presented at Fig. 9.

One can see that this dependence is close to exponential one

$$
k^{A_{3} B} / k^{A B} \approx \exp (4 \tilde{M})=\exp \left(4 \frac{V_{AA}^I - V_{BB}^I}{kT}\right). \tag{39}
$$

3. Suppression of A₃B-phase at the initial stage

Time of AB delay (diffusional suppression by A₃B phase) exponentially depends on the asymmetry parameter [see Fig. 10(b)].

![](./images/812778938383204352_16.jpg)

FIG. 9. Ratio of the phase growth rates in usual (a) and in logarithmic (b) scales vs reduced diffusion asymmetry parameter $\tilde{M} \equiv 2M/kT$.

![](./images/812778938383204352_17.jpg)

FIG. 10. Suppression of phase AB by A₃B: (a) delay of A₃B growth at T = 750, $\bar{M} \equiv 2M/kT = 0.7$, (b) the logarithm of A₃B suppression period vs the asymmetry parameter.

## 4. Analytic phenomenologic model of the phase competition at the late stage of parabolic growth

If one neglects the non-zero solubilities of A in B and of B in A, the concentration profile will be similar to shown in Fig. 11.
The flux balance equations give the growth equations for phase boundaries and for phase thicknesses

$$
\begin{cases}
\left(\frac{1}{4}-0\right) \frac{d x_{21}}{d t}=-\frac{D_{1} \Delta c_{1}}{\Delta x_{1}} \\
\left(\frac{1}{2}-\frac{1}{4}\right) \frac{d x_{12}}{d t}=\frac{D_{1} \Delta c_{1}}{\Delta x_{1}}-\frac{D_{2} \Delta c_{2}}{\Delta x_{2}} \\
\left(\frac{3}{4}-\frac{1}{2}\right) \frac{d x_{23}}{d t}=\frac{D_{2} \Delta c_{2}}{\Delta x_{2}}
\end{cases} \Rightarrow
\begin{cases}
\frac{d \Delta x_{1}}{d t}=8 \frac{D_{1} \Delta c_{1}}{\Delta x_{1}}-4 \frac{D_{2} \Delta c_{2}}{\Delta x_{2}} \\
\frac{d \Delta x_{2}}{d t}=-4 \frac{D_{1} \Delta c_{1}}{\Delta x_{1}}+8 \frac{D_{2} \Delta c_{2}}{\Delta x_{2}}.
\end{cases}
\tag{40}
$$

Equations (40) have a parabolic solution,

$$\Delta x_{1}=\beta_{1} \sqrt{t}, \Delta x_{2}=\beta_{2} \sqrt{t}, D_{i} \Delta c_{i} \equiv D_{W i},$$

$$
\frac{\beta_{1}}{\beta_{2}}=\frac{\left(\frac{D_{W 1}}{D_{W 2}}-1\right) \pm \sqrt{\left(\frac{D_{W 1}}{D_{W 2}}-1\right)^{2}+16 \frac{D_{W 1}}{D_{W 2}}}}{4} \equiv z,
\tag{41}
$$

$$\beta_{1}=\sqrt{16 D_{W 1}-8 D_{W 2} z}, \beta_{2}=\sqrt{16 D_{W 2}-8 D_{W 1} z}.$$

![](./images/812778938383204352_18.jpg)

FIG. 11. Schematic concentration profile in A–AB₃ couple with growing phase layers of A₃B and AB.

## 5. Comparison of analytics and SKMF model for two competing phases

### a. Symmetric case (asymmetry parameter M=0).
Let us substitute Wagner diffusivities into Eq. (40) and compare results with Subsection III E 2. In our case, $\beta_{1}$ corresponds to A₃B, and $\beta_{2}-$ to AB. According to Subsections III C and III D 2 $D_{W 1}=7.0 \cdot 10^{-14} \mathrm{~m}^{2} / \mathrm{s}$, $D_{W 2}=7.8 \cdot 10^{-14} \mathrm{~m}^{2} / \mathrm{s}$. Substitute these data into Eq. (40) and get

![](./images/812778938383204352_19.jpg)

FIG. 12. Dependence $\ln(\tau)$ on $\tilde{M} \equiv 2M/kT$ (symmetrically— for positive M).

$$
\frac{\beta_{1}}{\beta_{2}}=\frac{\left(\frac{7.0}{7.8}-1\right)+\sqrt{\left(\frac{7.0}{7.8}-1\right)^{2}+16 \cdot \frac{7.0}{7.8}}}{4}=0.92.
$$

On the other hand, according to SKMF simulations [Fig. 10(a)], $\beta_{1}/\beta_{2} \equiv k^{A_{3}B}/k^{AB}$ is equal to 0.98. We see that correspondence is good.

b. Asymmetric case. Now we try to understand the origin of the empirical rule [Eq. (39)]. Let us compare energetics of A–B exchanges in ideally stoichiometric $A_3B$ phase L1₂ and in ideally stoichiometric AB phase L1₀. Let us consider only the energies within the first coordination shell (since in our simulations we did not vary the energies in the second coordination shell). Then, the energetic barrier for A–B exchange in ideal L1₂ structure is

$$
\begin{aligned}
Q(A_{3} B) & =E^{s}-\left(E_{A}[i]+E_{B}[i n]\right) \approx E^{s}-\left(\left(8 V_{A A}+4 V_{A B}\right)+\left(12 V_{B A}\right)\right) \\
& =E^{s}-\left(8 V_{A A}+16 V_{A B}\right).
\end{aligned}
$$

<table>
<caption>TABLE II. Dependence of suppression time on the reduced asymmetry parameter $\tilde{M} \equiv 2M/kT$.</caption>
<thead>
<tr>
<th>$\tilde{M}$</th>
<th>$\ln(\tau)$</th>
<th>$\tilde{M}$</th>
<th>$\ln(\tau)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>—1.0</td>
<td>10.38</td>
<td>1.0</td>
<td>11.10</td>
</tr>
<tr>
<td>—0.9</td>
<td>9.92</td>
<td>0.9</td>
<td>9.77</td>
</tr>
<tr>
<td>—0.8</td>
<td>9.88</td>
<td>0.8</td>
<td>9.63</td>
</tr>
<tr>
<td>—0.7</td>
<td>9.16</td>
<td>0.7</td>
<td>9.21</td>
</tr>
<tr>
<td>—0.6</td>
<td>8.68</td>
<td>0.6</td>
<td>8.89</td>
</tr>
</tbody>
</table>

The energetic barrier for A–B exchange in ideal L1₀ structure is
$$
\begin{aligned}
Q(A B) & =E^{s}-\left(E_{A}[i]+E_{B}[i n]\right) \\
& \approx E^{s}-\left(\left(4 V_{A A}+8 V_{A B}\right)+\left(4 V_{B B}+8 V_{B A}\right)\right) \\
& =E^{s}-\left(4 V_{A A}+16 V_{A B}+4 V_{B B}\right).
\end{aligned}
$$

Then,
$$
\begin{aligned}
Q(A_{3} B)-Q(A B) & \approx-\left(8 V_{A A}+16 V_{A B}\right)+\left(4 V_{A A}+16 V_{A B}+4 V_{B B}\right) \\
& =-4\left(V_{A A}-V_{B B}\right).
\end{aligned}
$$

Thus, in strongly asymmetric case
$$
\begin{aligned}
\frac{k\left(A_{3} B\right)}{k(A B)} & \approx \frac{D_{W 1}}{D_{W 2}} \approx \exp \left(-\frac{Q\left(A_{3} B\right)-Q(A B)}{k T}\right) \\
& \approx \exp \left(4 \frac{V_{A A}-V_{B B}}{k T}\right)=\exp (4 \tilde{M}).
\end{aligned}
$$

It corresponds to Eq. (39) quite well.

## G. Phase growth and competition in full couple A-B with three intermediate phases
### Flux balances and growth rates

$$
\left\{
\begin{aligned}
\left(\frac{1}{4}-0\right)\frac{dx_{21}}{dt} &= -\frac{D_{W1}}{\Delta x_1} \\
\left(\frac{1}{2}-\frac{1}{4}\right)\frac{dx_{12}}{dt} &= \frac{D_{W1}d_1}{\Delta x_1} - \frac{D_{W2}}{\Delta x_2} \\
\left(\frac{3}{4}-\frac{1}{2}\right)\frac{dx_{23}}{dt} &= \frac{D_{W2}}{\Delta x_2} - \frac{D_{W3}}{\Delta x_3} \\
\left(1-\frac{3}{4}\right)\frac{dx_{3\beta}}{dt} &= \frac{D_{W3}}{\Delta x_3}
\end{aligned}
\right.
\Rightarrow
\left\{
\begin{aligned}
\frac{d\Delta x_1}{dt} &= 8\frac{D_{W1}}{\Delta x_1} - 4\frac{D_{W2}}{\Delta x_2} \\
\frac{d\Delta x_2}{dt} &= -4\frac{D_{W1}}{\Delta x_1} + 8\frac{D_{W2}}{\Delta x_2} - 4\frac{D_{W3}}{\Delta x_3} \\
\frac{d\Delta x_3}{dt} &= -4\frac{D_{W2}}{\Delta x_2} + 8\frac{D_{W3}}{\Delta x_3}
\end{aligned}
\right.
$$

![](./images/812778938383204352_20.jpg)
![](./images/812778938383204352_21.jpg)

FIG. 13. The ratio of parabolic rate constants $k^{\text{A}_3\text{B}}/k^{\text{AB}_3}$ (a) and their logarithms (b) as the functions of the reduced asymmetry parameter $\tilde{M} \equiv 2M/kT$ and the approximation by an exponential (a) or linear (b) dependences.

If $M = 0$, then $D_{W3} = D_{W1} \Rightarrow \Delta x_3 = \Delta x_1$; therefore,
$$
\begin{cases}
\frac{d\Delta x_1}{dt} = 8\frac{D_{W1}}{\Delta x_1} - 4\frac{D_{W2}}{\Delta x_2}, \\
\frac{d\Delta x_2}{dt} = -8\frac{D_{W1}}{\Delta x_1} + 8\frac{D_{W2}}{\Delta x_2}.
\end{cases} \tag{42}
$$

The parabolic solution of this set of equations gives the following prediction at $M = 0$:
$$
\frac{\Delta x_2}{\Delta x_1} = -\frac{1}{2}\left(1 - \frac{1}{2}\frac{D_{W2}}{D_{W1}}\right) + \sqrt{\frac{1}{4}\left(1 - \frac{1}{2}\frac{D_{W2}}{D_{W1}}\right)^2 + \frac{D_{W2}}{D_{W1}}}. \tag{43}
$$

In particular, at $D_{W2}/D_{W1} \approx 1$, it gives $\Delta x_2/\Delta x_1 \approx 0.78$.

Similar to the competition of two phases, in this case of three competing phases, the influence of diffusion asymmetry is clearly seen at the initial stage. Contrary to the previous case, phase AB is always suppressed at the initial stage—by $\text{A}_3\text{B}$ or by $\text{AB}_3$, depending on the sign of asymmetry. Time of suppression, again, exponentially depends on asymmetry (Fig. 12). For positive M, the dependence is almost symmetric (see Table II).

For the stage of simultaneous growth, the ratio of parabolic constants is presented at Fig. 13 as the functions of $2M/kT$.

## IV. CONCLUSIONS
1. Martin's kinetic mean-field (KMF) model and its 3D modification may lead only to the decrease of free energy (or constant free energy in equilibrium). Proof of this property has a structure similar to Boltzmann H-theorem. Thus, KMF cannot provide the first-order transformations with overcoming the nucleation barrier.
2. Adding the frequency noise (instead of concentration noise) and transition to SKMF improves this flaw and gives a reasonable description of the first-order transitions.
3. SKMF model allows us to model (using even very limited computational resources) the growth and competition of one, two, three intermediate phase layers in the process of reactive diffusion.
4. The results of SKMF simulations fully correlate with phenomenological theory of reactive diffusion at the growth stage. Moreover, it predicts the temporal suppression of some phases and the exponential influence of the diffusion asymmetry parameter on the suppression time at the initial stage.
5. Our next step will be the check of the theories of intermediate phases nucleation in the sharp concentration gradients.
6. SKMF might also be a proper tool to check the alternative theories of nucleation. $^{49,50}$

## ACKNOWLEDGMENTS
This work was supported by the Marie Curie International Research Staff Exchange Scheme Fellowship within the 7th European Community Framework Programme under Grant No. 612552 and also by the Ministry of Education and Science of Ukraine.

The authors are grateful to George Martin, Zoltan Erdelyi, Rafal Kozubski, and Helen Zapolsky for fruitful discussions.

REFERENCES

¹K. N. Tu, *Solder Joint Technology* (Springer, New York, 2007), p. 327.
²P. Glensdorf and I. Prigogine, *Thermodynamic Theory of Structure, Stability and Fluctuations* (Mir, Moscow, USSR, 1973).
³W. Ostwald, Z. Phys. Chem. **22(1)**, 289 (1897).
⁴J. W. P. Schmelzer and A. S. Abyzov, “How do crystals nucleate and grow: Ostwald’s rule of stages and beyond,” in *Thermal Physics and Thermal Analysis* (Springer, Cham, 2017), pp. 195–211.
⁵J. W. Schmelzer, G. S. Boltachev, and V. G. Baidakov, J. Chem. Phys. **124(19)**, 194503 (2006).
⁶J. W. Schmelzer and A. S. Abyzov, J. Non-Cryst. Solids **501**, 11–20 (2018).
⁷J. M. Poate, K. N. Tu, and J. W. Mayer, *Thin Films: Interdiffusion and Reactions* (John Wiley & Sons, New Jersey, USA, 1978).
⁸F. M. d’Heurle and P. Gas, J. Mater. Res. **1(1)**, 205 (1986).
⁹M. Van Rossum, M. A. Nicolet, and W. L. Johnson, Phys. Rev. B **29(10)**, 5498 (1984).
¹⁰B. M. Clemens, W. L. Johnson, and R. B. Schwarz, J. Non-Cryst. Solids **61**, 817 (1984).
¹¹C. Oberdorfer, S. M. Eich, and G. Schmitz, *Ultramicroscopy* **128**, 55 (2013).
¹²C. B. Ene, G. Schmitz, T. Al-Kassab, and R. Kirchheim, *Ultramicroscopy* **107(9)**, 802 (2007).
¹³Y. Geguzin, Y. S. Kaganovski, L. M. Paritskaya, and V. I. Solunskiy, Phys. Met. Metallogr. **47(4)**, 821 (1980) (in Russian).
¹⁴Ya. E. Geguzin, *Diffusion Zone* (Nauka, Moscow, USSR, 1979).
¹⁵U. Gösele and K. N. Tu, J. Appl. Phys. **53(4)**, 3252 (1982).
¹⁶A. M. Gusak and K. P. Gurov, Phys. Met. Metallogr. **53(5)**, 842 (1982).
¹⁷A. M. Gusak and K. P. Gurov, Izv. Acad. Sci. U.S.S.R. Met. **53(1)**, 163 (1990).
¹⁸A. M. Gusak and A. V. Nazarov, J. Phys.: Condens. Matter **4(20)**, 4753 (1992).
¹⁹A. M. Gusak and G. V. Lucenko, *Acta Mater.* **46(10)**, 3343 (1998).
²⁰P. J. Desre and A. R. Yavari, Phys. Rev. Lett. **64(13)**, 1533 (1990).
²¹P. J. Desre, *Acta Metall. Mater.* **39(10)**, 2309 (1991).
²²F. Hodaj and P. J. Desre, *Acta Mater.* **44(11)**, 4485 (1996).
²³A. M. Gusak, Ukr. J. Phys. **35(5)**, 725 (1990); A. M. Gusak, O. V. Dubiy, and S. V. Kornienko, ibid. **36**, 286 (1991); A. Gusak, Y. A. Lyashenko, and A. O. Bogatyrev, *Defect Diffus. Forum* **129**, 95 (1996).
²⁴A. M. Gusak and K. P. Gurov, *Solid State Phenom.* **23-24**, 117 (1992).
²⁵F. Hodaj, A. M. Gusak, and P. J. Desre, *Philos. Mag. A* **77(6)**, 1471 (1998).

²⁶A. M. Gusak, F. Hodaj, and A. O. Bogatyrev, J. Phys.: Condens. Matter **13(12)**, 2767 (2001).
²⁷F. Hodaj and A. M. Gusak, *Acta Mater.* **52(14)**, 4305 (2004).
²⁸A. M. Gusak, F. Hodaj, and G. Schmitz, *Philos. Mag. Lett.* **91(9)**, 610 (2011).
²⁹J. H. Perepezko, J. S. Park, K. Landry, H. Sieber, M. H. da Silva Bassani, and A. S. Edelstein, *MRS Online Proc. Libr. Arch.* **1997**, 481.
³⁰J. H. Perepezko, M. H. da Silva Bassani, J. S. Park, A. S. Edelstein, and R. K. Everett, *Mater. Sci. Eng.: A* **195**, 1 (1995).
³¹M. O. Pasichnyy, G. Schmitz, A. M. Gusak, and V. Vovk, Phys. Rev. B **72(1)**, 014118 (2005).
³²M. Ibrahim, Z. Balogh, P. Stender, R. Schlesiger, G. H. Greiwe, G. Schmitz, and Z. Erdélyi, *Acta Mater.* **76**, 306 (2014).
³³B. Parditka, J. Toman, C. Cserhati, Z. Jánosfalvi, A. Csik, I. Zizak, and Z. Erdelyi, *Acta Mater.* **87**, 111 (2015).
³⁴P. Swaminathan, M. D. Grapes, K. Woll, S. C. Barron, D. A. LaVan, and T. P. Weihs, J. Appl. Phys. **113(14)**, 143509 (2013).
³⁵P. Yi, M. L. Falk, and T. P. Weihs, J. Appl. Phys. **124(16)**, 165303 (2018).
³⁶Z. Erdélyi, M. Pasichnyy, V. Bezpalchuk, J. J. Tomán, B. Gajdics, and A. M. Gusak, *Comput. Phys. Commun.* **204**, 31 (2016).
³⁷G. Martin, Phys. Rev. B **41(4)**, 2279 (1990).
³⁸Z. Erdélyi, I. A. Szabó, and D. L. Beke, *Phys. Rev. Lett.* **89(16)**, 165901 (2002).
³⁹Z. Erdélyi, M. Sladecek, L. M. Stadler, I. Zizak, G. A. Langer, M. Kis-Varga, D. L. Beke, and B. Sepiol, *Science* **306**, 1913 (2004).
⁴⁰N. V. Storozhuk, K. V. Sopiga, and A. M. Gusak, *Philos. Mag.* **93(16)**, 1999 (2013).
⁴¹Y. Wang, L. Chen, and A. Khachaturyan, “Solid-solid phase transformation,” in *PTM’94*, edited by W. C. Jonhsons, J. M. Howe, D. E. Laughlin, and W. A. Soffa (The Minerals, Metals, Materials, Society, 1994), p. 245, ISBN: 0-87339-278-7.
⁴²Y. Wang, D. Banerjee, C. C. Su, and A. G. Khachaturyan, *Acta Mater.* **46(9)**, 2983 (1998).
⁴³V. M. Bezpalchuk, A. M. Gusak, and R. Kozubski, *Uspehi Fiz. Met.* **18(3)**, 205 (2017).
⁴⁴V. Bezpalchuk, R. Kozubski, M. Pasichnyy, and A. Gusak, *Defect Diffus. Forum* **383**, 59 (2018).
⁴⁵B. D. Gajdics, J. J. Tomán, F. Misják, G. Radnóczi, and Z. Erdélyi, *Defect Diffus. Forum* **383**, 89 (2018).
⁴⁶Z. Erdélyi, D. L. Beke, and A. Taranovskyy, *Appl. Phys. Lett.* **92(13)**, 133110 (2008).
⁴⁷C. Wagner, *Acta Metall.* **17(2)**, 99 (1969).
⁴⁸F. J. J. Van Loo, M. R. Rijnders, K. J. Rönkä, J. H. Gülpen, and A. A. Kodentsov, *Solid State Ionics* **95(1-2)**, 95 (1997).
⁴⁹A. S. Abyzov and J. W. Schmelzer, J. Non-Cryst. Solids **384**, 8 (2014).
⁵⁰J. W. Schmelzer, A. S. Abyzov, and J. Möller, J. Chem. Phys. **121(14)**, 6900 (2004).

J. Chem. Phys. **150**, 174109 (2019); doi: 10.1063/1.5086046
Published under license by AIP Publishing

150, 174109-15