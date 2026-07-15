# A Process Model for the Microstructure Evolution in Ductile Cast Iron: Part II. Applications of the Model

M.I. ONSØIEN, Ø. GRONG, Ø. GUNDERSEN, and T. SKALAND

In the present investigation, the process model developed in Part I has been implemented in a dedicated numerical code to reveal the evolution of the coupled thermal and microstructural fields during directional solidification of ductile iron. In a calibrated form, the model predicts adequately both the variation in the graphite nodule count and the resulting microstructural profiles (i.e., graphite, iron carbide, ferrite, and pearlite) in the length direction of the bar. At the same time, the model has the required flexibility to serve as a research tool and predict behavior under conditions that have not yet been explored experimentally. In this article, the aptness of the model to alloy design and optimization of melt treatment practice for ductile iron is illustrated in different case studies and numerical examples.

## I. INTRODUCTION

CASTINGS are prime examples of components where the properties achieved depend on the characteristics of the microstructure. $^{[1,2]}$ When viewed from the sideline, the field

seems to have reached a level where most of the under- lying physical mechanisms are well established. At the same time, the recent advances in computer technology and numerical methods have made it possible to rationalize mi- crostructural evolution and transport phenomena in terms of models based on the fundamental equations for energy, mass, and momentum conservation. $^{[3,4]}$ A synthesis of that knowledge has, in turn, been consolidated into various kinds of deterministic models to predict the as-cast micro- structure. $^{[5-14]}$ The main idea here is to divide the compu tational space into a series of interconnected volume elements, each of them acting as an open system with re- spect to heat transfer but being autonomous when it comes to microstructural evolution.

The process model developed in Part I of this investi- gation $^{[14]}$ is based on the same philosophy and combines information about the phase relations within the Fe-C sys- tem with kinetic data to describe the microstructural evo- lution in ductile cast iron. The reactions considered are the graphite/austenite eutectic transformation and the ledeburite eutectic transformation during solidification, the subsequent growth of the graphite phase in the austenite regime, and finally the decomposition of austenite into ferrite and pearl- ite during the eutectoid transformation. In this part of the investigation, the microstructural model will be linked to a well-proven experimental technique for assessment of in- oculant performance in ductile cast iron (here, directional solidification). As a starting point, the model will be applied to the reference iron described in Part $I^{[14]}$ and validated by comparison with experimental microstructural data. Sub- sequently, its potential for optimization of melt treatment practice and casting conditions for ductile iron will be il- lustrated in different numerical examples and case studies.

## II. TOOLBOX FOR SIMULATION OF MICROSTRUCTURAL EVOLUTION

The symbols and units used throughout the article are defined in the Nomeclature.

In the present investigation, a special MATLAB* tool- box has been developed to simulate the microstructural ev- olution during directional solidification of ductile iron. The toolbox consists of a numerical heat flow model and a series of microstructural models that are coupled.

*MATLAB is a trademark of The MathWorks, Inc., Natick, MA

### A. Heat Flow Model

Calculation of the temperature-time pattern in different positions along the bar is done by solving the differential heat flow equation for the appropriate boundary conditions:

$$
\frac{\partial T}{\partial t}=\frac{1}{\rho c} \frac{\partial}{\partial x}\left(\lambda \frac{\partial T}{\partial x}\right)+\frac{L}{\rho c} \frac{\partial f}{\partial t} \tag{1}
$$

where $\lambda$ is the thermal conductivity, $\rho c$ is the volume heat capacity, $L$ is the latent heat of transformation, and $f$ is the volume fraction of the transformation product.

The solution is based on the finite difference approach, where a coupled set of ordinary differential equations is derived by integrating Eq. [1] over a representative control volume. $^{[15]}$ Heat loss to the water-cooled copper chill is al lowed for by the use of a heat transfer coefficient $h$. In the MATLAB toolbox, $h$, $\lambda$, and $\rho c$ are defined as global var- iables, which means that the inherent temperature depend- ence of these parameters can readily be implemented in the model.

### B. Microstructural Models

Following the treatment in Part I, $^{[14]}$ the microstructural evolution in ductile cast iron is captured mathematically in

---
M.I. ONSØIEN and Ø. GUNDERSEN, Research Metallurgists, are with SINTEF Materials Technology, N-7034 Trondheim, Norway. Ø. GRONG, Professor, is with the Department of Metallurgy, Norwegian University of Science and Technology, N-7034 Trondheim, Norway. T. SKALAND, Research Metallurgist, is with Elkem a/s Research, N-4602 Kristiansand, Norway.

Manuscript submitted October 20, 1997.

---
METALLURGICAL AND MATERIALS TRANSACTIONS A
VOLUME 30A, APRIL 1999—1069

![](./images/812002745694289920_1.jpg)

Fig. 1—Flow chart for the MATLAB toolbox.

terms of differential variation of four primary state variables with time, each representing a specific phase transformation. For the sake of simplicity, no consideration is given to segregation of alloying elements during solidification, which will be dealt with in a separate communication. According to this formalism, the parameters $\Phi$ and $X$ refer to the graphite/austenite eutectic transformation and the ledeburite eutectic transformation during solidification, respectively; $Y$ denotes the subsequent growth of the graphite phase in the austenite regime; and $Z$ describes the decomposition of the austenite phase into ferrite and pearlite during the eutectoid transformation. Thus, the state variables $T$, $\Phi$, $X$, $Y$, and $Z$ uniquely define the microstructural state of the iron, and can be used as a basis for calculating the volume fraction of constituent phases in each regime via separate response equations.

The toolbox consists of several files, i.e., a main program for integration of the differential equations and separate subroutines for the input parameters, the derivatives, the time constants, and the response equations. Moreover, special postprocessing routines have been developed to facilitate both two-dimensional (2-D) and three-dimensional (3-D) graphical visualization of the output data. Figure 1 shows a simplified flow chart for the MATLAB toolbox (further details are given in Reference 16).

### C. Inputs and Outputs

In a calibrated form, the model allows prediction of the microstructural evolution under conditions that have not yet been explored experimentally. The primary model inputs are the initial melt temperature and the alloy composition, from which the fading potential, the nodule count, and the equilibrium temperatures for the stable (gray) and the metastable (white) eutectics can be evaluated. In addition, changes in the nucleating conditions during solidification can be allowed for through adjustment of the graphite nucleation temperature $T_{n,s}$. This parameter is a measure of the potency of the heterogeneous nucleation sites with respect to graphite formation, which, in turn, reflects the type of nonmetallic inclusions present in the melt after the refining and inoculation stage. $^{[14,17]}$ The outputs of the model are the temperature-time pattern and microstructure profiles in the length direction of the bar. These data can be presented in the form of 2-D or 3-D process diagrams to illustrate both separate and combined effects of various input parameters on the resulting microstructural evolution.

## III. EXPERIMENTAL VERIFICATION OF THE MODEL

Because the process model contains a number of poorly known constants, a means for calibrating the constants to experimental data is required. As shown in Part I, $^{[14]}$ this is achieved using a chosen reference iron and measurable microstructural quantities to determine the numerical values of state variables at fixed positions along the bar. Similar data extracted from other positions can then be used to check the predictive power of the model under different cooling conditions.

<table><thead><tr><th>Element</th><th>C</th><th>Si</th><th>Mn</th><th>S</th><th>P</th><th>Mg</th><th>Ti</th><th>Al</th><th>Pb</th></tr></thead><tbody><tr><td>Value</td><td>3.51</td><td>2.13</td><td><0.03</td><td>0.007</td><td>0.025</td><td>0.042</td><td>0.016</td><td>0.014</td><td><0.006</td></tr></tbody></table>

### A. Casting Procedure
The reference iron is produced from high purity pig iron, using a conventional magnesium-containing FeSi treatment alloy and inoculant. Directional solidification is carried out by pouring the superheated liquid metal into a 40-mm diameter and 140-mm-long insulated mold made of aluminosilicate fibers, which is cooled from the bottom by means of a water-cooled copper chill. Thermocouples are placed at fixed positions from the chilled end to register the temperature-time pattern during cooling. A full description of the casting procedure has been reported elsewhere.[¹⁸]

### B. Chemical and Metallographic Examinations
The concentrations of carbon, sulfur, and magnesium were analyzed on samples extracted 55 mm from the cooled end of the bar, while the remaining elements were obtained from quenched coin samples extracted from the melt prior to the casting operation. Characterization of the as-cast microstructure was performed in the cross section at different positions from the cooled end of the bar, according to the procedure described in Reference 18. After polishing to 1-µm diamond paste finish, the metallographic samples were etched in a 2 vol pct nital solution. Quantification of the different microconstituents was done by means of point counting in a light microscope (minimum 1000 points at a magnification of 200 times). Optical metallographic techniques were also employed to determine the extension of the iron carbide zone in the longitudinal direction of the bar following etching in an ammonium persulfate solution. Table I and II contain a summary of composition and microstructural data.

### C. Thermal Field
In general, the temperature-time pattern during directional solidification of cast iron is the result of the interplay between a number of variables that cannot readily be accounted for by means of classic heat conduction theory. For example, at temperatures above the melting point, a large contribution from convective heat flow is to be expected due to the high velocity fields set up within the liquid metal. Instead of seeking a complex numerical solution to this problem based on first principles, a more pragmatic approach would be to simulate convective heat flow by adjusting the value of the thermal conductivity in the liquid until a good agreement is obtained between predictions and experiments, as done in the present investigation. There is a well-accepted precedence for this in the scientific literature, but the drawback is that the calibrated value of $\lambda$ cannot be extended to other experimental conditions than those examined here. A similar type of approach can also be applied to determine the heat transfer coefficient $h$ between the water-cooled copper chill and the cooled end of the bar. Referring to Figure 2, the inherent variation in the heat transfer coefficient with temperature is allowed for by relating $h$ to the phase changes occurring during cooling of the outer volume element, which alter the cooling conditions by contributing to the formation of an air gap between the copper chill and the casting.[¹⁸] Table III contains a summary of all input data used in the numerical heat flow model.

Figure 3 shows a comparison between measured and predicted cooling curves for three different positions along the bar after these adjustments. If follows that the expected variation in the temperature-time pattern with position is readily captured by the model, although the calculated cooling curves are slightly shifted toward longer times in the diagram due to a steep thermal gradient in the length direction of the bar. However, the practical significance of this discrepancy is rather small, since it will just lead to a minor displacement of the predicted microstructural profiles in the length direction. The heat flow model is therefore accurate enough to justify calculations of the thermal field in the reference casting, and an illustration of this is given in Figure 4.

### D. Microstructural Fields
The microstructure model consists of five different submodels that are coupled in series, where outputs from one are used as inputs in the next one.

The fading model presented in Part I[¹⁴] predicts that the spatial graphite nodule count in the reference iron $N$ scales with the number density of nonmetallic inclusions present in the melt after the refining and inoculation stage. In the context of directional solidification, this essentially means that $N$ should fall from its initial value $N_r$, according to the following relationship:[¹⁴,²²]

$$
\frac{N}{N_{r}}=\left(\frac{d_{0}}{d}\right)^{3} \tag{2}
$$

where $d_0$ is the inclusion diameter close to the chilled end of the bar ($d$ denotes the inclusion diameter in an arbitrary position).

Figure 5(a) shows a plot of the variation in the inclusion diameter with position in the reference casting as calculated from the fading model, while the resulting change in the nodule count is given in Figure 5(b). It follows that the observed decrease in the graphite nodule count with position is readily captured by the model. An exception is the 10-mm position, where the predicted nodule count is seen to be higher than that observed experimentally. This discrepancy arises probably from the use of a lower threshold for the nodule diameter in the measurements, which tends to discriminate a higher proportion of small particles close to the chilled end of the bar compared with the other positions because of a finer nodule size.

In the model, the state variables $\Phi$, $X$, $Y$, and $Z$ define the microstructural state of the iron at a given temperature. Figure 6 shows graphical representations of the evolution of the state variables with time and position in the reference casting, as calculated from the model. Moreover, by utilizing the constraints provided by the phase diagram, the terminal values of the state variables can be converted into equivalent volume fractions of constituent phases at the end

<table>
<caption>Table II. Summary of Microstructural Data for Reference Iron (Symbols and Abbreviations are Defined in the Nomenclature)</caption>
<thead>
<tr>
<th>$l$
(mm)</th>
<th>$G$
(Vol Pct)</th>
<th>$F$
(Vol Pct)</th>
<th>$P$
(Vol Pct)</th>
<th>$C^{*}$
(Vol Pct)</th>
<th>$N_{A}$
No./mm²</th>
<th>$D_{A}$
($\mu$m)</th>
<th>$N_{V}^{**}$
No./mm³</th>
<th>$N/N_{r}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>10</td>
<td>11.4</td>
<td>44.2</td>
<td>16.2</td>
<td>28.2</td>
<td>172</td>
<td>17.5</td>
<td>9102</td>
<td>0.57</td>
</tr>
<tr>
<td>15</td>
<td>11.7</td>
<td>69.2</td>
<td>13.3</td>
<td>5.8</td>
<td>292</td>
<td>21.3</td>
<td>12696</td>
<td>0.80</td>
</tr>
<tr>
<td>35</td>
<td>10.3</td>
<td>62.8</td>
<td>26.9</td>
<td>0</td>
<td>227</td>
<td>26.0</td>
<td>8086</td>
<td>0.51</td>
</tr>
<tr>
<td>55</td>
<td>12.3</td>
<td>55.0</td>
<td>32.7</td>
<td>0</td>
<td>152</td>
<td>27.7</td>
<td>5082</td>
<td>0.32</td>
</tr>
<tr>
<td>95</td>
<td>10.5</td>
<td>47.2</td>
<td>42.3</td>
<td>0</td>
<td>99</td>
<td>23.4</td>
<td>3918</td>
<td>0.24</td>
</tr>
</tbody>
<tfoot>
<tr>
<td colspan="9">*Width of iron carbide zone: 30 mm.</td>
</tr>
<tr>
<td colspan="9">**Estimated from 2-D microstructural data.</td>
</tr>
</tfoot>
</table>

![](./images/812002745694289920_2.jpg)

Fig. 2—Schematic diagram illustrating how variations in the heat transfer coefficient $h$ are inter-related to the phase changes occurring during solidification and subsequent cooling in the solid state.

of each regime via separate response equations. This point is more clearly illustrated in Figure 7, which shows a comparison between measured and predicted volume fractions of graphite, ferrite, pearlite, and iron carbide in the reference casting after the eutectoid transformation. A closer inspection of the graphs reveals that the model, with a few exceptions, is capable of reproducing the measured microstructural profiles in the length direction of the bar. The poor agreement observed close to the cooled end of the bar is probably due to the fact that the model neglects a consideration of segregation of silicon during solidification, which leads to an underestimation of the formation of iron carbide at high cooling rates. More interesting, however, is that the model correctly predicts the unexpected fluctuations in the ferrite and pearlite contents. It will be shown subsequently that these fluctuations can mainly be attributed to an overall reduction in the graphite nodule count with position due to fading effects (Figure 5), which alters the kinetics of the subsequent solid-state transformations.

## IV. CASE STUDIES

In Sections A through D, the important features of the process model and its aptness to alloy design and optimization of melt treatment practice for ductile cast iron will be illustrated in various case studies and numerical examples.

### 4. Effects of Base Iron Composition

In addition to carbon, the important alloying elements in ductile cast iron are silicon and manganese. Silicon is a ferrite stabilizer, and addition of this element will thus promote the ferrite formation by raising the equilibrium temperatures of the eutectic and eutectoid transformations.[²³] Figure 8 shows how variations in the silicon content influence the microstructural evolution. As expected, a high silicon level will slightly suppress the iron carbide formation and increase the ferrite content, while the opposite is observed for the low Si (reference) iron. These results are interesting both from an academic and a practical point of view, since they illustrate in a quantitative manner how a shift in the stable and metastable phase boundaries alters the kinetics of the subsequent transformation reactions.

In contrast to silicon, manganese is an austenite stabilizer that affects the solid-state transformation behavior mainly by reducing the growth rate of unpartitioned proeutectoid ferrite (Figure 9). Addition of manganese to ductile cast iron will therefore retard the decomposition of austenite to graphite and ferrite, and thus indirectly promote the pearlite formation. Within the framework of the present process model, this change in the growth kinetics can be simulated by adjusting the value of the time constant $t_{r_{4}}$ for the eutectoid transformation. Based on the parabolic growth law, we may write

$$
t_{r_{4}}(s)=\left(\frac{\varepsilon_{r}}{\varepsilon}\right)^{2} 4.5 \tag{3}
$$

where $\varepsilon_{r}$ and $\varepsilon$ denote the parabolic thickening constant for the reference and the actual alloy, respectively.

By using data from Figure 9, it is easy to verify that an increase in the manganese content from essentially zero in the reference iron to, say, 0.25 and 0.50 wt pct increases the value of $t_{r_{4}}$ from initially 4.5 to 10 and 20 seconds, respectively. This change in the time constant for the eutectoid transformation will have a dramatic effect on the resulting ferrite/pearlite balance in the iron, as shown in Figure 10, because of the reduced ferrite growth rate. Consequently, in real castings, where a low pearlite content is aimed at in the finished product, an upper limit for the manganese level is usually specified, depending on the section size and the type of application.[²]

### B. Effects of Melt Treatment Practice

There is considerable circumstantial evidence available in the scientific literature that the conditions for graphite

<table>
<caption>Table III. Summary of Input Data Used in Numerical Heat Flow Model; the Data are Collected from Miscellaneous Sources<sup>[10,11,19–21]</sup> (Symbols and Abbreviations are Defined in the Nomenclature)</caption>
<tr>
<td colspan="2">Heat Transfer Coefficients*</td>
<td colspan="2">Thermal Properties</td>
</tr>
<tr>
<td colspan="2">
$h_{1a} = 1200$ J s<sup>−1</sup> m<sup>−2</sup> K<sup>−1</sup>
<br>$h_{1b} = 1000$ J s<sup>−1</sup> m<sup>−2</sup> K<sup>−1</sup>
<br>$h_{2a} = 800$ J s<sup>−1</sup> m<sup>−2</sup> K<sup>−1</sup>
<br>$h_{2b} = 400$ J s<sup>−1</sup> m<sup>−2</sup> K<sup>−1</sup>
</td>
<td>liquid iron
<br>$\lambda^* = 200$ J s<sup>−1</sup> m<sup>−1</sup> K<sup>−1</sup>
<br>$\rho c = 6.125 \times 10^6$ J m<sup>−3</sup> K<sup>−1</sup>
<br>$L_1 = 1.23 \times 10^9$ J m<sup>−3</sup>
<br>$L_2 = 1.0 \times 10^9$ J m<sup>−3</sup>
</td>
<td>solid iron
<br>$\lambda = 35$ J s<sup>−1</sup> m<sup>−1</sup> K<sup>−1</sup>
<br>$\rho c = 6.110 \times 10^6$ J m<sup>−3</sup> K<sup>−1</sup>
<br>$L_3 = 1.53 \times 10^8$ J m<sup>−3</sup>
</td>
</tr>
<tr>
<td colspan="4">*Calibrated values</td>
</tr>
</table>

![](./images/812002745694289920_3.jpg)

Fig. 3—Comparison between measured and predicted cooling curves at three different positions along the bar.

![](./images/812002745694289920_4.jpg)

Fig. 4—3-D graphical representation of the thermal field in the reference casting, as predicted from the numerical heat flow model.

![](./images/812002745694289920_5.jpg)

![](./images/812002745694289920_6.jpg)

Fig. 5—Experimental verification of fading model: (a) predicted variation in inclusion size with position in reference iron and (b) resulting change in the graphite nodule count. Data from Table II.

formation during solidification can be significantly improved by raising the level of sulfur and oxygen in the melt.<sup>[26,27,28]</sup> This is because the number density of inclusions that may act as heterogeneous nucleation sites for graphite is directly proportional to the concentration of the impurity elements. Figure 11 shows how variations in the sulfur and oxygen contents influence the microstructure evolution. It is evident that the concept of inclusion-stimulated graphite nucleation offers great opportunities for improved inoculation performance, provided that the impurity level in the iron can be controlled. Attempts are currently being made to explore this possibility experimentally to find the best technical solution for the addition of sulfur and oxygen via the treatment alloys.

Addition of rare earth metals (REM) such as cerium and lanthanum is another way of changing the nucleation conditions for graphite during solidification by virtue of their ability to modify the chemistry of the inclusions.<sup>[17,29–31]</sup> In

![](./images/812002745694289920_7.jpg)

Fig. 6—Diagrams showing the evolution of the primary state variables with time at different positions along the bar (from left: 2, 10, 15, 35, 55, 95, and 130 mm): (a) the graphite/austenite eutectic transformation, (b) the Ledeburite eutectic transformation, (c) graphite growth in the austenite regime, and (d) the eutectoid transformation.

both cases, the nodule count is seen to pass through a max- imum when the concentration of these elements in the iron is progressively increased. Referring to Figure 12, the initial increase in the nodule count can be explained by a gradual decrease in the nucleation potency of the primary (type A) inclusions, which makes graphite formation at other (type B) inclusions feasible.[¹⁷] However, in the presence of ex- cess amounts of Ce or La, the primary inclusions become completely inactive, leading to selective nucleation of graphite nodules at type B inclusions. In the process model, the important effects of cerium and lanthanum on the re- sulting microstructure evolution in ductile cast iron can be simulated by manipulating the input values for the graphite nucleation temperature $T_{n,s}$ and the initial inclusion number density $n/n_{r}$. Figure 13 shows examples of calculated mi- crostructural profiles after the eutectoid transformation. It is evident that the reported changes in the as-cast micro- structure with increasing Ce and La additions are readily reflected in the simulations.[¹⁷] In particular, the increased tendency to chill formation for the combination of a low graphite nucleation temperature (i.e., high undercooling) and a low inclusion number density is obvious from these data.

### C. Fading of Inoculation
It is a general observation that the potential for graphite formation during solidification tends to diminish as the time interval between inoculation and casting increases,[²·²²] a process frequently referred to as fading. As previously stated, the model adopted here is based on the assumption that nucleation of graphite occurs epitaxially on small (sub- microscopic) inclusions that are entrapped in the liquid after the magnesium treatment and activated by elements sup- plied through the inoculant.[²²·³²] Fading will then occur as a result of a general coarsening of the inclusion population with time.

Figure 14 shows how fading affects the microstructural evolution in ductile cast iron during directional solidifica- tion. If the fading model is fully decoupled from the mi- crostructural model (i.e., inclusion coarsening is excluded), the as-cast microstructure outside the chill zone tends to

![](./images/812002745694289920_8.jpg)

Fig. 7—Comparison between predicted and measured microstructural profiles in the length direction of the bar: (a) the graphite and iron carbide profiles and (b) the ferrite and pearlite profiles. Data from Table II.

stabilize and approach a constant level in the length direction of the bar. In contrast, an increased inclusion coarsening rate will accelerate the fading process, which, in turn, alters the kinetics of the subsequent solid-state transformations (both the graphite/iron carbide and the pearlite/ferrite balance). Although the origin of the fading phenomenon is reasonably well understood, these results highlight the severity of the problem during casting and show the potential for developing new and improved inoculants for ductile iron in the future.

### D. Future Work
It is believed that the modeling approach described here may be applied to a wide range of solidification problems involving use of inoculants for microstructure refinement, ranging from aluminum alloys to ductile cast iron. $^{[33,34]}$ However, to improve the confidence in the model predictions, it is always necessary to calibrate the evolution equations against experimental cooling curves and microstructural data. This type of information is best derived utilizing well-proven laboratory tests such as thermal analysis or directional solidification, where the heat flow

![](./images/812002745694289920_9.jpg)

Fig. 8—Results from numerical simulations showing how variations in the base iron silicon content affect the as-cast microstructure: (a) the graphite and iron carbide profiles and (b) the ferrite and pearlite profiles. Solid curves refer to reference iron with 2.13 wt pct Si.

![](./images/812002745694289920_10.jpg)

Fig. 9—Effect of manganese on the parabolic thickening constant $\varepsilon$ of unpartitioned proeutectoid ferrite at about 730 °C. Data from Refs. 24 and 25.

METALLURGICAL AND MATERIALS TRANSACTIONS A

VOLUME 30A, APRIL 1999—1075

![](./images/812002745694289920_11.jpg)

Fig. 10—Results from numerical simulations showing how variations in the base iron manganese content affect the eutectoid transformation: (a) the ferrite profile and (b) the pearlite profile. Solid curves refer to reference iron with less than 0.03 wt pct Mn.

problem is simple enough to be handled by means of process modeling techniques. The next step is to implement the complete process model outlined in Part I.[¹⁴] (including the microsegregation option) in a dedicated finite element code describing complex 3-D heat flow in real castings. This work is currently in progress.

## V. CONCLUSIONS

In the present investigation, a special MATLAB toolbox has been developed to simulate the microstructural evolution during directional solidification of ductile iron, based on the methodology presented in Part I.[¹⁴] The toolbox consists of a numerical heat flow model and a series of microstructural models that are coupled.

The solution for the thermal field is based on the finite difference approach, where a coupled set of ordinary differential equations is derived by integrating the heat flow equation over a representative control volume. A comparison between predicted and measured cooling curves shows that the numerical heat flow model is accurate enough to justify calculations of the thermal field in the casting, provided that the temperature dependence of the thermal conductivity and the heat transfer coefficient is adequately accounted for in the simulations.

![](./images/812002745694289920_12.jpg)

Fig. 11—Results from numerical simulations showing how variations in the base iron impurity level affect the as-cast microstructure: (a) the graphite and iron carbide profiles and (b) the ferrite and pearlite profiles. Solid curves refer to reference iron with [pct O + pct S] = 70 ppm.

The microstructural model consists of five different submodels that are coupled in series, where outputs from one are used as inputs in the next one. In a calibrated form, the model predicts adequately both the variation in the graphite nodule count and the resulting microstructural profiles (i.e., graphite, iron carbide, ferrite, and pearlite) in the length direction of the bar.

Because the process model is based on sound physical principles, it can also be used as a research tool to predict behavior under conditions that have not yet been explored experimentally. The areas of application are alloy design and optimization of melt treatment practice, where both separate and combined effects of different input parameters on the microstructural evolution can be simulated in a quantitative manner.

## ACKNOWLEDGMENTS

The authors acknowledge the financial support from Elkem as, Bjølvefossen ASA, Fesil AS, and the Norwegian

![](./images/812002745694289920_13.jpg)

Fig. 12—Schematic representation of the mechanism of graphite formation in ductile iron containing cerium and lanthanum: (a) nucleation conditions during solidification and (b) resulting change in nodule count with increasing Ce and La levels.¹⁷¹

![](./images/812002745694289920_14.jpg)

Fig. 13—Results from numerical simulations showing how variations in the base iron Ce or La level affect the as-cast microstructure: (a) the graphite and iron carbide profiles and (b) the ferrite and pearlite profiles. Solid curves refer to reference iron with $T_{n,s}=1160\ ^{\circ}\text{C}$ and $n/n_{r}=1$.

Research Council through grants provided by the Norwe- gian Ferroalloy Research Organization (FFF).

### NOMENCLATURE

<table>
<tr>
<td>$C$</td>
<td>volume fraction of carbide</td>
<td>$k_{1}$</td>
<td>kinetic constant in fading model ($\text{m}^{3}\ \text{s}^{-1}$)</td>
</tr>
<tr>
<td>$d$</td>
<td>inclusion diameter (m)</td>
<td>$l$</td>
<td>position in bar referred to chilled end (m)</td>
</tr>
<tr>
<td>$d_{0}$</td>
<td>initial inclusion diameter (m)</td>
<td>$L$</td>
<td>latent heat of transformation ($\text{J}\ \text{m}^{-3}$)</td>
</tr>
<tr>
<td>$D_{A}$</td>
<td>2-D diameter of graphite nodule (m)</td>
<td>$L_{1}$</td>
<td>latent heat released during the graphite/austenite eutectic transformation ($\text{J}\ \text{m}^{-3}$)</td>
</tr>
<tr>
<td>$f$</td>
<td>volume fraction of an arbitrary transformation product</td>
<td>$L_{2}$</td>
<td>latent heat released during the ledeburite eutectic transformation ($\text{J}\ \text{m}^{-3}$)</td>
</tr>
<tr>
<td>$F$</td>
<td>volume fraction of ferrite</td>
<td>$L_{3}$</td>
<td>latent heat released during the eutectoid transformation ($\text{J}\ \text{m}^{-3}$)</td>
</tr>
<tr>
<td>$G$</td>
<td>volume fraction of graphite</td>
<td>$n$</td>
<td>number of inclusions per unit volume (no. $\text{m}^{-3}$)</td>
</tr>
<tr>
<td>$h$</td>
<td>heat transfer coefficient ($\text{J}\ \text{s}^{-1}\ \text{m}^{-2}\ \text{K}^{-1}$)</td>
<td>$n_{r}$</td>
<td>number of inclusions per unit volume in reference alloy (no. $\text{m}^{-3}$)</td>
</tr>
<tr>
<td>$h_{1a}$</td>
<td>initial heat transfer coefficient in liquid regime ($\text{J}\ \text{s}^{-1}\ \text{m}^{-2}\ \text{K}^{-1}$)</td>
<td>$N$</td>
<td>number of graphite nodules per unit volume (no. $\text{m}^{-3}$)</td>
</tr>
<tr>
<td>$h_{1b}$</td>
<td>initial heat transfer coefficient during solidification ($\text{J}\ \text{s}^{-1}\ \text{m}^{-2}\ \text{K}^{-1}$)</td>
<td>$N_{r}$</td>
<td>number of graphite nodules per unit volume in reference alloy (no. $\text{m}^{-3}$)</td>
</tr>
<tr>
<td>$h_{2a}$</td>
<td>heat transfer coefficient in austenite regime ($\text{J}\ \text{s}^{-1}\ \text{m}^{-2}\ \text{K}^{-1}$)</td>
<td>$N_{A}$</td>
<td>number of graphite nodules per unit area (no. $\text{m}^{-2}$)</td>
</tr>
<tr>
<td>$h_{2b}$</td>
<td>heat transfer coefficient in postectectoid regime ($\text{J}\ \text{s}^{-1}\ \text{m}^{-2}\ \text{K}^{-1}$)</td>
<td>$N_{V}$</td>
<td>number of graphite nodules per unit volume (no. $\text{m}^{-3}$)</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$P$</td>
<td>volume fraction of pearlite</td>
</tr>
</table>

METALLURGICAL AND MATERIALS TRANSACTIONS A

VOLUME 30A, APRIL 1999—1077

![](./images/812002745694289920_15.jpg)

Fig. 14—Results from numerical simulations showing how the rate of inclusion coarsening (i.e., fading) affects the as-cast microstructure: (a) the graphite and iron carbide profiles and (b) the ferrite and pearlite profiles. Solid curves refer to reference iron with coarsening constant $k_{\mathrm{i}}$ = 0.011 $\mathrm{\mu m^{3}\ s^{-1}}$.

| $t$ | time(s) |
|-----|---------|
| $t_{1}^{*}$ | time constant in microstructural model (s) |
| $t_{f}$ | total computation time (s) |
| $t_{r,4}$ | reference time in kinetic model for the eutectoid transformation (s) |
| $T$ | temperature ($^\circ$C or K) |
| $T_{e,m}$ | eutectic temperature in metastable system ($^\circ$C or K) |
| $T_{e,s}$ | eutectic temperature in stable system ($^\circ$C or K) |
| $T_{n,s}$ | graphite nucleation temperature ($^\circ$C or K) |
| $T_{n,A}$ | temperature for nucleation of graphite on type A inclusions ($^\circ$C or K) |
| $T_{n,B}$ | temperature for nucleation of graphite on type B inclusions ($^\circ$C or K) |
| $X$ | state variable referring to the ledeburite eutectic transformation |
| $Y$ | state variable describing graphite growth in austenite regime |
| $Z$ | state variable referring to the eutectoid transformation |
| $\Phi$ | state variable referring to the graphite/austenite eutectic transformation |
| $\varepsilon$ | parabolic thickening constant (m $\mathrm{s^{-1/2}}$) |
| $\varepsilon_{r}$ | parabolic thickening constant in reference alloy (m $\mathrm{s^{-1/2}}$) |
| $\lambda$ | thermal conductivity (J $\mathrm{s^{-1}\ m^{-1}\ K^{-1}}$) |
| $\rho c$ | volume heat capacity (J $\mathrm{K^{-1}\ m^{-3}}$) |

## REFERENCES

1. I. Minkoff: *The Physical Metallurgy of Cast Iron*, John Wiley & Sons Ltd., New York, NY, 1983.
2. R. Elliott: *Cast Iron Technology*, Butterworth and Co., London, 1988.
3. M. Rappaz: *Int. Mater. Rev.*, 1989, vol. 34, pp. 93-123.
4. D.M. Stefanescu: *Iron Steel Inst. Jpn. Int.*, 1995, vol. 35, pp. 637-50.
5. D. Venugopalan: *Metall. Trans. A*, 1990, vol. 21A, pp. 913-18.
6. A. Almansour, K. Matsugi, T. Hatayama, and O. Yanagisawa: *Mater. Trans., JIM*, 1996, vol. 37, pp. 612-19.
7. A. Almansour, K. Matsugi, T. Hatayama, and O. Yanagisawa: *Mater. Trans., JIM*, 1995, vol. 36, pp. 1487-95.
8. L. Nastac and D.M. Stefanescu: *AFS Trans.*, 1995, vol. 103, pp. 329-37.
9. R. Mai, B. Leube, and E. Schüle: *Giessereiforschung*, 1995, vol. 47, pp. 1-5.
10. Q. Chen, E.W. Langer, and P.N. Hansen: *Scand. J. Metall.*, 1995, vol. 24, pp. 48-62.
11. S. Chang, D. Shangguan, and D.M. Stefanescu: *Metall. Trans. A*, 1992, vol. 23A, pp. 1333-46.
12. E. Fras, W. Kapturkiewicz, and H.F. Lopez: *AFS Trans.*, 1992, vol. 100, pp. 583-91.
13. G. Upadhya, D.K. Banerjee, D.M. Stefanescu, and J.L. Hill: *AFS Trans.*, 1990, vol. 98, pp. 699-706.
14. M.I. Onsøien, Ø. Grong, Ø. Gundersen, and T. Skaland: *Metall. Mater. Trans. A*, 1999, vol. 30A, pp. 1053-68.
15. S.V. Patankar: *Numerical Heat Transfer and Fluid Flow*, Hemisphere Publ. Co., Washington, DC, 1980.
16. Ø. Gundersen and M.I. Onsøien: "MATLAB Simulator for Directional Solidification of Ductile Iron," SINTEF Report No. STF24 A97314, SINTEF, Trondheim, Norway, 1997.
17. M.I. Onsøien, Ø. Grong, T. Skaland, and K. Jørgensen: *Mater. Sci. Technol.*, in press.
18. M.I. Onsøien, Ø. Grong, G. Rørvik, A. Nordmark, and T. Skaland: *Int. J. Cast Met. Res.*, 1997, vol. 10, pp. 17-26.
19. W. Kurz and D.J. Fisher: *Fundamentals of Solidification*, 3rd ed., Trans Tech Publications Ltd., Aedermannsdorf, Switzerland, 1992.
20. R.A. Krivanek and C.E. Mobley: *AFS Trans.*, 1984, vol. 92, pp. 311-18.
21. R.G. Faulkner, D.J. Fray, and R.D. Jones: *Worked Examples in the Kinetics and Thermodynamics of Phase Transformations*, The Institute of Metallurgists, London, 1980.
22. T. Skaland, Ø. Grong, and T. Grong: *Metall. Mater. Trans. A*, 1993, vol. 24A, pp. 2321-45.
23. D.M. Stefanescu: in *ASM Metals Handbook*, 9th ed., ASM INTERNATIONAL, Metals Park, 1988, vol. 15, pp. 61-70.
24. G.R. Purdy, D.H. Weichert, and J.S. Kirkaldy: *Trans. TMS-AIME*, 1964, vol. 230, pp. 1025-34.
25. K.R. Kinsman and H.I. Aaronson: *Metall. Trans.*, 1973, vol. 4, pp. 959-67.
26. M. Chisamera and I. Riposan: *Proc. 5th Int. Symp. on the Physical Metallurgy of Cast Iron*, Nancy, France, Sept. 1994.
27. T. Kusakawa, A. Ogame, X. Xu, and H. Lin: *Proc. 3rd Int. Symp. on the Physical Metallurgy of Cast Iron*, Stockholm, Sweden, Aug. 1984, Elsevier Science Publishing Company, Inc., New York, NY, 1984, pp. 109-17.
28. B. Francis: *Metall. Trans. A*, 1979, vol. 10A, pp. 21-31.
29. R.J. Warrick: *AFS Cast Met. Res. J.*, 1966, vol. 2, pp. 97-108.
30. M.J. Lalich and J.R. Hitchings: *AFS Trans.*, 1976, vol. 84, pp. 653-64.
31. C.S. Kanetkar, H.H. Cornell, and D.M. Stefanescu: *AFS Trans.*, 1984, vol. 92, pp. 417-28.


32. M.H. Jacobs, T.J. Law, D.A. Melford, and M.J. Stowell: *Met. Technol.*, 1974, vol. 1, pp. 490-500.

33. M.I. Onsøien, Ø. Grong, A.K. Dahle, and L. Arnberg: *Proc. 4th Decennial Int. Conf. on Solidification Processing*, Sheffield, United Kingdom, July 7-10, 1997, The University of Sheffield, Sheffield, 1997, pp. 358-61.

34. Ø. Grong, A.K. Dahle, M.I. Onsøien, and L. Arnberg: *Acta Mater.*, 1998, vol. 46, pp. 5045-52.