![](./images/811944607985172480_1.jpg)

Available online at www.sciencedirect.com

![](./images/811944607985172480_2.jpg)

Energy Conversion and Management 49 (2008) 1715-1723

![](./images/811944607985172480_3.jpg)

www.elsevier.com/locate/enconman

# Methodology on sizing and selecting thermoelectric cooler from different TEC manufacturers in cooling system design

F.L. Tan ${ ^{a, *}$ , S.C. Fok $^{b}$

${ }^{a}$ School of Mechanical and Aerospace Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore 639798, Singapore
${ }^{b}$ The Petroleum Institute in Abu Dhabi, Department of Mechanical Engineering, Abu Dhabi, United Arab Emirates

Received 19 July 2006; received in revised form 30 March 2007; accepted 22 November 2007
Available online 9 January 2008

## Abstract

The search and selection for a suitable thermoelectric cooler (TEC) to optimize a cooling system design can be a tedious task as there are many product ranges from several TEC manufacturers. Although the manufacturers do provide proprietary manuals or electronic search facilities for their products, the process is still cumbersome as these facilities are incompatible. The electronic facilities often have different user interfaces and functionalities, while the manual facilities have different presentations of the performance characteristics. This paper presents a methodology to assist the designer to size and select the TECs from different manufacturers. The approach will allow designers to find quickly and to evaluate the devices from different TEC manufacturers. Based on the approach, the article intro- duces a new operational framework for an Internet based thermoelectric cooling system design process that would promote the interac- tion and collaboration between the designers and TEC manufacturers. It is hoped that this work would be useful for the advancement of future tools to assist designers to develop, analyze and optimize thermoelectric cooling system design in minimal time using the latest TECs available on the market.
 2007 Elsevier Ltd. All rights reserved.

Keywords: Thermoelectric cooler (TEC); Thermoelectric cooling; TEC sizing and selection; Cooling system design

## 1. Introduction

Heat can be transferred through conduction, convection and radiation. Based on these three basic fundamental principles, many practical cooling systems utilizing fans, heat pipes, liquid and thermoelectric cooling devices have been developed. Among all these cooling innovations, ther- moelectric cooling [1-4] has become increasingly popular due to the rapid discovery and development of novel ther- moelectric materials.

Thermoelectric cooling is increasingly used in a variety of new products, which include picnic boxes, water cool- ers, laser devices, micro-electronics and optoelectronics appliances, highly specialized instrumentation and testing equipment. Thermoelectric cooling devices offer many advantages, which include good compactness, high reli- ability, long life span, fast thermal response (i.e. compared to air cooling fans and liquid heat exchangers) and excel- lent flexibility. Thermoelectric cooling can be used in refrigeration while generating direct current (DC) power in special circumstances (e.g, conversion of waste heat).

Thermoelectric cooling designs are accomplished using a thermoelectric cooler (TEC) [5], which is a solid state elec- trically driven heat exchanger that can pump heat in a direction depending on the polarity of the applied voltage. When the TEC is used as a cooler, it absorbs heat from the surface or object to be cooled and transfers the energy by conduction to the finned or liquid heat exchanger, which ultimately dissipates the waste heat to the surrounding ambient air by means of convection. The TEC operates by the Peltier Effect, which induces a temperature difference when an electrical current flows through a junction of dis- similar materials.

* Corresponding author.
E-mail address: mftan@ntu.edu.sg (F.L. Tan).

0196-8904/$ - see front matter  2007 Elsevier Ltd. All rights reserved.
doi:10.1016/j.enconman.2007.11.001

### Nomenclature

|  |  |  |  |
| --- | --- | --- | --- |
| $\Delta T$ | temperature difference across TEC (K) | $T_{\text{hot}}$, $T_{\text{h}}$ | TEC hot side temperature (K) |
| $Q$, $Q_{\text{c}}$ | heat input at cold side of TEC (W) | $T_{\text{load}}$ | temperature of load being cooled (K) |
| $Q_{\text{h}}$ | heat dissipated at hot side of TEC (W) | $T_{\text{amb}}$ | ambient temperature (K) |
| $Q_{\text{max}}$ | maximum heat input at cold side of TEC (W) | $T_{\text{HS}}$ | temperature at heat sink (K) |
| $I$ | electrical current (A) | $\theta_{\text{load}}$ | thermal resistance of heat spreader (K/W) |
| $R$ | TEC device electrical resistance ($\Omega$) | $\theta_{\text{HS}}$ | thermal resistance of heat sink (K/W) |
| $\Delta T_{\text{max}}$ | maximum temperature difference across TEC (K) | $\theta_{\text{TEC}}$ | thermal resistance of TEC (K/W) |
| $T_{\text{cold}}$, $T_{\text{c}}$ | TEC cold side temperature (K) | $S$ | TEC Seebeck coefficient (V/K) |
|  |  | $V$ | supplied voltage (V) |

In the world of thermoelectric cooler design and manufacturing, the designer does not usually custom make a TEC for a specific application. With modern technology, TECs are mass produced to deliver efficient solid state heat pumping for both cooling and heating purposes. Varieties of standard TECs having specified characteristics are available in the markets from many different TEC manufacturers.

Although the function of the synonymous types of standard TECs made by different manufacturers is the same, the geometry, specifications and characteristics may not be similar due to variations in design and manufacture. The designer has to select suitable TECs from among these manufacturers to meet the design requirements. Searching for a suitable TEC to optimize a design can be a tedious task as there are many global TEC manufacturers, each of whom has a large collection of products ranging from low cost commercial to high performance TECs. To complicate matters, different manufacturers use different formats to present their product performance characteristics. To facilitate the search, a few major TEC manufacturers offer software search facilities based on their proprietary products. These facilities are not compatible and cross searching for TECs from different companies is not supported. Furthermore, different manufacturers have different user interfaces based on different inquiry methodologies. Features such as component sizing and design analysis are often unsupported. As various operating conditions and geometry constraints are possible in the design of thermoelectric cooling systems, designers often have to search separately through the products from several manufacturers. This can be a cumbersome process. To facilitate the design task further, it is desirable to have a uniform electronic search and analysis facility with integrated functionalities and accessibility to the various manufacturers' product data on their TECs.

This paper presents the development of a methodology that can assist the designers in the selection and sizing of suitable TECs available from several TEC manufacturers. The search and analysis is based on the user input design specifications.

## 2. Search and analysis of TECs for cooling systems

This section provides the basic steps required in the search and analysis of appropriate TECs for a cooling system. Fig. 1 shows a typical assembly of a thermoelectric cooler in which the heat load is mounted on a sandwich consisting of a "load plate" or "heat spreader", a TEC or an array of TECs and a finned heat sink. This typical assembly is used to illustrate the TEC search process. Because of the non-linear behavior of thermoelectric coolers and the number of variables involved in their analysis, the steps presented here are mainly applicable for single and two stage thermoelectric coolers. For thermoelectric coolers with more than two stages, the accuracy of the results might be affected.

Every thermoelectric cooling application is characterized by a set of operational parameters and restrictions, which dictate the accurate selection of the optimal TEC type from among a wide range of single and multi stage TECs. The minimum specifications for finding a suitable TEC are:

- Heat load or the amount of heat to be absorbed at the TEC's cold surface ($Q_{\text{c}}$).
- Operating temperature difference ($\Delta T$), which is the temperature difference between the hot and cold side of the TEC.

![](./images/811944607985172480_4.jpg)

Fig. 1. A typical TEC assembly.

- Applied or operating current ($I$) of the TEC.
- Terminal or operating voltage ($V$) of the TEC.
- Dimensional and other restrictions.

Understanding these parameters and restrictions is important. In the preliminary design stage, one of the most important processes is to determine the total thermal load ($Q_{\text{c}}$) that must be pumped by the device. Prudent estimation of the amount of heat to be removed is often desired. The thermal load consists of both the active and passive loads. The active load actually produces the heat. This load could be the $I^{2}R$ load of an electrical component, the load of the dehumidifying air or the load of the cooling objects. In many TEC applications, the active load is usually not very significant.

A passive load exists when an object is cooler than the surrounding environment. This situation involves continual movement of energy into or out of the load so as to maintain the temperature difference between the object and the ambient environment. The rate at which this energy is moved is the passive load and is usually expressed in Watts. The passive load in a TEC system can be significant.

The temperature distribution of a practical TEC is shown in Fig. 2. The temperature gradient across the TEC device (actual $\Delta T$) is not the same as the apparent temperature difference (system $\Delta T$). The actual $\Delta T$ is defined as the temperature difference between the hot side temperature and the cold side temperature of the TEC device (i.e. actual $\Delta T=T_{\text{hot}}-T_{\text{cold}}$). The system $\Delta T$ is the temperature difference between the worst case temperature and the lowest possible heat load temperature (i.e. system $\Delta T=T_{\text{amb}}-T_{\text{load}}$).

The magnitude of the difference in these two $\Delta T$'s is mainly dependent on the type of heat exchangers utilized on either the hot or cold sides of the TEC. The thermal resistances of the heat exchangers could change the temperature drop across the TEC for a given $T_{\text{amb}}$ and $T_{\text{load}}$. This, in turn, could cause an increase in the current through the TEC device. A typical $\Delta T$ at the system hot side is around $10$–$15$ °C using forced air cooling with finned surfaces, $20$–$40$ °C for free convection and $2$–$5$ °C for cooling using a liquid heat exchanger. An approximate $\Delta T$ of about $50\%$ of the hot side $\Delta T$ (assuming similar types of heat exchangers) can be taken for the system cold side since the heat flux densities on the cold side of the system are considerably lower than those on the hot side. However, it is good practice to check the outputs of the selection process to reassure that the heat sink design parameters are reasonable.

The following is the step by step procedure for selection of the TEC [6] in cooling system designs:

**Step 1:** Determine the amount of heat to be pumped ($Q_{\text{c}}$).
**Step 2:** Determine the lowest needed heat load temperature (minimum $T_{\text{load}}$).
**Step 3:** Determine the worst case ambient temperature ($T_{\text{amb}}$).
**Step 4:** Determine the TECs hot and cold side temperatures and the temperature difference across it.

In most TEC performance data sheets, the maximum allowable temperature difference across the TEC $\Delta T_{\text{max}}$ is normally specified by the manufacturers. Therefore, the calculated temperature difference in step 4 is one criterion that can be used to search for appropriate TECs. However, the thermal resistance of the heat spreader and heat sink may not be known prior to the search. Improper design of a heat sink with high thermal resistance can cause a rise in the TEC's operating current and eventually force the entire cooling system into thermal "runaway". It is important to ensure that the design has sufficient safety margin for unexpected inefficiencies in the heat sink performance.

![](./images/811944607985172480_5.jpg)

Fig. 2. Temperature difference across the TEC.

To overcome this problem, a conservative estimate for the allowable temperature drops across the heat spreader and heat sink should always be made during the TEC selection process:

- The TEC hot side temperature should be determined as the sum of the typical allowable hot side temperature and the worst case ambient temperature, i.e. $T_{\text{hot}} =$ temperature drop due to heat sink thermal resistance + $T_{\text{amb}}$.
- The TEC cold side temperature is estimated as
$$
T_{\text{cold}} = T_{\text{load}} - \text{temperature drop due to thermal resistance of heat spreader}.
$$
- The temperature difference across the TEC ($\Delta T$) is calculated using
$$
\Delta T = T_{\text{hot}} - T_{\text{cold}}.
$$

Step 5: Define the minimum number of stages with which the required $\Delta T$ is to be met. As a rule of thumb, the maximum $\Delta T$ (i.e. $\Delta T_{\text{max}}$) achievable for 1, 2 and 3 stages are approximately 65 °C, 90 °C and 110 °C, respectively. The use of multiple stages can be complex as the TECs can be connected in different configurations (such as series or parallel), which can yield different cooling performances.

Step 6: Selection of appropriate TECs from different manufacturers. In this step, the normalized universal performance curve [7] provided by a TEC manufacturer (shown in Fig. 3) can be used to select the single or two stage TEC.

a. Determine the ratio of $\Delta T/\Delta T_{\text{max}}$. where $\Delta T$ is obtained from step 4 and $\Delta T_{\text{max}}$ is obtained from step 5.
b. In Fig. 3, draw a horizontal line on the graph corresponding to $\Delta T/\Delta T_{\text{max}}$.

![](./images/811944607985172480_6.jpg)

Fig. 3. Normalized universal curve of TEC provided by a TEC manufacturer.

c. Obtain the optimum value of $Q/Q_{\text{max}}$ at the intersection of the horizontal line just drawn and the diagonal optimum $Q/Q_{\text{max}}$ line. Obtain also the maximum value of $Q/Q_{\text{max}}$ at the intersection of the horizontal line (drawn in step b) and the right vertical axis.
d. Divide the total heat load (from step 1) by the $Q/Q_{\text{max}}$ ratio to calculate the optimum and maximum $Q_{\text{max}}$.

$$
\text{Optimum } Q_{\text{max}} = \frac{\text{Total heat load } (Q_{\text{c}})}{\text{(Optimum } Q/Q_{\text{max}})}
$$

$$
\text{Maximum } Q_{\text{max}} = \frac{\text{Total heat load } (Q_{\text{c}})}{\text{(Maximum } Q/Q_{\text{max}})}
$$

e. A TEC is normally identified with a rated $Q_{\text{max}}$, which is the maximum amount of heat that can be pumped at $\Delta T=0$ (i.e. $T_{\text{cold}}=T_{\text{hot}}$). Based on the values obtained in step (d), the TEC (or an array of TECs) can be selected so that maximum $Q_{\text{max}} <$ rated $Q_{\text{max}} <$ optimum $Q_{\text{max}}$. User preference can be exercised here. For conservative designs, it may be desirable to select a rated $Q_{\text{max}}$ that ranges from 1.5 to 2 times the maximum $Q_{\text{max}}$. This will ensure that the system is operated at no more than 50–75% of its rated $Q_{\text{max}}$ specification. However, such a design will not be optimal in terms of efficiency due to the conservative estimate of $\Delta T$ in step (4). A selection of TECs configuration with rated $Q_{\text{max}}$ that is close to the optimum $Q_{\text{max}}$ would provide the better efficiency, but often at a higher cost. A TEC with rated $Q_{\text{max}}$ close to the maximum $Q_{\text{max}}$ would be less efficient and possibly less expensive.

Steps 1–6 will give the designer a set of TECs from different manufacturers that would suit the application. Each TEC can be represented by a collection of characteristics data, which includes the model number, rated $Q_{\text{max}}$ (together with the TEC hot side temperature $T_{\text{hot}}$), rated $\Delta T_{\text{max}}$, rated $V_{\text{max}}$ (maximum voltage), rated $I_{\text{max}}$ (maximum current) and the dimensions. The set of suitable TECs could often be reduced based on the required dimensions.

To assist the designer further in the search, it will be necessary to compare the performances of TECs from different manufacturers using the characteristic parameters. This can be accomplished based on the model proposed by Lineykin et al. [8]. Using the performance data from the TEC manufacturer, such as $\Delta T_{\text{max}}$, $V_{\text{max}}$, $I_{\text{max}}$ and $T_{\text{hot}}$, the TEC device electrical resistance $R$, Seebeck coefficient $S$ and thermal resistance $\theta_{\text{TEC}}$ can be estimated as follows:

$$
R = \frac{V_{\text{max}}}{I_{\text{max}}} \frac{\left(T_{\text{hot}} - \Delta T_{\text{max}}\right)}{T_{\text{hot}}} \tag{1}
$$

$$
S = \frac{V_{\text{max}}}{T_{\text{hot}}} \tag{2}
$$

$$
\theta_{\text{TEC}} = \frac{\Delta T_{\text{max}}}{I_{\text{max}} V_{\text{max}}} \frac{2T_{\text{hot}}}{\left(T_{\text{hot}} - \Delta T_{\text{max}}\right)} \tag{3}
$$

Using the estimated values of $R$, $S$ and $\theta_{\text{TEC}}$, each TEC (derived in step 6) can be further evaluated as follows:

Step 7: Calculate the operating current $I$ and voltage $V$. Assuming the thermoelectric TEC can pump $Q_{\text{c}}$, the operating current of the TEC can be estimated by solving
$$
Q_{\mathrm{c}}=S T_{\mathrm{cold}} I-\frac{1}{2} I^{2} R-\frac{\Delta T}{\theta_{\mathrm{TEC}}}
\tag{4}
$$

The required voltage for the TEC can be calculated using
$$
V=S \Delta T+I R
\tag{5}
$$

Step 8: Find the TEC power and calculate the power dissipated into the heat sink. The TEC power $P$ can be found using
$$
P=I V
\tag{6}
$$

The power dissipated into the heat sink is given by
$$
Q_{\mathrm{h}}=Q_{\mathrm{c}}+P
\tag{7}
$$

If the heat sink thermal resistance $\theta_{\mathrm{HS}}$ and ambient temperature $T_{\mathrm{amb}}$ are available, then $T_{\mathrm{hot}}$ could be updated using
$$
T_{\mathrm{hot}}=T_{\mathrm{amb}}+Q_{\mathrm{h}}\left(\theta_{\mathrm{HS}}\right)
\tag{8}
$$

Based on the new $T_{\mathrm{hot}}$, $\Delta T=T_{\mathrm{hot}}-T_{\mathrm{cold}}$ can also be updated. In this case, steps 7 and 8 can be repeated until the value of $T_{\mathrm{hot}}$ does not change significantly. If no information is available for the heat sink, then $Q_{\mathrm{h}}$ can be used to guide the design for the heat exchanger.

Step 9: Determine the TEC coefficient of performance (COP). The coefficient of performance is the amount of heat pumped divided by the amount of supplied electrical power, i.e.
$$
\mathrm{COP}=\frac{Q_{\mathrm{c}}}{P}
\tag{9}
$$

After completing steps 7-9, the designer will have the predicted operating conditions of the TECs and their COPs.

Together with the TEC dimensions and costs, the information will allow the designer to make a proper comparison. The required TEC current and voltage can be used to select a suitable TEC driver. For safety reasons, it is recommended to choose a driver that provides at least 10% margin in both TEC current and voltage. If none of the available drivers is suitable, it may be necessary to select another TEC with different operating characteristics to match the voltage and current specifications for the available driver.

In the final selection of a suitable TEC, the designs of the heat spreader and heat sink together with the interface materials could be crucial. The sum of the thermal resistances should not be more than the estimated thermal resistance used in the procedures. If the heat spreader and heat sink designs yield excessive thermal resistances, it will be necessary to select another suitable TEC with the appropriate current and voltage.

### 3. Case study

Based on the procedures given in the previous section, the search and analysis of the TECs from different manufacturers can be conducted according to the flowchart shown in Fig. 4. In order to search and size a suitable TEC for a specific design requirement, the user needs to enter a minimum set of input data. These include ambient temperature ($T_{\mathrm{amb}}$), required design temperature for the load being cooled ($T_{\mathrm{load}}$) and the estimated amount of heat load ($Q_{\mathrm{c}}$). To implement the methodology, Fig. 3 was curve fitted, and a database of standard TEC information from four manufacturers was developed. The information in the database included the model number, rated $Q_{\text{max}}$, $\Delta T_{\text{max}}$, $V_{\text{max}}$, $I_{\text{max}}$, $T_{\text{hot}}$ and the TEC dimensions. This database can be extended to include other information such as costs and product data from other manufacturers

![](./images/811944607985172480_7.jpg)

Fig. 4. TEC search and analysis flowchart.

at a later stage. The search will first find the set of TECs based on the rated $Q_{\max}$ and $\Delta T$. The search result could be further constrained based on the required dimensions. The approach could check if the estimated value of the thermal resistance is acceptable for the cooling system to dissipate all the waste heat into the atmosphere. If the estimated thermal resistance is unacceptable, the actual value of thermal resistance that is required could be calculated. For example, if the estimated thermal resistance value of the heat sink is too high and the resultant temperature difference ($\Delta T$) across the entire heat sink is too large, then the thermal resistance can be progressively decreased until the minimum value for acceptance is attained. This would prevent thermal runaway of the system. The ultimate selection is based on the user preferences, which can include optimal thermal performance, cost etc.

The methodology was tested with a cooling system design case study. The case study involves finding suitable commercial TECs based on the following initial single stage cooler design specifications:

- The estimated heat load of the application to be cooled is $Q_{\mathrm{c}}=22\ \mathrm{W}$.
- The object to be cooled is in direct contact with the cold side of the TEC, which needs to be maintained at $5\ ^{\circ}\mathrm{C}$.
- A forced convection type heat sink is used. The thermal resistance of the heat sink is about $0.15\ ^{\circ}\mathrm{C/W}$. The ambient temperature is assumed to be $25\ ^{\circ}\mathrm{C}$.

The results obtained after step 6 indicated that the rated $Q_{\max}$ of the TEC for this application should be within $44\ \mathrm{W} < \text{rated } Q_{\max} < 88\ \mathrm{W}$. Table 1 shows the characteristics data of TECs from the four manufacturers with the required rated $Q_{\max}$ and footprint of $40\ \mathrm{mm} \times 40\ \mathrm{mm}$.

The electrical resistances $R$, Seebeck coefficients $S$ and thermal resistances $\theta_{\mathrm{TEC}}$ for the TECs in Table 1 were calculated using Eqs. (1)-(3). The results of the calculations are given in Table 2. Using Eqs. (4) and (5), the predicted performances of the TECs based on the calculated $R$, $S$ and $\theta_{\mathrm{TEC}}$ values were compared with the actual TEC characteristics obtained from the manufacturers. Figs. 5-7 show comparisons of the performance curves for models A2,

<table>
<caption>Table 1<br>Results for $40\ \mathrm{mm} \times 40\ \mathrm{mm}$ TEC with $44\ \mathrm{W} < \text{rated } Q_{\max} < 88\ \mathrm{W}$</caption>
<thead>
<tr>
<th>Manufacturer</th>
<th>Model</th>
<th>$Q_{\max}$ (W)</th>
<th>$I_{\max}$ (A)</th>
<th>$V_{\max}$ (V)</th>
<th>$\Delta T_{\max}$ ($^{\circ}\mathrm{C}$)</th>
<th>$T_{\text{hot}}$ ($^{\circ}\mathrm{C}$)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Company A</td>
<td>A1</td>
<td>51.4</td>
<td>6</td>
<td>15.4</td>
<td>67</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>A2</td>
<td>72</td>
<td>8.5</td>
<td>15.4</td>
<td>65</td>
<td>25</td>
</tr>
<tr>
<td>Company B</td>
<td>B1</td>
<td>60</td>
<td>6.1</td>
<td>15.9</td>
<td>70</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>B2</td>
<td>75</td>
<td>7.6</td>
<td>15.9</td>
<td>70</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>B3</td>
<td>76</td>
<td>7.9</td>
<td>15.7</td>
<td>69</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>B4</td>
<td>84</td>
<td>8.6</td>
<td>15.7</td>
<td>69</td>
<td>25</td>
</tr>
<tr>
<td>Company C</td>
<td>C1</td>
<td>57</td>
<td>6</td>
<td>17.5</td>
<td>71</td>
<td>25</td>
</tr>
<tr>
<td></td>
<td>C2</td>
<td>80</td>
<td>8.5</td>
<td>17.5</td>
<td>70</td>
<td>25</td>
</tr>
<tr>
<td>Company D</td>
<td>D1</td>
<td>54</td>
<td>5.6</td>
<td>14.7</td>
<td>66</td>
<td>27</td>
</tr>
<tr>
<td></td>
<td>D2</td>
<td>71</td>
<td>7.4</td>
<td>14.7</td>
<td>66</td>
<td>27</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>Calculated $R$, $S$, and $\theta_{\mathrm{TEC}}$ for the TECs</caption>
<thead>
<tr>
<th>Model</th>
<th>$R$ ($\Omega$)</th>
<th>$S$ (V/K)</th>
<th>$\theta_{\mathrm{TEC}}$ (K/W)</th>
</tr>
</thead>
<tbody>
<tr>
<td>A1</td>
<td>1.9896</td>
<td>0.0517</td>
<td>1.8708</td>
</tr>
<tr>
<td>A2</td>
<td>1.4166</td>
<td>0.0517</td>
<td>1.2702</td>
</tr>
<tr>
<td>B1</td>
<td>1.9943</td>
<td>0.0534</td>
<td>1.8866</td>
</tr>
<tr>
<td>B2</td>
<td>1.6007</td>
<td>0.0534</td>
<td>1.5143</td>
</tr>
<tr>
<td>B3</td>
<td>1.5272</td>
<td>0.0527</td>
<td>1.4479</td>
</tr>
<tr>
<td>B4</td>
<td>1.4029</td>
<td>0.0527</td>
<td>1.3300</td>
</tr>
<tr>
<td>C1</td>
<td>2.2218</td>
<td>0.0587</td>
<td>1.7754</td>
</tr>
<tr>
<td>C2</td>
<td>1.5752</td>
<td>0.0587</td>
<td>1.2301</td>
</tr>
<tr>
<td>D1</td>
<td>2.0475</td>
<td>0.0490</td>
<td>2.0558</td>
</tr>
<tr>
<td>D2</td>
<td>1.5495</td>
<td>0.0490</td>
<td>1.5557</td>
</tr>
</tbody>
</table>

B4 and D1, respectively. The results indicated that the predictions based on the calculated $R$, $S$ and $\theta_{\mathrm{TEC}}$ values are generally quite accurate for operating current up to about two thirds of $I_{\max}$. The error increases for operating current near $I_{\max}$ and higher $\Delta T$. This could be attributed to the temperature dependency of the thermocouples, which can affect the $R$, $S$ and $\theta_{\mathrm{TEC}}$ values. It is envisaged that the higher errors at elevated temperature difference will not be crucial as most designs would incorporate safety margins so that the operation would lie within 50-75% of the maximum bandwidth. Table 3 shows the predicted operating current, voltage and COP using Eqs. (4)-(9) and the comparison of these values with those recommended by the TEC manufacturers. The results indicated that the approach can give fairly good prediction of the actual operating conditions and COP. These estimated values could be used to guide the TEC selection. For example, the COP could be used as an indication of the operating cost, and this could be weighted against the operating conditions and TEC cost.

## 4. Discussions and framework for future extension

The methodology developed in this work aims to facilitate and accelerate the design process by giving the users a consistent search strategy and the choices of appropriate TECs from different TEC manufacturers. It is envisaged that the approach can be further improved to facilitate the designer tasks. These improvements include customiza-

# Performance Curves - Th = 25°C

![](./images/811944607985172480_8.jpg)

Fig. 5. Comparison of performance curves for model A2.

tions for specific cooling system prototypes, optimization of the thermal performance etc. The methodology can also be extended and implemented on the Internet to allow designers to source and procure commercially available TEC components.

The Internet based TEC sizing and selection system would create new paradigms for interaction between designers and manufacturers. Fig. 8 illustrates the proposed information flow between the manufacturers and designers via the web based thermoelectric cooling system design process. The information framework would provide designers the ability to customize electronically virtual prototypes of their thermoelectric cooling system designs through the Internet and receive real time responses regarding the prices and delivery dates for the desired TEC components. If the design performances and terms are acceptable, the designer can place an order to the TEC manufacturer, who can utilize the business information for production planning. The TEC manufacturers can also utilize the data for their enterprise resource planning and supply chain management. This process promotes active interaction between designers and TEC manufacturers to develop collaboratively the cooling system. Through the framework, the TEC manufacturers will be able to provide up to date information on their products and logistic support to their customers. In this aspect, a shared knowledge database shown in Fig. 8 could be established by the TEC manufacturer as a repository for technical information, business performances and customer feedback to facilitate continuous process improvement.

In terms of thermoelectric cooling system design, simulating complex configurations under different environmental conditions could be more cost effective, and the analysis could be more comprehensive than testing physical prototypes. For the proposed framework in Fig. 8 to function effectively, the framework could provide more facilities for the designers to develop and analyze thermoelectric cooling system design. For example, there has been renewed interest in the optimization of thermoelectric coolers [9-12]. These design tools could be incorporated into

![](./images/811944607985172480_9.jpg)

Fig. 6. Comparison of performance curves for model B4.

![](./images/811944607985172480_10.jpg)

Fig. 7. Comparison of performance curves for model D1.

the framework. This creation will permit designers to develop thermoelectric cooling systems in minimal time using the latest TEC components on the market. This is an increasingly critical factor. Many companies have real- ized that the first to get the new design to the market often wins the race.

### Table 3
Comparison of currents and voltages between predicted and manufacturer data

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th colspan="4">Predicted</th>
      <th colspan="4">From TEC manufacturers</th>
    </tr>
    <tr>
      <th></th>
      <th>$T_{\text{hot}}$ (°C)</th>
      <th>$I$ (A)</th>
      <th>$V$ (V)</th>
      <th>COP</th>
      <th>$T_{\text{hot}}$ (°C)</th>
      <th>$I$ (A)</th>
      <th>$V$ (V)</th>
      <th>COP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A1</td>
      <td>32.2</td>
      <td>3.3</td>
      <td>8.0</td>
      <td>0.84</td>
      <td>33</td>
      <td>3.5</td>
      <td>8.5</td>
      <td>0.74</td>
    </tr>
    <tr>
      <td>A2</td>
      <td>31.9</td>
      <td>3.7</td>
      <td>6.6</td>
      <td>0.91</td>
      <td>32</td>
      <td>3.9</td>
      <td>7</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>B1</td>
      <td>31.8</td>
      <td>3.1</td>
      <td>7.6</td>
      <td>0.95</td>
      <td>32</td>
      <td>3.1</td>
      <td>7.8</td>
      <td>0.91</td>
    </tr>
    <tr>
      <td>B2</td>
      <td>31.5</td>
      <td>3.2</td>
      <td>6.6</td>
      <td>1.04</td>
      <td>32</td>
      <td>3.5</td>
      <td>7</td>
      <td>0.90</td>
    </tr>
    <tr>
      <td>B3</td>
      <td>31.5</td>
      <td>3.3</td>
      <td>6.5</td>
      <td>1.02</td>
      <td>32</td>
      <td>3.5</td>
      <td>6.5</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>B4</td>
      <td>31.5</td>
      <td>3.4</td>
      <td>6.2</td>
      <td>1.04</td>
      <td>32</td>
      <td>3.8</td>
      <td>6.5</td>
      <td>0.89</td>
    </tr>
    <tr>
      <td>C1</td>
      <td>31.6</td>
      <td>2.8</td>
      <td>7.8</td>
      <td>1.01</td>
      <td>31.6</td>
      <td>3.1</td>
      <td>8.5</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>C2</td>
      <td>31.3</td>
      <td>3.1</td>
      <td>6.5</td>
      <td>1.08</td>
      <td>31.3</td>
      <td>3.5</td>
      <td>7.5</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>D1</td>
      <td>33.0</td>
      <td>3.6</td>
      <td>8.7</td>
      <td>0.71</td>
      <td>32.9</td>
      <td>3.5</td>
      <td>8–10</td>
      <td>0.69</td>
    </tr>
    <tr>
      <td>D2</td>
      <td>32.1</td>
      <td>3.7</td>
      <td>7.0</td>
      <td>0.86</td>
      <td>32.5</td>
      <td>3.9</td>
      <td>6.5–8.5</td>
      <td>0.75</td>
    </tr>
  </tbody>
</table>

![](./images/811944607985172480_11.jpg)

Fig. 8. Framework for Internet based thermoelectric cooling system design process.

## 5. Conclusion

TEC selection is one of the most important processes in the design of thermoelectric cooling systems. To assist the designer, this paper presents a methodology to size, search and compare TECs from different TEC manufacturers. The study shows that basic TEC data consisting of the rated pumping power, maximum temperature difference, rated temperature, maximum current and voltage can be used to approximate and compare the performances of products from different TEC manufacturers. An important application of this methodology is the development of a new operational framework for an Internet based thermoelectric cooling system design process that would promote interaction and collaboration between the designers and TEC manufacturers. It is hoped that the considerations and discussions in this paper may enable the advancement of better computer aided tools to assist the designers in the development, analysis, and optimization of thermoelectric cooling systems in minimal time using the latest TECs available on the market.

## Acknowledgements

The authors would like to acknowledge the work of Nanyang Technological University graduate student, T.S. Maung, for his contribution on the software development.

## References

[1] Phelan PE, Chiriac VA, Lee TY. Current and future miniature refrigeration cooling technologies for high power microelectronics. IEEE Trans Component Packag Technol 2002;25:356–65.

[2] Riffiat SB, Ma X. Thermo-electrics: a review of present and potential applications. Appl Therm Eng 2003;23:913–35.

[3] Chein R, Huang G. Thermoelectric cooler application in electronic cooling. Appl Therm Eng 2004;24:2207–17.

[4] Fukutani K, Shakouri A. Design of bulk thermoelectric modules for integrated circuit thermal management. IEEE Trans Component Packag Technol 2006;29:750–7.

[5] Rowe DM, Bhandari CM. Modern thermoelectrics. Virginia, USA: Reston Publishing Company; 2000.

[6] Rowe DM. CRC handbook of thermoelectrics. Boca Raton, FL: CRC Press; 1995.

[7] Buist RJ. Universal thermoelectric design curves. In: The 15th intersociety energy conversion engineering conference; 1980.

[8] Lineykin S, Ben-Yaakov S. Analysis of thermoelectric coolers by a spice-compatible equivalent 0 circuit model. IEEE Power Electron Lett 2005;3:63–6.

[9] Xuan XC. On the optimal design of multistage thermoelectric coolers. Semiconduct Sci Technol 2002;17:625–9.

[10] Yang R, Chen G, Snyder GJ, Fleurial J-P. Multistage thermoelectric microcoolers. J Appl Phys 2004;95:8226–32.

[11] Cheng Y, Shih C. Optimizing the arrangement of two-stage thermoelectric coolers through a genetic algorithm. JSME Int J, Series B (Fluids Therm Eng) 2006;49:831–8.

[12] Chen J, Chen X, Lin B. The parametric optimum design of a new combined system of semiconductor thermoelectric devices. Appl Energy 2006;83:681–6.