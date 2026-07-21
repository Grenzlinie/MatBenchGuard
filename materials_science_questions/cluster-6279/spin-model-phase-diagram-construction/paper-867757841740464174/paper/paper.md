
# Monte Carlo simulation of the three-dimensional XY model with bilinear-biquadratic exchange interaction

H. Nagata \( ^{a} \) , M. Žukovič \( ^{b} \)  and T. Idogaki \( ^{a*} \) 

 \( ^{a} \)  Department of Applied Quantum Physics, Kyushu University

 \( ^{b} \)  Institute of Environmental Systems, Kyushu University

Abstract. The three-dimensional XY model with bilinear-biquadratic exchange interactions J and  \( J' \) , respectively, has been studied by Monte Carlo simulations. From the detailed analysis of the thermal variation of various physical quantities, as well as the order parameter and energy histogram analysis, the phase diagram including two different ordered phases has been determined. There is a single phase boundary from a paramagnetic to a dipole-quadrupole ordered phase, which is of second order in a high  \( J/J' \)  ratio region, changing to a first-order one for  \( 0.35 \leq J/J' \leq 0.5 \) . Below  \( J/J' = 0.35 \)  there are two separate transitions: the first one to the quadrupole long-range order (QLRO) phase at higher temperatures, followed by another one to the dipole-quadrupole long-range order (DLRO) phase at lower temperatures. The finite-size scaling analysis yields values of the critical exponents for both the DLRO and QLRO transitions close to the values for the conventional XY model which includes no biquadratic exchange.

PACS codes: 75.10.Hk; 75.30.Kz; 75.40.Cx; 75.40.Mg.

Keywords: XY model; Bilinear-biquadratic exchange; Phase transition; Quadrupole ordering; Histogram Monte Carlo simulation;

 \( ^{*} \) Corresponding author.

Permanent address: Department of Applied Quantum Physics, Faculty of Engineering,
 

Kyushu University, Fukuoka 812-8581, Japan

Tel.: +81-92-642-3810; Fax: +81-92-633-6958
 

## 1. Introduction

The problem of biquadratic (or generally higher-order) interactions has attracted much attention for several decades now. For systems with Heisenberg symmetry and spin S = 1 it has been tackled by mean field approximation (MFA) \( ^{1} \) , high-temperature series expansion (HTSE) calculations \( ^{2} \) , as well as within a framework of some other approximative schemes \( ^{3,4} \) . The case of S > 1 has also been treated by MFA \( ^{5,6} \) . Those studies have shown that the biquadratic interactions can induce various interesting properties such as tricritical and triple points, quadrupole ordering, separate dipole and quadrupole phase transitions etc. The problem of the biquadratic interactions in systems with XY spin symmetry, however, has had received much less attention. The case S = 1 has been addressed, however, only in a high  \( J/J' \)  ratio region where the biquadratic exchange has no significant influence on phase transitions \( ^{7} \) . Chen et al for the first time looked into the problem of the critical exponents for the phase transitions in the classical XY model with the bilinear-biquadratic exchange. They used HTSE to calculate transition temperatures and critical exponents for cubic lattices in the region of  \( J/J' \geq 1^{8} \) . However, based on the MFA assumption that for  \( J/J' < 1 \)  the transition to the dipole long-range order (DLRO) phase is of first order, they limited their calculations in this region only to the separate quadrupole long-range order (QLRO) transitions taking place for  \( 0 < J/J \leq 0.35^{9} \) . Here we note, however, that the rigorous proof of the existence of dipole and quadrupole long-range order at finite temperature on the classical bilinear-biquadratic exchange model has been provided only recently \( ^{10,11} \) .

In the present paper we focus on the region of comparatively low  \( J/J' \)  ( \( \leq 1 \) ), which is the most interesting from the point of view of the critical behaviour but, at the same time, the least elucidated. We use standard Monte Carlo (SMC) and histogram Monte Carlo (HMC) simulations, and investigate the possible kinds of long-range ordering, their nature, and critical exponents, for a classical XY ferromagnet with biquadratic exchange on a simple cubic lattice. The obtained phase diagram captures all important features induced by the biquadratic exchange such as separate dipole and quadrupole ordering, first-order transitions, and consequently the triple and tricritical points appearance. Furthermore, we perform a finite-size scaling (FSS) analysis in order to calculate the susceptibility and correlation length critical exponents,  \( \nu \)  and  \( \gamma \) , respectively, for both DLRO and QLRO.
 

transitions.

## 2. Model and Monte Carlo simulation

The classical XY model with bilinear-biquadratic exchange interactions can be described by the Hamiltonian

 \[ H=-J\sum_{\langle i,j\rangle}\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{j}-J^{\prime}\sum_{\langle i,j\rangle}(\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{j})^{2}, \quad (1) \] 

where  \( \boldsymbol{S}_{i}=(S_{ix},S_{iy}) \)  is a two-dimensional unit vector at the ith lattice site,  \( \langle i,j\rangle \)  denotes the sum over nearest neighbors, and J,  \( J^{\prime}>0 \)  are the bilinear and biquadratic exchange interaction constants, respectively. It is known that such a spin system displays long-range ordering of both dipole and quadrupole moments. The order parameters corresponding to the respective kinds of ordering are the dipole long-range order (DLRO) and the quadrupole long-range order (QLRO) parameters, m and q, respectively, defined by

 \[ m=\langle M\rangle/N,\mathrm{w h e r e}M=\left[\left(\sum_{i}S_{i x}\right)^{2}+\left(\sum_{i}s_{i y}\right)^{2}\right]^{\frac{1}{2}}, \quad (2) \] 

 \[ q=\langle Q\rangle/N,\mathrm{w h e r e}Q=\left[\left(\sum_{i}\left((S_{i x})^{2}-(S_{i y})^{2}\right)\right)^{2}+\left(\sum_{i}2S_{i x}S_{i y}\right)^{2}\right]^{\frac{1}{2}}, \quad (3) \] 

where N is the total number of the lattice sites, and  \( \langle\cdots\rangle \)  denotes the thermal average. The respective orders are schematically depicted in Fig.1. DLRO corresponds to the ferromagnetic directional arrangement of spins while QLRO represents an axially ordered state in which spins can point either direction along the axis of ordering. Obviously, DLRO always includes QLRO and, hence, DLRO actually represents dipole-quadrupole long-range order.

In our simulations we first perform standard Monte Carlo (SMC) simulations on systems of the linear lattice size up to L = 24, assuming periodic boundary condition throughout. Spin updating follows a Metropolis dynamics and averages are calculated using  \( 1 \times 10^{4} \)  Monte Carlo steps per spin (MCS/s) after equilibrating over another  \( 5 \times 10^{3} \)  MCS/s. Besides DLRO and QLRO parameters m and q, we calculate the system internal energy E, and the specific heat per site c, calculated from energy fluctuations by

 \[ c=\frac{\left(\langle E^{2}\rangle-\langle E\rangle^{2}\right)}{N k_{B}T^{2}}, \quad (4) \]
 

the susceptibility per site  \( \chi_{O} \) , calculated from LRO parameters fluctuations by

 \[ \chi_{O}=\frac{(\langle O^{2}\rangle-\langle O\rangle^{2})}{Nk_{B}T}, \quad (5) \] 

and the fourth-order long-range order (LRO) cumulant (Binder parameter)  \( g_{O} \)  as

 \[ g_{O}=2-\frac{\langle O^{4}\rangle}{\langle O^{2}\rangle^{2}}, \quad (6) \] 

where O stands for the respective parameters M and Q.

Temperature dependence of these quantities gives us an estimate of the location, as well as nature of a transition. First-order transitions are usually accompanied by discontinuities in order parameters and energy, and hysteresis when cooling and heating. If transition is second order, it can be roughly located by the c peak position or, alternatively, by the position of the fourth-order LRO cumulant curves intersection for various lattice sizes.

In order to obtain more reliable and more precise data, we further perform histogram Monte Carlo (HMC) calculations, developed by Ferrenberg and Swendsen \( ^{12,13} \) , at the transition temperatures estimated from the SMC calculations for each lattice size. Here we also treat larger lattice sizes (up to L = 30), and thermal averages are taken over  \( 2 \times 10^{6} \)  MCS after discarding another  \( 1 \times 10^{6} \)  MCS used for bringing the system into the thermal equilibrium. We calculate the energy histogram  \( P(E) \) , the order parameters histograms  \( P(O) \)  (O = M, Q), as well as the logarithmic derivatives of O and  \( O^{2} \)  with respect to  \( K = 1/k_{B}T \) , which can be written in the form

 \[ D_{1O}=\frac{\partial}{\partial K}\ln\langle O\rangle=\frac{\langle O E\rangle}{\langle O\rangle}-\langle E\rangle, \quad (7) \] 

 \[ D_{2O}=\frac{\partial}{\partial K}\ln\langle O^{2}\rangle=\frac{\langle O^{2}E\rangle}{\langle O^{2}\rangle}-\langle E\rangle. \quad (8) \] 

Further, we use the histograms in order to determine FSS behaviour which allows us to extract the critical exponents. In the case of a second-order transition, the extrema of the calculated thermodynamic quantities are known to scale with a lattice size as:

 \[ \chi_{O,max}(L)\propto L^{\gamma_{O}/\nu_{O}}, \quad (9) \] 

 \[ D_{1O,max}(L)\propto L^{1/\nu_{O}}, \quad (10) \] 

 \[ D_{2O,max}(L)\propto L^{1/\nu_{O}}, \quad (11) \]
 

where  \( \nu_{O} \)  and  \( \gamma_{O} \)  represent the correlation length and susceptibility critical exponents, respectively. In the case of a first-order transition (except for the order parameters), they display a volume-dependent scaling,  \( \propto L^{3} \) .

## 3.Phase boundaries and transition order

The temperature dependences of the specific heat and the DLRO parameter in the region where the biquadratic exchange is less or equal to the bilinear one, namely  \( J/J' = 10 \) , 2.5, and 1.0, are shown in Fig.2. Observing the specific heat peaks we can see that with decreasing exchange ratio  \( J/J' \)  the transition temperature T/J is raised. In this region both dipole and quadrupole moments order at the same temperature and, therefore, there is only one phase transition from the disordered paramagnetic phase to the DLRO phase. This state of a single phase transition persists also for lower exchange ratio values down to  \( J/J' \simeq 0.35 \) . Below  \( J/J' \)   \( \simeq 0.35 \)  quadrupoles start ordering separately at temperatures higher than those for dipole ordering. Thus the phase boundary branches and a new middle phase of axial quadrupole long-range order (QLRO) without magnetic dipole ordering opens between the paramagnetic and DLRO phases, and it broadens as  \( J/J' \)  decreases. In Figs.3(a,b,c) we present the temperature variation of the specific heat, the DLRO and QLRO parameters m and q, respectively, and the corresponding susceptibilities  \( \chi_{M} \)  and  \( \chi_{Q} \)  at  \( J/J' = 0.2 \) . We can see that here quadrupoles order before dipoles, forming a fairly broad region of QLRO without DLRO. The snapshots of the spin states in the respective phases appearing as temperature is lowered are depicted in Fig.3d.

Further our concern will be the question of what order these transitions are. As mentioned earlier, a first-order transition is manifested by discontinuous behaviour of the order parameter and energy and, hence, the two quantities should display a bimodal (double-peak) distribution at the transition. On the other hand, if a transition is second order, only a single-peak distribution is observed. One should make sure, however, that the lattice size is sufficiently large and the single-peak behaviour does not result from finite size effects. We calculate the energy and order parameter histograms at the critical temperatures previously estimated by the SMC calculations for various lattice sizes. For  \( 0.5 < J/J' \)  only a singe-peak distribution is found, suggesting a second-order transition, in agreement with continuously looking temperature variation of both the order parameter and energy in this region.
 

the exchange ratio is lowered, the double-peak structure of the energy and order parameter histograms appears. Using the Lee and Kosterlitz method \( ^{14} \)  we can adjust temperature to make the two peaks equally high and, such a way, precisely determine the transition temperature for a given lattice size (Fig.4). Fig.5 shows the energy distribution diagrams for  \( J/J' = 0.35 \) , 0.4 and 0.5, and various lattice sizes with the respective size-dependent transition temperatures  \( T_{c}(L) \) . As can be seen from Figs.5(a,c), i.e. the cases of a comparatively weak first-order transitions near multicritical points, the bimodal distribution can only be observed at sufficiently large L. On the other hand, in the case of  \( J/J' = 0.4 \)  (Fig.5(b)), the dip between the peaks is observable already at smaller L, quite rapidly approaching zero as L is increased, indicating discontinuous behaviour of the energy at a rather strong first-order transition. If a transition is first order,  \( T_{c}(L) \)  should scale with volume as

 \[ |T_{c}-T_{c}(L)|\propto L^{-d}, \quad (12) \] 

where d is the system dimension. In Fig.6 we plot  \( T_{c}(L) \)  vs  \( L^{-3} \) , using the scaling relation (12), and the values of  \( T_{c}(L) \)  extrapolated to  \( L \longrightarrow \infty \)  give us fairly precise estimates of the real transition temperatures for the respective  \( J/J' \) , as follows:  \( T_{c}/J' = 1.2018(1) \)  for  \( J/J' = 0.35 \) ,  \( 1.2918(3) \)  for 0.4, and  \( 1.4851(2) \)  for 0.5. In the region of the separate QLRO and DLRO transitions ( \( 0 < J/J' < 0.35 \) ) we found no double-peak energy distribution for neither kind of transition. However, there are noticeable differences in thermodynamic quantities behaviour between the QLRO and DLRO transition. While in the case of the QLRO transition the energy and QLRO parameter show apparent continuous behaviour even at fairly large lattice sizes, in the case of the DLRO transition, although we could not observe any discontinuities nor hysteresis, the observed slopes are extremely sharp (Fig.3(b)), which is also reflected to the spike-like specific heat and susceptibility peaks (Figs.3(a,c)). This tendency is even more pronounced as the lattice size is increased. Therefore, we cannot exclude possibility of a discontinuous behaviour and, hence, a first-order transition, for  \( L \longrightarrow \infty \) . Another way to decide the order of the transition is by analyzing the temperature dependence of the Binder parameter  \( g_{O}(L, T) \) . In the case of a first-order transition it should display a minimum after entering a paramagnetic phase \( ^{15} \) . In our case, the DLRO parameter seemingly displays such a behaviour, in contrast to the QLRO one (Fig.7), however the transition is not to a disordered paramagnetic but another ordered - the QLRO phase. Moreover, the minima do not scale with volume as is should be at a first-order transition.
 

and, therefore, they should not be seen as a sign of a first-order transition. Unfortunately, unlike for the case of the QLRO transition, which has already been predicted to be of second order for a three-dimensional XY model \( ^{16} \) , there are no previous theories on what order the DLRO transition should be in this region. The resulting phase diagram for the region of  \( 0 \leq J/J' \leq 1 \)  is drawn in Fig.8. For the sake of comparison we also included the HTSE calculations results \( ^{8,9} \) . We can see that in spite of the relatively small lattice sizes used in our calculations the critical temperature values match quite well those obtained from the HTSE calculations. However, the DLRO transition temperature values within  \( 0 \leq J/J' < 1 \)  were not previously calculated and, hence, here, our data present completely new results.

## 4. Finite-size scaling analysis

## 4.1. Critical exponents at DLRO transition

Besides phase boundaries, we also investigated how the biquadratic exchange can modify the critical exponents at a second-order transition. We first perform a finite-size scaling for the DLRO transitions with  \( J/J' = \infty \) , 2.5, 1 and 0.8, and calculate the correlation length and susceptibility critical exponents  \( \nu_{M} \)  and  \( \gamma_{M} \) , respectively, associated with DLRO. We note that the case of  \( J/J' = \infty \) , i.e. when the biquadratic exchange is absent, has previously been calculated by MC simulations \( ^{17} \) , but we included it also in our calculations just for the sake of comparison. The results for  \( J/J' = 0.8 \)  are presented in Fig.9 in ln-ln plot. The slopes yield values of  \( 1/\nu_{M} \)  for the logarithmic derivatives  \( D_{1M} \) ,  \( D_{2M} \)  and  \( \gamma_{M}/\nu_{M} \)  for the susceptibility  \( \chi_{M} \) . Next, we plot the size-dependent transition temperatures  \( T_{c}(L) \) , determined from the peak positions of various quantities, versus  \( L^{-1/\nu_{M}} \) . The value of  \( \nu_{M} \)  is taken as an average of the two values obtained from the logarithmic derivatives. The data then should fit straight lines, which extrapolated to  \( L \longrightarrow \infty \)  should converge to a single point - the real  \( T_{c} \)  (Fig.10). The obtained values of  \( T_{c} \) ,  \( \gamma_{M}/\nu_{M} \)  and  \( 1/\nu_{M} \) , are listed in Table 1, comparing with those previously calculated in Ref. \( ^{17} \)  for  \( J/J' = \infty \)  and by the HTSE method \( ^{8} \) . As seen from the table, the exponents are modified by the presence of the biquadratic exchange in continuous manner, which is in agreement with the HTSE calculations.

## 4.2. Critical exponents at QLRO transition

In the region of the QLRO transition, we examined the critical exponents for transitions at  \( J/J' = 0 \) , 0.1, 0.2 and 0.3. Plots similar to those in Fig.9 are drawn in Fig.11 for the case
 

of  \( J/J' = 0.1 \) , this time in order to obtain the slopes corresponding to the values of  \( 1/\nu_{Q} \)  for the logarithmic derivatives  \( D_{1Q} \) ,  \( D_{2Q} \)  and  \( \gamma_{Q}/\nu_{Q} \)  for the susceptibility  \( \chi_{Q} \) . From the obtained values of  \( \nu_{Q} \)  we plot the size dependence of the transition temperature (Fig.12). Finally, the extrapolated values of  \( T_{q}(L \longrightarrow \infty) \)  are calculated for the respective values of  \( J/J' \) . In Table 2 the resulting values are listed and compared to those from the HTSE calculation \( ^{9} \) . Reasonable agreement between the present results and the HTSE results is achieved in both the critical exponents and transition temperatures cases.

## 4.3. Critical exponents in multicritical point vicinity

At  \( J/J' \simeq 0.35 \)  the frontiers of the paramagnetic, DLRO and QLRO phases merge into a single point. The vicinity of this point presents a crossover region between first- and second-order transitions which should be reflected to the critical exponents' behaviour. In Fig.13 we present the results for  \( J/J' = 0.35 \) . Here, the values of all slopes are significantly enhanced compared to the values for a second-order transition, and for the case of  \( J/J' = 0.38 \)  (Fig.14) quite close to the limiting value 3, which should be reached at a first-order transition. Observing the histograms issued at  \( J/J' = 0.35 \)  (Fig.5(a)) and 0.38, one would conclude, however, that the transitions are of a first order. The fact that the slopes are less than 3 should not be considered as a discrepancy, since the calculated slopes only present the effective values affected by finite size effects. The data in Figs.13 and 14 appear to lie on curves turning upwards, indicating that within the present sizes a true linear regime has not yet been established and still larger sizes would be needed to bring the system into such a regime. The calculated slopes are summarized in Table 3.

## 5.Concluding remarks

We studied effects of the biquadratic exchange on the phase diagram of the classical XY ferromagnet on a simple cubic lattice. We tried to cover all significant critical phenomena induced by the presence of the biquadratic exchange and bring a solid picture of a role of this higher-order exchange interaction in the critical behaviour of the considered system. In the region where the bilinear exchange is dominant we found only one phase transition to the DLRO phase, which remains second order until the exchange ratio reaches the value  \( J/J' \simeq 0.5 \) . Upon further lowering of the ratio, the transition changes to a first-order one at the tricritical point and remains this way down to  \( J/J' \simeq 0.35 \) . Below this value the
 

phase boundary splits into the QLRO transition line at higher temperatures and the DLRO transition line at lower temperatures. While the QLRO transition is clearly of second order, the order of the DLRO transition, due to ambiguous behaviour of the physical observables at the transition, could not be established with certainty, although, a second-order transition seems to be more likeable. We consider performing some more simulations on different lattices of larger sizes and longer simulation time in order to obtain reliable data for the scaling analysis, which should eventually provide a conclusive answer to the question of the order of the DLRO transition in the considered region. Finite-size scaling analysis showed that the critical exponents display a slight variation with changing  \( J/J' \)  but for neither DLRO nor QLRO transitions significantly deviate from the standard three-dimensional XY universality class values.

## Acknowledgments

We wish to thank Dr. A. Tanaka for valuable discussions concerning the theoretical background of the studied problem and Dr. Y. Muraoka for numerous technical consultations when running the simulations on the supercomputer.

 \( ^{1} \)  H.H. Chen and P. Levy, Phys. Rev. Lett. 27, 1383, (1971); Phys. Rev. B 7, 4267, (1973).

 \( ^{2} \)  H.H. Chen and P. Levy, Phys. Rev. B 7, 4284, (1973).

 \( ^{3} \)  R. Micnas, J. Phys. C: Solid St. Phys. 9, 3307, (1976).

 \( ^{4} \)  G.S. Chaddha and A. Sharma, J. Magn. Magn. Mater. 191, 373, (1999).

 \( ^{5} \)  J. Sivardiere, Phys. Rev. B 6, 4284, (1972).

 \( ^{6} \)  J. Sivardiere, A.N. Berker and M. Wortis, Phys. Rev. B 7, 343, (1973).

 \( ^{7} \)  G.S. Chaddha and S.M. Zheng, J. Magn. Magn. Mater. 152, 152, (1996).

 \( ^{8} \)  K.G. Chen, H.H. Chen, C.S. Hsue and F.Y. Wu, Physica 87A, 629, (1977).

 \( ^{9} \)  K.G. Chen, H.H. Chen and C.S. Hsue, Physica 93A, 526, (1978).

 \( ^{10} \)  A. Tanaka and T. Idogaki, J. Phys. Soc. Japan 67, 604, (1998).

 \( ^{11} \)  M. Campbell and L. Chayes, J. Phys. A 32, 8881, (1999).

 \( ^{12} \)  A.M. Ferrenberg and R.H. Swendsen, Phys. Rev. Lett. 61, 2635, (1988).

 \( ^{13} \)  A.M. Ferrenberg and R.H. Swendsen, Phys. Rev. Lett. 63, 1195, (1989).
 

 \( ^{14} \)  J. Lee and J.M. Kosterlitz, Phys. Rev. Lett. 65, 137, (1990).

 \( ^{15} \)  K. Vollmayr, J.D. Reger, M. Scheucher and K. Binder, Z. Phys. B 91, 113, (1993).

 \( ^{16} \)  H.-O. Carmesin, Phys. Lett. A 125, 294, (1987).

 \( ^{17} \)  W. Janke, Phys. Lett. 148, 306, (1990).
 
![](./images/867757841740464174_1.jpg)

FIG. 1: Schematic picture of DLRO and QLRO states.

TABLE I: The values of  \( T_{c} \) ,  \( \nu_{M} \)  and  \( \gamma_{M} \) 

<table><tr><td>J/J&#x27;</td><td>T_{c}/J&#x27;</td><td>\nu_{M}</td><td>\gamma_{M}</td><td>\( \gamma_{M} \)  (HTSE)</td></tr><tr><td>0.8</td><td>2.114(7)</td><td>0.608(11)</td><td>1.18(4)</td><td>-</td></tr><tr><td>1.0</td><td>2.547(7)</td><td>0.630(31)</td><td>1.22(9)</td><td>1.14(2)</td></tr><tr><td>2.5</td><td>5.835(20)</td><td>0.649(9)</td><td>1.30(3)</td><td>1.25(2)</td></tr><tr><td>\( \infty \)</td><td>2.196(8) \( ^{*} \)</td><td>0.669(38)</td><td>1.34(11)</td><td>1.33(2)</td></tr><tr><td>\( \infty \)  Ref. \( ^{17} \)</td><td>2.202  \( ^{*} \)</td><td>0.669(2)</td><td>1.32(1)</td><td></td></tr></table>

* Values of  \( T_{c}/J \)  instead of  \( T_{C}/J' \)
 
![](./images/867757841740464174_2.jpg)

![](./images/867757841740464174_3.jpg)

FIG. 2: Temperature dependence of (a) the specific heat and (b) the order parameter for  \( J/J' = 1.0 \) , 2.5 and 10.
 
![](./images/867757841740464174_4.jpg)

![](./images/867757841740464174_5.jpg)

![](./images/867757841740464174_6.jpg)

FIG. 3: Temperature dependence of (a) the specific heat, (b) the DLRO and QLRO parameters m and q, respectively, and (c) the corresponding susceptibilities  \( \chi_{M} \)  and  \( \chi_{Q} \)  for  \( J/J' = 0.2 \) . Snapshots in Fig.(d) depict spin states in paramagnetic, QLRO and DLRO states at  \( T/J' = 1.4 \) , 0.9 and 0.6, respectively.
 
![](./images/867757841740464174_7.jpg)

FIG. 4: Histogram of the internal energy distribution at the simulation temperature  \( T/J' = 1.2960 \)  and after the peaks heights adjustment by lowering temperature to  \( T/J' = 1.2956 \) .
 
![](./images/867757841740464174_8.jpg)

FIG. 5: Energy distribution at the size-dependent transition temperatures  \( T_{c}(L) \)  for various lattice sizes and (a)  \( J/J' = 0.35 \) , (b) 0.4, and (c) 0.5. Double-peak structures with deepening barrier between the two energy states with increasing lattice size indicate first-order transitions.
 
![](./images/867757841740464174_9.jpg)

![](./images/867757841740464174_10.jpg)

![](./images/867757841740464174_11.jpg)

FIG. 6: Volume dependence of the critical temperature for (a)  \( J/J' = 0.35 \) , (b) 0.4, and (c) 0.5.

![](./images/867757841740464174_12.jpg)

FIG. 7: Temperature variation of the Binder parameters  \( g_{O}(L,T) \)  (O = M, Q) for  \( J/J' = 0.3 \) . The circles, diamonds, squares and triangles represent data for the lattice sizes L = 6, 12, 18 and 24, respectively, while the filled symbols represent  \( g_{M} \)  and the blank ones  \( g_{Q} \)  data.
 
![](./images/867757841740464174_13.jpg)

FIG. 8: Phase diagram in  \( (T/J', J/J') \)  space. The solid and dashed lines denote second- and first-order transitions, respectively. The order of the DLRO transition in  \( 0 < J/J' < 35 \) , denoted by the dash-dot line, could not be determined with certainty. The crosses represent the HTSE results \( ^{8,9} \) 

TABLE II: The values of  \( T_{q} \) ,  \( \nu_{Q} \)  and  \( \gamma_{Q} \) 

<table><tr><td>J/J&#x27;</td><td>Tq/J&#x27;</td><td>{Tq/J&#x27;} (HTSE)</td><td>νQ</td><td>γQ</td><td>γQ (HTSE)</td></tr><tr><td>0</td><td>1.099(4)</td><td>1.100(5)</td><td>0.661(29)</td><td>1.34(7)</td><td>1.32(3)</td></tr><tr><td>0.1</td><td>1.104(4)</td><td>1.110(5)</td><td>0.661(38)</td><td>1.34(10)</td><td>1.32(3)</td></tr><tr><td>0.2</td><td>1.121(4)</td><td>1.125(5)</td><td>0.663(14)</td><td>1.34(6)</td><td>1.30(3)</td></tr><tr><td>0.3</td><td>1.165(3)</td><td>1.165<sup>(5)</sup></td><td>0.649<sup>(42)</sup></td><td>1.32<sup>(12)</sup></td><td><sup>1.26</sup><sup>(3)</sup></td></tr></table>
 
![](./images/867757841740464174_14.jpg)

FIG. 9: Scaling behaviour of the maxima of the susceptibility  \( \chi_{M} \)  and logarithmic derivatives of the DLRO parameter and its second moment  \( D_{1M} \)  and  \( D_{2M} \) , respectively, in ln-ln plot for  \( J/J' = 0.8 \) . The slopes yield values of  \( 1/\nu_{M} \)  for  \( D_{1M} \) ,  \( D_{2M} \)  and  \( \gamma_{M}/\nu_{M} \)  for  \( \chi_{M} \) .
 
![](./images/867757841740464174_15.jpg)

FIG. 10: Finite-size scaling of the critical temperature  \( T_{c}(L) \)  determined by the peaks of  \( \chi_{M} \) ,  \( D_{1M} \) , and  \( D_{2M} \)  for  \( J/J' = 0.8 \) .

TABLE III: The slopes of  \( \chi_{O} \) ,  \( D_{1O} \)  and  \( D_{2O} \) , where O = Q and M for  \( J/J' = 0.35 \)  and 0.38, respectively.

<table><tr><td>J/J&#x27;</td><td>slope of  \( \chi_{O} \)</td><td>slope of D_{1O}</td><td>slope of  \( D_{2O} \)</td></tr><tr><td>0.35</td><td>2.31(10)</td><td>2.16(15)</td><td>2.18(15)</td></tr><tr><td>0.38</td><td>2.79(32)</td><td>2.84(40)</td><td>2.79(36)</td></tr></table>
 
![](./images/867757841740464174_16.jpg)

FIG. 11: Scaling behaviour of the maxima of the susceptibility  \( \chi_{Q} \)  and logarithmic derivatives of the QLRO parameter and its second moment  \( D_{1Q} \)  and  \( D_{2Q} \) , respectively, in ln-ln plot for  \( J/J' = 0.1 \) . The slopes yield values of  \( 1/\nu_{Q} \)  for  \( D_{1Q} \) ,  \( D_{2Q} \)  and  \( \gamma_{Q}/\nu_{Q} \)  for  \( \chi_{Q} \) .

![](./images/867757841740464174_17.jpg)

FIG. 12: Finite-size scaling of the critical temperature  \( T_{q}(L) \)  determined by the peaks of  \( \chi_{Q} \) ,  \( D_{1Q} \) , and  \( D_{2Q} \)  for  \( J/J' = 0.1 \) .
 
![](./images/867757841740464174_18.jpg)

FIG. 13: Scaling behaviour of  \( \chi_{Q} \) ,  \( D_{1Q} \) ,  $ D_{2Q}$  for  \( J/J' = 0.35 \) 

![](./images/867757841740464174_19.jpg)

FIG. 14: Scaling behaviour of  \( \chi_{M} \) ,  \( D_{1M} \) ,  $ D_{2M}$  for  \( J/J' = 0.38 \) . See text for comments.
 
