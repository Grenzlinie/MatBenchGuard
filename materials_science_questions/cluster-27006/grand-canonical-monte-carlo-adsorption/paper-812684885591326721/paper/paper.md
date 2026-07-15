![](./images/812684885591326721_1.jpg)

# Numerical modeling of microscopic fluid distribution in porous media
Rosemary Knight, Alice Chapman, and Michael Knoll

Citation: *J. Appl. Phys.* **68**, 994 (1990); doi: 10.1063/1.346666
View online: http://dx.doi.org/10.1063/1.346666
View Table of Contents: http://jap.aip.org/resource/1/JAPIAU/v68/i3
Published by the AIP Publishing LLC.

---

## Additional information on J. Appl. Phys.
Journal Homepage: http://jap.aip.org/
Journal Information: http://jap.aip.org/about/about_the_journal
Top downloads: http://jap.aip.org/features/most_downloaded
Information for Authors: http://jap.aip.org/authors

---

## ADVERTISEMENT
![](./images/812684885591326721_2.jpg)

# Numerical modeling of microscopic fluid distribution in porous media
Rosemary Knight, Alice Chapman, and Michael Knoll
Department of Geological Sciences, University of British Columbia, 6339 Stores Road, Vancouver, British Columbia V6T 2B4, Canada

(Received 11 September 1989; accepted for publication 3 April 1990)

Three numerical methods have been developed to model the equilibrium distribution of fluid phases in a multiphase saturated porous medium. The basic assumption made is that the distribution of phases is governed by the static interfacial free energy of the system, such that the equilibrium phase distribution corresponds to a minimum in the total interfacial free energy of the system. The example of determining the distribution of water vapor and liquid water in 2D numerical models of the pore space in a rock is considered. Starting with a numerical model of the pore space, the objective of each method is to obtain the minimum energy configuration of water vapor and liquid water in the pore space for some set level of water saturation. Two of the methods are simple and computationally fast methods that can produce fluid distributions close to, or matching, the equilibrium configuration. These methods can, however, produce metastable configurations due to the simplistic nature of the algorithms. The third method applied to this problem is a simulated annealing method. This method consistently produced the lowest possible energy configuration. It is concluded that simulated annealing can be successfully used to numerically model fluid distribution in multiphase saturated porous media.

## INTRODUCTION
Much insight can be gained into the physical properties of rocks by numerically modeling rock properties on a microscopic scale. Previous numerical models of the physical properties of rocks have used sphere packs as models in which the void space between spheres is taken to represent the water-filled pore space in a rock. $^{1-3}$ The results of such modeling have greatly contributed to our understanding of transport in fully water-saturated porous media. An obvious extension of this type of modeling is to consider cases for which the model pore space contains more than one fluid. $^{4}$ In order to use such numerical techniques to study the behavior of multiphase saturated rocks, however, it is critically important that a realistic scheme is used to distribute the various fluids in the model pore space.

The importance of accurately representing microscopic fluid distribution in modeling rock properties is evidenced by the increasing number of observations of the strong dependence of rock properties on the details of the microscopic fluid distribution. It is clear that it is not simply the volume of fluids present that determines rock properties, but the microscopic distribution and geometries of the fluids. The microscopic distribution of fluids has been found to have a large effect in laboratory measurements of compressional wave velocities, $^{5}$ seismic attenuation, $^{6}$ electrical resistivity, $^{7}$ and dielectric constant. $^{8}$

Given the strong dependence of physical properties on details of the microscopic fluid distribution, a method must be found that can numerically reproduce fluid distribution in a porous medium. We have developed three numerical schemes that can be used to determine the equilibrium distribution of fluids in a model pore space. These numerically produced fluid distributions provide a realistic model of microscopic fluid distribution. The model pore space can be an idealized model such as created in a sphere pack, or a replica of an actual pore space, generated using digitized thin section data and serial reconstruction techniques. This multiphase saturated model provides a realistic starting point for numerically modeling the physical properties of multiphase saturated porous media.

## DESCRIPTION OF THE MODEL
The basic assumption in our technique is that the distribution of fluid phases is governed by the static interfacial free energy of the system, such that the equilibrium phase distribution corresponds to a minimum in the total interfacial free energy of the system. This technique can thus be applied to determining the equilibrium distribution of phases in any multiphase system once the interfacial free energies of all interfaces are known. The objective function to be minimized is
$$G_{i}^{s}=\sum_{i} A_{i} \gamma_{i},\qquad(1)$$
where $G_{i}^{s}$ is the total interfacial free energy of the system, $A_{i}$ is the area, and $\gamma_{i}$ is the interfacial free energy of the $i$ th interface.

To illustrate the use of our model, we will consider the problem of determining the distribution of liquid water and water vapor in the pore space of a rock. The liquid phase is assumed pure water; the vapor phase is assumed saturated with water vapor; the solid surface is assumed to be quartz at equilibrium with the water vapor and thus includes an adsorbed water layer, probably several monolayers thick. Parks $^{9}$ estimated ranges of interfacial free energies for two of the three interfaces we need to consider, solid quartz/liquid water (SL) and solid quartz/saturated water vapor (SV). The interfacial free energy of pure liquid water/water-vapor-saturated air (LV) is given by Adamson. $^{10}$ The values selected for use in this study are

---
994
J. Appl. Phys. 58 (3), 1 August 1990
0021-8979/90/150994-08$03.00
© 1990 American Institute of Physics

$$\gamma_{\mathrm{sv}}=422 \mathrm{~mJ} \mathrm{~m}^{-2},$$

$$\gamma_{\mathrm{SL}}=350 \mathrm{~mJ} \mathrm{~m}^{-2},$$

$$\gamma_{\mathrm{LV}}=72 \mathrm{~mJ} \mathrm{~m}^{-2}.$$

Our starting model of the rock is an array of elements, each designated as either a solid element or a pore element. We will first use, as an example in solving the problem in 2D, the digitized thin section image of Berea sandstone shown in Fig. 1. Each pixel in this image corresponds to a pore ele- ment or solid element in our model. For illustration pur- poses, we will consider a small region of the pore space en- larged so that each pixel or element appears as a square; this is shown in Fig. 2. Although the example we show here is2D, this technique can readily be extended to consider 3D models.

In modeling the distribution of liquid water and water vapor in a model pore space, we first select the desired level of water saturation, i.e., the number of pore elements that will be liquid elements or vapor elements. The level of water saturation $(S_{w})$ is defined as the volume fraction of the total number of pore elements that are liquid elements. Since our criterion for finding the equilibrium distribution of phases is the minimization of $G_{l}^{s}$ , our goal is to select the locations of liquid and vapor elements so as to minimize $G_{l}^{s}$ .

We have developed three methods to model the distribu- tion of fluid phases using this criterion. Methods 1 and 2 are very simple and computationally fast methods for determin- ing fluid distribution in which the state (liquid or vapor) of a single element is determined within each iteration and per- manently fixed as such. Method 3 involves the application of the simulated annealing method $^{11}$ to this problem, allowing us to consider all elements simultaneously.

![](./images/812684885591326721_3.jpg)
$1×10^{-4}m$

FIG. 1. Digitized thin section image. The black region corresponds to pore space, the patterned region corresponds to solid. A pore in the upper-left region is enlarged in Fig. 2.

![](./images/812684885591326721_4.jpg)
$1×10^{-5}m$

FIG. 2. Enlarged region of digitized thin section. The black region corre- sponds to solid; each white square corresponds to a single pore space ele- ment.

# SINGLE ELEMENT METHODS

Consider the model in Fig. 2. In method 1, all the pore space elements are initially designated as vapor elements; i.e., the pore space is filled with vapor. Our initial total inter- facial free energy includes only the solid/vapor interfaces. We now want to add a certain volume of water to the pore space, i.e., convert the appropriate number of vapor ele- ments to liquid elements. This conversion is done one ele- ment at a time; at each step one vapor element is selected to be replaced by a liquid element so as to minimize the total interfacial free energy of the system. This is done discretely by finding the element for which the conversion from vapor to liquid will cause the maximum drop in interfacial free energy $(G^{s})$ . Each element thus has associated with it a $\Delta G^{s}$ .

In calculating interfacial free energy we consider near- est and next-nearest neighbors. For example, select a vapor element in Fig. 2 surrounded by five solid elements and three vapor elements. Treating the length of the interface between any two elements as unity, the initial interfacial free energy of the element is
$$G_{i}^{s}=5 \gamma_{\mathrm{sv}}.\qquad(2)$$

If the selected vapor element is converted to a liquid element, the final state consists of a new liquid element surrounded by five solid elements and three vapor elements and the final interfacial free energy becomes
$$G_{f}^{s}=5 \gamma_{\mathrm{SL}}+3 \gamma_{\mathrm{LV}}.\qquad(3)$$

The change in interfacial free energy incurred by converting the selected element from a vapor element to a liquid element is
$$\begin{aligned}
\Delta G^{s} & =G_{f}^{s}-G_{i}^{s} \\
& =5\left(\gamma_{\mathrm{SL}}-\gamma_{\mathrm{SV}}\right)+3 \gamma_{\mathrm{LV}}.
\end{aligned}\qquad(4)$$
$\Delta G^{s}$ is determined in this way for each element and the ele ment associated with the minimum $\Delta G^{s}$ is converted to a liquid element. If there exist a number of elements of equal minimum $\Delta G^{s}$ , the choice is made randomly from among


those elements. The change of an element from a vapor ele- ment to a liquid element is a permanent one, so that in this method no rearrangement of elements can occur at some subsequent step. After each conversion of an element from vapor to liquid, the energies of any neighboring elements (for which the conversion will affect the free energies) are recalculated before converting the next element. This pro- cess for the conversion of vapor elements to liquid elements is repeated until the desired level of water saturation is reached.

Resulting fluid distributions obtained using this method are shown in Fig. 3 for $S_{w}=0.1$ to 0.9. As can be seen in this figure, realistic fluid distributions are obtained. At low satu- rations "high-energy" surface sites are filled with water; the greater the number of solid interfaces a vapor pore element has, the greater the drop in energy obtained by converting that element to a liquid element. Once the narrow (high- surface-area-to-volume ratio) regions in the pore space are filled, the central volumes of the pores start filling. As one would expect, the smaller pores fill first (e.g., the pore in the lower left of the figures). At the higher levels of water satura- tion a circular vapor bubble exists in the large pore that de- creases in radius as liquid elements are added.

The second simple algorithm, method 2, begins with a liquid-filled pore space and then converts liquid elements to vapor elements until the desired saturation level is obtained. Again, conversions are made by selecting those elements for which $\Delta G^{s}$ is a minimum, where $\Delta G^{s}$ is now the energy of the element as a vapor element minus the energy of the ele- ment as a liquid element. Results obtained using method 2 are shown in Fig. 4. While the results are very similar to those obtained using method 1, there are differences that are evident both in the fluid distribution patterns and in the magnitude of $G_{t}^{s}$ obtained with the two methods. To what extent then have we succeeded in solving our optimization problem, i.e. finding a distribution of fluid phases that mini- mizes $G_{t}^{s}$?

Methods 1 and 2 were each run numerous times for $S_{w}=0.0$ to 1.0, using the pore space in Fig. 2 as the pore space model. At any given $S_{w}$ , the value of $G_{t}^{s}$ obtained was different both for the two methods and for repeated runs of the same method using different random number seeds. The variation in $G_{t}^{s}$ was between $5 \%$ and $10 \%$ and the corre sponding differences in liquid and vapor distribution could be seen. This observed variation in $G_{t}^{s}$ and fluid distribution shows that we cannot assume that either of the two methods actually obtains the global minimum in $G_{t}^{s}$ . This is undoubt edly due to the major limitation of both of these schemes: Once an element is converted its state is permanently fixed;

![](./images/812684885591326721_5.jpg)

FIG. 3. Results obtained for modeling liquid and vapor distribution in the pore space using method 1. The black region corresponds to solid; white squares correspond to vapor elements in the pore space; patterned squares correspond to liquid elements in the pore space. Starting with all pore ele- ments set as vapor elements, vapor elements are converted to liquid ele- ments until the desired $S_{w}$ is reached. Results are shown for $S_{w}=0.1,0.3$ ,0.5, 0.7, and 0.9.

![](./images/812684885591326721_6.jpg)

FIG. 4. Results obtained for modeling liquid and vapor distribution in the pore space using method 2. The black region corresponds to solid; white squares correspond to vapor elements in the pore space; patterned squares correspond to liquid elements in the pore space. Starting with all pore ele- ments set as liquid elements, liquid elements are converted to vapor ele- ments until the desired $S_{w}$ is reached. Results are shown for $S_{w}=0.1,0.3$ ,0.5, 0.7, and 0.9.

elements cannot be rearranged at some subsequent step.
Choices made with either of the two methods in one iteration between equally advantageous sites might not lead in the direction of the global minimum; even if choices are made optimally, the global minimum might not be reached by successive conversion of elements.

What then can be done? One might suggest an "exhaus- tive search" for the fluid configuration that has the lowest total interfacial energy for a given saturation level. To con- sider every possible fluid distribution, however, quickly be- comes computationally infeasible, even for small models such as the one we consider here. A related and equally im- portant issue is the shape of the objective function. Because the size and shape of pores vary widely in rocks, we can expect the objective function $G_{i}^{s}$ to contain many minima of different depths. This immensely complicates the optimiz- ation problem.

We have found that this problem can be addressed using the simulated annealing method. $^{11}$ Simulated annealing is well suited to optimization problems in which the objective function to be minimized is defined on a discrete, very large configuration space; $^{12}$ our problem exactly.

# THE SIMULATED ANNEALING METHOD

The simulated annealing method is a Monte Carlo opti- mization procedure developed by Kirkpatrick and co- workers. $^{11}$ It is based on an analogy made between the ther modynamic problem of finding the low-temperature, minimum energy state of a material and the optimization problem of finding the global minimum of an objective func- tion. If a material is carefully annealed (slowly cooled from a high temperature) it will reach a stable minimum energy state. Conversely, if a material is quenched (rapidly cooled from a high temperature) it will not reach the minimum energy state. The process of annealing then is analogous to finding the global minimum in optimization, while the pro- cess of quenching is analogous to erroneously selecting a local minimum. In the simulated annealing method an an- nealing process is followed for the minimization of an objec- tive function by introducing a control parameter analogous to temperature which has the same units as the objective function.

A basic component of the simulated annealing method is the Metropolis algorithm $^{13}$ which can be used to simulate the equilibrium state of a system composed of a large number of atoms at some given temperature. Changes in the system(positions of the atoms) are randomly generated and cause an energy change in the system of magnitude $\Delta E$ . If a change results in $\Delta E ≤0$ , the change automatically takes place. If $\Delta E>0$ , the probability of the change occurring $[P(\Delta E)]$ is calculated using the Boltzmann probability distribution,

$$P(\Delta E)=\exp (-\Delta E / k T), \quad (5)$$

where $k$ is the Boltzmann constant and $T$ is temperature. $P(\Delta E)$ is compared to a random number $R$ between 0 and 1 ; if $P(\Delta E)>R$ then the change will occur, otherwise it will not. After numerous iterations, the system approaches a Boltzmann distribution.

When implementing simulated annealing to solve an op- timization problem, the objective function of the problem is the analog of energy in the Metropolis algorithm. Starting with a high value of $T(T_{0})$ which then decreases at each temperature step by a set factor $(T_{fac })$ , the Metropolis algo rithm is used at each temperature step to solve for the mini-mum energy state of the system. The choice of $T_{0}$ and $T_{fac }$  determine the cooling schedule of the annealing process.

The application of simulated annealing to our problem is relatively straightforward. The objective function to be minimized is an energy, $G_{i}^{s}$ . In order to find the equilibrium distribution of liquid and vapor for a certain $S_{w}$ , the required number of pore elements are first randomly selected and converted to liquid elements. Our starting point is thus a pore space containing the correct number of liquid and va- por elements but located randomly; we now need to find the optimal location for the liquid and vapor elements. The type of change in the system which we then consider at each tem- perature is the exchange of a randomly selected vapor ele- ment at one location in the pore space with a randomly se- lected liquid element at another location. This is the same as simultaneously converting the vapor element to a liquid ele- ment and the liquid element to a vapor element. The corre- sponding total change in energy for this vapor-liquid ex- change is the sum of $\Delta G^{s}$ for the vapor-to-liquid conversion and $\Delta G^{s}$ for the liquid-to-vapor conversion, calculated in the same way as is done using methods 1 and 2.

The cooling schedule parameters were determined by trial and error. For simplicity $k$ was set equal to 1. We then ran multiple realizations for a range of $T_{0}$ and $T_{fac}. T_{0}$ was varied from 2 to 4096. When $T_{0}$ was set to a value greater than $1000,80 \%$ of the changes generated in the first iteration were accepted; this is the guideline for the choice of $T_{0}$ suggested by Kirkpatrick. $^{14}$ With $T_{0}$ greater than $1000, T_{fac }$  was varied from 0.009 to 0.98. For $T_{fac }$ values greater than0.5 we consistently obtained minimum energy results. For lower values of either $T_{0}$ or $T_{fac }$ we found that the probabili ty of obtaining a minimum energy result was significantly decreased.

Results obtained using simulated annealing are shown in Fig. 5. All testing of the three methods was done using a Mac II computer; the computation time required for one saturation for methods 1 and 2 was approximately $5 ~s$ ; using simulated annealing the computation time ranged from 5 to25 min. The differences in fluid distributions obtained using the three methods are subtle, but it can be seen by comparing G; obtained with the three methods, shown in Table I, that simulated annealing always finds the fluid distribution that corresponds to the minimum in $G_{i}^{s}$ . While it is impossible to verify conclusively that we have found the global minimum with simulated annealing, repeated testing of this method, and visual assessment of the resulting distributions, suggest that we have obtained a realistic representation of the equi- librium fluid distribution.

# METASTABILITY

In the first example pore space we have shown, there exists little difference in the fluid distribution and $G_{i}^{s}$ found using the three methods. This suggests that given the compu- tational ease and speed of methods 1 and 2, these methods

![](./images/812684885591326721_7.jpg)

FIG. 5. Results obtained for modeling liquid and vapor distribution in the pore space using the simulated annealing method. The black region corre- sponds to solid; white squares correspond to vapor elements in the pore space; patterned squares correspond to liquid elements in the pore space. Results are shown for $S_{w}=0.1,0.3,0.5,0.7$ , and 0.9.

could be most readily used to obtain models of fluid distribu- tion. We have found, however, that with certain pore geome- tries, metastable fluid distributions will develop using meth- ods 1 and 2, such that the fluid distributions produced with these methods are very different from, and correspond to considerably higher values of $G_{t}^{s}$ than, those obtained with the simulated annealing method.

Consider the model of a pore space shown in Fig. 6. In this case we assume that the boundaries of this model (not shown in the figure) are mirror images of the elements sothat the pore space extends beyond the limits of the model; i.e., a region of the pore space is being considered that is connected to other pore space.

A set of results obtained from modeling the distribution of liquid water and water vapor in this pore space using the three methods is shown in Figs. 7 (method 1), 8 (method 2), and 9 (simulated annealing). A plot of $G_{t}^{s}$ vs $S_{w}$ for the three methods is given in Fig. 10. It can be seen in this case, both from the figures and the plot of the energies, that the three methods produce very different results. Again, simulated annealing consistently produces the lowest energy configu- ration. At the two extremes of the $S_{w}$ range all three methods produce very similar results. At intermediate $S_{w}$ values, however, the main problem with methods 1 and 2 becomes very obvious with a pore geometry of this type.

In comparing the results from method 1 (Fig. 7) and simulated annealing (Fig. 9): At low levels of $S_{w}$ , the fa vored locations for liquid elements are the sites with the highest number of solid interfaces along the surface of the pore space; this appears in the results from both methods. At some point the number of liquid elements present is high enough that the lowest energy state can only be reached by clustering the liquid elements to completely fill a region of the pore space. This clustering occurs in the simulated an- nealing example in Fig. 9 at $S_{w}=0.45$ . In fact, a closer look at this clustering shows that it occurs in the simulated an- nealing results between $S_{w}=0.43$ and $S_{w}=0.45$ (Fig. 11). What is occurring at this saturation point can be considered to be a critical phenomenon, somewhat analogous to a Haines jump, $^{15}$ in the pore space. With method 1, however, this clustering through rearrangement of the liquid elements cannot occur because of the "single element" nature of the algorithm. Consequently method 1 becomes trapped in a metastable state with an elongated central vapor phase maintained at $S_{w}=0.45$ . Referring to Fig. 10, it can be seen that this metastable configuration corresponds to a plateau and peak in $G_{t}^{s}$ in this saturation range. The same situation occurs at two other saturations where thin vapor pockets, clearly a metastable configuration, are maintained because of the deficiency in method 1.

In considering the results from method 2, the obtained energies and fluid distributions are closer to the simulated annealing results, but problems are again encountered due to the simplicity of the "single element" algorithm. An exam- ple of this is near $S_{w}=0.35$ where the liquid in this case stays clustered instead of rearranging to cover solid surfaces. A corresponding peak occurs in $G_{t}^{s}$ in this saturation range(Fig.10).

TABLE I. $G_{t}^{s}$ obtained at different $S_{w}$ using the three methods. $G_{t}^{s}$ values have been normalized such that $G_{t}^{s}$ for $S_{w}=0.0$ is equal to 1.000 and $G_{t}^{s}$ for $S_{w}=1.0$ is equal to 0.000 .

| $S_{w}$ | $G_{t}^{s}$ (method 1) | $G_{t}^{s}$ (method 2) | $G_{t}^{s}$ (simulated annealing) |
|--------|------------------------|------------------------|----------------------------------|
| 0.0    | 1.000                  | 1.000                  | 1.000                            |
| 0.1    | 0.755                  | 0.735                  | 0.731                            |
| 0.3    | 0.482                  | 0.447                  | 0.427                            |
| 0.5    | 0.312                  | 0.320                  | 0.304                            |
| 0.7    | 0.233                  | 0.229                  | 0.221                            |
| 0.9    | 0.126                  | 0.130                  | 0.126                            |
| 1.0    | 0.000                  | 0.000                  | 0.000                            |

![](./images/812684885591326721_8.jpg)

FIG. 6. Pore space model. The black re- gion corresponds to solid; each white square corresponds to a single pore space element.

![](./images/812684885591326721_9.jpg)

FIG. 7. Results obtained for modeling liquid and vapor distribution in the pore space model using method 1. The black region corresponds to solid; white squares correspond to vapor elements in the pore space; patterned squares correspond to liquid elements in the pore space. Results are shown for $S_{w}$ from 0.05 to 0.95.

## CONCLUSIONS

We have developed three methods that can be used to provide numerical models of the distribution of fluid phases in a multiphase-saturated porous medium. As we are interested in modeling the equilibrium distribution of phases, our problem has been that of minimizing the total interfacial free energy of the system. The adaptation of the simulated annealing method to this problem has been relatively straightforward and has produced realistic results which we believe represent an equilibrium fluid distribution for the system.

The two other simpler, single element methods that we have used can obtain results that are similar to those obtained with simulated annealing, but there is no guarantee with these two methods, because of the simplicity of the algorithm, that they will produce low-energy configurations. The possibility of being trapped in a metastable configuration with these two methods was shown with our second example. Nevertheless, these two methods may prove to be a useful way of obtaining a starting point for the simulated annealing method when dealing with larger 2D or 3D pore space models. At low saturations, method 1 provides the lower-energy result, while at higher saturations method 2 provides the lower energy result. At $S_{w}$ very close to 0 and 1, there is so little difference between the three methods that if these extreme values of saturation are of interest, any of the three methods could be used.

The examples shown here have been 2D, but these methods can easily be extended to treat 3D models. Because we are considering the equilibrium distribution of phases, the connectivity of the pore space does not affect the solution, as it can be assumed that given sufficient time to obtain equilibrium, all regions of the pore space are accessible to any phase; so the basic algorithm used in all three methods will remain the same.

The goal of this study has been to develop a means of

![](./images/812684885591326721_10.jpg)

FIG. 8. Results obtained for modeling liquid and vapor distribution in the pore space model using method 2. The black region corresponds to solid; white squares correspond to vapor elements in the pore space; patterned squares correspond to liquid elements in the pore space. Results are shown for $S_{w}$ from 0.05 to 0.95.


![](./images/812684885591326721_11.jpg)

FIG. 9. Results obtained for modeling liquid and vapor distribution in the pore space model using simulated annealing. The black region corresponds to solid; white squares correspond to vapor elements in the pore space; patterned squares correspond to liquid elements in the pore space. Results are shown for $S_{w}$ from 0.05 to 0.95.

![](./images/812684885591326721_12.jpg)

FIG. 10. $G_{l}^{s}$ vs $S_{w}$ obtained using methods 1 and 2, and simulated annealing. $G_{l}^{s}$ values have been normalized such that $G_{l}^{s}$ for $S_{w}=0.0$ is equal to1.00 and $G_{l}^{s}$ for $S_{w}=1.00$ is equal to 0.00.

![](./images/812684885591326721_13.jpg)

FIG. 11. Results obtained for modeling liquid and vapor distribution in the pore space model using simulated annealing for $S_{w}=0.43$ and $S_{w}=0.45$.

obtaining the equilibrium fluid distribution in a porous me- dium. Our approach has been to arrange liquid and vapor in a model pore space in such a way as to minimize the interfa- cial free energy of the system. If there is more than one ar- rangement of liquid and vapor that corresponds to the same minimum energy, the simulated annealing technique can produce these various equivalent configurations when dif- ferent random number seeds are used. In reality, the use of different processes (e.g., imbibition or drainage) to saturate a porous medium will lead to different fluid distributions. The simulated annealing technique can be used to find all possible minimum energy configurations, but cannot be used to simulate the saturating processes. It is not possible with any of the techniques presented to differentiate between min- imum energy distributions produced by different saturating processes.

The simulated annealing method has been successfully applied to the problem of determining an equilibrium distri- bution of fluid phases in a porous medium. This now pro- vides us with a realistic model of a multiphase saturated po- rous medium that can be the basis for further study of the physical properties of porous media.

## ACKNOWLEDGMENTS
This work began while one of the authors (R. K.) was with the Rock Physics Project in the Geophysics Depart- ment at Stanford University. She would like to thank Amos Nur, George Parks, and Brian Quinn for their encourage- ment and numerous helpful discussions, and Rick Ottolini and Stew Levin for their assistance with the computer dis- play of the results. At the University of British Columbia all authors have benefitted greatly from discussions with Barry Narod. We also would like to thank Ana Abad for her assis- tance in obtaining the digitized thin section image and Laura Wong for help with the figures. This research was supported by a grant (to R. K.) from the Natural Sciences and Engi- neering Research Council of Canada.


¹J. N. Roberts and L. M. Schwartz, Phys. Rev. B 31, 5990 (1985).

²L. M. Schwartz and J. R. Banavar, Physica A 157, 230 (1989).

³L. M. Schwartz, S. Tyc, P. N. Sen, and P. Wong, Physica A 157, 499 (1989).

⁴L. M. Schwartz and S. Kimminau, Geophysics 52, 1402 (1987).

⁵S. N. Domenico, Geophysics 41, 895 (1976).

⁶T. Bourbie and B. Zinszner, Society of Exploration Geophysicists Paper RPI, pp. 344-347 (1984).

⁷D. G. Longer, M. J. Argaud, and J. P. Feraud, Society of Petroleum Engineers Paper 15383 (1986).

⁸R. J. Knight and A. Nur, Log Ana. 28, 513 (1987).

⁹G. A. Parks, J. Geophys. Res. 89, 3997 (1984).

¹⁰A. W. Adamson, Physical Chemistry of Surfaces, 4th ed. (Wiley, New York, 1982).

¹¹S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, Science 220, 671 (1983).

¹²W. H. Press, B. P. Flannery, S. A. Teukolsky, and W. T. Vetterling, Nu- merical Recipes (Cambridge University, Cambridge, 1986).

¹³N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, J. Chem. Phys. 21, 1087 (1953).

¹⁴S. Kirkpatrick, J. Statist. Phys. 34, 975 (1984).

¹⁵W. B. Haines, J. Agr. Sci. 20, 97 (1930).