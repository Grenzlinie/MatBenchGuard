
# Relaxation dynamics in the energy landscape of glass-forming liquids

Yoshihiko Nishikawa, \( ^{1} \)  Misaki Ozawa, \( ^{2} \)  Atsushi Ikeda, \( ^{3} \)  Pinaki Chaudhuri, \( ^{4} \)  and Ludovic Berthier \( ^{1,5} \) 

 \( ^{1} \)  Laboratoire Charles Coulomb (L2C), Université de Montpellier, CNRS, 34095 Montpellier, France

 \( ^{2} \)  Laboratoire de Physique de l'Ecole normale supérieure,

ENS, Université PSL, CNRS, Sorbonne Université,

Université Paris-Diderot, Sorbonne Paris Cité, Paris, France

 \( ^{3} \)  Graduate School of Arts and Sciences, The University of Tokyo, Tokyo 153-8902, Japan

 \( ^{4} \)  The Institute of Mathematical Sciences, C.I.T. Campus, Taramani, Chennai 600 113, India

 \( ^{5} \)  Yusuf Hamied Department of Chemistry, University of Cambridge, Lensfield Road, Cambridge CB2 1EW, United Kingdom

(Dated: April 7, 2022)

We numerically study the zero-temperature relaxation dynamics of several glass-forming models to their inherent structures, following quenches from equilibrium configurations sampled across a wide range of initial temperatures. In a mean-field Mari-Kurchan model, we find that relaxation changes from a power-law to an exponential decay below a well-defined temperature, consistent with recent findings in mean-field p-spin models. By contrast, for finite-dimensional systems, the relaxation is always algebraic, with a non-trivial universal exponent at high temperatures crossing over to a harmonic value at low temperatures. We demonstrate that this apparent evolution is controlled by a temperature-dependent population of localised glassy excitations. Our work unifies several recent lines of studies aiming at a detailed characterisation of the complex potential energy landscape of glass-formers, and challenges both mean-field and real space descriptions of glasses.

## I. INTRODUCTION

Many systems of scientific interest are described as 'complex', even though definitions of complexity may vary across scientific fields  \( [1] \) . For many-body interacting systems, the potential energy landscape,  \( E(\{\boldsymbol{r}\}) \) , which describes the potential energy E of the system as a function of the complete set of coordinates  \( \{\boldsymbol{r}\} \)  of its constituents, has become a central object of study  \( [2, 3] \) . It serves both empirical goals, for instance to picture the dynamic evolution of a system in a 'rugged' landscape  \( [4] \) , but can also be described mathematically very precisely  \( [2, 5, 6] \) . The detailed characterisation and dynamic exploration of complex potential energy landscapes are important problems for amorphous materials  \( [4, 7, 8] \) , optimisation problems  \( [9] \) , machine learning algorithms  \( [10, 11] \) , and other disordered systems  \( [12] \) .

Since the work of Goldstein [13], the physics of glassy systems is often described in terms of the properties of their potential energy landscapes. The large number of energy minima connected by complex dynamic pathways is typically invoked in introductory lectures about amorphous media [4], and the sketch of complex energy landscapes very often accompanies the interpretation of experimental measurements [14], which makes this object more than a pure theoretical curiosity. Analytically, the properties of the potential energy landscape of glass-forming models have been studied extensively at the mean-field level through the analysis of fully-connected disordered spin models, such as p-spin models. In this limit, the phase space can be divided into long-lived metastable states (or, pure states), and both free-energy and energy landscapes can be studied in great detail, thus providing a firm relation between the landscape structure and the thermodynamics and dynamics of the system [5, 6, 15]. Current efforts in this area concern the analysis of dynamic pathways [16], or corrections to mean-field [17].

In finite dimensions, the study of energy minima, or inherent structures, first gained momentum when Stillinger and Weber transformed Goldstein's ideas into concrete tools to both explore and exploit the potential energy landscape of glasses  \( [4, 18] \) . A key step is the tiling of the equilibrium configuration space, pertinent to describe physical properties, into basins of attraction surrounding energy minima. It is this mapping which putatively connects the thermodynamic and dynamic properties of glass-formers to the topography of their potential energy landscape, although the relevance of such an approach has often been debated  \( [19, 20] \) , because the pure states defined in the mean-field limit do not exist in finite dimensions  \( [21] \) . The analysis of energy minima has been used to estimate the configurational entropy  \( [7] \) , while saddle points were discussed in connection with the dynamic mode-coupling crossover  \( [22–25] \) . However, these approaches do not have the same level of rigour as those in p-spin models since inherent structures are different from pure states  \( [21, 26, 27] \) : inherent structures are configurations that are energetically stable against infinitesimal particle moves whereas the pure states are defined as free energy minima. The structure of the potential energy landscape and its precise relationship with dynamics and thermodynamics remain under intense scrutiny  \( [8, 28] \) . In particular, the role of excitations in the potential energy landscape has been discussed in connection with sound propagation  \( [29] \) , specific heat  \( [30] \) , vibrational  \( [31] \)  and mechanical properties  \( [32] \) .

Virtually all studies of glassy landscapes start by ‘instantaneously’ relaxing configurations to the ‘nearest’ energy minimum, following known numerical recipes  \( [33] \) .
 

Strangely, however, only few studies have been dedicated to the physical processes at play during the energy minimization itself  \( [34–40] \) . In our view, this represents an important vacuum because this relaxation dynamics in fact provides a convenient way to navigate the potential energy landscape, explore its geometry and the nature as well as interactions between excitations that are relevant to describe glassy materials. Suppose for instance that the landscape is simple and smooth. Using steepest descent dynamics, the system should then settle in an inherent structure very quickly while, on a rugged landscape, the system meanders and crosses many saddles during relaxation  \( [41] \) . Similarly, the steepest descent dynamics obtained within kinetically constrained lattice models simply stems from a non-interacting set of excited defects and is therefore unremarkable  \( [19, 42] \) . Thus, in the context of glassy systems, the steepest descent dynamics probes the detailed structure of the potential energy landscape, potentially illuminates its connection to the physical dynamics, and provides novel constraints on physical descriptions of glassy excitations.

Recently, the analysis of steepest descent in mixed mean-field p-spin glass models revealed the existence of two important characteristic temperatures [35]. First, starting from initial states prepared at high temperatures T, the energy density of the final inherent state is constant for  \( T > T_{onset} \) , and it decreases with decreasing T when  \( T \leq T_{onset} \) . This sharp onset temperature does not affect the relaxation dynamics itself which obeys a nontrivial power-law time dependence as long as  \( T \geq T_{SF} \) . By contrast, the decay is exponentially fast below  \( T_{SF} \)  (initials stand for 'State Following'). This implies that the system is always close to an energy minimum for  \( T \leq T_{SF} \)  in which it converges very quickly by steepest descent. The critical temperature  \( T_{SF} < T_{onset} \)  also reflects a change in the structure of the potential energy landscape, as inherent states have a marginal density of states above  \( T_{SF} \) , which becomes gapped below. Within p-spin models, these two characteristic temperatures are unrelated to the equilibrium dynamics, which becomes non-ergodic at the mode-coupling temperature  \( T_{MCT} \) , distinct from both  \( T_{SF} \)  and  \( T_{onset} \) , showing that even at mean-field level free-energy and energy landscapes are different objects.

In numerical studies, the relaxation dynamics in D = 2 and 3 (D is the space dimension) harmonic spheres just above jamming was recently studied starting from high temperatures including random configurations at  \( T = \infty \)  [34], and a power-law time decay was found with a non-trivial, dimension-dependent exponent. Another recent work [36] explores the statistics of single particle displacements between initial and final configurations in several three-dimensional models and reports the existence of a crossover temperature separating high- from low-temperature behaviours. These interesting studies do not provide a complete physical picture of the relaxation dynamics towards energy minima, neither do they assess the existence of the critical temperature  \( T_{SF} \)  found in mean-field approaches. The universality of the power-law time dependence found near jamming across models, and even the effect of spatial dimension and initial temperatures were not fully elucidated, either.

Here, we provide a comprehensive numerical study of the steepest descent dynamics in generic glass-forming liquids. We address its dimensionality, universality, and initial stability dependences by studying a mean-field Mari-Kurchan model and three finite-dimensional models in two, three, four, and eight dimensions using a wide range of initial states obtained through the swap Monte-Carlo algorithm. We numerically detect the predicted mean-field transition at  \( T_{SF} \)  in the Mari-Kurchan model. However, the transition is absent in all finite dimensional models, where it is replaced by a smooth temperature evolution between two non-trivial limits that we analyse in detail. We show that this crossover is controlled by a finite population of localised defects where particle rearrangements take place during the minimisation, with the overall concentration of these defects decreasing at lower temperatures. Therefore, finite dimensional glass-forming systems at finite temperatures cannot be seen as inherent structures excited by small thermal fluctuations, since they are neither described by mean-field energy landscapes nor by a simple picture of non-interacting localised defects. Our results provide a complete picture of the relaxation dynamics in glassy landscapes, and illuminate the role, nature and interactions of localised defects in finite-dimensional structural glasses.

## II. RESULTS

## A. Steepest descent dynamics

We numerically solve the equations of motion of steepest descent dynamics,

 \[ \zeta\frac{\mathrm{d}\boldsymbol{r}_{i}}{\mathrm{d}t}=-\frac{\partial E}{\partial\boldsymbol{r}_{i}}, \quad (1) \] 

starting at time t = 0 from an equilibrium configuration prepared at initial temperature T, where  \( \zeta \)  is the damping coefficient and E is the potential energy. The time unit is  \( \tau_{0} = \zeta \ell^{2} / v_{0} \) , where  \( \ell \)  is the unit length scale, and  \( v_{0} \)  is the unit energy for particle interactions. In Eq. (1), energy is dissipated via a uniform background. We have not tested more complicated dissipation mechanisms such as used in dense particle suspensions [43]. Note that the dynamics in Eq. (1) is fully athermal (there is no noise term) and the temperature T that we vary only controls the Boltzmann distribution from which initial conditions for the dynamics are drawn.

We monitor the mean energy  \( \langle E(t)\rangle \)  and the root mean squared velocity,

 \[ \langle|\boldsymbol{v}(t)|\rangle=\left\langle\sqrt{\frac{1}{N}\sum_{i}\left|\frac{\mathrm{d}\boldsymbol{r}_{i}}{\mathrm{d}t}\right|^{2}}\right\rangle, \quad (2) \]
 

during the relaxation dynamics, where the brackets represent an average over initial equilibrium configurations, and N is the number of particles. We define an exponent  \( \beta \)  for the time decay [34] as

 \[ \langle|\boldsymbol{v}(t)|\rangle\sim t^{-\beta}. \quad (3) \] 

For the dynamics in Eq. (1), the energy decay is exactly related to the velocity decay as  \( \frac{1}{N}\frac{\mathrm{d}}{\mathrm{d}t}\langle E(t)\rangle=-\zeta\langle|\boldsymbol{v}(t)|^{2}\rangle \) . As a result, the energy decay can be expressed using the same exponent:  \( \langle E(t)-E(t\to\infty)\rangle\sim t^{-(2\beta-1)} \) . Therefore, we focus on the velocity relaxation and Eq. (3).

We consider several structural glass models in various dimensions and interaction potentials over a wide range of preparation temperatures. We study a soft sphere version of the mean-field Mari-Kurchan model  \( [44] \) , polydisperse soft sphere models in two  \( [45] \)  and three dimensions  \( [46] \) , harmonic spheres  \( [47] \)  in two, three, four, and eight dimensions, and the Kob-Andersen model  \( [48] \)  for two and three dimensions. Note that soft sphere models have a steep repulsive interaction with an  \( r^{-12} \)  core and a short cutoff (we have checked that extremely few rattler particles  \( [49] \)  are found in the corresponding inherent structures), whereas the harmonic potential models have a very soft core, which may affect the  \( T \rightarrow \infty \)  limit for initial conditions. The Kob-Andersen model uses the Lennard-Jones potential with a steep repulsive core and attractive forces at larger distances.

To prepare equilibrium configurations in a wide range of temperatures, we use the planting method  \( [50] \)  for the Mari-Kurchan model and the swap Monte-Carlo algorithm  \( [46] \)  for some of the finite-dimensional systems, which should allow us to detect any of the putative transitions predicted from mean-field landscapes. Further details about the models and simulation protocols are provided in Appendix A and Supplemental Material  \( [51] \) .

## B. Mean-field Mari-Kurchan model

Thanks to its mean-field nature, we can apply the replica liquid theory to the Mari-Kurchan model, as detailed in SI, and obtain the dynamical mode-coupling transition temperature:  \( T_{MCT} \simeq 0.0084 \) . We also studied the equilibrium dynamics using a simple Metropolis algorithm, and find that the theoretical estimate of  \( T_{MCT} \)  describes the numerical data reasonably well. This study allows us to also estimate the onset temperature for slow dynamics:  \( T_{onset} \simeq 0.015 \) .

We study the steepest descent starting from equilibrium configurations in the range  \( T \in [0.0001, 0.015] \) . Figure 1 shows the velocity decay  \( \langle |\pmb{v}(t)| \rangle \)  for various temperatures and system sizes. Figure 1(a) shows that the relaxation dynamics strongly depends on initial equilibrium temperature. For high temperatures,  \( T \gtrsim 0.006 \) ,  \( \langle |\pmb{v}(t)| \rangle \)  follows a clear power-law decay with an exponent that we estimate as  \( \beta \simeq 0.75 \) . In a finite size system, this power law decay is interrupted at long times. On the other hand, at low temperatures, an exponential decay

![](./images/867745664589627861_1.jpg)

![](./images/867745664589627861_2.jpg)

FIG. 1. (a) Velocity  \( \langle|\pmb{v}(t)|\rangle \)  as a function of time t in the Mari-Kurchan soft-sphere model at several temperatures with N = 16384. (b) Velocity decay at two selected initial equilibrium temperatures and several system sizes. The dashed line indicates  \( \beta = 0.75 \) .

occurs. These results suggest that the high and low temperature relaxation dynamics are qualitatively different, and are separated by a critical temperature.

To fully confirm the distinct occurrence of power-law and exponential decays, we analyse finite-size effects. In Fig. 1(b), we show the velocity  \( \langle|\pmb{v}(t)|\rangle \)  for several system sizes at two selected temperatures. At high initial temperature  \( T = 0.015 \) ,  \( \langle|\pmb{v}|\rangle \)  has a strong system-size dependence. Larger systems take longer times to reach energy minima and follow the power-law decay with  \( \beta \simeq 0.75 \)  over a broader time window. The system-size dependence suggests that in the thermodynamic limit,  \( N \to \infty \) , the velocity decay has a genuine power-law behaviour with a diverging time scale. At very low initial temperature, T = 0.0001 instead, the velocity decay has almost no system-size dependence, implying that the time to reach energy minima remains finite in the thermodynamic limit, confirming the exponential decay.

Therefore, in the initial temperature regime between 0.0001 and 0.006, the Mari-Kurchan model displays a transition characterising the nature of the relaxation dynamics akin to the behaviour reported at the temperature  \( T_{SF} \)  discussed in p-spin models. Interestingly, for the MK model, the  \( T_{SF} \)  is noticeably smaller than the estimated  \( T_{MCT} \approx 0.0084 \) , confirming that these two temperatures
 
![](./images/867745664589627861_3.jpg)

![](./images/867745664589627861_4.jpg)

![](./images/867745664589627861_5.jpg)

![](./images/867745664589627861_6.jpg)

![](./images/867745664589627861_7.jpg)

![](./images/867745664589627861_8.jpg)

FIG. 2. The velocity  \( \langle|\boldsymbol{v}(t)|\rangle \)  as a function of time t for the harmonic spheres in two, three, four, and eight dimensions (a), the three-dimensional soft-spheres (b), the Kob-Andersen Lennard-Jones model (c), the two-dimensional harmonic spheres (d), the soft spheres (e), and the Kob-Andersen Lennard-Jones model (f). In (a), the number of particles is N = 64000 for D = 2, N = 65536 for D = 3 and D = 4, and N = 16384 for D = 8 (data are shifted vertically for clarity). In (b), (d), (e), and (f), N = 96000, 64000, 64000 and 125000, respectively. In (c), N = 27135 at T = 0.37 and N = 76800 for other temperatures.

should be distinguished (they are equal in some versions of p-spin models).

While the existence of the transition is compatible with results for the mixed p-spin glass model, the decay exponent  \( \beta\simeq0.75 \)  at high temperatures observed for the Mari-Kurchan model differs slightly from the spin glass model where  \( \beta\simeq0.83 \)  [52], or the random Lorentz gas in  \( d\to\infty \)  where  \( \beta\approx1 \)  [40]. A broader class of mean-field models and even more extensive numerics should be explored to settle the relevance of this small difference.

## C. Finite-dimensional models

For finite D systems, we first consider the relaxation dynamics starting from the high-temperature limit,  \( T \rightarrow \infty \) , in various models and spatial dimensions. Figure 2(a) shows the results for monodisperse harmonic spheres in dimensions D = 2, 3, 4, and 8. In all dimensions, we observe a power-law decay, but the exponent  \( \beta \)  depends on D. We find  \( \beta \simeq 0.92 \)  for D = 2 and  \( \beta \simeq 0.85 \)  for D = 3, which are consistent with previous work [34]. For D = 4 and 8, on the other hand, the results are described by the same exponent  \( \beta \simeq 0.75 \) . This suggests that a mean-field value  \( \beta = 0.75 \)  in the high temperature regime is reached for  \( D \geq 4 \) . Interestingly, this exponent is close to the one observed in the Mari-Kurchan model at high temperatures. In SI, we discuss the system-size dependence of  \( \langle |\boldsymbol{v}(t)|\rangle \) . Larger systems always take a longer time to reach energy minima, consistently with a pure power law decay in the thermodynamic limit  \( N \rightarrow \infty \)  at large times.

To investigate universality, we look at the results at high temperatures for various models. Figures 2(b-f) show the velocity decay for harmonic and soft spheres, and the Kob-Andersen model. Note that for soft spheres and Kob-Andersen models, the influence of the repulsive core can be felt at arbitrarily large temperatures. Nevertheless, all models at higher initial temperatures asymptotically show  \( \beta\simeq0.92 \)  and 0.85 in D=2 and D=3, respectively. Therefore, we conclude that the value of  \( \beta \)  is universal, irrespective of the details of the interaction potentials, size polydispersity, or the proximity of a jamming transition.

We then study the effect of the initial stability on the relaxation dynamics. We first consider D = 3 polydisperse soft spheres. Using the swap Monte Carlo algorithm, we vary initial equilibrium temperature quite significantly,  \( T \in [0.062, 1.0] \) , which includes  \( T_{MCT} \simeq 0.1 \)  and  \( T_{onset} \simeq 0 \) .18 determined by standard methods [46]. The model reproduces the universal exponent in D = 3,  \( \beta = 0.85 \) , at finite but high temperatures, see Fig. 2(b). With decreasing temperature, the velocity relaxation  \( \langle |\pmb{v}(t)|\rangle \)  becomes faster, as expected from the physical intuition that the system starts closer to an energy minimum in a smoother landscape. However, even at temperatures much below  \( T_{MCT} \) , the velocity relaxation  \( \langle |\pmb{v}(t)|\rangle \)  displays a power-law decay, but with a larger apparent exponent,  \( \beta \simeq 1.25 \) . The same exponent at low T is found in the D = 3 Kob-Andersen model [see Fig. 2(c)],
 

suggesting that  \( \beta\simeq1.25 \)  is also universal. We vary the initial stability for D=2 harmonic spheres, soft spheres, and the Kob-Andersen model in Fig. 2(d), (e), and (f). The data demonstrate the same trend as in D=3 models, yet the low-temperature velocity decay exponent is now  \( \beta\simeq1 \)  in all three models, different from the D=3 value. Importantly, we do not observe an exponential decay at any studied temperatures in any of the finite-dimensional models, in contrast to the mean-field spin glass and Mari-Kurchan models. Instead, we find that the high- and low-temperature regimes are both characterised by universal power-laws, with an exponent which only depends on the spatial dimension.

## D. Harmonic limit

We can rationalize our numerical observations at low temperatures using a harmonic dynamical description  \( [53] \) . At very low initial temperatures, the initial equilibrium configuration is located nearer to the final inherent state. Thus, it makes sense to approximate the energy during the steepest descent dynamics using a harmonic expansion

 \[ E(t)\simeq E(t\rightarrow\infty)+\frac{1}{2}\Delta\boldsymbol{r}(t)\cdot\boldsymbol{H}\cdot\Delta\boldsymbol{r}(t), \quad (4) \] 

with  \( \Delta\boldsymbol{r}(t)=\boldsymbol{r}(t\rightarrow\infty)-\boldsymbol{r}(t) \)  and H the Hessian matrix in the energy minimum. Let us assume that the phononic modes following the Debye law and quasi-localised modes following the non-Debye quartic law coexist in the low-frequency region of the vibrational density of states [54]. By linearising the equations of motion, we can relate the time decay of the velocity to the properties of the Hessian matrix and we find that the velocity should decay with an exponent  \( \beta_{harm}=D/4+1/2 \) , yielding  \( \beta_{harm}=1 \)  and 1.25 for D=2 and D=3, respectively. (See Appendix A1d for a more detailed discussion of the harmonic approximation, which also shows that quasi-localised modes provide a subdominant contribution to the velocity decay for D<5.) These values are fully consistent with our numerical observations, which means that the low-temperature relaxation dynamics appears to be well-described, at least over the simulated timescales and system sizes, by a simple harmonic approach, for all types of particle interactions.

## E. Localised defects

The harmonic analysis shows that, because of phonons, the mean-field transition at  \( T_{SF} \)  to gapped energy minima reached exponentially fast cannot exist in finite D, and relaxation dynamics is in fact necessarily algebraic, even in a harmonic, 'state following' limit. Our numerics is nevertheless compatible with two distinct temperature regimes, with non-harmonic effects becoming predomi-

![](./images/867745664589627861_9.jpg)

FIG. 3. 2D soft spheres. (a-c) Non-affine displacements  \( D_{min}^{2} \)  and (d-f) defects for three different configurations. In (d-f), defects are shown in red, other particles are in blue. In all panels, the displacement vectors  \( \boldsymbol{r}_{i}(t=0)-\boldsymbol{r}_{i}({t}\rightarrow\infty) \)  (arrows) is amplified by a factor of 3. The temperature is T=0.035 in (a, d), 0.2 in (b, e), and 0.8 in (c, f).

nant at high initial T. Is a sharp transition separating these two regimes?

To address this question, we must understand the microscopic relaxation mechanism beyond the harmonic limit. At very low temperatures, we expect that the initial configuration and the final inherent state differ by small displacements which do not affect much the geometry of the particle packing. Figure 3(a-c) show the displacement and non-affine displacement fields [55] between initial and final configurations for the D=2 soft sphere system. For T=0.035, where the harmonic description works well (and  \( \beta=\beta_{harm}=1.0 \)  is measured), particle displacements are indeed very small, implying that most particles interact with the same neighbours in initial and final states, see Fig. 3(a). For T=0.2, however, larger displacements are observed, and the most mobile particles are spatially correlated, see Fig. 3(b). Large non-affine displacements are associated with localised particle rearrangements occurring during the steepest descent, which we call 'defects'. As the temperature is increased further, more particles have large non-affine displacements, see Fig. 3(c), and the initial and final configurations become substantially different.

To quantify particle rearrangements during minimisation, we introduce a variable  \( \phi_{i} \)  for each particle defined such that  \( \phi_{t}=0 \)  if particle i neither loses nor gains any neighbour during steepest descent, and  \( \phi_{i}=1 \)  otherwise (see SI for precise definitions), and denote  \( \phi=\frac{1}{N}\sum_{i}\phi_{i} \)  the concentration of such defects in a given configuration with N particles. The field  \( \phi_{i} \)  thus identifies the location of particle rearrangements, as shown in Fig. 3(d-f). Red particles with  \( \phi_{i}=1 \)  are found in high  \( D_{min}^{2} \)  regions, which validates the proposed identification of defects. The defects are also observed in the displacement
 
![](./images/867745664589627861_10.jpg)

![](./images/867745664589627861_11.jpg)

FIG. 4. Soft spheres. (a) Average concentration  \( \langle\phi\rangle \)  and (b) collective susceptibility  \( \chi \)  of defects, as a function of initial equilibrium temperature. The temperature evolution of the defect concentration is smooth, with a maximum variation near  \( T_{def} \approx 0.25 \)  and  \( T_{def'} \approx 0.15 \)  for D = 2 and 3, respectively.

field  \( |\boldsymbol{r}_{i}(t)-\boldsymbol{r}_{i}(\infty)| \) , see SI for further discussion. In Ref. [34], similar defects were visualised using the non-affine velocity field.

In Fig. 4, we show the average concentration of defects,  \( \langle\phi\rangle \) , for D = 2 and  \( D = 3 \)  soft-sphere models, and the collective susceptibility of defects,  \( \chi = N(\langle\phi^{2}\rangle - \langle\phi\rangle^{2}) \) . The average defect density is a smooth function of temperature which seems to remain finite at any initial T > 0. The susceptibility shows a well-defined peak, whose shape and location are independent of the system size, see Fig. 4(b). These results indicate that no sharp phase transition (with a vanishing  \( \langle\phi\rangle \) ) separates the relaxation dynamics between high and low temperatures. The defect density has a sigmoidal shape as it saturates to unity at large T and decreases very rapidly to small values as  \( T \to 0 \) . It displays an inflection point at a temperature  \( T_{def} \)  that also corresponds to the peak of the susceptibility. Physically,  \( T_{def} \)  represents the temperature where  \( \langle\phi\rangle \)  varies more strongly with T and has the largest fluctuations, thus separating the high-T regime where  \( \langle\phi\rangle \)  approaches unity, from low-T where it is very small. The gradual disappearance of localised rearrangements presumably explains the temperature evolution of the self-part of the van-Hove function [36]. The discussion of the harmonic limit in Sec. II D showed that the defects revealed by steepest descent dynamics at lower temperatures do not simply result from the harmonic excitation of the quasi-localised modes populating the low-frequency part of the density of states (which would lead to a different power law decay), although a more complicated relation could exist.

## III. DISCUSSION

We studied the physical dynamics during steepest descent energy minimisation for various glass-forming models in spatial dimensions D = 2 to D = 8 and also in the mean-field limit, for a wide range of initial conditions. Focusing on the exponent  \( \beta \)  characterising the algebraic decay of the average velocity, we identified its universal, finite dimensional features. First, we showed that the mean-field transition at temperature  \( T_{SF} \)  to an exponential decay cannot exist in finite D due to the presence of phonons. More importantly, we showed that the measured evolution of  \( \beta \)  from its high-temperature universal value towards a larger harmonic value  \( \beta_{harm} = D/4 + 1/2 \) , observed at low-temperatures, reflects in fact the gradual suppression of a population of localised defects with decreasing T. The relative importance of defects and plane waves explains the observed evolution of  \( \beta \) . Since  \( \beta_{harm} \)  is larger than its high-T value, we expect the latter exponent to dominate the long-time limit of the velocity decay at any finite temperature in the thermodynamic limit. In this view, the harmonic regime is only a transient which lasts longer at lower temperature when there are less defects. As a result, the mean-field critical temperature  \( T_{SF} \)  has no analog in finite D. This implies that, at finite temperature, an instantaneous configuration of a finite dimensional glass-forming system can never be seen as an inherent structure excited by small thermal fluctuations. It would be interesting to explore theoretical models alternative to mean-field glass models, such as elasto-plastic models [56], to account better for our numerical observations, in particular the value of the exponent  \( \beta \) .

Our results have broad physical consequences. First, they imply that the defect dynamics leading to the coarsening of the non-affine velocity field described in Ref. [34] (see also SI) is actually relevant for generic finite D glass-forming liquids, and is unrelated to the athermal jamming transition. The observed universal exponent  \( \beta \)  implies similarly universal geometrical features of the potential energy landscapes of generic structural glasses. Interestingly, an experimental realisation of the steepest descent dynamics has recently been proposed [57]. By perturbing a stable foam configuration in two dimensions, localised defects during the relaxation were also observed. Such experiments could validate our numerical findings, especially the universal exponent  \( \beta \)  found at high initial temperatures. More generally, our observations about defects at lower initial temperatures is another supporting evidence of the existence of localised excitations in stable glasses relevant for metallic and molecular glasses [58].
Second, together with recent analytic and numerical
 

works [35, 59], our results shed new light on the connection between equilibrium glassy dynamics and stationary points of the potential energy landscape. The interpretation of the mode-coupling temperature  \( T_{MCT} \)  as a topographic change in the potential energy landscape does not hold in mixed p-spin models [35]. Our simulations of the Mari-Kurchan model confirm that the saddle-to-minima transition occurs at a temperature  \( T_{SF} \)  distinct from  \( T_{MCT} \) , already at mean-field level. The emergence of localised defects in finite dimensions found here is consistent with the recent conclusion [59] that the critical transition at  \( T_{SF} \)  is replaced in finite D by a smooth crossover. A similar scenario controlled by non-interacting localised defects was also found in kinetically constrained models [42], thus suggesting a potential connection between the defects revealed by steepest descent dynamics and those discussed in the context of dynamic facilitation [60]. However, the power law decay revealed by our study cannot result from the de-excitation of a non-interacting gas of isolated defects and steepest descent dynamics in kinetically constrained models would instead be unremarkable. It is also unclear whether elasto-plastic models where relaxation events are coupled by elasticity can account for our findings.

Third, our finding that a finite concentration of defects controls the non-harmonic relaxation from equilibrated configurations to inherent states suggests that the potential energy landscape of glass-formers is both rugged and chaotic. To test this idea numerically, we applied a very small random perturbation to the initial configuration and monitored the subsequent steepest descent dynamics. We found that a slight perturbation typically leads to different inherent structures (not shown), consistent with earlier work  \( [61, 62] \) . The strong chaoticity of the minimisation dynamics implies that the energy minimum reached from a given equilibrium configuration in fact strongly depends on the minimisation algorithm itself  \( [63] \) . The steepest descent (SD) dynamics we used is just the simplest algorithm for numerical optimisation, but there are several other (usually more efficient) ways to reach the bottom of the potential energy landscape, such as conjugate-gradient (CG)  \( [64] \)  and fast inertial relaxation engine (FIRE)  \( [65] \) . Indeed, we find that starting from the same initial configuration, the SD, CG and FIRE dynamics typically converge to different inherent structures, as quantified by their mutual distances (see SI). The evolution of this distance mirrors the temperature evolution of the defect concentration in Fig. 4(a), higher initial temperatures leading to larger separations. In Fig. 5, we show representative snapshots of the displacement field between two inherent structures obtained by two different algorithms starting from a unique initial configuration. A single localised defects can be seen at low T, which naturally gives rise to a quadrupolar Eshelby-like displacement field. Defects proliferate at higher temperature. This shows that mapping an equilibrium liquid state to an inherent structure is a fully dynamical problem, which becomes uniquely defined only

![](./images/867745664589627861_12.jpg)

![](./images/867745664589627861_13.jpg)

FIG. 5. Displacement fields,  \( r_{i}^{CG} - r_{i}^{FIRE} \) , between pairs of minima obtained via conjugate gradient ( \( \{r_{i}^{CG}\} \) ) and FIRE algorithms ( \( \{r_{i}^{FIRE}\} \) ), following a quench from the same initial configuration at T = 0.07 (a) and T = 0.15 (b), for 2D soft spheres with N = 64000. Arrows magnified by a factor 40 and 2 for (a) and (b), respectively.

after a specific choice for the minimisation algorithm is made. Localised defects, which had been used by Stillinger [66] to construct an argument against the existence of a Kauzmann transition (see the discussion in [67]), instead weaken the thermodynamic significance of a tiling of configuration space directly based on inherent states.

In recent years, localised glassy defects have been reported from the study of harmonic  \( [31] \)  and non-harmonic excitations, in the fields of plasticity  \( [32] \)  and low-temperature transport properties  \( [30] \) , and in connection with secondary relaxations in deeply supercooled liquids  \( [68, 69] \)  and dynamic facilitation  \( [60] \) . Steepest descent dynamics thus corresponds to another situation where localised excitations control structural rearrangements at the particle scale and reveal that they interact in a non-trivial manner. Future work should establish the similarities and differences between these disparate observations. Ultimately, we expect that a unifying picture of localised defects with specific interactions will soon become available and applicable to a host of different physical situations.

## ACKNOWLEDGMENTS

We thank G. Biroli, R. Chacko, G. Folena, and H. Ikeda for discussions. We also thank A. D. S. Parmar for sharing stable Kob-Andersen configurations. This work was supported by grants from the Simons Foundation (#454935 L. Berthier) and JSPS KAKENHI (Grants No. 18H05225, 19H01812, 20H01868, 20H00128, A. Ikeda).

## Appendix A: Methods

## 1. Models

We study the steepest descent dynamics of models with three different interaction potentials: soft spheres, har-
 

monic spheres, and Lennard-Jones interactions. The dimensionality dependence, including the mean-field limit, of this dynamics is studied by using the models in two-, three-, four-, eight-dimensions, and the mean-field Marikurchan model [44, 70].

## a. Soft spheres

The two- and three-dimensional soft sphere models [45, 46] consist of particles with purely repulsive interactions and a continuous size polydispersity. Particle diameters,  \( d_{i} \) , are randomly drawn from a distribution of the form:  \( f(d) = Ad^{-3} \) , for  \( d \in [d_{\min}, d_{\max}] \) , where A is a normalization constant. The size polydispersity is quantified by  \( \delta = (\overline{d^{2}} - \overline{d}^{2})^{1/2}/\overline{d} \) , where the overline denotes an average over the distribution  \( f(d) \) . Here we choose  \( \delta = 0.23 \)  by imposing  \( d_{\min}/d_{\max} = 0.449 \) . The average diameter,  \( \overline{d} \) , sets the unit of length. The soft-sphere interactions are pairwise and described by an inverse power-law potential

 \[ \begin{aligned}&U_{ij}(r)=v_{0}\left(\frac{d_{ij}}{r}\right)^{12}+c_{0}+c_{1}\left(\frac{r}{d_{ij}}\right)^{2}+c_{2}\left(\frac{r}{d_{ij}}\right)^{4},\\&d_{ij}=\frac{(d_{i}+d_{j})}{2}(1-\epsilon|d_{i}-d_{j}|),\\ \end{aligned} \quad (A1) \] 

where  \( v_{0} \)  sets the unit of energy (and of temperature with the Boltzmann constant  \( k_{B} \equiv 1 \) ) and  \( \epsilon = 0.2 \)  quantifies the degree of nonadditivity of particle diameters. We introduce  \( \epsilon > 0 \)  in the model to suppress fractionation and thus to enhance the glass-forming ability. The constants  \( c_{0} \) ,  \( c_{1} \)  and  \( c_{2} \)  enforce a vanishing potential and continuity of its first- and second-order derivatives at the cut-off distance  \( r_{cutoff} = 1.25d_{ij} \) . We simulate a system with N particles within a square cell of area (volume)  \( V = L^{2} \)  ( \( V = L^{3} \) ) where L is the linear box length, under periodic boundary conditions, at a number density  \( \rho = N/V = 1 \)  (1.02) for 2D (3D).

We prepare equilibrium configurations using the swap Monte Carlo algorithm [46]. With probability  \( P_{swap} = 0.2 \) , we perform a swap move where we randomly pick two particles (i and j) having similar diameters ( \( |d_{i} - d_{j}| < 0.2 \) ) and attempt to exchange their diameters. With probability  \( 1 - P_{swap} = 0.8 \) , instead, we perform conventional Monte Carlo translational moves, where we pick one particle and displace it within a box with linear length  \( \delta_{max} = 0.12\overline{d} \) .

## b. Harmonic spheres

We study the harmonic sphere model [47, 71] in two, three, four, and eight dimensions. The harmonic sphere model has an interaction potential

 \[ U_{i j}(r_{i j})=\frac{v_{0}}{2}\left(1-\frac{r_{i j}}{d_{i j}}\right)^{2}, \quad (A2) \] 

 \[ d_{i j}=\frac{(d_{i}+d_{j})}{2}(1-\epsilon|d_{i}-d_{j}|), \quad (A3) \] 

where  \( v_{0} \)  is again the unit of the energy scale. For the two dimensional model, to avoid crystallisation at low temperature, we use the continuously polydisperse nonadditive model with the same distribution of the particle diameters used in the soft-sphere model and  \( \epsilon = 0.2 \)  in two dimensions. The unit length scale for the two-dimensional model is  \( \overline{d} \)  as well as the soft-sphere model. We again use the swap Monte Carlo algorithm with the same setting and parameters as for the polydisperse soft spheres to equilibrate down to very low temperatures. In three, four, and eight dimensions, crystallisation is highly suppressed, and the simple additive ( \( \epsilon = 0 \) ) monodisperse model is enough to study the relaxation dynamics to disordered states. Due to the finite range of the interaction, the system has a critical jamming transition at finite density, below which the relaxation dynamics shows an exponentially fast decay towards zero energy states [72]. Since in other models we study the relaxation dynamics towards energy minima with a finite energy, a direct comparison is possible when the inherent structures of harmonic spheres have finite energies as well. We thus set the volume fraction above the jamming transition to  \( \phi = 1.2 \) , 0.73, 0.5, 0.1 in two, three, four, and eight dimensions, respectively, so that the final energies are always finite.

## c. Kob-Andersen Lennard-Jones model

For the case of the well-studied Kob-Andersen binary Lennard-Jones (KALJ) model, the interaction between two particles has the following form:

 \[ U_{i j}(r_{i j})=4v_{0}\left(\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{12}-\left(\frac{\sigma_{i j}}{r_{i j}}\right)^{6}\right). \quad (A4) \] 

for  \( r < r_{cutoff} = 2.5\sigma_{ij} \)  and particles i, j can belong to either A or B species which constitute the binary mixture.  \( r_{cutoff} \)  is the cutoff distance at which the potential  \( U_{ij}(r_{ij}) \)  is truncated. The different interaction parameters for the binary mixture take the following values:  \( \epsilon_{AA} = 1.0 \) ,  \( \epsilon_{AB} = 1.5\epsilon_{AA} \) ,  \( \epsilon_{BB} = 0.5\epsilon_{AA} \) ;  \( \sigma_{AA} = 1.0 \) ,  \( \sigma_{AB} = 0.8\sigma_{AA} \) ,  \( \sigma_{BB} = 0.88\sigma_{AA} \) . The mixture has 80:20 composition in 3D and 65:35 composition in 2D, to optimise glass-forming ability. In D = 2, we study a system consisting 125000 particles and for D = 3, we study a system of 76800 particles. Additionally, in D = 3, we study a system of 27135 particles to probe the quench dynamics of states sampled at a low temperature (T = 0.37), where configurations are obtained by a swap Monte Carlo scheme developed in Ref. [73].
 

## d. Mari-Kurchan model

We study the mean-field Mari-Kurchan (MK) model [44, 70] in three dimensions with the simple monodisperse soft-sphere interaction in Eq. (A1) with  \( \epsilon = 0 \)  and the cutoff length  \( r_{cutoff} = 4d \) , where d is the diameter of particles. The volume fraction is  \( \phi = 0.5 \) . The MK model has quenched randomness in the particle distance, and the interaction potential is thus  \( U(|r_{i} - r_{j} + A_{ij}|) \) , where  \( A_{ij} \)  is a three-dimensional vector with each component sampled from the uniform distribution in the interval  \( [0, L] \)  (L the box size). Equilibrium configurations of the MK model are produced by using the planting technique [44, 74]. For systems with general isotropic interactions, the cubic shape of the box complicates the direct sampling of the random shifts from the Boltzmann distribution.

 \[ P(\boldsymbol{A}_{ij}|\boldsymbol{r}_{ij})=\frac{\exp(-\beta U_{ij}(|\boldsymbol{r}_{i}-\boldsymbol{r}_{j}+\boldsymbol{A}_{ij}|))}{\int d\boldsymbol{A}_{ij}\exp(-\beta U_{ij}(|\boldsymbol{r}_{i}-\boldsymbol{r}_{j}+\boldsymbol{A}_{ij}|))}. \quad (A5) \] 

We thus use the Markov chain Monte Carlo method to sample the random shifts  \( \{A_{ij}\} \)  from the distribution Eq. (A5) so that any given particle configuration follows from the Boltzmann distribution. For each pair of particles i and j, we take  \( A_{ij} \)  as the random shift after 200 Monte Carlo sweeps with the simple Metropolis algorithm starting from uniformly random numbers.

## Appendix B: Harmonic exponent

We discuss the asymptotic decay of the velocity by assuming that the system is perfectly harmonic and the vibrational density of states follows the Debye law. Let the Hessian matrix H of an inherent structure have eigenvalues  \( \{\lambda_{a}\} \)  and corresponding eigenvectors  \( \{\pmb{x}_{a}\} \) . Since the Hessian matrix is real symmetric, eigenvectors are orthogonal;  \( x_{a} \cdot x_{b} = \delta_{ab} \) , where  \( \delta_{ab} is the Kronecker's delta. Using the eigenvectors, we have the particle dis-

[1] Jean-Philippe Bouchaud, Marc Mézard, and Jean Dalibard, Complex systems: lecture notes of the Les Houches Summer School 2006 (Elsevier, 2007).

[2] David Wales, Energy Landscapes: Applications to Clusters, Biomolecules and Glasses, Cambridge Molecular Science (Cambridge University Press, 2004).

[3] Frank H Stillinger, Energy Landscapes, Inherent Structures, and Condensed-Matter Phenomena (Princeton University Press, 2015).

[4] Frank H Stillinger, “A topographic view of supercooled liquids and glass formation,” Science 267, 1935–1939 (1995).

[5] Antonio Auffinger, Gérard Ben Arous, and Ji?i Černý, "Random Matrices and Complexity of Spin Glasses,"

placement written as

 \[ \Delta\boldsymbol{r}(t)=\sum_{a}c_{a}(t)\boldsymbol{x}_{a}, \quad (B1) \] 

where  \( c_{a}(t) = \Delta \mathbf{r}(t) \cdot \mathbf{x}_{a} \) . Suppose that the system is perfectly harmonic, i.e. the system follows linearised equations of motion,

 \[ \zeta\frac{\mathrm{d}\Delta\boldsymbol{r}}{\mathrm{d}t}=-\boldsymbol{H}\cdot\Delta\boldsymbol{r}. \quad (B2) \] 

Then each mode decays exponentially with  \( c_{a}(t) = c_{a}(0)e^{-\lambda_{a}t} \)  and the equipartition law  \( \langle c_{a}(0)^{2} \rangle = \frac{T}{\lambda_{a}} \)  holds.

In this harmonic approximation, the potential energy decreases with time as

 \[ \begin{align*}\langle E(t)-E(t\rightarrow\infty)\rangle&=\frac{1}{2}\sum_{a}c_{a}^{2}(t)\lambda_{a}\exp\left(-2\lambda_{a}t\right)\\&=\frac{NT}{2}\int d\lambda\rho(\lambda)\exp\left(-2\lambda t\right),\end{align*} \quad (B3) \] 

where  \( \rho(\lambda)=\left\langle\frac{1}{N}\sum_{a}\delta(\lambda-\lambda_{a})\right\rangle \)  is the density of eigenvalues.

Let us assume that the density of state has the contributions from the phononic modes following the Debye law and quasi-localised modes following the non-Debye quartic law i.e.  \( g(\omega) = A_{0}\omega^{D-1} + A_{4}\omega^{4} \)  [54, 75, 76]. Then the density of eigenvalues reads  \( \rho(\lambda) = g(\omega)\frac{d\omega}{d\lambda} = A_{0}\lambda^{D/2-1} + A_{4}\lambda^{3/2} \) . Thus

 \[ \begin{align*}\langle E(t)-E(t\rightarrow\infty)\rangle&\sim\frac{NT}{2}\int d\lambda(A_{0}\lambda^{D/2-1}+A_{4}\lambda^{3/2})e^{-2\lambda t}\\&\sim t^{-D/2}+O(t^{-5/2}).\end{align*} \quad (B4) \] 

Therefore, the energy relaxation is dominated by  \( t^{-D/2} \)  when  \( D \leq 5 \) . Since, for the steepest descent dynamics with the equations of motion given by Eq. (1), the energy decay can be related to the velocity decay, we finally obtain  \( \langle |\boldsymbol{v}(t)| \rangle \sim t^{-\beta_{\mathrm{harm}}} \)  with  \( \beta_{harm} = D/4 + 1/2 \)  for  \( D \leq 5 \) .

Comm. Pure Appl. Math. 66, 165–201 (2013).

[6] Valentina Ros, Gerard Ben Arous, Giulio Biroli, and Chiara Cammarota, “Complex Energy Landscapes in Spiked-Tensor and Simple Glassy Models: Ruggedness, Arrangements of Local Minima, and Phase Transitions,” Phys. Rev. X 9, 011003 (2019).

[7] Francesco Sciortino, “Potential energy landscape description of supercooled liquids and glasses,” J. Stat. Mech.: Theory Exp. 2005, P05015 (2005).

[8] Andreas Heuer, “Exploring the potential energy landscape of glass-forming systems: from inherent structures via metabasins to macroscopic transport,” J. Phys. Condens. Matter 20, 373101 (2008).

[9] Florent Krzakala, Andrea Montanari, Federico Ricci-
 

Tersenghi, Guilhem Semerjian, and Lenka Zdeborová, "Gibbs states and the set of solutions of random constraint satisfaction problems," Proc. Natl. Acad. Sci. U.S.A. 104, 10318–10323 (2007).

[10] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton, "Deep learning," Nature 521, 436–444 (2015).

[11] Marco Baity-Jesi, Levent Sagun, Mario Geiger, Stefano Spigler, Gérard Ben Arous, Chiara Cammarota, Yann LeCun, Matthieu Wyart, and Giulio Biroli, “Comparing dynamics: deep neural networks versus glassy systems,” J. Stat. Mech.: Theory Exp. 2019, 124013 (2019).

[12] Jaron Kent-Dobias and Jorge Kurchan, “Complex complex landscapes,” Physical Review Research 3, 023064 (2021).

[13] Martin Goldstein, “Viscous Liquids and the Glass Transition: A Potential Energy Barrier Picture,” J. Chem. Phys. 51, 3728–3739 (1969).

[14] C. A. Angell, “Formation of Glasses from Liquids and Biopolymers,” Science 267, 1924–1935 (1995).

[15] Andrea Cavagna, Irene Giardina, and Giorgio Parisi, "Stationary points of the Thouless-Anderson-Palmer free energy," Phys. Rev. B 57, 11251–11257 (1998).

[16] Valentina Ros, Giulio Biroli, and Chiara Cammarota, "Complexity of energy barriers in mean-field glassy systems," EPL (Europhysics Letters) 126, 20003 (2019).

[17] Tommaso Rizzo, “Path integrals for activated dynamics in glassy systems,” arXiv preprint arXiv:2012.09556 (2020).

[18] Frank H. Stillinger and Thomas A. Weber, “Hidden structure in liquids,” Phys. Rev. A 25, 978–989 (1982).

[19] Ludovic Berthier and Juan P. Garrahan, “Nontopographic description of inherent structure dynamics in glassformers,” J. Chem. Phys. 119, 4367–4371 (2003).

[20] Jeppe C. Dyre, “Colloquium: The glass transition and elastic models of glass-forming liquids,” Rev. Mod. Phys. 78, 953–972 (2006).

[21] G. Biroli and R. Monasson, “From inherent structures to pure states: Some simple remarks and examples,” EPL (Europhysics Letters) 50, 155 (2000).

[22] Andrea Cavagna, “Fragile vs . strong liquids: A saddles-ruled scenario,” Europhysics Letters (EPL) 53, 490–496 (2001).

[23] L. Angelani, R. Di Leonardo, G. Ruocco, A. Scala, and F. Sciortino, “Saddles in the Energy Landscape Probed by Supercooled Liquids,” Phys. Rev. Lett. 85, 5356–5359 (2000).

[24] Kurt Broderix, Kamal K Bhattacharya, Andrea Cavagna, Annette Zippelius, and Irene Giardina, “Energy Landscape of a Lennard-Jones Liquid: Statistics of Stationary Points,” Phys. Rev. Lett. 85, 5360–5363 (2000).

[25] Tomás S. Grigera, Andrea Cavagna, I. Giardina, and Giorgio Parisi, “Geometric approach to the dynamic glass transition,” Phys. Rev. Lett. 88, 55502 (2002).

[26] Ludovic Berthier and Daniele Coslovich, “Novel approach to numerical measurements of the configurational entropy in supercooled liquids,” Proc. Natl. Acad. Sci. U.S.A. 111, 11668–11672 (2014).

[27] Misaki Ozawa, Atsushi Ikeda, Kunimasa Miyazaki, and Walter Kob, “Ideal glass states are not purely vibrational: Insight from randomly pinned glasses,” Phys. Rev. Lett. 121, 205501 (2018).

[28] Marco Baity-Jesi, Giulio Biroli, and David R Reichman, "Revisiting the concept of activation in supercooled liquids," arXiv preprint arXiv:2103.07211 (2021).

[29] Simon Gelin, Hajime Tanaka, and Anaël Lemaître, “Anomalous phonon scattering and elastic correlations in amorphous solids,” Nat. Mater. 15, 1177–1181 (2016).

[30] Dmytro Khomenko, Camille Scalliet, Ludovic Berthier, David R. Reichman, and Francesco Zamponi, “Depletion of Two-Level Systems in Ultrastable Computer-Generated Glasses,” Phys. Rev. Lett. 124, 225901 (2020).

[31] Edan Lerner, Gustavo Düring, and Eran Bouchbinder, "Statistics and Properties of Low-Frequency Vibrational Modes in Structural Glasses," Phys. Rev. Lett. 117, 035501 (2016).

[32] D. Richard, M. Ozawa, S. Patinet, E. Stanifer, B. Shang, S. A. Ridout, B. Xu, G. Zhang, P. K. Morse, J.-L. Barrat, L. Berthier, M. L. Falk, P. Guan, A. J. Liu, K. Martens, S. Sastry, D. Vandembroucq, E. Lerner, and M. L. Manning, “Predicting plasticity in disordered solids from structural indicators,” Phys. Rev. Mater. 4, 113609 (2020).

[33] William H Press, Saul A Teukolsky, William T Vetterling, and Brian P Flannery, Numerical Recipes in Fortran 90: Numerical recipes in Fortran 77V. 2. Numerical recipes in Fortran V90 (Cambridge University Press, 1996).

[34] R. N. Chacko, Peter Sollich, and S. M. Fielding, “Slow Coarsening in Jammed Athermal Soft Particle Suspensions,” Phys. Rev. Lett. 123, 108001 (2019).

[35] Giampaolo Folena, Silvio Franz, and Federico Ricci-Tersenghi, “Rethinking Mean-Field Glassy Dynamics and Its Relation with the Energy Landscape: The Surprising Case of the Spherical Mixed p-Spin Model,” Phys. Rev. X 10, 31045 (2020).

[36] Karina González-López and Edan Lerner, “An energy-landscape-based crossover temperature in glass-forming liquids,” J. Chem. Phys. 153, 241101 (2020).

[37] Patrick Charbonneau and Peter K. Morse, “Memory formation in jammed hard spheres,” Phys. Rev. Lett. 126, 088001 (2021).

[38] Giampaolo Folena, Silvio Franz, and Federico Ricci-Tersenghi, “Gradient descent dynamics in the mixed p-spin spherical model: finite-size simulations and comparison with mean-field integration,” J. Stat. Mech.: Theory Exp. 2021, 033302 (2021).

[39] Ethan Stanifer and M Lisa Manning, “Avalanche dynamics in sheared athermal particle packings occurs via localized bursts predicted by unstable linear response,” arXiv preprint arXiv:2110.02803 (2021).

[40] Alessandro Manacorda and Francesco Zamponi, “Gradient descent dynamics and the jamming transition in infinite dimensions,” arXiv preprint arXiv:2201.01161 (2022).

[41] Jorge Kurchan and Laurent Laloux, “Phase space geometry and slow dynamics,” J. Phys. A: Math. Gen. 29, 1929 (1996).

[42] Ludovic Berthier and Juan P. Garrahan, “Real space origin of temperature crossovers in supercooled liquids,” Phys. Rev. E 68, 041201 (2003).

[43] Peter Olsson, “Relaxation times and rheology in dense athermal suspensions,” Physical Review E 91, 062209 (2015).

[44] Romain Mari and Jorge Kurchan, “Dynamical transition of glasses: From exact to approximate,” J. Chem. Phys. 135, 124504 (2011).

[45] Ludovic Berthier, Patrick Charbonneau, Andrea
 

Ninarello, Misaki Ozawa, and Sho Yaida, “Zero-temperature glass transition in two dimensions,” Nat. Commun. 10, 1508 (2019).

[46] Andrea Ninarello, Ludovic Berthier, and Daniele Coslovich, “Models and Algorithms for the Next Generation of Glass Transition Studies,” Phys. Rev. X 7, 021039 (2017).

[47] Ludovic Berthier and Thomas A. Witten, “Glass transition of dense fluids of hard and compressible spheres,” Phys. Rev. E 80, 021502 (2009).

[48] Walter Kob and Hans C. Andersen, “Testing mode-coupling theory for a supercooled binary Lennard-Jones mixture. II. Intermediate scattering function and dynamic susceptibility,” Phys. Rev. E 52, 4134–4153 (1995).

[49] Ferdinando Giacco, Lucilla de Arcangelis, Massimo Pica Ciamarra, and Eugenio Lippiello, “Rattler-induced aging dynamics in jammed granular systems,” Soft Matter 13, 9132–9137 (2017).

[50] Florent Krzakala and Lenka Zdeborová, “Hiding quiet solutions in random constraint satisfaction problems,” Phys. Rev. Lett. 102, 238701 (2009).

[51] “See Supplemental Material for further discussions on the replica liquid theory of the MK model, velocity decay, and defects in real space, that includes Refs. [34, 54, 65, 74, 77–81],” (2021).

[52] The exponent  \( \beta \)  for the spin glass model is obtained from the exponent for the energy decay reported in [35] which is given by  \( 2\beta - 1 \) .

[53] The term ‘harmonic’ here means that the system energy is expanded up to the quadratic term. This harmonic approximation is applicable to any smooth interaction potential, and not only to the system of harmonic spheres.

[54] Hideyuki Mizuno, Hayato Shiba, and Atsushi Ikeda, "Continuum limit of the vibrational properties of amorphous solids," Proc. Natl. Acad. Sci. U.S.A. (2017).

[55] M L Falk and J S Langer, “Dynamics of viscoplastic deformation in amorphous solids,” Phys. Rev. E 57, 7192–7205 (1998).

[56] Jack T. Parley, Suzanne M. Fielding, and Peter Sollich, "Aging in a mean field elastoplastic model of amorphous solids," Phys. Fluids 32, 127104 (2020).

[57] Naoya Yanagisawa and Rei Kurita, “Size distribution dependence of collective relaxation dynamics in a two-dimensional wet foam,” Sci. Rep. 11, 2786 (2021).

[58] JC Qiao, Qiang Wang, JM Pelletier, Hidemi Kato, Riccardo Casalini, D Crespo, E Pineda, Yao Yao, and Y Yang, “Structural heterogeneities and mechanical behavior of amorphous alloys,” Progress in Materials Science 104, 250–329 (2019).

[59] Daniele Coslovich, Andrea Ninarello, and Ludovic Berthier, “A localization transition underlies the mode-coupling crossover of glasses,” SciPost Phys. 7, 077 (2019).

[60] Aaron S. Keys, Lester O. Hedges, Juan P. Garrahan, Sharon C. Glotzer, and David Chandler, “Excitations are localized and relaxation is hierarchical in glass-forming liquids,” Phys. Rev. X 1, 021013 (2011).

[61] Camille Scalliet, Ludovic Berthier, and Francesco Zamponi, “Absence of marginal stability in a structural glass,” Phys. Rev. Lett. 119, 205501 (2017).

[62] Camille Scalliet, Ludovic Berthier, and Francesco Zamponi, “Nature of excitations and defects in structural glasses,” Nat. Commun. 10, 5102 (2019).

[63] L. Angelani, G. Ruocco, M. Sampoli, and F. Sciortino, "General features of the energy landscape in lennard-jones-like model liquids," J. Chem. Phys. 119, 2120–2126 (2003).

[64] Jorge Nocedal and Stephen J Wright, Numerical Optimization, Springer Series in Operations Research and Financial Engineering (Springer New York, 2006).

[65] Erik Bitzek, Pekka Koskinen, Franz Gähler, Michael Moseler, and Peter Gumbsch, “Structural Relaxation Made Simple,” Phys. Rev. Lett. 97, 170201 (2006).

[66] Frank H. Stillinger, “Supercooled liquids, glass transitions, and the kauzmann paradox,” J. Chem. Phys. 88, 7818–7825 (1988).

[67] Ludovic Berthier, Misaki Ozawa, and Camille Scalliet, “Configurational entropy of glass-forming liquids,” J. Chem. Phys. 150, 160902 (2019).

[68] Hai-Bin Yu, Ranko Richert, and Konrad Samwer, "Structural rearrangements governing johari-goldstein relaxations in metallic glasses," Sci. Adv. 3 (2017), 10.1126/sciadv.1701577.

[69] Benjamin Guiselin, Camille Scalliet, and Ludovic Berthier, “Microscopic origin of excess wings in relaxation spectra of deeply supercooled liquids,” arXiv preprint arXiv:2103.01569 (2021).

[70] Robert H Kraichnan, J. Math. Phys. 3, 475–495 (1962).

[71] Corey S. O'Hern, Leonardo E. Silbert, Andrea J. Liu, and Sidney R. Nagel, "Jamming at zero temperature and zero applied stress: The epitome of disorder," Phys. Rev. E 68, 011306 (2003).

[72] Yoshihiko Nishikawa, Atsushi Ikeda, and Ludovic Berthier, “Relaxation Dynamics of Non-Brownian Spheres Below Jamming,” J. Stat. Phys. 182, 37 (2021).

[73] Anshul D. S. Parmar, Benjamin Guiselin, and Ludovic Berthier, “Stable glassy configurations of the kob?andersen model using swap monte carlo,” J. Chem. Phys. 153, 134505 (2020).

[74] Patrick Charbonneau, Yuliang Jin, Giorgio Parisi, and Francesco Zamponi, “Hopping and the Stokes–Einstein relation breakdown in simple glass formers,” Proc. Natl. Acad. Sci. U.S.A. 111, 15025–15030 (2014).

[75] Geert Kapteijns, Eran Bouchbinder, and Edan Lerner, "Universal nonphononic density of states in 2d, 3d, and 4d glasses," Phys. Rev. Lett. 121, 055501 (2018).

[76] Masanari Shimada, Hideyuki Mizuno, Ludovic Berthier, and Atsushi Ikeda, “Low-frequency vibrations of jammed packings in large spatial dimensions,” Phys. Rev. E 101, 052906 (2020).

[77] Harukuni Ikeda, Francesco Zamponi, and Atsushi Ikeda, "Mean field theory of the swap monte carlo algorithm," J. Chem. Phys. 147, 234506 (2017).

[78] Ryoichi Yamamoto and Akira Onuki, “Dynamics of highly supercooled liquids: Heterogeneity, rheology, and diffusion,” Phys. Rev. E 58, 3515–3529 (1998).

[79] Hayato Shiba, Takeshi Kawasaki, and Akira Onuki, “Relationship between bond-breakage correlations and four-point correlations in heterogeneous glassy dynamics: Configuration changes and vibration modes,” Phys. Rev. E 86, 041504 (2012).

[80] Ludovic Berthier, Daniele Coslovich, Andrea Ninarello, and Misaki Ozawa, “Equilibrium Sampling of Hard Spheres up to the Jamming Density and Beyond,” Phys. Rev. Lett. 116, 238002 (2016).

[81] Steve Plimpton, “Fast parallel algorithms for short-range molecular dynamics,” J. Comput. Phys. 117, 1–19
 

 

# Supplemental Material for “Relaxation dynamics in the energy landscape of glass-forming liquids”

Yoshihiko Nishikawa, \( ^{1} \)  Misaki Ozawa, \( ^{2} \)  Atsushi Ikeda, \( ^{3} \)  Pinaki Chaudhuri, \( ^{4} \)  and Ludovic Berthier \( ^{1,5} \) 

 \( ^{1} \)  Laboratoire Charles Coulomb (L2C), Université de Montpellier, CNRS, 34095 Montpellier, France

 \( ^{2} \)  Laboratoire de Physique de l'Ecole normale supérieure,

ENS, Université PSL, CNRS, Sorbonne Université,

Université Paris-Diderot, Sorbonne Paris Cité, Paris, France

 \( ^{3} \) Graduate School of Arts and Sciences, The University of Tokyo, Tokyo 153-8902, Japan

 \( ^{4} \) The Institute of Mathematical Sciences, C.I.T. Campus, Taramani, Chennai 600 113, India

 \( ^{5} \)  Yusuf Hamied Department of Chemistry, University of Cambridge,

Lensfield Road, Cambridge CB2 1EW, United Kingdom

(Dated: April 7, 2022)

## I. REPLICA LIQUID THEORY FOR THE MARI-KURCHAN (MK) MODEL

Thanks to the presence of the random shifts, the replica liquid theory can be applied to the MK model, which enables us to predict the dynamical transition in this model. This procedure is well established for the MK model with hard-sphere interactions  \( [S1, S2] \) , and the extension to soft spheres is straightforward. In the replica liquid theory, the cage size  \( \alpha \)  is used as the order parameter, and the self-consistent equation of  \( \alpha \)  for the 3D MK model can be written as

 \[ \frac{1}{\alpha}=-\frac{2\phi}{\pi}\int d\mathbf{r}\frac{\partial Q(\mathbf{r})}{\partial\alpha}\log Q(\mathbf{r}), \quad (S1) \] 

with

 \[ Q(\boldsymbol{r})=\int d\boldsymbol{r}^{\prime}\gamma_{2\alpha}(\boldsymbol{r}+\boldsymbol{r}^{\prime})e^{-\beta U(|\boldsymbol{r}^{\prime}|)}, \quad (S2) \] 

where  \( \gamma_{\alpha}(\boldsymbol{r})=(2\pi\alpha)^{-3/2}e^{-\frac{|\boldsymbol{r}|^{2}}{2\alpha}} \)  is the normalized gaussian function, and  \( U(r) \)  is the soft-sphere interaction potential Eq.(5). The dynamical transition temperature  \( T_{MCT} \)  is defined as the highest temperature at which the self-consistent equation Eq. (S1) has a solution. We numerically solved this equation and obtained  \( T_{MCT} \simeq 0.0084 \)  and  \( \alpha = 0.13 \)  at  \( T = T_{MCT} \) .

## II. SYSTEM-SIZE DEPENDENCE OF THE VELOCITY DECAY

In finite size systems, the power-law decay of the velocity is always cut off after a finite time. To conclude whether or not the decay is algebraic in the thermodynamic limit, it is essential to study its system-size dependence. We show  \( \langle|\boldsymbol{v}(t)|\rangle \)  of the two-dimensional harmonic spheres, three-dimensional soft spheres, and four-dimensional harmonic spheres for several system sizes in Fig. S1 (a-c). In finite dimensions, as we discussed in Sec.II C, the velocity shows a power-law decay in the short time regime. When the system size increases, the cutoff time becomes longer, meaning that, in the thermodynamic limit  \( N \to \infty \) , the power-law decay continues towards the long-time limit. We assume that the velocity decay follows a scaling form

 \[ \langle|\boldsymbol{v}(t)|\rangle=N^{-\beta z}F(t/N^{z}), \quad (S3) \] 

where  \(  F(x)  \)  is the scaling function, and z is another exponent characterising the cutoff time scale. Figures S1 (d-f) show the scaling plot using Eq. (S3). We find roughly  \( z \simeq 0.6 \)  and 0.4 for velocity decay of the two-dimensional and three-dimensional models at high temperature, respectively. In four- and eight-dimensional harmonic spheres in the high-temperature limit and the MK model at high temperature, we observe  \( z \simeq 0.75 \) . At very low temperature, where the harmonic exponent is observed,  \( z \simeq 1 \)  and  \( z \simeq \frac{1}{2} \)  in two and three dimensions, respectively.

## III. DEFINITION OF THE DEFECT FIELD

We explain how to identify defects and measure their concentration. We define the defect order parameter  \( \phi \)  based on the rearrangement of neighboring particles between the initial equilibrium and the final inherent structure.
 

configurations. Let us first imagine a perfect crystal quenched from a small, finite temperature to zero temperature. The two configurations before and after the quench should be essentially the same except for small thermal fluctuations. In this ideal situation, a given particle neither loses nor gains any neighbour during the quench dynamics. In that case, the defect order parameter should produce zero for all particles.

Instead, for a disordered liquid at finite temperature, the steepest descent dynamics involves collective rearrangements and a reshuffling of neighboring particles. When a given particle loses some of the neighboring particles, this process is referred to as a "bond-breaking", as studied extensively  \( [S3, S4] \) . We then assign a positive value to the defect order parameter for a particle involved in a bond-breaking process. We also expect that particles can gain new neighbours during the dynamics. Thus, a defect order parameter should also take into account this process which we call a "bond-insertion". These two processes are sketched in Fig. S2.

To define neighboring particles in practice, we monitor the radial distribution functions in Fig. S3. We compute a radial distribution function as a function of a normalized distance,  \( x_{ij} = r_{ij} / d_{ij} \) , which is a suitable representation for continuously polydisperse systems [S5]. In this 2D polydisperse model,  \( g(x) \)  for the equilibrium state changes quite a lot because the swap Monte Carlo allows us to sample an extremely wide range of temperatures. Consequently, the first local minimum of  \( g(x) \) ,  \( x_{\min}^{EQ} \) , varies  \( x_{\min}^{\text{EQ}} \approx 1.34 - 1.48 \)  with varying temperature,  \( T = 0.035 - 0.800 \) . On the other hand,  \( g(x) \)  for the inherent structure barely changes except for the amplitude of the first peak. In particular, the first local minimum is located in a nearly flat region ( \( x \approx 1.23 - 1.50 \) ).

Based on the observation of  \( g(x) \) , we consider the definition of neighbors for the bond-breaking process. For each particle, we define the neighboring particles in the initial equilibrium configurations as particles located within a cutoff,  \( x_{cut}^{EQ} \) . We set  \( x_{cut}^{\text{EQ}} = x_{min}^{\text{EQ}} \) . Similarly, we define neighboring particles in the inherent structure by introducing a cutoff  \( x_{cut}^{\text{IS}} \) . Ideally, one would like to use again  \( x_{cut}^{\text{IS}} = x_{min}^{\text{EQ}} \) , but then one finds that some neighbors have a displacement which is just above that threshold, and using the same  \( x_{min}^{EQ} \)  leads to false neighbor changes. Therefore, one needs to use  \( x_{cut}^{\text{IS}} > x_{cut}^{\text{EQ}} \)  to remove the false positives (see Fig. S2(a)), as already discussed in several previous studies [S3, S4]. Thus, we set  \( x_{cut}^{\text{IS}} = 1.5 \) .

Next, we consider the bond-insertion process. This can be viewed as a bond-breaking process for the time-reversal of the minimisation dynamics. Applying the same reasoning as above, we impose the condition  \( x_{cut}^{IS} < x_{cut}^{EQ} \)  to remove the false positives. Thus we set  \( x_{cut}^{IS} = 1.23 \) .

Once neighbors are defined, we determine the list of neighbors for each particle in both equilibrium  \( (L_{\mathrm{eq}}) \)  and inherent structure  \( (L_{\rm IS}) \)  configurations:  \( L_{eq} = \{l_{eq}\} \)  and  \( L_{IS} = \{l_{IS}\} \) , where  \( l_{eq} \)  and  \( l_{IS} \)  denote the identities of the neighbours. For each particle, say i, we define the number of bond breakings,  \( B_{i} \)  by counting particles with  \( l_{eq} \notin L_{IS} \) . We also count the number of bond insertions,  \( I_{i} \) , which is the number of particles with  \( l_{IS} \notin L_{EQ} \) . We note that our

![](./images/867745664589627861_14.jpg)

![](./images/867745664589627861_15.jpg)

![](./images/867745664589627861_16.jpg)

![](./images/867745664589627861_17.jpg)

![](./images/867745664589627861_18.jpg)

![](./images/867745664589627861_19.jpg)

FIG. S1. (a-c) The velocity  \( \langle|\boldsymbol{v}(t)|\rangle \)  as a function of time t of the two-dimensional harmonic-sphere, three-dimensional soft-sphere, and four-dimensional harmonic-sphere models for several system sizes. (d-f) The scaling plot using Eq. (S3) for the velocity decays.
 

choice of cutoff produces nearly identical mean values for  \( \overline{B}=\frac{1}{N}\sum_{i}B_{i} \)  and  \( \overline{I}=\frac{1}{N}\sum_{i}I_{i} \)  at all temperatures, meaning that the bond-breaking and bond-insertion processes take place with the same frequency, as expected.

Finally we define the defect order parameter  \( \phi_{i} \)  as follows:  \( \phi_{t}=1 \)  if  \( (B_{i}+I_{i})>0 \)  and  \( \phi_{i}=0 \)  if  \( (B_{i}+I_{i})=0 \) . It is useful to make the variable  \( \phi_{i} \)  binary, as it allows us to determine the absolute concentration of defects, defined as  \( \phi=\frac{1}{N}\sum_{i}\phi_{i} \) . In the main text, we report the behaviour of the average defect density,  \( \langle\phi\rangle \) , and of the corresponding collective susceptibility:  \( \chi=N(\langle\phi^{2}\rangle-\langle\phi\rangle^{2}) \) .

## IV. DISPLACEMENT FIELD

In Fig. S4, we show the displacement field  \( |\boldsymbol{r}_{i}(t)-\boldsymbol{r}_{i}({t}\to\infty)| \)  at temperatures T=0.2 and 0.035 and times  \( t=10^{-1} \) ,  \( 10^{0} \) ,  \( {10}^{1} \) , and  \( {10}^{2} \) . These two temperatures belong to the high- and low-temperature regimes, respectively (see Fig. 2(e)). At high temperature T=0.2, the displacement field reveals many defects at short times. At longer timescales, the number of localised defects decreases, but some of them survive for a very long time. When a defect disappears, particles around the defect rearrange and the velocity  \( \langle|\boldsymbol{v}(t)|\rangle \)  has a large sudden increase. The time-evolution of the displacement field at high temperature is consistent with the coarsening picture studied in the  \( T\to\infty \)  limit for harmonic spheres in Ref. [S6].

At lower temperature T = 0.0035, on the other hand, the displacement field is much smoother even at short times, and we hardly see localised defects. This smooth displacement field is consistent with a harmonic description, as shown in Sec.II C.

## A. Inherent structures from different algorithms

We show that localised defects affect the mapping between an equilibrium liquid microstate and a ‘corresponding’ minimum in the energy landscape, i.e. an inherent structure. Starting from the same initial equilibrium state, we minimize the energy using different algorithms available in LAMMPS [S8], namely conjugate gradient, FIRE [S7], and steepest descent. This exercise is done for the 2D system of polydisperse soft spheres. In all cases, we use the same tolerance thresholds (energy tolerance of  \( 10^{-16} \)  and force tolerance of  \( 1 \times 10^{-20} \)  [S9]) to end the convergence.

![](./images/867745664589627861_20.jpg)

FIG. S2. Bond-breaking (a) and bond-insertion (b) processes. Schematic pictures show a particle (particle 0) loses a bond (with particle 4) during the minimisation (a), or gains a new bond (with particle 8) (b). Neigbors are defined as a pair of particles closer than a cutoff  \( x_{cut}^{EQ} \)  (which depends on T) and  \( x_{cut}^{IS} \)  (which depends on the dynamic process under study).
 
![](./images/867745664589627861_21.jpg)

![](./images/867745664589627861_22.jpg)

FIG. S3. Radial distribution  \(  g(x_{ij})  \)  as functions of rescaled distances  \( x_{ij} = r_{ij}/d_{ij} \)  for the equilibrium (a) and inherent structure (b) states of the two-dimensional polydisperse soft sphere model. The curves are smoothed to determine the first minimum precisely. The system size N = 4000.

![](./images/867745664589627861_23.jpg)

FIG. S4. Displacement field  \( \left|\boldsymbol{r}_{i}(t)-\boldsymbol{r}_{i}(\infty)\right| \)  for the 2D soft sphere model at T=0.2 and 0.035.

to a local minimum. After obtaining the minima corresponding to the same initial state via the three different algorithms, we compute the distance between the minima obtained for each pair of these algorithms, which is given by  \( \left\langle\sqrt{\frac{1}{N}\sum_{i=1}^{N}\left|\boldsymbol{r}_{i}^{\mathrm{A}}-\boldsymbol{r}_{i}^{\mathbf{B}}\right|^{2}}\right\rangle \) , where  \( r_{i} \)  is the co-ordinate of the i-th particle in the configuration, and A,B represent labels corresponding to CG, SD, or FIRE. If the pair of minima are identical, this distance should be very close to zero (and is only set by the convergence criterion).

However, this is not what we observe, as shown in Fig. S5. Instead we find that the average distance is not given by the convergence criterion (it is much larger), and it depends continuously upon the temperature from where the initial state is sampled; it is larger for higher temperatures.

Only at very low temperatures in finite systems do we find that instances where the pair of minima obtained from different algorithms can become similar, within numerical resolution. In those cases, the initial equilibrium state rolls
 
![](./images/867745664589627861_24.jpg)

FIG. S5. The distance between the inherent-structure configurations of the two-dimensional soft-sphere model produced by the steepest descent (SD), conjugate gradient (CG), and FIRE algorithms  \( [S7] \) . N = 64000.

down to the same minimum, independent of the algorithm used and the mapping between an equilibrium liquid state and a local minimum in the energy landscape becomes unique. However, when increasing the system size and/or the temperature, these minima are always distinct and we suspect that this is always the case in the thermodynamic limit at any finite temperature. The difference between pairs of minima obtained from a given initial configuration is visualized in the main text.

[S1] P. Charbonneau, Y. Jin, G. Parisi, and F. Zamponi, Hopping and the Stokes–Einstein relation breakdown in simple glass formers, Proc. Natl. Acad. Sci. U.S.A. 111, 15025 (2014).

[S2] H. Ikeda, F. Zamponi, and A. Ikeda, Mean field theory of the swap monte carlo algorithm, J. Chem. Phys. 147, 234506 (2017).

[S3] R. Yamamoto and A. Onuki, Dynamics of highly supercooled liquids: Heterogeneity, rheology, and diffusion, Phys. Rev. E 58, 3515 (1998).

[S4] H. Shiba, T. Kawasaki, and A. Onuki, Relationship between bond-breakage correlations and four-point correlations in heterogeneous glassy dynamics: Configuration changes and vibration modes, Phys. Rev. E 86, 041504 (2012).

[S5] L. Berthier, D. Coslovich, A. Ninarello, and M. Ozawa, Equilibrium Sampling of Hard Spheres up to the Jamming Density and Beyond, Phys. Rev. Lett. 116, 238002 (2016).

[S6] R. N. Chacko, P. Sollich, and S. M. Fielding, Slow Coarsening in Jammed Athermal Soft Particle Suspensions, Phys. Rev. Lett. 123, 108001 (2019).

[S7] E. Bitzek, P. Koskinen, F. Gähler, M. Moseler, and P. Gumbsch, Structural Relaxation Made Simple, Phys. Rev. Lett. 97, 170201 (2006).

[S8] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, J. Comput. Phys. 117, 1 (1995).

[S9] The energy tolerance is defined as  \( \Delta E/E \) , where E is the total energy of the system and  \( \Delta E \)  is the energy difference between successive iterations during minimization. The force tolerance is defined as the length of the global force vector for all atoms, e.g. a vector of size 3N for N atoms. [S8].
 
