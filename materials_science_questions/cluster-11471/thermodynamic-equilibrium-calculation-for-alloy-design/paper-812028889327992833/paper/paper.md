# A computational study of austenite formation kinetics in rapidly heated steels

A.I. Katsamas *

University of Thessaly, Department of Mechanical and Industrial Engineering, Pedion Areos, 38334, Volos, Greece

Received 13 February 2006; accepted in revised form 13 December 2006
Available online 28 December 2006

## Abstract
Surface hardening of steels involves rapid austenitization and subsequent quenching of the surface. The resulting extent of hardening largely depends on the rate of austenitization of the surface under the applied high heating rates. In the present work the kinetics of austenite formation in Fe–C alloys during rapid, non-isothermal heating conditions, characterized by high heating rates and short austenitization periods, were studied by means of computational simulation. Austenitization of lamellar pearlite/proeutectoid ferrite microstructures was simulated by assuming two kinetically distinct stages: i) dissolution of lamellar pearlite followed by ii) dissolution of proeutectoid ferrite. The two stages were simulated by two corresponding 1-D diffusion models employed in series. Numerical solution of the resultant moving-boundary diffusion problems provide calculated results regarding the dependency of vol. fraction austenite on thermal cycle parameters and on initial microstructural features of the steel. Analysis of calculated results showed that the vol. fraction of pearlite transforming to austenite during pearlite dissolution depended on maximum temperature, dwell time and pearlite interlamellar spacing. A functional relationship between these variables, consisting of a thermodynamic and a kinetic term, was established. On the other hand, the total vol. fraction of austenite forming in the steel, after both stages of austenitization, was found to follow a typical sigmoidal kinetic behaviour.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Steels; Austenite; Annealing; Phase transformation kinetics; Simulation

## 1. Introduction
A significant variety of thermal and thermo-mechanical processing of steels involves, at some stage, the formation of austenite in the microstructure. Quench-hardening, normaliz-ing, surface transformation hardening, and carburizing are just some examples of processes involving austenitization, as it comprises the first stage to be completed before any further modification of the microstructure and, consequently, of the properties of steel can be obtained. Consequently, the inves-tigation of austenite formation kinetics presents an interest, from both a scientific and a technological point of view. Fur-thermore, it is quite evident that an investigation regarding the rate of austenitization under conditions of rapid heating and short austenitization times would be interesting, for reasons associated with productivity aspects, as well as with design considerations, regarding a particular process.

Both experimental and theoretical work on the formation of austenite, in various types of steels and starting microstructures, can be found in the literature [1–6]. These studies examine the formation of austenite either under isothermal conditions or under continuous heating at slow and moderate heating rates. However, limited experimental work, and even less theoretical work, exists on austenitization kinetics at high heating rates ($\geq 10^3$ K/s) and short austenitization periods. Such extreme heating conditions are usually encountered in processes like surface transformation hardening using laser or electron beams, where heating rates in the order of $10^4$ K/s or even greater can be obtained, with austenitization periods in the order of a few tenths of milliseconds [7]. In such processes, prediction of, for example, the depth of austenitization, which determines the final hardened case depth, is substantial to their design. But even in more industrially applied processes, like for example in continuous annealing of steel sheet, rapid austenitization could be translated to increased production rates.

Austenite formation is a process that requires small but definite time periods [8]. Therefore, a question arises regarding the pos-sibility to form homogeneous austenite during rapid heating. The

* Tel./fax: +30 2421074082.
E-mail address: akatsam@mie.uth.gr.

0257-8972/$ - see front matter © 2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.surfcoat.2006.12.014

issue becomes more complicated since critical austenitization temperatures on heating tend to assume higher values as heating rates increase. Studies have been reported, where the critical $A_{\text{e3}}$ austenitization temperature in rapidly heated low and medium carbon steels has increased by up to 200 °C, compared to the equilibrium critical $A_{\text{e3}}$ temperature [9–11]. An increase due to high-rate heating should also be expected for the critical $A_{\text{e1}}$ temperature, which is the equilibrium temperature for the start of austenite formation. However, since $A_{\text{e1}}$ actually represents the temperature at which the very first nuclei of austenite form, it should not be expected to vary as dramatically as the critical $A_{\text{e3}}$ temperature with heating rate. This is because the $A_{\text{e3}}$ temperature represents the completion of the austenitization process, which is a purely diffusion-controlled process. Therefore, when the rate of heating of the material (i.e. the rate at which the material's temperature increases) exceeds by far the rate of diffusional mass- transfer, austenitization completes at a significantly higher tem- perature than the one predicted by equilibrium. In contrast, for- mation of the first austenitic nuclei, a process associated with the $A_{\text{e1}}$ temperature, is mainly determined by the available free energy "driving force" for nucleation, a quantity not particularly depen- dent on the heating rate, but rather on the level of superheating.

The present work is an effort to study the kinetics of austenite formation in Fe–C binary alloys, under high heating rates and short austenitization periods. The basic incentive to this work was to employ modeling of austenitization kinetics, in order to predict the case-depths obtained during laser transformation hardening of plain carbon steels. The results of this effort, however, could be extended to any process involving rapid austenitization, since as will be made evident, they are inde- pendent of the specific type of processing.

The steels employed in laser transformation hardening are usually in the normalized condition, i.e. their starting microstruc- ture consists of a mixture of lamellar pearlite and proeutectoid ferrite. Austenitization of such microstructures can be assumed to proceed in two kinetically distinct stages: At the first stage, pearlite colonies dissolve, forming austenite of the eutectoid composition. Upon completion of the first stage, this high-carbon austenite formed from pearlite grows in expense of ferrite, a process comprising the second stage of austenitization [12].

In the present investigation, the kinetics of austenite formation was studied by employing two simple diffusion models used in series, each one simulating the corresponding stage of austenitization. The corresponding moving-boundary diffusion problems simulating austenitization were then solved numerically, employing mobility databases that account for the variation of C diffusivity in ferrite and austenite with tem- perature and C-concentration. Both models take into account parameters that describe the rapid variation of temperature with time, as well as characteristic features of the starting micro- structure of the steel, and calculate the amount of austenite formed in the microstructure.

## 2. The thermal cycle

In order to investigate the effect of high heating rates and short austenitization periods on the amount of austenite forming in the steel, certain assumptions regarding the *thermal cycle*, i.e. the temporal variation of temperature during the process, had to be considered. In a typical thermal cycle, undergone by a steel surface irradiated with a laser beam, temperature in- creases rapidly from room temperature, $T_0$, as the laser beam approaches the surface, and quickly reaches a maximum value, $T_{\text{max}}$. As the beam moves away, heat transfers rapidly by conduction into the cold interior of the work-piece and tem- perature decreases again very quickly (self-quenching). It is important to note that the thermal cycle depends strongly on process conditions, e.g. in the case of laser surface hardening, laser beam power, travel speed, etc. Thus, for example, increasing the beam power leads to higher values of $T_{\text{max}}$, while increasing travel speed increases the heating rate, but leads to lower values of $T_{\text{max}}$.

For the purposes of the present study, the thermal cycle was approached in a simpler way, as shown in Fig. 1a. The temperature was considered to increase linearly with a constant

![](./images/812028889327992833_1.jpg)

Fig. 1. (a) Approximation of the thermal cycle used in the present work. (b) Calculated thermal cycles at various depths of the surface of a Ck-60 steel specimen irradiated with a laser beam of 1500 W power, 5 mm diameter and 75 mm/s scanning speed.

heating rate, $H_{\mathrm{C}}$, and then to decrease linearly with a constant cooling rate, $H_{\mathrm{R}}$. The dwell time, $\tau$, represents the period of time spent above the critical $A_{\mathrm{e} 1}$ temperature $(727\ ^{\circ}\text{C}$ in binary Fe–C systems), during which austenitization is possible from a thermodynamic point of view. It can be readily shown that the dwell time, as defined here, is related to the other parameters of the thermal cycle by the equation:

$$
\tau=\frac{\left(T_{\max }-A_{\mathrm{e} 1}\right)\left(H_{\mathrm{C}}+H_{\mathrm{R}}\right)}{H_{\mathrm{C}} H_{\mathrm{R}}}. \tag{1}
$$

It is evident from Eq. (1) that any specific value of the dwell time can be achieved by various combinations of $T_{\max }, H_{\mathrm{C}}$ and $H_{\mathrm{R}}$.

As mentioned in the previous paragraph, the actual magnitudes of the heating $(H_{\mathrm{C}})$ and cooling rate $(H_{\mathrm{R}})$ and of the maximum temperature $(T_{\max })$ of the thermal cycle depend on process conditions. Through Eq. (1) it is evident that the same holds for the dwell time $(\tau)$. It should also be noted that during irradiation of a steel specimen with fixed process conditions, the thermal cycle experienced by each point of the specimen's surface varies, depending on the distance of the point from the heat source. For example, Fig. 1b depicts calculated thermal cycles for a Ck-60 steel specimen, irradiated with a 1500 W power laser-beam of 5 mm diameter at a scanning speed of 75 mm/s. Each curve in Fig. 1b corresponds to the thermal cycle experienced by points located at the center of the beam track, but at various depths below the specimen's surface ($z$=0 corresponds exactly on the irradiated surface). The horizontal dashed line represents the $A_{\mathrm{e} 1}$ temperature. As shown, the maximum temperature of the thermal cycle varies significantly with depth. The same is true for the dwell time, defined as the temporal duration of the thermal cycle spent above the $A_{\mathrm{e} 1}$ temperature. For the example given in Fig. 1b, the dwell time on the surface (i.e. at $z$=0) is approximately 32 ms, at $z$=0.2 mm approximately 9 ms, etc. The greater the maximum temperature and/or the dwell time of the thermal cycle at a specific point of the surface, the greater the expected fraction of austenitization will be, due to the higher thermodynamic driving force available for austenitization (mainly associated with the value of $T_{\max }$), and to the greater available time for austenitization (associated with both $T_{\max }$ and $\tau$). One of the scopes of this work was to determine the interrelationships between thermal cycle characteristics and the extent of austenitization of the surface.

## 3. Simulation of austenite formation kinetics

### 3.1. Pearlite dissolution model

The first stage of austenitization in pearlitic/ferritic steels involves the dissolution of lamellar pearlite, which transforms to C-rich austenite, as described earlier. Fig. 2a sketches part of a pearlitic colony, with the characteristic alternate lamellae of cementite ($\mathrm{Fe}_{3} \mathrm{C}$) and ferrite ($\alpha$). In order to study the kinetics of austenite formation from pearlite dissolution, the simplifying assumption was adopted stating that austenite ($\gamma$) nucleates at the $\mathrm{Fe}_{3} \mathrm{C} / \alpha$ lamellae interfaces, creating two new interfaces, $\mathrm{Fe}_{3} \mathrm{C} / \gamma$ and $\gamma / \alpha$, as shown in Fig. 2b. Austenite growth then takes place by the simultaneous movement of these two interfaces into $\mathrm{Fe}_{3} \mathrm{C}$ and $\alpha$, respectively. For reasons related to the symmetry of the microstructure, half of the $\mathrm{Fe}_{3} \mathrm{C}$ and $\alpha$ lamellae were taken into account. Furthermore, assuming a planar geometry for the interfaces, the problem is reduced to one dimension (1-D), and the domain of the diffusion model is the one depicted by the thick solid line in Fig. 2a.

![](./images/812028889327992833_2.jpg)

Fig. 2. (a) Schematic representation of the lamellar pearlite dissolution diffusion model and (b) adopted mechanism of austenite nucleation and growth in lamellar pearlite.

The relation between the thickness of the $\mathrm{Fe}_{3} \mathrm{C}$ and $\alpha$ lamellae, $s_{\mathrm{cem}}$ and $s_{\alpha}$, which are a measure of the interlamellar spacing of pearlite, and thus represent a characteristic feature of the starting microstructure, can be determined by thermodynamic considerations. Since the model is 1-D, the ratio $s_{\mathrm{cem}} / s_{\alpha}$ can be directly related to the ratio of vol. fractions of the two phases comprising pearlite:

$$
\frac{f_{\mathrm{cem}}}{f_{\alpha}}=\frac{S_{\mathrm{cem}}}{S_{\alpha}}. \tag{2}
$$

Then, the initial thickness and chemical composition of the two phases must conform to the eutectoid composition of pearlite:

$$
s_{\mathrm{cem}} \cdot c_{\mathrm{cem}}+s_{\alpha} \cdot c_{\alpha}=\left(s_{\mathrm{cem}}+s_{\alpha}\right) \cdot c_{\mathrm{eut}}. \tag{3}
$$

In Eq. (3) $c_{\mathrm{cem}}$ and $c_{\alpha}$ are the concentrations of C in cementite and ferrite, respectively, and $c_{\mathrm{eut}}$ the eutectoid concentration of C in pearlite (0.76% mass in binary Fe–C systems). The thickness of the $\mathrm{Fe}_{3} \mathrm{C}$ lamellae can be readily measured by light optical or scanning electron micrographs of the steel and the corresponding thickness of the ferrite lamellae can then be calculated by Eqs. (2) and (3).

Austenite formation from the dissolution of pearlite can be simulated by solving the diffusion equations in the phases

involved. The variation of C-content with time inside each phase is described by the mass conservation equation:

$$
\frac{\partial c_{i}}{\partial t}=\frac{\partial}{\partial x}\left(D_{i} \frac{\partial c_{i}}{\partial x}\right),
\tag{4}
$$

where $c_{i}$ is the concentration and $D_{i}$ the diffusion coefficient of C in phase $i$.

The flux of C atoms passing through the interfaces is described by the respective flux-balance equations:

$$
u_{\mathrm{Fe}_{3} \mathrm{C} / \gamma} \cdot\left(c_{\mathrm{Fe}_{3} \mathrm{C}}^{\mathrm{Fe}_{3} \mathrm{C} / \gamma}-c_{\gamma}^{\mathrm{Fe}_{3} \mathrm{C} / \gamma}\right)=\left.D_{\gamma} \frac{\partial c_{\gamma}}{\partial x}\right|_{\mathrm{Fe}_{3} \mathrm{C} / \gamma}-\left.D_{\mathrm{Fe}_{3} \mathrm{C}} \frac{\partial c_{\mathrm{Fe}_{3} \mathrm{C}}}{\partial x}\right|_{\mathrm{Fe}_{3} \mathrm{C} / \gamma},
\tag{5}
$$

at the $\mathrm{Fe}_{3} \mathrm{C} / \gamma$ interface and

$$
u_{\gamma / \alpha} \cdot\left(c_{\gamma}^{\gamma / \alpha}-c_{\alpha}^{\gamma / \alpha}\right)=\left.D_{\alpha} \frac{\partial c_{\alpha}}{\partial x}\right|_{\gamma / \alpha}-\left.D_{\gamma} \frac{\partial c_{\gamma}}{\partial x}\right|_{\gamma / \alpha},
\tag{6}
$$

at the $\gamma / \alpha$ interface.

In Eqs. (5) and (6), $c_{\mathrm{Fe}_{3} \mathrm{C}}^{\mathrm{Fe}_{3} \mathrm{C} / \gamma}, c_{\gamma}^{\mathrm{Fe}_{3} \mathrm{C} / \gamma}, c_{\gamma}^{\gamma / \alpha}$ and $c_{\alpha}^{\gamma / \alpha}$ represent the C concentration of each phase (denoted by the subscript) on the corresponding phase interface (denoted by the superscript). These concentrations can be readily determined by the Fe–C equilibrium diagram at any instantaneous temperature, under the assumption that the interfaces are in local thermodynamic equilibrium during the transformation (diffusion controlled transformation) [13,14]. The rate of transformation is effectively expressed by $u_{\mathrm{Fe}_{3} \mathrm{C} / \gamma}$ and $u_{\gamma / \alpha}$, which denote the velocity of the $\mathrm{Fe}_{3} \mathrm{C} / \gamma$ and $\gamma / \alpha$ interfaces, respectively. Finally, $D_{\mathrm{Fe}_{3} \mathrm{C}}, D_{\gamma}$ and $D_{\alpha}$ represent the diffusion coefficients of C in each phase. The diffusion coefficients are determined by the method described in detail in Engstrom et al. [15], which involves both thermody- namic and kinetic calculations, and leads to temperature- and concentration-dependent diffusion coefficients. Finally, the solution domain is considered not to exchange mass with its surroundings due to the symmetry of the problem, i.e.,

$$
\left.\frac{\partial c}{\partial x}\right|_{x=0}=0 \quad \text { and }\left.\quad \frac{\partial c}{\partial c}\right|_{x=s_{\mathrm{cem}}+s_{\alpha}}=0.
\tag{7}
$$

Solution of this 1-D moving boundary problem can then be obtained numerically, employing a method developed by Ågren [16,17] and incorporated in the commercial, diffusion- controlled transformations simulation software DICTRA, which also performs the calculation of the associated diffusion coefficients, retrieving the necessary thermodynamic and kinetic data from the SGTE databases also available with the software.

### 3.2. Proeutectoid ferrite dissolution model

For the purposes of the present work, the assumption was made that unless completion of the first stage was achieved, austenitization did not proceed to the second stage, i.e. no proeutectoid ferrite transformed to austenite. Therefore, the proeutectoid ferrite dissolution model, which will be described right away, was only used in those cases where all pearlite had been previously dissolved during a fraction of the thermal cycle.

![](./images/812028889327992833_3.jpg)

Fig. 3. Schematic representation of the proeutectoid ferrite dissolution model.

In other words, the two models were used in series, in order to simulate the overall austenitization process.

A schematic representation of the model is shown in Fig. 3, where it can be seen that the system comprises of two regions: a C-rich austenitic $(\gamma)$ region formed during the first stage, and a proeutectoid ferrite (pro,$\alpha$) region. The initial sizes of the two regions, $s_{\gamma}$ and $s_{\text{pro},\alpha}$, can be calculated by using the vol. fractions of the two phases at temperature $A_{\text{e}1}$:

$$
\frac{S_{\gamma}}{S_{\text{pro},\alpha}}=\frac{f_{\gamma}}{f_{\text{pro},\alpha}}.
\tag{8}
$$

It should be noted that the initial sizes of the regions are calculated at temperature $A_{\text{e}1}$ and not at the temperature where pearlite dissolves completely on heating, because it has already been assumed that during pearlite dissolution proeutectoid ferrite does not participate in the transformation. The initial size and composition of the two phases must conform to the nominal C-content of the steel:

$$
s_{\gamma} \cdot c_{\gamma}+s_{\text{pro},\alpha} \cdot c_{\text{pro},\alpha}=\left(s_{\gamma}+s_{\text{pro},\alpha}\right) \cdot c_{0},
\tag{9}
$$

where $c_{\gamma}$ and $c_{\text{pro},\alpha}$ are the concentrations of C in austenite and proeutectoid ferrite, respectively, and $c_{0}$ the nominal C-content of the steel. The initial proeutectoid ferrite region size $(s_{\text{pro},\alpha})$ is an indication of the ferrite grain-size, which can be determined by standard quantitative–metallography techniques. Then, Eq. (9) can be used in order to determine a realistic value for the corresponding size of the initial size of the austenite region $(s_{\gamma})$ for the simulations.

Austenitization can be simulated by solving the diffusion equations in the two phases. The variation of C in each phase is described by the conservation of mass:

$$
\frac{\partial c_{i}}{\partial t}=\frac{\partial}{\partial x}\left(D_{i} \frac{\partial c_{i}}{\partial x}\right),
\tag{10}
$$

where $c_{i}$ is the concentration and $D_{i}$ the diffusion coefficient of C in phase $i$ (austenite or proeutectoid ferrite).

The flux of C atoms through the $\gamma$/pro,$\alpha$ interface is described by the respective flux-balance equation:

$$
u_{\gamma / \text{pro},\alpha} \cdot\left(c_{\gamma}^{\gamma / \text{pro},\alpha}-c_{\alpha}^{\gamma / \text{pro},\alpha}\right)=\left.D_{\alpha} \frac{\partial c_{\text{pro},\alpha}}{\partial x}\right|_{\gamma / \text{pro},\alpha}-\left.D_{\gamma} \frac{\partial c_{\gamma}}{\partial x}\right|_{\gamma / \text{pro},\alpha}.
\tag{11}
$$

<table>
<caption>Table 1 Range of thermal cycle parameters employed in the simulations</caption>
<thead>
  <tr>
    <th>Maximum temperature, $T_{\text{max}}$ (°C)</th>
    <th>Heating/cooling rate, $H_{\text{C}}$/$H_{\text{R}}$ (K/s)</th>
    <th>Dwell time, $\tau$ (s)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>750</td>
    <td>$10^{3}$–$10^{6}$</td>
    <td>$4.70×10^{-2}$–$4.70×10^{-5}$</td>
  </tr>
  <tr>
    <td>800</td>
    <td>$10^{3}$–$10^{6}$</td>
    <td>$1.47×10^{-1}$–$1.47×10^{-4}$</td>
  </tr>
  <tr>
    <td>850</td>
    <td>$10^{3}$–$10^{6}$</td>
    <td>$2.47×10^{-1}$–$2.47×10^{-4}$</td>
  </tr>
  <tr>
    <td>900</td>
    <td>$10^{3}$–$10^{6}$</td>
    <td>$3.47×10^{-1}$–$3.47×10^{-4}$</td>
  </tr>
</tbody>
</table>

The various parameters in Eq. (11) have the same meaning as in the case of the pearlite dissolution model, described in the previous section. Concentrations $c_{\gamma}^{\gamma/\text{pro},\alpha}$ and $c_{\alpha}^{\gamma/\text{pro},\alpha}$ once again denote the C concentration in austenite and proeutectoid ferrite at the $\gamma/\text{pro,}\alpha$ interface, which is considered to be in local thermodynamic equilibrium during the transformation.

## 4. Results and discussion

The two previously described moving-boundary diffusion models were used in order to study the effect of thermal cycle parameters ($T_{\text{max}}$, $\tau$, $H_{\text{C}}$, $H_{\text{R}}$) and microstructural features ($s_{\text{cem}}$, $s_{\text{pro},\alpha}$) on the kinetics of austenitization, in a systematic manner. Table 1 presents the range of thermal cycle parameters employed in the analysis, while the values of microstructural features used are shown in Table 2. Austenitization simulations were carried out using a binary Fe–0.60% mass C system. The results of the parametric analysis are discussed in the following sections, separately for each stage of austenitization.

### 4.1. Pearlite dissolution

Fig. 4 depicts a typical curve of the vol. fraction pearlite transformed to austenite, $f_{\text{p}\rightarrow\gamma}$, as a function of time. Similar curves were calculated for all the range of parameters employed in the analysis. It should be noted that there is a time period during which no pearlite has transformed. This period corresponds to the time taken for the temperature to rise from room temperature ($T_{0}$=25 °C) to the critical temperature $A_{\text{e1}}$=727 °C. Austenite nucleates at time $t_{\text{N}}$, which corresponds to temperature $A_{\text{e1}}$, and then grows in pearlite. The simulation terminates at time $t_{\text{T}}$, which also corresponds to temperature $A_{\text{e1}}$, but this time on cooling. Below $A_{\text{e1}}$, no further austenite formation was considered to take place.

In order to correlate the amount of austenite forming from pearlite to thermal cycle and microstructural parameters, the values of $f_{\text{p}\rightarrow\gamma}$ at time $t_{\text{T}}$ were collected from all the simulations.

![](./images/812028889327992833_4.jpg)

Fig. 4. Typical calculated curve showing vol. fraction pearlite transformed to austenite vs. time, for $T_{\text{max}}$=750 °C, $\tau$=5.87×$10^{-4}$ s and $s_{\text{cem}}$=5 nm.

Fig. 5 depicts the variation of $f_{\text{p}\rightarrow\gamma}$ with dwell time for a specified interlamellar spacing. The various symbols depict simulation results at different maximum temperatures. Corresponding curves that best fit the results have been superimposed to the diagram. Similar diagrams were produced for all interlamellar spacings examined in the analysis. It should be made clear at this point that $f_{\text{p}\rightarrow\gamma}$=1 means that all pearlite managed to transform to austenite during the given thermal cycle. However, as regards the *total* amount of austenite in the steel, $f_{\text{p}\rightarrow\gamma}$=1 corresponds to about 78% vol. austenite, since this is the initial amount of pearlite in a Fe–0.60% C binary system.

A very interesting outcome of the simulations was that, regardless of their individual values, when heating and cooling rates, $H_{\text{C}}$ and $H_{\text{R}}$, were combined in such a way as to maintain a specific dwell time (for a given $T_{\text{max}}$), the same amount of pearlite was transformed to austenite. In other words, it was realized that dwell time was the decisive parameter, while heating and cooling rates were not so critical.

As shown in Fig. 5, the amount of dissolved pearlite increases with increasing dwell time and maximum temperature. More

<table>
<caption>Table 2 The values of microstructural features used in the simulations</caption>
<thead>
  <tr>
    <th>$\text{Fe}_{3}\text{C}$ lamella semi-thickness, $s_{\text{cem}}$ (nm)</th>
    <th>Proeutectoid ferrite region size, $s_{\text{pro},\alpha}$ ($\mu$m)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>5</td>
    <td>0.43</td>
  </tr>
  <tr>
    <td>10</td>
    <td></td>
  </tr>
  <tr>
    <td>25</td>
    <td>1.00</td>
  </tr>
  <tr>
    <td>50</td>
    <td></td>
  </tr>
</tbody>
</table>

![](./images/812028889327992833_5.jpg)

Fig. 5. Vol. fraction pearlite transformed to austenite ($f_{\text{p}\rightarrow\gamma}$) as a function of dwell time and maximum thermal cycle temperature ($s_{\text{cem}}$=25 nm).

specifically, $f_{\mathrm{p} \rightarrow \gamma}$ was correlated to dwell time by a function of the form:

$$
f_{\mathrm{p} \rightarrow \gamma}=k_{1} \cdot \tau^{n}. \tag{12}
$$

Analysis of simulation results showed that the exponent $n$ in Eq. (12) was insensitive to $T_{\max }$ and $s_{\text {cem }}$ and obtained a constant value, $n \cong 0.5$. In contrast, parameter $k_{1}$ in Eq. (12) depended strongly on $T_{\max }$, as shown in Fig. 6, which depicts the variation of $k_{1}$ with $T_{\max }$ for the values of interlamellar spacing examined in the simulations. It was found that $k_{1}$ varied linearly with $T_{\max }$:

$$
k_{1}=a_{1} \cdot T_{\max }-a_{2}. \tag{13}
$$

It should be considered here that when $T_{\max } \leq A_{\mathrm{e} 1}$, no pearlite transformation can occur even at infinitely long dwell times, i.e. $f_{\mathrm{p} \rightarrow \gamma}=0$. Therefore, from Eq. (12), at $T_{\max }=A_{\mathrm{e} 1} \Rightarrow k_{1}=0$ and subsequently Eq. (13) gives:

$$
a_{2}=a_{1} \cdot A_{\mathrm{e} 1}. \tag{14}
$$

Substituting $\alpha_{2}$ from Eq. (14), Eq. (13) becomes:

$$
k_{1}=a_{1} \cdot\left(T_{\max }-A_{\mathrm{e} 1}\right). \tag{15}
$$

Parameter $\alpha_{1}$ is the slope of the lines in Fig. 6, which clearly depends on interlamellar spacing. In Fig. 7, the variation of parameter $\alpha_{1}$ is depicted as a function of $s_{\text {cem }}$. The function that best fitted these results was of the form:

$$
a_{1}=\frac{\delta}{s_{\text {cem }}}, \tag{16}
$$

with $\delta \cong 2 \times 10^{-10}$. Finally, substituting Eqs. (15) and (16) to Eq. (12), and recalling that $n \cong 0.5$, the vol. fraction of pearlite transforming to austenite can be written as:

$$
f_{\mathrm{p} \rightarrow \gamma}=\left(T_{\max }-A_{\mathrm{e} 1}\right) \frac{\delta \sqrt{\tau}}{s_{\text {cem }}}. \tag{17}
$$

An attempt was then made to interpret the physical meaning of Eq. (17). In order to do so, the identity of parameter $\delta$ had to be clarified. By examining the dimensions of Eq. (17), since $f_{\mathrm{p} \rightarrow \gamma}$ is a dimensionless quantity (vol. fraction), then parameter $\delta$ should be a physical quantity with dimensions: length/(time $^{1 / 2} \times$ temperature). Thus, it could be considered that parameter $\delta$ is related to a characteristic diffusion coefficient and a characteristic temperature in the following way:

$$
\delta \propto \frac{\sqrt{D}}{T}. \tag{18}
$$

![](./images/812028889327992833_6.jpg)

Fig. 6. Variation of parameter $k_{1}$ in Eq. (12) with maximum temperature.

![](./images/812028889327992833_7.jpg)

Fig. 7. Variation of parameter $\alpha_{1}$ with $s_{\text {cem }}$. Parameter $\alpha_{1}$ represents the slope of the lines shown in Fig. 6.

Substituting $\delta$ from Eq. (18) to Eq. (17), the latter becomes:

$$
f_{\mathrm{p} \rightarrow \gamma}=\left(\frac{T_{\max }-A_{\mathrm{e} 1}}{T}\right) \cdot \frac{\sqrt{D \cdot \tau}}{s_{\text {cem }}}. \tag{19}
$$

The form of Eq. (19) suggests that the amount of pearlite transforming to austenite is determined by a thermodynamic term and a kinetic term. The thermodynamic term essentially represents the ratio of superheating $(T_{\max }-A_{\mathrm{e} 1})$ over a characteristic temperature $(T)$. It seems reasonable to assume that this characteristic temperature should be $A_{\mathrm{e} 1}$, which in this analysis has been considered to be the onset of austenite formation. In such case, it could be argued that the thermodynamic term actually expresses the magnitude by which the available superheating exceeds the minimum thermodynamic driving force required for the transformation.

As regards the kinetic term, the characteristic diffusion coefficient $(D)$ in Eq. (19) should be related to the diffusion process that controls the rate of transformation. Therefore, in order to examine the validity of the aforementioned concept and determine the actual diffusion coefficient entering Eq. (19), $f_{\mathrm{p} \rightarrow \gamma}$ was calculated as a function of $T_{\max }, \tau$ and $s_{\text {cem }}$ using Eq. (19) and the results were compared to the corresponding results from the simulations (i.e. the symbols in Fig. 5). Calculations using Eq. (19) were implemented by employing various different ways for determining the involved diffusion coefficient $D$:

a) The *average* diffusion coefficient of C in austenite within the temperature range $T_{\max }-A_{\mathrm{e} 1}, \bar{D}_{\gamma}$, was calculated, according to the relation:

$$
\bar{D}_{\gamma}=\frac{1}{T_{\max }-A_{\mathrm{e} 1}} \int_{A_{\mathrm{e} 1}}^{T_{\max }} D_{0} \cdot \exp \left(-\frac{Q}{R T}\right) \mathrm{d} T. \tag{20}
$$

Values for the frequency factor and the activation energy for C diffusion in fcc-Fe reported by Askeland [18] were

![](./images/812028889327992833_8.jpg)

Fig. 8. Comparison between $f_{\mathrm{p} \rightarrow \gamma}$ vs. $\tau$ results obtained by the simulations (square symbols) and by employing Eq. (19) (dashed and solid lines). Different curves correspond to different diffusion coefficients used in Eq. (19). (a) $T_{\max }=750{ }^{\circ} \mathrm{C}$, (b) $T_{\max }=800{ }^{\circ} \mathrm{C}$, (c) $T_{\max }=850{ }^{\circ} \mathrm{C}$ and (d) $T_{\max }=900{ }^{\circ} \mathrm{C}$.

adopted for calculating Eq. (20), i.e. $D_{0}=2.3 \times 10^{-5} \mathrm{~m}^{2} / \mathrm{s}$ and $Q=137700 \mathrm{~J} / \mathrm{mol}$.

b) The diffusion coefficient of $\mathrm{C}$ in austenite corresponding to the maximum temperature of the thermal cycle, $D_{\gamma}^{T_{\max }}$, was calculated, according to:

$$
D_{\gamma}^{T_{\max }}=D_{0} \cdot \exp \left(-\frac{Q}{R \cdot T_{\max }}\right). \tag{21}
$$

Once again the values $D_{0}=2.3 \times 10^{-5} \mathrm{~m}^{2} / \mathrm{s}$ and $Q=137700 \mathrm{~J} /$ mol were employed.

c) The average diffusion coefficient of $\mathrm{C}$ in ferrite (bcc-Fe) within the temperature range $T_{\max }-A_{\mathrm{el}}, \bar{D}_{\alpha}$, was calculated, according to the relation:

$$
\bar{D}_{\alpha}=\frac{1}{T_{\max }-A_{\mathrm{el}}} \int_{A_{\mathrm{el}}}^{T_{\max }} D_{0} \cdot \exp \left(-\frac{Q}{R T}\right) \mathrm{d} T, \tag{22}
$$

with $D_{0}=1.1 \times 10^{-6} \mathrm{~m}^{2} / \mathrm{s}$ and $Q=87500 \mathrm{~J} / \mathrm{mol}$ [16].

d) The diffusion coefficient of $\mathrm{C}$ in ferrite at the maximum temperature of the thermal cycle, $D_{\alpha}^{T_{\max }}$, was calculated, according to:

$$
D_{\alpha}^{T_{\max }}=D_{0} \cdot \exp \left(-\frac{Q}{R \cdot T_{\max }}\right), \tag{23}
$$

with $D_{0}=1.1 \times 10^{-6} \mathrm{~m}^{2} / \mathrm{s}$ and $Q=87500 \mathrm{~J} / \mathrm{mol}$.

e) The mean value of the average diffusion coefficients, as calculated by Eqs. (20) and (22), i.e.:

$$
\bar{D}=\frac{\bar{D}_{\gamma}+\bar{D}_{\alpha}}{2}. \tag{24}
$$

Calculated values of $f_{\mathrm{p} \rightarrow \gamma}$ as a function of dwell time using Eq. (19), calculated with each of the diffusion coefficients of Eqs. (20)-(24), are depicted by the lines in Fig. 8a-d, whereas the symbols depict the corresponding results from the simulations. It is interesting to note that the diffusion coefficient entering Eq. (19), giving results in agreement with the results of the simulations, varies with maximum thermal cycle temperature, $T_{\max }$. In Fig. 8a, which is for $T_{\max }=750{ }^{\circ} \mathrm{C}$, Eq. (19) calculates $f_{\mathrm{p} \rightarrow \gamma}$ values in good agreement with the simulation results, when the mean of the average diffusion coefficients, $(\bar{D}_{\gamma}+\bar{D}_{\alpha})/2$, is employed. In contrast, as $T_{\max }$ increases, Eq. (19) gives better results if the diffusion coefficient of $\mathrm{C}$ in austenite is employed. More specifically, Fig. $8 \mathrm{~b}-\mathrm{d}$ show that as $T_{\max }$ increases, the appropriate diffusion coefficient to be used in Eq. (19) gradually changes from $D_{\gamma}^{T_{\max }}$ to $\bar{D}_{\gamma}$. Therefore, it seems that at relatively low maximum-temperature thermal cycles (e.g. $750{ }^{\circ} \mathrm{C}$ ), pearlite dissolution is controlled by $\mathrm{C}$ diffusion in both ferrite and austenite. On the contrary, as the temperature level is increased, indicated by higher maximum-

temperature thermal cycles, the controlling process clearly becomes C diffusion in austenite. Furthermore, the gradual change from $D_{\gamma}^{T_{\max }}$ to $\bar{D}_{\gamma}$ could be attributed to that at moderate maximum temperatures (e.g. $800{ }^{\circ} \mathrm{C}$ ) the greatest portion of the "useful" part of the thermal cycle (i.e. where $A_{\mathrm{e} 1} \leq T \leq T_{\max }$ ) lies relatively close to $T_{\max }$, and thus the appropriate diffusion coefficient is close to $D_{\gamma}^{T_{\max }}$. On the other hand, at higher maximum temperatures (e.g. $850{ }^{\circ} \mathrm{C}$ and especially at $900{ }^{\circ} \mathrm{C}$ ) a great part of the "useful" thermal cycle is spent in intermediate temperatures, resulting in that $\bar{D}_{\gamma}$ seems to be the more appropriate diffusion coefficient for Eq. (19).

As a closure to the discussion regarding pearlite dissolution, it has to be recognized that the mechanism of austenite nucleation on pearlite adopted in this work is definitely not the only one and, certainly, not the most energetically favorable. It is well established that the most potent sites for austenite nucleation in pearlite-ferrite microstructures are the boundaries between different pearlite colonies, as well as the boundaries between pearlite colonies and proeutectoid ferrite grains. However, the mechanism of austenite nucleation and subsequent growth adapted in the present work displayed a series of advantages with respect to computational issues, since it provided a simpler basis for the simulation of the rapid austenitization process. Within this context, the simulation results presented above should be regarded as a lower limit for the actual extend of austenitization compared to reality. Nevertheless, the qualitative trends of austenitization revealed by the present analysis, such as the influence of thermal cycle and microstructural characteristics on the relative fraction of austenitization under rapid-heating conditions, will still be valid, even though the most energetically favorable nucleation mechanisms mentioned previously should dominate in reality.

### 4.2. Proeutectoid ferrite dissolution
In those cases, i.e. combinations of $T_{\max }, \tau$, etc., where full pearlite dissolution was achieved, simulation continued to the second stage of austenitization, which regarded the growth of high-C austenite (formed from pearlite in the first stage) in expense of proeutectoid ferrite. Fig. 9 depicts the way in which the temperature variation with time was handled in the second stage of austenitization. If it is assumed that $T_{\mathrm{d}}$ was the temperature at which full pearlite dissolution occurred during the first stage, simulation of the second stage was considered to begin at temperature $T_{\mathrm{d}}$ and continue for the remaining thermal cycle.

![](./images/812028889327992833_9.jpg)

Fig. 9. The thermal cycle during the second stage of austenitization (proeutectoid ferrite dissolution) was considered to begin at $T_{\mathrm{d}}$ (i.e. the temperature of complete pearlite dissolution) and terminate at $A_{\mathrm{e} 1}$, on cooling.

![](./images/812028889327992833_10.jpg)

Fig. 10. Typical curves showing the variation of total vol. fraction austenite in the microstructure as a function of dwell time and maximum temperature ( $s_{\mathrm{cem}}=25 \mathrm{~nm}$ and $s_{\text {pro, } \alpha}=0.43 \mu \mathrm{m}$ ).

After completion of the simulations, the values of the total vol. fraction austenite, $f_{\gamma}$, in the system were collected, and diagrams like those shown in Fig. 10 were constructed. In Fig. $10, f_{\gamma}$ is shown as a function of dwell time and maximum temperature. Symbols represent simulation results, while curves that best fit the results have been superimposed. The dashed horizontal line at $f_{\gamma}=0.78$ depicts the upper limit of austenite formed by complete pearlite dissolution, as mentioned in the previous section.

The first observation from Fig. 10 is that vol. fraction austenite seems to follow the well-known sigmoidal behaviour with respect to available transformation time, described by a Johnson-Mehl-Avrami type equation:
$$
f_{\gamma}=1-\exp \left(-k_{2} \cdot \tau^{m}\right). \tag{25}
$$

As in the case of pearlite dissolution, the exponent $m$ in Eq. (25) obtained values between 0.50 and 0.60 , not being particularly influenced by maximum temperature or microstructural parameters. In contrast, factor $k_{2}$ depended strongly on maximum temperature and to a smaller degree on microstructural features $\left(s_{\mathrm{cem}}\right.$ and $\left.s_{\mathrm{pro}, \alpha}\right)$. This can be seen in Table 3, which depicts the obtained values of coefficients $m$ and $k_{2}$ as functions of maximum thermal cycle temperature. It

Table 3
Obtained values for coefficients $m$ and $k_{2}$ as functions of maximum thermal cycle temperature

| Maximum thermal cycle temperature $\left({ }^{\circ} \mathrm{C}\right)$ | $m$    | $k_{2}$ |
| :----------------------------------------------------------------- | :----- | :------ |
| 750                                                                 | 0.600  | 4.90    |
| 800                                                                 | 0.587  | 12.30   |
| 850                                                                 | 0.525  | 14.90   |
| 900                                                                 | 0.571  | 29.80   |


should also be noted that the slope of the curves in Fig. 10 decreases rapidly above the 0.78 vol. fraction austenite, i.e. at the second stage of austenitization. This shows the large difference in the rates of transformation between the two stages.

Indeed, while pearlite dissolution takes place very rapidly, and in many cases manages to complete despite the very short transformation time available, proeutectoid ferrite dissolution proceeds at substantially lower rates. As a matter of fact, proeutectoid ferrite dissolution was completed only in a very few cases, corresponding to the longest dwell times and highest maximum temperatures employed in this study. This can certainly be attributed to the great difference in the required diffusion distances that have to be covered by C atoms in each stage. Diffusion distances in lamellar pearlite are substantially shorter, even in coarse pearlite, in comparison to proeutectoid ferrite, leading to high rates of pearlite dissolution. Another contribution to low proeutectoid ferrite dissolution rates could be due to the fact, that a great deal of the second stage takes place during the cooling part of the thermal cycle. Thus, the continuously decreasing temperature leads to decreased superheating and consequently to decreased driving force for austenitization. In addition, as temperature drops, diffusion coefficients become lower, decelerating the transformation even further.

## 5. Conclusions
In the present work the kinetics of austenite formation during rapid, non-isothermal heating conditions were studied by means of computational simulation. In particular, the austenitization of lamellar pearlite/proeutectoid ferrite microstructures was simulated by assuming that the overall process comprised of two kinetically distinct stages, i.e. pearlite dissolution followed by proeutectoid ferrite dissolution. The austenitization stages were simulated by two 1-D diffusion models employed in series. The thermal cycle undergone by the steel was assumed to consist of a linear increase of temperature up to a maximum value, followed by a linear decrease of temperature. A thermal cycle of such form can be fully described by the maximum temperature ($T_{\text{max}}$), the heating and cooling rates ($H_{\text{C}}$ and $H_{\text{R}}$) and the dwell time ($\tau$) spent above the critical $A_{\text{e1}}$ austenitization temperature. Numerical solution of the resultant moving-boundary diffusion problems provided calculated results regarding the dependency of vol. fraction austenite on thermal cycle parameters and on initial microstructural features of the steel (pearlite lamellae thickness, etc.).

The following concluding remarks can be deduced by the analysis of calculational results obtained for a Fe–0.60% C binary alloy:

i) The vol. fraction of pearlite transforming to austenite ($f_{\text{p}\rightarrow\gamma}$) during the first stage of austenitization (pearlite dissolution) was found to depend on maximum temperature, dwell time and pearlite interlamellar spacing.

ii) The individual values of heating and cooling rates were found not to have an effect on $f_{\text{p}\rightarrow\gamma}$, as long as dwell time, maximum temperature and interlamellar spacing were kept fixed.

iii) The vol. fraction of pearlite transforming to austenite was found to follow a relationship of the form:
$$
f_{\text{p}\rightarrow\gamma}=\left(\frac{T_{\text{max}}}{A_{\text{e1}}}-1\right)\cdot\frac{\sqrt{D\cdot\tau}}{s_{\text{cem}}},
$$
consisting of a thermodynamic and a kinetic term. The thermodynamic term represents the excess driving force available for austenitization. The appropriate diffusion coefficient entering the kinetic term was found to depend on the maximum temperature of the thermal cycle.

iv) The total vol. fraction austenite in the microstructure, after both stages of austenitization, was found to follow a sigmoidal kinetic behaviour, described by a relationship of the form:
$$
f_{\gamma}=1-\exp(-k_{2}\cdot\tau^{m}).
$$

v) For the range of values of the thermal cycle and microstructural parameters employed in the calculations, the exponent in the above equation obtained values in the range $m\cong0.5$–0.6, whereas $k_{2}$ depended strongly on maximum thermal cycle temperature.

## Acknowledgments
The present research has been supported by the Hellenic Ministry of National Education and Religious Affairs, through the EPEAEK II/PYTHAGORAS II programme.

## References
[1] R.R. Judd, H.W. Paxton, Trans. TMS–AIME 242 (1968) 206.
[2] G.R. Speich, A. Szirmae, Trans. TMS–AIME 245 (1969) 1063.
[3] N.C. Law, D.V. Edmonds, Metall. Trans., A, Phys. Metall. Mater. Sci. 11A (1980) 33.
[4] C.I. Garcia, A.J. Deardo, Metall. Trans., A, Phys. Metall. Mater. Sci. 12A (1981) 521.
[5] J.I. Kim, J.W. Morris Jr., Metall. Trans., A, Phys. Metall. Mater. Sci. 12A (1981) 1957.
[6] G.R. Speich, V.A. Demarest, R.L. Miller, Metall. Trans., A, Phys. Metall. Mater. Sci. 12A (1981) 1419.
[7] J.R. Bradley, S. Kim, Metall. Trans., A, Phys. Metall. Mater. Sci. 19A (1988) 2013.
[8] O.A. Sandven, in: ASM International (Eds.), ASM Handbook, Vol. 4 – Heat Treating, Materials Park (OH), 1991, pp. 286–296.
[9] K.J. Albutt, S. Garber, J.I.S.I. 204 (1966) 1217.
[10] S.-J. Na, Y.-S. Yang, Surf. Coat. Technol. 34 (1988) 319.
[11] A. Jacot, M. Rappaz, Acta Mater. 45 (1997) 575.
[12] E. Ohmura, K. Inoue, Y. Takamachi, JSME Int. J. 34 (1991) 421.
[13] J. Ågren, Scand. J. Metal. 19 (1990) 2.
[14] G. Inden, P. Neumann, Steel Res. 67 (1996) 401.
[15] A. Engstrom, L. Hoglund, J. Ågren, Metall. Mater. Trans., A Phys. Metall. Mater. Sci. 25A (1994) 1127.
[16] J. Ågren, J. Phys. Chem. Solids 43 (1982) 385.
[17] J. Ågren, I.S.I.J. Int. 32 (1992) 291.
[18] D.R. Askeland, The Science and Engineering of Materials, third ed. Chapman & Hall, London, UK, 1996.