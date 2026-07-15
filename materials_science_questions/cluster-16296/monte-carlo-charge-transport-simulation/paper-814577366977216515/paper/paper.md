OPEN
# Effective Temperature and Universal Conductivity Scaling in Organic Semiconductors

Hassan Abdalla¹, Kevin van de Ruit² & Martijn Kemerink¹,²

Received: 01 July 2015
Accepted: 13 October 2015
Published: 19 November 2015

We investigate the scalability of the temperature- and electric field-dependence of the conductivity of disordered organic semiconductors to 'universal' curves by two different but commonly employed methods; by so-called universal scaling and by using the effective temperature concept. Experimentally both scaling methods were found to be equally applicable to the out-of-plane charge transport in PEDOT:PSS thin films of various compositions. Both methods are shown to be equivalent in terms of functional dependence and to have identical limiting behavior. The experimentally observed scaling behavior can be reproduced by a numerical nearest-neighbor hopping model, accounting for the Coulomb interaction, the high charge carrier concentration and the energetic disorder. The underlying physics can be captured in a simple empirical model, describing the effective temperature of the charge carrier distribution as the outcome of a heat balance between Joule heating and (effective) temperature-dependent energy loss to the lattice.

Since the discovery of conductive polymers, tremendous progress has been made in rationalizing their electrical properties. At low charge carrier concentrations, typically stretched exponential behavior of the current $j$ on temperature $T$, $j \propto \exp\left(-\left(T_0/T\right)^\nu\right)$, is found and rationalized in terms of hopping in a disorder-broadened density of states (DOS), with the system dimensionality and DOS shape determining the stretching exponent $\nu^{1,2}$. The Ohmic conductivity of some conducting polymer systems with higher conductivity tends to show a power law temperature dependence, $\sigma \propto T^\alpha$, typically considered to be a consequence of the increasingly metallic properties of the system, causing an insulator-to-metal transition³⁻⁵.

For higher carrier concentrations and associated higher conductivities the situation is not so clear. Many recent studies on organic electronic systems, which do not only measure the Ohmic conductivity but also the non-Ohmic conductivity obtained at increased electric fields, reveal a curious pattern⁶⁻¹². They show that the Ohmic conductivity has a power law temperature dependence, but most importantly, that rescaling the current and voltage using the power law dependence on temperature collapses the data on a universal curve of $j/T^{1+\alpha}$ vs. $V/T$ that can be captured by

$$
j = bT^{1+\alpha} \sinh\left(\gamma \frac{eV}{k_B T}\right) \left| \Gamma\left( \frac{1+\beta}{2} + \frac{i}{\pi}\gamma \frac{eV}{k_B T} \right) \right|^2 \tag{1}
$$

with $e$ the elementary charge, $k_B$ the Boltzmann constant, $b$ a scaling parameter, $\gamma$ a parameter such that the crossover between the Ohmic and non-Ohmic regime takes place at $eV/k_B T \approx 2/\gamma$, and $\Gamma$ the complex Gamma function. (NB: the exponent in Eq. (1) is missing in ref. 6) The parameters $\alpha$ and $\beta$ reflect the power law temperature and field dependence in the ohmic and non-ohmic regimes, respectively, and are often related as $\beta = \alpha + 1$. The scaled curve consists of a crossover between an Ohmic voltage

¹Complex Materials and Devices, Department of Physics, Chemistry and Biology, Linköping University, 58183 Linköping, Sweden. ²Eindhoven University of Technology, Department of Applied Physics, P.O. Box 513, NL-5600 MB Eindhoven, the Netherlands. Correspondence and requests for materials should be addressed to M.K. (email: martijn.kemerink@liu.se)

dependence, $j \propto V$, and a steeper power law dependence, $j \propto V^3$. The property of obeying this scaling behavior is commonly referred to as universal scaling (US); accordingly in this work we shall refer to US as the property that the scaled $j(V,T)$ curves exhibit these limiting power law behaviors, not necessarily obeying the exact form Eq. (1).

There are at least five different theoretical frameworks that either exactly explain the functional shape (1), or give rise to functionally similar behavior. In most experimental investigations observations of US behavior are explained as stemming from Luttinger liquid behavior, which is related to interacting electrons confined to one dimension¹³. Because of the strong similarity in the resulting charge transport behavior, a strong case can also be made for a description based on a chain of quantum dots with Coulomb blockade behavior⁷,¹⁴,¹⁵. Alternatively, Rodin and Fogler¹⁶ have shown that the power law behavior of conductance might also be well explained in terms of quasi-1D variable range hopping (VRH). Asadi *et al.* showed universal scaling for a wide range of semiconducting polymers and interpreted the results in terms of a model that accounts for the zero-point energy of the charges and that holds for low disorder¹⁷. Finally, Li *et al.* argued that in the high-density regime 3D VRH can give rise to behavior resembling Eq. (1)¹⁸. No consensus exists regarding which of these prevails. Moreover, as these interpretations are based on fundamentally different and mutually exclusive assumptions, it is safe to conclude that the high-density conductivity of disordered organic semiconductors still poses a major question.

A seemingly unrelated concept that applies to amorphous semiconductors at high electric fields is the so-called effective temperature $T_{eff}$. The effective temperature framework was first described some 20 years ago by Marianer and Shklovskii (MS) and confirmed by Baranovskii *et al.*, for inorganic amorphous systems with an exponential density of states (DOS) in the Boltzmann limit¹⁹,²⁰. It has since been shown to be also valid for disordered organic systems with a Gaussian DOS and large charge densities²¹⁻²³. In their original work, MS found that a strong enough electric field has a similar effect on the charge carrier population and transport as an increased lattice temperature. The underlying physical picture is that the carrier can increase its energy by an amount $\Delta E = qFa$ by hopping a distance $a$ along the field $F$. In other words, the carrier becomes "hot". They argue that the temperature in the Miller Abrahams expression for hopping conduction can then be replaced by an effective temperature, which is dependent on the applied field and the lattice temperature. In their numerical variable range hopping study of the effective temperature as a function of lattice temperature and field, they find that the variation of $T_{eff}/T$ with $qFa/k_BT$ for different temperatures collapses to one line with a functional shape following the expression

$$
T_{eff} = \left[ T_{latt}^{\varsigma} + \left( \delta \frac{eFa}{k_B} \right)^{\varsigma} \right]^{\frac{1}{\varsigma}},
\tag{2}
$$

with $\delta=0.67$ and $\varsigma=2$. Marianer and Shklovskii write that they 'unfortunately do not have a satisfactory physical interpretation' of Eq. (2). Even though the concept of an effective temperature is by now theoretically well-established 'as a rough but useful approximation'²³⁻²⁵, the functional shape of Eq. (2) remains unexplained, both for inorganic and organic systems. Remarkably, when the conductivity obtained from these numerical simulations is plotted as a function of $T_{eff}$ another universal curve is obtained, with all data points following a power law in $T_{eff}$, $\sigma \propto T_{eff}^{\alpha}$. Also here no physical explanation is given. Experimentally, the validity of Eq. (2) has subsequently been confirmed by dark conductivity measurements of inorganic a-Si:H²⁶⁻²⁸; for organic semiconductors the concept received no experimental attention.

Despite evident similarities between the US and MS concepts, we are not aware of any attempts to unify both frameworks or to address a possible common physical origin. Here we show that the governing relations of universal scaling and effective temperature lead to fully equivalent functional shapes in temperature- and field-dependence of the conductivity and therefore equally well describe an extensive data set obtained on a practically relevant model system, the highly doped organic semiconductor PEDOT:PSS. Using kinetic Monte Carlo (MC) simulations we show that, in the experimentally relevant limit of large Gaussian disorder and high carrier concentrations, the US and MS scaling phenomena have their physical origin in the heating of the charge carrier distribution. The MC simulations are able to qualitatively reproduce all experimentally observed phenomena and relations. Furthermore, the time-dependent nature of the MC method allows us to investigate the energy relaxation of the charge carriers over time. Based on this knowledge we show how Marianer-Shklovskii-type behavior Eq. (2) and universal scaling can be obtained using a simple heat balance, based on Joule heating in combination with an algebraic energy dependence of the relaxation of charge carriers. The resulting empirical model consistently describes the numerical and experimental results.

### Results
As an experimental basis for our work, we investigated the out-of-plane conductivity of PEDOT:PSS thin films as a function of electric field, temperature, layer thickness and PEDOT:PSS weight ratio. The samples for the out-of-plane conductivity measurements were fabricated as described previously²⁹. A summary is given in the Methods section at the end.

![](./images/814577366977216515_1.jpg)

Figure 1. Universal scaling of the conductivity of PEDOT:PSS. (a) Conductivity vs. applied bias for a 1:2.5 (w/w) PEDOT:PSS thin film (thickness 50 nm, sample 1), measured at different temperatures indicated by the color scale. (b) Same data as in (a), rescaled according to the universal scaling procedure discussed in the text. The red and blue dotted lines indicate power laws with slope 1 and $\beta$, respectively; $\alpha=1.0$.

In Fig. 1a the conductivity of a 1:2.5 PEDOT:PSS thin film is plotted as a function of the applied bias voltage for temperatures ranging from 4 K to around 310 K. One can clearly see how the slope of the non-Ohmic behavior increases with decreasing temperature. The transition point at which the conductivity becomes field-dependent, i.e. non-ohmic, shifts to lower fields at lower temperatures. The low-field-conductivity plotted as a function of the temperature on a double-log scale shows a good linear behavior (see SI), from which we obtain the exponent $\alpha=1.0$ in the power law fit to the Ohmic data. If the current of the whole set of measurements is scaled to $j/T^{1+\alpha}$ and plotted as a function of the dimensionless ratio of field energy and thermal energy, $eV/k_BT$, all points collapse to one line and a universal curve is obtained in accordance with Eq. (1), as shown in Fig. 1b. Said $\gamma$ divides the universal curve into an Ohmic regime where $j\propto T^\alpha$ and a temperature-independent non-ohmic regime where $j\propto V^\beta$. The exponents obey the relation $\beta=\alpha+1$ as described previously. Other samples investigated in the course of this work show an equally satisfying universal scaling behavior; the respective plots can be found in the SI.

Using the same set of data we investigated the temperature- and field-dependence in the effective temperature framework. As suggested by Marianer and Shklovskii¹⁹, $T_{eff}$ is experimentally obtained in the following manner. The conductivity $\sigma(F,T)$ at each field and temperature combination is compared to the temperature dependence of the Ohmic conductivity $\sigma(0,T)$ to obtain the effective temperature from the condition $\sigma(0,T_{eff})=\sigma(F,T)$. The practical implementation of solving this equality uses a numerical interpolation of the measured data points in the Ohmic regime, i.e. $\sigma(F\cong0,T)$. The resulting $T_{eff}(F,T)$, seen in Fig. 2a, is a collapse of all data points to a single line following the functional shape of Eq. (2), which is plotted as a solid line with $\varsigma=1.5$ in accordance with ref. 21. Figure 2b shows the corresponding dependence of the measured conductivity on the effective temperature. In this case, the

![](./images/814577366977216515_2.jpg)

Figure 2. Effective temperature and correspondingly scaled conductivity of PEDOT:PSS. (a) Open circles show the collapse of the effective temperature for all data points of sample 1 (c.f. Fig. 1) when plotted against bias voltage and scaled with lattice temperature. The solid line is a fit of Eq. 2 to the experimental data with $\delta=0.67$, $\varsigma=1.5$ and $a=1.8 nm$. (b) Dependence of the measured conductivity on the effective temperature. The dashed line indicates $\sigma \propto T_{eff}^{\alpha}$ with $\alpha=1.2$.

collapse of all points to a single line is an obvious consequence of the procedure followed to determine $T_{eff}$. However, we find that the conductivity scales with a power law in $T_{eff}$, $\sigma \propto T_{eff}^{\alpha}$, as indicated by the solid line, with minor deviations at high temperatures. We have no explanation for this behavior, but note that it is strikingly similar to the dependence of the current on the lattice temperature observed in the Ohmic part of the universal scaling curve in Fig. 1b.

Summarizing our results so far, we have established that our experiments can be consistently analyzed in the US and MS frameworks, suggesting that these two frameworks may, in the present case, actually be equivalent. As a next step, we create synthetic IV-data from Eq. (1) with parameters obtained from fitting this equation to the universal scaling curve for sample 1 (Fig. 1b). We obtain and plot $T_{eff}$ in the same manner as we did for the experiments, cf. Fig. 2a. The result can be seen in Fig. 3a and highlights that both expressions are completely equivalent in terms of functional shape. We should stress that in Fig. 3 no additional fitting has been done to make the two frameworks collapse. The harmony between these two expressions is even more remarkable if one considers that Eq. (2) was found on basis of a numerical 3D-VRH model, while (behavior that functionally resembles) Eq. (1) has been derived for various models of conduction, only one of them being related to 3D-VRH. Figure 3b shows the collapse of the same data set when the conductivity is plotted as a function of $T_{eff}$, cf. Fig. 2b: the synthetic data created from the US expression Eq. (1) shows a power law scaling of the conductivity in $T_{eff}$. Since conductivity and current are proportional and $T_{eff}$ is, like the x-axis of Fig. 1b ($qV/k_{B}T$), basically a measure for the

![](./images/814577366977216515_3.jpg)

Figure 3. Effective temperature analysis of universal scaling behavior (Eq. 1). (a) Effective temperature vs. bias over temperature. Open circles are synthetic data generated from Eq. (1), the full line is a plot of the Marianer-Shklovskii expression Eq. (2), both with parameters corresponding to sample 1. (b) Conductivity vs. effective temperature for the same set of data. The inset shows the universal scaling behavior of the synthetic data from Eq. (1).

combined effect of field and lattice temperature, the main plot in Fig. 3b contains essentially the same information as the plot of the scaled current in Fig. 1b (which is shown as an inset in Fig. 3b).

Following the above, it is in fact straightforward to show full mathematical equivalence of the limiting low- and high-field behavior of the Universal Scaling and Marianer-Shklovskii expressions. As discussed above, the limiting behavior of Eq. (1) is

$$\text{low voltages: } j \propto T^{\alpha} \tag{3a}$$

$$\text{high voltages: } \frac{j}{T^{\alpha+1}} \propto \left(\frac{V}{T}\right)^{\beta} \tag{3b}$$

Transforming current density into conductivity using $j \propto \sigma V$ and $\beta = \alpha + 1$ yields

$$\text{low voltages: } \sigma \propto T^{\alpha} \tag{4a}$$

$$\text{high voltages: } \sigma \propto V^{\alpha} \tag{4b}$$

Inserting the Marianer-Shklovskii expression Eq. (2) into the experimentally found power law dependence of the conductivity on the effective temperature $\sigma \propto T_{eff}^{\alpha}$ (cf. Figs 2b and 3b), we obtain

$$
\sigma \propto \left[ T_{latt}^{\varsigma} + \left( \delta \frac{q \cdot V \cdot a \cdot l}{k_{B}} \right)^{\varsigma} \right]^{\frac{\alpha}{\varsigma}}
\tag{5}
$$

In the high- and low-field limits the first and second terms between the square brackets vanish, reducing Eq. (5) to Eqs (4b) and (4a), respectively. The equal exponents in Eqs (4a) and (4b) also explain why there is no longer a kink in the main panel of Fig. 3(b), whereas there is one in the inset where $j$ instead of $\sigma$ is plotted (c.f. Eq. 3).

Having established the experimental and functional connection between the US and MS, we can approach the question of the common physical background. To this end, theoretical investigations have been done using kinetic Monte Carlo simulations. Kinetic MC can be seen as a simulated real-world experiment under idealized and simplified conditions and with the ability to control every aspect of the virtual sample. In our case, we simulate Coulombically interacting particles performing nearest neighbor hopping (NNH) on a regular lattice with random site energies. Further details can be found in the meth- ods section below and ref. 30. In view of previous experimental work on the same PEDOT:PSS materials, that indicate hopping/percolative transport in the in-/out-of-plane directions³¹,³², this is a logical choice. The use of NNH is justified in the present MC simulations in which we only consider high temperatures and high carrier concentrations. For an analytical treatment of NNH without Coulomb interaction see ref. 33. A further consequence of the use of NNH is that our results are independent of localization length, which is not a parameter used to NNH - in our work $a$ refers to the lattice parameter.

The premise of the simulations used in this work is to reduce the number of assumptions and param- eters to an absolute minimum, making the results as transparent as possible. The model will be shown to be sufficient to qualitatively and even quasi-quantitatively reproduce the experimentally obtained results over a wide range of parameters. For the simulations we used a commonly accepted value for the width of the Gaussian disorder of $\sigma=0.1$ eV, a (relative) concentration $c=0.1$, which roughly corresponds to a 1:2.5 PEDOT:PSS ratio and a PEDOT ionization fraction around 1/3, and a lattice constant $a=1.8$ nm. Henceforth all simulation data presented in this work was calculated using these parameters unless stated otherwise. The specific morphological complexity of PEDOT:PSS is ignored, which not only facilitates computation but also warrants the relevance of the results to organic semiconductors in general. In order to keep calculation times within reasonable limits, only temperatures above room temperature are used.

We performed the same ‘universal’ scaling procedure as before, e.g. from Fig. 1a,b, on the raw simu- lation data in the inset of Fig. 4a. The resulting curve is shown in the main panel of Fig. 4a. The spread in the collapsed curve appears to be large at first glance, but due to the fact that only a limited field and temperature range can be accessed in the simulations, a greatly magnified version of Fig. 1b is obtained. Where experimentally we could cover 7 orders of magnitude, we can only cover 3 orders in simulations, with a relative spread that is in fact comparable to the experimental spread in Fig. 1b. Importantly, apart from the highest lattice temperatures where we cannot reach sufficiently high fields, the individual traces show a clear and shifting transition point from Ohmic to non-Ohmic behavior from high to low tem- peratures (see inset) that collapses onto the transition region between the power law limits in the main panel of Fig. 4a. Simulation and experiment are plotted together in Fig. 4b, and show a quasi-quantitative correspondence that is surprising given the fact that the simulations have not been fitted to the experi- mental results; the parameters were simply chosen to be physically meaningful.

Although an exhaustive investigation of the parameter space is beyond the purpose of the present work, a limited set of calculations with different disorder types and widths is shown in the SI and sug- gest the results are rather robust in terms of shape and width of the disorder, provided a strongly energy dependent DOS is used. For decreasing concentrations the compatibility of the numerical results with US and MS scaling becomes significantly less. Note that in all cases concentrations beyond the Boltzmann limit were used, in line with the experimental systems discussed in the introduction.

From the MC output the occupation probability can be calculated as a function of site energy. Fitting the occupation probability to the Fermi-Dirac distribution function, $f\left(E\right)=1/\left(1+e^{-\left(E-E_{F}\right)/k_{B}T_{eff}}\right)$, yields the effective temperature as a function of field and lattice temperature, $T_{eff}\left(F,T\right)$. This method follows common practice and is equivalent to the way Marianer and Shklovskii obtained $T_{eff}$ in their original work¹⁹,²¹,²². This method assures that, at least in the numerical simulations, $T_{eff}$ is a proper meas- ure of the characteristic energy of the charge carriers. In Fig. 5a $T_{eff}$ is plotted against the field, scaled in the same manner as in Figs 2a and 3a and fitted with the MS expression Eq. 2. Excellent agreement between the MS framework (solid line) and the simulation data (filled circles) is observed. In Fig. 5b, the conductivity is plotted against $T_{eff}$. Unlike for the experimental and synthetic data in Figs 2b and 3b, where the effective temperature was obtained from the Ohmic mobilities, a collapse of the MC conduc- tivity data to a single curve is not trivial for the used procedure of calculating $T_{eff}$ and in fact shows a significant spread. Hence, only an approximate power-law relation between conductivity and effective temperature can be established, as indicated by the dotted line in Fig. 5b. This observation is in line with earlier works concluding that the effective temperature is an approximate concept only²³⁻²⁵. However, it will be shown below that this approximate power law behavior is sufficient for the purposes of this work. Interestingly, when $T_{eff}$ is obtained from the mobility of the MC data, i.e. following the procedure used

![](./images/814577366977216515_4.jpg)

Figure 4. Universal scaling of simulation data. (a) Universal line of simulated current data scaled according to Eq. 1 with $\alpha=2.0$. The inset shows a plot of conductivity vs. bias voltage for various temperatures indicated by the color scale in the main panel. (b) Same as panel (a) with the addition of experimental data for PEDOT:PSS 1:2.5 and simulation data for two concentrations. The dotted lines are guides to the eye and represent an inclination of 1 (red) and 2 (blue) corresponding to the 2 regimes described above.

to analyze the experiments, the field- and temperature-dependence of $\sigma$ does collapse to a single power-law curve similar to Figs 2b and 3b, as is shown in the SI.

Having established both the functional equivalence of the US and MS frameworks and the applica- bility of our MC calculations, we shall now address a possible common physical background leading to the phenomenology that is characteristic for US and MS. Based on the knowledge that $T_{eff}$ represents a characteristic energy of the charge carriers and the fact that the concept of $T_{eff}$ is based on the heating of the charge carrier distribution, we start from the heat balance for the charge carriers in presence of an external field

$$
\dot{Q}_{H}=\sigma \cdot F^{2}=s_{0} \cdot T_{eff}^{\alpha} F^{2}=\dot{Q}_{C} \tag{6}
$$

where the left hand side is the Joule heating per unit volume, which equals the energy loss to the lattice per unit time and volume $\dot{Q}_{C}$. The second equality stems from substituting the conductivity with the experimentally obtained relation $\sigma=s_{0} \cdot T_{eff}^{\alpha}$ (cf. Figs 2b and 3b), where $s_{0}$ is a proportionality constant.

The cooling or relaxation of the charge carrier distribution (at $T_{eff}$) occurs via energy exchange with the lattice (at $T_{latt}$). Since $T_{eff}$ represents a characteristic energy of the charge carriers, the energy lost to the lattice per unit time and volume can be approximated by the time derivative of the Boltzmann energy of the charge distribution in absence of external heating,

$$
\dot{Q}_{C}=n k_{B} \dot{T}_{eff}, \tag{7}
$$

with $n$ the number of charge carriers per unit volume. Equations (6) and (7) are based on the assump- tions that the Ohmic conductivity has a power law dependence on temperature, and that $T_{eff}$ represents

![](./images/814577366977216515_5.jpg)

Figure 5. Effective temperature and correspondingly scaled conductivity of MC data. (a) Collapse of $T_{eff}$ obtained from a fit of the Fermi-Dirac distribution to the energy-dependent occupation probability of the simulation data with a Gaussian disorder of 0.1 eV. The solid line represents a fit of the MS framework (Eq. 2) to the simulation data using $\delta=0.67$, $\varsigma=1.5$ and $a=0.9 nm$. (b) Power law scaling of the conductivity with $T_{eff}$. The dotted line corresponds to the power law relation $\sigma \propto T_{eff}^{\alpha}$ with $\alpha=2$.

the characteristic charge carrier energy and can be used to describe the conductivity of the system. In view of earlier work discussed above and our results presented so far, these assumptions seem reasonable.

When the system has reached steady-state the heating power is equal to the cooling power $\dot{Q}_{H}=\dot{Q}_{C}$ and we can write the heat balance

$$
s_{0} T_{eff}^{\alpha} F^{2}-n k_{B} \dot{T}_{eff}=0. \tag{8}
$$

Solving this differential equation analytically requires an Ansatz for $\dot{Q}_{C}$ or, equivalently, a time-dependent expression of $T_{eff}$.

We use our MC model to find an expression that adequately describes the relaxation of $T_{eff}$. We define the same system as before and relax it to a high lattice temperature $T_{0}$. At time $t=0$ we step $T_{latt}$ from $T_{0}$ to a lower value and monitor the temporal evolution of the temperature of the charge carrier distribution $T_{eff}$, plotted as open circles for different final temperatures in Fig. 6. By inspection of this data we obtained the following purely phenomenological expression, which obeys the condition $f(0)=0$:

$$
T_{eff}=\frac{T_{0}-T_{latt}}{1+\left(\frac{t}{\tau}\right)^{\vartheta}}+T_{latt}, \tag{9}
$$

![](./images/814577366977216515_6.jpg)

Figure 6. Temporal evolution of the effective temperature of the charge carrier distribution following a step in lattice temperature. At $t=0$ the lattice temperature is stepped from $T_0=1900$ K to the value indicated in the legend. Symbols show the relaxation of $T_{eff}$ as calculated with MC. The full lines represent fits of Eqs (8) and (9) with a Gaussian disorder of 0.1 eV, $c=0.1$, $\alpha=2$, $\vartheta$~$1.0\pm0.2$ and $\tau$~$10^{-11}s^{-1}$ to the simulation data.

Here, $\tau$ is a relaxation time constant and $\vartheta$ is a stretching exponent; both are obtained from a fit of Eq. (9) to the simulation data, as shown in Fig. 6. The result is plotted as full lines in Fig. 6 for different final lattice temperatures, showing a reasonable approximation to the simulation data, especially in the relevant temperature range below ~1000 K.

It is noteworthy that at low concentrations, i.e. in or close to the Boltzmann limit, the relaxation of $T_{eff}$ deviates from Fig. 6, as shown in SI Figure 17. Instead, a double power law decay curve is found which cannot be fitted with our empirical expression Eq. (9). The fact that our empirical model breaks down at low concentrations is consistent with the previously discussed incapability of our numerical simulations to reproduce US and MS at lower concentrations. Additionally, when Coulomb interaction is not considered we find that Eq. (9) can only reproduce the relaxation of $T_{eff}$ with $\vartheta>1$, also leading to a failure of the empirical model to consistently reproduce US and MS. The details of the relaxation process under different circumstances as well as the connection to US and MS are topic of ongoing work.

The energetic relaxation of charge carriers in amorphous systems in the Boltzmann limit has been studied before for the case of exponential DOS³⁴ and Gaussian DOS³⁵. Our results indicate that the relaxation time increases with decreasing temperature in agreement with ref. 35. Remarkably the relaxation time constant from the fit to the MC results has roughly the same value as the attempt frequency used in the MC simulation. Inserting Eq. (9) into the heat balance Eq. (8) gives an expression that can analytically be solved for $F$ as a function of $T_{eff}$, the expression however is too lengthy for display here and gives little insight. It is given in the SI. In order to evaluate the field- and lattice temperature-dependence and to compare the empirical model to the MC simulations, we inserted the values of $T_{eff}$ and $T_{latt}$ from our MC simulations into the expression for $F$, SI Eq. (1). This gives $F$ for every $T_{eff}$, $T_{latt}$ combination. The result is plotted in Fig. 7a. The conductivity and current are then determined from $\sigma = s_0 \cdot T_{eff}^{\alpha}$ and $J=\sigma\cdot F$, respectively, using the same values for $T_{eff}$ that we entered into the expression for $F$. Independence of the results on $T_0$, which has no physical meaning beyond being the starting temperature of the relaxation process, was assured, provided it was set to a reasonable value, in our case 1900 K. All other parameters in the heat balance model are determined by the simulations.

Equivalent to the way the experimental, synthetic and simulation data have been analyzed in Figs 1–5, $T_{eff}$ and the scaled current from the heat balance model are plotted as lines in Fig. 7a,b together with the simulation data from Fig. 5a,b. We attribute the minor spread in the heat balance model curves to the imperfect fit of Eq. (9) to the data in Fig. 6. Nevertheless, the characteristics of both the Marianer-Shklovskii and universal scaling behavior are well-reproduced, showing that both can be understood as resulting from a balance between Joule heating and an (effective temperature dependent) relaxation. The crucial ingredient, leading to functional shapes resembling Eqs (1) and (2) is the algebraic time- or, equivalently, temperature-dependent relaxation rate shown in Fig. 6 and its approximation Eq. (9).

### Conclusions
In this work we have investigated two ‘universal’ scaling phenomena for the field- and temperature dependent conductivity of highly disordered organic semiconductors at high charge carrier concentration, the so-called universal scaling (US) and the Marianer-Shklovskii (MS) or effective temperature

![](./images/814577366977216515_7.jpg)

Figure 7. MS and US behavior of the heat balance model for current heating. (a) Effective temperature vs. field scaled with temperature. The dots represent the same MC data as Fig. 5a, the open circles are calculated from the heat balance model. (b) Current data from MC simulation (dots) and heat balance model (open circles) rescaled according to Eq. (1).

scaling. We have shown experimentally, numerically and analytically that phenomenologically the two scaling phenomena in fact describe the same functional dependence in temperature and voltage, with identical limiting behaviors. Experimentally US and MS scaling were observed in the out-of-plane trans- port in PEDOT:PSS thin films of various compositions. The observed behavior was quasi-quantitatively reproduced using a numerical nearest-neighbor hopping model with Coulomb interaction, high charge carrier concentration and energetic disorder as only ingredients. Finally, we derived an empirical model that shows that both scaling phenomena can have their physical origin in a simple heat balance of Joule heating and energy-dependent relaxation, under the condition that the Ohmic conductivity is a power law function of the (effective) temperature.

Although the described numerical and empirical models reproduce the main characteristics of US and MS scaling, they do not formally lead to the analytical expressions Eqs (1) and (2) that are com- monly associated with these scaling behaviors. In fact, depending on the used input parameters, both the numerical and the empirical model show smaller or larger deviations from the ideal scaling behavior – something that is quite reminiscent of experimental reality in which many investigated systems show deviations of similar or even larger magnitude.

### Methods
**Experimental.** PEDOT:PSS (Orgacon ICP-1050) with a PEDOT to PSS weight ratio of 1:2.5 was obtained from AGFA-Gevaert N.V. PEDOT:PSS weight ratios 1:6, 1:12, and 1:20 were prepared by add- ing PSS to the aqueous dispersions. Where necessary, water was added to obtain a solid content of $0.90\pm0.04$ w% and sonication was used to obtain homogeneous dispersions.

As substrates 4-inch silicon wafers with a 500 nm thermally grown silicon oxide were used. On this wafer, a 1 nm layer of chromium was thermally evaporated through a shadow mask, followed by 60 nm of gold. The root-mean-square (RMS) roughness of the bottom contact is about 0.7 nm over an area of 0.25 μm². The two terminal junctions were photolithographically defined in an insulating matrix of photoresist, ma-N 1410 (Micro Resist Technology GmbH). After a pre-bake step to remove any remaining solvents, the layer was exposed to UV light with a Karl Süss MA1006 mask aligner to define the vertical interconnects, ‘vias’, with diameters of 5, 10, 20, 50, and 100 μm. After development the film was hard baked at 200 °C for at least 1 h. The wafer was subsequently cut in several pieces using a diamond tip pen. This allowed the processing of different PEDOT:PSS compositions on a single wafer, thereby eliminating lithographic variations that can affect device performance. A last step before layer deposition was cleaning of the bottom gold contacts with a PDC plasma cleaner (Harrick plasma) to remove any photoresiduals. To obtain an equal layer thickness for all PEDOT:PSS ratios, the following spin coat parameters were used. The ramp-rate was 1000 RPM/s and the first spin coating step is 500 RPM for 5 s followed by 120 s of 2000 RPM (for 1:2.5), 1700 RPM (1:6), 1500 RPM (1:12), 1500 RPM (1:20). On planar test substrates these parameters led to layer thicknesses around 40 nm. After spin coating, the wafer was then immediately transferred to a vacuum oven to dry the film for at least 1 h. As top electrode, 100 nm of gold was evaporated through a shadow mask. This gold layer, apart from providing electrical contact with the measurement probes, also serves as a self-aligned mask for the removal of redundant PEDOT:PSS by reactive ion etching (O₂ plasma). This step eliminates any parasitic currents from top to bottom electrode.

Measurements were performed in a high-vacuum probe-station (Janis research) at controlled temperatures between 5 and 300 K. Two types of *J-V* curves have been determined using a Keithley 2636a source-measure unit. Measurements often show transient changes, usually as irreversible steps in the conductivity with temperature. The measurements used for analysis were selected to contain no such changes.

Numerical model. The MC experiments were performed in cube of variable side length *L* and periodic boundary conditions in all three dimensions. The localized sites are spatially distributed on a simple cubic lattice with an inter-site distance *a* = 1.8 nm and energetically with a Gaussian, exponential or constant distribution and varying degrees of disorder. The system contains *n* holes in a concentration *c* = *n/N* ($N=L^3/a^3$) and has no contacts, resulting in a constant carrier concentration during the course of one simulation. The size of the simulated system was chosen according to the relative concentration, i.e. small box size for high concentrations and large box size for small concentrations. The model example presented in this work with *c* = 0.1 was simulated in a $10 \times 10 \times 10$ box, enclosing 100 charges; for *c* = 0.01 and *c* = 0.001 $15 \times 15 \times 15$ and $32 \times 32 \times 32$ box sizes were used, enclosing 34 and 33 charges, respectively. For each set of parameters the data was averaged over 20 configurations. Coulomb interaction between all carriers was included using a commonly accepted value for the relative permittivity of 3.6. Also the Coulomb interactions of each carrier with the ‘twins’ of all other carriers that result from the 3D periodic boundary conditions have been included exactly up to a distance where the effect of the interaction becomes undiscernible – typically a cut-off of 5 box sizes was used.

We describe the charge transport by nearest-neighbor hopping of holes from an initial site *i* with energy $E_i$ to a final site *j* with energy $E_j$ with the hopping rate $\nu_{ij}$ according to the Miller-Abrahams expression

$$
\nu_{ij} = \nu_0 \exp\left(-2\frac{\overrightarrow{r_{ij}}}{a}ight)
\begin{cases}
\exp\left(-\dfrac{E_j - E_i - q \cdot \overrightarrow{F} + \Delta E_C}{k_B T}ight) & E_j > E_i \\
1 & E_j \leq E_i,
\end{cases}
$$

where $\nu_0$ is the attempt frequency, $r_{ij}$ the vector connecting initial and final sites. The change in Coulomb energy is represented by $\Delta E_C$ and calculated by evaluation of the interaction of the moving charge with all other charges in the sample. The waiting time between hops and the direction of a hop are selected randomly according to the MC mechanism, using the rates of all possible transitions as weight factors. It should be mentioned that the validity of the MC simulations is restricted foremost by the field term in the Miller-Abrahams expressions. Too low fields result in currents that are in the order of the achievable statistical accuracy, while too high fields lead to a saturation of the mobility and a subsequent decrease. The reason for the latter effect lies in the fact that at some field (depending on the concentration and lattice temperature) the characteristic final site sits energetically at or below the initial site, so no further current gain is achieved by further increasing the field. Hence, to rule out any misleading effects we limited our theoretical investigations to a field range between these two limits.

### References
1.  Mott, N. F. & Davis, E. A. *Electronic Processes in Non-Crystalline Materials*. (Oxford University Press, 2012).
2.  Shklovskiĭ, B. I. & Efros, A. L. *Electronic properties of doped semiconductors*. (Springer-Verlag, 1984).

3. Larkin, A. I. & Khmel'nitskii. Activation conductivity in disordered systems with large localization length. *Sov. Phys. JETP* **56**, 647–652 (1982).

4. Kim, J. Y., Jung, J. H., Lee, D. E. & Joo, J. Enhancement of electrical conductivity of poly(3,4-ethylenedioxythiophene)/poly(4- styrenesulfonate) by a change of solvents. *Synth. Met.* **126**, 311–316 (2002).

5. Duvail, J. L. *et al.* Effects of the Confined Synthesis on Conjugated Polymer Transport Properties. *J. Phys. Chem. B* **108**, 18552–18556 (2004).

6. Kronemeijer, A. J. *et al.* Universal scaling of the charge transport in large-area molecular junctions. *Small* **7**, 1593–1598 (2011).

7. Zhou, Z. *et al.* One-dimensional electron transport in Cu-tetracyanoquinodimethane organic nanowires. *Appl. Phys. Lett.* **90**, 90–92 (2007).

8. Aleshin, A., Lee, H., Park, Y. & Akagi, K. One-Dimensional Transport in Polymer Nanofibers. *Phys. Rev. Lett.* **93**, (2004).

9. Yuen, J. D. *et al.* Nonlinear transport in semiconducting polymers at high carrier densities. *Nat. Mater.* **8**, 572–575 (2009).

10. Kronemeijer, A. J. *et al.* Universal Scaling in Highly Doped Conducting Polymer Films. *Phys. Rev. Lett.* **105**, 156604 (2010).

11. Rahman, A. & Sanyal, M. K. Bias dependent crossover from variable range hopping to power law characteristics in the resistivity of polymer nanowires. *J. Phys. Condens. Matter* **22**, 175301 (2010).

12. Borsenberger, P. M., Pautmeier, L. T. & Bässler, H. Nondispersive-to-dispersive charge-transport transition in disordered molecular solids. *Phys. Rev. B* **46**, 12145–12153 (1992).

13. Deshpande, V. V., Bockrath, M., Glazman, L. I. & Yacoby, A. Electron liquids and solids in one dimension. *Nature* **464**, 209–216 (2010).

14. Dayen, J.-F. *et al.* Conductance of disordered semiconducting nanowires and carbon nanotubes: a chain of quantum dots. *Eur. Phys. J. Appl. Phys.* **48** (2009).

15. Fogler, M. M., Malinin, S. V. & Nattermann, T. Coulomb blockade and transport in a chain of one-dimensional quantum dots. *Phys. Rev. Lett.* **97**, 1–4 (2006).

16. Rodin, A. S. & Fogler, M. M. Apparent power-law behavior of conductance in disordered quasi-one-dimensional systems. *Phys. Rev. Lett.* **105**, 1–4 (2010).

17. Asadi, K. *et al.* Polaron hopping mediated by nuclear tunnelling in semiconducting polymers at high carrier density. *Nat. Commun.* **4**, 1710 (2013).

18. Li, L., Lu, N. & Liu, M. Physical Origin of Nonlinear transport in organic semiconductor at high carrier densities. **164504** (2013).

19. Marianer, S. & Shklovskii, B. I. Effective temperature of hopping electrons in a strong electric field. *Phys. Rev. B* **46**, 13100–13103 (1992).

20. Baranovskii, S. D., Cleve, B., Hess, R. & Thomas, P. Effective temperature for electrons in band tails. *J. Non. Cryst. Solids* **164–166**, 437–440 (1993).

21. Jansson, F., Baranovskii, S., Gebhard, F. & Österbacka, R. Effective temperature for hopping transport in a Gaussian density of states. *Phys. Rev. B* **77**, 195211 (2008).

22. Preezant, Y. & Tessler, N. Carrier heating in disordered organic semiconductors. *Phys. Rev. B* **74**, 235202 (2006).

23. Jurić, I., Batistić, I. & Tutiš, E. Beyond the effective temperature: The electron ensemble at high electric fields in disordered organics. *Phys. Rev. B - Condens. Matter Mater. Phys.* **82**, 1–11 (2010).

24. Cleve, B. *et al.* High-field hopping transport in band tails of disordered semiconductors. *Phys. Rev. B* **51** (1995).

25. Cottaar, J., Coehoorn, R. & Bobbert, P. A. Field-induced detrapping in disordered organic semiconducting host-guest systems. *Phys. Rev. B* **82**, 205203 (2010).

26. Nebel, C. E., Street, R. A., Johnson, N. M. & Kocka, J. High-electric-field transport in a-Si:H. I. Transient photoconductivity. *Phys. Rev. B* **46**, 6789–6802 (1992).

27. Muschik, T. & Schwarz, R. Electric-field dependence of low-temperature recombination in a-Si:H. *Phys. Rev. B* **51**, 5078–5088 (1995).

28. Palsule, C., Yi, S., Gangopadhyay, S., Schmidt, U. & Schröder, B. Experimental Evidence for the Applicability of an Effective Temperature Concept in a-Si:H. *Phys. Rev. Lett.* **73**, 3145–3148 (1994).

29. Katsouras, I., Geskin, V., Kronemeijer, A. J., Blom, P. W. M. & De Leeuw, D. M. Binary self-assembled monolayers: Apparent exponential dependence of resistance on average molecular length. *Org. Electron. physics, Mater. Appl.* **12**, 857–864 (2011).

30. Melianas, A. *et al.* Dispersion-dominated photocurrent in polymer:fullerene solar cells. *Adv. Funct. Mater.* **24**, 4507–4514 (2014).

31. Van de Ruit, K. *et al.* The Curious Out-of-Plane Conductivity of PEDOT:PSS. *Adv. Funct. Mater.* **23**, 5787–5793 (2013).

32. Van de Ruit, K. *et al.* Quasi-One Dimensional in-Plane Conductivity in Filamentary Films of PEDOT:PSS. *Adv. Funct. Mater.* **23**, 5778–5786 (2013).

33. Cotaar, J. *et al.* Scaling Theory for Percolative Charge Transport in Disordered Molecular Semiconductors. *Phy. Rev. Lett.* **107**, 1–4 (2011).

34. Monroe, D. Hopping in Exponential Band Tails. *Phys. Rev. Lett.* **54**, 146–149 (1985).

35. Bässler, H. Charge Transport in Disordered Organic Photoconductors. *Phys. Stat. Sol. (b)*. **175**, 15–56 (1993).

## Acknowledgements
It is a pleasure to acknowledge Ilias Katsouras and Dago de Leeuw for providing the via technology and for stimulating discussions. We are grateful to Dirk Bollen for providing the PEDOT:PSS material.

## Author Contributions
K.v.d.R. performed experiments, H.A. and K.v.d.R. performed data analysis, H.A. and M.K. performed numerical simulations and wrote the manuscript, M.K. initiated and coordinated the research.

## Additional Information
Supplementary information accompanies this paper at http://www.nature.com/srep

Competing financial interests: The authors declare no competing financial interests.

How to cite this article: Abdalla, H. *et al.* Effective Temperature and Universal Conductivity Scaling in Organic Semiconductors. *Sci. Rep.* **5**, 16870; doi: 10.1038/srep16870 (2015).

![](./images/814577366977216515_8.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/