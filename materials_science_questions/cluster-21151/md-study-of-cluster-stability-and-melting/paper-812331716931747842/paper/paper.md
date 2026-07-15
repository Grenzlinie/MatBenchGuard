# Molecular Dynamics of Phase Transitions in Clusters of Alkali Halides

PEDRO C. R. RODRIGUES, $^{1}$ FERNANDO M. S. SILVA FERNANDES $^{1,2}$

$^{1}$ Department of Chemistry and Biochemistry, Faculty of Sciences, University of Lisboa,
Rua Ernesto de Vasconcelos, Bloco C8, 1749-016 Lisboa, Portugal
$^{2}$ Centre of Electrochemistry and Kinetics (CECUL), Faculty of Sciences, University of Lisboa, Rua
Ernesto de Vasconcelos, Bloco C8, 1749-016 Lisboa, Portugal

Received 3 October 2000; accepted 9 February 2001

**ABSTRACT:** Molecular dynamics simulations of unconstrained alkali halide clusters with 8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, and 8000 ions have been carried out using the Born-Mayer-Huggins potential. All the clusters exhibit first-order melting and freezing transitions. The melting temperature increases with the number of ions and approaches the melting temperature of the bulk. Clusters with a number of ions less than approximately 1000 present hysteresis cycles and practically do not have phase coexistence. Clusters with a number of ions over 1000 present phase coexistence during a significant part of the transition region and hysteresis is progressively eliminated as the clusters size increases. It is suggested that hysteresis is an intrinsic characteristic of small clusters. In the transition regions the calculations have been performed by fixing the total energy of the clusters. It is shown that such a technique provides a better way of analyzing the transition mechanism than the usual procedure of fixing the temperature by ad hoc rescaling the velocities or by using canonical molecular dynamics or Monte Carlo.
A detailed analysis of the melting transition is presented. The effects of interfaces and impurities are discussed. A method based on the velocity autocorrelation functions is proposed, in order to determine the molar fraction of the ions present in the solid and liquid phases as well as to produce colored snapshots of the phases in coexistence. The overall agreement of the estimated melting points and enthalpies of melting with the experiment is fairly good. The estimated melting point and enthalpy of melting for KCl in particular are in excellent agreement with the experimental values.
© 2001 John Wiley & Sons, Inc. Int J Quantum Chem 84: 169–180, 2001

**Key words:** ionic clusters; phase transitions; alkali halides; computer simulation; molecular dynamics

Correspondence to: F. Silva Fernandes; e-mail: fsilva@fc.ul.pt.
Contract grant sponsor: Fundação para a Ciência a Tecno- logia (FCT).

International Journal of Quantum Chemistry, Vol. 84, 169–180 (2001)
© 2001 John Wiley & Sons, Inc.

RODRIGUES AND SILVA FERNANDES

## Introduction

The study of phase transitions is a challenging subject to statistical mechanics. The ideal approach would be to calculate the partition function of a given system and determine its singular points. Yang and Lee established the rigorous conditions for the occurrence of singularities in the thermodynamic limit [1, 2]. Apart from the trivial cases and the brilliant "tour de force" by Onsager [3], on the two-dimensional Ising model, the exact calculation of the partition function is impractical for the majority of systems. Thus, the introduction of approximations is inevitable, generally to be treated by numerical methods. Among them, for instance, are the hypernetted mean spherical approximation [4] and the modified hypernetted-chain [5] theories.

If the emphasis is on critical properties and continuous phase transitions, a variety of theoretical methods [6, 7], as the renormalization group theory [7, 8], can be applied in order to solve the simplest model of a given universality class. A beautiful example is the order-disorder transition of the $\beta$-brass alloy described by the spin-1/2 Ising model. The theoretical results are in excellent agreement with the data from X-ray and neutron scattering [7].

Between theory and experiment are, of course, the computer simulation methods. Presently, there are a considerable number of well-founded simulation techniques to study phase transitions in bulk systems. From indirect methods [9, 10] to, for example, the direct Gibbs-Ensemble [10] and the Gibbs-Duhem integration [11-13] methods, the decision on the ones that should be applied essentially depends on the complexity of the systems and the properties to be probed. All these methods, though, rely on the imposition of some kind of periodic boundary conditions.

Clusters require a different treatment. Indeed, their space scale is very limited, so the application of the conventional periodic boundary conditions is out of the question. Thus, the simulations of such delicate systems are usually performed by pure microcanonical and canonical molecular dynamics, or Monte Carlo, either by letting the clusters be totally unconstrained (as in the present work) or constraining them in small cavities [14]. The simulation data can be compared with experimental results, if available, and used to test phenomenological, ab initio, or semiempirical approaches [14-16].

Clusters of atoms, molecules, and ions play an important role in the real world. Their thermal, structural, and dynamical properties are of interest in many fields, for example, crystal growth, gas phase nucleation, structure of amorphous materials, catalysis, and atmospheric chemistry [16].

As far as unconstrained alkali halide clusters are concerned, the results obtained so far [17-25] mainly for KCl with a number of ions in the range 8-512, show that all the clusters exhibit first-order melting and freezing transitions with notorious hysteresis cycles and some of them also present glass-like transitions. The main characteristic of those calculations is that they have been generally driven by the control of the temperature. That is, the properties of the clusters have been studied by increasing, or decreasing, the temperature using ad hoc rescaling of the velocities, canonical molecular dynamics, or Monte Carlo. When the solid is heated up, a temperature $T_{am}$, the so-called apparent melting temperature, is detected where the system jumps to a liquid-like state at about the same temperature and from there up it remains liquid. When the liquid is cooled down, a temperature $T_{af}$, the so-called apparent freezing temperature, is detected where the system jumps to a solid-like state at about the same temperature and from there down it remains solid. $T_{af}$ is always less than $T_{am}$, defining the hysteresis cycle. The melting temperature is usually taken as the arithmetic mean of $T_{am}$ and $T_{af}$.

In the present work, however, we have driven the systems by the control of the total energy instead of the control of temperature. As we shall see, this procedure is able to unravel some important details of the transitions mechanism that otherwise remain hidden.

There is some controversy on the origin of the observed hysteresis as to whether it is caused by size effects, artifacts of the simulations concerned with the heating and cooling rates, or even the lack of impurities in most of the computational models once impurities are always present in any real substance. Moreover, the simulation of bulk systems, by imposing the usual periodic boundary conditions, also present hysteresis cycles [26-28] giving rise to further questions about the effects of the boundary conditions on the transitions behavior.

In this article, we present extensive molecular dynamics results of the evolution of temperature versus total energy for some unconstrained alkali halide clusters of different sizes mainly focusing on the transition regions. We also propose a method based on the analysis of the velocity autocorrelation functions of the ions, in order to determine the molar fraction of the ions present in the solid and

---

170
VOL. 84, NO. 2

liquid phases as well as to produce colored snap- shots of the phases in coexistence. The estimated melting temperatures and enthalpies of melting are compared with the experimental ones for bulk sys- tems.

The main objective of this work is to realize a de- tailed analysis of the influence of the clusters' size on the melting and freezing transitions with empha- sis on the origin and attenuation of hysteresis, the role of interfaces, and the effect of impurities. Also, of utmost importance is the analysis of the behavior of clusters compared with the behavior of the corre- sponding systems in the thermodynamic limit. This work is a development of our previous investiga- tions [17, 24, 26] regarding the methodology used, the number of ions, which has been substantially in- creased, and the broader conclusions drawn.

In the next section we present the computational details. The study of the temperature versus total energy is presented in the third section. The method based on the velocity autocorrelation functions is explained in the fourth section together with the es- timated melting points and enthalpies of melting. The fifth section discusses the importance of the presence of impurities. Finally, the sixth section con- tains the conclusions of this work.

## Computational Details

The computations have been performed using the Born-Mayer-Huggins potential

$$
\phi_{i j}(r)=\frac{z_{i} z_{j} e^{2}}{r}+c_{i j} b \exp \left[\frac{\sigma_{i j}-r}{d}\right]-\frac{C_{i j}}{r^{6}}-\frac{D_{i j}}{r^{8}} \quad (1)
$$

with parameters given by Watts and McGee [29] and the Verlet's leapfrog algorithm [30] for the numer- ical integration of Newton's equations of motion. A time step of $0.5 × 10^{-14} \mathrm{~s}$ has been used in all sim ulations.

The number of time steps needed to obtain ac- curate results in a phase transition region is several orders of magnitude larger than the number needed for a homogeneous phase region. Thus, a prelimi- nary determination of the minimum number of time steps required to maintain the systems as stable has been carried out. The thermal properties have been calculated with a number of time steps in the range $1.6 × 10^{3}-4 × 10^{6}$, depending on the size of the clusters. The determination of the velocity au- tocorrelation functions have been based on runs of $1.6 × 10^{4}-4 × 10^{6}$ time steps with a time origin in every fifth step.

## MOLECULAR DYNAMICS OF PHASE TRANSITIONS

The starting point of the simulations for each cluster type and size has been the f.c.c. (rock salt) lattice at $0 \mathrm{~K}$. This is not, strictly, the minimal energy state for clusters, but it is good enough to ensure that the system does not become overheated, which would result in a premature melting process.

The systems have then been quickly heated up, by rescaling the velocities of the ions, to tempera- tures near the start of the melting. Once a melting point is reasonably detected, a long run has been done to compute the average temperature. After that, the total energy of the system has been in- creased by a small amount, the resulting average temperature has been calculated, and the proce- dure has been repeated until the system has entirely melted. Thus, during the melting, the calculation of each state point has been carried out by fixing the total energy of the system and determining the resulting average temperature, instead of fixing a preset average temperature and calculating the re- sulting total energy. This is a very important detail regarding the considerations of the next section.

A similar technique has been used for the freez- ing process, but in that case we have started from a totally melted configuration and the total energy has been decreased by small amounts.

It is essential that the increasing or decreasing of the total energy is done smoothly in order to get a good relaxation of the clusters.

The calculations have been carried out in a Silicon Graphics Origin 200 (4 × 180 MHz CPU's) at the computing services of the Faculty of Sciences, University of Lisboa; in a Silicon Graphics Octane (2 × 225 MHz CPU's) at our research group; and in a pool of 8 × 350 MHz Intel PII at our classroom laboratory.

## Study of Temperature Versus Total Energy

The starting point of our analysis is the depen- dence of the temperature on the total energy of the clusters computed as previously explained.

In Figure 1 we can see that the melting process follows a distinct path from the freezing process for a small cluster of LiCl with 512 ions. There are some aspects of the graphic that must be pointed out.

- The temperature differences corresponding to consecutive values of the total energy are small for the homogeneous solid and liquid phases. However, they become very signifi- cant during the transition process especially

---

INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

![](./images/812331716931747842_1.jpg)

FIGURE 1. Hysteresis cycle for a 512 ion LiCl cluster.

during the melting. This suggests the occur- rence of abrupt structural change when the total energy varies by a small amount.

It is noteworthy that the intrinsic fluctua- tions of temperature (not represented in the graphic) also increase during the transitions but they are orders of magnitude less than the differences referred to previously. As we shall see, as the system size increases, those differ- ences become progressively smaller.

- During the heating process there exists a value of the total energy for which the cluster sud- denly changes from near the solid curve to the liquid one if a small increase in the energy is made. A similar situation occurs in the freez- ing process.

We have tagged four temperature values that are important to subsequent considerations:
$TA$ is the maximum temperature at which the system remains solid during the heating;
$TB$ is the temperature after complete melting;
$TC$ is the lowest temperature of the liquid at which the system remains liquid during the cooling, and $TD$ is the temperature after the liquid-solid transition.

- There exists a significant region inside the polygon $TA$, $TB$, $TC$, $TD$ where there are no points, suggesting that the system does not present phase coexistence during most of the transition process.

In the Introduction we have referred to the main characteristic of most of the calculations carried out so far. They usually simulate small clusters coupled to a heat reservoir. However, in view of our present results, the way those calculations were conducted seems to hide the true nature of the hysteresis. In- deed they try to adjust the final average temperature of the cluster to a preset value by a continuous rescaling of the velocities. In the present calcula- tions, the systems are free to reach any final tem- perature according to its structural changes, for only the total energy is constrained. The two methods produce, of course, similar results for homogeneous phases, but in the transition region the results differ. In the present calculations we can see the signifi- cant decrease or increase of temperatures because the systems are free to do so. If a system is coupled to a heat reservoir when it starts to melt at temper- ature $TA$, the natural tendency of the system is, as we have seen, to decrease its temperature when the total energy is increased by a small amount. How- ever, if the temperature is constrained the cluster is not able to reach an equilibrium with the heat source until it receives enough energy, by a contin- uous rescaling of the velocities, and jumps to the liquid state at approximately temperature $TA$. This suggests that the small cluster is not able to main- tain a solid-liquid coexistence at temperature $TA$.

A similar process occurs in the freezing transition giving $TA$ and $TC$ as the melting and freezing points, respectively.

Thus, we can point out at least two contributions for the hysteresis:

1. $TA$ and $TB$ are different,

MOLECULAR DYNAMICS OF PHASE TRANSITIONS

2. $TC$ is not coincident with $TB$; the resulting freezing point is at $TC$ enlarging the hysteresis interval.

This temperature-energy dependence behavior, in the transition region, is presumably due to the significant additional work that would be needed for a small cluster, in which a considerable number of the ions are at its envelope surface, to form an interface.

To proceed into a deeper analysis we have performed calculations for other cluster sizes and types searching for conditions that increase or decrease the hysteresis cycles.

We believe that increasing the clusters' size will progressively eliminate hysteresis. Therefore, we have simulated clusters with a number of ions as big as 8000.

Due to the computational power required we have concentrated our efforts in the melting process. The analysis of the freezing for the bigger clusters is still in progress and will be reported in a future article.

Figures 2 and 3 display, respectively, the results of the simulations for a set of lithium chloride and potassium chloride clusters of different sizes. Some of the corresponding numerical values are given in the Appendix.

It is notorious that there is an asymptotic approach to a melting process at approximately constant temperature as the clusters' size increases. Nevertheless, at the end of the melting, a significant decrease in temperature is still observed even for the biggest cluster studied. We shall return to this in the fifth section.

The regions where the melting is done at an approximately constant temperature suggests that there exists phase coexistence among them as is explained in following section.

# Study of the Phases in Coexistence. Melting Points and Enthalpies of Melting

In order to approach the problem of the coexistence of phases, a method based on the analysis of the velocity autocorrelation functions (VACF's) of the ions is presented. The method consists of finding a time window where the VACF's of each particle in the solid or liquid part of the system can be distinguished. This is possible if there exists a window where the individual functions evaluated for the entirely solid system, just before melting, do not overlap with the corresponding functions for the entirely liquid system immediately after melting.

There are three essential conditions that must be verified to allow the use of the method.

- Firstly, the exact VACF's are really distinguishable.
- Secondly, there exists a time window where the numerically computed functions can be

![](./images/812331716931747842_2.jpg)

FIGURE 2. Temperature versus total energy on melting for LiCl clusters.

INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

![](./images/812331716931747842_3.jpg)

FIGURE 3. Temperature versus total energy on melting for KCI clusters.

evaluated with sufficient accuracy in order to be distinguished.

- Thirdly, a large majority of the particles remains in the same phase during the simulation.

These conditions are fulfilled at least for the cases we have studied.

In what follows we shall refer to the location of the time window in terms of time step numbers because this is preferable under an operational context.

As an example, Figure 4 shows the individual VACF's of the cations, before and after melting, for a KCI cluster with 5832 ions.

The zoom in the region of the time window is shown in Figure 5. It is clear that between steps 32 and 40 approximately, the individual functions for the entirely liquid system take values greater than the corresponding values for the entirely solid system. This corresponds to a range 0.16–0.2 ps.

The location of the time window and the values of the VACF's are greatly independent on the cluster size, but they depend on the cluster type. Inside

![](./images/812331716931747842_4.jpg)

FIGURE 4. VACF's of the cations for a 5832 ions cluster of KCI.

MOLECULAR DYNAMICS OF PHASE TRANSITIONS

![](./images/812331716931747842_5.jpg)

FIGURE 5. Zoom of Figure 4 in the region of the time window.

that window we have chosen a point staying approximately in the middle of the solid and liquid covered regions. The chosen point corresponds to the time step 32 and a VACF value of $-0.22$. Now, for each state of the melting region, if a particle has a VACF value at step 32 greater than $-0.22$, then it is counted as an element of the liquid and red colored, or else it is counted as an element of the solid and blue colored. The choice of the decision point is, of course, somewhat arbitrary, but we have checked out that our main conclusions are independent, providing that the point is taken approximately at the middle of the time window.

Figure 6 displays a snapshot of the referred to cluster obtained along the melting region. (To improve clarity, only the cations are represented.) The agreement of the intuitive visual analysis with the structural order expected for solid-liquid coexistence is quite good.

Once we are able to count the particles belonging to each phase, the calculation of the respective molar fractions is straightforward. We have applied the method to a set of states along the melting regions of different cluster types. Figures 7 and 8 show, respectively, the molar fraction of the liquid versus the total energy for clusters of LiCl and KCl with different number of ions. For clarity, only the most representative results are displayed.

We must point out that the coexistence of phases is well confirmed for the bigger clusters. The intermediate sized clusters in the range of 216–1000 ions practically do not present phase coexistence but in a very small energy interval. As expected there are noticeable differences between the smaller clusters of LiCl and KCl. Although we still do not have results for the molar fractions of LiCl clusters as big as the KCl ones, the study of LiCl with 2744 ions suggests that it will quickly approach the KCl behavior as far as the molar fractions are concerned.

As we have pointed out at the end of the last section, there is an asymptotic approach to a melt-

![](./images/812331716931747842_6.jpg)

FIGURE 6. Snapshot of a 5832 ions cluster of KCl
(only the cations are represented).

INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

![](./images/812331716931747842_7.jpg)

FIGURE 7. Liquid phase molar fractions of LiCl clusters.

ing process at constant temperature as the clusters' size increases. Therefore, it seems plausible that the values of the temperature at which such behavior is detected should approach the melting temperatures of the bulk. Table I presents the estimated melting temperatures of some unconstrained alkali halide clusters of different sizes together with the experimental values for the bulk systems.

The overall agreement is fairly good. The agreement for KCl, in particular, is excellent. Woodcock and Singer [31] have shown, many years ago, that the Born-Mayer-Huggins potential predicts the correct experimental melting temperature of KCl. Note that our simulation results also predict that the melting point of NaCl is greater than the melting point of KCl in accordance with the experiment. The estimated melting point of LiCl is the worst value, when compared with the experimental one, despite that it has been obtained from the biggest cluster studied. This is presumably due to the Born-Mayer-Huggins potential, used in the present simulations, being a rigid ion model. As such, it does not take

![](./images/812331716931747842_8.jpg)

FIGURE 8. Liquid phase molar fractions of KCl clusters.

<table><caption>TABLE I<br>Experimental and estimated melting temperatures for some alkali halides.</caption>
<thead>
  <tr>
    <th></th>
    <th>Exp. (K)</th>
    <th>Our (K)</th>
    <th>Size</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>LiCl</td>
    <td>887</td>
    <td>≈750</td>
    <td>8000</td>
  </tr>
  <tr>
    <td>NaCl</td>
    <td>1074</td>
    <td>≈1050</td>
    <td>1728</td>
  </tr>
  <tr>
    <td>KCl</td>
    <td>1049</td>
    <td>1044 ± 35</td>
    <td>5832</td>
  </tr>
  <tr>
    <td>NaBr</td>
    <td>1028</td>
    <td>≈950</td>
    <td>1000</td>
  </tr>
</tbody>
</table>

properly into account the high polarizability effects of $Li^+$, although it predicts that LiCl has the smallest melting point of the alkali chlorides family in accordance with the experiment.

The enthalpy of melting can be directly calculated from the temperature-total energy diagrams, tracing a horizontal line from the solid phase curve to the liquid one, through the transition states of approximately constant temperature, and taking the difference of energies at the intersection points. Additionally, the enthalpy of melting can also be estimated from the liquid molar fractions plots, taking the segment of the molar fraction curve that is nearly linear and calculating the difference of energies at its intersection points with the $y = 0$ and $y = 1$ lines. The comparison between the values worked out by the two methods should be a further measure of the soundness of the present calculations and of the VACF's method. Table II contains the results for KCl clusters of different sizes. The agreement of the estimated enthalpy of melting with the experimental ones (eg. 25.5 [32] and eg. 26.5 [33] kJ mol⁻¹) is excellent. As expected, the direct method gives a better convergence than the VACF method. Nevertheless, it shows a clear convergence to the correct value as the number of ions increases.

<table><caption>TABLE II<br>Enthalpy of melting for KCI clusters.</caption>
<thead>
  <tr>
    <th rowspan="2">Size</th>
    <th>Direct</th>
    <th>VACFs</th>
  </tr>
  <tr>
    <th>kJ mol⁻¹</th>
    <th>kJ mol⁻¹</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>512</td>
    <td>22.6 ± 1.1</td>
    <td>—</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>22.7 ± 5.7</td>
    <td>13.8 ± 10.9</td>
  </tr>
  <tr>
    <td>1728</td>
    <td>22.8 ± 9.1</td>
    <td>14.1 ± 5.1</td>
  </tr>
  <tr>
    <td>2744</td>
    <td>23.8 ± 4.8</td>
    <td>14.6 ± 3.4</td>
  </tr>
  <tr>
    <td>4096</td>
    <td>24.7 ± 4.8</td>
    <td>18.0 ± 3.3</td>
  </tr>
  <tr>
    <td>5832</td>
    <td>25.4 ± 2.3</td>
    <td>17.4 ± 2.3*</td>
  </tr>
</tbody>
</table>

# MOLECULAR DYNAMICS OF PHASE TRANSITIONS

The star in the last VACF value means that calculations are still in progress to obtain better statistics.

## Importance of the Presence of Impurities

As we have pointed out in the third section the asymptotic approach to a melting process at constant temperature for the larger clusters studied breaks down at the end of the melting line. This is clearly observed in the temperature-total energy plots as well as in the plots of the liquid molar fractions. The persistence of such behavior is apparently surprising, when compared with the behavior at the initial region of the melting, suggesting a specific source for it.

Figure 9 shows a snapshot of a cluster of LiCl with 5832 ions at the end of the melting process. That final zone clearly corresponds to a very small amount of crystal inside a liquid bubble. Thus, it seems plausible to presume that there is a hindrance of the cluster in attaining a reversible state between the nucleation-crystal growth processes and the liquid. This behavior was thoroughly confirmed starting from different sets of initial conditions.

![](./images/812331716931747842_9.jpg)

FIGURE 9. Snapshot of a LiCl cluster at the end of the melting.

---

INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

RODRIGUES AND SILVA FERNANDES

Therefore, it turns out as an intrinsic characteristic of the cluster in this region.

In order to study these aspects we have set up a model with an impurity inserted into a 8000 ions cluster of LiCl. The impurity is a small 64 ion subcluster of NaF. The parameters of the Born–Mayer–Huggins potential for the subcluster have been modified to ensure that it does not break during the simulation. Although most of the calcu- lations are still in progress and a further thorough analysis is needed, the preliminary results show that the residual hysteresis is significantly reduced, at least, by an amount of 25%.

## Conclusions

From the results and discussions presented in the last sections the following general conclusions can be drawn.

- Clusters with a number of ions less than 200 do not have phase coexistence, but oscillate between the two phases during the transition with pronounced hysteresis cycles.
- Clusters with a number of ions between 200 and 1000, approximately, also have notorious hysteresis cycles, but show some tendency to establish a solid–liquid coexistence in very small energy intervals.
- Clusters with a number of ions greater than 1000 present phase coexistence during part of the melting process characterized by an ap- proximate constant temperature. At the end of the melting line, however, this behavior breaks down with more abrupt changes in the temperature.

Two main sources for the observed hysteresis are suggested.

- The interfacial energy contribution leads to a hindrance of phase coexistence when the in- terface size is of the same order of magnitude as the size of the whole system.
- Nucleation difficulties lead to a supercooling of the liquid before it starts to freeze.

The breakdown of the quasiconstant tempera- ture behavior at the end of the melting line of the larger clusters studied is presumably a consequence of the simultaneous action of those contributions. Indeed, once a fluctuation makes a crystal smaller, its reconstruction becomes more difficult, for this would increase the interface size. Thus, the presence of impurities, which can work as nucleation seeds, contributes significantly to reduce the residual hys- teresis, at least during the melting transition. The present results suggest that hysteresis is an intrin- sic characteristic of small clusters. As the clusters' size increases there is an asymptotic approach to a melting process at approximately constant temper- ature.

The overall agreement of the estimated melting points with the experimental ones is fairly good. In particular, the estimated melting point of KCl is in excellent agreement with the experimental value. The same is true for the enthalpy of melting.

The calculations have been carried out by fixing the total energy of the clusters. It has been shown that such a technique definitely provides a better way of analyzing the transitions mechanism than the usual procedure of fixing a preset temperature by an ad hoc rescaling the velocities or by using canonical molecular dynamics or Monte Carlo. In- deed, it is able to unravel some important details of the transitions mechanism which otherwise remain hidden.

A method based on the velocity autocorrelation functions has been proposed, in order to determine the molar fraction of the ions present in the solid and liquid phases as well as to produce colored snapshots of the phases in coexistence. The good qualitative results obtained and the correct conver- gence of the enthalpy of melting, calculated from the molar fractions plots, show that the method provides an operational procedure to analyze the properties of clusters.

We must emphasize that the calculations were conducted at virtually zero pressure, for the clus- ters were totally unconstrained. This certainly is a limitation of our present analysis. It is possible, however, to apply some kind of constraints in order to determine the $T(E)$ curves at other pressure val- ues. Although it is impractical to calculate partition functions and other relevant thermodynamic quan- tities directly from molecular dynamics, such sim- ulations would be invaluable as a screening tool for semiquantitative calculations. Work is in progress to study these aspects and a wider variety of systems, as well as, to develop other methods for analyzing the phases in coexistence and methods to measure the surface and interface properties of clusters.

Finally, it is worth mentioning that our results are in accordance with the basic principles of first-


MOLECULAR DYNAMICS OF PHASE TRANSITIONS

order phase transitions. In fact, the theory of Yang and Lee, referred to in the Introduction, shows that only in the thermodynamic limit do singularities in the partition function correspond to exactly horizontal transition isotherms. For finite systems it is expected that the predictions of statistical mechanics will be approached as the number of particles increases. This behavior has clearly been observed in the present work.

## ACKNOWLEDGMENTS
We thank Fundação para a Ciência e Tecnologia (FCT) for financial support and the Computing Services at Faculty of Sciences, University of Lisboa, for the allocation of computer time.

## Appendix

Numerical values of total energy and temperature through solid liquid transitions.

<table>
<thead>
<tr>
<th colspan="2">LiCl 1000</th>
<th colspan="2">LiCl 8000</th>
<th colspan="2">KCl 512</th>
<th colspan="2">KCl 5832</th>
</tr>
<tr>
<th>E/kJ mol⁻¹</th>
<th>T/K</th>
<th>E/kJ mol⁻¹</th>
<th>T/K</th>
<th>E/kJ mol⁻¹</th>
<th>T/K</th>
<th>E/kJ mol⁻¹</th>
<th>T/K</th>
</tr>
</thead>
<tbody>
<tr>
<td>−799.638</td>
<td>635.937</td>
<td>−799.648</td>
<td>731.98</td>
<td>−643.113</td>
<td>894.486</td>
<td>−643.078</td>
<td>1029.86</td>
</tr>
<tr>
<td>−799.414</td>
<td>637.559</td>
<td>−799.39</td>
<td>734.441</td>
<td>−642.803</td>
<td>901.235</td>
<td>−642.717</td>
<td>1039.16</td>
</tr>
<tr>
<td>−799.187</td>
<td>638.453</td>
<td>−799.133</td>
<td>735.512</td>
<td>−642.482</td>
<td>904.984</td>
<td>−642.354</td>
<td>1044.6</td>
</tr>
<tr>
<td>−798.963</td>
<td>644.703</td>
<td>−798.873</td>
<td>735.521</td>
<td>−642.168</td>
<td>910.801</td>
<td>−641.987</td>
<td>1050.74</td>
</tr>
<tr>
<td>−798.733</td>
<td>647.787</td>
<td>−798.615</td>
<td>740.397</td>
<td>−641.849</td>
<td>914.996</td>
<td>−641.62</td>
<td>1048</td>
</tr>
<tr>
<td>−798.502</td>
<td>646.123</td>
<td>−798.353</td>
<td>736.159</td>
<td>−641.532</td>
<td>918.085</td>
<td>−641.25</td>
<td>1053.51</td>
</tr>
<tr>
<td>−798.27</td>
<td>655.647</td>
<td>−798.093</td>
<td>736.506</td>
<td>−641.213</td>
<td>924.863</td>
<td>−640.882</td>
<td>1053.5</td>
</tr>
<tr>
<td>−798.04</td>
<td>661.087</td>
<td>−797.835</td>
<td>734.681</td>
<td>−640.893</td>
<td>930.011</td>
<td>−640.513</td>
<td>1052.27</td>
</tr>
<tr>
<td>−797.808</td>
<td>659.833</td>
<td>−797.575</td>
<td>732.848</td>
<td>−640.564</td>
<td>934.307</td>
<td>−640.143</td>
<td>1052.51</td>
</tr>
<tr>
<td>−797.575</td>
<td>665.088</td>
<td>−797.317</td>
<td>738.145</td>
<td>−640.23</td>
<td>939.317</td>
<td>−639.777</td>
<td>1049.93</td>
</tr>
<tr>
<td>−797.343</td>
<td>657.464</td>
<td>−797.058</td>
<td>738.008</td>
<td>−639.898</td>
<td>942.4</td>
<td>−639.41</td>
<td>1036.47</td>
</tr>
<tr>
<td>−797.11</td>
<td>664.827</td>
<td>−796.799</td>
<td>734.951</td>
<td>−639.566</td>
<td>948.685</td>
<td>−639.046</td>
<td>1040.26</td>
</tr>
<tr>
<td>−796.873</td>
<td>671.286</td>
<td>−796.54</td>
<td>741.185</td>
<td>−639.23</td>
<td>953.213</td>
<td>−638.683</td>
<td>1037.77</td>
</tr>
<tr>
<td>−796.638</td>
<td>673.096</td>
<td>−796.278</td>
<td>734.555</td>
<td>−638.892</td>
<td>958.022</td>
<td>−638.32</td>
<td>1039.54</td>
</tr>
<tr>
<td>−796.401</td>
<td>671.174</td>
<td>−796.018</td>
<td>742.083</td>
<td>−638.557</td>
<td>962.694</td>
<td>−637.956</td>
<td>1025.86</td>
</tr>
<tr>
<td>−796.166</td>
<td>670.287</td>
<td>−795.756</td>
<td>740.037</td>
<td>−638.219</td>
<td>967.793</td>
<td>−637.597</td>
<td>1037.6</td>
</tr>
<tr>
<td>−795.932</td>
<td>674.305</td>
<td>−795.494</td>
<td>733.799</td>
<td>−637.881</td>
<td>974.977</td>
<td>−637.237</td>
<td>1021.37</td>
</tr>
<tr>
<td>−795.693</td>
<td>677.812</td>
<td>−795.235</td>
<td>734.705</td>
<td>−637.537</td>
<td>979.181</td>
<td>−636.88</td>
<td>1014.44</td>
</tr>
<tr>
<td>−795.456</td>
<td>654.169</td>
<td>−794.976</td>
<td>737.433</td>
<td>−637.199</td>
<td>983.251</td>
<td>−636.524</td>
<td>1017.52</td>
</tr>
<tr>
<td>−795.224</td>
<td>643.788</td>
<td>−794.716</td>
<td>735.603</td>
<td>−636.854</td>
<td>988.219</td>
<td>−636.168</td>
<td>1012.58</td>
</tr>
<tr>
<td>−794.994</td>
<td>677.021</td>
<td>−794.456</td>
<td>739.053</td>
<td>−636.518</td>
<td>991.162</td>
<td>−635.817</td>
<td>1006.84</td>
</tr>
<tr>
<td>−794.756</td>
<td>680.012</td>
<td>−794.197</td>
<td>737.746</td>
<td>−636.164</td>
<td>993.634</td>
<td>−635.468</td>
<td>997.626</td>
</tr>
<tr>
<td>−794.517</td>
<td>684.909</td>
<td>−793.938</td>
<td>730.462</td>
<td>−635.81</td>
<td>999.772</td>
<td>−635.117</td>
<td>1011.76</td>
</tr>
<tr>
<td>−794.274</td>
<td>694.869</td>
<td>−793.684</td>
<td>728.33</td>
<td>−635.461</td>
<td>1007.3</td>
<td>−634.766</td>
<td>1003.84</td>
</tr>
<tr>
<td>−794.032</td>
<td>691.22</td>
<td>−793.427</td>
<td>731.253</td>
<td>−635.106</td>
<td>1001.67</td>
<td>−634.416</td>
<td>997.261</td>
</tr>
<tr>
<td>−793.785</td>
<td>705.195</td>
<td>−793.168</td>
<td>730.351</td>
<td>−634.753</td>
<td>1016.55</td>
<td>−634.068</td>
<td>993.237</td>
</tr>
<tr>
<td>−793.533</td>
<td>705.826</td>
<td>−793.095</td>
<td>726.378</td>
<td>−634.4</td>
<td>1009.9</td>
<td>−633.721</td>
<td>1003.78</td>
</tr>
<tr>
<td>−793.284</td>
<td>701.356</td>
<td>−792.838</td>
<td>721.65</td>
<td>−634.052</td>
<td>995.392</td>
<td>−633.373</td>
<td>991.263</td>
</tr>
<tr>
<td>−793.041</td>
<td>683.653</td>
<td>−792.585</td>
<td>718.733</td>
<td>−633.692</td>
<td>1030.23</td>
<td>−633.023</td>
<td>999.127</td>
</tr>
<tr>
<td>−792.796</td>
<td>681.241</td>
<td>−792.332</td>
<td>718.216</td>
<td>−633.326</td>
<td>1035.51</td>
<td>−632.674</td>
<td>996.245</td>
</tr>
<tr>
<td>−792.553</td>
<td>684.266</td>
<td>−792.079</td>
<td>712.684</td>
<td>−632.969</td>
<td>1040.28</td>
<td>−632.325</td>
<td>989.627</td>
</tr>
<tr>
<td>−792.313</td>
<td>705.754</td>
<td>−791.828</td>
<td>709.396</td>
<td>−632.61</td>
<td>1032.71</td>
<td>−631.977</td>
<td>988.341</td>
</tr>
<tr>
<td>−792.065</td>
<td>685.236</td>
<td>−791.579</td>
<td>708.397</td>
<td>−632.265</td>
<td>1013.59</td>
<td>−631.634</td>
<td>988.944</td>
</tr>
<tr>
<td>−791.827</td>
<td>673.06</td>
<td>−791.33</td>
<td>700.103</td>
<td>−631.915</td>
<td>1051.66</td>
<td>−631.731</td>
<td>985.713</td>
</tr>
<tr>
<td>−791.589</td>
<td>640.347</td>
<td>−791.082</td>
<td>694.798</td>
<td>−631.555</td>
<td>1038.42</td>
<td>−631.388</td>
<td>976.618</td>
</tr>
<tr>
<td>−791.368</td>
<td>614.019</td>
<td>−790.839</td>
<td>686.945</td>
<td>−631.205</td>
<td>933.961</td>
<td>−631.046</td>
<td>979.735</td>
</tr>
<tr>
<td>−791.15</td>
<td>615.579</td>
<td>−790.597</td>
<td>688.671</td>
<td>−630.867</td>
<td>948.734</td>
<td>−630.707</td>
<td>968.7</td>
</tr>
<tr>
<td>−790.932</td>
<td>620.08</td>
<td>−790.356</td>
<td>678.832</td>
<td>−630.544</td>
<td>913.41</td>
<td>−630.366</td>
<td>979.664</td>
</tr>
<tr>
<td>−790.713</td>
<td>624.8</td>
<td>−790.117</td>
<td>677.595</td>
<td>−630.216</td>
<td>943.732</td>
<td>−630.025</td>
<td>970.594</td>
</tr>
<tr>
<td>−790.49</td>
<td>626.246</td>
<td>−789.878</td>
<td>683.383</td>
<td>−629.891</td>
<td>922.344</td>
<td>−629.686</td>
<td>972.426</td>
</tr>
<tr>
<td>−790.272</td>
<td>629.675</td>
<td>−789.637</td>
<td>685.001</td>
<td>−629.589</td>
<td>792.894</td>
<td>−629.347</td>
<td>976.569</td>
</tr>
<tr>
<td>−790.05</td>
<td>629.64</td>
<td>−789.394</td>
<td>687.415</td>
<td>−629.315</td>
<td>787.317</td>
<td>−629.006</td>
<td>982.687</td>
</tr>
</tbody>
</table>

INTERNATIONAL JOURNAL OF QUANTUM CHEMISTRY

RODRIGUES AND SILVA FERNANDES

### References

1. Ruelle, D. Statistical Mechanics. Rigorous Results; Benjamin: New York, 1969.

2. Huang, K. Statistical Mechanics; John Wiley and Sons: New York, 1987.

3. Onsager, L. Phys Rev 1944, 65, 117.

4. Cheng, A.; Klein, M.; Caccamo, C. Phys Rev Lett 1993, 71, 1200.

5. Caccamo, C. Phys Rev 1995, 51, 3387.

6. Stanley, H. E. Introduction to Phase Transitions and Critical Phenomena; Oxford University Press: Oxford, 1971.

7. Yeomans, J. M. Statistical Mechanics of Phase Transitions; Claredon Press: Oxford, 1992.

8. Wilson, K. W. Rev Mod Phys 1983, 55, 583.

9. Allen, M.; Tildesley, D. Computer Simulation of Liquids; Claredon Press: Oxford, 1987.

10. Panagiotopoulos, A.; Quirke, N.; Stapleton, M.; Tildsley, D. Mol Phys 1988, 63, 527.

11. Kofke, D. J Chem Phys 1993, 98, 4149.

12. Agrawal, R.; Kofke, D. Mol Phys 1995, 85, 23.

13. Agrawal, R.; Kofke, D. Mol Phys 1995, 85, 43.

14. Quirke, N. Mol Simulation 1988, 1, 249.

15. Halicioglu, T.; Bauschlicher, Jr., C. Rep Prog Phys 1988, 51, 883.

16. Sugano, S. H. K. Microcluster Physics; Springer: New York, 1998.

17. Fernandes, F. S. Ph.D. thesis, University of Shouthampton, 1977.

18. Amini, M. D. F.; Hockney, R. W. J Phys C Solid St Phys 1979, 12, 4707.

19. Amini, M. D. F.; Hockney, R. W. J Phys C Solid St Phys 1980, 13, L221.

20. Amini, M.; Hockney, R. W. J Non Cryst Solids 1979, 31, 447.

21. Rose, J.; Berry, R. J Chem Phys 1991, 96, 517.

22. Rose, J.; Berry, R. J Chem Phys 1993, 98, 3246.

23. Rose, J.; Berry, R. J Chem Phys 1993, 98, 3262.

24. Fernandes, F.; Neves, L. in American Institute of Physics Conference Proceedings; Bernardi, F.; Rivail, J. L., Eds.; 1995, 330, 313.

25. Fernandes, F.; Rodrigues, P. 1998, URL http://elixir.dqb.fc.ul.pt.

26. Fernandes, F. S. unpublished results.

27. Chokappa, D.; Clancy, P. Mol Phys 1987, 61, 597.

28. Chokappa, D.; Clancy, P. Mol Phys 1987, 61, 617.

29. Watts, R.; McGee, I. Liquid State Chemical Physics; John Wi- ley and Sons: New York, 1976, pp. 307-312.

30. Rapaport, D. The Art of Molecular Dynamics Simula- tion; Cambridge University Press: Cambridge, 1995, pp. 57, 58.

31. Woodcock, L.; Singer, K. Transactions of the Faraday Society 1971, 67, 577.

32. Rice, S.; Klemperer, W. J Chem Phys 1957, 27, 573.

33. Dworkin, A.; Bredig, M. J Phys Chem 1960, 64, 269.
