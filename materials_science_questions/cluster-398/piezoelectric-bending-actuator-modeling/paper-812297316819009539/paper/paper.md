# Improving Transverse Actuation of Piezoceramics using Interdigitated Surface Electrodes

N. Hagood, R. Kindel, and K. Ghandi
P. Gaudenzi

Department of Aeronautics and Astronautics
Massachusetts Institute of Technology
Cambridge, Massachusetts, 02139

Dipartimento Aerospaziale
Universita' di Roma La Sapienza
Via Eudossiana 16 00184 Roma Italy

## Abstract

The possibility of using interdigitated surface electrode patterns to improve the transverse actuation capability of electroceramic actuators is investigated. This pattern produces nonuniform electrical fields in the plane of the wafer which utilize the longitudinal piezoelectric effect to generate larger, more anisotropic planar actuation than conventional piezoelectric devices. Analytical models are developed for a representative electroceramic volume element of a piezoelectric wafer with interdigitated electrodes. These models incorporate full electromechanical coupling through the constitutive relations and are solved using approximate energy methods. The analytical models are compared to piezoelectric finite element solutions. The analysis predicts an range of electrode thickness and spacings which can increase the achievable transverse actuation. An experimental program was performed to validate the analytical results. The experimental results verified the analytical prediction of highly orthotropic large magnitude in plane strains.

## Introduction

T HE technology of structural actuation and sensing is critical to the development of controlled structures. In recent years active materials such as piezoelectrics, electrostrictives and magnetostrictives have replaced the traditional electromechanical means for actuation. Piezoelectrics are perhaps the most widely used in this capacity because of their high actuation authority and their ease of control by an applied electric field. Piezoelectrics have been used extensively as actuators and sensors in vibration suppression applications. Coupled electro-mechanical models of beams, plates, shells and general elastic bodies [1-4] have been developed. Extensive experimental results in closed-loop control of structural vibration [4-6], aeroelastic response [7,8], and acoustic transmission of plates and shells [9] have demonstrated the feasibility of active structural control using piezoelectrics.

This paper presents a preliminary investigation into improving the planar actuation capability of piezoelectric materials by using interdigitated electrodes to create a component of the electric field in the plane of actuation. The geometry of conventional and interdigitated electrodes on piezoelectric wafers is shown in Figures 1a & b. Conventional planar actuation techniques utilize the electric fields through the thickness of the wafer (Z) and the transverse (d31) piezoelectric effect to create isotropic planar strains in the X and Y direction as shown in Figure la. By using interdigitated electrodes, a large component of the electric field can be aligned in the plane of the structure in the X direction as shown in Figure 1b. Thus, the longitudinal (or d33) piezoelectric effect is utilized in this direction. As the longitudinal piezoelectric effect can be significantly larger than the transverse effect (d33/d31~2.4 for most piezoceramics) an increased planar actuation is attained. It should be noted that in addition to increased free strain capability the induced stress capability is also greatly increased using longitudinal actuation since e33/e31 ~4 for conventional piezoceramic materials.

![](./images/812297316819009539_1.jpg)

Figure 1: Comparison of Conventional (a:Top Figure) and Interdigitated (b:Bottom Figure) Electroding of Piezoelectric Actuators.

The planar actuation also becomes highly anisotropic because the transverse effect is still utilized in the perpendicular, Y, direction. In a sense the wafer will expand in the X direction with the longitudinal effect while contracting in the Y direction with the transverse effect. This anisotropic actuation allows more efficient control of independent structural deflection shapes and

a Assistant Professor, Room 33-313, Tel: (617) 253 2738. Member SPIE.
b Undergraduate Student
c Graduate Student
d Assistant Professor, Tel: (39) (6) 44585304.

0-8194-1150-7/93/$6.00
SPIE Vol. 1917 Smart Structures and Intelligent Systems (1993) / 341

![](./images/812297316819009539_2.jpg)

Figure 2: Electric Field Arrangement Within Interdigitated Wafer Showing
Opposite Field Directions in Adjacent Sections

can greatly enhance structural control performance [8]. In particular, torsion could be easily induced in even isotropic hosts through the use of different actuator orientations, or a bimorph arrangement of the anisotropic actuators.

The challenge to realizing the potential of interdigitated electrodes is to maximize the component of the electric field in the plane of the structure while minimizing the inefficiencies due to electric field distribution. A schematic of the electric field within the material is shown in Figure 2. Both the material poling and the actuation are accomplished using the interdigitated electrodes. As can be seen in Figure 2, significant nonuniformity in the resulting electric field and strains develop, which result in internal stresses and incomplete material polarization. This motivates the modeling effort aimed at predicting the effective material properties resulting from a particular electrode arrangement.

Interdigitated surface electrodes have been successfully applied in many active material applications. They have been utilized for PLZT electro-optic shutter and flash goggles: [10-13] and in surface acoustic wave devices [14,15]. In the area of transducer materials, there have been experimental investigation into using interdigital electrodes as an alternative to conventional techniques for low voltage piezoelectric actuation devices [16]. There has been some analytical work in modeling the internal field distributions due to interdigital electrodes in the area of electro-optic shutters [13] and detailed analysis of the effective resonant electromechanical properties of piezoelectric wafers with such electrodes [17,18]. To date there has been little experimental or analytical work on inducing macroscopic structural deformation or stress utilizing this electroding technique.

This paper presents a combined analytical/experimental investigation of interdigitated actuators. First, the problem of finding the effective piezoelectric properties of the wafer is approached analytically using a simple assumed modes energy method for approximate modeling of the representative volume element (RVE) of the material. This simple uniform field analytical model is compared to a piezoelectric finite element analysis of the representative volume element of the actuator. The results for the analytical/numerical investigation provide an initial design for the electrode pattern. Finally, the manufacture and testing of the selected specimen are described and compared to the model prediction.

## Modeling

In this section the modeling and analysis of the performance of piezoelectric actuators with interdigitated electrodes will be developed. First, the approach and assumptions will be defined along with the possible figures of merit for the device. Both approximate assumed modes models and finite element models will be developed and compared to determine the effect that electrode geometry options have on effective actuator properties.

### Modeling Approach and Figures of Merit

The goal of this section is to set up the problem of predicting the performance capabilities of the macroscopic actuator as a function of the device local geometry and material properties. This can be interpreted as finding the effective homogeneous piezoelectric material properties of the nonhomogeneous device. The device local geometry is specified by three parameters: electrode spacing (p), wafer thickness (h) and electrode width (w) as shown in Figure 3.

![](./images/812297316819009539_3.jpg)

Figure 3: Geometry of Representative Volume Element (RVE)

The symmetries of the problem are such that a representative volume element (shaded region) can be defined whose effective material properties represent those of the entire actuator. The problem then becomes one of determining the response of the RVE to the applied field subject to the boundary conditions on the element. The boundary conditions are chosen so that RVE deformation is compatible with the macroscopic deflection of the device. The boundary conditions on the representative volume element (shaded region) are as follows:

Surface 1: $\mathrm{D_X} = 0, \mathrm{u_X} = 0$
Surface 2: $\mathrm{D_Z} = 0, \mathrm{u_Z} = 0$
Surface 3: $\varphi = 0, \mathrm{u_X} = \text{constant (=0 if clamped case is considered)}$
Surface 4: $\mathrm{D_Z} = 0 \, (\varphi = \text{V on electrode}), \mathrm{T_Z} = 0$
Y Face: $\mathrm{D_Y} = 0, \mathrm{u_Y} = \text{constant}$

Where D is the electrical displacement, $\varphi$ is the electric potential, and u is the mechanical displacement field. The actuator is assumed to operate in modified plane strain. Deflections in the Y direction are assumed to be constant and equal over the RVE unless otherwise specified. With the modified plain strain assumption, the problem becomes a two dimensional electroelastic boundary value problem which will be solved using two methods: 1) assumed modes method using a

modified version of Hamilton's Principle and 2) piezoelectric finite element method.

In addition to the geometric and boundary condition assumptions stated above, the constitutive relations for the material are required. In general the material properties can be stated using the standard convention [19]:

$$
\left[\begin{array}{c}
\mathbf{T}^{\prime} \\
\hdashline \mathbf{D}^{\prime}
\end{array}\right]=\left[\begin{array}{c:c}
\mathbf{c}^{E} & -\mathbf{e}_{t} \\
\hdashline \mathbf{e} & \boldsymbol{\varepsilon}^{S}
\end{array}\right]\left[\begin{array}{c}
\mathbf{S}^{\prime} \\
\hdashline \mathbf{E}^{\prime}
\end{array}\right]
\tag{1a}
$$

or

$$
\left[\begin{array}{c}
\mathbf{S}^{\prime} \\
\hdashline \mathbf{D}^{\prime}
\end{array}\right]=\left[\begin{array}{c:c}
\mathbf{s}^{E} & \mathbf{d}_{t} \\
\hdashline \mathbf{d} & \boldsymbol{\varepsilon}^{T}
\end{array}\right]\left[\begin{array}{c}
\mathbf{T}^{\prime} \\
\hdashline \mathbf{E}^{\prime}
\end{array}\right]
\tag{1b}
$$

where the $(\cdot)'$ denotes variables in the material coordinate frame attached to the poling direction and the subscript $(\cdot)_{t}$ denotes transpose. The superscript $(\cdot)^{S}$ signifies that the values are measured at constant strain (e.g.. clamped), the superscript $(\cdot)^{T}$ signifies that the values are measured at constant stress (e.g.. free strain), and the superscript $(\cdot)^{E}$ signifies that the values are measured at constant electrical field (e.g.. short circuit). The piezoceramics couple the mechanical and electrical equations. In the form of the equations given in (1) the coupling terms are the piezoelectric constants which relate stress to applied field (the $\mathbf{e}$ constants), or the constants which relate strain to applied field (the $\mathbf{d}$ constants). These constants are related through the expression:

$$
\mathbf{e}=\mathbf{d} \mathbf{c}^{E}
\tag{2}
$$

For a piezoceramic the matrix constitutive relations in the form of Equation (1a) can be expressed as:

$$
\left[\begin{array}{c}
T_{1}^{\prime} \\
T_{2}^{\prime} \\
T_{3}^{\prime} \\
T_{4}^{\prime} \\
T_{5}^{\prime} \\
T_{6}^{\prime} \\
\hdashline D_{1}^{\prime} \\
D_{2}^{\prime} \\
D_{3}^{\prime}
\end{array}\right]=\left[\begin{array}{cccccc:cccc}
c_{11}^{E} & c_{12}^{E} & c_{13}^{E} & 0 & 0 & 0 & 0 & 0 & -e_{31} \\
c_{12}^{E} & c_{11}^{E} & c_{13}^{E} & 0 & 0 & 0 & 0 & 0 & -e_{31} \\
c_{13}^{E} & c_{13}^{E} & c_{33}^{E} & 0 & 0 & 0 & 0 & 0 & -e_{33} \\
0 & 0 & 0 & c_{55}^{E} & 0 & 0 & 0 & -e_{15} & 0 \\
0 & 0 & 0 & 0 & c_{55}^{E} & 0 & -e_{15} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & c_{66}^{E} & 0 & 0 & 0 \\
\hdashline 0 & 0 & 0 & 0 & e_{15} & 0 & \varepsilon_{1}^{s} & 0 & 0 \\
0 & 0 & 0 & e_{15} & 0 & 0 & 0 & \varepsilon_{1}^{s} & 0 \\
e_{31} & e_{31} & e_{33} & 0 & 0 & 0 & 0 & 0 & \varepsilon_{3}^{s}
\end{array}\right]\left[\begin{array}{c}
S_{1}^{\prime} \\
S_{2}^{\prime} \\
S_{3}^{\prime} \\
S_{4}^{\prime} \\
S_{5}^{\prime} \\
S_{6}^{\prime} \\
\hdashline E_{1}^{\prime} \\
E_{2}^{\prime} \\
E_{3}^{\prime}
\end{array}\right]
\tag{3}
$$

Note that due to symmetry the material properties are identical in the 1 and 2 directions. The first term in the subscript of the coupling coefficients refers to the electrical axis while the second refers to the mechanical. Thus $e_{31}$ refers to the stress developed in the 1 direction in response to a field in the 3 direction (parallel to the material poling).

In actual implementation, the material is poled using the nonuniform electric field resulting from the electrode geometry, so the poling is in no sense uniform. In addition, the poling direction is reversed between alternating sets of the electrodes. For modeling purposes the material is assumed to be a piezoelectric ceramic which is uniformly poled in the X direction within the RVE. For large p/h this simplifying assumption should prove adequate. Thus in the physical coordinate system, with poling in the X direction, the constitutive relation is:

$$
\left[\begin{array}{c}
\mathbf{T} \\
\hdashline \mathbf{D}
\end{array}\right]=\left[\begin{array}{c:c}
\mathbf{c}^{E} & -\mathbf{e}_{t} \\
\hdashline \mathbf{e} & \boldsymbol{\varepsilon}^{S}
\end{array}\right]\left[\begin{array}{c}
\mathbf{S} \\
\hdashline \mathbf{E}
\end{array}\right]
\tag{4}
$$

$$
\left[\begin{array}{c}
T_{x} \\
T_{y} \\
T_{z} \\
T_{y z} \\
T_{x z} \\
T_{x y} \\
\hdashline D_{x} \\
D_{y} \\
D_{z}
\end{array}\right]=\left[\begin{array}{cccccc:cccc}
c_{33}^{E} & c_{13}^{E} & c_{13}^{E} & 0 & 0 & 0 & -e_{33} & 0 & 0 \\
c_{13}^{E} & c_{11}^{E} & c_{12}^{E} & 0 & 0 & 0 & -e_{31} & 0 & 0 \\
c_{13}^{E} & c_{12}^{E} & c_{11}^{E} & 0 & 0 & 0 & -e_{31} & 0 & 0 \\
0 & 0 & 0 & c_{66}^{E} & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & c_{55}^{E} & 0 & 0 & 0 & -e_{15} \\
0 & 0 & 0 & 0 & 0 & c_{55}^{E} & 0 & -e_{15} & 0 \\
\hdashline e_{33} & e_{31} & e_{31} & 0 & 0 & 0 & \varepsilon_{3}^{s} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & e_{15} & 0 & \varepsilon_{1}^{s} & 0 \\
0 & 0 & 0 & 0 & e_{15} & 0 & 0 & 0 & \varepsilon_{1}^{s}
\end{array}\right]\left[\begin{array}{c}
S_{x} \\
S_{y} \\
S_{z} \\
S_{y z} \\
S_{x z} \\
S_{x y} \\
\hdashline E_{x} \\
E_{y} \\
E_{z}
\end{array}\right]
\tag{5}
$$

The performance of the device can be measured and compared using any of several possible figures of merit. In general for planar actuation, actuator performance can be measured using either free strains in the X and Y directions, $S_{x}$ and $S_{y}$, or clamped stresses in the X and Y directions, $T_{x}$ and $T_{y}$. Clamped stress is the averaged normal stress over the X or Y surface when the RVE is allowed no normal deformation of the X face. Only X direction clamped stress is considered.

For comparison, the performance of the interdigitated actuator is normalized by the performance of a conventional transverse actuator. In evaluating the relative performance it is important to state whether the comparison is made at comparable field levels or at comparable applied voltage levels. This is necessary because the different electrode geometries produce different field levels within the materials at the same applied electrode voltages. Normalized figures of merit can be stated:

$$
\text { Field Normalized Strain: } \overline{S}_{E}=\left.\frac{S_{\text {int }}}{S_{\text {st }}}\right|_{E=\text { Specified }}=\frac{S_{\text {int }}}{d_{31} \overline{E}_{\text {int }}}=\frac{S_{\text {int }}}{d_{31} \frac{2 V}{p-w}}
$$

$$
\text { Voltage Normalized Strain: } \overline{S}_{V}=\left.\frac{S_{\text {int }}}{S_{\text {st }}}\right|_{V=\text { Specified }}=\frac{S_{\text {int }}}{d_{31} \overline{E}_{s t}}=\frac{S_{\text {int }}}{d_{31} \frac{2 V}{h}}
\tag{6}
$$

where the subscript $(\cdot)_{st}$ represents a quantity associated with the standard electrode configuration and the subscript $(\cdot)_{\text {int }}$ represents a quantity associated with the interdigitated electrode pattern. The electric field, $\overline{E}$, represents the average material electric field. Since the field varies throughout the interdigitated specimen this represents an averaged field along the surface of the specimen between the opposite polarity electrodes. This path contains the highest fields within the representative volume element. For stress capabilities a similar normalization can be defined:

$$
\text { Field Normalized Stress: } \overline{T}_{E}=\left.\frac{T_{\text {int }}}{T_{\text {st }}}\right|_{E=\text { Specified }}=\frac{T_{\text {int }}}{-e_{31} \overline{E}_{\text {int }}}=\frac{T_{\text {int }}}{-e_{31} \frac{2 V}{p-w}}
$$

$$
\text { Voltage Normalized Stress: } \overline{T}_{V}=\left.\frac{T_{\text {int }}}{T_{\text {st }}}\right|_{V=\text { Specified }}=\frac{T_{\text {int }}}{-e_{31} \overline{E}_{s t}}=\frac{T_{\text {int }}}{-e_{31} \frac{2 V}{h}}
\tag{7}
$$


The field normalized performance serves to measure the relative peak actuation capability of the device. To prevent depolarization during operation, the applied field levels are limited to those below the coercive field of the material. Thus, if voltage is unrestricted, then the peak strain or stress capabilities of an actuation device are limited by the allowable field levels. In contrast, voltage normalized actuation strains and stresses are important if the limitation in application is the applied voltage levels usually an amplifier constraint. Both types of normalization will be presented.

In the following sections, two approaches to modeling the behavior of the RVE will be presented. The first is a simple assumed modes Rayleigh-Ritz model which can be used for closed form, "back of the envelope" calculations of device effective piezoelectric properties and capabilities. The second is a more complex coupled field analysis using piezoelectric finite elements. The finite element modeling was done using ANSYS linear piezoelectric elements. The results of the two analyses will be compared.

### Rayleigh-Ritz Approximate Model

To obtain a model of the system, an approach based on variational principles is used as described in [4]. The Generalized Hamilton's Principle for a coupled electromechanical system is:
$$
\int_{t_{1}}^{t_{2}}\left[\left(\partial T-\partial U+\partial W_{e}-\partial W_{m}\right)+\partial W\right] d t=0
\tag{8}
$$

Ignoring the kinetic and magnetic energy terms:
$$
-\partial U+\partial W_{e}+\partial W=0
\tag{9}
$$

The mechanical and electrical energy terms are:
$$
\partial U=\iiint_{V} \partial \mathbf{S}^{T} \mathbf{T} d V \quad, \quad \partial W_{e}=\iiint_{V} \partial \mathbf{E}^{T} \mathbf{D} d V
\tag{10}
$$

The mechanical work term due to applied surface stresses ignore applied charge term are:
$$
\partial W=\iint_{S} \partial \mathbf{u} \cdot \mathbf{T}_{s} d A
\tag{11}
$$

To find a solution for the system, assumed shape functions for the displacement and the voltage potential are needed. The displacement field in the Y and Z directions is assumed to be linear. Using the average strains in these directions as the degrees of freedom:
$$
u_{y}=\bar{S}_{y} y \quad , \quad u_{z}=\bar{S}_{z} z
\tag{12}
$$

In the X direction it was desired to allow an extra degree of freedom. Assuming a displacement field that is piecewise linear, and using the average strain over the whole element and the average strain under the electrodes as the degrees of freedom:
$$
\begin{aligned}
\bar{S}_{x} & \equiv \text { average strain between }(0, p / 2). \\
\left(u_{x}\right)_{x=p / 2} & =\frac{1}{2} p \bar{S}_{x}=\Delta x
\end{aligned}
\tag{13a}
$$

$$
\begin{aligned}
\tilde{S}_{x} & \equiv \text { average strain between }(0, w / 2). \\
\left(u_{x}\right)_{x=w / 2} & =\frac{1}{2} w \tilde{S}_{x}=\Delta x^{*}
\end{aligned}
\tag{13b}
$$

A piecewise linear function satisfying the above conditions, as
![](./images/812297316819009539_4.jpg)

Figure 4: Assumed Mechanical and Electrical Field Shapes
well as the clamped condition at $x=0$ is:
$$
u_{x}=
\begin{cases}
\tilde{S}_{x} x & , \quad 0<x<w / 2 \\
\frac{1}{2} w \tilde{S}_{x}+\frac{(x-w / 2)}{(p-w)}\left(p \bar{S}_{x}-w \tilde{S}_{x}\right) & , \quad w / 2<x<p / 2
\end{cases}
\tag{14}
$$

Now calculate strains:
$$
\begin{aligned}
& S_{x}=
\begin{cases}
\tilde{S}_{x} & , \quad 0<x<w / 2 \\
\frac{p \bar{S}_{x}-w \tilde{S}_{x}}{p-w} & , \quad w / 2<x<p / 2
\end{cases} \\
& S_{y}=\bar{S}_{y} \\
& S_{z}=\bar{S}_{z}
\end{aligned}
\tag{15}
$$

The shear strains are zero. The strains can then be expressed as:
$$
\mathbf{S}=\mathbf{N}_{r} \mathbf{r}
\tag{16}
$$
where
$$
\mathbf{r}=\left[\begin{array}{llll}
\bar{S}_{x} & \bar{S}_{y} & \bar{S}_{z} & \tilde{S}_{x}
\end{array}\right]^{T}
\tag{17}
$$

$$
\mathbf{N}_{r}=
\begin{cases}
\mathbf{N}_{r}^{1} & , \quad 0<x<w / 2 \\
\mathbf{N}_{r}^{2} & , \quad w / 2<x<p / 2
\end{cases}
$$

$$
\mathbf{N}_{r}^{1}=\begin{bmatrix}
0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\hline \underline{0}_{3 \times 4}
\end{bmatrix}
, \quad
\mathbf{N}_{r}^{2}=\begin{bmatrix}
\alpha & 0 & 0 & -\beta \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
\hline \underline{0}_{3 \times 4}
\end{bmatrix}
$$

$$
\alpha=\frac{p}{p-w} \quad , \quad \beta=\frac{w}{p-w}
$$

---
344 / SPIE Vol. 1917 Smart Structures and Intelligent Systems (1993)

A shape function for the electric potential is obtained by assuming the whole region under the electrode is at potential $V$, and that the side at $x=p/2$ is grounded. A linearly varying potential satisfying these boundary conditions is:
$$
\varphi(x)=\left\{
\begin{array}{cc}
V & , \quad 0<x<w/2 \\
V-\overline{E}(x-w/2) & , \quad w/2<x<p/2
\end{array}
\right. \tag{18}
$$
where
$$
\overline{E}=\frac{2V}{p-w} \tag{19}
$$

So the electric field can be written as:
$$
\mathbf{E}=-\nabla \varphi=\mathbf{N}_{\mathbf{v}} \overline{E} \tag{20}
$$
where
$$
\mathbf{N}_{\mathbf{v}}=\left\{
\begin{array}{cc}
\mathbf{N}_{\mathbf{v}}^{\mathbf{1}}=\left[\begin{array}{lll}0 & 0 & 0\end{array}\right]^{T} & , \quad 0<x<w/2 \\
\mathbf{N}_{\mathbf{v}}^{2}=\left[\begin{array}{lll}1 & 0 & 0\end{array}\right]^{T} & , \quad w/2<x<p/2
\end{array}
\right. \tag{21}
$$

The constitutive relation (4) and the assumed shape functions (16,20) are substituted into the work and energy terms (10). The resulting integrals can be written as :
$$
\begin{aligned}
\partial W & =\iint_{S} \partial \mathbf{u} \cdot \mathbf{T} d A=\frac{1}{8} p h l\left(\partial \overline{S}_{x} \overline{T}_{x}+\partial \overline{S}_{y} \overline{T}_{y}+\partial \overline{S}_{z} \overline{T}_{z}\right) \\
& =\frac{1}{8} p h l \partial \mathbf{r}^{T} \mathbf{F}
\end{aligned}
$$
$$
\partial U=\iiint_{V} \partial \mathbf{S}^{T} \mathbf{T} d V=\frac{1}{8} p h l\left(\partial \mathbf{r}^{T} \mathbf{K r}-\partial \mathbf{r}^{T} \boldsymbol{\Theta}_{t} \overline{E}\right) \tag{22}
$$
$$
\partial W_{e}=\iiint_{V} \partial \mathbf{E}^{T} \mathbf{D} d V=\frac{1}{8} p h l\left(\partial \overline{E} \boldsymbol{\Theta} \mathbf{r}+\partial \overline{E} \mathbf{C} \overline{E}\right)
$$
where the following definitions were made in the above calculations:
$$
\begin{gathered}
\mathbf{K}=\frac{8}{p h l}\left(\iiint_{V} \mathbf{N}_{\mathbf{r}}^{T} \mathbf{c}^{E} \mathbf{N}_{\mathbf{r}} d V\right) \\
\boldsymbol{\Theta}=\frac{8}{p h l}\left(\iiint_{V} \mathbf{N}_{\mathbf{v}}^{T} \mathbf{e} \mathbf{N}_{\mathbf{r}} d V\right) \\
\mathbf{C}=\frac{8}{p h l}\left(\iiint_{V} \mathbf{N}_{\mathbf{v}}^{T} \boldsymbol{\varepsilon}^{s} \mathbf{N}_{\mathbf{v}} d V\right)
\end{gathered} \quad \mathbf{F}=\left[\begin{array}{c}
\overline{T}_{x} \\
\overline{T}_{y} \\
\overline{T}_{z} \\
0
\end{array}\right] \tag{23}
$$

Substituting back into Hamilton's equation (9):
$$
\begin{aligned}
& 0=\frac{1}{8} p h l\left(-\partial \mathbf{r}^{T} \mathbf{K} \mathbf{r}+\partial \mathbf{r}^{T} \boldsymbol{\Theta}_{t} \overline{E}+\partial \overline{E} \boldsymbol{\Theta} \mathbf{r}+\partial \overline{E} \mathbf{C} \overline{E}+\partial \mathbf{r}^{T} \mathbf{F}\right) \\
& 0=\partial \mathbf{r}^{T}\left(-\mathbf{K r}+\boldsymbol{\Theta}_{t} \overline{E}+\mathbf{F}\right)+\partial \overline{E}(\boldsymbol{\Theta} \mathbf{r}+\mathbf{C} \overline{E})
\end{aligned} \tag{24}
$$

Which gives the system of equations:
$$
\left[\begin{array}{c}
\mathbf{F} \\
\hline \mathbf{0}
\end{array}\right]=\left[\begin{array}{c:c}
\mathbf{K} & -\boldsymbol{\Theta}_{t} \\
\hline \boldsymbol{\Theta} & -\mathbf{C}
\end{array}\right]\left[\begin{array}{c}
\mathbf{r} \\
\hline \overline{E}
\end{array}\right] \tag{25}
$$

All that remains is to carry out the integrations for $\mathbf{K}$, $\boldsymbol{\Theta}$, and $\mathbf{C}$. Since the integrands are only functions of x, the integration over y and z are simple. Since the integrands are piecewise constant in the x direction, in each case we have:
$$
\begin{gathered}
\mathbf{K}=\left(\mathbf{N}_{\mathbf{r}}^{1 T} \mathbf{c}^{E} \mathbf{N}_{\mathbf{r}}^{1} w+\mathbf{N}_{\mathbf{r}}^{2 T} \mathbf{c}^{E} \mathbf{N}_{\mathbf{r}}^{2}(p-w)\right) / p \\
\boldsymbol{\Theta}=\mathbf{N}_{\mathbf{v}}^{2 T} \mathbf{e} \mathbf{N}_{\mathbf{r}}^{2}(p-w) / p \\
\mathbf{C}=\mathbf{N}_{\mathbf{v}}^{2 T} \boldsymbol{\varepsilon}^{s} \mathbf{N}_{\mathbf{v}}^{2}(p-w) / p
\end{gathered} \tag{26}
$$

after multiplying out all matrices we get the system of equations:
$$
\left[\begin{array}{c}
\overline{T}_{x} \\
\overline{T}_{y} \\
\overline{T}_{z} \\
\hline 0 \\
0
\end{array}\right]=\left[\begin{array}{ccccc}
\frac{p c_{33}^{E}}{p-w} & c_{13}^{E} & c_{13}^{E} & -\frac{w c_{33}^{E}}{p-w} & -e_{33} \\
c_{13}^{E} & c_{11}^{E} & c_{12}^{E} & 0 & -\frac{p-w}{p} e_{31} \\
c_{13}^{E} & c_{12}^{E} & c_{11}^{E} & 0 & -\frac{p-w}{p} e_{31} \\
\hline-\frac{w c_{33}^{E}}{p-w} & 0 & 0 & \frac{w c_{33}^{E}}{p-w} & \frac{w}{p} e_{33} \\
\hline e_{33} & \frac{p-w}{p} e_{31} & \frac{p-w}{p} e_{31} & -\frac{w}{p} e_{33} & \frac{p-w}{p} \varepsilon_{3}^{s}
\end{array}\right]\left[\begin{array}{c}
\overline{S}_{x} \\
\overline{S}_{y} \\
\overline{S}_{z} \\
\hline \tilde{S}_{x} \\
\overline{\bar{E}}
\end{array}\right]
\tag{27}
$$

Which after performing static condensation on $\tilde{S}_{x}$ reduces to:
$$
\left[\begin{array}{c}
\overline{T}_{x} \\
\overline{T}_{y} \\
\overline{T}_{z}
\end{array}\right]=\left[\begin{array}{ccc}
c_{33}^{E} & c_{13}^{E} & c_{13}^{E} \\
c_{13}^{E} & c_{11}^{E} & c_{12}^{E} \\
c_{13}^{E} & c_{12}^{E} & c_{11}^{E}
\end{array}\right]\left[\begin{array}{c}
\overline{S}_{x} \\
\overline{S}_{y} \\
\overline{S}_{z}
\end{array}\right]-\left[\begin{array}{c}
e_{33} \\
e_{31} \\
e_{31}
\end{array}\right] \frac{p-w}{p} \overline{E} \tag{28}
$$
$$
\left[\begin{array}{lll}
e_{33} & e_{31} & e_{31}
\end{array}\right]\left[\begin{array}{c}
\overline{S}_{x} \\
\overline{S}_{y} \\
\overline{S}_{z}
\end{array}\right]+\left(\frac{w e_{33}^{2}}{p c_{33}^{E}}+\varepsilon_{3}^{s}\right) \overline{E}=0
$$

Equation (28) summerizes the Rayleigh-Ritz model. The same material stiffness and coupling coefficients relating the pointwise stress, strain and field also relate the average quantities. However, a difference exists in the effective dielectric of the sample. The factor (p-w)/p in effect distributes the potential over the whole RVE rather than the region between the electrodes.

It is noted that the average X direction stress to field coupling coefficient is simply e33 reduced by a factor of (p-w)/p, and asymptotes to e33 as the ratio p/w increases. Thus, as suggested, interdigitated electrodes improve the transverse actuation by using the longitudinal piezoelectric effect.

### Piezoelectric Finite Element Model
Initial finite element studies utilized iterative electromechanical modeling of piezoelectrics within ADINA. The general methodology for such modeling is presented in [20]. The final model was implemented within ANSYS, which has the capability to model piezoelectric material as Multifield Solid Elements [21]. The model consisted of one layer of brick elements. Seven elements spanned the thickness of the RVE, with h=0.1905mm (corresponding to the thickness of the physical sample). The other element dimensions were set to produce an aspect ratio of approximately 1:1:1 in all elements, which were generated using the automatic meshing capabilities of ANSYS.

![](./images/812297316819009539_5.jpg)

Figure 5: Piezoelectric Finite Element Model (Z axis scaled by 2)

![](./images/812297316819009539_6.jpg)

Figure 6: Electric Potential Distribution (Z axis scaled by 2)

![](./images/812297316819009539_7.jpg)

Figure 7: X Displacement Distribution: Free (Z axis scaled by 2)

![](./images/812297316819009539_8.jpg)

Figure 8: Internal Stress X Distribution: Clamped (Z axis scaled by 2)

On each of the surfaces at $x=0$, $y=0$ and $z=0$, symmetry boundary conditions were enforced. On the $y=l/2$ surface, the Y displacements were coupled together, and on the $x=p/2$ surface, the X displacements were coupled together (=0 for clamped case). The $x=p/2$ surface was grounded, and 100V was applied to the portion of the surface covered by the electrode.

The average strain was readily obtained from the displacements at the boundary of the RVE. The average stress had to be calculated by numerically integrating nodal stresses on each surface.

Some sample results corresponding to the case $p/h=6$, $w/h=1$, are shown in Figures 5-8. The Z dimension in all 4 figures is exaggerated by a factor of 2.

Figure 5 shows the outline of the deformed RVE in the free strain case superimposed on the location of the original element mesh. Note that there is a large strain in the X direction, while there is little deformation in the Z direction.

Figure 6 is a contour plot of the electric potential. Note that the field nonuniformities are localized in the region near the electrode and that the potential drops uniformly in the region away from the electrode. This justifies the selection of a linear potential field in the region between the electrodes for the Rayleigh-Ritz model.

The X direction displacement, shown in Figure 7, also is very uniform in the region between the electrodes. Thus the choice of a linear displacement field in the Rayleigh-Ritz model is justified for this geometry. The approximation becomes less accurate at lower p/h ratios.

Figure 8 shows the X direction stress contours in the sample. The stress distribution is uniform in the RVE, with the exception of in the region under the electrode. The effects under the electrode are due to clamping of the dead areas, where the electric field is almost zero. Note that the electrodes protrude more when the X direction is clamped.

### Parametric Study Results

In this section, the simple Rayleigh-Ritz model will be compared to the piezoelectric finite element model to determine regions where electric field distortion effects near the electrodes become important. The results of the following parametric study

can also be used to help design actuators for specific actuation needs and constraints.

The first series of figures depicts the variation of relative actuation capability as a function of increasing electrode spacing to wafer thickness (p/h) at constant electrode width to wafer thickness (w/h = 1). Relative actuation capability is defined as the actuation capability of the interdigitated actuator normalized by the equivalent capability of a conventional piezoceramic actuator operating at the same internal field or applied voltage level: i.e. field normalized and voltage normalized (Equations 6,7). These curves are different due to the differing relative electrode spacings. Field normalized curves reflect the peak actuation capability if voltage is unconstrained, while voltage normalized data reflects the actuation capability constrained by voltage limitations.

![](./images/812297316819009539_9.jpg)

Figure 9: Field (Top) and Voltage (Bottom) Normalized Relative Strain in the X Direction. (Values Inverted for Presentation).

Figure 9 shows the comparison of the free strain predictions made by the assumed modes model and by the piezoelectric finite element model in both the field and voltage normalized cases. The values of the relative strains are negative since the predictions call for opposite phasing in the X direction response of the interdigitated wafer and the conventional wafer.

Field normalized relative strains in the X direction asymptote to d33/d31 in the high p/h regime since the interdigitated wafer uses the longitudinal piezoelectric effect in the X direction, while the conventional wafer uses the transverse effect. For the range of p/h considered, a value of -1.8 is attained. The voltage normalized relative strains asymptote to zero, since the larger electrode spacing implies a lower electric field at a specified voltage, and thus produces lower strain.

There is good agreement between the two models as p/h increases. At low p/h the field is more inhomogeneous, and thus the Rayleigh-Ritz model is less accurate.

![](./images/812297316819009539_10.jpg)

Figure 10: Field (Top) and Voltage (Bottom) Normalized Relative Strain in the Y Direction

Figure 10 shows the relative strain in the Y direction for the two different normalizations. Again there is good agreement between the models, particularly as p/h increases.

The field normalized relative strains in the Y direction should asymptote to 1 (d31/d31) since both the interdigitated wafer and conventional wafer utilize the transverse piezoelectric effect in this direction. Within the examined range of p/h, a ratio of 0.84 is obtained.

The voltage normalized Y direction relative strains asymptotes to zero for the same reason as the X direction values. Note that with either normalization both the magnitude and sign of the X and Y direction strains are very different. This anisotropy can be utilized in more effective actuation of independent structural modes, as mentioned earlier.

Figure 11 shows the X direction relative stress under clamped condition for each normalization case. In this case the agreement between the two models is greatly improved.

If the material was clamped in all 3 directions, the field normalized X direction relative stress would asymptote to e33/e31 as p/h increased. However, since the model is only

clamped in the X direction, the relative stress asymptotes to:

$$
\frac{e_{33}}{e_{31}}-\frac{2 c_{13}^{E}}{c_{11}^{E}+c_{12}^{E}}
$$

which for the selected material has a value of -3.718. The relative stress achieves a magnitude of 3 at p/h = 5.5. This shows a very large improvement in the actuation capability due to interdigitated electrodes. Thus the highly anisotropic, high magnitude properties apply to induced stress as well as induced strain.

![](./images/812297316819009539_11.jpg)

Figure 11: Field (Top) and Voltage (Bottom) Normalized Relative Stress in the X Direction

The voltage normalized relative stress in the X direction, while asymptoting towards zero, is not much smaller than 1 over the considered range of geometries. Thus the interdigitated electrode pattern provides stress actuation levels comparable to the standard wafer, even if voltage limitation, rather than peak actuation level, is the driving factor.

Examining the effect of varying electrode width (w) while holding all other parameters constant indicated a benefit for reducing the electrode width as much as possible. This however does not take into account the electrode current capabilities (burnout, etc) which would impose a lower limit on the electrode width.

In general, the comparison of the models shows a good agreement between the assumed modes model and the more complex piezoelectric finite element model. It was shown that with p/h = 6 field normalized relative free X direction strain levels of -1.82, relative Y direct strain levels of 0.833, and relative stress levels of -3.10 can be achieved. These values indicate very good orthotropic actuation capability. They can be improved further by increasing p/h until the voltage constraint becomes the dominating factor. These predictions warrant the experimental investigation which is presented in the next section.

## Specimen Manufacture

The design of the electrode pattern and the selection of a manufacturing process were defined by a number of requirements for the final test pieces. Primary among these was the complete separation of electrodes of opposite polarity to prevent sparking. This mandated an identical top and bottom electrode pattern and polarity at all points on the wafer, so as to not allow breakdown over the edges and a manufacturing process that removed all of the nickel from the surface to avoid surface arcing. The precision alignment of the electrodes on top and bottom surfaces was also of great importance in creating the electric field required to achieve transverse actuation.

The pattern design is shown in Figure 12 for a small test wafer. Electrode lines on the same side are of alternating polarity, while lines directly opposite through the chip are of the same polarity. Large pads were placed at the top corners on both sides to allow easy attachment of leads.

The geometry of the chip was motivated by many parameters. Increasing the electrode spacing, p, creates a more uniform electric field in the plane of actuation and thus increases the peak actuation capability. However, it also increases the required applied voltage levels and the possibility of arcing. Arcing typically damages the electrodes and results in loss of conductivity. The present geometry was chosen, with the electrode spacing of 1.143mm (.045") as a compromise to allow a relatively uniform transverse field and a poling voltage low enough to allow saturation poling using available amplifiers. The electrode width was chosen to equal the wafer thickness, both .1905mm (.0075"), as small as the electrode manufacturing process would easily allow.

The substrate used was PSI-5A-S2, a product of Piezo Systems, Inc. Its material properties are presented in Table 2. The initial size of these wafers was 6.1mmx9.14mmx.1905mm (2"x3".x0075"). The wafers were obtained pre-poled, and coated on both sides with electroless nickel. TechEtch, Inc. performed normal photochemical machining procedures upon them. This first involved the creation of the artwork and photomask from the sketch provided. Then both surfaces were cleansed and a dry film photoresist applied to the area that was to remain nickel. Finally, the excess nickel was removed with a proprietary etchant. Two complete patterns, top and bottom, were etched onto each wafer.

Another technique for applying electrodes to the wafers involving thermal evaporation for depositing the electrodes was attempted by the Micro Technology Central Facility at MIT. This technique involved the application of a photoresist to an unelectroded chip using the photomask generated at TechEtch, Inc. and modified by Advance Reproductions Corporation. The photoresist coated the sections of the chip that were to remain without electrodes. 2400 angstroms of gold was then evaporated onto the entire wafer surface over the photoresist. Then, through the use of an ultrasonic cleaner, all of the gold except for the electrode pattern was removed. The process was repeated on the other side using an infrared aligner to ensure precision. This technique encountered problems with the electrode quality. The


thin layer of gold did not conduct sufficiently, and would melt away when soldering was attempted.

Each 6.1mmx9.14mmx.1905mm (2"x3"x.0075") unetched wafer could produce two 25.4mmx25.4mm (1"x1") wafers with the electrode interdigitated pattern. The interdigitated electrode portions of the wafers were removed from the unelectroded portion through careful cutting with a craft knife. The edges of the resulting one inch square samples were sanded using high grit sandpaper to remove any irregularities that may have occurred in cutting. Initially, Stavely Sensors, Inc. was employed to do precision cutting of the wafers, but it was determined that the same yield could be acquired with only a small loss in precision through hand cutting.

![](./images/812297316819009539_12.jpg)

Figure 12: Specimen Geometry and Surface Electrode Pattern

A two inch length of strain gage wire was used to connect the corresponding pads on the top and the bottom of the chip and another wire was soldered to the top pad on both the left and the right sides to provide a means of applying voltage across the electrodes.

Before testing, the interdigitated electrode wafers required repoling. This was done at 2.4 kV at $80^\circ$ C. The heating was done with a Neslab Instruments, Inc. Exacal 250HT High Temperature Bath and an Exacal Controller/Readout using Dow Corning 200 silicon oil. The voltage was obtained through use of a GENCOM Division/Emitronics Inc. High Voltage Power Supply Model 3000R. The wafer was placed in the heated bath several minutes before voltage was applied, and was removed and allowed to cool and drip dry as soon as the voltage was removed. Voltage was increased for approximately three minutes and left at peak for ten minutes. The voltage was brought back to zero over the course of three minutes. The wafers were then allowed to age for three days to permit their properties to settle. Before data was taken the wafers were electrically cycled a number of times, with both DC and low frequency AC voltages, to ensure stable properties.

The final resistance of the electrode pattern was approximately 6 ohm/mm, and the resistance between the electrodes was greater than 200 Megaohms. The capacitance for this geometry was .505 nanofarads. All of these were determined using an Omega Digital Multimeter HHM57.

### Experimental Validation

Strain data was collected using Measurements Group, Inc. CEA-06-062UR-350 rosette style strain gages. One of the strain gages was parallel to the electrode lines (Y direction) and the other was perpendicular (X direction) as shown in Figure 12. The strain gages were conditioned with Measurements Group, Inc model 2120 and 2120A strain gage conditioners using a model 2110 power supply. The conditioners used a half bridge configuration, balancing the test piece with a dummy gage under similar operating conditions, but without applied voltage. They were adjusted to 1000 microstrain per volt output with a bridge voltage of 4.5 volts. Output from the conditioners was input into a Nicolet Instrument Corporation Model 206 Digitizing Oscilloscope.

The test signals were produced by a Philips PM5191 Programmable Synthesizer/Function Generator. These were amplified (x100) through a KEPCO Model BOP 1000M Bipolar Operational Power Supply/Amplifier. This was applied simultaneously to the leads on the wafer and a 100 times op amp based voltage divider, the output of which entered the Nicolet oscilloscope when needed.

The X and Y direction strains were collected as a function of voltage. All data was taken with both the test and the dummy wafers in a container of Dow Corning 200 silicon oil to improve temperature stability and decrease the likelihood of arcing. The X and Y direction strains were read off of the Nicolet digital oscilloscope and the voltage was read from a multimeter. During data acquisition, the voltage was incremented with a step function of approximately 10 volts approximately every 20 seconds. For the high field data, the voltage was systematically increased to 750 volts while data was acquired, and then returned to zero. The strain gages were then rezeroed, and the voltage was decreased to negative 750 volts.

For the small field data the voltage was quickly stepped up to a value and the transients were allowed to die out for 20 seconds before the trace was stored and recorded. The voltage was then brought to zero, the strain gages were rezeroed and the voltage was dropped to allow the data to be taken at the reverse polarity. The voltage and gages were then rezeroed and the process was repeated for the next higher voltage point. In this way any drift that might have occurred in the strain gages was mostly eliminated, producing cleaner data.

The free strain response of the interdigitated wafers is compared to the free response of a conventionally electroded wafer of PSI-5A-S2 in Figures 13-16. Both the X and Y strain are plotted versus the effective electric field, $\vec{E}$. Figure 13 compares the X direction high field response of the interdigitated and conventional samples. The negative of the data for the

SPIE Vol. 1917 Smart Structures and Intelligent Systems (1993) / 349

![](./images/812297316819009539_13.jpg)

Figure 13: High Field Comparison of X Direction Strains for Interdigitated (o)
and Conventionally Electroded (*) Wafers, as a Function of Applied
Electric Field Level, $\overline{E}$. Conventional Data (*) is Inverted for Easy
Comparison

![](./images/812297316819009539_14.jpg)

Figure 14: Low Field Comparison of X Direction Strains for Interdigitated (o)
and Conventionally Electroded (*) Wafers as a Function of Applied
Electric Field Level, $\overline{E}$. Conventional Data (*) is Inverted for Easy
Comparison

![](./images/812297316819009539_15.jpg)

Figure 15: High Field Comparison of Y Direction Strains for Interdigitated (o)
and Conventionally Electroded (*) Wafers, as a Function of Applied
Electric Field Level, $\overline{E}$.

![](./images/812297316819009539_16.jpg)

Figure 16: Low Field Comparison of Y Direction Strains for Interdigitated (o)
and Conventionally Electroded (*) Wafers as a Function of Applied
Electric Field Level, $\overline{E}$.

conventional samples is plotted for comparison. In actuality it is
out of phase from the interdigitated response. Figure 13 clearly
indicates the higher strain capability of the interdigitated
specimen. Comparing Figures 13 and 15 demonstrates the
orthotropy of the actuator. It is interesting to note the comparison
with the predictions made from the linear material properties,
using both d33 and -d31. The experimental responses maintain a
comparable ratio of interdigitated to conventional strain but both
specimens produced strain magnitudes much greater than the
linear piezoelectric published material properties. A comparison
of the relative performance of the interdigitated and conventional
wafers is given in Table 1 for 500V/mm average field value.

At the low field levels shown in Figure 14, the interdigitated
specimen has lower strain capability than expected from the d33
constant. This effect is as yet unexplained but may be attributable
to the fact that $\overline{E}$ is actually an average field between two field
singularities at the electrode edges. Nonlinear field and stress
concentration effects may be dominating the response at low field
levels. However, the interdigitated specimen does maintain
higher strain levels than the control.

Figure 15 compares the strain in the Y direction for the high
field case. In the Y direction, the strains of both wafers are in
phase since both the interdigitated and the conventionally
electroded wafers utilize the 31 effect The strain levels for the
interdigitated specimen are lower than those of the

conventionally electroded specimen because of clamping effects in the material directly under the electrodes. This phenomena was generally predicted by theory as shown in Table 1. It is interesting to note that the high strain response of the interdigitated specimen agrees very well with the low field linear d31 material properties of this material because of material nonlinearities.

In the low field case shown in Figure 16, the Y direction strains agree well with the linear material properties and illustrate the model predictions of relatively low Y direction strain in the interdigitated electrode specimen.

As seen form Table 1, the material achieved both the high strain predicted in the X direction and the opposite phase between the X and Y direction strains needed for high actuation orthotropy. The orthotropy of the material is quantified by the ratio X/Y. The experimentally obtained orthotropy ratio was -3.56. The large error is a refleection of the inexplicably low Y direction response.

A large portion of the errors can be attributed to error in the material properties. The inaccuracy of the material properties is due to unavailability of published high field properties. The predictions had to be made using only low field properties.

The transition in behavior between the high and low electric field cases is as yet not fully explained and may require a more rigorous look at the nonlinear mechanics and material properties of phase transitioning (polarization) materials.

Table 1: Data taken at 500 V/mm
(63.5% of Coercive Field)

<table>
<thead>
<tr>
<th>Direction<br>of Strain</th>
<th colspan="2">Data (microstrain)</th>
<th colspan="2">Ratios*</th>
<th rowspan="2">Error</th>
</tr>
<tr>
<th>Interd.</th>
<th>Control</th>
<th>Expermnt</th>
<th>Model</th>
</tr>
</thead>
<tbody>
<tr>
<td>X</td>
<td>324.0</td>
<td>-211.5</td>
<td>-1.53</td>
<td>-1.82</td>
<td>+15.9%</td>
</tr>
<tr>
<td>Y</td>
<td>-90.8</td>
<td>-211.5†</td>
<td>0.43</td>
<td>0.833</td>
<td>-57.0%</td>
</tr>
<tr>
<td>X/Y</td>
<td>-3.56</td>
<td>1.00</td>
<td>-3.56</td>
<td>-2.18</td>
<td>-63.3%</td>
</tr>
</tbody>
</table>

* Ratios are Interdigitated to Control, Model X/Y ratio is the model determined X ratio to the model determined Y ratio

+The control was assumed to be transversely isotropic.

## Conclusions

This paper has presented a new technique for improving the in-plane actuation capability of piezoelectric wafers by using interdigitated surface electrodes. The new technology enables wafers to exhibit both increased magnitude of the free strain and stress capabilities and markedly increased anisotropy in their planar actuation.

Two models were presented for predicting the actuation capabilities as a function of device geometry. The first is a Rayleigh-Ritz technique which used simple assumed field shapes and an electromechanical variational principle to develop an intuitive model of device performance. It predicted planar strains of approximately -1.8 and 0.83 times conventional in plane values and planar stress of approximately -3.1 times conventional values. It captured the high orthotropy of the actuation. The simple Ritz model compared favorably to the results obtained by a piezoelectric finite element model developed within ANSYS.

The finite element model revealed the details of the internal field geometry and validated the Ritz model in regimes of large relative electrode spacing (spacing to thickness ratio >5) where the field distortions near the electrodes could be ignored.

An experimental program established the manufacturing and testing procedures for the interdigitated electrode wafers. Experimental results in free strain tests demonstrated both the increased strain levels and the anisotropy at levels comparable to model predictions. At 500V/mm the modified wafers exhibited 1.53 times higher in plane strain than conventional piezoelectric wafers and anisotropy ratio, R, of -3.56 ( R=1 for conventional piezoceramics). Such improvements have applications in areas needing highly directional actuation such as induced torsion in elastic substrates, and aeroelastic surface control. Actuators can also be developed with electrodes on only one side of a piezoceramic wafer.

Future work will be concentrated in four areas: 1) further experimental investigation of the anisotropic stiffness and force properties, 2) further experimental investigation of new device geometries, 3) further investigation of different active materials such as electrostrictive materials, and 4) improvement of the modeling techniques. Model improvement can be achieved by using nonlinear material modeling for electrostrictors and piezoelectrics. In particular, continuum mechanical models of distributed phase transformation for piezoelectric polarization are needed.

The ultimate application of this technology will be in the actuation of piezoelectric fiber composites, where the ability to apply the electric field in the transverse direction, parallel to the fibers, would be most valuable.

## Acknowledgments

This work was supported by a grant from the Office of Naval Research (Grant # N00-14-92-J-4067).

## References

1 Crawley, E.F. and de Luis, J., "Use of Piezoelectric Actuators as Elements of Intelligent Structures," AIAA Journal, Vol. 25, No. 10, 1987.

2 Crawley, E.F. and Lazarus, K., "Induced Strain Actuation of Isotropic and Anisotropic Plates", AIAA Journal, Vol. 29, No. 6, June 1991, pp. 944-951.

3 Jia, J. and Rogers, C. A., "Formulation of a Laminated Shell Theory Incorporating Embedded Distributed Actuators," Adaptive Structures, AD-Vol 15, Edt. B. K. Wada, The American Society of Mechanical Engineers, New York, New York, 1989

4 Hagood, N.W., Chung, W.H., and von Flotow, A.H., "Modeling of Piezoelectric Actuator Dynamics for Active Structural Control," Journal of Intelligent Material Systems and Structures, Vol. 1, No. 3, July 1990, pp. 327-354.

5 Forward, R.L. and Swigert, C.J., "Electronic Damping of Orthogonal Bending Modes in a Cylindrical Mast-Theory," Journal of Spacecraft and Rockets, January-February, 1981.

6 Hanagud, S., Obal, M.W., and Calise, A.J., "Optimal Vibration Control by the Use of Piezoceramic Sensors and Actuators," Proceedings 28th AIAA/ASME/ASCE/AHS Structures, Structural Dynamics, and Materials Conference, Monterey, California, April 1987, AIAA Paper No. 87-0959, pp. 987-997.

SPIE Vol. 1917 Smart Structures and Intelligent Systems (1993) / 351

<table>
<caption>Table 2: Material Constants for PSI-5A-S2 ††</caption>
<tbody>
<tr>
<td>$e_{31}$</td>
<td>-5.35</td>
</tr>
<tr>
<td>$e_{33}$</td>
<td>15.78</td>
</tr>
<tr>
<td>$e_{15}$</td>
<td>12.29</td>
</tr>
<tr>
<td>$c_{11}^E$</td>
<td>12.03</td>
</tr>
<tr>
<td>$c_{12}^E$</td>
<td>7.52</td>
</tr>
<tr>
<td>$c_{13}^E$</td>
<td>7.517</td>
</tr>
<tr>
<td>$c_{33}^E$</td>
<td>11.09</td>
</tr>
<tr>
<td>$c_{66}^E$</td>
<td>2.1</td>
</tr>
<tr>
<td>$c_{55}^E$</td>
<td>2.1</td>
</tr>
<tr>
<td>$K_{11}$</td>
<td>1730</td>
</tr>
<tr>
<td>$K_{33}$</td>
<td>1700</td>
</tr>
</tbody>
</table>

†† units are $10^{10}$ Pa for stiffness, and Pa m/V for stress-to-field constants.
Stiffness values are not published as characterization is ongoing.

7 Lazarus, K. and Crawley, E.F., "Multivariate High-Authority Control of Plate-Like Active Structures," AIAA Paper No. 92-2529, AIAA Conference on Structures, Structural Dynamics, and Materials, Dallas, TX, April 13-15, 1992.

8 Ehlers, S.M. and Weisshaar, T.A., "Static Aeroelastic Behavior of an Adaptive Laminated Piezoelectric Composite Wing," AIAA Paper No. 90-1078, Proceedings of the 31st AIAA./ASME/ASCE/AHS Structures, Structural Dynamics, and Materials Conference, Long Beach, CA, April 1990.

9 Rogers, C. A., Fuller, C. R., "Recent Advances in Active Control of Sound and Vibration," Proceedings of the VPI and SU Conference on Recent Advances in Active Control of Sound and Vibration, Blacksburg, VA, April, 1991.

10 Cutchen, J. Thomas, "PLZT Thermal/Flash Protective Goggles: Device Concepts and Constraints", Ferroelectrics, Vol 27, pp 173-178, 1980.

11 Harris, James, Jack Cyrus, and George Laguna, "Minimum/Consistent Voltage Lead Lanthanum Zirconate Titanate (PLZT) Electro-optic Shutters", Proceedings of the SPIE, Vol. 307, p 53-59, 1981.

12 Cutchen, Thomas, James Harris, and George Laguna, "PLZT Electro-optic Shutters: Applications", Applied Optics, Vol. 14, No. 8, p1866-1873, August 1975.

13 Tanaka, Katshuiko, Masami Yamaguchi, Hiroyuki Seto, Michihiro Murata and Kikuo Wakino, "Analyses of PLZT Electro-optic Shutter and Shutter Array", Japanese Journal of Applied Physics, Vol. 24, pg 177, 1985

14 Toda, Kohji and Yoshinari Yamashita, "A Surface Acoustic Wave Tristate Device", Ferroelectrics, Vol. 42, pp 215-218, 1982.

15 Shiosaki, Tadashi and Akira Kawabata, "Piezoelectric Thin Films for SAW Applications", Ferroelectrics, Vol 42, 1982.

16 Fuda, Yoshiaki, Tetsuo Yoshida, Tomeji Ohno, and Shoko Yoshikawa, "Ceramic Actuator with Three-Dimensional Electrode Structure", IEEE International Symposium on Applications of Ferroelectrics, Greenville, S.C., Aug 31-Sep 3, 1992.

17 Shimizu, Hiroshi, Kiyoshi Nakamura, and Shigeru Oyama, "A Piezoelectric Single-Plate Bending Vibrator Using Interdigital electrodes", Japanese Journal of Applied Physics, Vol. 22, p163165, 1983.

18 Hirose, Seiji, Hisashi Nakamura, and Hiroshi Shimizu, "Analysis of Piezoelectric Ceramic LengthExpansion-Mode Resonators Using Interdigital Electrodes for Both Poling Treatment and AC Excitation", Electronics and Communications in Japan, Part 1, Vol. 71, No. 5, p41-50, 1988.

19 IEEE Std 176-1978, IEEE Standard on Piezoelectricity, The Institute of Electrical and Electronics Engineers, 1978.

20 Gaudenzi, P., Bathe, K.J., "An Iterative Finite Element Procedure For the Analysis of Piezoelectric Continua", Report 92-1, Dec. 1992, Finite Element Research Group, Department of Mechanical Engineering, MIT, Cambridge, MA.

21 Ostergaard, D.F., Coupled Field Analysis, Houston, PA: Swanson Analysis Systems, Inc., 1989.

### Nomenclature

The following nomenclature is used throughout this manuscript:
| | |
|---|---|
|$c_{ij}^E$|ijth piezoceramic stiffness at constant field|
|$s_{ij}^E$|ijth piezoceramic compliance at constant field|
|$d_{ij}$|ijth piezoceramic electric field-to-strain coefficient|
|$e_{ij}$|ijth piezoceramic electric field-to-stress coefficient|
|$\varepsilon_{ij}^T$|ijth piezoceramic dielectric, constant stress conditions|
|$S_i$|ith direction material strains|
|$T_i$|ith direction material stress|
|$D_i$|ith direction electrical displacement|
|$E_i$|ith direction electric field|
|$\boldsymbol{c}^E$|piezoceramic stiffness matrix at constant field|
|$\boldsymbol{s}^E$|piezoceramic compliance matrix at constant field|
|$\boldsymbol{\varepsilon}^S$|piezoceramic dielectric matrix at constant strain|
|$\boldsymbol{\varepsilon}^T$|piezoceramic dielectric matrix at constant stress|
|$\boldsymbol{e}$|piezoceramic electric field-stress coupling matrix|
|$\boldsymbol{d}$|piezoceramic electric field-strain coupling matrix|
|$\boldsymbol{S}$|material engineering strain|
|$\boldsymbol{T}$|material stress|
|$\boldsymbol{D}$|electrical displacement vector|
|$\boldsymbol{E}$|electric field vector|
|$p$|surface electrode spacing|
|$h$|wafer thickness|
|$l$|wafer length|
|$w$|surface electrode width|
|$\alpha$|geometric parameter|
|$\beta$|geometric parameter|
|$T$|kinetic energy term|
|$U$|mechanical potential energy term|
|$W_e$|electrical potential energy term|
|$W_m$|magnetic potential energy term|
|$W$|mechanical work term|
|$u_i$|ith direction displacement|
|$\boldsymbol{u}$|displacement vector|
|$\boldsymbol{T}_s$|surface stress vector|
|$\overline{T}_i$|average normal surface stress|
|$\overline{S}_j$|average strain in ith direction|
|$\overline{S}_x$|average X direction strain in region under electrodes|
|$V$|magnitude of voltage applied to electrodes|
|$\varphi$|electric potential field|
|$\overline{E}$|effective field between electrodes|
|$(\cdot)^T, (\cdot)_t$|matrix transpose|

352 / SPIE Vol. 1917 Smart Structures and Intelligent Systems (1993)