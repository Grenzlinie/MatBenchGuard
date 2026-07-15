
# Density-Jump Transitions in the Debye-Hückel Theory of Spin Ice and Electrolytes

Omar J. Abbas, \( ^{1,2} \)  Steven T. Bramwell, \( ^{1} \)  and Daan M. Arroo \( ^{1,3,*} \) 

 \( ^{1} \) London Centre for Nanotechnology and Department of Physics and Astronomy,

University College London, 17-19 Gordon Street, London WC1H 0AH, United Kingdom

 \( ^{2} \) Current address: London Centre for Nanotechnology and Department of Electronics and Electronic Engineering,

University College London, 17-19 Gordon Street, London WC1H 0AH, United Kingdom

 \( ^{3} \) Department of Materials, Imperial College London,

Exhibition Road, London SW7 2AZ, United Kingdom

Debye-Hückel theory, originally developed to describe dilute electrolyte solutions, has proved particularly successful as a description of magnetic monopoles in spin ice systems such as  \( Dy_{2}Ti_{2}O_{7} \) . For this model, Ryzhkin et al. predicted a phase transition in which the monopole density abruptly changes by several orders of magnitude but to date this transition has not been observed experimentally. Here we confirm that this transition is a robust prediction of Debye-Hückel theory, that does not rely on approximations made in the previous work. However, we also find that the transition occurs in a regime where the theory breaks down as a description of a Coulomb fluid and may be plausibly interpreted as an indicator of monopole crystallisation. By extending Ryzhkin's model, we associate the density jump of Debye-Hückel theory with the monopole crystallisation observed in staggered-potential models of 'magnetic moment fragmentation', as well as with crystallisation in conserved monopole-density models. The possibility of observing a true density-jump transition in real spin ice and electrolyte systems is discussed.

## I. INTRODUCTION

Frustrated magnetic materials have long been a focus of interest as systems in which large ground-state degeneracies can lead to the appearance of exotic states \( ^{1} \) . Prominent among these are spin ice systems \( ^{2,3} \)  such as  \( Dy_{2}Ti_{2}O_{7} \)  (DTO) and  \( Ho_{2}Ti_{2}O_{7} \)  (HTO), in which dipolar and exchange interactions between Ising-like rare-earth ions on a pyrochlore lattice lead to an extensively degenerate low temperature state in which each vertex of the pyrochlore lattice has two spins pointing in and two pointing out. This condition maps to the “ice rules” that govern proton disorder in water ice and hence spin ice and water ice share the same characteristic residual entropy per site first estimated by Pauling \( ^{4} \)  in 1935:

 \[ s_{0}\approx k_{\mathrm{B}}\ln\left(\frac{3}{2}\right). \quad (1) \] 

While at a basic level the natural models with which to describe such systems are the vertex models \( ^{5} \)  that were inspired by this feature of water ice \( ^{6} \) , a key insight in the study of spin ice systems has been that they can be usefully described in terms of an emergent Coulomb phase \( ^{7} \)  where spins are identified with the flux of a divergenceless field and ice rule defects carry a magnetic charge. Statics and dynamics can then be represented in terms of free magnetic monopoles that interact through a magnetic Coulomb interaction \( ^{8-10} \) .

Taking this picture of interacting magnetic charges seriously, the thermodynamics of monopoles in spin ice is elegantly captured by a “magnetolyte” model \( ^{11} \)  whose properties can be analysed in terms of Debye-Hückel theory, as applied to weak electrolytes \( ^{12,13} \) . The excitation of singly- and doubly-charged monopoles (3:1 vertices and all-in/all-out vertices, respectively) in the grand canonical ensemble is then analogous to ionisation in an electrochemical system of the form

 \[ 2\mathrm{H}_{2}\mathrm{O}\rightleftharpoons\mathrm{H}_{3}\mathrm{O}^{+}+\mathrm{OH}^{-}\rightleftharpoons\mathrm{H}_{4}\mathrm{O}^{2+}+\mathrm{O}^{2-} \quad (2) \] 

with the density of monopoles controlled by their respective chemical potentials. An equilibrium is reached in which charge correlations lead to an exponential screening of the Coulomb interactions between monopoles. When the grand canonical vacuum is identified as the Pauling ice state (with the associated residual entropy), Debye-Hückel theory applied to spin ice in this way provides remarkably good agreement with experiment \( ^{14} \)  and the theory has been widely used to describe a broad range of spin ice systems \( ^{15-17} \) .

There nevertheless remains an unresolved point of tension between the predictions of the Debye-Hückel magnetolyte model of spin ice and experimental measurements of real spin ice systems. Using parameters for HTO, an early work by Ryzhkin et al. \( ^{18} \)  shows that Debye-Hückel theory predicts a first-order phase transition at  \( T_{m} \approx 0.1887 \)  K in which the monopole density abruptly jumps by several orders of magnitude. A similar transition had previously been predicted within the framework of Debye-Hückel theory by Kozlov et al. \( ^{19} \) . Since Debye-Hückel theory is generally in excellent agreement with experiment as a model of spin ice systems, it is surprising that no experimental signatures of such a transition have been observed despite numerous studies having probed the relevant temperature regime for  \( HTO^{20-23} \) . It may be relevant that Ryzhkin et al. use certain approximations to the Debye-Hückel free energy and one might suspect that these either introduced a transition that does not occur without these approximations, or shifted it from a parameter range that has not yet been accessed experimentally. Hence it is useful to re-examine the problem using the Debye-Hückel theory developed by Kaiser et al. \( ^{14} \) , recapped below in Section II, which dispenses with
 

these approximations.
The first result of this paper, described in section III, is that the approximations made in the previous work do not introduce the transition, but removing them shifts it into a parameter range that is far from that applicable to HTO. More importantly, the transition occurs in a range where Debye-Hückel theory is no longer a formally valid description of the lattice Coulomb fluid, and where instead, there is monopole crystallisation \( ^{24,25} \) . We observe, however (section IV), that the Debye-Hückel theory nevertheless retains merit as a qualitative description of the lattice Coulomb fluid in this range, capturing important properties described in Ref. \( ^{25} \)  and clarifying how the model in this reference relates to an alternative model of crystallisation proposed by Borzi et al. \( ^{26} \) . The general conclusion (section V), then, is that either the transition of Ref. \( ^{18} \)  is a qualitative analogue of the crystallisation, or else it is a genuine liquid-liquid transition, but one that will be masked by crystallisation in a real lattice Coulomb fluid. We conclude by briefly speculating on the possibility of observing the transition in electrolyte systems.

## II. DEBYE-HÜCKEL THEORY

In this section we recap the full Debye-Hückel theory of the spin ice ‘magnetolyte’ as given by Kaiser et al. \( ^{14} \) . The magnetolyte model of spin ice begins by positing that the relevant degrees of freedom in spin ice systems are captured by a dilute ensemble of N singly- and  \( N_{2} \)  doubly-charged magnetic monopoles with respective chemical potentials  \( \mu < 0 \)  and  \( \mu_{2} = 4\mu \) . These may occupy any of the  \( N_{0} \)  sites of the diamond lattice with nearest-neighbour distance a and they interact with each other via a magnetic Coulomb potential, giving a Hamiltonian of the form

 \[ \mathcal{H}=\frac{1}{2}\sum_{i\neq j}\frac{\mu_{0}q_{i}q_{j}}{4\pi r_{i j}}-\mu N-\mu_{2}N_{2} \quad (3) \] 

where  \( q_{i,j} \in \{0, \pm Q, \pm 2Q\} \)  with Q a material-dependent elementary magnetic charge and  \( r_{ij} \)  the separation between sites i and j.

The behaviour of such an ensemble may be described by the free energy per site

 \[ f=u_{\mathrm{C}}-\mu n-\mu_{2}n_{2}-s T \quad (4) \] 

where  \( u_{C} \)  is the Coulomb energy per site, n and  \( n_{2} \)  are the respective site densities of singly- and double-charged monopoles, s denotes the entropy per site and T denotes the temperature of the ensemble. The challenge is in determining the equilibrium value of  \( u_{C} \) , since the long-range Coulomb interaction acts between every pair of magnetic charges.

Debye-Hückel theory tackles this problem by considering how spatial correlations between monopoles in the system affect the first term of Eq. 4. It is useful here to introduce the quantity  \( u(a) = \frac{\mu_{0}Q^{2}}{4\pi a} \)  as the Coulomb energy of a pair of singly charged monopoles separated by one lattice constant.

The total Coulomb energy of the system is determined by calculating the average energy associated with each monopole at a given monopole density  \( \rho_{\mathrm{I}} = (n + 4n_{2})/\bar{v} \) , where  \( \bar{v} = 8a^{3}/3\sqrt{3} \)  is the volume per site. Noting that in the vicinity of a given monopole one is more likely to find monopoles of opposite charge than of like charge, the linearised Poisson-Boltzmann equation may be solved to give a screened Coulomb potential which differs from the Coulomb term of Eq. 3 by a factor of  \( \exp(-r/l_{\mathrm{D}}) \) , where

 \[ l_{\mathrm{D}}=\sqrt{\frac{k_{\mathrm{B}}T}{\mu_{0}Q^{2}\rho_{\mathrm{I}}}} \quad (5) \] 

is the Debye length. The screening limits the average Coulomb energy of each monopole to that of the interaction between the monopole and its immediate atmosphere, giving \( ^{27} \) 

 \[ u_{\mathrm{C}}^{\mathrm{D H}}=-\frac{2k_{\mathrm{B}}T}{3\pi\sqrt{3}}\left[\ln\left(1+\frac{a}{l_{\mathrm{D}}}\right)-\left(\frac{a}{l_{\overline{{D}}}}\right)+\frac{1}{2}\left(\frac{a}{l_{\overline{{D}}}}\right)^{2}\right] \quad (6) \] 

To complete the expression for the free energy, the entropy per site for spin ice may be expressed in a low-density approximation as

 \[ \begin{align*}s=-k_{\mathrm{B}}\Biggl\{n\ln\left(\frac{n}{2}\right)+n_{2}\ln(2n_{2})\\+&(1-n-n_{2})\ln(1-n-n_{3})\\+&(1-n-n_{2})\ln\left(\frac{2}{3}\right)\Biggr\}.\end{align*} \quad (7) \] 

This approximate entropy expression returns negative values (rather than zero) when the density approaches unity. However in practice, the contribution of -sT to the free energy is always rather small when the negative entropy occurs so that its impact on observables is negligible. Since the expression in Eq. 7 accurately describes experimental data, we do not attempt to correct the negative entropy it assigns to high-density configurations, but simply note where it occurs.

From these equations and for a given chemical potential, one can calculate the equilibrium density that minimises the free energy as

 \[ n=\frac{\frac{4}{3}\exp\left(\beta\bar{\mu}\right)}{1+\frac{1}{3}[4\exp\left(\beta\bar{\mu}\right)+\exp\left(\beta\bar{{\mu}}_{2}\right)]} \quad (8) \] 

 \[ n_{2}=\frac{\frac{1}{3}\exp\left(\beta\bar{\mu}_{2}\right)}{1+\frac{1}{3}[4\exp\left(\beta\bar{\mu}\right)+\exp\left(\beta\bar{{\mu}}_{2}\right)]} \quad (9) \] 

where  \( \beta = 1/k_{B}T \)  and  \( \bar{\mu}, \bar{\mu}_{2} \)  are effective chemical potentials which depend on the Debye length and hence the monopole density as
 

 \[ \begin{aligned}\tilde{\mu}=\mu+\Delta^{\mathrm{DH}},\ \tilde{\mu}_{2}=\mu_{2}+4\Delta^{\mathrm{DH}}\\\Delta^{\mathrm{DH}}=k_{\mathrm{B}}T\frac{l_{\mathrm{T}}}{l_{\mathrm{D}}+a}.\end{aligned} \quad (10) \] 

From here it is possible to find solutions iteratively, alternately adjusting the effective chemical potential and density until a self-consistent solution is obtained.

The iteration will generally converge to a single free energy minimum, so if there is a double minimum in the free energy (as we expect for the first order transition), it is important to start the iteration at different initial densities, so that both minima can be found. The procedure that we settled on involved starting at a low temperature with initial densities set to zero, so that for the first iteration  \( \tilde{\mu} = \mu \)  and  \( \tilde{\rho}_{2} = \mu_{2} \) . This typically allows the iterative solution to converge within 10 steps. The temperature was then increased in steps of 10 mK, at each step using the converged  \( \tilde{\mu}_{i} \)  and  \( n_{i} \)  from the previous temperature as the starting point. Once a high temperature was reached, the system was cooled, again in small temperature steps, each time using the parameters from the previous step to start the iteration. In this way the cooling curve would give the absolute free energy minimum while the heating curve would follow a metastable minimum if there was one. Some tests showed that this procedure indeed located the correct (global) minima.

## III. RESULTS

## A. Monopole density and charge density

Using the physical quantities for dysprosium titanate  \( (a = 4.34 \, \text{\AA} \)  and magnetic charge  \( Q = 4.28 \times 10^{-13} \, \text{Am}) \)  and a variable chemical potential, effective chemical potentials  \( \tilde{\mu}_{i} \)  and monopole densities  \( n_{i} \)  (i = 1, 2 for singly- and doubly-charged monopoles respectively) were iterated to convergence as described above.

Fig. 1 illustrates the resulting curves of total monopole density per site,  \( n_{tot} = n_{1} + n_{2} \) , versus temperature. First order phase transitions are observed at bare chemical potentials of  \( |\mu| \lesssim 1.6 \)  K, with larger magnitude transitions at smaller temperatures. The heating/cooling cycle reveals hysteresis in these transitions, with the cooling curve generally finding the stable free energy minimum (full lines in Fig.1). Our results, however, indicate three regimes, depending on chemical potential: (i) For small  \( |\mu| \lesssim 1.3 \)  K, the lowest temperature state has equilibrium single-monopole densities approaching unity, while the free energy minimum found by heating is metastable up to the transition. The unit density state is reached at temperatures much higher than the first order transition, which only occurs for the metastable heating curve: that is, there is no equilibrium first order transition, but the first order transition does persist as a metastable feature. (ii) For  \( 1.6 \, K \gtrsim |\mu| \gtrsim 1.3 \, K \) , the single monopole equilibrium density falls to zero at low temperature and the heating curve is metastable only in the vicinity of the transition. Here there is an equilibrium first order transition between high and low density monopole states with thermal hysteresis in the total monopole density. (iii) At  \( |\mu| \gtrsim 1.6 \, K \)  there is a unique free energy minimum which is followed in both the heating and cooling curves, and hence no first order transition.

![](./images/939222012528689483_1.jpg)

FIG. 1. Total monopole density  \( n_{tot} = n + n_{2} \)  as a function of temperature for varying chemical potentials  \( \mu \)  with  \( \mu_{2} = 4\mu \) . Solid lines represent cooling curves (representing the true equilibrium state) and dashed lines represent heating curves (metastable where they deviate from the full lines). There is a first order transition and associated hysteresis when  \( 1.6 K \gtrsim |\mu| \gtrsim 1.3 K \) .

The evolution of the normalised charge density per site  \( (n + 2n_{2})/2 \)  with temperature and chemical potential directly reflects the properties described above. Fig. 2 shows the equilibrium charge density as a function of  \( |\mu| \)  and T, with a short line of first order phase transitions near to  \( |\mu| = 1.5 \)  K and  \( T \rightarrow 0 \) .

## B. Specific heat

Computing the specific heat as a function of temperature (Fig. 3) sheds further light on the nature of the three regimes (i) - (iii) identified in the previous section. In regime (i), the cooling (equilibrium) curve features a single broad peak associated with the crossover from a single-monopole dominated limit at high temperatures to a double-monopole dominated limit. At low temperatures, the large area under this peak is a result of the negative entropy assigned to configurations with monopole densities approaching unity, discussed where Eq. 7 was introduced. At lower temperatures, the heating (metastable) curve has a second very sharp peak where the double-monopole density discontinuously jumps by many orders of magnitude. The “monopole density inversion” where
 
![](./images/939222012528689483_2.jpg)

FIG. 2. The normalised equilibrium charge density  \( (n + 2n_{2})/2 \) , computed as a function of  \( |\mu| \)  and T, with standard material parameters for  \( Dy_{2}Ti_{2}O_{7} \)  and  \( \mu_{2} = 4\mu \) . Note the line of first order phase transitions near to  \( |\mu| = 1.5 \)  K and  \( T \rightarrow 0 \) .

![](./images/939222012528689483_3.jpg)

FIG. 3. Specific heat as a function of temperature for varying monopole chemical potential  \( \mu \) , showing three distinct regimes as in Fig. 1. The cooling (equilibrium) curves are solid, with the heating (metastable) curves dashed.

the  \( n_{2} \)  becomes greater than  \( n_{1} \)  is discussed further in the following subsection.

In regime (ii) the specific heat diverges when both the single- and double-monopole densities abruptly increase with the temperature by several orders of magnitude, with the thermal hysteresis in the monopole densities reflected in a shift in the temperature at which the divergence occurs. Close to these critical temperatures the specific heat has the asymmetric form characteristic of a mean field transition, as might be expected in this effective field model. In contrast to regime (i),  \( n_{1} \)  remains greater than  \( n_{2} \)  for all temperatures.
In regime (iii) with  \( |\mu| > 1.6 \)  K the heating and cooling curves are identical, with broad, continuous peaks in specific heat with larger  \( |\mu| \)  shifting the peaks to higher temperatures. These peaks are the familiar Schottky anomalies associated with single monopole activation as the temperature approaches their chemical potential. As for regime (ii),  \( n_{1} \)  remains greater than  \( n_{2} \)  for all temperatures.

## C. Monopole density inversion

In the canonical model of classical spin ice, the chemical potential for doubly charged monopoles is always four times that for singly charged monopoles. Hence in the low density and low temperature limit, for larger chemical potentials,  \( n_{2} \ll n_{1} \) , while in the high temperature limit,  \( n_{2} = 1/8 \)  and  \( n_{1} = 1/2 \) . However, we discovered that below the first order transition at  \( |\mu| \approx 1.5 \)  K, doubly-charged monopoles dominate and displace singly charged monopoles, then remaining dominant while the system remains in a high monopole density state. This behaviour is illustrated in Fig. 4 for  \( |\mu_{1}| = 1 \)  K, i.e. in regime (iii) above. At equilibrium (full line in figure) double monopoles smoothly start to dominate below  \( T \sim 1 \)  K. Although there is no density jump at equilibrium, there is a metastable first order transition in the heating curve at  \( T \sim 0.1 \)  K, where the relative site densities of single and double charge monopoles invert to reach the equilibrium values.

![](./images/939222012528689483_4.jpg)

FIG. 4. Single  \( (n) \)  and double  \( (n_{2}) \)  monopole site densities as a function of temperature for  \( |\mu|=1.00 \)  K with  \( \mu_{2}=4\mu \) . Solid lines represent cooling curves at equilibrium while dashed lines indicate heating curves which are metastable where they do not coincide with the cooling curves.

For a more general case (not shown), it is interesting to relax the constraint that  \( \mu_{2}=4\mu \) . For  \( \mu_{1}<4\mu \)  this allows the double monopoles to dominate for a larger temperature range immediately above the first-order transi-
 

tion, while for  \( \mu_{2} \gg 4\mu \)  the inversion is suppressed and single monopoles remain dominant in both the low- and high-density states. We discuss in Section IV how a staggered interaction relevant to spin ice iridates can lead to “dressed” chemical potentials that effectively break the constraint  \( \mu_{2} = 4\mu \) .

## D. Transitions in electrolytes

Since the Debye-Hückel picture outlined above can in principle be applied to electrolytes in general, it is natural to ask whether the first-order transition described in this work is relevant to other systems.

One difference between spin ice and an ordinary electrolyte is that spin ice has a structured vacuum for charge excitations, which is reflected in the details of the entropy, Eqn. 7. Specialising to the case of single charges (density n), a symmetric lattice electrolyte may be described by the equations used here, provided Eqn. 7 is replaced by the primitive electrolyte entropy \( ^{14} \) :

 \[ S_{\mathrm{e}}=-k_{\mathrm{B}}N_{0}\left[n\log(n/2)+(1-n)\log(1-n)\right]. \quad (11) \] 

It was confirmed that the first order transition is maintained when this entropy expression is used in place of Eqn. 7. To give some sense of the magnitudes involved we refer to the table of electrolyte parameters given by Kaiser et al. in Ref. \( ^{[28]} \) . Results for various electrolytes were generated using these parameters and the primitive entropy, including the case of water ice (where the ice entropy was used) and spin ice with as a comparison. These results are illustrated in Fig. 5. There is a first order transition for silicate glass  \( \left(\mathrm{Na}-\mathrm{Ca}-\mathrm{SiO}_{2}\right) \)  and a metastable one for methemoglobin. Whether or not the real systems would display such transitions is discussed subsequently.

## E. Breakdown of Debye-Hückel theory

The question arises, do the transitions observed occur in a parameter range where Debye-Hückel theory gives a valid description of the Coulomb fluid? To explore this question, we specialise to the single-charge case and define parameters  \( l = l_{T}/a \) ,  \( \nu = -\mu/k_{B}T \) . Note that l may be expressed equivalently as  \( l = u(a)/2k_{B}T \) , where  \( u(a) = \mu_{0}Q^{2}/4\pi a \)  as before. It is then easily shown that there are turning points in the free energy when

 \[ \phi_{\nu,l}(n)\equiv n\left(1+(3/4)e^{\nu-\frac{l\sqrt{n l}}{\sqrt{n l}+c}}\right)=1 \quad (12) \] 

where  \( c = 1/(\sqrt{\pi}3^{3/4}) \approx 0.2475 \) . We can study this equation for the case of  \( nl \ll c \)  and  \( nl \gg c \)  respectively:

 \[ n\left(1+(3/4)e^{\nu}\right)=1\qquad n\left(1+(3/4)e^{\nu-l}\right)=1. \quad (13) \] 

Each of these equations has only one solution. However, three solutions, that we interpret as two minima

![](./images/939222012528689483_5.jpg)

FIG. 5. Comparison of monopole densities against temperature (in the reduced units of Ref. \( ^{28} \)  for several ice-type and electrolyte systems. Note that 'spin ice' here is a hypothetical system with  \( |\mu|=1.00 \)  K and otherwise,  \( Dy_{2}Ti_{2}O_{7} \)  parameters, while other systems have realistic parameters as estimated in Ref. \( ^{28} \) . With the exception of the silicate glass \( ^{29} \) , it seems that the equilibrium phase transition is not generally available in these systems. Here the dimensionless temperature is defined as  \( T^{*}=k_{\mathrm{B}}T/u(a) \)  where  \( u(a) \)  is defined in Section II.

and a maximum in the free energy, can arise when there is a crossover between the two limiting forms (Fig. 6). From inspection, this requires  \( l \sim \nu \)  which evaluates to  \( (u(a)/2) \approx |\mu| \) , that is, half the Coulomb energy ( \( u \approx 3 \)  K) of a pair at contact – as we have observed, there is indeed an equilibrium transition for  \( |\mu| \approx 1.5 \)  K. In addition, it is clear from inspection that  \( l, \nu \)  need to be quite large, of order 10 or more, for there to be multiple minima.

On the other hand, the formal criterion for Debye-Hückel theory to be valid is that the total magnetostatic energy in a potential  \( \Phi \)  dominates the thermal energy scale,  \( 1 \gg Q\Phi/k_{B}T = 2\Delta_{\mathrm{DH}}(l_{D}/a) \) , which becomes:

 \[ 1\gg\frac{2\sqrt{\pi}l}{3^{3/4}\sqrt{\pi n l}+1}. \quad (14) \] 

The right hand side of this equation is a monotone decreasing function of n so we can identify  \( l^{max} \approx 1.82 \)  as the solution for n = 1. There is only one solution to Eqn. 12 for all values of  \( \nu \)  for  \( l \leq l^{max} \) , suggesting that the first order transition occurs in a parameter regime where Debye-Hückel theory breaks down.

One can expect the Bjerrum correction for bound pairs, as applied in Ref. \( ^{[28]} \) , to extend the range of validity of the theory to values of l rather larger than  \( l_{max} \) , but as illustrated in Fig. 6, the length l is always large at the transition and it seems unlikely that Debye-Hückel-Bjerrum theory can ever be strictly valid in this regime. Physically, such large values of l indicate a tendency to pairing,
 
![](./images/939222012528689483_6.jpg)

![](./images/939222012528689483_7.jpg)

FIG. 6. The Debye-Hückel free energy has equilibria where the function  \( \phi_{l,\nu}(n)=1 \)  (Eqn. 12)). Here we plot  \( \phi_{l,\nu}(n) \)  versus density n for different values of l and  \( \nu \) , while the straight dashed lines represent the limiting forms for small and large nl (left and right, respectively) (Eqn. 13). Equilibrium solutions for n occur where the solid curves intersect the dotted line at  \( \phi=1 \)  (see Eqn. 12). The upper plot has  \( \nu=10 \)  and (curves, left to right) l=9, 9.5, 10; the lower plot has  \( \nu=20 \) , l=30.

or strong correlation, driven by the Coulomb interaction. But more realistically, while the Debye-Hückel theory can only describe a fluid to fluid transition, for  \( |\mu| \leq \mu_{c} \)  (i.e. the regime of interest) it has been shown that the system is unstable against crystallisation, driven by a favourable Madelung energy \( ^{25} \) , and it may be reasonable to interpret the transition in the linearised Debye-Hückel theory as a remnant of this.

## IV. EFFECT OF A STAGGERED POTENTIAL

In light of an apparent relation to monopole crystallisation transitions at low temperatures, it is interesting to explore whether Debye-Hückel theory can be brought into contact with other models of spin ice that predict crystallisation. These models may be separated into monopole-conserving models \( ^{26,30} \)  in which charge-ordering is observed at high densities and models associated with the literature of spin ice fragmentation \( ^{24,25,31-33} \) . The most general case of the latter, as described by Raban et al. \( ^{25} \) , supplements the Hamiltonian of the dipolar spin ice model in the dumbbell picture with a staggered interaction, giving

 \[ \mathcal{H}=\frac{u(a)}{2}\sum_{i\neq j}\frac{a}{r_{i j}}\hat{n}_{i}\hat{n}_{j}-\mu\sum_{i}\hat{n}_{i}^{2}-\Delta\sum_{i}(-1)^{i}\hat{n}_{i} \quad (15) \] 

where  \( u(a) = \frac{\mu_{0}Q^{2}}{4\pi a} \)  (see above),  \( \hat{n}_{i} = \pm 1, \pm 2 \)  is the monopole occupation number for the ith site and  \( \Delta > 0 \)  is the strength of a staggered field. The first two terms are the same Coulomb interaction and chemical potential we have treated already, while the staggered field introduced here promotes ordered monopole states by shifting the energy cost of introducing monopoles from  \( \mu \rightarrow \mu \pm \Delta \)  for isolated single monopoles and from  \( 4\mu \rightarrow 4\mu \pm 2\Delta \)  for isolated double monopoles, with the sign depending on whether the monopole is on an odd or even site. Such staggered potentials have been explored in the context of  \( \mathrm{Ho}_{2}\mathrm{Ir}_{2}\mathrm{O}_{7} \)  ( \( \mathrm{HIO}^{34} \) ), in which both  \( Ho^{3+} \)  and  \( Ir^{4+} \)  ions have a net magnetic moment. The  \( Ir^{4+} \)  ions, which sit on a pyrochlore lattice that intersects with the  \( Ho^{3+} \)  pyrochlore structure, undergo an ordering transition to an antiferromagnetic all-in-all-out arrangement at temperatures well above the Coulomb scale. The internal magnetic fields generated by the  \( Ir^{4+} \)  sublattice thus have a staggered structure that promotes staggered order in the  \( Ho^{3+} \)  moments.

As well as distinguishing alternate lattice sites, the staggered field term will also tend to increase the monopole population at a given temperature since  \( e^{\beta(\mu+\Delta)} + e^{\beta(\mu-\Delta)} \geq 2e^{\beta\mu} \)  for all  \( \Delta \geq 0 \) . We can incorporate this latter effect into our Debye-Hückel picture by introducing a “dressed” chemical potential  \( \mu^{\star} \)  that averages the contributions from odd and even sites so that

 \[ e^{\beta\mu^{\star}}=\frac{1}{2}\left(e^{\beta(\mu+\Delta)}+e^{\beta(\mu-\Delta)}\right). \quad (16) \] 

This may be solved to give an expression for the (temperature-dependent) dressed chemical potential in terms of bare chemical potential and the staggered field strength

 \[ \mu^{\star}=\mu+\frac{\ln\left(\cosh(\beta\Delta)\right)}{\beta}\approx\mu+\Delta-\frac{\ln(2)}{\beta} \quad (17) \] 

where the approximate form is obtained by expanding the  \( \cosh(\beta\Delta) \)  term for large  \( \beta\Delta \)  (in practice, the approximate form converges rapidly and is already highly accurate for  \( \beta\Delta\gtrsim1 \)  as seen in Fig. 7). We see immediately that  \( \mu^{\star}>\mu\ \forall\beta,\Delta \)  so that monopole populations will be greater than without the staggered potential, as expected. We similarly obtain

 \[ \mu_{2}^{\star}=4\mu+\frac{\ln\left(\cosh(2\beta\Delta)\right)}{\beta}\approx4\mu+2\Delta-\frac{\ln(2)}{\beta} \quad (18) \]
 

so that varying the strength of the staggered field has the effect of allowing the ratio  \( \mu_{2}^{\star}/\mu^{\star} \)  to take arbitrary values.

![](./images/939222012528689483_8.jpg)

FIG. 7. The exact (solid) and approximate (dashed) forms of the dressed potentials  \( \mu^{\star} \) ,  \( \mu_{2}^{\star} \)  (Eqs. 17 and 18, respectively) as a function of the staggered potential  \( \Delta \)  with  \( \mu = -4.35 \)  K and  \( \beta = 1 K^{-1} \) . The points where  \( \mu^{\star} \)  crosses zero and where  \( \mu_{2}^{\star} \)  becomes greater than  \( \mu^{\star} \)  form the zero-temperature phase boundaries between the monopole vacuum and single- and double-monopole crystal phases for the non-interacting limit ( \( Q \rightarrow 0 \) ).

In the non-interacting limit  \( (Q \rightarrow 0) \) , we may readily use these approximate forms to determine the low-temperature phase boundaries between the vacuum, single-monopole crystal and double-monopole crystal phases (Fig. 7). The low-density phase occurs when  \( \mu_{2}^{\star} < \mu^{\star} < 0 \) , so that it is difficult to excite any monopoles. As  \( \Delta \)  is increased,  \( \mu^{\star} \)  becomes positive when  \( \Delta > -\mu + \ln(2)/\beta \)  which defines the first phase boundary. The double-monopole crystal phase is reached when  \( 0 < \mu^{\star} < \mu_{2}^{\star} \) , corresponding to the phase boundary  \( \Delta = -3\mu \) . At zero temperature, these phase boundaries are in exact agreement with those identified by Raban et al. \( ^{25,35} \)  based on an analogy with the S = 2 Blume-Capel model.

For the interacting case  \( (Q \neq 0) \) , charge screening reduces the magnitude of the effective chemical potentials as seen in previous sections, shifting the phase boundaries down to lower  \( \Delta \) . Figure 8 shows the equilibrium charge densities as a function of temperature and the staggered potential  \( \Delta \)  for both the non-interacting and interacting case. To determine the effect of incorporating charge screening on the phase boundaries we may use the zero-temperature correction to the dressed chemical potential,  \( \Delta^{\mathrm{DH}}(T = 0) = \frac{\mu_{0}Q^{2}}{8\pi a} \) , which is independent of the monopole densities. We may then obtain the zero-temperature phase boundaries as before by looking at the

![](./images/939222012528689483_9.jpg)

![](./images/939222012528689483_10.jpg)

FIG. 8. Monopole charge density  \( \phi = n + 2n_{2} \)  in the non-interacting limit (above) and in the case of interacting monopoles (below) calculated using material parameters for DTO with  \( \mu = -4.35 \)  K and an additional staggered field  \( \Delta \) . Low-temperature phase boundaries in the non-interacting limit agree with the crossing points identified in Fig. 7. In the interacting case, Coulomb interactions suppress the single-monopole crystal phase (where  \( \phi \approx 1 \) ) and shift the low-temperature phase boundaries down to lower values of  \( \Delta \)  given by Eqns. 19 and 20, in remarkable agreement with previous results by Raban et al. \( ^{25} \) .

hierarchy of 0,  \( \tilde{\mu}^{\star} \)  and  \( \tilde{\pmb{\mu}}_{2}^{\star} \) , giving

 \[ \Delta_{\mathrm{V a c}\leftrightarrow1\mathrm{M P}}=-\left(\mu+\frac{\mu_{0}Q^{2}}{8\pi a}\right), \quad (19) \] 

 \[ \Delta_{\mathrm{1MP}\leftrightarrow2\mathrm{MP}}=-3\left(\mu+\frac{\mu_{0}Q^{2}}{8\pi a}\right) \quad (20) \] 

(where Vac = vacuum and MP = monopole). Since  \( \Delta \)  is strictly positive, we can immediately conclude that no phase transitions are possible when  \( |\mu| < \frac{\mu_{0}Q^{2}}{8\pi a} \) , in agreement with the results of Section III A and the arguments in Section III E. We further see that the single monopole crystal phase only has a small window of stability when
 

 \( |\mu| \)  approaches  \( \frac{\mu_{0}Q^{2}}{8\pi a} \)  from above. We finally note that the phase boundaries in Equations 19 and 20 again show remarkable agreement with those obtained by Raban et al. in their model, with the exception that in their boundaries the  \( \frac{\mu_{0}Q^{2}}{8\pi a} \)  is multiplied by the Madelung constant for their system,  \( \alpha = 1.638 \) . Within Debye-Hückel theory we can argue that the effective Madelung constant is  \( \alpha = 1 \) , i.e. if the Madelung energy per site is written as  \( E = -\alpha z^{2}\mu_{0}Q^{2}/8\pi a \)  (where z is the charge number) then  \( \alpha = 1 \)  equates to the energy per charge of a pair of equal and opposite charges. So we may conclude that the monopole density-jump transitions of the magnetolyte model of spin ice is the “attempt” of Debye-Hückel theory to capture the monopole crystallisation seen in staggered potential models.

The Debye-Hückel model additionally gives insight into the nature of monopole crystallisation in staggered potential models. Naively, one might expect that the transition to a staggered-ordered state is induced solely by the change of symmetry introduced by the staggered potential  \( \Delta \) . However, in addition to the symmetry change, there is already an instability to monopole crystallisation that results from the runaway excitation of monopoles due to charge-screening lowering the effective chemical potential of each additional monopole. In the Debye-Hückel “dressed chemical potentials” picture presented here, this process is the only mechanism available, since the symmetry of the staggered potential has not been taken into account. Hence, in contrast to the case of the staggered-potential model \( ^{25} \) , monopole crystallisation does not require a potential that explicitly breaks the symmetry of the dipolar spin ice model. The remarkable similarity between the phase boundaries of the staggered-potential and the dressed chemical potential models implies that reducing the effective chemical potential is what in fact drives the transition and the only role left for the staggered potential is to pick one of the two “all-in, all-out” states.

## V. CONCLUSIONS

In conclusion, motivated by the arguments of Ryzhkin et al. \( ^{18} \) , we have had examined the possibility of density-jump transitions in the Debye-Hückel theory of spin ice, as formulated by Kaiser et al. \( ^{14} \) . While we conclude with certainty that such transitions do occur in the theory, it seems very likely that they represent the “closest approach” of Debye-Hückel theory to the true situation, as exposed by Raban et al. \( ^{25} \) , where the transitions become monopole crystallisations. We have shown that Debye-Hückel theory and its extensions do a surprisingly good job at capturing the true behaviour if one equates full site occupation to crystallisation.

Interpreted in this way, our analysis has value in understanding the monopole crystallisation transitions observed in the staggered-potential models of Ref. \( ^{25} \) , showing that the transitions are largely a consequence of the Coulomb interaction and magnitude of the chemical potential, rather than of the explicit symmetry-breaking introduced by the staggered potential. Debye-Hückel theory may therefore serve as a useful bridge between staggered potential models and monopole-conserving models \( ^{26,30} \)  in which charge ordering occurs spontaneously at certain fixed monopole densities. Recent progress in experimentally determining the monopole density in HIO via magnetoresistance measurements \( ^{36} \) , means that it should be possible to directly compare the behaviour of the monopole density in a staggered potential system with predictions of the Debye-Hückel model with dressed chemical potentials.

The alternative interpretation is that, either in spin ice systems or equivalent electrolytes, the transitions hint at true liquid-liquid transitions (i.e. jumps in charge density without crystallisation), as originally envisaged by Ryzhkin et al. \( ^{18} \)  For this to occur in real systems, one would presumably need to frustrate the crystallisation through supercooling \( ^{37} \)  or by removing the lattice as in electrolyte solutions (where the dielectric permittivity provides a further degree of freedom \( ^{19} \) ) and glassy solid-state electrolytes \( ^{38-40} \) . Therefore, one place to search for such transitions might be the silicate glass system \( ^{29} \)  discussed in Ref. \( ^{28} \)  and Section III D, where the parameters seem to be in the correct range.

An essential problem remains that the strong nonlinearities of Debye-Hückel theory, that give rise to the transitions, are also associated with the breakdown of the theory as an accurate description of the Coulomb fluid. Therefore while the theory presents an interesting example of a self-consistent model of liquid-liquid transitions that qualitatively describes transitions in certain physical systems, it is unlikely to be quantitative in this regard.

Since Debye-Hückel theory and ideas from the spin-fragmentation picture have been successfully applied to artificial spin ice systems \( ^{17,41} \) , the inherent versatility of artificial spin systems could provide another avenue for exploring density-jump transitions in a regime where crystallisation is frustrated. This could take the form of a system that “locally” resembles spin ice (i.e., vertices of coordination four that obey ice rules in the ground state) but is spatially disordered globally so that monopoles cannot form a lattice. Such systems have been realised previously by designing systems in which the spin-lattice itself is non-periodic \( ^{42-44} \)  or by employing lattices where topological constraints prevent global ordering \( ^{45} \) .

While careful attention should be paid to how the Debye-Hückel model breaks at high monopole densities, the model may thus prove useful nevertheless in describing and interpreting density transitions in certain electrolytes, artificial spin systems and spin ice iridates.

## ACKNOWLEDGMENTS

We acknowledge support from the Leverhulme Trust through Grant No. RPG-2016-391. D.M.A. acknowl-
 

 \( ^{*} \)  d.arroo14@imperial.ac.uk

 \( ^{1} \)  A. P. Ramirez, Annual Review of Materials Science 24, 453 (1994).

 \( ^{2} \)  C. Castelnovo, R. Moessner, and S. Sondhi, Annual Review of Condensed Matter Physics 3, 35 (2012).

 \( ^{3} \)  S. T. Bramwell and M. J. Harris, J. Phys.: Condens. Matter 32, 374010 (2020).

 \( ^{4} \)  L. Pauling, J. Am. Chem. Soc. 57, 2680 (1935).

 \( ^{5} \)  R. J. Baxter, Exactly Solved Models in Statistical Mechanics (Academic Press, New York, 1982).

 \( ^{6} \)  E. H. Lieb, Phys. Rev. 162, 162 (1967).

 \( ^{7} \)  C. L. Henley, Annual Review of Condensed Matter Physics 1, 179 (2010).

 \( ^{8} \)  I. A. Ryzhkin, J. Exp. Theor. Phys. 101, 481 (2005).

 \( ^{9} \)  C. Castelnovo, R. Moessner, and S. L. Sondhi, Nature 451, 42 (2008).

 \( ^{10} \)  C. Castelnovo and P. C. W. Holdsworth, “Modelling of classical spin ice: Coulomb gas description of thermodynamic and dynamic properties,” in Spin Ice, edited by M. Udagawa and L. Jaubert (Springer International Publishing, Cham, 2021) pp. 143–188.

 \( ^{11} \)  C. Castelnovo, R. Moessner, and S. L. Sondhi, Phys. Rev. B 84, 144435 (2011).

 \( ^{12} \)  P. Debye and E. Hückel, Physikalische Zeitschrift 24, 185 (1923).

 \( ^{13} \)  W. Moore, Physical Chemistry, Prentice-Hall Chemistry Series (Prentice-Hall, 1964).

 \( ^{14} \)  V. Kaiser, J. Bloxsom, L. Bovo, S. T. Bramwell, P. C. W. Holdsworth, and R. Moessner, Phys. Rev. B 98, 144413 (2018).

 \( ^{15} \)  H. D. Zhou, S. T. Bramwell, J. G. Cheng, C. R. Wiebe, G. Li, L. Balicas, J. A. Bloxsom, H. J. Silverstein, J. S. Zhou, J. B. Goodenough, and J. S. Gardner, Nat. Commun. 2, 478 (2011).

 \( ^{16} \)  F. K. K. Kirschner, F. Flicker, A. Yacoby, N. Y. Yao, and S. J. Blundell, Phys. Rev. B 97, 140402 (2018).

 \( ^{17} \)  A. Farhan, M. Saccone, C. F. Petersen, S. Dhuey, R. V. Chopdekar, Y.-L. Huang, N. Kent, Z. Chen, M. J. Alava, T. Lippert, A. Scholl, and S. van Dijken, Science Advances 5 (2019), 10.1126/sciadv.aav6380.

 \( ^{18} \)  I. A. Ryzhkin, A. V. Klyuev, M. I. Ryzhkin, and I. V. Tsybulin, JETP Lett. 95, 302 (2012).

 \( ^{19} \)  V. Kozlov, S. Sokolova, and N. Trufanov, Sov. Phys. JETP 71, 1224 (1990).

 \( ^{20} \)  M. J. Harris, S. T. Bramwell, D. F. McMorrow, T. Zeiske, and K. W. Godfrey, Phys. Rev. Lett. 79, 2554 (1997).

 \( ^{21} \)  K. Matsuhira, Y. Hinatsu, K. Tenya, and T. Sakakibara, J. Phys.: Condens. Matter 12, L649 (2000).

 \( ^{22} \)  J. P. Clancy, J. P. C. Ruff, S. R. Dunsiger, Y. Zhao, H. A. Dabkowska, J. S. Gardner, Y. Qiu, J. R. D. Copley, T. Jenkins, and B. D. Gaulin, Phys. Rev. B 79, 014408 (2009).

 \( ^{23} \)  C. Paulsen, S. R. Giblin, E. Lhotel, D. Prabhakaran, K. Matsuhira, G. Balakrishnan, and S. T. Bramwell, Nature Communications 10, 1509 (2019).

 \( ^{24} \)  M. E. Brooks-Bartlett, S. T. Banks, L. D. C. Jaubert, A. Harman-Clarke, and P. C. W. Holdsworth, Phys. Rev. X 4, 011007 (2014).

 \( ^{25} \)  V. Raban, C. T. Suen, L. Berthier, and P. C. W. Holdsworth, Phys. Rev. B 99, 224425 (2019).

 \( ^{26} \)  R. A. Borzi, D. Slobinsky, and S. A. Grigera, Phys. Rev. Lett. 111, 147204 (2013).

 \( ^{27} \)  Note that this corrects an error in the expression given for the Coulomb energy in Equation 13 of Ref. \( ^{14} \) , which is too small by a factor of four; the error does not propagate into the results of that paper.

 \( ^{28} \)  V. Kaiser, S. T. Bramwell, P. C. W. Holdsworth, and R. Moessner, Nature Mater. 12, 1033 (2013).

 \( ^{29} \)  M. Ingram, C. Moynihan, and A. Lesikar, Journal of Non-Crystalline Solids 38-39, 371 (1980), xIIth International Congress on Glass.

 \( ^{30} \)  P. C. Guruciaga, S. A. Grigera, and R. A. Borzi, Phys. Rev. B 90, 184423 (2014).

 \( ^{31} \)  S. Petit, E. Lhotel, B. Canals, M. C. Hatnean, J. Ollivier, H. Mutka, E. Ressouche, A. R. Wildes, M. R. Lees, and G. Balakrishnan, Nature Physics 12, 746 (2016).

 \( ^{32} \)  E. Lhotel, L. D. C. Jaubert, and P. C. W. Holdsworth, J. Low Temp. Phys. 201, 710 (2020).

 \( ^{33} \)  V. Raban, L. Berthier, and P. C. Holdsworth, Physical Review B 105, 134431 (2022).

 \( ^{34} \)  E. Lefrançois, V. Cathelin, E. Lhotel, J. Robert, P. Lejay, C. V. Colin, B. Canals, F. Damay, J. Ollivier, B. Fák, L. C. Chapon, R. Ballou, and V. Simonet, Nature Communications 8, 209 (2017).

 \( ^{35} \)  V. Raban, Dynamique hors équilibre des monopoles magnétiques dans la glace de spin, Ph.D. thesis, Université de Lyon (2018), NNT: 2018LY-SEN052. tel-01974349.

 \( ^{36} \)  M. J. Pearce, K. Götze, A. Szabó, T. S. Sikkenk, M. R. Lees, A. T. Boothroyd, D. Prabhakaran, C. Castelnovo, and P. A. Goddard, Nature Communications 13, 444 (2022).

 \( ^{37} \)  E. R. Kassner, A. B. Eyvazov, B. Pichler, T. J. S. Munsie, H. A. Dabkowska, G. M. Luke, and J. C. S. Davis, Proc. Natl. Acad. Sci. U.S.A. 112, 8549 (2015).

 \( ^{38} \)  M. Tomozawa, J. Cordaro, and M. Singh, Journal of Non-Crystalline Solids 40, 189 (1980), proceedings of the Fifth University Conference on Glass Science.

 \( ^{39} \)  V. K. Deshpande, IOP Conference Series: Materials Science and Engineering 2, 012011 (2009).

 \( ^{40} \)  Z. A. Grady, C. J. Wilkinson, C. A. Randall, and J. C. Mauro, Frontiers in Energy Research 8, 218 (2020).

 \( ^{41} \)  B. Canals, I.-A. Chioar, V. Nguyen, M. Hehn, D. Lacour, F. Montaigne, A. Locatelli, T. O. Mentes, B. S. Burgos, and N. Rougemaille, Nature Communications 7, 11446 (2016).

 \( ^{42} \)  D. Shi, Z. Budrikis, A. Stein, S. A. Morley, P. D. Olmsted, G. Burnell, and C. H. Marrows, Nature Physics 14, 309 (2018).

 \( ^{43} \)  M. Saccone, A. Scholl, S. Velten, S. Dhuey, K. Hofhuis, C. Wuth, Y.-L. Huang, Z. Chen, R. V. Chopdekar, and A. Farhan, Physical Review B 99, 224403 (2019).

 \( ^{44} \)  M. Saccone, K. Hofhuis, D. Bracher, A. Kleibert, S. van Dijken, and A. Farhan, Nanoscale 12, 189 (2020).

 \( ^{45} \)  M. J. Morrison, T. R. Nelson, and C. Nisoli, New Journal of Physics 15, 045009 (2013).
 
