
# Phase separation in binary Bose mixtures at finite temperature

Gabriele Spada \( ^{1*} \) , Luca Parisi \( ^{2} \) , Gerard Pascual \( ^{3} \) , Nicholas G. Parker \( ^{2} \) , Thomas P. Billam \( ^{2} \) ,

Sebastiano Pilati \( ^{4,5} \) , Jordi Boronat \( ^{3} \)  and Stefano Giorgini \( ^{1} \) 

1 Pitaevskii Center on Bose-Einstein Condensation, CNR-INO and Dipartimento di Fisica, Università di Trento, 38123 Povo, Trento, Italy

2 Joint Quantum Centre (JQC) Durham-Newcastle, School of Mathematics, Statistics and Physics, Newcastle University, Newcastle upon Tyne, NE1 7RU, United Kingdom

3 Departament de Física i Enginyeria Nuclear, Universitat Politècnica de Catalunya, Campus Nord B4-B5, E-08034, Barcelona, Spain

4 School of Science and Technology, Physics Division, Università di Camerino, 62032 Camerino, Italy

5 INFN, Sezione di Perugia, I-06123 Perugia, Italy

 \( ^{*} \)  gabriele.spada@unitn.it

## Abstract

We investigate the magnetic behavior of finite-temperature repulsive two-component Bose mixtures by means of exact path-integral Monte-Carlo simulations. Novel algorithms are implemented for the free energy and the chemical potential of the two components. Results on the magnetic susceptibility suggest that the conditions for phase separation are not modified from the zero temperature case. This contradicts previous predictions based on approximate theories. We also determine the temperature dependence of the chemical potential and the contact parameters for experimentally relevant balanced mixtures.

## Contents

1 Introduction 2
2 Methods 3
3 Magnetic behavior of binary mixtures 3
3.1 Particle-position snapshots 6
4 Thermodynamic properties of balanced mixtures 8
5 Conclusion 9
A PIMC computation of chemical potential and free energy 10
A.1 Details of the algorithm 10
A.2 Benchmarks 12
B PIMC algorithm for a binary Bose mixture 13
B.1 Details of the algorithm for free energy differences in a mixture 15
 

## 1 Introduction

The realization of mixtures of ultracold gases in the quantum-degenerate regime has opened new interesting directions to study the simultaneous presence of superfluidity in multicomponent systems, which could not be addressed with traditional quantum fluids such as liquid  \( {}^{4} \) He or standard superconductors. The first examples of superfluid mixtures have been produced both with atoms obeying the same  \( [1,2] \)  or different statistics  \( [3] \) . In particular, two-component mixtures of bosonic species below the Bose-Einstein transition temperature provide one with the simplest set up to investigate the interplay between quantum magnetism and superfluid properties. This includes novel phenomena such as combined mass and spin superfluidity  \( [4] \) , non dissipative spin drag  \( [5] \) , and Bose-enhanced magnetic effects  \( [6] \) . In the case of repulsive mixtures, the zero temperature scenario is well described by mean-field theory  \( [7] \) : the ground state is paramagnetic if the interspecies coupling constant is below a threshold set by the strength of interactions within each component, and is instead fully ferromagnetic, i.e. full phase separation between the two components occurs, if the coupling exceeds this critical value. This scenario has been also confirmed in a series of experiments  \( [8–11] \)  and quantum Monte Carlo simulations for trapped mixtures, both at zero  \( [12] \)  and finite temperature  \( [13] \) . At finite temperatures, perturbative approaches, such as Hartree-Fock (HF) and Popov theories, predict an intriguing scenario holding for mixtures below the Bose-Einstein condensation (BEC) temperature: The paramagnetic state at low temperature can turn ferromagnetic at higher temperature if the interspecies coupling is close enough to the T = 0 threshold  \( [14–16] \) . According to these theoretical schemes, the mechanism responsible for the magnetic transition are beyond mean-field effects induced by temperature, which destabilize the paramagnetic phase. Similar effects of pure quantum nature have instead a stabilizing role in attractive mixtures and lead to the formation of self-bound droplets  \( [17–19] \) . An important question, which needs to be answered, is whether the predictions of perturbative approaches are accurate enough to include the relevant role played by fluctuations around the transition temperature.

In this work we use exact path-integral Monte Carlo (PIMC) simulations to investigate the magnetic and thermodynamic properties of a repulsive two-component Bose mixture. In particular, novel algorithms are implemented to obtain precise unbiased predictions for the chemical potentials of the two separate components and for the total free energy. This provides us with crucial information on the chemical equilibrium at finite polarization and on the occurrence of stable free energy minima. We find that the magnetic susceptibility at finite temperature is well described by the simple zero temperature mean-field prediction and also that there is no evidence of a temperature-induced ferromagnetic transition. Consequently, the conditions for phase separation remain unchanged from the T = 0 case. Furthermore, for the choice of interspecies coupling corresponding to a balanced mixture of sodium atoms, we calculate chemical potential and contact parameters as a function of temperature, pointing out their deviations in the critical region from the predictions of perturbative methods. In particular, the interspecies contact parameter features a suppression at intermediate temperatures caused by statistical effects which indicates an enhanced repulsive correlation between the two components.
 

## 2 Methods

We consider the following Hamiltonian describing a system of  \( N = N_{1} + N_{2} \)  Bose particles belonging to two distinguishable components with equal mass m

 \[ H=-\frac{\hbar^{2}}{2m}\sum_{i=1}^{N_{1}}\nabla_{i}^{2}-\frac{\hbar^{2}}{2m}\sum_{i^{\prime}=1}^{N_{2}}\nabla_{i^{\prime}}^{2}+\sum_{i<j}^{N_{1}}v(|{\bf r}_{i}-{\bf r}_{j}|)+\sum_{i^{\prime}<j^{\prime}}^{N_{2}}v(|{\bf r}_{i^{\prime}}-{\bf r}_{j^{\prime}}|)+\sum_{i,i^{\prime}}^{N_{1},N_{2}}v_{12}(|{\bf r}_{i}-{\bf r}_{i^{\prime}}|). \quad (1) \] 

The intraspecies potentials are assumed to be the same, denoted by  \( v(r) \) , and  \( v_{12}(r) \)  describes interspecies interactions. All potentials are repulsive and modeled by hard spheres, i.e. the potential is infinite inside the diameter of the sphere and zero outside. The two parameters a and  \( a_{12} \)  define, respectively, the range of the v and  \( v_{12} \)  potential and the corresponding value of the s-wave scattering length. In the dilute regime of interest, interaction effects only depend on the coupling strengths:  \( g = \frac{4\pi\hbar^{2}a}{m} \)  and  \( g_{12} = \frac{4\pi\hbar^{2}a_{12}}{m} \) . To discuss magnetic properties we introduce the component densities  \( n_{1} + n_{2} = n \)  and the polarization parameter  \( p = (n_{1} - n_{2})/n \) . For such a symmetric mixture, mean-field theory at zero temperature predicts miscibility (p = 0) if  \( g_{12} < g \)  and a fully separated state (p = 1) if  \( g_{12} > g \)  [7]. Furthermore, the same theory yields the expression  \( \chi = \frac{2}{g - g_{12}} \)  for the magnetic susceptibility in the paramagnetic phase.

In a PIMC simulation, we use periodic boundary conditions in a box of volume V at fixed density n = N/V. We work with the well established worm algorithm in continuous space to efficiently sample bosonic permutations [20]. Recently the method has been further developed to be fully consistent with periodic boundary conditions and was applied to the study of the single-component gas [21]. The algorithm is described in details in Ref. [22]. In the present study, we implemented also the calculation of the total free energy, of the free energy differences for different polarizations, and of the chemical potentials for both components in the canonical ensemble, generalizing to mixtures the technique first proposed in Ref. [23]. The details of the Monte Carlo moves added to the PIMC algorithm can be found in the Appendices A and B. In addition, we use also HF and Popov theories to compare with PIMC results. Details on the derivation of the free energy and related quantities within the HF and Popov scheme are given in Appendix C.

## 3 Magnetic behavior of binary mixtures

We first focus on the magnetic properties of the mixture, analyzing how the chemical potential and the total free energy depend on the polarization. We choose the value  \( na^{3}=10^{-4} \)  for the gas parameter which on one side emphasizes the interesting effects due to interactions and on the other side ensures that the results are universal in terms of solely the gas parameter. However it is worth pointing out that stronger interactions could be realized in resonantly interacting gases [24].

In Fig. 1, the chemical potentials of the two components are plotted against polarization at fixed temperature  \( T = 0.794T_{c}^{0} \) , where  \( k_{B}T_{c}^{0} = \frac{2\pi\hbar^{2}}{m}(n/2\zeta(3/2))^{2/3} \)  is our reference energy scale, corresponding to the BEC transition temperature of a balanced  \( (p = 0) \)  non-interacting mixture. The majority component 1 is Bose condensed for all values of p shown in the figure, while, at this temperature, the minority component 2 turns normal at the critical polarization  \( p_{c} \simeq 1 - (T/T_{c}^{0})^{3/2} \simeq 0.292 \)  corresponding to the maximum of the HF and Popov results for  \( \mu_{2} \) . In panels (b) and (c), referring to  \( g_{12} > 0 \) , we notice that HF and Popov theories predict a crossing of chemical potentials at finite polarization  \( p > p_{c} \) . This crossing corresponds to a minimum in the free energy F according to the thermodynamic relation  \( \mu_{1} - \mu_{2} = \left(\frac{\partial F/N}{\partial p}\right)_{n,T} \) . The minimum signals the phase-separated state where the majority component
 
![](./images/867749749405515850_1.jpg)

![](./images/867749749405515850_2.jpg)

![](./images/867749749405515850_3.jpg)

![](./images/867749749405515850_4.jpg)

Figure 1: Chemical potentials  \( \mu_{1} \)  (blue) and  \( \mu_{2} \)  (red) as a function of the polarization  \( p = (N_{1} - N_{2})/N \)  for a system with a total of  \( N = N_{1} + N_{2} = 128 \)  particles at temperature  \( T = 0.794T_{c}^{0} \)  and with gas parameter  \( na^{3} = 10^{-4} \) , for four values of the couplings ratio  \( g_{12}/g \) . The dashed lines are the HF predictions, the solid lines are the Popov predictions. For the minority (red) component, the two coincide for  \( p > p_{c} \) . In panel (d) only the HF lines are shown. The vertical lines indicate the critical polarization  \( p_{c} \) .

is Bose condensed and in equilibrium with the minority one in the normal phase [15]. This behavior of the HF and Popov free energies is shown in Fig. 2 [see panels (b) and (c)]. Note that the chosen value of  \( g_{12}/g = 0.93 \)  corresponds to the  \( |F = 1, m_{F} = 1\rangle \)  and  \( |F = 1, m_{F} = -1\rangle \)  Bose-Bose mixture of  \( {}^{23}Na \)  atoms investigated experimentally in Refs. [25, 4]. According to HF and Popov theories, this mixture should provide an example of the striking phenomenon of a paramagnetic state at low temperature which turns ferromagnetic at higher temperatures, as predicted in Ref. [15]. However, the PIMC results for  \( \mu_{1} \)  and  \( \mu_{2} \)  at  \( g_{12}/g = 0.93 \) , do not confirm this scenario. The majority component chemical potential  \( \mu_{1} \)  is in good agreement with the Popov result, but  \( \mu_{2} \)  deviates significantly in the region  \( p > p_{c} \)  and does not exhibit the peak predicted by HF and Popov theories. As a result, no crossing occurs for  \( p > p_{c} \)  and no minimum appears in  \( F(p) \)  other than at p = 0. Furthermore, from the thermodynamic relation  \( F(p) = F(0) + \frac{N}{2} \frac{\pi p^{2}}{\chi} \)  holding at small polarization, we find a good agreement using the zero temperature mean-field result  \( \chi = 2/(g - g_{12}) \)  of the magnetic susceptibility, as can be seen in panels (a) and (b) of Fig. 2, where the MF prediction, shifted to coincide with the PIMC data at p = 0, well reproduces the  \( p^{2} \)  behavior of the PIMC data. Similar results are obtained for the fully symmetric case  \( g_{12} = g \) , where the chemical potentials exactly coincide for  \( p < p_{c} \)  and separate without crossing for larger polarizations. As a result the free energy is flat as a function of polarization and the magnetic susceptibility diverges. Interestingly, this behavior, which is well understood at T = 0 where the ground state is degenerate with respect to polarization, remains valid at finite temperature as long as both condensates are present. The results shown in panels (a) and (d) of Figs. 1 and 2 are instead in better qualitative agreement with approximate perturbative approaches. The case  \( g_{12} = 0 \)  corresponds to no
 
![](./images/867749749405515850_5.jpg)

![](./images/867749749405515850_6.jpg)

![](./images/867749749405515850_7.jpg)

![](./images/867749749405515850_8.jpg)

Figure 2: Free energy as a function of the polarization  \(  p = (N_{1} - N_{2}) / N  \)  for a system with a total of  \( N = N_{1} + N_{2} = 128 \)  particles at temperature  \( T = 0.794T_{c}^{0} \)  and with gas parameter  \( na^{3} = 10^{-4} \) , for four values of the couplings ratio  \( g_{12}/g \) . The dotted blue lines in the panels (a) and (b) are the parabolas obtained from the mean-field prediction of the magnetic susceptibility  \( \chi = 2/(g - g_{12}) \) , the green dashed lines are the HF predictions, the red solid lines are the Popov predictions. In panel (d) only the HF line is shown. The vertical lines indicate the critical polarization  \( p_{c} \) .

interaction between the two components:  \( \mu_{2} \)  decreases with p, although without a small peak, and F monotonically increases following the mean-field magnetic susceptibility. More interesting is the case  \( g_{12}=1.2g \) , where the mixture is phase separated already at T=0. Notice that Popov theory cannot be applied here if both condensates are present because spin excitations acquire an unphysical complex energy. The minority chemical potential  \( \mu_{2} \)  displays a maximum, although not as large as predicted by HF theory, and a crossing point with  \( \mu_{1} \) . As a consequence, the free energy indicates instability at p=0 and shows a clear minimum at  \( p>p_{c} \) , corresponding to the phase separated state with partial polarization.

We further analyze the magnetic behavior of the mixture in Fig. 3 where we show the free energy difference  \( \Delta F = F(p) - F(0) \)  as a function of  \( p^{2} \)  for the intermediate value  \( g_{12} = 0.5g \)  of the interspecies coupling constant and at  \( T = 0.794T_{c}^{0} \) . This choice of parameters and, in particular, the choice of temperature emphasizes thermal effects in HF and Popov theories yielding important corrections to the T = 0 magnetic susceptibility. We also note that finite-size effects in PIMC simulations of the free energy are negligible if one increases further the total number of particles. We find that F depends linearly on  \( p^{2} \)  over a large range of values extending also beyond the critical polarization  \( p_{c} \) . Furthermore, the coefficient of the linear dependence, proportional to  \( \chi^{-1} \) , is well reproduced by the mean-field result  \( \chi^{-1} = (g - g_{12})/2 \)  shown in the figure by the MF line. In contrast, HF and Popov results provide a poor account of the polarization dependence of the free energy. A possible explanation of this inadequacy involves the role of critical fluctuations which control the thermodynamics close to the transition point and, in general, can not be described using perturbative methods such as HF and Popov theories. The width of the critical region is predicted to shrink as  \( na^{3} \rightarrow 0 \)  [26],
 
![](./images/867749749405515850_9.jpg)

Figure 3: Free energy difference for a mixture with  \( na^{3}=10^{-4} \) , and  \( g_{12}/g=0.5 \)  and  \( T=0.794T_{c}^{0} \)  as a function of the polarization squared. The PIMC results are compared with the T=0 mean-field (MF - blue dotted line), HF (green dashed line) and Popov (red solid line) predictions. The vertical line indicates the critical polarization  \( p_{c} \) .

but for experimentally relevant values of the gas parameter  \( (na^{3} \simeq 10^{-4} - 10^{-6}) \)  it remains of the same order as the transition temperature itself.

From these results we conclude that, in contrast to HF and Popov predictions, the magnetic susceptibility depends very little on the temperature, and the conditions for phase separation seem to remain the same as at T = 0. In fact, if  \( g_{12} < g \) , our results indicate that the only thermodynamically stable phase is the paramagnetic state at p = 0. A ferromagnetic state forms when  \( g_{12} > g \)  and the effect of temperature is to reduce the equilibrium polarization from the p = 1 value achieved only at zero temperature. This is found at a high temperature not far from the BEC transition point and we expect the same to be true also for lower temperatures, where thermal effects not captured by the mean-field description should play a minor role. In this respect one should also notice that higher order interaction effects at T = 0 do not change the critical value  \( g_{12} = g \)  for the onset of ferromagnetism (see Ref. [16]). As an additional remark, we point out that our results do not exclude a non trivial interplay between ferromagnetic and critical fluctuations in the close vicinity of the transition point. To carefully investigate these effects would require a much deeper analysis of the shift of the transition point in interacting mixtures beyond the scope of this work. Furthermore, we expect the simple T = 0 scenario to hold also at densities lower than  \( na^{3} = 10^{-4} \) . Numerical checks show that for vanishing gas parameter the free energy difference between the p = 0 state and the stable minimum at finite p predicted by Popov theory is suppressed as  \( g^{3/2} \)  and furthermore the minimum is shifted towards higher temperatures occurring closer to the transition point. As a consequence, we expect critical fluctuations to play a major role in the magnetic response of the mixture also in the regime of extremely low densities, thereby invalidating the predictions of Popov theory.

## 3.1 Particle-position snapshots

Visualizing instantaneous particle positions during PIMC simulations allows us to shed some light on the ferromagnetic transition. To minimize the effects due to inter-domain interfaces, we consider large scale simulations comprising N = 8000 particles, with  \( N_{1} = N_{2} \) . The gas parameter is  \( na^{3} = 10^{-4} \) . Fig. 4 shows the position snapshots observed after thermalization is reached. Two initial particle configurations are considered. They feature either vertically separated or mixed components. In the separated configuration, the first component is uni-
 
![](./images/867749749405515850_10.jpg)

 \( T/T_{c}^{0} \approx 0.238; g_{12}/g = 0.93 \) 

![](./images/867749749405515850_11.jpg)

 \( T/T_{c}^{0} \approx 0.238; g_{12}/g = 1.2 \) ; initially separated

![](./images/867749749405515850_12.jpg)

 \( T/T_{c}^{0} \approx 0.4762; g_{12}/g = 1.2 \) 

![](./images/867749749405515850_13.jpg)

 \( T/T_{c}^{0} \approx 0.873; g_{12}/g = 0.93 \) 

![](./images/867749749405515850_14.jpg)

 \( T/T_{c}^{0} \approx 0.238; g_{12}/g = 1.2 \) ; initially mixed

![](./images/867749749405515850_15.jpg)

 \( T/T_{c}^{0} \approx 0.7937; g_{12}/g = 1.2 \) 

Figure 4: Snapshots of particle positions during PIMC simulations at equilibrium. Blue circles represent the  \( N_{1}=4000 \)  particles of the first component, the red squares represent the  \( N_{2}=4000 \)  particles of the second component. A single imaginary-time slice is considered. The gas parameter is  \( na^{3}=10^{-4} \) . The five panels correspond to different temperatures T, interspecies couplings  \( g_{12} \) , or different initial configurations. Panel (a):  \( T/T_{c}^{0}\cong0.238 \) ,  \( g_{12}/g=0.93 \) , components initially separated (along the vertical direction). Panel (b):  \( T/T_{c}^{0}\cong0.873 \) ,  \( g_{12}/g=0.93 \) , components initially separated. Panel (c):  \( T/T_{c}^{0}\cong0.238 \) ,  \( g_{12}/g=1.2 \) , components initially separated. Panel (d):  \( T/T_{c}^{0}\cong0.238 \) ,  \( g_{12}/g=1.2 \) , components initially mixed. Panel (e):  \( T/T_{c}^{0}\cong0.4762 \) ,  \( g_{12}/g=1.2 \) , components initially separated. Panel (f):  \( T/T_{c}^{0}\cong0.7937 \) ,  \( g_{12}/g=1.2 \) , components initially mixed.

formly randomly distributed in the lower half of the 3D simulation box, while the second component is in the upper half. In the mixed initial configuration, both components are uniformly distributed in the whole box. In panels (a) and (b), the interspecies coupling strength is  \( g_{12}/g = 0.93 \) , i.e., below the T = 0 MF critical point. In the first panel, the temperature is relatively low, namely,  \( T/T_{c}^{0} \cong 0.238 \) . Here, even Popov theory would predict a paramagnetic state. In the second, it is closer to the BEC transition temperature, where Popov theory would predict a ferromagnetic state. The two simulations start in the separated configuration. Despite of being initially separated, the two components rapidly mix, indicating a paramagnetic state, both at low temperature and closer to the BEC transition. In panel (c), the inter-species interaction strength  \( (g_{12}/g = 1.2) \)  is beyond the critical point predicted by the MF theory. In this case, the two components keep the initial spatial separation along the vertical direction, with only minor mixing close to the interface separating the two domains. Interestingly, even when they start from a mixed configuration [panel (d)], they form two well-defined ferromagnetic domains. This indicates that large-scale PIMC simulations are able to simulate phase separated states. Chiefly, these observations further corroborate the claim that the finite temperature transition corresponds to the T = 0 MF scenario, in contrast to the HF and Popov predictions. When the temperature is raised [panel (e)], the interface is
 
![](./images/867749749405515850_16.jpg)

Figure 5: Chemical potential of an unpolarized mixture with  \( na^{3}=10^{-6} \) , and  \( g_{12}/g=0.93 \)  as a function of the temperature. The PIMC results in the thermodynamic limit (black points) are compared with the HF (green dashed line) and the Popov (red solid line) predictions.

less regular and it looses memory of the initial position. One also notices a larger impurity density, corresponding to a ferromagnetic state with partial polarization. Moving even closer to the BEC transition temperature  \( T_{c}^{0} \)  [panel (f)], the two domains can be hardly identified by naked eye. However, we argue that in the thermodynamic limit one would still observe a (partially) ferromagnetic state, meaning that the Curie critical temperature where melting occurs is even higher.

## 4 Thermodynamic properties of balanced mixtures

We now turn our attention to the study of thermodynamic quantities, focusing on the  \( g_{12}=0.93g \)  sodium mixture in the balanced state p=0. In this case we have chosen the value  \( na^{3}=10^{-6} \)  for the gas parameter which is closer to experimentally relevant conditions in the absence of Feshbach resonances. The PIMC results for the thermodynamic quantities shown below are the extrapolations to the thermodynamic limit of the data computed with up to 512 total particles. In Fig. 5 we show the chemical potential  \( \mu=\mu_{1}=\mu_{2} \)  of the mixture as a function of temperature below and above the transition point and we compare it with the results of perturbative approaches. The results are in good agreement with both HF and Popov predictions when the temperature is not too close to the critical point. In the critical region around  \( T_{c}^{0} \) , deviations are sizable. They tend to suppress the maximum, similarly to the results of Fig. 1 for the minority component. We notice that a maximum in the temperature dependence of the chemical potential should be expected on general grounds from the theory of superfluids and has been recently observed in a single-component dilute Bose gas [27]. The PIMC results for  \( \mu \)  in a single-component gas are discussed in the appendix as a test study of the chemical potential algorithm.

In Fig. 6 we show the results for the contact parameters, important thermodynamic quantities sensitive to short-range correlations. In a symmetric unpolarized mixture one defines two contact parameters  \( C_{11} = C_{22} = C \)  and  \( C_{12} \)  associated to correlations within each component and between the two components respectively

 \[ C=16\pi^{2}a^{2}\frac{\partial F/V}{\partial g},\quad C_{12}=32\pi^{2}a_{12}^{2}\frac{\partial F/V}{\partial g_{12}}. \quad (2) \] 

The contact parameter C has been measured as a function of temperature in a single-
 
![](./images/867749749405515850_17.jpg)

![](./images/867749749405515850_18.jpg)

Figure 6: Intraspecies (panel (a)) and interspecies (panel (b)) contact parameters of an unpolarized mixture with  \( na^{3}=10^{-6} \) , and  \( g_{12}/g=0.93 \)  as a function of the temperature. The PIMC results in the thermodynamic limit (black points) are compared with the HF (green dashed line) and the Popov (red solid line) predictions.

component gas [28] and in a mixture of a Bose gas with impurities [29]. In our PIMC simulations we have computed C and  \( C_{12} \)  from the short-range behavior of the pair correlation function for particles belonging to the same and to different components [21]. The results for C are in good agreement with both HF and Popov predictions, showing deviations only in the vicinity of  \( T_{c}^{0} \) . For  \( C_{12} \) , instead, the HF prediction does not depend on the temperature, while the Popov prediction yields a small minimum. Our PIMC findings show a small minimum around  \( T \simeq 0.7T_{c}^{0} \)  which reproduces this. This enhanced repulsive correlation between the two components at intermediate temperatures has been already discussed in repulsive mixtures [30,31] and deserves further investigation.

## 5 Conclusion

We have investigated the magnetic and thermodynamic properties of repulsive Bose mixture using exact numerical methods. For the values of the parameters considered in the simulations we do not find the ferromagnetic transition predicted to occur at finite temperature by perturbative approaches and we find good agreement with the magnetic susceptibility from simple mean-field theory at zero temperature. We further argue that a similar conclusion is expected to hold for lower values of the gas parameter. This claim is further corroborated by the analysis of particle-positions snapshots. Thermodynamic quantities reveal the role of critical fluctuations close to the BEC transition point and the behavior of the contact parameters contains important information on short-range correlations in the mixture that can be measured in future experiments. Our findings indicate the importance of unbiased simulations for atomic mixtures, in contrast to previous perturbative treatments of repulsive and attractive two-component Bose gases.

## Acknowledgments

Funding information This work was supported by the Italian Ministry of University and Research under the PRIN2017 project CEnTraL 20172H2SC4. G.S. and S.G. acknowledge financial support from the Provincia Autonoma di Trento. S.P. acknowledges support from the PNRR MUR project PE0000023-NQSTI, and PRACE for awarding access to the Fenix Infrastructure resources at Cineca, which are partially funded from the European Union's Horizon 2020 research and innovation programme through the ICEI project under the grant agreement.
 
![](./images/867749749405515850_19.jpg)

Figure 7: The four sectors interconnected by the web of sector-changing moves.

No. 800858. J.B. and G. P. acknowledge financial support from Ministerio de Economia, Industria y Competitividad (MINECO, Spain) under grant No. PID2020-113565GB-C21. L.P, N.G.P and T.P.B acknowledge support from the UK Engineering and Physical Sciences Research Council (Grant No. EP/T015241/1).

## A PIMC computation of chemical potential and free energy

In this appendix, we present the details of the PIMC algorithm we employ for the computation of the chemical potential of a Bose gas. The basic idea is to recognize that the chemical potential can be derived from the ratio of the partition functions for the systems with  \( N + 1 \)  and N particles (at fixed volume and temperature) as

 \[ \mu(N,T)=F(N+1,T)-F(N,T)=-k_{B}T\log\frac{Z_{N+1}}{Z_{N}}. \quad (A.1) \] 

As noted in Ref. [23] the above formula can be leveraged in a canonical PIMC calculation by enlarging the configurational space to include the sector with one additional particle. The ratio  \( Z_{N+1}/Z_{N} \)  is then evaluated as the relative time spent by the simulation in the two sectors. The simulation resembles a grand canonical one, with the difference that it is restricted to states with either N or  \( N+1 \)  particles, thus providing higher statistics for the computation of  \( \mu(N,T) \) . Combining the chemical potential with the pressure, we can obtain the free energy

 \[ F=\Omega+\mu N=-P V+\mu N, \quad (A.2) \] 

where  \( \Omega = -PV \)  is the grand canonical potential.

## A.1 Details of the algorithm

In order to extend the algorithm described in Ref. [22] and enable the computation of the chemical potential we work with  \( N + 1 \)  polymers and implement a boolean variable for each polymer to activate or deactivate it.

The configurational space is now composed by four sectors: the original  \( Z_{N} \)  and  \( G_{N} \)  together with the corresponding sectors with one additional particle  \( Z_{N+1} \)  and  \( G_{N+1} and one needs to introduce appropriate Monte Carlo moves to allow the Markov-Chain to visit all the configurations within these sectors. The four sectors together with the sector-changing moves are summarized in Fig. 7. In general one can introduce a grand canonical chemical potential  \( \mu_{gc} \)  as a simulation parameter to be used to increase the sampling efficiency. In particular it
 

can be tuned to be close to the expected value e.g. by using the Hartree-Fock approximation, in order to balance the simulation time spent within the sectors with N and  \( N + 1 \)  particles. The chemical potential is then evaluated as

 \[ \mu(N,T)=\mu_{\mathrm{g c}}-k_{B}T\log\frac{t(Z_{N+1})}{t(Z_{N})}, \quad (A.3) \] 

where  \( t(Z_{N+1})/t(Z_{N}) \)  is the ratio of the simulation time spent in the two sectors  \( Z_{N+1} \)  and  \( Z_{N} \) . We have implemented three sets of particle-number changing moves—Extend/Shorten Worm, Add/Remove Worm and Add/Remove Ring Polymer—that are briefly described below using the notation of Ref. [22] and indicating with  \( \Delta U \)  the variation in the potential energy between the new proposed configuration and the old one. Within the primitive approximation we would have  \( \Delta U = \frac{\beta}{M} \sum_{j} \left( V_{j}' - V_{j} \right) \) , where M is the total number of imaginary-time slices and  \( V_{j}' \)  ( \( V_{j} \) ) is the sum of the two-body potentials over all pairs of particles at the slice j after (before) the Monte Carlo update. Note that, when in the sectors with N particles, one must be careful to exclude the deactivated polymer from the computation.

Extend/Shorten Worm These moves connect the sectors  \( G_{N} \)  and  \( G_{N+1} \)  by adding or removing a polymer at the end of the worm. To extend the worm we first check if sector is  \( G_{N} \) , then we activate the extra polymer and we put it in permutation with the worm's head. We then use the staging algorithm to redraw the last polymer as in Move Head. The move is accepted with probability

 \[ A_{E X}=\min\left\{1,e^{\beta\mu_{\mathrm{g c}}-\Delta U}\right\}. \quad (A.4) \] 

To shorten the worm we first check if sector is  \( G_{N+1} \)  and if the worm is at least two polymers long. Then we deactivate the last polymer of the worm. The move is accepted with probability

 \[ A_{S H}=\min\left\{1,e^{-\beta\mu_{\mathrm{g c}}-\Delta U}\right\}. \quad (A.5) \] 

Add/Remove Worm These moves connect the sectors  \( Z_{N} \)  and  \( G_{N+1} \)  by adding or removing a one-polymer worm. To add the worm we first check if sector is  \( Z_{N} \) , then we activate the extra polymer, we uniformly sample its first bead in the volume and we use the staging algorithm to sample the rest of the polymer as in Move Head. The move is accepted with probability

 \[ A_{A W}=\min\left\{1,C e^{\beta\mu_{\mathrm{g c}}-\Delta U}\right\}, \quad (A.6) \] 

where C is the open/close parameter. The complementary move consists in removing a one-polymer long worm from the  \( G_{N+1} \)  sector by deactivating it. The move is accepted with probability

 \[ A_{R W}=\min\left\{1,C^{-1}e^{-\beta\mu_{\mathrm{g c}}-\Delta U}\right\}. \quad (A.7) \] 

Add/Remove Ring Polymer These moves connect the sectors  \( Z_{N} \)  and  \( Z_{N+1} \)  by adding or removing a ring polymer (i.e. a polymer in permutation with itself and with zero winding). To add the ring we first check if sector is  \( Z_{N} \) , then we activate the extra polymer and we uniformly sample its first bead in the volume. The last bead M of the polymer is then set to be equal to the first and we use the staging algorithm to sample the rest of the polymer. The move is accepted with probability

 \[ A_{A R}=\min\left\{1,\frac{V}{(N+1)\lambda_{T}^{D}}e^{\beta\mu_{\mathrm{g c}}-\Delta U}\right\}. \quad (A.8) \]
 
![](./images/867749749405515850_20.jpg)

Figure 8: Chemical potential of an ideal Bose gas with N particles at temperature  \( T = 1.5T_{c}^{0} \) . The PIMC values (black diamonds) are compared with the exact results at fixed N (connected by the blue dotted line) and with the result in the thermodynamic limit (green horizontal line). Inset: the difference between the PIMC and the exact values.

The complementary move consists in removing a one-polymer ring with zero winding from the  \( Z_{N+1} \)  sector by deactivating it. The move is accepted with probability

 \[ A_{R R}=\min\left\{1,\frac{(N+1)\lambda_{T}^{D}}{V}e^{-\beta\mu_{\mathrm{g c}}-\Delta U}\right\}. \quad (A.9) \] 

## A.2 Benchmarks

Following the strategy of Ref. [22] we carefully check our implementation by running a number of tests. First of all, we verify that we correctly recover the values of the chemical potential for the ideal Bose gas for each system size N. In Fig. 8 we show the PIMC results at the temperature  \( T = 1.5T_{c}^{0} \)  compared with the exact values (obtained via the recursion formulas as in Refs. [32,33] and reviewed in Ref. [22]) and with the result in the thermodynamic limit given by

 \[ \mu_{\mathrm{I B G}}=k_{B}T\log(z)\;, \quad (A.10) \] 

where z is an effective fugacity that determines the total density of the gas via the equation  \( n\lambda_{T}^{3}=g_{3/2}(z) \)  with  \( g_{\nu}(z) \)  the usual special Bose functions. The agreement between the PIMC data and the expected values is perfect at any size and does not depend on the number of imaginary-time slices used in the simulation. Moreover we verify that below  \( T_{c}^{0} \)  the PIMC results are compatible with a zero chemical potential.

We then benchmark the interacting gas, where the repulsive interaction is modeled by a hard sphere potential. As in Ref. [21], we use the pair-product ansatz [34] for the computation of the potential energy  \( \Delta U \) . In Fig. 9 we compare the PIMC results for the chemical potential and the free energy with the perturbative predictions. The PIMC data are extrapolated to the thermodynamic limit using a linear fit in 1/N of the results for four sizes N = 128, 256, 384, 512. The number of imaginary-time slices is 16 for all sizes. For the chemical potential, we also compare our results with the predictions from the universal relations of Ref. [26], using their data for the density shift  \( \lambda(X) \propto n - n_{c} \)  to extract the reduced temperature  \( t = T / T_{c}^{0} \)  and then mapping it to the corresponding chemical potential using the data for the chemical potential shift  \( X \propto \mu - \mu_{c} \) . In particular, expressing the relations in our units, we find that each value of  \( \lambda(X) \)  can be mapped to a value of t solving the equation

 \[ \frac{16\pi^{3}}{\zeta(3/2)}a n^{1/3}\left(\lambda(X)-\mathcal{C}\right)t^{2}+t^{3/2}=1, \quad (A.11) \]
 
![](./images/867749749405515850_21.jpg)

![](./images/867749749405515850_22.jpg)

Figure 9: Results for an interacting Bose gas with gas parameter  \( na^{3}=10^{-6} \)  as a function of the temperature. The PIMC values, extrapolated to the thermodynamic limit (black crosses), are compared with the perturbative results of Hartree-Fock (green dashed line) and Popov (red solid line) theories. Left panel: Results for the chemical potential, also compared with the predictions from the universal relations of Ref. [26] (blue dots). Right panel: difference in free energy with the ideal Bose gas result.

in the region where the universal relations can be applied, namely  \( t \sim 1 \) . The numerical constant C is determined as  \( \mathcal{C} = 0.0142(4) \) . From the corresponding values of X we then determine the chemical potential shift as

 \[ \frac{\mu-\mu_{c}}{k_{B}T_{c}^{0}}=\frac{32\pi^{3}a^{2}n^{2/3}}{\zeta(3/2)^{2/3}}t^{2}X. \quad (A.12) \] 

Finally, to get the sought-after values of  \( \mu \) , we need to add the values of  \( \nu_{c} \)  as obtained from Ref. [35]

 \[ \frac{\mu_{c}}{k_{B}T_{c}^{0}}=4a n^{1/3}\zeta(3/2)^{2/3}t^{3/2}-\frac{32\pi a^{2}n^{2/3}}{\zeta(3/2)^{2/3}}t^{2}\log\left(\mathcal{K}\frac{\zeta(3/2)^{1/3}}{a n^{1/3}\sqrt{32\pi^{3}}t}\right), \quad (A.13) \] 

where  \( \mathcal{K}=0.673(1) \)  is a numerical constant \( ^{1} \) . The data for  \( \mu \)  obtained from the universal are represented by the blue dots in the left panel of Fig. 9 and show a good agreement with the PIMC data for  \( T<T_{c}^{0} \) , while, for  \( T>T_{c}^{0} \( , a discrepancy builds up for increasing temperatures, since the universal relations are valid only in the regime of large occupation numbers for single-particle modes. In that regime, the PIMC data nicely reproduce the HF predictions. With the benchmarks shown so far, we are now confident that the PIMC algorithm correctly reproduces the physics of a single-component Bose gas both in the non-interacting and in the interacting case. In the following section we show how to extend the algorithm for Bose mixtures.

## B PIMC algorithm for a binary Bose mixture

Extending the PIMC algorithm to the case of multicomponent gases is pretty straightforward: one just needs to restrict the Swap move to involve only particles of the same species and, in the interacting case, to take into account the inter-species interaction described by the s-wave scattering length  \( a_{12} \) . The computation of the chemical potentials for the two species proceeds as before via the free energy difference, this time making sure the number of particles of the other species is kept fixed. For a two-component mixtures we have:

 \[ \begin{aligned}&\mu_{1}(N_{1},N_{2},T)=F(N_{1}+1,N_{2},T)-F(N_{1},N_{2},T),\\&\mu_{2}(N_{1},N_{2},T)=F(N_{1},N_{1}+1,T)-F(N_{1}, N_{2},T).\\ \end{aligned} \quad (B.14) \]
 
![](./images/867749749405515850_23.jpg)

Figure 10: Chemical potentials  \( \mu_{1} \)  (blue) and  \( \mu_{2} \)  (red) for a non-interacting mixture of ideal Bose gases as a function of the polarization. The temperature is kept fixed at  \( T = 0.5T_{c}^{0} \)  and the total number of particles is N = 128. The PIMC points are compared to the exact results connected by the dotted lines. The critical polarization, at which the minority component becomes normal, is signaled by a gray vertical line. Inset: the difference between the PIMC data and the exact results.

where the differences are numerically computed as the ratios of Monte Carlo times spent in the different sectors. The simulation now lives in a configurational space made by  \( 4 \times 4 = 16 \)  sectors. Several consistency checks where made on the algorithm. In Fig. 10 we show the results for two non-interacting ideal Bose gases, where we recover the known exact result as a function of the polarization. The chemical potential  \( \mu_{1} \)  for the majority component is consistent with zero, while the chemical potential  \( \mu_{2} \)  for the minority component becomes non-zero above the critical polarization, where it becomes normal.

Using the above method for computing the chemical potentials, one can obtain the value of the free energy of the mixture via the thermodynamic relation

 \[ F=-P V+\mu_{1}N_{1}+\mu_{2}N_{2}. \quad (B.15) \] 

Notice that, while this quantity contains valuable information and it represents our main test-bench for the perturbative predictions, it comes at the cost of a cancellation between the pressure term and the chemical potential terms, that amplifies its final statistical error. However, when we focus on the magnetic properties of a binary mixture, we are only interested in the free energy difference among mixtures at different values of the polarization  \(  p = (N_{1} - N_{2}) / N  \) , where  \( N = N_{1} + N_{2} \)  is the total number of particles. Such a difference can be evaluated more efficiently by devising an algorithm that directly samples configurations with different values of the polarization, while keeping N fixed. Denoting with  \( Z_{N,p} \)  the partition function with N total particles and polarization p, the free energy difference  \( \Delta F(N, p) \)  between the state at polarization p and the unpolarized state with p = 0 can be computed as

 \[ \Delta F(N,p)=F\left(\frac{N(1+p)}{2},\frac{N(1-p)}{2},T\right)-F\left(\frac{N}{2},\frac{N}{2},T\right)=-k_{B}T\log\frac{t(Z_{N,P})}{t(Z_{N,0})}. \quad (B.16) \] 

where the ratio  \( t(Z_{N,P})/t(Z_{N,0}) \)  is the ratio between the time spent in the sector with polarization p and the time spent in the secto with zero polarization. There are many possible ways to implement such an algorithm: One possibility is, for example, to combine the moves of Sec. A.1 for the two species in such a way that each time a particle of one species is created a particle of the other species is removed. In the following we mention another possibility, which is slightly more sophisticated.
 

## B.1 Details of the algorithm for free energy differences in a mixture

An efficient algorithm that spans the configurations with different polarizations, while keeping N fixed can be devised by taking close inspiration from the original grand canonical implementation of Refs. [20,36]. The Monte Carlo moves have been adapted in such a way that both the total number of polymers and the total number of beads are kept constant throughout the simulation. Within this algorithm, the worms for the two species might be present simultaneously, also in a configuration where the beads of one polymer are shared between the two worms. For example, the polymer  \( i_{0} \)  might be filled by the species 1 up to the imaginary-time slice  \( j_{0} \)  (corresponding to the head of the worm 1), while the rest of the slices are filled by the worm of the species 2 (that has its tail at the imaginary-time slice  \( j_{0} + 1 \)  of the polymer  \( i_{0} \) ). We briefly describe below a minimal pair of moves, called Advance/Recede, that allows the simulation to span the configurations at different values of polarization (except the case at p = 1). Other moves can be included in order to improve the ergodicity of the Markov chain across the sectors, for example by combining Advance/Recede with Open/Close. The details of these combined moves will not be given here; instead we just outline the aforementioned minimal addition that can be used for small values of the polarization.

The Advance and Recede moves change the relative lengths of the worms and can only be performed when both worms are present. In the Advance move the head of the worm of species s is advanced in imaginary time from the slice j to the slice  \( j + \Delta j \) , by sampling the new  \( \Delta j \)  beads with the staging algorithm as in Move Head. The tail of the worm of the other species  \( s' \)  is advanced as well by deleting all the beads between the slice j and the slice  \( j + \Delta j \) . Note that we must reject the move if the worm of species  \( s' \)  is completely deleted by the proposed update. The move is then accepted with probability

 \[ A_{\mathrm{a d v a n c e}}=\min\left\{1,e^{\beta\Delta\mu}\Delta j/M-\Delta U\right\}, \quad (B.17) \] 

where  \( \Delta\mu=\mu_{gc}^{s}-\mu_{gc}^{s^{\prime}} \)  is the difference between the grand canonical chemical potentials of the two species. The complementary Recede move is completely symmetric and can be obtained as the Advance move with negative values of  \( \Delta j \) . It consists in receding the head of the species s by deleting  \( \Delta j \)  beads, while simultaneously creating  \( \Delta j_{n} \)  new beads for the species  \( s^{\prime} \) . The move is accepted with probability

 \[ A_{\mathrm{r e c e d e}}=\min\left\{1,e^{-\beta\Delta\mu}\Delta j/M-\Delta U\right\}. \quad (B.18) \] 

This pair of moves can change the species of whole polymers, thus allowing the algorithm to sample configurations with different polarizations. We have checked that the free energy differences computed directly through Eq. (B.16) reproduce those obtained from the full computation of the free energy, but deliver smaller statistical errors.

## C Hartree-Fock and Popov theories

The Hartree-Fock and Popov theories of repulsive binary Bose mixtures at finite temperature are described in details in Refs. [15,16]. We note that Popov's theory is also known as the finite temperature extension of Beliaev's approach and includes the important contribution of anomalous fluctuations to thermodynamic quantities [37,38]. Here we report the results for the Helmholtz free energy obtained in the two approaches from which all thermodynamic quantities discussed in the main text can be derived.
 

Within the HF approximation one finds

 \[ \begin{align*}\frac{F_{\mathrm{HF}}}{V}&=\frac{g}{2}\left(n_{1}^{2}+n_{2}^{2}\right)+g_{12}n_{1}n_{2}+gn_{T}^{0\;2}\\&+\frac{1}{\beta V}\sum_{\mathbf{k}}\left[\ln\left(1-e^{-\beta(\epsilon_{k}+gn_{1,0})}\right)+\ln\left(1-e^{-\beta(\epsilon_{k}+gn_{2,0})}\right)\right],\end{align*} \quad (C.19) \] 

holding when both condensates are present, i.e. in the polarization range  \( p < p_{c} \)  set by the critical polarization  \( p_{c} = 1 - (T/T_{c}^{0})^{3/2} \)  at which the minority component 2 turns normal. Here  \( \epsilon_{k} = \hbar^{2}k^{2}/(2m) \)  is the single-particle kinetic energy and  \( n_{T}^{0} = \zeta(3/2)/\lambda_{T}^{3} \)  is the noninteracting thermal density written in terms of the thermal wavelength  \( \lambda_{T} = \sqrt{2\pi\hbar^{2}/mk_{B}T} \)  and  \( \zeta(3/2) \simeq 2.612 \) . Furthermore,  \( n_{i,0} \)  (i = 1, 2) correspond to the condensate density of the two components calculated to lowest order in the interaction strength:  \( n_{i,0} = n_{i} - n_{T}^{0} \) . When  \( p > p_{c} \)  and the density  \( n_{2} \)  of the minority component does not exceed the thermal density  \( n_{T}^{0} \) , the above expression for free energy becomes

 \[ \begin{align*}\frac{F_{\mathrm{HF}}}{V}&=\frac{g}{2}\left(n_{1}^{2}+2n_{2}^{2}+n_{T}^{0\;2}\right)+g_{12}n_{1}n_{2}+\mu_{2}^{\mathrm{IBG}}n_{2}\\&+\frac{1}{\beta V}\sum_{\mathbf{k}}\left[\ln\left(1-e^{-\beta(\epsilon_{k}+g(n_{1}-n_{T}^{0}))}\right)+\ln\left(1-e^{-\beta(\epsilon_{k}-\mu_{2}^{\mathrm{IBG}})}\right)\right],\end{align*} \quad (C.20) \] 

where the effective chemical potential  \( \mu_{2}^{IBG} \)  is fixed by the normalization condition of the minority component  \( n_{2}=g_{3/2}(e^{\beta\mu_{2}^{\mathrm{IBG}}})/\lambda_{T}^{3} \) , with  \( g_{3/2}(z) \)  the usual special Bose function. Notice that expressions (C.19) and (C.20) coincide at  \( p=p_{c} \)  where  \( n_{2}=n_{T}^{0} \)  and  \( \mu_{2}^{IBG}=0 \) .

The Popov theory includes the contribution from collective excitations (density and spin waves) into the thermodynamics of the mixture yielding the following expression for the free energy:

 \[ \begin{align*}\frac{F}{V}&=\frac{g}{2}\left(n_{1}^{2}+n_{2}^{2}\right)+g_{12}n_{1}n_{2}+gn_{T}^{0\;2}\\&+\frac{1}{\beta V}\sum_{\pm}\sum_{\mathbf{k}}\ln\left(1-e^{-\beta E_{k}^{\pm}}\right)+\left(\frac{m}{2\pi\hbar^{2}}\right)^{3/2}\frac{4}{15\sqrt{\pi}}\sum_{\pm}\left(2\Lambda_{\pm}\right)^{5/2},\end{align*} \quad (C.21) \] 

valid when both components are in the condensed state  \( (p < p_{c}) \) . The first term in the second line collects the thermal contribution from the excitation spectrum in the density and spin channel  \( E_{k}^{\pm} = \sqrt{\epsilon_{k}^{2} + 2\Lambda_{\pm}\epsilon_{k}} \)  whereas the last term survives also at T = 0 yielding the Lee-Huang-Yang beyond mean-field corrections to the ground-state energy. Both terms involve the effective chemical potentials

 \[ \Lambda_{\pm}=\frac{1}{2}\left(g n_{0}\pm\sqrt{(g^{2}-g_{12}^{2})n^{2}p^{2}+g_{12}^{2}n_{0}^{2}}\right), \quad (C.22) \] 

where  \( n_{0}=n-2n_{T}^{0} \)  is the condensate density calculated to lowest order in the interaction strength. In the regime of high polarization  \( (p>p_{c}) \)  the above expression reduces to

 \[ \begin{align*}\frac{F}{V}&=\frac{g}{2}\left(n_{1}^{2}+2n_{2}^{2}+n_{T}^{0\;2}\right)+g_{12}n_{1}n_{2}+\left(\frac{m}{2\pi\hbar^{2}}\right)^{3/2}\frac{4}{15\sqrt{\pi}}\left(2g(n_{1}-n_{T}^{0})\right)^{5/2}+\mu_{2}^{\mathrm{IBG}}n_{2}\\&+\frac{1}{\beta V}\sum_{\mathbf{k}}\left[\ln\left(1-e^{-\beta\sqrt{\epsilon_{k}^{2}+2\epsilon_{k}}g(n_{1}-n_{T}^{0})}\right)+\ln\left(1-e^{-\beta(\epsilon_{k}-\mu_{2}^{\mathrm{IBG}})}\right)\right],\end{align*} \quad (C.23) \] 

where similarly to the HF case the effective chemical potential  \( \mu_{2}^{IBG} \)  is determined by the normalization condition  \( n_{2}=g_{3/2}(e^{\beta\mu_{2}^{\mathrm{IBG}}})/\lambda_{T}^{3} \) .
 

## References

[1] C. J. Myatt, E. A. Burt, R. W. Ghrist, E. A. Cornell and C. E. Wieman, Production of two overlapping Bose-Einstein condensates by sympathetic cooling, Phys. Rev. Lett. 78, 586 (1997), doi:10.1103/PhysRevLett.78.586.

[2] G. Modugno, M. Modugno, F. Riboli, G. Roati and M. Inguscio, Two atomic species superfluid, Phys. Rev. Lett. 89, 190404 (2002), doi:10.1103/PhysRevLett.89.190404.

[3] I. Ferrier-Barbut, M. Delehaye, S. Laurent, A. T. Grier, M. Pierce, B. S. Rem, F. Chevy and C. Salomon, A mixture of Bose and Fermi superfluids, Science 345(6200), 1035 (2014), doi:10.1126/science.1255380.

[4] E. Fava, T. Bienaime, C. Mordini, G. Colzi, C. Qu, S. Stringari, G. Lamporesi and G. Ferrari, Observation of spin superfluidity in a Bose gas mixture, Phys. Rev. Lett. 120, 170401 (2018), doi:10.1103/PhysRevLett.120.170401.

[5] J. Nespolo, G. E. Astrakharchik and A. Recati, Andreev-bashkin effect in superfluid cold gases mixtures, New Journal of Physics 19(12), 125005 (2017), doi:10.1088/1367-2630/aa93a0.

[6] D. M. Stamper-Kurn and M. Ueda, Spinor Bose gases: Symmetries, magnetism, and quantum dynamics, Rev. Mod. Phys. 85, 1191 (2013), doi:10.1103/RevModPhys.85.1191.

[7] L. Pitaevskii and S. Stringari, Bose-Einstein Condensation and Superfluidity, Oxford University Press (2016).

[8] D. J. McCarron, H. W. Cho, D. L. Jenkin, M. P. Köppinger and S. L. Cornish, Dual-species Bose-Einstein condensate of  \( {}^{87}Rb \)  and  \( {}^{133}Cs \) , Phys. Rev. A 84, 011603 (2011), doi:10.1103/PhysRevA.84.011603.

[9] L. Wacker, N. B. Jørgensen, D. Birkmose, R. Horchani, W. Ertmer, C. Klempt, N. Winter, J. Sherson and J. J. Arlt, Tunable dual-species Bose-Einstein condensates of  \( {}^{39} \) K and  \( {}^{87} \) Rb, Phys. Rev. A 92, 053602 (2015), doi:10.1103/PhysRevA.92.053602.

[10] F. Wang, X. Li, D. Xiong and D. Wang, A double species na-23 and rb-87 Bose-Einstein condensate with tunable miscibility via an interspecies Feshbach resonance, JOURNAL OF PHYSICS B-ATOMIC MOLECULAR AND OPTICAL PHYSICS 49(1) (2016), doi:10.1088/0953-4075/49/1/015302.

[11] K. L. Lee, N. B. Jørgensen, L. J. Wacker, M. G. Skou, K. T. Skalmstang, J. J. Arlt and N. P. Proukakis, Time-of-flight expansion of binary Bose–Einstein condensates at finite temperature, New Journal of Physics 20(5), 053004 (2018), doi:10.1088/1367-2630/aaba39.

[12] V. Cikojević, L. V. Markić and J. Boronat, Harmonically trapped Bose–Bose mixtures: a quantum Monte Carlo study, New Journal of Physics 20(8), 085002 (2018), doi:10.1088/1367-2630/aad6cc.

[13] K. Dželalija, V. Cikojević, J. Boronat and L. Vranješ Markić, Trapped Bose-Bose mixtures at finite temperature: A quantum Monte Carlo approach, Phys. Rev. A 102, 063304 (2020), doi:10.1103/PhysRevA.102.063304.

[14] B. Van Schaeybroeck, Weakly interacting Bose mixtures at finite temperature, Physica A: Statistical Mechanics and its Applications 392(17), 3806 (2013), doi:https://doi.org/10.1016/j.physa.2013.04.026.
 

[15] M. Ota, S. Giorgini and S. Stringari, Magnetic phase transition in a mixture of two interacting superfluid Bose gases at finite temperature, Phys. Rev. Lett. 123, 075301 (2019), doi:10.1103/PhysRevLett.123.075301.

[16] M. Ota and S. Giorgini, Thermodynamics of dilute Bose gases: Beyond mean-field theory for binary mixtures of Bose-Einstein condensates, Phys. Rev. A 102, 063303 (2020), doi:10.1103/PhysRevA.102.063303.

[17] D. S. Petrov, Quantum mechanical stabilization of a collapsing Bose-Bose mixture, Phys. Rev. Lett. 115, 155302 (2015), doi:10.1103/PhysRevLett.115.155302.

[18] C. R. Cabrera, L. Tanzi, J. Sanz, B. Naylor, P. Thomas, P. Cheiney and L. Tarruell, Quantum liquid droplets in a mixture of Bose-Einstein condensates, Science 359(6373), 301 (2018), doi:10.1126/science.aa05686.

[19] G. Semeghini, G. Ferioli, L. Masi, C. Mazzinghi, L. Wolswijk, F. Minardi, M. Modugno, G. Modugno, M. Inguscio and M. Fattori, Self-bound quantum droplets of atomic mixtures in free space, Phys. Rev. Lett. 120, 235301 (2018), doi:10.1103/PhysRevLett.120.235301.

[20] M. Boninsegni, N. Prokof'ev and B. Svistunov, Worm algorithm for continuous-space path integral Monte Carlo simulations, Phys. Rev. Lett. 96, 070601 (2006), doi:10.1103/PhysRevLett.96.070601.

[21] G. Spada, S. Pilati and S. Giorgini, Thermodynamics of a dilute Bose gas: A path-integral Monte Carlo study, Phys. Rev. A 105, 013325 (2022), doi:10.1103/PhysRevA.105.013325.

[22] G. Spada, S. Giorgini and S. Pilati, Path-integral Monte Carlo worm algorithm for Bose systems with periodic boundary conditions, Condensed Matter 7(2) (2022), doi:10.3390/condmat7020030.

[23] C. M. Herdman, A. Rommal and A. Del Maestro, Quantum Monte Carlo measurement of the chemical potential of  \( {}^{4} \) He, Phys. Rev. B 89, 224502 (2014), doi:10.1103/PhysRevB.89.224502.

[24] R. J. Fletcher, A. L. Gaunt, N. Navon, R. P. Smith and Z. Hadzibabic, Stability of a unitary Bose gas, Phys. Rev. Lett. 111, 125303 (2013), doi:10.1103/PhysRevLett.111.125303.

[25] T. Bienaïmé, E. Fava, G. Colzi, C. Mordini, S. Serafini, C. Qu, S. Stringari, G. Lamporesi and G. Ferrari, Spin-dipole oscillation and polarizability of a binary Bose-Einstein condensate near the miscible-immiscible phase transition, Phys. Rev. A 94, 063652 (2016), doi:10.1103/PhysRevA.94.063652.

[26] N. Prokof'ev, O. Ruebenacker and B. Svistunov, Weakly interacting Bose gas in the vicinity of the normal-fluid-superfluid transition, Phys. Rev. A 69, 053625 (2004), doi:10.1103/PhysRevA.69.053625.

[27] C. Mordini, D. Trypogeorgos, A. Farolfi, L. Wolswijk, S. Stringari, G. Lamporesi and G. Ferrari, Measurement of the canonical equation of state of a weakly interacting 3d Bose gas, Phys. Rev. Lett. 125, 150404 (2020), doi:10.1103/PhysRevLett.125.150404.

[28] R. J. Wild, P. Makotyn, J. M. Pino, E. A. Cornell and D. S. Jin, Measurements of Tan's contact in an atomic Bose-Einstein condensate, Phys. Rev. Lett. 108, 145305 (2012), doi:10.1103/PhysRevLett.108.145305.
 

[29] Z. Z. Yan, Y. Ni, C. Robens and M. W. Zwierlein, Bose polarons near quantum criticality, Science 368(6487), 190 (2020), doi:10.1126/science.aax5850.

[30] H. Ma and T. Pang, Condensate-profile asymmetry of a boson mixture in a disk-shaped harmonic trap, Phys. Rev. A 70, 063606 (2004), doi:10.1103/PhysRevA.70.063606.

[31] P. Jain and M. Boninsegni, Quantum demixing in binary mixtures of dipolar bosons, Phys. Rev. A 83, 023602 (2011), doi:10.1103/PhysRevA.83.023602.

[32] Borrmann, Peter and Franke, Gert, Recursion formulas for quantum statistical partition functions, The Journal of Chemical Physics 98(3), 2484 (1993), doi:10.1063/1.464180.

[33] Krauth, Werner, Statistical Mechanics Algorithms and Computations, Oxford University Press, Oxford, ISBN 9781429459501 1429459506 (2006).

[34] D. M. Ceperley, Path integrals in the theory of condensed helium, Rev. Mod. Phys. 67, 279 (1995), doi:10.1103/RevModPhys.67.279.

[35] P. Arnold, G. Moore and B. Tomásik,  \( T_{c} \)  for homogeneous dilute Bose gases: A second-order result, Phys. Rev. A 65, 013606 (2001), doi:10.1103/PhysRevA.65.013606.

[36] M. Boninsegni, N. V. Prokof'ev and B. V. Svistunov, Worm algorithm and diagrammatic Monte Carlo: A new approach to continuous-space path integral Monte Carlo simulations, Phys. Rev. E 74, 036701 (2006), doi:10.1103/PhysRevE.74.036701.

[37] A. Boudjemâa, Quantum and thermal fluctuations in two-component Bose gases, Phys. Rev. A 97, 033627 (2018), doi:10.1103/PhysRevA.97.033627.

[38] N. Guebli and A. Boudjemâa, Quantum self-bound droplets in Bose-Bose mixtures: Effects of higher-order quantum and thermal fluctuations, Phys. Rev. A 104, 023310 (2021), doi:10.1103/PhysRevA.104.023310.
 
