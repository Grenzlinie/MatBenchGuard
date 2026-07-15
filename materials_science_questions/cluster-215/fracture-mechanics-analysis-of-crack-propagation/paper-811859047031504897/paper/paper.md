# Determination of masonry crack evolution due to differential displacements: a numerical study*

A.M. FATHY¹·², J. PLANAS¹ and J.M. SANCHO³

¹Departamento de Ciencia de Materiales, E.T.S. de Ingenieros de Caminos, Canales y Puertos, Universidad Politécnica de Madrid, C/Profesor Aranguren s/n, 28040 Madrid, Spain, ²Faculty of Engineering, Ain Shams University, Abdo Basha, Cairo, Egypt, ³Universidad CEU-San Pablo, Escuela Politécnica Superior, Campus de Montepríncipe, Boadilla del Monte, 28668 Madrid, Spain

Received in final form 04 March 2009

## ABSTRACT
Brick walls of ceramics without any mortar covering or paint are used extensively in building façades in Spain. One of the most used masonry wall systems is based on non-bearing panels partially supported, about two-thirds of the brick width, over the edge beams of the structural skeleton. The edge beam is veneered with special thinner bricks to achieve the visual continuity of the façade. A considerable number of these walls show cracking. In a previous work, finite element simulations were performed in order to gain insight into the causes of cracking. A special finite element, based on the strong discontinuity analysis and the cohesive crack theory, is used in the numerical simulations. The results agree with the overall cracking patterns observed but if an imposed displacement is applied in the range allowed by the standards, extensive cracking occurs. This implies that the design displacements are not the actual ones. In this work, an elastic study using the principle of superposition is used to determine the effective deflections under service loading. Then, these deflections are applied to the structure and the evolution of cracking is studied. This study shows that the masonry panels of the first and last store have the major probability of cracking. Another parametric study is carried out changing the elastic and tensile properties of the masonry. This study shows that although the cracking of the masonry panels starts at different loads for different tensile properties, the crack patterns are similar for a given panel geometry and loading. This numerical study provides a method of design to determine the crack width for different geometries, loadings and fracture properties.

Keywords cohesive crack; crack control; finite elements; fracture; masonry; masonry façades.

## NOMENCLATURE
$E$ = elastic modulus
$f_\text{t}$ = tensile strength
$G_\text{F}$ = fracture energy
$h$ = panel height
$\lambda$ = panel length
$\lambda_\text{ch}$ = characteristic length
$p_\text{s}$ = slab own weight per unit length of the edge beam
$p_\text{m}$ = average masonry panel weight per unit horizontal length
$p_\text{r}$ = roof masonry protection wall weight per unit horizontal length
$p_\text{f}$ = flooring weight per unit length of the edge beam
$p_\text{l}$ = live load per unit length of the edge beam
$p_\text{lr}$ = roof live load per unit length of the edge beam

*This manuscript is based on a presentation made at the XXV Spanish Fracture Group Meeting in Sigüenza 2008.

Correspondence: A. M. Fathy. E-mail: adel@mater.upm.es

$u$ = imposed displacement at the centre of the beam
$u^{(i)}$ = displacement at a given point for case (i) where i equals a, b or c (related to the sequence of construction)
$u^{(j)}$ = displacement at a given point for load case (j) where j equals 1–7 (related to superposed loading cases)
$w_{\text{max}}$ = the maximum crack width for a given displacement
$y$ = the distance from the surface of the beam in contact with the masonry to the beam neutral line
$\varepsilon\left(t\right)$ = creep strain at time $t$
$\phi\left(t,t'\right)$ = creep compliance function between time $t$ and $t'$

## INTRODUCTION
In the last decade, the price of residential flats raised considerably in Spain. One of the consequences was the reduction of the time employed in the building process. One of the most used construction systems for residential buildings is based on a skeleton of reinforced concrete or steel columns with reinforced concrete uni- or bidirectional slabs. Masonry walls are used as partitions and the façade is usually constructed partially supported, about two-thirds of the brick width, over the end beams. The good quality and appearance of the ceramic masonry unit used lead to intensive use of this type of exterior walls without mortar cover or paint.

There are no Spanish standards for this construction system. Usually, the standards NBE_FL90, NTE-FFL and NTE EFL are used. The first gives instructions about the properties of the mortar and masonry units used in bearing walls and the last two standards provide rules for the structural design of bearing walls. A considerable number of these buildings show cracking in different zones of the façade walls. As a result of the lack of standards, each construction company uses its own experience to prescribe the necessary recommendations to minimize the width and extension of the cracks. There are many possible load patterns that can cause such cracks. The authors developed a special finite element, based on the strong discontinuity approach and the cohesive crack theory, that is very effective in the numerical simulation of cracking in quasi brittle materials such as concrete and masonry. The authors applied such element to the analysis of the cracks appearing in the foregoing masonry walls in order to have a better understanding of the cracking phenomena. Detailed notices about this element can be found in Refs [1–3]. In previous work,⁴·⁵ the steps taken to incorporate this element in a finite element program and test its efficiency to detect cracked zones were explained. But one of the conclusions of that study was that the deflections allowed by standards seem to be design values rather than the real or average ones. The program is applied to a typical structure loaded with service-imposed deformations to gain a better understanding of the cracking phenomena and to devise a method that can be used in the design of this type of façades.

## NUMERICAL MODEL USED
The cohesive crack model, first introduced by Hillerborg for concrete⁶ and later used for other quasibrittle materials,⁷ has laid the way to the appearance of many models that study crack propagation in such materials. In the 1980s, there were two paradigmatic approaches to modelling fracture of quasibrittle materials at a structural level: the discrete crack approach and the smeared crack approach. Typically, the former used inter-element cracking with cohesive interface elements and, eventually, remeshing algorithms, while the latter used intra-element cracking with the crack displacement continuously distributed over the finite element and thus implemented as a continuous strain. Although the smeared approach was clearly the easiest to implement in commercial FEM codes, the discrete approach could also be handled in such kind of programs. For a deeper discussion about these issues, see Ref. [7] (sections 7.2.3, 8.6 and 8.7). In the last 10 or 15 years, other methods have been developed based, roughly speaking, on letting displacement discontinuities to lay and grow in a standard finite element mesh. Two basic families of procedures exist: those in which the displacement discontinuities (crack openings) appear as global degrees of freedom, and those in which the crack openings are local to the finite elements and can be solved at the element level.

The model used in this work, developed by the last two authors, has the following essential ingredients:

1.  Strong discontinuity kinematics (a displacement jump along a line inside the element).
2.  Simple cohesive crack with central forces (traction and crack opening vectors collinear).

3 Simple element formulation: constant strain elements, triangles or tetrahedra.
4 Local crack equilibrium solved at the element level without static condensation.
5 Crack is given limited local adaptability.

Reference [1] provides detailed information about the model.

# STRATEGY OF THE WORK

In previous work, $^{4,5}$ the steps taken to incorporate the model in a finite element program and test its efficiency to detect cracked zones were explained. To speed up the initial development, a combination of ready-to-use programs was used: (1) a user-defined finite element incorporating the cohesive crack was developed using OOP and C++ in the open source finite element program FEAP;$^{8}$ (2) the mesh was generated first using the pre-processor of the commercial finite element program ANSYS$^{9}$ and then converting the output file to the FEAP input format using a translator program written by the authors.

Because the interfacing of the FORTRAN code of FEAP and the C++ code used by the authors to support tensor and vector algebra was somewhat difficult to maintain due to the different format of data structures, a full featured finite element program was developed by the authors using C++ and OOP that fully supports the tensor and vector algebra used in Continuum Mechanics, and so was called COFE (Continuum Oriented Finite Elements). The pre-and post-processing as well as dynamic (real computation time) graphical display of the results is carried out using GMSH$^{10}$ an open source program.

In previous work, $^{4,5}$ it was shown that confined wall panels experiment extensive cracking when they are submitted to boundary displacements imposed by the confining frame up to the maximum beam deflections allowed by codes. In fact, it is obvious that a quasibrittle material such as masonry cannot accommodate differential deflections of, say, 10 mm over 5 m without cracking, either internally or at the interface with the frame.

It then become obvious that the *design* (i.e. computed) beam deflection in the codes represents an ultimate service state that is an upper bound of those that might occur, but is very far from *actual, average* deflections. Building practice, through the committees for standards in each country, has set the allowable value for the design deflection to avoid functional problems, in particular to avoid visible cracks on internal masonry walls. To study the cracking process of a typical confined wall panel, it is essential to determine the maximum real expected displacement it can undergo.

So, as a first step, an elastic-viscoelastic study using the principle of superposition is used to determine the effective beam deflections under service loading; the stiffness of panels is taken into account in the calculations. It is shown that the study of seven patterns of loading is required to determine the effective deflections of the structure when the construction loading sequence is taken into account.

In a second step, these calculated deflections are applied to separate typical panels as imposed displacement with fourth degree polynomial distribution to study the cracking process.

Finally, a parametric study applied to the critical panel is carried out by changing the material properties of the masonry; dimensionless curves are drawn that relate the material properties, the beam deflection at its centre and the maximum crack width (maximum among all the active cracks). Those curves clearly show the point of crack initiation, the evolution of maximum crack width and a *saturation range* in which the maximum crack opening is roughly proportional to the deflections of the confining beams independently of the material properties.

# CALCULATING REAL DEFLECTIONS

## Procedure of the work

As mentioned before, an elastic study using the principle of superposition is used to compute the short-term deformations arising along the building process which is then extended using the elastic-viscoelastic analogy—also known as the correspondence principle—to extend the solution to long-term deflections.

To do this, a series of data have to be assumed for the geometry of the building, the service loads and the sequence of construction. A typical building of four storeys is studied. A vertical expansion joint in the masonry wall, every two panels, is supposed to exist. It is also assumed that there are large number of panels in both left and right directions, so that the mid-plane between expansion joints is a symmetry plane. Common masonry panel geometry, selected by a consulting office for a large number of construction companies in Spain, is used. Figure 1 shows the geometrical details of one half of the masonry panel unit of the five-story building analysed and the boundary conditions the right half part of a vertical unit between expansion joints. The left vertical line is the symmetry plane, which thus has horizontal displacements impeded and zero vertical load, both in the masonry and in the frame. The right vertical line coincides with the expansion joints in the masonry; therefore, the horizontal displacement is restricted for the frame while the masonry is subjected to zero tractions along this boundary.

Figure 2 shows the loading cases needed for the elastic calculation. Let $u^{(i)}$ be the displacement at a given point for case (i), then, if the sequence of construction is supposed to be as follows:

![](./images/811859047031504897_1.jpg)

Fig. 1 Dimensions of the masonry panel
and boundary conditions on the vertical
structural unit.

(a) constructing all the concrete skeleton;
(b) constructing all the masonry panels starting from down-
stairs floors: (b1) panel on the first floor finished, (b2)
panel on the second floor finished, (b3) panel of the
third floor finished, (b4) panel of the fourth floor fin-
ished, (b5) protection wall on the roof floor finished;
and
(c) finishing the building process, flooring and life loads are
applied.

Then the elastic displacement at the end of the various
stages would be as follows:
$$u^{(\mathrm{a})}=p_{\mathrm{s}} u^{(6)} \quad(1)$$

$$u^{(\mathrm{b} j)}=p_{\mathrm{s}} u^{(6)}+p_{\mathrm{m}}\left(u^{(1)}+\cdots+u^{(j)}\right) \quad j=1, \ldots, 4 \quad(2)$$

$$u^{(\mathrm{b} 5)}=p_{\mathrm{s}} u^{(6)}+p_{\mathrm{m}}\left(u^{(1)}+u^{(2)}+u^{(3)}+u^{(4)}\right)+p_{\mathrm{r}} u^{(5)} \quad(3)$$

$$\begin{aligned}
u^{(\mathrm{c})}= & p_{\mathrm{s}} u^{(6)}+p_{\mathrm{m}}\left(u^{(1)}+u^{(2)}+u^{(3)}+u^{(4)}\right)+p_{\mathrm{r}} u^{(5)} \\
& +\left(p_{\mathrm{f}}+p_{\mathrm{l}}\right) u^{(7)}+\left(p_{\mathrm{lr}}-p_{\mathrm{l}}\right) u^{(5)},
\end{aligned}\qquad(4)$$

where $p_{\mathrm{s}}=$ slab own weight per unit length of edge beam,
$p_{\mathrm{m}}=$ average masonry panel weight per unit horizontal
length, $p_{\mathrm{r}}=$ roof masonry protection wall weight per unit
horizontal length, $p_{\mathrm{f}}=$ flooring weight per unit length
of the edge beam, $p_{1}=$ live load per unit length of the
edge beam and $p_{\mathrm{lr}}=$ roof live load per unit length of
the edge beam; it is assumed that the flooring weight
is the same in all floors, including the roof one; if re-
quired, the difference may be taken into account in the last
term.

A life load of $2 \mathrm{kN} / \mathrm{m}^{2}$, slab own weight of $2.5 \mathrm{kN} / \mathrm{m}^{2}$ and
flooring cover load of $1.5 \mathrm{kN} / \mathrm{m}^{2}$ are assumed. Also the
weight of the masonry panel is taken as $3000 \mathrm{~N} / \mathrm{m}^{2}$. Slab
dimensions between frames are taken to be $5.00 \times 5.40 \mathrm{~m}$.
The concrete column's dimensions are taken as $400 \times$
400 mm for the ground and first floor, and $300 \times$
300 mm for other floors. A 300-mm-thick slab is used.
A steel angle of $100 \times 100 \times 10 \mathrm{~mm}$ is used for the win-
dow lintel and round bars of 10 mm diameter for ties.
The concrete beams are 500 mm in width and 300 mm in
depth. Also, the modulus of elasticity of 200, 30 and 3 GPa
was used for steel, concrete and homogenized masonry,
respectively. Equivalent 2D dimensions and stiffnesses
were calculated. Square elements were used for lintel and
beam sections with sides 50 and 75 mm, respectively. Tri-
angle elements were used for the masonry panels. The
size is kept about 50 mm (on the edges that are not con-
nected to the lintel or beam) and grows progressively up to
100 mm in the zones far from the edges.

To take into account the deferred displacements due to
creep, a simplified viscoelastic model has been used, which
allows using the elastic-viscoelastic equivalence. Consider
a structure build with various viscoelastic materials all
having proportional creep compliance function, that is,
the uniaxial creep strain of any of the materials can be
written in the form
$$\varepsilon(t)=\int_{0}^{t} \varphi\left(t, t^{\prime}\right) \frac{1}{E_{\mathrm{m}}} d \sigma\left(t^{\prime}\right),\qquad(5)$$

where the only difference between the materials is a ref-
erence elastic modulus $E_{\mathrm{m}}$, the dimensionless creep com-
pliance function $\phi(t, t^{\prime})$ being the same for all of them. If,

![](./images/811859047031504897_2.jpg)

Fig. 2 Loading cases required for the calculations.

furthermore, Poisson' ratio is constant for each material, then, for a structure composed of several such materials, if the elastic displacement at any given point computed with elastic moduli $E_{\mathrm{m}}$ in response of a loading process $P(t)$ is $u^{\mathrm{el}}(t)$, then the corresponding viscoelastic displacement at time $t$ is given by

$$
u(t)=\int_{0}^{t} \varphi\left(t, t^{\prime}\right) d u^{\mathrm{el}}\left(t^{\prime}\right). \tag{6}
$$

Then, if all the loading takes place in a relatively short time interval $\left[t_{0}, t_{1}\right]$ so that the creep compliance at time $t_{0}, \phi\left(t, t_{0}\right)$, does not differ much from that at $t_{1}, \phi\left(t, t_{1}\right)$, then we can approximate the result as

$$
\begin{aligned}
u(t) &=\int_{t_{0}}^{t_{1}} \phi\left(t, t^{\prime}\right) d u^{\mathrm{el}}\left(t^{\prime}\right) \approx \phi\left(t, \bar{t}_{0}\right) \int_{t_{0}}^{t_{1}} d u^{\mathrm{el}}\left(t^{\prime}\right) \\
&=\phi\left(t, \bar{t}_{0}\right) u^{\mathrm{el}}\left(t_{1}\right) \text { with } \bar{t}_{0} \in\left[t_{0}, t_{1}\right] \text { and } t \geq t_{1},
\end{aligned} \tag{7}
$$

where $\bar{t}_{0}$ may be understood as an average time of loading.
We can renormalize the elastic moduli and creep function so that $E_{\mathrm{m}}=\phi\left(t_{1}, \bar{t}_{0}\right) E_{\mathrm{m}}^{*}$ and $\phi^{*}\left(t, t^{\prime}\right)=\phi\left(t, t^{\prime}\right) / \phi\left(t_{1}, \bar{t}_{0}\right)$ so that the short-term displacement $u\left(t_{1}\right)$ coincides with the corresponding elastic displacement computed with elastic moduli $E_{\mathrm{m}}^{*}$, and so the short- and long-time $(t \rightarrow \infty)$ loadings are

$$
u_{\mathrm{st}}=u^{\mathrm{el}^{*}}, \quad u_{\infty}=\varphi_{\infty}^{*} u^{\mathrm{el}^{*}},
$$

where $\phi_{\infty}^{*}=\phi^{*}\left(\infty, \bar{t}_{0}\right)$ is the creep factor.

This is a rough approximation, as the strict proportionality of creep compliance functions in the short term is impossible to meet exactly for ageing materials that are cast at different times, although it can be met approximately if the loading of each component takes place after a reasonable amount of maturity is achieved. However rough, it is premature at this moment to try to put

© 2009 Blackwell Publishing Ltd. Fatigue Fract Engng Mater Struct 32, 430-440

forward a more sophisticated model as little is known about the creep compliance of the specific type of ma- sonry used in the construction under study, and as the objective is to get an estimate of the importance of the active deflections for the various panels in the building. Lacking specific data, we follow the recommendation of the Spanish Standard for the design of concrete structures and take $\phi_{\infty}^{*}=2(^{11}$ , section 50.2.2.3).

## Calculation results
Elastic computations for the seven cases shown in Fig. 2 were carried out using ANSYS with the boundary condi- tions depicted on the right of Fig. 1. These results were fed to Eqs (1)-(4) to compute the displacement at each build- ing stage and the creep factor was applied to the final displacements to get the final long-term displacements. The effective displacements of the beams are calculated as the total ones minus the displacement produced till the construction of each masonry panel. The effective deflec- tions are calculated as the total effective ones minus the shortening of the columns.
Figure 3 shows the computed long-term displacements of the beams in each floor. Figure 3a shows the total dis- placement while Fig. 3b shows the effective displacement and deflection.

## Discussion
From this part of the work, it can be noticed that the max- imum total displacement occurs in the last floor because it is affected by the column's shortening in all floors while the total maximum deflection occurs in the first floor and does not exceed 2.4 mm. The maximum shortening of columns occurs in the first floor also with a value of about1.1 mm. This large value of shortening is of the same order as the beams deflection. The maximum effective deflection, which controls the cracking, occurs in the first floor, with a value less than 1.5 mm.

## STUDY OF THE CRACKING PHENOMENON

### Procedure of the study
After calculating the effective displacements with the fore- going elastic study, these displacements are applied sepa- rately to each panel and a nonlinear calculation is carried out using the embedded cohesive crack model described in section 'Numerical Model Used' to study the cracking process. Half of the panel between vertical joints was anal- ysed as those shown in Fig. 2. The panels were subjected to the following boundary conditions: (1) zero horizontal displacement and zero vertical traction on the left ver- tical side; (2) free border (zero tractions) on the right side; (3) imposed displacements proportional to the ef- fective displacements computed in section 4 on the lower and upper sides of the panel; both vertical and horizontal displacements were imposed. (Note that the horizontal displacements were not shown in the previous section be- cause they are much less than the vertical components; previous work $^{4,5}$ showed, however, that they do influence the peripheral crack pattern and that they are basically induced by the rotation of the cross-section of the beam and so they are roughly proportional to $y \partial u / \partial x$ , where $u$ is the vertical displacement along the neutral line of the beam and $y$ the distance from the surface of the beam to the neutral line; smaller contributions arise due to shearstresses.)

![](./images/811859047031504897_3.jpg)
Fig. 3 Total and effective displacements and deflection for the beams in all floors.

Masonry is a brittle material whose fracture properties are not very well known, and different approaches to de- scribe the cracking behaviour can be found in the liter- ature. Some analytical papers $^{12-14}$ use the homogeniza tion technique to give relations between the strength of the masonry unit and mortar with the overall strength of the wall. The same concept was investigated experimen- tally $^{15,16}$ for concrete blocks. As the masonry wall is a

non-isotropic material, several works investigate the strength of the masonry wall at varying directions with the bed joint.¹⁷ The results overall support the idea that an equivalent homogeneous material can be used for masonry walls. The equivalent strength depends on the strength of the unit and mortar as well as on the direction of the loading with respect to the bed joint, and strength changes with orientation up to about 20% have been recorded.¹⁷ To keep the analysis simple, and as a first approximation, homogenous isotropic material is assumed for the masonry wall with a modulus of elasticity of 3 GPa, fracture energy of 100 N/m and tensile strength of 1.0 MPa; an exponential softening is used for the cohesive crack (see Ref. [7], section 7.2).

## Results
Figure 4 shows the crack patterns for each floor after exposing the structure to the maximum service loads as described in section 'Calculating Real Deflections'. As can be noted from the figure, the cracks occur at the same position in all the floors (at the window corners), and, as expected from the results in the previous section, the first floor suffers the largest cracks followed by the last floor. The intermediate floors hardly suffer cracks. Thus, in the following, we are going to concentrate on the panels in the first floor which are those most severely cracked.

![](./images/811859047031504897_4.jpg)

Fig. 4 Crack patterns in all floors of the building under long-term service loads.

## PARAMETRIC STUDY
### Basis for the parametric analysis
As it transpires from the preceding analysis, there is a great deal of uncertainty in the whole data chain required to carry out accurate predictions of the cracking of a brick masonry façade, and the most scientific approach is, to our understanding, to try to ascertain the influence of a few key parameters on the cracking behaviour of the façade. The driving force is taken here to be the effective displacements of the slabs which can be characterized by a unique parameter if one accepts that the distribution of the displacements on the upper and lower sides of a panel, both horizontal and vertical, are proportional to the elastic-viscoelastic solution proposed in section 'Calculating Real Deflections' in which it is worth noting that the absolute values of the displacements are not important as they are allowed to vary proportionally: only their ratios are important. Apart from this, the material elastic and fracture parameters are rarely known with enough accuracy, and so it is useful to let the independent material parameters to vary so that in any particular case, we can find the right solution among the set of solutions provided in the parametric study. Now, the results we seek are basically the cracking pattern (which is usually rather insensitive to the detailed material properties over wide ranges when the boundary conditions are proportional) and, most importantly, the maximum crack width, which will dictate the response of the owner. Therefore, we design the parametric study to trace the general cracking patterns and the maximum crack width as a function of the applied proportional boundary conditions and the masonry material properties (the concrete material properties, basically its elastic modulus, are 'dumped' in the boundary conditions outputted by the procedure described in section 'Calculating Real Deflections').

Based on the concepts developed in Ref. 7 (chapter 7), it can be shown from dimensional analysis and cohesive crack properties that, for geometrically similar panels, the maximum crack width $w_{\text{max}}$ for a given displacement level

<table>
<caption>Table 1 Values of the material parameters used throughout the computations</caption>
<thead>
<tr>
<th rowspan="2">$G_{F}=100$ N/m</th>
<th colspan="2">$\frac{G_{F}}{f_{\mathrm{t}}}$</th>
<th colspan="3">$\lambda_{\mathrm{ch}}$ (mm)</th>
</tr>
<tr>
<th colspan="2">($\mu$m)</th>
<th>$E=2.0$ GPa</th>
<th>$E=3.0$ GPa</th>
<th>$E=4.0$ GPa</th>
</tr>
</thead>
<tbody>
<tr>
<td>$f_{\mathrm{t}}$ (MPa)</td>
<td>0.50</td>
<td>200</td>
<td>800</td>
<td>1200</td>
<td>1600</td>
</tr>
<tr>
<td></td>
<td>1.00</td>
<td>100</td>
<td>200</td>
<td>300</td>
<td>400</td>
</tr>
<tr>
<td></td>
<td>1.50</td>
<td>67</td>
<td>89</td>
<td>133</td>
<td>178</td>
</tr>
</tbody>
</table>

must follow an equation of the form

$$
w_{\max }=\frac{G_{\mathrm{F}}}{f_{\mathrm{t}}} \Phi\left(\frac{u f_{\mathrm{t}}}{G_{\mathrm{F}}}, \frac{h}{\lambda_{\mathrm{ch}}}\right) \quad \text { with } \quad \lambda_{\mathrm{ch}}=\frac{E G_{F}}{f_{\mathrm{t}}^{2}}. \quad (8)
$$

$\lambda_{\mathrm{ch}}$ is the characteristic length, $u$ is the displacement factor (made to coincide with the effective vertical displacement at the centre of the beam supporting the panel) and $h$ is the panel height, its length $\lambda$ being proportional to $h$ according to geometrical similarity. According to this, the result for any combination of material properties can be defined by two material ratios, namely $G_{\mathrm{F}}/f_{\mathrm{t}}$ and $\lambda_{\mathrm{ch}}$. Thus, we need to vary only two material properties to capture the behaviour for any material and geometrically similar panel.

As shown in section 'Study of the Cracking Phe- nomenon', the first floor is the floor that suffers the max- imum cracking, so in the parametric study, this floor is considered. The fracture energy was kept constant, while, as shown in Table 1, the tensile strength and the elastic modulus were changed in $\pm 50\%$ of the values considered in the previous computations. This leads to three differ- ent values of $G_{\mathrm{F}}/f_{\mathrm{t}}$, ranging from 67 to $200\ \mu$m, and to nine values of $\lambda_{\mathrm{ch}}$, ranging from 89 to 1600 mm, as shown in Table 1.

## Results

Figures 5 and 6 show the crack patterns for all the nine cases for two different displacements; the first equals the expected displacement under service load, as computed in section 'Calculating Real Deflections' and the second equals twice that value. It may be noted that cracks start at the bottom corners of the window, and that this type of crack can be seen in all cases. As the displacement increases, a horizontal bottom crack also occurs and be- comes dominant in some ductile cases with a relatively high value of $\lambda_{\mathrm{ch}}$.

The values of $(w_{\max}f_{\mathrm{t}}/G_{\mathrm{F}})$ and $(u f_{\mathrm{t}}/G_{\mathrm{F}})$ for the nine val- ues used of $\lambda_{\mathrm{ch}}$ are calculated for different values of im- posed vertical displacement for a range from 0 to the double of the expected displacement under service load with increments of 0.1 of it. For the two lowest values of $\lambda_{\mathrm{ch}}$ (89 and 133 mm), the panel became unstable just after crack initiation due to the high brittleness, and for the case of $\lambda_{\mathrm{ch}}=178$ mm, the instability appeared when the horizontal bottom crack suddenly developed. So, results for $\lambda_{\mathrm{ch}}$ equal to 89 and 133 mm are given up to the point of initiation of the crack only, while for the case of $\lambda_{\mathrm{ch}}$ equal to 178 mm, values were calculated up to just before the appearance of the horizontal bottom crack. In Fig. 7, the evolution of the maximum crack width at each deflection step is plotted as a curve of $(w_{\max}f_{\mathrm{t}}/G_{\mathrm{F}})$ versus $(u f_{\mathrm{t}}/G_{\mathrm{F}})$, as described by Eq. (5), for each value of $\lambda_{\mathrm{ch}}$ corresponding to the cases defined in Table 1.

Two families of curves are clearly visible. The first fam- ily has been drawn with framed symbols in Fig. 7; it

![](./images/811859047031504897_5.jpg)

Fig. 5 Crack patterns for all the nine cases for an applied imposed vertical displacement equal to the expected one under service loads (1.45 mm).

![](./images/811859047031504897_6.jpg)

Fig. 6 Crack patterns for all the nine cases for an applied imposed vertical displacement equal to the double of the expected one under service loads (2.90 mm).

![](./images/811859047031504897_7.jpg)

Fig. 7 Relation between the maximum crack width $w$ and the maximum imposed displacement $u$.

corresponds to cases with values of $\lambda_{\text{ch}} < 400$ for which the dominant crack is always the crack at one of the bottom window corners. For this family, it can be seen that the crack initiation (first point close to abscissa zero) depends on $\lambda_{\text{ch}}$, but then the crack width grows rapidly with increasing $u$ and approaches a proportionality line (dash-dot line) for which, roughly, $w_{\text{max}} \approx 0.52u$.

The second family, which has been drawn with filled symbols in Fig. 7, corresponds to cases with values of $\lambda_{\text{ch}} > 400$. In this case, the initially dominant crack is, as for the previous family, the one at the bottom window corner. However, at a certain deflection, the horizontal crack at the bottom of the panel suddenly opens and becomes dominant; this is seen as a jump in the curves in Fig. 7. After the horizontal bottom crack becomes dominant, the maximum crack opening again becomes roughly proportional to the central deflection of the beam, with $w_{\text{max}} \approx 0.78u$.

## Design method for the crack width control

The procedure developed in this research can be used as a general methodology to specify structural and material properties to limit the maximum crack width in the

masonry panels, for any given geometry. The use in design may tend either to select the masonry properties to keep the crack width within the bounds, for an expected maximum beam deflection, or to limit the beam deflection when the masonry properties are given.

The second method is more efficient, we think, in the present state of knowledge, in which designing a masonry for specific fracture properties is more difficult than using a masonry of known fracture properties (although there is not a database for such properties, there are at, at least, procedures to measure them in particular cases). Then, the deflections of the structure can be limited accordingly, which is feasible given the state of development of structural design technology.

Consider, for example, a masonry wall with the geometry studied in the foregoing, which, from previous experience, is known to have values of $G_{\mathrm{F}}/f_{\mathrm{t}} \approx 107\ \mu\mathrm{m}$ and $\lambda_{\mathrm{ch}} \approx 300$ mm, and assume that we want to limit the maximum long-term crack width to 0.3 mm. Then, we compute $w_{\max}f_{\mathrm{t}}/G_{\mathrm{F}} \approx 2.8$. We enter this value as the ordinate of the graph in Fig. 7 and find the corresponding abscissa for the curve with $\lambda_{\mathrm{ch}} = 300$ mm in the graph (see arrows A–B–C), which gives $uf_{\mathrm{t}}/G_{\mathrm{F}} \approx 11.3$, and thus the maximum deflection of the beam would be $11.3 \times 0.107 \approx 1.2$ mm. From the same graph, we can see that the maximum deflection to completely avoid cracking corresponds to the open circle on the horizontal axis, i.e. to $uf_{\mathrm{t}}/G_{\mathrm{F}} \approx 6$ which would require a limitation in deflection to about 0.64 mm.

Thus, the graphs developed in this work, relatively cheap to build (in computer and human time), provide a systematized information about the evolution of the crack width with the beam deflection which allows determination of allowable deflections for any given allowable crack width and, moreover, give valuable information about how close to an instability (a sudden jump in crack opening) the façade is operating.

## CONCLUSIONS

From the foregoing results, the following conclusions can be drawn.

1 Beam deflections allowed by standards are upper-bound design values, much larger than actual (average) deflections.

2 Shortening of columns are of the same order as the beam deflections under service loads.

3 When there is no masonry panel in the ground floor, panels of the first and last floors suffer the maximum cracking under vertical loads.

4 The maximum real deflection of beams is in the order of 1.9 mm while the maximum effective one, which controls the cracking of the masonry panels, is in the order of 1.3 mm (roughly equal to the 1/3800 of the beam span).

5 For the geometry under study, the parametric study shows that two kinds of overall behaviour can be found: one for smaller values of $\lambda_{\mathrm{ch}}$ (more brittle material), for which the dominant crack is always one at a bottom corner of the window, and another for larger values of $\lambda_{\mathrm{ch}}$ for which the horizontal bottom crack forms and becomes dominant after a certain threshold displacement.

6 The methodology used in the present investigation can be used as a numerical design method for the crack width of masonry panels.

7 To make reasonable predictions of the main cracking behaviour of masonry panels due to differential structural displacements, average *in situ* masonry properties, including tensile strength, elastic modulus and fracture energy, should be made available to the building community by *in situ* measurements on a representative sample of brick façade walls. This type of information has never been compiled and a field work on this topic would be welcome as the usual combination of estimated upper and lower bounds (for structural deformations as well as for masonry properties) leads to lower and upper bounds for crack width that are too far apart to be useful.

## Acknowledgements

The authors gratefully acknowledge partial financial support for this work form GOP Project Consulting (Spain), and from the Spanish Ministry of Science and Innovation under grant BIA2005-09250-C03-01. The present work was conducted within the framework provided by the project SEDUREC (CSD2006-60) integrated in the Spanish National Research Program CONSOLIDER-INGENIO 2010.

## REFERENCES

1 Sancho, J. M., Planas, J., Fathy, A. M., Gálvez, J. C. and Cendón, D. A. (2007) Three-dimensional simulation of concrete fracture using embedded crack elements without enforcing crack path continuity. *Int. J. Numer. Anal. Methods Geomech.* **31**, 173–187.

2 Sancho, J. M., Planas, J., Gálvez, J. C., Reyes, E. and Cendón, D. A. (2006) An embedded cohesive crack model for finite element analysis of mixed mode fracture of concrete. *Fatigue Fract. Eng. Mater. Struct.* **29**, 1056–1065.

3 Sancho, J. M., Planas, J., Cendón D. A., Reyes, E. and Gálvez, J. C. (2007) An embedded cohesive crack model for finite element analysis of concrete fracture. *Eng. Fract. Mech.* **74**, 75–86.

4 Fathy, A. M., Planas, J. and Sancho, J. M. (2009) A Numerical Study of Masonry Cracks. *Engng. Fail. Anal.* **16**, 675–689.

5 Fathy, A. M., Planas, J. and Sancho, J. M. (2007) A finite element study of masonry cracks. *6th International Conference*

on Fracture Mechanics of Concrete Structures, Taylor and Francis, Catania, Italia, pp. 1595-1600.

6 Hillerborg, A., Modéer, M., Petersson, P. E. (1976) Analysis of crack formation and crack growth in concrete by means of fracture mechanics and fracture elements. *Cement Concr. Res.* **6**, 773-782.

7 Bazant, Z. P. and Planas, J. (1998) Fracture and Size Effect in Concrete and Other Quasibrittle Materials. CRC Press, Boca Raton, FL.

8 Taylor, R. L. (2001) FEAP: a finite element analysis program. Programmer Manual. University of Berkeley, Berkeley, CA.

9 Swanson, J. A finite element analysis program. http://www.ansys.com/.

10 Geuzaine, C. and Remacle, J.-F. GMSH: a pre- and post-processing program. http://www.geuz.org/gmsh.

11 Ministerio de Fomento Español (2002) Instrucción de Hormigón Estructural, EHE/Comisión Permanente del Hormigón, 5ª edición, Ministerio de Fomento, Centro de Publicaciones, Madrid, 476 pp.

12 Zucchini, A. and Lourenco, P. B. (2004) A coupled homogenisation-damage model for masonry cracking. *Comput. Struct.*, **GB 82**, 917-929.

13 Lee, J. S., Pande, G. N., Middieton, T. J., Kraij, B. (1996). Numerical modelling of brick masonry panels subject to lateral loadings. *Comput. Struct.*, **GB 61**, 735-745.

14 Uva, G. and Salerno, P. B. G. (2005) Towards a multiscale analysis of periodic masonry brickwork: a FEM algorithm with damage and friction. *Solids Struct.* **43**, 3739-3769.

15 Khalaf, F. M., Hendy, A. W. and Fairbairn, D. R. (1994) Study of the compressive strength of blockwork masonry. *ACI Struct. J.* **91**, 367-375.

16 Ramamurthy, K., Sathish, V. and Ambalavanan, R. (2000) Compressive strength prediction of hollow concrete block masonry prisms. *ACI Struct. J.* **97**, 61-67.

17 Khattab, M. M. and Drysdle, R. G. (1992) Tests of concrete block masonry under biaxial tension-compression. *Canadian Masonry Symposium 15-17 June, 1992*, pp. 645-656.

© 2009 Blackwell Publishing Ltd. *Fatigue Fract Engng Mater Struct* **32**, 430-440