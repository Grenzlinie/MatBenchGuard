# ORDER, DISORDER, AND PHASE TRANSITIONS IN CONDENSED SYSTEMS

## The Influence of the Icosahedral Percolation Transition in Supercooled Liquid Iron on the Diffusion Mobility of Atoms

A. V. Evteev, A. T. Kosilov, E. V. Levchenko, and O. B. Logachev

Voronezh State Technical University, Moskovskiĭ pr. 14, Voronezh, 394026 Russia

e-mail: evteev@vmail.ru

Received April 8, 2005

**Abstract**—The paper develops concepts of the structure of pure amorphous metals and atomic mechanisms of its formation. It is shown that a stable percolation cluster of interpenetrating and contacting icosahedra whose vertices and centers are occupied by atoms is formed under the conditions of isothermal annealing of instanta- neously supercooled iron melt only below the critical temperature ~1180 K identified with the glass transition temperature. The duration of isothermal annealing up to the formation of the icosahedral percolation cluster does not exceed ~1.5 × 10⁻¹¹ s at 900–1180 K. The time of the beginning of homogeneous nucleation was found to be minimum at the critical temperature above which stable icosahedral percolation cluster did not form. Arguments are provided in favor of the assumption that the formation of icosahedral percolation cluster inter- feres with the beginning of crystallization. A quantitative model is suggested to describe the diffusion mobility of atoms in metallic glasses. In this model, the mean-square displacement of atoms is represented as the sum of the contributions of the linear (Einstein) and logarithmic components. The latter appears because of irrevers- ible structural relaxation. The icosahedral percolation transition was shown to change the activation parameters of the model jumpwise. © 2005 Pleiades Publishing, Inc.

## 1. INTRODUCTION

In recent years, more and more data have been col- lected in favor of the concept first formulated in [1] in terms of the free volume model. According to this con- cept, percolation transitions play a fundamental role in structural self-organization of amorphous materials close to the glass transition temperature $T_g$. A fractal percolation cluster is formed in a disordered system (melt or glass) from local atomic configurations of the same type (Delaunay simplexes with an increased or decreased density of filling the space with atoms [2], icosahedra interpenetrating and contacting with each other [3, 4], and defects in the network of covalent bonds [5]). The formation of a percolation cluster is evidence of system transition into a new structural state (from liquid to vitreous or vice versa, from vitreous to liquid) and, as a consequence, a change in atomic dynamics. Recently, it was shown theoretically on the basis of a thermodynamic description of structural defects [5] that glass transition in amorphous $SiO_2$ could be treated as a percolation transition in the system of network defects presumably consisting of defect SiO molecules, which substantially influence diffusion and viscous flow [6]. The suggested approach can in princi- ple be extended to glass formation in other materials. Its development, however, requires identifying the structural elements of percolation clusters for every type of amorphous materials and studying their thermo- dynamic parameters. In the majority of cases, this is a difficult problem that cannot be solved analytically. For instance, as distinct from the structure of amorphous $SiO_2$, which, by virtue of the special features of local bonds in it, can be treated as a topologically disordered three-dimensional network comprising $SiO_4$ tetrahedra connected by bridge oxygen atoms, the structure of amorphous metals cannot be given such an unambigu- ous description and represents a complex mosaic of a fairly large set of coordination polyhedra of different types [4].

Currently, one of the most effective approaches to studying the principles of the structural organization of disordered systems is computer simulation, which opens up possibilities for analyzing the atomic struc- ture and dynamics and the mechanisms governing the space-time evolution of all system particles [7–11]. This approach inspires certain hopes for constructing a complete theory of metallic glass structure formation from melts and their rearrangement during structural relaxation. For instance, studies of the glass transition of iron melt by molecular dynamics simulation with the Johnson pair interatomic interaction potential [12] at a constant volume [13] and, more recently, at a constant pressure [14] showed that a correlation of local atomic stresses appeared below ~1400–1600 K. This was evi- dence of atomic ordering in the liquid phase followed by glass transition. These spatial correlations of local atomic stresses were accompanied by substantial changes in the dynamic properties of the model. At

1063-7761/05/10103-0521$26.00 © 2005 Pleiades Publishing, Inc.

the same time, no significant structural reorganization was observed; the authors only mentioned an important phenomenon, namely, a transition between bond orientation ordering types in the supercooled liquid phase [13].

A structural model of the glass transition of pure metals was suggested in [3, 4]. According to this model, the atomic structures of metallic melts and glasses are fundamentally different. It was shown in [4] by molecular dynamics simulations with the Pak–Doyama pair interatomic interaction potential [15] that a central role in the structural organization of the amorphous phase of pure iron is played by the formation (at the glass transition temperature, $T_g \sim 1180$ K) and growth of a percolation cluster of interpenetrating and contacting icosahedra whose vertices and centers are occupied by atoms. Interpenetrating icosahedra are those sharing seven atoms, and contacting ones share three (face contact), two (edge contact), or one (vertex contact) atoms. The mechanisms that were shown to govern the self-organization of the icosahedral structure during glass transition well correlated with the temperature dependences of the main thermodynamic characteristics of the model [4]; certain features of these dependences were characteristic of a second-order phase transition [16]. These mechanisms also explained the behavior of thermodynamic characteristics at the microscopic level. The results made it possible to suggest [4] that a fractal cluster that consists of icosahedra incompatible with translational symmetry and comprises more than half of all the atoms plays the role of a binding framework that hinders crystallization. It is the basic element of the structural organization of the solid amorphous state of pure metals that radically distinguishes it from melts. Because of the closeness of the Johnson and Pak–Doyama pair potentials, it is also important that a temperature of 1460 K, below which size fluctuations of small-sized clusters comprising icosahedra interpenetrating and contacting with each other increase sharply [4], is fairly close to the temperature at which local atomic stresses begin to correlate [13, 14].

A more detailed quantitative analysis of structural rearrangements and the influence of the icosahedral percolation transition on the diffusion mobility of atoms and nucleation with subsequent crystallization can be performed by conducting isothermal annealings of an instantaneously supercooled melt close to the glass transition temperature.

In this work, we use the results of a series of computer molecular dynamics experiments to study the influence of the isothermal annealing temperature on the kinetics of the icosahedral percolation transition (which we identify with glass transition) and the beginning of homogeneous nucleation in a supercooled iron melt. We also consider the influence of the icosahedral percolation transition on the activation parameters that determine the diffusion mobility of atoms.

## 2. DESCRIPTION OF THE MODEL

The initial molecular dynamics model of liquid iron was constructed at $T = 2300$ K and had a density of $7800$ kg/m³ (the density was set in conformity with the data on $\alpha$-Fe [17] with about a 1% correction for the amorphous state). The initial structure was a random close packing of atoms. The interaction between the atoms was described using the Pak–Doyama empirical pair potential [15]

$$
\begin{aligned}
\phi(r) &= -0.188917(r - 1.82709)^4 \\
&+ 1.70192(r - 2.50849)^2 - 0.198294\ \text{eV},
\end{aligned} \tag{1}
$$

where $r$ is in angstroms. The potential cutoff radius (the distance at which the potential and its first derivative smoothly vanished) was taken to be $r_c = 3.44$ Å. The potential parameters were determined from the data on the elastic properties of $\alpha$-Fe. The use of this potential for modeling liquid and amorphous iron [18–20] and iron–metalloid alloys [21, 22] provided close agreement between calculation results and experimental structural characteristics. The model contained 100000 atoms in a basic cube with periodic boundary conditions. The velocities of atoms at the initial time were set according to the Maxwell distribution. Molecular dynamics simulations were performed by numerically integrating equations of motion in time steps of $\Delta t = 1.523 \times 10^{-15}$ s using the Verlet algorithm [23]. The system was maintained at a fixed temperature for 3000 time steps (isothermal conditions). The temperature was then allowed to change, and thermal equilibrium at a constant internal energy (adiabatic conditions) was attained during the 3000 time steps.

Next, the system was studied under isochoric conditions over the temperature range 1240–900 K in steps of 20 K. The procedure for modeling involved an instantaneous drop in melt temperature to the required value followed by isothermal annealing until a crystalline nucleus of a critical size began to grow rapidly. The structural characteristics of the system were measured cyclically every $5000\Delta t$, or $0.7615 \times 10^{-11}$ s. Each annealing cycle at the required temperature took a time of $1000\Delta t$ under isothermal and $4000\Delta t$ under adiabatic conditions. The thermodynamic characteristics of the system were averaged over a time period of $2000\Delta t$ at the end of each cycle. Note that the temperature $T$ of the system under adiabatic conditions and the required temperature of measurements (the temperature of the “environment”) did not coincide exactly. After every cycle, the system was driven to the state with $T = 0$ K by the method of static relaxation. The atoms then occupied equilibrium positions in local potential wells, and their mean-square displacements were calculated.

The instant of the formation of a crystalline nucleus of a critical size that began to grow rapidly and of an icosahedral percolation cluster was identified by two methods, namely, using statistical geometric analysis

based on Voronoi polyhedra and cluster analysis based on percolation theory; these methods are described in detail in [3, 4, 24, 25].

## 3. RESULTS AND DISCUSSION

We found that, in the model of an instantaneously supercooled iron melt, the formation and subsequent growth of a percolation cluster built of icosahedra interpenetrating and contacting with each other whose vertices and centers are occupied by atoms occurred only below the critical temperature $T_g$ ~ 1180 K under isothermal conditions (Fig. 1). Note that this temperature coincided with the temperature of the formation of icosahedral percolation cluster during glass transition of iron melt in the molecular dynamics model under the conditions of linear cooling at a rate of $4.4 \times 10^{12}$ K/s [4]. In addition, the glass transition temperature coincided with the temperature at which the time of annealing up to the beginning of homogeneous nucleation was minimum.

This time sharply increases and the number of icosahedra in the system decreases as the temperature grows ($T > T_g$). No stable percolation cluster of interpenetrating and contacting icosahedra does not form then.

The beginning of homogeneous nucleation at temperatures below the glass transition temperature ($T < T_g$) is always preceded by the formation and growth of an icosahedral percolation cluster. Importantly, the duration of annealing before the formation of an icosahedral percolation cluster did not exceed $1.5 \times 10^{-11}$ s in the temperature range studied, 900–1180 K. The formation of an icosahedral percolation cluster was observed either at the first ($t = 0.7615 \times 10^{-11}$ s) or at the second ($t = 1.523 \times 10^{-11}$ s) cycle of measurements counting from the instant of the beginning of isothermal annealing.

The time up to the beginning of homogeneous nucleation, the size to which the icosahedral percolation cluster manages to grow, and the total number of icosahedra in the system increase as the temperature decreases. We found that the fractal icosahedral cluster and the total number of icosahedra continued to grow for some time after the beginning of homogeneous nucleation. This is evidence that the formation of crystalline nuclei and their growth at early stages occur by addition of atoms situated in "pores" of fractal icosahedral cluster rather than by absorption of icosahedra. The presence of a fractal cluster stable toward decomposition limits the mobility of atoms that do not participate in constructing it. This restrains homogeneous nucleation.

In order to determine the character and strength of the influence of icosahedral percolation transition on the diffusion mobility of atoms, we constructed the kinetic curves for the mean-square displacements of atoms close to the $T_g$ temperature. It follows from an analysis of the data obtained in computer experiments and shown in Fig. 2 that the time dependence of the mean-square displacement of atoms at temperatures higher than $T_g$ is linear in conformity with the Einstein equation $\langle \Delta r^2(t) \rangle = 6Dt$, where $D$ is the self-diffusion coefficient. Below $T_g$, this dependence acquires an essentially nonlinear transition character at the initial

![](./images/812134303692488704_1.jpg)

Fig. 1. Isothermal kinetic diagram of the beginning of homogeneous nucleation in the molecular dynamics model of an instantaneously supercooled iron melt (rhombuses). Pentagons correspond to the formation of a stable icosahedral percolation cluster. No stable icosahedral percolation cluster is formed at temperatures above $T_g$ ~ 1180 K (dashed horizontal line).

![](./images/812134303692488704_2.jpg)

Fig. 2. Kinetics of mean-square displacements of atoms in the molecular dynamics models of liquid and amorphous iron (from $\tau = 0.7615 \times 10^{-11}$ s to the beginning of crystallization) at various temperatures (symbols) and approximating curves obtained using the model that takes into account the kinetics of irreversible structural relaxation (solid lines).

annealing stages, which is especially noticeable when the temperature decreases, and gradually becomes steady-state and linear. The appearance of the nonsta- tionary stage in the kinetics of the mean-square dis- placement of atoms at $T<T_{g}$ can only be related to the formation of icosahedral percolation cluster, that is, to the transition of a supercooled melt into the metallic glass state and subsequent structural relaxation.

An analysis of the kinetics of transition processes and related mean-square displacements of atoms at temperatures below the glass transition temperature was performed using the activation energy spectrum model [26] for irreversible structural relaxation [27]. According to [27], structural relaxation can be treated as a sequence of spatially isolated irreversible elemen- tary thermally activated rearrangements in certain structure regions, which are relaxation centers with dis- tributed activation energies. The relaxation centers are physically distinguished structure regions with excess free volume. There are stoppers that restrain local rear- rangements of atomic configurations in adjacent struc- ture regions [27]. Of all the coordination polyhedra that we encounter in closely packed structures (both ordered and disordered), the icosahedron is the most compact and energetically stable. Relaxation centers should therefore be situated outside both fractal and smaller icosahedral clusters, that is, in their pores. Thermally activated stopper removal results in free volume redis- tribution in volume $\Omega$ adjacent to a relaxation center, which increases the mobility of neighboring atoms and thereby activates the second stage of the process. This is the cooperative displacement of atoms in the sur- rounding region, which can be treated as local viscous flow [27]. No matter what the character of the activa- tion energy spectrum, structural relaxation continues up to the beginning of crystallization, which results in the cutoff of the spectrum near the activation energy $E_{c}$ . This energy is some effective parameter of the model that we use.

The kinetic equation for the spectral density (distri- bution function) of relaxation centers $n(E, t)$ has the form

$$
\frac{d n}{d t}=-n v_{0} \exp \left(-\frac{E}{k_{B} T}\right), \quad(2)
$$

where $v_{0}$ is the characteristic frequency on the order of the Debye frequency. Equation (2) is central to the acti- vation energy spectrum model [26]. The integration of this equation under isothermal annealing conditions allows us to track changes in the spectral density of relaxation centers with time. After annealing at temper- ature $T$ for time $\tau$ , the spectral density of relaxation cen ters takes the form

$$
n(E, \tau)=n_{0}(E) \Theta(E, \tau), \quad(3)
$$

where $n_{0}(E)$ is the initial spectral density of relaxation centers and

$$
\Theta(E, \tau)=\exp \left[-v_{0} \tau \exp \left(-\frac{E}{k_{B} T}\right)\right], \quad(4)
$$

is the characteristic function of isothermal annealing. The time of preannealing in our computer experiment was $\tau=0.7615 ×10^{-11} s$ .

If the $n_{0}(E)$ function is fairly flat, that is, if it changes much more slowly than the exponential function $\Theta(E, t)$ varies, annealing development is largely deter mined by the exponential term. During annealing, the $\Theta(E, t)$ curve shifts along the $E$ axis but virtually does not change its shape of a step function, which sharply increases from zero to one near the characteristic energy $E_{0}=k_{B} T \ln (v_{0} t)$ [26] corresponding to the inflec tion point. It follows from the definition of $E_{0}$ that vir tually all the relaxation centers with activation energies $E \leq E_{0}$ come into action by the time $t$ . As a first approx imation, the $\Theta(E, t)$ dependence can be described by the Heavyside step function [28] $\Theta(E-E_{0})$ . Impor tantly, using this approximation does not cause a loss in the accuracy of structural relaxation kinetics calcula- tions. To show this, let us consider the exact solution to the problem.

Time $t$ will be counted from the moment when pre annealing during time $\tau$ ends. The time $t$ dependence of the spectral density of relaxation centers then takes the form

$$
\begin{gathered}
n(E, t)=n(E, \tau) \Theta(E, t) \\
=n_{0}(E) \exp \left[-v_{0}(\tau+t) \exp \left(-\frac{E}{k_{B} T}\right)\right].
\end{gathered}\qquad(5)
$$

According to the superposition principle, the total den- sity of relaxation centers that remain intact by the time t is given by the equation

$$
\begin{gathered}
N_{R C}(t)=\int_{0}^{\infty} n_{0}(E) \\
\times \exp \left[-v_{0}(\tau+t) \exp \left(-\frac{E}{k_{B} T}\right)\right] d E.
\end{gathered}\qquad(6)
$$

It follows that the mean-square displacement of atoms under the conditions of irreversible structural relaxation can be written as

$$
\left\langle\Delta r^{2}(t)\right\rangle=\delta r^{2} \Omega\left(N_{R C}(0)-N_{R C}(t)\right)+6 D t, \quad(7)
$$

where $\delta r^{2}$ is the mean-square displacement of atoms that accompanies the thermally activated removal of one relaxation center.

According to the popular hypothesis about the acti- vation energy spectrum of irreversible structural relax- ation in metallic glasses, this spectrum is generally uni- form and has no significant singularities [27]. We can therefore assume that $n_{0}(E)=n_{0}=$ const to check (7)(Fig. 3). The upper limit of the integral in (6) can con- veniently be replaced by $E_{max} \to \infty$ ; (6) then takes the form

$$
\begin{aligned}
& N_{R C}(t)=n_{0} k_{B} T \int_{(\tau+t) / t_{\max }}^{\mathrm{v}_{0}(\tau+t)} \frac{\exp (-x)}{x} d x \\
& =n_{0} k_{B} T\left[\operatorname{Ei}\left(-\mathrm{v}_{0}(\tau+t)\right)-\operatorname{Ei}\left(-\frac{\tau+t}{t_{\max }}\right)\right],
\end{aligned}
$$

where the notation

$$
t_{\max }=\mathrm{v}_{0}^{-1} \exp \left(E_{\max } / k_{B} T\right)
$$

is used and

$$
-\operatorname{Ei}(-x)=\int_{x}^{\infty} \frac{\exp (-x)}{x} d x
$$

is the integral exponential function [28]. Under the con- ditions of the problem under consideration $(v_{0} \sim 10^{13} s^{-1}$ , and $\tau=0.7615 ×10^{-11} s)$ , we have $-Ei(-v_{0}(\tau+t))<10^{-34}$ . The first term in (8) can therefore be ignored and the second term can be written using the known expansion of the integral exponential function into a series [28],

$$
\begin{gathered}
N_{R C}(t)=-n_{0} k_{B} T \\
×\left[C+\ln \left(\frac{\tau+t}{t_{\max }}\right)+\sum_{i=1}^{\infty} \frac{(-1)^{i}}{i! i}\left(\frac{\tau+t}{t_{\max }}\right)^{i}\right],
\end{gathered}
$$

where $C=0.5772$ is the Euler constant. As $E_{c} \ll E_{max }$ , the argument under the sum sign in (10) can be esti- mated as a value much smaller than one. It follows that, at an arbitrary time moment preceding crystallization, we have

$$
N_{R C}(0)-N_{R C}(t)=n_{0} k_{B} T \ln \left(\frac{t}{\tau}+1\right).
$$

This allows Eq. (7) for the mean-square displacement of atoms to be rewritten as

$$
\left\langle\Delta r^{2}(t)\right\rangle=\delta r^{2} n_{0} \Omega k_{B} T \ln \left(\frac{t}{\tau}+1\right)+6 D t.
$$

In Fig. 2, the time dependences of the mean-square displacement of atoms before the beginning of crystal- lization at several temperatures after preannealing for $\tau=0.7615 ×10^{-11} s$ are shown by symbols and their approximations according to (12), by solid lines. We see that the model is in close agreement with the com- puter experiment results. Similar calculations were per- formed for other temperatures between 1240 and 900 K(the interval studied in this work) and for 1260 K (the instant of the beginning of crystallization at this tem- perature was not determined because of enormous real time expenditures of molecular dynamics computa- tions). Our analysis allowed us to obtain the tempera- ture dependence of the product $\delta r^{2} n_{0} \Omega$ (Fig. 4) and the self-diffusion coefficient $D$ (Fig. 5).

![](./images/812134303692488704_3.jpg)

Fig. 3. Schematic drawing of changes in the spectral density of relaxation centers during isothermal annealing (the plane spectrum approximation).

![](./images/812134303692488704_4.jpg)

Fig. 4. Temperature dependence of the $\delta r^{2} n_{0} \Omega$ product.

![](./images/812134303692488704_5.jpg)

Fig. 5. Temperature dependence of the self-diffusion coefficient.

Changes in the spectral density of relaxation centers as the temperature increases are shown in Fig. 4 within a factor of $\delta r^{2}\Omega$. Since $\delta r^{2}\Omega$ weakly depends on temperature, it follows from Fig. 4 that a sharp decrease in the spectral density of relaxation centers occurs near $T_{g}$ as the temperature increases. This is evidence of the transition of the structure of the model system from the glassy state to a supercooled melt.

Figure 5 shows that the temperature dependence of the self-diffusion coefficient both above and below $T_{g}$ is well described by the Arrhenius equation $D = D_{0}\exp(-E_{s}/k_{\text{B}}T)$. The self-diffusion activation energy $E_{s}$ and the preexponential factor $D_{0}$, however, change jumpwise at $T = T_{g}$ because of the transition of a supercooled melt into the metallic glass state. The activation parameters for the supercooled melt and metallic glass are $E_{s}^{(m)} = 1.05$ eV, $D_{0}^{(m)} = 5.25 \times 10^{-6}$ m²/s and $E_{s}^{(g)} = 1.2$ eV, $D_{0}^{(g)} = 2.05 \times 10^{-5}$ m²/s, respectively.

## 4. CONCLUSIONS

A stable percolation cluster of interpenetrating and coming into contact icosahedra whose vertices and centers are occupied by atoms is formed under isothermal conditions in the molecular dynamics model of an instantaneously cooled iron melt only at a temperature below critical (~1180 K). We identify this temperature with the glass transition temperature. The formation of an icosahedral percolation cluster below this temperature occurs at the initial stages of isothermal annealing, and the expectation time for the process does not exceed $1.5 \times 10^{-11}$ s. The critical temperature above which no stable icosahedral percolation cluster is formed coincides with the temperature at which the time of the beginning of homogeneous nucleation is minimum. The time of the beginning of homogeneous nucleation and the size of the cluster increase as the temperature decreases. This substantiates the suggestion that a fractal cluster comprising icosahedra that are incompatible with translational symmetry and are built of more than half of all the atoms plays the role of a binding framework that restrains crystallization and is the basic element of the structural organization of the solid amorphous state of pure metals that radically distinguishes it from melts.

We obtained an equation that correctly describes the influence of irreversible structural relaxation on the kinetics of the mean-square displacements of atoms in metallic glasses. The icosahedral percolation transition in supercooled liquid iron was shown to cause a sharp change in the activation parameters that determined the diffusion mobility of atoms.

## REFERENCES

1. M. H. Cohen and G. S. Grest, Phys. Rev. B **20**, 1077 (1979).
2. N. N. Medvedev, A. Geiger, and W. Brostow, J. Chem. Phys. **93**, 8337 (1990).
3. A. V. Evteev, A. T. Kosilov, and E. V. Levchenko, Pis'ma Zh. Éksp. Teor. Fiz. **76**, 115 (2002) [JETP Lett. **76**, 104 (2002)].
4. A. V. Evteev, A. T. Kosilov, and E. V. Levchenko, Zh. Éksp. Teor. Fiz. **126**, 600 (2004) [JETP **99**, 522 (2004)].
5. M. I. Ojovan, Pis'ma Zh. Éksp. Teor. Fiz. **79**, 769 (2004) [JETP Lett. **79**, 632 (2004)].
6. R. H. Doremus, J. Appl. Phys. **92**, 7619 (2002).
7. J. M. Ziman, *Models of Disorder: The Theoretical Physics of Homogeneously Disordered Systems* (Cambridge Univ. Press, Cambridge, 1979; Mir, Moscow, 1982).
8. R. Zallen, *The Physics of Amorphous Solids* (Wiley, New York, 1983).
9. V. A. Polukhin and N. A. Vatolin, *Modeling of Amorphous Metals* (Nauka, Moscow, 1985) [in Russian].
10. P. H. Gaskell, in *Materials Science and Technology*, Ed. by J. Zarzycki (VCH, Cambridge, 1991), Vol. 9, p. 175.
11. V. A. Likhachev and V. E. Shudegov, *Organization Principles of Amorphous Structures* (S.-Peterb. Gos. Univ., St. Petersburg, 1999) [in Russian].
12. R. A. Johnson, Phys. Rev. **134**, A1329 (1964).
13. S.-P. Chen, T. Egami, and V. Vitek, Phys. Rev. B **37**, 2440 (1988).
14. L. J. Lewis, Phys. Rev. B **39**, 12954 (1989).
15. H. M. Pak and M. Doyama, J. Fac. Sci., Univ. Tokyo, Ser. B **30**, 111 (1969).
16. L. D. Landau and E. M. Lifshitz, *Course of Theoretical Physics*, Vol. 5: *Statistical Physics*, Part 1, 4th ed. (Nauka, Moscow, 1995; Butterworths, London, 1999).

JOURNAL OF EXPERIMENTAL AND THEORETICAL PHYSICS Vol. 101 No. 3 2005

17. C. J. Smithells, *Metals Reference Book*, 5th ed. (Butterworths, London, 1976; Metallurgiya, Moscow, 1980).

18. R. Yamamoto, H. Matsuoka, and M. Doyama, Phys. Status Solidi A **45**, 305 (1978).

19. D. K. Belashchenko, Fiz. Met. Metalloved. **60**, 1076 (1985).

20. A. V. Evteev and A. T. Kosilov, Rasplavy **1**, 55 (1998).

21. A. V. Evteev and A. T. Kosilov, Rasplavy **4**, 82 (2001).

22. A. V. Evteev, A. T. Kosilov, and E. V. Levtchenko, Acta Mater. **51**, 2665 (2003).

23. L. Verlet, Phys. Rev. **159**, 98 (1967).

24. A. V. Evteev, A. T. Kosilov, and A. V. Milenin, Pis'ma Zh. Éksp. Teor. Fiz. **71**, 294 (2000) [JETP Lett. **71**, 201 (2000)].

25. A. V. Evteev, A. T. Kosilov, and A. V. Milenin, Fiz. Tverd. Tela (St. Petersburg) **43**, 2187 (2001) [Phys. Solid State **43**, 2284 (2001)].

26. W. Primak, Phys. Rev. **100**, 1677 (1955).

27. V. A. Khonik, A. T. Kosilov, V. A. Mikhailov, and V. V. Sviridov, Acta Mater. **46**, 3399 (1998).

28. G. A. Korn and T. M. Korn, *Mathematical Handbook for Scientists and Engineers*, 2nd ed. (McGraw-Hill, New York, 1968; Nauka, Moscow, 1977).

Translated by V. Sipachev

JOURNAL OF EXPERIMENTAL AND THEORETICAL PHYSICS Vol. 101 No. 3 2005