# An elastic model to quantify the effect of moisture on the mechanical properties of concrete at the time of test

J. S. Guo* and P. Waldron†

Babtee Group; Sheffield University

This paper describes the detailed development of a mathematical model for determining the effect of moisture on the mechanical properties of concrete at the time of test. Based on the theory of elasticity, it focuses on the stress distribution around spherical cavities in concrete filled with different types of inclusions. Results obtained from the mathematical model have assisted in interpreting a number of experimental phenomena that have been the subject of long-term controversy. In particular the model explains why compressive strength tests yield higher measured values for dry concrete specimens than for otherwise identical wet specimens, while the measured values of static modulus exhibit the opposite effect. It also provides an explanation as to why measured tensile strength values obtained from direct tension, tensile splitting or torsion tests are largely independent of moisture content. The model provides an analytical tool for studying the interdependence between the mechanical properties of concrete and its moisture content. It also yields essential input for the computational simulation of the behaviour of concrete structures that are subjected to large changes of moisture condition. Moreover, it provides a method for analysing the stresses at the surface of any type of inclusion but particularly for cavities filled with incompressible liquids under any stress field.

## Notation

|  |  | $ww$ | hoop stress (on the equator in the same direction as the applied load) |
|---|---|---|---|
| $\Delta$ | dilatation or volume expansion <br> $\Delta = e = \frac{\partial u_x}{\partial x} + \frac{\partial u_y}{\partial y} + \frac{\partial u_z}{\partial z}$ | $vw$ | hoop stress (on the equator but at right angles to $ww$) |
| $\nabla^2$ | Laplacian operator $\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}$ | $rw$ | shear stress |
| $\lambda$ | Lame's constant $\lambda = \frac{vE}{(1 - v)(1 - 2v)}$ | $u_r$ | radial displacement |
| $\mu$ | modulus of rigidity | $u_w$ | circumferential displacement |
| $E$ | modulus of elasticity |  |  |
| $v$ | Poisson's ratio |  |  |
| $u_x$ | displacement of $x$ direction |  |  |
| $u_y$ | displacement of $y$ direction |  |  |
| $u_z$ | displacement of $z$ direction |  |  |
| $rr$ | radial stress |  |  |

---

* Babtee Group, 95 Bothwell Street, Glasgow, G2 7HX, UK
† Department of Civil and Structural Engineering, Sheffield University, Mappin Street, Sheffield S1 3JD, UK.

(MCR 850) Paper received 23 March 2000; last revised 9 August 2000; accepted 30 January 2001

## Introduction

Concrete contains a great number of voids compris- ing gel pores, capillary pores and flaws. At the two extremes, these voids may either be full (filled with absorbed water when the concrete is saturated) or empty (filled with air) when the concrete is fully dry. Under intermediate conditions, a mixture of water, water vapour and air may be present. The change in moisture content caused by wetting and drying has been shown to have a considerable effect on the mech- anical properties of concrete and in a variety of ways. $^{1-5}$ For example, it is now widely accepted that a concrete with a lower moisture content at the time of

Guo and Waldron

test will have a higher compressive strength and lower static modulus than a concrete with a higher moisture content taken from the same mix and subjected to an identical curing process. However, there is no univer- sally accepted mechanistic interpretation of the phe- nomenon, and no mathematical model or numerical simulation apparently exits to take this effect into ac- count.

Feldman and Sereda $^{6}$ suggested that the Si-O bonds can break more readily to form Si-OH HO-Si bonds in the presence of adsorbed water on the gel particles. When the concentration of water molecules is sufficient to maintain the delivery of moisture to a spreading crack, no further decrease in strength will occur. How- ever, this is disputed by Glucklich and Korin, $^{7}$ who question whether enough water can be continuously present at the crack tip to maintain the necessary ag- gressive environment. Other researchers, including Wittmann $^{2}$ and Neville, $^{3}$ explained this phenomenon based on combination of the Griffith's fracture criterion and surface free energy theory. It is suggested that change in strength during adsorption is correlated with surface free energy. When water is absorbed into the gel, the spreading pressure forces the gel surfaces further apart resulting in a reduction in the Van der Waals forces between gel particles. This leads to a decrease in the surface free energy since the specific surface energy is proportional to the adhesive forces. Thus, using Griffith's criterion, the critical stress de- creases as the amount of absorbed water increases.

Popovics $^{8}$ argued that a moisture gradient over the cross-section of a prismatic concrete specimen causes a change in the measured strength. When the moisture level on the outside is lower than that on the inside of a concrete specimen, the outside layer tends to shrink because it is dryer than the core of the specimen. This shrinkage is restrained by the core of the specimen. Consequently, the core is subjected to a lateral biaxial compression, increasing its measured compressive strength in the third direction. However, tests have shown that well-cured mortar prisms and concrete cores and cylinders, when completely dried, have ahigher compressive strength than when tested wet. $^{9}$  Since these specimens were not subjected to differen- tial shrinkage, no such biaxial stress system would have been induced and therefore this phenomenon does not explain the increase in strength. Galloway et al. $^{10}$ argued that the occurrence of water in the con crete may cause a dilation of the cement gel which results in a weakness in cohesion of the solid particles. Another hypothetical explanation has been suggested by Neville, $^{5}$ Popovics $^{8}$ and Wittman. $^{2}$ This states that the water absorbed into the gel pores leads to a trans- verse bursting effect in the solid matrix of the con- crete and this effect increases with an increase in the external compressive load. However, this is purely a conceptual hypothesis without any theoretical model to support it.

Guo $^{11}$ has proposed that the effect of moisture on the measured mechanical properties should be consid- ered separately in two significantly different stages. The first stage is prior to the measurement of the mechanical properties when moisture migrates from or into the concrete body. Changes in magnitude of shrinkage and creep strains, which are cause by moist- ure migration, affect the stress distribution that conse- quently results in differences in the mechanical properties such as strength and elasticity. The second stage applies at the time of mechanical testing when moisture acting as a component of the concrete re- sponds to external load. Some detailed theoretical studies into the moisture effect in the first stage have already been reported by Guo $^{11}$ using a model that predicts the stresses at interface between the cement paste and the aggregate in concretes subjected to ther- mal loading. This study indicated that large changes of moisture content have a significant effect on the values of shrinkage, creep, elastic modulus, coefficient of thermal expansion and thermal conductivity. This paper focuses on the effects of moisture in the second stage only.

## Analytical developments

In developing a theoretical model for the effects of moisture on concrete at the time of testing, a considera- tion of the three general equations of equilibrium and displacement yields a solution for the case of an iden- tical spherical inclusion inside an elastic solid body. Further consideration is then given to the description of stress in the solid body when the spherical inclusion is assumed to be fully filled with compressible air/vapour or with incompressible water. By applying these models to simple structural concrete elements subjected to idealised loading, the effects of moisture content on the static modulus of elasticity and the distribution of stress have been obtained for compressive, tensile and shear loading conditions.

For the purposes of mathematical deduction and cal- culation, it has been assumed that: (i) the pores are spherical; (ii) the concrete surrounding the pores is infinite in extent and subjected to uniform applied stress at infinity; and (iii) the concrete has the ideal properties of elasticity, isotrophy and homogeneity.

Based on the theory of elasticity, the displacement in an elastic solid free from body forces can be derived from a combination of the equation of equilibrium,Hooke's Law and the boundary conditions (Love, $^{12}$ Timoshenko and Goodie $^{13}$ and Saada $^{14}$ )

$$(\lambda+\mu)\left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z}\right) \Delta+\mu \nabla^{2}\left(u_{x}, u_{y}, u_{z}\right)=0 \quad(1)$$

As the pores to be analysed are assumed to be spherical bodies, it is convenient to carry out the analy- sis in polar coordinates (r-w-v transformed from the

152
Magazine of Concrete Research, 2001, 53, No. 3

An elastic model to quantify the effect of moisture on the mechanical properties of concrete at the time of test

Cartesian coordinates (x-y-z). The general stress-strain formulae then become

$$
r r, w w, v v,=2 \mu\left[\frac{v}{1-2 v} \Delta+\left(e_{r r}, e_{w w}, e_{v v}\right)\right] \tag{2}
$$

$$
r w=\mu e_{r w}
$$

where

$$
e_{r r}=\frac{\partial u_{r}}{\partial r}
$$

$$
e_{w w}=\frac{1}{r} \frac{\partial u_{w}}{\partial w}+\frac{u_{r}}{r}
$$

$$
e_{v v}=\Delta-e_{r r}-e_{w w}
$$

$$
e_{r w}=\frac{1}{r} \frac{\partial u_{r}}{\partial w}+r \frac{\partial}{\partial r}\left(\frac{u_{w}}{r}\right)
$$

### Uniaxial compression

For the case of a spherical inclusion inside an elastic body, which is subjected to a uniform uniaxial compressive stress $p$ applied remotely from the inclusion, Goodier¹⁵ provided the solution. Summarising his results, the stresses and displacements in the concrete surrounding the inclusion are as follows (see Fig. 1)

$$
\begin{aligned}
r r= & 2 \mu\left\{\frac{2 A}{r^{3}}-\frac{2 v}{1-2 v} \frac{C}{r^{3}}+12 \frac{B}{r^{5}}\right. \\
& \left.+\left[-\frac{2(5-v)}{1-2 v} \frac{C}{r^{3}}+36 \frac{B}{r^{5}}\right] \cos 2 w\right\}+\frac{p}{2}(1+\cos 2 w)
\end{aligned}
$$

$$
\begin{aligned}
w w= & 2 \mu\left\{-\frac{A}{r^{3}}-\frac{2 v}{1-2 v} \frac{C}{r^{3}}-3 \frac{B}{r^{5}}\right. \\
& \left.+\left[\frac{C}{r^{5}}-21 \frac{B}{r^{5}}\right] \cos 2 w\right\}+\frac{p}{2}(1-\cos 2 w)
\end{aligned}
$$

$$
\begin{aligned}
v v= & 2 \mu\left\{-\frac{A}{r^{3}}-\frac{2(1-2 v)}{1-2 v} \frac{C}{r^{3}}-9 \frac{B}{r^{5}}\right. \\
& \left.+\left[3 \frac{C}{r^{3}}-15 \frac{B}{r^{5}}\right] \cos 2 w\right\} \tag{3}
\end{aligned}
$$

$$
r w=2 \mu\left[-\frac{2(1+v) C}{(1-2 v) r^{3}}+24 \frac{B}{r^{5}}\right] \sin 2 w-\frac{p}{2} \sin 2 w
$$

$$
\begin{aligned}
u_{r}= & -\frac{A}{r^{2}}-\frac{3 B}{r^{4}}+\left[\frac{5-4 v}{1-2 v} \frac{C}{r^{2}}-9 \frac{B}{r^{4}}\right] \cos 2 w \\
& +\frac{p r}{2 E}[(1-v)+(1-V) \cos 2 w]
\end{aligned}
$$

$$
u_{w}=-\left[\frac{2 C}{r^{2}}+6 \frac{B}{r^{4}}\right] \sin 2 w-\frac{p r}{2 E}(1+v) \sin 2 w
$$

![](./images/811827389620289537_1.jpg)

Fig. 1. Coordinate system adopted for the spherical inclusion

Stresses and displacements inside the spherical inclusion are given by

$$
\begin{aligned}
r r= & 2 \mu\left\{\frac{(1+v)}{1-2 v} H+F-v G r^{2}\right. \\
& \left.+\left[3 F-3 v G r^{2}\right] \cos 2 w\right\}
\end{aligned}
$$

$$
\begin{aligned}
w w= & 2 \mu\left\{\frac{(1+v)}{1-2 v} H+F-5 v G r^{2}\right. \\
& \left.-\left[3 F+7(2-v) G r^{2}\right] \cos 2 w\right\}
\end{aligned}
$$

$$
\begin{aligned}
v v= & 2 \mu\left\{\frac{(1+v)}{1-2 v} H-2 F-(15-7 v) G r^{2}\right. \\
& \left.-(7+11 v) G r^{2} \cos 2 w\right\} \tag{4}
\end{aligned}
$$

$$
r w=2 v\left\{3 F+(7+2 v) G r^{2}\right\} \sin 2 w
$$

$$
u_{r}=H r+F r+2 v G r^{3}+\left[3 F r+6 v G r^{3}\right] \cos 2 w
$$

$$
u_{w}=-\left[3 F r+(7-4 v) G r^{3}\right] \sin 2 w
$$

where $A, B, C, F, G$ and $H$ are constants determined by the specified boundary conditions.

By considering the boundary condition $(r=a)$ where perfect contact is assumed between the spherical inclusion and elastic body, the values of the six unknown constants can be obtained. The values of $A, B$ and $C$ are (Goodier)¹⁵

Magazine of Concrete Research, 2001, 53, No. 3

Guo and Waldron

$$
\begin{aligned}
\frac{A}{a^{3}}= & -\frac{p}{8 \mu} \frac{\mu-\mu_{i}}{(7-5 v) \mu+(8-10 v) \mu_{i}} \\
& \times \frac{\left(1-2 v_{i}\right)(6-5 v) 2 \mu+\left(3+19 v_{i}-20 v v_{i}\right) \mu_{i}}{\left(1-2 v_{i}\right) 2 \mu+\left(1+v_{i}\right) \mu_{i}} \\
& +\frac{p}{4} \frac{\left[(1-v) \frac{1+v_{i}}{1+v}-v_{i}\right] \mu_{i}-\left(1-2 v_{i}\right) \mu}{\left(1-2 v_{i}\right) 2 \mu+\left(1+v_{i}\right) \mu_{i}} \\
\frac{B}{a^{5}}= & \frac{p}{8 \mu} \frac{\mu-\mu_{i}}{(7-5 v) \mu+(8-10 v) \mu_{i}} \\
\frac{C}{a^{3}}= & \frac{p}{8 \mu} \frac{5(1-2 v)\left(\mu-\mu_{i}\right)}{(7-5 v) \mu+(8-10 v) \mu_{i}}
\end{aligned}
$$

where the elastic constants of the spherical inclusion are distinguished by the subscript $i$.

A concrete cavity fully filled with air or vapour.
For the case where the cavity is filled with compres- sible air or vapour, it can be assumed that $\mu_{i}=0$. The distributions of deduced stresses around the hol- low cavity are then given by

$$
\begin{aligned}
r r= & 0 \\
w w= & p\left\{\frac{5-10 v}{14-10 v}-\frac{8+5 v}{14-10 v} \cos 2 w\right] \\
& +\frac{p}{2}(1-\cos 2 w) \\
v v= & p\left\{\frac{-3}{14-10 v}-\frac{15 v}{14-10 v} \cos 2 w\right\} \\
r w= & 0
\end{aligned}
$$

Assuming the same value of of $v=0 \cdot 2$, these four stress distributions for $w=0$ to $\pi$ are presented in Fig. 2. The radial and shear stresses are always zero around the surface of the hollow cavity. The term $w w$, repre- senting the hoop stress on the equator in the same direction as the applied load, has a maximum compres- sive stress value of $2 p$ at $w=\pi / 2$ and a maximum tensile stress of magnitude $-\{(3+15 v) /(14-10 v)\} p$ at the points $A$ and $A^{\prime}$ (top and bottom of the cavity, respectively). This is equivalent to a tensile stress of $-0.5 p$ for the typical value of $v=0.2$. The hoop stress $v v$ on the equator at right angles to $w w$ has a zero value at $w=\pi / 2$ but the same values as the hoop stress $w w$ at the points $A$ and $A^{\prime}$.

![](./images/811827389620289537_2.jpg)

Fig. 2. Stress distributions around the hollow cavity in uniaxial compression

A concrete cavity fully filled with water. From equations (3) and equation (5), it is apparent that radial displacement $u_{r}$ is a function of both radius $r$ and angle $w$, which can be expressed as

$$
u_{r}=f_{1}(r, p)+f_{2}(r, p) \cos 2 w
$$

where $f_{1}$ is a function of $r$ and $p$ only irrespective of the value of $w$, and $f_{2}$ is a function of $r, p$ and $\cos 2 w$. Considering the second part of equation (7) only, the total change in $u_{r}$ around the sphere due to this compo- nent is zero such that

$$
\int_{0}^{2 \pi} f_{2}(r, p) \cdot \cos 2 w \cdot d w \equiv 0
$$

For the purpose of estimating volume change in the spherical cavity, the second term may therefore be removed from equation (7), yielding

$$
u_{r}=\left\{\frac{10-10 v}{7-5 v}+\frac{2(1-v)}{1+v}\right\} \frac{a p}{8 \mu}
$$

Apparently, this is always greater than zero, therefore a change in the volume of the spherical cavity is un- avoidable. However, in the case of a cavity fully filled with water, the change in the cavity volume is resisted

An elastic model to quantify the effect of moisture on the mechanical properties of concrete at the time of test

by the water inside the cavity. Provided the usual assumption that water is incompressible is satisfied (any loss of water being neglected), the volume of the cavity filled with water does not change, and the resis- tance produced by the pressurised water is always con- stant in all directions for a given external load. The theoretical model may therefore be considered as a superimposition of two parts. This is shown in Fig. 3 where (a) represents the case being studied of a single water filled cavity within an elastic (concrete body), (b) represents the hollow cavity within the elastic body subjected to a uniform uniaxial compressive stress, and (c) represents the cavity in the unloaded elastic body subjected to an uniform internal pressure.

In case (b), the radial displacement $u_{rb}$ can be expressed as in equation (3)

$$
\begin{aligned}
u_{r b}= & -\frac{A}{r^{2}}-\frac{3 B}{r^{4}}+\left\{\frac{5-4 v}{1-2 v} \frac{C}{r^{2}}-9 \frac{B}{r^{4}}\right\} \cos 2 w \\
& +\frac{p r}{2 E}\{(1-v)+(1+v) \cos 2 w\}
\end{aligned}
$$

For $r=a$ at the cavity boundary, the radial displacement (denoted as $u_{rb1}$) derived from that part of the equation only affecting volume change (i.e. neglecting the $\cos 2 w$ term) is as given by equation (9)

$$
u_{r b 1}=\left\{\frac{10-10 v}{7-5 v}+\frac{2(1-v)}{1+v}\right\} \frac{a p}{8 \mu}
$$

In case (c), the radial displacement $u_{rc}$, based on Hooke's law, can be obtained as follows

$$
E \frac{u_{r c}}{a}=(1-v) w w_{c}-v r r_{c} \quad(10)
$$

since $r r_{c}=-q, w w_{c}=v v_{c}=q / 2$ (Timoshenko and Goodier $^{13}$ ) and $\mu=E / 2(1+v)$, equation (10) may be simplified to

$$
u_{r c}=\frac{a}{4 \mu} q \quad(11)
$$

![](./images/811827389620289537_3.jpg)

Fig. 3. Schematic illustration of (a) theoretical model repre- sented by the superposition of (b) the externally loaded speci- men containing an empty spherical cavity, and (c) the unloaded specimen subjected to uniform internal cavity pres- sure

Equating the displacements $u_{rb1}=u_{rc}$, the following relationship between the intensity of the external load and the internal cavity pressure is obtained

$$
q=\frac{p}{2}\left\{\frac{10-10 v}{7-5 v}+\frac{2(1-v)}{1+v}\right\} \quad(12)
$$

If we chose a typical value of Poisson's ratio for concrete, $v=0 \cdot 2$, then

$$
q=-0.667 p \quad(13)
$$

and

$$
\begin{aligned}
r r_{c} & =-0.667 p \\
w w_{c} & =0.333 p \\
v v_{c} & =0.333 p
\end{aligned} \quad(14)
$$

The stress distribution around the cavity boundary $r=a$ can then be obtained for case (a) by combining the solutions for cases (b) and (c)

$$
\begin{aligned}
r r= & 0.667 p \\
w w= & p\left\{\frac{5-10 v}{14-10 v}-\frac{8+5 v}{14-10 v} \cos 2 w\right\} \\
& +\frac{p}{2}(1-\cos 2 w)-0.333 p \\
v v= & p\left\{\frac{-3}{14-10 v}-\frac{15 v}{14-10 v} \cos 2 w\right\}-0.333 p \\
r w= & 0
\end{aligned}
$$

The corresponding stresses for $w=0$ to $\pi$ are pre sented in Fig. 4. It can be seen that the shear stress still remains at zero around the whole surface which is in accordance with the boundary condition, since the water can not produce resistance to the shearing defor- mation. While the radial stress increases from zero to0.667 p around the unfilled cavity, the hoop stresses at the points $A$ and $A^{\prime}$ are in tension but with a magnitude of $-0.833 p$ . This is $66.7 \%$ higher than that for the hollow cavity and this indicates that, in specimens with water filled cavities, the first crack will initiate at a lower critical load. Generally, specimens having a lower critical crack load will display reduced strength despite experiencing additional plasticity between crack initia- tion and final failure. In comparing this theory with existing experimental results, general agreement exists. For instance, Pihlajavaara $^{3}$ reported from his experi mental results on a wide range of concretes that dry compressive strength is about $30 \%$ to $60 \%$ higher than wet strength. A comparison of the two hoop stresses within the range $w=0$ to $\pi$ for the hollow cavity and the cavity fully filled with water is shown in Fig. 5 for different loading situations.

Since the water in the cavity develops an internal pressure equivalent to two-thirds of the applied external stress $(r r=0.667 p)$ , it is to be expected that the static modulus of elasticity of the concrete will increase. This

Magazine of Concrete Research, 2001, 53, No. 3

![](./images/811827389620289537_4.jpg)

Fig. 4. Stress distribution around the water filled cavity in uniaxial compression

![](./images/811827389620289537_5.jpg)

Fig. 5. Comparison of hoop stress (ww) for the hollow cavity and the cavity fully filled with water under different loading situations

confirms experimental observations that the static mod- ulus of elasticity of a dried concrete is always lower than that of an otherwise identical wet concrete. For a detailed interpretation of this phenomenon consider the cubic element of side length $L$ extracted from a con crete specimen subjected to a uniaxial uniform load of intensity of $p$ in the $z$ direction (Fig. 6). If a hollow spherical cavity of diameter $D$ is included within the elastic body with a static modulus of $E$, based on the thoery of elasticity, the displacement $\Delta L_{1}$ over the whole length $L$ can be estimated as follows (detailed in Guo)¹¹

$$
\Delta L_{1}=\frac{p}{E}\left[(L-D)+\frac{4 L^{2} D}{4 L^{2}-\pi D^{2}}\right] \tag{16}
$$

If an incompressible sphere is included in the elastic body, the displacement $\Delta L_{2}$ over the whole length $L$, under the same external load, can be approximated by the following equation

$$
\Delta L_{2}=\frac{p}{E}\left[(L-D)+\frac{4 L^{2}-0.667 \pi D^{2}}{4 L^{2}-\pi D^{2}} D\right] \tag{17}
$$

It is apparent that $\Delta L_{2}$ is always less that $\Delta L_{1}$, under the same external load $p$. An element with a cavity

An elastic model to quantify the effect of moisture on the mechanical properties of concrete at the time of test

![](./images/811827389620289537_6.jpg)

Fig. 6. Schematic model to determine the influence of moisture content on the static modulus of elasticity

fully filled with water is therefore stiffer than an element with a hollow cavity and the extent is dependent on the ratio of $D/L$. The dependence of $\Delta L_1/\Delta L_2$ on the $D/L$ ratio, based on equations (16) and (17), is presented in Fig. 7. By way of an example, consider two specimens in which the ratio of voids $D/L$ is equal to 0·5 and 0·667. The corresponding values of the cavity to total element volume are 6·5% and 15·5%, and the displacement ratios $(\Delta L_1/\Delta L_2)$ are then 1·078 and 1·213. This represents an increase in stiffness of 7·8% and 21·3% respectively for the two specimens with water filled cavities over those values obtained for the dried specimens.

Considering the analytical results above, and noting that the porosity (ratios and voids) for normal concrete is usually within the range 5–16% (Neville⁵ and Brandt),¹⁶ it may be expected that a saturated specimen would yield an increase in static modulus in comparison with that for an otherwise identical dried specimen within the range 7–22%. This is in general agreement with the experimental results reported by Davis and Troxell,¹⁷ who conducted an extensive experimental investigation into the effect of moisture condition on the secant modulus of elasticity for a wide range of concretes. Results show that wet concrete specimens consistently had a higher modulus of elasticity than dry specimens. The difference in measured moduli between the two moisture conditions was in the range from 12–25% decreasing slightly with an increase in the age of the concrete.

### Uniaxial tension
For the case of a concrete specimen containing a hollow cavity, subjected to uniform axial tension applied remotely from the cavity, the stress distribution can be simply expressed by equation (6) but with the term $p$ replaced by $-p$. For the case of a cavity fully filled with water, the external tensile stress produces an increase in the volume of the hollow cavity rather than a decrease as it does under compression. This can be clearly seen from equation (9). However, in this case, the water cannot provide any significant resistance to the increase in the volume of the cavity which will be filled with water vapour. Although the stresses are not affected by the presence of moisture, the maximum hoop stress $ww$ is four times greater than that for the specimen subjected to compression and it occurs at $w=\pi/2$ and $3\pi/2$ rather than at $w=0$ and $\pi$, as shown in Fig. 5. The

![](./images/811827389620289537_7.jpg)

Fig. 7. Correlation between static modulus of elasticity, ratio of void and ratio of $D/L$

Magazine of Concrete Research, 2001, **53**, No. 3

Guo and Waldron

stress distributions around hollow and water filled cav- ities in tension are presented in Fig. 8.

Pure shear

Consider the case of a hollow cavity in an elastic body that is subjected to pure shear stress applied remotely from the cavity. A pure shear stress state can be obtained by combining a compressive stress with an equal tensile stress applied perpendicularly at the same distance from the cavity, as shown in Fig. 9. Hence, based on equation (6), the stress distributions around the cavity for the pure shear stress state can be derived (Fig. 10) as follows

$$rr = 0$$

$$
\begin{align*}
ww &= -p\frac{8+5v}{14-10v}\cos2w+\frac{p}{2}(1-\cos2w) \\
&\quad +p\frac{8+5v}{14-10v}\cos2\left(w+\frac{\pi}{2}\right) \\
&\quad -\frac{p}{2}\left[1-\cos2\left(w+\frac{\pi}{2}\right)\right] \tag{18}
\end{align*}
$$

$$
vv = -p\frac{15v}{14-10v}\cos2w+p\frac{15v}{14-10v}\cos2\left(w+\frac{\pi}{2}\right)
$$

$$rw = 0$$

The stresses $rw$ and $rr$ are zero around the surface of the cavity. The component of hoop stress $vv$ is the same as when in compression but $ww$ yields a maxi- mum tensile stress as high as $-2.5p$ (Fig. 10), which is five times greater than that for the specimen sub- jected to uniaxial compression (Fig. 5).

In the case of a concrete cavity fully filled with water, although both the compressive and tensile com- ponents of the external shear load contribute to a change in cavity shape, the total volume change is zero. As a consequence, the water in the cavity is not pres- surised and hence provides no internal reaction. There- fore, the stress distributions in this case are the same as those given by equation (18), and are shown graphically in Fig. 10.

![](./images/811827389620289537_8.jpg)

Fig. 9. Schematic illustration of the external loading system for the pure shear stress situation

![](./images/811827389620289537_9.jpg)

Fig. 8. Stress distributions around hollow and water filled cavities in uniaxial tension

Analytical results and discussion

Based on the mathematical model developed above, the following significant remarks can be made.

The effect of moisture on the two principal strength tests

In the two principal tensile strength tests, the analysis shows that the stress distribution around an empty

![](./images/811827389620289537_10.jpg)

Fig. 10. Stress distributions around hollow and water filled cavities in shear

cavity and water-filled cavity are the same. It is therefore expected that the strength values measured by the direct tension test and tensile splitting test are both entirely independent of the moisture condition of the specimen at the time of testing. In practice, however, direct tension test specimens that have been allowed to air-dry before testing display a slight reduction in strength over similar specimens tested in a saturated condition. This difference is likely to be due to the presence of differential stresses induced by restrained shrinkage prior to the application of the load since the air-drying causes the surface layer to shrink more than the core of the concrete. In the tensile splitting test, the system of self-equilibrated tensile stresses caused by the differential drying shrinkage before testing will complement, to some extent, the load-induced compressive stress in the vicinity of the applied loads. As a consequence, the strength determined by the splitting test, although very close to that determined by the direct tensile strength of concrete, is expected to be slightly higher.

In the preceding theory, it has been demonstrated that the compressive test is much more likely to be affected by moisture content than are the direct tension and tensile splitting tests. As indicated by the analytical results, the maximum hoop stress for a specimen under uniaxial compressive loading is approximately 1·667 times higher when the cavities are filled with water than when filled with air or vapour. This is believed to be the dominant factor contributing to the experimental observation that the measured uniaxial compressive strength for a pre-dried specimen is higher than that for an otherwise identical wet specimen. Despite the greater significance of moisture content for concrete tested in compression, the compression test still remains the most commonly used standard test method for determining characteristic strength. This may be attributed to the fact that concrete is generally used in compression, and that the values obtained from the test are not significantly affected by centralisation errors (as for the direct tension test) and represent the average characteristics of the whole specimen (unlike those from the tensile splitting test). Given the pre-eminent position of the compression test in construction practice, careful control and standardisation of the moisture condition at the time of test is clearly of some importance.

### Quantitative evaluation of the effect of different types of inclusion on stress distribution

For concretes subjected to uniaxial compressive loading, the radial, hoop and shear stress distributions are presented in Figs 11–14 respectively for a range of different cavity conditions. These include hollow and water filled cavities, cavities containing alternatively a rigid ($\mu = \infty$) inclusion, an aggregate particle ($E_i = 4E = 90\ \text{kN/mm}^2$), and a particle with the same static modulus as the surrounding concrete ($E_i = E = 22.5\ \text{kN/mm}^2$). Firstly, it can be seen that when $E_i = E$ the four stress distributions are exactly the same as those for a specimen of homogeneous concrete subjected to an uniform uniaxial compressive load, as is to be expected. It can also be seen that the maximum tensile hoop stresses $ww$ and $vv$ occur in specimens in which the cavities are fully filled with water in which the shear stress always remains zero. If $E_i < E$, tensile hoop stresses ($ww$ and $vv$) occur. Otherwise, compressive hoop stresses of increasing intensity are developed for inclusions of increasing stiffness (see Figs 12 and 13). However, the value of shear stress also increases

![](./images/811827389620289537_11.jpg)

Fig. 11. Radial stress (rr) distributions for different inclusions arising from uniaxial compression (rigid cavity means $E_2 = \infty$, same as following)

![](./images/811827389620289537_12.jpg)

Fig. 12. Hoop stress (ww) distributions for different inclusions arising from uniaxial compression

with an increase in the stiffness of the inclusion, and has a maximum value approximately equal to that of the tensile stress caused by the pressure of water at $w = k\pi/4(k = 1, 3, 5, 7)$ as can be seen from Fig. 14. This indicates that there is no tensile hoop stress around the boundary between aggregate and cement paste for normal concrete subjected to a uniaxial compression load. With the development of higher stresses inside the specimen resulting from an increase of the external load, initial tensile type cracks are highly likely to occur around a cavity fully filled with water rather than around an aggregate particle. However, shearing type cracks between the cement paste and aggregate are also entirely possible due to the high values of shear stress developed.

Quantitative implementation of moisture effect on multi-dimensional compressive stress field

The model also predicts that different types of compression tests are affected by moisture content to different extents. As determined earlier, the maximum tensile stresses $ww$ and $vv$ around a fully water filled cavity are $-0.83\ p$ for the uniaxial compressive state of stress. If the same concrete specimen is subjected to an equivalent multi-axial state of compressive stress, the hoop stresses $ww$ and $vv$ at points of A and $A'$ both

An elastic model to quantify the effect of moisture on the mechanical properties of concrete at the time of test

![](./images/811827389620289537_13.jpg)

Fig. 13. Hoop stress (vv) distributions for different inclusions arising from uniaxial compression

![](./images/811827389620289537_14.jpg)

Fig. 14. Shear stress (rw) distributions for different inclusions arising from uniaxial compression

reverse sign and become compressive with a value of +0·83 p. For a two-dimensional compressive stress field, for instance, a combination of two compression loads perpendicular to each other applied in the plane ROW (see Fig. 9), the maximum hoop stress vv in the plane of loading remains at +0·83 p but the maximum hoop stress vv in the orthogonal direction becomes −1·167 p. These results indicate that the biaxial compression test is the state of loading most significantly affected by the specimen's moisture condition, yielding a lower measured strength than for a saturated concrete specimen loaded either uniaxially or in all three dimensions.

## Conclusions and recommendations

The effect of moisture on the mechanical properties of concrete at the time of test can be quantified by the elastic model developed in this paper. Results obtained from the model are in good general agreement with experimental observations.

For concrete subjected to uniaxial compressive loading, the maximum hoop stress associated with a fully water filled cavity is approximately 67% higher than that for an identical air filled cavity. For concrete under uniaxial tensile loading, the magnitude and distribution of stresses around a cavity are unaffected by whether

Magazine of Concrete Research, 2001, 53, No. 3

Guo and Waldron

the cavity is filled with water or air. The standard uniaxial compressive strength test is therefore affected to a much greater extent by the moisture condition of the concrete than are the direct tension and tensile splitting test methods which are theoretically entirely independent of the moisture condition. Standardisation of moisture conditions at the time of test is therefore of particular importance if reliable results are to be ob- tained from the industry standard test for characteristic compressive strength.

In practice, if the specimen is allowed to become surface dry prior to the test, the tensile splitting test has been found to yield a slightly higher value of tensile strength than that measured with the direct tension test. This is attributed to the formation of a system of self- equilibrated residual stresses arising from the differen- tial shrinkage.

Under the same external load, an element with water filled cavities will deform less than if the cavities were filled with air or vapour, the magnitude of the deforma- tion being dependent on the void ratio. This phenomen- on has the effect of increasing the static modulus of the saturated specimen over that of the dried specimen. For normal concretes, with void ratios varying from 5% to 16%, the increase in static modulus is estimated to be in the range 7–22%, which compares well with experi- mental observation.

For concrete specimens subjected to multi-dimen- sional compressive stress fields, those under biaxial loading are affected adversely by the moisture condi- tions to a greater degree than those under either uni- axial or three dimensional loading.

The mathematical model developed in this paper provides fundamental information for the computa- tional or numerical simulation of the behaviour of con- crete structures subjected to wide variations in moisture content.

The mathematical models developed in this paper are based principally on the theory of elasticity, and further development of a plastic model and the use of the finite element method are recommended. By em- ploying these more advanced theoretical and analytical approaches, the difficulties arising from irregular speci- men geometries, stress re-distribution, interaction be- tween adjacent cavities, the propagation of cracks and the connection of cracks to each other, will be resolved, yielding more accurate solutions and an improved un- derstanding of this highly complex problem.

## References
1. BESSEY G. E. and DILNOT S. The relation between strength and free water content of aerated concretes. *Magazine of Concrete Research*, 1949, **1**, No. 3, 119–122.
2. WITTMANN F. H. Interaction of hardened cement paste and water. *Journal of The American Ceramic Society*, 1973, **56**, No. 2, 409–415.
3. PIHLAJAVAARA S. E. A review of some of the main results on the ageing phenomena of concrete: effect of moisture conditions on strength, shrinkage and creep of mature concrete. *Cement and Concrete Research*, 1974, **4**, No. 5, 761–771.
4. NEVILLE A. M. *Properties of Concrete*, 3rd edn. Longman Scien- tific and Technical, 1981.
5. NEVILLE A. M. *Properties of Concrete*, 4th edn. Longman Scien- tific and Technical, 1995.
6. FELDMAN R. F. and SEREDA P. J. New model for hydrated Port- land cement and its practical implications. *Engineering Journal*, 1970, 53–59.
7. GLUCKLICK J. and KORIN U. Effect of moisture content on strength and strain energy release rate of cement mortar. *Journal of the American Ceramic Society*, 1975, **58**, Nos 11–12, 517–521.
8. POPOVICS S. Effect of curing method and final moisture condition on compressive strength of concrete. *ACI Materials Journal*, 1986, **83**, No. 4, 650–657.
9. BARTLETT F. M. and MACGREGOR J. G. Effect of moisture condi- tion on concrete core strengths. *ACI Materials Journal*, 1994, **91**, No. 3, 227–236.
10. GALLOWAY J. W., HARDING H. M. and RAITHBY K. D. Effect of moisture changes of flexural and fatigue strength of concrete. *Transport and Road Research Laboratory*, 1979, No. 864.
11. GUO J. S. *Behavior of concrete subjected to thermal load.* PhD thesis, 1997, University of Sheffield, UK.
12. LOVE A. E. H. *Mathematical theory of elasticity*, 4th edn. Cam- bridge University Press, Cambridge, 1924.
13. TIMOSHENKO S. and GOODIER J. N. *Theory of Elasticity*, 3rd edn. McGraw-Hill Book Company, Inc., 1958.
14. SAADA A. S. *Elasticity: Theory and Applications.* Pergamon Unifield Engineering Series, Pergamon Press Inc, 1974.
15. GOODIER J. N. Concentration of stress around spherical and cylindrical inclusions and flaws. *Applied Mechanics*, 1993, **55**, No. 7, 39–44.
16. BRANDT A. M. *Cement Based Composites, Materials, Mechanical Properties and Performance.* E & FN Spon, London, 1995.
17. DAVIS R. E. and TROXELL G. E. Modulus and elasticity and Poisson’s ratio for concrete and the influence of age and the other factors upon these values. *Proc. ASTM*, 1929, **29**, Part II, 678–710.

Discussion contributions on this paper should reach the editor by
21 November 2001

---

*Magazine of Concrete Research*, 2001, **53**, No. 3