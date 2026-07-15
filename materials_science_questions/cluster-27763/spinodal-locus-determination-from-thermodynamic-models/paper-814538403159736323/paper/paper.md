Spinodals and critical point using short-time dynamics for a simple model of liquid

Ernesto S. Loscar, C. Gastón Ferrara, and Tomás S. Grigera'

Citation: *The Journal of Chemical Physics* **144**, 134501 (2016); doi: 10.1063/1.4944926
View online: http://dx.doi.org/10.1063/1.4944926
View Table of Contents: http://aip.scitation.org/toc/jcp/144/13
Published by the American Institute of Physics

Articles you may be interested in

Critical-point of the Lennard-Jones fluid: A finite-size scaling study
*The Journal of Chemical Physics* **109**, 4885 (1998); 10.1063/1.477099

Critical point and phase behavior of the pure fluid and a Lennard-Jones mixture
*The Journal of Chemical Physics* **109**, 10914 (1998); 10.1063/1.477787

Melting line of the Lennard-Jones system, infinite size, and full potential
*The Journal of Chemical Physics* **127**, 104504 (2007); 10.1063/1.2753149

Phase diagrams of Lennard-Jones fluids
*The Journal of Chemical Physics* **96**, 8639 (1998); 10.1063/1.462271

![](./images/814538403159736323_1.jpg)

# Spinodals and critical point using short-time dynamics for a simple model of liquid

Ernesto S. Loscar, $^{1,2,3}$ C. Gastón Ferrara, $^{1,4}$ and Tomás S. Grigera $^{1,2,3,a)}$

$^{1}$Instituto de Física de Líquidos y Sistemas Biológicos (IFLYSIB), CONICET and Facultad de Ciencias Exactas, Universidad Nacional de La Plata, Calle 59 no. 789, B1900BTE La Plata, Argentina
$^{2}$CCT CONICET La Plata, Consejo Nacional de Investigaciones Científicas y Técnicas, Buenos Aires, Argentina
$^{3}$Departamento de Física, Universidad Nacional de La Plata, c.c. 67, 1900 La Plata, Argentina
$^{4}$Instituto de Ingeniería, Universidad Nacional Arturo Jauretche, Av. Calchaquí no. 6200, B1888BTE Florencio Varela, Argentina

(Received 19 December 2015; accepted 11 March 2016; published online 1 April 2016)

We have applied the short-time dynamics method to the gas-liquid transition to detect the supercooled gas instability (gas spinodal) and the superheated liquid instability (liquid spinodal). Using Monte Carlo simulation, we have obtained the two spinodals for a wide range of pressure in sub-critical and critical conditions and estimated the critical temperature and pressure. Our method is faster than previous approaches and allows studying spinodals without needing equilibration of the system in the metastable region. It is thus free of the extrapolation problems present in other methods, and in principle could be applied to systems such as glass-forming liquids, where equilibration is very difficult even far from the spinodal. We have also done molecular dynamics simulations, where we find the method again able to detect the both spinodals. Our results are compared with different previous results in the literature and show a good agreement. © 2016 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4944926]

## I. INTRODUCTION

In the region near a first-order phase transition, a system can present itself in a metastable phase, i.e., a stable phase which does not correspond to the absolute minimum of the free energy at the given values of pressure, temperature, and field. This phase has a finite lifetime (though it can be extremely long, like in the cases of diamond at room temperature and pressure, or glass-forming supercooled liquids) and can only exist within a finite region of the parameter space around the transition. Sufficiently far from the transition, the phase ceases to be stable: this is the *thermodynamic spinodal*, or simply spinodal, which corresponds to the divergence of some susceptibility, similar to a second-order transition point. Actually, the region where the system can be experimentally prepared in the metastable phase can be smaller than the region defined by the thermodynamic spinodal, because the lifetime of the metastable phase (given by the process of nucleation of the stable phase, which in many cases gets faster further from the transition) can become shorter than the time required for the phase to equilibrate. The border of this smaller region isthe metastability limit, or kinetic spinodal. $^{1–3}$

Hysteresis loops are a physical manifestation of metastability around a first-order phase transition, and, when observable, can provide a rough estimate of the spinodal. For example, Fig. 1 (top) shows a schematic phase diagram of a gas-liquid transition. When the temperature is varied following an isobaric path that crosses the coexistence line at finite speed, the result is a hysteresis loop (bottom panels of Fig. 1). The area of the loop decreases as pressures is increased, disappearing above the critical pressure. The place where the jump to the stable phase occurs depends on the cooling/heating rate but occurs within metastable region. These points are thus bounds of the spinodal and can be considered a first crude estimate.

However, precise determination of the spinodal is more difficult. And, in cases like supercooled liquids, where both the relaxation times of the liquid and the nucleation time of the crystal are very large, the hysteresis loop is not observable. Apart from the theoretical interest in describing the phase diagram as accurately as possible, knowledge of the location of the spinodal would be desired in cases where properties are discussed involving extrapolations intoexperimentally inaccessible (because of timescale issues) regions of metastable phases, such as in the case of the liquid-liquid transition in water, $^{4,5}$ or the Kauzmann transition in supercooled liquids. $^{6}$ In such cases, the thermodynamic spinodal would be a valuable bound for the metastability limit (since the kinetic spinodals must lie within the region bounded by the thermodynamic spinodals).

Here we focus on thermodynamic spinodals, defined as the points where the metastable phase becomes unstable. Thermodynamically, the instability occurs when one of the second derivatives of the free energy changes sign, i.e., when a susceptibility diverges. For the case of fluids, which we consider here, the relevant susceptibility is the compressibility,

$$
\kappa_{T}=-\left.\frac{1}{V} \frac{\partial V}{\partial P}\right|_{T}. \tag{1}
$$

The stability condition is $\kappa_{T}>0$. At the spinodal, $\kappa_{T}$ diverges and changes sign. Experimentally, the susceptibility and

a)URL: http://iflysib14.iflysib.unlp.edu.ar/tomas

![](./images/814538403159736323_2.jpg)

FIG. 1. Top: Schematic phase diagram of the gas-liquid transition for a classical fluid. The continuous line is the coexistence curve of the liquid and gas phases, which ends in the critical point (CP). Dashed lines are the spinodals: the gas spinodal line (liquid spinodal line) is where the gas (liquid) becomes unstable. The horizontal line represents an isobaric process where the system is carried from a high to a low temperature and back to the starting point. Decreasing the temperature from (1) to (3), one crosses the coexistence line, and beyond this point the stable phase is the liquid. However, cooling at a finite rate, the system will stay in the gas phase (now metastable), up to the point (2) at temperature close (but above) the spinodal line, while at lower temperatures the gas is unstable. Increasing the temperature again, the coexistence line is crossed and the system stays in the metastable liquid up to the point (4) close (but below) the liquid spinodal line. Bottom: hysteresis loops at constant pressure. The points are values obtained by Monte Carlo simulation of the $NpT$ ensemble, varying temperature in steps $\Delta T^{*}=0.01$, after letting the system relax for a long period $\tau_{R}$ and starting with a well equilibrated system at (1) (more details in the text).

relaxation times of the metastable phase increase as one goes deeper into the metastable region, and if extrapolated with a power law, they seem to diverge at a point beyond the metastability limit called pseudo-spinodal. $^{7}$ Since the point itself is not reachable because it lies beyond the metastability limit, the true asymptotic behavior of compressibility is difficult to measure experimentally. A classical example is the isothermal compressibility for superheated water at atmospheric pressure. $^{7}$ The power law fit predicts a pseudo spinodal at $T_{sp}=315\ ^{\circ}\text{C}$ and exponent $\sim 1$, but the maximum temperature studied was $T = 220\ ^{\circ}\text{C}$, thus raising concern about the reliability of the extrapolation involved.

Here we show how spinodals in an off-lattice model can be determined using short-time dynamics (STD). STD is a powerful technique to study critical points (CPs), i.e., continuous phase transitions. Following an idea previously developed by some of us, $^{8}$ we use here the same method to identify a critical regime in the metastable region near the gas- liquid coexistence line. The idea is that the spinodal is similar to a critical point of a second-order phase transition, in the sense that both show infinite susceptibility and relaxation time. This should be the sign of the development of an instability, which we identify with the spinodal. As in the original STD technique, our method *does not need equilibrium data*, so that we can perform measurements arbitrarily close to the spinodal. Thus this method is free from the equilibration and extrapolation issues that pervade the determination of pseudo-spinodals.

Several approaches have been proposed to determine spinodals. Methods based on the equation of state $^{9-11}$ have been proposed. $^{12,13}$ Analytic methods (using integral equations and perturbation theory) have been used by Watson *et al.*$^{14}$ and by Chu Nie *et al.*$^{15}$ Using molecular dynamics simulations, Linhart *et al.*$^{16}$ have estimated the gas spinodal by studying the properties of clusters in the $NVT$ ensemble, starting with the particles placed in a fcc lattice. Checking for the existence of a plateau in pressure and the number of particles belonging to the largest cluster in the vapor phase, the spinodal was determined as the point where the plateau disappears. Kraska *et al.*,$^{13}$ using molecular dynamics simulations of the gas-liquid coexistence in equilibrium, have proposed to determine the liquid spinodal from the local extreme values of the tangential pressure along the interface. This method has been applied to several systems, such as Lennard-Jones (LJ) argon, $^{13}$ carbon dioxide, $^{17}$ helium, $^{18}$ and water. $^{19}$ Here we apply the STD method to the liquid-gas transition of a Lennard-Jones fluid. To our knowledge, this is the first application of STD to a simple off-lattice model in 3-$d$. $^{20-22}$

## II. METHOD AND SIMULATIONS

### A. Short time dynamics

The STD technique to identify critical points is based on the work of Janssen *et al.*,$^{23}$ who have shown that universality

and scaling behavior are already present in the early times of the critical relaxation process.

For a system characterized by an order parameter $M$, one studies the relaxation starting from configurations with negligible spatial correlations. These macrostates are prepared with a well controlled condition given by particular values of the order parameter $M_0$. Two initial conditions are used for studying criticality. In the first case, the system is prepared in a macrostate of small $M_0$ at high temperature and quenched to the critical temperature $T_c$. Then its time evolution is (after a microscopic time $t_{mic}$) described by a power law. $^{23}$ This behavior is obtained from the more general scaling form for the $n$-th moment of the order parameter $M^{(n)}(t),^{20,23}$

$$
M^{(n)}(t,c,L,M_0)=b^{-n\beta/\nu}g_n(b^{-z}t,b^{1/\nu}\tau,L/b,b^{\mu}M_0),\quad(2)
$$

where $t$ is time, $\tau$ is the reduced temperature $\tau=(T-T_c)/T_c$, $L$ is the system size, $M_0$ is the initial value of the order parameter (assumed nonzero but small), and $b$ is a rescaling parameter. $\beta$ and $\nu$ are the static critical exponents, while $z$ is the dynamical critical exponent and $\mu$ is a new dynamical exponent related only with the STD. We call this high temperature condition: disordered initial condition (DIC).

In the second case, it is generally assumed in agreement with numerical results, $^{20,22}$ that also an universal behavior of the dynamical relaxation process can be obtained with an ordered ($maximum$) initial macrostate $M_0=1$. It is obtained imposing a very low temperature condition. For this relaxation, a scaling similar to Eq. (2) holds,

$$
M^{(n)}(t,\tau,L)=b^{-n\beta/\nu}g_n(b^{-z}t,b^{1/\nu}\tau,L/b).\quad(3)
$$

We call this condition ordered initial condition (OIC).

In this work, we are interested in the behavior of second the moment $M^{(2)}$, since it is independent on the absolute value of the order parameter. This behavior is obtained from Eqs. (2) and (3) using large values of $L$ (in the case of Eq. (2) small values of $t^{1/z}M_0$), setting $b=t^{1/z}$ and taking the temperature precisely at the critical point ($\tau=0$), to give

$$
M^{(2)}(t)\sim t^{d/z-2\beta/z\nu}.\quad(4)
$$

Then, the critical point can be calculated using any of these two initial macrostates, by performing simulations at several temperatures and tuning $T$ to obtain a power law in time.

We apply the method to the liquid-gas phase transition. Fixing the pressure, we look for singular behavior in the supercooled liquid using the OICs and in the supersaturated gas using the DIC. We associate the appearing singular behavior with OIC (DIC) to the liquid (gas) spinodal temperature. In this way, the critical point can be determined as the intersection of both spinodal lines.

### B. Order parameter

For the liquid-gas transition, the standard order parameter is the difference of density between gas and liquid $\phi=\rho^{liq}-\rho^{gas}$, or simply $\phi=|\rho-\rho_c|$, where $\rho_c$ the critical density. However for spinodal points, the order parameter should be $\phi=|\rho-\rho_{sp}^{\alpha}|$, where $\rho_{sp}^{\alpha}$ is the spinodal density of the phase $\alpha$, which generally is a function of $T$. Letting this order parameter evolve requires an ensemble where the volume is not fixed. The density is analogous to the magnetization in the Ising model, while pressure corresponds to the magnetic field. When applying STD to the Ising model, the evolution of the magnetization is measured fixing the number of spins $N$, the magnetic field $h$, and the temperature $T.^{24}$ This $NhT$ ensemble is analogous to the $NpT$ ensemble for the fluid.

As a measure of the spatial correlation, we take the fluctuations of the overall density,

$$
\rho^{(2)}(t)=\langle[\rho(t)-\langle\rho(t)\rangle]^2\rangle,\quad(5)
$$

where the ensemble average is achieved by doing several runs with different initial configurations. This second moment is identical to the second moment of the order parameter which is independent of $\rho_{sp}^{\alpha}$, therefore we expect the validity of Eq. (4). We now discuss the initial conditions.

### C. DIC

The initial states in STD are given by fixed order parameter and zero correlation. Disordered initial condition is obtained with high temperature and the order parameter taking the critical value. For the archetypal Ising Model, these states are obtained by fixing the magnetic $m_0=0$ and $T_0=\infty$. Physically this state is a completely disordered paramagnet. In the case of the liquid-gas critical point, these conditions mean $\rho_0=\rho_c$ and $T=\infty$. In the case of the spinodals a null order parameter implies $\rho_0=\rho_{sp}^{\alpha}(T)$. Physically these initial states are very hot gases with different densities, and therefore, as we will show below, the technique allow us to determine the gas spinodal line (see Fig. 1). We note, for the gas spinodal line, that the spinodal density varies considerably with the temperature. $^{14,17}$ So, for starting our STD attempts, we need some estimation of this density. As a first step we can estimate these densities from the hysteresis curves in Fig. 1 (for more details see Sec. III).

Also, in order to obtain initial configurations statistically independent controlling exactly the density $\rho$, it must be used the $NVT$-ensemble. In practice, for the case of the Monte Carlo simulation and low density, we obtain this kind of configuration localizing randomly particles in a determined volume, given by a fixed number of particles $N_0$.

### D. OIC

In the case of ordered initial configurations, a high value of the order parameter is necessary, which means a very compressed liquid system. Looking at the complete phase diagram of the LJ system, a very compressed liquid is given for the conditions $\rho_0>\rho_{tr}^{liq}$ and $T_0\gtrsim T_{tr},^{25,26}$ where $\rho_{tr}^{liq}$ and $T_{tr}$ are the liquid density and temperature corresponding to the triple point. To obtain uncorrelated configurations, but still representative of the system, we use the $NVT$ ensemble preparing a well equilibrated sample at $T_0>T_{tr}$, and after obtaining new configurations each a interval of time $\Delta t$. We have tested that our determined values (liquid spinodal temperatures $T_{sp}^{liq}$) are not dependent, within the error bars, on the initial temperature $T_0$. In MC, infinite temperature

configurations (without correlation) can be easily obtained, implying a computational convenience. For this reason, we have used this. However, only in the critical point as it will be discussed below, the initial condition can affect the precise determination of the critical exponents, similarly to the condition of not null magnetization in the Ising model. $^{20,22}$

## E. Model and simulations

We have applied the short-time dynamics technique to a LJ system simulated both with Monte Carlo and Molecular Dynamics. Monte Carlo simulations were done with the truncated, unshifted LJ pair potential,

$$
V(r)=
\begin{cases}
4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right] & \text{if } r \leq r_c, \\
0 & \text{if } r_c > r,
\end{cases}
\tag{6}
$$

with $r_c = 2.5\sigma$. This potential has been used extensively in recent Monte Carlo studies, mainly because the critical values of the transition are known precisely and have been verified with different techniques. $^{27-29}$ It is also very simple to implement and fast to run.

All runs are in the canonical or isobaric ensembles where the number of particles $N$ is fixed (we used $N=1728$), and the number density $\rho=N/V$ can fluctuate in the latter. Monte Carlo simulations were standard Metropolis with local moves (particle shifts and volume changes, limited to a maximum value). These values are chosen in order to obtain an acceptance rate of particle shifts $a_r \sim 0.40$ and volume changes $a_v \sim 0.40$. As usual, the progress in the Monte Carlo simulation is measured in number of attempted moves per particle, a unit called the Monte Carlo step (MCS). In these units, the equilibration period to start the hysteresis loops of Fig. 1 was a $5 \times 10^5$ MCS and $\tau_R = 10^5$ MCS. The results are expressed in reduced units, that is $T^*=k_{\text{B}}T/\epsilon$, $p^*=p\epsilon/\sigma^3$, and $\rho^*=\rho\sigma^3$, where $k_{\text{B}}$ is the Boltzmann constant, while $\epsilon$ and $\sigma$ are the parameters of the LJ pair potential given by the Eq. (6).

For the Molecular Dynamics runs we used the GROMACS 4.6.5 package $^{30}$ in which the equations of motion are solved using a leap-frog integration step. The initial system consisted of a cubic simulation box of $L_x = L_y = 21.2\sigma$, $L_z=21.55\sigma$, with a total volume of $9685.4\sigma^3$ and 1728 Lennard-Jones particles. The systems were weakly coupled to a Berendsens thermal or hydrostatic bath or both, in order to work in the $NVT$ or $NpT$ ensemble. $^{31}$ All simulations were run under periodic boundary conditions and a different number seed was used to assign the initial velocities. Results are also given reduced units, and the time is expressed in units of $t^*=t/\sqrt{m\sigma^2/\epsilon}$.

In the MD runs two cut-off radii ($r_c=2.25\sigma$ and $r_c=5\sigma$) was used, but instead of the simple unshifted truncation the scheme of cut-offs consisted in a twin range cut-offs with neighbor list and long range corrections for energy and pressure. $^{32}$ This difference prevents to compare the two simulation methods directly (see below).

The procedure in both kind of simulations was the same. That is, once the initial configuration is prepared in the $NVT$ ensemble, the system is evolved in the $NpT$ ensemble and the first steps of the evolution of the density are studied. We study the relaxation of the system coming from the both initial macrostates prepared at $(\rho_0,T_0)$ to different final points $(P_{\text{f}},T_{\text{f}})$. These final points are near the zone of coexistence in the phase diagram shown in the $P$-$T$ plane of the Fig. 1.

## III. MONTE CARLO RESULTS

Fig. 2 shows the evolution of the density from the two initial states prescribed by STD for reduced pressure $p_f^*=0.04$. The upper curves are initialized with reduced density $\rho_0^*=0.82$ in the liquid phase, whereas the bottom curves are initialized in the gas phase with $\rho_0^*=0.085$. From this figure we can bound the region where the two spinodals should be searched, is between metastable states of the same phase and stable states of the other phase.

### A. Relaxation from OIC

The relaxation from the high density liquid shows, for the highest final reduced temperature, $T_f^*=1.15$, a jump in density (Fig. 2), indicating a sudden phase change (from liquid to gas). As we shall see, this happens because this temperature is above the liquid spinodal, hence the only stable state is the gas phase (see Fig. 1 for $p^*=0.04$). For the other $T_f^*$ reported, the relaxation is qualitatively different, involving slight decompression but no density jump. In these cases, the final point is in the same (liquid) phase as the initial condition. However, while for some temperatures this is the stable liquid, above the coexistence line ($T^*>T_{coex}^*\sim1.00$ as estimated below) the final state is *metastable*. Thus the liquid spinodal must lie in the range $1.05<T_{sp}^{*liq}<1.15$. We note that with STD, in contrast with the other methods, one can study this relaxation varying the temperature continuously and exploring this range to search the spinodal singularity.

![](./images/814538403159736323_3.jpg)

FIG. 2. Density relaxation from the initial states prescribed by the STD technique ($NpT$ ensemble). The upper curves correspond to the ordered initial condition (compressed liquid) with initial reduced density $\rho_0^*$=0.82 and $T_0^*=\infty$. The bottom curves correspond to the disordered condition (hot gas) with $\rho_0^*$=0.085 (taken from data of Fig. 1) and $T_0^*=\infty$. The final reduced pressure is always $p_f^*$=0.04 and the final reduced temperature $T_f^*$ varies as indicated.

The (pseudo)critical nature of the thermodynamic spinodal will show up in a power law relaxation, best observed in the second moment of the OP given by Eq. (5).

We have done extensive STD simulations from ordered state using as final parameters fixed pressures and exploring the temperature (varying $T_f^*$). Results for each point $(p_f^*,T_f^*)$ are obtained by means of average of $n \approx 2 \times 10^3$ of independent evolutions.

Figure 3 shows the results for the case of initial ordered condition $(\rho_0^* = 0.82$ and $T_0^* = \infty)$. Here we can observe $\rho^{*(2)}(t)$ for $p_f^* = 0.04, 0.10$ and $0.1105$. For each pressure we can detect with good precision a power law behavior. For example for $p_f^* = 0.04$ we find $T_{sp}^{*liq} = 1.105 \pm 0.005$, a value compatible with the previous analysis of Fig. 2. The power law regime lasts until $t_{max} \sim 4 \times 10^3$ MCS (for $p_f^* = 0.04$), and $t_{max} \sim 2 \times 10^4$ MCS (for $p_f^* = 0.1105$).

Also the resolution is very good, note for $p_f^* = 0.1105$ that the evolutions for relative temperature difference of $\Delta T/T = 2 \times 10^{-3}$ can be resolved. We have determined, for each pressure, the liquid spinodal temperature $T_{sp}^{*liq}$. With these data we estimate the liquid spinodal line as shown in Fig. 5.

### B. Relaxation from DIC

This initial state is a gas with low density and infinite temperature. In Fig. 2 we see that for $T_f^* = 1.15$ the relaxation is to the stable gas phase, the same final state reached from the ordered initial state (also, see Fig. 1 for $p^* = 0.04$). For somewhat lower temperatures $(T_f^* = 0.95, 1.05)$ the relaxation is still to a gas, but for $T_f^* = 0.95$ the stable phase is the liquid (note that, for this temperature, coming from the liquid the system remains in the liquid phase) and therefore the relaxation is to a metastable state, which is below the coexistence line. Nevertheless, this relaxation is expected to be similar to the previous one because the final phase is the same.

In contrast, for $T_f^* = 0.80$ the only stable state is the liquid branch (see Fig. 1 for $p^* = 0.04$), with a very different density. So, the relaxation will be qualitatively different because there is a change of phase. In this point of diagram of Fig. 1, $T_f^*$ is below of the gas spinodal line. Therefore, we expect the gas spinodal temperature is in the interval $0.80 < T_{sp}^{*gas} < 0.95$. Again, at the gas spinodal point, STD is applied varying the temperature continuously and exploring this range to detect this singularity.

We have detected this spinodal instability using the STD technique (starting from the disordered state) and done extensive simulations organized by using a fixed pressure $(p_f^*)$.

We can use for starting our STD simulations as initial densities an estimation taken from the hysteresis loop. This is possible for $p^* \leqslant 0.10$ because the hysteresis loops have a well defined jump. For example, our initial density for $p^* = 0.04$ is estimated with the point marked by an arrow in the middle panel of Fig. 1. In the hysteresis loops, when the system goes deep in the metastable branch, the hysteresis curve depends on the rate of change and on the system size. For these reason, we can obtain only a gross estimation for the spinodal density. With this estimate for the initial density and fixing the pressure, we find a power law regime and determine a first estimate for $T_{sp}^{*gas}$. Additionally we have explored other initial densities, repeating the search with densities very close to the original. In some cases, the power law regime disappears. For low pressures $(p^* \leqslant 0.10)$, the estimate of the gas spinodal temperature $(T_{sp}^{*gas})$ has a little dependence on the initial density. Then, we select (among the initial densities) the spinodal temperature, as that which has the best (longer) power law. Once two spinodal points are determined, intermediate points are initialized with the density given by interpolation and the procedure is repeated.

The top of Fig. 4 shows the evolution of the second moment of the density, given by the Eq. (5) for $p_f^* = 0.04$, and starting with the initial density $\rho_0^* = 0.085$ for different final temperatures $(T_f^*)$. We obtain $T_{sp}^{*gas} = 0.85 \pm 0.02$, a value compatible with the previous analysis of Fig. 2. The power law regime starts at $t_{mic} \sim 1$ MCS and lasts until $t_{max} \sim 100$ MCS. This short period of validity of the power law reduces significantly the precision of the method to approximately $2\%$ for this low pressure. Increasing the pressure, $t_{mic}$ and $t_{max}$ increase, allowing a better resolution. For example, for $p_f^* = 0.10$ (middle panel of Fig. 4), we have $t_{mic} \sim 4$ MCS and $t_{max} \sim 400$ MCS and we have obtained $T_{sp}^{*gas} = 1.155 \pm 0.003$, that is an error of approximately $0.3\%$. The best resolution is obtained near the critical point.

![](./images/814538403159736323_4.jpg)

FIG. 3. Second moment of the global density obtained from the relaxation of the ordered initial states for three pressures $p_f^* = 0.040, 0.100, 0.1105$. The final temperatures $(T_f^*)$ are indicated. The initial density is $\rho_0^* = 0.82$.

![](./images/814538403159736323_5.jpg)

FIG. 4. Second moment of the global density obtained from the relaxation of the disordered initial states for three reduced pressures $p_f^*$ = 0.040, 0.100, 0.112. The final temperatures $(T_f^*)$ are indicated. The reduced initial densities are $\rho_0^*$=0.085, 0.19, and 0.22, respectively.

For high pressures $(p_f^* > 0.10)$, we have not detected a significant dependence on the initial densities. In this range $(0.9 \lesssim \frac{p_f^*}{p_c^*} \lesssim 1)$, our results are obtained with the same density $\rho_0^* = 0.24$, this is enough to obtain the gas spinodals near the critical zone.

![](./images/814538403159736323_6.jpg)

FIG. 5. Estimation of the spinodal lines by means of STD. Filled black squares are from DIC and empty blue squares from OIC. The inset is a zoom of the critical region. The critical point is estimated by the intersection of the two quadratic fits (continuous lines) giving $p_c^*$=0.1105 and $T_c^*$=1.1875.

In this way, we have determined, for each pressure, the critical temperature $T_{sp}^{*gas}$. With these data, we estimate the gas spinodal line showed in Fig. 5.

The bottom panel of Fig. 4 shows the result for $p_f^* = 0.1105$. We can find a power law regime for $T_{sp}^{*gas}$ = 1.1875 $\pm$ 0.0015. We note that the horizontal axis scales for the gas relaxation are shorter than for the liquid relaxation. This difference shows that the characteristic times involved in dynamical processes (relaxation times, microscopic time, $t_{max}$, etc.) are faster in the gas phase than in the liquid phase. This fact implies, considering that these times can be similar or smaller than the experimental times of observation, additional difficulties and imprecisions in the determination of the gas spinodals.

### 1. Phase diagram and critical point

Fig. 5 collects the points obtained with both initial conditions (the gas spinodals from DIC and the liquid spinodal from OIC). The two curves seem to have the same slope as the coexistence line, forming a cusp in the intersection point which is the (equilibrium) critical point where the phase coexistence line ends. This is similar to what is found from the exact solution for the magnetic spinodal field in the fully connected Ising model. $^{8,33}$ The inset of Fig. 5 is a zoom of the critical zone. Our estimate for the critical point is $p_c^* = 0.1105(15)$ and $T_c^* = 1.1875(15)$, in very good agreement with previous results obtained by MC simulation with finite size scaling (FSS)$^{28}$ ($T_c^* = 1.1876(3)$, $p_c^* = 0.1093(6)$), MC with mixed-field FSS$^{29}$ ($T_c^* = 1.186(2)$; $p_c^* = 0.109(2)$), and MD with mixed-field FSS$^{27}$ ($T_c^* = 1.1879(4)$).

Once the critical point is found, we can estimate the STD exponents. The critical behavior for the second moment is expected to be described by Eq. (4). We extract the exponent $\psi = d/z - 2\beta/z\nu$ for the DIC by fitting a power law in Fig. 4, which gives $\psi = 0.85 \pm 0.05$ (approximately independent of the initial density). Using the $3d$ exponents for the Ising model$^{34}$, we have $\frac{2\beta}{\nu} = 0.517 \pm 0.002$ and so we can estimate the dynamic exponent as $z = 2.9 \pm 0.2$.

In the case of the evolution from ordered state, we have found that the critical temperature $T_c^*$ determined by STD is in practice independent of the different conditions such as initial temperature or density, density, or MC simulation acceptance-rate. We can estimate $\psi$ for the OIC fitting a power law in Fig. 3 and we obtain $\psi = 0.62$. However the estimation of the exponent $\psi$ varies appreciably with different conditions. We note two main sources affecting the value of the exponent. First, the initial temperature was chosen infinity for simplicity, but actually this affect the estimation of the exponent and using $T^* = T_c^*$ or $T^* = 0.8T_c^*$, we obtain estimates of $\psi \sim 0.7$. Second, the microscopic time $t_{mic}$ varies with different acceptance rates (all data until here have been obtained with acceptance rate $a_r \sim 0.40$). This affects the estimation of $\psi$ using OIC. It is due to the fact that we have worked with finite sizes, so the interval of the validity of the power law can change. Fig. 6 shows the second moment $\rho^{*(2)}$ obtained from OIC with the initial samples prepared at $T^* = 0.8T_C^*$ and setting the acceptance rate $a_r \sim 0.20$. We obtain from this figure our best estimate for the exponent,

![](./images/814538403159736323_7.jpg)

FIG. 6. Second moment of the density starting from a compressed liquid at $T^{*}=0.8T_{c}^{*}$ and with final parameters in the critical region (that is $p^{*}=p_{c}^{*}$ $=0.1105$ and $T^{*}=T_{c}^{*}=1.1875$). The power law fit is the best estimation using OIC for the exponent $\psi \sim 0.75$.

$\psi \sim 0.75 \pm 0.05$. It should be remarked that the initial state for the STD technique starting with the ordered phase should be $T^{*}=0$, but this condition is impossible for the LJ-system because the solid phase appears for $T^{*}<T_{tr}^{*}\sim 0.8$. From this estimated value of $\psi$ we can calculate the dynamic exponent $z=3.3\pm 0.3$.

In summary, our results for the exponent $z$ from the two different initial conditions are compatible, but with significant error bars. We report for it $z=3.0\pm 0.3$.

### 2. Comparisons
The locus of the critical point of the LJ fluid depends on the way the long-range cutoff is introduced. $^{27,35}$ For this reason, in order to compare our results with published data (following Ref. 36), we use the concept of corresponding states and adopt the reduced variables $\frac{p^{*}}{p_{c}^{*}}$, $\frac{T^{*}}{T_{c}^{*}}$ and $\frac{\rho^{*}}{\rho_{c}^{*}}$.

The gas-liquid coexistence line for the Lennard-Jones fluid is given by the vapor pressure formula of Lotfi $et$ $al.^{37}$ Rewriting this in the form of corresponding states, we have
$$
\begin{aligned}
\frac{p^{*}}{p_{c}^{*}}= & \exp \left[-1.6544\left(1-\epsilon^{-1}\right)+3.6714(1-\epsilon)\right. \\
& \left.+0.051\ 324\left(1-\epsilon^{4}\right)\right],
\end{aligned} \tag{7}
$$
where $\epsilon=\frac{T^{*}}{T_{c}^{*}}$. This curve is plotted in Fig. 7 as a dashed line. This line can be used to obtain an estimation of the locus of the first order transition in our model (for example, for $p_{0}^{*}=0.04$, we obtain $T_{coex}^{*}\approx 1.00$). The same figure shows both spinodals points (empty black triangles) obtained by Watson $et$ $al.^{14}$ with the temperature perturbation method. $^{38}$ We have used for this $T_{c}^{*}=1.313$ and $p_{c}^{*}=0.128.^{29}$ These points have been obtained using Monte Carlo simulation data in a system size of $N=216$ particles for 16 different temperatures. Except for the region near the critical point (where disagreement is expected due to the small system size used in Ref. 38), our results are in good agreement. Both methods seems to be consistent, especially for the case of the liquid spinodal.

The continuous lines in Fig. 7 are obtained from the equation of state for LJ-potential of Johnson $et$ $al.,^{10}$ while the open black diamonds are from Ref. 15, using integral equations. Brown filled triangles are from Ref. 16, obtained by means of proper definition of clusters.

![](./images/814538403159736323_8.jpg)

FIG. 7. Corresponding states comparison of STD results (filled black and empty blue squares) with other estimations in the literature. The continuous lines are obtained from the equation of state for the LJ-potential of Johnson, $^{10}$ empty black triangles are from Ref. 14, open black diamonds from Ref. 15, and the brown filled triangles are from Ref. 16. The empty and the filled black circles are STD results using MD with cutoff radius $r_{c}=2.25\sigma$ and $r_{c}=5\sigma$, respectively. Black dashed line is the gas-liquid coexistence given by the formula of Lotfi $et$ $al.^{37}$

The case of the liquid spinodal line is remarkable because all the results are consistent, including MD (see below). In the case of the determination of the gas spinodals, as we have noted above, there are more imprecisions which are reflected for the dispersion of the results using different techniques. However the results are qualitatively similar and quantitatively they are all in close proximity.

### IV. MOLECULAR DYNAMICS RESULTS
A very large number of computational studies of liquids use Molecular Dynamics rather than Monte Carlo, in part because MD uses a realistic dynamics (Newton's laws) for the time evolution. It is thus interesting to explore whether STD can be used with MD trajectories. We have tested the method using the two initial states and fixing the pressure.

We have applied the protocol described in Sec. II. First we have done hysteresis loops for $p^{*}=0.083$. Figure 8 shows the results for this pressure varying the temperature between $T_{min}^{*}=0.77$ and $T_{max}^{*}=3.20$. With these data, we have estimated the spinodals using the criteria of the intersection of the straight line with maximal slope (fitted in the jump between different phases) with a base curve (a second-degree polynomial fitted in one phase near the transition) as shown in Fig. 8. From this estimation, we obtain the density $\rho_{sp}^{*gas}\sim 0.122$. In contrast with MC, in this case, we cannot generate initial configurations at $T=\infty$. Instead we use well equilibrated samples (with runs lasting $t_{eq}^{*}=6\times 10^{4}$) prepared at high temperature $T^{*}=3.20$ and $\rho_{sp}^{*gas}\sim 0.122$ with the $NVT$ simulations.

After that, in order to obtain non-correlated samples, configurations were recorded at $\Delta t^{*}=5$ intervals and resetting the velocities at $T^{*}=3.20$. The results for the (global) second

![](./images/814538403159736323_9.jpg)

FIG. 8. Hysteresis loop at constant pressure $p^{*}=0.083$ with MD in the $NpT$-ensemble. The arrows indicate the locus of the spinodals obtained by intersecting the extrapolations (red dashed lines). More details in the text.

moment of the density are shown in Fig. 9(a). We observe a power law lasting three decades for $T^{*}=1.11$, which is interpreted as the gas-spinodal temperature. For ordered initial conditions, we have used compressed configurations at $\rho^{*} \sim 0.85$ and $T^{*}=1.30$. Fig. 9(b) shows the evolution of $\rho^{*(2)}$. From this initial state, we detect a power law lasting more that two and a half-decades at $T^{*}=1.33$. This is our estimation of the liquid spinodal temperature for $p^{*}=0.083$. This is in very good agreement with the value obtained with the intersection lines criteria indicated with an arrow in the Fig. 8.

These two spinodals have been including in Fig. 7 using the critical values $p_{c}^{*}=0.128$ and $T_{c}^{*}=1.312$, obtained from the literature for the LJ potential without cutoff. $^{39}$ These points show some disagreement because of the different cutoff value and procedure used in MD. This noticeably modifies the value of $T_{c}^{*}$ and $P_{c}^{*}$ and we have no better estimation for them.

![](./images/814538403159736323_10.jpg)

FIG. 9. Results of STD for pressure $p^{*}=0.083$ and final temperatures $T_{f}^{*}$ as indicated. (a) Results for the relaxation from disordered initial conditions (hot gas). The gas spinodal resulting is $T_{sp}^{*gas}=1.11(3)$. (b) Results for the relaxation from ordered initial conditions (compressed liquid). The liquid spinodal resulting is $T_{sp}^{*liq}=1.33(1)$.

![](./images/814538403159736323_11.jpg)

FIG. 10. Results of STD using $r_{c}=5\sigma$ (a) starting with disordered initial conditions for pressure $p^{*}=0.083$ and final temperatures $T_{f}^{*}$ as indicated. The gas spinodal resulting is $T_{sp}^{*gas}=1.16(1)$. (b) Starting with ordered initial conditions for pressure $p^{*}=0.083$ and final temperatures $T_{f}^{*}$ as indicated. The resulting value for the liquid spinodal is $T_{sp}^{*liq}=1.25(1)$.

We have repeated these simulations using $r_{c}=5\sigma$, a value of $r_{c}$ for which the critical temperature and pressure should be closer to $T_{c}^{*}=1.312$ and $p_{c}^{*}=0.128$. Fig. 10 shows results for the same pressure $p^{*}=0.083$, but with the new $r_{c}$, for both initial conditions. Both results are also included in Fig. 7 (adding also the result for $p^{*}=0.059$ with OIC). We can see a much better agreement with the results of STD with MC, and also with those from the equation of state, $^{10}$ confirming that for this new range we can use the critical values corresponding to the full potential.

## V. CONCLUSIONS

We have shown how short-time dynamics can be applied to determine the location of the thermodynamic spinodals in off-lattice models of fluids, thus extending the ideas presented in Ref. 8. Both molecular dynamics and Monte Carlo can be used for this purpose.

Our results are compatible with those obtained by other methods, but STD is able to give good estimates also near the critical point. In this region, STD presents significant advantage, because it is not necessary to reach equilibrium.

We remark that in the case of liquid-gas transitions, the order parameter $(|\rho - \rho_{sp}^{\alpha}|)$ is unknown $a$ $priori$. For the disordered initial conditions, in order to apply the method to obtain the gas spinodal, some rough estimation is needed, which we have obtained here through the hysteresis loops. This is an important disadvantage if the hysteresis loop is not observable in system under study. However, this situation seems to be a special case. For example, for the Potts Model

(see Ref. 8), we know *a priori* that the order parameter is zero for any supercooled condition. So, the central question is the election of a convenient order parameter whose value results to be null even in the supercooled state. These kinds of parameter exist but may not be obvious, as in the case of the solid-liquid transition where the orientational order parameter $Q_6$ is null for the liquid phase (including the supercooled liquid). So the applicability of STD method for detecting spinodal points rests in our ability to find such kind of order parameter. This difficulty surmounted, STD is a powerful method, and can potentially overcome the problems present in cases where equilibration is difficult or impossible, such as in deeply supercooled glass forming liquids near the Kauzmann transition, $^6$ or near the proposed liquid-liquid transition of water. $^{4,5}$ We hope to apply this technique to these kinds of systems in the near future.

## ACKNOWLEDGMENTS

This work was supported by CONICET, Universidad Nacional de La Plata, Universidad Nacional Arturo Jauretche, ANPCyT Grant No. PICT 0206/12 (Argentina).

$^1$A. Z. Patashinskii and B. I. Shumilo, Sov. Phys. JETP **50**, 712 (1979).
$^2$A. Z. Patashinskii and B. I. Shumilo, Sov. Phys. Solid State **22**, 655 (1980).
$^3$A. Cavagna, I. Giardina, and T. S. Grigera, *J. Chem. Phys.* **118**, 6974 (2003).
$^4$H. Poole, F. Sciortino, U. Essmann, and H. E. Stanley, *Nature* **360**, 324 (1992).
$^5$D. T. Limmer and D. Chandler, *J. Chem. Phys.* **135**, 134503 (2011).
$^6$W. Kauzmann, *Chem. Rev.* **43**, 219 (1948).
$^7$P. G. Debenedetti, *Metastable Liquids: Concepts and Principles* (Princeton University Press, Princeton, 1996).
$^8$E. S. Loscar, E. E. Ferrero, T. S. Grigera, and S. A. Cannas, *J. Chem. Phys.* **131**, 024120 (2009).
$^9$R. B. Steward and R. T. Jacobsen, *J. Phys. Chem. Ref. Data* **18**, 639 (1989).
$^{10}$J. K. Johnson, J. A. Zollweg, and K. Gubbins, *Mol. Phys.* **78**, 591 (1993).
$^{11}$J. Kolafa and I. Nezbeda, *Fluid Phase Equilib.* **100**, 1 (1994).
$^{12}$D. S. Corti and P. G. Debenedetti, *Chem. Eng. Sci.* **49**, 2717 (1994).
$^{13}$A. R. Imre, G. Mayer, G. Hazi, R. Rozas, and T. Kraskaj, *J. Chem. Phys.* **128**, 114708 (2008).
$^{14}$B. S. Watson, R. A. Greenkorn, and K. C. Chao, *Ind. Eng. Chem. Res.* **35**, 4336 (1996).
$^{15}$C. Nie, J. Geng, and W. H. Marlow, *J. Chem. Phys.* **128**, 054305 (2008).
$^{16}$A. Linhart, C. C. Chen, J. Vrabec, and H. Hasse, *J. Chem. Phys.* **122**, 144506 (2005).
$^{17}$T. Kraska, F. Röemer, and A. R. Imre, *J. Phys. Chem. B* **113**, 4688 (2009).
$^{18}$A. R. Imre, A. Baranyai, U. K. Deiters, P. T. Kiss, T. Kraska, and S. E. Quiñones Cisneros, *Int. J. Thermophys.* **34**, 2053 (2013).
$^{19}$A. R. Imre and T. Kraska, *Phys. B: Condens. Matter* **403**, 3663 (2008).
$^{20}$B. Zheng, *Int. J. Mod. Phys. B* **12**, 1419 (1989).
$^{21}$B. Zheng, in *Computer Simulation Studies in Condensed-Matter Physics*, edited by D. P. Landau, S. P. Lewis, and H.-B. Schüttler (Springer, New York, 2006).
$^{22}$E. V. Albano, M. A. Bab, G. Baglietto, R. A. Borzi, T. S. Grigera, E. S. Loscar, D. E. Rodriguez, M. L. Rubio Puzzo, and G. P. Saracco, *Rep. Prog. Phys.* **74**, 026501 (2011).
$^{23}$H. K. Janssen, B. Schaub, and Schmittmann, *Z. Phys. B* **73**, 539 (1989).
$^{24}$Z. B. Li, L. Schücle, and B. Zheng, *Phys. Rev. Lett.* **74**, 3396 (1995).
$^{25}$J. P. Hansen and L. Verlet, *Phys. Rev.* **184**, 151 (1969).
$^{26}$E. A. Mastny and J. J. de Pablo, *J. Chem. Phys.* **127**, 104504 (2007).
$^{27}$W. Shi and J. K. Johnson, *Fluid Phase Equilib.* **187**, 171 (2001).
$^{28}$N. B. Wilding, *Phys. Rev. E* **52**, 602 (1995).
$^{29}$J. J. Potoff and A. Z. Panagiotopoulos, *J. Chem. Phys.* **109**, 10914 (1998).
$^{30}$D. Van Der Spoel, E. Lindahl, B. Hess, G. Groenhof, A. E. Mark, and H. J. C. Berendsen, *J. Comput. Chem.* **26**, 1701 (2005).
$^{31}$H. J. C. Berendsen, J. P. M. Postma, A. DiNola, and J. R. Haak, *J. Phys. Chem.* **81**, 3684 (1984).
$^{32}$GROMACS User Manual, Version 4.6.5, 2013, page 195, www.gromacs.org.
$^{33}$T. Mori, S. Miyashita, and P. A. Rikvold, *Phys. Rev. E* **81**, 011135 (2010).
$^{34}$A. Jaster, J. Mainville, L. Schülke, and B. Zheng, *J. Phys. A: Math. Gen.* **32**, 1395 (1999).
$^{35}$B. Smit, *J. Chem. Phys.* **96**, 8639 (1992).
$^{36}$B. N. Hale and M. Thomason, *Phys. Rev. Lett.* **105**, 046101 (2010).
$^{37}$A. Lotfi, J. Vrabec, and J. Fischer, *Mol. Phys.* **76**, 1319 (1992).
$^{38}$B. S. Watson and K. C. Chao, *J. Chem. Phys.* **96**, 9046 (1992).
$^{39}$J. Pérez-Pelliteroa, P. Ungerer, G. Orkoulas, and A. D. Mackie, *J. Chem. Phys.* **125**, 054515 (2006).