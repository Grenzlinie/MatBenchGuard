Thomas J. Kronenberger
David H. Johnson
John T. Roth

School of Engineering, Mechanical Engineering,
Penn State Erie, The Behrend College,
Erie, PA 16563

# Coupled Multifield Finite Element Analysis Model of Upsetting Under an Applied Direct Current

Recent research studying the deformation of various metals in compression, while running an electric current through the material, has been quite promising. A problem occurs when trying to identify the specific mechanisms that cause the changes in the mechanical properties, however, since the flow of electricity produces resistive heating, which also affects the mechanical properties of metals. However, previous research has proven that not all of the effects on the properties can be explained through resistive heating, implying that the electron flow through the metal also causes changes to the mechanical properties. Therefore, this work develops a model capable of differentiating between the effects of resistive heating and the effects of the electron flow when deforming 6061-T6511 aluminum in compression. To accomplish this, a detailed finite element simulation has been developed using ANSYS® with two models in symbiosis. The first model predicts the temperature of the specimen and compression fixtures due to the applied electrical current. The resulting thermal data are then input into a deformation model to observe how the temperature change affects the deformation characteristics of the material. From this model, temperature profiles for the specimen are developed along with true stress versus strain plots. These theoretical data are then compared with experimentally determined data collected for 6061-T6511 aluminum in compression. By knowing the exact effects of resistive heating, as obtained through the finite element analysis (FEA) model, the effects of the electron flow are isolated by subtracting out the effects of resistive heating from the data obtained experimentally. Future work will use these results to develop a new material behavior model that will incorporate both the resistive and flow effects from the electricity. [DOI: 10.1115/1.3090833]

## 1 Introduction

Many manufacturing processes involve the deformation of materials, such as forging, rolling, extrusion, and drawing. Many of these manufacturing processes deform the material in compression. However, whichever method is chosen, a significant amount of energy must be expended due to the high strength of most metals. This energy translates to added costs for the manufacturing process. Moreover, the more force that is required to deform a material, the more readily dies and machines will wear, which adds to the tooling cost of the manufacturing process. From this, it can be said that a significant portion of the manufacturing cost of a part is directly related to the amount of force required to deform the material (other than material and labor costs). Therefore, if this deformation force can be decreased, it could result in significant cost savings in many aspects of the manufacturing process. Currently, it is common practice to run many of these manufacturing processes at elevated temperatures in order to decrease the strength of the material being deformed, thereby requiring less force to deform the material. There are significant drawbacks, however, to hot-working materials. First and foremost, a great deal of energy is expended to heat the part to sufficient temperatures for processing. Then, once the part is at this elevated temperature, the adhesion increases between the tool/die and workpiece, the die becomes weaker, and material is often lost due to scale on the workpiece. Therefore, if a method could be developed that decreased the deformation force without significantly heating the part while allowing high production rates and minimizing costs, it would be extremely beneficial.

Along these lines, research has been conducted to see how materials respond when they are deformed with an electric current running through them. In 1969, Troitskii [1] found that electric current pulses could be used to temporarily reduce the yield strength in metal. Since then, further research has been conducted to investigate the effect of the passage of an electric current on various material properties. Investigations by Xu et al. [2] demonstrated that continuous current flow can enhance the recrystallization rate and grain size in select materials. Chen et al. [3,4] linked electrical flow to the formation and growth of intermetallic compounds, and Conrad [5–7] reported in several publications that very short duration high density electrical pulses affect the plasticity and phase transformations of metals and ceramics. Based on these studies there is a strong indication that an electric current flowing through a workpiece may reduce the flow stress of a material (the stress at any given strain required to maintain plastic deformation). This would consequently reduce both the force and energy necessary to deform the part. This effect should be similar to hot-working without the drawbacks of elevated temperature methods.

In 2004, as part of the preliminary investigation into the possibility of using an electrical current in this manner, Andrawes et al. [8] reported on the effects of direct current on the stress-strain behavior of aged 6061-T6511 aluminum. From this study, it was found that the current flow brought about significant reductions in both the force and energy required to perform tensile deformations. Similarly, in a study by Perkins et al. [9], it was shown that, when current was applied during compressive deformations, the total energy expenditure (electrical+mechanical) was significantly less than when using mechanical means alone (up to 90% decreases in required energy were observed). These changes in be-

---

Contributed by the Manufacturing Engineering Division of ASME for publication in the JOURNAL OF MANUFACTURING SCIENCE AND ENGINEERING. Manuscript received July 30, 2007; final manuscript received July 21, 2008; published online April 21, 2009. Review conducted by Jian Cao. Paper presented at the 2007 International Conference on Manufacturing Science and Engineering (MSEC2007), Atlanta, GA, October 15–17, 2007.

---

Journal of Manufacturing Science and Engineering
Copyright © 2009 by ASME

JUNE 2009, Vol. 131 / 031003-1

![](./images/811849027111878657_1.jpg)

Fig. 1 FE model geometry and boundary conditions

havior occurred at relatively low workpiece temperatures (i.e., the workpiece temperature remained well below the recrystallization temperature of the material). Following this investigation, a secondary study was conducted by Heigel et al. [10] to determine whether the effects of the electricity in the 6061-T6511 aluminum samples were due to microstructural changes in the specimens. It was shown in this work that microstructural changes in the material, such as recrystallization, were not the major contributors to the electrical effects.

Furthermore, in the prior work presented by Andrawes et al. [8], the temperature field in a circular cross section tensile specimen carrying a large direct current was approximated with an axisymmetric heat transfer model with constant material properties and a constant uniform heat generation rate computed using $I^2R$. More recently, in 2006, Khalilollahi et al. [11] developed a finite element analysis (FEA) model, with the same interactive approach as the model presented herein, for the estimation of temperature's effect when deforming 6061-T6511 aluminum in tension. In the current study it is desired to have a model that more accurately estimates the effects of the resistive heating on 6061-T6511 aluminum while in compression.

The ultimate goal of this work is to have a representative model of the thermal effects due to the electrical current in the compression specimen. These thermal data will then be applied to a 3D structural model to see what the effect of the temperature is on a typical compression test. By coupling these FEA results with experimental data of tests conducted with current present, the effect of temperature, due to Joule heating, can be separated from any mechanical material property changes due to the electrical current. This ability to isolate the resistive heating effect will aid in the development of a robust model of the effects that electricity has on the structural behavior of metals.

## 2 FEA Model and Theory

A finite element analysis simulation model of the experiment was developed with the ANSYS® software. The laboratory setup exhibits one plane of reflective symmetry; therefore, a threedimensional, half-symmetry model was developed for this study. The model uses a lower-order, eight-node hexahedral finite element formulation for all bodies of this assembly. To electrically isolate the experimental setup, thermoset material was placed between the upper and lower fixtures and the corresponding platens of the machine. In the simulation, the thermal and electrical insulation layers above and below the rectangular steel plates are treated as boundaries, which do not permit heat or electrical current flow to or from the model. Figure 1 illustrates these decisions.

The interfaces between the various steel parts comprising the fixture are assumed fully bonded for the thermal, electrical, and structural simulations. Any increased thermal and electrical resistance at these interfaces was ignored in the model. The interfaces between the aluminum specimen and the steel platens were treated with contact-target finite element pairs, which permit heat and electrical flow in the thermal-electric transient simulation only where the parts are found to be in contact and, likewise, transfer loads and deformation between parts in the structural analysis solution. These standard elements available within ANSYS (contact174/target170) exist to handle large deformation and large relative sliding behavior at the interface between flexible, deformable bodies. This formulation tracks the changing contact of the surface of the specimen on the platens as the specimen is compressed to its final shape. This allows for the relative flow between the surfaces of the aluminum specimen and the steel platens. (This behavior is illustrated later in Figs. 14 and 15.)

The mesh, as illustrated in Fig. 1, is refined in the areas where more deformation is anticipated. Specifically, a finer mesh was used in the aluminum specimen due to the greater deformation that will occur there. A progressively coarser mesh was then built out from the fixture blocks becoming coarser as shown. The mesh presented in Fig. 1 includes 8910 total elements. To determine the required number of elements, the mesh was refined until no changes in the output were apparent as mesh changed. This required the mesh to be changed from 4964 to 8910 to 17,322 total elements, and the medium mesh, 8910 elements and 11,221 nodes, was found to be acceptably refined for this study.

Several boundary conditions were also required in order to accurately model the system. As displayed in Fig. 1, only half of the fixtures and specimen is present, and a symmetry boundary condition was applied along the cut. Therefore, anywhere along the symmetry plane, an adiabatic boundary condition was utilized. Starting with the larger upper and lower steel plates, convection was considered on all three sides, excluding the symmetry side. However, the top of the top rectangular plate and the bottom of the bottom rectangular plate were considered insulated since these interfaces are in contact with insulative Haysite reinforced polyester. Convection boundary conditions were applied to the faces of the rectangular plates that face one another (i.e., the bottom of the top plate and the top of the bottom plate). Second, considering the two steel cylinders on the fixtures, a convection boundary condition was put on the cylindrical sides and on the faces that are parallel to one another (i.e., bottom of the top cylinder and the top of the bottom cylinder). Third, considering the smaller, rectangular fixture blocks, aside from the symmetry boundary condition, convection was used on two of the sides of the blocks, while the third side had no boundary conditions due to these sides being the contact points for the electrical input. The faces of the fixture blocks that oppose one another also had no boundary conditions on them because this is where the deformation of the specimen will be contacting. Finally, the specimen had a convection boundary condition applied to the sides of the cylindrical specimen.

The aluminum material is defined having a room-temperature elastic modulus of 73,000 MPa and Poisson's ratio of 0.33. The material's yield point is defined as 280 MPa, and the tangent modulus after yielding is set at 142 MPa. This material model was developed using the measured data from experiments performed without electricity applied to the parts. This treatment of the nonlinear stress-strain material behavior is a "bilinear" stress-strain curve where the response is a straight line with the elastic modulus slope up to the yield point, then after yield, the response is a straight line with the tangent modulus slope. This experimentally based model was sufficient for this proof of concept study. Future work will consider a piecewise, multilinear stress-strain model. The effect of temperature is included in the bilinear stress-strain model from room temperature up to $140^\circ$C using experimental data obtained from tensile testing of the 6061-T6511 alloy investigated herein (shown in Fig. 2). A comparison of the effect of this

![](./images/811849027111878657_2.jpg)

Fig. 2 Stress-strain input for aluminum specimen

bilinear model to the actual data when performing compression (i.e., with friction) will be presented and discussed in Sec. 4.1 for both room-temperature and elevated temperature data (also, refer to Figs. 10 and 11). The material data input also includes the density, specific heat, thermal conductivity and electrical resistiv- ity for the thermal-electric simulation and elastic modulus, Pois- son's ratio, and the coefficient of thermal expansion for the struc- tural analysis. It is important to note that thermal expansion was accounted for in order to capture the full effect of how the expan- sion of both the fixture blocks and the specimen, when heated, will increase the stress during the compression test.

The material behavior of the steel fixture (i.e., the plates, cyl- inders, and platens) is defined as linear elastic, and this assump- tion is supported by observations from the test. For the tempera- ture range reached by the steel fixtures, the properties (shown in Table 1) were found to remain relatively constant since the tem- perature of the fixtures remained at roughly room temperature.

Since most material properties are functionally related to the temperature, it is important to include this relationship into the model of the aluminum specimen. Figure 3 shows the dependency of the thermal conductivity and the specific heat of 6061-T6511 aluminum on the temperature. In addition, Fig. 4 shows the de- pendency of electrical resistivity and the thermal expansion coef- ficient on the temperature.

The analysis begins with an initial static structural analysis to bring the assembly under pressure. To match the experiment, a 223 N axial load is applied to the upper rectangular plate to en- gage the contact surfaces. Once the static load is established, the electricity is introduced between the platens. The electrical bound- ary conditions are illustrated in Fig. 5, showing electric current (in amperes) input on the right face of the upper platen and 0 V applied on the right face of the lower platen, as was the case in the actual setup. The electric circuit is formed from the input face to the grounded face, passing the current through the aluminum specimen.

Radiation heat transfer effects are ignored in the thermal simu- lation environment. Convection from the outside surface of the specimen and steel platens is included using a convective film coefficient representing free convection to room-temperature air from horizontal, vertical, and cylindrical surfaces. Conduction out through the fixtures was also modeled for the simulation.

The structural analysis includes mechanical loading as the specimen is compressed at a rate of 25.4 mm/min. The tempera- ture effects on the material properties and the thermal strain be- havior are included in the system response.

<table><thead><tr><th colspan="2">Table 1 Material properties of steel fixtures</th></tr></thead><tbody><tr><td>Elastic modulus</td><td>205 GPa</td></tr><tr><td>Poisson's ratio</td><td>0.30</td></tr><tr><td>Thermal expansion</td><td>$12.6×10^{-6}/^{\circ }C$</td></tr><tr><td>Thermal conductivity</td><td>$29W/(m^{\circ }C)$</td></tr><tr><td>Specific heat</td><td>$460J/(kg^{\circ }C)$</td></tr><tr><td>Density</td><td>$7810kg/m^{3}$</td></tr><tr><td>Elect. resistivity</td><td>$1.7×10^{-7}\Omega m$</td></tr></tbody></table>

![](./images/811849027111878657_3.jpg)

Fig. 3 Thermal conductivity and specific heat versus temperature

![](./images/811849027111878657_4.jpg)

Fig. 4 Resistivity and thermal expansion versus temperature of 6061-T6511 aluminum

![](./images/811849027111878657_5.jpg)

Fig. 5 Electrical boundary conditions

Journal of Manufacturing Science and Engineering
JUNE 2009, Vol. 131 / 031003-3

Ideally, a single transient analysis could be performed using a multifield finite element to capture the electric field, heat transfer, and structural analysis behavior. Unfortunately, the ANSYS mul- tifield elements do not include plasticity material behavior and could not be used for this simulation. Therefore, a looping analy- sis macro was written to treat the process as sequential steps through time with manual coupling of the deformation results to the thermal-electric model. This looping macro was written in ANSYS® parametric design language (APDL) and maintained two simulation models: a thermal/electric transient model and a struc- tural static model.

The thermal/electric simulation was transient, capturing the gradual heating of the specimen while the test was performed. A loop interval of 0.5 s was used for the APDL macro. This means that the thermal/electric transient simulation ran for 0.5 s then was stopped. The temperature field was imposed on the structural model, and a static analysis was performed for the thermal expan- sion behavior, plus the crosshead movement at the same time point. After completing the structural analysis and determining the deformations, the shape of the thermal model was adjusted to account for the distortion of the specimen. This process repeats in a loop with each analysis continuing from the previously com- pleted solution, until the final target time (18 s.) is reached. It was found that using a smaller or larger looping time interval (0.25 s versus 1.0 s) had a negligible effect on the results.

To summarize the simulation process, it was necessary to use a different structural element to capture yielding and plasticity since no multifield element included those nonlinear material capabili- ties along with the necessary electrical and thermal behavior. Also, as the specimen is flattened, the region of contact between the platens and specimen increases so the electrical current den- sity decreases in that region, thereby generating less heat. This aspect of the test is treated in the simulation by the adjustment of the thermal/electric model mesh based on the structural model displacements at each loop of the APDL macro.

## 3 Experimental Validation Setup

The experimental portion of this paper was conducted using several pieces of equipment. The force was generated using a Tinius Olsen Super "L" universal testing machine and the elec- tricity was generated with a Lincoln R35 arc welder. In order to control the amount of current running through the test specimen, the arc welder was used in conjunction with a cooled-steel vari- able resistor. This allowed the resistance to be controlled, which, in turn, allowed the current and voltage to be controlled. The electrical leads from the welder were connected to the fabricated terminals that were located on the testing fixtures. The testing fixtures were made out of hardened steel. However, because of the presence of electricity, these fixtures had to be isolated from the testing machine to ensure that all of the electricity was going through the test specimen and not into the testing machine. This was done using Haysite reinforced polyester and polyvinyl chlo- ride (PVC) tubing. The Haysite was used in areas that experienced compressive loading, while the PVC tubing was used in areas that did not see any load. Haysite polyester is known for its high compressive strength and ability as an electrical insulator.

For each of the tests, the current was measured using an Omega HHM592D digital clamp-on ammeter, which was attached to one of the leads of the welder. The voltage was measured using a BK Survivor digital multimeter between the positive and negative leads at the welder. Each test was controlled using the TINIUS OLSEN NAVIGATOR software. This software that records the force and position data, which later in conjunction with the fixture com- pliance, can be converted to stress-strain plots. The complete test setup is displayed schematically in Fig. 6 and physically in Fig. 7. The temperature was monitored during the experimental tests us- ing a FLIR thermal imaging camera (Thermovision A20m).

The test specimens were made of 6061-T6511 aluminum. They were $6.35\pm 0.013$ mm in diameter and $9.53\pm 0.013$ mm in length. The specimens were measured each time to account for any variability in the manufacturing of the specimens. Once the specimen was inserted between the platens, it was preloaded to 222 N to ensure fixture/specimen contact for electrical purposes. Once it was preloaded, the test began. The tests were conducted at a loading rate of 25.4 mm/min. An infrared camera was used to verify uniform temperature across the sample. The thermal image indicated that while the temperature varied along the axis of the specimen, the temperature along the specimen's external cross section was constant, only varying slightly due to the positioning of the electrical contacts (this variation is also predicted by the FEA model, refer to Figs. 15 and 16). Furthermore, in the work presented in Ref. [11], it was shown that the temperature variabil- ity along the material's radial direction is negligible. A more de- tailed investigation of the temperature distribution can also be found in Ref. [12]. The test ended after either the specimen frac- tured or when the limit of the testing fixtures was reached (244.65 kN).

![](./images/811849027111878657_6.jpg)

Fig. 6 Schematic of test setup

## 4 Comparison of Model and Validation Results

Since both temperature and deformation were investigated, the results of the FEA model and the validation results will be com- pared on these aspects. To help validate the model, temperature results will be presented using maximum temperature profiles. These temperature profiles were obtained both from the FEA model and from the experimental test.

To further validate the model's results, comparisons will be made between the baseline test with no current present and the respective results from the FEA model. The model will also be validated through the use of several isothermal tests, which were conducted to compare with the results from the model and to provide supporting thermal sensitivity data with respect to the material properties of the aluminum. These validations will prove the robustness of the model.

The deformation characteristics will then be compared using true stress versus strain graphs. These plots will show the strength

![](./images/811849027111878657_7.jpg)

Fig. 7 Physical test setup

031003-4 / Vol. 131, JUNE 2009

Transactions of the ASME

![](./images/811849027111878657_8.jpg)

Fig. 8 60 A/mm² temperature profiles

![](./images/811849027111878657_9.jpg)

Fig. 9 45 A/mm² temperature profiles

of the aluminum during each type of test. The idea is that the stress versus strain plots obtained for the deformation using the model will be altered only as a result of the resistive heating that occurs while the electricity is on. The stress versus strain plots obtained from the experimental portion of this work will be altered by both the resistive heating and the electron flow. Therefore, any difference in the two plots will be a result of the electron flow, not due to Joule heating.

### 4.1 Model Validation.
The model was validated using various temperature profiles, the baseline test comparison, and the isothermal test comparisons.

#### 4.1.1 Temperature Profiles.
The temperature profile from the model was obtained using the thermal field of the FEA model. This was done by modeling the electrical flow through the fixtures and specimen in 3D using ANSYS®. From this, temperature profiles of the specimen can be determined in which a maximum temperature can be obtained and plotted with respect to time. This time is the time from which the electricity is turned on, until the electricity is turned off.

The temperature profiles from the experimental portion of this work were obtained from the thermal images that were found using the thermal imaging camera. The image was originally taken from the entire experimental setup, but after some post-test processing, the image was focused on the specimen so only the temperature profile of the specimen was visible. From this, a maximum temperature could be obtained for each frame. Knowing the length of the tests and the sampling rate, this maximum temperature could be plotted against time, resulting in a temperature profile. Before the thermal camera was used to collect data, however, it was first examined to ensure that it was calibrated properly. To calibrate the camera a piece of painted black steel was heated to temperatures which far exceeded those which would be experienced during a typical test (approximately 400°C). This piece of metal was then placed directly in front of the camera with a thermocouple attached to it, as well as a non-contact thermal infrared gun pointing at it. All three temperature measuring devices compared ensure that they read the same temperatures within 2–5°C. Using this approach, it was determined that the camera was calibrated and that the emissivity associated with the black paint did not affect the measured temperatures.

For emissive purposes, the test specimens were coated with black emissive paint before they were processed. This verified that the emissivity of the specimen was approximately 1 as the camera was calibrated to read.

The experimental temperature profile should match up relatively with the temperature profile from the FEA model. Figure 8 shows the temperature profiles for the 60 A/mm² tests. The model's profile and the experimental test profile are labeled explicitly on the graph. The temperatures shown represent the maximum value on the surface of the specimen, which occurred both for the experiment and for the simulation model, at the midpoint along the specimen's length due to the convective effects of the fixtures cooling the specimens at either end.

As can be seen in Fig. 8, the temperature profiles exhibit similar shapes and trends. The maximum temperatures reached are only different by approximately 5°C. Even though the plots do match up rather well, there are still some differences in the plots. This is a result of the thermal and electrical contact resistances defined for the ANSYS® model. The state of the art does not include experimental data on the contact resistance between aluminum and steel at the level of contact pressure experienced during forging processes. Unfortunately, existing theoretical calculations cannot also be applied to the temperature and pressure conditions of the current investigation. However, in the work cited previously [9], 6061 aluminum and C11000 copper were found to have nearly identical yields (an important parameter for contact resistance), to have similar resistivities, and responded to an applied electric current during deformation in similar ways (requiring comparable current densities to illicit comparable alterations in their respective mechanical properties). Fortunately, while aluminum-steel contact resistance data do not exist, copper-steel contact resistance has been studied by Rao et al. [13] and by Babu et al. [14]. Therefore, given the similarities cited above, these copper-steel findings were incorporated into the model developed herein.

It is known that these contact resistances decrease as pressure is applied to the interface. This is due to the changing surface roughness of the two contacting parts as well as the mechanical locking that occurs as the parts deform into one another. To reduce the impact of the surface roughness, both the specimen and the fixtures were hand polished to a mirror finish so that these surfaces matched the model's smooth surfaces. The effect of surface roughness in the model was also accounted for by carefully selecting the contact resistance parameters. Although future work will investigate the impact of the starting roughness on both the electro-plastic effect and Joule heating, it is not expected that the roughness will significantly affect the results beyond the initial contact period due to the high pressures involved, which will force conformation between the two surfaces. However, the transient nature of the deformation makes measuring any specific value for contact resistance nearly impossible. This was found to be a major factor when obtaining model results and is the main reason why the experimental and FEA models do not match exactly. As noted in Sec. 2, the actual contact resistances may also be off due to air gaps at the welded interfaces of the fixtures. However, given the concern with contact resistance, the results displayed in Fig. 8 are promising in that the maximum and ending temperatures are nearly identical between the two tests. Also, the basic trend is the same experimentally as was obtained through FEA. A similar profile is displayed in Fig. 9 for the test with a current density of 45 A/mm².

As is apparent, the temperature profiles for a slightly lower

![](./images/811849027111878657_10.jpg)

Fig. 10 Stress-strain baseline comparison

![](./images/811849027111878657_11.jpg)

Fig. 11 Isothermal test and model compared

current density also exhibit similar shapes and trends. It should be noted that in order to protect the thermal imaging camera, a double ply piece of plastic was stretched in front of it while the test was being conducted. It was found through testing that this plastic typically results in approximately a temperature reading of 2.8°C less than the actual. This should be kept in mind when comparing the data. Along with the issue with contact resistance, this is one other possible reason why the results do not match up exactly. However, as mentioned, the temperature profiles have the same basic trend for the 45 A/mm² test as well as the same ending temperature. The maximum temperature appears to be off by approximately 30°C, which is a result of the variations that have been discussed.

4.1.2 Baseline Comparison. To further validate the accuracy of the FE model, the baseline experimental test (0 A/mm²) was compared with a test run with the model in which no current was present. In theory, the deformation results from these two tests should match exactly. With no effect from the electricity and also no resistive heating, the stress versus strain plot generated from the experimental test should look almost identical to the stress versus strain plot obtained from the FEA model. Figure 10 shows the results of these two tests plotted in the same figure.

As shown in Fig. 10, the results for the test with no current from both the model and the experimental test are comparable. The modulus of elasticity and the yield stress are nearly identical between the two tests. Both the experimental test and model show approximately the same rate of strain hardening, and the flow stress seems to vary only after yield. The bilinear stress-strain curve selected for the model in these initial studies will be re-placed in future work with a piecewise multilinear curve to im-prove this comparison. Given this difference, however, the two tests coincide extremely well, which helps to prove how robust this multifield model is.

4.1.3 Isothermal Tests. To make one further validation be-tween the FEA model and experimental tests, several isothermal tests were conducted. An isothermal test is one with no current present, but rather the specimen is heated to a constant tempera-ture prior to starting deformation.

The specimen was heated from its ends by raising the tempera-ture of the fixture blocks using circular band heaters. For these tests, this was done in order to more closely mimic the manner in which it would be heated during a typical electrical test. By heat-ing from the ends, it also allows convection and radiation heat transfer to be present as boundary conditions on the specimen allowing energy to be taken away from the specimen. To maintain thermal contact between the band heaters and the fixture blocks, aluminum cylindrical inserts were fabricated to fit around the blocks. Aluminum was chosen due to its high thermal conductivity.

The temperature of the band heaters was maintained using a controller. This controller could be set and would act as a thermo-stat to maintain the desired temperature level. The set point on the controller was increased until the temperature of the specimen reached and held the desired temperature. Once the desired tem-perature was reached, the upsetting process would commence.

The goal of these tests was to heat the specimen to the levels in which it was heated resistively and show that the results do not compare with the tests when the electron flow is present. How-ever, the isothermal tests should overestimate the results that are produced by resistive heating because the maximum temperature is held constant for the entire process. During typical electrical tests, this maximum temperature is only reached briefly at about 4 s into the test. This can be seen in the temperature profiles in Figs. 8 and 9. Therefore, the results of the isothermal tests should ap-proximately compare with the same results from the model.

This comparison is made in Fig. 11. Figure 11 shows the true stress versus strain plot of an isothermal test at 142°C as well as a true stress versus strain plot from the FEA model run at the same temperature. Comparable results were observed, which further validates the robustness of the FEA model. The variation between the two curves is a direct result of the bilinear stress-strain mate-rial model used for the FEA simulation.

4.2 Model Result Comparison. It can now be concluded that the developed FEA model is accurate, to the point that it can be used to predict the effects that resistive heating has during elec-trical compression tests. Therefore, two current densities were ex-amined and compared. These current densities were 60 A/mm² and 45 A/mm². Figure 12 contains the true stress versus strain plots from the 60 A/mm² test.

It can be seen that the plot obtained from the model, which is only affected by resistive heating, does not compare with the plot obtained experimentally. This is because of the presence of the electron flow during the test. While the modulus of elasticity and

![](./images/811849027111878657_12.jpg)

Fig. 12 Stress versus strain plot 60 A/mm² test

![](./images/811849027111878657_13.jpg)

Fig. 13 Stress versus strain plot $45\ \text{A/mm}^2$ test

elongation are approximately the same between the two tests, the yield stress and flow stress are significantly less. From this it can be seen that the resistive heating that occurs during the electrical tests does not come close to producing the results that the electron flow does. Within the experimental results, it can be seen that the electron flow actually caused the stress to decrease as further deformation occurred. An extremely low stress was then maintained for a majority of the test and only increased once the height of the test specimen was severely lessened. The differences viewed in Fig. 12 are much greater than any differences that were observed within the previous validation plots. Therefore, the electron flow must be the primary cause of the observed differences since nothing else was altered between the experiment and the model.

One item that is noteworthy pertains to the elongation. Even though the elongation is the same between the FEA model and the experimental results, it is, in fact, much different when electricity is applied and compared with tests with no electricity. In fact, previous research has shown a doubling to quadrupling of the elongation when the electricity is applied compared with cases when no electricity is applied [12]. The reason the elongations were the same between the model and the experimental results was because the elongation is input into the model as a test parameter since there is no fracturing or fixture limits in the model.

The true stress versus strain plots from the $45\ \text{A/mm}^2$ test are displayed in Fig. 13.

Again, it can be seen in Fig. 13 that the respective results are comparable to these observed for the $60\ \text{A/mm}^2$ test. Specifically, the modulus of elasticity and elongation are relatively unchanged, while the yield and flow stress is significantly different. Therefore, again it can be seen that the results obtained due to resistive heating are far less than the results obtained when an electron flow is present.

### 4.2.1 Current Density Variations
Without the electrical FE model, it is impossible to predict the current density distribution across the specimen and how this affects the deformation characteristics. In fact, through this work it was found that the current density does vary somewhat as the specimen is deformed. Figure 14 shows the current density vectors at the beginning of the $60\ \text{A/mm}^2$ electrical test.

As the specimen was deformed, it was found that the current density decreases and becomes more concentrated on one side of the specimen. This can be seen in Fig. 15, where the current density vector plot is shown at the time when the $60\ \text{A/mm}^2$ test ends ($\sim 20$ s). By comparing the scale on the right in Fig. 15 with the scale in Fig. 14, the magnitude of the peak current density is approximately 49% lower. The current density decreases because the specimen's cross-sectional area increases during the deformation. Specifically, if the current does not change and the area increases, the current density will decrease.

An interesting observation to make is how the current density is more concentrated on one side of the specimen at the test's end.

![](./images/811849027111878657_14.jpg)

Fig. 14 Current density vectors at test beginning

The reason for this is that the electrical terminals are modeled on the same sides of the fixtures, which can be seen in Fig. 5 where the electrical boundary conditions are plotted on the fixtures. Therefore, the current is coming in and going out on one side of the fixture, which causes the current density to be higher on that side of the specimen. This is more apparent at the test's end because the specimen's diameter is larger.

This current density difference can be further observed in the final temperature profile of the fixtures/specimen. This profile is displayed in Fig. 16. This image shows that the temperature is higher on the side of the specimen in which the current density was concentrated. Therefore, since current density varies across the specimen's diameter, the temperature also varies.

## 5 Conclusion
From this work, many conclusions can be drawn. One major outcome of this work is a robust FEA model that can accurately predict the effect that resistive heating will have during an electrical compression test. This model was proven to be accurate through various validations such as temperature profiles, baseline testing, and isothermal testing. This model was then applied to several electrical compression tests. From this application it can be concluded that resistive heating does not produce the extreme property changes experienced when an electron flow is present.

Therefore, it can be concluded that when an electron flow is present during the compression of 6061-T6511 aluminum, the yield stress and flow stress are dramatically decreased without the

![](./images/811849027111878657_15.jpg)

Fig. 15 Current density vectors at test end (20 s)

Journal of Manufacturing Science and Engineering
JUNE 2009, Vol. 131 / 031003-7

![](./images/811849027111878657_16.jpg)

Fig. 16 Final temperature profile

excessive heating that is needed for hot-working. This then provides a viable improvement over hot-working since greater force reductions can be obtained without any of the drawbacks that are associated with hot-working.

It was also concluded that it does matter where the electrical terminals are placed on the fixtures. Specifically, if the terminals are both on one side then the current density will be somewhat concentrated on that side, thereby causing more resistive heating to occur on that side. Therefore, if the positive terminal were placed on one side and the ground terminal was placed on the opposite side, a more constant current density profile and temperature profile may have been produced.

## 6 Future Work

From this point, there is more work that will be conducted in the future. One area of interest will be to improve the model. From the results that were obtained, it has been concluded that ANSYS® can be used to make even more accurate predictions of experimental results. One aspect for improvement is by using a multilinear model for the stress versus strain response of the material, rather than a bilinear model, which was used in this work.

Another avenue that may be explored is developing a new model that will be able to predict the response of materials due to the influence of an electrical current. This will be a significant task since there are not any FEA material behavior models that currently exist that take electron flow into account when predicting deformation. However, from this work it was shown that the electron flow significantly alters a materials mechanical response; therefore new material behavior routines will have to be developed that will be able to predict this response.

Another area of future work is to develop a model with shaped dies, rather than flat dies. It would be interesting to be able to see the electron flow's effect when the strain rate is not constant throughout the material, as is the case in many common impression and closed die processes.

One last area that could be looked into would be the placement of the electrical terminals on the testing fixtures. As found in this work, it does matter where the terminals are placed on the experimental setup. Therefore, future models may explore the placement of the terminals and how the resulting current density and deformation are affected.

## References

[1] Troitskii, O. A., 1969, "Electromechanical Effect in Metals," Zh. Eksp. Teor. Fiz. Pis'ma Red., 10, p. 18.

[2] Xu, Z. S., Lai, Z. H., and Chen, Y. X., 1988, "Effect of Electric Current on the Recrystallization Behavior of Cold Worked $\alpha$-Ti," Scr. Metall., 22, pp. 187-190.

[3] Chen, S. W., Chen, C. M., and Liu, W. C., 1998, "Electric Current Effects Upon the Sn/Cu and Sn/Ni Interfacial Reactions," J. Electron. Mater., 27, pp. 1193-1199.

[4] Chen, S. W., and Chen, C. M., 1999, "Electric Current Effects on Sn/Ag Interfacial Reactions," J. Electron. Mater., 28, pp. 902-906.

[5] Conrad, H., 2000, "Electroplasticity in Metals and Ceramics," Mater. Sci. Eng., A, 287, pp. 276-287.

[6] Conrad, H., 2000, "Effects of Electric Current on Solid State Phase Transformations in Metals," Mater. Sci. Eng., A, 287, pp. 227-237.

[7] Conrad, H., 2002, "Thermally Activated Plastic Flow of Metals and Ceramics With an Electric Field or Current," Mater. Sci. Eng., A, 322, pp. 100-107.

[8] Andrawes, J. S., Kronenberger, T. J., Roth, J. T., and Warley, R. L., 2007, "Effects of DC Current on the Mechanical Behavior of AlMg1SiCu," Mater. Manuf. Processes., 22(1), pp. 91-101.

[9] Perkins, T. A., Kronenberger, T. J., and Roth, J. T., 2007, "Metallic Forging Using Electrical Flow as an Alternative to Warm/Hot Working," ASME J. Manuf. Sci. Eng., 129(1), pp. 84-94.

[10] Heigel, J. C., Andrawes, J. S., Roth, J. T., Hoque, M. E., and Ford, R. M., 2005, "Viability of Electrically Treating 6061 T6511 Aluminum for Use in Manufacturing Processes," Trans. North Am. Manuf. Res. Inst. SME, 33, pp. 145-152.

[11] Khalilollahi, A., Roth, J. T., and Johnson, D., 2006, "Multi-Field FE Modeling of Resistive Heating in a 6061-T6511 Aluminum Specimen," ASME Paper No. 15677.

[12] Ross, C. D., Kronenberger, T. J., and Roth, J. T., 2006, "Effect of DC Current on the Formability of 6AL-4V Titanium," ASME Paper No. 21028.

[13] Rao, V. V., Bapurao, K., Nagaraju, J., and Krishna Murthy, M. V., 2004, "Instrumentation to Measure the Thermal Contact Resistance," Meas. Sci. Technol., 15, pp. 275-278.

[14] Babu, S. S., Santella, M. L., Feng, Z., Riemer, B. W., and Cohron, J. W., 2001, "Empirical Model of Effects of Pressure and Temperature on Electrical Contact Resistance of Metals," Sci. Technol. Weld. Joining, 6(3), pp. 126-132.
